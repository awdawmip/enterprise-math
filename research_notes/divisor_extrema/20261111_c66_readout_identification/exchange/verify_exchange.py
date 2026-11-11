"""Integer sign certificates for the local two-gap exchange 02 versus 20."""
from math import prod
from collections import Counter
import json


def dual_block(r,c,m):
    k=2*r+1
    stock=c-m
    remaining=range(stock,c+1)
    a=prod(k+4*n for n in remaining)
    b=prod(k+n for n in remaining)
    e=(k-1+stock)*prod(4*k+n for n in remaining)
    tau=28*(k-1+4*stock)*a*b
    return tau,a*e,tau,4**m*e*b


def multiply(u,v):
    a,b,c,d=u
    e,f,g,h=v
    return a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h


def difference(r,c):
    a,b,h,d=multiply(dual_block(r,c,0),dual_block(r-1,c,2))
    e,f,g,i=multiply(dual_block(r,c,2),dual_block(r-1,c-2,0))
    return a*g-e*h,a*i+b*g-e*d-f*h,b*i-f*d


def newton(values):
    firsts=[]
    while values:
        firsts.append(values[0])
        values=[y-x for x,y in zip(values,values[1:])]
    return firsts


def certificate(label, inventory, sign):
    degree=20
    coeffs=[]
    grid=[[difference(*inventory(x,y)) for y in range(degree+1)] for x in range(degree+1)]
    for index in range(3):
        by_y=[newton([sign*cell[index] for cell in row]) for row in grid]
        values={(i,j):v for j in range(degree+1) for i,v in enumerate(newton([row[j] for row in by_y]))}
        if min(values.values())<0 or values[0,0]<=0:
            raise AssertionError((label,index,[(k,str(v)[:30]) for k,v in values.items() if v<0][:10]))
        assert all(v==0 for (i,j),v in values.items() if i+j>degree)
        coeffs.append(dict(nonzero=sum(v>0 for v in values.values()),maximum_degree=max(i+j for (i,j),v in values.items() if v),
                           constant=str(values[0,0])))
    return dict(region=label,sign=sign,coefficients=coeffs)


def main():
    return [
        certificate("4<=c<=2r, even c",lambda x,y:(2+x+y,4+2*x),1),
        certificate("4<=c<=2r, odd c",lambda x,y:(3+x+y,5+2*x),1),
        certificate("c>=4r, r>=2",lambda x,y:(2+x,8+4*x+y),-1)
    ]


if __name__=='__main__':
    print(json.dumps(main(),indent=2))
