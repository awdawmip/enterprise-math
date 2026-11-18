"""Single-digit weighted germ transport through finite colored translation orbits."""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys
from types import SimpleNamespace


def setup(root):
    global wm, wl, matrix, mm, inv, eye, Affine, ControlPacket, solve, lift, Problem, norm
    sys.path.insert(0,str(root/'src'))
    from enterprise_math import heartbeat_weighted_germ_lift as wm
    from enterprise_math.brc_transport import matrix, mm, inv, eye, Affine
    from enterprise_math.brc_control_port import ControlPacket
    from enterprise_math.heartbeat_congruence_lift import (
        solve_modular_linear as solve, lift_germ_seed as lift, GermLiftProblem as Problem,
        _normalize_frame as norm)
    orig=root/'research_notes/heartbeat_weighted_lift_20260927_AD0416/snapshot/src/enterprise_math/heartbeat_weighted_germ_lift.py'
    assert sha256(orig.read_bytes()).hexdigest()=='9cb757ea3df90ff11b5f943410b1f1e90181d53bb5a95e995b76dd8068cbbcf1'
    assert sha256(Path(wm.__file__).read_bytes()).hexdigest()=='5077223829003df6e4ea890e3190a15d7583c115463a4046e0a2b74e30f78ef3'
    spec=spec_from_file_location('enterprise_math._frozen_stabilizer_wl',orig)
    wl=module_from_spec(spec);sys.modules[spec.name]=wl;spec.loader.exec_module(wl)


def flat(a):
    return tuple(x for row in a for x in row)


def grid(a):
    return tuple(tuple(a[i:i+6]) for i in range(0,36,6))


def dot(a,b,p):
    return sum(x*y for x,y in zip(a,b))%p


def sub(a,b,p):
    return tuple((x-y)%p for x,y in zip(a,b))


def annihilator(vectors,n,p):
    rows=list(vectors) or [(0,)*n]
    return solve(rows,[0]*len(rows),p).basis


def valid_shifts(left,right,p):
    if not left or len(left)!=len(right):
        return []
    anchor=next(iter(left))
    candidates=[sub(y,anchor,p) for y in right if right[y]==left[anchor]]
    return [v for v in candidates if all(
        right.get(tuple((a+b)%p for a,b in zip(x,v)))==color for x,color in left.items())]


class Incomplete(Exception):
    pass


def direct(left,right,low,p,m=1,cap=None,witness=None):
    if cap is not None and (type(cap) is not int or cap<0):
        raise ValueError('nonnegative pair-test budget required')
    problem=wl.WeightedLiftProblem.from_control_packets(left,right,p)
    S,pivot=problem.normalize_seed(low,m)
    if not problem.row_certificate(S,m):
        raise ValueError('given frame is not a valid low transporter')
    if witness is not None:
        if norm(witness,p,m+problem.guard)[0]!=S or not problem.row_certificate(witness,m+1):
            raise ValueError('supplied high witness fails original row/seed')
    l=wm.packet_germ_classes(left,p,m+1)
    r=wm.packet_germ_classes(right,p,m+1)
    s=matrix(S); si=inv(s)
    nodes=[(0,mm(mm(s,c.representative),si),c.port_masses) for c in l]
    nodes += [(1,c.representative,c.port_masses) for c in r]
    seed=SimpleNamespace(prime=p,precision=m,guard=problem.guard,frame=eye(6),pivot=0)
    tests=0
    cache={}
    form=(1,)+(0,)*35
    def one(a,b):
        nonlocal tests
        if (a,b) in cache:
            return cache[a,b]
        if cap is not None and tests>=cap:
            raise Incomplete
        tests+=1
        u=wm._scalar_at_seed(a,b,seed)
        space=None
        if u is not None:
            prob=Problem(p,(wm._primitive(a,p),),(wm._primitive(b,p),),problem.guard,6)
            fixed=prob.seed(seed.frame,(u,),m)
            cert=lift(prob,fixed)
            if cert.space.particular is not None:
                space=cert.space
        cache[a,b]=space
        return space

    eq, rhs, ker_eq=[form],[0],[form]
    stats=[]
    maps=[]
    pending=list(range(len(nodes)))
    try:
        while pending:
            anchor=nodes[pending[0]][1]
            fixed=one(anchor,anchor)
            assert fixed and all(x==0 for x in fixed.particular)
            # Project away the one auxiliary unit-scalar digit.
            L=annihilator([v[:36] for v in fixed.basis],36,p)
            ker_eq.extend(L)
            left_colors,right_colors={},{}
            left_ids,right_ids={},{}
            keep=[]
            for idx in pending:
                side,germ,color=nodes[idx]
                sol=one(anchor,germ)
                if sol is None:
                    keep.append(idx)
                    continue
                pos=tuple(dot(row,sol.particular[:36],p) for row in L)
                named=right_colors if side else left_colors
                assert pos not in named
                named[pos]=color
                if side:
                    right_ids[pos]=idx-len(l)
                else:
                    left_ids[pos]=idx
            pending=keep
            shifts=valid_shifts(left_colors,right_colors,p)
            periods=valid_shifts(left_colors,left_colors,p)
            stats.append(dict(left=len(left_colors),right=len(right_colors),
                              local_periods=len(periods),legal_shifts=len(shifts)))
            if not shifts:
                return dict(status='NO_LIFTS',reason='orbit color/occupancy',pair_tests=tests,orbits=stats)
            a0=shifts[0]
            dual=annihilator([sub(x,a0,p) for x in shifts[1:]],len(L),p)
            assert len(shifts)==p**(len(L)-len(dual))
            for d in dual:
                eq.append(tuple(dot(d,col,p) for col in zip(*L)))
                rhs.append(dot(d,a0,p))
            maps.append((L,left_ids,right_ids))
    except Incomplete:
        return dict(status='INCOMPLETE_ORBIT_TESTS',pair_tests=tests,
                    verified_high_witness=witness is not None,known_lower_bound=int(witness is not None),
                    verified_frame=witness,fully_processed_orbits=len(stats))
    result=solve(eq,rhs,p)
    if result.particular is None:
        assert result.verify()
        return dict(status='NO_LIFTS',reason='joint linear obstruction',left_null_verified=True,
                    obstruction_terms=[dict(equation=i,coefficient=c,row=list(eq[i]),rhs=rhs[i])
                                       for i,c in enumerate(result.obstruction) if c],
                    pair_tests=tests,orbits=stats)
    K=solve(ker_eq,[0]*len(ker_eq),p)
    H=solve(eq,[0]*len(eq),p)
    assert H.verify() and K.verify() and result.verify()
    assert all(all(dot(row,v,p)==0 for row in H.coefficients) for v in K.basis)
    def point(x):
        g=grid(x); scale=p**(m+problem.guard)
        fx=tuple(tuple(int(i==j)+scale*g[i][j] for j in range(6)) for i in range(6))
        return norm(mm(matrix(fx),s),p,m+problem.guard+1)[0]
    # Distinct permutations induced by H basis generators. Keep the joint dependence.
    def induced(v,to_right=False):
        permutation=[None]*len(l)
        for L,left_ids,right_ids in maps:
            targets=right_ids if to_right else left_ids
            delta=tuple(dot(row,v,p) for row in L)
            for x,src in left_ids.items():
                dest=tuple((a+b)%p for a,b in zip(x,delta))
                permutation[src]=targets[dest]
        assert sorted(permutation)==list(range(len(l)))
        return permutation
    perms=[]
    for v in H.basis:
        perm=induced(v)
        if any(i!=j for i,j in enumerate(perm)) and perm not in perms:
            perms.append(perm)
    def chart(x):
        fx=point(x); scale=p**(m+problem.guard)
        return tuple(((fx[i][j]-S[i][j])//scale)%p for i in range(6) for j in range(6))
    base=chart(result.particular)
    high_points=[result.point(tuple(int(i==j) for i in range(len(result.basis))))
                 for j in range(len(result.basis))]
    rows=[sub(chart(x),base,p) for x in high_points]
    dual=annihilator(rows,36,p)
    old_chart=solve(dual,[dot(q,base,p) for q in dual],p)
    def pack(v):
        return [[k,x] for k,x in enumerate(v) if x]
    return dict(status='COMPLETE',pair_tests=tests,orbits=stats,count=result.count,
                kernel_dim=len(K.basis),stabilizer_dim=len(H.basis),
                image_order=H.count//K.count,image_generators=perms,
                kernel_basis=[pack(v) for v in K.basis],stabilizer_basis=[pack(v) for v in H.basis],
                transporter_base=pack(result.particular),
                transporter_base_class_bijection=induced(result.particular,to_right=True),
                base_and_basis_frames=[point(result.particular)]+[point(x) for x in high_points],
                old_chart=old_chart)


def same(x,y):
    def inc(a,b):
        return all(dot(v,a.particular,a.prime)==c and all(dot(v,w,a.prime)==0 for w in a.basis)
                   for v,c in zip(b.coefficients,b.rhs))
    return inc(x,y) and inc(y,x)


def embed(a):
    return matrix([[a[i%2][j%2] if i//2==j//2 else 0 for j in range(6)] for i in range(6)])


def packet(edges,states=1):
    return ControlPacket.from_edges(states,0,1,[(s,t,q,Affine(embed(a),tuple([shift]+[0]*5)),count)
                                               for s,t,q,a,shift,count in edges])


def rows(actions):
    return packet([(0,0,w,a,0,1) for a,w in actions])


def run(root):
    setup(root)
    identity=eye(6); i2=((1,0),(0,1))
    def D(d,k,p):return ((1,p*k),(0,d))
    tri=rows([(D(2,t,3),F(1,3)) for t in range(3)])
    A=((1,0),(0,3)); B=((1,-2),(0,3)); U=embed(((1,1),(0,-1)))
    swap=rows([(A,F(1,2)),(B,F(1,2))])
    bias=rows([(A,F(1,3)),(B,F(2,3))])
    duplicate=packet([(0,0,F(1,3),i2,j,1) for j in range(3)])
    guarded=packet([(0,0,F(1,6),((3,9*t),(0,1)),0,1) for t in range(3)]
                   +[(0,1,F(1,2),i2,0,1),(1,1,F(1),i2,0,1)],2)
    named=packet([(0,t,F(k+1 if t==0 else 3-k,12),D(2,k,3),0,1)
                  for k in range(3) for t in (0,1)]+[(1,1,F(1),i2,0,1)],2)
    rank2=rows([(D(d,t,5),F(1,10)) for d in (2,3) for t in range(5)])
    mixleft=rows([(D(2,0,5),F(1,2)),(D(3,0,5),F(1,2))])
    mixright=rows([(D(2,0,5),F(1,2)),(D(3,1,5),F(1,2))])
    result={}
    def audit(name,a,b,f,p,expected,baseline):
        out=direct(a,b,f,p)
        assert out.get('count',0)==expected
        pr=wl.WeightedLiftProblem.from_control_packets(a,b,p)
        if expected:
            fs=out.pop('base_and_basis_frames')
            assert all(pr.row_certificate(v,2) for v in fs)
            out['original_row_checks']=len(fs)
        chart=out.pop('old_chart',None)
        if baseline:
            old=wl.lift_weighted_kernel(pr,f,1)
            assert old.is_complete and old.certified_frame_count==expected
            if expected:
                assert same(chart,old.repairs)
            out['wl_forest_subsets']=old.support_checks
            out['wl_positive_forest_pieces']=len(old.pieces)
            if a==b:
                wm_old=wm.lift_weighted_seed(a,wm.weighted_lift_seed(a,f,p,1))
                assert wm_old.complete and wm_old.certified_count==expected
                if expected: assert same(chart,wm_old.space)
                out['wm_matchings']=len(wm_old.components)
        result[name]=out
    audit('ternary_equal',tri,tri,identity,3,3**18,True)
    audit('binary_nonidentity_seed',swap,swap,U,2,2**35,True)
    audit('binary_biased',bias,bias,U,2,0,True)
    audit('duplicate_supports',duplicate,duplicate,identity,3,3**35,True)
    audit('nonzero_guard',guarded,guarded,identity,3,3**27,True)
    audit('named_port_breaks_cycle',named,named,identity,3,3**17,False)
    counted=packet([(0,0,F(1,6),D(2,k,3),0,k+1) for k in range(3)])
    audit('positive_multiplicity_breaks_cycle',counted,counted,identity,3,3**17,True)
    audit('two_orbits_same_frame',rank2,rank2,identity,5,5**18,False)
    assert result['two_orbits_same_frame']['image_order']==5
    audit('nonempty_local_empty_joint',mixleft,mixright,identity,5,0,True)
    assert result['nonempty_local_empty_joint']['reason']=='joint linear obstruction'
    goodright=rows([(D(2,1,5),F(1,2)),(D(3,2,5),F(1,2))])
    audit('cross_packet_nondiagonal_base',mixleft,goodright,identity,5,5**17,True)
    assert result['cross_packet_nondiagonal_base']['transporter_base']
    result['partial_with_known_solution']=direct(tri,tri,identity,3,cap=0,witness=identity)
    result['partial_no_known_solution']=direct(bias,bias,U,2,cap=0)
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--verify',type=Path)
    args=ap.parse_args()
    result=run(args.repo.resolve())
    payload=json.dumps(result,sort_keys=True,indent=2,default=lambda v:int(v) if isinstance(v,F) and v.denominator==1 else str(v))+'\n'
    if args.verify:
        assert payload==args.verify.read_text()
        print('PASS',sha256(payload.encode()).hexdigest())
    else:
        print(payload,end='')


if __name__=='__main__':
    main()
