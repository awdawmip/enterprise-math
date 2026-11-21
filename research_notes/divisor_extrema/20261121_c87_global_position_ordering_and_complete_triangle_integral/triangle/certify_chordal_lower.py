#!/usr/bin/env python3
"""C86 chordal Farey identity lower bound; C85 upper bounds retained."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import argparse,hashlib,json,time
import c84_interval_kernel as k
import certify_extended as ex
import certify_middle_bounds as mid
import certify_farey_parallelogram as old

I,Q,ZETA=k.I,k.Q,k.ZETA

@lru_cache(None)
def parallelogram_upper(a,dmesh=256):
    """Upper enclosure of every d-cell, including the support-crossing cell."""
    a=F(a)
    assert a<=4
    if a<=2:return 0
    total=I.rat(0)
    for j in range(dmesh//2,dmesh):
        l,h=F(j,dmesh),F(j+1,dmesh)
        if 2*a*h<=4:continue
        total+=old.kernel(a,h)/(I.cv(l)**3)*old.H_cell(j,dmesh)
    return (6/ZETA*total).hi

def certify(mesh=1024,qmesh=512,gmesh=512,agrid=64,dmesh=256):
    start=time.time()
    half=I.rat(1,2)
    head=4*half*half.sqrt()/3-4*k.C1*half*half*half.sqrt()/5
    exact=I.rat(0);middle=I.rat(0);improved=0
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
            chordal=((baselo-th-I(pu))*weight).lo
            if chordal>lo:improved+=1
            lo=max(lo,chordal)
        if l>=F(8,3):hi=min(hi,(I(mid.general_row_upper(l))*weight).hi)
        if l>=4:hi=min(hi,(I(mid.row_upper(l))*weight).hi)
        assert lo<=hi
        middle+=I(lo,hi)
    tail=ex.tail_series();total=head+exact+middle+tail
    return {'schema':'C86_CHORDAL_LOWER_CERTIFICATE_V1',
            'arithmetic':'integer outward intervals with denominator 2^112',
            'new_lower_bound':'Psi(A)>=R(A)-tau(A)-Pi(A), 0<A<4',
            'area_mesh_per_unit':mesh,'short_direction_mesh':qmesh,
            'g_mesh_per_unit':gmesh,'parallelogram_area_grid':agrid,
            'parallelogram_d_mesh':dmesh,'improved_lower_cells':improved,
            'head':head.json(),'exact_middle':exact.json(),
            'bounded_middle':middle.json(),'tail':tail.json(),'kappa3':total.json(),
            'seconds':time.time()-start,
            'source_sha256':{p:hashlib.sha256(Path(__file__).with_name(p).read_bytes()).hexdigest()
              for p in ['certify_chordal_lower.py','c84_interval_kernel.py',
                        'certify_extended.py','certify_middle_bounds.py',
                        'certify_farey_parallelogram.py']}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mesh',type=int,default=1024)
    p.add_argument('--qmesh',type=int,default=512);p.add_argument('--gmesh',type=int,default=512)
    p.add_argument('--agrid',type=int,default=64);p.add_argument('--dmesh',type=int,default=256)
    a=p.parse_args();d=certify(a.mesh,a.qmesh,a.gmesh,a.agrid,a.dmesh)
    Path(__file__).with_name('chordal_lower_certificate.json').write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(d,indent=2))
