#!/usr/bin/env python3
"""Exact prime-field cotangent ranks of joint-zero Reeve canonical-cover fibers.

Reference: research_notes/driver/2026-11-16_r6_prefix808_relative_cotangent_length_characteristic_jumps.md
No external dependencies, floating point arithmetic, or random sampling.
"""

PRIMES = (2, 3, 5, 7)


def rank_mod_p(rows, p):
    """Sparse exact row reduction over F_p; columns are integer indexed."""
    pivots = {}
    for entries in rows:
        row = {j: c % p for j, c in entries.items() if c % p}
        while row:
            j = min(row)
            if j not in pivots:
                inverse = pow(row[j], -1, p)
                pivots[j] = {col: val * inverse % p for col, val in row.items()}
                break
            scale = row[j]
            for col, val in pivots[j].items():
                row[col] = (row.get(col, 0) - scale * val) % p
                if row[col] == 0:
                    del row[col]
    return len(pivots)


def odd_cotangent_length(h, p):
    """F=F_p[u,v]/(u,v)^h; conormal generators d(u^a v^(h-a))."""
    assert h >= 3 and h % 2 == 1
    basis = [(a, d - a) for d in range(h) for a in range(d + 1)]
    index = {(a, b, j): n for n, (a, b, j) in enumerate(
        (a, b, j) for a, b in basis for j in range(2))}
    rows = []
    for a in range(h + 1):
        b = h - a
        row = {}
        if a:
            row[index[(a - 1, b, 0)]] = a
        if b:
            row[index[(a, b - 1, 1)]] = b
        rows.append(row)
    return len(index) - rank_mod_p(rows, p)


def even_cotangent_length(k, p):
    """F=F_p[x,y,z]/(y^2-xz,S_>=k), with y exponent 0 or 1."""
    assert k >= 1
    basis = []
    for degree in range(k):
        for exponent_y in (0, 1):
            if exponent_y > degree:
                continue
            for exponent_x in range(degree - exponent_y + 1):
                exponent_z = degree - exponent_y - exponent_x
                basis.append((exponent_x, exponent_z, exponent_y))
    assert len(basis) == k * k
    index = {(a, b, e, j): n for n, (a, b, e, j) in enumerate(
        (a, b, e, j) for a, b, e in basis for j in range(3))}

    def add(row, key, coefficient):
        if key in index:
            column = index[key]
            row[column] = row.get(column, 0) + coefficient

    rows = []
    # For all degrees <k, the relation df=2y dy-z dx-x dz.
    for a, b, e in basis:
        if a + b + e > k - 2:
            continue
        row = {}
        add(row, (a, b + 1, e, 0), -1)
        add(row, (a + 1, b, e, 2), -1)
        if e == 0:
            add(row, (a, b, 1, 1), 2)
        else:
            add(row, (a + 1, b + 1, 0, 1), 2)  # y^2=xz
        rows.append(row)
    # Truncation conormal: d(x^a y^e z^b) for a+b+e=k.
    for e in (0, 1):
        for a in range(k - e + 1):
            b = k - e - a
            row = {}
            if a:
                add(row, (a - 1, b, e, 0), a)
            if b:
                add(row, (a, b - 1, e, 2), b)
            if e:
                add(row, (a, b, 0, 1), 1)
            rows.append(row)
    return len(index) - rank_mod_p(rows, p)


def expected_odd(h, p):
    return h * h + h // p if h % p == 0 else h * h - 1


def expected_even(k, p):
    if k == 1:
        return 0
    return 2 * k * k - 2 + (2 * k // p + 1 if k % p == 0 else 0)


def main():
    checked = 0
    for h in (3, 5, 7, 9, 11, 13):
        for p in PRIMES:
            obtained = odd_cotangent_length(h, p)
            expected = expected_odd(h, p)
            assert obtained == expected, (h, p, obtained, expected)
            checked += 1
    for k in range(1, 9):
        for p in PRIMES:
            obtained = even_cotangent_length(k, p)
            expected = expected_even(k, p)
            assert obtained == expected, (2 * k, p, obtained, expected)
            checked += 1
    assert checked == 56
    print(f"PASS: {checked} exact characteristic/height cotangent length checks")
    for h in (3, 4, 6, 8, 10, 12):
        nums = [odd_cotangent_length(h, p) if h % 2 else even_cotangent_length(h // 2, p)
                for p in PRIMES]
        print(f"h={h:2d}: " + " ".join(f"char{p}={n}" for p, n in zip(PRIMES, nums)))


if __name__ == "__main__":
    main()
