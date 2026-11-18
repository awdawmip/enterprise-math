"""Exact finite exchangeability masses from integer Laplacian cofactors (python-flint)."""
import json
from fractions import Fraction
from hashlib import sha256
from math import comb, factorial, lcm, prod
from flint import fmpz, fmpz_mat, fmpz_poly


def scaled_tree(m):
    """Return the row multiplier and an integer evaluator of its tree cofactor."""
    n = m - 1
    w = [(-1) ** i * comb(n, i) for i in range(m)]

    def denominator(i, j, s):
        return 1 + i + m*j + m*m*s

    left = [lcm(*(denominator(i, j, s) for j in range(m) for s in range(m)))
            for i in range(m)]
    right = [lcm(*(denominator(i, j, s) for i in range(m) for s in range(m)))
             for j in range(n)]
    common = lcm(*left)
    toward_left = [common // scale for scale in left]
    toward_right = [common // scale for scale in right]
    edge_coefficients = [[[fmpz(w[i]*w[j]*w[s]*(common // denominator(i, j, s)))
                           for s in range(m)] for j in range(m)] for i in range(m)]

    def tree(t):
        edges = []
        for row in edge_coefficients:
            edge_row = []
            for coefs in row:
                value = 0
                for coefficient in reversed(coefs):
                    value = value*t + coefficient
                edge_row.append(value)
            edges.append(edge_row)
        mat = fmpz_mat(2*m-1, 2*m-1)
        for i in range(m):
            mat[i, i] = sum(edges[i]) // toward_left[i]
            for j in range(n):
                mat[i, m+j] = -edges[i][j] // toward_left[i]
                mat[m+j, i] = -edges[i][j] // toward_right[j]
        for j in range(n):
            mat[m+j, m+j] = sum(row[j] for row in edges) // toward_right[j]
        return mat.det()
    return prod(left)*prod(right), tree


def polynomial(m):
    n = m - 1
    degree = n*(2*m-3)
    scale, tree = scaled_tree(m)
    differences = []
    for t in range(1, degree+2):
        value, remainder = divmod(tree(t), t**n)
        assert remainder == 0
        differences.append(value)
    newton = []
    for k in range(degree+1):
        value, remainder = divmod(differences[0], factorial(k))
        assert remainder == 0
        newton.append(value)
        differences = [b-a for a,b in zip(differences, differences[1:])]
    f = fmpz_poly([0])
    for k in range(degree, -1, -1):
        f = f*fmpz_poly([-k, 1]) + newton[k]
    assert f.degree() == degree
    # Together with the interpolation nodes, these are more than deg(tau)
    # distinct values of t.  Thus even the lower and upper cancellations are checked.
    maximum_degree = (2*m-1)*n
    for t in range(degree+2, maximum_degree+2):
        assert f(t-1)*t**n == tree(t)
    b = m*m
    q0 = Fraction(n**n * m**(n*(n+3)+m) * factorial(n)**(2*m) * (3*b+1)
                  * prod(comb(n, j)**2 for j in range(m)), 2*factorial(2*b))
    assert int(f(-1)) == scale*q0
    return f


def scientific_bracket(mass):
    """Give a strict rational interval with four significant decimal digits."""
    scaled = mass
    power = 0
    while abs(scaled) < 1000:
        scaled *= 10
        power += 1
    lower = scaled.numerator // scaled.denominator
    assert lower < scaled < lower+1
    return {"decimal_multiplier_power": power, "floor": lower}


def certificate(m):
    f = polynomial(m)
    d = f.degree()
    total = int(f(-1))
    assert total > 0
    numerators = [(-1)**j * int(f[j]) for j in range(d+1)]
    assert sum(numerators) == total
    zero = [j for j,a in enumerate(numerators) if not a]
    negative = [j for j,a in enumerate(numerators) if a < 0]
    assert zero == [] and negative == ([255] if m == 13 else [])
    masses = [Fraction(a, total) for a in numerators]
    digest = sha256()
    for mass in masses:
        for number in (mass.numerator, mass.denominator):
            digits = format(abs(number), "x")
            digest.update((("-" if number < 0 else "+") + digits + "\n").encode("ascii"))
    result = {"m": m, "degree": d, "positive_count": d+1-len(zero)-len(negative),
              "negative_indices": negative, "zero_indices": zero,
              "smallest_mass_index": min(range(d+1), key=numerators.__getitem__),
              "exact_normalized_masses_sha256_signed_hex_lines": digest.hexdigest()}
    if negative:
        mass = masses[255]
        scaled = mass*10**335
        lower = scaled.numerator // scaled.denominator
        assert lower < scaled < lower+1
        result["negative_witness"] = {"index": 255, "forward_difference_order": d-255,
                                      "floor_of_mass_times_10_power_335": lower,
                                      "reduced_numerator_bits": mass.numerator.bit_length(),
                                      "reduced_denominator_bits": mass.denominator.bit_length()}
        layer = numerators
        denominator = total
        for s in range(d, 254, -1):
            assert len(layer) == s+1 and sum(layer) == denominator
            assert all((v < 0 if j == 255 else v > 0) for j, v in enumerate(layer))
            if s == 255:
                h255 = Fraction(layer[255], denominator)
                direct_h255 = Fraction(-int(f(fmpz_poly([-1, 1]))[255]),
                                       comb(d, 255)*total)
                assert h255 == direct_h255
            layer = [(s-j)*layer[j] + (j+1)*layer[j+1] for j in range(s)]
            denominator *= s
        assert len(layer) == 255 and min(layer) > 0 and sum(layer) == denominator
        result["deletion"] = {"largest_realizable_order": 254,
                              "strict_positive_count_at_254": len(layer),
                              "only_negative_index_at_every_order_255_to_276": 255,
                              "normalized_moment_255": scientific_bracket(h255),
                              "smallest_mass_at_order_254":
                                  scientific_bracket(Fraction(min(layer), denominator))}
    return result


if __name__ == "__main__":
    print(json.dumps([certificate(m) for m in (11, 12, 13)], indent=2))
