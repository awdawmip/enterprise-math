"""Six-coordinate Jacobians after restricting the possible shortest-gap drifts."""
from fractions import Fraction as Q
import json
import sympy as sp
from fifth_rank import tangent_duals
from mixed_rank import P,dual_run


def gap_derivative(r,k):
    xs=[Q(13-i,13+i) for i in range(1,r+1)]
    values=[Q(0) for _ in xs]
    if k>0:
        values[k-1]+=4*xs[k-1]**3
    if k<r:
        values[k]-=4*xs[k]**3
    return [x.numerator*pow(x.denominator,-1,P)%P for x in values]


def main():
    r=6
    prefix=dual_run(r)
    ranks=[]
    for k,slope in enumerate(tangent_duals(r)):
        J=prefix+[list(slope[1:]),gap_derivative(r,k)]
        ranks.append(int(sp.Matrix(J).det())%P)
    assert ranks[0]==0 and all(ranks[1:])
    print(json.dumps(dict(prime=P,visible_blocks=r,determinant_by_shortest_gap=ranks),indent=2))


if __name__=='__main__':
    main()
