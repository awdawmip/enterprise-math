"""Exact p-local Ward seam resonance certificate; standard library only.

Auxiliary corrected-Clausen Ward algebra, not native CM or a formal proof.
"""
from math import comb


def target_primes(limit=997):
    return [p for p in range(7, limit + 1) if p % 6 == 1 and all(p % d for d in range(2, int(p**0.5) + 1))]


def inv(x, q):
    return pow(x % q, -1, q)


def weight(n, q):
    return pow(2, n, q)


def check(p):
    m = (p - 1) // 6
    M, L, N = 2 * m - 1, 1 - 2 * m, 2 * m - 1
    q = p * p
    # Left-Dirichlet forward adjoint; p-unit denominators only.
    nu = {}
    nu[L - 1] = 0
    for n in range(L, 0):
        nu[n] = ((weight(n, q) + (p - 2*n + 1) * nu[n-1]) * inv(p - 2*n, q)) % q
    rho_star = (nu[-1] + inv(p+1, q)) % q
    G = inv(p + 2*M, q)
    for t in range(M-1, 0, -1):
        G = G * (p + 2*t+1) * inv(p+2*t, q) % q
    delta_from_seam = rho_star * inv(G, q) % q
    # Independent right-Dirichlet (predecessor) negative adjoint.
    lam = {0: 0}
    for n in range(0, L, -1):
        lam[n-1] = ((p-2*n)*lam[n] - weight(n, q)) * inv(p-2*n+1, q) % q
    delta_from_left = (weight(L, q) - (p-2*L)*lam[L]) % q
    assert delta_from_seam == delta_from_left
    # Independent finite-binomial tangent in the formal parameter p.
    A, c, h = inv(p+2, q), inv(2, q), -inv(2, q) % q
    rho0, rho1, half = 1, -1, inv(2, q)
    for t in range(1, M+1):
        if t > 1:
            A = A * (p+2*t-1) * inv(p+2*t, q) % q
            c = c * (2*t-1) * inv(2*t, q) % q
            h = (h + inv(2*t-1, q) - inv(2*t, q)) % q
            half = half * inv(2, q) % q
        rho0 = (rho0 + half*c) % q
        rho1 = (rho1 + half*c*h) % q
    assert A == G
    assert rho_star == (rho0 + p*rho1) % q
    tangent = ((rho0 + p*(rho1-h*rho0)) * inv(c, q)) % q
    assert tangent == delta_from_left
    assert (delta_from_left % p == 0) == (rho0 % p == 0)
    assert c % p != 0
    # Genuine seam residual, as a functional on an arbitrary labeled Y.
    y = {n: (n*n + 17*n + 11) % q for n in range(L, N+1)}
    y[N+1] = 0
    source = {n: ((p-2*n)*y[n] - (p-2*n-1)*y[n+1]) % q for n in range(L, N+1)}
    left_observer = sum(weight(n,q)*y[n] for n in range(L,1)) % q
    seam_factor = (1 + (p+1)*nu[-1]) % q
    assert seam_factor == (p+1)*rho_star % q
    left_source = (sum(nu[n]*source[n] for n in range(L,0)) + seam_factor*y[0]) % q
    assert left_observer == left_source
    # Globally p-integral source-only telescoper iff the seam defect is divisible by p.
    if rho0 % p == 0:
        global_nu = dict(nu)
        global_nu[0] = seam_factor // p
        for n in range(1, N+1):
            global_nu[n] = ((weight(n,q) + (p-2*n+1)*global_nu[n-1])*inv(p-2*n,q)) % q
        for n in range(L,N+1):
            lhs = (p-2*n)*global_nu[n] - ((p-2*n+1)*global_nu[n-1] if n>L else 0)
            assert lhs % q == weight(n,q)
        assert sum(global_nu[n]*source[n] for n in range(L,N+1)) % q == sum(weight(n,q)*y[n] for n in range(L,N+1)) % q
    else:
        assert seam_factor % p != 0
    return dict(p=p, M=M, rho0=rho0, rho1=rho1, rho_star=rho_star,
                G=G, delta=delta_from_left, seam_factor=seam_factor,
                global_unit_telescoper=(rho0 % p == 0))


def check_third_digit_seam(p):
    """Third-digit omega_0, independently checked against inherited delta second p-jet."""
    M, L, q = (p - 1)//3 - 1, -((p - 1)//3 - 1), p**3
    nu = {L-1: 0}
    for n in range(L, 0):
        nu[n] = (weight(n,q) + (p-2*n+1)*nu[n-1])*inv(p-2*n,q)%q
    rho = (nu[-1] + inv(p+1,q))%q
    xi = (p+1)*rho%q
    assert xi%p==0
    omega0 = xi//p
    # Right-boundary adjoint algebraically independent of left-Dirichlet recursion.
    lam = {0: 0}
    for n in range(0,L,-1):
        lam[n-1] = ((p-2*n)*lam[n]-weight(n,q))*inv(p-2*n+1,q)%q
    delta = (weight(L,q)-(p-2*L)*lam[L])%q
    # Consume the predecessor's independent finite Gauss second p-jet.
    D=[0]*(M+1); L2=[0]*(M+1); b=[1]*(M+1)
    for t in range(1,M+1):
        D[t]=(D[t-1]+inv(t,q)-inv(2*t-1,q)-inv(2*t,q))%q
        L2[t]=(L2[t-1]+inv(2*t-1,q)**2-inv(2*t,q)**2)%q
        b[t]=b[t-1]*(2*t-1)*inv(4*t,q)%q
    P=pow(4,M,q)*inv(comb(2*M,M),q)%q
    total=0
    for t in range(M+1):
        d=(D[M]-D[t])%q
        correction=(1+p*d+p*p*inv(2,q)*(d*d+L2[M]-L2[t]))%q
        total=(total+b[t]*correction)%q
    assert delta==P*total%q
    if p==733:
        assert (rho,xi,delta,omega0)==(304414900,137318021,7698699,187337)
    return rho,xi,delta,omega0


if __name__ == '__main__':
    ps = target_primes()
    results = [check(p) for p in ps]
    assert len(results) == 80
    resonances = [a['p'] for a in results if a['global_unit_telescoper']]
    assert resonances == [733]
    r13 = next(x for x in results if x['p'] == 13)
    r733 = next(x for x in results if x['p'] == 733)
    assert (r13['rho_star'], r13['delta']) == (48, 47)
    assert (r733['rho0'], r733['rho1'] % 733, r733['rho_star'], r733['G'], r733['delta'], r733['seam_factor'] % (733*733)) == (157595, 207, 309326, 475737, 176653, 309326)
    assert r733['rho_star']//733 == 422
    assert r733['delta']//733 == 241
    print('PASS', len(ps), 'target primes; resonance candidates within p<=997:', resonances)
    print('p13 rho*=48 delta=47 (mod 169): no p-integral global seam adjoint')
    print('p733 rho0=733*215, rho1=207 (mod 733), G0=20, rho*/733=422, delta/733=241')
    assert check_third_digit_seam(733)==(304414900,137318021,7698699,187337)
    print('p733: constructed full-rank integral adjoint modulo 733^2; third-digit omega0=187337 mod 733^2')
