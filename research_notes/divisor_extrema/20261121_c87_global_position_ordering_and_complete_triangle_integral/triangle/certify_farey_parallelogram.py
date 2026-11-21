#!/usr/bin/env python3
"""Refine C85's Euler upper bound with actual unit parallelograms."""
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import json,time,hashlib,argparse
import c84_interval_kernel as k
import certify_extended as ex
import certify_middle_bounds as mid

I,Q,ZETA=k.I,k.Q,k.ZETA

def H_primitive(d):
    d=Fraction(d)
    x=I.cv(d);v=1-x
    vlog=I.rat(0) if d==1 else v*k.log(v)
    return x-x*x/2+vlog-v

@lru_cache(None)
def H_cell(j,mesh):
    return (H_primitive(Fraction(j+1,mesh))-H_primitive(Fraction(j,mesh))).nonnegative()

def kernel(a,d):
    z=2*a*d
    if z<=4:return I.rat(0)
    zz=I.cv(z);s=zz.sqrt();t=(zz-4).sqrt()
    u=k.log((s+t)/2)
    return (2*(zz+2)*u-3*s*t).nonnegative()

@lru_cache(None)
def parallelogram_lower(a,dmesh=256):
    """Full-cell lower enclosure of the one-dimensional basis integral."""
    a=Fraction(a)
    if a<=2:return 0
    total=I.rat(0)
    for j in range(dmesh//2,dmesh):
        l,h=Fraction(j,dmesh),Fraction(j+1,dmesh)
        if 2*a*l<=4:continue
        value=kernel(a,l)/(I.cv(h)**3)
        total+=value*H_cell(j,dmesh)
    return (6/ZETA*total).lo

def certify(mesh=1024,qmesh=512,gmesh=512,agrid=64,dmesh=256):
    assert mesh>0 and mesh%2==0 and agrid>0 and dmesh%2==0
    start=time.time()
    half=I.rat(1,2)
    head=4*half*half.sqrt()/3-4*k.C1*half*half*half.sqrt()/5
    exact=I.rat(0);middle=I.rat(0);new_cells=0
    for j in range(mesh//2,9*mesh//2):
        l,h=Fraction(j,mesh),Fraction(j+1,mesh)
        val=ex.area_cell(l,h)
        if l>=2:
            lv,hv=I.cv(l),I.cv(h)
            weight=4*(hv.sqrt()-lv.sqrt())
            lo=max(val.lo,(I(mid.short_lower(h,qmesh,gmesh))*weight).lo)
            hi=val.hi
            if h<=4:
                _,_,_,c1l=k.moments(l)
                _,_,b1h,_=k.moments(h)
                base=hv-k.C1*lv*lv+b1h-c1l
                tc=ex.centered_triangle(l)
                euler=(base-tc).hi
                hi=min(hi,(I(euler)*weight).hi)
            if l>=Fraction(8,3):hi=min(hi,(I(mid.general_row_upper(l))*weight).hi)
            if l>=4:hi=min(hi,(I(mid.row_upper(l))*weight).hi)
            old_hi=hi
            if h<=4:
                aa=Fraction((l*agrid).numerator//(l*agrid).denominator,agrid)
                pl=parallelogram_lower(aa,dmesh)
                combined=(base-(tc+I(pl))/2).hi
                hi=min(hi,(I(combined)*weight).hi)
            if hi<old_hi:new_cells+=1
            assert lo<=hi
            middle+=I(lo,hi)
        else:exact+=val
    tail=ex.tail_series();total=head+exact+middle+tail
    result={"schema":"C85_FAREY_PARALLELOGRAM_CERTIFICATE_V1",
            "arithmetic":"integer outward intervals; denominator 2^112",
            "exact_formula_domain":"0<A<2","Euler_and_parallelogram_domain":"0<A<4",
            "area_mesh_per_unit":mesh,"short_direction_mesh":qmesh,"g_mesh_per_unit":gmesh,
            "parallelogram_area_grid":agrid,"parallelogram_d_mesh":dmesh,
            "head":head.json(),"exact_middle":exact.json(),"bounded_middle":middle.json(),
            "tail":tail.json(),"kappa3":total.json(),"newly_improved_upper_cells":new_cells,
            "seconds":time.time()-start,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "middle_script_sha256":hashlib.sha256(Path(mid.__file__).read_bytes()).hexdigest(),
            "extended_script_sha256":hashlib.sha256(Path(ex.__file__).read_bytes()).hexdigest(),
            "interval_kernel_sha256":hashlib.sha256(Path(k.__file__).read_bytes()).hexdigest()}
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mesh',type=int,default=1024)
    ap.add_argument('--qmesh',type=int,default=512);ap.add_argument('--gmesh',type=int,default=512)
    ap.add_argument('--agrid',type=int,default=64);ap.add_argument('--dmesh',type=int,default=256)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('parallelogram_certificate.json'))
    a=ap.parse_args();r=certify(a.mesh,a.qmesh,a.gmesh,a.agrid,a.dmesh)
    a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
