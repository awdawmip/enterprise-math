#!/usr/bin/env python3
"""PREFIX-972 exact signed source-fiber parity theorem and independent checks."""
import argparse
import json
from math import gcd
from collections import Counter


def origin(p):
    return [(i,j,s,(1<<i)-s*(1<<j)) for i in range(p) for j in range(p) for s in (1,-1)]


def order_and_minus(g):
    if g==1: return (1,False)
    v=2%g; h=1
    while v!=1:
        v=2*v%g; h+=1
    return h,(h%2==0 and pow(2,h//2,g)==g-1)


def series(p,start,step):
    if start>=p: return 0
    q=(p-1-start)//step+1
    return q*(p-start)-step*q*(q-1)//2


def spectrum(p,g):
    """Return exact numeric even/odd and source-slot even/odd counts."""
    if g==1:
        n=(3*p*p-5*p+10)//2
        odd=3*p-4
        total=2*p*p
        slotodd=4*(p-1)
        return {'numeric_even':n-odd,'numeric_odd':odd,
                'slots_even':total-slotodd,'slots_odd':slotodd,
                'slots_plus':p*p,'slots_minus':p*p}
    h,eta=order_and_minus(g)
    A=series(p,h,h)
    B=series(p,h//2,h) if eta else 0
    D=1+2*A+B-(p-2 if g==3 else 0)
    ne=2*((p-1)//h)+(sum(1 for e in range(h//2,p,h)) if eta else 0)-(1 if g==3 else 0)
    slots_plus=p+2*A
    slots_minus=2*B
    slotodd=2*((p-1)//h)+2*(sum(1 for e in range(h//2,p,h)) if eta else 0)
    return {'numeric_even':D-ne,'numeric_odd':ne,
            'slots_even':slots_plus+slots_minus-slotodd,'slots_odd':slotodd,
            'slots_plus':slots_plus,'slots_minus':slots_minus}


def source_fiber(p,g):
    """Generate exact labeled triples using exponent congruence, not c % g."""
    if g==1: return origin(p)
    h,eta=order_and_minus(g)
    z=[(i,i,1,0) for i in range(p)]
    for e in range(1,p):
        pos=e%h==0
        neg=eta and e%h==h//2
        if not(pos or neg):continue
        for r in range(p-e):
            if pos:
                z.extend([(r+e,r,1,(1<<(r+e))-(1<<r)),
                          (r,r+e,1,(1<<r)-(1<<(r+e)))])
            if neg:
                n=(1<<(r+e))+(1<<r)
                z.extend([(r+e,r,-1,n),(r,r+e,-1,n)])
    return z


def direct(p,g):
    z=[(i,j,s,c) for i,j,s,c in origin(p) if c%g==0]
    d={c for i,j,s,c in z}
    return {'numeric_even':sum(c%2==0 for c in d),
            'numeric_odd':sum(c%2!=0 for c in d),
            'slots_even':sum(c%2==0 for i,j,s,c in z),
            'slots_odd':sum(c%2!=0 for i,j,s,c in z),
            'slots_plus':sum(s==1 for i,j,s,c in z),
            'slots_minus':sum(s==-1 for i,j,s,c in z)}


def phi(n):
    v=n;d=2
    while d*d<=n:
        if n%d==0:
            while n%d==0:n//=d
            v-=v//d
        d+=1
    if n>1:v-=v//n
    return v


def named_average(p,k):
    a=sum(phi(k//g)*(spectrum(p,g)['slots_even']+spectrum(p,g)['slots_odd']) for g in range(1,k+1,2) if k%g==0)
    n=sum(phi(k//g)*(spectrum(p,g)['numeric_even']+spectrum(p,g)['numeric_odd']) for g in range(1,k+1,2) if k%g==0)
    return {'named':a,'numeric':n,'loss_by_numeric_projection':a-n}


def verify(max_p):
    fiber_cases=core_cases=0
    for p in range(4,max_p+1):
        for g in range(1,1<<(p-1),2):
            assert spectrum(p,g)==direct(p,g),(p,g,'parity')
            assert sorted(source_fiber(p,g))==sorted((i,j,s,c) for i,j,s,c in origin(p) if c%g==0),(p,g,'labeled')
            fiber_cases+=1
        for k in range(1,(1<<(p-1))-2,2):
            z=origin(p)
            real=sum(sum(c%gcd(k,t)==0 and c%2==(1-t)%2 for i,j,s,c in z) for t in range(1,2*k+1))
            distinct={c for _,_,_,c in z}
            numeric_real=sum(sum(c%gcd(k,t)==0 and c%2==(1-t)%2 for c in distinct) for t in range(1,2*k+1))
            pred=named_average(p,k)
            assert (real,numeric_real)==(pred['named'],pred['numeric']),(p,k,'average')
            core_cases+=1
    return {'p_min':4,'p_max':max_p,'all_g_parity_fibers':fiber_cases,'eligible_k_average':core_cases}


def q19():
    p=19;k=21
    rows=[]
    for g in (1,3,7,21):
        row={'g':g,'phi(k/g)':phi(k//g),**spectrum(p,g)}
        assert spectrum(p,g)==direct(p,g)
        rows.append(row)
    pred=named_average(p,k)
    assert pred=={'named':11133,'numeric':7653,'loss_by_numeric_projection':3480}
    return {'p':p,'k':k,'signed_slot_examined_before_gcd':k*2*p*p,'distinct_residual_examined_before_gcd':k*len({c for _,_,_,c in origin(p)}), 'by_g':rows,**pred}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-p',type=int,default=9)
    args=ap.parse_args()
    out={'schema':'PREFIX972_PARITY_REFINED_FIBER_V1','frozen_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','finite_checks':verify(args.max_p),'q19':q19(),'status':'AUTHOR_PROOF_EXACT_INTEGER_VERIFIED_NOT_REVIEWED'}
    print(json.dumps(out,indent=2,ensure_ascii=False))


if __name__=='__main__':main()
