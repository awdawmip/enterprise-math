"""R273 exact algebra and finite integer replication, not a proof of the infinite theorem."""
from collections import defaultdict
import json
import sympy as S
u=S.symbols('u',nonzero=True); x=S.symbols('x'); p=(1+S.sqrt(5))/2
E={0:((2,-1,-1),(2,1,-1)),1:((0,-1,-1),(0,1,-1)),2:((1,1,1),(2,1,-1))}
C=[(q,z,e) for q,z in ((0,0),(1,1),(2,0),(2,1)) for e in (1,-1)]
F=[(q,e) for q in range(3) for e in (1,-1)]
def transfer(states,clean):
    ind={v:i for i,v in enumerate(states)};M=S.zeros(len(states))
    for v in states:
        q,e=v[0],v[-1]
        for bit in (0,1):
            if clean and v[1]==1 and bit==0:continue
            nq,eta,b=E[q][bit];ne=e*eta
            target=(nq,int(bit==0),ne) if clean else (nq,ne)
            M[ind[v],ind[target]]+=u**(ne*b)
    return M
A=transfer(C,True);D=transfer(F,False)
assert S.cancel(A.charpoly(x).as_expr()-(x*x+1)*(x**6-(u+1/u)*x**5+2*x*x-1))==0
assert S.cancel(D.charpoly(x).as_expr()-x*x*(x-u-1/u)*(x**3+x-u-1/u))==0
right=S.Matrix([1 if v[0]==0 or (v[0]==2 and v[1]==0) else 1/p for v in C])
left=S.Matrix([1 if v[0]==0 else p if v[0]==1 else p*p if v[1]==0 else 1/p for v in C])
assert (A.subs(u,1)*right-p*right).applyfunc(S.simplify)==S.zeros(8,1)
assert (left.T*A.subs(u,1)-p*left.T).applyfunc(S.simplify)==S.zeros(1,8)
assert S.simplify((left.T*right)[0]-10)==0
assert S.simplify(2*p**4/(6*p**5-10*p**4+4*p)-S.Rational(3,2)-7*S.sqrt(5)/10)==0
pi=S.Matrix([S.Rational(1,8) if v[0]<2 else S.Rational(1,4) for v in F])
assert pi.T*D.subs(u,1)==2*pi.T

def step(st,bit):
 q,r,e,k=st;nq,eta,b=E[q][bit]
 nr=2 if r==2 or r==1 and bit==0 else int(bit==0)
 return (nq,nr,e*eta,eta*k+b)
hist={(0,0,1,0):1};raw=0;matched=0;exceptions=[];at400={}
for n in range(401):
 assert sum(hist.values())==2**n
 assert all(k%2==n%2 for (_,_,_,k) in hist)
 if n<=12:
  naive=defaultdict(int)
  for w in range(2**n):
   st=(0,0,1,0)
   for j in range(n-1,-1,-1):st=step(st,(w>>j)&1)
   naive[st]+=1
  assert dict(naive)==hist;raw+=2**n
 bins=defaultdict(lambda:[0]*6);reset={}
 for (q,r,e,k),v in hist.items():
  bins[(e,k)][2*q+int(r==2)]+=v
  if q==0 and r==0:reset[(e,k)]=v
 B=max((min(y) for y in bins.values()),default=0);L=max(reset.values(),default=0)
 if n>=12:assert B==L,(n,B,L);matched+=1
 elif n>=7:assert B<L;exceptions.append([n,B,L])
 if n==400:at400={'effect':[list(g) for g,v in reset.items() if v==L],'peak':str(L)}
 nxt=defaultdict(int)
 for st,v in hist.items():
  for bit in (0,1):nxt[step(st,bit)]+=v
 hist=dict(nxt)
assert exceptions==[[7,1,2],[8,2,3],[9,2,4],[10,2,5],[11,5,6]]
print(json.dumps({'status':'PASS','clean_and_full_charpoly':'EXACT','eigenvectors_and_variance':'EXACT','raw_words':raw,'integer_depth':400,'finite_equalities_12_to_400':matched,'exceptions_7_to_11':exceptions,'at_400':at400,'universal_inference_from_finite_checks':False},ensure_ascii=False,indent=2))
