"""Exact finite profile witnesses for universal T6 p=7^3 and p=13^2 cancellation."""

BUDGET = 2331


def profiles(prime, power):
    base = prime ** power
    multipliers = tuple(j for j in range(1, (BUDGET + 1) // base + 1)
                        if j % prime != 0)
    weights = tuple(base * j - 1 for j in multipliers)
    cur = [0] * len(weights)

    def generate(i, remaining):
        if i == len(weights):
            yield tuple(cur)
            return
        for n in range(remaining // weights[i] + 1):
            cur[i] = n
            yield from generate(i + 1, remaining - n * weights[i])
        cur[i] = 0

    return multipliers, weights, list(generate(0, BUDGET))


def generating_function_count(weights):
    coeff = [0] * (BUDGET + 1)
    coeff[0] = 1
    for weight in weights:
        for mass in range(weight, BUDGET + 1):
            coeff[mass] += coeff[mass - weight]
    return sum(coeff)


def signature(profile, multipliers, prime, k):
    return tuple(sum(m * pow(j, -degree, prime)
                     for j, m in zip(multipliers, profile)) % prime
                 for degree in range(1, k + 1))


def audit(prime, power, expected):
    multipliers, weights, rows = profiles(prime, power)
    assert len(rows) == generating_function_count(weights)
    print(f"p={prime}, valuation={power}, profiles={len(rows)}")
    for k, distinct_expected, collision_expected in expected:
        fibers = {}
        for row in rows:
            fibers.setdefault(signature(row, multipliers, prime, k), []).append(row)
        pairs = [(a, b) for group in fibers.values()
                 for i, a in enumerate(group) for b in group[i + 1:]]
        assert (len(fibers), len(pairs)) == (distinct_expected, collision_expected)
        print(f"  moments={k}, fibers={len(fibers)}, collisions={len(pairs)}")
        if prime == 13 and k == 4:
            assert len(pairs) == 1
            assert {pairs[0][0], pairs[0][1]} == {
                (0,) * 12, (13,) + (0,) * 11}
    return len(rows)


def main():
    assert audit(7, 3, [(1, 7, 52), (2, 29, 1), (3, 30, 0)]) == 30
    assert audit(13, 2, [(1, 13, 5152), (2, 161, 319),
                         (3, 355, 17), (4, 371, 1)]) == 372
    print("PASS: complete two-route profile counts and all modular-signature assertions")
    print("p=13 exception: empty vs 13 copies of denominator 169;")
    print("full S_2 equality eliminates that exception by p-adic valuation -3 vs >=-2")


if __name__ == "__main__":
    main()
