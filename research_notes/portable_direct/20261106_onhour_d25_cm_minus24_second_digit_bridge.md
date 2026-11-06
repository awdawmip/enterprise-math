# D25 — explicit p² Gauss-to-CM Legendre bridge, retaining the tail

2026-11-06 · TASK_RESEARCH author-side · exact theorem with finite verification; UNREVIEWED / NOT_ADMITTED; no Source CLAIM/run/admission.

Frozen D25 scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This directly consumes the preceding CM(-24) uniform zero-channel result at commit `32838336446e9498f47f087f2401c33e62a2d8df`. The mother target `Delta_p-R_p=0 (mod p)` for `p≡13,19 (mod24)` remains OPEN; native p373 #1559 remains NOT_RUN.

## Theorem — two-source first p-adic correction (all p=6m+1>3)

Let `p=6m+1` be any prime, `u²=1/2`, and let all factorial, harmonic, and rational denominators below be interpreted as units of `Z_(p)`. Define

`S_p = sum_{n=0}^{p-1} d_n`, with `d_n=(1/6)_n(1/3)_n/[2^n(n!)²]`;

`f_n=binom(m,n)binom(2m,n)/2^n` for `0<=n<=m`;

`A_n=H_m-H_{m-n}`, `B_n=H_{2m}-H_{2m-n}`, with `H_r=sum_{i=1}^r 1/i`;

and for `m+1<=n<=2m`,

`b_n=(-1)^{m+n} m! (2m)! (n-m-1)! / [6 (2m-n)! 2^n (n!)²] mod p`.

Set `C_param=(1/6)sum_{n=0}^m f_n(B_n-A_n)` and `C_tail=sum_{n=m+1}^{2m}b_n` in `F_p`. Then

**`S_p ≡ P_{2m}(u)+p(C_param+C_tail) (mod p²)`.**

The expression `P_{2m}(u)` is even in `u`; it has a well-defined value in `Z_(p)` for `u²=1/2` by polynomial evaluation (or its three-term recurrence). The theorem preserves the distinct **parameter-drift** and **truncation-tail** signed sources; their sum may cancel without either source vanishing.

## Proof

The first Gauss factor is the rational hypergeometric coefficient `d_n`. Since `p=6m+1`,

`1/6=-m+p/6`, `1/3=-2m+p/3`, `m+1/2=-2m+p/2`.

The terminating Legendre identity is exact over the rationals:

`P_{2m}(sqrt(1-z))={}_2F_1(-m,m+1/2;1;z)`.

At `z=1/2`, its summand `e_n=(-m)_n(m+1/2)_n/[2^n(n!)²]` vanishes for `n>m`. For `0<=n<=m`, expanding each nonzero factor to first order in p gives the exact congruences

`d_n ≡ f_n [1-p(A_n/6+B_n/3)] (mod p²)`,

`e_n ≡ f_n [1-p B_n/2] (mod p²)`.

Consequently `d_n-e_n ≡ (p/6) f_n(B_n-A_n)` for `n<=m`.

For `m<n<=2m`, the `j=m` factor of `(1/6)_n` is exactly `p/6`, and no factor in `(1/3)_n` is yet divisible by p. Dividing by p and reducing each remaining factor gives **`d_n/p≡b_n (mod p)`**. For `2m<n<p`, each numerator Pochhammer has a p-factor, so `d_n≡0 (mod p²)`. Adding these three *disjoint indexed ranges* proves the formula. No analytic convergence or floating approximation is involved.

On the D25 target classes `p≡13,19 (mod24)`, the preceding CM(-24) theorem proves `P_{2m}(u)≡0 (mod p)`. The present formula therefore expresses the exact **divided first digit**

**`S_p/p ≡ P_{2m}(u)/p + C_param + C_tail (mod p)`**,

where all three terms have explicit integer/modular evaluation. The p-adic scalar `P_{2m}(u)/p` is well-defined on these primes because the Legendre polynomial evaluated at `u²=1/2` belongs to `Z_(p)` and vanishes modulo p. This is a concrete computable input to the pending `(S_p/p)K_p ≡ 1+2pJ_p (mod p²)`, not itself that full identity.

## Independent exact checks

Two separate modular computations evaluate `S_p mod p²` from the original Gauss coefficient recurrence and `P_{2m}(u) mod p²` from the Legendre three-term recurrence. A third evaluator computes `C_param,C_tail` using factorial and harmonic residues. All 80 primes `p≡1 (mod6)` with `7<=p<=997` passed with zero assertion failures.

| p | S mod p² | P mod p² | C_param mod p | C_tail mod p | (S-P)/p mod p |
|---:|---:|---:|---:|---:|---:|
| 7 | 23 | 37 | 4 | 1 | 5 |
| 13 | 143 | 26 | 8 | 1 | 9 |
| 19 | 152 | 76 | 8 | 15 | 4 |
| 31 | 858 | 858 | 6 | 25 | 0 |
| 67 | 4087 | 1876 | 56 | 44 | 33 |
| 139 | 11398 | 8062 | 23 | 1 | 24 |
| 373 | 8952 | 17158 | 273 | 78 | 351 |
| 997 | 912255 | 471581 | 648 | 791 | 442 |

These illustrate why silently identifying `S_p` with the CM Hasse polynomial *modulo p²* loses a nonzero arithmetic correction and obscures signs. The mod-p identification remains exact.

The checker is `d25_cm_minus24_second_digit_bridge_check_20261106.py`. No previous proof or experiment is reclassified as a new native Result.

**Next exact action:** combine the explicit `S_p/p` formula with `K_p mod p²` and the existing SIGNED triangular cutoff `J_p`; seek an identity `(S_p/p)K_p ≡ 1+2pJ_p modp²` for target p, using p=13/19 as exact nonzero-boundary test cases. Preserve original native p373 H0/B0 #1559 and independent reviewer requirements.
