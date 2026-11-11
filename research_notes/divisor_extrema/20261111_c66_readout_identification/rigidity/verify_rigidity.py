"""Exact decoding, polynomial positivity and counting certificates for C66.

Uses the standard library. Optional --c64 points to the C64 checks directory
for direct verification with the original three columns at every terminal.
"""
import argparse
from fractions import Fraction as Q
from functools import cache
from math import comb, isqrt, prod
import json
from pathlib import Path
import sys


def negative_separator(r, c, m):
    k = 2*r + 1
    e = c - m - 1
    ns = range(c-m, c+1)
    d = 4**m * prod(k+n for n in ns)
    a = prod(k+4*n for n in ns)
    b = prod(4*k+n for n in ns)
    return (3 * 4**m * k * b * (4*k+e) * (k-1+e) * (k-2+e)
            - 28 * (k+e) * (d-a) * (k+4*e) * (k-1+4*e) * (k-2+4*e))


def positive_separator(r, c):
    k = 2*r + 1
    t = (4*k+c) * (k-1+c) * (k-2+c)
    u = 28 * (k+4*c) * (k-1+4*c) * (k-2+4*c)
    e = (k+4*c)*(k+4*c-4) - 4*(k+c)*(k+c-1)
    return 12*c*(k+c-1)*t - e*(t+u)


def newton_check(value, degree):
    """Bivariate Newton coefficients from exact forward differences at zero."""
    values = [[value(x, y) for y in range(degree+1)] for x in range(degree+1)]
    coeff = {(i, j): sum((-1)**(i+j-x-y) * comb(i,x)*comb(j,y)*values[x][y]
                          for x in range(i+1) for y in range(j+1))
             for i in range(degree+1) for j in range(degree+1)}
    assert all(a > 0 if i+j <= degree else a == 0 for (i,j),a in coeff.items())
    for x,y in [(0,0),(9,13),(51,1),(1,105)]:
        assert sum(a*comb(x,i)*comb(y,j) for (i,j),a in coeff.items()) == value(x,y)
    positive = [a for a in coeff.values() if a > 0]
    return dict(total_degree=degree,positive_count=len(positive),smallest=min(positive),
                at_origin=value(0,0))


def decode_region(r, c):
    return c <= r+1+r//51


def dp_distinguished(q):
    @cache
    def count(r,c):
        if r == 0:
            return 1
        if not decode_region(r,c):
            return 0
        return sum(count(r-1,c-m) for m in range(c-1))
    return count(q,q+1)


def recover_two_native(intervals, readings):
    """Recover the positive increasing odds from two original-history scales."""
    eq=[]
    for (a,b),h in zip(intervals,readings):
        w=(b-a)/(h-1)
        eq.append((w+b,w-a,a*b))
    (b1,l1,c1),(b2,l2,c2)=eq
    A=b2*c1-b1*c2
    B=b1*l2-c2-b2*l1+c1
    C=l2-l1
    if A:
        d=B*B-4*A*C
        sqrt_d=Q(isqrt(d.numerator),isqrt(d.denominator))
        assert sqrt_d**2==d
        roots={(-B+sqrt_d)/(2*A),(-B-sqrt_d)/(2*A)}
    else:
        roots={-C/B}
    candidates=[]
    for t in roots:
        if t<=-1 or l1-c1*t==0: continue
        p=(1+b1*t)/(l1-c1*t)
        if p>t and all((1+p*b)*(1+t*a)==h*(1+p*a)*(1+t*b)
                       for (a,b),h in zip(intervals,readings)):
            candidates.append((p,t))
    assert len(candidates)==1
    return candidates[0]


def direct_check(c64, q_max):
    sys.path.insert(0,str(c64.resolve()))
    import suffix_limits as model
    from observed_four import tail_forms
    branch_hulls = {}
    @cache
    def slope_hulls(r,c):
        if not r:
            slopes = [a/b for a,b in tail_forms(c)]
            return min(slopes),max(slopes)
        intervals=[]
        for m in range(c-1):
            a,b,h,d=model.block(r,c,m)
            assert a==0
            low,high=slope_hulls(r-1,c-m)
            ends=sorted([Q(h,b*(1+t)+d-b) for t in (low,high)])
            intervals.append(ends)
        branch_hulls[r,c] = intervals
        if decode_region(r,c):
            assert all(intervals[i][0]>intervals[i+1][1] for i in range(len(intervals)-1)),(r,c)
        return min(x[0] for x in intervals),max(x[1] for x in intervals)
    for q in range(2,q_max+1):
        slope_hulls(q,q+1)
    # Use only two exact synthetic common-input readings to reconstruct each
    # actual signature, then invert the first affine factor to recover every
    # gap up to the first stock outside the proved corridor.
    def reading(forms,x,y):
        ratios=[(a*y+b)/(a*x+b) for a,b in forms]
        return max(ratios)/min(ratios)
    tests,identified,prefixes=0,0,0
    for q in range(2,min(8,q_max)+1):
        outer=model.block(q+1,q+2,1)
        inner=model.compose(outer,model.block(q+2,q+3,1))
        canonical_intervals=[model.interval_image(mat,(Q(0),Q(1))) for mat in (outer,inner)]
        def visit(r,c,mat,path):
            nonlocal tests,identified,prefixes
            if r:
                for m in range(c-1):
                    visit(r-1,c-m,model.compose(model.block(r,c,m),mat),path+[m])
                return
            a,b,h,d=mat
            forms=[(p*a+t*h,p*b+t*d) for p,t in tail_forms(c)]
            mid=reading(forms,Q(0),Q(1,2))
            full=mid*reading(forms,Q(1,2),Q(1))
            den_slope=(2*mid-full-1)/(full-mid)
            num_slope=full-1+full*den_slope
            native=tuple(reading(forms,a,b) for a,b in canonical_intervals)
            assert recover_two_native(canonical_intervals,native)==(num_slope,den_slope)
            original={p/t for p,t in forms}
            assert {num_slope,den_slope} <= original
            cnow=q+1
            for step,m in enumerate(path):
                rnow=q-step
                if not decode_region(rnow,cnow): break
                chosen=[i for i,(lo,hi) in enumerate(branch_hulls[rnow,cnow])
                        if lo <= num_slope <= hi]
                assert chosen==[m], (q,path,step)
                _,b,h,d=model.block(rnow,cnow,m)
                num_slope=(Q(h,num_slope)-d)/b
                cnow-=m
                prefixes+=1
            else:
                assert cnow-2==c-2
                identified+=1
            tests+=1
        visit(q,q+1,(1,0,0,1),[])
    return dict(maximum_canonical_cut=q_max,stock_states=slope_hulls.cache_info().currsize,
                columns="all three",arithmetic="exact Fraction",two_probe_schedules=tests,
                original_history_scale_pairs=tests,
                recovered_decisions=prefixes,fully_decoded_schedules=identified)


def main(args):
    certificates={}
    for m in (1,2):
        certificates['base_m'+str(m)] = newton_check(
            lambda x,y:negative_separator(m+2+x+y,m+3+x,m), m+5)
    certificates['surplus_m0']=newton_check(
        lambda x,y:positive_separator(51*(x+1)+y,52*(x+1)+y+1),5)
    certificates['surplus_m2']=newton_check(
        lambda x,y:negative_separator(51*(x+1)+y,52*(x+1)+y+1,2),7)
    assert Q(7,4)*3*Q(17,8)**2*Q(8,23)**4 < Q(15,32)
    assert Q(17,8)**3/16 < 1
    def barrier(x):
        return 1792*x**4+895*x**3-342*x**2-233*x-32
    assert barrier(Q(50983984480,10**11)) < 0 < barrier(Q(50983984482,10**11))
    counting={}
    for q in (2,5,10,25,51,52,53,64,100,200,400):
        n=q-1
        total=comb(2*q-1,q)
        catalan=comb(2*n,n)//(n+1)
        cyclic=Q(comb(2*n-1,n-1)*((n+51)//52),n)
        guaranteed=max(catalan,-(-cyclic.numerator//cyclic.denominator))
        d=q//52+1
        largest=comb(2*q-1-d,q-d)
        assert Q(largest,total) <= Q(q,2*q-1)**d
        row=dict(catalan=catalan,guaranteed_identifiable=guaranteed,
                 total=total,unconditionally_decodable_gaps=d,largest_prefix_cylinder=largest)
        if q<=100:
            actual=dp_distinguished(q)
            assert actual>=guaranteed
            row['certified_corridor_count']=actual
        counting[str(q)]=row
    report=dict(newton_coefficients=certificates,
                positive_density_lower='q/[104(2q-1)] > 1/208',
                scalar_hull_asymptotic_boundary=['0.50983984480','0.50983984482'],
                counts=counting)
    if args.c64:
        report['native_slope_hulls']=direct_check(args.c64,args.max_cut)
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--c64', type=Path)
    parser.add_argument('--max-cut',type=int,default=24)
    main(parser.parse_args())
