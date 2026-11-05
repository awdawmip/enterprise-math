"""Exact author-side check of the diagonal low-digit/original-216 bridge.

The independent Pochhammer recurrence and signed Lucas harmonic/carry
expression are evaluated with exact integer modular arithmetic.
"""
from math import comb, isqrt, prod

def primes(hi):
    return [q for q in range(5, hi + 1)
            if all(q % d for d in range(2, isqrt(q) + 1))]

def original_216_sum(q):
    m = q*q
    t = 1
    total = 1
    for k in range(1, q):
        t = t*(2*k-1)*(3*k-2)*(3*k-1)*pow(36*k**3, -1, m) % m
        total = (total+(6*k+1)*t) % m
    return total

def low_digit_derived(q):
    m = q*q
    n = (q*q-1)//6
    N, r = divmod(n,q)
    s = [(i*r)%q for i in (2,3,4)]
    M = [i*N+(i*r)//q for i in (2,3,4)]
    a = -pow(2,-1,m)
    u = [pow(a,j,m)*prod(comb(x,j) for x in s) % m
         for j in range(min(s)+1)]
    L = sum((6*j+1)*v for j,v in enumerate(u)) % m
    H = [0]*q
    fac = [1]*q
    for j in range(1,q):
        H[j] = (H[j-1]+pow(j,-1,q)) % q
        fac[j] = fac[j-1]*j % q
    def tau(x,j):
        return (-1 if (j-x)%2==0 else 1)*fac[x]*fac[j-x-1]*pow(fac[j],-1,q)%q
    U = []
    K = []
    for i,x in enumerate(s):
        U.append(sum((6*j+1)*u[j]*(H[x]-H[x-j])
                     for j in range(len(u))) % q)
        K.append(sum((6*j+1)*pow(a,j,q)*tau(x,j) *
                     prod(comb(s[t],j) for t in range(3) if t!=i)
                     for j in range(x+1, min(s[t] for t in range(3)
                                           if t!=i)+1)) % q)
    phi = (pow(2,q-1,m)-1)//q
    Ac = sum(M[i]*(U[i]+K[i]) for i in range(3)) % q
    A = (2*N*phi*L+Ac) % q
    bridge = (L+q*Ac) % m
    return L,A,Ac,bridge,s,M,K

if __name__ == "__main__":
    ps = primes(1200)
    for q in ps:
        W = original_216_sum(q)
        L,A,Ac,bridge,s,M,K = low_digit_derived(q)
        assert W == bridge, (q,W,bridge)
        if W % q == 0:
            assert L % q == 0
            assert (L//q+A-W//q) % q == 0
    for q in [5,7,11,13,17,19,23,29,31,37,43,373]:
        W = original_216_sum(q)
        L,A,Ac,bridge,s,M,K = low_digit_derived(q)
        print(q,"W mod q^2=",W,"W/q mod q=",W//q,
              "lambda=",L//q,"A=",A,"carry=",K,"bridge=",bridge)
    print("PASS",len(ps),"primes, low-digit original-216 congruence mod q^2")
