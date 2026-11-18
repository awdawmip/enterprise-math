"""Recompute the U27F-03 five-stop recovery comparison from public JSON.

Optional authorized source archive replays only the five-stage geometry and
positive branches used here. No network, native extension or external packages.
"""
import argparse
import copy
from fractions import Fraction
import gzip
import hashlib
import importlib
from itertools import combinations, product
import json
from pathlib import Path
import sys
import tempfile
import zipfile

AB, AD, BC, CD = (0, 1), (0, 3), (1, 2), (2, 3)
PAIRS = list(combinations(range(4), 2))
IDS = {'0', '1', '2', '3'}
ARCHIVE = 'a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7'
FIXTURES = {
    'carry_Q': 'acd915da997e0703ae72395e805126b29d841d47a68a435e75af379e40f76708',
    'interrupted_after_carry': '31012bcbfa2cfb0bdfbbfa073616ac9244130e429a6f166f927968d2ad68847e',
}


def step(cell, port):
    assert 0 <= port < 12 and len(cell) == 6
    end = list(cell)
    end[port // 2] += 1 if port % 2 == 0 else -1
    return end


def delta(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


def port_to(x, y):
    return next(i for i in range(12) if step(x, i) == list(y))


def partitions(edges):
    groups = [{v} for v in range(4)]
    for u, v in edges:
        a, b = (next(i for i in groups if vtx in i) for vtx in (u, v))
        if a != b:
            a.update(b)
            groups.remove(b)
    return sorted(sorted(g) for g in groups)


def geometric_table(s):
    """Exact on this prefix family: at most one real letter per edge and side."""
    cells = s['body_cells']
    groups = {}
    for rec in s['bound'].values():
        edge, side = tuple(rec['edge']), rec['side']
        assert edge in PAIRS and side in (0, 1)
        slots = groups.setdefault(edge, [(), ()])
        assert not slots[side] and rec['cell'] == cells[edge[side]]
        slots[side] = (rec['port'],)
    table = {}
    for edge, words in groups.items():
        ends = [step(cells[v], w[0]) if w else cells[v] for v, w in zip(edge, words)]
        if ends[0] == ends[1]:
            table[edge] = tuple(words)
    return table


def view(s):
    cells = s['body_cells']
    assert len(cells) == len({tuple(i) for i in cells}) == 4
    groups = [set(s[k]) for k in ('free', 'held', 'bound')]
    assert sum(map(len, groups)) == 4 and set.union(*groups) == IDS
    assert set(s['modes']) == {str(AB), str(AD)} | ({str(BC)} if '3' in s['bound'] else set())
    assert all(len(p) == 6 for p in [*cells, *s['free'].values(), *s['held'].values()])
    assert all(tuple(r['edge']) != CD for r in s['bound'].values())
    edges = sorted(geometric_table(s))
    return {'edges': edges, 'components': partitions(edges)}


def load_inputs(fixtures):
    data = {}
    for key, digest in FIXTURES.items():
        blob = (fixtures / (key + '.json')).read_bytes()
        assert hashlib.sha256(blob).hexdigest() == digest
        data[key] = json.loads(blob)['data']
    return data


def inject(item):
    """New injection from the public source event, used only for the five Q stages."""
    assert set(item['eligible']) == {str(CD)}
    side, token, pos = item['eligible'][str(CD)]
    stop = copy.deepcopy(item['frame'])
    rec = stop['bound'].pop(str(token))
    assert list(CD) == rec['edge'] and side == rec['side'] and pos == rec['cell']
    assert str(token) not in stop['free'] and str(token) not in stop['held']
    stop['free'][str(token)] = pos
    stop['modes'] = {k: v for k, v in item['modes'].items() if k != str(CD)}
    stop.update(kind='INTERRUPTED_BY_FINAL_RELEASE', lost_edge=list(CD),
                released_token=token, released_at=pos, pending_reference=item['reference'],
                automatic_cached_commit_permitted=False)
    return stop


def resume(stop, route):
    """Two policies acting only on the real IDs; no successor-install operation.

    Supported observations are the five Q grow stages and their transverse
    equivalents. A stale reference authenticates the former CD, never a record.
    """
    assert route in ('forward', 'reverse')
    assert stop['automatic_cached_commit_permitted'] is False and tuple(stop['lost_edge']) == CD
    assert stop['released_token'] == 3 and stop['released_at'] == stop['free']['3'] == stop['body_cells'][2]
    assert str(CD) not in stop['modes'] and CD in {tuple(v[:2]) for v in stop['pending_reference']['paths']['links']}
    s = {k: copy.deepcopy(stop[k]) for k in ('body_cells', 'free', 'held', 'bound', 'modes')}
    cells = s['body_cells']
    b = step(s['bound']['0']['cell'], s['bound']['0']['port'])
    assert s['bound']['0']['edge'] == list(AB) and s['bound']['0']['side'] == 0
    grow_label = stop.get('label')
    if grow_label is None:
        # The first FREE_NATIVE_HOP forgets future direction. Reversing it uses
        # the witnessed courier location; only forward completion needs a command.
        if route == 'forward':
            raise ValueError('missing grow command at the free-hop stop')
        assert cells[1] == b and s['free'].get('2') == b
        p, bp = None, None
    else:
        kind, actor, p, grow = grow_label
        assert (kind, actor, grow) == ('body', 1, True) and 4 <= p <= 11
        bp = step(b, p)
        assert cells[1] in (b, bp)
    assert cells[0] == s['bound']['1']['cell'] and cells[3] == step(cells[0], 2)
    assert s['bound']['1']['edge'] == list(AD) and s['bound']['1']['port'] == 2
    assert cells[2] == step(b, 2) and set(s['modes'].values()) == {'A'}
    role2 = next(g for g in ('bound','free','held') if '2' in s[g])
    if role2 == 'bound':
        assert s['bound']['2'] == {'edge': list(AB), 'side': 1, 'cell': bp, 'port': p^1}
        assert cells[1] == bp
    else:
        assert s[role2]['2'] == cells[1] and (role2 != 'free' or cells[1] == b)
    trace = []
    def record(action):
        trace.append({'action': action, **copy.deepcopy(s), **view(s)})
    record('STOP')
    def relocate(role, token, dest):
        src = s[role][token]
        assert delta(src, dest) == 1
        s[role][token] = list(dest)
    if route == 'forward':
        if '2' in s['free']:
            s['held']['2'] = s['free'].pop('2')
            record('reserve_2')
        if cells[1] == b:
            assert s['held']['2'] == b
            relocate('held', '2', bp)
            cells[1] = bp.copy()
            record('carry_B_and_2_forward')
        if '2' in s['held']:
            assert s['held']['2'] == bp
            s['bound']['2'] = {'edge': list(AB), 'side': 1, 'cell': s['held'].pop('2'), 'port': p^1}
            record('bind_2_to_AB')
        # U26 coordinate courier, two explicit native hops C -> B_old -> A.
        for dest in (b, cells[0]):
            relocate('free', '3', dest)
            record('courier_3')
    else:
        if '2' in s['bound']:
            rec = s['bound'].pop('2')
            assert rec['port'] == p^1 and rec['cell'] == bp
            s['held']['2'] = rec['cell']
            record('detach_2_from_AB')
        if cells[1] == bp:
            assert '2' in s['held']
            relocate('held', '2', b)
            cells[1] = b.copy()
            record('carry_B_and_2_back')
        if '2' in s['held']:
            s['free']['2'] = s['held'].pop('2')
            record('unreserve_2')
        assert s['free']['3'] == cells[2] and cells[1] == b
        capture_port = port_to(cells[2], cells[1])
        s['held']['3'] = s['free'].pop('3')
        record('reserve_3_at_C')
        s['bound']['3'] = {'edge': list(BC), 'side': 1, 'cell': s['held'].pop('3'), 'port': capture_port}
        s['modes'][str(BC)] = 'D'
        record('fresh_birth_BC_side1')
        relocate('free', '2', cells[0])
        record('courier_2')
    assert not s['held'] and all(q == cells[0] for q in s['free'].values())
    assert len(s['bound']) == sum(len(w) for words in geometric_table(s).values() for w in words)
    record('STABLE')
    return trace


def tree_budget(cells):
    allowed = [e for e in PAIRS if e != CD]
    costs = [sum(delta(cells[i],cells[j]) for i,j in tree)
             for tree in combinations(allowed, 3) if len(partitions(tree)) == 1]
    return min(costs)


def stage_summary(trace):
    return {'actions_after_stop': [f['action'] for f in trace[1:]],
            'component_counts': [len(f['components']) for f in trace],
            'final_free_ids': sorted(trace[-1]['free']),
            'final_edges': trace[-1]['edges']}


def authority(stop, p):
    out = copy.deepcopy(stop)
    expected = ['body', 1, p, True]
    assert out.get('label', expected) == expected
    out.setdefault('label', expected)
    return out


def public(fixtures):
    d = load_inputs(fixtures)
    records = []
    for j, item in enumerate(d['carry_Q'], 1):
        stop = inject(item)
        if j == 3:
            assert stop == d['interrupted_after_carry']
            stop = d['interrupted_after_carry']
        if j == 1:
            try:
                resume(stop, 'forward')
            except ValueError as e:
                assert 'missing grow' in str(e)
            else:
                raise AssertionError('inferred a missing source label')
            assert resume(stop,'reverse') == resume(authority(stop,4),'reverse')
        records.append({'stage': j, 'kind': item['frame']['kind'],
                        'routes': {r: resume(authority(stop, 4), r) for r in ('forward', 'reverse')}})
    bounds = []
    for p in range(4, 12):
        cells = copy.deepcopy(d['carry_Q'][0]['frame']['body_cells'])
        assert tree_budget(cells) == 3
        cells[1] = step(cells[1], p)
        near = [e for e in PAIRS if delta(cells[e[0]],cells[e[1]]) == 1]
        assert near == [AD,CD] and tree_budget(cells) == 5
        bounds.append({'port': p, 'minimum_records_without_CD': 5})
    shells = {}
    square = d['carry_Q'][0]['frame']['body_cells']
    for v in product(range(-4,5),repeat=4):
        radius = sum(map(abs,v))
        if radius > 4:
            continue
        cells = copy.deepcopy(square)
        cells[1][2:] = v
        cycle_cost = sum(delta(cells[i],cells[j]) for i,j in (AB,AD,BC))
        assert cycle_cost == 3+2*radius
        assert tree_budget(cells) == 2+radius+min(2,1+radius)
        shells[radius] = shells.get(radius,0) + 1
    stats = {'abstract_MST_shells_checked': shells, 'task': 'RS-CELL-U27F-03-INTERRUPTED-RECOVERY-20261012',
             'input_sha256': FIXTURES, 'budget_by_transverse_port': bounds,
             'five_stops': [{'stage': x['stage'], 'kind': x['kind'],
                             'routes': {k: stage_summary(v) for k,v in x['routes'].items()}} for x in records]}
    return stats, records


def rehydrate(h, endpoint):
    tab = geometric_table(endpoint)
    cells = tuple(tuple(x) for x in endpoint['body_cells'])
    paths = h.m.make(cells, tab)
    geom = h.z.state(paths,{e: endpoint['modes'][str(e)] for e in tab})
    ledger = object.__new__(h.v.Ledger)
    ledger.s, ledger.B, ledger.ids, ledger.log = geom, 4, frozenset(range(4)), []
    ledger.tokens = {e: [[], []] for e in tab}
    for k, rec in endpoint['bound'].items():
        ledger.tokens[tuple(rec['edge'])][rec['side']].append(int(k))
    ledger.free = {int(k): tuple(v) for k,v in endpoint['free'].items()}
    assert jsonable(h,ledger.validate(stable=True)) == endpoint['bound']
    assert h.c.connected(paths) == (len(endpoint['components']) == 1)


def jsonable(h, x):
    return json.loads(json.dumps(h.v.encode(x)))


def source(path, fixtures):
    assert hashlib.sha256(path.read_bytes()).hexdigest() == ARCHIVE
    with tempfile.TemporaryDirectory() as td, zipfile.ZipFile(path) as zf:
        assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in zf.namelist())
        zf.extractall(td)
        pkg = Path(td)/'em_u27_followup'
        baseline = pkg/'baseline'/'cell_u27'
        for k,v in FIXTURES.items():
            assert json.loads((pkg/'fixtures'/(k+'.json')).read_bytes()) == json.loads((fixtures/(k+'.json')).read_bytes())
        sys.path.insert(0, str(baseline))
        h = importlib.import_module('work_exposure')
        budget = h.v.Capped(4,Fraction(1,16))
        counts = dict(source_stops=0, completed_ledgers=0, positive_birth_tests=0, blocked_birth_tests=0)
        first_stops, forward_positions = set(), set()
        for p in range(4,12):
            ledger = h.v.Ledger(h.f.root_state(), 4)
            prep = h.ONE
            for label in [('mode', BC), ('contact', BC, 0), ('mode', CD)]:
                y, w = h.v.accepted(budget, ledger.s, label)
                prep = h.r.serial(prep, w)
                ledger.commit(label,y)
            old = ledger.s
            label = ('body',1,p,True)
            y,w = h.v.accepted(budget,old,label)
            assert (prep.total, w.total) == (Fraction(1,802816),Fraction(1,18816))
            n = len(ledger.log)
            ledger.commit(label,y)
            frames = list(h.references(old,y,ledger.log[n:]))
            assert len(frames)==5
            if p == 4:
                assert jsonable(h,frames) == load_inputs(fixtures)['carry_Q']
            mass = h.r.serial(prep,w)
            for j,item in enumerate(frames):
                only = h.freeze_loss(item, CD)
                stop = jsonable(h, only)
                assert inject(jsonable(h,item)) == stop
                if j == 0:
                    first_stops.add(json.dumps(stop,sort_keys=True))
                safe, loss = h.stage_law(item['eligible'],Fraction(1,256))
                assert loss[CD].total == Fraction(1,12544)
                hit = h.r.serial(mass,loss[CD])
                assert hit.total == prep.total*w.total*(1-loss[CD].total)**j*loss[CD].total and hit.live
                mass = h.r.serial(mass,safe)
                counts['source_stops'] += 1
                for route in ('forward','reverse'):
                    trace = resume(authority(stop,p),route)
                    endpoint = trace[-1]
                    rehydrate(h,endpoint)
                    counts['completed_ledgers'] += 1
                    candidate = next((f for f in trace if f['action']=='reserve_3_at_C'),endpoint)
                    paths = h.m.make(tuple(tuple(x) for x in candidate['body_cells']),geometric_table(candidate))
                    geom = h.z.state(paths,{e: candidate['modes'][str(e)] for e in paths.table()})
                    direct = h.c.toggle(paths,BC,1)
                    if route == 'forward':
                        if j == 0:
                            forward_positions.add(tuple(endpoint['body_cells'][1]))
                        assert direct is None and h.K.proposal(geom,('contact',BC,1)) is None
                        counts['blocked_birth_tests'] += 1
                    else:
                        assert direct == h.m.make(tuple(tuple(x) for x in endpoint['body_cells']),geometric_table(endpoint))
                        nextstate,weight = h.v.accepted(budget,geom,('contact',BC,1))
                        assert nextstate.paths == direct and weight.total == Fraction(1,2352)
                        counts['positive_birth_tests'] += 1
        assert len(first_stops) == 1 and len(forward_positions) == 8
        return dict(distinct_first_stop_snapshots=1, distinct_forward_B_positions=8,
                    archive_sha256=ARCHIVE, loss_delta='1/256', prep_weight='1/802816',
                    grow_weight='1/18816', stage_hazard='1/12544', BC_label_branch='1/2352', **counts)


def save_traces(path, records):
    """Deduplicate exact state vectors while retaining every step and action."""
    states, lookup, runs = [], {}, []
    for row in records:
        routes = {}
        for key, trace in row['routes'].items():
            sequence = []
            for frame in trace:
                state = {k:v for k,v in frame.items() if k!='action'}
                canonical = json.dumps(state,sort_keys=True,separators=(',',':'))
                if canonical not in lookup:
                    lookup[canonical] = len(states)
                    states.append(state)
                sequence.append([frame['action'],lookup[canonical]])
            assert [{**states[index], 'action': action} for action,index in sequence] == trace
            routes[key] = sequence
        runs.append({'stage':row['stage'], 'kind':row['kind'], 'routes':routes})
    packed = {'schema':'U27F03_RECOVERY_PATHS_V1',
              'expansion':'Each [action,k] gives that action and the full state states[k]. All indices are zero-based.',
              'states': states,'runs': runs}
    data = (json.dumps(packed,sort_keys=True,separators=(',',':'))+chr(10)).encode()
    path.write_bytes(gzip.compress(data,mtime=0) if path.suffix=='.gz' else data)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--fixtures',type=Path)
    ap.add_argument('--archive',type=Path)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--traces',type=Path)
    a=ap.parse_args()
    candidates = [Path.cwd(), *Path(__file__).resolve().parents]
    fixtures = a.fixtures or next((d/'research_inputs/U27F_20261012/fixtures' for d in candidates
                                   if (d/'research_inputs/U27F_20261012/fixtures').is_dir()),None)
    if not fixtures:
        ap.error('use --fixtures DIRECTORY with both pinned public inputs')
    stats,records=public(fixtures)
    if a.archive:
        stats['authorized_source_replay']=source(a.archive,fixtures)
    if a.traces:
        save_traces(a.traces,records)
    out=json.dumps(stats,ensure_ascii=False,indent=2)+'\n'
    if a.output:
        a.output.write_text(out)
    else:
        print(out,end='')


if __name__ == '__main__':
    main()
