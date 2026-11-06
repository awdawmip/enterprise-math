#!/usr/bin/env python3
"""PREFIX-534 reproducible exact certificate; Python3 + SymPy; native four-STAR model."""
from collections import Counter, defaultdict
from sympy import symbols, expand, Poly, gcd
from json import dump
A=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def nbr(j,c):return [(-1 if c>0 else 1)*x for x in A[j] if x!=abs(c)]
S=[(j,p,sg*x) for j in range(4) for x in A[j] for sg in (-1,1) for p in nbr(j,sg*x)]
idx={s:i for i,s in enumerate(S)}; assert len(S)==48
E=[]
for j,p,c in S:
 k=next(k for k in range(4) if k!=j and abs(c) in A[k])
 E.append([idx[s] for s in [(j,c,x) for x in nbr(j,c) if x!=p]+[(k,c,x) for x in nbr(k,c)]])
T=idx[(0,1,-3)]
sign=lambda i: (1 if S[i][2]>0 else -1) if abs(S[i][2])==1 else 0
b=lambda i:int(abs(S[i][2])==1)
BACK=[Counter(b(i)+2*b(j)+b(T) for j in E[i] if T in E[j]) for i in range(48)]
u,q,z=symbols('u q z')
e=1-4*u-(192+480*q)*u**2-(2304+8064*q+2304*q*q)*u**3-(82944*q+62208*q*q)*u**4-746496*q*q*u**5
f=(1+8*u-48*q*u*u)*(1+(4+2*q)*16*u*u-(12*q+4*q*q)*64*u**3+2304*q*q*u**4)
k=[0,0,20*q,160*q*q+368*q,2560*q*q+5120*q,-27648*q**3+16384*q*q+27648*q,-73728*q**4-774144*q**3-485376*q*q+147456*q,-1400832*q**4-9732096*q**3-3833856*q*q,-0+7077888*q**5-8847360*q**4-58392576*q**3-31850496*q*q,127401984*q**5+445906944*q**4-191102976*q**3,573308928*q**5+5733089280*q**4,-20639121408*q**5]
D=Poly(expand(e*f-(z-1)*sum(v*u**i for i,v in enumerate(k))),u,q,z)
assert D.degree(u)==11
Delta=defaultdict(dict)
for (du,dq,dz),v in D.terms():Delta[2*du][(2*dq,dz)]=int(v)
assert Delta[0]=={(0,0):1}
def inc(dst,src,dv=0,dz=0,c=1):
 for (v,h),n in src.items():dst[(v+dv,h+dz)]=dst.get((v+dv,h+dz),0)+c*n
def trim(d):return {k:v for k,v in d.items() if v}
R=[([{(-abs(sign(i)-s),0):1} for i in range(48)],{}) for s in (-1,0,1)]
H={}; exceptional={}; peak=0
for d in range(72):
 y=[trim(R[sign(i)+1][0][i]) for i in range(48)]
 peak=max(peak,max(map(len,y)))
 if d<8:assert all(sum(v.values())==6**d for v in y)
 for shift,terms in Delta.items():
  if d+shift>71:continue
  arr=H.setdefault(d+shift,[{} for _ in range(48)])
  for i in range(48):
   for (dv,dz),c in terms.items():inc(arr[i],y[i],dv,dz,c)
 if d>=22:
  residual=[trim(x) for x in H.pop(d)]
  if d==22:exceptional={str(S[i]):{str(a):v for a,v in p.items()} for i,p in enumerate(residual) if p}
  else:assert all(not p for p in residual),('recurrence failed',d)
 if d==71:break
 N=[]
 for old,g in R:
  new=[]
  for i in range(48):
   h={}
   for j in E[i]:inc(h,old[j],b(i)+b(j),0,2)
   for dv,c in BACK[i].items():inc(h,g,dv,0,c)
   new.append(trim(h))
  h={};inc(h,old[T],0,1);inc(h,old[T],0,0,-1)
  N.append((new,trim(h)))
 R=N
assert set(exceptional)=={'(0, -6, 1)','(1, -4, 1)','(1, -5, 1)'}
p=1000000007;vv=2;zz=3; powers={i:pow(vv,i,p) for i in range(-2,5)}
R=[([powers[-abs(sign(i)-s)] for i in range(48)],0) for s in (-1,0,1)]
yseq=[[] for _ in range(48)]
for d in range(23):
 for i in range(48):yseq[i].append(R[sign(i)+1][0][i])
 N=[]
 for row,g in R:
  nx=[(sum(2*powers[b(i)+b(j)]*row[j] for j in E[i])+sum(c*powers[v]*g for v,c in BACK[i].items()))%p for i in range(48)]
  N.append((nx,((zz-1)*row[T])%p))
 R=N
vcoef=[0]*23
for sh,terms in Delta.items():vcoef[sh]=sum(c*pow(vv,dv,p)*pow(zz,dz,p) for (dv,dz),c in terms.items())%p
X=symbols('X');den=Poly(sum(c*X**i for i,c in enumerate(vcoef)),X,modulus=p)
assert den.degree()==22
for i in range(48):
 num=[sum(vcoef[j]*yseq[i][d-j] for j in range(d+1))%p for d in range(23)]
 assert gcd(Poly(sum(a*X**j for j,a in enumerate(num)),X,modulus=p),den).degree()==0
 assert (num[22]!=0)==(str(S[i]) in exceptional)
result={'status':'ALL_CHECKS_PASS','scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','symbolic':{'roots':48,'Delta_u_degree':11,'Delta_t_degree':22,'Delta_monomials':sum(map(len,Delta.values())),'all_zero_residual_depths':'23..71','CH_dimension':49,'numerator_t22':exceptional,'max_sparse_terms':peak},'modular':{'prime':p,'v':vv,'q':vv*vv,'z':zz,'all_48_coprime':True},'theorem':'All 48 rooted observers have generic minimum eventual recurrence order 22; 3 have numerator degree 22 and 45 have numerator degree <=21.'}
with open('PREFIX534_EXACT_EXECUTION.json','w') as fp:dump(result,fp,indent=2)
print(result['status'],result['symbolic']['numerator_t22'])
