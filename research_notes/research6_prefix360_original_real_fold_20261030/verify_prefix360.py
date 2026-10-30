#!/usr/bin/env python3
"""PREFIX-360 static auxiliary five-Port model: exact rational interval Newton
certificate of first real fold in the original 4-variable intensity equations.
Contains no native X6/heartbeat arithmetic or ordinary propagator.
"""
import json
from fractions import Fraction as Fr
from itertools import permutations
from pathlib import Path
import sympy as s

R=s.Rational; I=s.I
x=s.symbols('x0:4',real=True);t=s.symbols('t',real=True);Z=(*x,t)
Q=[34000+204144*t,3200+56336*t,58250+1286*t,46600+12936*t,31525+28011*t]
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=s.simplify(A[3:,:]*A[:3,:].inv())
assert B==s.Matrix([[R(5,2)+R(9,2)*I,R(3,2)+R(7,2)*I,4*I],[R(11,4)+R(15,8)*I,R(11,4)+R(15,8)*I,R(5,4)+R(9,4)*I]])
H=[x[0]**2+x[1]**2,x[2]**2+x[3]**2]
for k in range(2):
 b0,b1,b2=list(B.row(k))
 re=s.re(b0)+s.re(b1)*x[0]-s.im(b1)*x[1]+s.re(b2)*x[2]-s.im(b2)*x[3]
 im=s.im(b0)+s.im(b1)*x[0]+s.re(b1)*x[1]+s.im(b2)*x[2]+s.re(b2)*x[3]
 H.append(s.expand(re*re+im*im))
F=s.Matrix([s.expand(Q[0]*H[k]-Q[k+1]) for k in range(4)])
J=F.jacobian(x)
Fx_t=F.diff(t)
Jpartial=[J.diff(z) for z in Z]
Hess=[s.hessian(F[i],x) for i in range(4)]

coords=Path(__file__).with_name('center360.txt').read_text().splitlines()
assert len(coords)==5
c=[Fr(a) for a in coords]
r=Fr(1,10**24)
LO=Fr('0.0140246596320690270474');HI=Fr('0.0140246596320690270475')
assert LO<c[4]-r<c[4]+r<HI

class Iv:
 def __init__(self,lo,hi=None):
  self.lo=tofr(lo);self.hi=tofr(hi if hi is not None else lo)
  assert self.lo<=self.hi
 def __add__(self,o):
  o=toi(o);return Iv(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return Iv(-self.hi,-self.lo)
 def __sub__(self,o):return self+(-toi(o))
 def __rsub__(self,o):return toi(o)+(-self)
 def __mul__(self,o):
  o=toi(o);q=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
  return Iv(min(q),max(q))
 __rmul__=__mul__
 def __pow__(self,k):
  assert isinstance(k,int) and k>=0
  if k==0:return Iv(1)
  if k%2==0:
   low=0 if self.lo<=0<=self.hi else min(self.lo**k,self.hi**k)
   return Iv(low,max(self.lo**k,self.hi**k))
  return Iv(self.lo**k,self.hi**k)
 def absup(self):return max(abs(self.lo),abs(self.hi))
 def includes_zero(self):return self.lo<=0<=self.hi
 def __repr__(self):return f'[{float(self.lo):.8g},{float(self.hi):.8g}]'
def tofr(y):
 if isinstance(y,Fr):return y
 if isinstance(y,s.Rational):return Fr(int(y.p),int(y.q))
 return Fr(y)
def toi(a):return a if isinstance(a,Iv) else Iv(a)
cache={}
def ev(expr,box):
 if expr not in cache:
  poly=s.Poly(expr,*Z,domain=s.QQ)
  cache[expr]=[(tuple(int(p) for p in mon),tofr(co)) for mon,co in poly.terms()]
 z=Iv(0)
 for mon,co in cache[expr]:
  y=Iv(co)
  for k,p in enumerate(mon):
   if p:y=y*box[k]**p
  z=z+y
 return z

def detm(mat):
 n=len(mat);out=Iv(0)
 for perm in permutations(range(n)):
  term=Iv(1)
  for i,j in enumerate(perm):term=term*mat[i][j]
  inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
  out=out+(-term if inversions%2 else term)
 return out

def cof(mat):
 n=len(mat)
 return [[((-1)**(i+j))*detm([[mat[k][l] for l in range(n) if l!=j] for k in range(n) if k!=i]) for j in range(n)] for i in range(n)]

def augJac(box):
 ij=[[ev(J[i,j],box) for j in range(4)]for i in range(4)]
 cf=cof(ij)
 ans=[[ij[i][j] for j in range(4)]+[ev(Fx_t[i],box)] for i in range(4)]
 bottom=[]
 for k in range(5):
  deriv=Iv(0)
  for i in range(4):
   for j in range(4):deriv=deriv+cf[i][j]*ev(Jpartial[k][i,j],box)
  bottom.append(deriv)
 ans.append(bottom)
 return ans,ij,cf

center={z:s.Rational(v.numerator,v.denominator) for z,v in zip(Z,c)}
Jc=J.subs(center)
Jcof=Jc.cofactor_matrix()
g0=[tofr(f.subs(center)) for f in F]+[tofr(Jc.det())]
a0=s.Matrix(5,5,lambda i,j:(Jc[i,j] if i<4 and j<4 else
                              Fx_t[i].subs(center) if i<4 else
                              sum(Jcof[p,q]*Jpartial[j][p,q].subs(center) for p in range(4) for q in range(4))))
assert a0.det()!=0
Minv=a0.evalf(95).inv().evalf(85)
scale=10**55
M=[[Fr(int(s.floor(Minv[i,j]*scale+s.Rational(1,2))),scale) for j in range(5)]for i in range(5)]
box=[Iv(z-r,z+r) for z in c]
aint,ij,cf=augJac(box)
K=Fr(0)
for i in range(5):
 row=Fr(0)
 for j in range(5):
  q=Iv(int(i==j))
  for k in range(5):q=q-M[i][k]*aint[k][j]
  row+=q.absup()
 K=max(K,row)
d=max(abs(sum(M[i][j]*g0[j] for j in range(5))) for i in range(5))
assert K<Fr(1,10),f'Newton contraction insufficient: {float(K)}'
assert d+K*r<r,f'Newton cube mapping insufficient {float(d)}'

minor=detm([[ij[i][j] for j in range(3)]for i in range(3)])
assert not minor.includes_zero(), 'rank-three cofactor not certified'
adj=[[cf[j][i] for j in range(4)] for i in range(4)]
w=[adj[i][3] for i in range(4)]
lam=[adj[3][i] for i in range(4)]
assert all(z.absup()>0 for z in w+lam)
Ftbox=[ev(Fx_t[i],box) for i in range(4)]
trans=sum((lam[i]*Ftbox[i] for i in range(4)),Iv(0))
quad=Iv(0)
for i in range(4):
 for j in range(4):
  for k in range(4):quad=quad+lam[i]*w[j]*w[k]*ev(Hess[i][j,k],box)
assert not trans.includes_zero(), 'lambda.F_t transversality unknown'
assert not quad.includes_zero(), 'lambda.F_xx(w,w) degeneracy unknown'

result={
 'schema':'ENTERPRISE_MATH_PREFIX360_EXACT_ORIGINAL_FOLD_INTERVAL_CERTIFICATE_V1',
 'status':'AUTHOR_SIDE_EXACT_RATIONAL_CERTIFICATE_UNREVIEWED_NOT_ADMITTED',
 'scope':'Original four real quadratic source-ratio equations for the static auxiliary complex 3x5 model; not native X6/BRC time evolution',
 'source_pins':{'enterprise_math_main':'f2972ea48c82f39c42fb8e269489d609a36aee4c','global_knowledge_main':'0e491176513f7ff996d61c71827e2701bad1c225'},
 'A':[[str(A[i,j]) for j in range(3)]for i in range(5)],'Q':[str(v) for v in Q],
 'critical_t_bracket':[str(LO),str(HI)],'center_rationals_as_decimals':coords,
 'cube_radius':'1/10^24',
 'augmented_system':'G(x,t)=(F_1,F_2,F_3,F_4,det(F_x)); F_k=Q1*H_k-Q_{k+1}; H=(|u|^2,|v|^2,|B0+B1*u+B2*v|^2,|D0+D1*u+D2*v|^2)',
 'exact_rational_certificate':{
  'contraction_lt_1_over_10':K<Fr(1,10),
  'displacement_plus_contraction_r_lt_r':d+K*r<r,
  'K_lt':str(Fr(int(K*10**18)+1,10**18)),
  'd_lt':str(Fr(int(d*10**36)+1,10**36)),
  'minor_rank3_sign':'positive' if minor.lo>0 else 'negative',
  'minor_abs_lower_gt_10pow14':min(abs(minor.lo),abs(minor.hi))>10**14,
  'lambda_Ft_sign':'positive' if trans.lo>0 else 'negative',
  'lambda_Ft_abs_gt_10pow18':min(abs(trans.lo),abs(trans.hi))>10**18,
  'lambda_Hessian_ww_sign':'positive' if quad.lo>0 else 'negative',
  'lambda_Hessian_ww_abs_gt_10pow48':min(abs(quad.lo),abs(quad.hi))>10**48,
 },
 'proof_type':'Exact rational interval Banach (uniform augmented Jacobian) + interval adjugate rank/transversality/curvature',
 'logical_conclusion':'Unique augmented critical (x,t) in box; rank J=3; lambda Ft !=0 and lambda Fxx[w,w] !=0; ordinary fold of F at critical point.',
 'dependencies':'Prior PREFIX-356 isolates H12 root and confirms no alternative positive H12 root in bracket; PREFIX-355 supplies endpoint 6/4 count. This check is independent for local fold structure.',
 'boundaries':'No claim of native X6 physical dynamics, global branch pairing beyond local fold, second fold not checked, not reviewed/admitted.'
}
assert result['exact_rational_certificate']['minor_abs_lower_gt_10pow14']
assert result['exact_rational_certificate']['lambda_Ft_abs_gt_10pow18']
assert result['exact_rational_certificate']['lambda_Hessian_ww_abs_gt_10pow48']
out=Path(__file__).with_name('RESULTS_PREFIX360.json')
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('PASS_PREFIX360_EXACT_ORIGINAL_REAL_FOUR_VARIABLE_ORDINARY_FOLD')
print('critical parameter bracket',LO,HI)
print('cube radius',r)
print('K<',result['exact_rational_certificate']['K_lt'],'d<',result['exact_rational_certificate']['d_lt'])
print('3x3 minor',result['exact_rational_certificate']['minor_rank3_sign'],'abs>1e14')
print('lambda.F_t',result['exact_rational_certificate']['lambda_Ft_sign'],'abs>1e18')
print('lambda.Hessian(w,w)',result['exact_rational_certificate']['lambda_Hessian_ww_sign'],'abs>1e48')
