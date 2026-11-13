"""Depth-five sensitivity ranks, from continuant derivatives and dual recurrences."""
from fractions import Fraction as Q
import json
import sympy as sp
from mixed_rank import P,add,mul,power,dual_run


def tangent_duals(r):
    def scalar(x):
        return (x % P, *(0 for _ in range(r)))
    xs=[scalar(1)]
    for i in range(1,r+1):
        xs.append(((13-i)*pow(13+i,-1,P)%P, *(int(i==j) for j in range(1,r+1))))
    one, minus, zero=scalar(1),scalar(-1),scalar(0)
    tail,sensitivity=zero,one
    layers=[]
    for i in range(r,0,-1):
        d=3*(2*(r-i+1)+1)
        rate=mul(scalar(4),power(mul(xs[i],power(xs[i-1],-1)),d))
        a=power(mul(scalar(7*pow(16,-1,P)),power(rate,4)),-1)
        center=power(add(one,mul(a,tail)),-1)
        slope=mul(mul(minus,a),power(center,2))
        layers.append((a,tail,sensitivity,center))
        sensitivity=mul(sensitivity,slope)
        tail=center
    layers.reverse()
    scale=power(xs[-1],-12)
    rows=[]
    for i in range(r+1):
        dr=zero
        for j,(a,tail,sensitivity,center) in enumerate(layers):
            if j<i:
                dr=add(dr,mul(scalar(-2),mul(mul(a,center),sensitivity)))
            elif j==i and i<r-1:
                dr=add(dr,mul(mul(power(tail,-1),center),sensitivity))
                break
            elif j==i and i==r-1:
                dr=add(dr,mul(minus,mul(mul(a,center),sensitivity)))
        if i>=r-1:
            dr=add(dr,minus)
        rows.append(mul(dr,scale))
    return rows


def log_sensitivity_check():
    # Compare the parenthesized first-order formula against differentiation of
    # the exact one-parameter rational map before any asymptotic simplification.
    p,delta=sp.symbols('p delta')
    a=[Q(5,3),Q(8,5),Q(3,4),Q(11,7),Q(7,12)]
    scalar=lambda t:sp.Rational(t.numerator,t.denominator)
    a=list(map(scalar,a))
    count=0
    for i in range(6):
        full=(1+delta)*p if i==5 else p
        for j in reversed(range(5)):
            full=sp.cancel((1+(delta*full if j==i else 0))/(1+a[j]*full))
        direct=sp.cancel(sp.diff(full,delta).subs(delta,0))
        if i>=4:
            direct=sp.cancel(direct/p)
        exact=sp.cancel(sp.diff(direct,p)/direct).subs(p,0)
        tails=[0]*6;derivs=[0]*6
        tails[-1],derivs[-1]=0,1
        for j in reversed(range(5)):
            c=1/(1+a[j]*tails[j+1])
            tails[j],derivs[j]=c,-a[j]*c**2*derivs[j+1]
        predicted=sp.Integer(0)
        for j in range(min(i,5)):
            predicted-=2*a[j]*tails[j]*derivs[j+1]
        if i<4:
            predicted+=tails[i]*derivs[i+1]/tails[i+1]
        if i==4:
            predicted-=a[i]*tails[i]*derivs[i+1]
        assert predicted==exact
        count+=1
    return count


def main():
    r=5
    prefix=dual_run(r)
    ranks=[int(sp.Matrix(prefix+[list(t[1:])]).det())%P for t in tangent_duals(r)]
    assert ranks[0]==0 and all(ranks[1:])
    print(json.dumps(dict(prime=P,exact_scalar_direction_checks=log_sensitivity_check(),
                          determinant_by_shortest_gap=ranks),indent=2))


if __name__=='__main__':
    main()
