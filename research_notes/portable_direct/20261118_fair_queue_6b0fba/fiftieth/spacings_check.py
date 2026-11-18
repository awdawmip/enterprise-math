"""Finite-field image windows and fibre masses; all reported data are exact."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import isqrt,prod
import json


def chi_table(p):
    result=[-1]*p
    result[0]=0
    for x in range(1,p):
        result[x*x%p]=1
    return result


def mapping(p):
    # Use p to denote infinity.
    return [p if x in (0,p) else (-(6*x*x+1)*pow(2*x,-1,p))%p for x in range(p+1)]


def push(weights,f):
    out=[0]*len(f)
    for x,y in enumerate(f):
        out[y]+=weights[x]
    return out


def cyclic_sums(weights,h):
    n=len(weights)
    running=sum(weights[:h])
    out=[]
    for t in range(n):
        out.append(running)
        running+=weights[(t+h)%n]-weights[t]
    return out


def exact_stats(values):
    size=len(values)
    mean=Fraction(sum(values),size)
    second=Fraction(sum(z*z for z in values),size)
    return {'mean':str(mean),'variance':str(second-mean*mean),'number_zero':values.count(0)}


def theta(k):
    q=Fraction(1)
    for _ in range(k): q=q-q*q/2
    return q


def finite_window(p,k):
    f=mapping(p)
    weights=[1]*(p+1)
    for _ in range(k): weights=push(weights,f)
    assert sum(weights)==p+1 and max(weights)<=2**k
    assert all(weights[x]==weights[-x%p] for x in range(p))
    support=[int(z>0) for z in weights[:p]]
    q=theta(k)
    h=int(1/q+Fraction(1,2))
    population=cyclic_sums(support,h)
    mass=cyclic_sums(weights[:p],h)
    pattern=sum(support[x]*support[(x+1)%p]*support[(x+3)%p] for x in range(p))
    assert [v==0 for v in population]==[v==0 for v in mass]
    assert sum(population)==h*sum(support) and sum(mass)==h*(p+1-weights[p])
    hits=[x for x,z in enumerate(support) if z]
    gaps=[(hits[(i+1)%len(hits)]-t)%p for i,t in enumerate(hits)]
    assert sum(gaps)==p
    thresholds=[h//2,h,2*h]
    return {'prime':p,'depth':k,'window_length':h,'N_targets':len(hits),
            'outside_affine_fibres':weights[p],'support_triple_offsets_0_1_3':pattern,
            'unscaled_hit_count':exact_stats(population),'unscaled_preimage_mass':exact_stats(mass),
            'Palm_forward_gap_strictly_above':dict(zip(thresholds,[sum(g>t for g in gaps) for t in thresholds]))}


def level_one_tests():
    cases=colliding=0
    for p in range(5,150):
        if any(p%i==0 for i in range(2,isqrt(p)+1)): continue
        chi=chi_table(p)
        z=[x for x in range(p) if x*x%p==6%p]
        image=set(mapping(p))-{p}
        assert image=={x for x in range(p) if chi[(x*x-6)%p]>=0}
        for h in range(1,p):
            joint=sum((x+h)%p in image for x in image)
            if h*h%p==24%p:
                numerator=p+2-chi[-1]+2*chi[2]
                colliding+=1
            else:
                a=-1-sum(chi[((x*x-6)*((x+h)**2-6))%p] for x in range(p))
                cross=sum(chi[(h*h+2*h*r)%p] for r in z)
                numerator=p-3+2*len(z)+2*cross-a
            assert numerator==4*joint
            cases+=1
    return {'shift_tests':cases,'singular_tests':colliding}


def branch_tests():
    """Quadratic elements represented as a+b/√6, hence equality is exact in the nonsplit field."""
    result={}
    for p in (101,103,107,109,127,131,137):
        depth=4
        chi=chi_table(p)
        v=1
        posts=[]
        all_finite=True
        for i in range(1,depth+1):
            if not v:
                all_finite=False
                break
            v=-3*(v+pow(v,-1,p))%p
            posts.extend([v,(-v)%p])
        if not all_finite or len(set(posts))<2*depth: continue
        if chi[6]>0:
            c=next(x for x in range(p) if 6*x*x%p==1)
            B={c*u%p for u in posts}
            dif={(b-a)%p for a in B for b in B}-{0}
            for h in range(1,p):
                assert (h in dif)==bool(B.intersection({(x+h)%p for x in B}))
        else:
            B={(0,u) for u in posts}
            dif=set()
            for h in range(1,p):
                assert not B.intersection({(h,u) for _,u in B})
        assert len(dif)<=4*depth*depth
        result[p]={'legendre_6':chi[6],'depth':depth,'number_finite_branch_values':len(B),
                   'number_bad_nonzero_shifts':len(dif)}
    return result


def transfer_tests():
    checks=0
    for p in (5,7,11,13,17,19,23,29,31,37,41,43):
        f=mapping(p)
        weights=[1]*(p+1)
        direct=list(range(p+1))
        for k in range(1,6):
            weights=push(weights,f)
            direct=[f[y] for y in direct]
            counted=Counter(direct)
            assert weights==[counted[y] for y in range(p+1)]
            h=min(k+1,p)
            fast=cyclic_sums(weights[:p],h)
            slow=[sum((y-t)%p<h for y in direct if y!=p) for t in range(p)]
            assert fast==slow
            checks+=1
    return checks


def main():
    examples=[finite_window(p,k) for p in (10007,65537,100003) for k in (2,4,6)]
    print(json.dumps({'depth_one_comparison_to_prior_quartic':level_one_tests(),
                      'all_preimages_direct_vs_transfer':transfer_tests(),
                      'branch_translation_controls':branch_tests(),
                      'cyclic_finite_range_counts':examples},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
