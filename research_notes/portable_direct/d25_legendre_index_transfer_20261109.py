#!/usr/bin/env python3
"""D25 Legendre p-block identity: exact integer and quadratic-ring checks."""
from math import comb
import json

def P(n,x,p):
 a=(x-1)%p;b=(x+1)%p
 s=sum(comb(n,k)**2*pow(a,k,p)*pow(b,n-k,p) for k in range(n+1))%p
 return s*pow(pow(2,n,p),-1,p)%p

def P_quadratic(n,t,p):
 def mul(u,v):
  return ((u[0]*v[0]+2*u[1]*v[1])%p,(u[0]*v[1]+u[1]*v[0])%p)
 neg=(-1,t);pos=(1,t);mn=[(1,0)];pl=[(1,0)]
 for k in range(n):
  mn.append(mul(mn[-1],neg));pl.append(mul(pl[-1],pos))
 acc=(0,0)
 for k in range(n+1):
  x=mul(mn[k],pl[n-k]);c=comb(n,k)**2
  acc=((acc[0]+c*x[0])%p,(acc[1]+c*x[1])%p)
 h=pow(pow(2,n,p),-1,p)
 return (acc[0]*h%p,acc[1]*h%p)

if __name__=="__main__":
 ps=[5,13,29,37,61,109];count=0;special=[]
 for p in ps:
  for q in sorted({0,1,(p-1)//4,p-2,p-1}):
   for t in (0,1,2,3,5):
    v0=P(p+q,t,p);v1=P(2*p-q-1,t,p);v2=pow(t,p,p)*P(q,t,p)%p
    assert v0==v1==v2,(p,q,t,v0,v1,v2)
    count+=1
 for p in ps+[373]:
  q=(p-1)//4;t=2*pow(3,-1,p)%p
  a=P_quadratic(p+q,t,p);b=P_quadratic(2*p-q-1,t,p)
  c=P_quadratic(q,t,p)
  # -t*T*(c0+c1*T) = -2t*c1-t*c0*T in ring T^2=2
  rhs=(-2*t*c[1]%p,-t*c[0]%p)
  assert a==b==rhs,(p,a,b,c,rhs)
  special.append({'p':p,'q':q,'J_a_mod_p':a,'J_b_mod_p':b,'P_q_mod_p':c})
 print(json.dumps({'schema':'D25_LEGENDRE_PBLOCK_V1','general_tests':count,
                   'quadratic_ring_tests':len(special),'all_passed':True,'special':special},indent=2))
