#!/usr/bin/env python3
"""R246 exact rational counterexample: the R245 two-mode error is NOT parameter monotone.
All decisions use Python Fraction and integer comparisons; no floating-point decisions.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34
"""
from fractions import Fraction as F
from math import lcm
import hashlib,json,sys
sys.set_int_max_str_digits(1000000)
W=(144,576,1440,4320,17280,86400,518400)
PARAMS=(F(39,100),F(2,5),F(41,100))
EVENT=126
BISECTIONS=96

def parameters(s):
    t=(1691*s-2615)/(2615*s-3539)
    a=(F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t)
    b=(F(13,60),)+tuple(F(5,18)*abs(F(1,2)-v) for v in a[1:])
    pi=tuple(v/(1-x) for v,x in zip(b,a))
    assert all(x>0 for x in b) and all(0<x<1 for x in a) and sum(pi)==1
    Z=sum((v/(1-x)**2 for x,v in zip(a,b)),F(0))
    rho=tuple(v/(1-x)**2/Z for x,v in zip(a,b))
    return a,b,pi,Z,rho

def ids(mask):return [0]+[j for j in range(1,7) if mask&(1<<(j-1))]

def secular(x,a,b,ix):return sum((b[i]/(x-a[i]) for i in ix),F(0))-1

def bounds_root(a,b,mask):
    ix=ids(mask);lo=max(a[i] for i in ix);hi=F(1)
    assert secular(hi,a,b,ix)<0
    for _ in range(BISECTIONS):
        mid=(lo+hi)/2
        if secular(mid,a,b,ix)>0:lo=mid
        else:hi=mid
    assert 0<lo<hi<1 and secular(lo,a,b,ix)>0 and secular(hi,a,b,ix)<0
    return lo,hi

def amplitude_bounds(lo,hi,a,b,Z,mask):
    ix=ids(mask)
    def S(x):return sum((b[i]/((1-a[i])*(x-a[i])) for i in ix),F(0))
    def Q(x):return sum((b[i]/(x-a[i])**2 for i in ix),F(0))
    w=W[mask.bit_count()]
    return w*S(hi)**2/(Z*Q(lo)),w*S(lo)**2/(Z*Q(hi))

def phi_exact(s,n):
    a,b,pi,Z,rho=parameters(s)
    P=[[a[i]*(i==j)+(1-a[i])*pi[j] for j in range(7)] for i in range(7)]
    d=lcm(*(v.denominator for row in P for v in row))
    M=[[int(v*d) for v in row] for row in P]
    q=lcm(*(v.denominator for v in rho))
    r=[int(v*q) for v in rho]
    k=n-1
    total=0
    for mask in range(63):
        ix=ids(mask); v=[1]*len(ix)
        for _ in range(k):
            v=[sum(M[i][j]*v[c] for c,j in enumerate(ix)) for i in ix]
        total+=W[mask.bit_count()]*sum(r[i]*v[c] for c,i in enumerate(ix))
    return F(total,q*d**k), (a,b,Z)

def phi_rank_one_exact(s,n):
    """Independent exact rank-one factorization; O(n sum_D |D|) integer operations."""
    a,b,pi,Z,rho=parameters(s)
    C=lcm(*(x.denominator for x in a))
    Q=lcm(*(x.denominator for x in pi))
    d=C*Q
    diag=[int(d*x) for x in a]
    U=[int(C*(1-x)) for x in a]
    V=[int(Q*x) for x in pi]
    rden=lcm(*(v.denominator for v in rho))
    rn=[int(v*rden) for v in rho]
    total=0
    for mask in range(63):
        ix=ids(mask)
        v=[1]*len(ix)
        for _ in range(n-1):
            dot=sum(V[j]*v[jj] for jj,j in enumerate(ix))
            v=[diag[i]*v[jj]+U[i]*dot for jj,i in enumerate(ix)]
        total+=W[mask.bit_count()]*sum(rn[i]*v[jj] for jj,i in enumerate(ix))
    return F(total,rden*d**(n-1))

def cert(s,n):
    phi,(a,b,Z)=phi_exact(s,n)
    assert phi == phi_rank_one_exact(s,n)
    root={};amps={};k=n-1
    for mask in (59,55):
        l,u=bounds_root(a,b,mask)
        al,au=amplitude_bounds(l,u,a,b,Z,mask)
        assert 0<al<au
        root[str(mask)]=(l,u);amps[str(mask)]=(al,au)
    assert root['55'][1]<root['59'][0]
    lower=sum(amps[str(mask)][0]*root[str(mask)][0]**k for mask in (59,55))
    upper=sum(amps[str(mask)][1]*root[str(mask)][1]**k for mask in (59,55))
    assert 0<lower<upper
    E_lo=phi/upper-1;E_hi=phi/lower-1
    assert E_lo<E_hi
    return dict(s=str(s),n=n,phi=phi,X_lower=lower,X_upper=upper,E_lower=E_lo,E_upper=E_hi,roots=root,amplitudes=amps)

def digest_margin(v):
    assert v>0
    d=(str(v.numerator)+'/'+str(v.denominator)).encode('utf8')
    return dict(sign='positive',numerator_bits=v.numerator.bit_length(),denominator_bits=v.denominator.bit_length(),sha256=hashlib.sha256(d).hexdigest())

def main():
    rows=[cert(s,EVENT) for s in PARAMS]
    left,mid,right=rows
    margins={
        'E_126(2/5)>E_126(39/100)':mid['phi']*left['X_lower']-left['phi']*mid['X_upper'],
        'E_126(2/5)>E_126(41/100)':mid['phi']*right['X_lower']-right['phi']*mid['X_upper']
    }
    assert all(v>0 for v in margins.values()),[(k,float(v)) for k,v in margins.items()]
    output={'schema':'EM_R246_TWO_MODE_PARAMETER_NONMONOTONICITY_V1',
         'frozen_scientific_commit':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
         'model':'R245 seven-source reversible sticky-reset; 63 proper masks; W fixed; two Perron modes masks 59/55',
         'result':'INTERIOR_STRICT_MAXIMUM_WITNESS; GLOBAL_NONDECREASING_AND_NONINCREASING_BOTH_FALSE',
         'event_n':EVENT,'root_bisections':BISECTIONS,'exact_integer_matrix_propagation':True,'rank_one_factorization_exactly_matches_dense_at_all_anchors':True,
         'rank_one_scalar_multiplications_per_time_step_max':2*249,'dense_scalar_multiplications_per_time_step':1071,
         'comparison_margins':{k:digest_margin(v) for k,v in margins.items()},
         'parameters':[
             {'s':r['s'],'E_certified_bracket':[
                 format(float(r['E_lower']),'.16g'),format(float(r['E_upper']),'.16g')],
              'Phi_n_numerator_bits':r['phi'].numerator.bit_length(),
              'Phi_n_denominator_bits':r['phi'].denominator.bit_length(),
              'root_bounds':{mask:[str(root[0]),str(root[1])] for mask,root in r['roots'].items()}}
             for r in rows],
         'status':'PASS', 'review':'NOT_REVIEWED','native_BRC':'NOT_EXECUTED'}
    print(json.dumps(output,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()
