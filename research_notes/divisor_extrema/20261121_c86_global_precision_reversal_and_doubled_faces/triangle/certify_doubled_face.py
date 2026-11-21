#!/usr/bin/env python3
"""C86 triangle constant: exact doubled-face Q_P correction."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,time
import c84_interval_kernel as k
import certify_extended as ex
import certify_middle_bounds as mid
import certify_farey_parallelogram as old
from certify_chordal_lower import parallelogram_upper
from doubled_face_integral import doubled_parallelogram

I,Q,ZETA=k.I,k.Q,k.ZETA

def certify(mesh=1024,qmesh=512,gmesh=512,agrid=64,dmesh=256,qpmesh=64):
    start=time.time()
    half=I.rat(1,2)
    head=4*half*half.sqrt()/3-4*k.C1*half*half*half.sqrt()/5
    exact=I.rat(0);middle=I.rat(0);improved_low=improved_high=0
    for j in range(mesh//2,9*mesh//2):
        l,h=F(j,mesh),F(j+1,mesh)
        val=ex.area_cell(l,h)
        if l<2:exact+=val;continue
        lv,hv=I.cv(l),I.cv(h)
        weight=4*(hv.sqrt()-lv.sqrt())
        lo=max(val.lo,(I(mid.short_lower(h,qmesh,gmesh))*weight).lo)
        hi=val.hi
        if h<=4:
            _,_,b1l,c1l=k.moments(l)
            _,_,b1h,c1h=k.moments(h)
            baselo=lv-k.C1*hv*hv+b1l-c1h
            basehi=hv-k.C1*lv*lv+b1h-c1l
            tl,th=ex.centered_triangle(l),ex.centered_triangle(h)
            al=F((l*agrid).numerator//(l*agrid).denominator,agrid)
            ah=F(-((-h*agrid).numerator//(-h*agrid).denominator),agrid)
            pl=old.parallelogram_lower(al,dmesh)
            pu=parallelogram_upper(ah,dmesh)
            hi=min(hi,((basehi-tl)*weight).hi,
                   ((basehi-(tl+I(pl))/2)*weight).hi)
            lo=max(lo,((baselo-th-I(pu))*weight).lo)
        if l>=F(8,3):hi=min(hi,(I(mid.general_row_upper(l))*weight).hi)
        if l>=4:hi=min(hi,(I(mid.row_upper(l))*weight).hi)
        previous_lo,previous_hi=lo,hi
        if h<=4:
            qpl=doubled_parallelogram(al,qpmesh).lo
            lo=max(lo,((baselo-th-I(pu)+I(qpl))*weight).lo)
            # The exact formula extends to A<4. For the upper endpoint
            # at A=4 retain C85's bound; no singular-endpoint evaluation.
            if ah<4:
                qph=doubled_parallelogram(ah,qpmesh).hi
                correction=tl if h<F(8,3) else I.rat(0)
                hi=min(hi,((basehi-I(pl)+I(qph)-correction)*weight).hi)
        if lo>previous_lo:improved_low+=1
        if hi<previous_hi:improved_high+=1
        assert lo<=hi,(l,h,k.decimal(lo),k.decimal(hi))
        middle+=I(lo,hi)
    tail=ex.tail_series();total=head+exact+middle+tail
    return {'schema':'C86_DOUBLED_FACE_CERTIFICATE_V1',
            'arithmetic':'integer outward intervals with denominator 2^112',
            'new_probability_bounds':'R-tau-Pi+QP <= Psi <= R-Pi+QP, 0<A<4; exact R-tau-Pi+QP for A<8/3',
            'area_mesh_per_unit':mesh,'short_direction_mesh':qmesh,
            'g_mesh_per_unit':gmesh,'parallelogram_area_grid':agrid,
            'parallelogram_d_mesh':dmesh,'QP_midpoint_mesh_per_u_piece':qpmesh,
            'further_improved_lower_cells':improved_low,
            'further_improved_upper_cells':improved_high,
            'head':head.json(),'exact_middle':exact.json(),
            'bounded_middle':middle.json(),'tail':tail.json(),'kappa3':total.json(),
            'seconds':time.time()-start,
            'source_sha256':{p:hashlib.sha256(Path(__file__).with_name(p).read_bytes()).hexdigest()
              for p in ['certify_doubled_face.py','doubled_face_integral.py',
                        'certify_chordal_lower.py','c84_interval_kernel.py',
                        'certify_extended.py','certify_middle_bounds.py',
                        'certify_farey_parallelogram.py']}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mesh',type=int,default=1024)
    p.add_argument('--qmesh',type=int,default=512);p.add_argument('--gmesh',type=int,default=512)
    p.add_argument('--agrid',type=int,default=64);p.add_argument('--dmesh',type=int,default=256)
    p.add_argument('--qpmesh',type=int,default=64)
    a=p.parse_args();d=certify(a.mesh,a.qmesh,a.gmesh,a.agrid,a.dmesh,a.qpmesh)
    Path(__file__).with_name('doubled_face_certificate.json').write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(d,indent=2))
