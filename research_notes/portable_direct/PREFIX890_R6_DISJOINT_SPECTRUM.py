#!/usr/bin/env python3
"""PREFIX-890: exact additive BRC collision-spectrum checks, Python 3 standard library."""
from collections import Counter, defaultdict
from math import gcd, lcm
import json

def zero_zero(p,q1,q2):
    n=1<<p; L=lcm(q1,q2); t,r=divmod(n,L)
    return r*(t*(t+1)//2)+(L-r)*(t*(t-1)//2)

def ones_below(i,t):
    unit=1<<i; block=unit<<1
    return unit*(t//block)+max(0,(t%block)-unit)

def zero_flip(p,q1,q2):
    if gcd(q1,q2)>1: return 0
    n=1<<p; K=(n-1)//q1; inv=pow(q1,-1,q2)
    total=0
    for i in range(p):
        r=((1<<i)*inv)%q2
        for sign,bit in [(1,1),(-1,0)]:
            rem=r if sign==1 else (-r)%q2
            # k in 1..K with congruence k=rem mod q2
            k=rem or q2
            while k<=K:
                a=k*q1
                ones=n//2-ones_below(i,a)
                zeros=n-a-ones
                total+=ones if bit==1 else zeros
                k+=q2
    return total*2

def axis(p,q):
    return (1<<(p-1))*sum((p-h) for h in range(1,p)
      if ((1<<h)-1)%q==0 or ((1<<h)+1)%q==0)

def direct(p,q1,q2):
    n=1<<p; fibers=defaultdict(list)
    for x in range(n):
        fibers[(x%q1,x%q2)].append(('Z',x,x,-1))
        for i in range(p):
            fibers[(x%q1,(x^(1<<i))%q2)].append(('F',x,x^(1<<i),i))
    counts=Counter()
    for family in fibers.values():
        for i,a in enumerate(family):
            for b in family[i+1:]:
                if a[0]=='Z' and b[0]=='Z': key='ZZ'
                elif a[0]=='Z' or b[0]=='Z': key='ZF'
                elif a[1]==b[1]: key='FF_same_start'
                elif a[2]==b[2]: key='FF_same_end'
                else: key='FF_residual'
                counts[key]+=1
    return dict(counts)

def exact(p,q1,q2):
    zz=zero_zero(p,q1,q2)
    zf=zero_flip(p,q1,q2)
    ax1=axis(p,q1)
    ax2=axis(p,q2)
    return {'ZZ':zz,'ZF':zf,'FF_same_end':ax1,'FF_same_start':ax2,'additive_lower_bound':zz+zf+ax1+ax2}

diagonal_extremal=[]
for p in range(2,11):
    q=(1<<p)-1
    d=direct(p,q,q)
    c=sum(d.values())
    expected=5 if p==2 else 1
    assert c==expected, (p,c,d)
    diagonal_extremal.append({'p':p,'q':q,'C':c})

small=0
for p in range(2,9):
  for q1 in range(3,min(25,1<<p),2):
    for q2 in range(3,min(25,1<<p),2):
      d=direct(p,q1,q2); e=exact(p,q1,q2)
      for k in ('ZZ','ZF','FF_same_end','FF_same_start'):
        assert d.get(k,0)==e[k], (p,q1,q2,k,d,e)
      assert sum(d.values())>=e['additive_lower_bound']
      small+=1

cases=[(524287,524285,1260570120266),
       (500383,522777,61029441402),
       (523001,523003,502527821442),
       (262143,524287,1329274396737),
       (524287,524287,568927306772480)]
rows=[]
for q1,q2,C in cases:
  v=exact(32,q1,q2)
  v.update({'q1':q1,'q2':q2,'inherited_C_from_PREFIX884':C,'FF_residual_derived':C-v['additive_lower_bound'],
           'new_bound_fraction':f"{v['additive_lower_bound']}/{C}"})
  assert v['FF_residual_derived']>=0,v
  rows.append(v)
results={'title':'PREFIX-890 exact disjoint collision spectrum','model':'p-bit states; named zero-or-single-XOR trajectories; positive odd q1,q2>1; ordered residue pair observer',
         'diagonal_extremal_exact_small_checks':diagonal_extremal,
         'diagonal_extremal_theorem':'for p>=3, q1=q2=2^p-1 implies C=1; p=2 implies C=5',
         'small_parameter_exhaustive_cases':small,'small_p_range':[2,8],
         'small_q_ranges':'odd 3..min(23,2^p-1), both ports',
         'small_checks':'independent direct pair classification vs all four exact formulas, zero mismatches',
         'large_case_C_source':'PREFIX-884 author-reported full C at p=32; residual subtraction is conditional on its declared values',
         'large_cases':rows}
print(json.dumps(results,ensure_ascii=False,indent=2))
