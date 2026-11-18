#!/usr/bin/env python3
"""Exact rational reproducer for R284R; auxiliary named-Port algebra only."""
from fractions import Fraction as Q
from itertools import product
import json

N = 6
EDITS = ((1, 2), (3, 4), (5, 5))

def inverse(W):
    n = len(W)
    a = [[(Q(i == j) - W[i][j]) for j in range(n)]
         + [Q(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        h = next(i for i in range(k, n) if a[i][k])
        a[k], a[h] = a[h], a[k]
        c = a[k][k]
        a[k] = [v / c for v in a[k]]
        for i in range(n):
            if i != k:
                c = a[i][k]
                a[i] = [v - c * w for v, w in zip(a[i], a[k])]
    return [row[n:] for row in a]

def build(model, x=Q(0), y=Q(0), z=Q(0)):
    W = [[Q(0) for _ in range(N)] for _ in range(N)]
    W[0][1] = Q(1,4)
    if model == 1:
        W[2][0] = Q(1,4)
        W[0][3], W[4][0] = Q(1,8), Q(1,8)
    else:
        W[2][0], W[2][1] = Q(15,64), Q(1,4)
    W[1][2], W[3][4], W[5][5] = x, y, z
    assert all(sum(row) < 1 and min(row) >= 0 for row in W)
    return W

def closure(seeds, arcs, reverse=False):
    visited = set(seeds)
    frontier = list(seeds)
    while frontier:
        v = frontier.pop()
        for a, b in arcs:
            i, j = (b,a) if reverse else (a,b)
            if i == v and j not in visited:
                visited.add(j)
                frontier.append(j)
    return visited

def signatures(W):
    S = inverse(W)
    initial = {i for i,(u,v) in enumerate(EDITS) if S[0][u] > 0}
    terminal = {i for i,(u,v) in enumerate(EDITS) if S[v][0] > 0}
    arcs = {(i,j) for i,(_,v) in enumerate(EDITS)
            for j,(u,_) in enumerate(EDITS) if S[v][u] > 0}
    relevant = closure(initial,arcs) & closure(terminal,arcs,True)
    cyclic = {i for i in range(len(EDITS)) if (i,i) in arcs
              or any((i,j) in arcs and i in closure({j},arcs)
                     for j in range(len(EDITS)) if i != j)}
    return relevant, cyclic

def valuation(x, p):
    if x == 0: return None
    a,b = x.numerator,x.denominator
    z=0
    while a%p == 0: a//=p; z+=1
    while b%p == 0: b//=p; z-=1
    return z

def kappa(nodes,p):
    return max(sum(valuation(nodes[j]-nodes[l],p) for l in range(len(nodes)) if l!=j)
               for j in range(len(nodes))) if len(nodes)>1 else 0

R1, C1 = signatures(build(1))
R2, C2 = signatures(build(2))
U = R1 | R2
B = R1 & R2 & (C1 | C2)
assert (R1, R2, C1, C2, U, B) == (
    {0,1}, {0}, {0,1,2}, {0,2}, {0,1}, {0})

check_count = 0
for x,y,z in product((Q(0),Q(1,101),Q(2,101),Q(1,2)),
                     (Q(0),Q(1,101),Q(1,4)), (Q(0),Q(1,101))):
    f1, f2 = inverse(build(1,x,y,z))[0][0], inverse(build(2,x,y,z))[0][0]
    assert f1 == Q(1)/(1-x/Q(16)-y/Q(64))
    assert f2 == (1-x/Q(4))/(1-Q(79,256)*x)
    check_count += 2

new_grid = list(product((Q(0),Q(1,101),Q(2,101)),(Q(0),Q(1,101))))
assert len(new_grid) == 6
assert inverse(build(1,Q(1,4),Q(1,4),Q(0)))[0][0] == Q(256,251)
assert inverse(build(2,Q(1,4),Q(1,4),Q(0)))[0][0] == Q(64,63)
for x in (Q(0),Q(1,4)):
    assert inverse(build(1,x,0,0))[0][0] == inverse(build(2,x,0,0))[0][0]
assert inverse(build(1,Q(1,2),0,0))[0][0] == Q(32,31)
assert inverse(build(2,Q(1,2),0,0))[0][0] == Q(448,433)

assert kappa((Q(0),Q(1,101),Q(2,101)),2) == 1
assert kappa((Q(0),Q(1,101)),2) == 0
assert kappa((Q(0),Q(1,101),Q(2,101)),13) == 0

print(json.dumps({
  "status":"PASS", "matrix_inverse_and_closed_form_checks":check_count,
  "model1_relevant":sorted(R1),"model2_relevant":sorted(R2),
  "model1_cycle_support":sorted(C1),"model2_cycle_support":sorted(C2),
  "global_relevant":sorted(U),"three_sample_set":sorted(B),
  "adaptive_grid_points":len(new_grid),"R284_cycle_grid_points":27,
  "R282_general_grid_points":27,"p2_interpolation_loss_digits":1,
  "p13_interpolation_loss_digits":0,
  "witness_at_x_y_1over4":["256/251","64/63"],
  "two_node_failure_at_y0_x1over2":["32/31","448/433"]
},sort_keys=True,indent=2))
