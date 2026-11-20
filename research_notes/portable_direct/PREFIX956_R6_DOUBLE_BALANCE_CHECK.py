#!/usr/bin/env python3
"""PREFIX-956 exact core-ensemble theorem checker; Python >=3.10, no packages."""

def floor_sum(n: int, m: int, a: int, b: int) -> int:
    total = 0
    while True:
        if a >= m:
            total += n * (n - 1) // 2 * (a // m)
            a %= m
        if b >= m:
            total += n * (b // m)
            b %= m
        y = a * n + b
        if y < m:
            return total
        n, b = divmod(y, m)
        m, a = a, m

def counts(p: int, r: int) -> dict:
    assert 3 <= p and 2 <= r <= p-1
    H, N, K = 1 << (p-1), 1 << (p-2), 1 << (r-1)
    max_k = (1 << r) - 1
    low = N * K * (p-2) // 2
    top = sum(floor_sum(N, H, 2*k, k) - 2 * floor_sum(N, 2*H, 2*k, k)
              for k in range(1, 1 << r, 2))
    special = 2 * (K-1)
    L = (H-1) // max_k
    exceptional_moduli = 2 * ((L+1)//2)
    return dict(p=p, r=r, H=H, moduli=N, cores=K, lower_zero_count=low,
                top_zero_count=top, special_source_count=special,
                all_named_source_count=low+top+special,
                all_top_one_moduli=exceptional_moduli)

def test_small() -> int:
    checked = 0
    for p in range(3, 12):
        H = 1 << (p-1)
        for r in range(2, p):
            ks = range(1, 1 << r, 2)
            K = 1 << (r-1)
            top = 0
            for u in range(1, H, 2):
                a = H+u
                assert sum((((k*a >> j) & 1) == 0)
                           for k in ks for j in range(1, r)) == (r-1)*K//2
                z = sum((((k*a >> (p-1)) & 1) == 0) for k in ks)
                assert (z == 0) == (((1 << r)-1) * min(u, H-u) < H)
                top += z
                checked += 1
            result = counts(p, r)
            assert top == result['top_zero_count']
            assert sum(((1 << r)-1)*min(u, H-u) < H
                       for u in range(1, H, 2)) == result['all_top_one_moduli']
    return checked

if __name__ == '__main__':
    import json
    tested = test_small()
    full = counts(19, 13)
    assert full['lower_zero_count'] == 4_563_402_752
    assert full['top_zero_count'] == 268_098_436
    assert full['all_named_source_count'] == 4_831_509_378
    assert full['all_top_one_moduli'] == 32
    print('small_all_cases_verified=', tested)
    print(json.dumps(full, sort_keys=True, indent=2))
