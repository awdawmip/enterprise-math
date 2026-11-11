"""Exact accidental ties, quadratic-field decoding, and anchored crossing census."""
from argparse import ArgumentParser
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
import sys


def shape(odds):
    return F(*odds.p), F(*odds.q)


def read(params, t):
    a, b = params
    return (1 + a*t)/(1 + b*t)


def read_quadratic(params):
    # h=h0+h1*t, with t=sqrt(2)-1 and t*t=1-2*t.
    a, b = params
    den = 1 - 2*b - b*b
    return (1-2*b-a*b)/den, (a-b)/den


def restore_quadratic(value):
    h0, h1 = value
    b = (1-h0)/h1
    return h1 + b*(h0-2*h1), b


def restore_rational(h1, h2):
    # h1=R(1/2), h2=R(1); the linear equations have nonzero determinant.
    b = (2*(h1-1)-(h2-1))/(h2-h1)
    return h2-1+b*h2, b


def main(checks, prior, max_cut):
    sys.path[:0] = [str(checks.resolve()), str(prior.resolve())]
    from observed_four import tail_forms
    from verify_germs import all_suffixes, sorted_ids, inversion_count
    import suffix_limits as model
    terminal = lru_cache(None)(tail_forms)
    data = []
    witness = None
    for q in range(2, max_cut+1):
        words, odds = zip(*all_suffixes(q, model, terminal))
        shapes = list(map(shape, odds))
        start = sorted_ids([o.slope(F(0)) for o in odds])
        finish = sorted_ids([o.secant(F(0),F(1)) for o in odds])
        count = inversion_count(start,finish)
        heights = [max(abs(v.numerator),v.denominator) for pair in shapes for v in pair]
        max_height = max(heights)
        assert max_height <= (16*(q+2))**(8*q+2)
        for p in shapes:
            assert restore_rational(read(p,F(1,2)),read(p,F(1))) == p
            assert restore_quadratic(read_quadratic(p)) == p
        if q==3:
            pos={i:l for l,i in enumerate(finish)}
            i,j=next((i,j) for i,j in zip(start,start[1:]) if pos[i]>pos[j])
            a,b=shapes[i]
            c,d=shapes[j]
            t=-(a+d-b-c)/(a*d-b*c)
            assert 0<t<1 and read(shapes[i],t)==read(shapes[j],t)
            assert read(shapes[i],t/2)<read(shapes[j],t/2)
            assert read(shapes[i],(1+t)/2)>read(shapes[j],(1+t)/2)
            witness=dict(words=[words[i],words[j]],shapes=[[str(v) for v in s] for s in (shapes[i],shapes[j])],
                         second_input_at_equal_H=str(t),common_H=str(read(shapes[i],t)))
        data.append(dict(q=q,suffixes=len(odds),anchored_crossing_pairs=count,
                         largest_reduced_slope_height_bits=max_height.bit_length()))
    assert witness is not None
    return dict(anchored_pair_experiment="left endpoint 0; right endpoint t in (0,1)",cuts=data,
                physical_readout_witness=witness)


if __name__=="__main__":
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--checks',type=Path,required=True)
    parser.add_argument('--prior',type=Path,required=True)
    parser.add_argument('--max-cut',type=int,default=10)
    args=parser.parse_args()
    print(json.dumps(main(args.checks,args.prior,args.max_cut),indent=2))
