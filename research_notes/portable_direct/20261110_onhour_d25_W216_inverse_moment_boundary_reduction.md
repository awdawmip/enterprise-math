# D25 / W216 — exact inverse-moment telescoping and terminal-boundary reduction

Date: 2026-11-10 (Asia/Hong_Kong); role: TASK_RESEARCH, logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`, distinct from Maintenance. Status: AUTHOR_SIDE / EXACT_ALGEBRAIC_IDENTITY_PROVED / NINE_EXACT_PRIME_CHECKS / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN.

Parent Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Consume the accepted original source-port alignment (2026-10-26), earlier W216 terminal-valuation theorem, signed Clausen cutoff and streaming certificate. Do not recredit the preceding results.

## 1. Exact new finite identity, for arbitrary n

Set, over `Q`,

`a_k = (1/2)_k (1/3)_k (2/3)_k / [2^k(k!)^3] = binom(2k,k)^2 binom(3k,k)/216^k`.

The **correct** coefficient ratio is

`a_(k+1)/a_k = (2k+1)(3k+1)(3k+2) / [36(k+1)^3]`.

Define the rational inverse-moment weight

`d_k = -(k-1)(6k+5)/[3(k+1)^2] = -2 + 13/[3(k+1)] - 2/[3(k+1)^2]`.

For every integer `n>=1`, the following is an exact equality of rational numbers:

```
 sum_(k=0)^(n-1) (6k+1)a_k
   = sum_(k=0)^(n-2) d_k a_k + (7-6n)a_(n-1).      (IM-EXACT)
```

In particular, the right sum is empty for n=1, and `d_1=0`.

**Proof.** Let `T_k=-12k a_k`. The coefficient ratio gives, identically,

`T_(k+1)-T_k = [(6k+1)-d_k]a_k`,

since `(6k+1)+12[(k+1)a_(k+1)/a_k-k] = -(k-1)(6k+5)/[3(k+1)^2]`. Summing over k=0,...,n-1 produces `T_n-T_0=-12na_n`. The final `k=n-1` term and this boundary combine, again by the same recurrence, as

`d_(n-1)a_(n-1)-12n a_n=(7-6n)a_(n-1)`.

No asymptotic approximation or congruence is used. This establishes IM-EXACT over Q.

## 2. The p^3 original-LIFT reduction and the p^4 boundary charge

Let p>5 be prime and `S_p=sum_(k=0)^(p-2) d_k a_k` in `Z_(p)`. Each denominator k+1 in this range is a p-unit. The previously proved original W216 terminal valuation is

`v_p(a_(p-1))=3`, with `a_(p-1) = -p^3 (mod p^4)`.

Apply IM-EXACT at n=p:

```
  W_p = S_p + (7-6p)a_(p-1)                        (EXACT over Q)
  W_p = S_p                           (mod p^3)     (IM3)
  W_p = S_p - 7p^3                    (mod p^4).    (IM4)
```

These equations are valid for every prime p>5; the terminal contribution is retained exactly in IM-EXACT and IM4. In the frozen target classes p≡13,19 (mod 24), consume the **previously established** signed original interface `Delta_p-R_p = (W_p-p)/p^2 (mod p)`, including the original ordered Clausen cutoff Q and R. Therefore the remaining original hard target has the following **new derivative-free equivalent certificate**:

```
  Delta_p - R_p = (S_p-p)/p^2 (mod p),              (IM-LIFT)
  S_p = -1/3 * sum_(k=0)^(p-2)
            [(k-1)(6k+5)/(k+1)^2] a_k.
```

The p-local division in IM-LIFT is legal because the accepted prior second-order congruence gives `p^2 | (W_p-p)` and IM3 transports it to S. The transformation removes the growing linear theta-weight `6k+1` without changing the original signed Delta/R observer; the single remaining inverse-moment sum has p-unit denominators and ends before the p-divisible denominator k+1=p.

The fourth digit is not compressed away: whenever the target p^3 congruence holds, the S-side fourth residue is exactly the W-side fourth residue plus 7 modulo p. This is a signed **terminal boundary charge** produced by the operator change.

## 3. Bounded-degree polynomial one-term telescopers: exact obstruction

Write p=6m+1 and work in `F_p`, for p>=13. On the full grade-0 range `0<=k<=2m`, the original a_k is a p-unit. Consider the narrow Gosper/WZ-style ansatz `T_k=k^3 P(k) a_k`, with `P in F_p[k]` of degree d. Suppose it would produce the *full original weighted term* pointwise:

`T_(k+1)-T_k = (6k+1)a_k (mod p)` for every `0<=k<=2m`.

After division by the p-unit a_k and multiplication by the p-unit `36`, this forces

```
 D_P(k) = (2k+1)(3k+1)(3k+2) P(k+1)
          -36k^3 P(k) -36(6k+1) =0 (mod p)
```

at **2m+1 distinct residues**. The polynomial D_P has degree d+3, with nonzero leading coefficient `-18 lc(P)` in F_p (p>5); if P=0, the displayed condition also fails. A polynomial of degree <=2m cannot have 2m+1 roots. Therefore the ansatz requires

`d >= 2m-2 = (p-1)/3 - 2.`                     (DEGREE-BARRIER)

The lower bound holds even if P depends on p. In particular, no uniformly fixed-degree polynomial P(k) can yield this grade-0 pointwise telescoper for arbitrarily large target primes. This is a **scoped no-go for the stated polynomial ansatz only**, not for rational WZ, parameter-contiguous relations or telescoping after summing the grades.

The successful construction `T_k=-12k a_k` corresponds to the rational multiplier `P(k)=-12/k^2` and escapes this bound; its non-negligible order-p endpoint at k=p is repaired using the last-index residue, restoring the original p^3 precision. This is an explicit BRC observer/operation example: quotienting away the boundary before recombination would lose a signed residue.

## 4. Independent exact validations

Author checker: `research_notes/portable_direct/d25_w216_inverse_moment_boundary_20261110.py`. Exact integers, inverses only of declared p-unit denominators and no floats. Tests at p = 13,19,37,43,61,67,373,10069,10099, both original residue classes. For all p, directly check IM-EXACT modulo p^4, IM3, IM4 and the p^3 LIFT-equivalent residue. For every p<=373 in that set, independently reconstruct every a_k using the raw integer binomial expression (not the Pochhammer recurrence). The symbolic telescoping rational identity was independently simplified to zero.

Selected raw finite witnesses:

| p | class mod24 | W_p mod p^4 | S_p mod p^4 | (W-p)/p^3 mod p | (S-p)/p^3 mod p |
|---:|---:|---:|---:|---:|---:|
| 13 | 13 | 19786 | 6604 | 9 | 3 |
| 19 | 19 | 82327 | 19 | 12 | 0 |
| 373 | 13 | 11832087049 | 12195352868 | 228 | 235 |
| 10069 | 13 | 8114682266998110 | 8121828169107673 | 7949 | 7956 |
| 10099 | 19 | 4084960171195933 | 4092170136198026 | 3966 | 3973 |

Each difference of fourth-digit residues is +7 mod p, as IM4 requires. These finite observations check the implementation; the all-n identity, terminal transport and degree barrier are algebraically proved. No new independent review or native H0/B0 observation is claimed.

## 5. Source and BRC continuation

BRC resolution: `COMPOSE_APPLIED`. Carrier: original integer k, signed weight, Pochhammer/binomial source, p-local valuation, original ordered Q/R cutoff, operator T, endpoint/terminal charge and precision horizon p^4. The quotient to the derivative-free S retains the original Delta-R observable through p^3 (IM-LIFT), but not the fourth digit without the explicit -7 correction (IM4). External rational hypergeometric arithmetic is not a native X6 or H0/B0 Frobenius claim.

This is a **strict reduction in theta/weight complexity** of the still-open LIFT scalar certificate, not a proof of all-prime `S_p=p (mod p^3)`. Next scientific action: investigate a finite rational WZ/parameter-contiguous certificate for the reduced inverse-moment weight d_k, retaining the endpoint charge and both residue classes; test at p=13,19,373 and existing large-prime witnesses before asserting a universal cancellation. Keep the native fixed original-class H0/B0 `[X]U mod139129`, rank, semilinear eta, signed kappa, Delta-R and independent reproduction pending under existing Issue #1559, `PENDING_OWNER/NOT_RUN`. No claim of Source-native checkpoint, winning CLAIM, run, formal Result or mathematical admission.
