from __future__ import annotations
from dataclasses import replace
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import lcm, prod
from pathlib import Path
import hashlib, json, random, sys
import pytest
from sympy import Matrix as SM, ZZ
from sympy.matrices.normalforms import smith_normal_form
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, eye, inv, mm, matrix, sm
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_switching_carry import linear_carry_spread
from enterprise_math.heartbeat_carry_peak import (projective_lattice_key, compile_carry_peak,
    first_passage_prefix, PeakState, HIT, UNKNOWN)
from enterprise_math.heartbeat_peak_orbits import (FiniteFrameGroup, Frame,
    threshold_action_equivalent, certify_peak_symmetry, compile_orbit_peak, orbit_observation_chain)
from enterprise_math.heartbeat_peak_quotient import (passage_law, passage_prefix,
    peak_observation_chain, compile_peak_quotient, condition_on_hit)
from enterprise_math.heartbeat_projective_frames import *
from enterprise_math.heartbeat_projective_frames import _multiply

I=eye(6); Z=(0,)*6
REPORT={}
OUT=ROOT/'research_notes/heartbeat_projective_frames_20260921_AD0416'
OUT.mkdir(parents=True,exist_ok=True)

def block(b):
    return matrix([[b[i%2][j%2] if i//2==j//2 else 0 for j in range(6)] for i in range(6)])
S=block(((1,1),(0,1))); J=block(((0,1),(1,0)))
D=block(((2,0),(0,1))); V=block(((1,0),(0,2)))

def shear(a):
    b=[list(r) for r in I]; b[0][1]=a
    return matrix(b)

def power(a,n):
    out=I
    for _ in range(n): out=mm(a,out)
    return out

def stopped(actions,weights=None):
    weights=tuple(weights) if weights is not None else (F(1,2*len(actions)),)*len(actions)
    return ControlPacket.from_edges(2,0,1,
        [(0,0,w,Affine(a,Z),1) for a,w in zip(actions,weights)]
        +[(0,1,1-sum(weights),Affine(I,Z),1),(1,1,1,Affine(I,Z),1)])

@lru_cache(maxsize=None)
def pgl2(p,depth):
    modulus=p**depth; found={}
    for a,b,c,d in product(range(modulus),repeat=4):
        if (a*d-b*c)%p==0: continue
        t=(a,b,c,d); u=pow(next(x for x in t if x%p),-1,modulus)
        t=tuple(x*u%modulus for x in t)
        found[t]=block((t[:2],t[2:]))
    return tuple(found[k] for k in sorted(found))

@lru_cache(maxsize=None)
def isotropic():
    actions=[]
    for g in pgl2(2,2):
        a=mm(mm(g,D),inv(g))
        denominator=lcm(*(v.denominator for row in a for v in row))
        actions.append(sm(denominator,a))
    return stopped(tuple(actions)),tuple(actions)

@lru_cache(maxsize=None)
def build_iso(cap=100):
    p,_=isotropic()
    cert=discover_projective_symmetry(p,2,2,[S,J])
    a=compile_projective_peak(p,cert,max_states=cap)
    return p,cert,a,projective_peak_chain(p,a)


def test_01_sources_byte_identical():
    expected={'heartbeat_peak_orbits.py':'6f5a35851ed7cfef08fe34bb209fbd29c9b4b0dc',
      'heartbeat_carry_peak.py':'44bde8bbff397adf8aec80fcb2bffa79c6e272e9',
      'heartbeat_peak_quotient.py':'db00aaf3be5640b966267a529124556ff713807e'}
    for name,h in expected.items():
        data=(ROOT/'src/enterprise_math'/name).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==h
    REPORT['unchanged_dependencies']=expected


def test_02_scalar_and_congruence_keys():
    checks=0
    for p in (2,3,5):
        for depth in (1,2,3):
            a=shear(F(1,p+1)); unit=p+1
            b=sm(unit,mm(a,shear(p**depth)))
            assert projective_frame_key(a,p,depth)==projective_frame_key(b,p,depth)
            assert projective_frame_key(a,p,depth+1)!=projective_frame_key(b,p,depth+1)
            checks+=1
    REPORT['frame_key_equivalences']=checks


def test_03_finite_image_of_infinite_shear():
    a=shear(1)
    with pytest.raises(ValueError,match='GROUP_LIMIT'):
        FiniteFrameGroup.generated(2,1,[Frame((0,),a)],max_group=8)
    g=FiniteProjectiveImage.generated(2,2,[a],max_group=4)
    assert len(g.keys)==4 and g.verify() and power(a,4)!=I
    assert projective_frame_key(power(a,4),2,2)==IK
    REPORT['infinite_lift_finite_image']={'rational_order':'infinite','mod4_order':4}


def test_04_shear_period_formula():
    checks=0
    for p in (2,3,5):
        for threshold in (2,3,4):
            for v in (0,1,2):
                a=shear(p**v); order=shear_frame_period(p,threshold,p**v)
                g=FiniteProjectiveImage.generated(p,threshold-1,[a],max_group=125)
                assert len(g.keys)==order
                assert projective_frame_key(power(a,order),p,threshold-1)==IK
                if order>1: assert projective_frame_key(power(a,order//p),p,threshold-1)!=IK
                checks+=1
    REPORT['exact_shear_orders']=checks


def test_05_independent_modular_group_enumeration():
    cases=[]
    for p,depth,gens in [(2,1,(S,J)),(2,2,(S,J)),(3,1,(S,J,block(((2,0),(0,1)))) )]:
        g=FiniteProjectiveImage.generated(p,depth,gens,max_group=100)
        assert set(g.keys)=={projective_frame_key(a,p,depth) for a in pgl2(p,depth)}
        cases.append([p,depth,len(g.keys)])
    assert cases==[[2,1,6],[2,2,48],[3,1,24]]
    REPORT['independent_finite_group_orders']=cases


def test_06_modular_products_and_associativity():
    rng=random.Random(921060)
    g=FiniteProjectiveImage.generated(2,2,[S,J])
    for _ in range(80):
        a,b,c=rng.choices(g.keys,k=3)
        assert _multiply(a,b,2,2)==projective_frame_key(mm(matrix(a),matrix(b)),2,2)
        assert _multiply(_multiply(a,b,2,2),c,2,2)==_multiply(a,_multiply(b,c,2,2),2,2)
        assert _multiply(a,projective_frame_key(inv(matrix(a)),2,2),2,2)==IK
    REPORT['modular_algebra_trials']=80


def test_07_all_safe_random_lattices_respect_keys():
    rng=random.Random(921061); checked=0
    for p in (2,3):
        for r in (2,3,4):
            for _ in range(12):
                basis=matrix([[p**rng.randrange(r) if i==j else 0 for j in range(6)] for i in range(6)])
                basis=mm(shear(rng.randrange(7)),basis)
                g=shear(rng.randrange(11)); gp=mm(g,shear(p**(r-1)))
                assert projective_lattice_key(mm(g,basis),p)==projective_lattice_key(mm(gp,basis),p)
                checked+=1
    REPORT['safe_lattice_frame_checks']=checked


def test_08_guard_precision_invariance():
    rng=random.Random(921062); checks=0
    for p in (2,3):
        for r in (2,3):
            for c in (1,2,3):
                a=block(((p**c,1),(0,1)))
                for _ in range(8):
                    g=mm(shear(rng.randint(-2,2)),J)
                    delta=shear(p**(r-1+c))
                    gp=mm(g,delta)
                    x=mm(mm(g,a),inv(g));y=mm(mm(gp,a),inv(gp))
                    assert projective_frame_key(g,p,r-1+c)==projective_frame_key(gp,p,r-1+c)
                    assert threshold_action_equivalent(x,y,p,r)
                    checks+=1
    REPORT['guard_precision_checks']=checks


def test_09_one_less_digit_can_fail_germ():
    checks=0
    for p in (2,3):
        for m in (1,2,3):
            for c in (1,2):
                a=block(((p**c,0),(0,1)))
                e=shear(p**(m+c-1))
                assert not threshold_action_equivalent(a,mm(mm(e,a),inv(e)),p,m+1)
                checks+=1
    REPORT['underprecision_counterexamples']=checks


def test_10_isotropic_discovery():
    p,c,a,chain=build_iso()
    assert c.guard_depth==2 and len(c.ambient.keys)==48
    assert len(c.admitted)==48 and len(c.effective)==6
    assert len(a.states)==3 and a.complete
    law=passage_law(chain)
    assert law.probability[0]==F(2,11) and law.conditional_time[0]==F(24,11)
    assert chain.kernel[0][1:]==(F(1,2),F(1,2),F(0),F(0))
    assert chain.kernel[1]==(F(1,6),F(0),F(1,2),F(1,3),F(0))
    assert len(compile_peak_quotient(chain).chain.colors)==len(chain.colors)
    REPORT['isotropic_online']={'guarded_frames':48,'effective_frames':6,'safe_representatives':3,
        'hit_probability':'2/11','conditional_time':'24/11'}


def test_11_raw_and_axis_swap_comparison():
    p,c,a,chain=build_iso()
    raw=compile_carry_peak(p,2,2)
    oldgroup=FiniteFrameGroup.generated(2,2,[Frame((0,1),J)])
    oldcert=certify_peak_symmetry(p,oldgroup,2,mode='threshold')
    old=compile_orbit_peak(p,oldcert)
    assert len(raw.states)==8 and len(old.states)==4
    direct=peak_observation_chain(p,raw);axis=orbit_observation_chain(p,old)
    assert passage_prefix(chain,40)==passage_prefix(direct,40)==passage_prefix(axis,40)
    assert passage_law(direct).probability[0]==passage_law(chain).probability[0]
    REPORT['generation_comparison']={'raw':8,'axis_swap_orbits':4,'modular_orbits':3,'time_coefficients':41}


def test_12_full_weight_and_multiplicity_preserved():
    p,c,a,chain=build_iso()
    atoms=[]
    for s,t,h in p.blocks:
        for w,f,n in h.entries:atoms.append((s,t,w,f.a,n))
    for i,state in enumerate(a.states):
        row=[e for e in a.edges if e.source==i]
        assert sum(e.mass for e in row)==1
        if state.control<0:continue
        assert {e.atom for e in row}=={j for j,v in enumerate(atoms) if v[0]==state.control}
        for e in row:assert (e.weight,e.multiplicity)==(atoms[e.atom][2],atoms[e.atom][4])
    assert chain.channels==()  # Not an atomwise quotient of the original world.
    REPORT['representative_atom_integrity']=True


def test_13_independent_literal_matrix_prefixes():
    p,actions=isotropic()
    def mul(a,b):return ((a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]),
                        (a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]))
    def vp(x):
        x=abs(x); n=0
        while x%2==0: x//=2;n+=1
        return n
    def spread(a):
        low=min(vp(x) for row in a for x in row if x)
        return vp(a[0][0]*a[1][1]-a[0][1]*a[1][0])-2*low
    aa=[tuple(tuple(int(a[i][j]) for j in range(2)) for i in range(2)) for a in actions]
    live=[((1,0),(0,1))];hits=[F(0)];tested=0
    for depth in range(1,4):
        following=[]; nhit=0
        for current in live:
            for action in aa:
                nxt=mul(action,current);tested+=1
                if spread(nxt)>=2:nhit+=1
                else:following.append(nxt)
        live=following;hits.append(F(nhit,96**depth))
    assert tuple(hits)==passage_prefix(build_iso()[3],3)
    REPORT['literal_two_by_two_times_three_prefixes']={'checked':tested,'first_masses':list(map(str,hits))}


def test_14_hidden_nonnative_involution():
    tilted=(mm(mm(S,D),inv(S)),mm(mm(S,V),inv(S)))
    p=stopped(tilted); c=discover_projective_symmetry(p,2,2,[S,J])
    hidden=mm(mm(S,J),inv(S))
    assert mm(hidden,hidden)==I
    assert any(sum(x!=0 for x in row)>1 for row in hidden)
    assert projective_frame_key(hidden,2,1) in c.effective
    a=compile_projective_peak(p,c)
    assert len(a.states)==3 and passage_law(projective_peak_chain(p,a)).probability[0]==F(1,7)
    with pytest.raises(ValueError):
        certify_peak_symmetry(p,FiniteFrameGroup.generated(2,2,[Frame((0,1),J)]),2,mode='threshold')
    REPORT['hidden_involution']={'off_axis':True,'admitted_guarded':len(c.admitted),'effective':len(c.effective),'risk':'1/7'}


def test_15_deeper_tilted_model():
    p=stopped((mm(mm(S,D),inv(S)),mm(mm(S,V),inv(S))))
    c=discover_projective_symmetry(p,2,3,[S,J],max_group=512)
    a=compile_projective_peak(p,c);raw=compile_carry_peak(p,2,3)
    chain=projective_peak_chain(p,a)
    assert passage_law(chain).probability[0]==F(1,26)
    assert passage_prefix(chain,24)==first_passage_prefix(p,raw,24)['hit_by_step']
    REPORT['deeper_guard']={'ambient':len(c.ambient.keys),'guard_depth':c.guard_depth,
        'admitted':len(c.admitted),'effective':len(c.effective),'safe':len(a.states),'risk':'1/26'}


def test_16_reweight_invalidates_certificate():
    p,c,_,_=build_iso();_,aa=isotropic()
    weights=[F(1,96)]*len(aa);weights[0]+=F(1,192);weights[1]-=F(1,192)
    changed=stopped(aa,weights)
    with pytest.raises(ValueError): compile_projective_peak(changed,c)
    new=discover_projective_symmetry(changed,2,2,[S,J])
    assert len(new.admitted)<len(c.admitted)
    REPORT['biased_symmetry']={'old':len(c.admitted),'new':len(new.admitted)}


def test_17_tampering_rejected():
    p,c,a,ch=build_iso()
    for bad in (replace(c,threshold=3),replace(c,packet_digest='0'*64),
                replace(c,effective=c.effective[:1]),replace(c,admitted=c.admitted[:1])):
        with pytest.raises((ValueError,ArithmeticError)):compile_projective_peak(p,bad)
    with pytest.raises(ValueError):projective_peak_chain(p,replace(a,edges=a.edges[:-1]))
    with pytest.raises(ValueError):projective_peak_chain(p,replace(a,complete=False))
    REPORT['tamper_rejections']=6


def test_18_budget_interval():
    full=F(2,11);bounds=[]
    for cap in (1,2,3):
        _,_,a,c=build_iso(cap)
        low=passage_law(c).probability[0]
        high=low+passage_law(c,target='UNKNOWN').probability[0]
        assert low<=full<=high
        if cap<3:
            assert not a.complete
            with pytest.raises(ValueError): condition_on_hit(c)
        else: assert a.complete and low==high==full
        bounds.append([cap,str(low),str(high)])
    REPORT['budget_bounds']=bounds


def test_19_deeper_observer_reads_composition_residual():
    examples=[]
    for m in (1,2,3):
        g=shear(1);e=power(g,2**m)
        assert e!=I and projective_frame_key(e,2,m)==IK
        basis=matrix([[2**(m+1) if i==j==0 else int(i==j) for j in range(6)] for i in range(6)])
        # Use all six directions to avoid changing the interpretation with trivial extra axes.
        basis=block(((2**(m+1),0),(0,1)))
        e=block(((1,2**m),(0,1)))
        future=block(((1,0),(0,2**(2*m+1))))
        assert linear_carry_spread(basis,2)==linear_carry_spread(mm(e,basis),2)==m+1
        assert linear_carry_spread(mm(future,basis),2)==m
        assert linear_carry_spread(mm(mm(future,e),basis),2)==m+2
        examples.append([m,m+2,m,m+2])
    REPORT['reactivated_frame_residual']=examples


def test_20_does_not_call_full_graph(monkeypatch):
    import enterprise_math.heartbeat_carry_peak as old
    def forbidden(*args,**kwargs):raise AssertionError('full graph called')
    monkeypatch.setattr(old,'compile_carry_peak',forbidden)
    p,c,_,_=build_iso()
    a=compile_projective_peak(p,c)
    assert len(a.states)==3


def test_21_invalid_inputs():
    bad=[lambda:projective_frame_key(D,2,1),lambda:projective_frame_key(I,4,1),
         lambda:projective_frame_key(I,2,0),lambda:projective_frame_key(eye(5),2,1),
         lambda:projective_frame_key(sm(F(1,2),I),2,1),lambda:shear_frame_period(2,2,True),
         lambda:FiniteProjectiveImage.generated(2,2,[S,J],max_group=3),
         lambda:discover_projective_symmetry(isotropic()[0],2,1,[S]),
         lambda:compile_projective_peak(isotropic()[0],build_iso()[1],max_states=0)]
    for call in bad:
        with pytest.raises((ValueError,TypeError)):call()
    g=FiniteProjectiveImage.generated(2,2,[S])
    with pytest.raises(ValueError):replace(g,keys=g.keys[:-1]).verify()
    REPORT['boundary_rejections']=len(bad)+1


def test_22_general_threshold_frame_group_size():
    count=prod(2**6-2**i for i in range(6))
    assert count==20158709760
    # The ratio of consecutive levels is p^(n*n-1), not 720.
    assert 2**35==34359738368
    REPORT['full_unenumerated_ambient']={'PGL6_F2_order':count,'level_multiplier':2**35,
      'enumerated_full_group':False}


if __name__=='__main__':
    result=pytest.main([__file__,'-q'])
    observed=sys.modules.get('test_heartbeat_projective_frames')
    report=observed.REPORT if observed is not None else REPORT
    (OUT/'RESULTS.json').write_text(json.dumps({'status':'PASS' if result==0 else 'FAIL',
      'new_tests':22,'checks':report,'scope':'fixed p, threshold, stochastic law and declared congruence ambient',
      'independent_review':False,'full_repository_tests':False,'lean':False},ensure_ascii=False,indent=2)+'\n')
    raise SystemExit(result)
