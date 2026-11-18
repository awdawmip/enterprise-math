"""Integer continuants, sign variations, and rational enclosures from the internal S,C."""
from fractions import Fraction as Q
from math import comb, isqrt
import json


def trig_bounds(x, cosine=False):
    """Alternating power series through index 22, then its next term (|x| <= 4)."""
    assert abs(x) <= 4
    if x < 0:
        a,b = trig_bounds(-x,cosine)
        return (a,b) if cosine else (-b,-a)
    q = 0 if cosine else 1
    term = Q(1) if cosine else x
    total = term
    for j in range(1,23):
        term *= -x*x/((2*j+q-1)*(2*j+q))
        total += term
    nxt = -term*x*x/((46+q-1)*(46+q))
    return min(total,total+nxt),max(total,total+nxt)


def scaled_bounds(lo,hi,n=12):
    base = 10**n
    return [(base*lo).__floor__(),(base*hi).__ceil__()]


def constants():
    den = 10**18
    tl = Q(3141592653589793238,den)
    th = tl+Q(1,den)
    assert trig_bounds(tl)[0]>0 and trig_bounds(th)[1]<0
    ul = Q(1324194449575502705,den)
    uh = ul+Q(1,den)
    for x,bit in ((ul,1),(uh,-1)):
        s,S = trig_bounds(x);c,C = trig_bounds(x,True)
        assert ((3*x*c-S)>0 if bit==1 else (3*x*C-s)<0)
    # S'>0 here, lower and upper cubes for kappa = 2*S(u)/(48*u)^(1/3).
    u_sin_lo = trig_bounds(ul)[0]
    u_sin_hi = trig_bounds(uh)[1]
    kl = Q(485986657922172548,den)
    kh = Q(485986657922172552,den)
    assert kl**3 < 8*u_sin_lo**3/(48*uh)
    assert kh**3 > 8*u_sin_hi**3/(48*ul)
    return tl,th,ul,uh,kl,kh


def determinant_and_count(M,x=None,squared=None):
    u = (x*x if squared is None else squared)/(M*M)
    top,den = u.numerator,u.denominator
    coeff = 2*den-top
    old,now = 1,coeff
    flips = int(now<0)
    sign = -1 if now<0 else 1
    for _ in range(2,M):
        old,now = now,coeff*now-den**2*old
        if now:
            next_sign = 1 if now>0 else -1
            flips += int(sign!=next_sign)
            sign=next_sign
    return now,den**(M-1)*M,flips


def count_tests(tl,th):
    out = {}
    for M,ks in ((16,[8,9,10]),(32,[13,16,17]),(64,[21,26,29]),
                 (128,[34,42,47]),(256,[54,67,76]),(512,[86,107,122])):
        for ell,k in enumerate(ks,1):
            for n in (k-1,k):
                observed = []
                for tau in (tl,th):
                    val,_,count = determinant_and_count(M,n*tau)
                    assert n*tau<2*M and val!=0
                    observed.append(count)
                assert observed[0]==observed[1]
                assert (observed[0]-n>=ell) == (n==k)
        out[M]=ks
    return out


def bulk_samples(tl,th,ul,uh):
    tc=(tl+th)/2
    uc=(ul+uh)/2
    ratios = []
    for q in (4,6,8,10,12,16):
        M=q**3
        # Fixed decimal below is only a probe placement. Actual error is certified below.
        n=round(Q(399084,100000)*q*q/tc)
        x=Q(round(1000*(n*tc-uc)),1000)
        assert 0<x<M
        Fnum,Fden,_=determinant_and_count(M,x)
        fm=Q(Fnum,Fden)
        lo,hi=trig_bounds(x-n*tc)
        displacement=n*(th-tl)/2
        lo,hi=lo-displacement,hi+displacement
        if n%2:
            lo,hi=-hi,-lo
        el,eh=fm-hi/x,fm-lo/x
        if eh<0:
            el,eh=-eh,-el
        assert el>0
        ratios.append({"M":M,"probe":str(x),"scaled_abs_error_units_1e12":scaled_bounds(q*q*el,q*q*eh)})
    return ratios


def edge_samples(tl,th):
    # Truncate the physical band at 2M-q/4, hence d/M^(1/3)=1/4.
    tc=(tl+th)/2
    records=[]
    for q in (4,6,8,10,12,16):
        M=q**3
        n=(Q(q*q,1)/tc-Q(1,2)).__ceil__()+1
        y=Q(round(1000*((n+Q(1,2))*tc-Q(1,24))),1000)
        xsq=4*M*M-y*y
        assert 2*M*M <= xsq <= (2*M-Q(q,4))**2
        scale=10**16
        xl=Q(isqrt((xsq*scale**2).__floor__()),scale)
        xh=xl+Q(1,scale)
        xc=(xl+xh)/2
        n=round(xc/tc)
        sl,sh=trig_bounds(xc-n*tc)
        rad=(xh-xl+n*(th-tl))/2
        sl,sh=sl-rad,sh+rad
        if n%2:
            sl,sh=-sh,-sl
        values=[u/v for u in (sl,sh) for v in (xl,xh)]
        fnum,fden,_=determinant_and_count(M,y)
        fm=(-1)**(M-1)*Q(fnum,fden)
        lo,hi=fm-max(values),fm-min(values)
        if hi<0:
            lo,hi=-hi,-lo
        assert lo>0
        records.append({"M":M,"reflected_probe":str(y),"scaled_abs_error_units_1e12":scaled_bounds(q*q*lo,q*q*hi)})
    return records


def parity_and_coefficients():
    checked=0
    for M in range(2,22):
        for t in [Q(0),Q(1,7),Q(M*M,3),Q(6*M*M,5),Q(4*M*M)]:
            n,d,_=determinant_and_count(M,squared=t)
            total=sum((-t)**j*comb(M+j,2*j+1)/Q(M**(2*j+1)) for j in range(M))
            assert n==d*total
            n2,d2,_=determinant_and_count(M,squared=4*M*M-t)
            assert n*d2==(-1)**(M-1)*n2*d
            checked+=1
    # Coefficients in x=A*M^(2/3)+B+C*M^(-2/3) at fixed phase slip:
    # B=b*A^3, C=c*A^5. Solve the two nonconstant Taylor coefficients.
    b=-Q(3,80)
    c=Q(1,22400)
    assert b/8+Q(3,640)==0
    assert (c+b*b)/8+Q(15,640)*b+Q(5,7168)==0
    return checked


if __name__=="__main__":
    tl,th,ul,uh,kl,kh=constants()
    print(json.dumps({"constant_enclosures":{"units":"1e-18","tau":scaled_bounds(tl,th,18),
                      "critical_u":scaled_bounds(ul,uh,18),"kappa":scaled_bounds(kl,kh,18)},
                      "determinant_reflections_and_coefficient_checks":parity_and_coefficients(),
                      "first_integer_with_extra_ell_modes_ell_1_2_3":count_tests(tl,th),
                      "bulk_probes":bulk_samples(tl,th,ul,uh),"upper_edge_probes":edge_samples(tl,th)},indent=2))
