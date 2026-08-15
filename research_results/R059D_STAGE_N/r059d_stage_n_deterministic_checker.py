#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent; C=[]
def ck(x,s):
 C.append(s)
 if not x: raise AssertionError(s)
def ld(n): return json.loads((R/n).read_text())
S=ld("R059D_STAGE_N_SCALAR_UP_DOWN_COLLAPSE_PROTOCOL.json"); H=ld("R059D_STAGE_N_SYMMETRIC_PRECOLLAPSE_HALF_STATE_DERIVATION.json"); E=ld("R059D_STAGE_N_DIRECT_INTEGER_VS_HALF_STATE_EQUIVALENCE.json"); D=ld("R059D_STAGE_N_D6_TRANSFER_EMERGENCE_AUDIT.json"); G=ld("R059D_STAGE_N_GENERAL_COUPLED_BOOLEAN_COLLAPSE_ALGEBRA.json"); P=ld("R059D_STAGE_N_POST_CREDIT_FINITE_DIFFERENCE_ALGEBRA.json"); K=ld("R059D_STAGE_N_LARGE_BACKGROUND_COVARIANCE_REGISTRY.json"); X=ld("R059D_STAGE_N_TRIVIALITY_TARGET_LEAKAGE_LEDGER.json")
ck(S["normal_form"]["idempotence"]=="b^2=b","bool-idem"); ck(S["no_local_selector_assumed"],"no-selector"); ck(H["native_packet_quantity_claim"] is False,"half-not-native"); ck(D["classification"]=="ESTABLISHED_ONLY_WITH_ADDITIONAL_MINIMALITY_ASSUMPTION","d6-qualified"); ck(G["set_valued_rule"].startswith("multiple exact"),"set-valued"); ck(P["no_arbitrary_reward_weights"],"no-weights")
for q in X["gates"]:
 ck(q["status"]=="PASS" or (q["id"]=="STAGE_J_K_L_M_ARTIFACTS_IMMUTABLE" and q["status"]=="PASS_BY_GITHUB_COMPARE_PRE_MANIFEST"),"gate:"+q["id"])
# scalar exact/covariance
for L in range(-5,5):
 for U in range(L+1,7):
  for n in range(L+1,U):
   for b in (0,1):
    z=L+(U-L)*b; r=n-z
    ck(z==(L if not b else U),f"s:{L}:{U}:{n}:{b}")
    for c in (-7,0,3): ck((L+c)+(U-L)*b==z+c and n+c-((L+c)+(U-L)*b)==r,f"t:{L}:{U}:{n}:{b}:{c}")
    for a in (1,2,5): ck(a*L+(a*U-a*L)*b==a*z,f"k:{L}:{U}:{n}:{b}:{a}")
    bp=1-b; ck(-U+((-L)-(-U))*bp==-z,f"i:{L}:{U}:{n}:{b}")
for L,U in [(-1,0),(0,1),(-3,2)]:
 n=F(L+U,2)
 for b in (0,1): ck(n-(F(L)+(U-L)*b)==((-F(U-L,2)) if b else F(U-L,2)),f"m:{L}:{U}:{b}")
ck(5-(4+5*0)==1 and 5-(4+5*1)==-4,"5-res"); ck(2-5*0==2 and 2-5*1==-3,"nonmid")
# mandatory sheet/direct/half
direct={(a,1,c) for a,c in product((-1,0),repeat=2) if a+1+c==0}; ck(direct=={(-1,1,0),(0,1,-1)},"direct2"); ck(sum((100,1,0))==101,"off-sheet")
ck({(100+a,1,c) for a,_,c in direct}=={(99,1,0),(100,1,-1)},"ends")
h=F(-1,2); ck(2*h+1==0,"half"); 
for a in [F(-3,2),F(-1),F(-1,2),F(0),F(2,3)]: ck(a+1+(-1-a)==0,f"no-ex:{a}")
bits={(a,c) for a,c in product((0,1),repeat=2) if a+c==1}; ck(bits=={(0,1),(1,0)},"compbits"); ck({(-1+a,1,-1+c) for a,c in bits}==direct,"bijection")
for b in (0,1): ck((-b,1,-(1-b))==(-1+(1-b),1,-1+b) and sum((-b,1,-(1-b)))==0,f"onebit:{b}")
# derive six from ordered transfers, then compare names
B=[(1,0,0),(0,1,0),(0,0,1)]; sub=lambda a,b:tuple(x-y for x,y in zip(a,b)); T={sub(B[i],B[j]) for i in range(3) for j in range(3) if i!=j}
ck(len(T)==6 and all(sum(v)==0 for v in T),"six-derived"); ck(all(tuple(-x for x in v) in T for v in T),"inv")
u=(1,-1,0);v=(0,1,-1);w=(-1,0,1); ck(T=={u,tuple(-x for x in u),v,tuple(-x for x in v),w,tuple(-x for x in w)},"d6-eq")
for p in [(0,1,2),(1,2,0),(2,0,1),(0,2,1),(2,1,0),(1,0,2)]: ck({tuple(x[p[j]] for j in range(3)) for x in T}==T,f"perm:{p}")
for t in range(-32,33): ck(t+1+(-1-t)==0,f"inf:{t}")
# assumption removals
ck(len({(a,1,c) for a,c in product((-1,0),repeat=2)})==4,"A1")
ck({(a,r,c) for a,c in product((-1,0),repeat=2) for r in (1,2) if a+r+c==0}=={(-1,1,0),(0,1,-1),(-1,2,-1)},"A2")
ck(all(sum(x)==0 for x in {(F(k,8),1,-1-F(k,8)) for k in range(-8,1)}),"A3")
ck(len({(t,1,-1-t) for t in range(-50,51)})==101,"A5A6"); ck({(a,1,c) for a,c in product((-1,0),repeat=2) if a+1+c==0}==direct,"A6-red"); ck((h,1,h) not in direct,"A7")
# Boolean solution sets
def cls(a): return "INCONSISTENT_CONSTRAINT_SET" if not a else ("UNIQUE_COLLAPSE_ASSIGNMENT" if len(a)==1 else "MULTIBRANCH_ADMISSIBLE")
tests=[(lambda b:b[0]+b[1]==1,{(0,1),(1,0)},"MULTIBRANCH_ADMISSIBLE"),(lambda b:b[0]+b[1]==0,{(0,0)},"UNIQUE_COLLAPSE_ASSIGNMENT"),(lambda b:b[0]+b[1]==2,{(1,1)},"UNIQUE_COLLAPSE_ASSIGNMENT"),(lambda b:b[0]+b[1]==3,set(),"INCONSISTENT_CONSTRAINT_SET")]
for j,(f,e,c) in enumerate(tests):
 a={b for b in product((0,1),repeat=2) if f(b)}; ck(a==e and cls(a)==c,f"B:{j}")
# multilinear finite-difference theorem
def ev(p,b): return sum(c*mathprod([b[i] for i in S]) for S,c in p.items())
def mathprod(a):
 z=1
 for x in a:z*=x
 return z
def dp(p,T):
 T=set(T);o={}
 for S,c in p.items():
  if T<=set(S):
   q=frozenset(set(S)-T);o[q]=o.get(q,0)+c
 return {q:c for q,c in o.items() if c}
Q={frozenset():1,frozenset({0}):-1,frozenset({1}):-1,frozenset({0,1}):2}
for b in product((0,1),repeat=2): ck(ev(Q,b)==(b[0]+b[1]-1)**2,f"Q:{b}")
ck(dp(Q,{0})=={frozenset():-1,frozenset({1}):2},"Dx"); ck(dp(Q,{1})=={frozenset():-1,frozenset({0}):2},"Dz"); ck(dp(Q,{0,1})=={frozenset():2},"Dxz")
for m in range(1,5):
 ss=[frozenset(S) for r in range(m+1) for S in combinations(range(m),r)]
 for seed in range(1,7):
  p={S:((sum(S)+1)*(seed+1)+3*len(S))%7-3 for S in ss};p={S:c for S,c in p.items() if c}
  for r in range(1,m+1):
   for T0 in combinations(range(m),r):
    q=dp(p,T0)
    for b in product((0,1),repeat=m):
     z=0
     for vals in product((0,1),repeat=r):
      bb=list(b)
      for i,a in zip(T0,vals):bb[i]=a
      z+=(-1)**(r-sum(vals))*ev(p,bb)
     ck(z==ev(q,b),f"D:{m}:{seed}:{T0}:{b}")
    ck(ev(q,[0]*m)==p.get(frozenset(T0),0),f"M:{m}:{seed}:{T0}")
# straightness rank
a=(-1,1,0);b=(0,1,-1)
def rank(vs):
 x=vs[0]
 for y in vs[1:]:
  if any(x[i]*y[j]-x[j]*y[i] for i,j in combinations(range(3),2)): return 2
 return 1
ck(rank([a,a])==1 and rank([b,b])==1 and rank([a,b])==2,"straight")
# huge background
for s in K["K_registry"]:
 k=int(s); p=(k-1,1,0);q=(k,1,-1); ck(sum(p)==k and sum(q)==k and (p[0]-k,p[1],p[2])==(-1,1,0) and (q[0]-k,q[1],q[2])==(0,1,-1),f"K:{k}")
# stored theorem flags
ck(E["mandatory_case"]["set_equality"] is True,"stored-eq");ck(G["freeze"]=="BRC_CONSTRAINT_SOLUTION_SET_ALGEBRA_ESTABLISHED","stored-B");ck(P["freeze"]=="POST_CREDIT_DISCRETE_DIFFERENCE_ALGEBRA_ESTABLISHED","stored-post")
dig=hashlib.sha256("\n".join(C).encode()).hexdigest()
out={"schema":"R059D_STAGE_N_DETERMINISTIC_CHECKER_OUTPUT_V1","researcher_id":"EM-R059D-9C6B2A","taskbook_source":"0ded98e376b649cbe41e47e18ea23c8c2daf59ca","frozen_parent":"d6cfcb3435deac50901581cd4fa82e6b3cf588d3","status":"PASS","checks_total":len(C),"checks_passed":len(C),"checks_failed":0,"checks_digest_sha256":dig,"large_background_method":"closed-form exact integer arithmetic only","boolean_enumeration_role":"tiny oracle only; symbolic normal forms and finite-difference formulas are the theorem mechanism","parent_immutability":"PASS_BY_GITHUB_COMPARE_PRE_MANIFEST"}
(R/"R059D_STAGE_N_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n");print(json.dumps(out,indent=2))
