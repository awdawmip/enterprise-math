#!/usr/bin/env python3
"""Exact-rational Bayesian hinge / three-point moment gate verification.
External two-measure finite tree; not a native X6 physical simulation.
Uses only fractions.Fraction; assertions are exact.
"""
from fractions import Fraction as F
from itertools import product

z = F(0)
one = F(1)
gamma = F(7, 48)
low, middle, high = F(1, 10), one, F(19, 10)
yvals = (F(1, 2), one, F(3, 2))
ka = (F(1, 4), F(1, 2), F(1, 4))
kb = (F(1, 3), F(1, 3), F(1, 3))
q2 = (F(2, 5), F(1, 5), F(2, 5))

def weighted_sum(a, b):
    return sum((x*y for x,y in zip(a,b)), z)

def phi(r):
    return min(r, one)

def moment(k, law):
    return weighted_sum((yy**k for yy in yvals), law)

assert sum(q2, z) == one and weighted_sum((low, middle, high), q2) == one
assert all(x>0 for x in q2+ka+kb)
for law in (ka,kb):
    assert sum(law,z)==one and moment(1,law)==one
ma, mb = moment(2,ka), moment(2,kb)
ha, hb = weighted_sum((phi(y) for y in yvals),ka),weighted_sum((phi(y) for y in yvals),kb)
assert (ma,mb,ha,hb)==(F(9,8),F(7,6),F(7,8),F(5,6))
assert ha-hb==-(ma-mb)/(yvals[-1]-yvals[0])==F(1,24)
assert gamma==phi(one)-(ha+hb)/2
assert ha+gamma-one==F(1,48) and hb+gamma-one==-F(1,48)

# Full tree. Node tuple: (name, t, unconditional Q mass, LR, children-names).
# The next-step Q transition weights are child.mass/parent.mass.
nodes={}
def add(name,t,q,r,children=()):
    assert name not in nodes
    nodes[name]=(t,q,r,tuple(children))

for branch,law in (("a",ka),("b",kb)):
    add(branch,1,F(1,2),one,(branch+"L",branch+"M",branch+"H"))
    for key,p,r in (("L",q2[0],low),("M",q2[1],middle),("H",q2[2],high)):
        n=branch+key
        if key=="M":
            kids=tuple(n+str(j) for j in range(3))
            add(n,2,F(1,2)*p,r,kids)
            for j in range(3):
                add(kids[j],3,F(1,2)*p*law[j],yvals[j])
        else:
            add(n,2,F(1,2)*p,r,(n+"0",))
            add(n+"0",3,F(1,2)*p,r)

for depth in (1,2,3):
    names=[name for name,node in nodes.items() if node[0]==depth]
    assert sum((nodes[n][1] for n in names),z)==one
    assert sum((nodes[n][1]*nodes[n][2] for n in names),z)==one
for name,(t,q,r,kids) in nodes.items():
    if kids:
        assert sum((nodes[k][1] for k in kids),z)==q
        assert sum((nodes[k][1]*nodes[k][2] for k in kids),z)==q*r
assert len([n for n in nodes if nodes[n][0]==3])==10

# Fixed deterministic stopping policy; choose Bayes-optimal binary decisions.
def observables(rule):
    out=[z,z,z,z]
    def walk(name):
        t,q,r,children=nodes[name]
        if children and rule(name):
            for child in children:
                walk(child)
        else:
            # When r=1, ties are broken toward deciding P.
            decide_q=r<one
            out[0]+=q*r if decide_q else z
            out[1]+=q if not decide_q else z
            out[2]+=t*q*r
            out[3]+=t*q
    for first in ("a","b"):
        walk(first)
    return tuple(out)

def J(o):
    return o[0]+o[1]+gamma*o[3]

coarse=((1,one),(2,low),(2,middle),(2,high))
all_compressed=[]
for bits in product((False,True),repeat=4):
    rule=dict(zip(coarse,bits))
    o=observables(lambda n: rule.get((nodes[n][0],nodes[n][2]),False))
    all_compressed.append((J(o),bits,o))
sc=min(j for j,_,_ in all_compressed)
assert sc==F(559,600)

full_nodes=tuple(n for n,d in nodes.items() if d[0]<3)
assert len(full_nodes)==8
all_full=[]
for bits in product((False,True),repeat=8):
    rule=dict(zip(full_nodes,bits))
    o=observables(lambda n: rule.get(n,False))
    all_full.append((J(o),bits,o))
sf=min(j for j,_,_ in all_full)
assert sf==F(2231,2400)
assert sc-sf==F(1,480)

full_opt=observables(lambda n: n in ("a","b","bM"))
compressed_stop=observables(lambda n: n in ("a","b"))
compressed_cont=observables(lambda n: n in ("a","b","aM","bM"))
assert full_opt==(F(17,300),F(17,30),F(21,10),F(21,10))
assert compressed_stop==(F(1,25),F(3,5),F(2),F(2))
assert compressed_cont==(F(83,1200),F(13,24),F(11,5),F(11,5))
assert J(full_opt)==sf and J(compressed_stop)==J(compressed_cont)==sc

print("K_a_m2",ma,"K_b_m2",mb,"Delta_m2",ma-mb)
print("K_a_hinge",ha,"K_b_hinge",hb,"Delta_hinge",ha-hb)
print("gamma_Q",gamma,"collision_continue_costs",ha+gamma-one,hb+gamma-one)
print("history_count",len(nodes),"strict_positive_leaf_count",10)
print("full_deterministic_patterns",len(all_full),"compressed_deterministic_patterns",len(all_compressed))
print("full_opt_four",tuple(map(str,full_opt)))
print("compressed_stop_four",tuple(map(str,compressed_stop)))
print("compressed_continue_four",tuple(map(str,compressed_cont)))
print("full_opt_cost",sf,"compressed_opt_cost",sc,"exact_gap",sc-sf)
print("ALL EXACT CHECKS PASSED")
