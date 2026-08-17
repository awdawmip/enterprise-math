#!/usr/bin/env python3


def bracket_kappa(levels: int):
    if not isinstance(levels, int) or levels < 0:
        raise ValueError("levels must be a nonnegative integer")
    L, U = 3, 4
    n = 0
    for _ in range(levels):
        M = L + U
        rhs = 12 * (1 << (2 * n + 2))
        if M * M < rhs:
            L, U = M, 2 * U
        else:
            L, U = 2 * L, M
        n += 1
        if U - L != 1:
            raise AssertionError("dyadic width invariant failed")
        scale2 = 1 << (2 * n)
        if not (L * L < 12 * scale2 < U * U):
            raise AssertionError("root bracket invariant failed")
    return {"level": n, "lower_num": L, "upper_num": U, "den": 1 << n}


if __name__ == "__main__":
    import json
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    print(json.dumps(bracket_kappa(n), sort_keys=True))
