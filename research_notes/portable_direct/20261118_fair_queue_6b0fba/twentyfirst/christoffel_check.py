"""Exact dyadic operator bounds and modular AP Laplacian certificates (NumPy)."""
import hashlib
import json
from fractions import Fraction as F
from math import comb, factorial, isqrt, prod

import numpy as np


def c(m, j, layer):
    z = m * j + m * m * layer
    return F(factorial(m - 1), prod(z + r for r in range(1, m + 1)))


def translation_bounds(m):
    """Exact upper bound of Euclidean operator norm using row and column sums."""
    n = m - 1
    norms = [0, 1]
    total = [[int(i == j) for i in range(m)] for j in range(m)]
    for s in range(2, n + 1):
        for j in range(m):
            z = j + m * (s - 1)
            # Interpolating polynomials on 0,...,n at an integer z>n.
            for i in range(m):
                total[j][i] += (-1)**(n-i) * comb(z, i) * comb(z-i-1, n-i)
        rows = max(sum(map(abs, row)) for row in total)
        cols = max(sum(abs(row[i]) for row in total) for i in range(m))
        squared = rows * cols
        ceiling = isqrt(squared)
        norms.append(ceiling + (ceiling**2 < squared))
    return norms


def radius(m):
    n = m - 1
    w = [(-1)**j * comb(n, j) for j in range(m)]
    weight = [c(m, j, 1)/c(m, 0, 1) for j in range(m)]
    delta = sum(wj / u for wj, u in zip(w, weight))
    assert delta == (-1)**n * c(m, 0, 1) * m**m * F(3*m*m+1, 2)
    k = max(F(1), (max(1 / abs(wj * u) for wj, u in zip(w, weight))
                    + sum(1 / u**2 for u in weight) / abs(delta)) / n)
    norms = translation_bounds(m)
    # Use each exact layer diagonal norm, including the first.
    layers = [comb(n, s) * max(abs(wj) * c(m, j, s) / c(m, 0, 1)
                              for j, wj in enumerate(w)) for s in range(1, m)]
    for exponent in range(1, 19*m+1):
        z = F(1, 2**exponent)
        r = z*z
        error = layers[0]*(r+2*z) + sum(layers[s-1] * r**(s-1)*(z+norms[s])**2
                                         for s in range(2, m))
        if k*error < 1:
            return {"m":m, "radius_power_of_two":-2*exponent,
                    "ceiling_of_one_million_times_K_error":(10**6*k*error).__ceil__()}
    raise AssertionError("universal radius did not certify")


def endpoints_mod(m, p):
    n, b = m-1, m*m
    # Factorials below p are sufficient, since p>m^3.
    fac = [1]
    for j in range(1, m**3+1):
        fac.append(fac[-1]*j % p)
    lead_part = pow(n, n, p) * pow(m, n*(n+3)+m, p) % p
    c0 = lead_part * prod(comb(n,j)**2 % p for j in range(m)) * pow(fac[n], 2*m, p) % p
    h0 = c0 * (3*b+1) * pow(2*fac[2*b], -1, p) % p
    ratio = ((2*n-1)*b+1) * fac[2*b] * fac[(n-1)*b] % p
    ratio = ratio * pow((3*b+1)*fac[(n+1)*b], -1, p) % p
    return [h0, (-1)**(n*(2*m-3)) * h0 * ratio % p]


def determinant_batch(matrix, inverses, p):
    count, size, _ = matrix.shape
    rows = np.arange(count)
    value = np.ones(count, dtype=np.int64)
    for k in range(size):
        pivot = k + np.argmax(matrix[:,k:,k] != 0, axis=1)
        old = matrix[:,k,:].copy()
        matrix[:,k,:] = matrix[rows,pivot,:]
        matrix[rows,pivot,:] = old
        diag = matrix[:,k,k]
        value = value * np.where(pivot == k, diag, -diag) % p
        if k+1 < size:
            scale = matrix[:,k+1:,k] * inverses[diag,None] % p
            matrix[:,k+1:,k+1:] = (matrix[:,k+1:,k+1:] -
                scale[:,:,None] * matrix[:,None,k,k+1:]) % p
    return value


def newton_coefficients(values, d, p):
    """Interpolate d+1 values at 0,...,d in the ordinary power basis."""
    column = np.array(values[:d+1], dtype=np.int64)
    fac, diffs = 1, []
    for k in range(d+1):
        if k:
            fac = k*fac % p
        diffs.append(int(column[0])*pow(fac,-1,p) % p)
        column = np.diff(column) % p
    poly = np.array(diffs[-1:], dtype=np.int64)
    for k in reversed(range(d)):
        out = np.zeros(len(poly)+1, dtype=np.int64)
        out[1:] = poly
        out[:-1] -= k*poly
        out[0] += diffs[k]
        poly = out % p
    points = np.arange(p, dtype=np.int64)
    evaluated = np.zeros(p, dtype=np.int64)
    for coefficient in reversed(poly):
        evaluated = (evaluated*points+coefficient) % p
    assert evaluated.tolist() == values[:-1] and poly[-1] == values[-1]
    return poly


def gcd_degree(a, b, p):
    def trim(x):
        nz = np.flatnonzero(x)
        return x[:nz[-1]+1] if len(nz) else x[:0]
    a, b = trim(a), trim(b)
    while len(b):
        inv = pow(int(b[-1]), -1, p)
        for k in reversed(range(len(a)-len(b)+1)):
            a[k:k+len(b)] = (a[k:k+len(b)] - (int(a[k+len(b)-1])*inv % p)*b) % p
        a, b = b, trim(a)
    return len(a)-1


def degrees(poly, p, cutoff):
    """Distinct-degree Frobenius gcds and possible small rational-factor degrees."""
    f = poly * pow(int(poly[-1]), -1, p) % p
    d = len(f)-1
    assert d*p*p < 2**62  # convolution coefficients fit int64
    inverse_reverse = np.ones(d, dtype=np.int64)
    rev = f[::-1]
    for i in range(1,d):
        inverse_reverse[i] = -int(np.dot(rev[1:i+1], inverse_reverse[:i][::-1])) % p
    def mul(a,b):
        product = np.convolve(a,b) % p
        high = product[d:][::-1]
        quotient = (np.convolve(high, inverse_reverse)[:len(high)] % p)[::-1]
        return (product[:d] - np.convolve(quotient, f)[:d]) % p
    x = np.zeros(d, dtype=np.int64)
    x[1] = 1
    h = x.copy()
    derivative = f[1:] * np.arange(1,d+1) % p
    squarefree = gcd_degree(f.copy(), derivative.copy(), p) == 0
    counts = {}
    for k in range(1,cutoff+1):
        base, power, result = h, p, np.zeros(d, dtype=np.int64)
        result[0] = 1
        while power:
            if power % 2:
                result = mul(result,base)
            power //= 2
            if power:
                base = mul(base,base)
        h = result
        shared = gcd_degree(f.copy(), (h-x) % p, p)
        new = shared - sum(e*v for e,v in counts.items() if k % e == 0)
        assert new >= 0 and new % k == 0
        if new:
            counts[k] = new//k
    possible = {0}
    for e,count in counts.items():
        for _ in range(count if squarefree else cutoff//e):
            possible.update(k+e for k in list(possible) if k+e <= cutoff)
    return {"squarefree":squarefree, "irreducible_counts_through_cutoff":counts,
            "possible_factor_degrees_through_cutoff":sorted(possible-{0})}


def projective_test(m, p, cutoff=12):
    """Projective q on (a:1) in residue order followed by (1:0)."""
    assert p > m**3 and p < 1_000_000
    n = m-1
    win = [(-1)**i * comb(n, i) % p for i in range(m)]
    inv = np.array([0] + [pow(j, -1, p) for j in range(1, p)], dtype=np.int64)
    coefficients = np.array([[[win[i]*win[j]*win[s]*pow(i+1+m*j+m*m*s, -1, p) % p
        for j in range(m)] for i in range(m)] for s in range(m)], dtype=np.int64)
    q0, qd = endpoints_mod(m, p)
    values = [q0]
    for start in range(1, p, 128):
        points = np.arange(start, min(start+128, p), dtype=np.int64)
        size = len(points)
        edges = np.zeros((size, m, m), dtype=np.int64)
        for layer in reversed(coefficients):
            edges = (edges * points[:,None,None] + layer[None,:,:]) % p
        lap = np.zeros((size, 2*m-1, 2*m-1), dtype=np.int64)
        lap[:,range(m),range(m)] = edges.sum(axis=2) % p
        lap[:,range(m,2*m-1),range(m,2*m-1)] = edges.sum(axis=1)[:,:-1] % p
        lap[:,:m,m:] = -edges[:,:,:-1] % p
        lap[:,m:,:m] = -edges[:,:,:-1].transpose((0,2,1)) % p
        vals = determinant_batch(lap, inv, p).tolist()
        values.extend(v * pow(int(t), -n, p) % p for v,t in zip(vals,points))
    values.append(qd)
    poly = newton_coefficients(values, n*(2*m-3), p)
    return {"m":m, "p":p, **degrees(poly,p,cutoff), "endpoints":[q0,qd], "projective_roots":values.count(0),
            "sha256_csv_q_on_0_to_p_minus_1_then_infinity":hashlib.sha256(
                ",".join(map(str,values)).encode("ascii")).hexdigest()}


def main():
    prime_sets = {11:[1373,1381],12:[1753,1759],13:[2203,2207],
                  14:[2749,2753,2767],15:[3391,3407,3413,3433],
                  16:[4099,4111,4127,4129]}
    certificates = []
    for m, primes in prime_sets.items():
        d = (m-1)*(2*m-3)
        common = set(range(1,d//2+1))
        records = []
        for p in primes:
            assert all(p % j for j in range(2,isqrt(p)+1))
            record = projective_test(m,p,d//2)
            possible = record.pop("possible_factor_degrees_through_cutoff")
            common &= set(possible)
            record["remaining_possible_rational_degrees"] = sorted(common)
            records.append(record)
        assert not common and records[0]["projective_roots"] == 0
        certificates.append({"m":m, "degree":d, "primes":records})
    print(json.dumps({"dyadic_bounds":[radius(m) for m in range(2,21)],
                      "modular_checks":certificates}, indent=2))


if __name__ == "__main__":
    main()
