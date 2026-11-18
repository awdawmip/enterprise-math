"""Exact small 3-adic affine towers and good-prime order samples; Python stdlib."""
import json
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import isqrt

P,Q=233,119
A=-(P*P+Q*Q)
B=P*P*Q*Q
H=(194089,69872040)
BAD=6*P*Q*(P*P-Q*Q)


def vp3(v,cut):
    if not v:return cut
    s=0
    while s<cut and v%3==0:
        v//=3;s+=1
    return s


def f(n,k):
    if k>=n:return F(1)
    f0=F(1,4)+F(3,4*9**(n-k))
    return 1-(1-f0)/3**k


@lru_cache(None)
def expected(n,k,gl):
    if n==0 or k>=n:return F(1)
    g=expected(n-1,k-1,False) if k>0 else expected(n-1,0,False)/9
    if gl:return (27+20*f(n,k)+g)/48
    return (48+32*f(n,k)+g)/81


def finite(n):
    r=3**n
    pairs=tuple(product(range(r),repeat=2))
    hist=[Counter(),Counter()]
    diag=list(3**j for j in range(n+1))
    rank1=[0,0]
    explicit=0
    for a,b,c,d in product(range(r),repeat=4):
        # M=I-A. Enumerate M in all matrices, selecting the affine linear subgroup by invertibility of A.
        gl=((1-a)*(1-d)-b*c)%3!=0
        s1=min(vp3(v,n) for v in (a,b,c,d))
        s2=min(n,vp3(a*d-b*c,2*n)-s1)
        assert 0<=s1<=s2<=n
        hist[0][s1,s2]+=1
        if gl:hist[1][s1,s2]+=1
        if s1==0 and s2>0:
            rank1[0]+=1
            rank1[1]+=3**(n-s2)
        if n<=2:
            image={((a*x+b*y)%r,(c*x+d*y)%r) for x,y in pairs}
            for k in range(n+1):
                successes=sum(((diag[k]*x)%r,(diag[k]*y)%r) in image for x,y in pairs)
                assert successes==r*r//3**(max(s1-k,0)+max(s2-k,0))
                explicit+=r*r
    assert F(rank1[1],rank1[0]*r)==f(n,0)
    result={}
    for gl,hits in enumerate(hist):
        count=sum(hits.values())
        assert count==(48*81**(n-1) if gl else 81**n)
        prob=[]
        good=[]
        for k in range(n+1):
            yes=sum(v*(r*r//3**(max(s1-k,0)+max(s2-k,0))) for (s1,s2),v in hits.items())
            fraction=F(yes,count*r*r)
            assert fraction==expected(n,k,gl)
            good.append(yes);prob.append(str(fraction))
        result['GL' if gl else 'Mat']={'linear_elements':count,
                 'all_matrix_translation_pairs':count*r*r,'successful_affine_pairs_k_0_to_n':good,
                 'probability_k_0_to_n':prob,
                 'Smith_valuation_counts':{f'{s},{t}':v for (s,t),v in sorted(hits.items())}}
    return {'n':n,'r':r,'rank_one_conditional_factor':str(f(n,0)),
            'direct_image_membership_tests':explicit,**result}


def add(p,U,V):
    if U is None:return V
    if V is None:return U
    x,y=U;z,w=V
    if x==z:
        if (y+w)%p==0:return None
        slope=(3*x*x+2*A*x+B)*pow(2*y,-1,p)%p
    else:slope=(w-y)*pow(z-x,-1,p)%p
    t=(slope*slope-A-x-z)%p
    return t,(slope*(x-t)-y)%p


def mul(p,n,U):
    R=None
    while n:
        if n&1:R=add(p,R,U)
        U=add(p,U,U);n//=2
    return R


def points_and_count(p,enumerate_points):
    # A table of quadratic residues gives the group order, independently of the point order routine.
    squares={v*v%p:v for v in range((p+1)//2)}
    order=1;points=[None] if enumerate_points else None
    for x in range(p):
        value=(x*(x-P*P)*(x-Q*Q))%p
        if value in squares:
            y=squares[value];order+=1 if y==0 else 2
            if enumerate_points:
                points.append((x,y))
                if y:points.append((x,p-y))
    return order,points


def prime_sample(bound, image_bound):
    hist=Counter();examples={}; skipped=[];count=0
    divisibility={n:[0]*(n+1) for n in (1,2)}
    for p in range(2,bound+1):
        if any(p%j==0 for j in range(2,isqrt(p)+1)):continue
        if BAD%p==0:skipped.append(p);continue
        num,points=points_and_count(p,p<=image_bound)
        hp=tuple(z%p for z in H)
        assert (hp[1]**2-hp[0]*(hp[0]-P*P)*(hp[0]-Q*Q))%p==0
        assert mul(p,num,hp) is None
        cofactor=num
        while cofactor%3==0:cofactor//=3
        z=mul(p,cofactor,hp);j=0
        while z is not None:z=mul(p,3,z);j+=1
        hist[j]+=1
        examples.setdefault(j,{'p':p,'E_order':num})
        if points is None:continue
        assert len(points)==len(set(points))==num
        count+=1
        for n,acc in divisibility.items():
            image={mul(p,3**n,U) for U in points}
            for k in range(n+1):
                acc[k]+=int(mul(p,3**k,hp) in image)
            if j==0:assert hp in image
            if p==23 and n==1:assert hp not in image
    return {'p_upper_inclusive':bound,'excluded_primes_dividing_6PQ_P2_minus_Q2':skipped,
            'good_primes':sum(hist.values()),'v3_order_H_histogram':dict(sorted(hist.items())),
            'first_examples_by_order_valuation':examples,
            'full_group_direct_membership_sample':{'p_upper_inclusive':image_bound,'good_primes':count,
                 'number_of_primes_with_3^k_H_in_3^n_E_for_k_0_to_n':divisibility},
            'scope':'finite empirical histogram; does not infer density'}


def run():
    assert H[1]**2==H[0]*(H[0]-P*P)*(H[0]-Q*Q)
    c4=16*(A*A-3*B);disc=16*P**4*Q**4*(P*P-Q*Q)**2
    d=disc;v=0
    while d%7==0:d//=7;v+=1
    assert c4%7!=0 and v==4
    levels=[finite(n) for n in range(1,4)]
    return {'curve':{'P':P,'Q':Q,'H':H,'c4_mod_7':c4%7,'discriminant_v7':v},
            'levels':levels,'good_prime_curve_sample':prime_sample(5000,499),
            'affine_condition':'(I-A)v=3^k t modulo 3^n; t uniform and includes zero',
            'Smith_truncation':'s2=min(n,v3(det M)-s1), det valuation computed with cutoff 2n',
            'limiting_model_cdf_k_0_to_4':[str(1-F(69,208*3**k)) for k in range(5)]}


if __name__=='__main__':
    print(json.dumps(run(),indent=1,sort_keys=True))
