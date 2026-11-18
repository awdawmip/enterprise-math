#!/usr/bin/env python3
"""Exact Fraction checks for R283; examples only, not a substitute for symbolic proof."""
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path

INF = 10**8

def vp(a, p):
    a = Q(a)
    if a == 0:
        return INF
    def count(z):
        z = abs(z)
        c = 0
        while z % p == 0:
            z //= p
            c += 1
        return c
    return count(a.numerator) - count(a.denominator)

def exact_one_port(w, x):
    assert 0 <= w and 0 <= x and w + x < 1
    return 1 / (1 - w - x)

def check_resonance(p, N, t):
    delta = Q(p**N, 1 + p**(2*N))
    eps = Q(p**t, 1 + 4*p**t)
    w0, w1 = Q(1,2), Q(1,2) + delta
    grid = [Q(0), Q(1,16), Q(1,8)]
    assert 0 < delta < eps < Q(1,2) and t > N
    vals = []
    for x in grid:
        z = exact_one_port(w1,x) - exact_one_port(w0,x)
        vals.append(vp(z,p))
        assert vp(z,p) == N
    x = Q(1,2) - eps
    diff = exact_one_port(w1,x) - exact_one_port(w0,x)
    assert vp(1-w0-x,p) == t
    assert vp(1-w1-x,p) == N
    assert vp(diff,p) == -t
    return {"p":p,"N":N,"t":t,"grid_difference_valuations":vals,
            "resonant_x":[x.numerator,x.denominator],"difference_valuation_at_x":vp(diff,p)}

def polyvals(coef, nodes):
    return [sum(c*(x**j) for j,c in enumerate(coef)) for x in nodes]

def check_interpolation(p, nodes, kappa):
    checked=0
    for coeff in product(range(-2,3),repeat=3):
        if not any(coeff):
            continue
        inp=min(vp(c,p) for c in coeff)
        out=min(vp(v,p) for v in polyvals(coeff,nodes))
        assert inp >= out-kappa,(p,coeff,inp,out,kappa)
        checked+=1
    return checked

def brc_sharpness():
    # Models on ports 0,1,2. Baseline edges 0->1=a, 2->0=b,
    # 2->1=gamma; named edit 1->2 of weight x.
    a=Q(1,4)
    def F(b,g,x):
        assert 0<=g and 0<=b and b+g<1 and x<1
        return (1-g*x)/(1-(g+a*b)*x)
    nodes=[Q(0),Q(1,5),Q(2,5)]
    lhs=[F(Q(1,4),Q(0),x) for x in nodes]
    rhs=[F(Q(6,25),Q(1,5),x) for x in nodes]
    assert lhs[:2] == rhs[:2]
    assert lhs[2] != rhs[2]
    # p=2 integral presentations of the two response functions.
    def N1(x): return Q(16)
    def D1(x): return Q(16)-x
    def N2(x): return Q(2)-Q(2,5)*x
    def D2(x): return Q(2)-Q(13,25)*x
    cross=[N1(x)*D2(x)-N2(x)*D1(x) for x in nodes]
    assert cross==[Q(0),Q(0),Q(-4,125)]
    assert min(vp(c,2) for c in [Q(2,25),Q(-2,5)])==1
    assert min(vp(c,2) for c in cross)==2
    return {"grid":[str(x) for x in nodes],"F1":[str(x) for x in lhs],
            "F2":[str(x) for x in rhs],"cross_product_grid":[str(x) for x in cross],
            "grid_min_v2":2,"coefficient_min_v2":1,"sharp_loss":1}

def main():
    p2=[Q(0),Q(1,5),Q(2,5)]
    p13=[Q(0),Q(1,16),Q(1,8)]
    # Lagrange denominator valuations: max over nodes of sum of two differences.
    def kappa(nodes,p):
        return max(sum(vp(nodes[j]-nodes[a],p) for a in range(3) if a!=j) for j in range(3))
    assert kappa(p2,2)==1 and kappa(p13,13)==0
    checks={"interpolation_p2":check_interpolation(2,p2,1),
            "interpolation_p13":check_interpolation(13,p13,0)}
    sharp=brc_sharpness()
    res=[check_resonance(13,N,t) for (N,t) in [(1,2),(2,3),(4,7),(6,10)]]
    # Tensor interpolation loss m is attained by P=prod x_i*(1/5-x_i).
    tensor={}
    for m in range(1,5):
        grid_vals=[]
        for xs in product(p2,repeat=m):
            v=Q(1)
            for x in xs: v*=x*(Q(1,5)-x)
            grid_vals.append(v)
        assert min(vp(v,2) for v in grid_vals)==m
        tensor[str(m)]={"minimum_grid_v2":m,"unit_leading_coefficient":True}
    data={"status":"PASS","arithmetic":"Python fractions.Fraction, exact integer p-adic valuations",
          "science_pin":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
          "interpolation_kappa":{"p2_nodes_0_1over5_2over5":1,"p13_nodes_0_1over16_1over8":0},
          "finite_coefficient_sets_checked":checks,"brc_p2_sharpness":sharp,
          "p13_unbounded_resonance_witnesses":res,"tensor_sharpness":tensor,
          "scope":"exact example checks; universal interpolation and resonance claims established by written algebraic proofs"}
    target=Path("R283_verification.json")
    target.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(data,indent=2,ensure_ascii=False))
if __name__=="__main__":main()
