#!/usr/bin/env python3
"""Exact tests of signed-dependent support choices and Walsh-ratio transfer."""
from itertools import combinations, product
from fractions import Fraction as F
import json
AX=range(6)
S=[frozenset(c) for c in combinations(AX,2)]
E=[(A,B) for A in S for B in S if len(A&B)==1]
assert len(E)==120
bits=list(product((-1,1),repeat=3))

def lift(A,B):
    order=sorted(A|B)
    return [{a:s[i] for i,a in enumerate(order)} for s in bits]

def signmask(x,order,mask):
    z=1
    for i,a in enumerate(order):
        if mask>>i&1: z*=x[a]
    return z

def trans(A,B,C,x,p):
    old=next(iter(A-B));new=next(iter(C-B));t=C==A^B
    if t:
        theta=8*p/(1+7*p)
        opts=[(x[old],(1+theta)/2),(-x[old],(1-theta)/2)]
    else:opts=[(-1,F(1,2)),(1,F(1,2))]
    return [(dict({a:x[a] for a in B},**{})|{new:v},w) for v,w in opts if w]

def pull(A,B,C,mask,p):
    init=sorted(A|B); final=sorted(B|C)
    old=next(iter(A-B));new=next(iter(C-B))
    chosen={a for j,a in enumerate(final) if mask>>j&1}
    if C!=A^B and new in chosen:return F(0),0
    theta=8*p/(1+7*p)
    coeff=theta if C==A^B and new in chosen else F(1)
    if C!=A^B:chosen.remove(new) if new in chosen else None
    return coeff,sum(1<<j for j,a in enumerate(init) if a in chosen)

def verify(A,B,C,p):
    isforced=C==A^B
    if p==1 and not isforced:return 0
    init=sorted(A|B);fin=sorted(B|C);old=next(iter(A-B));b=next(iter(B))
    oldbit=1<<init.index(old); bbit=1<<fin.index(b)
    old_co=F(1,4) if isforced else F(-1,4)
    checks=0
    for q0 in range(8):
      for q1 in range(8):
        coef={}
        for fmask,fc in ((q1,F(1,2)),(q1^bbit,F(1,4))):
          coefk,ib=pull(A,B,C,fmask,p)
          for sm,sc in ((q0,F(1,2)),(q0^oldbit,old_co)):
            z=ib^sm
            coef[z]=coef.get(z,F(0))+fc*coefk*sc
        for x in lift(A,B):
          direct=F(0)
          ell0=(F(2)+ (x[old] if isforced else -x[old]))/4
          for y,w in trans(A,B,C,x,p):
            ell1=(F(2)+y[b])/4
            direct+=ell0*ell1*w*signmask(x,init,q0)*signmask(y,fin,q1)
          via=sum((coef[k]*signmask(x,init,k) for k in coef),F(0))
          assert direct==via,(A,B,C,p,q0,q1,x,direct,via)
          checks+=1
    return checks

def main():
    checked=0;words=0
    for p in (F(0),F(1,2),F(1)):
      for A,B in E:
        for C in S:
          if len(B&C)!=1:continue
          if p==1 and C!=A^B:continue
          checked+=verify(A,B,C,p);words+=1
    A=frozenset((0,1));B=frozenset((1,2));C=A^B;old=0
    for m in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
      plus=(1+m)/2;minus=(1-m)/2
      den=plus*F(3,4)+minus*F(1,4)
      num=plus*F(3,4)-minus*F(1,4)
      assert den>0 and num/den==(1+2*m)/(2+m)
      for p in (F(0),F(1,2),F(1)):
        theta=8*p/(1+7*p)
        init=lift(A,B)
        dist={tuple(sorted(x.items())):(plus if x[old]==1 else minus)/4 for x in init}
        assert sum(dist.values())==1
        expected=sum(w*F(2+x[old],4) for x,w in [(dict(k),v) for k,v in dist.items()])
        numerator=sum(w*F(2+x[old],4)*sum(prob*y[old] for y,prob in trans(A,B,C,x,p)) for x,w in [(dict(k),v) for k,v in dist.items()])
        assert expected==den and numerator/den==theta*(1+2*m)/(2+m)
    print(json.dumps({'status':'PASS','unsigned_directed_supports':120,'signed_lifts_each':8,
       'conditioned_two_gate_words':words,'exact_joint_walsh_equalities':checked,
       'parameter_values':['0','1/2','1'],'signed_dependence_example':'posterior initial m = (1+2m)/(2+m)',
       'forced_final_sign_p_half_at_uniform_prior':'4/9',
       'native_event_permission':False},indent=2,sort_keys=True))
if __name__=='__main__':main()
