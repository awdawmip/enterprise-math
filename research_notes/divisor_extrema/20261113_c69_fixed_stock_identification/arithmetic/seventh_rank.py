"""All 56 rank tests for the two shortest-block positions at depth seven."""
import json
import sympy as sp
from sixth_rank import P,dual_run,tangent_duals,gap_derivative


def main():
    r=7
    base=dual_run(r)
    jets=tangent_duals(r)
    values=[t[0] for t in jets]
    assert len(set(values))==r+1
    rows=[]
    for i,t in enumerate(jets):
        ds=[]
        for j in range(r+1):
            if i==j:
                ds.append(None)
                continue
            matrix=base+[list(t[1:]),gap_derivative(r,i),gap_derivative(r,j)]
            d=int(sp.Matrix(matrix).det())%P
            assert (d==0)==(i==0 or (i,j)==(1,0))
            ds.append(d)
        rows.append(ds)
    print(json.dumps(dict(prime=P, normalized_tangent_specializations=values,
                          nonzero_determinants=48, ordered_determinants=rows),indent=2))


if __name__=='__main__':
    main()
