from collections import Counter, defaultdict
from itertools import product
from math import factorial
import json

A=(1,-1,2,-2)
def zof(w):
    z=[0]*6
    for v in w:z[abs(v)-1]+=1 if v>0 else -1
    return tuple(z)
def edges(w):return Counter(zip(w,w[1:]))
def sig(w,c):
    if c==0:return w[-1] if w else 0
    return (sig(w,c-1),sig(w[:-1],c-1) if w else None,sig(w[:-2],c-1) if len(w)>1 and w[-1]==-w[-2] else None)
def det(m):
    if not m:return 1
    a=[r[:] for r in m];prev=1;sgn=1
    for k in range(len(a)-1):
        if not a[k][k]:
            p=next((p for p in range(k+1,len(a)) if a[p][k]),None)
            if p is None:return 0
            a[k],a[p]=a[p],a[k];sgn=-sgn
        q=a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                x=a[i][j]*q-a[i][k]*a[k][j]
                assert x%prev==0
                a[i][j]=x//prev
            a[i][k]=0
        prev=q
    return sgn*a[-1][-1]
def euler(R,s,t):
    if not R:return int(s==t)
    out=Counter();inc=Counter();v={s,t}
    for (x,y),n in R.items():out[x]+=n;inc[y]+=n;v.update((x,y))
    if any(out[x]-inc[x]!=(x==s)-(x==t) for x in v):return 0
    v=sorted(v);sub=[x for x in v if x!=t]
    tau=det([[out[x]*(x==y)-R.get((x,y),0) for y in sub] for x in sub])
    if tau<=0:return 0
    N=tau
    for x in v:
        k=out[x]-1+(x==t)
        if k<0:return 0
        N*=factorial(k)
    D=1
    for n in R.values():D*=factorial(n)
    assert N%D==0
    return N//D
def transfer(J,z,m,C,alphabet=A):
    if m==0:return {sig((),C):1} if z==(0,)*6 and not J else {}
    k=min(m,2*C+1);out=Counter()
    for (x,y),n in J.items():out[x]+=n
    D=Counter()
    for u in product(alphabet,repeat=k):
        z0=[0]*6
        for x in alphabet:
            count=out[x]+(x==u[-1]);z0[abs(x)-1]+=count if x>0 else -count
        if tuple(z0)!=z:continue
        R=J.copy()
        for edge in zip(u,u[1:]):
            if not R.get(edge):break
            R[edge]-=1
            if not R[edge]:del R[edge]
        else:
            count=0
            if k==m:count=int(not R)
            else:
                for b in alphabet:
                    if not R.get((b,u[0])):continue
                    P=R.copy();P[(b,u[0])]-=1
                    if not P[(b,u[0])]:del P[(b,u[0])]
                    count+=sum(euler(P,s,b) for s in alphabet)
            if count:D[sig(u,C)]+=count
    return dict(D)
def main():
    checks=0;words=0
    for m in range(8):
        groups=defaultdict(Counter)
        for w in product(A,repeat=m):
            groups[(zof(w),tuple(sorted(edges(w).items())))][sig(w,2)]+=1
            words+=1
        for (z,E),expected in groups.items():
            assert transfer(Counter(dict(E)),z,m,2)==dict(expected)
            checks+=1
    fam=[tuple(-1 if j==r else 1 for j in range(1,9)) for r in range(2,8)]
    D=transfer(edges(fam[0]),zof(fam[0]),8,2,(1,-1))
    assert D==dict(Counter(sig(w,2) for w in fam)) and sorted(D.values())==[1,1,4]
    print(json.dumps(dict(status='STAGE399B_EULER_SUFFIX_TRANSFER_PASS',checked_words=words,checked_histogram_fibers=checks,stage398_fiber_size=sum(D.values()),stage398_q=len(D),stage398_multiplicities=sorted(D.values())),sort_keys=True))
if __name__=='__main__':main()
