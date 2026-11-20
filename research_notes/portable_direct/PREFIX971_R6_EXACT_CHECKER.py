#!/usr/bin/env python3
"""PREFIX-971 exact gcd-fiber counts, integer-only reference."""
import argparse
import json
from math import gcd

def residuals(p):
    return {2**i-s*2**j for i in range(p) for j in range(p) for s in (-1,1)}

def order_and_minus(g):
    r=2%g
    h=1
    while r!=1:
        r=2*r%g
        h+=1
    return h,h%2==0 and pow(2,h//2,g)==g-1

def series(p,start,step):
    if start>=p:
        return 0
    n=(p-1-start)//step+1
    return n*(p-start)-step*n*(n-1)//2

def count_fiber(p,g):
    if g==1:
        return (3*p*p-5*p+10)//2
    h,minus=order_and_minus(g)
    return 1+2*series(p,h,h)+(series(p,h//2,h) if minus else 0)-(p-2 if g==3 else 0)

def count_slots(p,g):
    if g==1:
        return 2*p*p
    h,minus=order_and_minus(g)
    return p+2*series(p,h,h)+2*(series(p,h//2,h) if minus else 0)

def phi(n):
    v=n
    f=2
    while f*f<=n:
        if n%f==0:
            while n%f==0:
                n//=f
            v-=v//f
        f+=1
    if n>1:
        v-=v//n
    return v

def divisors(k):
    return [g for g in range(1,k+1) if k%g==0]

def analytic(p,k):
    return sum(phi(k//g)*count_fiber(p,g) for g in divisors(k))

def verify(max_p):
    cg=ck=0
    for p in range(4,max_p+1):
        D=residuals(p)
        for g in range(1,2**(p-1),2):
            assert count_fiber(p,g)==sum(c%g==0 for c in D),(p,g)
            actual_slots=sum((2**i-s*2**j)%g==0
                             for i in range(p) for j in range(p) for s in (-1,1))
            assert count_slots(p,g)==actual_slots,(p,g,'slots')
            cg+=1
        for k in range(1,2**(p-1)-2,2):
            direct=sum(sum(c%gcd(k,t)==0 and c%2==(1-t)%2 for c in D)
                       for t in range(1,2*k+1))
            assert analytic(p,k)==direct,(p,k)
            ck+=1
    return {'p':[4,max_p], 'numeric_and_slot_fiber_checks':cg,
            'all_eligible_odd_core_checks':ck}

def q19():
    p,k=19,21
    D=residuals(p)
    rows=[]
    for g in divisors(k):
        fib={c for c in D if c%g==0}
        rows.append({'g':g,'phi_k_over_g':phi(k//g),'numeric':len(fib),
                     'even':sum(c%2==0 for c in fib),
                     'odd':sum(c%2!=0 for c in fib),
                     'named_slot_count':count_slots(p,g),
                     'weighted':phi(k//g)*len(fib)})
    direct=sum(sum(c%gcd(k,t)==0 and c%2==(1-t)%2 for c in D)
               for t in range(1,2*k+1))
    admitted=analytic(p,k)
    assert admitted==direct==7653 and len(D)==499
    return {'p':p,'k':k,'gaps':[1,3,5],'distinct_residuals':len(D),
            'by_divisor':rows,'source_numeric_examined':k*len(D),
            'source_numeric_admitted':admitted,
            'source_numeric_eliminated':k*len(D)-admitted}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-p',type=int,default=9)
    args=ap.parse_args()
    print(json.dumps({'schema':'PREFIX971_GCD_FIBER_V1',
        'frozen_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'finite_checks':verify(args.max_p),'q19':q19(),
        'status':'AUTHOR_PROOF_EXACT_INTEGER_VERIFIED_NOT_REVIEWED'},
        indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
