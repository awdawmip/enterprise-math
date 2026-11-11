"""Exact intersections of first-gap joint signature hulls, using original three tails."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import cache
from pathlib import Path
import json
import sys


def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]


def minus(a,b):
    return (a[0]-b[0],a[1]-b[1])


def weighted(a,b,t):
    return tuple((1-t)*x+t*y for x,y in zip(a,b))


def decimal_upper_power(x):
    """The least integer p with x <= 10^p, using no floating arithmetic."""
    p=len(str(x.numerator))-len(str(x.denominator))
    return p if x<=Q(10)**p else p+1


def run(model_root):
    sys.path.insert(0,str(model_root.resolve()))
    from observed_four import tail_forms
    from suffix_limits import block,compose
    blocks=cache(block)
    terminals=cache(tail_forms)
    def sig(r,c,w):
        mat=(1,0,0,1)
        assert len(w)==r+1 and sum(w)==c-2
        for j,m in enumerate(w[:-1]):
            mat=compose(blocks(r-j,c,m),mat)
            c-=m
        a,b,e,d=mat
        z=[1+(p*a+s*e)/(p*b+s*d) for p,s in terminals(c)]
        return (min(z),max(z))
    paths=[(0,4,2),(0,6,0),(1,2,3),(1,3,2)]
    shapes=[sig(2,8,w) for w in paths]
    a,b,c,d=shapes
    left,right,offset=minus(b,a),minus(d,c),minus(c,a)
    den=cross(left,right)
    t0,t1=cross(offset,right)/den,cross(offset,left)/den
    assert 0<t0<1 and 0<t1<1 and weighted(a,b,t0)==weighted(c,d,t1)
    all_shapes=[sig(2,8,(i,j,6-i-j)) for i in range(7) for j in range(7-i)]
    assert len(set(all_shapes))==28
    small=dict(r=2,c=8,words=paths,convex_weights=list(map(str,(t0,t1))),different_actual_pairs=28,
               common_point=list(map(str,weighted(a,b,t0))))
    def extremal(r,c,m,thick,extra):
        consumed=12 if thick else c-m-2
        fixed=[m]+[0]*extra+[consumed]
        return fixed+[0]*(r-len(fixed))+[c-m-consumed-2]
    test=[]
    for r in (25,50,100):
        c=3*(2*r+1)//5
        x=Q(53,50)
        heights=[]
        for m in (0,1):
            pair=[]
            for thick in (False,True):
                chord=[]
                for extra in (0,1):
                    lo,hi=sig(r,c,extremal(r,c,m,thick,extra))
                    chord.append(((lo+hi)/2,hi-lo))
                (a,b),(c0,d)=chord
                mix=(x-a)/(c0-a)
                assert 0<mix<1
                pair.append((1-mix)*b+mix*d)
            heights.append(pair)
        thin=max(pair[0] for pair in heights)
        thick=min(pair[1] for pair in heights)
        assert thin<thick
        test.append(dict(r=r,c=c,center=str(x),thick_prefix_gap=12,
                         thin_chord_upper_power10=decimal_upper_power(thin),
                         thick_chord_lower_power10=decimal_upper_power(thick)-1))
    return dict(smallest_exhibited_r2_witness=small,positive_strip_examples=test)


if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--c64',type=Path,required=True)
    args=p.parse_args()
    print(json.dumps(run(args.c64),indent=2))
