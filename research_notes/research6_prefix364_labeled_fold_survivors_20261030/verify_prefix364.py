#!/usr/bin/env python3
"""PREFIX-364 exact rational four-label interval continuation.
Numerical scipy guesses only prepare rational candidate centers; this checker
can run without scipy/numpy and every asserted bound uses fractions.Fraction.
Static five-Port inverse auxiliary model, not native X6/BRC dynamics.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
T = lambda s:Q(str(s))
qa=list(map(Q,[34000,3200,58250,46600,31525]))
qb=list(map(Q,[204144,56336,1286,12936,28011]))
Z=Q(0)
# Linear coefficients L=c+a*x+i(d+b*x), H=|L|^2, exactly B above.
forms=[
 (Z,[Q(1),Z,Z,Z],Z,[Z,Q(1),Z,Z]),
 (Z,[Z,Z,Q(1),Z],Z,[Z,Z,Z,Q(1)]),
 (Q(5,2),[Q(3,2),Q(-7,2),Z,Q(-4)],Q(9,2),[Q(7,2),Q(3,2),Q(4),Z]),
 (Q(11,4),[Q(11,4),Q(-15,8),Q(5,4),Q(-9,4)],Q(15,8),[Q(15,8),Q(11,4),Q(9,4),Q(5,4)])
]
hess=[[[2*(a[j]*a[l]+b[j]*b[l]) for l in range(4)] for j in range(4)] for c,a,d,b in forms]
hess_norm=[[sum(abs(z) for z in H[j]) for j in range(4)] for H in hess]
def hgj(x):
 hs=[];gs=[]
 for c,a,d,b in forms:
  real=c+sum(a[j]*x[j] for j in range(4))
  imag=d+sum(b[j]*x[j] for j in range(4))
  hs.append(real**2+imag**2)
  gs.append([2*(real*a[j]+imag*b[j]) for j in range(4)])
 return hs,gs

def matdet(M):
 # Exact elementary row elimination, no trust in float determinant.
 a=[row[:] for row in M]; sig=1
 for k in range(4):
  idx=next((i for i in range(k,4) if a[i][k]!=0),None)
  if idx is None:return Z
  if idx!=k:a[k],a[idx]=a[idx],a[k];sig=-sig
  for i in range(k+1,4):
   r=a[i][k]/a[k][k]
   for j in range(k+1,4):a[i][j]-=r*a[k][j]
   a[i][k]=Z
 d=Q(sig)
 for k in range(4):d*=a[k][k]
 return d

def inverse4(a):
 # Solve [A | I] over the rational field, no floating inverse in the proof.
 tab=[a[i][:]+[Q(int(i==j)) for j in range(4)] for i in range(4)]
 for j in range(4):
  pivot=next((i for i in range(j,4) if tab[i][j]!=0),None)
  assert pivot is not None
  tab[j],tab[pivot]=tab[pivot],tab[j]
  z=tab[j][j]
  tab[j]=[v/z for v in tab[j]]
  for i in range(4):
   if i==j: continue
   f=tab[i][j]
   tab[i]=[tab[i][k]-f*tab[j][k] for k in range(8)]
 return [row[4:] for row in tab]

def normcert(tlo,thi,xc,r):
 assert tlo<=thi and r>0
 t0=(tlo+thi)/2;dt=(thi-tlo)/2
 hs,gs=hgj(xc)
 q0=qa[0]+qb[0]*t0;q0_hi=q0+qb[0]*dt
 f=[q0*hs[k]-qa[k+1]-qb[k+1]*t0 for k in range(4)]
 ft=[qb[0]*hs[k]-qb[k+1] for k in range(4)]
 J=[[q0*gs[k][j] for j in range(4)] for k in range(4)]
 M=inverse4(J)
 assert matdet(M)!=0
 e=[[Q(int(i==j))-sum(M[i][k]*J[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
 delta=[[qb[0]*dt*abs(gs[k][j])+q0_hi*r*hess_norm[k][j] for j in range(4)] for k in range(4)]
 K=max(sum(abs(e[i][j]) for j in range(4))+
       sum(abs(M[i][k])*sum(delta[k]) for k in range(4)) for i in range(4))
 R=max(abs(sum(M[i][k]*f[k] for k in range(4)))+
       dt*abs(sum(M[i][k]*ft[k] for k in range(4))) for i in range(4))
 assert K<1 and R+K*r<r, (str(tlo),str(thi),float(K),float(R),float(r-R-K*r))
 return K,R,r-R-K*r

def nearest12(y):
 z=y*10**12+Q(1,2)
 return Q(z.numerator//z.denominator,10**12)

def proposal(x,t):
 # Numerical-looking but *exact* finite rational Newton iteration.
 # The existence proof is entirely in subsequent Banach bounds.
 x=list(x)
 for _ in range(3):
  hs,gs=hgj(x); q0=qa[0]+qb[0]*t
  f=[q0*hs[k]-qa[k+1]-qb[k+1]*t for k in range(4)]
  m=inverse4([[q0*gs[k][j] for j in range(4)] for k in range(4)])
  x=[nearest12(x[i]-sum(m[i][k]*f[k] for k in range(4))) for i in range(4)]
 return x

# Completes a closed, exact rational four-branch path from the PREFIX-362
# t=1/16 fiber to t=0.066934, below the proven second fold tb.
import sys
START=Q(1,16)
END=Q(66934,10**6)
assert START<END<T('0.0669341021803707452694')
seeds=[
 ['-0.377672048073067810','-0.033179190554807625','-1.024551038755984257','0.444706162301618834'],
 ['-0.356409585780010685','-0.129264232275208610','-0.996054577075402787','0.505315427522394764'],
 ['-0.352894576312037190','-0.138572914348820846','-0.712359837804994165','0.860239422072391724'],
 ['0.050087969218036839','0.375803445861251879','-1.103871278550833250','0.170107619451771814']]
seeds=[list(map(T,row)) for row in seeds]
# Exact Newton, 3 rounds, 10^-12 quantization. Roots/estimates here are
# candidates; every existence and continuation assertion is certified below.
node_center=[proposal(row,START) for row in seeds]
node_times=[START];nodes=[node_center]
segments=[];attempts=0;failed=0
step=Q(1,10000)
WITNESS_R=Q(1,10**8)
min_radius=Q(1,10**8)
max_steps=2000

def limit_fraction(y,prec=10**8):
 z=y*prec;return Q(z.numerator//z.denominator+1,prec)

def separated(centers,radii):
 for i in range(4):
  for j in range(i+1,4):
   if max(abs(centers[i][k]-centers[j][k]) for k in range(4))<=radii[i]+radii[j]:
    return False
 return True

while node_times[-1]<END:
 assert len(segments)<max_steps, 'Exceeded segment budget'
 a=node_times[-1];b=min(END,a+step);mid=(a+b)/2
 previous=nodes[-1]
 ends=[proposal(previous[i],b) for i in range(4)]
 mids=[proposal(previous[i],mid) for i in range(4)]
 radii=[]
 for i in range(4):
  movement=max(abs(ends[i][k]-mids[i][k]) for k in range(4))
  movement=max(movement,max(abs(previous[i][k]-mids[i][k]) for k in range(4)))
  r=limit_fraction(Q(2)*movement+Q(1,10**7))
  radii.append(max(r,Q(1,10**6)))
 attempts+=1;valid=separated(mids,radii)
 checks=[]
 if valid:
  for i in range(4):
   try:
    K,R,M=normcert(a,b,mids[i],radii[i])
    assert all(max(abs(node[k]-mids[i][k]) for k in range(4))+WITNESS_R<radii[i] for node in (previous[i],ends[i]))
    checks.append((K,R,M))
   except (AssertionError,ZeroDivisionError,OverflowError,ValueError):
    valid=False;break
 if not valid:
  failed+=1
  step/=2
  if step<Q(1,10**13):
   raise AssertionError(f'Adaptive step below 10^-13 at {float(a)}')
  continue
 segments.append({'lo':str(a),'hi':str(b),
                  'centers':[[str(z) for z in row] for row in mids],
                  'radii':[str(r) for r in radii]})
 node_times.append(b);nodes.append(ends)
 step=min(Q(3,1000),step*Q(3,2))
 if len(segments)%20==0:
  print('progress',len(segments),'t=',float(b),'step=',float(step),file=sys.stderr)

max_k=Q(0); max_R=Q(0); min_margin=None
for j,t in enumerate(node_times):
 for i in range(4):
  kw,rw,mw=normcert(t,t,nodes[j][i],WITNESS_R)
  assert mw>0 and kw<1
  max_k=max(max_k,kw)
for j,seg in enumerate(segments):
 c=[[T(z) for z in row]for row in seg['centers']];rr=[T(z) for z in seg['radii']]
 assert separated(c,rr)
 for i in range(4):
  K,R,M=normcert(T(seg['lo']),T(seg['hi']),c[i],rr[i]);max_k=max(max_k,K);max_R=max(max_R,R)
  min_margin=M if min_margin is None else min(M,min_margin)
  for boundary in (nodes[j][i],nodes[j+1][i]):
   assert max(abs(boundary[k]-c[i][k]) for k in range(4))+WITNESS_R<rr[i]
# PREFIX-362 proven roots are contained in the first unique Banach box.
for i in range(4):
 c=[T(z)for z in segments[0]['centers'][i]];r=T(segments[0]['radii'][i])
 for k in range(4):
  e=Q(1,10**12) if k<2 else Q(1,10**6)
  assert abs(seeds[i][k]-c[k])+e<r
r2_v_lower=min(T(s['centers'][2][2])-T(s['radii'][2]) for s in segments)
r1_v_upper=max(T(s['centers'][1][2])+T(s['radii'][1]) for s in segments)
r1_bound=-Q(985,1000);r2_bound=-Q(72,100)
assert r2_v_lower>r2_bound,('r2',float(r2_v_lower))
assert r1_v_upper<r1_bound,('r1',float(r1_v_upper))
q1_lower=(qa[0]+qb[0]*START)/Q(59536)
assert q1_lower>Q(78,100)
midpoint=(r1_bound+r2_bound)/2
margin=2*q1_lower*(r2_bound-r1_bound)/2
assert margin>Q(1,5)>Q(1,8)
assert 2*margin>Q(2,5)

# Two smooth regular survivors cross the exact second fold t_b.
SURVIVOR_RIGHT=Q(7,100)
assert END<T('0.0669341021803707452694')<T('0.0669341021803707452695')<SURVIVOR_RIGHT
survivor_nodes=[nodes[-1][2],nodes[-1][3]]
survivor_times=[END]
survivor_segments=[]
sstep=Q(1,1000)
fail_survivor=0
while survivor_times[-1]<SURVIVOR_RIGHT:
 assert len(survivor_segments)<300
 a=survivor_times[-1]; b=min(SURVIVOR_RIGHT,a+sstep);m=(a+b)/2
 end_roots=[proposal(survivor_nodes[-2+i],b)for i in range(2)]
 mid_roots=[proposal(survivor_nodes[-2+i],m)for i in range(2)]
 radii=[]
 for i in range(2):
  motion=max(max(abs(end_roots[i][k]-mid_roots[i][k]) for k in range(4)),
             max(abs(survivor_nodes[-2+i][k]-mid_roots[i][k]) for k in range(4)))
  radii.append(max(limit_fraction(2*motion+Q(1,10**7)),Q(1,10**6)))
 valid=max(abs(mid_roots[0][k]-mid_roots[1][k]) for k in range(4))>sum(radii)
 if valid:
  for i in range(2):
   try:
    K,R,M=normcert(a,b,mid_roots[i],radii[i]);assert M>0
    assert all(max(abs(z[k]-mid_roots[i][k]) for k in range(4))+WITNESS_R<radii[i] for z in [survivor_nodes[-2+i],end_roots[i]])
   except (AssertionError,ZeroDivisionError):valid=False;break
 if not valid:
  fail_survivor+=1;sstep/=2
  assert sstep>Q(1,10**13)
  continue
 survivor_segments.append({'lo':str(a),'hi':str(b),'centers':[[str(z) for z in row]for row in mid_roots],'radii':[str(r)for r in radii]})
 survivor_times.append(b);survivor_nodes.extend(end_roots)
 sstep=min(Q(1,1000),sstep*Q(3,2))
for j,t in enumerate(survivor_times):
 for i in range(2):
  x=survivor_nodes[2*j+i]
  normcert(t,t,x,WITNESS_R)
  if j==0:
   assert x==nodes[-1][i+2]
for j,seg in enumerate(survivor_segments):
 cc=[[T(z)for z in row]for row in seg['centers']];rr=[T(z)for z in seg['radii']]
 assert max(abs(cc[0][k]-cc[1][k])for k in range(4))>rr[0]+rr[1]
 for i in range(2):
  normcert(T(seg['lo']),T(seg['hi']),cc[i],rr[i])
  for boundary in [survivor_nodes[2*j+i],survivor_nodes[2*(j+1)+i]]:
   assert max(abs(boundary[k]-cc[i][k])for k in range(4))+WITNESS_R<rr[i]
res={
 'schema':'EM_PREFIX364_FOUR_BRANCH_EXACT_INTERVAL_CERTIFICATE_V1',
 'classification':'AUTHOR_SIDE_EXACT_RATIONAL / UNREVIEWED / NOT_ADMITTED',
 'global_snapshot':'b86a7783db271ebadd217ac6acbd0249653336d3',
 'project_source_snapshot':'bcd9709cc57f0313c734d0b53110f9f0d6f0cd1a',
 'span':[str(START),str(END)],
 'interval_segments':len(segments),'banach_root_boxes':4*len(segments),
 'survivor_span':[str(END),str(SURVIVOR_RIGHT)],
 'survivor_labels':['R2','R3'],
 'survivor_segments':len(survivor_segments),
 'survivor_boxes':2*len(survivor_segments),
 'survivor_endpoint_witnesses':2*len(survivor_times),
 'survivor_failed_attempts':fail_survivor,
 'endpoint_witness_boxes':4*len(node_times),
 'failed_adaptive_attempts':failed,
 'max_K_ceiling_1e9':(max_k*10**9).__ceil__(),
 'max_R_ceiling_1e9':(max_R*10**9).__ceil__(),
 'min_self_mapping_margin_floor_1e9':(min_margin*10**9).__floor__(),
 'r1_Re_v_upper':str(r1_v_upper),'r2_Re_v_lower':str(r2_v_lower),
 'uniform_source_labels':['R0','R1','R2','R3'],
 'observer_C_gap_R2_minus_R1_gt':'2/5',
 'observer_threshold':'(Q1(t)+Q3(t)- (341/200)*Q1(t))/59536',
 'observer_threshold_margin_each_gt':'1/5',
 'measurement_additive_noise_abs_le':'1/8',
 'branch_distinctness':'For every exact-parameter Banach box all 6 label pairs have disjoint real coordinate cubes',
 'proof_basis':'Fraction-only four-real-variable Banach contractions, exact continuous-parameter bounds and shared endpoint witnesses; initial labeled t=1/16 roots rely on PREFIX362 certified Rouché/lift boxes',
 'limitation':'Exact full-branch continuation to 0.066934 plus two surviving labels through tb to 0.07; R0/R1 fold pairing follows only when the predecessor H12 exhaustive-unique-ordinary-fold classification is accepted as dependency.',
 'next':'Obtain a standalone certified Lyapunov-Schmidt or interval-normal-form splice from R0/R1 at 0.066934 to tb, discharging dependency on global H12 uniqueness; then extend R2/R3 to t=1/4.'}
(ROOT/'RESULTS_PREFIX364.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print('PASS_PREFIX364_EXACT_FOUR_TO_0P066934_AND_TWO_CROSS_TB')
print(json.dumps({k:v for k,v in res.items() if k not in ['proof_basis','limitation','next']},ensure_ascii=False,indent=2))
