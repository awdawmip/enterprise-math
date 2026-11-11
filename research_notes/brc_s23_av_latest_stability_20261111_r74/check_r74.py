"""R74: exact O(1) generic affine arc existence and O(n) latest-time stability.
Assumes original stable nonwrapping half-open arc; branch identity preserved.
"""
from fractions import Fraction as F
from math import floor
from random import Random
from pathlib import Path
import json

def frac(x): return x-floor(x)

def affine_exists(alpha, low, high, L, U):
    """Exact existential membership in all integer shifts [low,high) for real theta in [L,U].
    The affine functions require high(theta)>low(theta) for theta throughout I.
    Returns (bool, rational witness | None, criterion).
    """
    assert L<=U and high(L)>low(L) and high(U)>low(U)
    u=lambda z:alpha(z)-low(z)
    v=lambda z:alpha(z)-high(z)
    k0=floor(u(L))
    if k0>v(L):return True,L,'LEFT'
    if u(U)>u(L) and floor(u(U))>k0:
        k=k0+1
        z=L+(F(k)-u(L))*(U-L)/(u(U)-u(L))
        assert v(z)<k<=u(z)
        return True,z,'LOWER_CROSS'
    if v(U)<v(L) and v(U)<floor(v(L)):
        k=floor(v(L))
        z0=L+(F(k)-v(L))*(U-L)/(v(U)-v(L))
        assert L<=z0<U and u(z0)>k and v(z0)==k
        slope_u=(u(U)-u(L))/(U-L)
        delta=min((U-z0)/2,(u(z0)-v(z0))/(2*(abs(slope_u)+1)))
        z=z0+delta
        assert v(z)<k<=u(z)
        return True,z,'UPPER_CROSS'
    return False,None,'NONE'

def classify(t,j,x,a,b,L,U):
    ka,kb=floor(a*L),floor(b*L)
    assert floor(a*U)==ka and floor(b*U)==kb
    A=lambda z:a*z-ka
    B=lambda z:b*z-kb
    assert 0<=A(L)<B(L)<1 and 0<=A(U)<B(U)<1
    al=lambda z:x+(t-j)*z
    enters,yes,_=affine_exists(al,A,B,L,U)
    if not enters:return 'OUT',None,None
    # Complement [B(theta),A(theta)+1), interpreted modulo integer shifts.
    shifted=lambda z:A(z)+1
    absent,no,_=affine_exists(al,B,shifted,L,U)
    if not absent:return 'IN',yes,None
    return 'MIXED',yes,no

def latest(events,j,x,a,b,L,U):
    """(status, time, branch, yes_theta, no_theta).
    A fixed source time has the same auxiliary phase for every branch.
    """
    bytime={}
    for t,branch in events:
        bytime.setdefault(t,[]).append(branch)
    for t in sorted(bytime,reverse=True):
        status,yes,no=classify(t,j,x,a,b,L,U)
        if status=='OUT':continue
        if status=='IN':return 'STABLE',t,min(bytime[t]),yes,None
        return 'CHANGES',t,min(bytime[t]),yes,no
    return 'STABLE_NONE',None,None,None,None

def direct(events,j,x,a,b,z):
    A,B=frac(a*z),frac(b*z)
    assert A<B
    good=[(t,branch) for t,branch in events if A<=frac(x+(t-j)*z)<B]
    return max(good,key=lambda e:(e[0],tuple(-ord(c) for c in str(e[1])))) if good else None

def direct_time(events,j,x,a,b,z):
    row=direct(events,j,x,a,b,z)
    return row[0] if row else None

def partition_points(events,j,x,a,b,L,U):
    ka,kb=floor(a*L),floor(b*L)
    roots={L,U}
    for t,_ in events:
        alpha=lambda z:x+(t-j)*z
        for low in (lambda z:a*z-ka,lambda z:b*z-kb):
            f=lambda z:alpha(z)-low(z)
            if f(L)==f(U):continue
            lo,hi=f(L),f(U)
            for k in range(floor(min(lo,hi)),floor(max(lo,hi))+2):
                z=L+(F(k)-f(L))*(U-L)/(f(U)-f(L))
                if L<=z<=U: roots.add(z)
    points=sorted(roots)
    return sorted(set(points+[(p+q)/2 for p,q in zip(points,points[1:])]))

def run():
    rng=Random(741126)
    valid=0;stats={};largest_points=0
    for _ in range(6000):
        a=rng.randint(-4,7);b=rng.randint(-4,7)
        if a==b:continue
        d=rng.randint(8,71);L=F(rng.randint(-2*d,2*d),d)
        U=L+F(rng.randint(0,6),rng.randint(100,700))
        if floor(a*L)!=floor(a*U) or floor(b*L)!=floor(b*U):continue
        if not 0<=frac(a*L)<frac(b*L)<1 or not 0<=frac(a*U)<frac(b*U)<1:continue
        x=F(rng.randint(-7,7),rng.randint(1,13));j=rng.randint(-7,7)
        rows=[(rng.randint(-55,55),f'branch-{i}') for i in range(rng.randint(1,9))]
        if rng.randrange(5)==0:rows.append((rows[0][0],'branch-extra'))
        state,t,branch,yes,no=latest(rows,j,x,a,b,L,U)
        pts=partition_points(rows,j,x,a,b,L,U)
        times=[direct_time(rows,j,x,a,b,z) for z in pts]
        stable=all(v==times[0] for v in times)
        if state=='STABLE_NONE':assert stable and times[0] is None
        elif state=='STABLE':assert stable and t==times[0] and (t,branch) in rows
        else:
            assert not stable and direct_time(rows,j,x,a,b,yes)==t
            assert direct_time(rows,j,x,a,b,no)!=t
        valid+=1;stats[state]=stats.get(state,0)+1
        largest_points=max(largest_points,len(pts))
    assert valid>1000
    big=[(10**30+3,'alpha'),(10**30+3,'beta'),(10**18+3,'lower')]
    L,U=F(6,25),F(13,50)
    status,t,branch,yes,no=latest(big,0,F(0),1,2,L,U)
    assert status=='CHANGES' and direct_time(big,0,F(0),1,2,yes)==t and direct_time(big,0,F(0),1,2,no)!=t
    return {'seed':741126,'valid_random_models':valid,'exact_direct_critical_partition_crosscheck':'all passed','status_counts':stats,'max_finite_partition_points':largest_points,'large_case':{'status':status,'latest_at_yes':str(t),'yes_parameter':str(yes),'no_parameter':str(no)},'frozen_science':'43ec6098b1330ae86d0a7863be336c5d97f6ef34','scope':'auxiliary stable nonwrapping arc, latest SOURCE TIME, all real parameter interval'}

if __name__=='__main__':
    ans=run()
    print('R74_PASS',ans['valid_random_models'],ans['status_counts'])
    with (Path(__file__).resolve().parent/'verification.json').open('w') as f:json.dump(ans,f,indent=2)
