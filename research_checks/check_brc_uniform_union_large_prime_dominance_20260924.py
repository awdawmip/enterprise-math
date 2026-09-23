from math import factorial


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("vp(0,p) not used")
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def target_primes(limit: int):
    out = []
    for n in range(2, limit + 1):
        if any(n % q == 0 for q in range(2, int(n**0.5) + 1)):
            continue
        if n % 24 in (13, 19):
            out.append(n)
    return out


def epsilon(p: int, j: int) -> int:
    return 0 if (2 * j) % (p - 1) == 0 else 1


def beta(p: int, j: int) -> int:
    return 2 * j + epsilon(p, j) + vp(1 + pow(4, j), p) - vp(j, p)


def generic_beta(j: int) -> int:
    return 2 * j + 1


def fact_vp(m: int, p: int) -> int:
    e = 0
    q = p
    while q <= m:
        e += m // q
        q *= p
    return e


def branch_monomials(N: int, p: int | None):
    # Enumerate only j whose one-copy lower bound is below N.
    js = []
    j = 1
    while True:
        b = generic_beta(j) if p is None else beta(p, j)
        if b >= N and 2 * j - (0 if p is None else vp(j, p)) >= N:
            if 2 * j >= N + 4:
                break
        if b < N:
            js.append((j, b))
        j += 1

    out = set()

    def rec(i, weight, acc):
        if i == len(js):
            out.add(tuple(acc))
            return
        j, b = js[i]
        m = 0
        while True:
            w = weight + m * b
            if p is not None:
                w -= fact_vp(m, p)
            if w >= N:
                break
            if m:
                acc.append((j, m))
            rec(i + 1, w, acc)
            if m:
                acc.pop()
            m += 1

    rec(0, 0, [])
    return out


def verify_horizon(N: int, limit: int = 200):
    primes = target_primes(limit)
    generic = branch_monomials(N, None)
    branches = {p: branch_monomials(N, p) for p in primes}

    large_subset = {p: branches[p] <= generic for p in primes if p > N}
    assert all(large_subset.values()), (N, [p for p, ok in large_subset.items() if not ok])

    full_union = set(generic)
    for p in primes:
        full_union |= branches[p]
    reduced_union = set(generic)
    for p in primes:
        if p <= N:
            reduced_union |= branches[p]
    assert full_union == reduced_union
    return generic, branches, reduced_union


horizons = list(range(12, 41, 2))
for N in horizons:
    verify_horizon(N)

_, b30, u30 = verify_horizon(30)
g32, b32, u32 = verify_horizon(32)
_, b34, u34 = verify_horizon(34)

sharpness = []
for p in target_primes(200):
    gp = branch_monomials(p, None)
    bp = branch_monomials(p, p)
    if not bp <= gp:
        sharpness.append(p)
assert sharpness[:3] == [13, 19, 37]

summary = {
    "horizons_checked": horizons,
    "target_prime_limit": 200,
    "N30_union": len(u30),
    "N32": {
        "generic": len(g32),
        "p13": len(b32[13]),
        "p19": len(b32[19]),
        "reduced_union": len(u32),
        "large_branches_subset_generic": {p: b32[p] <= g32 for p in (37, 43, 61)},
    },
    "N34_union": len(u34),
    "sharpness_equalities": sharpness[:3],
}
print(summary)
