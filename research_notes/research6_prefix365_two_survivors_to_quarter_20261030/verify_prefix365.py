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


# Exact rational two-label extension. PREFIX-362 R2/R3 seeds at t=1/16.
def ceilr(x):
 z=x*10**8
 return Q(z.numerator//z.denominator+1,10**8)
START=Q(1,16);END=Q(1,4);W=Q(1,10**8)
seeds=[[T(z) for z in row] for row in [
 ['-0.352894576312037190','-0.138572914348820846','-0.712359837804994165','0.860239422072391724'],
 ['0.050087969218036839','0.375803445861251879','-1.103871278550833250','0.170107619451771814']]]
times=[START];nodes=[[proposal(row,START) for row in seeds]]
for i in range(2):
 normcert(START,START,nodes[0][i],W)
 normcert(START,START,nodes[0][i],Q(1,10**5))
 for j in range(4):
  err=Q(1,10**12) if j<2 else Q(1,10**6)
  assert abs(seeds[i][j]-nodes[0][i][j])+err<Q(1,10**5)
step=Q(1,1000);fail=0;segments=[];maxk=Q(0);maxr=Q(0);minm=None
while times[-1]<END:
 assert len(segments)<2500
 a=times[-1];bb=min(END,a+step);mid=(a+bb)/2
 prev=nodes[-1]
 ends=[proposal(prev[i],bb) for i in range(2)]
 centers=[proposal(prev[i],mid) for i in range(2)]
 rr=[]
 for i in range(2):
  motion=max(abs(z[j]-centers[i][j]) for z in [prev[i],ends[i]] for j in range(4))
  rr.append(max(ceilr(2*motion+Q(1,10**7)),Q(1,10**6)))
 valid=max(abs(centers[0][j]-centers[1][j]) for j in range(4))>rr[0]+rr[1]
 if valid:
  try:
   checks=[normcert(a,bb,centers[i],rr[i]) for i in range(2)]
   for i in range(2):
    for z in [prev[i],ends[i]]:
     assert max(abs(z[j]-centers[i][j]) for j in range(4))+W<rr[i]
  except (AssertionError,ZeroDivisionError,ValueError,StopIteration):valid=False
 if not valid:
  fail+=1;step/=2
  assert step>Q(1,10**12),f'Adaptive lower limit at {a}'
  continue
 segments.append((centers,rr))
 times.append(bb);nodes.append(ends)
 for K,R,M in checks:
  maxk=max(maxk,K);maxr=max(maxr,R);minm=M if minm is None else min(minm,M)
 step=min(Q(1,100),step*Q(3,2))
for j,t in enumerate(times):
 for i in range(2):normcert(t,t,nodes[j][i],W)
r2low=min(c[0][2]-r[0] for c,r in segments)
r2high=max(c[0][2]+r[0] for c,r in segments)
r3low=min(c[1][2]-r[1] for c,r in segments)
r3high=max(c[1][2]+r[1] for c,r in segments)
qlow=(qa[0]+qb[0]*START)/Q(59536)
gap=2*qlow*(r2low-r3high)
ref=-Q(381,500)
m2=2*qlow*(r2low-ref);m3=2*qlow*(ref-r3high)
assert gap>Q(3,20) and m2>Q(3,40) and m3>Q(3,40)
res={'schema':'EM_PREFIX365_TWO_FULL_INTERVAL_SURVIVORS_V1',
 'status':'AUTHOR_SIDE_EXACT_RATIONAL / UNREVIEWED / NOT_ADMITTED',
 'global_snapshot':'78f6e3adeafa9ba289243bc44594ba502f512f6f',
 'project_input_snapshot':'ed9e44843ff386caea4371cb3990323cbf219457',
 'range':['1/16','1/4'],'labels':['R2','R3'],'segments':len(segments),
 'root_boxes':2*len(segments),'endpoint_witness_boxes':2*len(times),
 'failed_step_proposals':fail,
 'max_K_upper_1e9':(maxk*10**9).__ceil__(),
 'max_R_upper_1e9':(maxr*10**9).__ceil__(),
 'min_margin_lower_1e9':(minm*10**9).__floor__(),
 'r2_Re_v_bounds':[str(r2low),str(r2high)],
 'r3_Re_v_bounds':[str(r3low),str(r3high)],
 'C_R2_minus_R3_lower':str(gap),
 'threshold':'(Q1+Q3-(381/250)*Q1)/59536',
 'R2_margin_lower':str(m2),'R3_margin_lower':str(m3),
 'uniform_robust_noise_abs_le':'3/40',
 'scope':'Exact rational continuous t interval for two labeled auxiliary sources, not native X6 or a global full-source count'}
(ROOT/'RESULTS_PREFIX365.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('PASS_PREFIX365_TWO_LABELED_SURVIVORS_TO_ONE_QUARTER')
print(json.dumps(res,ensure_ascii=False,indent=2))
