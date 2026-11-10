"""Author-side exact regression for original W216 p^3 observer-reflection theorem.
No external modules; no native H0/B0 experiment or Source admission.
"""
from math import comb, isqrt

def primes_upto(n):
    return [p for p in range(5,n+1)
            if all(p%d for d in range(2,isqrt(p)+1))]

def check_prime(p):
    mod, half, third = p**3, (p-1)//2, (p-1)//3
    a, entries = 1, []
    # Independent hypergeometric recurrence over every original source index.
    for k in range(p):
        entries.append(a)
        if k+1 < p:
            a = (a*(2*k+1)*(3*k+1)*(3*k+2)
                 * pow(36*(k+1)**3,-1,mod))%mod
    # Integer-binomial route for representative boundary/target primes.
    if p in (5,11,13,19,37,109,139,157,373,997):
        inv216=pow(216,-1,mod)
        for k,ak in enumerate(entries):
            other=comb(2*k,k)**2*comb(3*k,k)*pow(inv216,k,mod)%mod
            assert ak==other,(p,k,"original-coefficient")
    fac=[1]*p
    for i in range(1,p):
        fac[i]=fac[i-1]*i%p
    repair=[0]*5
    for k in range(third+1,half+1):
        assert entries[k]%p==0 and entries[k]%(p*p)!=0
        u=(-fac[2*k]*fac[3*k-p]*pow(216,-k,p)*pow(fac[k],-5,p))%p
        assert u==entries[k]//p%p,(p,k,"independent-p-unit")
        inv=pow(36*k**3*u,-1,p)
        for d in range(5):
            repair[d]=(repair[d]+pow(-k,d,p)*inv)%p
    full,low=[0]*5,[0]*5
    for k,ak in enumerate(entries):
        for d in range(5):
            term=pow(k,d,mod)*ak
            full[d]=(full[d]+term)%mod
            if k<=half:
                low[d]=(low[d]+term)%mod
    for d in range(5):
        assert (full[d]-low[d]-p*p*repair[d])%mod==0,(p,d)
    signed_full=(full[0]+6*full[1])%mod
    signed_low=(low[0]+6*low[1])%mod
    signed_repair=(repair[0]+6*repair[1])%p
    assert signed_full==(signed_low+p*p*signed_repair)%mod
    return dict(p=p,repair_moments=repair,
                signed_repair=signed_repair,
                signed_full=signed_full,signed_low=signed_low)

def main():
    rows=[check_prime(p) for p in primes_upto(997)]
    assert len(rows)==166
    assert sum(x["p"]%6==1 for x in rows)==80
    assert sum(x["p"]%6==5 for x in rows)==86
    for x in rows:
        if x["p"] in (5,11,13,19,109,139,157,373,997):
            print(x)
    print("PASS: 166 primes, 830 moment identities and 166 signed identities")

if __name__=="__main__":
    main()
