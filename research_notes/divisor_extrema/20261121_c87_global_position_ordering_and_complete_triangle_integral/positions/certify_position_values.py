#!/usr/bin/env python3
"""Integrate C87's existing whole-interval affine certificates in x.

No new cubature is performed. The stored A(x) affine models, their rigorous
uniform remainders, and the analytic x<=1/8 expansion are integrated exactly
against the position weights. All transcendental enclosures are directed.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

from c84_interval_kernel import I,Q,ZETA
from certify_axis_midpoint import root20

HERE=Path(__file__).resolve().parent
GAMMA=F(1,20)
X0=F(1,8)


def restore(row):
    assert int(row['denominator'])==Q
    return I(int(row['lower_numerator']),int(row['upper_numerator']))


def rational_log(x):
    x=F(x)
    assert x>=1
    z=(x-1)/(x+1)
    if not z:return I.rat(0)
    assert 0<z<F(1,2)
    total=sum((2*z**(2*k+1)/F(2*k+1)for k in range(12)),F(0))
    remainder=2*z**25/(25*(1-z*z))
    return I(I.cv(total).lo,I.cv(total+remainder).hi)


def power_moment(a,b,n):
    return (b**n*root20(b)-a**n*root20(a))/(n+GAMMA)


def models_from_certificate(data):
    assert data['status']=='PASS'
    assert data['chamber_source_sha256']==hashlib.sha256((HERE/'mellin_chambers.json').read_bytes()).hexdigest()
    rows=[]
    for row in data['intervals']:
        a,b=map(F,row['x_interval'])
        center=restore(row['center'])
        slope=restore(row['linear_slope'])
        error=restore(row['error'])
        dx=(b-a)/2
        slope_abs=F(max(abs(slope.lo),abs(slope.hi)),Q)
        # Parent construction is E_all = E_0 + cv(|slope|*dx), with
        # exact endpoint addition. Remove exactly that outward upper endpoint.
        remainder_numerator=error.hi-I.cv(slope_abs*dx).hi
        assert remainder_numerator>=0
        rows.append((a,b,center,slope,I(remainder_numerator)))
        assert F(int(row['A_interval']['lower_numerator']),Q)>=b*b/200
    assert rows[0][0]==X0 and rows[-1][1]==1
    assert all(a[1]==b[0]for a,b in zip(rows,rows[1:]))
    return rows


def axis_integrals(theta,q,a2,b2,E):
    if q>=X0:return I.rat(0),I.rat(0)
    a,b=q,X0
    m0=(1-theta)*(b*b-a*a)/2-theta*(b-a)
    mg=(1-theta)*power_moment(a,b,2)-theta*power_moment(a,b,1)
    m1=(1-theta)*(b**3-a**3)/3-theta*(b*b-a*a)/2
    value=a2*m0+b2*mg
    error=I.cv(E*m1)
    gap=value+I(-error.hi,error.hi)
    n0=(b-a)+(b*b-a*a)/2
    ng=power_moment(a,b,1)+power_moment(a,b,2)
    n1=(b*b-a*a)/2+(b**3-a**3)/3
    value=a2*n0+b2*ng
    error=I.cv(E*n1)
    derivative=value+I(-error.hi,error.hi)
    return gap,derivative


def value(theta,models,a2,b2,E):
    assert 0<=theta<=F(1,2)
    q=theta/(1-theta)
    gap,derivative=axis_integrals(theta,q,a2,b2,E)
    for left,right,center,slope,remainder in models:
        a,b=max(left,q),right
        if a>=b:continue
        xc=(left+right)/2
        logarithm=rational_log(b/a)
        m0=(1-theta)*logarithm+theta*(1/b-1/a)
        m1=(1-theta)*(b-a)-theta*logarithm-xc*m0
        assert m0.lo>=0
        integral=center*m0+slope*m1
        error=remainder*m0
        gap+=integral+I(-error.hi,error.hi)
        n0=logarithm+1/a-1/b
        n1=(b-a)+logarithm-xc*n0
        integral=center*n0+slope*n1
        error=remainder*n0
        derivative+=integral+I(-error.hi,error.hi)
    factor=2/(ZETA*F(19,20)*F(21,20)*F(41,20))
    return {'theta':str(theta),'I_theta_minus_mid':(-factor*gap).json(),
            'first_derivative':(factor*derivative).json()}


def main():
    family_path=HERE.parent/'integrated_kernel_certificate.json'
    axis_path=HERE/'axis_midpoint_certificate.json'
    family=json.loads(family_path.read_text())
    axis=json.loads(axis_path.read_text())
    assert family['chamber_source_sha256']==axis['chamber_source_sha256']
    models=models_from_certificate(family)
    a2=restore(axis['a2'])
    b2=restore(axis['b2']['integral'])
    E=F(axis['axis_remainder_constant'])
    positions=[F(0),F(1,64),F(1,32),F(1,16),F(1,10),F(1,8),F(1,6),F(1,5),
               F(1,4),F(1,3),F(2,5),F(9,20),F(49,100),F(1,2)]
    values=[value(theta,models,a2,b2,E)for theta in positions]
    for row in values[:-1]:
        assert int(row['I_theta_minus_mid']['upper_numerator'])<0
        assert int(row['first_derivative']['lower_numerator'])>0
    result={'schema':'C87_POSITION_VALUE_CERTIFICATE_V1','status':'PASS',
            'method':'Exact x-weight integration of stored uniform affine A models plus analytic axis expansion',
            'interval_bits':112,'certified_positions':len(positions),
            'input_sha256':{
                'integrated_kernel_certificate.json':hashlib.sha256(family_path.read_bytes()).hexdigest(),
                'axis_midpoint_certificate.json':hashlib.sha256(axis_path.read_bytes()).hexdigest()},
            'values':values}
    (HERE/'position_value_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
