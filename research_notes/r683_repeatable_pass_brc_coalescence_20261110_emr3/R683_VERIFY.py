from itertools import combinations
from collections import defaultdict
from fractions import Fraction
import json

TRIADS = tuple(combinations(range(6), 3))
MATCH = (((0,1),(2,3),(4,5)), ((0,2),(1,4),(3,5)),
         ((0,3),(1,5),(2,4)), ((0,4),(1,3),(2,5)))
PASS = ((0,1), (1,2), (2,0))
BIASES = ((-4,-3,-2,10), (-3,-2,-4,10), (-2,-4,-3,10),
          (2,4,3,-10), (3,2,4,-10), (4,3,2,-10))
W = (-1,1,-2,-1)

def code(S, matching):
    if any((a in S) + (b in S) != 1 for a,b in matching):
        return 0
    return 1 if sum(b in S for a,b in matching) % 2 == 0 else -1

C = {S:tuple(code(S,m) for m in MATCH) for S in TRIADS}
N = {S:tuple(T for T in TRIADS if len(set(S) & set(T)) == 2) for S in TRIADS}
assert len(C) == 20 and len(set(C.values())) == 20
assert all(len(N[S]) == 9 for S in TRIADS)

def step(u, M, e):
    a,b = PASS[e]
    v = list(u); v[a] += 1; v[b] -= 1
    L = [list(row) for row in M]; L[a][b] += 1
    return tuple(v), tuple(tuple(row) for row in L)

def psi(u, M, S, T):
    omega = sum(C[S][i] * (M[i][j]-M[j][i]) * C[T][j]
                for i in range(4) for j in range(4))
    return 7*(sum(u[i]*C[T][i] for i in range(4)) + omega) + sum(W[i]*C[T][i] for i in range(4))

def branch_choice(u, M, S):
    candidates = []
    for e,(a,b) in enumerate(PASS):
        v,L = step(u,M,e)
        scores = {T:psi(v,L,S,T) for T in N[S]}
        q = max(scores.values())
        maximizers = tuple(T for T in N[S] if scores[T] == q)
        candidates.append((q, W[a]-W[b], e, maximizers))
    winner = max(candidates)
    return winner, candidates

def propagate(bias, S0, horizon=64):
    zero = tuple((0,0,0,0) for _ in range(4))
    states = {(bias,zero,S0):Fraction(1)}
    samples = {0:states}
    for t in range(1,horizon+1):
        nxt = defaultdict(Fraction)
        for (u,M,S),mass in states.items():
            (q,d,e,bests),candidates = branch_choice(u,M,S)
            assert len(bests) >= 1
            assert all((q,d) >= (q0,d0) for q0,d0,_,_ in candidates)
            v,L = step(u,M,e)
            assert sum(v) == sum(bias)
            assert all(x>=0 for row in L for x in row)
            assert sum(map(sum,L)) == t
            for T in bests:
                nxt[(v,L,T)] += mass / len(bests)
        states = dict(nxt)
        assert sum(states.values(),Fraction(0)) == Fraction(1)
        if t in (12,13,14,18,19,32,64):
            samples[t] = states
    return samples

def certificate():
    b = (-2,-4,-3,10)
    S = (0,2,4)
    zero = tuple((0,0,0,0) for _ in range(4))
    u,M = b,zero
    word = []
    for k in range(12):
        (_,_,e,bests),_ = branch_choice(u,M,S)
        assert len(bests) == 1
        word.append("ABC"[e])
        u,M = step(u,M,e); S = bests[0]
    assert ''.join(word) == "BABABABABABA"
    assert u == (4,-4,-9,10) and S == (1,2,3)
    assert (M[0][1],M[1][2],M[2][0]) == (6,6,0)
    (q,d,e,bests), candidates = branch_choice(u,M,S)
    assert e == 1 and q == 98 and d == 3
    assert bests == ((1,2,5),(2,3,4))
    assert { "ABC"[j]:q0 for q0,d0,j,_ in candidates } == {"A":91,"B":98,"C":84}
    v,L = step(u,M,e)
    assert v == (4,-3,-10,10)
    assert (L[0][1],L[1][2],L[2][0]) == (6,7,0)

    supports = {k:[] for k in (0,13,14,18,19,32,64)}
    sample = None
    for bias in BIASES:
        for start in TRIADS:
            observations = propagate(bias,start)
            for k in supports:
                supports[k].append(len(observations[k]))
            if (bias,start) == (b,(0,2,4)):
                sample = observations
    total = {str(k):sum(a) for k,a in supports.items()}
    split = {str(k):sum(x>1 for x in a) for k,a in supports.items()}
    assert total == {"0":120,"13":122,"14":123,"18":123,"19":121,"32":121,"64":121}
    assert split == {"0":0,"13":2,"14":3,"18":3,"19":1,"32":1,"64":1}
    assert sorted(str(p) for p in sample[13].values()) == ["1/2","1/2"]
    assert len(sample[19]) == 1
    (u19,M19,S19),mass19 = next(iter(sample[19].items()))
    assert (u19,S19,mass19) == ((5,1,-15,10),(0,3,5),Fraction(1))
    assert (M19[0][1],M19[1][2],M19[2][0]) == (7,12,0)
    return {
        "schema":"R683_REPEAT_PASS_BRC_EXACT_CERTIFICATE_V1",
        "predecessor":"R681@3b3414dc143583f06e71b8595f67235bf038305a",
        "frozen_science":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
        "model":"repeat-enabled PASS A/B/C, autonomous lexicographic (Q,w_a-w_b), uniform rational ties",
        "witness":{
            "initial_bias":list(b),"initial_triad":"024","first_12_PASS":"BABABABABABA",
            "time12_u":[4,-4,-9,10],"time12_counts":[6,6,0],"time12_triad":"123",
            "time13_selected_event":"B","event_scores":{"A":91,"B":98,"C":84},
            "max_score":98,"tied_triads":["125","234"],
            "time13_u":[4,-3,-10,10],"time13_counts":[6,7,0],
            "each_positive_branch_mass":"1/2","time19_recoalesced_u":[5,1,-15,10],
            "time19_recoalesced_counts":[7,12,0],"time19_triad":"035",
            "time19_mass":"1"
        },
        "exact_finite":{
            "initial_conditions":120,"horizon":64,
            "total_support_by_time":total,"starts_with_multiple_states_by_time":split,
            "arithmetic":"Python integers and Fraction; mass conservation per update"
        }
    }

if __name__ == "__main__":
    print(json.dumps(certificate(),ensure_ascii=False,indent=2))
    print("R683_REPEAT_PASS_BRC_EXACT_PASS")
