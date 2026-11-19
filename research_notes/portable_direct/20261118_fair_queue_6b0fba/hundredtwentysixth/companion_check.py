"""Exact arithmetic. Run --repo PATH to add frozen six-axis WM and WL certificates."""
import argparse
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import product
import json
from pathlib import Path
import sys


def val(x,p,cap):
    v=0
    while v<cap and x%p==0:
        x//=p; v+=1
    return v


def scalar_count(b,p,m,e):
    t=min(val(a,p,e)+val(i,p,e) for i,a in enumerate(b,1))
    if p!=2 or m>=2:
        return p**min(e-m,t)
    if e==1: return 1
    odd=min(val(a,2,e) for a in b[::2])
    return 2**min(e-2,t)*(1+int(odd>=e-1))


def scalars(b,p,m,e):
    q=p**e
    return [c for c in range(1,q,p**m)
            if all(a*(pow(c,i,q)-1)%q==0 for i,a in enumerate(b,1))]


def ident(d):
    return tuple(int(i==j) for i in range(d) for j in range(d))


def companion(b):
    d=len(b)
    return tuple(-b[d-1-i] if j==d-1 else int(i==j+1)
                 for i in range(d) for j in range(d))


def mm(a,b,d,q):
    return tuple(sum(x*y for x,y in zip(a[i*d:(i+1)*d],b[j::d]))%q
                 for i in range(d) for j in range(d))


def normal(a,q,p):
    t=pow(next(x for x in a if x%p),-1,q)
    return tuple(t*x%q for x in a)


def key_product(g,a,d,q,p):
    return normal(mm(g,a,d,q),q,p)==normal(mm(a,g,d,q),q,p)


def permute(g,gi,a,d,q,p):
    return normal(mm(mm(g,a,d,q),gi,d,q),q,p)


def check_small_orbit():
    # Complete three-axis control at p=2; the mod-2 cyclic centralizer has
    # dimension 3 < minimum nonzero commutator rank 4 in this dimension.
    d,p,q=3,2,8
    a=companion((0,0,1)); one=ident(d)
    fixed=[]
    for rest in product(range(4),repeat=8):
        g=tuple((v+2*z)%8 for v,z in zip(one,(0,)+rest))
        if key_product(g,a,d,q,p): fixed.append(g)
    generators=[]
    for v in (2,4):
        for i in range(d*d):
            g=tuple((u+v*(j==i))%8 for j,u in enumerate(one))
            gi=tuple((u+(-v+(v*v if i%(d+1)==0 else 0))*(j==i))%8
                     for j,u in enumerate(one))
            assert mm(g,gi,d,q)==one
            generators.append((g,gi))
    orbit=[normal(a,q,p)]; seen=set(orbit)
    for b in orbit:
        for g,gi in generators:
            x=permute(g,gi,b,d,q,p)
            if x not in seen:
                seen.add(x);orbit.append(x)
    core=[g for g in fixed if all(key_product(g,b,d,q,p) for b in orbit)]
    assert len(fixed)==16 and len(orbit)==4096 and len(core)==4
    assert all(all((x-y)%4==0 for x,y in zip(g,one)) for g in core)
    return dict(d=d,p=p,m=1,e=3,frames=65536,ordinary_orbit_size=len(orbit),
                point_stabilizer=len(fixed),pointwise_kernel=len(core),permutation_image=65536//len(core))


def check_scalars():
    total=matrix_cases=0
    for p in (2,3,5,7):
        for e in range(2, (9 if p==2 else 6 if p==3 else 5)):
            for m in range(1,e):
                for mask in range(32):
                    b=tuple(p**(i%3) if mask&(1<<i) else 0 for i in range(5))+(1,)
                    us=scalars(b,p,m,e)
                    assert len(us)==scalar_count(b,p,m,e)
                    q=p**e; a=companion(b)
                    for c in us:
                        diag=[pow(c,i,q) for i in range(6)]
                        assert all((diag[i]*a[6*i+j]-c*a[6*i+j]*diag[j])%q==0
                                   for i in range(6) for j in range(6))
                        matrix_cases+=1
                    total+=1
    tower=[]
    for s in (1,2,4,7):
        a=(0,0,0,0,2**s,1); free=(0,0,0,0,0,1)
        row=[]
        for e in range(2,s+5):
            us=scalars(a,2,1,e); large=scalars(free,2,1,e)
            assert (us==large)==(e<=s+1)
            if e==s+1:
                assert 2**e-1 in us and all(c%2**e != 2**e-1 for c in scalars(a,2,1,e+1))
            row.append([e,len(us),len(large),2**(30*(e-1))//len(us)])
        tower.append(dict(s=s,rows_e_U_Uinfty_orbit=row))
    return dict(parameter_checks=total,intertwiner_matrix_checks=matrix_cases,branch_towers=tower)


def native(repo):
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import heartbeat_weighted_germ_lift as wm
    from enterprise_math.brc_transport import matrix,eye,Affine
    from enterprise_math.brc_control_port import ControlPacket
    wl_path=repo/'research_notes/heartbeat_weighted_lift_20260927_AD0416/snapshot/src/enterprise_math/heartbeat_weighted_germ_lift.py'
    fingerprints=[sha256(Path(wm.__file__).read_bytes()).hexdigest(),sha256(wl_path.read_bytes()).hexdigest()]
    assert fingerprints==['5077223829003df6e4ea890e3190a15d7583c115463a4046e0a2b74e30f78ef3',
                          '9cb757ea3df90ff11b5f943410b1f1e90181d53bb5a95e995b76dd8068cbbcf1']
    spec=spec_from_file_location('enterprise_math._hbw_frozen_wl',wl_path)
    wl=module_from_spec(spec);sys.modules[spec.name]=wl;spec.loader.exec_module(wl)
    def grid(a):
        return matrix([list(a[i:i+6]) for i in range(0,36,6)])
    def packet(a):
        return ControlPacket.from_edges(1,0,1,[(0,0,Fraction(1),Affine(grid(a),(0,)*6),1)])
    one=eye(6)
    rows=[]
    for p in (2,3,5):
        for m in (1,2):
            for b in [(0,0,0,0,0,1),(0,0,0,0,p,1),(0,0,0,0,1,1)]:
                q=p**(m+1); a=companion(b)
                obj=packet(a)
                germ_count=len(wm.packet_germ_classes(obj,p,m+1))
                w=wm.lift_weighted_seed(obj,wm.weighted_lift_seed(obj,one,p,m))
                assert w.status=="COMPLETE" and len(w.components)==1
                dim=len(w.space.basis)
                expected=p**5*scalar_count(b,p,m,m+1)
                assert w.certified_count==expected and p**dim==expected and germ_count==1
                high=grid([int(i==j)*pow(1+p**m,i,q) for i in range(6) for j in range(6)])
                cert=wl.WeightedLiftProblem.from_control_packets(obj,obj,p)
                accepts=cert.row_certificate(high,m+1)
                assert bool(accepts)==(1+p**m in scalars(b,p,m,m+1))
                rows.append([p,m,list(b),dim,bool(accepts)])
    a=companion((0,0,0,0,0,1)); q=8; i6=ident(6)
    g=grid(tuple((x+2*y)%q for x,y in zip(i6,a)))
    h=tuple((u+2*int(i==0))%q for i,u in enumerate(i6))
    hi=tuple((u+2*int(i==0))%q for i,u in enumerate(i6))
    b=mm(mm(h,a,6,q),hi,6,q)
    pair=wl.WeightedLiftProblem.from_control_packets(packet(a),packet(b),2)
    assert pair.guard==0 and pair.row_certificate(grid(h),3)
    ca=wl.WeightedLiftProblem.from_control_packets(packet(a),packet(a),2)
    cb=wl.WeightedLiftProblem.from_control_packets(packet(b),packet(b),2)
    assert ca.row_certificate(g,3) and cb.row_certificate(g,2) and not cb.row_certificate(g,3)
    towers=[]
    f0=companion((0,0,0,0,0,1))
    neg=grid(tuple((-1)**i if i==j else 0 for i in range(6) for j in range(6)))
    for s in (1,2,4,7):
        f=companion((0,0,0,0,2**s,1))
        both=ControlPacket.from_edges(1,0,1,[(0,0,Fraction(1,2),Affine(grid(mat),(0,)*6),1)
                                            for mat in (f0,f)])
        class_counts=[len(wm.packet_germ_classes(both,2,e)) for e in (s,s+1)]
        assert class_counts==[1,2]
        lift_counts=[]
        for mat in (f0,f):
            obj=packet(mat)
            oracle=wl.WeightedLiftProblem.from_control_packets(obj,obj,2)
            assert oracle.row_certificate(neg,s+1)
            assert bool(oracle.row_certificate(neg,s+2))==(mat==f0)
            res=wm.lift_weighted_seed(obj,wm.weighted_lift_seed(obj,neg,2,s+1))
            assert res.complete
            lift_counts.append(res.certified_count)
        assert lift_counts==[64,0]
        towers.append(dict(s=s,WM_projective_classes_levels_s_splus1=class_counts,
                           WM_children_of_negative_seed_infinite_finite=lift_counts))
    return dict(negative_seed_towers=towers,WM_WL_sha256=fingerprints,one_step_p_m_coefficients_kernel_dimension_diag_accepted=rows,
                actual_transported_anchor_and_noncore_frame_mod8=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,help='enterprise-math checkout with the two frozen source files')
    args=parser.parse_args()
    report=dict(scalars=check_scalars(),small_control=check_small_orbit())
    if args.repo: report['native']=native(args.repo.resolve())
    print(json.dumps(report,indent=2))
