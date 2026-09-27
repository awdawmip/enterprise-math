"""Scoped BRC-only checks; the oracle is the inherited BRC row/germ kernel.

No classical dynamics, matrix exponential, numeric approximation, or untyped
physics reference is run. Small repair candidates are passed to the inherited
full BRC row certificate; probability checks reuse its original peak compiler.
"""
from dataclasses import replace
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib,json,subprocess,sys
import pytest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import matrix,mm,eye,Affine
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_congruence_lift import GermLiftProblem,lift_germ_seed
from enterprise_math.heartbeat_weighted_germ_lift import (
    WeightedLiftProblem, PositiveTransport, lift_weighted_kernel,
)
from enterprise_math.heartbeat_carry_peak import compile_carry_peak
from enterprise_math.heartbeat_peak_quotient import (
    peak_observation_chain,passage_law,passage_prefix,compile_peak_quotient,
)
from enterprise_math.heartbeat_peak_orbits import (
    Frame,FiniteFrameGroup,certify_peak_symmetry,compile_orbit_peak,orbit_observation_chain,
)
REPORT={}
I2=((1,0),(0,1));J2=((0,1),(1,0));U2=((2,0),(0,1));V2=((1,0),(0,2))
A2=((1,0),(0,3));B2=((1,-2),(0,3));S2=((1,1),(0,-1))

def block(a):
    n=len(a)
    return matrix([[a[i%n][j%n] if i//n==j//n else 0 for j in range(6)] for i in range(6)])

def packet(actions,weights,*,translation=(0,)*6,counts=None):
    counts=counts or [1]*len(actions)
    return ControlPacket.from_edges(1,0,1,[(0,0,w,Affine(block(a),translation),n)
                                         for a,w,n in zip(actions,weights,counts)])

@lru_cache(None)
def alternative_problem(dim=2,biased=False):
    a=packet([A2,B2],[F(1,3),F(2,3)] if biased else [F(1,2)]*2)
    return WeightedLiftProblem.from_control_packets(a,a,2,block_size=dim)

@lru_cache(None)
def ternary_problem(dim=2):
    a=packet([((1,3*t),(0,2)) for t in range(3)],[F(1,3)]*3)
    return WeightedLiftProblem.from_control_packets(a,a,3,block_size=dim)

@lru_cache(None)
def lift_ternary(dim=2):return lift_weighted_kernel(ternary_problem(dim),eye(dim),1)

@lru_cache(None)
def split_problem(k=1,dim=2):
    ue=mm(matrix(U2),matrix(((1,2**k),(0,1))))
    a=packet([U2,ue,V2],[F(1,4),F(1,4),F(1,2)])
    return WeightedLiftProblem.from_control_packets(a,a,2,block_size=dim)

def complete_oracle(prob,seed,m):
    """Independent enumeration of the finite frame fibre, checked ONLY by BRC."""
    s,pivot=prob.normalize_seed(seed,m);n=prob.block_size;p=prob.prime
    slots=[i for i in range(n*n) if i!=pivot];out=set();checked=0
    for vals in product(range(p),repeat=len(slots)):
        z=[0]*(n*n)
        for i,v in zip(slots,vals):z[i]=v
        f=tuple(tuple(s[i][j]+p**(m+prob.guard)*z[n*i+j] for j in range(n)) for i in range(n))
        checked+=1
        if prob.row_certificate(f,m+1):out.add(f)
    return out,checked

@lru_cache(None)
def peak_packet(split=False):
    u,v=block(U2),block(V2)
    items=[(u,F(1,4)),(v,F(1,4))]
    if split:items=[(u,F(1,8)),(mm(u,block(((1,2),(0,1)))),F(1,8)),(v,F(1,4))]
    return ControlPacket.from_edges(2,0,1,[(0,0,w,Affine(a,(0,)*6),1) for a,w in items]+[
        (0,1,F(1,2),Affine(eye(6),(0,)*6),1),
        (1,1,1,Affine(eye(6),(0,)*6),1)])

@lru_cache(None)
def peak_run(split,R):
    a=peak_packet(split); aut=compile_carry_peak(a,2,R,max_states=400)
    ch=peak_observation_chain(a,aut)
    q=compile_peak_quotient(ch)
    return aut,ch,q,passage_law(ch)

@pytest.fixture(scope='session',autouse=True)
def save_report():
    yield
    path=ROOT/'research_notes/heartbeat_weighted_lift_20260927_AD0416/RESULTS.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+'\n')


def test_01_frozen_brc_sources():
    tracked=['brc_transport.py','brc_control_port.py','heartbeat_congruence_lift.py',
             'heartbeat_peak_orbits.py','heartbeat_carry_peak.py','heartbeat_peak_quotient.py',
             'brc_weighted_recurrent.py','brc_control_mass.py','brc_histogram.py']
    hashes={}
    for name in tracked:
        p='src/enterprise_math/'+name;raw=(ROOT/p).read_bytes()
        expected=json.loads((ROOT/'research_notes/heartbeat_weighted_lift_20260927_AD0416/FROZEN_DEPENDENCIES.json').read_text())['files'][p]
        assert hashlib.sha256(raw).hexdigest()==expected
        hashes[name]=hashlib.sha256(raw).hexdigest()
    REPORT['frozen_brc_sources']=hashes


def test_02_split_positive_transport():
    c=PositiveTransport((F(1,8),F(3,8)),(F(1,2),),((0,0,F(1,8)),(1,0,F(3,8))))
    assert c.verify([(0,0),(1,0)])
    REPORT['split_coupling']={'row_masses':['1/8','3/8'],'target_mass':'1/2'}


def test_03_transport_tampering():
    c=PositiveTransport((F(1),),(F(1),),((0,0,F(1)),))
    for bad in [replace(c,entries=((0,0,F(2)),)),replace(c,entries=((0,0,F(-1)),)),
                replace(c,entries=((0,0,F(1)),(0,0,F(1))))]:
        with pytest.raises(ValueError):bad.verify([(0,0)])


def test_04_changed_correspondence_rescues():
    p=alternative_problem();c=lift_weighted_kernel(p,S2,1)
    fixed=GermLiftProblem.build([A2,B2],[A2,B2],2)
    old=lift_germ_seed(fixed,fixed.seed(S2,[1,1],1))
    assert old.space.count==0
    assert c.status=='COMPLETE' and c.certified_frame_count==8 and c.verify()
    assert sorted(x.lift.space.count for x in c.pieces)==[0,8]
    REPORT['changed_correspondence']={'fixed_identity_lifts':0,'weighted_lifts':8}


def test_05_all_rescued_frames_checked():
    p=alternative_problem();c=lift_weighted_kernel(p,S2,1)
    truth,steps=complete_oracle(p,S2,1)
    assert set(c.all_frames())==truth
    REPORT['rescued_fibre_oracle']={'candidates':steps,'valid':len(truth)}


def test_06_bias_removes_rescue():
    p=alternative_problem(biased=True);c=lift_weighted_kernel(p,S2,1)
    assert c.status=='NO_LIFTS' and c.verify()
    assert all(not piece.lift.space.count for piece in c.pieces)
    REPORT['bias']={'weights':['1/3','2/3'],'next_lifts':0}


def test_07_ternary_affine_union():
    c=lift_ternary()
    assert c.status=='COMPLETE' and c.support_checks==336 and len(c.pieces)==6
    assert sorted(x.lift.space.count for x in c.pieces)==[0,0,0,3,3,3]
    assert c.certified_frame_count==9 and len(c.repairs.basis)==2
    assert c.verify()
    REPORT['ternary_union']={'coupling_vertices':6,'nonempty_families':3,
        'fixed_family_size':3,'combined_frame_count':9,'combined_free_dimension':2}


def test_08_ternary_oracle():
    c=lift_ternary();truth,steps=complete_oracle(c.problem,eye(2),1)
    assert set(c.all_frames())==truth
    REPORT['ternary_oracle']={'candidates':steps,'valid':len(truth)}


def test_09_full_six_axis_symbolic():
    c=lift_ternary(6)
    assert c.certified_frame_count==3**18 and len(c.repairs.basis)==18 and c.verify()
    for i in range(19):
        par=[0]*18
        if i<18:par[i]=1
        assert c.problem.row_certificate(c.frame(par),2)
    with pytest.raises(ValueError):c.all_frames(limit=1000)
    REPORT['full_native_x6']={'field':3,'equations_per_support':109,
        'support_solutions':[x.lift.space.count for x in c.pieces],
        'free_dimension':18,'exact_repair_count':c.certified_frame_count,
        'additional_reconstructed_frames':19,'all_repairs_enumerated':False}


def test_10_overlap_not_double_counted():
    a=packet([I2,I2],[F(1,3),F(2,3)]);b=packet([I2,I2],[F(1,4),F(3,4)])
    p=WeightedLiftProblem.from_control_packets(a,b,2,block_size=2)
    c=lift_weighted_kernel(p,eye(2),1)
    assert len(c.pieces)==2 and sum(x.lift.space.count for x in c.pieces)==16
    assert c.certified_frame_count==8 and c.verify()
    REPORT['overlapping_witnesses']={'naive_sum':16,'distinct_frames':8}


def test_11_zero_budget_not_no_lift():
    c=lift_weighted_kernel(ternary_problem(),eye(2),1,max_support_checks=0)
    assert c.status=='SUPPORT_LIMIT' and not c.is_complete and c.repairs is None and c.verify()


def test_12_partial_affine_family_is_safe():
    p=ternary_problem();counts=[]
    for budget in (1,30,50,80,100):
        c=lift_weighted_kernel(p,eye(2),1,max_support_checks=budget)
        assert c.status=='SUPPORT_LIMIT'
        for f in c.all_frames():assert p.row_certificate(f,2)
        assert c.verify();counts.append((budget,c.certified_frame_count))
    REPORT['budget_frontier']=counts


def test_13_mass_split_lifetime():
    out=[]
    for k in (1,2,3):
        p=split_problem(k)
        for m in range(1,k+1):
            c=lift_weighted_kernel(p,J2,m)
            assert c.certified_frame_count==(0 if m==k else 2)
            assert c.verify()
            out.append((k,m,c.status,c.certified_frame_count))
    REPORT['collision_lifetime']=out


def test_14_split_obstruction_full_six_axes():
    p=split_problem(1,6);c=lift_weighted_kernel(p,block(J2),1)
    assert c.status=='NO_LIFTS' and c.verify()
    assert len(c.pieces)==1
    sol=c.pieces[0].lift.space
    assert sol.obstruction is not None
    REPORT['joint_mass_split_obstruction']={'shared_frame_dimension':6,'support_count':1,
        'left_annihilator_nonzero':True,'all_high_digit_frames_rejected':True}


def test_15_original_atom_weight_multiplicity():
    a=packet([U2,V2],[F(1,8),F(1,4)],counts=[2,1])
    p=WeightedLiftProblem.from_control_packets(a,a,2,block_size=2)
    assert sorted((x.weight,x.multiplicity,x.mass) for x in p.left)==[
        (F(1,8),2,F(1,4)),(F(1,4),1,F(1,4))]
    c=lift_weighted_kernel(p,J2,1)
    assert c.repairs is not None
    assert p.left_packet==a and p.right_packet==a


def test_16_affine_offset_is_retained_but_not_observed():
    a=packet([I2],[F(1)],translation=(1,2,3,4,5,6));b=packet([I2],[F(1)])
    p=WeightedLiftProblem.from_control_packets(a,b,2,block_size=2)
    c=lift_weighted_kernel(p,eye(2),1)
    assert c.certified_frame_count==8
    assert p.left[0].translation!=p.right[0].translation


def test_17_control_ports_cannot_mix():
    a=ControlPacket.from_edges(2,0,1,[(0,0,1,Affine.identity(6),1),(1,1,1,Affine.identity(6),1)])
    b=ControlPacket.from_edges(2,0,1,[(0,1,1,Affine.identity(6),1),(1,0,1,Affine.identity(6),1)])
    p=WeightedLiftProblem.from_control_packets(a,b,2,block_size=2)
    with pytest.raises(ValueError):lift_weighted_kernel(p,eye(2),1)


def test_18_invalid_types_time_and_block():
    a=alternative_problem().left_packet
    for left,right,p,bs in [(a,a.at(1),2,2),(a,a,4,2),(a,a,2,4),(object(),a,2,2)]:
        with pytest.raises((ValueError,TypeError)):
            WeightedLiftProblem.from_control_packets(left,right,p,block_size=bs)
    with pytest.raises(ValueError):lift_weighted_kernel(alternative_problem(),S2,0)
    with pytest.raises(ValueError):lift_weighted_kernel(alternative_problem(),S2,1,max_support_checks=True)


def test_19_certificates_are_bound():
    c=lift_ternary()
    with pytest.raises(ValueError):replace(c,support_checks=c.support_checks+1).verify()
    bad=replace(c.problem,guard=c.problem.guard+1)
    with pytest.raises(ValueError):lift_weighted_kernel(bad,eye(2),1)


def test_20_individual_joint_obstruction_retained():
    a=((1,1),(0,1));b=((3,1),(0,1))
    pkt=packet([a,b],[F(1,2)]*2)
    p=WeightedLiftProblem.from_control_packets(pkt,pkt,2,block_size=2)
    c=lift_weighted_kernel(p,a,1)
    assert c.status=='NO_LIFTS' and c.verify()


def test_21_brc_exact_risk_and_stronger_certificate():
    out=[]
    for R in (2,3):
        plain,base,q0,law0=peak_run(False,R)
        mod,ch,q1,law1=peak_run(True,R)
        assert base.kernel==ch.kernel and base.colors==ch.colors
        assert q0.chain.kernel==q1.chain.kernel and q0.chain.colors==q1.chain.colors
        assert law0.probability[0]==law1.probability[0]
        assert passage_prefix(base,20)==passage_prefix(ch,20)
        group=FiniteFrameGroup.generated(2,2,[Frame((0,1),block(J2))])
        if R==2:assert certify_peak_symmetry(peak_packet(True),group,R,mode='threshold')
        else:
            with pytest.raises(ValueError):certify_peak_symmetry(peak_packet(True),group,R,mode='threshold')
        out.append({'R':R,'same_complete_probability_kernel':True,
                    'probability':str(law0.probability[0]),'safe_states':len(mod.states)})
    REPORT['certificate_vs_observation']=out


def test_22_deeper_observation_detects_difference():
    a,x,_,la=peak_run(False,4);b,y,_,lb=peak_run(True,4)
    assert la.probability[0]==F(1,97) and lb.probability[0]==F(11717,1135289)
    px,py=passage_prefix(x,8),passage_prefix(y,8)
    assert px[:8]==py[:8] and px[8]==F(7,16384) and py[8]==F(57,131072)
    REPORT['deeper_risk']={'R':4,'base_hit':str(la.probability[0]),'split_hit':str(lb.probability[0]),
        'base_states':len(a.states),'split_states':len(b.states),
        'first_time_difference':8,'base_first_hit_at_8':str(px[8]),'split_first_hit_at_8':str(py[8])}


def test_23_symbolic_fibre_closure_on_prime_field():
    c=lift_ternary();p=c.problem
    for vals in product(range(3),repeat=2):assert p.row_certificate(c.frame(vals),2)
    assert c.repairs.verify()


def test_24_true_germ_transport_is_more_than_total_mass():
    a=packet([U2],[F(1)]);b=packet([V2],[F(1)])
    p=WeightedLiftProblem.from_control_packets(a,b,2,block_size=2)
    assert sum(x.mass for x in p.left)==sum(x.mass for x in p.right)
    assert not p.row_certificate(eye(2),1)
    assert p.row_certificate(J2,1)


def test_25_all_small_fibres_compared_to_inherited_brc():
    checks=0
    for p,seed,m in [(alternative_problem(),S2,1),(alternative_problem(biased=True),S2,1),
                     (ternary_problem(),eye(2),1),(split_problem(1),J2,1),
                     (split_problem(2),J2,1),(split_problem(2),J2,2)]:
        c=lift_weighted_kernel(p,seed,m);truth,n=complete_oracle(p,seed,m)
        assert set(c.all_frames())==truth
        checks+=n
    REPORT['complete_small_fibre_cross_checks']={'cases':6,'candidate_frames':checks,
        'oracle':'unchanged inherited BRC weighted row-germ certificate'}
