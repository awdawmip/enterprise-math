#!/usr/bin/env python3
"""Exact nonenumerating Farey-epoch sweep for the frozen S23/AV risk."""
from fractions import Fraction as F
from collections import defaultdict
import sys,hashlib
LO,HI=F(262204504569236716045286,10**24),F(262204504569236716045287,10**24)
M=128

def cert():
 def log(z):
  s,t=F(0),z
  for k in range(160):s+=2*t/F(2*k+1);t*=z*z
  return s,s+2*t/(321*(1-z*z))
 a,b=log(F(3,4));c,d=log(F(3,17));r0,r1=a/d,b/c
 def th(r):return 79*(2074774-380295*r)/(79*r-431)-46
 assert 79*r0>431 and LO<th(r1)<th(r0)<HI

def fs(n,m,a,b):
 ans=(a//m)*n*(n-1)//2+(b//m)*n;a%=m;b%=m
 while True:
  if a>=m:ans+=n*(n-1)//2*(a//m);a%=m
  if b>=m:ans+=n*(b//m);b%=m
  y=a*n+b
  if y<m:return ans
  n=y//m;b=y%m;m,a=a,m

def count(A,B,p,q,wrap,x):
 if A>B:return 0
 u,v=x.numerator,x.denominator
 def s(z):return fs(B+1,v,u,-z*u)-fs(A,v,u,-z*u)
 return s(p)-s(q)+(p*u//v-q*u//v+wrap)*(B-A+1)

def farey(x,cap):
 p,q=x.numerator,x.denominator;a,b,c,d=0,1,1,1
 while b+d<=cap:
  if (a+c)*q<(b+d)*p:
   t=min((cap-b)//d,(p*b-q*a-1)//(q*c-p*d));a+=t*c;b+=t*d
  else:
   t=min((cap-d)//b,(q*c-p*d-1)//(p*b-q*a));c+=t*a;d+=t*b
 assert b*c-a*d==1 and a*q<b*p and p*d<q*c
 return a,b,c,d

def select(p,q,w,d,end):
 def C(A,B):return count(A,B,p,q,w,LO)
 if d<end and C(d,end-1):
  l,h=d,end-1
  while l<h:
   t=(l+h)//2
   if C(d,t):h=t
   else:l=t+1
  v=l
 else:v=None
 if C(0,d-1):
  l,h=0,d-1
  while l<h:
   t=(l+h+1)//2
   if C(t,d-1):l=t
   else:h=t-1
  z=l
 else:z=None
 def D(A,B):return count(A,B,p,q,w,HI)
 assert (v is None and not D(d,end-1)) or (v is not None and not D(d,v-1) and D(v,v)==1)
 assert (z is None and not D(0,d-1)) or (z is not None and not D(z+1,d-1) and D(z,z)==1)
 return v,z

def choose(types,on):
 options=[types[i] for i in range(3) if on[i]];assert options
 out=max(options,key=lambda t:t[0]+t[1]*LO)
 assert all(out[0]+out[1]*HI>=t[0]+t[1]*HI for t in options)
 return out

def run(L,path):
 cert();N=M+L
 def sort(x):return sorted(range(M),key=lambda i:(i*x.numerator)%x.denominator)
 order=sort(LO);assert order==sort(HI)
 arcs=[(p,order[(j+1)%M],int((p*LO)%1>(order[(j+1)%M]*LO)%1)) for j,p in enumerate(order)]
 n=M;start=M;last=None;blocks=[];epochs=candidates=0
 def change(at,expr):
  nonlocal start,last
  if last is None:last=expr
  elif last!=expr:
   assert all(expr[0]+expr[1]*x>last[0]+last[1]*x for x in (LO,HI))
   blocks.append((start,at-1,*last));start=at;last=expr
 while n<=N:
  a,b,c,d=farey(LO,n-1);assert farey(HI,n-1)==(a,b,c,d)
  end=min(N,b+d);assert farey(LO,end-1)==farey(HI,end-1)==(a,b,c,d)
  lengths=[(-a,b),(c,-d),(c-a,b-d)];active=[];winners=[];ev=defaultdict(list)
  for j,(p,q,w) in enumerate(arcs):
   v,z=select(p,q,w,d,end)
   on=[n>=b+p+1,v is not None and n>=v+1,z is not None and n<=b+z]
   active.append(on);winners.append(choose(lengths,on))
   if n<b+p+1<=end:ev[b+p+1].append((j,0,True))
   if v is not None and n<v+1<=end:ev[v+1].append((j,1,True))
   if z is not None and n<b+z+1<=end:ev[b+z+1].append((j,2,False))
  expr=(1-sum(t[0] for t in winners),-sum(t[1] for t in winners));change(n,expr)
  for at in sorted(ev):
   for j,k,on in ev[at]:
    old=winners[j];active[j][k]=on;new=choose(lengths,active[j]);winners[j]=new
    expr=(expr[0]+old[0]-new[0],expr[1]+old[1]-new[1])
   change(at,expr)
  n=end+1;epochs+=1;candidates+=len(ev)
 blocks.append((start,N,*last))
 with open(path,'w') as f:
  f.write('n_start\tn_end\tA\tB\n')
  for a,b,c,d in blocks:f.write(f'{a}\t{b}\t{c}\t{d}\n')
 with open(path,'rb') as f:h=hashlib.sha256(f.read()).hexdigest()
 assert blocks[0]==(M,M,0,0)
 if L==2_000_000:assert (epochs,candidates,len(blocks),blocks[-1][2:])==(29,6577,3426,(-21156991,80688896))
 if L==10**12:assert (epochs,candidates,len(blocks),blocks[-1][2:])==(78,19072,9698,(-4017401528447,15321634290944))
 print('PASS_CERTIFIED_NONENUMERATING_EPOCH_SWEEP',L,epochs,candidates,len(blocks),h)

if __name__=='__main__':
 L=int(sys.argv[1]) if len(sys.argv)>1 else 10**12
 path=sys.argv[2] if len(sys.argv)>2 else 'BLOCKS_1T.tsv'
 run(L,path)
