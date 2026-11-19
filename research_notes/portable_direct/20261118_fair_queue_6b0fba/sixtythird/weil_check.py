"""Exact rational inequalities, plus outward interval checks on Li's source responses."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from mpmath import iv

iv.dps=38
LI_SHA="ff635e2e070d442ba5b48b20a29a1a908942254887d46bacca77d9cd551f3e8d"


def interval(x):
    if isinstance(x,F):
        return iv.mpf(x.numerator)/x.denominator
    return iv.mpf(x)


def bounds(x,places=10):
    """An outward decimal lattice with explicitly checked interval comparisons."""
    unit=10**places
    lo=int(float(x.a)*unit)-2
    hi=int(float(x.b)*unit)+2
    assert interval(F(lo,unit)) <= x.a and x.b <= interval(F(hi,unit))
    return [str(F(lo,unit)),str(F(hi,unit))]


def exp_lower(x,n):
    term=total=F(1)
    for j in range(1,n+1):
        term*=x/j
        total+=term
    return total


def gram_entry(L,sgn,i,j):
    c,d=interval(2*i)+interval("0.5"),interval(2*j)+interval("0.5")
    z,w=iv.exp(-2*c*L),iv.exp(-2*d*L)
    crossing=2*L*z if i==j else (w-z)/(c-d)
    return ((1-z*w)/(c+d)+sgn*crossing)/iv.sqrt((1-sgn*z)*(1-sgn*w))


def head_entry(L,sgn,j,q):
    c=2*j+interval("0.5")
    k=(interval(q)+(interval("0.5") if sgn==-1 else 0))*iv.pi/L
    b=(-1)**q*iv.sqrt((1 if sgn==1 and q==0 else 2)/L)
    return b*iv.sqrt(1-sgn*iv.exp(-2*c*L))*c/(c*c+k*k)


def source_quadrature(L,sgn,j,q,n=128):
    """Use boxes in y=x/L, no oscillatory midpoint evaluations as certificates."""
    c=2*j+interval("0.5")
    out=interval(0)
    for i in range(n):
        y=iv.mpf([i,i+1])/n
        head=(1/iv.sqrt(L) if q==0 else iv.sqrt(2/L)*iv.cos(q*iv.pi*y)) if sgn==1 else (
              iv.sqrt(2/L)*iv.sin((q+interval("0.5"))*iv.pi*y))
        r=(iv.exp(-c*L*(1-y))+sgn*iv.exp(-c*L*(1+y)))/iv.sqrt(1-sgn*iv.exp(-2*c*L))
        out+=r*head
    out*=L/n
    direct=head_entry(L,sgn,j,q)
    assert out.a<=direct.a and direct.b<=out.b
    return bounds(direct)


def outlier(L,n=256):
    a=gram_entry(L,1,0,0)
    total=sum((gram_entry(L,1,0,j)**2 for j in range(1,n+1)),interval(0))
    # Each omitted positive scalar product is < (11/10)/j.
    mean=iv.mpf([total.a,(total+interval(F(121,100*n))).b])/a
    b=iv.pi/2
    lo=a+mean
    hi=(a+b+iv.sqrt((a-b)**2+4*a*mean))/2
    return dict(j_through=n,rank_one_gram=bounds(a),spectral_mean=bounds(mean),
                isolated_eigenvalue=[bounds(lo)[0],bounds(hi)[1]])


def quadratic_full_port(L,sgn,J):
    # Enclose J ||(I-P_1)S_J e_0||²/|e_0(L)|² by monotone double integrals.
    c=interval(2*J)+interval("0.5")
    ell=iv.ln(2)
    I=ell/(2*c)
    top=I+ell/c**2+1/(2*c**3)
    k=iv.pi/(2*L) if sgn==-1 else interval(0)
    rel=k**2/c**2+4*iv.exp(-c*L)/c
    head_b2=(2 if sgn==-1 else 1)/L
    head_max=(1+iv.exp(-2*c*L))*(1/(2*c)+1/c**2)
    lo=J*(I*(1-rel)**2-head_b2*head_max**2)
    hi=J*top*(1+rel)**2
    assert 0<lo.a and lo.b<ell.a/4 and ell.b/4<hi.a
    return [bounds(lo)[0],bounds(hi)[1]]


def moments():
    l=iv.ln(2)
    def A(n):
        x=l
        for j in range(1,n+1):
            x=1/interval(j)-x
        return x
    def gram(a,b):
        return (A(a)+A(b))/(2**(a+b+3)*(a+b+1))
    g00,g02,g22=gram(0,0),gram(0,2),gram(2,2)
    perp=g22-g02**2/g00
    exact=(64*l*l-32*l-5)/(46080*l)
    assert 0<exact.a and (perp-exact).a<=0<=(perp-exact).b
    return dict(first=bounds(g00),second_profile_orthogonalized=bounds(perp,14))


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--li-source",type=Path,help="optionally verify the frozen Li v2 source")
    args=p.parse_args()
    if args.li_source:
        assert hashlib.sha256(args.li_source.read_bytes()).hexdigest()==LI_SHA
    assert exp_lower(F(2),6)>7 and exp_lower(F(8,5),4)>4 and exp_lower(F(12,5),4)>7
    assert F(13,63)<F(1,4)<(1-F(1,7))/(4*F(81,100))
    assert (1-F(4,9))**2/(1+F(4,9))<F(1,4) and 5*16<81
    assert F(16,10)/(F(9,4)-1)+1+F(4,9)>F(22,14)
    rows={}
    for name,L in [("4/5",interval(F(4,5))),("log(5)/2",iv.ln(5)/2)]:
        rows[name]=dict(even_outlier=outlier(L),head_endpoint_quadratures={},scaled_Q1_energy={})
        for sgn in [1,-1]:
            rows[name]["head_endpoint_quadratures"][str(sgn)]=[
                source_quadrature(L,sgn,j,q) for j,q in [(0,0),(1,2),(7,1)]]
            rows[name]["scaled_Q1_energy"][str(sgn)]={str(J):quadratic_full_port(L,sgn,J)
                                                      for J in (16,64,256,1024)}
    print(json.dumps(dict(li_v2_sha256=LI_SHA,source_quadratures=12,
                          window_inequalities={"image_error_upper":"13/63","carleman_margin_lower":"1/4"},
                          limiting_norm= bounds(iv.pi/2),profile_moments=moments(),endpoints=rows),
                     ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
