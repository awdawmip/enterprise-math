"""Exact independent W216 scale/diagonal certificates, author-side 2026-11-10.

No floating point; inversions occur only on p-units.
Run: python3 d25_w216_diagonal_target_primes_20261110.py
"""

def p_unit_and_val(x: int, p: int):
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return x, v


def ratio_path(p: int, rmax: int = 3, d: int = 4):
    """Original A[k+1]/A[k] ratio, retaining coefficient valuation and unit."""
    mod = p ** (3 * rmax + d)
    targets = {p ** r: r for r in range(1, rmax + 1)}
    N = p ** rmax
    unit, val, total = 1, 0, 0
    out = {0: 1}
    inv36 = pow(36, -1, mod)
    for k in range(N):
        if val < 0:
            raise AssertionError('negative p-adic coefficient valuation')
        if val < 3 * rmax + d:
            total = (total + (6 * k + 1) * unit * pow(p, val, mod)) % mod
        if k + 1 in targets:
            out[targets[k+1]] = total
        if k + 1 == N:
            break
        a, va = p_unit_and_val(2*k+1, p)
        b, vb = p_unit_and_val(3*k+1, p)
        c, vc = p_unit_and_val(3*k+2, p)
        den, vd = p_unit_and_val(k+1, p)
        val += va + vb + vc - 3*vd
        unit = unit * a * b * c * inv36 * pow(den, -3, mod) % mod
    return out, mod


def factorial_path(p: int, rmax: int = 3, d: int = 4):
    """Independent p-unit factorial expression A[k]=(2k)!(3k)!/(k!)^5/216^k."""
    mod = p ** (3 * rmax + d)
    N = p ** rmax
    targets = {p ** r: r for r in range(1, rmax + 1)}
    f1 = f2 = f3 = if1 = inv216pow = 1
    v1 = v2 = v3 = 0
    total = 0
    out = {0: 1}
    inv216 = pow(216, -1, mod)
    for k in range(N):
        val = v2 + v3 - 5*v1
        if val < 0:
            raise AssertionError('negative p-adic factorial valuation')
        if val < 3 * rmax + d:
            unit = f2 * f3 * pow(if1, 5, mod) * inv216pow % mod
            total = (total + (6*k+1)*unit*pow(p, val, mod)) % mod
        if k+1 in targets:
            out[targets[k+1]] = total
        if k+1 == N:
            break
        a = k+1
        v = 0
        while a % p == 0:
            a//=p
            v+=1
        v1+=v
        f1=f1*a % mod
        if1=if1*pow(a, -1, mod) % mod
        for t in (2*k+1, 2*k+2):
            a,v=p_unit_and_val(t,p)
            f2=f2*a % mod
            v2+=v
        for t in (3*k+1,3*k+2,3*k+3):
            a,v=p_unit_and_val(t,p)
            f3=f3*a % mod
            v3+=v
        inv216pow=inv216pow*inv216 % mod
    return out, mod


def witnesses(p: int, rmax: int = 3, d: int = 4):
    w1, mod = ratio_path(p,rmax,d)
    w2, mod2 = factorial_path(p,rmax,d)
    assert mod == mod2 and w1 == w2, f'Independent W mismatch p={p}'
    chi = 1 if p%3==1 else -1
    e = {}
    for r in range(1,rmax+1):
        diff = (w1[r]-chi*p*w1[r-1])%mod
        assert diff%p**(3*r)==0,(p,r,'defect not divisible')
        e[r]=diff//p**(3*r)%p**d
    transitions=[]
    for r in range(1,rmax):
        delta=(e[r+1]-e[r])%(p**(r+1))
        if delta%p**r==0:
            transitions.append(dict(r=r,digit=delta//p**r,val_at_least_r=True))
        else:
            transitions.append(dict(r=r,difference_mod=delta,val_at_least_r=False))
    return dict(p=p,length=p**rmax,rmax=rmax,precision=3*rmax+d,
                W=w1,E=e,transitions=transitions)


if __name__ == '__main__':
    expect = {
        109: dict(E={1:64750664,2:90905868,3:48728318}, delta=47),
        139: dict(E={1:100717108,2:124405627,3:151397064}, delta=7),
    }
    for p, check in expect.items():
        row = witnesses(p)
        assert row['E'] == check['E'], (p,'E mismatch',row['E'])
        assert [x['digit'] for x in row['transitions']] == [check['delta']]*2
        print(row, flush=True)
