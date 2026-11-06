"""Exact p-adic Gauss-port deformation; independent original216 checking."""
from math import comb, factorial, isqrt

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def check(p):
    assert p > 3 and p % 6 == 1 and prime(p)
    m = (p-1)//6
    q = p*p
    zq = pow(2, -1, q)
    zp = pow(2, -1, p)
    harm = [0] * (2*m+1)
    for j in range(1, 2*m+1):
        harm[j] = (harm[j-1] + pow(j,-1,p)) % p
    S = sum(comb(m,k)*comb(2*m+k,k) for k in range(m+1))
    T = sum(k*comb(m,k)*comb(2*m+k,k) for k in range(m+1))
    B = (1-12*m)*S + 24*T
    D = sum(comb(m,k)*comb(2*m,k)*pow(zq,k,q) for k in range(m+1)) % q
    assert D == S * pow(pow(2,m,q),-1,q) % q
    low = 0
    for k in range(m+1):
        d = comb(m,k)*comb(2*m,k) % p
        delta = (- (harm[m]-harm[m-k])*pow(6,-1,p)
                 - (harm[2*m]-harm[2*m-k])*pow(3,-1,p)) % p
        low = (low + d*pow(zp,k,p)*delta) % p
    middle = 0
    fact = [factorial(j) % p for j in range(2*m+1)]
    for k in range(m+1,2*m+1):
        c = ((-1)**(m+k) *fact[m]*fact[k-m-1]*fact[2*m]
             *pow(6*fact[2*m-k]*fact[k]**2,-1,p)) % p
        middle = (middle + c*pow(zp,k,p)) % p
    C = (low + middle) % p
    u = 1
    direct_u = []
    F = theta = 0
    for k in range(p):
        direct_u.append(u)
        term = u*pow(zq,k,q) % q
        F = (F+term)%q
        theta = (theta+k*term)%q
        if k<p-1:
            u = u*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,q)%q
    E = (F+12*theta)%q
    a = 1
    W = 0
    for k in range(p):
        W = (W+(6*k+1)*a)%q
        if k<p-1:
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,q)%q
    assert W == F*E%q, (p,'Clausen mod p^2',W,F*E%q)
    for k in range(m+1):
        d=comb(m,k)*comb(2*m,k)%q
        assert (direct_u[k]-d)%p == 0
        delta = (- (harm[m]-harm[m-k])*pow(6,-1,p)
                 - (harm[2*m]-harm[2*m-k])*pow(3,-1,p)) % p
        assert ((direct_u[k]-d)%q)//p == (d*delta)%p, (p,k,'low')
    for k in range(m+1,2*m+1):
        c = ((-1)**(m+k) *fact[m]*fact[k-m-1]*fact[2*m]
             *pow(6*fact[2*m-k]*fact[k]**2,-1,p)) % p
        assert (direct_u[k]%q)//p == c, (p,k,'middle')
    for k in range(2*m+1,p):
        assert direct_u[k]%q == 0,(p,k,'high')
    assert F==(D+p*C)%q,(p,F,D,C)
    assert E%p== B*pow(2,-m,p)%p
    if S%p == 0:
        fquot = F//p
        assert fquot%p == (pow(2,-m,q)*(S%q)//p+C)%p
        uD=(-(S//p)*pow(4*T,-1,p))%p
        assert (S//p+4*T*uD)%p == 0
        predicted_fquot = (C-4*T*uD*pow(2,-m,p))%p
        assert fquot%p==predicted_fquot
        second = (fquot*(E%p))%p
        assert W%p==0 and W//p%p==second
        return (p,'D',S%q,T%p,uD,low,middle,C,fquot%p,E%p,second)
    return (p,'E',S%q,T%p,None,low,middle,C,None,E%p,None)

if __name__ == '__main__':
    vals = [check(p) for p in range(7, 2000) if p%6==1 and prime(p)]
    assert len(vals)==148
    extra=check(5113)
    target=[v for v in vals if v[0]%24 in (13,19)]
    assert len(target)==77
    assert all(v[1]=='D' and v[-1]==1 for v in target)
    print('PASS 148 p<=1999 plus 5113; target 77 second-digit defects=0')
    for v in vals+[extra]:
        if v[0] in (13,19,31,67,373,5113): print(v)
