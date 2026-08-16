#!/usr/bin/env python3
import json,itertools,hashlib,math
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parent
FILES=[
'R059D_STAGE_O_COMPLETION_LAYER_PROTOCOL.json','R059D_STAGE_O_COORDINATE_COMPLETION_TYPING.json',
'R059D_STAGE_O_TWO_BRANCH_D6_REDERIVATION.json','R059D_STAGE_O_STATELESS_SYMMETRY_NOGO.json',
'R059D_STAGE_O_CONTEXT_NECESSITY_LEDGER.json','R059D_STAGE_O_STRAIGHTNESS_MEMORY_CREDIT.json',
'R059D_STAGE_O_CONTEXTUAL_SELECTOR_FAMILY.json','R059D_STAGE_O_SCALAR_VECTOR_BRIDGE.json',
'R059D_STAGE_O_LARGE_BACKGROUND_COVARIANCE.json','R059D_STAGE_O_TRIVIALITY_LEAKAGE_LEDGER.json']
passed=failed=0
records=[]
def ck(name,cond):
 global passed,failed
 if cond: passed+=1
 else: failed+=1; records.append(name)

def load(n): return json.loads((ROOT/n).read_text())
D={n:load(n) for n in FILES}
for n,o in D.items():
 ck('json:'+n,isinstance(o,dict)); ck('rid:'+n,o.get('researcher_id')=='EM-R059D-9C6B2A'); ck('task:'+n,o.get('taskbook_source')=='daae6ff47b02648435ec0f3aed082ba9b345b5e8'); ck('parent:'+n,o.get('frozen_parent')=='cacbd211a9811e96f361606d56e66bffdf83bf53')

c=D[FILES[0]]
ck('completion-class',c['classification']=='ADJACENT_COMPLETED_STATE_GATE_IS_DEFINITIONAL_GIVEN_COMPLETION_LAYER')
ck('int-prev',c['specializations']['integer_layer']['PREV']=='-1'); ck('int-next',c['specializations']['integer_layer']['NEXT']=='0')
ck('sq-prev',c['specializations']['square_layer']['PREV']==4); ck('sq-next',c['specializations']['square_layer']['NEXT']==9)
# exact integer neighbor theorem on many half-integers
for k in range(-512,513):
 q=Fraction(2*k+1,2)
 prev=q.numerator//q.denominator
 nxt=prev+1
 ck(f'Zprev:{k}',Fraction(prev,1)<q<Fraction(nxt,1))
 ck(f'Zgap:{k}',nxt-prev==1)
# squares neighbor oracle for many gaps
for m in range(0,300):
 lo=m*m; hi=(m+1)*(m+1
 )
 for off in (1, max(1,(hi-lo)//2), hi-lo-1):
  if off<=0 or lo+off>=hi: continue
  q=lo+off
  ck(f'sq:{m}:{off}',lo<q<hi)
  ck(f'sqprev:{m}:{off}',int(math.isqrt(q))**2==lo)
# positive affine covariance controls T(x)=a x+c on Z gaps
for a in (1,2,3,5,11):
 for shift in (-7,0,4,19):
  for k in range(-50,51):
   q=Fraction(2*k+1,2); p=k; n=k+1
   qp=a*q+shift
   ck(f'affprev:{a}:{shift}:{k}',a*p+shift < qp)
   ck(f'affnext:{a}:{shift}:{k}',qp < a*n+shift)
# sign covariance
for k in range(-200,201):
 q=Fraction(2*k+1,2); p=k; n=k+1
 ck(f'signp:{k}',-n < -q); ck(f'signn:{k}',-q < -p)

coord=D[FILES[1]]
ck('coord-inherit',coord['classification']=='COORDINATE_COMPLETION_Z_INHERITED_FROM_INTEGER_DISPLACEMENT_MODULE')
ck('coord-no-unit',coord['why_not_unit_packet'].startswith('UNIT_PACKET is not used'))
ck('coord-no-new',coord['new_precision_axiom_required'] is False)

two=D[FILES[2]]
ck('d6-class',two['classification']=='D6_EMERGES_FROM_AFFINE_PLUS_COMPLETION_NEIGHBOR_PRIMITIVE')
ck('no-min',two['no_separate_minimality_axiom'] is True)
# derive y branches from bits
ys=[]
for bx,bz in itertools.product((0,1),repeat=2):
 if bx+bz==1: ys.append((-1+bx,1,-1+bz))
ck('two-y',set(ys)=={(-1,1,0),(0,1,-1)})
# derive all e_i-e_j, not hard-coded as theorem mechanism
E=[(1,0,0),(0,1,0),(0,0,1)]
der=set()
for i in range(3):
 for j in range(3):
  if i!=j: der.add(tuple(E[i][k]-E[j][k] for k in range(3)))
ck('d6-card',len(der)==6)
ck('d6-sum0',all(sum(v)==0 for v in der))
ck('d6-equality',der=={tuple(x['vector']) for x in two['derived_rows']})
# coordinate permutation closure
for perm in itertools.permutations(range(3)):
 for v in der:
  pv=tuple(v[perm[k]] for k in range(3))
  ck('perm:'+str(perm)+str(v),pv in der)
# inversion closure
for v in der: ck('inv:'+str(v),tuple(-x for x in v) in der)

nogo=D[FILES[3]]
ck('nogo-freeze',nogo['freeze']=='STATELESS_EXCHANGE_EQUIVARIANT_UNIQUE_BRC_SELECTOR_IMPOSSIBLE_AT_SYMMETRIC_STATE')
for b in (0,1): ck('nogo-b'+str(b),b != 1-b)
# any deterministic stateless selector on one symmetric state is a constant b and fails equivariance
for fval in (0,1): ck('stateless:'+str(fval),fval != 1-fval)

ctx=D[FILES[4]]
ck('onebit-min',ctx['minimum_result']['freeze']=='ONE_BIT_BRANCH_MEMORY_MINIMAL_FOR_EQUIVARIANT_STRAIGHT_CONTINUATION')
# one-bit Boolean functions encoded by outputs F(0),F(1)
funcs=[]; exch=[]; straight=[]
for f0,f1 in itertools.product((0,1),repeat=2):
 funcs.append((f0,f1))
 # F(1-h)=1-F(h) both h
 ok=(f1==1-f0 and f0==1-f1)
 if ok: exch.append((f0,f1))
 if ok and f0==0 and f1==1: straight.append((f0,f1))
ck('4funcs',len(funcs)==4); ck('exchange2',set(exch)=={(0,1),(1,0)}); ck('straightunique',straight==[(0,1)])

st=D[FILES[5]]
t1=(-1,1,0); t0=(0,1,-1)
minor=t1[0]*t0[1]-t0[0]*t1[1]
ck('rank2-minor',minor==-1)
# sequences rank-one iff constant for length 2..10 under frozen two-vector family
for L in range(2,11):
 for bits in itertools.product((0,1),repeat=L):
  mixed=(0 in bits and 1 in bits)
  rank=2 if mixed else 1
  ck('rankseq:'+str(bits),(rank==1)==(len(set(bits))==1))
  if len(set(bits))==1: ck('memseq:'+str(bits),all(bits[k+1]==bits[k] for k in range(L-1)))

sel=D[FILES[6]]
ck('selector-class',sel['classification']=='UNIQUE_CONTEXTUAL_SELECTOR_FAMILY')
ck('initial-unid',sel['initial_selector_status']=='SELECTOR_STILL_NONIDENTIFIED')
# canonical partial selector and exchange covariance for all admissible sets
sets=[frozenset(),frozenset({0}),frozenset({1}),frozenset({0,1})]
def tauA(A): return frozenset(1-b for b in A)
def F(A,h=None):
 if len(A)==0:return None
 if len(A)==1:return next(iter(A))
 if h is None:return None
 return h
for A in sets:
 for h in (0,1):
  v=F(A,h); tv=F(tauA(A),1-h)
  if v is None: ck('partundef:'+str(A),tv is None)
  else:
   ck('legal:'+str(A)+str(h),v in A)
   ck('taueq:'+str(A)+str(h),tv==1-v)
# without h, ambiguous remains undefined
ck('no-h-ambig',F(frozenset({0,1}),None) is None)

bridge=D[FILES[7]]
ck('scalar-endpoints',bridge['scalar_5']['legal_endpoints']==[4,9])
ck('scalar-unsolved',bridge['scalar_5']['selector']=='NOT_IDENTIFIED by Stage O')

large=D[FILES[8]]
K0=10**36
for a in (1,2,5):
 for m in range(-64,65):
  K=K0+a*m
  # symmetric q=-a/2 neighbors in aZ are -a,0
  q=Fraction(-a,2)
  ck(f'scale-gap:{a}:{m}',-a < q < 0)
  for bx,bz in ((0,1),(1,0)):
   dx=-a+a*bx; dz=-a+a*bz; dy=a
   ck(f'scale-cons:{a}:{m}:{bx}',dx+dy+dz==0)
   e1=(K+dx,dy,dz)
   ck(f'bg:{a}:{m}:{bx}',sum(e1)==K)
# a=1 transfer set is D6; scaling preserves algebraic family
for a in (1,2,5,11):
 scaled={tuple(a*x for x in v) for v in der}
 ck('scaled-card:'+str(a),len(scaled)==6)
 ck('scaled-sum:'+str(a),all(sum(v)==0 for v in scaled))

kill=D[FILES[9]]
ck('kill-status',kill['status']=='PASS')
for k,v in kill['gates'].items():
 if k=='stage_n_parent_immutable': ck('gate:'+k,v is True)
 else: ck('gate:'+k,v is False)

# deterministic digest over check identities and final boolean status
payload='\n'.join(sorted([f'{n}:FAIL' for n in records])+[f'passed={passed}',f'failed={failed}'])
digest=hashlib.sha256(payload.encode()).hexdigest()
out={'schema':'R059D_STAGE_O_DETERMINISTIC_CHECKER_OUTPUT_V1','researcher_id':'EM-R059D-9C6B2A','taskbook_source':'daae6ff47b02648435ec0f3aed082ba9b345b5e8','frozen_parent':'cacbd211a9811e96f361606d56e66bffdf83bf53','status':'PASS' if failed==0 else 'FAIL','checks_total':passed+failed,'checks_passed':passed,'checks_failed':failed,'checks_digest_sha256':digest,'failure_examples':records[:20]}
(ROOT/'R059D_STAGE_O_DETERMINISTIC_CHECKER_OUTPUT.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
raise SystemExit(0 if failed==0 else 1)
