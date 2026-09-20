from dataclasses import replace
from fractions import Fraction as F
from itertools import product
import random
import pytest
from sympy import Matrix as SM, ZZ
from sympy.matrices.normalforms import smith_normal_form

from enterprise_math.brc_transport import Affine, eye, matrix, mm, inv, sm
from enterprise_math.brc_control_port import ControlPacket, certify_control_partition, refine_control_partition
from enterprise_math.brc_control_mass import quotient_control_mass_matrix
from enterprise_math.heartbeat_switching_carry import linear_carry_spread, split_feedback_packet, _valuation
from enterprise_math.heartbeat_lattice_search import find_phase_lattice, find_common_lattice
import enterprise_math.heartbeat_constrained_carry as h


def diagonal(xs):
    return matrix(tuple(tuple(x if i == j else 0 for j in range(6)) for i, x in enumerate(xs)))


def rotation(p):
    return matrix(tuple(tuple((p if i == 0 else 1) if j == (i-1) % 6 else 0 for j in range(6)) for i in range(6)))


def one_port(actions):
    return h.ControlGraph(1, tuple(h.LinearEdge(0, 0, a) for a in actions))


def smith_width(a, p):
    s = smith_normal_form(SM(a), domain=ZZ)
    ds = [_valuation(int(s[i, i]), p) for i in range(6)]
    return max(ds)-min(ds)


def transient_graph(p=2, mixed=True):
    d = diagonal((p**6, 1, 1, 1, 1, 1))
    t = matrix([[int(i == j) + int(j == i+1) for j in range(6)] for i in range(6)])
    a = mm(mm(t, d), inv(t)) if mixed else d
    return h.ControlGraph(2, (h.LinearEdge(0, 0, eye(6)), h.LinearEdge(1, 1, eye(6)),
                              h.LinearEdge(0, 1, eye(6)), h.LinearEdge(0, 1, a)))


def test_one_way_inclusions_have_real_strict_slack():
    for p in (2, 3, 5):
        g = transient_graph(p)
        r = h.find_graph_lattices(g, p, depth_budget=1)
        assert r.status == 'FIXED_LATTICES' and r.rounds == 2
        assert h.verify_graph_lattice_result(g, r)
        assert r.certificate.volume_potential == (0, -5)
        assert [e[3] for e in r.certificate.edge_slacks] == [0, 5, 5, 0]
        assert r.certificate.all_path_spread_bound == 6
        assert smith_width(g.edges[3].action, p) == 6
        # Arbitrary repetitions of the SAME matrix are illegal in this graph.
        with pytest.raises(ValueError, match='illegal edge succession'):
            h.replay_graph_word(g, 0, (3, 3))


def test_transient_budget_escape_is_not_unboundedness():
    g = transient_graph()
    r = h.find_graph_lattices(g, 2, depth_budget=0)
    assert r.status == 'ESCAPING_PATH' and h.verify_graph_lattice_result(g, r)
    assert h.find_graph_lattices(g, 2, depth_budget=1).status == 'FIXED_LATTICES'
    r = h.find_graph_lattices(g, 2, depth_budget=1, max_rounds=0)
    assert r.status == 'SEARCH_LIMIT'
    with pytest.raises(ValueError):
        h.verify_graph_lattice_result(g, r)


def test_rotation_bound_is_sharp_one_not_old_two():
    for p in (2, 3, 5):
        a = rotation(p)
        old = find_phase_lattice((a,), p, depth_budget=1)
        assert old.all_word_spread_bound == 2
        g = one_port((a,))
        r = h.classify_monomial_carry(g, p)
        assert r.status == 'BOUNDED_EXACT' and r.exact_spread_bound == 1
        assert h.verify_monomial_carry_result(g, r)
        gr = h.find_graph_lattices(g, p, depth_budget=1)
        assert h.verify_graph_lattice_result(g, gr)
        assert all(s == 0 for _u, _v, _i, s in gr.certificate.edge_slacks)


def test_nonperiodic_forward_backward_pauses_still_width_one():
    for p in (2, 3, 5):
        a = rotation(p)
        g = one_port((a, mm(a, a), sm(p, inv(a)), eye(6)))
        r = h.classify_monomial_carry(g, p)
        assert r.status == 'BOUNDED_EXACT' and r.exact_spread_bound == 1
        assert h.verify_monomial_carry_result(g, r)
        for word in product(range(4), repeat=4):
            _, b = h.replay_graph_word(g, 0, word)
            assert smith_width(b, p) <= 1


def test_same_rotation_different_radix_can_accumulate():
    g = one_port((rotation(2), rotation(3)))
    for p in (2, 3):
        r = h.classify_monomial_carry(g, p)
        assert r.status == 'UNBOUNDED_CYCLE' and h.verify_monomial_carry_result(g, r)
        c, pre = r.positive_cycle, r.cycle_prefix
        for n in (1, 2, 7):
            _, a = h.replay_graph_word(g, pre.source, pre.word+c.word*n)
            assert smith_width(a, p) >= pre.debt+n*c.debt
    # A human-readable loop: one radix-2 step, then five radix-3 steps.
    _, c = h.replay_graph_word(g, 0, (0, 1, 1, 1, 1, 1))
    for n in (1, 3, 8):
        a = matrix([[int(x) for x in row] for row in (SM(c)**n).tolist()])
        assert smith_width(a, 2) == n and smith_width(a, 3) == n


def test_existing_feedback_has_initialization_dependent_sharp_bound():
    packet, _, _ = split_feedback_packet()
    g = h.packet_control_graph(packet)
    all_starts = h.classify_monomial_carry(g, 2)
    center = h.classify_monomial_carry(g, 2, initial_states=(1,))
    assert all_starts.exact_spread_bound == 2
    assert center.exact_spread_bound == 1
    assert h.verify_monomial_carry_result(g, all_starts)
    assert h.verify_monomial_carry_result(g, center)


def test_control_mass_one_does_not_allow_erasing_future_effects():
    g0 = transient_graph()
    identity = Affine.identity(6)
    changed = Affine(g0.edges[3].action, (1, -2, 3, -4, 5, -6))
    packet = ControlPacket.from_edges(2, 0, 1, (
        (0, 0, F(1, 4), identity, 2),
        (0, 1, F(1, 4), identity, 1),
        (0, 1, F(1, 8), changed, 2),
        (1, 1, F(1), identity, 1)))
    assert quotient_control_mass_matrix(packet, (0, 0)) == ((F(1),),)
    with pytest.raises(ValueError):
        certify_control_partition(packet, (0, 0))
    assert refine_control_partition((packet,), (0, 0)) == (0, 1)
    g = h.packet_control_graph(packet)
    r = h.find_graph_lattices(g, 2, depth_budget=1)
    assert r.certificate.all_path_spread_bound == 6
    serial = ControlPacket.identity(2)
    for n in range(1, 13):
        serial = serial.then(packet.at(serial.end))
        out = serial.evaluate(0, (0,)*6)
        assert sum(hist.total_mass for hist in out.values()) == 1
        assert sum(hist.total_mass for (s, _x), hist in out.items() if s == 0) == F(1, 2)**n
        for _s, _t, hist in serial.blocks:
            assert all(linear_carry_spread(a.a, 2) <= 6 for _w, a, _c in hist.entries)
    collapsed = one_port(tuple(e.action for e in g.edges))
    for n in (1, 2, 5):
        assert linear_carry_spread(matrix([[int(x) for x in row] for row in (SM(changed.a)**n).tolist()]), 2) == 6*n
    assert collapsed.state_count == 1


def test_transient_monomial_bound_exactly_six():
    g = transient_graph(mixed=False)
    r = h.classify_monomial_carry(g, 2)
    assert r.status == 'BOUNDED_EXACT' and r.exact_spread_bound == 6
    assert h.verify_monomial_carry_result(g, r)


def test_pair_transport_is_not_optional():
    a = rotation(2)
    # Wrong fixed-axis accounting would call the one-edge loop imbalanced.
    assert _valuation(a[0][5], 2)-_valuation(a[1][0], 2) == 1
    r = h.classify_monomial_carry(one_port((a,)), 2)
    assert r.status == 'BOUNDED_EXACT'
    assert matrix([[int(x) for x in row] for row in (SM(a)**6).tolist()]) == sm(2, eye(6))


def test_unreachable_bad_cycles_do_not_pollute_initial_scope():
    bad = diagonal((2, 1, 1, 1, 1, 1))
    g = h.ControlGraph(2, (h.LinearEdge(0, 0, eye(6)), h.LinearEdge(1, 1, bad)))
    assert h.classify_monomial_carry(g, 2).status == 'UNBOUNDED_CYCLE'
    r = h.classify_monomial_carry(g, 2, initial_states=(0,))
    assert r.exact_spread_bound == 0 and h.verify_monomial_carry_result(g, r)


def test_random_monomial_gauges_and_independent_smith():
    rng = random.Random(2026092001)
    for sample in range(12):
        p = (2, 3, 5)[sample % 3]
        potentials = [[rng.randrange(-2, 3) for _ in range(6)] for _ in range(3)]
        edges = []
        for s in range(3):
            for target in ((s+1) % 3, s):
                perm = list(range(6)); rng.shuffle(perm)
                a = [[0]*6 for _ in range(6)]
                for i in range(6):
                    exponent = 4+potentials[target][perm[i]]-potentials[s][i]
                    a[perm[i]][i] = p**exponent * (-1 if rng.randrange(2) else 1)
                edges.append(h.LinearEdge(s, target, matrix(a)))
        g = h.ControlGraph(3, tuple(edges))
        r = h.classify_monomial_carry(g, p)
        assert r.status == 'BOUNDED_EXACT' and h.verify_monomial_carry_result(g, r)
        _, best = h.replay_graph_word(g, r.attaining_path.source, r.attaining_path.word)
        assert smith_width(best, p) == r.exact_spread_bound
        for _ in range(10):
            source = rng.randrange(3); s = source; word = []
            for _ in range(5):
                k = rng.choice([i for i, e in enumerate(edges) if e.source == s])
                word.append(k); s = edges[k].target
            _, a = h.replay_graph_word(g, source, word)
            assert smith_width(a, p) <= r.exact_spread_bound


def test_random_general_mixed_lattice_gauges():
    rng = random.Random(2026092002)
    for sample in range(9):
        p = (2, 3, 5)[sample % 3]
        bs = []
        for s in range(3):
            v = [-2, -1, 0, 0, 0, 0]; rng.shuffle(v)
            bs.append(diagonal([F(p)**d for d in v]))
        edges = []
        for s in range(3):
            for t in ((s+1) % 3, s):
                u = eye(6)
                for _ in range(4):
                    i, j = rng.sample(range(6), 2)
                    v = [list(row) for row in eye(6)]; v[i][j] = rng.choice((-1, 1))
                    u = mm(matrix(v), u)
                a = sm(p**2, mm(mm(bs[t], u), inv(bs[s])))
                edges.append(h.LinearEdge(s, t, a))
        g = h.ControlGraph(3, tuple(edges))
        r = h.find_graph_lattices(g, p, depth_budget=2)
        assert r.status == 'FIXED_LATTICES' and h.verify_graph_lattice_result(g, r)
        assert all(slack == 0 for _u, _v, _i, slack in r.certificate.edge_slacks)
        assert r.certificate.all_path_spread_bound <= 4
        for start in range(3):
            state, word = start, []
            for _ in range(4):
                i = rng.choice([i for i, e in enumerate(edges) if e.source == state])
                word.append(i); state = edges[i].target
            _, a = h.replay_graph_word(g, start, word)
            assert smith_width(a, p) <= r.certificate.all_path_spread_bound


def test_random_unbounded_cycles_have_actual_legal_witnesses():
    rng = random.Random(2026092003)
    for _ in range(15):
        actions = []
        for _ in range(2):
            perm = list(range(6)); rng.shuffle(perm)
            a = [[0]*6 for _ in range(6)]
            for i in range(6): a[perm[i]][i] = 2**rng.randrange(4)
            actions.append(matrix(a))
        g = one_port(actions)
        r = h.classify_monomial_carry(g, 2)
        assert h.verify_monomial_carry_result(g, r)
        if r.status == 'UNBOUNDED_CYCLE':
            pre, c = r.cycle_prefix, r.positive_cycle
            _, a = h.replay_graph_word(g, pre.source, pre.word+c.word*3)
            assert smith_width(a, 2) >= pre.debt+3*c.debt


def test_finite_dag_monomial_sharpness_by_exhaustive_paths():
    rng = random.Random(2026092004)
    for _ in range(10):
        edges = []
        for s in range(3):
            for t in range(s+1, 4):
                perm = list(range(6)); rng.shuffle(perm)
                a = [[0]*6 for _ in range(6)]
                for i in range(6): a[perm[i]][i] = 2**rng.randrange(4)
                edges.append(h.LinearEdge(s, t, matrix(a)))
        g = h.ControlGraph(4, tuple(edges))
        r = h.classify_monomial_carry(g, 2)
        stack = [(s, eye(6)) for s in range(4)]; best = 0
        while stack:
            s, a = stack.pop(); best = max(best, smith_width(a, 2))
            for e in edges:
                if e.source == s: stack.append((e.target, mm(e.action, a)))
        assert r.exact_spread_bound == best and h.verify_monomial_carry_result(g, r)


def test_terminal_verifiers_do_not_replay_search(monkeypatch):
    g = transient_graph()
    r = h.find_graph_lattices(g, 2, depth_budget=1)
    mg = one_port((rotation(2),))
    mr = h.classify_monomial_carry(mg, 2)
    def forbidden(*_a, **_k): raise AssertionError('search called during verification')
    monkeypatch.setattr(h, '_hnf_basis', forbidden)
    monkeypatch.setattr(h, 'classify_monomial_carry', forbidden)
    assert h.verify_graph_lattice_result(g, r)
    assert h.verify_monomial_carry_result(mg, mr)


def test_tampering_and_bad_inputs_rejected():
    g = one_port((rotation(2),))
    r = h.classify_monomial_carry(g, 2)
    bads = [replace(r, exact_spread_bound=0), replace(r, source_digest='0'*64),
            replace(r, potentials=(0,)*30), replace(r, attaining_path=replace(r.attaining_path, debt=7))]
    for bad in bads:
        with pytest.raises((ValueError, TypeError)):
            h.verify_monomial_carry_result(g, bad)
    mixed = transient_graph()
    with pytest.raises(ValueError): h.classify_monomial_carry(mixed, 2)
    with pytest.raises(ValueError): h.classify_monomial_carry(g, 4)
    with pytest.raises(ValueError): h.classify_monomial_carry(g, 2, initial_states=())
    with pytest.raises(ValueError): h.LinearEdge(0, 0, sm(F(1, 2), eye(6)))
    with pytest.raises(ValueError): h.LinearEdge(0, 0, diagonal((0, 1, 1, 1, 1, 1)))
    with pytest.raises(ValueError): h.ControlGraph(True, ())
    lr = h.find_graph_lattices(mixed, 2, depth_budget=0)
    with pytest.raises(ValueError):
        h.verify_graph_lattice_result(mixed, replace(lr, escape=replace(lr.escape, vector=(F(1),)*6)))
    packet, _, _ = split_feedback_packet()
    pg = h.packet_control_graph(packet); pr = h.classify_monomial_carry(pg, 2)
    with pytest.raises(ValueError):
        h.verify_monomial_carry_result(h.packet_control_graph(packet.at(1)), pr)


def test_empty_graph_and_integer_units():
    g = h.ControlGraph(2, ())
    r = h.find_graph_lattices(g, 2, depth_budget=0)
    assert r.certificate.all_path_spread_bound == 0 and h.verify_graph_lattice_result(g, r)
    mr = h.classify_monomial_carry(g, 2)
    assert mr.exact_spread_bound == 0 and h.verify_monomial_carry_result(g, mr)
    a = diagonal((-3, 5, 7, 9, 11, 13))
    mr = h.classify_monomial_carry(one_port((a,)), 2)
    assert mr.exact_spread_bound == 0


def test_existing_t12_closure_implementation_on_transported_axis_pairs():
    import importlib.util
    from pathlib import Path
    path = Path(__file__).resolve().parents[1]/'research_notes/heartbeat_constrained_carry_20260920_AD0416/t12_closure_excerpt.py'
    spec = importlib.util.spec_from_file_location('t12_closure_reuse', path)
    t12 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(t12)
    packet, _, _ = split_feedback_packet()
    for graph in (one_port((rotation(2),)), transient_graph(mixed=False), h.packet_control_graph(packet)):
        perms, vals = h._monomial_data(graph, 2)
        size = 30*graph.state_count
        adjacency = [[None]*size for _ in range(size)]
        for u, v, weight, _edge in h._pair_edges(graph, perms, vals):
            adjacency[u][v] = t12.envelope(adjacency[u][v], weight, 'max')
        closure = t12.floyd_warshall_star(adjacency, 'max')
        assert all(closure[i][i] == 0 for i in range(size))
        assert max(v for row in closure for v in row if v is not None) == h.classify_monomial_carry(graph, 2).exact_spread_bound


def test_finite_controller_linear_witness_and_single_schedule_are_distinct():
    from enterprise_math.heartbeat_switching_carry import growing_block_state
    u = diagonal((2, 2, 2, 1, 1, 1))
    v = diagonal((1, 1, 1, 2, 2, 2))
    graph = one_port((u, v))
    result = h.classify_monomial_carry(graph, 2)
    assert result.status == 'UNBOUNDED_CYCLE' and h.verify_monomial_carry_result(graph, result)
    # The selected nonregular schedule U V U^2 V^2 ... has sqrt-scale bursts;
    # that is not the worst-case envelope of all words in {U,V}*.
    for k in (1, 2, 5, 10, 20):
        n = k*k
        state = growing_block_state(n)
        assert state.debt == k
        _, worst = h.replay_graph_word(graph, 0, (0,)*n)
        assert linear_carry_spread(worst, 2) == n
