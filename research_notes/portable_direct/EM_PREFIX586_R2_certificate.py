#!/usr/bin/env python3
"""Frozen native X6-BRC 96-port endpoint transport certificate; standard library only.
Source formula checked against PREFIX585_R2_96port_ABBA_certificate.py
at immutable revision 5ec3c4c3787fb1e98cc9d8f288cf0d2f28f2efd7.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
from pathlib import Path

SCIENCE_PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
ORIGIN_PROOF='5ec3c4c3787fb1e98cc9d8f288cf0d2f28f2efd7'
STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*k for k in STARS[a] if k!=abs(c))
PHASE=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in (-1,1) for p in near(a,s*k))
IX={x:i for i,x in enumerate(PHASE)}
def nexts(i):
 a,p,c=PHASE[i]
 b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
 return tuple(IX[t] for t in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=tuple(nexts(i) for i in range(48))
TARGET=IX[(0,1,-3)]
ALPHA=(3,4,1,2,5,6)
def flip(x): return (-1 if x>0 else 1)*ALPHA[abs(x)-1]
THETA=[]
for a,p,c in PHASE:
 u,v=flip(c),flip(p)
 aa=next(j for j,s in enumerate(STARS) if abs(u) in s and abs(v) in s)
 THETA.append(IX[(aa,u,v)])
H=tuple(2*THETA[i//2]+i%2 for i in range(96))
assert len(PHASE)==48 and len(set(PHASE))==48 and len(set(H))==96
assert all(THETA[THETA[i]]==i for i in range(48)) and THETA[TARGET]==TARGET
assert all((THETA[j],THETA[i]) in {(u,v) for u,row in enumerate(NEXT) for v in row} for i,row in enumerate(NEXT) for j in row)
S=[[0]*48 for _ in range(48)]
for i,row in enumerate(NEXT):
 assert len(row)==3
 for j in row:S[i][j]+=1

def invert_and_det(a):
 n=len(a)
 m=[[F(t) for t in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
 det=F(1)
 for k in range(n):
  r=next((r for r in range(k,n) if m[r][k]),None)
  assert r is not None,('singular',k)
  if r!=k:m[k],m[r]=m[r],m[k];det=-det
  pivot=m[k][k];det*=pivot
  m[k]=[t/pivot for t in m[k]]
  for i in range(n):
   if i==k or not m[i][k]:continue
   factor=m[i][k]
   m[i]=[x-factor*y for x,y in zip(m[i],m[k])]
 assert all(m[i][j]==int(i==j) for i in range(n) for j in range(n))
 return det,[row[n:] for row in m]

detS,S_inv=invert_and_det(S)
assert detS==3**12,(detS,'not 3^12')
T=[[int(3*a) for a in row] for row in S_inv]
assert all(F(t)==3*a for rowt,rowa in zip(T,S_inv) for t,a in zip(rowt,rowa))
assert Counter(v for row in T for v in row)=={0:2112,1:144,-2:48}
assert all(sum(t!=0 for t in row)==4 for row in T)
assert all(sum(T[i][j]!=0 for i in range(48))==4 for j in range(48))
for M,N in ((S,T),(T,S)):
 for i in range(48):
  for j in range(48):
   assert sum(M[i][k]*N[k][j] for k in range(48))==3*int(i==j)

def native_A(x,z):
 A=[{} for _ in range(96)]
 for i in range(48):
  weight=x[abs(PHASE[i][2])-1]
  for j in NEXT[i]:
   for u,v in product((0,1),repeat=2):
    val=weight*(z if j==TARGET and u==v==1 else 1)
    if val:A[2*i+u][2*j+v]=F(val)
 return A

def mul(A,B):
 R=[{} for _ in range(len(A))]
 for i,row in enumerate(A):
  for k,v in row.items():
   for j,w in B[k].items():R[i][j]=R[i].get(j,F(0))+v*w
 return [{j:v for j,v in row.items() if v} for row in R]

def trans(A):
 R=[{} for _ in range(len(A))]
 for i,row in enumerate(A):
  for j,v in row.items(): R[j][i]=v
 return R

def U_and_inverse(x):
 U=[{} for _ in range(96)];Ui=[{} for _ in range(96)]
 for i in range(48):
  xi=x[abs(PHASE[i][2])-1]
  for j in NEXT[i]:
   for u in (0,1):U[H[2*j+u]][2*i+u]=F(xi)
  if xi:
   for j in range(48):
    if T[j][i]:
     for u in (0,1):Ui[2*i+u][H[2*j+u]]=F(T[j][i],3*xi)
 return U,Ui

E=[{i:F(1)} for i in range(96)]
for x,z in [((1,1,1,1,1,1),1),((2,3,5,7,11,13),17),((1,2,3,4,5,6),0)]:
 A=native_A(x,z)
 ax=tuple(x[ALPHA[i]-1] for i in range(6))
 Aa=native_A(ax,z)
 U,Ui=U_and_inverse(x)
 assert mul(U,Ui)==E and mul(Ui,U)==E
 assert mul(mul(U,trans(A)),Ui)==Aa
 assert mul(mul(Ui,Aa),U)==trans(A)
 if x==(1,1,1,1,1,1) and z==1:
  assert all(sum(row.values())==6 for row in A)
  assert sum(len(row) for row in A)==576

for j in range(48):
 support=[i for i in range(48) if T[j][i]]
 assert len(support)==4
 assert sorted(T[j][i] for i in support)==[-2,1,1,1]
 assert all(abs(PHASE[i][2])==abs(PHASE[j][1]) for i in support)
 assert len([i for i in range(48) if j in NEXT[i]])==3
 assert all(abs(PHASE[i][2])==abs(PHASE[j][1]) for i in range(48) if j in NEXT[i])

def matvec(A,v):
 return [sum(t*v[j] for j,t in row.items()) for row in A]

open_path_examples=[]
for x,z in [((2,3,5,7,11,13),17),((1,1,1,1,1,1),1),((1,2,3,4,5,6),0)]:
 A=native_A(x,z); ax=tuple(x[ALPHA[i]-1] for i in range(6)); Aa=native_A(ax,z)
 U,Ui=U_and_inverse(x)
 r=[F(1)]*96
 b=matvec(U,r)
 a=[sum(row.get(j,F(0)) for row in Ui) for j in range(96)]
 assert all(t>0 for t in a) and all(t>0 for t in b)
 for j in range(48):
  for u in (0,1):
   pos=H[2*j+u]
   assert a[pos]==F(1,3*x[abs(PHASE[j][1])-1])
   assert b[pos]==F(3*x[abs(PHASE[j][1])-1])
 yy=r[:]; vv=b[:]
 for d in range(9):
  lhs=sum(yy);rhs=sum(a[i]*vv[i] for i in range(96))
  assert lhs==rhs,(x,z,d,lhs,rhs)
  if x==(2,3,5,7,11,13) and z==17 and d in (0,1,8):
   open_path_examples.append({'d':d,'total_original_open_paths_weighted':str(lhs),'positive_twisted_alpha_total':str(rhs)})
  yy=matvec(A,yy);vv=matvec(Aa,vv)
assert any(t<0 for row in T for t in row)

x=(2,3,5,7,11,13);z=2
A=native_A(x,z);ax=tuple(x[ALPHA[i]-1] for i in range(6));Aa=native_A(ax,z)
U,Ui=U_and_inverse(x)
l=[F((i//2)%7+1) for i in range(96)]
r=[F(1+i%2) for i in range(96)]
a=[sum(row.get(j,F(0))*r[i] for i,row in enumerate(Ui)) for j in range(96)]
b=matvec(U,l)
assert min(a)>0 and min(b)>0
for d in range(7):
 lhs=sum(l[i]*r[i] for i in range(96))
 rhs=sum(a[i]*b[i] for i in range(96))
 assert lhs==rhs,(d,lhs,rhs)
 r=matvec(A,r);b=matvec(Aa,b)

def rank_mod(A,p=101):
 arr=[[int(row.get(j,0))%p for j in range(96)] for row in A]
 r=0
 for j in range(96):
  piv=next((k for k in range(r,96) if arr[k][j]),None)
  if piv is None:continue
  arr[r],arr[piv]=arr[piv],arr[r]
  v=pow(arr[r][j],-1,p)
  arr[r][j:]=[(t*v)%p for t in arr[r][j:]]
  for i in range(r+1,96):
   if arr[i][j]:
    b=arr[i][j]
    arr[i][j:]=[(w-b*t)%p for w,t in zip(arr[i][j:],arr[r][j:])]
  r+=1
  if r==96:break
 return r

rank_table=[]
for mask in range(64):
 x=tuple(int(bool(mask&(1<<i))) for i in range(6))
 m=sum(x)
 for z in (0,1,2):
  r=rank_mod(native_A(x,z))
  expected=8*m+int(x[0]!=0 and z!=1)
  assert r==expected,(mask,z,r,expected)
  rank_table.append({'mask':mask,'z':z,'rank_96_native_A_mod_101':r,'predicted_rank_over_Q':expected})

res={
 'schema':'EM_PREFIX586_R2_NATIVE_INTERTWINER_EXACT_CERTIFICATE_V1',
 'science_pin':SCIENCE_PIN,'predecessor_immutable_commit':ORIGIN_PROOF,
 'phase_count':48,'port_count':96,'labeled_actions':576,'gate_target':TARGET,
 'rank_phase_S':48,'det_phase_S':str(detS),'T_equals_3_S_inverse':True,
 'T_histogram':{'0':2112,'1':144,'-2':48},
 'T_nonzero_count':192,'T_nnz_each_row_and_col':4,'S_T_and_T_S_equal_3I':True,
 'all_axis_weights_nonzero':{
  'rank_U':96,'det_U_formula':'3^24 * product(x_i^16 for i=1..6)',
  'inverse_U_formula':'(1/3)*(X_inverse T_transpose tensor I2)*H_inverse',
  'open_endpoint_similarity':'A(alpha*x,z)=U*A(x,z)^T*U_inverse, all z'
 },
 'rank_U_at_zero_axis_weights':'16*number_of_nonzero_axis_weights',
 'rank_V':'48 if z=1; 49 if z!=1',
 'rank_A_for_zero_axis_weights':'8*number_of_nonzero_axis_weights + indicator(x_1!=0 and z!=1)',
 'modular_rank_coverage':{'field_prime':101,'all_64_axis_support_masks':True,'z_values':[0,1,2],
                          'cases':len(rank_table),'all_passed':True},
 'ranks_at_all_positive_axes':{'z=1':48,'z!=1':49},
 'boundary_conversion':'l^T*A(x,z)^d*r=(U^{-T}r)^T*A(alpha*x,z)^d*(U*l)',
 'inverse_T_entries':'-2, 0, +1; signs show no positivity-preserving endpoint map on the whole nonnegative orthant',
 'positive_endpoint_cone': {
  'scope':'x_i>0 for i=1..6; nonnegative original boundary vectors',
  'U_l':'(U*l)[H(j,u)] = x_axis(p_j) * sum_{i: S_ij=1} l[i,u]',
  'U_inverse_transpose_r':'(U^-T*r)[H(j,u)] = (sum_i T[j,i]*r[i,u])/(3*x_axis(p_j))',
  'exact_inequalities':'for each of 48 j and u=0,1: -2*r[i_negative(j),u] + sum_{3 other i in row-support(T[j,*])} r[i,u]>=0',
  'number_of_inequalities':96,
  'independent_of_positive_x':True,
  'uniform_boundary_twist':'U*1[H(j,u)]=3*x_axis(p_j), U^-T*1[H(j,u)]=1/(3*x_axis(p_j))',
  'all_length_exact_identity':True,'open_path_examples':open_path_examples
 },
 'test_cases':{'x_allones_z1':'PASS','x_2_3_5_7_11_13_z17':'PASS','x_1_2_3_4_5_6_z0':'PASS'},
 'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'
}
Path(__file__).with_name('EM_PREFIX586_R2_results.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(res['status'],'detS=',detS,'T_nonzeros=',192,'modular_cases=',len(rank_table))
