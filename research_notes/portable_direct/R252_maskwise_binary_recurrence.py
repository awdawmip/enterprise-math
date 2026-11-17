#!/usr/bin/env python3
"""R252: exact labelled-mask binary coefficient extraction for frozen R234 observer.

Independent Python Fraction implementation of R250/R251 model; no 229-degree
polynomial LCM, roots, floats, or external libraries. Finite tests also use a
separate direct rank-one propagation and modular matrix powering.
"""
from fractions import Fraction as F
import hashlib, json, time
from pathlib import Path

W = (144,576,1440,4320,17280,86400,518400)
SOURCE = '43ec6098b1330ae86d0a7863be336c5d97f6ef34'

def setup(j):
    s=F(j,1000)
    t=(1691*s-2615)/(2615*s-3539)
    a=[F(1,5), F(1,4), F(3,10), F(9,20), s, F(2,3), t]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-x) for x in a[1:]]
    pi=[y/(1-x) for x,y in zip(a,b)]
    assert sum(pi)==1
    z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
    return a,b,pi,rho

def indices(m):
    return [0]+[i+1 for i in range(6) if (m>>i)&1]

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def char_poly(ix,a,b):
    # Polynomial coefficients ascending, det(x I-P_D).
    allp=[F(1)]
    for i in ix: allp=mul(allp,[-a[i],F(1)])
    for i in ix:
        p=[F(1)]
        for j in ix:
            if j!=i: p=mul(p,[-a[j],F(1)])
        for j,c in enumerate(p): allp[j]-=b[i]*c
    assert len(allp)==len(ix)+1 and allp[-1]==1
    return allp

def moments(ix,a,pi,rho,count,weight):
    v=[F(1)]*len(ix)
    out=[]
    for _ in range(count):
        out.append(weight*sum((rho[i]*v[t] for t,i in enumerate(ix)),F(0)))
        mass=sum((pi[i]*v[t] for t,i in enumerate(ix)),F(0))
        v=[a[i]*v[t]+(1-a[i])*mass for t,i in enumerate(ix)]
    return out

def poly_reduce(product, q, mod=None):
    d=len(q)-1
    p=list(product)+[0]*max(0,d-len(product))
    for k in range(len(p)-1,d-1,-1):
        v=p[k]
        if v:
            for i in range(d): p[k-d+i]-=v*q[i]
    p=p[:d]
    return [x%mod for x in p] if mod else p

def x_power_mod(k,q,mod=None):
    # x^k mod monic characteristic, using binary multiplication in Q[x]/(q).
    d=len(q)-1
    ans=[1]+[0]*(d-1)
    base=poly_reduce([0,1],q,mod) # handles degree one.
    while k:
        if k&1: ans=poly_reduce(mul(ans,base),q,mod)
        k//=2
        if k: base=poly_reduce(mul(base,base),q,mod)
    return ans

def fast_mask(k,ix,a,b,pi,rho,weight):
    q=char_poly(ix,a,b)
    h=moments(ix,a,pi,rho,len(ix),weight)
    r=x_power_mod(k,q)
    return sum((u*v for u,v in zip(r,h)),F(0))

def fast_total(j,k):
    a,b,pi,rho=setup(j)
    return sum((fast_mask(k,indices(m),a,b,pi,rho,W[m.bit_count()]) for m in range(63)), F(0))

def direct_total(j,ks):
    # Entire sequence computed by a different propagation route.
    a,b,pi,rho=setup(j)
    n=max(ks)+1
    totals={k:F(0) for k in ks}
    for m in range(63):
        ix=indices(m);w=W[m.bit_count()];v=[F(1)]*len(ix)
        for k in range(n):
            if k in totals: totals[k]+=w*sum((rho[i]*v[t] for t,i in enumerate(ix)),F(0))
            mass=sum((pi[i]*v[t] for t,i in enumerate(ix)),F(0))
            v=[a[i]*v[t]+(1-a[i])*mass for t,i in enumerate(ix)]
    return totals

def mod_fraction(v,p):
    return (v.numerator%p)*pow(v.denominator%p,-1,p)%p

def matmul(A,B,p):
    d=len(A);out=[[0]*d for _ in range(d)]
    for i in range(d):
        for k in range(d):
            aik=A[i][k]
            for j in range(d): out[i][j]=(out[i][j]+aik*B[k][j])%p
    return out

def modular_independent_matrix(k,ix,a,pi,rho,weight,p):
    d=len(ix)
    mat=[[(mod_fraction(a[i],p) if i==j else 0)+mod_fraction(1-a[i],p)*mod_fraction(pi[j],p) for j in ix] for i in ix]
    mat=[[x%p for x in r] for r in mat]
    out=[[int(i==j) for j in range(d)] for i in range(d)]
    while k:
        if k&1:out=matmul(out,mat,p)
        k//=2
        if k:mat=matmul(mat,mat,p)
    v=[sum(row)%p for row in out]
    return mod_fraction(F(weight),p)*sum(mod_fraction(rho[i],p)*v[t] for t,i in enumerate(ix))%p

def modular_fast(k,ix,a,b,pi,rho,weight,p):
    q=[mod_fraction(x,p) for x in char_poly(ix,a,b)]
    h=[mod_fraction(x,p) for x in moments(ix,a,pi,rho,len(ix),weight)]
    r=x_power_mod(k,q,p)
    return sum(x*y for x,y in zip(r,h))%p

def main():
    started=time.monotonic()
    # k is exponent, observation event n=k+1. Values n=1..235 include R251 anchors.
    targets={390:[0,1,2,8,63,126],400:[0,1,2,3,4,8,63,126,234],410:[0,1,2,8,63,126]}
    first5=['1406969190/2053','2637842299181/4110106','6772582479238063/11177993736','23248822376339528113/40422082051296','13709572447745051946478717/25009840364735903040']
    checks=0; anchors=[]
    for j,ks in targets.items():
        expected=direct_total(j,ks)
        for k in ks:
            got=fast_total(j,k)
            assert got==expected[k], ('exact_mismatch',j,k)
            if j==400 and k<5:
                assert str(got)==first5[k],('r251_anchor_mismatch',k)
            anchors.append({'s':str(F(j,1000)),'n':k+1,'value_sha256':hashlib.sha256(str(got).encode()).hexdigest(), 'value_num_bits':got.numerator.bit_length(), 'value_den_bits':got.denominator.bit_length()})
            checks+=1
    highks=[65535,999999]
    primes=[1000000007,1000000009]
    a,b,pi,rho=setup(400)
    modular=[]
    for k in highks:
        for p in primes:
            fsum=0;msum=0
            for mask in range(63):
                ix=indices(mask);w=W[mask.bit_count()]
                f=modular_fast(k,ix,a,b,pi,rho,w,p)
                z=modular_independent_matrix(k,ix,a,pi,rho,w,p)
                assert f==z,('mod_mismatch',k,p,mask,f,z)
                fsum=(fsum+f)%p;msum=(msum+z)%p
            assert fsum==msum
            modular.append({'s':'2/5','n':k+1,'p':p,'value_mod_p':fsum,'mask_checks':63})
    evidence={'schema':'ENTERPRISE_MATH_R252_MASKWISE_BINARY_CERT_V1',
      'source_commit_pin':SOURCE,'predecessors':{'R250':'acb90adc07ec249069e3662140a8a53e794db615','R251':'3836e783853c34397f87a7a0efe89f94b53c51fd'},
      'rational_anchors':anchors,'rational_exact_checks':checks,
      'modular_checks':modular,'modular_mask_checks':len(modular)*63,
      'unreduced_mask_count':63,'sum_mask_degrees':249,
      'sum_mask_degree_squares':sum(len(indices(m))**2 for m in range(63)),
      'all_pass':True, 'test_scope':'Exact Fraction cross-check n<=235 at three rational parameters; independent matrix powering mod two primes at n=65536,1000000 for s=2/5; formal polynomial identity covers all n and all valid parameters.',
      'not_claimed':'no complete rational integer computed for n=65536 or 1000000; modular equality not a rational equality proof, no measured bit-complexity advantage; no native BRC EffectHistogram integration'}
    outfile=Path(__file__).with_name('R252_verification.json')
    outfile.write_text(json.dumps(evidence,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print('PASS',checks,'full Fraction coefficient comparisons;',len(modular)*63,'independent modular mask comparisons')
    print('Elapsed_seconds',round(time.monotonic()-started,3))
    print('Evidence_SHA256',hashlib.sha256(outfile.read_bytes()).hexdigest())
    print('Evidence',str(outfile))
    print('Modular values',modular)

if __name__=='__main__': main()
