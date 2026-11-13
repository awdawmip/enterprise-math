"""Independent exact checks for the two-block partial-center and width identities."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from itertools import combinations, product
from math import prod
from pathlib import Path
import sys
import json


def order(x):
    def nv(n):
        return (n & -n).bit_length() - 1
    if not x:
        raise ValueError("zero has no finite valuation")
    return nv(x.numerator) - nv(x.denominator)


def params(k, n, v):
    # Use the unsimplified products from the positive three-state kernel.
    m = n-v
    numerator = prod(k+4*i for i in range(v, n+1))
    rho = Q(numerator, 4**m * prod(k+i for i in range(v, n+1)))
    tau = Q(28*(k-1+4*v)*numerator,
            4**m*(k-1+v)*prod(4*k+i for i in range(v, n+1)))
    a = Q((k-1+v)*prod(range(n+k+1, n+4*k+1)), 28*(k-1+4*v)*prod(range(v+k, v+4*k)))
    assert a == rho/tau
    return a, 1/tau, rho, tau


LABELS = [(Q(5), Q(3, 32)), (Q(5, 4), Q(3, 2)), (Q(1, 2), Q(6))]


def tail_values(w, l):
    W = Q((w+2)*(w+3)*(w+4), 840)
    return [(1+j*W)/(1+l*W/u) for j,u in LABELS]


def cells(c, v, w, keep):
    a,t,r1,h1 = params(5,c,v)
    b,s,r2,h2 = params(3,v,w)
    ell = Q(prod(4*i+4 for i in range(3,w+1)), prod(4*i+1 for i in range(3,w+1)))
    ts = [p if k else Q(0) for p,k in zip([t,s,ell],keep)]
    t_hold,s_hold,l_hold = ts
    C=(1+t_hold)/(a-t_hold)
    h=1/(a-t_hold)
    T = tail_values(w,l_hold)
    xs = [C+h*(b-s_hold)/(z+s_hold) for z in T]
    # Compare directly against composition of the *full* linear-fractional maps.
    for z,x in zip(T,xs):
        y=(z+b)/(z+s_hold)
        whole=(y+a)/(y+t_hold)
        assert x == 1/(whole-1)
    if not keep[2]:
        D,d=Q(5),Q(1,2)
        W=Q((w+2)*(w+3)*(w+4),840)
        width = xs[2]-xs[0]
        desired = h*(b-s_hold)*(D-d)*W/((1+s_hold+d*W)*(1+s_hold+D*W))
        assert desired==width
        base=(D*xs[0]-d*xs[2])/(D-d)
        assert base-C==(1+s_hold)*width/((D-d)*W)
    return xs


def check_native(prior):
    sys.path.insert(0,str(prior.resolve()))
    from mixed_kernel import responses
    words=partial=0
    for c in range(2,19):
        for v in range(2,c+1):
            for w in range(2,v+1):
                rows,_=responses(2,c,(c-v,v-w,w-2))
                z=[(7*rows[0][j]+rows[1][j])/(7*rows[0][j]+rows[2][j]) for j in (3,4,5)]
                full=cells(c,v,w,(1,1,1))
                assert [1/(x-1) for x in z]==full
                labels=(0,1 if w<=3 else 2)
                assert sorted((z[labels[0]],z[labels[1]]))==[min(z),max(z)]
                for mask in product((0,1),repeat=3):
                    cells(c,v,w,mask)
                    partial+=1
                words+=1
    return dict(stocks=17, native_words=words, native_columns=3*words,
                partial_masks_compared=partial)


def jets():
    ans=[]
    for count in range(3):
        for indices in combinations(range(3),count):
            gaps=[240,270,300]
            for i in indices:
                gaps[i]=7+i
            c=sum(gaps)+2;v=c-gaps[0];w=v-gaps[1]
            mask=tuple(int(i in indices) for i in range(3))
            x=cells(c,v,w,(1,1,1))
            U=cells(c,v,w,mask)
            agreements=[order(x[j]-U[j]) for j in (0,2)]
            unfrozen=min(g for i,g in enumerate(gaps) if not mask[i])
            assert min(agreements)>2*unfrozen
            ans.append(dict(gaps=gaps, kept=list(mask), agreements=agreements))
    return ans


def main():
    p=ArgumentParser(description=__doc__)
    p.add_argument('--prior',type=Path,required=True,help='C67/joint')
    args=p.parse_args()
    print(json.dumps(dict(native=check_native(args.prior),mixed_controls=jets(),
                          frozen_limit_base="449/3",zero_limit_max_base=112,
                          matched_central_width_ratio_power12="4/3",
                          matched_real_width_ratio_power12=1),indent=2))


if __name__=='__main__':
    main()
