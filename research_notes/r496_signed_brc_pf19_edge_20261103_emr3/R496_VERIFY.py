#!/usr/bin/env python3
"""R496: exact signed BRC s=3 m=19 Toeplitz determinant certificate under frozen R462 input.
Run: python3 R496_VERIFY.py > R496_EVIDENCE.json
Python standard-library exact int and Fraction arithmetic only.
"""
from fractions import Fraction as Q
from math import comb, factorial, gcd, lcm
from functools import reduce
import json
RANK=19
PIN='18783e01e3646c72b7aab3b16d3f565e83e6446f'

def B(n,j): return comb(n,j) if 0<=j<=n else 0
def C(k): return comb(2*k,k)//(k+1)
def H(k,t):
    r=2*k+1
    if t<2 or t>r:return 0
    return B(r+t,2*t)*sum(B(r-t,q)*(B(2*t,r-2*q)-B(2*t,r-2*q-1)) for q in range(r-t+1))
def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a
def add(a,b):
    z=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return trim(z)
def mul(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:z[i+j]+=x*y
    return trim(z)
def prod(xs):
    z=[Q(1)]
    for x in xs:z=mul(z,x)
    return z
def ev(a,k):
    z=Q(0)
    for v in reversed(a):z=z*k+v
    return z
def p(t):
    z=[Q(0)]
    for q in range((t-1)//2+1):
        factors=[]
        for h in range(q):factors.extend(([-h,1],[1-h,1]))
        for e in range(2-t,t+2):
            if e not in range(1-2*q,1):factors.append([e,2])
        term=prod(factors)
        z=add(z,[Q(B(t-1,2*q)*4**q,factorial(2*t))*v for v in term])
    return z
def exact_div(a,b):
    assert len(a)>=len(b) and b[-1]
    z=a[:];q=[Q(0)]*(len(a)-len(b)+1)
    for i in range(len(q)-1,-1,-1):
        v=z[i+len(b)-1]/b[-1];q[i]=v
        for j,w in enumerate(b):z[i+j]-=v*w
    assert all(v==0 for v in z)
    return trim(q)
def bareiss(a):
    a=[row[:] for row in a];n=len(a);last=1;sign=1
    for i in range(n-1):
        if a[i][i]==0:
            j=next((j for j in range(i+1,n) if a[j][i]),None)
            if j is None:return 0
            a[i],a[j]=a[j],a[i];sign=-sign
        pivot=a[i][i]
        for j in range(i+1,n):
            for h in range(i+1,n):
                val=pivot*a[j][h]-a[j][i]*a[i][h]
                assert val%last==0
                a[j][h]=val//last
            a[j][i]=0
        last=pivot
    return sign*a[-1][-1]

ps={t:p(t) for t in range(2,RANK+3)}
f=[[Q(1)]]
for m in range(1,RANK+1):
    z=[Q(0)]
    for ell in range(1,m+1):
        term=prod([ps[ell+2]]+[ps[2]]*(ell-1)+[f[m-ell]])
        z=add(z,[(-1)**(ell-1)*v for v in term])
    assert len(z)==6*m+1,(m,len(z))
    f.append(z)
fac=prod([[0,1]]*RANK+[[1,1]]*RANK+[[2,1]]+[[1,2]]*RANK+[[3,2]]*RANK)
assert len(fac)==4*RANK+2
quot=exact_div(f[RANK],fac)
assert len(quot)==2*RANK
L=reduce(lcm,(v.denominator for v in quot))
P=[int(v*L) for v in quot]
g=reduce(gcd,(abs(v) for v in P))
assert g>0 and L%g==0
P=[v//g for v in P];den=L//g
assert len(P)==38 and len(f[RANK])==115
assert f[RANK]==mul(fac,[Q(v,den) for v in P])

sign=lambda v: 'POS' if v>0 else ('NEG' if v<0 else 'ZERO')
# Find an explicit all-one-sign shifted-coefficient certificate, minimizing the integer boundary search.
lead_sign=sign(P[-1]);shift=None; shifted=None
for bound in range(1,1501):
    q=[sum(P[i]*B(i,j)*bound**(i-j) for i in range(j,len(P))) for j in range(len(P))]
    if all((v>0 if lead_sign=='POS' else v<0) for v in q):
        shift=bound;shifted=q;break
if shift is None:
    raise AssertionError('No strict single-sign shifted coefficient certificate found <=1500; need alternate argument')

boundary={str(k):str(ev(P,k)) for k in range(1,shift)}
# Exact sign transitions, including zeros.
intervals=[]
for k in range(1,shift+1):
    sk=sign(ev(P,k)) if k<shift else lead_sign
    if not intervals or intervals[-1]['sign']!=sk:
        intervals.append({'from_k':k,'to_k':k,'sign':sk})
    else:intervals[-1]['to_k']=k
intervals[-1]['to_k']='infinity'

raw_checks=0
for k in range(1,41):
    for t in range(2,RANK+3):
        assert ev(ps[t],k)*C(k)==H(k,t),(k,t)
        raw_checks+=1
ks=list(range(1,23))+[25,30,37,38,50,80]
examples={}
for k in ks:
    det=bareiss([[H(k,3+i-j) for j in range(RANK)] for i in range(RANK)])
    expected=ev(f[RANK],k)*C(k)**RANK
    assert expected.denominator==1 and det==expected,(k,det,expected)
    if k in (1,5,9,10,11,12,20,21,37,38,50,80):examples[str(k)]=str(det)

k2=2;r=2*k2+1
coeff=[Q(0)]+[(-1)**(ell-1)*ev(ps[ell+2],k2)*ev(ps[2],k2)**(ell-1) for ell in range(1,r-1)]
assert len(coeff)==r-1
for m in range(1,RANK+1):
    assert ev(f[m],k2)==sum(coeff[ell]*ev(f[m-ell],k2) for ell in range(1,min(len(coeff),m+1)))

out={
 'status':'R496_EXACT_PASS','source_pin':PIN,
 'model':'frozen R462 signed BRC auxiliary scalar, odd r=2k+1, s=3, rank m=19',
 'claim_sign_intervals':intervals,
 'p19_ascending':[str(v) for v in P], 'normalizing_denominator':str(den),
 'degree_f19':len(f[RANK])-1,'degree_p19':len(P)-1,
 'polynomial_coefficient_identity_checks':len(f[RANK]),
 'factorization_remainder_zero':True, 'tail_shift':shift,
 'tail_sign':lead_sign,
 'shifted_tail_coefficients_ascending':[str(v) for v in shifted],
 'all_shifted_strict_tail_sign':True,
 'min_abs_shifted_coefficient':str(min(abs(v) for v in shifted)),
 'boundary_exact_values':boundary,
 'asymptotic_normalized_limit':str(f[RANK][-1]/2**(6*RANK)),
 'raw_signed_convolution_checks':raw_checks,
 'independent_original_integer_determinant_checks':len(ks),
 'direct_determinant_examples':examples,
 'k2_rank_recurrence_coefficients':[str(v) for v in coeff[1:]],
 'k2_rank_generating_denominator':'1 - ('+' + '.join(str(v)+'*z^'+str(i) for i,v in enumerate(coeff[1:],1))+')',
 'k2_rank_generating_recurrence_checks':RANK,
 'arithmetic':'exact Python standard-library int and Fraction; no floating point',
 'evidence_status':'AUTHOR_SIDE_EXACT_SYMBOLIC / DRIVER_UNREVIEWED / NOT_ADMITTED'
}
print(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2))
