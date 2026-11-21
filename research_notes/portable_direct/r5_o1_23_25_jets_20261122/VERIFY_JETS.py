"""Frozen R5 primitive-23/25 root jets: exact integer cyclic convolution.

Recompute 2T thresholds and check an independent direct enumeration at m=46.
Requires Python 3 and numpy. dtype=object => arbitrary-precision integers.
"""
import json
import numpy as np

SUPPORTS = (
    {214, 215, 216, 217, 218},
    {214, 216, 217, 218, 219, 220, 221},
    {215, 216, 217, 218, 219, 220, 221},
)

def zero(d):
    return np.zeros(d, dtype=object)

def one(d):
    z = zero(d)
    z[0] = 1
    return z

def shift(v, exponent):
    return np.roll(v, exponent % len(v))

def mul(a, b):
    result = zero(len(a))
    for i, coefficient in enumerate(a):
        if coefficient:
            result += coefficient * shift(b, i)
    return result

def seq(d, prices, M):
    h = [zero(d) for _ in range(M + 1)]
    dh = [zero(d) for _ in range(M + 1)]
    h[0] = one(d)
    for price in prices:
        for n in range(1, M + 1):
            dh[n] += shift(dh[n - 1] + price * h[n - 1], price)
            h[n] += shift(h[n - 1], price)
    return h, dh

def cumulative(v):
    total = zero(len(v[0]))
    result = []
    for term in v:
        total += term
        result.append(total.copy())
    return result

def product_jet(d, prices):
    value, deriv = one(d), zero(d)
    for price in sorted(prices):
        factor = one(d) - shift(one(d), price)
        dfactor = -price * shift(one(d), price)
        deriv = mul(deriv, factor) + mul(value, dfactor)
        value = mul(value, factor)
    return value, deriv

def normal_form(v, d):
    if d == 23:
        return [int(v[j] - v[22]) for j in range(22)]
    if d == 25:
        return [int(v[j] - v[(j % 5) + 20]) for j in range(20)]
    raise ValueError(d)

def threshold_jets(d, M):
    J, DJ = seq(d, (219, 220, 221), M)
    U, DU = seq(d, (216, 217, 218), M)
    JC, DJC = cumulative(J), cumulative(DJ)
    UC, DUC = cumulative(U), cumulative(DU)
    signed = [zero(d) for _ in range(M)]
    dsigned = [zero(d) for _ in range(M)]
    for mask in range(1, 8):
        support = set().union(*(SUPPORTS[k] for k in range(3) if mask & (1 << k)))
        C, DC = product_jet(d, support)
        x_used, y_used, j_used = bool(mask & 3), bool(mask & 5), bool(mask & 6)
        sign = 1 if mask.bit_count() % 2 else -1
        old, dold = zero(d), zero(d)
        for n in range(M):
            v, dv = zero(d), zero(d)
            for x in (range(n + 1) if x_used else (0,)):
                for y in (range(n + 1) if y_used else (0,)):
                    if (mask & 1) and x + y > n:
                        continue
                    cap = n
                    if mask & 2:
                        cap = min(cap, n - x)
                    if mask & 4:
                        cap = min(cap, n - y)
                    w = JC[cap] if j_used else one(d)
                    dw = DJC[cap] if j_used else zero(d)
                    exponent = 214 * x + 215 * y
                    v += shift(w, exponent)
                    dv += shift(dw + exponent * w, exponent)
            b, db = v - old, dv - dold
            signed[n] += sign * mul(C, b)
            dsigned[n] += sign * (mul(DC, b) + mul(C, db))
            old, dold = v, dv
    A, DA = [], []
    for m in range(1, M + 1):
        v, dv = zero(d), zero(d)
        for n in range(m):
            v += mul(signed[n], UC[m - 1 - n])
            dv += mul(dsigned[n], UC[m - 1 - n]) + mul(signed[n], DUC[m - 1 - n])
        A.append(normal_form(v, d))
        DA.append(normal_form(dv, d))
    return A, DA

def direct_jet(d, m):
    """Second algorithm: enumerate simultaneous original inequalities directly."""
    J, DJ = seq(d, (219, 220, 221), m)
    U, DU = seq(d, (216, 217, 218), m)
    UC, DUC = cumulative(U), cumulative(DU)
    W = [[mul(J[j], UC[k]) for k in range(m)] for j in range(m)]
    DW = [[mul(DJ[j], UC[k]) + mul(J[j], DUC[k])
           for k in range(m)] for j in range(m)]
    total, dtotal = zero(d), zero(d)
    for mask in range(1, 8):
        xs = range(m) if mask & 3 else (0,)
        ys = range(m) if mask & 5 else (0,)
        js = range(m) if mask & 6 else (0,)
        P, DP = zero(d), zero(d)
        for x in xs:
            for y in ys:
                if (mask & 1) and x + y >= m:
                    continue
                exponent = 214 * x + 215 * y
                for j in js:
                    loads = []
                    if mask & 1:
                        loads.append(x + y)
                    if mask & 2:
                        loads.append(x + j)
                    if mask & 4:
                        loads.append(y + j)
                    cap = m - 1 - max(loads)
                    if cap < 0:
                        continue
                    P += shift(W[j][cap], exponent)
                    DP += shift(DW[j][cap] + exponent * W[j][cap], exponent)
        C, DC = product_jet(
            d, set().union(*(SUPPORTS[k] for k in range(3) if mask & (1 << k)))
        )
        sign = 1 if mask.bit_count() % 2 else -1
        total += sign * mul(C, P)
        dtotal += sign * (mul(DC, P) + mul(C, DP))
    return normal_form(total, d), normal_form(dtotal, d)

def main():
    output = {"schema": "R5_23_25_FIRST_JET_CERTIFICATE_V1",
              "scientific_status": "AUTHOR_EXACT_INTEGER_CHECKED_NOT_REVIEWED",
              "results": []}
    for d, T, exceptional, p0, witnesses in (
        (23, 46, [42, 43, 44, 45, 46], 299,
         [-28589, -4209, 47219, -66815, 33787]),
        (25, 50, [46, 47, 48, 49, 50], 300,
         [-1090275, 1015225, -493900, 26000, 97675]),
    ):
        A, DA = threshold_jets(d, 2 * T)
        assert [m for m in range(1, T + 1) if not any(A[m - 1])] == exceptional
        assert all(A[m - 1] == A[m - 1 + T] for m in range(1, T + 1))
        rows = []
        for r, witness in zip(exceptional, witnesses):
            assert not any(A[r - 1])
            assert DA[r + T - 1] == [2 * x for x in DA[r - 1]]
            assert DA[r - 1][1] == witness != 0
            full = DA[r - 1].copy()
            full[0] -= 2 * d * p0
            rows.append({"r": r, "normal_DA": DA[r - 1],
                         "normal_full_DR": full,
                         "index_1_nonzero": witness,
                         "full_derivative_at_r_plus_kT": "(k+1)*normal_full_DR"})
        original_A, original_DA = direct_jet(d, 46)
        assert original_A == A[45] and original_DA == DA[45]
        output["results"].append({
            "d": d, "T": T, "p0": p0,
            "zero_phases": exceptional,
            "complete_periodicity_checked": T,
            "complete_derivative_scaling_checked": len(exceptional),
            "direct_intersection_crosscheck_m": 46,
            "rows": rows
        })
        print("PASS", d, "period", T, "first-jets", len(rows), "direct m=46")
    with open("CERTIFICATE.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
