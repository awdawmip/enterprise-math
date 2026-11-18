"""Exact support/rank and positive-mass checks. Standard library, Python 3.8+."""
from fractions import Fraction
from itertools import combinations
from math import fsum, gcd, log, pi, sin


def factor(n):
    out = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e:
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append((n, 1))
    return out


def support(q, m):
    rows = [v for v in range(q) if (q % 2 or v % 2)
            and all(e < m or v % (p**m) for p, e in factor(q))]
    cols = [v for v in range(q) if q % 2 or v % 2]
    return rows, cols


def primary_size(p, n, m):
    if p == 2 and n >= 3:
        return (2 // gcd(m, 2)) * (2 ** (n - 2) // gcd(m, 2 ** (n - 2)))
    phi = p ** (n - 1) * (p - 1)
    return phi // gcd(phi, m)


def decomposition(q, r, m):
    angular = 1
    threshold_bits = 0
    unit_modulus = 1
    for p, e in factor(q):
        if p == 2 and r % 2 == 0:
            return 0, 0, 0, 0
        n = e
        t = r
        while n and t % p == 0:
            t //= p
            n -= 1
        if n:
            angular *= primary_size(p, n, m)
            unit_modulus *= p**n
        elif e % m:
            threshold_bits += 1
    return angular * 2**threshold_bits, angular, threshold_bits, unit_modulus


def rank_mod_two(rows):
    pivots = {}
    for row in rows:
        while row:
            j = row.bit_length() - 1
            if j not in pivots:
                pivots[j] = row
                break
            row ^= pivots[j]
    return len(pivots)


def components(rows):
    # Each bitset is the neighbor set of one realized row. Ignore isolated vertices.
    clusters = []
    for row in rows:
        if not row:
            continue
        distinct = []
        for existing in clusters:
            if row & existing:
                row |= existing
            else:
                distinct.append(existing)
        distinct.append(row)
        clusters = distinct
    return len(clusters)


def all_residues(q, m):
    row_classes, cols = support(q, m)
    values = {r: [] for r in range(q)}
    for row in row_classes:
        observed = {}
        for j, col in enumerate(cols):
            r = row * pow(col, m, q) % q
            observed[r] = observed.get(r, 0) | (1 << j)
        for r, mask in observed.items():
            values[r].append(mask)
    for r, masks in values.items():
        expected, angular, bits, unit_modulus = decomposition(q, r, m)
        distinct = set(masks)
        assert rank_mod_two(distinct) == len(distinct) == expected
        assert components(distinct) == angular
    return len(values)


def all_unit_events(q, m):
    units = [i for i in range(q) if gcd(i, q) == 1]
    powers = {pow(t, m, q) for t in units}
    checked = 0
    for size in range(1, len(units) + 1):
        for seq in combinations(units, size):
            A = set(seq)
            invariant = {a * v % q for a in A for v in powers} == A
            rowmasks = {sum(1 << j for j, y in enumerate(units) if x * pow(y, m, q) % q in A)
                        for x in units}
            assert (len(rowmasks - {0}) == 1) == invariant
            checked += 1
    return checked


def thresholds():
    checked = 0
    example = None
    for p in [3, 5, 7, 11]:
        rho = Fraction(1, p**2)
        for m in range(2, 7):
            for e in range(1, 3 * m + 1):
                k, d = divmod(e, m)
                Z = rho**e
                # R exact; T below, at, or strictly above k, using exact geometric tails.
                rowmasses = [(1 - rho) * rho**r / (1 - rho**m) for r in range(m)]
                table = [[Fraction(0) for _ in range(2)] for _ in range(2)]
                for r, pr in enumerate(rowmasses):
                    for j, pj in [(k, rho**(m*k) * (1 - rho**m)), (k + 1, rho**(m*(k+1)))]:
                        if r + m * j >= e:
                            table[int(r >= d)][int(j > k)] += pr * pj / Z
                assert sum(map(sum, table)) == 1
                if d:
                    assert table[0][0] == 0
                    assert table[0][1] + table[1][1] == rho ** (m - d)
                    assert table[1][0] + table[1][1] == (1 - rho**(m-d)) / (1 - rho**m)
                    assert table[1][1] / sum(table[1]) == rho**m
                    if p == 3 and m == 2 and e == 1:
                        example = [[str(x) for x in row] for row in table]
                checked += 1
    return checked, example


def critical_example():
    # Rigorously enclose P(T^2=1 mod 5) at exponent two by correct directed rounding.
    bound = 10000
    scale = 10**14
    lower = {1: 0, 4: 0}
    upper = {1: 0, 4: 0}
    for n in range(1, bound + 1, 2):
        if n % 5:
            label = n * n % 5
            lower[label] += scale // (n * n)
            upper[label] += -((-scale) // (n * n))
    for label in upper:
        upper[label] += (scale + bound - 1) // bound  # integral tail sum over all n>bound
    lo = Fraction(lower[1], lower[1] + upper[4])
    hi = Fraction(upper[1], upper[1] + lower[4])
    assert 2 * lo > 1 and (6 * lo - 3)**2 < 5 < (6 * hi - 3)**2
    milli = 10**6
    return {
        "sum_cutoff": bound,
        "lower": str(Fraction((lo * milli) // 1, milli)),
        "upper": str(Fraction(-((-hi * milli) // 1), milli)),
    }


def dyadic_entropy_diagnostics():
    # Monotone integral bounds for the tail of sum_{n odd} log(n)/n^2.
    cutoff = 250000
    first = cutoff + 1
    partial = fsum(log(n) / n**2 for n in range(1, cutoff, 2))
    lower_tail = (log(first) + 1) / (2 * first)
    upper_tail = lower_tail + log(first) / first**2
    z = pi**2 / 8
    low = log(z) + 2 * (partial + lower_tail) / z
    high = log(z) + 2 * (partial + upper_tail) / z
    result = {}
    for e in (6, 8, 10):
        modulus = 2 ** (e - 1)
        weights = [8 / (modulus * sin(pi * a / modulus))**2 for a in range(1, modulus // 2, 2)]
        assert abs(fsum(weights) - 1) < 1e-12
        coarse = -fsum(p * log(p) for p in weights)
        diagnostic = modulus * ((low + high) / 2 - coarse)
        assert 3.9 < diagnostic < 4 and (high - low) * modulus < 1e-6
        result[str(e)] = round(diagnostic, 6)
    return result


def split(n, m):
    s = t = 1
    for p, e in factor(n):
        j, i = divmod(e, m)
        s *= p**i
        t *= p**j
    return s, t


if __name__ == "__main__":
    import json
    total = 0
    for q in list(range(1, 76)) + [81, 90, 105, 120, 144, 189, 225]:
        for m in [2, 3, 4, 5]:
            total += all_residues(q, m)
    count = sum(all_unit_events(q, m) for q in [3, 4, 5, 7, 8, 9, 10, 12, 15, 16, 20, 24]
                for m in [2, 3, 4])
    concrete = 0
    for n in range(1, 10000, 2):
        for m in [2, 3, 4]:
            s, t = split(n, m)
            assert s * t**m == n
            for q in [8, 9, 30, 35]:
                row, col = s % q, t % q
                assert row * pow(col, m, q) % q == n % q
            concrete += 1
    checks, matrix = thresholds()
    examples = [(3, 0, 2), (9, 0, 2), (9, 3, 2), (35, 1, 2),
                (105, 3, 2), (105, 0, 2), (144, 9, 2), (225, 0, 2)]
    print(json.dumps({
        "all_single_residue_rank_and_component_checks": total,
        "all_nonempty_unit_set_tests": count,
        "actual_odd_integer_decompositions": concrete,
        "examples_q_r_m_to_rank_angular_components_threshold_primes_unit_modulus": [
            [q, r, m, *decomposition(q, r, m)] for q, r, m in examples
        ],
        "prime_threshold_exact_mass_cases": checks,
        "q3_zero_m2_sigma2_table_low_high_by_near_far": matrix,
        "q5_critical_square_label_mass_enclosure": critical_example(),
        "dyadic_diagnostic_2_to_e_minus_1_times_entropy_loss_nats": dyadic_entropy_diagnostics(),
    }, indent=2))
