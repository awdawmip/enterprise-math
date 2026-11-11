"""R73: constant-candidate exact affine-circle interval membership.
Python Fraction oracle versus independent finite integer-layer enumeration.
Author-side auxiliary model, not a native BRC solver.
"""
from fractions import Fraction as F
from math import floor
from random import Random
import json, time
from pathlib import Path

def fpart(z):
    return z - floor(z)

def oracle(t, j, x, a, b, L, U):
    """Exact O(1) rational-op EXISTS_MEMBER / ALL_OUT for stable original arc.
    Returns (member, rational_witness_or_None, route).
    """
    assert L <= U
    A = lambda z: a*z - floor(a*L)
    B = lambda z: b*z - floor(b*L)
    assert floor(a*L) == floor(a*U) and floor(b*L) == floor(b*U)
    assert 0 <= A(L) < B(L) <= 1 and 0 <= A(U) < B(U) <= 1
    # Endpoints are the original affine arc endpoints, not newly sorted labels.
    DA = lambda z: x + (t-j)*z - A(z)
    DB = lambda z: x + (t-j)*z - B(z)
    if floor(DA(L)) > DB(L):
        return True, L, 'LEFT_ENDPOINT'
    if DA(U) > DA(L) and floor(DA(U)) > floor(DA(L)):
        k = floor(DA(L)) + 1
        z = L + (F(k) - DA(L))*(U-L)/(DA(U)-DA(L))
        assert L < z <= U and DB(z) < k <= DA(z)
        return True, z, 'LOWER_BOUNDARY_ENTER'
    if DB(U) < DB(L) and DB(U) < floor(DB(L)):
        k = floor(DB(L))
        z0 = L + (F(k)-DB(L))*(U-L)/(DB(U)-DB(L))
        assert L <= z0 < U and DB(z0) == k and DA(z0) > k
        width = DA(z0)-DB(z0)
        slope_a = F(t-j-a)
        delta = min((U-z0)/2, width/(2*(abs(slope_a)+1)))
        z = z0 + delta
        assert L < z <= U and DB(z) < k <= DA(z)
        return True, z, 'UPPER_BOUNDARY_LEAVE'
    return False, None, 'ALL_OUT'

def brute(t, j, x, a, b, L, U):
    A = lambda z: a*z - floor(a*L)
    B = lambda z: b*z - floor(b*L)
    DA = lambda z: x + (t-j)*z - A(z)
    DB = lambda z: x + (t-j)*z - B(z)
    lo, hi = floor(min(DB(L), DB(U)))+1, floor(max(DA(L), DA(U)))
    for k in range(lo, hi+1):
        lower, upper = L, U
        lower_closed, upper_closed = True, True
        for f, strict in ((lambda z:DA(z)-k,False),(lambda z:k-DB(z),True)):
            q0, q1 = f(L), f(U)
            slope = (q1-q0)/(U-L) if U!=L else 0
            if slope==0:
                if q0 < 0 or (strict and q0 == 0):
                    break
            else:
                root = L-q0/slope
                if slope>0:
                    if root > lower:
                        lower,lower_closed=root,not strict
                    elif root==lower:
                        lower_closed=lower_closed and not strict
                else:
                    if root < upper:
                        upper,upper_closed=root,not strict
                    elif root==upper:
                        upper_closed=upper_closed and not strict
        else:
            if lower<upper or (lower==upper and lower_closed and upper_closed):
                return True
    return False

def valid(t,j,x,a,b,L,U):
    if L > U: return False
    if floor(a*L)!=floor(a*U) or floor(b*L)!=floor(b*U):return False
    A=lambda z:fpart(a*z)
    B=lambda z:fpart(b*z)
    return A(L) < B(L) and A(U) < B(U)

def run():
    rng=Random(731126)
    cases,by_route,fail=0,{},[]
    for _ in range(18000):
        a=rng.randint(-5,7);b=rng.randint(-5,7)
        if a==b: continue
        q=rng.randint(9,101);L=F(rng.randint(-3*q,3*q),q)
        U=L+F(rng.randint(0,8),rng.randint(200,1000))
        j=rng.randint(-8,8);t=rng.randint(-180,180)
        x=F(rng.randint(-4,4),rng.randint(1,12))
        if not valid(t,j,x,a,b,L,U):continue
        res,w,how=oracle(t,j,x,a,b,L,U)
        check=brute(t,j,x,a,b,L,U)
        if res!=check: fail.append((str(L),str(U),a,b,t,j,str(x),res,check,how))
        if res:
            assert L<=w<=U and fpart(x+(t-j)*w) >= fpart(a*w) and fpart(x+(t-j)*w) < fpart(b*w), (t,j,x,a,b,L,U,w,how)
        by_route[how]=by_route.get(how,0)+1
        cases+=1
    assert cases > 2000 and not fail, (cases, fail[:3])
    special={}
    for t in (10**18+3,10**30+3):
        L,U=F(6,25),F(13,50)
        start=time.perf_counter()
        ans,w,route=oracle(t,0,F(0),1,2,L,U)
        elapsed=time.perf_counter()-start
        assert ans and L<=w<=U
        dA=lambda z: t*z-z
        dB=lambda z: t*z-2*z
        K=floor(max(dA(L),dA(U)))-floor(min(dB(L),dB(U)))
        special[str(t)]={'exists_member':ans,'route':route,'witness':str(w),'integer_levels_upper_bound':K,'elapsed_seconds_single_run':elapsed}
    return {'model':'stable_nonwrapping_affine_half_open_arc','random_seed':731126,'valid_cases':cases,'routes':by_route,'disagreements':len(fail),'large_time':special,'scientific_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34','scope':'rational input; entire real parameter interval by exact proof; author-side'}

if __name__=='__main__':
    ans=run()
    print('R73_PASS',ans['valid_cases'],ans['routes'])
    with (Path(__file__).resolve().parent / 'verification.json').open('w') as f:json.dump(ans,f,indent=2)
