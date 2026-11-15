# JT2 QTF3 fixed-point: exact prime-class boundary audit

Date: 2026-11-15. Driver: EM-DVR-DEBB5E. Status: bounded independent arithmetic cross-check and a precise out-of-scope counterexample; **not** a new Native Result, review disposition or mother-objective closure.

## Source and contribution boundaries

The theorem under inspection is the historical QTF3 finite fixed-point return, authored/delivered by EM-JT2-EF9380 with finite reflection-degree proof attributed to EM-DVR-57CCCE, and a separate earlier non-author paper check attributed in the return. Its frozen Result is `RR-69FC34FA8AE1E91244F2` (Git blob `14d89853f268724d49331984b16ce2421b94bb45`). Original return: `research_returns/EMW59A_JT2_QTF3_FIXED_POINT_RETURN_EF9380_20260909.md` (blob `72941a9b14304686e279f9ec6e19eac58ad61853`). These author/contributor records are unchanged. This audit is a fresh, independently implemented finite modular computation, not an assertion of institutional or contribution-independent review.

## Exactly tested formula

For p>3 prime, with rational coefficients interpreted in Z_(p), define the *p-1-truncated* series

```math
L_p(1/2) = \sum_{k=0}^{p-1} ((1/3)_k(2/3)_k/(k!)^2) 2^{-k},
F_p(1)   = \sum_{k=0}^{p-1} ((1/6)_k(1/3)_k/(k!)^2).
```

The published theorem asserts `L_p(1/2) - F_p(1) == 0 (mod p^3)` **for p>3, p ≡ 1 (mod 6)**. No claim for all primes is present in the original Result.

A second implementation using exact `fractions.Fraction` arithmetic cross-checked the modular recurrence for p=5,7,11,13,19. No floating-point operations were used.

## Reproducible finite computation

```python
def truncated_2f1_mod(p, a_num, a_den, b_num, b_den, z_num, z_den, power=4):
    q = p**power
    z = z_num * pow(z_den, -1, q) % q
    term = 1
    total = 0
    for k in range(p):
        total = (total + term) % q
        if k == p - 1:
            break  # next factorial would not be a p-unit
        term = term * (a_num + a_den*k) * pow(a_den, -1, q) % q
        term = term * (b_num + b_den*k) * pow(b_den, -1, q) % q
        term = term * pow(k+1, -2, q) * z % q
    return total

def delta(p, power=4):
    q = p**power
    left = truncated_2f1_mod(p, 1,3, 2,3, 1,2, power)
    right = truncated_2f1_mod(p, 1,6, 1,3, 1,1, power)
    return (left-right) % q
```

Primes p ≡ 1 (mod 6): `7,13,19,31,37,43,61,67,73,79,97`. For all eleven, `delta(p,3)=0`. At the stricter p^4 precision each has a **nonzero** quotient `delta(p,4)/p^3 mod p`, respectively `6,9,4,21,11,37,47,55,23,47,27`. These are finite computations only; the all-prime theorem rests on the original proof, not these tests.

Primes p ≡ 5 (mod 6): `5,11,17,23,29,41,47,53,59,71,83,89`. For all twelve, `delta(p,3)` has exact p-adic valuation 1. In particular, the exact p=5 calculation gives

```text
L_5(1/2) ≡ 25 (mod 125)
F_5(1)   ≡ 95 (mod 125)
difference ≡ 55 (mod 125), v_5=1.
```

Thus the naive extension of the unchanged QTF3 congruence to **all** p>3 is **false** (single explicit counterexample p=5). This does not contradict the original p ≡ 1 (mod 6) theorem and does not rule out a different renormalized identity for p ≡ 5 (mod 6). Similarly, the eleven nonzero p^3 residues show that an indiscriminate upgrade to p^4 would fail already at p=7.

## Disposition

QTF3 p^3 PASS remains in its original established congruence class, with its recorded proof and contributors. This local audit adds precise boundary and sharpness examples. JT2 UR all-prime epsilon_p vanishing and the parent-line integration remain open independently.
