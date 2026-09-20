from __future__ import annotations
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import random
import sys
import pytest
from sympy import Matrix as SM, ZZ
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, eye, matrix, mm, inv
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_carry_peak import (compile_carry_peak, peak_probability,
    first_passage_prefix, first_hit_generating_value, projective_lattice_key)
from enterprise_math.heartbeat_peak_quotient import (PeakChain, compile_peak_quotient,
    peak_observation_chain, verify_peak_quotient, passage_law, passage_prefix,
    condition_on_hit, compile_first_passage_model, distinguishing_first_time)
# Fixture/oracle bodies extracted from the inherited tests; the production
# BRC modules are reused unchanged. This avoids a remote test-file dependency.
I=eye(6)
ZERO=(0,)*6
def diag(values):
    return matrix([[v if i == j else 0 for j in range(6)] for i, v in enumerate(values)])
U,V=diag((2,2,2,1,1,1)),diag((1,1,1,2,2,2))

def triple(b):
    out = [[0]*6 for _ in range(6)]
    for k in range(3):
        for i in range(2):
            for j in range(2):
                out[2*k+i][2*k+j] = b[i][j]
    return matrix(out)

def act(a, offset=ZERO):
    return Affine(a, offset)

def killed(c=F(1,2), conjugator=None):
    u, v = U, V
    if conjugator is not None:
        u, v = [mm(mm(conjugator,a),inv(conjugator)) for a in (u,v)]
    edges = [(0,0,c/2,act(u),1),(0,0,c/2,act(v),1),(1,1,1,act(I),1)]
    if c < 1:
        edges.append((0,1,1-c,act(I),1))
    return ControlPacket.from_edges(2,0,1,edges)

def independent_smith(a, p=2):
    d = smith_normal_form(SM(a), domain=ZZ)
    vals = []
    for i in range(6):
        n = abs(int(d[i,i])); exponent=0
        assert n
        while n%p==0:
            exponent+=1; n//=p
        vals.append(exponent)
    return tuple(sorted(vals))

def literal_first_hits(packet, r, steps):
    atoms=[]
    for s,t,h in packet.blocks:
        for w,a,c in h.entries:
            atoms.append((s,t,w*c,a.a))
    alive=[(0,I,F(1))]
    hits=[F(r==0)]+[F(0)]*steps
    if r==0:
        return tuple(hits),0
    checks=0
    for t in range(1,steps+1):
        following=[]
        for s,b,mass in alive:
            for src,dst,w,a in atoms:
                if src!=s: continue
                m=mm(a,b)
                depths=independent_smith(m)
                checks+=1
                if depths[-1]-depths[0]>=r:
                    hits[t]+=mass*w
                else:
                    following.append((dst,m,mass*w))
        alive=following
    return tuple(hits),checks


OUT=ROOT/'research_notes/heartbeat_peak_quotient_20260920_AD0416'
OUT.mkdir(parents=True,exist_ok=True)
REPORT={}


def observed(p,r=4,cap=1000):
    a=compile_carry_peak(p,2,r,max_states=cap)
    return a,peak_observation_chain(p,a)


def cheb(x,r):
    a,b=F(1),F(x)
    if r==0: return a
    for _ in range(1,r): a,b=b,2*x*b-a
    return b


def direct_chain(rows,colors,initial=0):
    return PeakChain(tuple(tuple(F(x) for x in row) for row in rows),tuple(colors),initial)


def test_01_inherited_source_integrity():
    pins={
       'brc_control_mass.py':'e8811e5f194fc57b294be7255214361fe99395d5',
       'brc_weighted_recurrent.py':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb',
       'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
       'heartbeat_carry_peak.py':'44bde8bbff397adf8aec80fcb2bffa79c6e272e9'}
    for f,h in pins.items():
        b=(ROOT/'src/enterprise_math'/f).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==h
    REPORT['unchanged_inherited_modules']=pins


def test_02_exact_radial_quotient_counts_and_laws():
    rows=[]; checks=0
    p=killed()
    for r in range(1,9):
        a,c=observed(p,r)
        cert=compile_peak_quotient(c)
        assert verify_peak_quotient(c,cert)
        qa=compile_peak_quotient(c,mode='atoms')
        assert verify_peak_quotient(c,qa)
        assert len(a.states)==4*r-2
        assert cert.chain.colors.count('SAFE')==r+1
        assert qa.chain.colors.count('SAFE')==2*r
        first=first_passage_prefix(p,a,32)['hit_by_step']
        assert passage_prefix(cert.chain,32)==first
        assert passage_prefix(qa.chain,32)==first
        raw,q=passage_law(c),passage_law(cert.chain)
        assert raw.probability[c.initial]==q.probability[cert.chain.initial]
        assert raw.conditional_time[c.initial]==q.conditional_time[cert.chain.initial]
        checks+=66
        rows.append({'R':r,'raw_safe':len(a.states),'mass_safe':r+1,'atom_safe':2*r,
          'mass_star_useful':q.useful_states,'raw_star_useful':raw.useful_states,
          'probability':str(q.probability[cert.chain.initial]),
          'conditional_arrows':str(q.conditional_time[cert.chain.initial])})
    REPORT['radial_rows']=rows;REPORT['radial_prefix_equalities']=checks


def test_03_symmetric_merge_not_valid_for_action_choice():
    a,c=observed(killed(),3)
    plus=projective_lattice_key(U,2);minus=projective_lattice_key(V,2)
    i=next(i for i,s in enumerate(a.states) if s.control==0 and s.lattice==plus)
    j=next(i for i,s in enumerate(a.states) if s.control==0 and s.lattice==minus)
    mass=compile_peak_quotient(c); atoms=compile_peak_quotient(c,mode='atoms')
    assert mass.labels[i]==mass.labels[j]
    assert atoms.labels[i]!=atoms.labels[j]
    # A declared change of probabilities, not a numerical perturbation.
    biased=ControlPacket.from_edges(2,0,1,[(0,0,F(3,8),act(U),1),
            (0,0,F(1,8),act(V),1),(0,1,F(1,2),act(I),1),(1,1,1,act(I),1)])
    aa,cc=observed(biased,3)
    bplus=next(k for k,s in enumerate(aa.states) if s.control==0 and s.lattice==plus)
    bminus=next(k for k,s in enumerate(aa.states) if s.control==0 and s.lattice==minus)
    bq=compile_peak_quotient(cc)
    assert bq.labels[bplus]!=bq.labels[bminus]
    with pytest.raises(ValueError):verify_peak_quotient(cc,mass)
    REPORT['direction_erasure_boundary']={'symmetric_mass_merge':True,'atom_merge':False,
                                         'biased_mass_merge':False,'changed_law_rejected':True}


def test_04_distinct_shear_orientation_is_retained():
    p,q,a=triple(((2,0),(0,1))),triple(((2,1),(0,1))),triple(((1,0),(0,2)))
    packet=ControlPacket.from_edges(3,0,1,[(0,1,F(1,2),act(p),1),(0,1,F(1,2),act(q),1),
                                          (1,2,1,act(a),1),(2,2,1,act(I),1)])
    auto,chain=observed(packet,2)
    i=next(i for i,s in enumerate(auto.states) if s.control==1 and s.lattice==projective_lattice_key(p,2))
    j=next(i for i,s in enumerate(auto.states) if s.control==1 and s.lattice==projective_lattice_key(q,2))
    cert=compile_peak_quotient(chain)
    assert cert.labels[i]!=cert.labels[j]
    model=compile_first_passage_model(chain)
    assert distinguishing_first_time(model,model.safe_indices.index(i),model.safe_indices.index(j))==1
    assert passage_law(cert.chain).probability[cert.chain.initial]==F(1,2)


def test_05_eventual_probability_does_not_preserve_time():
    # a -> HIT or never-hit; b -> a. Both eventual probability 1/2.
    c=direct_chain([[0,0,F(1,2),F(1,2)], [1,0,0,0], [0,0,1,0],[0,0,0,1]],
                   ['SAFE','SAFE','HIT','SAFE'])
    law=passage_law(c)
    assert law.probability[0]==law.probability[1]==F(1,2)
    assert law.conditional_time[:2]==(1,2)
    q=compile_peak_quotient(c)
    assert q.labels[0]!=q.labels[1]
    m=compile_first_passage_model(c)
    assert distinguishing_first_time(m,0,1)==1
    REPORT['same_event_different_time']={'ever_probability':'1/2','conditional_times':[1,2]}


def test_06_alltime_signature_strictly_weaker_than_lumping():
    # a->c; b->1/2 d+1/2 e; c->1/2 HIT+1/2 z; d->HIT; e,z never hit.
    n=7; rows=[[F(0)]*n for _ in range(n)]
    rows[0][2]=1; rows[1][3]=rows[1][4]=F(1,2)
    rows[2][6]=rows[2][5]=F(1,2); rows[3][6]=1; rows[4][5]=1;rows[5][5]=1;rows[6][6]=1
    c=PeakChain(tuple(map(tuple,rows)),('SAFE',)*6+('HIT',))
    q=compile_peak_quotient(c); model=compile_first_passage_model(c)
    assert q.labels[0]!=q.labels[1]
    assert model.basis[0]==model.basis[1]
    assert distinguishing_first_time(model,0,1) is None
    assert model.rank==2
    assert passage_prefix(c,20)==passage_prefix(replace(c,initial=1),20)
    assert tuple(model.coefficient(i) for i in range(21))==passage_prefix(c,20)
    REPORT['law_equivalence_not_markov_lumping']={'safe_states':6,'safe_bisimulation_classes':5,
       'equal_law_states':[0,1],'observable_rank':2,'positive_lumping_rejected':True}


def test_07_exact_krylov_coefficients_and_signed_readout():
    p=killed();cases=0
    for r in range(1,9):
        _,c=observed(p,r); model=compile_first_passage_model(c)
        assert model.rank==r
        prefix=passage_prefix(c,50)
        assert tuple(model.coefficient(t) for t in range(51))==prefix
        if r>=4:assert any(x<0 for row in model.transition for x in row)
        cases+=51
    _,c=observed(p,4); a=passage_prefix(c,30)
    assert a[4]==F(1,128)
    for n in range(5,31):assert a[n]==F(1,4)*a[n-2]-F(1,128)*a[n-4]
    assert all(x>=0 for x in a)
    REPORT['krylov_prefix_checks']=cases
    REPORT['signed_analytic_recurrence']={'R':4,'a4':'1/128','law':'a_n=(1/4)a_(n-2)-(1/128)a_(n-4), n>4',
        'all_probability_coefficients_nonnegative':True,'not_positive_BRC_transition':True}


def test_08_doob_hit_conditioning_and_commutation():
    rows=[];checks=0
    for r in range(2,8):
        _,c=observed(killed(),r); cert=compile_peak_quotient(c)
        cr,keep_raw=condition_on_hit(c); cq,keep_q=condition_on_hit(cert.chain)
        pre=passage_prefix(c,35); pc=passage_prefix(cr,35)
        h=passage_law(c).probability[c.initial]
        assert pc==tuple(x/h for x in pre)
        assert passage_prefix(cq,35)==pc
        assert passage_law(cr).probability[cr.initial]==1
        # Check K^h P = P Q^h entrywise, with zero-risk states removed.
        qpos={j:i for i,j in enumerate(keep_q)}
        labels=[qpos[cert.labels[j]] for j in keep_raw]
        for i,old in enumerate(keep_raw):
            for g in range(len(keep_q)):
                total=sum(cr.kernel[i][j] for j in range(len(keep_raw)) if labels[j]==g)
                assert total==cq.kernel[labels[i]][g];checks+=1
        rows.append({'R':r,'probability':str(h),
                     'conditional_arrows':str(passage_law(cr).conditional_time[cr.initial])})
    REPORT['doob_commutation_equalities']=checks;REPORT['conditional_rows']=rows


def test_09_rare_risk_direction_and_chebyshev_mean():
    r=6;_,c=observed(killed(),r);q=compile_peak_quotient(c).chain
    cond,keep=condition_on_hit(q)
    # canonical BFS radial order: 0,1,...,R with HIT at R after stop removal
    assert cond.kernel[1][2]==F(7,8) and cond.kernel[1][0]==F(1,8)
    assert cond.kernel[2][3]==F(13,14) and cond.kernel[2][1]==F(1,14)
    assert passage_law(cond).conditional_time[cond.initial]==F(9360,1351)
    # independently differentiate Chebyshev recurrence with rational arithmetic
    x=F(2); a,b=F(1),x; da,db=F(0),F(1)
    for _ in range(1,r): a,b,da,db=b,2*x*b-a,db,2*b+2*x*db-da
    assert x*db/b==F(9360,1351)
    REPORT['rare_path_explanation']={'R':6,'ever_risk':'1/1351',
       'outward_at_debt1':'7/8','outward_at_debt2':'13/14','conditional_arrows':'9360/1351'}


def test_10_generating_values_preserved():
    checks=0
    for r in range(1,6):
        p=killed();a,c=observed(p,r);q=compile_peak_quotient(c).chain
        for z in (F(0),F(1,3),F(2,3),F(1),F(3,2)):
            expected=first_hit_generating_value(p,a,z)
            assert passage_law(q,z=z).probability[q.initial]==expected
            assert passage_law(c,z=z).probability[c.initial]==expected
            checks+=2
    REPORT['pgf_exact_comparisons']=checks


def test_11_incomplete_model_preserves_both_absorptions():
    p=killed(); rows=[]
    for cap in (1,2,4,8,14):
        a,c=observed(p,4,cap);q=compile_peak_quotient(c)
        original=peak_probability(p,a)
        low=passage_law(q.chain).probability[q.chain.initial]
        unknown=passage_law(q.chain,target='UNKNOWN').probability[q.chain.initial]
        assert (low,low+unknown)==(original.lower,original.upper)
        for t in ('HIT','UNKNOWN'):assert passage_prefix(q.chain,20,target=t)==passage_prefix(c,20,target=t)
        if not a.complete:
            with pytest.raises(ValueError):condition_on_hit(c)
            with pytest.raises(ValueError):compile_first_passage_model(c)
        rows.append([cap,str(low),str(low+unknown)])
    REPORT['partial_budget_intervals']=rows


def test_12_noncommuting_original_matrix_oracle():
    s=matrix([[int(i==j)+(1 if j==i+1 else 0) for j in range(6)] for i in range(6)])
    base=(triple(((2,0),(0,1))),triple(((1,0),(0,2))),triple(((1,1),(0,1))))
    actions=[mm(mm(s,a),inv(s)) for a in base]
    p=ControlPacket.from_edges(2,0,1,[(0,0,F(1,4),act(a),1) for a in actions]+
                               [(0,1,F(1,4),act(I),1),(1,1,1,act(I),1)])
    a,c=observed(p,3);q=compile_peak_quotient(c);model=compile_first_passage_model(c)
    literal,checks=literal_first_hits(p,3,6)
    assert passage_prefix(q.chain,6)==literal
    assert tuple(model.coefficient(t) for t in range(7))==literal
    law=passage_law(q.chain)
    assert law.probability[q.chain.initial]==F(7309,56081)
    assert q.chain.colors.count('SAFE')==11 and model.rank==10
    REPORT['noncommuting']={'raw_safe':20,'quotient_safe':11,'observable_rank':10,
       'independent_smith_prefix_checks':checks,'ever_probability':'7309/56081',
       'note':'Here safe reduction merges only never-hit stopped states; it does not identify distinct active orientations.'}


def test_13_random_split_chains():
    rng=random.Random(202609206);comparisons=0
    for _ in range(30):
        # 3 safe blocks each split into 2 hidden states, with HIT and UNKNOWN.
        small=[]
        for i in range(3):
            values=[rng.randint(1,5) for _ in range(5)];tot=sum(values)
            small.append([F(v,tot) for v in values])
        small+= [[0,0,0,1,0],[0,0,0,0,1]]
        labels=(0,0,1,1,2,2,3,4);big=[[F(0)]*8 for _ in range(8)]
        for i in range(6):
            for g in range(3):
                split=F(rng.randint(1,4),5)
                big[i][2*g]=small[labels[i]][g]*split
                big[i][2*g+1]=small[labels[i]][g]*(1-split)
            big[i][6],big[i][7]=small[labels[i]][3:]
        big[6][6]=big[7][7]=1
        c=PeakChain(tuple(map(tuple,big)),('SAFE',)*6+('HIT','UNKNOWN'),complete=False)
        cert=compile_peak_quotient(c,initial_labels=labels)
        assert cert.labels==labels and verify_peak_quotient(c,cert)
        for initial in range(6):
            raw=replace(c,initial=initial)
            quo=replace(cert.chain,initial=labels[initial])
            for target in ('HIT','UNKNOWN'):
                assert passage_prefix(raw,20,target=target)==passage_prefix(quo,20,target=target)
                assert passage_law(raw,target=target).probability[initial]==passage_law(quo,target=target).probability[labels[initial]]
                comparisons+=22
    REPORT['random_split_chain_comparisons']=comparisons


def test_14_initial_hit_nohit_and_clock_types():
    p=killed();a,c=observed(p,0);q=compile_peak_quotient(c)
    assert passage_prefix(q.chain,5)==(1,0,0,0,0,0)
    assert compile_first_passage_model(c).coefficient(0)==1
    no=PeakChain(((F(1),),),('SAFE',))
    m=compile_first_passage_model(no)
    assert m.rank==0 and m.coefficient(100)==0
    with pytest.raises(ValueError):condition_on_hit(no)
    _,c=observed(p,2); q=compile_peak_quotient(replace(c,duration=7))
    assert q.chain.duration==7
    assert passage_law(q.chain).conditional_time[q.chain.initial]*q.chain.duration==16


def test_15_tampered_certificate_rejected():
    _,c=observed(killed(),3);q=compile_peak_quotient(c)
    with pytest.raises(ValueError):verify_peak_quotient(c,replace(q,source_digest='0'*64))
    with pytest.raises(ValueError):verify_peak_quotient(c,replace(q,labels=(0,)*len(c.colors)))
    with pytest.raises(ValueError):verify_peak_quotient(c,replace(q,chain=replace(q.chain,duration=2)))
    with pytest.raises(ValueError):compile_peak_quotient(c,mode='forget_everything')
    with pytest.raises(ValueError):compile_peak_quotient(c,initial_labels=(0,))
    with pytest.raises(ValueError):compile_peak_quotient(replace(c,channels=()),mode='atoms')


@pytest.mark.parametrize('bad',[-1,True,0.5])
def test_16_invalid_time_and_inexact_inputs(bad):
    c=PeakChain(((F(1),),),('SAFE',))
    with pytest.raises((ValueError,TypeError)):passage_prefix(c,bad)
    with pytest.raises((ValueError,TypeError)):compile_first_passage_model(c).coefficient(bad)


def test_17_prefix_plateau_is_not_closure():
    # A long deterministic delay is silent before its first HIT. A few zero
    # observations prove nothing; exact invariant span reaches full rank.
    n=9;rows=[[F(0)]*n for _ in range(n)]
    for i in range(n-1):rows[i][i+1]=1
    rows[-1][-1]=1
    c=PeakChain(tuple(map(tuple,rows)),('SAFE',)*8+('HIT',))
    model=compile_first_passage_model(c)
    assert model.rank==8
    assert all(model.coefficient(t)==0 for t in range(8))
    assert model.coefficient(8)==1
    REPORT['silent_prefix_counterexample']={'zero_prefix_steps':7,'exact_rank':8,'first_hit_time':8}


def test_18_literal_conditioned_path_weights():
    # Direct enumeration in the observation chain, independent of matrix star.
    _,c=observed(killed(),3);cond,keep=condition_on_hit(c)
    index={j:i for i,j in enumerate(keep)}; h=passage_law(c).probability[c.initial]
    todo=[(c.initial,F(1),F(1))]; comparisons=0
    for depth in range(1,7):
        nxt=[]
        for i,raw,changed in todo:
            for j,w in enumerate(c.kernel[i]):
                if not w or j not in index:continue
                nr=raw*w; nc=changed*cond.kernel[index[i]][index[j]]
                if c.colors[j]=='HIT':
                    assert nc==nr/h;comparisons+=1
                elif c.colors[j]=='SAFE':nxt.append((j,nr,nc))
        todo=nxt
    assert comparisons>0
    REPORT['conditioned_literal_path_equalities']=comparisons


def test_19_risk_timing_parameter_sweep():
    from enterprise_math.heartbeat_peak_quotient import killed_debt_risk_timing
    rows=[]
    for c in (F(1,4),F(1,2),F(3,4),F(1)):
        for r in range(1,7):
            _,chain=observed(killed(c),r)
            actual=passage_law(chain); expected=killed_debt_risk_timing(c,r)
            assert actual.probability[chain.initial]==expected['risk']
            assert actual.conditional_time[chain.initial]==expected['conditional_steps']
            if c==1:assert expected['conditional_steps']==r*r
            rows.append((str(c),r,str(expected['risk']),str(expected['conditional_steps'])))
    assert killed_debt_risk_timing(0,1)['conditional_steps'] is None
    assert killed_debt_risk_timing(0,0)['conditional_steps']==0
    REPORT['risk_timing_parameter_sweep']=rows


def test_99_write_results():
    data={'status':'PASS_IF_FULL_SUITE_EXIT_ZERO','scope':'Exact local research; no full-repo, independent review, or production claim',
          'checks':REPORT}
    (OUT/'RESULTS.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
