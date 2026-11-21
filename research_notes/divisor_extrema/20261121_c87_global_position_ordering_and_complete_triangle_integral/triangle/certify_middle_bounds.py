#!/usr/bin/env python3
"""C85 structural row bounds for the middle-area triangle constant.

All probability bounds and integrals use directed integer arithmetic.
The q mesh bounds the entire cell using monotonicity of g, not node sampling.
"""
from fractions import Fraction
from pathlib import Path
import argparse,json,time,hashlib
import c84_interval_kernel as k
import certify_extended as ex

I,Q,ZETA=k.I,k.Q,k.ZETA

def short_lower(a,qmesh=512,gmesh=512):
    """Pointwise lower bound on Psi(a), a in [2,9/2]."""
    assert 2<=a<=Fraction(9,2)
    # qcap^2<1/2 and sqrt(2a)*qcap<=2 in each indicated range.
    qcap=Fraction(181,256) if a<=4 else Fraction(2,3)
    rhi=(2*I.cv(a)).sqrt().hi
    capnum,capden=qcap.numerator,qcap.denominator
    den=capden*qmesh
    total=0
    for j in range(1,qmesh+1):
        num=capnum*j
        # Upper endpoint for x=(rq-1)/q^2, rounded UP to the g grid.
        raw=(rhi*num-Q*den)*den*gmesh
        idx=k.ceildiv(raw,Q*num*num)
        if idx<=0: glow=Q
        elif idx>=2*gmesh: glow=0
        else: glow=k.g(Fraction(idx,gmesh)).lo
        total += glow*(j**4-(j-1)**4)
    integral=I.cv(Fraction(total*capnum**4,4*qmesh**4*capden**4*Q))
    return (3/ZETA*integral).lo

def row_upper(a):
    """Pointwise decreasing upper bound for 4<=a<=9/2."""
    assert 4<=a<=Fraction(9,2)
    r=(2*I.cv(a)).sqrt()
    discriminant=(2*I.cv(a)-8).nonnegative().sqrt()
    qm=(r-discriminant)/4
    qp=(r+discriminant)/4
    qm2=2*qm
    bound=2/I.rat(3).sqrt()
    upper=I(min(qm2.lo,bound.lo),min(qm2.hi,bound.hi))
    def f1(q):return q*q/2-r*q**3/3+q**4/2
    def f2(q):return q*q-r*q**3/3+q**4/4
    one=I.rat(1)
    return (3/ZETA*(qm**4/4+f1(one)-f1(qp)+f2(upper)-f2(one))).hi

def general_row_upper(a,mesh=1024):
    """Integrate the minimum of three row bounds for a>=8/3.

    The rational q cutoff exceeds the exact Minkowski cutoff 2/sqrt(3).
    The added region has nonnegative integrand and only enlarges the bound.
    """
    assert a>=Fraction(8,3)
    rlo=(2*I.cv(a)).sqrt().lo
    capnum,capden=1183,1024
    den=capden*mesh
    den2=den*den
    total=0
    def f1(num):return k.ceildiv(Q*den2-rlo*num*den+2*Q*num*num,den2)
    def f2(num):return k.ceildiv(2*Q*den2-rlo*num*den+Q*num*num,den2)
    for j in range(1,mesh+1):
        nl,nh=capnum*(j-1),capnum*j
        q2=k.ceildiv(Q*nh*nh,den2)
        # Both quadratic functions are convex in q: their cell maximum is
        # at an endpoint. Taking the minimum of individual maxima is safe.
        height=max(0,min(q2,max(f1(nl),f1(nh)),max(f2(nl),f2(nh))))
        total+=height*(2*j-1)
    integral=I.cv(Fraction(total*capnum*capnum,2*mesh*mesh*capden*capden*Q))
    return (3/ZETA*integral).hi

def certify(mesh=1024,qmesh=512,gmesh=512):
    start=time.time();assert mesh>0 and mesh%2==0 and qmesh>0 and gmesh>0
    half=I.rat(1,2)
    head=4*half*half.sqrt()/3-4*k.C1*half*half*half.sqrt()/5
    exact=I.rat(0);middle=I.rat(0)
    improved_lower=improved_upper=0
    for j in range(mesh//2,9*mesh//2):
        l,h=Fraction(j,mesh),Fraction(j+1,mesh)
        val=ex.area_cell(l,h)
        if l>=2:
            weight=4*(I.cv(h).sqrt()-I.cv(l).sqrt())
            low=(I(short_lower(h,qmesh,gmesh))*weight).lo
            if low>val.lo: improved_lower+=1
            high=val.hi
            if h<=4:
                lv,hv=I.cv(l),I.cv(h)
                _,_,_,c1l=k.moments(l)
                _,_,b1h,_=k.moments(h)
                euler_upper=(hv-k.C1*lv*lv+b1h-c1l-ex.centered_triangle(l)).hi
                high=min(high,(I(euler_upper)*weight).hi)
            if l>=Fraction(8,3):
                high=min(high,(I(general_row_upper(l))*weight).hi)
            if l>=4:
                high=min(high,(I(row_upper(l))*weight).hi)
            if high<val.hi: improved_upper+=1
            val=I(max(val.lo,low),high)
            assert val.lo<=val.hi
            middle+=val
        else:exact+=val
    tail=ex.tail_series()
    total=head+exact+middle+tail
    assert total.lo<=total.hi
    result={"schema":"C85_TRIANGLE_MIDDLE_BOUNDS_CERTIFICATE_V1",
            "arithmetic":"integer outward intervals with denominator 2^112",
            "exact_formula_domain":"0<A<2", "area_mesh_per_unit":mesh,
            "five_term_euler_upper_domain":"0<A<4",
            "short_direction_mesh":qmesh,"g_mesh_per_unit":gmesh,
            "short_direction_caps":{"2<=A<=4":"181/256","4<A<=9/2":"2/3"},
            "row_upper_domain":"4<=A<=9/2",
            "general_row_upper_domain":"8/3<=A<=9/2",
            "general_row_upper_q_mesh":1024,
            "general_row_upper_q_cap":"1183/1024 > 2/sqrt(3)",
            "head":head.json(),"exact_middle":exact.json(),"bounded_middle":middle.json(),
            "tail":tail.json(),"kappa3":total.json(),
            "improved_lower_cells":improved_lower,"improved_upper_cells":improved_upper,
            "seconds":time.time()-start,"tail_series_terms":256,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "extended_script_sha256":hashlib.sha256(Path(ex.__file__).read_bytes()).hexdigest(),
            "interval_kernel_sha256":hashlib.sha256(Path(k.__file__).read_bytes()).hexdigest()}
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mesh',type=int,default=1024)
    ap.add_argument('--qmesh',type=int,default=512);ap.add_argument('--gmesh',type=int,default=512)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('middle_bounds_certificate.json'))
    args=ap.parse_args();r=certify(args.mesh,args.qmesh,args.gmesh)
    args.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
