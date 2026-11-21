#!/usr/bin/env python3
"""C87: prove A(x)/x^2 >= 1/200 for every x in [1/8,1].
A(x)=integral_0^1 r^(1/20) H(r,x) dr.
Each certificate covers a complete x interval, never just sampled values.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,sys,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'inputs'/'c86'))
import certify_mellin_integral as base
I,Q=base.I,base.Q
TARGET=F(1,200)

def interval_box(terms,n,xa,xb):
    xc=(xa+xb)/2;dx=(xb-xa)/2
    center=I.rat(0);slope=I.rat(0);error=I.rat(0)
    interior=boundary=0
    for i in range(n):
        ra,rb=F(i,n),F(i+1,n)
        rm,r0,re=base.r_moments(ra,rb)
        ri=base.index((ra+rb)/2);si=base.index(r0*xc)
        h,_,hx=base.evaluate(terms[ri,si],r0,xc,gradient=True)
        center+=rm*h
        possible=[k for k in range(ri+1)
                  if rb*xb>base.CUTS[k] and ra*xa<base.CUTS[k+1]]
        hr=rb-ra
        if len(possible)==1:
            gr,gx,mrr,mxx,mrx=base.derivative_bounds(terms[ri,si],ra,rb,xa,xb)
            slope+=rm*hx
            err=mrr*hr*hr/8+mxx*dx*dx/2+gr*re
            interior+=1
        else:
            rc=(ra+rb)/2;gr=gx=F(0)
            for k in possible:
                _,dhr,dhx=base.evaluate(terms[ri,k],rc,xc,gradient=True)
                _,_,mrr,mxx,mrx=base.derivative_bounds(terms[ri,k],ra,rb,xa,xb)
                gr=max(gr,base.abs_upper(dhr)+mrr*hr/2+mrx*dx)
                gx=max(gx,base.abs_upper(dhx)+mrx*hr/2+mxx*dx)
            err=gr*hr+gx*dx
            boundary+=1
        error+=rm*err
    allerror=error+base.abs_upper(slope)*dx
    bound=center+I(-allerror.hi,allerror.hi)
    return bound,{"interior_r_cells":interior,"boundary_r_cells":boundary,
                  "center":center.json(),"linear_slope":slope.json(),
                  "error":allerror.json()}

def certify(n=96):
    assert n%6==0
    terms,source_hash=base.terms_from_json()
    stack=[(F(1,2),F(1),0),(F(1,4),F(1,2),0),(F(1,8),F(1,4),0)]
    accepted=[];trials=0;start=time.time()
    while stack:
        l,h,depth=stack.pop();trials+=1
        bound,detail=interval_box(terms,n,l,h)
        if F(bound.lo,Q)>=TARGET*h*h:
            accepted.append({"x_interval":[str(l),str(h)],"depth":depth,
                             "A_interval":bound.json(),**detail})
        else:
            if depth>=16:raise RuntimeError(("unresolved",l,h,bound.json()))
            m=(l+h)/2
            stack.append((m,h,depth+1));stack.append((l,m,depth+1))
        if trials%50==0:
            print(json.dumps({"trials":trials,"accepted":len(accepted),
                              "pending":len(stack),"seconds":round(time.time()-start,2)}),flush=True)
    accepted.sort(key=lambda z:F(z['x_interval'][0]))
    assert F(accepted[0]['x_interval'][0])==F(1,8)
    assert F(accepted[-1]['x_interval'][1])==1
    for a,b in zip(accepted,accepted[1:]):assert a['x_interval'][1]==b['x_interval'][0]
    minimum=min(F(int(a['A_interval']['lower_numerator']),Q)/
                F(a['x_interval'][1])**2 for a in accepted)
    assert minimum>=TARGET
    result={"schema":"C87_INTEGRATED_KERNEL_UNIFORM_CERTIFICATE_V1",
            "quantity":"A(x)/x^2","domain":["1/8","1"],
            "proved_lower_bound":str(TARGET),
            "actual_minimum_certified_ratio":str(minimum),
            "actual_minimum_decimal":float(minimum),
            "r_grid":n,"accepted_x_intervals":len(accepted),"trials":trials,
            "chamber_source_sha256":source_hash,
            "interval_bits":112,"integer_root_checks":base.ROOT_CHECKS,
            "proof_type":"weighted r-centroid cubature, whole x-interval Taylor, boundary Lipschitz",
            "status":"PASS","seconds":time.time()-start,
            "source_sha256":{
                "certify_integrated_kernel.py":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "inputs/c86/certify_mellin_integral.py":hashlib.sha256((HERE/'inputs/c86/certify_mellin_integral.py').read_bytes()).hexdigest(),
                "inputs/c86/triangle/c84_interval_kernel.py":hashlib.sha256((HERE/'inputs/c86/triangle/c84_interval_kernel.py').read_bytes()).hexdigest()},
            "intervals":accepted}
    (HERE/'integrated_kernel_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='intervals'},indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=96)
    args=ap.parse_args();certify(args.n)

