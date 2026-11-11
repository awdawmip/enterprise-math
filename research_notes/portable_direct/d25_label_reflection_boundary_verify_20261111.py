#!/usr/bin/env python3
"""Direct exact verification of D25 second-label reflection and orphan weighted BRC ports."""
def primes(n):
    s=bytearray([1])*(n+1);s[0]=s[1]=0
    for k in range(2,int(n**.5)+1):
        if s[k]:s[k*k:n+1:k]=bytes((n-k*k)//k+1)
    return (p for p in range(7,n+1) if s[p])
def inv(x,p):return pow(x%p,-1,p)
def check(p):
    eps=0 if p%6==1 else 1;m=(p-1-4*eps)//6
    N=-inv(pow(2,2*m+eps,p),p)%p
    def T(t):return -2*(t+1)*inv(t+2,p)%p
    labels={};seen=set()
    for t in range(p):
        if t in (0,p-1,p-2) or t in seen:continue
        v=T(t);O={t,v};assert T(v)==t
        seen.update(O);lam=(t+v)%p;assert lam not in labels
        A=B=0
        for x in O:
            U=(x+1)*(x+2)**2*inv(x,p)%p
            V=pow(U,m,p)*pow(x+2,eps,p)%p
            w=(2-12*eps-(3+10*eps)*x)*inv(x+2,p)%p
            A=(A+N*V)%p;B=(B+N*V*w)%p
        labels[lam]=(A,B,tuple(sorted(O)))
    orphan=(-7)%p
    assert (-1)%p not in labels and orphan in labels
    assert labels[orphan][2]==tuple(sorted({-3%p,-4%p}))
    q=pow(2*inv(3,p),m,p);s=pow(3,m,p)
    a=N*((-1)**eps*q+(-2)**eps*s)%p
    b=-N*((11+18*eps)*(-1)**eps*q+(7+14*eps)*(-2)**eps*s)%p
    assert (a,b)==labels[orphan][:2]
    paired=fixed=0;visited={orphan};totA=totB=0
    for lam in labels:
        if lam in visited:continue
        other=(-8-lam)%p
        assert other in labels
        assert ((lam+4)**2-8)%p==((other+4)**2-8)%p
        for k in {lam,other}:
            totA+=labels[k][0];totB+=labels[k][1];visited.add(k)
        if other==lam:
            assert lam==(-4)%p;fixed+=1
        else:paired+=1
    assert len(visited)==len(labels)
    assert (totA+a)%p==sum(x[0] for x in labels.values())%p
    assert (totB+b)%p==sum(x[1] for x in labels.values())%p
    assert bool(fixed)==(pow((-2)%p,(p-1)//2,p)==1)
    return len(labels),paired,fixed
if __name__=="__main__":
    count=labels=pairs=fixed=0
    for p in primes(2500):
        a,b,c=check(p);count+=1;labels+=a;pairs+=b;fixed+=c
    assert (count,labels,pairs,fixed)==(364,210031,104745,177)
    print({"primes":count,"orbit_labels":labels,"S_pairs":pairs,"S_fixed":fixed,"orphan":count,"status":"PASS"})
