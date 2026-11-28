from fractions import Fraction as F

def jets(d,j):
 q=-j;u=d-j;n=d-2*j
 def rr(v,s):
  r=[(F(1),F(0))]
  for i in range(d):
   f=F(v-i,v+i+3);df=F(s*(2*i+3),(v+i+3)**2)
   a,b=r[-1];r.append((a*f,b*f+a*df))
  return r
 U,N=rr(u,1),rr(n,2)
 V=Q=A=Vp=Qp=Ap=F(0)
 for k in range(d+1):
  l=d-k;a=(k+1)*(l+1)*U[k][0]*N[l][0];ap=(k+1)*(l+1)*(U[k][1]*N[l][0]+U[k][0]*N[l][1]);b=(k+1)*l*U[k][0]*N[l-1][0] if l else 0;bp=(k+1)*l*(U[k][1]*N[l-1][0]+U[k][0]*N[l-1][1]) if l else 0
  v=F((u-k)*(u+k+2),2*u*(2*u+1));vp=(2*u+2-v*(8*u+2))/(2*u*(2*u+1));V+=a;Q+=b;A+=v*(a+b);Vp+=ap;Qp+=bp;Ap+=v*(ap+bp)+vp*(a+b)
 E=U[d][0]*F((u-d)*(2*d+3)*(n+2),2*(2*u+1)*(4*n+2));Ep=U[d][1]*F((u-d)*(2*d+3)*(n+2),2*(2*u+1)*(4*n+2))
 assert V==Q==A==E==0
 Wp=Ap+Ep;Zp=q*Ap+Qp+Vp
 T=3*q*(4*q+3*d+1)**2*Wp*Qp-32*(3*q+d+1)*Zp**2
 return T,(Vp,Qp,Ap,Ep,Wp,Zp)

def modC(q,d,M):
 u=q+d;n=2*q+d
 def r(v):
  a=[1]
  for i in range(d):a.append(a[-1]*(v-i)*pow(v+i+3,-1,M)%M)
  return a
 U,N=r(u),r(n);V=Q=A=0;iv=pow(2*u*(2*u+1),-1,M)
 for k in range(d+1):
  l=d-k;a=(k+1)*(l+1)*U[k]*N[l];b=(k+1)*l*U[k]*N[l-1] if l else 0
  V=(V+a)%M;Q=(Q+b)%M;A=(A+(u-k)*(u+k+2)*iv*(a+b))%M
 E=U[d]*(u-d)*(2*d+3)*(n+2)*pow(2*(2*u+1)*(4*n+2),-1,M)%M
 Z=(q*A+Q+V)%M
 return (3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2)%M

def cert():
 from math import isqrt
 from collections import Counter
 ct=Counter();exc=[];surv=[]
 def mod(v,M):return v.numerator*pow(v.denominator,-1,M)%M
 for d in range(4,121):
  for j in range((d+1)//3+1,d//2+1):
   T,_=jets(d,j);ct['fibers']+=1;ct['positive' if T>0 else 'negative' if T<0 else 'zero']+=1
   for p in range(2*d+3,8*d+9):
    if any(p%i==0 for i in range(2,isqrt(p)+1)):continue
    ct['prime_pairs']+=1;tmod=mod(T,p)
    assert modC(-j+p,d,p**3)==p*p*tmod
    assert modC(-j+2*p,d,p**3)==p*p*(4*tmod%p)
    if tmod:ct['unit']+=1;continue
    ct['exception']+=1;B=mod(T,p*p)//p;v=modC(-j+p,d,p**4);assert v%p**3==0;U=(v//p**3-B)%p
    assert modC(-j+2*p,d,p**4)==p**3*(4*(B+2*U)%p)
    assert modC(-j+3*p,d,p**4)==p**3*(9*(B+3*U)%p)
    if U:ts=[(-B*pow(U,-1,p))%p];ct['linear_unit']+=1
    elif B:ts=[];ct['constant_unit']+=1
    else:ts=list(range(1,p));ct['double_degenerate']+=1
    qs=[p*t-j for t in ts if 1<=t<p and p*t-j>=64 and 4*d*d<=5*(p*t-j) and 3*(p*t-j)<=4*d*d]
    if qs:
     for q in qs:
      r=modC(q,d,p**4);assert r==0
      r=modC(q,d,p**5);assert r%p**4==0
      assert r!=0
      surv.append((d,j,p,q,r//p**4))
    exc.append((d,j,p,B,U))
 print(dict(ct));print('survivors',surv);print('exception_count',len(exc));print('first_exceptions',exc[:10])
if __name__=='__main__':cert()
