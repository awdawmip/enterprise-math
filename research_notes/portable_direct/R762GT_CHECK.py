"""Exact finite certificates for R762GT: K4 star triad incidence and observer ranks.

Typed candidate on P000 X6 with four STAR supports; not a native
TRIADIC_CLOSURE_E permission or moving-Port/rotation law.
"""
from itertools import combinations, permutations, product
from fractions import Fraction
from collections import Counter
import json

V = tuple(range(4))
E = tuple(combinations(V, 2)) # 01, 02, 03, 12, 13, 23
STARS = {v: frozenset(i for i,e in enumerate(E) if v in e) for v in V}
B = tuple(tuple(int(v in e) for v in V) for e in E) # rows edge observers, cols STAR source types
assert len(E)==6 and all(len(STARS[v]) == 3 for v in V)
assert all(len(STARS[u] & STARS[v])==1 for u,v in combinations(V,2))
assert all(sum(i in STARS[v] for v in V)==2 for i in range(6))

# Fully enumerated automorphism action under four-vertex relabeling.
for perm in permutations(V):
    qi = tuple(E.index(tuple(sorted((perm[u],perm[w])))) for u,w in E)
    for v in V:
        assert frozenset(qi[j] for j in STARS[v]) == STARS[perm[v]]

# Candidate positive and negative closures, indexed by (v,s).
TRIADS = {(v,s): tuple(s*int(i in STARS[v]) for i in range(6))
          for v in V for s in (-1,+1)}
assert len(TRIADS)==8
assert all(sum(x!=0 for x in z)==3 for z in TRIADS.values())

# Exact rational row rank of a chosen set of named axis-count observers.
def rank(rows):
    mat = [[Fraction(x) for x in row] for row in rows]
    if not mat: return 0
    h=len(mat); w=len(mat[0]); r=0
    for c in range(w):
        k=next((j for j in range(r,h) if mat[j][c]),None)
        if k is None: continue
        mat[r],mat[k] = mat[k],mat[r]
        d=mat[r][c]
        mat[r] = [x/d for x in mat[r]]
        for j in range(h):
            if j!=r:
                t=mat[j][c]
                if t: mat[j] = [a-t*b for a,b in zip(mat[j],mat[r])]
        r+=1
        if r==h: break
    return r

R = {k:Counter() for k in range(7)}
for k in range(7):
    for obs in combinations(range(6),k):
        R[k][rank([B[i] for i in obs])] += 1
assert R[3] == Counter({3:20})
assert R[4] == Counter({4:12,3:3})
assert R[5] == Counter({4:6})
assert R[6] == Counter({4:1})

# Four named axis measurements miss exactly two edges. Rank loss iff missing edges disjoint.
good = []
bad = []
for retained in combinations(range(6),4):
    missing=tuple(i for i in range(6) if i not in retained)
    disjoint = set(E[missing[0]]).isdisjoint(E[missing[1]])
    assert (rank([B[i] for i in retained])==3)==disjoint
    (bad if disjoint else good).append(tuple(''.join(map(str,E[i])) for i in retained))
assert len(good)==12 and len(bad)==3

# Explicit nonnegative inventory collision on 4-axis observer retaining 02,03,12,13:
a=(1,1,0,0)
b=(0,0,1,1)
y_a=tuple(sum(B[i][v]*a[v] for v in V) for i in range(6))
y_b=tuple(sum(B[i][v]*b[v] for v in V) for i in range(6))
kept=tuple(E.index(e) for e in ((0,2),(0,3),(1,2),(1,3)))
assert y_a==(2,1,1,1,1,0)
assert y_b==(0,1,1,1,1,2)
assert all(y_a[i]==y_b[i] for i in kept)

# For each 2-axis subset with a shared vertex, unique third support of STAR triad.
PAIR_COMPLETIONS = {}
for i,j in combinations(range(6),2):
    vs=[v for v in V if i in STARS[v] and j in STARS[v]]
    assert len(vs)==(1 if not set(E[i]).isdisjoint(E[j]) else 0)
    if vs:
        third=next(iter(STARS[vs[0]]-{i,j}))
        PAIR_COMPLETIONS[''.join(map(str,E[i]))+'-'+''.join(map(str,E[j]))]=''.join(map(str,E[third]))
assert len(PAIR_COMPLETIONS)==12

# Exact two-letter source-BRC count at full six-axis displacement zero.
zero_words = [(u,w) for u,w in product(TRIADS,repeat=2)
              if all(TRIADS[u][i]+TRIADS[w][i] == 0 for i in range(6))]
assert len(zero_words)==8 and len(set(zero_words))==8
assert all(u[0]==w[0] and u[1]==-w[1] for u,w in zero_words)

out = {
 'schema':'R762GT_SIGNED_STAR_TRIAD_INCIDENCE_OBSERVER_V1',
 'task_id':'RS-X6-TRIADIC-CLOSURE-DYNAMICS',
 'publication_id':'TP2-8B7E13C5904A2D6F1142',
 'frozen_taskbook':'857280d1012943290d141d1317179c40ec3cbdf8',
 'frozen_p000':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'type':'CONSTRUCTED_STAR_INCIDENCE_CANDIDATE_NOT_NATIVE_PERMISSION',
 'axis_labels':[''.join(map(str,e)) for e in E],
 'star_incidence_columns':[list(int(v in e) for e in E) for v in V],
 'candidate_signed_triads':8,
 'automorphisms_checked':24,
 'distinct_axis_pair_completion_count':12,
 'distinct_axis_disjoint_pair_no_completion_count':3,
 'signed_pair_projection_with_unique_completion':24,
 'full_observer_rank':rank(B),
 'subset_ranks':{str(k):{str(r):c for r,c in sorted(R[k].items())} for k in range(7)},
 'four_axis_injective_observers':good,
 'four_axis_noninjective_observers':bad,
 'collision':{'inventory_a':list(a),'inventory_b':list(b),
              'y_a':list(y_a),'y_b':list(y_b),'kept_axes':[''.join(map(str,E[i])) for i in kept]},
 'free_candidate_two_step_BRC':{'alphabet_size':8,'total_source_words':64,'zero_cell_words':len(zero_words),'uniform_zero_probability':'1/8','named_source_words':[[list(u),list(w)] for u,w in zero_words]},
 'source_provenance_loss':'eight length-two signed opposite STAR source words give zero net six-axis displacement; complete Cell readout and step count still lose source history',
 'native_event_permission':'UNRESOLVED',
 'author_exact_check':'PASS',
 'independent_review':'NOT_REVIEWED'
}
print(json.dumps(out,ensure_ascii=False,indent=2))
