#!/usr/bin/env python3
"""Integer-verified weighted cubature of the C86 two-variable Mellin formula.

The floating power operation proposes an integer only.  Two integer inequalities
verify every twentieth-root enclosure before it enters the proof computation.
All subsequent arithmetic is outward fixed-point interval arithmetic.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import argparse, hashlib, json, sys, time

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'triangle'))
from c84_interval_kernel import I,Q,ZETA,decimal

ROOT_BITS=48
NODE_BITS=40
P=F(41,20)
GAMMA=F(1,20)
CUTS=(F(0),F(1,3),F(1,2),F(2,3),F(1))
ROOT_CHECKS=0

def cv(x):
    return I.cv(x)

def root20(x):
    global ROOT_CHECKS
    x=F(x)
    assert x>=0
    if not x:return I.rat(0)
    den=1<<ROOT_BITS
    # Heuristic proposal; the exact checks, not libm, establish validity.
    n=int(float(x)**.05*den)
    rhs=x.numerator << (20*ROOT_BITS)
    while n**20*x.denominator>rhs:n-=1
    while (n+1)**20*x.denominator<=rhs:n+=1
    assert n**20*x.denominator<=rhs<(n+1)**20*x.denominator
    ROOT_CHECKS+=1
    return I.rat(n,den)+I(0,Q//den)

def rational_log(x):
    """Positive log of a nearby rational via an exact geometric tail."""
    x=F(x);assert x>=1
    z=(x-1)/(x+1)
    if not z:return I.rat(0)
    assert 0<z<F(1,2)
    total=sum((2*z**(2*k+1)/F(2*k+1) for k in range(12)),F(0))
    tail=2*z**25/(25*(1-z*z))
    lo=cv(total);hi=cv(total+tail)
    return I(lo.lo,hi.hi)

def node_and_error(mean):
    n=((mean.lo+mean.hi)*(1<<NODE_BITS))//(2*Q)
    node=F(n,1<<NODE_BITS)
    eps=max(abs(node-F(mean.lo,Q)),abs(node-F(mean.hi,Q)))
    return node,eps

@lru_cache(None)
def r_moments(a,b):
    ar,br=root20(a),root20(b)
    mass=F(20,21)*(b*br-a*ar)
    first=F(20,41)*(b*b*br-a*a*ar)
    node,eps=node_and_error(first/mass)
    assert a<=node<=b
    return mass,node,eps

@lru_cache(None)
def x_moments(a,b):
    log=rational_log(b/a)
    mass=3*log+F(1,b)-F(1,a)
    first=3*(b-a)-log
    assert mass.lo>0
    node,eps=node_and_error(first/mass)
    assert a<=node<=b
    return mass,node,eps

def terms_from_json():
    path=HERE/'smallarea'/'mellin_chambers.json'
    data=json.loads(path.read_text())
    out={}
    for ch in data['chambers']:
        out[ch['r_index'],ch['s_index']]=[
          tuple(F(t[k]) for k in ('a_r','b_s','c_rs','weight'))
          for t in ch['terms']]
    return out,hashlib.sha256(path.read_bytes()).hexdigest()

def index(x):
    return min(3,sum(x>=c for c in CUTS[1:-1]))

def evaluate(terms,r,x,gradient=False):
    h=I.rat(0);hr=I.rat(0);hx=I.rat(0)
    for a,b,c,w in terms:
        z=a+b*x+c*r*x
        root=root20(abs(z))
        h+=w*z*z*root
        if gradient:
            d=P*w*z*root
            hr+=c*x*d
            hx+=(b+c*r)*d
    return h,hr,hx

def derivative_bounds(terms,ra,rb,xa,xb):
    """Exact rational bounds on |H_r|, |H_x| and the three Hessian entries."""
    gr=gx=rr=xx=rx=F(0)
    for a,b,c,w in terms:
        m=max(abs(a+b*x+c*r*x) for r in (ra,rb) for x in (xa,xb))
        # m**(1/20) <= max(1,m), including m=0.
        q=max(F(1),m)
        dr=abs(c)*xb
        dx=max(abs(b+c*ra),abs(b+c*rb))
        ww=abs(w)
        gr+=P*ww*m*q*dr
        gx+=P*ww*m*q*dx
        rr+=P*(P-1)*ww*q*dr*dr
        xx+=P*(P-1)*ww*q*dx*dx
        rx+=ww*(P*(P-1)*q*dr*dx+P*m*q*abs(c))
    return gr,gx,rr,xx,rx

def abs_upper(v):
    return F(max(abs(v.lo),abs(v.hi)),Q)

def certify(n,output):
    assert n%6==0 and n>=12
    terms,source_hash=terms_from_json()
    start=time.time();total=I.rat(0);quadrature=I.rat(0)
    error_total=I.rat(0);interior_error=I.rat(0);boundary_error=I.rat(0)
    interior=boundary=0
    rows=[]
    for i in range(n):
        ra,rb=F(i,n),F(i+1,n)
        rm,r0,re=r_moments(ra,rb)
        ri=index((ra+rb)/2)
        row_sum=I.rat(0)
        for j in range(n):
            xa,xb=F(1,3)+F(2*j,3*n),F(1,3)+F(2*(j+1),3*n)
            xm,x0,xe=x_moments(xa,xb)
            mass=rm*xm
            si=index(r0*x0)
            h,_,_=evaluate(terms[ri,si],r0,x0)
            possible=[k for k in range(ri+1) if rb*xb>CUTS[k] and ra*xa<CUTS[k+1]]
            hr,hx=rb-ra,xb-xa
            if len(possible)==1:
                gr,gx,mrr,mxx,mrx=derivative_bounds(terms[ri,si],ra,rb,xa,xb)
                error=(mrr*hr*hr+mxx*hx*hx)/8+gr*re+gx*xe
                interior+=1
                interior_error+=mass*error
            else:
                # H is continuous across every chamber edge.  A piecewise
                # gradient enclosure therefore gives a Lipschitz bound on the
                # entire rectangle, without any C1 matching assumption.
                rc,xc=(ra+rb)/2,(xa+xb)/2
                gr=gx=F(0)
                for k in possible:
                    _,dhr,dhx=evaluate(terms[ri,k],rc,xc,gradient=True)
                    _,_,mrr,mxx,mrx=derivative_bounds(terms[ri,k],ra,rb,xa,xb)
                    gr=max(gr,abs_upper(dhr)+mrr*hr/2+mrx*hx/2)
                    gx=max(gx,abs_upper(dhx)+mrx*hr/2+mxx*hx/2)
                # Every node lies in its rectangle, so these distances cover
                # both weighted-centroid and geometric-centroid locations.
                error=gr*hr+gx*hx
                boundary+=1
                boundary_error+=mass*error
            center=mass*h;err=mass*error
            bound=center+I(-err.hi,err.hi)
            total+=bound;row_sum+=bound;quadrature+=center;error_total+=err
        rows.append({'row':i,'interval':row_sum.json()})
        if (i+1)%max(1,n//6)==0:
            print(json.dumps({'row':i+1,'n':n,'seconds':round(time.time()-start,2),
                              'current_integral':total.json()['decimal']}),flush=True)
    factor=-1/(2*ZETA*F(19,20)*F(21,20)*F(41,20))
    difference=factor*total
    result={'schema':'C86_MELLIN_INTEGER_CUBATURE_V1',
      'quantity':'I_(1/4)-I_(1/2)',
      'domain':'r in [0,1], x in [1/3,1]',
      'measure':'r^(1/20) * (3*x-1)/x^2 dr dx',
      'grid':[n,n],'interval_bits':112,'root_bits':ROOT_BITS,'node_bits':NODE_BITS,
      'chamber_source_sha256':source_hash,'root_integer_checks':ROOT_CHECKS,
      'interior_cells':interior,'boundary_cells':boundary,
      'weighted_integral':total.json(),'quadrature_sum':quadrature.json(),
      'total_error_bound':error_total.json(),
      'interior_error':interior_error.json(),'boundary_error':boundary_error.json(),
      'moment_difference':difference.json(),
      'strict_negative_proved':difference.hi<0,
      'seconds':time.time()-start,'rows':rows}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='rows'},indent=2))
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--n',type=int,default=96)
    parser.add_argument('--output',type=Path,default=HERE/'mellin_integral_certificate.json')
    args=parser.parse_args()
    certify(args.n,args.output)
