"""Exact polynomial derivative certificates for the two-stock center fiber bound."""
from math import comb
from fractions import Fraction as F
from functools import reduce
import json


def trim(P):
    while len(P)>1 and P[-1]==0:
        P.pop()
    return P

def add(P,Q):
    return trim([(P[i] if i<len(P) else 0)+(Q[i] if i<len(Q) else 0)
                 for i in range(max(len(P),len(Q)))])

def scale(P,a):
    return [a*b for b in P]

def mul(P,Q):
    R=[0]*(len(P)+len(Q)-1)
    for i,p in enumerate(P):
        for j,q in enumerate(Q):
            R[i+j]+=p*q
    return trim(R)

def product(items):
    return reduce(mul,items,[1])

def diff(P):
    return [i*P[i] for i in range(1,len(P))] or [0]

def difference_products(a,b,c,d):
    return add(mul(a,b),scale(mul(c,d),-1))

def log_derivative(n,d=(1,)):
    return difference_products(diff(n),d,diff(d),n),mul(n,d)

def quotient_elas(fn,fd,gn,gd):
    num,den=log_derivative(fn,fd)
    gnum,gden=log_derivative(gn,gd)
    return mul(num,gden),mul(den,gnum)

def shift(P,a):
    return [sum(P[j]*comb(j,i)*a**(j-i) for j in range(i,len(P))) for i in range(len(P))]

def signs(n,d,a,sign):
    D=difference_products(diff(n),d,n,diff(d))
    new=scale(shift(D,a),sign)
    assert all(v>0 for v in new)
    return dict(degree=len(new)-1,shift=a,derivative_sign=sign,
                smallest_signed_coefficient=str(min(new)),
                largest_signed_coefficient=str(max(new)))

def main():
    # Unneeded positive scalar factors are omitted throughout.
    V=product(([i,1] for i in (2,3,4)))
    E_num=product([[1,2],add(V,[168]),add(V,[1680])]+[[k,1] for k in range(5,12)])
    E_den=mul([2,1],[2,1])
    e=quotient_elas(E_num,E_den,V,[1])
    P=product(([k,1] for k in range(4,13)))
    B_num=product([[1,1]]+[[k,1] for k in range(5,20)])
    B_den=[4,1]
    r=quotient_elas(P,[1],B_num,B_den)
    # Underlying positive denominators plus their logarithmic derivatives.
    assert all(i>0 for i in shift(log_derivative(B_num,B_den)[0],4))
    assert all(i>0 for i in shift(log_derivative(E_num,E_den)[0],4))
    return dict(terminal_elasticity=signs(*e,4,1),
                stock_elasticity=signs(*r,4,-1))

if __name__=='__main__':
    print(json.dumps(main(),indent=2))
