"""Integer endpoint certificates and rational log bounds for the fixed-support law."""
import hashlib
import json
import math
from fractions import Fraction
from itertools import combinations


def mul(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c


def power(z, k):
    out = (1, 0)
    while k:
        if k & 1:
            out = mul(out, z)
        k >>= 1
        if k:
            z = mul(z, z)
    return out


def primitive(z):
    g = math.gcd(*z)
    return z[0]//g, z[1]//g


def det(z, w):
    return z[0]*w[1] - z[1]*w[0]


def encode_atom(z):
    h = hashlib.sha256()
    for x in z:
        raw = x.to_bytes((x.bit_length()+7)//8, 'big')
        h.update(len(raw).to_bytes(8, 'big'))
        h.update(raw)
    return h.hexdigest()


def root_chain(s, n):
    k, grid = 1 << n, 1 << (n*n)
    previous = (1, 1)
    path = []
    atoms = []
    for j in range(1, s):
        # On this short interval k-th powers stay in the open right half-plane.
        def below(m):
            z = power((grid, m), k)
            assert z[0] > 0 and z[1] >= 0
            return det(z, previous) >= 0

        lo, hi = 0, grid//k
        assert below(lo) and not below(hi)
        while lo+1 < hi:
            mid = (lo+hi)//2
            if below(mid):
                lo = mid
            else:
                hi = mid
        m = lo-(4**j)
        assert m > 0 and below(lo) and not below(lo+1)
        root = primitive((grid, m))
        z = power(root, k)
        remainder = primitive(mul(previous, (z[0], -z[1])))
        assert 0 < remainder[1] < remainder[0] and 0 < root[1] < root[0]
        assert primitive(mul(remainder, z)) == previous
        if atoms:
            assert det(atoms[-1], remainder) > 0
        atoms.append(remainder)
        path.append({"layer": j, "last_grid_index_below": lo, "root": list(root),
                     "residual_sha256_length_prefixed_den_num": encode_atom(remainder)})
        previous = root
    atoms.append(previous)
    assert len(set(atoms)) == s
    # A completely expanded check is affordable for the deliberately small examples.
    direct = n <= 4
    if direct:
        z = (1, 0)
        for j, atom in enumerate(atoms):
            z = primitive(mul(z, power(atom, k**j)))
        assert z == (1, 1)
    # For each slope b/a, v <= log2(b/a) < v+1 by integer shifts.
    ratio_logs = [(b//a).bit_length()-1 for b, a in atoms]
    assert min(ratio_logs) > 0
    bit_sum = sum(b.bit_length() for b, a in atoms)
    # bit_sum-s <= B_log <= bit_sum. Enclose the normalized product
    # (s-1) mu ln B_log / ln 10 using only integer-power bounds.
    log_height_lb = (bit_sum-s).bit_length()-1
    log_height_ub = bit_sum.bit_length()
    lower = (s-1)*log_height_lb*sum(Fraction(1, v+1) for v in ratio_logs)
    upper = (s-1)*log_height_ub*sum(Fraction(1, v) for v in ratio_logs)
    return {"s": s, "n": n, "k": k, "grid_log2": n*n, "layers": path,
            "coefficient_bits": [(k**j).bit_length() for j in range(s)],
            "denominator_bits": [b.bit_length() for b, a in atoms],
            "floor_log2_rho": ratio_logs, "winding": 0,
            "normalized_product_rational_enclosure": [str(lower), str(upper)],
            "full_word_expanded": direct}


def old_calibrations():
    # First strict crossing by directly multiplying the seed q+i.
    crossing = []
    for q in (3, 10, 31, 100, 251):
        z, j = (1, 0), 0
        while z[1] <= z[0]:
            z, j = mul(z, (q, 1)), j+1
        A, B = z
        h = primitive((A+B, B-A))
        assert primitive(mul((1, 1), h)) == primitive(z)
        assert 0 < q*h[1] < h[0] and q-1 < 2*j <= 2*q
        crossing.append([q, j, h[0].bit_length()])
    # Consecutive diagonal complements approach the half diagonal.
    z, pell = (2, 1), []
    for j in range(14):
        b, a = z
        comp = primitive((b+a, b-a))
        assert primitive(mul(z, comp)) == (1, 1)
        assert abs(b*b-2*a*b-a*a) == 1
        pell.append([b, a, comp[0], comp[1]])
        z = (2*b+a, b)
    lead = primitive(mul(power((79, 3), 7), power((278, 29), 5)))
    assert lead == (1, 1)
    return {"first_crossing_q_k_residual_den_bits": crossing,
            "pell_b_a_complement_b_a": pell, "H1000_leader_endpoint": list(lead)}


def parity_test():
    # An even-content matrix with rank 2, nullity 2 and all six raw minors even.
    rows = [[2, 0, 2, 2], [0, 2, 2, -2]]
    minors = {(i,j): rows[0][i]*rows[1][j]-rows[0][j]*rows[1][i]
              for i,j in combinations(range(4),2)}
    d = math.gcd(*minors.values())
    circuits = [(-1,-1,1,0), (-1,1,0,1)]
    assert d == 4 and all(sum(x*y for x,y in zip(r,u)) == 0
                          for r in rows for u in circuits)
    for coeff in ((1,1), (1,2), (3,-5)):
        target = [sum(z*v[i] for z,v in zip(coeff,circuits)) for i in range(4)]
        for mask in range(16):
            pair = lambda v: sum(v[i] for i in range(4) if mask & (1<<i))
            if pair(target) % 2:
                assert any(pair(v) % 2 for v in circuits)
    return {"raw_minor_gcd": d, "primitive_minors": [v//d for v in minors.values()]}


def main():
    cases = [(2,3), (3,4), (2,6), (3,6), (4,6), (5,6), (3,8), (4,8), (5,8), (3,10)]
    print(json.dumps({"schema": "exact_diagonal_fixed_support_resource_v1",
                      "root_chains": [root_chain(s,n) for s,n in cases],
                      "older_exact_calibrations": old_calibrations(),
                      "odd_minor_regression": parity_test()}, indent=2))


if __name__ == "__main__":
    main()
