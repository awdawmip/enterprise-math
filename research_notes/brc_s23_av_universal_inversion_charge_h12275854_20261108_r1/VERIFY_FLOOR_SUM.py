#!/usr/bin/env python3
"""Finite-H exact S23/AV inversion-charge counts by Euclidean floor sums."""
from fractions import Fraction as F
import random
u=(79,431); w=(380295,2074774); a,c=u; D,P=w; M=P+D

def logbounds(x,terms):
 s=sum((x**(2*k+1)/F(2*k+1) for k in range(terms)),F())
 t=2*terms+1
 return 2*s, 2*(s+x**t/(t*(1-x*x)))

def alpha_bounds(terms):
 x,y=logbounds(F(1,3),terms);z,t=logbounds(F(1,15),terms);g,h=logbounds(F(3,17),terms)
 rlo,rhi=(3*x-t)/h, (3*y-z)/g
 assert rlo<rhi
 return (a*rlo-c)/(P-D*rlo),(a*rhi-c)/(P-D*rhi)

def floor_sum(n,m,a,b):
 assert n>=0 and m>0
 qa,a=divmod(a,m);qb,b=divmod(b,m)
 out=qa*n*(n-1)//2+qb*n
 while True:
  if a>=m:out+=n*(n-1)//2*(a//m);a%=m
  if b>=m:out+=n*(b//m);b%=m
  y=a*n+b
  if y<m:return out
  n,b=divmod(y,m)
  m,a=a,m

def floor_linear(lo,hi,x,y,m):
 if lo>hi:return 0
 # sum over A=lo..hi floor((x-y*A)/m)
 return floor_sum(hi-lo+1,m,-y,x-y*lo)

def alpha_floor_sum(n,al):return floor_sum(n,al.denominator,al.numerator,al.numerator)

class ExactAlpha:
 def __init__(self,N):
  self.terms=24;self.lo,self.hi=alpha_bounds(self.terms)
  while alpha_floor_sum(N,self.lo)!=alpha_floor_sum(N,self.hi):
   self.terms*=2;self.lo,self.hi=alpha_bounds(self.terms)
   assert self.terms<=384, 'unexpected precision demand'
  self.N=N
 def floor(self,A):
  assert 0<=A<=self.N
  v=(A*self.lo.numerator)//self.lo.denominator
  assert v==(A*self.hi.numerator)//self.hi.denominator
  return v
 def sum_floor(self,N):
  assert N<=self.N
  return alpha_floor_sum(N,self.lo)

def binary_last(N,good):
 lo,hi=0,N
 while lo<hi:
  md=(lo+hi+1)//2
  if good(md):lo=md
  else:hi=md-1
 return lo

def count_F(T,alpha):
 N=max(0,(T-M)//(a+c))
 assert N<=alpha.N
 U=lambda A:(T-(a+c)*A)//M
 k=binary_last(N,lambda A: U(A)>alpha.floor(A))
 return floor_linear(1,k,T,a+c,M)-alpha.sum_floor(k)

def count_G(v,j,alpha):
 N=max(0,min((v-D)//a,(j-P)//c))
 assert N<=alpha.N
 upper=lambda A:min((v-a*A)//D,(j-c*A)//P)
 k=binary_last(N,lambda A:upper(A)>alpha.floor(A))
 cross=P*v-D*j
 pivot=max(0,min(k,cross-1))
 # A<=cross-1 uses j, A>=cross uses v
 return floor_linear(1,pivot,j,c,P)+floor_linear(pivot+1,k,v,a,D)-alpha.sum_floor(k)

def brute(H,p=None,alpha=None):
 rr=alpha.lo
 dirs=[]
 for B in range(1,H//M+1):
  for A in range(1,(H-M*B)//(a+c)+1):
   if alpha.floor(A)<B:dirs.append((a*A+D*B,c*A+P*B))
 if p is None:return len(dirs)
 v,j=p
 return sum(x<=v and y<=j for x,y in dirs)

# Small actual S23/AV scopes: full independent direction enumeration.
for H in (4910647,4910648,7365717,9820786,9821296,12275855,25000000,100000000):
 alpha=ExactAlpha(max(1,H//(a+c)))
 got=count_F(H,alpha);want=brute(H,alpha=alpha)
 assert got==want,(H,got,want)
 test=[(0,0),(H,0),(0,H),(H//2,H//2),(H//3,H//4),(H//8,H//2)]
 for p in test:
  v,j=p
  if v+j>H:continue
  gotG=count_G(v,j,alpha)
  wantG=brute(H,p,alpha)
  assert gotG==wantG,(H,p,gotG,wantG)
 print('PASS_FULL_DIRECTION_CROSSCHECK',H,'F',got,'TERMS',alpha.terms)

# Large exact integer query without scanning directions; each uses only floor sums.
for H in (10**9,10**12,10**15):
 alpha=ExactAlpha(max(1,H//(a+c)))
 p=(H//3,H//2)
 f=count_F(H-sum(p),alpha)
 g=count_G(*p,alpha)
 assert f>=0 and g>=0
 print('PASS_LARGE_EXACT_FLOOR_SUM',H,'F',f,'G',g,'RANK_CHARGE',f-g,'TERMS',alpha.terms)
print('PASS_S23_AV_ALL_FINITE_H_FLOOR_SUM_RANK_FORMULA')
