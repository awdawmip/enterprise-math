"""Proved quadratic character-count theorem; finite sextic bucket symmetry check.
Universal algebraic criterion is proved; 77-prime sextic equality is NOT a universal proof.
"""
from math import comb, isqrt

def prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))

def run(p):
    assert p>3 and p%6==1 and prime(p)
    m=(p-1)//6
    sixth=[v for v in range(1,p) if pow(v,6,p)==1]
    assert len(sixth)==6
    counts={v:0 for v in sixth}
    pos=neg=0
    A=[0]*6
    for x in range(p):
        f=pow(x,5,p)*pow(x+1,2,p)*(2*x+1)%p
        v=pow(f,m,p)
        if v:
            counts[v]+=1
            eps=pow(v,3,p)
            if eps==1:pos+=1
            else:
                assert eps==p-1
                neg+=1
        for j in (1,3,5):
            A[j]=(A[j]+pow(v,j,p))%p
    assert pos+neg==p-3
    chi2=pow(2,(p-1)//2,p)
    eps2=1 if chi2==1 else -1
    assert pos-neg==-eps2-1
    assert A[3]==(-eps2-1)%p
    S=sum(comb(m,k)*comb(2*m+k,k) for k in range(m+1))%p
    assert A[1]==(-S)%p
    assert A[5]==pow(2,m,p)*A[1]%p
    exact_opposite=all(counts[v]==counts[-v%p] for v in sixth)
    assert (S==0 and eps2==-1)==(exact_opposite and eps2==-1)
    return p,eps2,pos,neg,S,exact_opposite,sorted(counts.items())

if __name__=="__main__":
    vals=[run(p) for p in range(7,2000) if p%6==1 and prime(p)]+[run(5113)]
    assert len(vals)==149
    inert=[v for v in vals if v[1]==-1]
    assert len(inert)==77 and all(v[5] for v in inert)
    print("PASS",len(vals),"quadratic balances,",len(inert),"inert finite sextic symmetries")
    for v in vals:
        if v[0] in (7,13,19,31,37,43,67,373,5113):print(v[:6])
