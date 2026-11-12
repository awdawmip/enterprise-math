#!/usr/bin/env python3
"""R89 exact union-of-envelope-box certificates + two-polarity champion.
All arithmetic for membership and certificate coverage is fractions.Fraction.
The comparison baseline independently constructs the full R77 critical-cut union.
"""
from fractions import Fraction as F
from math import floor, ceil
from dataclasses import dataclass
from collections import Counter
from random import Random
import json
from pathlib import Path


def frac(x): return x-floor(x)
def member(t,z,j,x,a,b):
    A,B,s=frac(a*z),frac(b*z),frac(x+(t-j)*z)
    return ((A<=s<B) if A<B else (s>=A or s<B) if A>B else False)

def witness_cuts(t,I,j,x,a,b):
    L,U=I;points={L,U}
    for c,d in ((a,F(0)),(b,F(0)),(a-b,F(0)),(t-j,x),(t-j-a,x),(t-j-b,x)):
        if not c:continue
        low,high=sorted((c*L+d,c*U+d))
        for k in range(ceil(low),floor(high)+1):
            z=(k-d)/c
            if L<=z<=U:points.add(z)
    return sorted(points)

def atoms(points):
    for i,p in enumerate(points):
        yield p
        if i+1<len(points):yield (p+points[i+1])/2

def oracle(t,want,I,j,x,a,b,counts):
    counts['oracle_calls']+=1
    for z in atoms(witness_cuts(t,I,j,x,a,b)):
        counts['oracle_atoms']+=1
        if member(t,z,j,x,a,b)==want:return z
    return None

def winner(identities,z,j,x,a,b):
    return next(((t,br) for t,br in sorted(identities,reverse=True) if member(t,z,j,x,a,b)),None)

def full_reference(identities,I,j,x,a,b,counts):
    cuts=set(I)
    for t in {t for t,_ in identities}: cuts.update(witness_cuts(t,I,j,x,a,b))
    profile=[]
    for z in atoms(sorted(cuts)):
        counts['reference_atoms']+=1
        profile.append((z,winner(identities,z,j,x,a,b)))
    vals={v for _,v in profile}
    return ('STABLE_NONE',None) if vals=={None} else ('STABLE',next(iter(vals))) if len(vals)==1 else ('CHANGES',None)

@dataclass(frozen=True)
class Box:
    r:int; q:int; theta0:F
    J:tuple[F,F]; lo:int; hi:int
    j:int; x:F; a:int; b:int
    # valid only when make_box returns a proof-checked instance

def make_box(r,q,theta0,J,lo,hi,j,x,a,b):
    L,U=J
    assert q>0 and 0<=r<q and L<=U and lo<=hi and theta0.denominator==q
    # Anchored values are equal for all t ≡ r (mod q) at theta0=p/q.
    ka,kb=floor(a*L),floor(b*L)
    if ka!=floor(a*U) or kb!=floor(b*U):return None
    if not all(a*z-ka<b*z-kb for z in (L,U)):return None
    beta=frac(x+(r-j)*theta0)
    corners=[(t-j)*(z-theta0) for t in (lo,hi) for z in (L,U)]
    smin,smax=beta+min(corners),beta+max(corners)
    qmin=min(a*L-ka,a*U-ka)
    qmax=max(b*L-kb,b*U-kb)
    # No integer translate of the closed target enclosure meets source envelope.
    if ceil(smin-qmax)<=floor(smax-qmin):return None
    return Box(r,q,theta0,J,lo,hi,j,x,a,b)

def covers_real_time_slice(active,lo,hi):
    """Does the union of closed real intervals [lo_i,hi_i] cover [lo,hi]?"""
    end=lo
    for k in sorted(active,key=lambda c:(c.lo,c.hi)):
        if k.hi<end:continue
        if k.lo>end:return False
        end=max(end,k.hi)
        if end>=hi:return True
    return end>=hi

def box_cover(I,lo,hi,certs,signature,r,q,theta0,counts):
    """Exact closed-rectangle coverage using endpoints AND open-gap probes."""
    L,U=I
    j,x,a,b=signature
    selected=[]; pts={L,U}
    for c in certs:
        if (c.r,c.q,c.theta0,c.j,c.x,c.a,c.b)!=(r,q,theta0,j,x,a,b):continue
        l=max(L,c.J[0]);u=min(U,c.J[1])
        if l<=u:
            selected.append(c);pts.update((l,u))
    if not selected:return False
    for z in atoms(sorted(pts)):
        counts['cover_atoms']+=1
        active=[c for c in selected if c.J[0]<=z<=c.J[1]]
        if not covers_real_time_slice(active,lo,hi):return False
    return True

def classify(E,I,j,x,a,b,certs,theta0,stats):
    """R87 exact champion with conservative R89 group exclusion skips.
    Caller supplies certified boxes only; no heuristic trust in unvalidated flags.
    """
    L,U=I; w0=winner(E,L,j,x,a,b)
    present=sorted({t for t,_ in E},reverse=True)
    # Each nonempty congruence group of competitors is skipped if a box cover
    # certifies its entire real-time envelope for the whole query interval.
    threshold = None if w0 is None else w0[0]
    candidates=[t for t in present if threshold is None or t>threshold]
    byres={}
    q=theta0.denominator
    for t in candidates:byres.setdefault(t%q,[]).append(t)
    skips=set()
    for r,ts in byres.items():
        if box_cover(I,min(ts),max(ts),certs,(j,x,a,b),r,q,theta0,stats):
            skips.update(ts)
            stats['box_groups_hit']+=1
            stats['times_skipped']+=len(ts)
    for t in candidates:
        if t in skips:continue
        z=oracle(t,True,I,j,x,a,b,stats)
        if z is not None:
            w1=winner(E,z,j,x,a,b)
            assert w1!=w0
            return ('CHANGES',(L,w0),(z,w1))
    if w0 is None:return ('STABLE_NONE',None,None)
    z=oracle(w0[0],False,I,j,x,a,b,stats)
    if z is not None:
        w1=winner(E,z,j,x,a,b)
        assert w1!=w0
        return ('CHANGES',(L,w0),(z,w1))
    return ('STABLE',w0,None)

def baseline(E,I,j,x,a,b,stats):
    return classify(E,I,j,x,a,b,[],F(1,16),stats)

def test():
    rng=Random(8920261112); q=16;theta0=F(1,16)
    big=(theta0-F(3,500),theta0+F(3,500))
    left=(big[0],theta0);right=(theta0,big[1])
    p=(-14,18);sig=(0,F(0),4,8)
    assert make_box(2,q,theta0,big,*p,*sig) is None
    c1=make_box(2,q,theta0,left,*p,*sig)
    c2=make_box(2,q,theta0,right,*p,*sig)
    assert c1 is not None and c2 is not None
    c_all=[c1,c2]
    # Four smaller boxes tile both the parameter axis and the source-time axis;
    # no individual box contains the full requested rectangle.
    grid=[make_box(2,q,theta0,J,lo,hi,*sig) for J in (left,right)
          for lo,hi in ((-14,2),(2,18))]
    assert all(z is not None for z in grid)
    measures=Counter()
    assert box_cover(big,-14,18,grid,sig,2,q,theta0,measures)
    assert not any(z.J[0]<=big[0] and z.J[1]>=big[1] and z.lo<=-14 and z.hi>=18 for z in grid)
    measures['strict_two_axis_union']+=1
    assert box_cover(big,*p,c_all,sig,2,q,theta0,measures)
    assert not box_cover((big[0],big[1]+F(1,1000)),*p,c_all,sig,2,q,theta0,Counter())
    assert not box_cover(big,-30,18,c_all,sig,2,q,theta0,Counter())
    assert not box_cover(big,*p,c_all,(1,F(0),4,8),2,q,theta0,Counter())
    # One interval may be certified only by a union, even for two present times.
    for z in atoms(sorted({*big,theta0})):
        assert not member(-14,z,*sig) and not member(18,z,*sig)
    measures['unions_without_single_coverage']+=1

    # Same-source history, branch-specific winners and many distinct query intervals.
    actual={(5,1),(-14,0),(18,0)}
    history=[frozenset(actual)]
    for k in range(180):
        t=rng.choice([5,7,9,18,-14,23,-9,1,3])
        br=rng.choice([0,1,2,3]);e=(t,br)
        actual.symmetric_difference_update({e})
        history.append(frozenset(actual))
    # Separate workloads: inside the certified interval, and sometimes outside.
    stats=Counter();base=Counter();scenarios=0;strict_savings=0
    for k in range(360):
        E=history[rng.randrange(len(history))]
        if k%5==0:
            I=(big[0]-F(1,1500),big[1]+F(1,1500))
        elif k%7==0:
            I=big
        else:
            l=big[0]+(big[1]-big[0])*F(rng.randrange(50),100)
            u=big[0]+(big[1]-big[0])*F(rng.randrange(51,101),100)
            I=(l,u)
        ans=classify(E,I,*sig,c_all,theta0,stats)
        ref=full_reference(E,I,*sig,stats)
        assert ans[0]==ref[0],(k,E,I,ans,ref)
        if ans[0]=='STABLE':assert ans[1]==ref[1]
        if ans[0]=='CHANGES':
            for z,w in ans[1:]:
                assert I[0]<=z<=I[1] and w==winner(E,z,*sig)
            assert ans[1][1]!=ans[2][1]
            stats['changes_verified']+=1
        a0=baseline(E,I,*sig,base)
        assert a0[0]==ans[0]
        if a0[0]=='STABLE':assert a0[1]==ans[1]
        scenarios+=1
    matched_stats=stats.copy()
    # Dedicated dynamic version workload: every version retains the top OUT time 18,
    # time 5 remains IN and the full interval needs TWO covering boxes.
    stable={(5,1),(18,0),(-14,0)}; stable_versions=[frozenset(stable)]
    for k in range(180):
        e=(rng.choice([18,-14,5]),rng.randint(2,6))
        stable.symmetric_difference_update({e})
        stable_versions.append(frozenset(stable))
    stable_fast=Counter();stable_baseline=Counter();stable_ref=Counter()
    for k in range(360):
        E=stable_versions[rng.randrange(len(stable_versions))]
        lo=big[0]+(big[1]-big[0])*F(rng.randint(0,40),100)
        hi=big[0]+(big[1]-big[0])*F(rng.randint(60,100),100)
        I=(lo,hi)
        got=classify(E,I,*sig,c_all,theta0,stable_fast)
        old=baseline(E,I,*sig,stable_baseline)
        ref=full_reference(E,I,*sig,stable_ref)
        assert got[0]==old[0]==ref[0]=='STABLE'
        assert got[1]==old[1]==ref[1] and got[1][0]==5
    # Independent random signatures, certificates inapplicable -> oracle fallback.
    for k in range(140):
        E=history[rng.randrange(len(history))]
        j=rng.randint(-3,3); x=F(rng.randint(-3,3),rng.randint(2,7))
        a=rng.randint(-5,5);b=rng.randint(-5,5)
        L=F(rng.randint(-5,4),rng.randint(5,11));U=L+F(rng.randint(0,3),rng.randint(8,13))
        I=(L,U)
        ans=classify(E,I,j,x,a,b,c_all,theta0,stats)
        ref=full_reference(E,I,j,x,a,b,stats)
        assert ans[0]==ref[0],(k,ans,ref,I,j,x,a,b)
        if ans[0]=='STABLE':assert ans[1]==ref[1]
        if ans[0]=='CHANGES':
            assert winner(E,ans[1][0],j,x,a,b)!=winner(E,ans[2][0],j,x,a,b)
        scenarios+=1
    # Certificate is even sufficient for all θ on closed I; endpoint not omitted.
    endpoint_c1=make_box(2,q,theta0,(big[0],theta0),18,18,*sig)
    endpoint_c2=make_box(2,q,theta0,(theta0,big[1]),18,18,*sig)
    assert endpoint_c1 and endpoint_c2
    assert box_cover(big,18,18,[endpoint_c1,endpoint_c2],sig,2,q,theta0,Counter())
    measures['endpoint_covered']+=1
    output={'schema':'EM_R89_BOX_COVER_VERIFICATION_V1','seed':8920261112,
      'model':'auxiliary exact rational circular-source','frozen_science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
      'anchor':[1,16], 'big_interval':[[z.numerator,z.denominator] for z in big],
      'counterexample_to_single_envelope':'times [-14,18], residue 2 mod 16, target labels 4 and 8; full envelope rejected; left and right separately certified',
      'history_versions':len(history),'random_version_query_comparisons':scenarios,
      'box_groups_hit':stats['box_groups_hit'],'times_skipped':stats['times_skipped'],
      'matched_mixed_query_calls_fast':matched_stats['oracle_calls'],
      'matched_mixed_query_calls_baseline':base['oracle_calls'],
      'matched_mixed_query_atoms_fast':matched_stats['oracle_atoms'],
      'matched_mixed_query_atoms_baseline':base['oracle_atoms'],
      'dedicated_dynamic_versions':len(stable_versions),
      'dedicated_query_comparisons':360,
      'dedicated_fast_oracle_calls':stable_fast['oracle_calls'],
      'dedicated_baseline_oracle_calls':stable_baseline['oracle_calls'],
      'dedicated_fast_oracle_atoms':stable_fast['oracle_atoms'],
      'dedicated_baseline_oracle_atoms':stable_baseline['oracle_atoms'],
      'dedicated_group_skips':stable_fast['box_groups_hit'],
      'dedicated_reference_atoms':stable_ref['reference_atoms'],
      'accelerated_oracle_calls_all_500':stats['oracle_calls'],
      'independent_reference_atoms':stats['reference_atoms'],'verified_changes':stats['changes_verified'],
      'box_cover_atoms_tested':stats['cover_atoms'], 'cover_checks':dict(measures),
      'status':'ALL_ASSERTIONS_PASS','scope':'exact all-real rational closed intervals; conservative closed boxes; canonical original-label nonwrapping subinterval certificates; historical identities retained; finite tests only'}
    Path(__file__).with_name('verification.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print('R89_PASS',scenarios, stats['times_skipped'],matched_stats['oracle_calls'],base['oracle_calls'],stable_fast['oracle_calls'],stable_baseline['oracle_calls'])
    return output

if __name__=='__main__':test()
