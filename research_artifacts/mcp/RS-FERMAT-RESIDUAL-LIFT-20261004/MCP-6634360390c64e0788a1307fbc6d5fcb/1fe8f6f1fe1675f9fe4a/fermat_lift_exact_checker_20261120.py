# Exact integer checks for Fermat q-adic squaring and section changes
import json

def ds(x,q,n):
 a=x%q**n; d=[]
 for _ in range(n): d.append(a%q); a//=q
 return d

def lift(d,r,c,q):
 out=[]; carry=0
 for i,a in enumerate(d):
  v=(c if i==0 else 0)+2*r*a+sum(d[j]*d[i-1-j] for j in range(i))+carry
  digit=v%q; carry=(v-digit)//q; out.append(digit)
 return out

def one(x,q,k,t,u):
 r=(x+q//2)%q-q//2; r1=(x*x+q//2)%q-q//2
 A=(x-r)//q; c=(r*r-r1)//q
 nxt=lift(ds(A,q,k-1),r,c,q)
 assert nxt==ds((x*x-r1)//q,q,k-1)
 assert (r1+q*sum(v*q**j for j,v in enumerate(nxt)))%q**k==x*x%q**k
 rp=r+q*t; r1p=r1+q*u; Ap=A-t; cp=(rp*rp-r1p)//q
 nxtp=lift(ds(Ap,q,k-1),rp,cp,q)
 assert nxtp==ds((x*x-r1p)//q,q,k-1)
 assert (r1p+q*sum(v*q**j for j,v in enumerate(nxtp)))%q**k==x*x%q**k
 assert (sum(v*q**j for j,v in enumerate(nxtp))+u-sum(v*q**j for j,v in enumerate(nxt)))%q**(k-1)==0

n=0
for q in (3,5,9,17,25,41,641):
 for k in (2,3,4):
  for x in (-q*17-3,0,1,2,7,q-1,q,q*11+2,2**16,2**32):
   for t,u in ((0,0),(1,-2),(-2,3)):
    one(x,q,k,t,u);n+=1
cal={}
for p,j in ((5,1),(17,2),(257,3),(641,5)):
 X=2**(2**j);assert (X+1)%p==0
 h=(p-1)//2**(j+1); U=(X+1)//p
 Q=(pow(2,p-1,p**3)-1)//p
 assert Q%p==(-2*h*U)%p
 assert Q%(p*p)==(-2*h*U+p*(2*h*(2*h-1)//2)*U*U)%(p*p)
 cal[str(p)]=[U%p,U%(p*p),Q%p,Q%(p*p)]
assert cal['641'][0]==44
assert (5*1*1+4)%25==9 and 4%25!=9
assert 2%5==7%5 and 5%25!=50%25
print(json.dumps({'exact_checks':n,'calibrations':cal},sort_keys=True))