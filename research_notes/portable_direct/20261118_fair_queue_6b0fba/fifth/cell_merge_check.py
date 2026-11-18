"""Self-contained planar joint-witness obstruction certificate for the public example."""
from argparse import ArgumentParser
from hashlib import sha256
from pathlib import Path
import sys
from fractions import Fraction as F
from itertools import combinations

# New triangles and four independently selectable readouts. Each observes the
# half-open bin [-1/2,1/2) of a scalar affine functional, at candidate c=(0,0).
positive = ((F(3,2),F(3,4)),(F(3,4),F(3,2)),(F(3,2),F(3,2)))
negative = tuple((-x,-y) for x,y in positive)
sources = (positive,negative)
readouts = ((1,0),(0,1),(-1,0),(0,-1))


def aff(p, operator):
    return operator.apply(p)[0]


def matches(point, indices, operators):
    return all(-F(1,2)<=aff(point,operators[i])<F(1,2) for i in indices)


def main():
    parser=ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    args=parser.parse_args()
    module=args.repo/"src"/"enterprise_math"/"brc_transport.py"
    assert sha256(module.read_bytes()).hexdigest()=="386f9b955a65aba938b08bf76f21330c612a7e7a396d0c3dd83523bfaaa9d4e7"
    sys.path.insert(0,str(args.repo/"src"))
    from enterprise_math.brc_transport import Affine
    operators=[Affine(((F(a,4),F(b,4)),(0,0)),(F(1,4),0)) for a,b in readouts]
    indices=tuple(range(4))
    assert matches((0,0),indices,operators)
    # Directed adjacent pairs rule out each entire triangle by linearity.
    # A matched first/second readout forces x+y<2; on P0 it is >=9/4.
    # A matched third/fourth readout forces -x-y<2; on P1 it is >=9/4.
    for sign,source in zip((1,-1),sources):
        assert min(sign*(x+y) for x,y in source)==F(9,4)
        assert max(max(abs(x),abs(y)) for x,y in source)==F(3,2)
    for size in range(4):
        for sub in combinations(indices,size):
            witnesses=[(source_id,p) for source_id,source in enumerate(sources)
                       for p in source if matches(p,sub,operators)]
            assert witnesses
            if size==3:
                print("times",tuple(t+1 for t in sub),"source",witnesses[0][0]+1,
                      "point",tuple(map(str,witnesses[0][1])))
    for pair, source in (((0,1),positive),((2,3),negative)):
        for i in pair:
            assert any(matches(p,[i],operators) for p in source)
    assert not matches((1,0),[0],operators) and matches((-3,0),[0],operators)
    print("15 proper subsets have a single witness; all four tests together are infeasible.")


if __name__ == "__main__":
    main()
