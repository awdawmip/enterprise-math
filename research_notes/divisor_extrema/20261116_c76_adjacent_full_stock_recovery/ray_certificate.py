"""Formal leading coefficients and odd unit modulo 16 on two dyadic rays."""
from fractions import Fraction as F
from math import prod
import json


# A germ descriptor retains valuation slope, constant and residue of the odd unit.
# Products/quotients and finite integer shifts require only this information.
def factor(a,b=0):
    if not b:
        assert a
        p=abs(a)&-abs(a)
        return (1,p.bit_length()-1,(a//p)%16)
    p=abs(b)&-abs(b)
    return (0,p.bit_length()-1,(b//p)%16)


def mul(*ts):
    return sum(t[0] for t in ts),sum(t[1] for t in ts),prod(t[2] for t in ts)%16


def inv(t):
    a,b,u=t
    return -a,-b,pow(u,-1,16)


def unit(a,b):
    return mul(factor(0,a),inv(factor(0,b)))


def shift(a, b, base_unit):
    fs = [factor(a,i) for i in (range(1,b+1) if b>=0 else range(b+1,1))]
    val = mul(*fs)
    if b<0:
        val=inv(val)
    return mul(base_unit,val)


def factorial_ray(A,B):
    # Strip 2^(A X). For h>=4, the odd factorial of A*2^h is fixed mod 16.
    # Each new layer for the doubling multiplies by the product of all odd
    # residues mod 16 repeated A*2^h/16 times, hence by 1.
    n=A*16
    odd=prod(i//(i&-i) for i in range(1,n+1))%16
    return shift(A,B,(0,-A.bit_count(),odd))


def progress_ray(A,B,k):
    # At X=2^h,h>=6 the complete product up to AX has unit 1 by period 4
    # (the product of the four odd residues of the progression is an odd unit).
    fs = [(4*z+k)%16 for z in (range(1,B+1) if B>=0 else range(B+1,1))]
    val=prod(fs)%16
    return (0,0,val if B>=0 else pow(val,-1,16))


def rising_ray(A,B,L):
    return mul(*(factor(A,B+i) for i in range(L)))


def edge(n,s,k):
    A,B=n; C,D=s
    a=mul(factor(C,D+k-1),inv(factor(4*C,4*D+k-1)),inv(factor(0,28)),
          rising_ray(A,B+k+1,3*k),inv(rising_ray(C,D+k,3*k)))
    t=mul(a,(0,2*(B-D),1),factorial_ray(A,B+k),inv(factorial_ray(C,D+k-1)),
          progress_ray(C,D-1,k),inv(progress_ray(A,B,k)))
    return a,t


def tail(w):
    A,B=w
    return mul((0,2*(B-2),1),factorial_ray(A,B+1),inv(factor(0,6)),
               factor(0,5*9),inv(progress_ray(A,B,1)))


# Truncated approach is rigorous here because checking a nonzero Laurent
# leading term never relies on unseen higher powers.
N=10
def series(a):
    return ([F(a)]+[F(0)]*(N-1)) if not isinstance(a,list) else a


def add_s(a,b):
    return [x+y for x,y in zip(series(a),series(b))]


def mult_s(a,b):
    u,v=series(a),series(b)
    return [sum(u[j]*v[i-j] for j in range(i+1)) for i in range(N)]


def div_s(a,b):
    u,v=series(a),series(b)
    assert v[0], 'only division by a series unit'
    out=[]
    for i in range(N):
        out.append((u[i]-sum(v[j]*out[i-j] for j in range(1,i+1)))/v[0])
    return out


def rising_s(A,B,L):
    o=series(1)
    for i in range(L):
        o=mult_s(o,[F(B+i),F(A)]+[F(0)]*(N-2))
    return o


def block_s(n,s,k):
    A,B=n;C,D=s
    # Factor all powers of X first to ensure an invertible denominator.
    def prod_f(factors):
        exp,ser=0,series(1)
        for A,B in factors:
            if not B:exp+=1;ser=mult_s(ser,A)
            else:ser=mult_s(ser,[F(B),F(A)]+[F(0)]*(N-2))
        return exp,ser
    i,num=prod_f([(C,D+k-1)]+[(A,B+k+1+j) for j in range(3*k)])
    j,den=prod_f([(0,28),(4*C,4*D+k-1)]+[(C,D+k+l) for l in range(3*k)])
    assert i>=j
    return ([F(0)]*(i-j)+div_s(num,den))[:N]


def derivative_leads(n,v,w):
    a=block_s(n,v,5);b=block_s(v,w,3)
    W=div_s(rising_s(w[0],w[1]+2,3),840)
    p=div_s(1,add_s(1,div_s(W,2)))
    q=div_s(1,add_s(1,mult_s(5,W)))
    def den(t):return add_s(1,mult_s(b,t))
    def den2(t):return add_s(a,den(t))
    def sub(u,v):return add_s(u,mult_s(-1,v))
    def last(t,k):return div_s(t,mult_s(k,mult_s(den(t),den2(t))))
    derivatives=[sub(div_s(1,den(p)),div_s(1,den(q))),
                 mult_s(mult_s(-1,a),sub(div_s(p,den2(p)),div_s(q,den2(q)))),
                 mult_s(mult_s(a,mult_s(b,W)),sub(last(p,6),last(q,F(3,32))))]
    out=[]
    for derivative in derivatives:
        i=next(i for i,x in enumerate(derivative) if x)
        y=derivative[i]
        out.append(mul((i,0,1),unit(y.numerator,y.denominator)))
    return out


def check(n,v,w,expected):
    _,t=edge(n,v,5)
    _,s=edge(v,w,3)
    l=tail(w)
    coeff=derivative_leads(n,v,w)
    terms=[mul(a,b) for a,b in zip((t,s,l),coeff)]
    assert terms==expected
    return dict(stock_coefficients=[n,v,w],parameters=[t,s,l],derivatives=coeff,
                linear_terms=terms)


def main():
    results=[check((6,2),(4,-4),(2,-2),[(4,15,11),(3,-6,11),(3,-11,9)]),
             check((7,-16),(4,-6),(2,-2),[(3,-36,5),(2,-15,1),(2,-15,7)])]
    print(json.dumps(results,indent=2))

if __name__=='__main__':
    main()
