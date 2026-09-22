from fractions import Fraction as F
from itertools import product,permutations
from pathlib import Path
from dataclasses import replace
import sys,random,hashlib,json
import pytest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import matrix,mm,inv,eye,Affine,sm
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_congruence_lift import verify_lifted_peak_frame
from enterprise_math.heartbeat_mass_refinement import *
from enterprise_math.heartbeat_peak_orbits import Frame,FiniteFrameGroup,certify_peak_symmetry,compile_orbit_peak,orbit_observation_chain
from enterprise_math.heartbeat_carry_peak import compile_carry_peak
from enterprise_math.heartbeat_peak_quotient import peak_observation_chain,passage_law,passage_prefix
from enterprise_math.heartbeat_switching_carry import linear_carry_spread
REPORT={}
D=matrix(((2,0),(0,1)));V=matrix(((1,0),(0,2)));J=matrix(((0,1),(1,0)));I=eye(2)
def block(a):return matrix([[a[i%len(a)][j%len(a)] if i//len(a)==j//len(a) else 0 for j in range(6)] for i in range(6)])
def packet(terms):
 return ControlPacket.from_edges(2,0,1,[(0,0,w,Affine(block(a),(0,)*6),k) for a,w,k in terms]+[(0,1,F(1,2),Affine(eye(6),(0,)*6),1),(1,1,1,Affine(eye(6),(0,)*6),1)])
def stopped_kernel(terms,p=2):
 return MassKernel.build([KernelTerm(0,0,w,a,k) for a,w,k in terms]+[KernelTerm(0,1,F(1,2),I),KernelTerm(1,1,1,I)],p,controls=2)
def example(a=1):
 E=matrix(((1,2**a),(0,1)))
 return [(D,F(1,4),1),(V,F(1,8),1),(mm(V,E),F(1,8),1)]
def raw_frames(seed,kernel):
 n=kernel.dimension;p=kernel.prime;level=p**(seed.precision+kernel.guard)
 for digit in product(range(p),repeat=n*n-1):
  xs=list(digit);xs.insert(seed.pivot,0)
  yield matrix([[seed.frame[i][j]+level*xs[n*i+j] for j in range(n)] for i in range(n)])
def literal_valid(kernel,frame,m):
 # Independent whole-row checker from the inherited peak module, via real X6 packet.
 terms=[(t.source,t.target,t.weight,Affine(block(t.action),(0,)*6),t.multiplicity) for t in kernel.terms]
 pk=ControlPacket.from_edges(kernel.controls,0,1,terms)
 try:verify_lifted_peak_frame(pk,block(frame),kernel.prime,m+1);return True
 except ValueError:return False

def test_01_frozen_sources():
 expected={'heartbeat_congruence_lift.py':'3909cc89b97b5e3a14fb0f1f18d85d19b7a390f9','heartbeat_peak_orbits.py':'6f5a35851ed7cfef08fe34bb209fbd29c9b4b0dc','heartbeat_carry_peak.py':'44bde8bbff397adf8aec80fcb2bffa79c6e272e9'}
 for name,digest in expected.items():
  raw=(ROOT/'src/enterprise_math'/name).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==digest
 REPORT['unchanged_inherited_sources']=len(expected)

def test_02_mass_classes_not_atoms():
 k=stopped_kernel([(D,F(1,4),1),(V,F(1,8),1),(sm(3,V),F(1,8),1)])
 assert len(k.terms)==5 and len(k.classes(1))==3
 assert k.classes(1)[1].members==(1,2)
 assert literal_valid(k,J,4)
 # No individual atom of mass1/4 with action V exists to match D's mass1/4.
 assert not any(t.mass==F(1,4) and t.action in (V,sm(3,V)) for t in k.terms)
 REPORT['aggregate_not_atom_bijection']={'atoms':5,'classes':3,'unequal_atom_masses':'1/4 versus 1/8+1/8'}

def test_03_successful_aggregate_lift():
 k=stopped_kernel([(D,F(1,4),1),(V,F(1,8),1),(sm(3,V),F(1,8),1)])
 r=lift_mass_seed(k,k.seed(J,1));assert r.verify() and r.count==2
 assert all(literal_valid(k,s.frame,2) for s in r.all_seeds())
 REPORT['aggregate_lifts']=r.count

def test_04_split_mass_obstruction():
 k=stopped_kernel(example());r=lift_mass_seed(k,k.seed(J,1))
 assert r.status=='MASS_SPLIT_OBSTRUCTION' and r.count==0 and r.verify()
 assert r.obstruction.source_children!=r.obstruction.target_children
 assert not any(literal_valid(k,f,2) for f in raw_frames(r.seed,k))
 REPORT['split_obstruction']={'coarse_classes':len(k.classes(1)),'fine_classes':len(k.classes(2)),'systems_solved':r.processed_matchings,'raw_next_frames_checked':8}

def test_05_geometric_obstruction():
 a=matrix(((1,0),(0,3)));k=MassKernel.build([KernelTerm(0,0,1,a)],2)
 r=lift_mass_seed(k,k.seed(J,3));assert r.status=='GEOMETRIC_OBSTRUCTION' and r.verify() and r.count==0
 assert r.rejected[0].certificate.space.obstruction is not None
 REPORT['geometric_obstruction_after_profiles_match']=True

def test_06_joint_not_separate():
 a=matrix(((1,1),(0,1)));b=matrix(((3,1),(0,1)))
 for x in (a,b):
  k=MassKernel.build([KernelTerm(0,0,1,x)],2);assert lift_mass_seed(k,k.seed(a,1)).count==4
 k=MassKernel.build([KernelTerm(0,0,F(1,3),a),KernelTerm(0,0,F(2,3),b)],2)
 r=lift_mass_seed(k,k.seed(a,1));assert r.count==0 and r.status=='GEOMETRIC_OBSTRUCTION' and r.verify()
 REPORT['joint_obstruction']={'separate_lifts':[4,4],'joint_lifts':0}

def test_07_changing_matching_adds_dimension():
 e=matrix(((1,2),(0,1)))
 k=MassKernel.build([KernelTerm(0,0,F(1,4),D),KernelTerm(0,0,F(1,4),mm(D,e)),KernelTerm(0,0,F(1,2),I)],2)
 r=lift_mass_seed(k,k.seed(I,1));joint=compress_mass_lifts(r)
 assert len(r.components)==2 and [c.count for c in r.components]==[4,4]
 assert joint.count==8 and len(joint.basis)==3 and joint.verify()
 expected={s.frame for s in r.all_seeds()}
 assert {joint.instantiate(c).frame for c in product(range(2),repeat=3)}==expected
 REPORT['matching_freedom']={'components':2,'per_component':4,'joint_free_bits':3,'total_lifts':8}

def test_08_random_independent_complete_lifts():
 rng=random.Random(927221);cases=0;frames=0
 for p in (2,3):
  for _ in range(10):
   actions=[]
   for _j in range(2):
    while True:
     a=matrix([[rng.randint(-2,3) for _j in range(2)] for _i in range(2)])
     try:inv(a);break
     except (ValueError,ZeroDivisionError):pass
    actions.append(a)
   k=MassKernel.build([KernelTerm(0,0,F(1,2),a) for a in actions],p)
   seed=k.seed(I,1);r=lift_mass_seed(k,seed);assert r.complete and r.verify()
   expected=set()
   for f in raw_frames(seed,k):
    frames+=1
    if literal_valid(k,f,2):expected.add(k.seed(f,2).frame)
   assert {s.frame for s in r.all_seeds()}==expected
   joint=compress_mass_lifts(r);assert joint.count==len(expected);cases+=1
 REPORT['independent_fiber_checks']={'kernels':cases,'full_frame_candidates':frames}

def test_09_large_six_axis_symbolic_family():
 k=MassKernel.from_packet(packet([(D,F(1,4),1),(V,F(1,4),1)]),2)
 r=lift_mass_seed(k,k.seed(eye(6),1));j=compress_mass_lifts(r)
 assert r.count==2**17 and len(j.basis)==17 and j.verify()
 rng=random.Random(50012)
 for _ in range(12):
  seed=j.instantiate(tuple(rng.randrange(2) for _ in j.basis))
  assert literal_valid(k,seed.frame,2)
 with pytest.raises(ValueError,match='LIFT_LIMIT'):r.all_seeds(limit=100)
 REPORT['full_six_axis_symbolic']={'free_bits':17,'lifts':2**17,'literal_samples':12,'all_lifts_enumerated':False}

def test_10_scalar_kernel_unbounded_free_dimension():
 k=MassKernel.build([KernelTerm(0,0,1,eye(6))],2)
 r=lift_mass_seed(k,k.seed(eye(6),1));j=compress_mass_lifts(r)
 assert len(j.basis)==35 and j.count==2**35
 REPORT['scalar_kernel_free_bits']=35

def test_11_matching_budget_not_no_lifts():
 e=matrix(((1,2),(0,1)))
 k=MassKernel.build([KernelTerm(0,0,F(1,4),D),KernelTerm(0,0,F(1,4),mm(D,e)),KernelTerm(0,0,F(1,2),I)],2)
 r=lift_mass_seed(k,k.seed(I,1),max_matchings=1)
 assert r.status=='MATCHING_LIMIT' and r.count is None and r.known_count==4 and r.verify()
 with pytest.raises(ValueError):r.all_seeds()
 with pytest.raises(ValueError):compress_mass_lifts(r)
 REPORT['matching_budget']={'status':r.status,'known_lifts':4,'total_lifts':None}

def test_12_family_budget_and_refinement():
 k=stopped_kernel([(D,F(1,4),1),(V,F(1,8),1),(sm(3,V),F(1,8),1)])
 seed=k.seed(J,1)
 out=lift_mass_family(k,[seed],3,max_seeds=100)
 assert out['status']=='COMPLETE' and len(out['seeds'])==4
 tiny=lift_mass_family(k,[seed],3,max_seeds=1)
 assert tiny['status']=='LIFT_LIMIT' and tiny['frontier'][0].count==2
 broken=stopped_kernel(example())
 assert lift_mass_family(broken,[broken.seed(J,1)],3)['status']=='NO_LIFTS'
 REPORT['multilevel']={'complete_final_frames':4,'tiny_limit_retains_affine_frontier':True}

def test_13_finite_collision_horizon():
 for a in range(1,7):
  k=stopped_kernel(example(a));h=collision_horizon(k)
  assert h['separation_precision']==a+1
  assert len(k.classes(a))==3 and len(k.classes(a+1))==4
  assert k.classes(a+1)==k.classes(a+3)
 k=MassKernel.build([KernelTerm(0,0,F(1,2),D),KernelTerm(0,0,F(1,2),sm(5,D))],2)
 assert collision_horizon(k)['separation_precision']==1 and len(k.classes(100))==1
 REPORT['finite_collision_horizon_cases']=7

def test_14_defect_refinement_monotonicity():
 k=stopped_kernel(example());d=[mass_germ_defect(k,J,m) for m in range(1,6)]
 assert d==[(F(0),F(0))]+[(F(1,4),F(0))]*4
 assert all(d[i][0]<=d[i+1][0] for i in range(4))
 REPORT['row_mass_defect_by_precision']=[[str(x) for x in row] for row in d]

def test_15_control_profiles_not_global_total():
 k=MassKernel.build([KernelTerm(0,0,1,D),KernelTerm(1,1,1,V)],2,controls=2)
 with pytest.raises(ValueError,match='mass-germ law'):k.seed(J,1)
 assert sorted(sum(c.mass_profile) for c in k.classes(1))==[1,1]
 REPORT['control_labels_preserved']=True

def test_16_risk_appears_after_class_split():
 pk=packet(example());base=packet([(D,F(1,4),1),(V,F(1,4),1)])
 records={}
 for r in (2,3):
  ch=peak_observation_chain(pk,compile_carry_peak(pk,2,r));bc=peak_observation_chain(base,compile_carry_peak(base,2,r))
  v=passage_law(ch).probability[ch.initial];b=passage_law(bc).probability[bc.initial]
  if r==2:assert v==b==F(1,7) and passage_prefix(ch,12)==passage_prefix(bc,12)
  else:
   assert v==F(457,11702) and b==F(1,26)
   assert passage_prefix(ch,5)[5]==F(13,2048) and passage_prefix(bc,5)[5]==F(12,2048)
  records[str(r)]={'refined':str(v),'base':str(b),'chain_states_including_hit_unknown':len(ch.colors)}
 REPORT['risk_comparison']=records

def test_17_literal_word_oracle():
 pk=packet(example());ch=peak_observation_chain(pk,compile_carry_peak(pk,2,3))
 actions=example();hits=[F(0)]*7;front={I:F(1)};checks=0
 def two_kappa(a):
  def vp(v):
   n=abs(int(v));out=0
   if not n:return 10**8
   while n%2==0:n//=2;out+=1
   return out
  return vp(a[0][0]*a[1][1]-a[0][1]*a[1][0])-2*min(vp(x) for row in a for x in row)
 for t in range(1,7):
  nxt={}
  for a,mass in front.items():
   for b,w,k in actions:
    c=mm(b,a);checks+=1
    if two_kappa(c)>=3:hits[t]+=mass*w*k
    else:nxt[c]=nxt.get(c,F(0))+mass*w*k
  front=nxt
 assert tuple(hits)==passage_prefix(ch,6)
 REPORT['independent_aggregated_raw_matrix_prefix_checks']=checks

def test_18_BRC_orbit_with_nonbijective_atoms():
 pk=packet([(D,F(1,4),1),(V,F(1,16),2),(sm(3,V),F(1,8),1)])
 k=MassKernel.from_packet(pk,2);r=lift_mass_seed(k,k.seed(block(J),1))
 assert r.count>0
 j=compress_mass_lifts(r);s=j.instantiate((0,)*len(j.basis))
 assert verify_lifted_peak_frame(pk,matrix(s.frame),2,3)
 group=FiniteFrameGroup.generated(2,2,[Frame((0,1),block(J))])
 cert=certify_peak_symmetry(pk,group,3,mode='threshold')
 raw=compile_carry_peak(pk,2,3);orb=compile_orbit_peak(pk,cert)
 rc=peak_observation_chain(pk,raw);oc=orbit_observation_chain(pk,orb)
 assert passage_prefix(rc,18)==passage_prefix(oc,18)
 assert passage_law(oc).probability[oc.initial]==F(1,26)
 REPORT['BRC_aggregate_orbit']={'raw_states':len(raw.states),'orbit_states':len(orb.states),'risk':'1/26','original_multiplicity_two_retained':True}

def test_19_tampered_certificates():
 k=stopped_kernel([(D,F(1,4),1),(V,F(1,4),1)]);r=lift_mass_seed(k,k.seed(J,1))
 with pytest.raises(ValueError):replace(r,processed_matchings=9).verify()
 with pytest.raises(ValueError):compress_mass_lifts(replace(r,processed_matchings=9))
 j=compress_mass_lifts(r)
 with pytest.raises(ValueError):replace(j,basis=()).verify()
 with pytest.raises(ValueError):lift_mass_seed(k,replace(r.seed,kernel_digest='wrong'))

def test_20_invalid_input_contracts():
 bad=[lambda:MassKernel.build([KernelTerm(0,0,.5,I)],2),lambda:MassKernel.build([KernelTerm(0,0,F(1,2),I)],2),lambda:MassKernel.build([KernelTerm(0,0,1,((1,0),(0,0)))],2),lambda:MassKernel.build([KernelTerm(0,0,1,I)],4),lambda:MassKernel.build([KernelTerm(0,0,1,I,0)],2)]
 for f in bad:
  with pytest.raises((ValueError,ZeroDivisionError)):f()
 k=MassKernel.build([KernelTerm(0,0,1,I)],2)
 for f in [lambda:k.seed(I,0),lambda:k.seed(((F(1,2),0),(0,1)),1),lambda:lift_mass_seed(k,k.seed(I,1),max_matchings=0),lambda:mass_germ_defect(k,I,0)]:
  with pytest.raises(ValueError):f()
 REPORT['invalid_input_rejections']=9



def test_21_nonidentity_seed_complete_fibers():
 rng=random.Random(55172);cases=0;frames=0
 for p in (2,3):
  for m in (1,2,3):
   t=matrix(((1,rng.randint(-3,3)),(0,1)));s=mm(mm(t,J),inv(t))
   b=mm(mm(s,D),inv(s))
   k=MassKernel.build([KernelTerm(0,0,F(1,2),D),KernelTerm(0,0,F(1,2),b)],p)
   seed=k.seed(s,m);r=lift_mass_seed(k,seed);j=compress_mass_lifts(r)
   expected=set()
   for frame in raw_frames(seed,k):
    frames+=1
    if literal_valid(k,frame,m+1):expected.add(k.seed(frame,m+1).frame)
   assert expected=={q.frame for q in r.all_seeds()}
   assert j.count==len(expected);cases+=1
 REPORT['nonidentity_fibers']={'cases':cases,'literal_candidates':frames}


if __name__=='__main__':
 result=pytest.main([__file__,'-q'])
 imported=next(m for name,m in sys.modules.items() if name.endswith('test_heartbeat_mass_refinement') and hasattr(m,'REPORT'))
 target=ROOT/'research_notes/heartbeat_mass_refinement_20260922_AD0416/RESULTS.json';target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps({'status':'PASS' if result==0 else 'FAIL','new_tests':21,'checks':imported.REPORT},ensure_ascii=False,indent=2)+'\n')
 raise SystemExit(result)
