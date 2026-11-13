"""Direct finite-depth seven controls for dyadic removal of a one-gap curve."""
from fractions import Fraction as Q
from math import prod
import json
from verify_density import coefficient,order


def compose(M,N):
    a,b,c,d=M
    e,f,g,h=N
    return a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h


def actual_and_curves(gaps):
    r=len(gaps)-1
    n=sum(gaps)+2
    params=[]
    for index,g in enumerate(gaps[:-1]):
        k=2*(r-index)+1
        s=n-g
        a=coefficient(k,n,s)
        irho=Q(4**g*prod(range(k+s,k+n+1)),prod(k+4*j for j in range(s,n+1)))
        params.append((a,a*irho))
        n=s
    W=Q((n+2)*(n+3)*(n+4),840)
    h=Q(prod(4*j+4 for j in range(3,n+1)),prod(4*j+1 for j in range(3,n+1)))
    output=[]
    prefix=(Q(1),Q(0),Q(0),Q(1))
    prefixes=[prefix]
    for a,t in params:
        prefix=compose(prefix,(Q(0),Q(1),a,Q(1)))
        prefixes.append(prefix)
    for j,u in [(Q(1,2),Q(6)),(Q(5),Q(3,32))]:
        tail=1/(1+j*W)
        real=(1+h*W/u)*tail
        centers=[tail]
        for a,t in reversed(params):
            real=(1+t*real)/(1+a*real)
            centers.append(1/(1+a*centers[-1]))
        centers.reverse()
        ds=[]
        for i in range(r+1):
            A,B,C,D=prefixes[i]
            if i==r:
                n1,n0,d1,d0=tail*W/u,tail,0,1
            else:
                old=centers[i+1]
                n1,n0,d1,d0=old,1,0,1+params[i][0]*old
            p,q=A*n1+B*d1,A*n0+B*d0
            h1,s=C*n1+D*d1,C*n0+D*d0
            assert q/s==centers[0]
            ds.append(((p*s-q*h1)/s**2,h1/s))
        output.append((real-centers[0],ds))
    return output


def main():
    controls=[]
    # In the close chart a second gap lies below twice the least gap;
    # in the other chart several powers of the least gap precede it.
    for base in [(62,95,130,152,186,217,246,273), (38,130,172,204,235,268,303,337)]:
        for shift in (0,1,3,7):
            g=base[shift:]+base[:shift]
            i,j=sorted(range(len(g)),key=g.__getitem__)[:2]
            (u,du),(v,dv)=actual_and_curves(g)
            slope=du[i][0]/dv[i][0]
            curve=(dv[i][1]-du[i][1])/dv[i][0]
            first=order(u)
            residual=order(u-slope*v-curve*u*v)
            leading=order(u-slope*v)
            below=(g[j]<2*g[i])
            assert abs(first-3*g[i])<60
            assert abs(residual-3*g[j])<60
            if below:
                assert abs(leading-3*g[j])<60
                assert order((u-slope*v)/(u*v)) < -30
            else:
                assert order((u-slope*v)/(u*v)-curve)>30
            controls.append(dict(gaps=g,shortest=i+1,second_shortest=j+1,first_order=first,
                                 untailored_normal_order=leading,exact_curve_residual_order=residual))
    print(json.dumps(dict(exact_finite_controls=controls),indent=2))


if __name__=='__main__':
    main()
