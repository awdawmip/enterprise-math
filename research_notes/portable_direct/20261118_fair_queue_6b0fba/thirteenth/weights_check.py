"""Cross-evaluate the two original weighted-germ lift interfaces without replacing either file."""
import argparse
from fractions import Fraction as F
from hashlib import sha1, sha256
from importlib.util import spec_from_file_location, module_from_spec
import json
from pathlib import Path
import sys


WL_SHA = "9cb757ea3df90ff11b5f943410b1f1e90181d53bb5a95e995b76dd8068cbbcf1"
WM_SHA = "5077223829003df6e4ea890e3190a15d7583c115463a4046e0a2b74e30f78ef3"
BASE = "research_notes/heartbeat_weighted_lift_20260927_AD0416"
PINS = {
    'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
    'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
    'heartbeat_congruence_lift.py':'3909cc89b97b5e3a14fb0f1f18d85d19b7a390f9',
    'heartbeat_peak_orbits.py':'6f5a35851ed7cfef08fe34bb209fbd29c9b4b0dc',
    'heartbeat_carry_peak.py':'44bde8bbff397adf8aec80fcb2bffa79c6e272e9',
    'heartbeat_switching_carry.py':'81fa56ea5967daa9fbbec66f06fed696a5620bb5',
}


def same_space(a,b):
    if a is None or b is None:
        return a is None and b is None
    def included(inside,outside):
        return all(sum(x*y for x,y in zip(row,inside.particular))%a.prime==rhs
                   and all(sum(x*y for x,y in zip(row,v))%a.prime==0 for v in inside.basis)
                   for row,rhs in zip(outside.coefficients,outside.rhs))
    return a.prime==b.prime and included(a,b) and included(b,a)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--json',type=Path)
    args=parser.parse_args()
    root=args.repo
    src=root/'src/enterprise_math'
    for name,digest in PINS.items():
        raw=(src/name).read_bytes()
        assert sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==digest
    archived=(root/BASE/'RESULTS.json').read_bytes()
    blob=sha1(b'blob '+str(len(archived)).encode()+b'\x00'+archived).hexdigest()
    assert blob=='2cac53a51dc8876ac6f5c8ef8443f94a9142543e'
    for name,digest in json.loads(archived)['frozen_brc_sources'].items():
        assert sha256((src/name).read_bytes()).hexdigest()==digest
    snapshot=root/BASE/'snapshot/src/enterprise_math/heartbeat_weighted_germ_lift.py'
    assert sha256(snapshot.read_bytes()).hexdigest()==WL_SHA
    assert sha256((src/'heartbeat_weighted_germ_lift.py').read_bytes()).hexdigest()==WM_SHA
    sys.path.insert(0,str(root/'src'))
    from enterprise_math import heartbeat_weighted_germ_lift as wm
    from enterprise_math.brc_transport import eye,matrix,Affine,mm
    from enterprise_math.brc_control_port import ControlPacket
    from enterprise_math.heartbeat_congruence_lift import solve_modular_linear, _normalize_frame
    spec=spec_from_file_location('enterprise_math._reconciliation_wl',snapshot)
    wl=module_from_spec(spec);sys.modules[spec.name]=wl;spec.loader.exec_module(wl)

    def embed(a):
        n=len(a)
        return matrix([[a[i%n][j%n] if i//n==j//n else 0 for j in range(6)] for i in range(6)])

    def packet(entries, stopped=False, duration=1, offset=(0,)*6):
        edges=[(0,0,w,Affine(embed(a),offset),1) for a,w in entries]
        if stopped:
            edges.extend(((0,1,F(1,2),Affine.identity(6),1),(1,1,1,Affine.identity(6),1)))
        return ControlPacket.from_edges(2 if stopped else 1,0,duration,edges)

    def compare(pkt,p,s,m=1,wl_cap=20000,wm_cap=4096):
        problem=wl.WeightedLiftProblem.from_control_packets(pkt,pkt,p)
        low=wm.weighted_lift_seed(pkt,s,p,m)
        a=wl.lift_weighted_kernel(problem,s,m,max_support_checks=wl_cap)
        b=wm.lift_weighted_seed(pkt,low,max_matchings=wm_cap)
        if a.is_complete and b.complete:
            assert a.status==b.status and same_space(a.repairs,b.space)
            if a.repairs is not None:
                # Rebind the affine origin and every direction via the original two row observers.
                for coeff in ([0]*len(a.repairs.basis),*([int(j==k) for j in range(len(a.repairs.basis))]
                              for k in range(len(a.repairs.basis)))):
                    v=a.frame(coeff)
                    assert problem.row_certificate(v,m+1)
                    assert wm.weighted_lift_seed(pkt,v,p,m+1).frame==v
        return a,b

    def record(a,b):
        return dict(wl_status=a.status,wm_status=b.status,wl_count=a.certified_frame_count,
                    wm_count=b.certified_count,wl_checks=a.support_checks,wm_visited=len(b.components),
                    wl_feasible_piece_counts=[z.lift.space.count for z in a.pieces if z.lift.space.count],
                    wm_feasible_piece_counts=[z.certificate.space.count for z in b.components
                                             if z.certificate.space.count])

    def restrict(full,block):
        A=[tuple(row) for row in full.coefficients]; rhs=list(full.rhs)
        for x in range(6):
            for y in range(6):
                row=[0]*36
                row[6*x+y]+=1
                if x//block==y//block:
                    row[6*(x%block)+(y%block)]-=1
                if any(row):
                    A.append(tuple(row));rhs.append(0)
        return solve_modular_linear(A,rhs,full.prime)

    data={}
    i2=((1,0),(0,1));s2=((1,1),(0,-1));j2=((0,1),(1,0))
    a2=((1,0),(0,3));b2=((1,-2),(0,3))
    swap=packet([(a2,F(1,2)),(b2,F(1,2))])
    a,b=compare(swap,2,embed(s2))
    assert a.certified_frame_count==2**35 and restrict(b.space,2).count==8
    small=wl.WeightedLiftProblem.from_control_packets(swap,swap,2,block_size=2)
    sa=wl.lift_weighted_kernel(small,s2,1)
    restricted=restrict(b.space,2)
    assert sa.certified_frame_count==restricted.count
    for z in sa.all_frames():
        assert b.packet==swap and wm.weighted_lift_seed(swap,embed(z),2,2)
    data['binary_swap_same_input']={**record(a,b),'block_2':sa.certified_frame_count}
    a,b=compare(packet([(a2,F(1,3)),(b2,F(2,3))]),2,embed(s2))
    assert a.status=='NO_LIFTS'
    data['binary_bias_same_input']=record(a,b)

    tri=packet([(((1,3*t),(0,2)),F(1,3)) for t in range(3)])
    a,b=compare(tri,3,eye(6))
    assert a.certified_frame_count==3**18 and restrict(b.space,2).count==9
    data['wl_ternary_same_input']={**record(a,b),'block_2':9}
    pa,pb=compare(tri,3,eye(6),wl_cap=1,wm_cap=1)
    assert not pa.is_complete and not pb.complete
    assert pa.certified_frame_count==0 and pb.certified_count==3**17
    data['same_cap_one_ternary']=record(pa,pb)

    toggle=packet([(((3,9*t),(0,1)),F(1,6)) for t in range(3)],stopped=True)
    a,b=compare(toggle,3,eye(6))
    assert a.certified_frame_count==3**27
    data['wm_ternary_same_input']=record(a,b)

    split=packet([(((2,0),(0,1)),F(1,4)),(((2,4),(0,1)),F(1,4)),
                  (((1,0),(0,2)),F(1,2))])
    a,b=compare(split,2,embed(j2))
    assert a.status=='NO_LIFTS'
    data['fine_class_split']=record(a,b)
    ca,cb=compare(split,2,embed(j2),wl_cap=0,wm_cap=0)
    assert ca.status=='SUPPORT_LIMIT' and cb.status=='NO_LIFTS'
    data['same_cap_zero_split']=record(ca,cb)

    # Two different histograms entries from one germ, kept distinct by their translation and weight.
    same_germ=ControlPacket.from_edges(1,0,1,[(0,0,F(1,3),Affine.identity(6),1),
                                              (0,0,F(2,3),Affine(eye(6),(1,0,0,0,0,0)),1)])
    a,b=compare(same_germ,2,eye(6))
    assert len(a.pieces)==2 and len(b.components)==1
    assert sum(x.lift.space.count for x in a.pieces)==2*a.certified_frame_count
    data['same_packet_overlapping_forests']=record(a,b)

    three_equal=ControlPacket.from_edges(1,0,1,[(0,0,F(1,3),Affine(eye(6),(i,0,0,0,0,0)),1)
                                                 for i in range(3)])
    a,b=compare(three_equal,3,eye(6))
    assert len(a.pieces)==6 and len(b.components)==1
    assert sum(x.lift.space.count for x in a.pieces)==6*a.certified_frame_count
    data['three_indistinguishable_germs']=record(a,b)

    # A low-compatible transporter from the identity action to a nonscalar action can fail above it.
    left=packet([(i2,1)])
    right=packet([(((1,2),(0,1)),1)])
    x=wl.WeightedLiftProblem.from_control_packets(left,right,2)
    bad=wl.lift_weighted_kernel(x,eye(6),1)
    _,self_a=compare(left,2,eye(6))
    assert bad.status=='NO_LIFTS' and self_a.certified_count==2**35
    data['two_packet_obstruction']=dict(wl_transporter=bad.status,wm_left_self=self_a.certified_count)

    # Known-cross-frame adapter. Conjugate a nontrivial singleton action by the reversal of each pair.
    ok_left=packet([(((2,0),(0,1)),1)])
    ok_right=packet([(((1,0),(0,2)),1)])
    cross=wl.WeightedLiftProblem.from_control_packets(ok_left,ok_right,2)
    cross_cert=wl.lift_weighted_kernel(cross,embed(j2),1)
    seed=wm.weighted_lift_seed(ok_left,eye(6),2,1)
    ident=wm.lift_weighted_seed(ok_left,seed)
    assert cross_cert.certified_frame_count==ident.certified_count==2**26
    # Apply the source stabilizer at the next digit, then normalize in the target chart.
    for k in range(len(ident.space.basis)+1):
        pars=tuple(int(j==k) for j in range(len(ident.space.basis)))
        left_frame=ident.instantiate(pars).frame
        mapped=_normalize_frame(mm(embed(j2),matrix(left_frame)),2,2+cross.guard)[0]
        assert cross.row_certificate(mapped,2)
    data['known_transporter_coset']=dict(dimension=len(ident.space.basis),
                                         row_checked=len(ident.space.basis)+1)

    for kind,pkt in [('zero_duration',packet([(i2,1)],duration=0)),
                     ('non_stochastic',packet([(i2,2)])),
                     ('rational_offset',packet([(i2,1)],offset=(F(1,2),0,0,0,0,0)))]:
        prob=wl.WeightedLiftProblem.from_control_packets(pkt,pkt,2)
        aa=wl.lift_weighted_kernel(prob,eye(6),1)
        try:
            wm.weighted_lift_seed(pkt,eye(6),2,1)
        except ValueError as exc:
            data[kind]={'wl':aa.status,'wm_input_rejected':str(exc)}
        else:
            raise AssertionError(kind)
    output=dict(wl_source_sha256=WL_SHA,wm_source_sha256=WM_SHA,exact_cases=data)
    payload=json.dumps(output,sort_keys=True,indent=2)+'\n'
    if args.json: args.json.write_text(payload)
    print('PASS',sha256(payload.encode()).hexdigest())


if __name__=='__main__':
    main()
