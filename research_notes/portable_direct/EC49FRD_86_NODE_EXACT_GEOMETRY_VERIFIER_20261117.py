#!/usr/bin/env python3
"""EC49FRD: exact 86-node area/regret checker.
Usage: python EC49FRD_GEOMETRY.py old71.json old12seams.json new3seams.json
Input old71.json is the inherited EC49FRC old71 list; old12seams.json
is the EC49FRC seams list. New three seams below can be supplied in a JSON file.
No network, floating-point certificate comparison, or proof assistant required.
"""
import sys,json
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
from decimal import Decimal,localcontext

assert len(sys.argv)==4
old71=sorted(set(Q(s) for s in json.loads(Path(sys.argv[1]).read_text())))
old12=[Q(s["x"]) for s in json.loads(Path(sys.argv[2]).read_text())]
new3=json.loads(Path(sys.argv[3]).read_text())
added=[Q(s["x"]) for s in new3]
old83=sorted(set(old71)|set(old12))
new=sorted(set(old83)|set(added))
assert len(old71)==71 and len(old83)==83 and len(new)==86
assert old71[0]==new[0]==1 and old71[-1]==new[-1]==3
assert all(z not in old83 for z in added)
K=lambda x:Q(7557)-169*x
G=lambda x:310*(3-x)/K(x)
D=Q(2185500)
assert all(K(x)>0 for x in new)
assert all(Q(s["lambda"])==G(Q(s["x"])) for s in new3)

def area(nodes):
    return sum(((b-a)*(G(a)-G(b)) for a,b in zip(nodes,nodes[1:])),Q(0))
S83=area(old83);S86=area(new)
assert S83==Q(44429865301826323916995,20209109482201273759125792)
assert S86==Q(10770320075410254305,5143575841741225186848)
assert S83-S86==Q(36425,348329424)
assert 1-S86/2==Q(10276381363407040119391,10287151683482450373696)
for nodes in (old83,new):
    assert area(nodes)==D/Q(169**2)*sum(
        (K(a)/K(b)+K(b)/K(a)-2 for a,b in zip(nodes,nodes[1:])),Q(0))

def root_bounds(v):
    scale=10**32
    q=isqrt(v.numerator*scale**2//v.denominator)
    lo,hi=Q(q,scale),Q(q+1,scale)
    assert lo**2<=v<hi**2
    return lo,hi

def regret_bounds(a,b):
    la,ua=root_bounds(K(a))
    lb,ub=root_bounds(K(b))
    return 50*(b-a)/(ua+ub)**2,50*(b-a)/(la+lb)**2

def strict_leader(nodes):
    items=[(a,b,*regret_bounds(a,b)) for a,b in zip(nodes,nodes[1:])]
    leader=max(items,key=lambda v:v[2])
    assert all(leader[2]>v[3] for v in items if v is not leader)
    return leader

before=strict_leader(old83);after=strict_leader(new)
assert (before[0],before[1])==(Q(13,12),Q(9,8))
assert (after[0],after[1])==(Q(19,8),Q(77,32))
with localcontext() as ctx:
    ctx.prec=75
    dec=lambda v:Decimal(v.numerator)/Decimal(v.denominator)
    R=lambda a,b:50*dec(b-a)/(dec(K(a)).sqrt()+dec(K(b)).sqrt())**2
    print(json.dumps({
      "source_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
      "nodes":len(new),"intervals":len(new)-1,
      "S83":str(S83),"S86":str(S86),"area_gain":str(S83-S86),
      "certified_percent_lower_bound":str(dec((1-S86/2)*100)),
      "old_leader":[str(before[0]),str(before[1])],
      "new_leader":[str(after[0]),str(after[1])],
      "old_regret_over_t":str(R(before[0],before[1])),
      "new_regret_over_t":str(R(after[0],after[1])),
      "strict_all_interval_comparison":True
    },indent=2))
print("EC49FRD_86_NODE_EXACT_GEOMETRY_PASS")
