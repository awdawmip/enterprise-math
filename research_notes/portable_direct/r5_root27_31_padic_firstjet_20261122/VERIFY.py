"""R5 frozen scalar observer. Exact first q-derivatives at primitive d=27,31.
Python standard library only. Finite checks; all-m proof is in RESEARCH.md.
"""
import hashlib
import json

S = (
    set(range(214, 219)),
    {214, 216, 217, 218, 219, 220, 221},
    {215, 216, 217, 218, 219, 220, 221},
)
S3 = set(range(223, 291))
S4 = set(range(296, 313))

def zero(d):
    return [0] * d

def one(d):
    a = zero(d)
    a[0] = 1
    return a

def add(a, b):
    return [x + y for x, y in zip(a, b)]

def scale(a, c):
    return [c * x for x in a]

def shift(a, power):
    d = len(a)
    ans = zero(d)
    for i, coeff in enumerate(a):
        ans[(i + power) % d] += coeff
    return ans

def mul(a, b):
    d = len(a)
    ans = zero(d)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    ans[(i + j) % d] += x * y
    return ans

def factor(d, price):
    return add(one(d), scale(shift(one(d), price), -1))

def complete_h(d, prices, m):
    h = [one(d)] + [zero(d) for _ in range(m - 1)]
    for price in prices:
        for n in range(1, m):
            h[n] = add(h[n], shift(h[n - 1], price))
    return h

def finite_joint_threshold(d, mask, m, U, J):
    ans = zero(d)
    xs = range(m) if mask & 3 else (0,)
    ys = range(m) if mask & 5 else (0,)
    js = range(m) if mask & 6 else (0,)
    for x in xs:
        for y in ys:
            for j in js:
                loads = []
                if mask & 1:
                    loads.append(x + y)
                if mask & 2:
                    loads.append(x + j)
                if mask & 4:
                    loads.append(y + j)
                bound_u = m - 1 - max(loads)
                if bound_u >= 0:
                    for u in range(bound_u + 1):
                        ans = add(ans, shift(mul(U[u], J[j]), 214*x + 215*y))
    return ans

def primitive_normal_form(v, d):
    if d == 27:
        # Phi_27(X)=1+X^9+X^18.
        return [v[i] - v[18 + (i % 9)] for i in range(18)]
    if d == 31:
        # Phi_31(X)=sum_(i=0)^30 X^i.
        return [v[i] - v[30] for i in range(30)]
    raise ValueError(d)

def first_jet(d, m):
    p0 = {27: 216, 31: 217}[d]
    p4 = {27: 297, 31: 310}[d]
    U = complete_h(d, (216, 217, 218), m)
    J = complete_h(d, (219, 220, 221), m)
    derivative = zero(d)
    for mask in range(1, 8):
        support = set().union(*(S[k] for k in range(3) if mask & (1 << k)))
        assert [p for p in sorted(support) if p % d == 0] == [p0]
        prefactor = one(d)
        for p in sorted(support - {p0}):
            prefactor = mul(prefactor, factor(d, p))
        part = mul(prefactor, finite_joint_threshold(d, mask, m, U, J))
        sign = 1 if mask.bit_count() % 2 else -1
        derivative = add(derivative, scale(part, -p0 * sign))
    prefactor = one(d)
    for p in sorted(S4 - {p4}):
        prefactor = mul(prefactor, factor(d, p))
    threshold = zero(d)
    for row in complete_h(d, sorted(S4), m):
        threshold = add(threshold, row)
    derivative = add(derivative, scale(mul(prefactor, threshold), -p4))
    return primitive_normal_form(derivative, d)

def direct_all_31_masks_at_m1(d):
    # For m=1 every selected event fixes every variable on its union to zero.
    # Thus P_(I,1)=1: exact complete 31-mask derivative, independent of
    # the seven-event load enumerator above.
    supports = (*S, S3, S4)
    derivative = zero(d)
    for mask in range(1, 32):
        support = set().union(*(supports[k] for k in range(5) if mask & (1 << k)))
        zeros = [p for p in sorted(support) if p % d == 0]
        if len(zeros) != 1:
            continue
        p0 = zeros[0]
        part = one(d)
        for p in sorted(support - {p0}):
            part = mul(part, factor(d, p))
        sign = 1 if mask.bit_count() % 2 else -1
        derivative = add(derivative, scale(part, -p0 * sign))
    return primitive_normal_form(derivative, d)

EXPECTED_INDEX_ZERO = {
    27: [-1323, -2646, -5751, 6021, 8775],
    31: [1302, 713, 93, 744, -1984],
}

def main():
    certificate = {
        "schema": "R5_ROOT27_31_FIRST_JET_P_ADIC_CHECK_V1",
        "arithmetic": "exact_integer_cyclic_ring",
        "proof_scope": "all-m residue classes in RESEARCH.md",
        "finite_check_m": [1, 2, 3, 4, 5],
        "full_31_mask_crosscheck": "m=1 for d=27,31",
        "rows": [],
    }
    for d in (27, 31):
        assert first_jet(d, 1) == direct_all_31_masks_at_m1(d)
        for m in range(1, 6):
            v = first_jet(d, m)
            assert v[0] == EXPECTED_INDEX_ZERO[d][m-1]
            nonzero_class = m % 9 in (1, 4) if d == 27 else 1 <= m % 31 <= 26
            if nonzero_class:
                assert any(v)
            certificate["rows"].append({
                "d": d, "m": m,
                "p_adic_guaranteed_nonzero": nonzero_class,
                "computed_nonzero": any(v),
                "normal_form": v,
                "normal_form_sha256": hashlib.sha256(
                    json.dumps(v, separators=(",", ":")).encode()
                ).hexdigest(),
            })
    print(json.dumps(certificate, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
