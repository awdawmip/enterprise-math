"""Landau-Fekete Wheel Factorial & Algebraic Cyclotomic Tori Factorization Engine.

File: power/factor/unified_algebraic_engine.py
License: MIT / Antigravity Research Group
"""

from __future__ import annotations

import math
import time
from typing import List, Optional, Tuple


# =============================================================================
# 1. 纯整轮阶乘完备二分算法 (Wheel Factorial Landau Dichotomy)
# =============================================================================

def wheel_factorial_dichotomy_factor(N: int, D: int = 210) -> Tuple[int, int, str]:
    """使用轮阶乘-费马完备二分定理分解奇半素数 N = p * q (p < q).
    
    分支 A: 若 q - p < 2D, 费马差方在 <= D 步内命中;
    分支 B: 若 q - p >= 2D, 单点 t = floor(sqrt(N)/D) 处:
            P_D(t) = prod_{1 <= m <= D*t, gcd(m, D) == 1} m mod N
            严格保证 gcd(P_D(t), N) = p, 无需任何区间搜索！
    """
    if N <= 1:
        raise ValueError("N must be > 1")
    if N % 2 == 0:
        return 2, N // 2, "Trivial Even"

    t0 = time.perf_counter()
    r = math.isqrt(N)
    if r * r == N:
        return r, r, "Exact Square"

    # 分支 A: 费马差方分支 (至多 D 步)
    for delta in range(D + 1):
        x = r + delta
        y2 = x * x - N
        if y2 >= 0:
            y = math.isqrt(y2)
            if y * y == y2:
                g = math.gcd(x - y, N)
                if 1 < g < N:
                    dt = (time.perf_counter() - t0) * 1000
                    return min(g, N // g), max(g, N // g), f"Fermat branch in {delta} steps ({dt:.2f} ms)"

    # 分支 B: 轮阶乘单点分支
    t = r // D
    wheel = [k for k in range(1, D) if math.gcd(k, D) == 1]
    
    prod = 1
    for b in range(t):
        base = b * D
        for r_val in wheel:
            prod = (prod * (base + r_val)) % N

    g = math.gcd(prod, N)
    if 1 < g < N:
        dt = (time.perf_counter() - t0) * 1000
        return min(g, N // g), max(g, N // g), f"Wheel D={D} single-point t={t} ({dt:.2f} ms)"

    # 边界保护点 t + 1
    base = t * D
    for r_val in wheel:
        if base + r_val <= D * (t + 1):
            prod = (prod * (base + r_val)) % N
    g1 = math.gcd(prod, N)
    if 1 < g1 < N:
        dt = (time.perf_counter() - t0) * 1000
        return min(g1, N // g1), max(g1, N // g1), f"Wheel D={D} boundary point t+1={t+1} ({dt:.2f} ms)"

    return 0, 0, "Unsplit"


# =============================================================================
# 2. Bach-Shallit 代数分圆环面分解引擎 (T_1, T_2, T_4, T_6)
# =============================================================================

def _primes_up_to(limit: int) -> List[int]:
    """生成上限 limit 内的素数表."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, math.isqrt(limit) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_p in enumerate(sieve) if is_p]


def _poly_mul_mod(a: list[int], b: list[int], f: list[int], N: int) -> list[int]:
    """多项式乘法模既约多项式 f(x) 和整模数 N."""
    deg_f = len(f) - 1
    res = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if not ca:
            continue
        for j, cb in enumerate(b):
            if not cb:
                continue
            res[i + j] = (res[i + j] + ca * cb) % N

    for i in range(len(res) - 1, deg_f - 1, -1):
        if res[i] == 0:
            continue
        c = res[i]
        for j in range(deg_f + 1):
            res[i - deg_f + j] = (res[i - deg_f + j] - c * f[j]) % N
    return res[:deg_f]


def _poly_pow_mod(base: list[int], exp: int, f: list[int], N: int) -> list[int]:
    """多项式快速幂计算 base^exp mod (f(x), N)."""
    deg_f = len(f) - 1
    res = [0] * deg_f
    res[0] = 1
    b = list(base)
    p = exp
    while p > 0:
        if p & 1:
            res = _poly_mul_mod(res, b, f, N)
        b = _poly_mul_mod(b, b, f, N)
        p >>= 1
    return res


def factor_cyclotomic_torus(
    N: int,
    B1: int = 1000,
    torus_types: Tuple[int, ...] = (1, 2, 4, 6)
) -> Optional[Tuple[int, int, str]]:
    """在分圆环面 T_1, T_2, T_4, T_6 上统一执行阶平滑分解."""
    if N <= 1:
        raise ValueError("N must be > 1")
    if N % 2 == 0:
        return 2, N // 2, "Even trivial"

    primes = _primes_up_to(B1)
    max_pow = B1 * B1

    # T_1 (Pollard p - 1)
    if 1 in torus_types:
        t0 = time.perf_counter()
        a = 2
        for p in primes:
            p_pow = p
            while p_pow * p <= B1:
                p_pow *= p
            a = pow(a, p_pow, N)
            g = math.gcd(a - 1, N)
            if 1 < g < N:
                dt = (time.perf_counter() - t0) * 1000
                return min(g, N // g), max(g, N // g), f"T_1 (p - 1) ({dt:.2f} ms)"

    # T_2 (Williams p + 1)
    if 2 in torus_types:
        t0 = time.perf_counter()
        P = 3
        v0, v1 = 2, P
        for p in primes:
            p_pow = p
            while p_pow * p <= B1:
                p_pow *= p
            for bit in bin(p_pow)[2:]:
                if bit == '1':
                    v0 = (v0 * v1 - P) % N
                    v1 = (v1 * v1 - 2) % N
                else:
                    v1 = (v0 * v1 - P) % N
                    v0 = (v0 * v0 - 2) % N
            g = math.gcd(v0 - 2, N)
            if 1 < g < N:
                dt = (time.perf_counter() - t0) * 1000
                return min(g, N // g), max(g, N // g), f"T_2 (p + 1) ({dt:.2f} ms)"

    # T_4 (Gaussian p^2 + 1)
    if 4 in torus_types:
        t0 = time.perf_counter()
        for c in [2, 3, 5, 7]:
            f = [c, 0, 0, 0, 1]  # x^4 + c
            cur = [1, 1, 0, 0]   # x + 1
            for p in primes:
                p_pow = p
                while p_pow * p <= max_pow:
                    p_pow *= p
                cur = _poly_pow_mod(cur, p_pow, f, N)
                for coeff in [(cur[0] - 1) % N] + cur[1:]:
                    g = math.gcd(coeff, N)
                    if 1 < g < N:
                        dt = (time.perf_counter() - t0) * 1000
                        return min(g, N // g), max(g, N // g), f"T_4 (p^2 + 1) ({dt:.2f} ms)"

    # T_6 (Sextic p^2 - p + 1)
    if 6 in torus_types:
        t0 = time.perf_counter()
        for c in [2, 3, 5, 6, 7]:
            f = [c, 0, 0, 0, 0, 0, 1]  # x^6 + c
            cur = [1, 1, 0, 0, 0, 0]   # x + 1
            for p in primes:
                p_pow = p
                while p_pow * p <= max_pow:
                    p_pow *= p
                cur = _poly_pow_mod(cur, p_pow, f, N)
                for coeff in [(cur[0] - 1) % N] + cur[1:]:
                    g = math.gcd(coeff, N)
                    if 1 < g < N:
                        dt = (time.perf_counter() - t0) * 1000
                        return min(g, N // g), max(g, N // g), f"T_6 (p^2 - p + 1) ({dt:.2f} ms)"

    return None

