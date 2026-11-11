"""One-sided certificate for every off-diagonal stock 2..96 at the C63 cut."""
import argparse
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

from finite_certificate import map_bounds, read_model, schedule_matrix


def round_down(value):
    """Keep about 60 binary digits. Exact downward rounding at all exponents."""
    exp = value.numerator.bit_length()-value.denominator.bit_length()-60
    scale = Q(2)**exp
    return (value//scale)*scale


def compute(model):
    stocks=range(2,97)
    previous={c:round_down(model.terminal_lower(c)) for c in stocks}
    for r in range(1,64):
        current={}
        for c in stocks:
            least=min(model.derivative_lower(q)*previous[c-m]
                      for m,q in enumerate(model.block_maps(r,c)))
            current[c]=round_down(least)
        previous=current
    canonical=(1,)*62+(0,0)
    U=map_bounds(schedule_matrix(canonical,model,True,64))[2]
    floors={}
    for c in stocks:
        if c==64:
            continue
        s=c-64
        weight=(Q(16)**s if s<=0 else Q(16)**(s-1)*Q(factorial(127+c),factorial(192)))
        floors[c]=(weight*previous[c])//U
    assert min(floors.values())>600
    return dict(cut=63,minimum_floor=min(floors.values()),
                at_stocks=[c for c,v in floors.items() if v==min(floors.values())],
                floor_by_stock=floors)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=compute(read_model(args.model))
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(result["minimum_floor"],result["at_stocks"])
