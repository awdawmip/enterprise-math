from fractions import Fraction as F
from dataclasses import replace
from itertools import product
from math import comb
from pathlib import Path
import hashlib, json, sys, pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, eye, matrix, mm
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_carry_peak import (compile_carry_peak, peak_probability,
    projective_lattice_key, first_passage_prefix, HIT, UNKNOWN)
from enterprise_math.heartbeat_peak_quotient import (peak_observation_chain, passage_law,
    passage_prefix, compile_peak_quotient, condition_on_hit)
from enterprise_math.heartbeat_peak_symmetry import (AxisControlSymmetry, certify_peak_symmetry,
    verify_peak_symmetry, retained_symmetries, compile_orbit_peak, verify_orbit_peak,
    orbit_peak_chain, symmetric_depth_state_counts, shared_stop_defect_bound)

I=eye(6); Z=(0,)*6

def diag(ds): return matrix([[ds[i] if i==j else 0 for j in range(6)] for i in range(6)])
def act(a): return Affine(a,Z)
U,V=diag((2,2,2,1,1,1)),diag((1,1,1,2,2,2))

def killed(c=F(1,2),bias=F(0),duration=1):
    return ControlPacket.from_edges(2,0,duration,[(0,0,c/2+bias,act(U),1),
        (0,0,c/2-bias,act(V),1),(0,1,1-c,act(I),1),(1,1,1,act(I),1)])

def swap_halves(controls=(0,1)):
    return AxisControlSymmetry((3,4,5,0,1,2),controls)

def full_generators(controls=(0,1)):
    return (AxisControlSymmetry((1,2,3,4,5,0),controls),
            AxisControlSymmetry((1,0,2,3,4,5),controls))

def axis_packet(weights=None,prime=2):
    weights=tuple(weights or (F(1,12),)*6)
    edges=[(0,0,w,act(diag(tuple(prime if j==i else 1 for j in range(6)))),1)
           for i,w in enumerate(weights)]
    edges.extend([(0,1,1-sum(weights),act(I),1),(1,1,1,act(I),1)])
    return ControlPacket.from_edges(2,0,1,edges)

def observed(packet,r,generators=(),cap=10000,**kw):
    cert=certify_peak_symmetry(packet,generators)
    autom=compile_orbit_peak(packet,2,r,cert,max_states=cap,**kw)
    return autom,orbit_peak_chain(packet,autom)

OUT=ROOT/'research_notes/heartbeat_peak_symmetry_20260920_AD0416'
OUT.mkdir(parents=True,exist_ok=True)
REPORT={}


def test_01_reuse_bytes():
    pins={'heartbeat_peak_quotient.py':'db00aaf3be5640b966267a529124556ff713807e',
          'heartbeat_carry_peak.py':'44bde8bbff397adf8aec80fcb2bffa79c6e272e9',
          'brc_control_mass.py':'e8811e5f194fc57b294be7255214361fe99395d5',
          'brc_weighted_recurrent.py':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb'}
    for name,wanted in pins.items():
        data=(ROOT/'src/enterprise_math'/name).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==wanted
    REPORT['unchanged_inherited_modules']=pins


def test_02_group_certificate_and_corruption():
    p=killed(); cert=certify_peak_symmetry(p,(swap_halves(),))
    assert len(cert.elements)==2 and cert.checked_generator_atoms==4
    assert verify_peak_symmetry(p,cert)
    with pytest.raises(ValueError): verify_peak_symmetry(p,replace(cert,packet_digest='bad'))
    with pytest.raises(ValueError): certify_peak_symmetry(p,(swap_halves(),),group_limit=1)
    with pytest.raises(ValueError): AxisControlSymmetry((0,0,2,3,4,5),(0,1))
    with pytest.raises(ValueError): certify_peak_symmetry(p,(swap_halves((0,)),))


def test_03_debt_orbit_before_discovery():
    rows=[]; comparisons=0
    for r in range(1,9):
        p=killed(); raw=compile_carry_peak(p,2,r,max_states=100)
        a,q=observed(p,r,(swap_halves(),),cap=r+1)
        assert a.complete and len(a.states)==r+1
        assert a.expanded_representatives==r+1
        assert a.frozen_controls==(1,)
        assert passage_prefix(q,2*r+8)==first_passage_prefix(p,raw,2*r+8)['hit_by_step']
        prob=peak_probability(p,raw)
        law=passage_law(q)
        assert law.probability[q.initial]==prob.exact
        post=compile_peak_quotient(peak_observation_chain(p,raw)).chain
        assert len(post.kernel)==len(q.kernel)
        assert passage_prefix(post,2*r+8)==passage_prefix(q,2*r+8)
        rows.append({'R':r,'raw_expanded':len(raw.states),'orbit_expanded':len(a.states),
                     'risk':str(prob.exact),'cap':a.state_budget})
        comparisons+=2*r+9
    REPORT['debt_generation_rows']=rows
    REPORT['debt_first_time_equalities']=comparisons


def test_04_bias_refines_symmetry_not_object_rejection():
    p=killed(); base=certify_peak_symmetry(p,(swap_halves(),))
    biased=killed(bias=F(1,16))
    with pytest.raises(ValueError): verify_peak_symmetry(biased,base)
    with pytest.raises(ValueError): certify_peak_symmetry(biased,(swap_halves(),))
    repaired,order=retained_symmetries(biased,base)
    assert order==1
    a=compile_orbit_peak(biased,2,4,repaired)
    assert len(a.states)==8
    raw=compile_carry_peak(biased,2,4)
    assert passage_prefix(orbit_peak_chain(biased,a),12)==first_passage_prefix(biased,raw,12)['hit_by_step']
    REPORT['bias_refinement']={'old_group':2,'new_group':1,'active_sign_preserved':True}


def test_05_six_axis_direct_counts():
    p=axis_packet(); cert=certify_peak_symmetry(p,full_generators())
    assert len(cert.elements)==720
    rows=[]
    for r in range(1,5):
        counts=symmetric_depth_state_counts(r)
        a=compile_orbit_peak(p,2,r,cert,max_states=counts['orbit_safe_with_stop'])
        assert a.complete
        assert len(a.states)==counts['orbit_safe_with_stop']
        assert sum(s.control==0 for s in a.states)==counts['orbit_active']
        assert all(s.lattice==tuple(tuple(sorted(s.lattice[j][j] for j in range(6))[i] if i==k else 0
                    for k in range(6)) for i in range(6)) for s in a.states)
        rows.append({'R':r,**counts,'actual_expanded':a.expanded_representatives,
                     'temporary_successor_keys':a.canonicalized_successors})
    REPORT['six_axis_counts']=rows
    REPORT['six_axis_group_order']=len(cert.elements)


def test_06_six_axis_raw_and_independent_prefix():
    p=axis_packet(); a,q=observed(p,2,full_generators(),cap=7)
    raw=compile_carry_peak(p,2,2,max_states=200)
    assert len(raw.states)==126 and len(a.states)==7
    rawchain=peak_observation_chain(p,raw)
    assert passage_prefix(rawchain,10)==passage_prefix(q,10)
    # independent integer count-vector DP: no HNF and no orbit canonicalizer
    for r in (2,3):
        a,q=observed(p,r,full_generators())
        alive={(0,)*6:F(1)}; expected=[F(0)]
        for n in range(1,11):
            nxt={}; hit=F(0)
            for v,w in alive.items():
                for axis in range(6):
                    fresh=tuple(x+int(i==axis) for i,x in enumerate(v))
                    if max(fresh)-min(fresh)>=r: hit+=w/12
                    else: nxt[fresh]=nxt.get(fresh,F(0))+w/12
            expected.append(hit); alive=nxt
        assert tuple(expected)==passage_prefix(q,10)
    REPORT['raw_six_axis_threshold2']=126
    REPORT['independent_count_vector_first_times']=22


def test_07_exact_risk_and_size_budget_advantage():
    p=axis_packet(); rows=[]
    for r in (2,3):
        cap=comb(r+4,5)+1
        a,q=observed(p,r,full_generators(),cap=cap)
        full=passage_law(q)
        partial=compile_carry_peak(p,2,r,max_states=cap)
        assert not partial.complete
        interval=peak_probability(p,partial)
        assert interval.lower<=full.probability[q.initial]<=interval.upper
        rows.append({'R':r,'same_budget':cap,'raw_interval':[str(interval.lower),str(interval.upper)],
                     'orbit_exact':str(full.probability[q.initial]), 'conditional_arrows':str(full.conditional_time[q.initial])})
    REPORT['budget_advantage']=rows


def test_08_histogram_multiplicity_not_uniform_orbits():
    p=axis_packet(); a,q=observed(p,2,full_generators())
    # From the all-equal state: SIX distinguishable axis choices go to one orbit.
    active0=next(i for i,s in enumerate(a.states) if s.control==0 and s.lattice==tuple(tuple(int(i==j) for j in range(6)) for i in range(6)))
    edges=[e for e in a.edges if e.source==active0]
    targets={e.target for e in edges if a.states[e.target].control==0}
    assert len(targets)==1
    assert sum(e.mass for e in edges if e.target in targets)==F(1,2)
    # Each next increment chooses one of the multiplicities in the depth histogram.
    for i,s in enumerate(a.states):
        if s.control!=0: continue
        k=sum(s.lattice[j][j]==2 for j in range(6))
        hit=sum(e.mass for e in a.edges if e.source==i and e.target==HIT)
        assert hit==F(k,12)
    REPORT['orbit_multiplicity']={'initial_axis_atoms':6,'summed_probability':'1/2','not_orbit_uniform':True}


def test_09_partial_symmetry_subgroup():
    p=axis_packet(); parent=certify_peak_symmetry(p,full_generators())
    p2=axis_packet((F(1,18),)*3+(F(1,9),)*3)
    repaired,order=retained_symmetries(p2,parent)
    assert order==36
    a=compile_orbit_peak(p2,2,2,repaired,max_states=50)
    raw=compile_carry_peak(p2,2,2,max_states=200)
    assert len(a.states)==16  # (4*4-1) active depth-color classes plus stopped
    assert passage_prefix(orbit_peak_chain(p2,a),10)==first_passage_prefix(p2,raw,10)['hit_by_step']
    REPORT['partial_symmetry']={'parent_group':720,'retained_group':36,'orbit_safe':len(a.states),'raw_safe':len(raw.states)}


def test_10_control_phase_must_transform_together():
    # A six-phase fixed scan. Relabeling axes without phase does not preserve law.
    edges=[]
    for i in range(6):
        a=diag(tuple(2 if j==i else 1 for j in range(6)))
        edges.append((i,(i+1)%6,1,act(a),1))
    p=ControlPacket.from_edges(6,0,2,edges)
    cycle=(1,2,3,4,5,0)
    with pytest.raises(ValueError):
        certify_peak_symmetry(p,(AxisControlSymmetry(cycle,tuple(range(6))),))
    cert=certify_peak_symmetry(p,(AxisControlSymmetry(cycle,cycle),))
    for start in (0,3,5):
        a=compile_orbit_peak(p,2,2,cert,initial_control=start)
        raw=compile_carry_peak(p,2,2,initial_control=start)
        assert passage_prefix(orbit_peak_chain(p,a),12)==first_passage_prefix(p,raw,12)['hit_by_step']
        assert a.duration==2 and a.complete
    REPORT['phase_covariance']={'joint_group':6,'axis_only_rejected':True,'initial_distribution_need_not_be_symmetric':True}


def test_11_noncommuting_oriented_orbits():
    a=[list(row) for row in I]; a[0][0]=F(2); a[0][1]=F(1); a=matrix(a)
    b=[list(row) for row in I]; b[1][1]=F(2); b[1][0]=F(1); b=matrix(b)
    assert mm(a,b)!=mm(b,a)
    p=ControlPacket.from_edges(2,0,1,[(0,0,F(1,4),act(a),1),(0,0,F(1,4),act(b),1),
                                    (0,1,F(1,2),act(I),1),(1,1,1,act(I),1)])
    swap=AxisControlSymmetry((1,0,2,3,4,5),(0,1))
    reduced,q=observed(p,3,(swap,),cap=100)
    raw=compile_carry_peak(p,2,3,max_states=200)
    assert raw.complete and reduced.complete
    assert passage_prefix(q,12)==first_passage_prefix(p,raw,12)['hit_by_step']
    risk=passage_law(q).probability[q.initial]
    assert risk==peak_probability(p,raw).exact
    REPORT['noncommuting']={'raw_safe':len(raw.states),'orbit_safe':len(reduced.states),'risk':str(risk)}


def test_12_tilted_false_symmetry_remains_distinct():
    def triple(b):
        out=[[0]*6 for _ in range(6)]
        for k in range(3):
            for i in range(2):
                for j in range(2):out[2*k+i][2*k+j]=b[i][j]
        return matrix(out)
    P,Q,A=map(triple,(((2,0),(0,1)),((2,1),(0,1)),((1,0),(0,2))))
    assert projective_lattice_key(P,2)!=projective_lattice_key(Q,2)
    p=ControlPacket.from_edges(3,0,1,[(0,1,F(1,2),act(P),1),(0,1,F(1,2),act(Q),1),
                                    (1,2,1,act(A),1),(2,2,1,act(I),1)])
    a,q=observed(p,2)
    assert passage_law(q).probability[q.initial]==F(1,2)
    states=[s for s in a.states if s.control==1]
    assert len(states)==2
    REPORT['tilt_witness_retained']=True


def test_13_original_atoms_are_not_global_quotient_channels():
    p=killed(); a,q=observed(p,4,(swap_halves(),))
    assert not q.channels
    with pytest.raises(ValueError): compile_peak_quotient(q,mode='atoms')
    assert len([e for e in a.edges if e.source==0])==3
    REPORT['literal_action_boundary']='representative-frame labels are not original global channels'


def test_14_unknown_bounds_and_tamper_rejection():
    p=killed(); full,q=observed(p,4,(swap_halves(),))
    risk=passage_law(q).probability[q.initial]; rows=[]
    for budget in (1,2,3,4,5):
        a,part=observed(p,4,(swap_halves(),),cap=budget)
        low=passage_law(part).probability[part.initial]
        upper=low+passage_law(part,target='UNKNOWN').probability[part.initial]
        assert low<=risk<=upper
        rows.append([budget,str(low),str(upper)])
    with pytest.raises(ValueError): verify_orbit_peak(p,replace(full,threshold=3))
    with pytest.raises(ValueError): verify_orbit_peak(p,replace(full,edges=full.edges[:-1]))
    assert all(a<=b for _,a,b in [(x,F(y),F(z)) for x,y,z in rows])
    REPORT['orbit_budget_bounds']=rows


def test_15_scalar_units_offsets_and_no_fake_resampling():
    p=ControlPacket.from_edges(1,0,1,[(0,0,F(1,2),Affine(I,(3,0,0,0,0,0)),2)])
    a,q=observed(p,4,(AxisControlSymmetry((1,2,3,4,5,0),(0,)),))
    assert len(a.states)==1 and passage_law(q).probability[q.initial]==0
    assert a.edges[0].weight==F(1,2) and a.edges[0].multiplicity==2
    # Spatial offsets are irrelevant only because the observer is linear carry.
    REPORT['mass_and_offset_boundary']={'mass':'1','multiplicity':2,'position_not_preserved':True}


def test_16_initial_threshold_and_input_errors():
    p=killed(); cert=certify_peak_symmetry(p,(swap_halves(),))
    a=compile_orbit_peak(p,2,0,cert)
    assert a.initial_hit and passage_law(orbit_peak_chain(p,a)).probability[0]==1
    for fn in (lambda:compile_orbit_peak(p,4,2,cert),lambda:compile_orbit_peak(p,2,-1,cert),
               lambda:compile_orbit_peak(p,2,2,cert,max_states=0),
               lambda:compile_orbit_peak(p,2,2,cert,initial_control=2),
               lambda:symmetric_depth_state_counts(0),
               lambda:shared_stop_defect_bound(F(3,4),F(1,2))):
        with pytest.raises((ValueError,TypeError)):fn()


def test_17_doob_and_first_time_reuse():
    p=killed(); a,q=observed(p,6,(swap_halves(),))
    raw=compile_carry_peak(p,2,6)
    rawchain=peak_observation_chain(p,raw)
    cond,_=condition_on_hit(q); ref,_=condition_on_hit(rawchain)
    assert passage_prefix(cond,25)==passage_prefix(ref,25)
    law=passage_law(q)
    assert law.probability[q.initial]==F(1,1351) and law.conditional_time[q.initial]==F(9360,1351)
    REPORT['conditioned_law_reused']={'risk':'1/1351','conditional_arrows':'9360/1351'}


def test_18_little_bias_is_quantified_not_erased():
    eps=F(1,16); bound=shared_stop_defect_bound(eps,F(1,2))
    assert bound==F(1,9)
    rows=[]
    for r in range(1,6):
        sym=killed(); biased=killed(bias=eps)
        sa,sq=observed(sym,r,(swap_halves(),))
        ba,bq=observed(biased,r)
        ps,pb=passage_law(sq).probability[sq.initial],passage_law(bq).probability[bq.initial]
        assert abs(ps-pb)<=bound
        fp,fq=passage_prefix(sq,12),passage_prefix(bq,12)
        for n in range(13):
            assert abs(sum(fp[:n+1])-sum(fq[:n+1]))<=shared_stop_defect_bound(eps,F(1,2),n)
        rows.append([r,str(ps),str(pb),str(abs(pb-ps))])
    REPORT['symmetry_defect_risk_rows']=rows
    REPORT['defect_uniform_bound']=str(bound)


def test_19_no_termination_no_small_all_time_defect_bound():
    from enterprise_math.heartbeat_peak_quotient import PeakChain
    eps=F(1,1000)
    stable=PeakChain(((F(1),F(0)),(F(0),F(1))),('SAFE','HIT'))
    leaky=PeakChain(((1-eps,eps),(F(0),F(1))),('SAFE','HIT'))
    assert passage_law(stable).probability[0]==0 and passage_law(leaky).probability[0]==1
    assert shared_stop_defect_bound(eps,F(0))==1
    REPORT['no_stop_counterexample']={'one_step_TV':'1/1000','all_time_risk_gap':'1'}


def test_20_six_axis_histogram_law_independent():
    # Independent six-state recurrence for R=2: k high coordinates; choosing a
    # high coordinate hits, otherwise k increases and 5->0 after common carry.
    from enterprise_math.heartbeat_peak_quotient import PeakChain
    c=F(1,2); kernel=[[F(0)]*8 for _ in range(8)]
    for k in range(6):
        kernel[k][6]=c*k/6
        kernel[k][(k+1)%6]=c*(6-k)/6
        kernel[k][7]=1-c
    kernel[6][6]=kernel[7][7]=F(1)
    independent=PeakChain(tuple(map(tuple,kernel)),('SAFE',)*6+('HIT','SAFE'))
    p=axis_packet(); a,q=observed(p,2,full_generators())
    x=passage_law(independent); y=passage_law(q)
    assert x.probability[independent.initial]==y.probability[q.initial]
    assert x.conditional_time[independent.initial]==y.conditional_time[q.initial]
    assert passage_prefix(independent,20)==passage_prefix(q,20)
    REPORT['six_axis_threshold2_exact']={'risk':str(y.probability[q.initial]),'conditional_arrows':str(y.conditional_time[q.initial]),
                                        'raw_active':63,'generated_active':6}


def test_21_checked_defect_certificate():
    from enterprise_math.heartbeat_peak_symmetry import certify_stopped_law_comparison
    cert=certify_stopped_law_comparison(killed(),killed(bias=F(1,16)),2,stop_control=1)
    assert cert.row_total_variations==(F(1,16),F(0))
    assert cert.common_stop==F(1,2) and cert.all_time_risk_error==F(1,9)
    bad=ControlPacket.from_edges(2,0,1,[(0,1,1,act(U),1),(1,1,1,act(I),1)])
    with pytest.raises(ValueError): certify_stopped_law_comparison(killed(),bad,2,stop_control=1)
    badstop=ControlPacket.from_edges(2,0,1,[(0,1,1,act(I),1),(1,0,1,act(I),1)])
    with pytest.raises(ValueError): certify_stopped_law_comparison(killed(),badstop,2,stop_control=1)
    REPORT['checked_residual_certificate']={'TV':'1/16','common_stop':'1/2','risk_error':'1/9',
                                           'false_stop_rejected':True}


def test_22_width_is_not_histogram():
    p=axis_packet(); a,q=observed(p,2,full_generators())
    risks={}
    for i,s in enumerate(a.states):
        if s.control==0:
            k=sum(s.lattice[j][j]==2 for j in range(6))
            risks[k]=sum(e.mass for e in a.edges if e.source==i and e.target==HIT)
    assert risks[1]==F(1,12) and risks[5]==F(5,12)
    REPORT['same_gap_different_population']={'gap':1,'one_high_next_hit':'1/12','five_high_next_hit':'5/12'}


def test_23_common_stop_bound_is_attained_by_native_actions():
    from enterprise_math.heartbeat_peak_symmetry import certify_stopped_law_comparison
    eps,eta=F(1,100),F(1,5)
    h=diag((2,1,1,1,1,1))
    ref=ControlPacket.from_edges(2,0,1,[(0,0,1-eta,act(I),1),(0,1,eta,act(I),1),(1,1,1,act(I),1)])
    pert=ControlPacket.from_edges(2,0,1,[(0,0,1-eta-eps,act(I),1),(0,0,eps,act(h),1),
                                       (0,1,eta,act(I),1),(1,1,1,act(I),1)])
    cert=certify_stopped_law_comparison(ref,pert,2,stop_control=1)
    ra,rq=observed(ref,1)
    pa,pq=observed(pert,1)
    gap=passage_law(pq).probability[pq.initial]-passage_law(rq).probability[rq.initial]
    assert gap==cert.all_time_risk_error==eps/(eta+eps)==F(1,21)
    REPORT['sharp_defect_witness']={'row_TV':'1/100','common_stop':'1/5','actual_risk_gap':'1/21','bound':'1/21'}


def teardown_module():
    (OUT/'RESULTS.json').write_text(json.dumps({'status':'SEE_PYTEST_RESULT','checks':REPORT,
        'scope':'research candidate; no full-repository, independent review, or production claim'},
        ensure_ascii=False,indent=2)+'\n')
