"""Exact first-divergence search over distinct positive fractional-linear continuations."""
from fractions import Fraction as F
from functools import cache
from math import gcd,prod

SCALE=2**100
ID=(1,0,0,1)
def mul(u,v):
 a,b,h,d=u;e,f,g,i=v
 w=(a*e+b*g,a*f+b*i,h*e+d*g,h*f+d*i)
 t=gcd(*w)
 return tuple(x//t for x in w)
@cache
def edge(r,c,m):
 k=2*r+1;v=c-m
 A=prod(k+4*n for n in range(v,c+1));B=prod(k+n for n in range(v,c+1))
 E=(k-1+v)*prod(4*k+n for n in range(v,c+1))
 t=28*(k-1+4*v)*A*B
 return mul(ID,(t,A*E,t,4**m*E*B))
@cache
def ends(c):
 x=F(840,(c+2)*(c+3)*(c+4))
 y=prod((F(4*n+1,4*n+4) for n in range(3,c+1)),start=F(1))
 z=sorted(y*(x*a+b)/(1+x*y*a) for a,b in zip((F(3,32),F(3,2),F(6)),(F(15,32),F(15,8),F(3))))
 return z[0],z[-1]
def image(M,lo,hi):
 a,b,h,d=M
 if a*d<b*h:lo,hi=hi,lo
 return ((a*lo+b*SCALE)*SCALE//(h*lo+d*SCALE),-(-(a*hi+b*SCALE)*SCALE//(h*hi+d*SCALE)))
@cache
def span(r,c):
 if not r:
  x,y=ends(c);return (x*SCALE).__floor__(),(y*SCALE).__ceil__()
 ims=[image(edge(r,c,m),*span(r-1,c-m)) for m in range(c-1)]
 return min(x[0] for x in ims),max(x[1] for x in ims)
WIDTH=2**512

def width_image(M,r,c,low,high):
 a,b,h,d=M
 lo,hi=span(r,c)
 top=abs(a*d-b*h)*SCALE**2
 return low*top//(h*hi+d*SCALE)**2,-(-high*top//(h*lo+d*SCALE)**2)

@cache
def widths(r,c):
 if not r:
  a,b=ends(c)
  return ((b-a)*WIDTH).__floor__(),((b-a)*WIDTH).__ceil__()
 ims=[width_image(edge(r,c,m),r-1,c-m,*widths(r-1,c-m)) for m in range(c-1)]
 return min(x[0] for x in ims),max(x[1] for x in ims)

def node(r,c,M,w):
 lo,hi=image(M,*span(r,c))
 wl,wh=width_image(M,r,c,*widths(r,c))
 return (lo,hi,r,c,M,w,wl,wh)
from functools import lru_cache
@lru_cache(maxsize=4096)
def children(n):
 lo,hi,r,c,M,w,_,_=n
 return tuple(node(r-1,c-m,mul(M,edge(r,c,m)),w+(m,)) for m in range(c-1))
def leaf(n):
 _,_,r,c,(a,b,h,d),w,_,_=n
 return tuple(sorted((a*z+b)/(h*z+d) for z in ends(c)))
def verify(r,c):
 roots=children(node(r,c,ID,()))
 stack=[(u,v) for i,u in enumerate(roots) for v in roots[:i]]
 overlaps=leaves=maxdepth=0
 while stack:
  u,v=stack.pop()
  if u[0]>v[1] or v[0]>u[1] or u[6]>v[7] or v[6]>u[7]:continue
  # A leaf's two actual endpoints lie within one dyadic rounding step of its
  # stored bounds only before the outer map. Compare exact endpoints if needed.
  if u[2]==v[2]==0:
   leaves+=1
   assert leaf(u)!=leaf(v),(r,c,u[5],v[5])
   continue
  overlaps+=1;maxdepth=max(maxdepth,len(u[5]),len(v[5]))
  if not u[2] or (v[2] and v[1]-v[0]>u[1]-u[0]):u,v=v,u
  stack.extend((ch,v) for ch in children(u) if ch[0]<=v[1] and v[0]<=ch[1] and ch[6]<=v[7] and v[6]<=ch[7])
 return overlaps,leaves,maxdepth
if __name__=='__main__':
 import sys,time
 if len(sys.argv)==3:
  r,c=map(int,sys.argv[1:]);t=time.monotonic();print(r,c,verify(r,c),time.monotonic()-t)
