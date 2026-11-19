import math
import scipy.integrate as si
from sympy import totient
pi=math.pi; zeta=pi*pi/6;c=7/(8*zeta)
def f(s):
 if s<=0 or s>=1:return 0.
 if s>=.25:
  t=math.sqrt(4*s-1);u=pi/3-math.atan(t)
  return 12*(1-s)-6*(1+24*s+6*s*math.log(s))*math.log(s)-12*(1+26*s)*t*u-144*s*(1+s)*u*u
 t=math.sqrt(1-4*s);u=math.atanh(t)
 return 12*(1-s)-6*(1+24*s+6*s*math.log(s))*math.log(s)-12*(1+26*s)*t*u-144*s*(1+s)*(pi*pi/9-u*u)
def psiub(r):
 A=r*r/2
 if r>=3:
  zz=(r*r-r*math.sqrt(r*r-8))/4
  return 3*zz**4/(4*zeta*r**4)
 B=A*A/(4*zeta)*sum(float(totient(n))/n*f(n/(2*A)) for n in range(1,math.ceil(2*A)))
 C=A*A/(8*zeta)*sum(float(totient(n))/n*f(n/A) for n in range(1,math.ceil(A)))
 B-=(1 if A<4 else .75)*C
 p=min(A-2*c*A*A/(k+1)+2*B/(k*(k+1)) for k in range(1,32))
 cant=A/(A*A-A+1) if A>1 else 1.
 if r>=3:
  zz=(r*r-r*math.sqrt(r*r-8))/4
  tail=3*zz**4/(4*zeta*r**4)
 else:tail=1.
 return min(A,1,p,cant,tail)
if __name__=='__main__':
 print('norm',si.quad(f,0,1,points=[.25]))
 print('mean',si.quad(lambda x:x*f(x),0,1,points=[.25]))
 print('lower',8/15*c**(-1.5))
 for r in [1,1.2,1.41421356,1.6,1.8,2,2.2,2.5,2.8,3,3.2,4,5]: print(r,psiub(r))
 knots=sorted(set([0,1,1.41421356237,3]+[math.sqrt(i) for i in range(1,11)]))
 vals=[si.quad(psiub,a,b,epsabs=1e-7)[0] for a,b in zip(knots,knots[1:])]
 tail=si.quad(psiub,knots[-1],math.inf,epsabs=1e-7)[0]
 print('ub',2*math.sqrt(2)*(sum(vals)+tail))

def psilb(r):
 A=r*r/2
 B=A*A/(4*zeta)*sum(float(totient(n))/n*f(n/(2*A)) for n in range(1,math.ceil(2*A)))
 C=A*A/(8*zeta)*sum(float(totient(n))/n*f(n/A) for n in range(1,math.ceil(A)))
 M=math.floor(2*A)+1
 return max(0,A-c*A*A+2/M*max(0,B-C),3/(4*zeta*r**4) if r>=math.sqrt(2) else 0)
knots=[0]+[math.sqrt(i) for i in range(1,31)]
print('lower2',2*math.sqrt(2)*sum(si.quad(psilb,a,b,epsabs=1e-6)[0] for a,b in zip(knots,knots[1:])))
for r in [1,1.4,1.6,1.8,2,2.2,2.4,2.6,3,4,5]:print('lb',r,psilb(r))
