"""Exact rational Schur trace and independent graph determinant checks (Python 3)."""
import json
from fractions import Fraction as Q
from math import comb, factorial, isqrt, lcm, prod


def weights(m):
    return [(-1)**j * comb(m - 1, j) for j in range(m)]


def layer(m, s):
    # Keep the left vertex block and suppress the last right vertex.
    n = m - 1
    w = weights(m)
    A, G, C = [Q(0)]*m, [[Q(0)]*n for _ in range(m)], [Q(0)]*n
    if s >= 0:
        for i in range(m):
            for j in range(m):
                edge = Q(w[i]*w[j]*w[s], 1 + i + m*j + m*m*s)
                A[i] += edge
                if j < n:
                    G[i][j] -= edge
                    C[j] += edge
    return A, G, C


def trace_solve(B, rhs):
    """Gauss elimination on B X = rhs, returning tr(X)."""
    n = len(B)
    a = [row[:] + more[:] for row, more in zip(B, rhs)]
    for j in range(n):
        i = next(i for i in range(j, n) if a[i][j])
        a[j], a[i] = a[i], a[j]
        v = a[j][j]
        a[j] = [x / v for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                v = a[i][j]
                for k in range(j, 2*n):
                    a[i][k] -= v*a[j][k]
    return sum(a[i][n+i] for i in range(n))


def vieta(m):
    n = m-1
    a, g, _ = layer(m, n)
    lift = [[-x / a[i] for x in row] for i, row in enumerate(g)]

    def blocks(s):
        diag, cross, right = layer(m, s)
        C = [[cross[i][j] + diag[i]*lift[i][j] for j in range(n)]
             for i in range(m)]
        B = [[(right[j] if j == k else 0)
              + sum(lift[i][j]*C[i][k] + cross[i][j]*lift[i][k]
                    for i in range(m))
              for k in range(n)] for j in range(n)]
        return diag, C, B

    _, C0, B0 = blocks(n)
    assert not any(x for row in C0+B0 for x in row)
    diag, C, B = blocks(n-1)
    _, _, B2 = blocks(n-2)
    G = [[B2[j][k] - sum(C[i][j]*C[i][k]/a[i] for i in range(m))
          for k in range(n)] for j in range(n)]
    return -sum(x/y for x, y in zip(diag, a)) - trace_solve(B, G)


def integer_det(rows):
    a = [row[:] for row in rows]
    sign, prev = 1, 1
    for k in range(len(a)-1):
        i = next((i for i in range(k, len(a)) if a[i][k]), None)
        if i is None:
            return 0
        if i != k:
            a[k], a[i] = a[i], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                a[i][j], rem = divmod(a[i][j]*pivot - a[i][k]*a[k][j], prev)
                assert not rem
        prev = pivot
    return sign*a[-1][-1]


def determinant_from_edges(m, edge):
    mat = [[0]*(2*m-1) for _ in range(2*m-1)]
    for i in range(m):
        for j in range(m):
            v = edge(i,j)
            mat[i][i] += v
            if j < m-1:
                r = m+j
                mat[r][r] += v
                mat[i][r] -= v
                mat[r][i] -= v
    return integer_det(mat)


def interpolate_positive(vals, mod=None):
    """Power coefficients from values at 1,2,... via forward differences."""
    coeff, basis = [0]*len(vals), [1]
    for k in range(len(coeff)):
        if mod is None:
            digit, rem = divmod(vals[0], factorial(k))
            assert not rem
        else:
            digit = vals[0]*pow(factorial(k), -1, mod) % mod
        for j, x in enumerate(basis):
            coeff[j] += digit*x
        new = [0] + basis
        for j,x in enumerate(basis):
            new[j] -= (k+1)*x
        basis = new if mod is None else [x % mod for x in new]
        vals = [b-a for a,b in zip(vals,vals[1:])]
        if mod is not None:
            vals = [x % mod for x in vals]
    return coeff if mod is None else [x % mod for x in coeff]


def top_coefficient(m):
    # Archived endpoint formula (21), including the signed normalization.
    n, b = m-1, m*m
    D = n*(2*m-3)
    q0 = Q(n**n*m**(n*(n+3)+m)*factorial(n)**(2*m)*(3*b+1)
           *prod(w*w for w in weights(m)), 2*factorial(2*b))
    return q0*Q((-1)**D*n*n*(2*m+1), (3*b+1)*comb(m**3, 2*b))


def full_coefficients(m):
    n, w = m-1, weights(m)
    den = lcm(*range(1, m**3+1))
    D = n*(2*m-3)
    def eval_at(t):
        cs = [w[s]*t**s for s in range(m)]
        def edge(i,j):
            return w[i]*w[j]*sum(x*(den//(1+i+m*j+m*m*s))
                                  for s,x in enumerate(cs))
        v, rest = divmod(determinant_from_edges(m, edge), t**n)
        assert not rest
        return v
    raw = interpolate_positive([eval_at(t) for t in range(1, D+2)])
    assert sum(c*(-1)**j for j,c in enumerate(raw)) == eval_at(-1)
    out = [Q(c, den**(2*m-1)) for c in reversed(raw)]
    assert out[0] == top_coefficient(m)
    return out


def valuation(x, p):
    if x == 0:
        return float("inf")
    x = Q(x)
    def order(i):
        k = 0
        while i % p == 0:
            i //= p
            k += 1
        return k
    return order(x.numerator) - order(x.denominator)


def mod_q(x, mod):
    x = Q(x)
    return x.numerator*pow(x.denominator, -1, mod) % mod


def primes_above(start, stop):
    return [p for p in range(start+1, stop+1)
            if all(p%j for j in range(2, isqrt(p)+1))]


def reverse_modular(m, p):
    """p^J q*(y) modulo p^(J+1), directly from the full unreduced graph."""
    n, w, size = m-1, weights(m), 2*m-1
    J, D = m**3//p, n*(2*m-3)
    mod, high = p**(J+1), p**(size+1)
    assert p > 2*m*m and J <= size and D+2 < p
    def den_coeff(i,j,s):
        z = 1+i+m*j+m*m*s
        return (1 if z%p == 0 else p)*pow(z//p if z%p == 0 else z,
                                             -1, high)*w[i]*w[j]*w[s] % high
    table = [[[den_coeff(i,j,s) for s in range(m)] for j in range(m)]
             for i in range(m)]
    def eval_at(y):
        powers = [pow(y, n-s, high) for s in range(m)]
        det = determinant_from_edges(m, lambda i,j:
                sum(x*v for x,v in zip(powers,table[i][j])) % high)
        c, r = divmod(det % high, p**(size-J))
        assert not r
        return c*pow(y, -n, mod) % mod
    vals = [eval_at(i) for i in range(1, D+2)]
    co = interpolate_positive(vals, mod)
    assert sum(c*pow(D+2,k,mod) for k,c in enumerate(co)) % mod == eval_at(D+2)
    assert co[0] == mod_q(p**J*top_coefficient(m), mod)
    return co, J


def newton_certificate(m, p):
    coeff, J = reverse_modular(m,p)
    # Unknown terms have v_p >= 1. As the initial height is <= 0, these
    # cannot affect any descending edge.
    pts = [(k,int(valuation(c,p))-J) for k,c in enumerate(coeff) if c]
    hull = []
    for k,v in pts:
        while len(hull)>=2:
            i,a = hull[-2]
            j,b = hull[-1]
            if (v-b)*(j-i) > (b-a)*(k-j):
                break
            hull.pop()
        hull.append((k,v))
    falling = [hull[0]]
    for left,right in zip(hull,hull[1:]):
        if right[1] >= left[1]:
            break
        falling.append(right)
    residuals = []
    for (a,u),(b,v) in zip(falling,falling[1:]):
        slope = Q(u-v,b-a)
        step, drop = slope.denominator,slope.numerator
        # y^step / p^drop is the residue variable for this side.
        res = [coeff[k]//(p**(J+u-drop*((k-a)//step)))%p
               for k in range(a,b+1,step)]
        roots = [x for x in range(1,p) if
                 sum(c*pow(x,i,p) for i,c in enumerate(res))%p == 0]
        residuals.append(dict(negative_valuation_magnitude=str(slope),
                              root_count=b-a, coefficients=res,
                              nonzero_residue_roots=roots))
    return dict(m=m,p=p,J=J,degree=len(coeff)-1,
                positive_multiples=list(range(p,m**3+1,p)),
                reverse_newton_vertices=falling,residuals=residuals), coeff


def main():
    samples, checked_polys, counts, squarefree_checked = [], [], [], 0
    for m in range(2, 13):
        n,b = m-1,m*m
        sigma = vieta(m)
        possible, seen, cancelled = [], [], []
        baseprimes = primes_above(2*b,m**3+10)
        for p in baseprimes:
            a = int(m**3 % p < 2*b)
            assert valuation(top_coefficient(m),p) == -a
            squarefree_checked += 1
            assert valuation(sigma,p)>=-1
            if (m**3-2*b)//p != (m**3-3*b)//p and m>=3:
                possible.append(p)
            if valuation(sigma,p)==-1:
                assert p in possible
                seen.append(p)
            elif p in possible:
                cancelled.append(p)
        counts.append(dict(m=m, third_layer=len(possible), roots=len(seen),
                           cancellations=cancelled))
        if m>6:
            continue
        co = full_coefficients(m)
        assert -co[1]/co[0] == sigma
        for p in baseprimes:
            a = int(m**3 % p < 2*b)
            costs = sorted(((m**3-hp)//b-1) for hp in range(p,m**3+1,p)
                           if (m**3-hp)//b>=2)
            for k, c in enumerate(co):
                max_poles = sum(sum(costs[:j])<=k for j in range(1,len(costs)+1))
                assert valuation(c,p)>=-a-max_poles and max_poles<=isqrt(k)
            red = [mod_q(c*p**(a+k),p) for k,c in enumerate(co)]
            assert red[0] and not any(red[2:])
            if red[1]:
                z = -red[0]*pow(red[1],-1,p)%p
                fmod = sum(mod_q(c*p**(a+k),p*p)*pow(z,k,p*p)
                           for k,c in enumerate(co))%(p*p)
                z1 = z+p*(-(fmod//p)*pow(red[1],-1,p)%p)
                assert fmod%p == 0
                assert sum(mod_q(c*p**(a+k),p*p)*pow(z1,k,p*p)
                           for k,c in enumerate(co))%(p*p) == 0
                samples.append(dict(m=m,p=p,a=a,constant_linear=red[:2],
                                    reciprocal_root_over_p=z,lift_mod_p_squared=z1))
        checked_polys.append(dict(m=m,degree=len(co)-1,primes=len(baseprimes),
                                  coefficient_bounds=len(co)*len(baseprimes)))
    seven,_ = newton_certificate(7,101)
    nine,co = newton_certificate(9,179)
    assert seven["reverse_newton_vertices"] == [(0,-1),(1,-2),(4,-3)]
    assert nine["reverse_newton_vertices"] == [(0,-1),(4,-3),(9,-4)]
    assert [r["coefficients"] for r in nine["residuals"]] == [[178,5,49],[49,100]]
    p = 179
    nine["quadratic_unit_symbols"] = [pow(u,(p-1)//2,p) for u in (86,155)]
    assert nine["quadratic_unit_symbols"] == [178,1]
    nine["root_sum_mod_p"] = mod_q(vieta(9),p)
    assert (-co[1]//p**3)*pow(co[0]//p**3,-1,p)%p == nine["root_sum_mod_p"]
    return dict(method="signed bipartite Laplacian, last right row and column deleted",
                three_top_layer_trace=counts, large_prime_tests=squarefree_checked,
                full_rational_coefficients=checked_polys, simple_negative_unit_slopes=samples,
                full_modular_cofactors=[seven,nine])


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=2))
