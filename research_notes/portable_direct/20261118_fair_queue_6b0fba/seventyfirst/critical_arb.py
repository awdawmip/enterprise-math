"""Rigorous finite original-road fixtures. Requires python-flint 0.9.0."""
from fractions import Fraction as F
from math import gcd
import json
from flint import acb, arb, ctx, fmpq

ctx.prec=160

def rational_arb(x): return arb(fmpq(x.numerator,x.denominator))

def bounds(v,places=14):
    scale=10**places
    lo=(v*scale).floor().unique_fmpz()
    if lo is None: raise ArithmeticError('interval too wide')
    lo=int(lo)
    l,u=arb(fmpq(lo,scale)),arb(fmpq(lo+1,scale))
    assert v>=l and v<u
    def dec(b):
        sign='-' if b<0 else ''
        return '%s%d.%0*d'%(sign,abs(b)//scale,places,abs(b)%scale)
    return [dec(lo),dec(lo+1)]

def actual(numer,denom,X=4096,Q=16):
    a=arb(fmpq(numer,denom));s=1+a;c=1/s.zeta();end=4*X
    mu=[1]*(end+1);primes=[];sieved=bytearray(end+1)
    for p in range(2,end+1):
        if sieved[p]:continue
        primes.append(p)
        for n in range(p,end+1,p):mu[n]=-mu[n];sieved[n]=1
        for n in range(p*p,end+1,p*p):mu[n]=0
    R=[arb(0) for n in range(end+1)]
    for d in range(1,end+1):
        if mu[d]:
            h=mu[d]*arb(d)**(-a)
            for n in range(d,end+1,d):R[n]+=h
    b=[-1-c/2]
    for n in range(1,end+1):b.append(b[-1]+R[n]-c)
    yn=sum(x*x for x in b[X+1:2*X+1])/X
    wt=X*sum((b[n]/n)**2 for n in range(X+1,end+1))
    w=arb(0); ideal=arb(0);weighted_penalty=arb(0); seen=[]
    maxerr=arb(0)
    for q in range(2,Q+1):
        if mu[q]==0:continue
        bq=mu[q]*c
        j2=F(q*q)
        for p in primes:
            if p>q:break
            if q%p==0:
                bq/=arb(p)**s-1
                j2*=F(p*p-1,p*p)
        ideal+=bq*bq*rational_arb(j2/12)
        weighted_penalty+=abs(bq)*rational_arb(j2/12)
        bins=[arb(0) for _ in range(q)]
        for n in range(X+1,2*X+1):bins[n%q]+=b[n]
        roots=[(acb(-2*k)/q).exp_pi_i() for k in range(q)]
        for r in range(1,q):
            if gcd(r,q)!=1:continue
            seen.append(F(r,q))
            zbar=roots[r]; bhat=sum(roots[(i*r)%q]*v for i,v in enumerate(bins))/X
            w+=abs(bhat)**2
            er=abs((1-zbar)*bhat-bq)
            if er>maxerr:maxerr=er
            elif not er<=maxerr:
                assert er.overlaps(maxerr)
                maxerr=maxerr.union(er)
    rows=[]
    for x in seen:
        val=arb(0)
        for y in seen:
            if y==x:continue
            t=x-y
            if (X*t).denominator!=1:
                val+=abs(rational_arb(X*t).sin_pi())/(X*abs(rational_arb(t).sin_pi()))
        rows.append(val)
    # Fixed rational majorants to certificate standards--all tested row-by-row/frequency-by-frequency.
    assert all(val<arb(fmpq(1,8)) for val in rows)
    assert maxerr<arb(fmpq(1,450))
    cert=(ideal-2*weighted_penalty/450)*arb(fmpq(8,9))
    assert yn>w*arb(fmpq(8,9))>cert>0
    return {'a':f'{numer}/{denom}','X':X,'Q':Q,'precision_bits':ctx.prec,'observed_frequencies':len(seen),
            'c_a':bounds(c),'actual_raw_dyadic_mean':bounds(yn),'X_times_tail_prefix_X_to_4X':bounds(wt),
            'spectral_E':bounds(ideal),'observed_squared_Fourier_coefficients':bounds(w),
            'maximum_twisted_coefficient_error':bounds(maxerr),'offdiagonal_Gram_rows_strictly_below':'1/8',
            'source_lower_bound_from_arithmetic_E_Gram_and_leakage':bounds(cert)}
if __name__=='__main__':
    print(json.dumps([actual(n,16) for n in (7,8,9)],indent=2))
