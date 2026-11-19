"""C84 exact elementary kernel for the one-dimensional F3 integral.

The formula is analytic. mpmath evaluations are exploratory, not interval
certificates. All inner antiderivatives are explicit; no nested quadrature.
"""
import argparse
import json
from pathlib import Path
import mpmath as mp


def rational_moments(r, D):
    u=mp.atanh(D/r)
    R0=u/r
    R1=-mp.log1p(-(D/r)**2)/2
    R2=r*r*R0-D
    R3=r*r*R1-D*D/2
    S0=D/(2*r*r*(r*r-D*D))+u/(2*r**3)
    S2=r*r*S0-R0
    return R0,R1,R2,R3,S0,S2


def log_minus(r,D):
    if D == r:
        return 2*r*mp.log(2*r)-2*r, 2*r**3*mp.log(2*r)/3-8*r**3/9
    u=mp.atanh(D/r)
    v=mp.log(r*r-D*D)
    return D*v+2*r*u-2*D, D**3*v/3+2*r**3*u/3-2*r*r*D/3-2*D**3/9


def log_plus(r,D):
    u=mp.atan(D/r)
    v=mp.log(r*r+D*D)
    return D*v-2*D+2*r*u, D**3*v/3-2*D**3/9+2*r*r*D/3-2*r**3*u/3


def atanh_odd(r,D):
    if D == r:
        return r*r/2,r**4/3
    u=mp.atanh(D/r)
    return (D*D-r*r)*u/2+r*D/2, (D**4-r**4)*u/4+r**3*D/4+r*D**3/12


def atanh_even(r,D):
    u=mp.atanh(D/r)
    R1=-mp.log1p(-(D/r)**2)/2
    return D*u-r*R1, D**3*u/3-r*(r*r*R1-D*D/2)/3


def kernel(A,z):
    q=mp.sqrt(max(mp.mpf('0'),z*z-4*A))
    b=2-z
    D=q if z <= 1+A else b
    if D <= 0:return mp.mpf('0')
    k=mp.sqrt(8*A-z*z)
    K=4*A
    c=mp.mpf(9)*z/2-12
    e=4-z
    C0=4-2*z+3*q
    P1=-4+mp.mpf(5)*z/2
    value=(C0*(b*b*D-D**3/3)-mp.mpf(9)/2*(b*b*D*D/2-D**4/4))/4
    R0,R1,R2,R3,S0,S2=rational_moments(z,D)
    value+=K/4*(P1*(b*b*R0-R2)+mp.mpf(3)/2*(b*b*R1-R3))
    value-=z*K*K/8*(b*b*S0-S2)
    for coefficient,(L0,L2) in [(c,log_minus(q,D)),(e,log_plus(k,D)),(-c-e,log_minus(z,D))]:
        value+=coefficient*(b*b*L0-L2)/4
    A1,A3=atanh_odd(q,D)
    A0,A2=atanh_even(z,D)
    value+=-mp.mpf(3)/4*(b*b*A1-A3)+3*z/4*(b*b*A0-A2)
    return value


def correction(a):
    a=mp.mpf(a)
    if a>=mp.mpf('0.5'):return mp.mpf('0')
    if a<=mp.mpf('0.25'):raise ValueError('proved interval is a>1/4')
    A=2*a
    result=mp.quad(lambda z: kernel(A,z),[2*mp.sqrt(A),1+A,2])
    return result/(mp.zeta(2)*A)


def evaluate(a):
    a=mp.mpf(a)
    c=correction(a)
    return 1-mp.mpf(161)/(80*mp.pi**2*a)+c,c


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--digits',type=int,default=40)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    mp.mp.dps=args.digits
    rows=[]
    for a in [mp.mpf(13)/50,mp.mpf(3)/10,mp.mpf(1)/3,mp.mpf(2)/5,mp.mpf(49)/100,mp.mpf(499)/1000]:
        value,c=evaluate(a)
        row={'a':str(a),'F3':str(value),'correction':str(c)}
        rows.append(row)
        print(row,flush=True)
    data={'scope':'Exploratory mpmath evaluations of a proved one-dimensional exact formula; not rigorous numerical enclosures.','working_decimal_digits':args.digits,'rows':rows}
    if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n')
