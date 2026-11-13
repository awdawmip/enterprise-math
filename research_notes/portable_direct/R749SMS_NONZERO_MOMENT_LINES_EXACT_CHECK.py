# R749SMS: exact finite basis/endpoint checker, Python 3 stdlib only.
from fractions import Fraction as F
from itertools import combinations
import json
C=(1,2,4,8,15); B=tuple(i for i in range(1,16) if i not in C)
ch=lambda a,x: 1-2*((a&x).bit_count()%2)
def solve(A,b):
 n=len(b); T=[[F(v) for v in r]+[F(z)] for r,z in zip(A,b)]
 for k in range(n):
  j=next((j for j in range(k,n) if T[j][k]),None)
  if j is None:return None
  T[k],T[j]=T[j],T[k]; z=T[k][k]; T[k]=[v/z for v in T[k]]
  for j in range(n):
   if j!=k and T[j][k]:
    z=T[j][k]; T[j]=[v-z*w for v,w in zip(T[j],T[k])]
 return [r[-1] for r in T]
def tv(mu,q):
    return sum(max(x-y,F(0)) for x,y in zip(mu,q))
def run(kind):
 if kind=='C':
  rows=[[1]*16]+[[ch(a,x) for x in range(16)] for a in C]
  k=6; b0=[1,0,0,0,0,0];b1=[1,1,0,0,0,0];character=1;bound=F(3,4)
 else:
  rows=[[ch(a,x) for a in C] for x in range(16)]
  k=5;b0=None;b1=None;character=3;bound=F(1,2)
 hits=non=feasible=0;knots=set();maxrisk=F(0)
 for S in combinations(range(16),k):
  A=[[r[x] for x in S] for r in rows] if kind=='C' else [rows[x] for x in S]
  v=solve(A,b0 if kind=='C' else [-1]*5)
  if v is None:continue
  non+=1
  w=solve(A,b1 if kind=='C' else [-1-ch(character,x) for x in S])
  w=[y-x for x,y in zip(v,w)]
  lo,hi=F(-1),F(1)
  linear=[(v[i],w[i]) for i in range(k)] if kind=='C' else [(1+sum(v[j]*rows[x][j] for j in range(5)),ch(character,x)+sum(w[j]*rows[x][j] for j in range(5))) for x in range(16)]
  for a,b in linear:
   if b>0:lo=max(lo,-a/b)
   elif b<0:hi=min(hi,-a/b)
   elif a<0:lo=F(2)
  if lo>hi:continue
  feasible+=1
  for t in {lo,hi}:
   q=[(1+t*ch(character,x))/16 for x in range(16)]
   if kind=='C':
    p=[F(0)]*16
    for x,a,b in zip(S,v,w):p[x]=a+t*b
   else:
    z=[v[j]+t*w[j] for j in range(5)]
    p=[(1+t*ch(character,x)+sum(z[j]*rows[x][j] for j in range(5)))/16 for x in range(16)]
   assert min(p)>=0 and sum(p)==1
   val=tv(p,q)
   assert val<=bound
   maxrisk=max(maxrisk,val);hits+=1;knots.add(t)
 return dict(nonsingular=non,feasible_segments=feasible,endpoint_tests=hits,knots=sorted(str(v) for v in knots),max_endpoint_risk=str(maxrisk))
def main():
 a,b=run('C'),run('B')
 assert (a['nonsingular'],a['feasible_segments'],a['endpoint_tests'],set(a['knots']),a['max_endpoint_risk'])==(4048,3568,5376,{'-1','-1/3','0','1/3','1'},'3/4')
 assert (b['nonsingular'],b['feasible_segments'],b['endpoint_tests'],set(b['knots']),b['max_endpoint_risk'])==(3008,2288,2816,{'-1','-1/2','0','1/2','1'},'1/2')
 return dict(schema='R749SMS_ONE_CHARACTER_LINE_RISK_V1',status='PASS',C_line=a,B_line=b,all_real_t='[-1,1]',basis_coverage={'C':8008,'B':4368},scope='exact rational endpoint verification plus analytic four/two disjoint lower witnesses')
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
