#!/usr/bin/env python3
"""R459 author-side signed BRC local PF3 certificate, exact Z[u] arithmetic.
Reuses R452 factorization with fixed legally-physical k0=(s+2)//2.
Independent condensation check a_s*P3_s=P2_s^2-P2_{s-1}*P2_{s+1}.
"""
import sys,time,json,hashlib
from math import comb,factorial

def add(*ps):
 n=max(map(len,ps));out=[0]*n
 for p in ps:
  for i,x in enumerate(p):out[i]+=x
 while len(out)>1 and out[-1]==0:out.pop()
 return out

def neg(p):return [-v for v in p]

def mul(a,b):
 if len(a)>len(b):a,b=b,a
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:z[i+j]+=x*y
 return z

def prod(ps):
 out=[1]
 for p in ps:out=mul(out,p)
 return out

def B(s,k0,F):
 if s<2:return [0]
 m=(s-1)//2
 E=prod([[2*(k0+1-s//2+j),2] for j in range(s)])
 O=prod([[2*k0+2*j+1,2] for j in range(s//2+1)])
 R=add(*[
  [comb(s-1,2*q)*(2**q)*v for v in prod([[2*k0-(2*t+1),2] for t in range(q,m)] + [[k0+1-d,1] for d in range(q)])]
  for q in range(m+1)])
 assert F%factorial(2*s)==0
 return [v*(F//factorial(2*s)) for v in prod([E,O,R])]

def H_raw(k,s):
 if not (2<=s<=2*k+1):return 0
 r=2*k+1;d=r-s
 def c(n,j):return comb(n,j) if 0<=j<=n else 0
 return comb(r+s,2*s)*sum(comb(d,q)*(c(2*s,r-2*q)-c(2*s,r-2*q-1)) for q in range(d+1))

def H_positive(k,s):
 if not(2<=s<=2*k+1):return 0
 r=2*k+1
 return comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*comb(2*(k-q),k-q)//(k-q+1) for q in range((s-1)//2+1))

def at(p,u):
 out=0
 for v in p[::-1]:out=out*u+v
 return out

def s_certificate(s,detail=False):
 ts=time.monotonic();k0=(s+2)//2;F=factorial(2*(s+2));p={t:B(t,k0,F) for t in range(s-2,s+3)}
 a,b,c,d,e=[p[s+i] for i in (0,-1,1,-2,2)]
 P2=add(mul(a,a),neg(mul(b,c)))
 P2low=add(mul(b,b),neg(mul(d,a)))
 P2high=add(mul(c,c),neg(mul(a,e)))
 # Direct determinantal 3x3 polynomial.
 P3=add(mul(mul(a,a),a),neg([2*x for x in mul(mul(b,a),c)]),mul(mul(d,c),c),mul(mul(b,b),e),neg(mul(mul(d,a),e)))
 assert len(P2)==4*s+1 and len(P3)==6*s+1
 assert min(P2)>0,(s,'P2',next(i for i,v in enumerate(P2) if v<=0))
 assert min(P3)>0,(s,'P3',next(i for i,v in enumerate(P3) if v<=0))
 # Exact Desnanot-Jacobi identity in Z[u] via independent factorization.
 assert mul(a,P3)==add(mul(P2,P2),neg(mul(P2low,P2high))),(s,'condensation')
 if detail:
  for k in [k0,k0+1]:
   for t in range(s-2,s+3):
    if t<2:continue
    v=at(p[t],k-k0)* (comb(2*k,k)//(k+1))
    assert v==F*H_raw(k,t),(s,k,t,'raw')
    assert H_raw(k,t)==H_positive(k,t),(s,k,t,'pos')
  print('RAW PASS',s,flush=True)
 h=hashlib.sha256()
 for order,P in ((2,P2),(3,P3)):
  h.update(bytes((order,)));h.update(len(P).to_bytes(2,'big'))
  for z in P:
   b=z.to_bytes((z.bit_length()+7)//8,'big')
   h.update(len(b).to_bytes(4,'big'));h.update(b)
 return {"s":s,"k0":k0,"r_min":2*k0+1,"degree_p2":len(P2)-1,"degree_p3":len(P3)-1,
         "strict_positive_coefficients":len(P2)+len(P3),"sha256":h.hexdigest(),"elapsed_seconds":round(time.monotonic()-ts,3)}

def main():
 lo=int(sys.argv[1]) if len(sys.argv)>1 else 101
 hi=int(sys.argv[2]) if len(sys.argv)>2 else 110
 rows=[]
 for s in range(lo,hi+1):
  row=s_certificate(s,detail=(s in [lo,hi]));rows.append(row)
  print(json.dumps(row),flush=True)
 result={"result":"R459_EXACT_PASS","s_range":[lo,hi],"verified_count":len(rows),"positive_coefficients":sum(x['strict_positive_coefficients'] for x in rows),"rows":rows,"method":"Positive integer coefficients in u=k-k0 for D2,D3; exact independent Desnanot-Jacobi polynomial identity; boundary raw signed BRC checks"}
 with open('R459_EVIDENCE.json','w') as f:json.dump(result,f,indent=2)
 print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2),flush=True)
if __name__=='__main__':main()
