"""Cyclic finite-field coefficient/translation tests. All example fields are fixed."""
from collections import Counter
from itertools import combinations_with_replacement
from math import isqrt, prod
import json


def arrays(R, field, omega, c):
    assert all(field % d for d in range(2, isqrt(field)+1))
    roots = [pow(omega, i, field) for i in range(R)]
    assert len(set(roots)) == R and pow(omega,R,field) == 1
    assert c and pow(c,R,field) != 1
    f = [(-omega-1 + z + c*pow(z,-1,field))%field for z in roots]
    g = [f[-x%R] for x in range(R)]
    assert Counter(f) == Counter(g)
    return f,g


def moment(a, offsets, field):
    return sum(prod(a[(x+t)%len(a)] for t in offsets) for x in range(len(a)))%field


def sample_alpha(a, omega, field):
    # z*f(z) has degree at most two. Its leading coefficient is the +1 mode.
    roots = [1, omega, omega*omega%field]
    coef = 0
    for i,z in enumerate(roots):
        den = prod(z-v for j,v in enumerate(roots) if i!=j)
        coef += z*a[i]*pow(den,-1,field)
    return coef%field


def check(R, field, omega, c, exhaustive):
    f,g = arrays(R,field,omega,c)
    inv = pow(omega,-1,field)
    def future(a):
        return [(a[(x+1)%R]-inv*a[x])%field for x in range(R)]
    ff, gg = future(f), future(g)
    assert ff.count(0)==1 and gg.count(0)==0
    for x in range(R):
        z=pow(omega,x,field)
        assert ff[x]==(omega-inv)*(z-1)%field
        assert gg[x]==(omega-inv)*(c*z-1)%field
    count = 0
    if exhaustive:
        # Translation fixes the first entry at zero; product is symmetric in the rest.
        for k in range(1,R+1):
            for rest in combinations_with_replacement(range(R), k-1):
                ts = (0,) + rest
                diff = (moment(f,ts,field)-moment(g,ts,field))%field
                w = pow(omega,sum(ts),field)
                rhs = R*(1-pow(c,R,field))*(w-pow(w,-1,field)) if k==R else 0
                assert diff == rhs%field
                count += 1
    ts=(0,)*(R-1)+(1,)
    witness=(moment(f,ts,field)-moment(g,ts,field))%field
    assert witness==R*(1-pow(c,R,field))*(omega-inv)%field and witness
    for i in range(R):
        for a,indicator in ((f,1),(g,0)):
            rot=a[i:]+a[:i]
            alpha=sample_alpha(rot,omega,field)
            cR=pow(c,R,field)
            assert (pow(alpha,R,field)-cR)*pow(1-cR,-1,field)%field == indicator
    row=dict(R=R,field=field,omega=omega,c=c,normalized_moment_entries_checked=count,
             first_differing_arity=R,ordered_shift_witness_difference=witness,
             zero_counts_after_kernel=[ff.count(0),gg.count(0)],
             multiplicative_depth=(R-1).bit_length())
    if R==4:
        row.update(f=f,reflection=g,future_f=ff,future_reflection=gg)
    return row


def histogram_fibers(R, field, omega):
    # Full two-frequency population with known constant C=0.
    roots=[pow(omega,x,field) for x in range(R)]
    fibers={}
    reverse={}
    ts=(0,)*(R-1)+(1,)
    neg=(0,)*(R-1)+(-1,)
    oriented=set()
    holes_by_histogram={}
    for a in range(1,field):
        for b in range(1,field):
            f=[(a*z+b*pow(z,-1,field))%field for z in roots]
            hist=tuple(sorted(f))
            X,Y=pow(a,R,field),pow(b,R,field)
            signature=(a*b%field,*sorted((X,Y)))
            assert fibers.setdefault(hist,signature)==signature
            assert reverse.setdefault(signature,hist)==hist
            diff=(moment(f,ts,field)-moment(f,neg,field))%field
            assert diff == R*(X-Y)*(omega-pow(omega,-1,field))%field
            oriented.add((hist,diff))
            holes_by_histogram.setdefault(hist,Counter())[int(a in roots)]+=1
            for t in range(field):
                # D_j(t,ab) is determined by D_0=2,D_1=t.
                u,v=2,t
                for _ in range(2,R+1):
                    u,v=v,(t*v-a*b*u)%field
                assert (v-X-Y-prod(t-h for h in f))%field==0
    errors=sum(min(h[0],h[1]) for h in holes_by_histogram.values())
    assert errors==R*(field-1-R)
    assert len(oriented)==(field-1)**2//R
    return dict(R=R,field=field,nonzero_pairs=(field-1)**2,
                histogram_classes=len(fibers),translation_classes=len(oriented),
                ambiguous_histograms=len(oriented)-len(fibers),
                optimum_uniform_wrong_inputs=errors)


def main():
    examples=[(3,7,2,3),(4,13,5,2),(5,11,3,2),(6,13,4,2),(8,17,2,3)]
    all_tensors=[check(*r,True) for r in examples]
    fixed=[]
    for R,field in ((3,7),(5,31),(7,127),(11,23),(13,8191),(17,131071)):
        assert pow(2,R,field)==1
        fixed.append(check(R,field,pow(2,-1,field),field-1,False))
    print(json.dumps({"full_tensor_small_groups":all_tensors,
                      "fixed_shift_minus_twice_identity":fixed,
                      "histogram_fibers":[histogram_fibers(R,field,omega)
                                          for R,field,omega,c in examples]},indent=2))


if __name__=="__main__":
    main()
