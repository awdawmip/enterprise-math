#!/usr/bin/env python3
"""R5 exact rational Farkas certificate generator/verifier for all non-diagonal <=4-edge couplings.
Scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568;
EM 86149263e38c22292c9def1e0f69092efa1be77e.
Numerical SciPy HiGHS is used ONLY to find candidate dual support; each certificate is
re-solved in exact SymPy rationals and verified over the complete original equations.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import hashlib
import numpy as np
import sympy as S
from scipy.optimize import linprog

r=tuple(F(v) for v in ('1/10','1/2','3/4','1','5/4','3/2','19/10'))
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)

def mass(x):
 g,a,b,u,v,w,z=x
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
 F(13,40)*a+b/80-u,(g-a)/2,
 1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
 (g-b)/2,F(3,40)*a+F(21,80)*b-w,
 u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(x):
 g,a,b,u,v,w,z=x
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
 1+g+(a+b)/2+u+v+w)

def restrictions(p):
 x,y=p[:7],p[7:]
 return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,*(a-b for a,b in zip(times(x),times(y))))

def slacks(x):
 g,a,b,u,v,w,z=x
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

def phys(p):return slacks(p[:7])+slacks(p[7:])

def rhs(p):
 m,n=mass(p[7:]),mass(p[:7]);return m+n+tuple(r[j]*n[j] for j in range(7))

def jac(fun):
 z=(F(0),)*14; f0=fun(z)
 return S.Matrix([[S.Rational(fun(tuple(F(j==k) for j in range(14)))[i]-f0[i]) for k in range(14)] for i in range(len(f0))])

def col(e):
 i,j=e;v=[F(0)]*21;v[i]=1;v[7+j]=1;v[14+j]=r[i];return S.Matrix(v)

A1=jac(restrictions);b1=S.Matrix(restrictions((F(0),)*14))
A2=jac(rhs);b2=S.Matrix(rhs((F(0),)*14))
A3=jac(phys);b3=S.Matrix(phys((F(0),)*14))
assert A1.shape==(5,14) and A2.shape==(21,14) and A3.shape==(26,14)
assert len(D)==30

# Any positive offdiagonal arc at source j needs both r_i<r_j and r_k>r_j;
# otherwise its nonnegative moment sum cannot vanish. Diagonal arcs do not
# affect moment balance. This filter omits only impossible positive supports.
def balanced_pattern(es):
 for j in (1,2,3,5):
  values=[r[i]-r[j] for i,k in es if k==j and i!=j]
  if values and not(min(values)<0<max(values)):
   return False
 return True

def certificate(es):
 k=4
 C=S.Matrix.hstack(*(col(e) for e in es))
 EQ=A1.row_join(S.zeros(5,k)).col_join((-A2).row_join(C))
 bEQ=(-b1).col_join(b2)
 UB=(-A3).row_join(S.zeros(26,k)).col_join(S.zeros(k,14).row_join(-S.eye(k)))
 bUB=b3.col_join(S.zeros(k,1))
 # Primal: EQ*p=bEQ, UB*p<=bUB, p=(physical_14, four edge weights).
 # Farkas: EQ^T*y+UB^T*z=0, z>=0, bEQ^T*y+bUB^T*z=-1.
 n=EQ.cols;m=EQ.rows;l=UB.rows
 B=EQ.T.row_join(UB.T).col_join(bEQ.T.row_join(bUB.T))
 numerical=linprog(np.array([0.0]*m+[1.0]*l),A_eq=np.array(B,float),
                   b_eq=np.array([0.0]*n+[-1.0]),
                   bounds=[(None,None)]*m+[(0,None)]*l,method='highs')
 if not numerical.success:raise RuntimeError(('dual discovery failed',es,numerical.message))
 active=[i for i,v in enumerate(numerical.x) if abs(v)>1e-8]
 exact,params=B[:,active].gauss_jordan_solve(S.Matrix([0]*n+[-1]))
 if len(params):exact=exact.subs({q:0 for q in params})
 proof=S.zeros(m+l,1)
 for i,v in zip(active,exact):proof[i]=v
 assert all(proof[i]>=0 for i in range(m,m+l))
 assert EQ.T*proof[:m,:]+UB.T*proof[m:,:]==S.zeros(n,1)
 assert (bEQ.T*proof[:m,:]+bUB.T*proof[m:,:])[0]==-1
 # Therefore 0 = y.T EQ*p + z.T UB*p <= y.T bEQ + z.T bUB = -1,
 # contradiction. No numeric solver verdict is used in the final proof.
 return tuple((i,str(proof[i])) for i in range(m+l) if proof[i])

count=Counter();fingerprint=hashlib.sha256();max_terms=0
for es in combinations(D,4):
 if all(i==j for i,j in es):
  count['diagonal_only']+=1;continue
 if not balanced_pattern(es):
  count['moment_excluded']+=1;continue
 cert=certificate(es)
 count['exact_farkas_verified']+=1
 count['offdiagonal_'+str(sum(i!=j for i,j in es))]+=1
 max_terms=max(max_terms,len(cert))
 fingerprint.update((repr(es)+' '+repr(cert)+'\n').encode('utf-8'))
assert count['diagonal_only']==15
assert count['moment_excluded']==26345
assert count['exact_farkas_verified']==1045
assert sum((count[key] for key in ('diagonal_only','moment_excluded','exact_farkas_verified')))==27405
assert count['offdiagonal_2']==405 and count['offdiagonal_3']==324 and count['offdiagonal_4']==316
print('TOTAL_ALLOWED_ARCS',len(D))
print('FOUR_SUPPORT_SUBSETS',27405)
print('DIAGONAL_ONLY',count['diagonal_only'])
print('MOMENT_EXCLUDED_EXACT',count['moment_excluded'])
print('EXACT_RATIONAL_FARKAS_CERTIFICATES',count['exact_farkas_verified'])
print('OFFDIAGONAL_2_3_4_COUNTS',count['offdiagonal_2'],count['offdiagonal_3'],count['offdiagonal_4'])
print('MAX_NONZERO_CERTIFICATE_TERMS',max_terms)
print('CERTIFICATE_TRACE_SHA256',fingerprint.hexdigest())
print('PASS_GLOBAL_NO_NONDIAGONAL_SUPPORT_OF_SIZE_AT_MOST_FOUR_IN_FROZEN_R5')
