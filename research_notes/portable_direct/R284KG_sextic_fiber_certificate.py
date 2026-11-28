from math import factorial, prod, isqrt
from fractions import Fraction as F
import numpy as np

def sextic(d):
    return (((((64*d-61)*d+13)*d+61)*d-29)*d)*d+16

def mul(a,b):return a[0]*b[0],a[0]*b[1]+a[1]*b[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,n):return a[0]*n,a[1]*n
def scaled(v,s,d):
    tail=[(1,0)]*(d+1)
    for k in range(d-1,-1,-1):tail[k]=mul(tail[k+1],(v+k+3,s))
    z=(1,0);out=[]
    for k in range(d+1):
        out.append(mul(z,tail[k]));z=mul(z,(v-k,s))
    return tail[0],out

def jet(d):
    Du,U=scaled(0,1,d); Dn,N=scaled(-d,2,d)
    V=Q=A=(0,0)
    for k in range(d+1):
        l=d-k
        a=scale(mul(U[k],N[l]),(k+1)*(l+1))
        b=scale(mul(U[k],N[l-1]),(k+1)*l) if l else (0,0)
        V=add(V,a);Q=add(Q,b)
        A=add(A,mul((-k*(k+2),2),add(a,b)))
    J=(0,2);L=(2-4*d,8);q=(-d,1)
    W=add(mul(L,A),scale(mul(mul(mul(mul((0,1),U[d]),Dn),q),(2-d,2)),2*d+3))
    Qn=mul(mul(J,L),Q);Zn=mul(L,add(mul(q,A),mul(J,add(Q,V))))
    assert W[0]==Qn[0]==Zn[0]==0
    B=factorial(d+2)//2*((-1)**d)*factorial(2*d-1)//factorial(d-1)
    assert V[0]==(d+1)*B and Q[0]==F(-2*d*B,2*d-1) and A==(0,2*(d+1)*B)
    coef=-3*d*(d-1)**2*W[1]*Qn[1]-32*(1-2*d)*Zn[1]**2
    assert coef==F(8*L[0]**2*B**2*sextic(d),2*d-1)>0
    assert 0<sextic(d)<64*d**6
    return coef

for d in range(3,301):jet(d)
print('exact integer jet identities: d=3..300 (298)')
# exact exhaustive large prime count within KD bracket for d=3001..3100
lo_d,hi_d=3001,3100
max_b=4*hi_d**2//3+hi_d
mask=np.ones(max_b+1,dtype=bool);mask[:2]=False
for p in range(2,isqrt(max_b)+1):
    if mask[p]:mask[p*p::p]=False
pr=np.flatnonzero(mask).astype(np.int64)
initial=large=survivors=0;maxsurv=0;maxp=0;rows=[]
for d in range(lo_d,hi_d+1):
    a=(4*d*d+4)//5+d;b=4*d*d//3+d
    lower=2*d+2
    pp=pr[np.searchsorted(pr,lower+1):np.searchsorted(pr,b+1)]
    cnt=0
    # each n in [a,b] has at most one such prime, so exact sum counts distinct integers
    for t in range(1,b//(lower+1)+1):
        cnt+=max(0,int(np.searchsorted(pr,b//t+1)-np.searchsorted(pr,max(lower+1,(a+t-1)//t))))
    # Horner mod p in int64 (all multiplications bounded by d*max_b+64)
    z=np.full(pp.shape,64,dtype=np.int64)
    for c in [-61,13,61,-29,0,16]:z=(z*d+c)%pp
    ex=pp[z==0];ss=sum(b//int(p)-(a-1)//int(p) for p in ex)
    assert len(ex)<=5 and ss<=cnt
    initial+=b-a+1;large+=cnt;survivors+=ss;maxsurv=max(maxsurv,ss);maxp=max(maxp,len(ex))
    rows.append((d,cnt,ss,[int(p) for p in ex]))
print(dict(domain=[lo_d,hi_d],initial=initial,large_prime_budgets=large,excluded=large-survivors,remaining_large_prime_budgets=survivors,max_remaining_per_d=maxsurv,max_eligible_exception_primes=maxp))
print('examples',rows[:5]);print('all rows',rows)
