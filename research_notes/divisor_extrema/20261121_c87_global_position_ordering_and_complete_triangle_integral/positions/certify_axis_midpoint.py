#!/usr/bin/env python3
"""Integer-certified endpoint expansion and midpoint curvature for C87.

The finite chamber data and interval kernel are pinned copies from C86.
Floating powers only propose dyadic root brackets; integer inequalities verify
every bracket. All numerical conclusions use outward interval endpoints.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import argparse
import hashlib
import json
import time

from c84_interval_kernel import I, Q, ZETA

HERE=Path(__file__).resolve().parent
P=F(41,20)
GAMMA=F(1,20)
CUTS=[F(0),F(1,3),F(1,2),F(2,3),F(1)]
ROOT_BITS=48
NODE_BITS=40
ROOT_CHECKS=0


def root20(x):
    global ROOT_CHECKS
    x=F(x)
    assert x>=0
    if not x:return I.rat(0)
    den=1<<ROOT_BITS
    n=int(float(x)**.05*den)
    rhs=x.numerator << (20*ROOT_BITS)
    while n**20*x.denominator>rhs:n-=1
    while (n+1)**20*x.denominator<=rhs:n+=1
    assert n**20*x.denominator<=rhs<(n+1)**20*x.denominator
    ROOT_CHECKS+=1
    return I.rat(n,den)+I(0,Q//den)


def terms_from_json():
    source=HERE/'mellin_chambers.json'
    data=json.loads(source.read_text())
    terms={}
    assert list(map(F,data['cuts']))==CUTS
    assert F(data['exponent'])==P
    for ch in data['chambers']:
        terms[ch['r_index'],ch['s_index']]=[
          tuple(F(t[k]) for k in ('a_r','b_s','c_rs','weight')) for t in ch['terms']]
    assert set(terms)=={(ri,si)for ri in range(4)for si in range(ri+1)}
    return terms,hashlib.sha256(source.read_bytes()).hexdigest()


@lru_cache(None)
def r_moments(a,b):
    ar,br=root20(a),root20(b)
    mass=F(20,21)*(b*br-a*ar)
    first=F(20,41)*(b*b*br-a*a*ar)
    mean=first/mass
    node=F(((mean.lo+mean.hi)*(1<<NODE_BITS))//(2*Q),1<<NODE_BITS)
    error=max(abs(node-F(mean.lo,Q)),abs(node-F(mean.hi,Q)))
    assert a<=node<=b
    return mass,node,error


def scalar_value(rows,r):
    value=I.rat(0)
    for a,c,w in rows:
        z=a+c*r
        value+=w*z*z*root20(abs(z))
    return value


def scalar_bounds(rows,a,b):
    gradient=hessian=F(0)
    for z,c,w in rows:
        m=max(abs(z+c*a),abs(z+c*b))
        u=max(F(1),m)
        gradient+=P*abs(w)*m*u*abs(c)
        hessian+=P*(P-1)*abs(w)*u*c*c
    return gradient,hessian


def integrate_rows(families,n):
    total=I.rat(0)
    quadrature=I.rat(0)
    errors=I.rat(0)
    for i in range(n):
        a,b=F(i,n),F(i+1,n)
        ri=sum((a+b)/2>=c for c in CUTS[1:-1])
        rows=families[ri]
        mass,node,eps=r_moments(a,b)
        gr,rr=scalar_bounds(rows,a,b)
        error=rr*(b-a)**2/8+gr*eps
        value=mass*scalar_value(rows,node)
        bound=mass*error
        total+=value+I(-bound.hi,bound.hi)
        quadrature+=value
        errors+=bound
    return {'integral':total,'quadrature':quadrature,'error':errors}


def axis_expansion(terms,x0):
    a2_terms=defaultdict(F)
    remainder=F(0)
    for ri in range(4):
        lo,hi=CUTS[ri:ri+2]
        constant=defaultdict(F)
        linear=defaultdict(lambda:[F(0),F(0)])
        quadratic=defaultdict(lambda:[F(0),F(0),F(0)])
        for a,b,c,w in terms[ri,0]:
            if not a:continue
            assert a>0
            constant[a]+=w*a*a
            linear[a][0]+=P*w*a*b
            linear[a][1]+=P*w*a*c
            for k,v in enumerate((b*b,2*b*c,c*c)):
                quadratic[a][k]+=P*(P-1)*w*v/2
            m=max(abs(b+c*lo),abs(b+c*hi))
            assert m<=a
            lower=a-m*x0
            assert 0<lower<=1
            remainder+=abs(w)*m**3/lower*(hi-lo)*P*(P-1)*GAMMA/6
        assert all(v==0 for v in constant.values())
        assert all(v==[0,0]for v in linear.values())
        for a,coefficients in quadratic.items():
            for k,v in enumerate(coefficients,1):
                a2_terms[a*hi]+=v*hi**k/(GAMMA+k)
                if lo:a2_terms[a*lo]-=v*lo**k/(GAMMA+k)
    a2_terms={a:c for a,c in a2_terms.items()if c}
    assert a2_terms=={F(1,2):F(211,244),F(1,4):-F(101,122),F(1):F(23,61)}
    a2=I.rat(0)
    for a,c in a2_terms.items():a2+=c*root20(a)
    return a2,a2_terms,remainder


def certify(n):
    assert n>=12 and n%6==0
    start=time.time()
    terms,source_hash=terms_from_json()
    b_families={ri:[(b,c,w)for a,b,c,w in terms[ri,0]if not a]for ri in range(4)}
    mid_families={ri:[(a+b,c,w)for a,b,c,w in terms[ri,ri]]for ri in range(4)}
    b2=integrate_rows(b_families,n)
    a1=integrate_rows(mid_families,n)
    x0=F(1,8)
    a2,expression,remainder=axis_expansion(terms,x0)
    assert remainder==F(9318931,47520000)
    assert F(b2['integral'].lo,Q)>-F(433,1000)
    assert b2['integral'].hi<0
    axis_lower=a2-F(433,1000)*root20(x0)-remainder*x0
    assert F(axis_lower.lo,Q)>F(1,40)
    assert a1['integral'].lo>0
    factor=2/(ZETA*F(19,20)*F(21,20)*F(41,20))
    endpoint_curvature=-factor*a2
    midpoint_curvature=-8*factor*a1['integral']
    out={'schema':'C87_AXIS_MIDPOINT_CERTIFICATE_V1','n':n,
         'chamber_source_sha256':source_hash,'interval_bits':112,
         'root_bits':ROOT_BITS,'node_bits':NODE_BITS,'root_integer_checks':ROOT_CHECKS,
         'a2_expression':[{'base':str(a),'coefficient':str(c)}for a,c in sorted(expression.items())],
         'a2':a2.json(),
         'b2':{k:v.json()for k,v in b2.items()},
         'A_at_one':{k:v.json()for k,v in a1.items()},
         'axis_domain':'0 < x <= 1/8','axis_remainder_constant':str(remainder),
         'axis_lower_bound':axis_lower.json(),'uniform_A_over_x_squared_gt':'1/40',
         'endpoint_second_derivative':endpoint_curvature.json(),
         'midpoint_second_derivative':midpoint_curvature.json(),
         'certified_claims':{'axis_positive':True,'endpoint_curvature_negative':True,
                             'midpoint_curvature_negative':True},
         'seconds':time.time()-start}
    (HERE/'axis_midpoint_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    return out


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--n',type=int,default=192)
    args=ap.parse_args()
    certify(args.n)
