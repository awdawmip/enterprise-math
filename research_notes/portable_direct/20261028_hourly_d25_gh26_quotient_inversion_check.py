"""GH-26: exact phi-quotient character sum and inversion anti-invariance."""
from math import isqrt


def primes_under(limit):
    for p in range(11, limit):
        if all(p % d for d in range(2, isqrt(p)+1)):
            yield p


def chi(x,p):
    q=pow(x%p,(p-1)//2,p)
    return 0 if q==0 else (1 if q==1 else -1)


def check(p):
    m=(p-3)//8
    inv=lambda x:pow(x%p,-1,p)
    U=[x for x in range(p) if x*(x+1)*(9*x+1)%p]
    phi=lambda x:(9*x+1)*inv(9*x*(x+1))%p
    h=lambda x:chi(x,p)*pow(x*(x+1),3*m+1,p)*pow(9*x+1,m,p)%p
    fibers={v:[] for v in range(1,p)}
    for x in U:
        v=phi(x);fibers[v].append(x)
        assert h(x)==pow(9,m,p)*pow(v,m,p)*chi(1+x,p)%p,(p,x,'weight reduction')
    totals={v:sum(chi(1+x,p) for x in fibers[v]) for v in fibers}
    for v, xs in fibers.items():
        disc=(9*v*v-14*v+9)%p
        assert len(xs)==1+chi(disc,p),(p,v,'fiber count')
        vv=inv(v)
        assert totals[vv]==chi(v,p)*totals[v],(p,v,'inversion')
        if chi(v,p)==1:assert totals[v]==0,(p,v,'square cancellation')
        if chi(v,p)==-1 and xs:assert abs(totals[v])==len(xs),(p,v,'nonsquare equal chars')
    assert len(fibers[p-1])==0,(p,'v=-1 forbidden')
    full=sum(h(x) for x in U)%p
    reduced=pow(9,m,p)*sum(pow(v,m,p)*totals[v] for v in range(1,p))%p
    assert full==reduced
    reps=[v for v in range(1,p) if v<inv(v) and chi(v,p)==-1 and len(fibers[v])>0]
    pairparts=[(v,inv(v),len(fibers[v]),totals[v],pow(9,m,p)*((pow(v,m,p)-pow(inv(v),m,p))%p)*totals[v]%p) for v in reps]
    byinversion=sum(z[-1] for z in pairparts)%p
    assert byinversion==full,(p,'inversion quotient')
    return {'p':p,'pairs':pairparts,'S_F':full}


def main():
    n=0
    for p in primes_under(2000):
        if p%8==3:
            q=check(p);n+=1
            if p in (11,19,43):print('QUOTIENT_CERT',q)
    print('PASS_GH26_EXACT_POINTWISE_WEIGHT_COLLAPSE_AND_FIBER_DISCRIMINANT')
    print('PASS_GH26_INVERSION_ANTISYMMETRIC_QUOTIENT_MOMENT')
    print('target_primes_p_lt_2000:',n)

if __name__=='__main__':main()
