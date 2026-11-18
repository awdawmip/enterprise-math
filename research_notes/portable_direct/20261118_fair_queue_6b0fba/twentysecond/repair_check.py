"""Reconstruct original positive six-axis packets and verify the multilayer certificate."""
import argparse
import json
import sys
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path


def diag_blocks(t,g,h,n=3):
    return tuple(tuple((1 if i==j and not i%2 else 1+g if i==j else
                        g*h*t if not i%2 and j==i+1 else 0)
                       for j in range(2*n)) for i in range(2*n))


def model_branches(p,n,source,target,vanish):
    mod=p**n
    def tally(atoms):
        q=Counter()
        for t,w in atoms: q[t%mod]+=w
        return q
    x,y=tally(source),tally(target)
    t0=next(iter(x))
    t1=next(t for t in x if (t-t0)%p)
    inverse=pow(t1-t0,-1,mod)
    out=[]
    for s0 in y:
        for s1 in y:
            alpha=(s1-s0)*inverse%mod
            beta=(s0-alpha*t0)%mod
            if alpha%p!=1 or (vanish and beta%p): continue
            if {(alpha*t+beta)%mod:w for t,w in x.items()}==y:
                out.append((alpha,beta))
    return sorted(out)


def all_block_frames(p,d,binary):
    mod=p**d
    for x,y,z in product(range(0,mod,p),repeat=3):
        if binary:
            # H S where S=[[1,1],[0,-1]]
            yield ((1,(1-x)%mod),(y,(y-1-z)%mod))
        else:
            yield ((1,x),(y,1+z))


def small_predicted(Fm,p,d,g,h,branches,b,c,binary=False):
    mod=p**d
    (u,v),(w,z)=Fm
    if binary:
        # Undo the exact involution S.
        v=(u-v)%mod; z=(w-z)%mod
    M=p**(d-b); m=M//p**c
    if w%M: return False
    return any((u-a*z)%m==0 and (v-h*beta*z)%M==0 for a,beta in branches)


def direct_block(Fm,p,d,g,h,source,target):
    # Compare every ordered 2x2 intertwining equation up to its independently
    # slotted projective scalar, grouping source masses for each target residue.
    mod=p**d
    (u,v),(w,z)=Fm
    def key(a):
        first=next(x for x in a if x%p)
        return tuple(x*pow(first,-1,mod)%mod for x in a)
    left=Counter();right=Counter()
    for t,mass in source:
        left[key((u,g*h*t*u+(1+g)*v,w,g*h*t*w+(1+g)*z))]+=mass
    for t,mass in target:
        right[key((u+g*h*t*w,v+g*h*t*z,(1+g)*w,(1+g)*z))]+=mass
    return left==right


def native_import(root):
    src=root/'src/enterprise_math'
    wlfile=root/'research_notes/heartbeat_weighted_lift_20260927_AD0416/snapshot/src/enterprise_math/heartbeat_weighted_germ_lift.py'
    expected={'WL':(wlfile,'9cb757ea3df90ff11b5f943410b1f1e90181d53bb5a95e995b76dd8068cbbcf1'),
              'WM':(src/'heartbeat_weighted_germ_lift.py','5077223829003df6e4ea890e3190a15d7583c115463a4046e0a2b74e30f78ef3')}
    for where,digest in expected.values(): assert sha256(where.read_bytes()).hexdigest()==digest
    sys.path.insert(0,str(root/'src'))
    from enterprise_math.brc_control_port import ControlPacket
    from enterprise_math.brc_transport import Affine, matrix
    from enterprise_math import heartbeat_weighted_germ_lift as wm
    spec=spec_from_file_location('enterprise_math._wl_multilayer',wlfile)
    wl=module_from_spec(spec);sys.modules[spec.name]=wl;spec.loader.exec_module(wl)
    def packet(atoms,g,h):
        return ControlPacket.from_edges(1,0,1,[(0,0,w,Affine(matrix(diag_blocks(t,g,h)),
                                          (0,0,0,0,0,0)),1) for t,w in atoms])
    return wl,wm,packet


def canonical_full(u,v,w,z):
    blocks=((u,v),(w,z))
    return tuple(tuple(blocks[i%2][j%2][i//2][j//2] for j in range(6))
                 for i in range(6))


def full_cases(wl,wm,packet):
    I=tuple(tuple(int(i==j) for j in range(3)) for i in range(3))
    E=tuple(tuple(int(i==0 and j==1) for j in range(3)) for i in range(3))
    O=tuple(tuple(0 for j in range(3)) for i in range(3))
    def plus(x,y,f): return tuple(tuple(a+f*b for a,b in zip(s,t)) for s,t in zip(x,y))
    def times(x,f): return plus(O,x,f)
    def run(source,target,frames,d):
        left=packet(source,1,3);right=packet(target,1,3)
        pr=wl.WeightedLiftProblem.from_control_packets(left,right,3)
        assert pr.guard==0
        out=[]
        for frame,yes in frames:
            got=pr.row_certificate(frame,d)
            assert got==yes
            if yes:
                for i,atom in enumerate(pr.left):
                    assert any(pr.edge_scalar(i,j,frame,d)==1 for j in range(len(pr.right)))
                # WM certifies only the same-packet transporter in this call.
                if source==target: assert wm.weighted_lift_seed(left,frame,3,d)
            out.append(got)
        return out
    uniform=lambda n:[(t,F(1,n)) for t in range(n)]
    I3=canonical_full(I,O,O,I);Z=plus(I,E,3)
    f1=canonical_full(Z,O,O,Z)
    f2=canonical_full(I,times(I,3),O,I)
    total=canonical_full(Z,times(I,3),O,Z)
    f12=canonical_full(Z,times(Z,3),O,Z)
    tri=uniform(3);wide=uniform(9)
    collision=run(wide,wide,[(I3,True),(f1,True),(f2,True),(total,False),(f12,True)],3)
    tri_second=run(tri,tri,[(I3,True),(f1,True),(f2,False),
                  (canonical_full(I,O,O,plus(I,E,9)),True)],3)
    shifted=[(t+1,w) for t,w in tri]
    transport=run(tri,shifted,[(f2,True),(I3,False),(f12,True)],3)
    return dict(nine_atom_affine_rectangle=collision,three_atom_second_lift=tri_second,
                shifted_three_atom_common_frame=transport)


def main(root):
    wl,wm,packet=native_import(root)
    data={}
    for name,p,g,h,b,c,atoms in [
        ('ternary',3,1,3,0,1,[(t,F(1,3)) for t in range(3)]),
        ('binary',2,2,-1,1,0,[(t,F(1,2)) for t in range(2)])]:
        binary=name=='binary'
        pkt=packet(atoms,g,h)
        pr=wl.WeightedLiftProblem.from_control_packets(pkt,pkt,p,block_size=2)
        assert pr.guard==0
        if binary: seed=((1,1),(0,-1))
        else: seed=((1,0),(0,1))
        old=[seed];stages={}
        for d in (2,3,4):
            branches=model_branches(p,d-b-c,atoms,atoms,c==0)
            actual=set();tested=0
            for frame in all_block_frames(p,d,binary):
                direct=direct_block(frame,p,d,g,h,atoms,atoms)
                predicted=small_predicted(frame,p,d,g,h,branches,b,c,binary)
                assert direct==predicted
                if direct: actual.add(frame)
                tested+=1
            if d<=3:
                union=set();child_hist=Counter()
                for f in old:
                    step=wl.lift_weighted_kernel(pr,f,d-1)
                    assert step.is_complete
                    children=list(step.all_frames()) if step.repairs is not None else []
                    child_hist[len(children)]+=1
                    for v in children:
                        assert pr.row_certificate(v,d)
                        union.add(tuple(tuple(map(int,row)) for row in v))
                assert actual==union
                old=sorted(actual)
            else: child_hist={}
            e=8*(d-b-1)+9*c+35*b
            stages[d]=dict(affine_parameters=branches,full_six_axis_count=len(branches)*p**e,
                           comparison_2x2_frames=tested,repeated_2x2_valid=len(actual),
                           original_WL_parent_child_histogram=dict(child_hist))
        data[name]=stages
    data['full_native_rows']=full_cases(wl,wm,packet)
    wide=[(t,F(1,9)) for t in range(9)]
    branches=model_branches(3,2,wide,wide,False)
    assert len(branches)==27
    data['nine_atom_alpha_beta']=branches
    data['nine_atom_full_six_axis_count']=27*3**25
    stable={}
    for p,n,source,target,need_zero,expected in [
        (3,5,[0,2,4],[0,8,16],False,[(4,0)]),
        (2,6,[0,1,2],[0,1,2],True,[(1,0),(-1,2)]),
        (3,5,[0,1,2],[0,1,2],False,[(1,0)]),
        (2,6,[0,1],[0,1],True,[(1,0)])]:
        x=[(t,F(1,len(source))) for t in source]
        y=[(t,F(1,len(target))) for t in target]
        got=model_branches(p,n,x,y,need_zero)
        assert p**n>2*(max(source)-min(source))*(max(target)-min(target))
        assert got==sorted((a%(p**n),b%(p**n)) for a,b in expected)
        stable[str((p,tuple(source),tuple(target)))]=got
    data['deep_integer_affine_examples']=stable
    return data


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--repo',type=Path,required=True)
    cfg=args.parse_args()
    print(json.dumps(main(cfg.repo.resolve()),indent=2,sort_keys=True))
