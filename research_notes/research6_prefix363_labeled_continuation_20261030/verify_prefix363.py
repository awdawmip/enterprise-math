#!/usr/bin/env python3
"""PREFIX-363 exact rational uniform interval Banach continuation.
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

lo=T('0.0598990506977195435624')
hi=T('0.0598990506977195435625')
Tc=(lo+hi)/2
top=Q(1,16)
assert lo<Tc<hi and Tc<top
N=32
h3_centers=[
 list(map(T,['-0.350254450435209402','-0.139786042875789802','-0.717408911887365257','0.864319809947346322'])),
 list(map(T,['-0.350254450435209402','-0.139786042875789802','-0.998209376262943823','0.515075064299927955']))]
old362={
 'R1':list(map(T,['-0.356409585780010685','-0.129264232275208610','-0.996054577075402787','0.505315427522394764'])),
 'R2':list(map(T,['-0.352894576312037190','-0.138572914348820846','-0.712359837804994165','0.860239422072391724']))}
branches=[]
for x0 in h3_centers:
 segments=[]; boundaries=[]
 for j in range(2*N+1):
  t_here=Tc+(top-Tc)*Q(j,2*N)
  x0=proposal(x0,t_here)
  if j%2==0:boundaries.append({'center':x0})
  else:segments.append({'center':x0})
 branches.append({'segments':segments,'boundaries':boundaries})

mesh=[Tc+(top-Tc)*Q(j,N) for j in range(N+1)]
r=Q(1,2000)
witness_r=Q(1,10**7)
maxK=Z; maxR=Z; minMargin=None;maxGap=Z
proof={"schema":"EM_PREFIX363_EXACT_CONTINUATION_V1","number_of_segments":N,
       "span":[str(Tc),"1/16"],"cube_radius":str(r),"witness_cube_radius":str(witness_r),"branches":[]}
for branchno, b in enumerate(branches):
 maxKb=Z;maxRb=Z;minMb=None
 for i,node in enumerate(b['segments']):
  x=list(map(T,node['center']))
  K,R,margin=normcert(mesh[i],mesh[i+1],x,r)
  maxKb=max(maxKb,K);maxRb=max(maxRb,R);minMb=margin if minMb is None else min(minMb,margin)
 for j,wit in enumerate(b['boundaries']):
  x=list(map(T,wit['center']))
  K,R,margin=normcert(mesh[j],mesh[j],x,witness_r)
  assert K<Q(1,20) and margin>0
  for neigh in ([0] if j==0 else [N-1] if j==N else [j-1,j]):
   c=list(map(T,b['segments'][neigh]['center']))
   # A whole small witness cube sits inside both adjacent large cubes.
   assert max(abs(x[k]-c[k]) for k in range(4))+witness_r<r,(branchno,j,neigh)
 # Compare the start witness to the cited PREFIX358 Banach cube.
 h3=h3_centers[branchno]
 x0=list(map(T,b['boundaries'][0]['center']))
 assert max(abs(x0[k]-h3[k]) for k in range(4))+witness_r<Q(1,10000)
 # Compare t=1/16 to PREFIX362 labeled physical R1 (index1) / R2(index2).
 physical=old362['R1' if branchno==1 else 'R2']
 c_last=list(map(T,b['segments'][-1]['center']))
 assert max(abs(physical[k]-c_last[k])+(Q(1,10**12) if k<2 else Q(1,10**6)) for k in range(4))<r
 proof['branches'].append({"h3_branch":branchno+1,"fiber_label":'R1' if branchno==1 else 'R2',
 "maximum_contraction_ceiling_over_1e9":(maxKb*10**9).__ceil__(),
 "maximum_displacement_ceiling_over_1e9":(maxRb*10**9).__ceil__(),
 "minimum_self_mapping_margin_floor_over_1e9":(minMb*10**9).__floor__(),
 "endpoint_witnesses":len(b['boundaries'])})
 maxK=max(maxK,maxKb);maxR=max(maxR,maxRb)
 minMargin=minMb if minMargin is None else min(minMargin,minMb)
# Two branches remain distinct on [Tc,top]: the real part of v has a disjoint
# range even across the whole path; sufficient because local boxes fix labels.
bs=branches
branch0_v_max=max(T(z['center'][2])+r for z in bs[0]['segments'])
branch1_v_min=min(T(z['center'][2])-r for z in bs[1]['segments'])
assert branch0_v_max < -Q(7,10)
assert branch1_v_min < -Q(99,100)
# strong global separation: branch0 Re(v)>-0.73, branch1 Re(v)<-0.99
branch0_v_min=min(T(z['center'][2])-r for z in bs[0]['segments'])
branch1_v_max=max(T(z['center'][2])+r for z in bs[1]['segments'])
assert branch0_v_min>-Q(73,100) and branch1_v_max<-Q(99,100)
# C(t)=|y1+y3|²=q1(t)*(1+r3(t)+2*Re(v)). The parameter-dependent
# threshold uses *only* original intensities and the fixed midpoint -43/50.
# The two source branches are robustly separated for ALL t on the chain.
q1_lower=(qa[0]+qb[0]*lo)/Q(59536)
assert q1_lower>Q(10,13)
assert 2*q1_lower*Q(13,50)>Q(2,5)
assert 2*q1_lower*Q(13,100)>Q(1,5)>Q(1,8)
proof['global_v_real_part_separation_gt']='26/100'
proof['global_v_squared_separation_gt']='169/2500' # (0.26)^2
proof['uniform_C_R2_minus_R1_gt']='2/5'
proof['threshold']='(Q1(t)+Q3(t)-(43/25)*Q1(t))/59536'
proof['threshold_margin_each_gt']='1/5'
proof['additive_noise_abs_robust']='1/8'
proof['verified_interval_boxes']=2*N
proof['verified_endpoint_witnesses']=2*(N+1)
proof['verification']='Exact fractions only; finite cubic-complex model; each branch unique in own cube; shared endpoint witness links adjacent parameter cubes.'
proof['status']='AUTHOR_SIDE_EXACT_RATIONAL / UNREVIEWED / NOT_ADMITTED'
proof['pending']='No two-fold global branch matching, no native X6 and no typed BRC heartbeat test'
(ROOT/'RESULTS_PREFIX363.json').write_text(json.dumps(proof,indent=2,ensure_ascii=False)+'\n')
print('PASS_PREFIX363_EXACT_TWO_LABELED_BRANCH_CONTINUATIONS')
print('segments',N,'boxes',2*N,'witnesses',2*(N+1))
for b in proof['branches']:print(b)
