#!/usr/bin/env python3
"""PREFIX-662, standalone exact low-count BRC certificate; frozen pin f42f2906d77f24085c123f3ccfe9667d41caa96d."""
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json

N, D, WIDTH = 189, 2**18, F(1, 2**21)
checks = 0

def ck(assertion, label):
    global checks
    assert assertion, label
    checks += 1

@lru_cache(None)
def inside(n, k, a):
    return 40*(n+1)*comb(n,k)*a**k*(D-a)**(n-k) > D**n

@lru_cache(None)
def wide(n, k):
    if k > n//2:
        return wide(n,n-k)
    middle = k*D//n
    ck(inside(n,k,middle), ('central',n,k))
    if k==0:
        ll=lh=0
    else:
        low, high = 0, middle
        while high-low>1:
            m=(low+high)//2
            if inside(n,k,m):high=m
            else:low=m
        ll,lh=low,high
    low,high=middle,D
    while high-low>1:
        m=(low+high)//2
        if inside(n,k,m):low=m
        else:high=m
    rl,rh=low,high
    if 4*(rl-lh)>D: return True
    if 4*(rh-ll)<D: return False
    raise AssertionError(('ambiguous',n,k))

def certificate():
    a=[1,0,0]; rows=[tuple(a)]
    for n in range(1,N):
        a=[((a[k] if k<=n-1 else 0) + (a[k-1] if 0<k<=n else 0))
           if k<=n else 0 for k in range(3)]
        a=[v if wide(n,k) else 0 for k,v in enumerate(a) if k<=n]+[0]*max(0,2-n)
        rows.append(tuple(a))
    ck(len(rows)==N, '189 low-degree rows')
    ck(all(rows[n][k]==comb(n,k) for n in range(2,25) for k in range(3)), '24 full survivor layers')
    ck(rows[25]==(0,25,300) and rows[33]==(0,25,500) and rows[34]==(0,0,525) and rows[41]==(0,0,525) and rows[42]==(0,0,0), 'exact low-count support')
    ck(all(rows[n]==(0,0,0) for n in range(42,N)), 'later first three coefficients vanish')
    ck(all(rows[n][1]-n*rows[n][0]==(25 if 25<=n<=33 else 0) for n in range(1,N)), 'edge derivative support')
    d2=[]
    for n in range(2,N):
        f0=F(rows[n][0]);f1=F(rows[n][1],n);f2=F(rows[n][2],comb(n,2))
        d2.append(f2-2*f1+f0)
    A=sum(n*(n-1)*abs(d2[n-2]) for n in range(2,N))
    C=sum((n+1)*n*(n-1)*abs(d2[n-2]) for n in range(2,N))
    B=2*sum(n*(n-1)*(n-2) for n in range(3,N))
    E=2*sum((n+1)*n*(n-1)*(n-2) for n in range(3,N))
    ck((A,C,B,E)==(13800,485400,617937012,93926425824), 'exact Bernstein second-difference budgets')
    M2=A+B*WIDTH
    H2=C+E*WIDTH
    M1=225+A*WIDTH+F(B,2)*WIDTH**2
    W2=2*H2+2*M1*M1+756*M2
    K=576*W2+24*M2
    loss=WIDTH*K
    ck(loss < 3246, 'new strip variation strictly below 3246')
    ck(-76650+loss < -73404, 'strict uniform derivative less than -73404')
    ck(WIDTH / F(1,2**30) == 512, 'exact strip-area expansion')
    result={
      'schema':'EM_PREFIX662_R6_LOW_COUNT_BERNSTEIN_STRIP_CERTIFICATE_V1',
      'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'domain':{'p':['0','1/2097152'],'z':['607/4096','609/4096'],'q':['12','24']},
      'low_count_support_last_n':41,
      'moment_second_derivative_coefficients':{'mu_A':str(A),'H_C':str(C),'mu_B':str(B),'H_E':str(E)},
      'mu_p0_uniform_upper':'225',
      'new_gradient_loss_exact':str(loss),
      'new_gradient_loss_strict':'<3246',
      'gradient_strict':'d_p V_q < -73404',
      'maximizer':'(0,z_star(q)), unique on new strip',
      'stability':'M_q-V_q(p,z) >= 73404*p+6400000*(z-z_star(q))^2',
      'area_gain_over_PREFIX661':'512',
      'predecessor_assumptions':['PREFIX660 strict z concavity','PREFIX661 exact p=0 gradient on z band'],
      'verification':'integer and Fraction arithmetic, frozen predicate for k<=2, analytic Bernstein tail',
      'status':'AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED',
      'checks_passed':checks,'result':'ALL_CHECKS_PASS'}
    return result

if __name__=='__main__':
    result=certificate()
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS',checks)
