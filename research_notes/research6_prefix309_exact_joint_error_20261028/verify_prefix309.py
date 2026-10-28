#!/usr/bin/env python3
"""PREFIX309: exact independent per-readout-error LS gain for source-labelled BRC frames.
The 12 Gaussian matrices are frozen from PREFIX299 RESULTS_PREFIX299.json,
blob b6acffe158f014469235f5428d2889ff43b62810.
Computation is exact Gaussian integer arithmetic and bounded error corners.
This is an auxiliary register, not native X6/Detector simulation.
"""
import json
from fractions import Fraction

ORBIT_DATA={
"S4":[[[[-5,2],[0,0],[2,0]],[[-4,1],[4,0],[-2,1]],[[-1,0],[0,-4],[-1,-6]]],[[[-5,-2],[0,0],[2,0]],[[-4,-1],[4,0],[-2,-1]],[[-1,0],[0,4],[-1,6]]],[[[-5,-2],[0,0],[2,0]],[[-3,2],[4,0],[1,4]],[[-2,1],[0,-4],[-4,-3]]],[[[-5,2],[0,0],[2,0]],[[-3,-2],[4,0],[1,-4]],[[-2,-1],[0,4],[-4,3]]],[[[-5,-2],[0,0],[2,0]],[[-3,1],[0,0],[-5,3]],[[-2,-2],[4,4],[2,2]]],[[[-5,2],[0,0],[2,0]],[[-3,-1],[0,0],[-5,-3]],[[-2,-2],[4,4],[2,2]]]],
"S7":[[[[-6,1],[4,0],[0,1]],[[-2,0],[0,0],[5,-2]],[[-2,1],[-4,0],[-4,1]]],[[[-6,-1],[4,0],[0,-1]],[[-2,-1],[-4,0],[-4,-1]],[[-2,0],[0,0],[5,2]]],[[[-5,3],[0,0],[-3,1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,2]]],[[[-5,-3],[0,0],[-3,-1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,-2]]],[[[-4,-3],[0,4],[-2,1]],[[-4,1],[0,-4],[-2,-3]],[[-2,0],[0,0],[5,2]]],[[[-4,-1],[0,4],[-2,3]],[[-4,3],[0,-4],[-2,-1]],[[-2,0],[0,0],[5,-2]]]]}
Z=(0,0);ONE=(1,0);II=(0,1)
BRC_COUNTS={'mass_reads':0,'ordered_source_pairs':0}
def plus(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return plus(x,neg(y))
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return (x[0],-x[1])
def scale(x,n):return (x[0]*n,x[1]*n)
def summ(xs):
 r=Z
 for x in xs:r=plus(r,x)
 return r
def minor2(a,b,c,d):return sub(mul(a,d),mul(b,c))
def det3(A):
 return summ((mul(A[0][0],minor2(A[1][1],A[1][2],A[2][1],A[2][2])),
             neg(mul(A[0][1],minor2(A[1][0],A[1][2],A[2][0],A[2][2]))),
             mul(A[0][2],minor2(A[1][0],A[1][1],A[2][0],A[2][1]))))
def adj3(A):
 C=[]
 for i in range(3):
  row=[]
  for j in range(3):
   ii=[k for k in range(3) if k!=i];jj=[k for k in range(3) if k!=j]
   z=minor2(A[ii[0]][jj[0]],A[ii[0]][jj[1]],A[ii[1]][jj[0]],A[ii[1]][jj[1]])
   row.append(z if (i+j)%2==0 else neg(z))
  C.append(row)
 return [[C[j][i] for j in range(3)] for i in range(3)]
def matmul(X,Y):return [[summ(mul(X[i][k],Y[k][j]) for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]
def dagger(X):return [[conj(X[j][i]) for j in range(len(X))] for i in range(len(X[0]))]
def rows(M,q):
 q2=mul(q,q)
 return [[(4,0),scale(q,4),Z],[Z,(-4,0),scale(q,4)]]+[
  [mul(tuple(row[k]),(ONE,q,q2)[k]) for k in range(3)] for row in M]
def brc_mass(paths):
 BRC_COUNTS['mass_reads']+=1
 BRC_COUNTS['ordered_source_pairs']+=len(paths)**2
 val=summ(mul(conj(x),y) for _,x in paths for _,y in paths)
 assert val[1]==0 and val[0]>=0
 return val[0]
def brc_polar_test(A):
 a=[(1,0),(0,1),(-1,1)]
 for row in A:
  paths=[('source'+str(k),mul(row[k],a[k])) for k in range(3)]
  z=summ(x for _,x in paths)
  Q0=brc_mass(paths)
  Q1=brc_mass(paths+[('independent_ref_1',(8,0))])
  Qi=brc_mass(paths+[('independent_ref_i',(0,8))])
  assert Q0==z[0]**2+z[1]**2
  assert Q1-Q0-64==16*z[0] and Qi-Q0-64==16*z[1]
def error_vectors(B):
 # delta(a) = (4/detG) sum_j B_j[(s1_j-s0_j)+i(si_j-s0_j)].
 coeffs=[]
 for j in range(len(B[0])):
  b=[B[k][j] for k in range(3)]
  for typ in (0,1,2):
   t=[neg(mul((1,1),x)) if typ==0 else (x if typ==1 else mul(II,x)) for x in b]
   coeffs.append(tuple(v for z in t for v in z))
 return coeffs
def exhaustive_gain(A):
 G=matmul(dagger(A),A);d=det3(G);assert d[1]==0 and d[0]>0
 adj=adj3(G)
 assert matmul(G,adj)==[[scale(ONE,d[0]) if i==j else Z for j in range(3)] for i in range(3)]
 B=matmul(adj,dagger(A))
 coeffs=error_vectors(B);m=len(coeffs)
 curr=[sum(c[k] for c in coeffs) for k in range(6)]
 signs=[1]*m
 best=-1;best_mask=0;max_count=0
 for step in range(1<<m):
  val=sum(v*v for v in curr)
  if val>best:best=val;best_mask=step;max_count=1
  elif val==best:max_count+=1
  if step+1==(1<<m):break
  bit=((step+1)&-(step+1)).bit_length()-1
  old=signs[bit];signs[bit]=-old
  for k in range(6):curr[k]-=2*old*coeffs[bit][k]
 gray=best_mask^(best_mask>>1)
 sign_witness=[-1 if (gray>>k)&1 else 1 for k in range(m)]
 assert sum(sum(sign_witness[u]*coeffs[u][k] for u in range(m))**2 for k in range(6))==best
 witness=[(sign_witness[3*j],sign_witness[3*j+1],sign_witness[3*j+2]) for j in range(len(A))]
 return Fraction(16*best,d[0]**2),{'detG':d[0],'max_norm_Bw_sq':best,
  'max_corner_count':max_count,'corner_index':best_mask,
  'signed_error_witness':witness,'corners_checked':1<<m}
def run():
 phases=[ONE,II,(-1,0),(0,-1)]
 outcomes=[];sum_corners=0;checks=0;success=0
 for family,ms in ORBIT_DATA.items():
  S=[1,0,2] if family=='S4' else [2,0,1]
  for orbit,M in enumerate(ms,1):
   assert sorted(sum(z[0]*z[0]+z[1]*z[1] for z in row) for row in M) in ([33,38,54],[33,44,48],[33,46,46])
   for q in phases:
    A=rows(M,q)
    fullG=matmul(dagger(A),A)
    assert fullG==[[scale(ONE,64-S[k]) if k==l else Z for l in range(3)] for k in range(3)]
    checks+=9
    brc_polar_test(A);success+=15
    selections=[]
    for omit in range(2,5):
     a=[A[k] for k in range(5) if k!=omit]
     gain,witness=exhaustive_gain(a)
     if sum(z[0]*z[0]+z[1]*z[1] for z in M[omit-2])==33:
      assert gain<=Fraction(512,29)
     sum_corners+=witness['corners_checked']
     selections.append({'omit_port':'R'+str(omit-1),'gain_squared':str(gain),**witness})
    gain10,wit10=exhaustive_gain(A)
    assert gain10<=Fraction(320,31)
    sum_corners+=wit10['corners_checked']
    best_gain=min(Fraction(x['gain_squared']) for x in selections)
    winners=[x['omit_port'] for x in selections if Fraction(x['gain_squared'])==best_gain]
    outcomes.append({'family':family,'orbit':orbit,'q':[q[0],q[1]],
       'eight_ref':{'optimal_squared_gain':str(best_gain),'optimal_omissions':winners,'options':selections},
       'ten_ref':{'squared_gain':str(gain10),**wit10}})
 assert BRC_COUNTS=={'mass_reads':720,'ordered_source_pairs':9840}
 assert sum_corners==2162688 and checks==432 and success==720
 max8=max(Fraction(o['eight_ref']['optimal_squared_gain']) for o in outcomes)
 max10=max(Fraction(o['ten_ref']['squared_gain']) for o in outcomes)
 assert max8==Fraction(47553,3364)
 assert max10==Fraction(37829377,3814209)
 return {'status':'PASS','configs':len(outcomes),'gram_entries':checks,
   'polar_readouts':success,'brc_counts':BRC_COUNTS,
   'exhaustive_error_corners':sum_corners,'max8':str(max8),'max10':str(max10),
   'results':outcomes}
if __name__=='__main__':
 print(json.dumps(run(),indent=2))