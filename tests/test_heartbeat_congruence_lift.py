from fractions import Fraction as F
from itertools import product
from math import lcm
from pathlib import Path
from dataclasses import replace
from functools import lru_cache
import hashlib,json,random,sys
import pytest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import matrix,mm,inv,eye,Affine
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_carry_peak import compile_carry_peak
from enterprise_math.heartbeat_peak_quotient import peak_observation_chain,passage_law,passage_prefix
from enterprise_math.heartbeat_switching_carry import linear_carry_spread
from enterprise_math.heartbeat_projective_frames import discover_projective_symmetry,compile_projective_peak,projective_peak_chain
from enterprise_math.heartbeat_congruence_lift import *
from enterprise_math.heartbeat_congruence_lift import _normalize_frame,_mod
REPORT={}
A=((1,0),(0,3));J=((0,1),(1,0));D=((2,0),(0,1));V=((1,0),(0,2));S=((1,1),(0,1))
def block(a):return matrix([[a[i%2][j%2] if i//2==j//2 else 0 for j in range(6)] for i in range(6)])
def stopped(actions):
 return ControlPacket.from_edges(2,0,1,[(0,0,F(1,2*len(actions)),Affine(a,(0,)*6),1) for a in actions]+[(0,1,F(1,2),Affine(eye(6),(0,)*6),1),(1,1,1,Affine(eye(6),(0,)*6),1)])
def check_equations(prob,frame,u,m):
 for a,b,v in zip(prob.sources,prob.targets,u):
  x=mm(mm(inv(b),matrix(frame)),a)
  try:
   if any(_mod(xx-v*ss,prob.prime**m) for row,srow in zip(x,frame) for xx,ss in zip(row,srow)):return False
  except ValueError:return False
 return True
@lru_cache(None)
def pgl2(p,depth):
 mod=p**depth;out=set()
 for a,b,c,d in product(range(mod),repeat=4):
  if (a*d-b*c)%p==0:continue
  f=(a,b,c,d);pivot=next(i for i,x in enumerate(f) if x%p);u=pow(f[pivot],-1,mod)
  f=tuple(x*u%mod for x in f);out.add((f[:2],f[2:]))
 return tuple(sorted(out))
@lru_cache(None)
def hidden(m):
 actions=tuple(mm(mm(matrix(S),matrix(a)),inv(matrix(S))) for a in (D,V))
 outputs=[];layers=[]
 for pi in ((0,1),(1,0)):
  prob=GermLiftProblem.build(actions,[actions[j] for j in pi],2);seeds=[]
  for f in pgl2(2,2):
   try:seeds.append(prob.seed(f,(1,1),1))
   except ValueError:pass
  out=lift_seed_family(prob,seeds,m,max_seeds=1024)
  assert out['status']=='COMPLETE'
  outputs.extend(out['seeds']);layers.extend(out['layers'])
 return actions,tuple(outputs),tuple(layers)

def test_01_sources():
 for file,sha in {'heartbeat_projective_frames.py':'78e1b765f2355156d9e529835ced7527bb5cd46e','heartbeat_peak_orbits.py':'6f5a35851ed7cfef08fe34bb209fbd29c9b4b0dc','heartbeat_carry_peak.py':'44bde8bbff397adf8aec80fcb2bffa79c6e272e9'}.items():
  raw=(ROOT/'src/enterprise_math'/file).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha
 REPORT['inherited_byte_identity_checks']=3

def test_02_solver_exhaustive():
 rng=random.Random(20260922);count=0
 for p in (2,3,5):
  for _ in range(25):
   a=tuple(tuple(rng.randrange(p) for j in range(3)) for i in range(4));b=tuple(rng.randrange(p) for i in range(4))
   sol=solve_modular_linear(a,b,p);assert sol.verify()
   expected={x for x in product(range(p),repeat=3) if all(sum(v*w for v,w in zip(row,x))%p==z for row,z in zip(a,b))}
   actual={sol.point(c) for c in product(range(p),repeat=len(sol.basis))} if sol.count else set()
   assert actual==expected;count+=1
 REPORT['linear_full_solution_comparisons']=count

def test_03_independent_lift_enumeration():
 rng=random.Random(928301);checked=0;candidates=0
 for p in (2,3):
  for _ in range(20):
   while True:
    a=matrix([[rng.randint(-3,4) for j in range(2)] for i in range(2)])
    try:inv(a);break
    except (ValueError,ZeroDivisionError):pass
   while True:
    f=matrix([[rng.randint(-4,5) for j in range(2)] for i in range(2)])
    try:_normalize_frame(f,p,2);break
    except (ValueError,ZeroDivisionError):pass
   b=mm(mm(f,a),inv(f));denom=lcm(*(v.denominator for row in b for v in row));b=matrix([[denom*x for x in row] for row in b])
   prob=GermLiftProblem.build([a],[b],p);s=prob.seed(f,[F(1,denom)],1);cert=lift_germ_seed(prob,s);assert cert.verify()
   expected=set()
   for z in product(range(p),repeat=5):
    if z[s.pivot]:continue
    f2=tuple(tuple(s.frame[i][j]+p**(1+prob.guard)*z[2*i+j] for j in range(2)) for i in range(2));u=(s.multipliers[0]+p*z[4],);candidates+=1
    if check_equations(prob,f2,u,2):expected.add((f2,u))
   actual={(x.frame,x.multipliers) for x in cert.all_lifts(limit=10000)}
   assert actual==expected;checked+=1
 REPORT['independent_lifts']={'seeds':checked,'literal_candidates':candidates}

def test_04_nonzero_repair():
 a=((1,1),(0,3));p=GermLiftProblem.build([a],[a],2);c=lift_germ_seed(p,p.seed(S,[1],1))
 assert any(c.space.rhs) and c.space.count==4 and p.seed(a,[1],2) in c.all_lifts()
 REPORT['repairable']={'nonzero_residual':True,'lifts':4,'repair':a}

def test_05_obstruction():
 p=GermLiftProblem.build([A],[A],2);c=lift_germ_seed(p,p.seed(J,[3],3))
 assert c.space.count==0 and c.verify()
 REPORT['obstruction']={'precision':3,'next_modulus':16,'rhs':c.space.rhs,'annihilator':c.space.obstruction}

def test_06_full6_no_lift():
 p=GermLiftProblem.build([block(A)],[block(A)],2)
 first=lift_germ_seed(p,p.seed(block(J),[1],1));last=lift_germ_seed(p,p.seed(block(J),[3],3))
 assert first.space.count==2**35 and last.space.count==0 and last.verify()
 with pytest.raises(ValueError,match='LIFT_LIMIT'):first.all_lifts(limit=100)
 REPORT['six_axis_exchange']={'first_lifts':2**35,'fourth_level_lifts':0}

def test_07_full6_affine_success():
 p=GermLiftProblem.build([block(D),block(V)],[block(D),block(V)],2);c=lift_germ_seed(p,p.seed(eye(6),[1,1],1))
 assert p.guard==1 and len(c.space.basis)==17 and c.space.count==131072 and c.verify()
 rng=random.Random(7621)
 for _ in range(20):
  s=c.instantiate(tuple(rng.randrange(2) for _ in c.space.basis));assert check_equations(p,s.frame,s.multipliers,2)
 REPORT['large_affine_family']={'variables':38,'equations':73,'rank':c.space.rank,'free_bits':17,'lifts':131072,'reconstructions':20}

def test_08_two_precision_clocks():
 p=GermLiftProblem.build([D,V],[D,V],2);s=p.seed(((1,0),(0,3)),[1,1],1)
 for new in lift_germ_seed(p,s).all_lifts():
  assert all((x-y)%4==0 for row,old in zip(new.frame,s.frame) for x,y in zip(row,old))
  assert all((x-y)%2==0 for x,y in zip(new.multipliers,s.multipliers))
  assert check_equations(p,new.frame,new.multipliers,2)

def test_09_hidden_lifts():
 actions,seeds,layers=hidden(6)
 assert len(seeds)==len({x.frame for x in seeds})==128 and sum(x[1] for x in layers)==124
 REPORT['hidden_normalizer']={'base_frames':48,'base_matching_tests':96,'final_frame_depth':7,'modulus':128,'retained_frames':128,'linear_systems':124,'unenumerated_ambient_order':6*8**6}

def test_10_full_small_ambient():
 actions,seeds,_=hidden(2);actual={x.frame for x in seeds};expected=set()
 problems=[GermLiftProblem.build(actions,[actions[j] for j in pi],2) for pi in ((0,1),(1,0))]
 for f in pgl2(2,3):
  for p in problems:
   for u in product((1,3),repeat=2):
    if check_equations(p,f,u,2):expected.add(f)
 assert actual==expected and len(actual)==8
 REPORT['full_ambient_crosscheck']={'frames':384,'accepted':8}

def test_11_BRC_replay():
 actions,seeds,_=hidden(2);packet=stopped(tuple(block(a) for a in actions));frames=tuple(block(s.frame) for s in seeds)
 for f in frames:assert verify_lifted_peak_frame(packet,f,2,3)
 cert=discover_projective_symmetry(packet,2,3,frames,max_group=8)
 compressed=projective_peak_chain(packet,compile_projective_peak(packet,cert))
 raw=peak_observation_chain(packet,compile_carry_peak(packet,2,3))
 assert passage_prefix(raw,25)==passage_prefix(compressed,25)
 a,b=passage_law(raw),passage_law(compressed)
 assert a.probability[raw.initial]==b.probability[compressed.initial]==F(1,26)
 assert a.conditional_time[raw.initial]==b.conditional_time[compressed.initial]==F(45,13)
 REPORT['BRC_replay']={'frames':8,'raw_safe_states':raw.colors.count('SAFE'),'compressed_safe_states':compressed.colors.count('SAFE'),'hit_probability':str(a.probability[raw.initial]),'conditional_time':str(a.conditional_time[raw.initial]),'coefficients':26}

def test_12_observable_failure():
 l=block(((16,1),(0,1)));a=block(A);b=block(((3,0),(0,1)));tail=block(((3,-1),(0,128)))
 assert linear_carry_spread(l,2)==4
 assert linear_carry_spread(mm(a,l),2)==linear_carry_spread(mm(b,l),2)==4
 assert linear_carry_spread(mm(tail,mm(a,l)),2)==3
 assert linear_carry_spread(mm(tail,mm(b,l)),2)==5
 packet=ControlPacket.from_edges(4,0,1,[(0,1,1,Affine(l,(0,)*6),1),(1,2,F(1,2),Affine(a,(0,)*6),1),(1,2,F(1,2),Affine(b,(0,)*6),1),(2,3,1,Affine(tail,(0,)*6),1),(3,3,1,Affine(eye(6),(0,)*6),1)])
 chain=peak_observation_chain(packet,compile_carry_peak(packet,2,5));law=passage_law(chain)
 REPORT['actual_peak_witness']={'before':4,'after_A':3,'after_exchanged_A':5,'law':repr(law),'prefix':repr(passage_prefix(chain,5))}
 assert law.probability[chain.initial]==F(1,2) and law.conditional_time[chain.initial]==3

def test_13_exchange_ceiling():
 count=0
 for p in (2,3,5):
  for a in range(1,5):
   d=1+p**a;v=0;t=d*d-1
   while t%p==0:t//=p;v+=1
   prob=GermLiftProblem.build([((1,0),(0,d))],[((1,0),(0,d))],p)
   for m in range(1,v+1):
    c=lift_germ_seed(prob,prob.seed(J,[d],m));assert (c.space.count==0)==(m==v);count+=1
 REPORT['exchange_cutoff_checks']=count

def test_14_budget():
 p=GermLiftProblem.build([A],[A],2);s=p.seed(J,[1],1)
 out=lift_seed_family(p,[s],3,max_seeds=2)
 assert out['status']=='LIFT_LIMIT' and out['frontier_certificates'][0].space.count==8
 assert lift_seed_family(p,[s],4,max_seeds=1000)['status']=='NO_LIFTS'

def test_15_matching_probabilities():
 from enterprise_math.heartbeat_carry_peak import _atoms
 packet=stopped((block(D),block(V)));atoms=_atoms(packet);pi=list(range(len(atoms)))
 i=next(i for i,x in enumerate(atoms) if x[0:2]==(0,0));j=next(i for i,x in enumerate(atoms) if x[0:2]==(0,1));pi[i],pi[j]=pi[j],pi[i]
 with pytest.raises(ValueError):packet_matching_problem(packet,2,pi)
 assert packet_matching_problem(packet,2,range(len(atoms))).dimension==6

def test_16_tamper():
 p=GermLiftProblem.build([A],[A],2);s=p.seed(J,[1],1);c=lift_germ_seed(p,s)
 with pytest.raises(ValueError):lift_germ_seed(p,replace(s,problem_digest='false'))
 with pytest.raises(ValueError):replace(c.space,rank=999).verify()
 c=lift_germ_seed(p,p.seed(J,[3],3)).space
 with pytest.raises(ValueError):replace(c,obstruction=(0,)*len(c.rhs)).verify()

def test_17_domains():
 calls=[lambda:GermLiftProblem.build([A],[A],4),lambda:GermLiftProblem.build([((0,0),(0,0))],[A],2),lambda:GermLiftProblem.build([A],[],2),lambda:GermLiftProblem.build([A],[A],2).seed(J,[2],1),lambda:GermLiftProblem.build([A],[A],2).seed(J,[1],0),lambda:GermLiftProblem.build([A],[A],2).seed(D,[1],1)]
 for f in calls:
  with pytest.raises((ValueError,TypeError,ZeroDivisionError)):f()

def test_18_empty_and_identity():
 p=GermLiftProblem.build([A],[A],2);assert lift_seed_family(p,[],2)['status']=='NO_LIFTS'
 s=p.seed(((1,0),(0,1)),[1],1);o=lift_seed_family(p,[s],1,max_seeds=1)
 assert o['status']=='COMPLETE' and o['seeds']==(s,)

def test_19_individually_repairable_jointly_obstructed():
 a=((1,1),(0,1));b=((3,1),(0,1));counts=[];last=None
 for actions in ((a,),(b,),(a,b)):
  problem=GermLiftProblem.build(actions,actions,2)
  last=lift_germ_seed(problem,problem.seed(a,[1]*len(actions),1))
  assert last.verify();counts.append(last.space.count)
 assert counts==[4,4,0]
 REPORT['joint_repair_obstruction']={'individual_lifts':counts[:2],'joint_lifts':0,'rhs':last.space.rhs,'annihilator':last.space.obstruction}

if __name__=='__main__':
 code=pytest.main([__file__,'-q']);report=sys.modules.get('test_heartbeat_congruence_lift').REPORT
 out=ROOT/'research_notes/heartbeat_congruence_lift_20260922_AD0416';out.mkdir(parents=True,exist_ok=True)
 (out/'RESULTS.json').write_text(json.dumps({'status':'PASS' if code==0 else 'FAIL','new_tests':19,'checks':report},indent=2)+'\n')
 raise SystemExit(code)
