"""R762X exact integer checks of prefix-inventory theorem in a *conditional* V29 token lift.
No physical TRIADIC_CLOSURE_E admission, V17 or V39 dynamics are assumed.
"""
from itertools import product
from collections import Counter
import json


def fixed_seed_profile(events):
    deficit, need = Counter(), Counter()
    for a, b in events:
        # Pre-event enabling requires one token at the tail, including self-loops.
        need[a] = max(need[a], 1 + deficit[a])
        deficit[a] += 1
        deficit[b] -= 1
    return sum(need.values()), {str(x): need[x] for x in sorted(need) if need[x]}


def can_replay(events, initial):
    n = Counter(initial)
    for a,b in events:
        if n[a] <= 0:
            return False
        n[a] -= 1
        n[b] += 1
    return True


def allocations(vertices, total):
    if len(vertices) == 1:
        yield {vertices[0]: total}
    else:
        for n in range(total+1):
            for z in allocations(vertices[1:], total-n):
                yield {vertices[0]: n, **z}


def verify_short_sequences(include_loops=False, max_length=5):
    vertices = ('a','b','c')
    opts = [(a,b) for a in vertices for b in vertices if include_loops or a!=b]
    checks = 0
    for length in range(1,max_length+1):
        for seq in product(opts, repeat=length):
            val, profile = fixed_seed_profile(seq)
            assert can_replay(seq,profile)
            for init in allocations(vertices,val-1):
                assert not can_replay(seq,init), (seq,init,val)
            checks += 1
    return checks


def cycle_examples():
    out = {}
    a,b,c = ('a','b'),('b','c'),('c','a')
    for k in range(1,9):
        good = [e for _ in range(k) for e in (a,b,c)]
        grouped = [a]*k+[c]*k+[b]*k
        gv,gp = fixed_seed_profile(good)
        bv,bp = fixed_seed_profile(grouped)
        assert gv == 1 and bv == 2*k
        assert Counter(good) == Counter(grouped)
        out[str(k)] = {'interleaved':gv,'grouped':bv,'grouped_profile':bp}
    return out


def network_example(shared):
    p = [('A:0','A:1'),('A:1','A:2'),('A:2','A:0')]
    t = [(f'A:{i}', 'B:0' if shared else 'B:1') for i,m in ((0,2),(1,4),(2,3)) for _ in range(m)]
    f = [('B:0','A:3')]*10
    good = p+t+f
    bad = f+t+p
    kg,pg = fixed_seed_profile(good)
    kb,pb = fixed_seed_profile(bad)
    assert Counter(good)==Counter(bad)
    assert (kg,kb)==((10,20) if shared else (19,20))
    assert can_replay(good,pg) and can_replay(bad,pb)
    return {'good_seed':kg,'bad_seed':kb,'good_profile':pg,'bad_profile':pb, 'count_events':len(good)}


def run():
    evidence={
      'schema':'R762X_TEMPORAL_PREFIX_CAUSAL_SEED_EXACT_V1',
      'status':'CONDITIONAL_TOKEN_LIFT_ONLY_NOT_NATIVE_TRIADIC_EVENT',
      'arithmetic':'exact unbounded Python integers; no floats',
      'nonloop_sequences_exhaustively_verified':verify_short_sequences(),
      'including_loops_sequences_exhaustively_verified':verify_short_sequences(include_loops=True,max_length=4),
      'domain':'all ordered nonloop directed events on a,b,c lengths 1..5, and all ordered directed events including loops lengths 1..4; all initial allocations with K-1 tokens excluded',
      'cycle_family':cycle_examples(),
      'R762U_original_two_B_ports':network_example(False),
      'R762U_reconnected_shared_B_port':network_example(True),
    }
    assert evidence['nonloop_sequences_exhaustively_verified']==sum(6**m for m in range(1,6))
    assert evidence['including_loops_sequences_exhaustively_verified']==sum(9**m for m in range(1,5))
    return evidence


if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False,sort_keys=True))
