from __future__ import annotations
import hashlib,itertools,json,math,pathlib,random,sys
from collections import Counter
from fractions import Fraction as Q
ROOT=pathlib.Path(__file__).resolve().parents[1]
VENDOR=ROOT/'vendor'/'enterprise_math'
if not VENDOR.is_dir(): VENDOR=ROOT.parents[1]/'src'/'enterprise_math'
PRIOR=ROOT/'research'
if not (PRIOR/'heartbeat_algebra.py').exists(): PRIOR=ROOT.parent/'heartbeat_world_algebra_20260919_AD0416'/'research'
sys.path[:0]=[str(ROOT/'research'),str(PRIOR),str(VENDOR.parent)]
from brc_residue_transport import *
from heartbeat_residue_gates import *
from enterprise_math.brc_transport import matrix
from enterprise_math.predictive_quotient import predictive_block_profile
from phase_algebra import FrameProgram,analyze_fiber,synthesize_fiber
from heartbeat_algebra import beat
R=random.Random(20260920);checks={}
def record(name,data):checks[name]=data;print('PASS',name,flush=True)
def rv():return tuple(R.randrange(-20,21) for _ in range(6))
def blob(path):
 b=path.read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def measure(items):
 out={}
 for x,w in items:
  x=native(x);h=WeightHistogram.from_counts({Q(w):1})
  out[x]=histogram_recoalesce(out[x],h) if x in out else h
 return out
def stats(m):
 a=m.total().to_matrix();mass=a[6][6];mean=tuple(a[i][6]/mass for i in range(6))
 return mass,mean,tuple(tuple(a[i][j]/mass-mean[i]*mean[j] for j in range(6)) for i in range(6))
expected={VENDOR/'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',VENDOR/'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',VENDOR/'predictive_quotient.py':'f27d9ddf908f5b07051acfaf0c69f359d499b98b',PRIOR/'heartbeat_algebra.py':'c8d0b73a805740075e9b485d53e3b9ab71636490',PRIOR/'phase_algebra.py':'501e3d57021357630275762e989278a1ea29925d'}
for p,s in expected.items():assert blob(p)==s,(p,blob(p))
record('01_exact_source_reuse',{p.name:s for p,s in expected.items()})
count=0
for x in itertools.product((-2,-1,0,1,2),repeat=6):
 for i in range(6):
  y=gate(x,i);assert gate(y,i)==x
  assert sum(abs(a-b) for a,b in zip(x,y))==1
  want=list(x);want[i]+=1-2*((x[i]+x[(i+1)%6])%2)
  assert y==tuple(want);count+=1
for _ in range(800):
 x=rv();i=R.randrange(6);d=R.randrange(4);w=2**d
 q,digits=analyze_fiber(x,6*d);y=synthesize_fiber(gate(q,i),digits)
 assert y==gate(x,i,w) and tuple(a%w for a in y)==tuple(a%w for a in x)
 assert sum(abs(a-b) for a,b in zip(x,y))==w
record('02_local_gate_and_scale_lift',{'exhaustive_local_cases':count,'original_radix_lift_cases':800})
parities=tuple(itertools.product((0,1),repeat=6));velocities=Counter()
for r in parities:
 v=velocity(r);velocities[v]+=1
 for k in (1,2,5,20):
  assert walk(r,FORWARD*k)==tuple(a+k*b for a,b in zip(r,v))
  assert walk(r,REVERSE*k)==tuple(a-k*b for a,b in zip(r,v))
 assert walk(r,FORWARD+REVERSE)==r and math.prod(v)==-1
assert len(velocities)==32 and set(velocities.values())=={2}
for n in range(1,6):
 for subset in itertools.combinations(range(6),n):assert sum(math.prod(v[i] for i in subset)*w for v,w in velocities.items())==0
record('03_equal_cost_and_joint_six_axis_law',{'initial_parities':64,'channels':32,'fine_cost_per_12_ticks':12,'forward_twice':walk(ZERO,FORWARD*2),'return':walk(ZERO,FORWARD+REVERSE),'reverse_twice':walk(ZERO,REVERSE*2),'sixfold_velocity_product':-1,'all_nonempty_lower_order_sign_products_through_degree5':0})
for x in parities:
 for i in range(6):
  j=(i+1)%6;d=1-2*((x[i]+x[j])%2)
  assert walk(x,(i,j,i,j))==tuple(a+(2*d if k==i else 0) for k,a in enumerate(x))
  for j in range(6):
   if j not in (i,(i+1)%6,(i-1)%6):assert walk(x,(i,j))==walk(x,(j,i))
record('04_order_commutator',{'adjacent_cases':384,'nonadjacent_ordered_cases':1152,'G1G2':walk(ZERO,(0,1)),'G2G1':walk(ZERO,(1,0)),'four_gate_residual':walk(ZERO,(0,1,0,1))})
ctrl=ResidueControl();obs=lambda r:ctrl.observe(r)
actions={f'g{i}':(lambda r,i=i:tuple(a%2 for a in gate(r,i))) for i in range(6)}
prof=predictive_block_profile(parities,actions,obs,3);assert prof==(32,32,32,32)
actions['material_heartbeat']=lambda r:tuple(a%2 for a in beat(r))
wide=predictive_block_profile(parities,actions,obs,3);assert wide==(32,64,64,64)
assert ctrl.observe(ZERO)==ctrl.observe(ONE) and ctrl.observe(beat(ZERO))!=ctrl.observe(beat(ONE))
record('05_original_T6_minimum_and_boundary',{'gate_only':prof,'with_material_heartbeat':wide,'sector_moment_entries':896,'parity_sector_entries':1792,'scope':'future displacement control, not full position identity'})
for _ in range(12):
 axes=[R.randrange(6) for _ in range(3)];a,b,c=[gate_kernel(i,tick=t,fire=Q(1,2)) for t,i in enumerate(axes)]
 assert a.then(b).then(c)==a.then(b.then(c))
 q=gate_kernel((axes[1]+1)%6,tick=1,fire=Q(1,3))
 assert a.then(b.alternatives(q))==a.then(b).alternatives(a.then(q))
 assert GuardedKernel.identity(0,ctrl).then(a)==a and a.then(GuardedKernel.identity(1,ctrl))==a
 assert a.then(GuardedKernel.zero(1,1,ctrl))==GuardedKernel.zero(0,2,ctrl)
for _ in range(12):
 c=R.choice(ctrl.states);m=MomentState.from_point(rv())
 packet=next(p for r,d,p in gate_kernel(R.randrange(6),fire=Q(2,3)).blocks if r==c)
 assert packet_moment(packet,m).to_matrix()==packet.moment_action(m.to_matrix())
record('06_original_BRC_laws',{'kernel_triples':12,'original_moment_comparisons':12})
generated=0
for case in range(10):
 width=1 if case<6 else 2;control=ResidueControl(width=width)
 labels=[(rv(),Q(1,3)) for _ in range(3)];point=measure(labels);state=GuardedMoments.from_points(point,0,control)
 for t in range(7):
  i=R.randrange(6);fire=lambda c:Q(1,3) if c[(i+1)%6] else Q(2,3)
  k=gate_kernel(i,tick=t,control=control,fire=fire)
  expanded=[]
  for x,w in labels:
   p=fire(control.observe(x));expanded.extend(((gate(x,i,width),w*p),(x,w*(1-p))))
  labels=expanded;generated+=len(labels);brute=measure(labels)
  point=k.apply_points(point,t);assert point==brute
  state=state.then(k);assert state==GuardedMoments.from_points(brute,t+1,control)
record('07_independent_path_oracle',{'ensembles':10,'depth':7,'generated_labels':generated,'weights':'control-dependent 1/3 and 2/3'})
mu=measure([((-1,0,0,0,0,0),Q(1,2)),((1,0,0,0,0,0),Q(1,2))])
nu=measure([((-2,0,0,0,0,0),Q(1,8)),(ZERO,Q(3,4)),((2,0,0,0,0,0),Q(1,8))])
a=GuardedMoments.from_points(mu,0,ctrl);b=GuardedMoments.from_points(nu,0,ctrl);assert a.total()==b.total()
ma,mb=stats(a.then(gate_kernel(0)))[1],stats(b.then(gate_kernel(0)))[1];assert ma[0]==-1 and mb[0]==1
record('08_moment_failure_and_repair',{'same_input_global_moments':True,'output_means':[ma,mb]})
orders=tuple(itertools.permutations(range(6)));counts0=None
for c in ctrl.states:
 x=ctrl.representative(c);counts=Counter(tuple(b-a for a,b in zip(x,walk(x,w))) for w in orders)
 assert len(counts)==62 and sum(counts.values())==720
 assert all(sum(w*v[i] for v,w in counts.items())==0 for i in range(6))
 for i in range(6):
  for j in range(6):
   actual=Q(sum(w*v[i]*v[j] for v,w in counts.items()),720)
   want=Q(1) if i==j else -Q((1-2*c[i])*(1-2*c[j]),3) if (i-j)%6 in (1,5) else Q(0)
   assert actual==want,(c,i,j,actual,want)
 if c==ZERO:counts0=counts
k=shuffled_sweep();point=measure([(ZERO,Q(1))]);out=k.apply_points(point,0)
assert {p:h.entries for p,h in out.items()}=={v:((Q(1,720),n),) for v,n in counts0.items()}
out2=k.at(6).apply_points(out,6);count2=Counter()
for a,n in counts0.items():
 for b,m in counts0.items():count2[tuple(x+y for x,y in zip(a,b))]+=n*m
assert {p:h.entries for p,h in out2.items()}=={v:((Q(1,720**2),n),) for v,n in count2.items()}
record('09_shuffle_covariance',{'controls':32,'orders_per_control':720,'orders_examined':23040,'one_sweep_endpoints':62,'two_sweep_paths':720**2,'two_sweep_endpoints':len(count2),'diagonal_per_sweep':'1','adjacent_offdiagonal_zero_control':'-1/3'})
state=GuardedMoments.from_points(point,0,ctrl)
for s in range(60):state=state.then(k.at(6*s))
mass,mean,cov=stats(state);assert mass==1 and mean==tuple(Q(0) for _ in range(6))
assert cov==tuple(tuple(Q(60) if i==j else Q(-20) if (i-j)%6 in (1,5) else Q(0) for j in range(6)) for i in range(6))
record('10_long_exact_contraction',{'sweeps':60,'ticks_and_fine_steps_per_path':360,'represented_schedule_count':str(720**60),'not_enumerated':True,'active_sectors':len(state.blocks),'mass':mass,'mean':mean,'covariance':cov})
state=GuardedMoments.from_points(point,0,ctrl)
for t in range(96):state=state.then(gate_kernel(t%6,tick=t,fire=Q(1,2)))
assert stats(state)[0]==1 and len(state.blocks)==32
record('11_recurrent_guarded_moments',{'ticks':96,'branches_represented':str(2**96),'active_sectors':32,'independent_rationals':sum(len(m.upper) for _,m in state.blocks),'max_rational_bit_length':max(max(abs(q.numerator).bit_length(),q.denominator.bit_length()) for _,m in state.blocks for q in m.upper),'not_occupancy_or_full_provenance':True})
program=FrameProgram((0,1,2,3,4,5,6,5,4,3,2,1))
for _ in range(120):
 x=rv();t=R.randrange(36);i=R.randrange(6);y=program.at(t).encode(x)
 next_y=program.at(t+1).encode(gate(program.at(t).decode(y),i))
 assert program.at(t+1).decode(next_y)==gate(x,i)
record('12_original_frame_covariance',{'cases':120,'pure_frame_change_not_interaction':True})
rejected=0
def rejects(fn):
 global rejected
 try:fn()
 except (TypeError,ValueError):rejected+=1
 else:raise AssertionError('invalid input accepted')
for fn in [lambda:gate((0,)*5,0),lambda:gate((True,0,0,0,0,0),0),lambda:gate(ZERO,6),lambda:gate(ZERO,0,0),lambda:ResidueControl('unknown'),lambda:ctrl.validate((1,0,0,0,0,0)),lambda:gate_kernel(0,fire=0.5),lambda:gate_kernel(0,fire=Q(-1)),lambda:gate_kernel(0).then(gate_kernel(1,tick=2)),lambda:gate_kernel(0).alternatives(gate_kernel(1,tick=1))]:rejects(fn)
A=matrix([[2*int(i==0 and j==5)+int(i>0 and j==i-1) for j in range(6)] for i in range(6)])
rejects(lambda:ctrl.target(ZERO,Affine(A,ZERO)))
rejects(lambda:ctrl.target(ZERO,Affine(eye(6),(Q(1,2),0,0,0,0,0))))
rejects(lambda:ResidueControl(width=2).target(ZERO,Affine(eye(6),(1,0,0,0,0,0))))
rejects(lambda:GuardedMoments.from_points(point,0,ctrl).then(gate_kernel(0,tick=1)))
pc=ResidueControl('parity');hk=GuardedKernel.from_rows(0,1,pc,{r:[(1,Affine(A,ZERO),1)] for r in pc.states})
assert GuardedMoments.from_points(mu,0,pc).then(hk)==GuardedMoments.from_points(hk.apply_points(mu,0),1,pc)
record('13_typed_boundaries',{'invalid_rejections':rejected,'64_class_heartbeat_fallback':True})
# Actual material scale evolution, not a frame-only redraw.
for _ in range(600):
 x=rv();y=x
 for i in range(6):y=gate(beat(y),i)
 want=tuple(2*a-(2*(x[0]%2) if i==5 else 0) for i,a in enumerate(x))
 assert y==want
pc=ResidueControl('parity');initial=measure([(r,Q(1,64)) for r in parities])
state=GuardedMoments.from_points(initial,0,pc);points=initial
for i in range(6):
 step=active_heartbeat_gate(i,tick=i)
 state=state.then(step);points=step.apply_points(points,i)
 assert state==GuardedMoments.from_points(points,i+1,pc)
assert len(state.blocks)==1 and len(points)==64
mass,mean,cov=stats(state)
assert mean==(1,1,1,1,1,0) and cov[0][5]==-1 and cov[5][5]==2
record('14_active_material_heartbeat',{'signed_cases':600,'law':'X_6=2X_0-2*(X_0[0] mod2)*e6','distinct_material_states':64,'visible_parity_classes_after_sweep':1,'mean':mean,'covariance_first_last':cov[0][5],'last_variance':cov[5][5],'full_coordinate_information_not_erased':True})

result={'status':'PASS','check_groups':len(checks),'seed':20260920,'checks':checks,'scope':'chosen Heartbeat World dyadic gate model; finite-control affine BRC extension','independent_review':False,'full_project_tests':False,'production_changed':False}
(ROOT/'research'/'RESIDUE_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+'\n')
print('ALL',len(checks),'CHECK GROUPS PASS',flush=True)
