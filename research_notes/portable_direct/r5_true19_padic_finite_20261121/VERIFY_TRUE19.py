"""R5 primitive 19, exact seven-mask intersection numerator.

No external dependencies or floating-point arithmetic.
Verifies m=1..19 and the separate m=2 closed form.
Author-side arithmetic evidence, not independent mathematical review.
"""
from math import comb
D = 19
S = {
  0: [214, 215, 216, 217, 218],
  1: [214, 216, 217, 218, 219, 220, 221],
  2: [215, 216, 217, 218, 219, 220, 221],
}
U = list(range(214, 222))

def zero():
    return [0] * D

def one():
    return [1] + [0] * (D - 1)

def add(a, b, sign=1):
    return [x + sign*y for x, y in zip(a, b)]

def monomial(n):
    x = zero()
    x[n % D] = 1
    return x

def mul(a, b):
    out = zero()
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i+j) % D] += x*y
    return out

def factors(prices):
    out = one()
    for p in prices:
        out = mul(out, add(one(), monomial(p), -1))
    return out

def complete_homogeneous(prices, m):
    h = [zero() for _ in range(m)]
    h[0] = one()
    for p in prices:
        new = [zero() for _ in range(m)]
        for total in range(m):
            for count in range(total+1):
                shift = (count*p) % D
                for i, v in enumerate(h[total-count]):
                    new[total][(i+shift) % D] += v
        h = new
    return h

def phi19_basis(v):
    # In Z[z]/Phi19, z^18=-(1+...+z^17).
    return [v[i] - v[18] for i in range(18)]

def numerator(m):
    hu = complete_homogeneous([216,217,218], m)
    hj = complete_homogeneous([219,220,221], m)
    total = zero()
    for mask in range(1,8):
        indices = [i for i in (0,1,2) if mask & (1 << i)]
        prices = sorted(set().union(*(set(S[i]) for i in indices)))
        xx = range(m) if 214 in prices else (0,)
        yy = range(m) if 215 in prices else (0,)
        jj = range(m) if 219 in prices else (0,)
        term = zero()
        for x in xx:
            for y in yy:
                for u in range(m):
                    for j in jj:
                        loads = (x+y+u, x+u+j, y+u+j)
                        if any(loads[i] >= m for i in indices):
                            continue
                        w = mul(hu[u], hj[j] if 219 in prices else one())
                        shift = (214*x+215*y) % D
                        for k, v in enumerate(w):
                            term[(k+shift) % D] += v
        term = mul(factors(prices), term)
        total = add(total, term, 1 if len(indices)%2 else -1)
    return total

def sum_monomials(prices):
    v = zero()
    for p in prices:
        v = add(v, monomial(p))
    return v

def independent_closed_m2():
    single = zero()
    for i in (0,1,2):
        single = add(single, mul(factors(S[i]), add(one(), sum_monomials(S[i]))))
    base = add(one(), sum_monomials(U))
    exceptions = add(
        mul(add(monomial(214),monomial(215)),sum_monomials([219,220,221])),
        monomial(429),
    )
    return add(single, mul(factors(U), add([2*x for x in base], exceptions)), -1)

def main():
    previous_m1 = [6,7,10,12,13,10,11,2,0,-6,-8,-18,-14,-17,-14,-14,-10,-8]
    assert phi19_basis(numerator(1)) == previous_m1, "historic m1 regression"
    assert numerator(2) == independent_closed_m2(), "closed m2 crosscheck"
    rows=[]
    for m in range(1,20):
        v=phi19_basis(numerator(m))
        assert any(v), f"unexpected zero at m={m}"
        rows.append((m,v))
        print(f"m={m:02d} root19_nonzero=True first={v[0]} second={v[1]}")
    assert [rows[m-1][1][0] for m in (15,16,17,18,19)] == [-210,210,-160,28,101]
    assert [rows[m-1][1][1] for m in (15,16,17,18,19)] == [-437,452,-365,165,86]
    print("PASS: 19/19 exact nonzero, historic m1 and independent m2 verified")
    return rows

if __name__ == "__main__":
    main()
