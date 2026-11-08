#!/usr/bin/env python3
"""PREFIX-604: exact O7 factorization and strictly-positive 96-port collisions.
Native source: frozen PREFIX565; weighted phase deformation as in PREFIX601.
"""
import io,json
from contextlib import redirect_stdout
from collections import defaultdict
from fractions import Fraction as F
with redirect_stdout(io.StringIO()):
 from PREFIX565_positive_marginal_certificate import PHASES,NEXT,TARGET,ROOTS,edge,SCIENCE_PIN
 from PREFIX603_R6_internal_branch_observer_certificate import order,position,ei,pairs,weighted_kernel,left_null_basis
assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'

def reward_from_target(q,root):
    _a,prev,cur=PHASES[q]
    def sg(c,k):return (1 if c>0 else -1) if abs(c)==k else 0
    w=[]
    for k in range(1,7):
        left,right,z=sg(prev,k),sg(cur,k),root[k-1]
        v=abs(left)+abs(right)-abs(right-z)+abs(left-z)
        assert v in (0,2)
        w.append(v//2)
    return tuple(w)

for root in ROOTS:
 for p in range(48):
  for slot in range(3):
   q=NEXT[p][slot]
   assert PHASES[q][1]==PHASES[p][2]
   for b in (0,1):
    for newbit in (0,1):
     nxt,w=edge(2*p+b,(slot,newbit),root)
     assert nxt==2*q+newbit
     assert w[:6]==reward_from_target(q,root)
     assert w[6]==int(b==newbit==1 and q==TARGET)

def observer(pi,t,root):
    out=defaultdict(F)
    for p in range(48):
     e=ei[(PHASES[p][0],abs(PHASES[p][2]))];s=1+2*t[e]
     for b in (0,1):
      if pi[2*p+b]==0:continue
      for slot in range(3):
       prob=[F(1),t[e],t[e]][slot]/(2*s)
       if not prob:continue
       for newbit in (0,1):
        nextport,w=edge(2*p+b,(slot,newbit),root)
        out[(nextport,w)]+=pi[2*p+b]*prob
    return dict(out)

def phase_output(piphase,t):
    P,C,s=weighted_kernel(t)
    src=[piphase[p] for p in order]
    z=[sum(src[i]*P[i][j] for i in range(48)) for j in range(48)]
    return {order[j]:z[j] for j in range(48)}

def factor_law(piphase,t,root,beta=F(1,2)):
    z=phase_output(piphase,t)
    out={}
    for q in range(48):
      for newbit in (0,1):
        w=reward_from_target(q,root)
        if q==TARGET and newbit==1:
          for gate,x in ((0,1-beta),(1,beta)):
            val=z[q]*x/2
            if val:out[(2*q+newbit,w+(gate,))]=val
        else:
          val=z[q]/2
          if val:out[(2*q+newbit,w+(0,))]=val
    return out

def check_case(t,k):
    P,C,s=weighted_kernel(t);L=left_null_basis(t,s)
    assert len(L)==2*k
    ell=L[0] if L else None
    eps=F(1,96*(max(abs(v) for v in ell)+1)) if ell else F(0)
    a=[F(1,48)+eps*(ell[i] if ell else 0) for i in range(48)]
    b=[F(1,48)-eps*(ell[i] if ell else 0) for i in range(48)]
    assert min(a)>0 and min(b)>0 and sum(a)==sum(b)==1
    aa=[F(0)]*48; bb=[F(0)]*48
    for i,p in enumerate(order):aa[p]=a[i];bb[p]=b[i]
    mu=[x for p in range(48) for x in (aa[p]/2,aa[p]/2)]
    nu=[x for p in range(48) for x in (bb[p]/2,bb[p]/2)]
    assert min(mu)>0 and min(nu)>0 and sum(mu)==sum(nu)==1
    for root in ROOTS:
        x=observer(mu,t,root);y=observer(nu,t,root)
        assert x==factor_law(aa,t,root)
        assert y==factor_law(bb,t,root)
        if k:assert x==y
    return {'critical_pairs':k,'full_o7_collision':bool(k),'strictly_positive_both_bits':True,
            'nine_roots_exact_factor_checked':True,'epsilon':str(eps), 'source_phase_laws_differ':bool(k)}

one=[F(1)]*12
cases=[]
for k in (0,1,2,6):
  t=one.copy()
  for e,f in pairs[:k]:t[e]=t[f]=F(1,2)
  cases.append(check_case(t,k))
print(json.dumps({'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,'native_target_reward_checks':48*3*9*4,'case_results':cases,
  'claim':'For fixed independent source bit B~Bernoulli(beta), full original six-axis BRC reward+gate+next original port factors through terminal phase law; 2k critical phase directions remain invisible even with O7'},indent=2))
