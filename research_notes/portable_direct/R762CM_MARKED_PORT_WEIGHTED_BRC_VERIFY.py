#!/usr/bin/env python3
"""R762CM: pure exact-integer marked-token BRC enumeration and quotient checks."""
from itertools import combinations, permutations
import json

V = tuple(range(4))
E = tuple(combinations(V, 2))
ES = frozenset(E)
MARKED = (0, 1)
ORDER = "FMO"

def canon(A):
    A = frozenset(A)
    return tuple(sorted((tuple(sorted(A)), tuple(sorted(ES - A)))))

STATES = tuple(sorted({canon(A) for A in combinations(E, 3)}))
assert len(STATES) == 10

def state_class(s):
    degree_profiles = [tuple(sorted(sum(v in e for e in T) for v in V)) for T in s]
    if (1, 1, 1, 3) in degree_profiles:
        return "F"
    T = next(T for T in s if MARKED in T)
    degrees = {v: sum(v in e for e in T) for v in V}
    return "M" if all(degrees[v] == 2 for v in MARKED) else "O"

CLS = {s: state_class(s) for s in STATES}
assert [sum(CLS[s] == c for s in STATES) for c in ORDER] == [4, 2, 4]

def swaps(s):
    A,B = map(set,s)
    d = {}
    for a in A:
        for b in B:
            t = canon((A - {a}) | {b})
            assert t not in d
            d[t] = int(MARKED in (a,b))
    assert set(d) == set(STATES)-{s}
    assert sum(d.values()) == 3
    return d

SWAP = {s: swaps(s) for s in STATES}
for s in STATES:
    for t,m in SWAP[s].items():
        assert SWAP[t][s] == m

def transfer(lam):
    return [
        [lam+2, 2, 2*lam+2],
        [4, lam, 2*lam+2],
        [2*lam+2, lam+1, 3]
    ]

def act(s,p):
    return canon(tuple(sorted((p[u],p[v]))) for u,v in s[0])

STABILIZER = [p for p in permutations(V) if tuple(sorted((p[0],p[1]))) == MARKED]
assert len(STABILIZER) == 4
for s in STATES:
    for p in STABILIZER:
        assert CLS[s] == CLS[act(s,p)]
        for t,m in SWAP[s].items():
            assert SWAP[act(s,p)][act(t,p)] == m

def counts(s,lam,n):
    z = {s:1}
    for _ in range(n):
        nxt = {t:0 for t in STATES}
        for a,w in z.items():
            for b,marked in SWAP[a].items():
                nxt[b] += w*(lam if marked else 1)
        z=nxt
    return [sum(w for t,w in z.items() if CLS[t]==c) for c in ORDER]

LAMBDAS = [0,1,2,3,4,5,7,11]
DEPTH = 9
checks = 0
for lam in LAMBDAS:
    M = transfer(lam)
    d = 3*lam+6
    assert all(sum(row)==d for row in M)
    for s in STATES:
        obs = [sum(lam if is_marked else 1
                   for t,is_marked in SWAP[s].items() if CLS[t]==c)
               for c in ORDER]
        assert obs == M[ORDER.index(CLS[s])]
        checks += 1
    a=[4,2,4]
    assert [sum(a[i]*M[i][j] for i in range(3)) for j in range(3)] == [d*x for x in a]
    for s in STATES:
        vec=[int(CLS[s]==c) for c in ORDER]
        for t in range(DEPTH+1):
            assert vec == counts(s,lam,t)
            assert sum(vec) == d**t
            checks += 1
            vec = [sum(vec[i]*M[i][j] for i in range(3)) for j in range(3)]
    ev=[d,lam-2,1-2*lam]
    trace=sum(M[i][i] for i in range(3))
    min2=sum(M[i][i]*M[j][j]-M[i][j]*M[j][i] for i,j in combinations(range(3),2))
    det=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    assert trace == sum(ev)
    assert min2 == sum(x*y for x,y in combinations(ev,2))
    assert det == ev[0]*ev[1]*ev[2]
    checks += 4

for lam in LAMBDAS:
    M = transfer(lam)
    assert (M[1][0] == M[2][0]) == (lam == 1)

for cls in ORDER:
    s = next(s for s in STATES if CLS[s]==cls)
    for t in range(1,11):
        out = counts(s,2,t)
        correction = [-4,-2,6] if cls in "FM" else [6,3,-9]
        assert [5*x for x in out] == [12**t*x+(-3)**(t-1)*y
                                     for x,y in zip([2,1,2],correction)]
        checks += 1

print(json.dumps({
    "schema":"R762CM_MARKED_PORT_WEIGHTED_BRC_EVIDENCE_V1",
    "task_id":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
    "scope":"conditional six-distinguishable-token candidate, NOT native event license",
    "marked_native_axis_token":"K4-edge-01",
    "number_of_assemblies":10,
    "observer_classes":{"F":4,"M":2,"O":4},
    "test_lambda_values":LAMBDAS,
    "test_depth_range":[0,DEPTH],
    "raw_named_states_per_lambda":10,
    "group_stabilizer_size":len(STABILIZER),
    "exact_assertion_checks":checks,
    "transfer_matrix_lambda_2":transfer(2),
    "spectrum_lambda_2":[12,0,-3],
    "row_total_lambda_formula":"3*lambda+6",
    "stationary_class_mass_ratio":[4,2,4],
    "minimal_predictive_classes":"2 if lambda=1, else 3",
    "author_execution":"PASS",
    "independent_review":"NOT_REVIEWED",
    "native_event_license":"UNVERIFIED"
},indent=2))
