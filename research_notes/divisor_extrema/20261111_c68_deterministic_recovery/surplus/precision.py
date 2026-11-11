"""Exact first variation of the single anchored H for the two-block resonance."""
from fractions import Fraction as F
from math import gcd,lcm
import json

W=(448,4,448,1)
B=(-1680,-3,-1680,0)
def matmul(u,v):
    a,b,h,d=u;e,f,g,i=v
    return a*e+b*g,a*f+b*i,h*e+d*g,h*f+d*i
def power(n):
    w=(1,0,0,1)
    for _ in range(n):w=matmul(w,W)
    return w
def derivatives(r):
    a,b,h,d=power(r)
    rows=[]
    for i in range(r):
        k=2*(r-i)+1
        s=matmul(matmul(power(i),B),power(r-1-i))
        u,v,y,z=(k*t for t in s)
        rows.append((F(b*u-a*v,b*b)+F(3*a,4*b),F(d*y-h*z,d*d)+F(3*h,4*d)))
    return rows
def main():
    a,b,h,d=power(2)
    row=derivatives(2)
    h0,h1=[x-y for x,y in row]
    vals=[-h1,h0]
    den=lcm(*(v.denominator for v in vals))
    ns=[int(den*v) for v in vals]
    gaps=[x//gcd(*ns) for x in ns]
    assert gaps==[29002230,46552051]
    slopes=[sum(v*a[i] for a,v in zip(row,gaps)) for i in range(2)]
    assert slopes[0]==slopes[1]==-40550508096
    coeff=-slopes[0]*(F(a,b)-F(h,d))*(9-F(15,32)**2)
    assert coeff>0
    return dict(depth=2,first=gaps,second=[0,0],derivative_rows=[[str(v) for v in z] for z in row],
                common_first_order_shift=str(slopes[0]),exponent='5/2',
                limit_of_c_times_H_difference_over_Y_squared=str(coeff))
if __name__=='__main__':print(json.dumps(main(),indent=2))
