"""Different direct constructions for the CM norm-jet and its precision boundary."""
from fractions import Fraction as F
from math import comb, isqrt
import json


def evaluate(coeffs, y, mod):
    total = 0
    for a in reversed(coeffs):
        total = (total * y + a) % mod
    return total


def coeffs(m, mod):
    scale = pow(2, -2*m, mod)
    return [(-1)**(m-r)*comb(2*m, m-r)*comb(2*m+2*r, 2*m)*scale % mod
            for r in range(m+1)]


def raw_ports(p, mod):
    b = c = 1
    g = h = w = 0
    for k in range(p):
        g += b
        h += (12*k+1)*b
        w += (6*k+1)*c
        if k+1 < p:
            b = b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2, -1, mod) % mod
            c = c*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3, -1, mod) % mod
    return g % mod, h % mod, w % mod


def sun(p, mod):
    half = pow(2, -1, mod)
    # B(t) = sum (1/3)_k (2/3)_k / k!^2 * ((1-t)/2)^k, t^2=1/2.
    u = prod0 = 1
    v = summed0 = summed1 = 0
    for k in range(p):
        summed0 += prod0*u
        summed1 += prod0*v
        if k+1 < p:
            u, v = (u-v*half)*half % mod, (v-u)*half % mod
            prod0 = prod0*(3*k+1)*(3*k+2)*pow(9*(k+1)**2, -1, mod) % mod
    return summed0 % mod, summed1 % mod


def exact_fraction_check(p):
    # Use the ordinary three-term Legendre recurrence over Q[x]; no binomial row.
    prev, cur = [F(1)], [F(0), F(1)]
    for j in range(1, (p-1)//3):
        nxt = [F(0)]*(len(cur)+1)
        for i, a in enumerate(cur):
            nxt[i+1] += (2*j+1)*a/(j+1)
        for i, a in enumerate(prev):
            nxt[i] -= j*a/(j+1)
        prev, cur = cur, nxt
    a = cur[::2]
    q = sum(v/F(2)**r for r,v in enumerate(a))
    deriv = sum(r*v/F(2)**(r-1) for r,v in enumerate(a) if r)
    norm = sum(u*v/(F(2)**(i+j)*(2*i+2*j+1)) for i,u in enumerate(a) for j,v in enumerate(a))
    defect = 18*q*deriv-p*(2*norm+3)
    mod = p**3
    return (str(q), str(deriv), str(norm), str(defect),
            defect.numerator*pow(defect.denominator,-1,mod) % mod)


def check(p):
    assert p%24 in (13,19) and all(p%j for j in range(2, isqrt(p)+1))
    n, m, mod = (p-1)//3, (p-1)//6, p**3
    y = pow(2,-1,mod)
    a = coeffs(m,mod)
    da = [r*a[r] % mod for r in range(1,m+1)]
    q, dq = evaluate(a,y,mod), evaluate(da,y,mod)
    square = [0]*(2*m+1)
    for i,v in enumerate(a):
        for j,u in enumerate(a):
            square[i+j] += v*u
    norm = evaluate([v*pow(2*r+1,-1,mod) % mod for r,v in enumerate(square)],y,mod)
    assert q%p == 0 and dq%p != 0
    g,h,w = raw_ports(p, mod)
    assert g%p == 0 and h%p == -6*dq % p
    assert w % (p*p) == g*h % (p*p) == p
    b0,b1 = sun(p,mod)
    assert b1 % (p*p) == 0 and b0%(p*p) == g%(p*p)
    assert (6*b0*dq+p)%(p*p) == 0
    defect = (18*q*dq-p*(2*norm+3)) % mod
    assert defect%(p*p) == 0
    yp = pow(2,-1,p*p)
    root = (yp - p*(2*norm+3)*pow(18*dq*dq,-1,p)) % (p*p)
    assert evaluate(a,root,p*p) == 0 and root%p == yp%p
    # The divided norm-jet as an actual polynomial in z=x².
    def at_z(z):
        prim = evaluate([v*pow(2*r+1,-1,mod) % mod for r,v in enumerate(square)],z,mod)
        return (18*evaluate(a,z,mod)*evaluate(da,z,mod)-p*(2*prim+3))%mod
    assert all((at_z(yp+p*k)-p*k*18*dq**2)%(p*p) == 0 for k in (0,1,p-1))
    ans = {'p':p,'m':m,'Q_over_p_mod_p':q//p%p,'Qprime_mod_p':dq%p,
           'I_over_t_mod_p':norm%p,'G_div_mod_p':g//p%p,
           'epsilon_mod_p':(18*(q//p)*dq-2*norm-3)%p,
           'next_norm_jet_digit':defect//(p*p),'Q_root_mod_p2':root}
    if p<=19:
        u,v,en,d,z = exact_fraction_check(p)
        assert z == defect
        ans['exact_rationals']={'Q':u,'Qprime':v,'I_over_t':en,'undivided_norm_jet_over_t':d}
    return ans


if __name__ == '__main__':
    print(json.dumps([check(p) for p in (13,19,2029,2083)], indent=2))
