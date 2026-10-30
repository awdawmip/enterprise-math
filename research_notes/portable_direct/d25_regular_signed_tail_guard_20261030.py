"""D25 A216 regular signed tier-2 port; exact original-integer regression."""
from math import comb, factorial, isqrt


def primes(limit):
    a = bytearray(b'\x01') * limit
    a[:2] = b'\x00\x00'
    for n in range(2, isqrt(limit - 1) + 1):
        if a[n]:
            a[n*n:limit:n] = b'\x00' * (1 + (limit-1-n*n)//n)
    return (p for p in range(7, limit) if a[p] and p % 6 == 1)


def hreg(p):
    m = (p-1)//6
    x, total = 1, 0
    for s in range(m):
        total = (total + (6*s+4)*x) % p
        d = 9*(2*s+3)**3
        assert d % p
        if s+1 < m:
            x = x*(6*s+7)*(6*s+5)*(s+1)*pow(d, -1, p) % p
        else:
            assert (6*s+7) == p  # next coefficient terminates, no pole
    return total


def original(p, direct=False):
    mod = p**3; m = (p-1)//6
    a, w, low, middle = 1, 0, 0, 0
    for n in range(p):
        if direct:
            a = comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod) % mod
        z = (6*n+1)*a % mod
        w = (w+z) % mod
        if n<=3*m: low=(low+z)%mod
        elif n<=4*m: middle=(middle+z)%mod
        if not direct and n+1 < p:
            a = a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod) % mod
    return w, low, middle


def main():
    count=targets=0
    for p in primes(1500):
        m=(p-1)//6; mod=p**3
        H=hreg(p)
        eps=pow(p-2,(p-1)//2,p)
        assert eps in (1,p-1)
        scale=eps*pow(9,-1,p)%p
        fact_scale=(-m*factorial(3*m)*factorial(2*m)*factorial(4*m) *
            pow(6*2**(3*m+1)*factorial(3*m+1)**3,-1,p))%p
        assert scale==fact_scale
        q=scale*H%p
        W, low, mid=original(p)
        assert mid==p*p*q%mod
        assert (W-low-mid)%mod==0
        assert (low-p)%(p*p)==0
        J=((low-p)%mod)//(p*p)
        assert (J+q)%p==0 and (W-p)%mod==0
        if p%24 in (13,19): targets+=1
        count+=1
        if p in (7,13,19,31,37,43,373):
            assert original(p,True)==(W,low,mid)
            print('P',p,'epsilon',1 if eps==1 else -1,
                  'D',scale,'Hreg',H,'A_mid_over_p2',q,'J',J,'LIFT', (J+q)%p)
    assert (count,targets)==(115,60)
    print('PASS_D25_REGULAR_SIGNED_TERMINATING_PORT',count,'TARGET',targets)

if __name__=='__main__': main()
