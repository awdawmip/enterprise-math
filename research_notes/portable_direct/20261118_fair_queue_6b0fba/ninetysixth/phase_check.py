"""Rebuild the fixed K4 first-return law and its exact laboratory-phase observer."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha1
from itertools import permutations, product
import json
from pathlib import Path
import sys

PINS = {
    "research_tasks/RS-EULER-FIELD-RATE-JOINT-CLOSURE-20261007.md": "9a9d683d7aa44965b1354e62a44ac992f23abb8c",
    "research_notes/chatgpt_direct/20261007_EULER_VARIABLE_MEMORY_STATE_FEEDBACK.md": "bb375b97413dfee0f10ecd298e8bbfc05e51f050",
    "research_notes/chatgpt_direct/20261008_EULER_INCOMING_EDGE_MEMORY.md": "38c68bf3421ae29501f5e718856543c2d61ce5d7",
    "research_notes/chatgpt_direct/20261008_EULER_NONBACKTRACKING_INCOMING_MEMORY.md": "abfdd09387308ace72d7721f2e5e3c3728ea7060",
    "research_notes/chatgpt_direct/20261008_EULER_CHANGING_FIELD_TEMPORAL_GLUE.md": "58f8e50fb50ad24e0bc8b73b1c6640c1f8723d2c",
    "src/enterprise_math/euler_fcc_chirality.py": "6f8b147c094720c2749f620a40394c4d7b67a386",
    "src/enterprise_math/brc_weighted.py": "3f205696709e847909958a153f8fe10d3f6b70f0",
    "src/enterprise_math/brc_logarithm.py": "4732e5fc381ce613d240c4381ccbef03c27a69c7",
    "src/enterprise_math/exact_arithmetic.py": "35ea95b0916494b83a92386e3e313928362dd79e",
}
ZERO, ONE, OMEGA, BAR = (0, 0), (1, 0), (0, 1), (-1, -1)
PHASE = (ONE, OMEGA, BAR)
EDGES = (0, 0, 0, 1, 1, 0)
PORTS = (1, 2, 3)
ATOMS = tuple(product(range(3), (1, -1), PORTS))


def scale(q, v):
    return q * v[0], q * v[1]


def add(v, w):
    return v[0] + w[0], v[1] + w[1]


def mul(v, w):
    a, b = v
    c, d = w
    return a * c - b * d, a * d + b * c - b * d


def dot(v, w):
    out = ZERO
    for x, y in zip(v, w, strict=True):
        out = add(out, mul(x, y))
    return out


def fmt(x):
    if isinstance(x, (list, tuple)):
        return [fmt(v) for v in x]
    return str(x)


def load_repo(repo):
    for relative, expected in PINS.items():
        data = (repo / relative).read_bytes()
        assert sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == expected
    sys.path.insert(0, str(repo / "src"))
    from enterprise_math import brc_weighted, euler_fcc_chirality
    return brc_weighted, euler_fcc_chirality


def enumerate_returns(b, field, counts):
    # Keep each path separate until it first returns. The dictionary only
    # combines completed paths, by exact length and final named port/parity.
    kernel = {}
    for incoming in PORTS:
        active = [(incoming, 0, 0, b.CWM_ONE)]
        stopped = defaultdict(lambda: b.CWM_ZERO)
        pending_counts = []
        for length in range(1, 15):
            following = []
            for previous, current, sign, weight in active:
                for nxt in field.VERTICES:
                    if nxt in (previous, current):
                        continue
                    h = sign ^ field.transition_bit(EDGES, current, nxt)
                    new = b.cwm_propagate(weight, b.cwm_edge(Q(1, 2)))
                    counts["transition_bit"] += 1
                    counts["cwm_propagate"] += 1
                    counts["cwm_edge"] += 1
                    if nxt == 0:
                        key = (length, current, h)
                        stopped[key] = b.cwm_recoalesce(stopped[key], new)
                        counts["cwm_recoalesce"] += 1
                    else:
                        following.append((current, nxt, h, new))
            active = following
            pending_counts.append(len(active))
            if length >= 2:
                assert sum(w.total for *_, w in active) == Q(1, 2**(length - 2))
            if length >= 3:
                assert sum(stopped[length, j, h].count for j in PORTS for h in (0, 1)) == 4
        assert pending_counts == [2] + [4] * 13
        for j, h in product(PORTS, (0, 1)):
            for length in range(3, 9):
                now, later = stopped[length, j, h], stopped[length + 6, j, h]
                assert (later.count, later.total, later.dominant) == (
                    now.count, now.total / 64, now.dominant / 64
                )
            kernel[incoming, j, h] = Q(64, 63) * sum(stopped[l, j, h].total for l in range(3, 9))
        assert sum(v for (i, j, h), v in kernel.items() if i == incoming) == 1
    return kernel


def compressed_matrix(kernel):
    kernels = []
    for parity in (0, 1):
        by_port = [(kernel[i, 1, parity], kernel[i, 2, parity] + kernel[i, 3, parity]) for i in PORTS]
        assert by_port[1] == by_port[2]
        kernels.append(by_port[:2])
    even, odd = kernels
    assert even == [(0, Q(4, 7)), (Q(1, 14), Q(2, 7))]
    assert odd == [(Q(3, 7), 0), (Q(3, 14), Q(3, 7))]
    matrix = []
    for sign_index, mode in product(range(2), range(2)):
        row = []
        for next_sign, next_mode in product(range(2), range(2)):
            mass = kernels[sign_index ^ next_sign][mode][next_mode]
            row.append(scale(mass, (OMEGA, BAR)[sign_index]))
        matrix.append(row)
    return kernels, matrix


def observers(matrix, horizon):
    rows = [[ONE] * 4]
    for _ in range(horizon):
        rows.append([dot(row, rows[-1]) for row in matrix])
    return rows


def determinant(rows):
    out = ZERO
    for perm in permutations(range(4)):
        inversions = sum(x > y for i, x in enumerate(perm) for y in perm[i + 1:])
        term = ((-1)**inversions, 0)
        for i, j in enumerate(perm):
            term = mul(term, rows[i][j])
        out = add(out, term)
    return out


def exact_phases(kernel, initial, horizon):
    # Independent 18-atom laboratory readout. This uses exact first-return
    # masses; the number of original paths at an unbounded return is infinite.
    state = dict(initial)
    values = []
    for step in range(horizon + 1):
        phase = ZERO
        for (channel, sign, incoming), mass in state.items():
            phase = add(phase, scale(mass, PHASE[channel]))
        values.append(phase)
        if step == horizon:
            break
        nxt = defaultdict(Q)
        for (channel, sign, incoming), mass in state.items():
            for j, h in product(PORTS, (0, 1)):
                prob = kernel[incoming, j, h]
                if prob:
                    nxt[(channel + sign) % 3, (-1)**h * sign, j] += mass * prob
        assert sum(nxt.values()) == sum(state.values())
        state = nxt
    return values


def project(ensemble):
    v = [ZERO] * 4
    for (channel, sign, incoming), mass in ensemble.items():
        i = 2 * (sign == -1) + (incoming != 1)
        v[i] = add(v[i], scale(mass, PHASE[channel]))
    return v


def marginal(ensemble, positions):
    res = defaultdict(Q)
    for atom, mass in ensemble.items():
        res[tuple(atom[i] for i in positions)] += mass
    return res


def main(repo):
    b, field = load_repo(repo)
    calls = Counter()
    kernel = enumerate_returns(b, field, calls)
    blocks, matrix = compressed_matrix(kernel)
    r = observers(matrix, 16)
    det = determinant(r[:4])
    assert det == (Q(81, 1372), 0)
    for n in range(len(r) - 4):
        for j in range(4):
            assert dot([(k, 0) for k in (1, 2, -12, 14, 49)], [r[n+i][j] for i in range(5)]) == ZERO
    for atom in ATOMS:
        init = {atom: Q(1)}
        assert exact_phases(kernel, init, 16) == [dot(project(init), obs) for obs in r]

    left_atoms = [(0, 1, 1), (1, 1, 2), (2, -1, 1), (0, -1, 2)]
    right_atoms = [(1, 1, 1), (0, 1, 2), (0, -1, 1), (2, -1, 2)]
    left, right = ({a: Q(1, 4) for a in world} for world in (left_atoms, right_atoms))
    assert marginal(left, (0, 1)) == marginal(right, (0, 1))
    assert marginal(left, (1, 2)) == marginal(right, (1, 2))
    zl, zr = (exact_phases(kernel, state, 4) for state in (left, right))
    gap = add(zl[3], scale(-1, zr[3]))
    assert zl[:3] == zr[:3] and gap == scale(Q(-9, 392), (1, 2))
    # First missing input port. Complex squared length in the Eisenstein basis.
    pair = [exact_phases(kernel, {(0, 1, port): 1}, 2)[-1] for port in (1, 2)]
    a, c = add(pair[0], scale(-1, pair[1]))
    assert a*a - a*c + c*c == Q(27, 196)
    return {
        "arithmetic": "exact rational pair [a,b] denotes a+b*omega",
        "source_git_blobs": PINS,
        "input_field_in_01_02_03_12_13_23_order": list(EDGES),
        "source_package_status": "public-source reconstruction; no replay of the fingerprinted original attachment",
        "source_calls_in_finite_returns": dict(sorted(calls.items())),
        "literal_enumeration": {"starting_ports": 3, "terminal_lengths": [3,14],
                                "stopped_paths": 144, "positive_weight_paths_per_port_and_length": 4,
                                "period_six_comparisons_including_zeros": 108},
        "kernel_arrival_rows_by_named_ingress": {str(h): fmt([[kernel[i,j,h] for j in PORTS] for i in PORTS]) for h in (0,1)},
        "even_odd_class_blocks": fmt(blocks),
        "observability_rows_0_to_3": fmt(r[:4]),
        "determinant": fmt(det),
        "recurrence_coefficients_low_to_high": [1,2,-12,14,49],
        "source_atoms_by_read_times_verified": [len(ATOMS),17],
        "matrix_recurrence_scalar_identities_checked": (len(r)-4)*4,
        "two_return_conditional_uncertainty": {"endpoint_gap_squared":"27/196","minimax_squared":"27/784"},
        "positive_witness": {"worlds_left":left_atoms, "worlds_right":right_atoms,"weight_per_world":"1/4",
                             "equal_marginals":[["channel","sign"],["sign","named_incoming"]],
                             "phase_left":fmt(zl),"phase_right":fmt(zr),"first_difference_time":3,"difference":fmt(gap)},
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, default=Path("/workspace/enterprise-math"))
    print(json.dumps(main(p.parse_args().repo.resolve()), indent=2, sort_keys=True))
