#!/usr/bin/env python3
"""D25 corrected-Clausen rank-one six-channel port and p-adic seam gauge.

Author-only exact arithmetic over Z/(p^r), standard library; external
hypergeometric auxiliary family. Not an original-class CM experiment.
"""
from math import isqrt


def inv(a, q):
    return pow(a % q, -1, q)


def primes(limit):
    return [p for p in range(7, limit + 1) if p % 6 == 1 and all(p % d for d in range(2, isqrt(p) + 1))]


def jets(p, q):
    m = (p - 1) // 6
    v = [[0] * p for _ in range(5)]
    v[0][0] = 1
    half_p = p * inv(2, q)
    for r in range(1, p):
        d = inv(r * (r - half_p), q)
        for a in range(5):
            x = (r - 1 - m) * (r - 1 - 2*m) * v[a][r - 1]
            if a:
                x += 3*r*v[a - 1][r] - (3*(r - 1) - 4*m)*v[a - 1][r - 1]
            if a >= 2:
                x += 2*v[a - 2][r - 1]
            v[a][r] = x * d % q
    return v


def original(p, q):
    # Original r_r=((1/6)_r(1/3)_r)/(2^r*(r!)^2).
    r = [0] * p
    r[0] = 1
    for k in range(p - 1):
        r[k + 1] = r[k]*(6*k+1)*(3*k+1)*inv(36*(k+1)**2, q) % q
    return r


def exact_source(p):
    m = (p-1)//6
    M = 2*m-1
    L = -M
    q = p**3
    u = jets(p, q)
    r = original(p, p**5)
    tau = -p * inv(6, q) % q
    lo = [(u[0][j] + tau*u[1][j] + tau*tau*u[2][j]) % q for j in range(2*m+1)]
    hi = [(u[2][j] + tau*u[3][j] + tau*tau*u[4][j]) % q for j in range(p)]
    # Independent ORIGINAL parameter-evaluation (one-stream recurrence)
    # check: F_j(-p/6)=2^j r_j, and high F_j/tau^2=36*2^j*r_j/p^2.
    for j in range(2*m+1):
        assert lo[j] == pow(2, j, q) * r[j] % q, (p,j,'low factor')
    for j in range(2*m+1, p):
        x = pow(2, j, p**5) * r[j] % p**5
        assert x % (p*p) == 0, (p,j,'high valuation')
        assert hi[j] == 36*(x//(p*p)) % q, (p,j,'high factor')
    M0 = [0] * (2*M + 1)
    M1 = [0] * (2*M + 1)
    bracket = 0
    endpoint = 0
    infinity = 0
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            n = ell - j
            a = lo[j] * hi[p-ell] % q
            k = n - L
            M0[k] = (M0[k] + a) % q
            M1[k] = (M1[k] + j*a) % q
            w = pow(2,n,q)
            val = (1 - 6*n + 6*p) * w * a
            endpoint = (endpoint + val) % q
            if ell <= j:
                bracket = (bracket + val) % q
            else:
                infinity = (infinity - val) % q
    assert (endpoint + infinity) % q == bracket
    half = inv(2,q)
    Y = {n:(M1[n-L]-(p-n)*half*M0[n-L])%q for n in range(L,M+1)}
    Y[M+1] = 0
    S = {n:((p-2*n)*Y[n]-(p-2*n-1)*Y[n+1]) % q for n in range(L,M+1)}
    AM = sum(pow(2,n,q)*M0[n-L] for n in range(L,M+1))%q
    KM = sum(pow(2,n,q)*M1[n-L] for n in range(L,M+1))%q
    WM = sum(pow(2,n,q)*Y[n] for n in range(L,M+1))%q
    assert endpoint == (AM+12*(KM-WM))%q, (p,'full-Laurent Ward')
    nu = {L-1:0}
    for n in range(L,0):
        nu[n] = (pow(2,n,q)+(p-2*n+1)*nu[n-1])*inv(p-2*n,q)%q
    Xi = (1+(p+1)*nu[-1])%q
    resonance = Xi%p==0
    a0 = Xi//p if resonance else 0
    omega = {n:nu[n] for n in range(L,0)}
    omega[0] = a0
    for n in range(1,M+1):
        omega[n] = (pow(2,n,q)+(p-2*n+1)*omega[n-1])*inv(p-2*n,q)%q
    source = sum(omega[n]*S[n] for n in range(L,M+1))%q
    defect = (Xi-p*a0)%q
    assert WM == (source+defect*Y[0])%q, (p,'seam gauge')
    assert bracket == (AM+12*KM-12*source-12*defect*Y[0]+infinity)%q

    # Original Q includes a separate ordered high-high population.
    q5=p**5
    s0=[0]*(p+1)
    s1=[0]*(p+1)
    for a in range(p-1,-1,-1):
        s0[a]=(s0[a+1]+r[a])%q5
        s1[a]=(s1[a+1]+a*r[a])%q5
    Q=sum(r[a]*((6*a+1)*s0[p-a]+6*s1[p-a]) for a in range(1,p))%q5
    assert Q%(p*p)==0
    Qnorm=(Q//(p*p))%q
    gam=pow(2,-p,q)*inv(18,q)%q
    high=[0]*p
    for a in range(2*m+1,p):
        high[a]=u[2][a]*pow(2,-a,p)%p
    h0=[0]*(p+1);h1=[0]*(p+1)
    for a in range(p-1,-1,-1):
        h0[a]=(h0[a+1]+high[a])%p
        h1[a]=(h1[a+1]+a*high[a])%p
    HH=sum(high[a]*((6*a+1)*h0[max(2*m+1,p-a)]+6*h1[max(2*m+1,p-a)]) for a in range(2*m+1,p))%p
    HHnorm=p*p*inv(1296,q)*HH%q
    assert Qnorm==(gam*bracket+HHnorm)%q, (p,'original ordered Q')
    return dict(p=p, q=q, m=m, L=L, M=M, u=u, Y=Y, S=S, Xi=Xi, a0=a0,
                resonance=resonance, source=source, W=WM, A=AM, K=KM,
                defect=defect, endpoint=endpoint, infinity=infinity,
                bracket=bracket, Qnorm=Qnorm, highhigh=HHnorm, gamma=gam,
                omega=omega)


def precision_witness(z):
    p=z['p']
    assert p==733 and z['resonance']
    q=p**3
    M,L=z['M'],z['L']
    big=p**4
    nu={L-1:0}
    for n in range(L,0):
        nu[n]=(pow(2,n,big)+(p-2*n+1)*nu[n-1])*inv(p-2*n,big)%big
    Xi_big=(1+(p+1)*nu[-1])%big
    assert Xi_big%p==0
    a_exact=Xi_big//p
    assert a_exact%p**2==z['a0']==187337
    assert a_exact==295158998
    d=(a_exact-z['a0'])//(p*p)
    assert d==549
    h={0:1}
    for n in range(1,M+1):
        h[n]=h[n-1]*(p-2*n+1)*inv(p-2*n,q)%q
    weighted=sum(h[n]*z['S'][n] for n in range(M+1))%q
    assert weighted==p*z['Y'][0]%q
    n0_change=(p*p*d*z['S'][0])%q
    pos_change=(p*p*d*sum(h[n]*z['S'][n] for n in range(1,M+1)))%q
    assert (n0_change,pos_change)==(p*p*403,p*p*(p-403))
    assert (n0_change+pos_change)%q==0
    assert z['S'][0]%p==440
    assert (z['Xi'],z['Y'][0],z['Qnorm'],z['bracket'])==(137318021,166585929,99531942,392689714)
    return dict(p=p, Xi_mod_p4=Xi_big, a0_mod_p3=a_exact,
                a0_mod_p2=z['a0'], hidden_digit=d, S0_mod_p=440,
                n0_delta=n0_change, positive_delta=pos_change,
                total_delta=0, W=z['W'], bracket=z['bracket'],
                original_Q_div_p2_mod_p3=z['Qnorm'], highhigh=z['highhigh'])


def main():
    ps=primes(211)+[733]
    assert len(ps)==23
    results=[exact_source(p) for p in ps]
    print('PASS',len(results),'target primes; rank-one six-channel source, original-Q and seam-gauge identities')
    for z in results:
        if z['p'] in (7,13,19,733):
            print('p',z['p'],'Xi',z['Xi'],'Y0',z['Y'][0], 'S0 mod p',z['S'][0]%z['p'],
                  'resonance',z['resonance'],'L3',z['bracket'],'Q/p2',z['Qnorm'])
    w=precision_witness(results[-1])
    print('p733 new seam precision witness:',w)

if __name__=='__main__':
    main()
