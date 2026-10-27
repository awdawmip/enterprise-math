# D25/LIFT R43–R44 — Reflected-rank valuation pairing and Wilson-free first jet

2026-10-27 Asia/Hong_Kong. Portable TASK_RESEARCH author continuation (logical lane `chatgpt-research-hourly-enterprise-math-20260923`, **not** an assertion of native execution authorization). Exact task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; parent D25/LIFT/JT2 OPEN; frozen **scientific** Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY`.

## Exact unchanged source and typed observer

For any prime `p=6m+1>=7` and integer `1<=k<=p-1`, retain R39–R42's original weighted rational sources

```text
w_k=(6k+1)(2k)!(3k)!/((k!)^5 216^k),
s_k=(8k+1)(4k)!/((k!)^4 2304^k),
tau_k=(k! (4k)!/((2k)! (3k)!)) (3/32)^k,
s_k/w_k=((8k+1)/(6k+1))tau_k  (exact in Q).
```

Here `k` is a summation rank, **not** a native X6 axis. Define `q_a=floor(ak/p)`, `r_a=ak-pq_a` for `a=2,3,4`. Because `1<=k<p` and `p>=7`, each `r_a` lies in `1,...,p-1`. Put

```text
e_k=q_4-q_2-q_3,
u_(p,k)=p^(-e_k) tau_k  (a p-adic unit),
C_(p,k)=(-1)^e_k [q_4!(3-q_4)!]/[q_2!(1-q_2)!q_3!(2-q_3)!].
```

The fraction in `C` has denominator prime to `p`. These are **unweighted kernel** observables. The original linear weights and W/S provenance remain additional labelled coordinates: removing weights for an auxiliary observation does not remove their special valuations.

## R43-A. Six-interval exact valuation staircase and its rank involution

Legendre's formula, for `k<p`, gives

```text
v_p(tau_k)=floor(4k/p)-floor(2k/p)-floor(3k/p)=e_k
          = +1 when p/4<k<p/3,
          = -1 when 2p/3<k<3p/4,
          =  0 otherwise (1<=k<p).
```

Endpoints are never integer ranks because `p>=7` is prime to 2, 3, 4. There are exactly `ceil(m/2)` ranks of each exceptional sign. For the **literal** reflection `k -> p-k` (not `p-1-k`),

```text
q_a(p-k)=a-1-q_a(k),  r_a(p-k)=p-r_a(k),  e_(p-k)=-e_k.
```

Thus `tau_k tau_(p-k)` has valuation zero. The positive mismatch `p/4<k<p/3` pairs bijectively with R41's negative mismatch `2p/3<k<3p/4`; the earlier R39/R41/R42 three-regime high-rank result is **consumed**, not recredited. The new part is the global exact reflection law and lower-band classification.

## R43-B. Closed first residue of the pair

For `F(n)=n!/p^floor(n/p)`, and `n=qp+r <4p`, `0<=r<p`,

```text
F(n) = q! [(p-1)!]^q r! times p-unit correction products;
F(n) = (-1)^q q!r! (mod p).
```

Consequently `u_(p,k)= (3/32)^k k! F(4k)/[F(2k)F(3k)]` and reflection yields

```text
u_(p,k)u_(p,p-k)
 = (3/32)^p * k!(p-k)! * F(4k)F(4(p-k))
   / [F(2k)F(2(p-k))F(3k)F(3(p-k))].
```

Use the elementary Wilson reflection `r!(p-r)! = (-1)^r r (mod p)`, the `q_a` complements, `r_a=ak (mod p)`, and Fermat `(3/32)^p=3/32 (mod p)`. The factorial sign is `(-1)^{k+r_4-r_2-r_3}=(-1)^{e_k}`. Also `k r_4/(r_2r_3)=2/3 (mod p)`. Therefore **for every** `1<=k<p`,

```text
u_(p,k)u_(p,p-k) = C_(p,k)/16 (mod p).                 (R43)
```

The right-hand side is rank-independent *within each band*:

| Rank band | e_k | C_(p,k) | Pair residue |
|---|---:|---:|---:|
| 0<k<p/4, and 3p/4<k<p | 0 | 3 | 3/16 |
| p/4<k<p/3, and 2p/3<k<3p/4 | +1 or -1 | -1 | -1/16 |
| p/3<k<2p/3 | 0 | 2 | 1/8 |

A corresponding global multiplicative certificate is obtained by pairing all `3m=(p-1)/2` unordered reflected ranks. The counts are `floor(3m/2)` first-band pairs, `ceil(m/2)` exceptional pairs and `m` middle pairs. Hence

```text
prod_(k=1..p-1) u_(p,k)
 = (-1)^ceil(m/2) 3^floor(3m/2) 2^(-11m) (mod p).   (R43-global)
```

This is a product invariant, **not** a claim about the required W/S additive compensation.

## R44. Wilson-quotient-free first jet modulo p²

Write `H_n=sum_(j=1..n)1/j` in `Z_(p)`, with `H_0=0`, and for a p-adic unit `x` define `q_p(x)=(x^(p-1)-1)/p (mod p)`. In particular

```text
Q_* = q_p(3/32) = q_p(3)-5q_p(2) (mod p).
J_(p,k) = Q_* + H_(k-1) + 4H_(r_4-1)
                 -2H_(r_2-1) -3H_(r_3-1)  (mod p).
```

**Theorem (all p=6m+1>=7, all 1<=k<p):**

```text
u_(p,k)u_(p,p-k)
 = [C_(p,k)/16] [1+p J_(p,k)]  (mod p²).            (R44)
```

**Proof.** The exact factorial block decomposition for `n=qp+r<4p` gives, modulo `p²`,

```text
F(qp+r)=(-1)^q q!r! [1+pq(H_r-Q_p)] (mod p²),
Q_p=((p-1)!+1)/p.
```

Indeed every full block's linear correction contains `pH_(p-1)`, which vanishes modulo `p²` by `H_(p-1)=0 (mod p)`. Moreover

```text
r!(p-r)! = (-1)^r r [1+p(H_(r-1)-Q_p)] (mod p²),
H_(p-r)=H_(r-1) (mod p).
```

In the reflected ratio the exponents of the full factorial/Wilson corrections cancel, since `(4-1)-(2-1)-(3-1)=0`. The remaining first-order harmonic correction from the four reflected factorial pairs and the block offsets is

```text
H_(k-1)+4H_(r_4-1)-2H_(r_2-1)-3H_(r_3-1)
 + q_4/r_4-q_2/r_2-q_3/r_3.
```

Replacing the exact residue ratio `k r_4/(r_2r_3)` by its leading `2/3` adds

```text
-q_4/(4k)+q_2/(2k)+q_3/(3k) (mod p)
```

to the correction. These extra terms cancel because `r_a=ak (mod p)`. Finally `(3/32)^p=(3/32)(1+pQ_*) (mod p²)`. The displayed `J_(p,k)` follows; in particular **the Wilson quotient disappears**. QED.

## Evidence and strict scope

Companion exact standard-library program: `20261027_hourly_d25_reflected_kernel_r43_r44_check.py`. Actual author execution: **80** primes `7<=p<=997`, `p=1 mod6`; **36,588** ranks; **18,294** reflected unordered pairs; **66** independently evaluated exact `Fraction` kernel instances at `p<=31`. All assertions PASS, including every modulo-`p²` R44 pair, valuation antisymmetry and the global product. Examples:

```text
p=181, k=46, p-k=135: (u_k,u_(p-k)) mod p=(152,126),
pair mod p=147=-1/16, pair mod p²=2681, J_(p,k)=125.
p=373, k=94: pair mod p=303, pair mod p²=136448, J=115.
```

The all-prime statements rely on the above algebraic proof, not finite interpolation. No native CM/Frobenius/H0/B0 or independent-review result is claimed.

BRC `COMPOSE_APPLIED`: carrier consists of rank pair `(k,p-k)`, original W and S source labels, valuation `e_k`, regularized units, multiplicative observer and future additive source observer kept separate. Multiplicative equality is **not** permission to erase original linear weights, special `6k+1`/`8k+1` zeros, sign/port data, Green endpoints, positive infinity or the original unchanged-input WZ residual. A summed supercongruence remains unproved.

**Next smallest scientific unit:** evaluate the R44 harmonic first jet against the actual low-half `p²`-divided W/S difference and R36 finite Green boundary adjoint; test whether a *source-labelled cross-rank additive telescoper* exists, preserving the isolated `p=181` S-tail zero. Retain fixed `z=2` six-channel Hasse J/E `3+2+1` ports, finite boundaries, positive-infinity/high-high ports, original `H0/B0`, `[X]U mod p²`, semilinear Frobenius `eta/kappa`, native `p=373` and independent Driver review. D25/LIFT/JT2 remains OPEN; old predecessor CLAIM repair belongs to existing #1558. No role-bound CLAIM, OPEN, Source checkpoint, Result or review is asserted.
