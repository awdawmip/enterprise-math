"""Independent order checks for the actual single-center perturbation and integer-column numerator."""
from fractions import Fraction as Q
from math import prod


def rising(s,d):
    return prod(range(s,s+d))


def parameters(start,landings):
    rows=[]
    r=len(landings)
    for i,x in enumerate(landings):
        K=2*(r-i)+1
        ni=(x+K-1)*rising(start+K+1,3*K)
        di=28*(4*x+K-1)*rising(x+K,3*K)
        rows.append((ni,di));start=x
    return rows


def cols(rows,V):
    a,b=1680,1680+V
    for n,d in reversed(rows):
        a,b=d*b,d*b+n*a
    return a,b


def differentiate(rows,p,k,pdist=Q(0)):
    y=p;v=pdist
    for i in range(len(rows)-1,-1,-1):
        a=Q(*rows[i]);old=y
        y=1/(1+a*old)
        v=-a*v*y*y + (old*y if i==k else 0)
    return y,v


def test(r):
    controls=0
    for c in (64,129,257,531):
        for shift in range(3):
            xs=[(c-7*i)//(2+i)+shift for i in range(r)]
            v=xs[-1]
            V=(v+2)*(v+3)*(v+4)
            W=Q(V,840)
            rows=parameters(c,xs)
            A,B=cols(rows,V);C,D=cols(rows,10*V)
            R=max(Q(A*D,B*C),Q(B*C,A*D))
            P=rising(c+2*r+2,3*(2*r+1))
            tail1=cols(rows[1:],V)[1]
            tail2=cols(rows[1:],10*V)[1]
            integer_numerator=1680*9*V*(xs[0]+2*r)*prod(n*d for n,d in rows[1:])
            den=tail2*B if A*D>B*C else tail1*D
            assert (R-1)/P==Q(integer_numerator,den)
            p,q=Q(1)/(1+W/2),Q(1)/(1+5*W)
            for i in range(r+1):
                xp,dx=differentiate(rows,p,i,p*W/6 if i==r else 0)
                yq,dy=differentiate(rows,q,i,q*W/Q(3,32) if i==r else 0)
                assert dx/xp != dy/yq
                controls+=1
    return controls


if __name__=="__main__":
    for r in (4,5): print("r",r,"nonzero logarithmic directions",test(r))
