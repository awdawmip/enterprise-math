# Exact small-prime subgroup-orbit certificate for auxiliary rank-two K=[B,A].
# Does not execute original H0/B0.
from collections import defaultdict
P=(3,5,7,11,13,17)
def divs(n): return [h for h in range(1,n+1) if n%h==0]
def mul(x,y,p,d): return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def power(x,n,p,d):
    r=(1,0)
    while n:
        if n&1:r=mul(r,x,p,d)
        x=mul(x,x,p,d);n//=2
    return r
def verify(X,H,act,key,expected):
    fib=defaultdict(set)
    for x in X:fib[key(x)].add(x)
    used=set()
    for x in X:
        if x in used:continue
        orb={act(h,x) for h in H}
        assert orb==fib[key(x)]
        used|=orb
    assert used==set(X) and len(fib)==expected
    return len(fib)
total=0
for p in P:
    X=[(a,b) for a in range(p) for b in range(p)]
    g=next(i for i in range(2,p) if len({pow(i,k,p) for k in range(p-1)})==p-1)
    for h in divs(p-1):
        H=[pow(g,(p-1)//h*j,p) for j in range(h)]
        verify(X,H,lambda s,x:(s*x[0]%p,pow(s,-1,p)*x[1]%p),lambda x:(pow(x[0],h,p),pow(x[1],h,p),x[0]*x[1]%p),1+(p*p-1)//h);total+=1
    d=next(i for i in range(2,p) if i not in {(j*j)%p for j in range(p)})
    z=next(power((a,b),p*p-p,p,d) for a,b in X if (a,b)!=(0,0) and len({power(power((a,b),p*p-p,p,d),j,p,d) for j in range(p+1)})==p+1)
    for h in divs(p+1):
        H=[power(z,(p+1)//h*j,p,d) for j in range(h)]
        verify(X,H,lambda s,x:mul(s,x,p,d),lambda x:power(x,h,p,d),1+(p*p-1)//h);total+=1
    for H in ((0,),tuple(range(p))):
        h=len(H)
        key=(lambda x:(x[0],x[1])) if h==1 else (lambda x:(x[1],x[0]*(1-pow(x[1],p-1,p))%p))
        verify(X,H,lambda c,x:((x[0]+2*c*x[1])%p,x[1]),key,p+p*(p-1)//h);total+=1
print('PASS',total,'subgroup orbit/complete-label cases, p=',P)
