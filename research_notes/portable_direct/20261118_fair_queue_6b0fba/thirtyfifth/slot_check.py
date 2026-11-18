"""Exact V30 two-PASS fiber census. Optional --source-root audits frozen files and CWM."""
import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path

SETS = tuple(combinations(range(6), 3))
NEIGH = {s: [t for t in SETS if len(set(s) & set(t)) == 2] for s in SETS}
MATCHINGS = (((0,1),(2,3),(4,5)), ((0,2),(1,4),(3,5)),
             ((0,3),(1,5),(2,4)), ((0,4),(1,3),(2,5)))
M0 = ((0,0,2,2),(0,0,1,1),(0,0,0,1),(0,0,0,0))
RIN, ROUT = (0,0,6,3), (7,2,0,0)
S0, ID = (3,4,5), (0,1,2)
PIN = '9bd555f38528adc18dc4fbda71bb5dff2d57fbd4'
SOURCES = {
    'research_notes/X6_EVENT_ORDER_RELATIVE_HOLONOMY_OBSTRUCTION_V30_20260906.md':
        'fb63d8ed671ee846540085e4f51844f7313f04497368d4d4c654d6f7f6809a8f',
    'research_notes/X6_PASSAGE_CONTINUITY_AND_NETWORK_BIAS_V28_20260906.md':
        '63c0bf6b46e7f8f3ebb5fa9409175c6c0c26965af83d7beaa37cd74acd6afdf1',
    'experiments/x6_network_event_ledger_v29_20260906/check_event_order_holonomy.py':
        '184c5954d9211f8c2c1ee55972008d6b5b324b60e4c7c64a7ca3fef6046673d4',
    'src/enterprise_math/brc_weighted.py':
        '4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f',
}


def compact(seq):
    return ''.join(map(str,seq))


def matching_sign(m,s):
    value = 1
    for x,y in m:
        if (x in s) == (y in s):
            return 0
        value *= -1 if y in s else 1
    return value


C = {s:tuple(matching_sign(m,s) for m in MATCHINGS) for s in SETS}


def canonical_slots(slots,s,t):
    removed = next(x for x in s if x not in t)
    return tuple(slots[s.index(x if x in s else removed)] for x in t)


def compact_step(s,delta):
    # V28 u0, Omega0, followed by the signed valuation of PASS(0,1)-PASS(1,0).
    u = [-3+delta,-delta,4,-1]
    omega = ((0,delta,2,2),(-delta,0,1,1),(-2,-1,0,1),(-2,-1,-1,0))
    coeff = [u[b]+sum(C[s][a]*omega[a][b] for a in range(4)) for b in range(4)]
    options = [(sum(x*y for x,y in zip(coeff,C[t])),t) for t in NEIGH[s]]
    options.sort(reverse=True)
    if options[0][0]==options[1][0]:
        return None
    return options[0][1],options[0][0]-options[1][0]


@lru_cache(None)
def candidates(s,delta):
    win = compact_step(s,delta)
    if win is None:
        return None
    t,gap = win
    return t,canonical_slots(ID,s,t),gap


def ledger(a,b):
    m = [list(r) for r in M0]
    m[0][1] += a
    m[1][0] += b
    return m


@lru_cache(None)
def ledger_step(s,a,b):
    # Direct nonnegative tally. Each M_ij contributes cT_i - cT_j and
    # cS_i*cT_j - cS_j*cT_i. Residual occurrences contribute +/- cT_i.
    m = ledger(a,b)
    choices = []
    for t in NEIGH[s]:
        pos,neg = 0,0
        def credit(sign,mass):
            return (mass,0) if sign==1 else ((0,mass) if sign==-1 else (0,0))
        marks = [(C[t][i],RIN[i]) for i in range(4)] + [(-C[t][i],ROUT[i]) for i in range(4)]
        for i,j in product(range(4),repeat=2):
            if m[i][j]:
                for sign in (C[t][i],-C[t][j],C[s][i]*C[t][j],-C[s][j]*C[t][i]):
                    marks.append((sign,m[i][j]))
        for sign,mass in marks:
            p,n = credit(sign,mass)
            pos += p
            neg += n
        choices.append((t,pos,neg))
    winners = [(t,p,n) for t,p,n in choices if all(p+nn>pp+n for tt,pp,nn in choices if t!=tt)]
    if not winners:
        return None
    t,p,n = winners[0]
    gap = min((p+nn)-(pp+n) for tt,pp,nn in choices if t!=tt)
    return t,gap


def raw_word(word):
    s = S0
    named_axes = list(s)  # position is the original slot, value is the current axis.
    a = b = 0
    gaps = []
    for symbol in word:
        a += symbol=='A'
        b += symbol=='B'
        step = ledger_step(s,a,b)
        if step is None:
            return None
        t,gap = step
        gone, = set(s)-set(t)
        entered, = set(t)-set(s)
        named_axes[named_axes.index(gone)] = entered
        gaps.append(gap)
        s = t
    return (s,tuple(named_axes.index(axis) for axis in s),a-b),gaps


def block(s,name):
    slots,d = ID,0
    trace = []
    for symbol in name:
        d += 1 if symbol=='A' else -1
        t,act,gap = candidates(s,d)
        slots = tuple(slots[j] for j in act)
        trace.append([compact(t),gap])
        s = t
    assert d == 0
    return {'end':compact(s),'slots':compact(slots),'path_and_gaps':trace}


def run(source_root):
    if source_root:
        for path,sha in SOURCES.items():
            assert hashlib.sha256((source_root/path).read_bytes()).hexdigest()==sha
        sys.path.insert(0,str(source_root/'src'))
        from enterprise_math.brc_weighted import CWM_ONE,CWM_ZERO,cwm_recoalesce,cwm_propagate
        init = CWM_ONE
        def add(a,b):
            return cwm_recoalesce(a,cwm_propagate(b,CWM_ONE))
        zero = CWM_ZERO
        def mass(c):
            assert c.total==c.count and c.dominant==int(c.live)
            return c.count
    else:
        # Unit-weight specialization CWM(k,k,1[k>0]): serial unit is identity,
        # disjoint alternative histories add counts.
        init,zero,add,mass = 1,0,int.__add__,int
    layer = {(S0,ID,0):init}
    levels = []
    witnesses = {}
    for length in range(11):
        groups = defaultdict(dict)
        simple = defaultdict(Counter)
        last_observed = defaultdict(set)
        accepted,attempted = 0,2**length
        for letters in product('AB',repeat=length):
            word = ''.join(letters)
            result = raw_word(word)
            if result is None:
                continue
            accepted += 1
            (s,slots,d),gaps = result
            simple[(s,d)][slots] += 1
            last_observed[(s,d,word[-1:])].add(slots)
            groups[(s,d)].setdefault(slots,(word,gaps))
        compare = {(s,slots,d):count for (s,d),row in simple.items() for slots,count in row.items()}
        assert compare == {k:mass(v) for k,v in layer.items()}
        profile = Counter(map(len,groups.values()))
        max_size = max(profile)
        winners = [(s,d) for s,d in groups if len(groups[s,d])==max_size]
        if length in (9,10):
            for s,d in sorted(winners):
                witnesses[f'{length}_{compact(s)}_{d}'] = {
                    compact(slots):{'first_word':word,'winner_gaps':gaps,'path_count':simple[s,d][slots]}
                    for slots,(word,gaps) in sorted(groups[s,d].items())}
        levels.append({'length':length,'raw_words':attempted,'strict_words':accepted,
                       'group_count_by_frame_fiber_size':dict(sorted(profile.items())),
                       'largest':max_size,'largest_with_last_pass':max(map(len,last_observed.values())),
                       'reachable_framed_states':len(layer)})
        if length == 10:
            break
        next_layer = {}
        for (s,slots,d),v in layer.items():
            for plus in (1,-1):
                new_d = d+plus
                step = candidates(s,new_d)
                if step:
                    t,act,_ = step
                    key=t,tuple(slots[j] for j in act),new_d
                    next_layer[key] = add(next_layer.get(key,zero),v)
        layer = next_layer
    assert [r['largest'] for r in levels] == [1,1,2,2,2,2,2,2,2,4,6]
    assert [r['largest_with_last_pass'] for r in levels] == [1,1,1,2,2,2,2,2,2,2,6]
    assert set(witnesses) == {'9_134_1','10_034_0','10_034_2'}
    assert len(witnesses['10_034_0']) == 6

    blocks = {compact(s):{word:block(s,word) for word in ('AB','BA')}
              for s in ((3,4,5),(0,3,4),(2,3,5),(0,1,5))}
    for s,t,k in [('034','235','210'),('235','015','102'),('015','034','021')]:
        assert all((b['end'],b['slots'])==(t,k) for b in blocks[s].values())
    assert {b['slots'] for b in blocks['345'].values()} == {'201','021'}
    transport_round = ID
    for s in ('034','235','015'):
        transport_round = tuple(transport_round[int(j)] for j in blocks[s]['AB']['slots'])
    assert transport_round==(1,0,2)
    departure_reads = {}
    for word in ('AA','AB','BA','BB'):
        outputs = {}
        for p in permutations(ID):
            s,slots,d = (0,3,4),p,0
            reads = []
            for symbol in word:
                d += 1 if symbol=='A' else -1
                t,action,_ = candidates(s,d)
                gone, = set(s)-set(t)
                reads.append(slots[s.index(gone)])
                s,slots = t,tuple(slots[j] for j in action)
            assert tuple(reads)==(p[2],p[0])
            outputs[compact(p)] = compact(reads)
        assert len(set(outputs.values()))==6
        departure_reads[word] = outputs
    return {'source_commit':PIN,'source_sha256':SOURCES,'typed_events':['PASS(0,1)','PASS(1,0)'],
            'seed':{'M':M0,'Rin':RIN,'Rout':ROUT,'triad':S0,'named_slots':ID},
            'semantic_scope':'V30 local research transducer; supplied words; no autonomous inter-Cell scheduler',
            'finite_ledger_word_crosscheck':'raw two-color signed tally and named slots vs compressed BRC',
            'raw_word_slices_tested':sum(r['raw_words'] for r in levels),
            'levels':levels,'maximal_fiber_witnesses_at_9_10':witnesses,'paired_blocks':blocks,
            'three_paired_blocks_from_034_slot_transport':compact(transport_round),
            'two_departure_readouts_from_full_balanced_034':departure_reads}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path)
    args=parser.parse_args()
    print(json.dumps(run(args.source_root),sort_keys=True,indent=2))
