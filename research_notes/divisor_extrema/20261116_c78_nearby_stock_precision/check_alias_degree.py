"""Prove all ten quadratic monomials independent on the implicit C76 arc."""
from fractions import Fraction as Q
import json

from rational_interval_high import Interval, box
from alias_jets_high import J, compute


def center(x,y):
    return x**9/((1+112*x**15)*y**12)


def signed(x,y):
    A=4*x.sqrt().sqrt()**15
    D=4*(y/x).sqrt().sqrt()**9
    B=Q(7,16)*A**5
    L=Q(7,16)*D**5
    return B*L*(1-A)*(1-D)/(y.sqrt().sqrt()**3*(1+B*D)*(A+B*D))


def pivot_determinant(matrix):
    rows=[row.copy() for row in matrix]
    value=box(1)
    for k in range(len(rows)):
        # Largest magnitude midpoint is only a pivot-choice rule.
        j=max(range(k,len(rows)),key=lambda i:abs(rows[i][k].lo+rows[i][k].hi))
        if j!=k:
            rows[k],rows[j]=rows[j],rows[k]
            value=-value
        pivot=rows[k][k]
        assert pivot.lo*pivot.hi>0
        value=value*pivot
        for i in range(k+1,len(rows)):
            ratio=rows[i][k]/pivot
            for l in range(k+1,len(rows)):
                rows[i][l]=rows[i][l]-ratio*rows[k][l]
    return value


def check():
    m=Q(1,5)
    y0=Q('0.38767863872593543468499989301522663760840087384831652938382908528202066331421724')
    u0=Q('0.52081542166611978246043104628884966839423234480915481233758352391972543712032802')
    radius=Q(1,10**31)
    for sign in (-1,1):
        y=y0+sign*radius
        target=center(1-m,y)
        lo,hi=Q('0.52080'),Q('0.52083')
        assert center(lo,lo-m)>target>center(hi,hi-m)
        for _ in range(230):
            trial=(lo+hi)/2
            if center(trial,trial-m)>target:
                lo=trial
            else:
                hi=trial
        assert u0-3*radius < lo < hi < u0+3*radius
        root=Interval(lo,hi)
        residual=signed(box(1-m),box(y))-signed(root,root-m)
        assert residual.lo>0 if sign==1 else residual.hi<0
    J.n=9
    M,Y,U=compute(box(m),Interval(y0-radius,y0+radius),Interval(u0-3*radius,u0+3*radius))
    M=M-J([M.a[0]]);Y=Y-J([Y.a[0]]);U=U-J([U.a[0]])
    columns=[J(1),M,Y,U,M*M,M*Y,M*U,Y*Y,Y*U,U*U]
    # Constant and first-linear columns already echelon.
    value=pivot_determinant([[f.a[k] for f in columns[2:]] for k in range(2,10)])
    assert value.inside('-850000000000000','-840000000000000')
    return dict(parameter='1/5',root_radius='1e-31',
                degree_two_columns=10,highest_derivative=9,
                normalized_wronskian_range=['-850000000000000','-840000000000000'])
if __name__=='__main__':
    print(json.dumps(check(),indent=2))
