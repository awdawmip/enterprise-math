        raise ValueError("negative Gaussian exponent")
    out = (1, 0)
    base = z
    k = e
    while k:
        if k & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        k >>= 1
    return out

def gnorm(z: Gaussian) -> int:
    return z[0]*z[0] + z[1]*z[1]

def tonelli_shanks(n: int, p: int) -> int:
    n %= p
    if n == 0:
        return 0
    if p == 2:
        return n
    if pow(n, (p-1)//2, p) != 1:
        raise ValueError("not a quadratic residue")
    if p % 4 == 3:
        r = pow(n, (p+1)//4, p)
        return min(r, p-r)
    q = p-1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p-1)//2, p) != p-1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q+1)//2, p)
    while t != 1:
        i = 1
        t2 = (t*t) % p
        while i < m and t2 != 1:
            t2 = (t2*t2) % p
            i += 1
        if i == m:
            raise ArithmeticError("Tonelli-Shanks invariant failure")
        b = pow(c, 1 << (m-i-1), p)
        r = (r*b) % p
        t = (t*b*b) % p
        c = (b*b) % p
        m = i
    return min(r, p-r)

@lru_cache(maxsize=None)
def split_prime_gaussian(p: int) -> Gaussian:
    if p <= 2 or p % 4 != 1:
        raise ValueError("p == 1 mod 4 required")
    t0 = tonelli_shanks(p-1, p)
    for t in sorted({t0, p-t0}):
        r0, r1 = p, t
        while r1*r1 > p:
            r0, r1 = r1, r0 % r1
        x = abs(r1)
        y2 = p - x*x
        y = isqrt(y2)
        if y*y == y2:
            a, b = sorted((x, y), reverse=True)
            if b > 0 and a*a + b*b == p:
                return (a, b)
    raise ArithmeticError(f"Cornacchia failed for {p}")

def gaussian_prime_typing(N: int) -> Dict[str, object]:
    factors = factor_integer(N)
    rows: List[Dict[str, object]] = []
    for p, e in sorted(factors.items()):
        if p == 2:
            rows.append({"prime": p, "exponent": e, "type": "RAMIFIED", "gaussian_prime": [1, 1]})
        elif p % 4 == 1:
            pi = split_prime_gaussian(p)
            rows.append({
                "prime": p, "exponent": e, "type": "SPLIT",
                "pi": list(pi), "pi_conjugate": list(gconj(pi)),
                "allocation_range": [0, e],
            })
        else:
            rows.append({
                "prime": p, "exponent": e, "type": "INERT",
                "requires_even_exponent": True,
                "fixed_integer_gaussian_exponent_if_supported": e//2,
            })
    return {
        "N": N,
        "integer_factorization": factor_rows(N),
        "prime_typing": rows,
        **support_reason(factors),
    }

def gaussian_signed_root_channels(N: int, detailed: bool = False) -> Tuple[Dict[Gaussian, List[Dict[str, object]]], Dict[str, object]]:
    """DISCOVERY primitive: UFD exponent allocation only; no target coordinate scan."""
    meta = gaussian_prime_typing(N)
    if not meta["supported"]:
        return {}, meta
    factors = factor_integer(N)
    base: Gaussian = (1, 0)
    split: List[Tuple[int, int, Gaussian]] = []
    for p, e in sorted(factors.items()):
        if p == 2:
            base = gmul(base, gpow((1, 1), e))
        elif p % 4 == 1:
            split.append((p, e, split_prime_gaussian(p)))
        else:
            base = gmul(base, (p ** (e//2), 0))
    ranges = [range(e+1) for _, e, _ in split]
