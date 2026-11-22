#!/usr/bin/env python3
"""X6 R102 exact rational verification (author-side, finite bounds only)."""
from fractions import Fraction as Q
import itertools, json

C10 = [(1,0,0),(4,-1,0),(5,-4,1),(6,-4,1),(9,-5,1),
       (10,-5,1),(14,-9,2),(15,-9,2),(19,-10,2),(24,-14,3)]
PORT = {a:max(sum(max(k,0) for k in a),sum(max(-k,0) for k in a)) for a in C10}

def plateau(S,T,p):
    return T<=23 and (S<=5 or T<=11) and (p<=26 or S<=11)

def equal_half(S,T,p):
    sel={(10,-5,1)}
    if S==5 and 13<=T<=23: sel.add((1,0,0))
    if T==23 and S<=5: sel.update(((4,-1,0),(6,-4,1)))
    if (S==5 and 11<=T<=23) or (T==11 and S>=5):
        sel.update(((5,-4,1),(9,-5,1)))
    if p>=16 and T<=11 and S>=11: sel.add((14,-9,2))
    if p>=17 and ((S==5 and 13<=T<=23) or (T==11 and S>=7)):
        sel.add((15,-9,2))
    if p>=21 and T==11 and S>=7: sel.add((19,-10,2))
    if p>=27 and S==11 and T<=11: sel.add((24,-14,3))
    return frozenset(a for a in sel if PORT[a]<=p)

def score(a,S,T):
    x,y,z=a
    u=x+3*y+6*z;v=3*x+12*y+30*z;h=7*x+39*y+126*z
    return max(Q(abs(u),2),abs(v)/(S+1),abs(h)/(T+1),
               abs(v-u)/(S+1),abs(h-u)/(T+1),abs(h-v)/(S+T))

def exact_full(S,T,p,vecs):
    m=None;out=set()
    for a in vecs:
        if max(sum(max(k,0) for k in a),sum(max(-k,0) for k in a))>p: continue
        val=score(a,S,T)
        if m is None or val<m: m=val;out={a}
        elif val==m: out.add(a)
    return m,frozenset(out)

SS=[Q(v) for v in (1,4,5,6,7,10,11,12,24)] + [Q(9,2),Q(11,2),Q(23,2)]
TT=[Q(v) for v in (1,10,11,12,13,14,22,23,24)] + [Q(21,2),Q(23,2),Q(27,2)]
samples=list(itertools.product(SS,TT))+[(Q(100),Q(12)),(Q(5),Q(23)),(Q(11),Q(11))]
budgets=(11,15,16,17,20,21,26,27,30,40)
compare_count=plateau_count=0
for S,T in samples:
    for p in budgets:
        val,candidates=exact_full(S,T,p,C10)
        if plateau(S,T,p):
            assert val==Q(1,2),(S,T,p,val)
            assert candidates==equal_half(S,T,p),(S,T,p,candidates,equal_half(S,T,p))
            plateau_count+=1
        else: assert val<Q(1,2),(S,T,p,val)
        compare_count+=1

# Exhaustive q<=30 with exact 6-term F, independent of the C10 hypothesis.
vecs=[]
for x in range(-30,31):
 for y in range(-30,31):
  for z in range(-30,31):
   a=(x,y,z)
   if a==(0,0,0) or a<(0,0,0): continue
   if max(sum(max(k,0) for k in a),sum(max(-k,0) for k in a))<=30: vecs.append(a)
assert len(vecs)==47305,len(vecs)
probe=[(Q(5),Q(23)),(Q(11),Q(11)),(Q(5),Q(13)),(Q(7),Q(11)),
       (Q(100),Q(11)),(Q(11),Q(1)),(Q(1),Q(23)),(Q(5),Q(24)),
       (Q(6),Q(27)),(Q(12),Q(12)),(Q(9,2),Q(23)),(Q(5),Q(23,2))]
full_checks=0
for S,T in probe:
    for p in (11,16,17,21,26,27,30):
        val,full=exact_full(S,T,p,vecs)
        cval,core=exact_full(S,T,p,C10)
        assert val==cval and full==core,(S,T,p,val,cval,full,core)
        if plateau(S,T,p): assert full==equal_half(S,T,p)
        full_checks+=1

result={"status":"PASS","theorem":"R102 exact eta=1/2 plateau and tie atlas",
"method":"Python fractions exact rationals; direct six-term F; independent full search for q<=30",
"sample_parameter_pairs":len(samples),"sampled_port_budgets":list(budgets),
"core_comparisons":compare_count,"plateau_comparisons":plateau_count,
"unoriented_integer_directions_q_le_30":len(vecs),
"exhaustive_probe_parameter_pairs":len(probe),
"exhaustive_probe_port_budgets":[11,16,17,21,26,27,30],
"exhaustive_probe_compared_cases":full_checks,
"universal_scope":"not established by this program; theorem uses R98/R99 and direct inequalities",
"r99_dependency":"author proof, not independently reviewed"}
print(json.dumps(result,indent=2,ensure_ascii=False))
