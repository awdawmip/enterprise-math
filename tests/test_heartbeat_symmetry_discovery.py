from __future__ import annotations
from dataclasses import replace
from fractions import Fraction as F
from math import prod
from pathlib import Path
from hashlib import sha1
import json, random, sys
import pytest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, matrix, eye, mm, sm
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_carry_peak import compile_carry_peak, projective_lattice_key
from enterprise_math.heartbeat_peak_quotient import passage_law, passage_prefix, peak_observation_chain
from enterprise_math.heartbeat_peak_orbits import (threshold_action_equivalent, certify_peak_symmetry,
    compile_orbit_peak, verify_orbit_peak)
from enterprise_math.heartbeat_symmetry_discovery import *
from enterprise_math.heartbeat_symmetry_discovery import _canonical, _certificate, _closure
from enterprise_math.heartbeat_switching_carry import linear_carry_spread
I=eye(6); ZERO=(0,)*6; REPORT={}
OUT=ROOT/'research_notes/heartbeat_symmetry_discovery_20260921_AD0416'
OUT.mkdir(parents=True,exist_ok=True)
def diag(v):return matrix([[v[i] if i==j else 0 for j in range(6)]for i in range(6)])
U,V=diag((2,2,2,1,1,1)),diag((1,1,1,2,2,2))
def stopped(u=U,v=V,a=F(1,4),b=F(1,4)):
 return ControlPacket.from_edges(2,0,1,[(0,0,a,Affine(u,ZERO),1),(0,0,b,Affine(v,ZERO),1),
     (0,1,1-a-b,Affine(I,ZERO),1),(1,1,1,Affine(I,ZERO),1)])
def six(c=F(1,2),p=2):
 edges=[(0,0,c/6,Affine(diag(tuple(p if i==k else 1 for i in range(6))),ZERO),1)for k in range(6)]
 if c<1:edges.append((0,1,1-c,Affine(I,ZERO),1))
 return ControlPacket.from_edges(2,0,1,edges+[(1,1,1,Affine(I,ZERO),1)])
def shear(m):
 E=[list(row)for row in I];E[0][3]=2**m
 return stopped(v=mm(V,matrix(E)))
def solve(P,r,cap=1000,**kwargs):
 d=discover_axis_symmetries(P,2,r,**kwargs);a=compile_discovered_peak(P,d,max_states=cap)
 return d,a,discovered_observation_chain(P,d,a)

def test_01_source_identity():
 expected={'heartbeat_carry_peak.py':'44bde8bbff397adf8aec80fcb2bffa79c6e272e9',
 'heartbeat_peak_quotient.py':'db00aaf3be5640b966267a529124556ff713807e',
 'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
 'brc_weighted_recurrent.py':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb'}
 for name,digest in expected.items():
  b=(ROOT/'src/enterprise_math'/name).read_bytes()
  assert sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==digest
 REPORT['unchanged_verified_modules']=expected

def test_02_eight_probes_safe():
 checks=0
 for p in (2,3,5):
  for r in range(1,6):
   probes=safe_lattice_probes(p,r);assert len(probes)==(1 if r==1 else 8)
   for x in probes:assert linear_carry_spread(x,p)<r;checks+=1
 REPORT['safe_probe_checks']=checks

def test_03_key_scalar_congruence():
 rng=random.Random(2026092101);checks=0
 for p in (2,3,5):
  for r in (1,2,3,4):
   for _ in range(8):
    A=[list(row)for row in diag(tuple(p**rng.randrange(3)for _ in range(6)))]
    A[0][2]+=rng.randrange(-3,4);A[1][4]+=rng.randrange(-3,4);A=matrix(A)
    E=[list(row)for row in I];E[1][5]=p**(r-1)*rng.choice((-2,-1,1,2))
    B=sm(F(-7,11),mm(A,matrix(E)))
    assert action_germ_key(A,p,r)==action_germ_key(B,p,r)
    assert threshold_action_equivalent(A,B,p,r);checks+=1
 REPORT['scalar_congruence_key_equalities']=checks

def test_04_legacy_crosscheck():
 rng=random.Random(2026092102);checks=0
 for p in (2,3,5):
  for r in (1,2,3,4):
   for _ in range(8):
    a=diag(tuple(rng.randrange(1,7)for _ in range(6)));b=[list(row)for row in a]
    b[rng.randrange(3)][rng.randrange(3,6)]+=rng.randrange(-4,5);b=matrix(b)
    assert (action_germ_key(a,p,r)==action_germ_key(b,p,r))==threshold_action_equivalent(a,b,p,r)
    checks+=1
 REPORT['legacy_criterion_comparisons']=checks

def test_05_actual_separating_probes():
 checks=witnesses=0
 for p in (2,3,5):
  for r in range(1,5):
   for v in (0,1,2):
    e=[list(row)for row in I];e[0][4]=p**v;A=mm(U,matrix(e))
    w=separate_safe_actions(A,U,p,r)
    if w is not None:
     assert w.left_output!=w.right_output and linear_carry_spread(w.input_basis,p)<r
     assert projective_lattice_key(mm(A,w.input_basis),p)==w.left_output;witnesses+=1
    else:assert action_germ_key(A,p,r)==action_germ_key(U,p,r)
    checks+=1
 w=separate_safe_actions(diag((1,3,1,1,1,1)),I,2,3)
 assert w is not None and w.probe_index==7
 assert separate_safe_actions(sm(F(3,7),U),U,2,5) is None
 REPORT['separation']={'pair_cases':checks,'real_witnesses':witnesses+1,'last_probe':7}

def test_06_symmetric_biased():
 a=discover_axis_symmetries(stopped(),2,2)
 b=discover_axis_symmetries(stopped(a=F(3,8),b=F(1,8)),2,2)
 assert a.complete and b.complete and len(a.accepted)==72 and len(b.accepted)==36
 assert set(b.accepted)<=set(a.accepted) and _closure(a.generators)==frozenset(a.accepted)
 assert a.group.verify()
 REPORT['weight_dependence']={'candidates':720,'symmetric':72,'biased':36}

def test_07_atomwise_stronger():
 a=discover_axis_symmetries(stopped(),2,2,atomwise=True)
 b=discover_axis_symmetries(six(),2,2,atomwise=True)
 assert len(a.accepted)==36 and len(b.accepted)==1
 REPORT['atomwise']={'UV':36,'six_distinct_actions':1}

def test_08_full_shear_filtration():
 rows=[]
 for m in (1,3):
  p=discover_axis_profile(shear(m),2);summary=[(r,len(g))for r,g in p.changes]
  assert summary==[(1,72),(m+2,4)] and p.exact_group_order==4
  rows.append({'m':m,'changes':summary,'pair_checks':p.matrix_pairs_checked})
 REPORT['automatic_filtration']=rows

def test_09_legacy_compiler_agrees():
 P=stopped();d=discover_axis_symmetries(P,2,3)
 old=certify_peak_symmetry(P,d.group,3,mode='threshold');assert old==_certificate(P,d)
 a=compile_discovered_peak(P,d);b=compile_orbit_peak(P,old)
 assert a.states==b.states and a.edges==b.edges and a.complete==b.complete
 assert verify_orbit_peak(P,a)
 REPORT['legacy_unchanged_execution']={'certificate_equal':True,'states':len(a.states)}

def test_10_full_six_axes_to_risk(monkeypatch):
 P=six();import enterprise_math.heartbeat_carry_peak as old
 original=old.compile_carry_peak
 def forbidden(*a,**k):raise AssertionError('discovery or online compilation called raw graph')
 monkeypatch.setattr(old,'compile_carry_peak',forbidden)
 d,a,ch=solve(P,2,cap=7)
 assert len(d.accepted)==720 and len(a.states)==7 and a.complete
 assert passage_law(ch).probability[0]==F(2089,20731)
 raw=original(P,2,2,max_states=126);assert raw.complete and len(raw.states)==126
 full=peak_observation_chain(P,raw);assert passage_prefix(ch,50)==passage_prefix(full,50)
 assert passage_law(ch).probability[0]==passage_law(full).probability[0]
 lookup={s:i for i,s in enumerate(a.states)}
 labels=[lookup[_canonical(s.control,s.lattice,a.certificate,d.generators)[0]]for s in raw.states]
 for i,row in enumerate(full.kernel[:len(raw.states)]):
  sums=[F(0)]*(len(a.states)+2)
  for j,w in enumerate(row):
   target=labels[j]if j<len(raw.states)else len(a.states)+j-len(raw.states);sums[target]+=w
  assert tuple(sums)==ch.kernel[labels[i]]
 REPORT['six_axis']={'raw_safe':126,'online_safe':7,'group':720,'generators':len(d.generators),
 'atom_successors':a.atom_successors,'canonical_steps':a.canonical_candidates,'raw_rows':126,
 'prefix_equalities':51,'risk':str(passage_law(ch).probability[0]),
 'conditional_time':str(passage_law(ch).conditional_time[0])}

def test_11_renewal_independent_oracle():
 rows=[]
 for c in (F(1,4),F(1,2),F(3,4),F(1)):
  P=six(c);d,a,ch=solve(P,2,cap=7)
  g=lambda k:F(prod(range(7-k,7)),6**k)
  reset=c**6*g(6);b={k+1:c**(k+1)*g(k)*F(k,6)for k in range(1,6)}
  exact=sum(b.values())/(1-reset);pmf=[F(0)]*61
  for t in range(1,61):pmf[t]=b.get(t,F(0))+(reset*pmf[t-6]if t>=6 else 0)
  prefix=passage_prefix(ch,60)
  assert tuple(prefix)==tuple(pmf)  # inherited API already returns first-hit masses, not a CDF
  law=passage_law(ch);assert law.probability[0]==exact
  mean=sum(k*w for k,w in b.items())/sum(b.values())+6*reset/(1-reset)
  assert law.conditional_time[0]==mean
  rows.append({'c':str(c),'reset':str(reset),'risk':str(exact),'conditional_time':str(mean)})
 REPORT['renewal']=rows;REPORT['renewal_pmf_equalities']=240

def test_12_shear_event_preserved():
 P=shear(1);d,a,ch=solve(P,3);raw=compile_carry_peak(P,2,3)
 assert len(d.accepted)==4 and passage_law(ch).probability[0]==F(247,6242)
 assert passage_prefix(ch,24)==passage_prefix(peak_observation_chain(P,raw),24)
 REPORT['residual_retained']={'group':4,'states':len(a.states),'risk':'247/6242','prefix_equalities':25}

def test_13_budget_not_completeness():
 d=discover_axis_symmetries(stopped(),2,2,max_candidates=1)
 assert not d.complete and d.status=='CANDIDATE_LIMIT' and len(d.accepted)==1
 assert verify_symmetry_discovery(stopped(),d)
 a=compile_discovered_peak(stopped(),d);ch=discovered_observation_chain(stopped(),d,a)
 assert passage_law(ch).probability[0]==F(1,7) and len(a.states)==4
 REPORT['candidate_budget']={'searched':1,'group':1,'safe':4,'risk':'1/7','complete':False}

def test_14_unknown_mass():
 P=six();d=discover_axis_symmetries(P,2,2);rows=[]
 for budget in (1,2,4,7):
  a=compile_discovered_peak(P,d,max_states=budget);ch=discovered_observation_chain(P,d,a)
  low=passage_law(ch).probability[0];high=low+passage_law(ch,target='UNKNOWN').probability[0]
  assert low<=F(2089,20731)<=high
  if budget==7:assert low==high==F(2089,20731)
  rows.append([budget,str(low),str(high)])
 REPORT['unknown_bounds']=rows

def test_15_forged_stale_rejected():
 P=stopped();d=discover_axis_symmetries(P,2,2)
 with pytest.raises(ValueError):verify_symmetry_discovery(stopped(a=F(3,8),b=F(1,8)),d)
 with pytest.raises(ValueError):verify_symmetry_discovery(P,replace(d,packet_digest='0'*64))
 with pytest.raises(ValueError):verify_symmetry_discovery(P,replace(d,complete=False))
 with pytest.raises(ValueError):replace(d.group,frames=d.group.frames[:-1]).verify()
 a=compile_discovered_peak(P,d)
 with pytest.raises(ValueError):discovered_observation_chain(P,d,replace(a,complete=not a.complete))
 REPORT['forgery_rejections']=5

def test_16_original_multiplicity():
 P=ControlPacket.from_edges(2,0,1,[(0,0,F(1,8),Affine(U,ZERO),2),(0,0,F(1,4),Affine(V,ZERO),1),
   (0,1,F(1,2),Affine(I,ZERO),1),(1,1,1,Affine(I,ZERO),1)])
 d,a,ch=solve(P,3);assert len(d.accepted)==72 and passage_law(ch).probability[0]==F(1,26)
 source={(w,n)for _s,_t,h in P.blocks for w,_a,n in h.entries}
 assert all((e.weight,e.multiplicity)in source or e.atom==-1 for e in a.edges)
 assert all(sum(row)==1 for row in ch.kernel)
 REPORT['original_weight_count_preserved']=True

def test_17_control_and_frame_scope():
 d=discover_axis_symmetries(stopped(),2,2);assert all(g.controls==(0,1)for g in d.group.frames)
 with pytest.raises(ValueError):AxisPermutationGroup(2,2,(Frame((1,0),I),)).verify()
 with pytest.raises(ValueError):AxisPermutationGroup(2,2,(Frame((0,1),sm(-1,I)),)).verify()
 REPORT['scope']=['controls fixed','positive axis permutations only','no arbitrary GL search']

def test_18_invalid():
 cases=[lambda:action_germ_key(I,4,2),lambda:action_germ_key(I,2,0),lambda:action_germ_key(eye(7),2,2),
 lambda:action_germ_key(sm(0,I),2,2),lambda:discover_axis_symmetries(stopped(),2,2,max_candidates=0),
 lambda:discover_axis_symmetries(stopped(),2,2,atomwise=1),lambda:safe_lattice_probes(2,True),
 lambda:action_germ_key(I,2,2,mode='approximate')]
 for call in cases:
  with pytest.raises((ValueError,TypeError)):call()
 REPORT['invalid_rejections']=len(cases)

if __name__=='__main__':
 result=pytest.main([__file__,'-q'])
 observed=sys.modules.get('test_heartbeat_symmetry_discovery');report=observed.REPORT if observed else REPORT
 if result==0 and len(report)<18:raise RuntimeError('incomplete report')
 data={'status':'PASS'if result==0 else 'FAIL','new_tests':18,'checks':report,
  'scope':'Exact fixed-law germ contract within S6, not arbitrary minimal state realization',
  'full_project_tests':False,'independent_review':False,'lean':False}
 (OUT/'RESULTS.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 raise SystemExit(result)
