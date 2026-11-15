# R749SRS — Sharp finite phase decoding and operation-scoped minimal carriers

2026-11-16 (Asia/Shanghai) · AUTHOR_EXACT_NOT_REVIEWED

## Scientific scope and exact inputs

Continuation: R749SQR, immutable scientific note at awdawmip/enterprise-math@833a27613a2580f1e7b9ec4f6663ddbe9aa22aa2. Frozen auxiliary Walsh scientific input remains awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This is the independent positive *labeled-source* model, rather than a claimed native X6 spatial state, signed BRC port, or heartbeat-time event. The allowed operation here is a shift of the integer cutoff.

Fix weights s=(1,1,2,3,6), with the first weight-one source marked. For every integer r≥1 define

\[
\Omega_r=\{k\in\mathbb Z_{\ge0}^{5}:k_1+k_2+2k_3+3k_4+6k_5\le r-1\},\
C_r=|\Omega_r|,\quad T_r=\sum_{k\in\Omega_r}k_1,\quad E_r=T_r/(rC_r).
\]

Reuse the previously established smooth fourth-order expression and periodic leading correction:

\[
H_4(r)=\frac16+\frac1{2r}-\frac{115}{36r^2}+\frac{115}{6r^3}-\frac{16315}{108r^4},
\quad R(r)=r^4(E_r-H_4(r)),
\]
\[
P(r)=\frac1{36}(455,-295,-25,185,-25,-295)_{r\bmod6}.
\]

For an integer shift t≥0, define the ideal signature S_{a,t}=(P(a),P(a+t)), a∈Z/6Z, and the actual read Y_t(r)=(R(r),R(r+t)). The **specified decoder** chooses the closest *distinct* ideal signature under the max norm and returns its phase fiber. Equal ideal signatures are a single class; a tie between distinct signatures is a decoding failure.

## Theorem A — exact minimal phase carrier for restricted future shifts

For the ideal periodic observer P and the future-operation semigroup consisting only of increments by multiples of t, two phase classes a,b can be identified precisely when P(a+nt)=P(b+nt) for all integers n≥0. For each t modulo 6, this equivalence is determined by the first two reads:

| t mod 6 | Exact phase fibers of the smallest future-sufficient quotient | Number of states |
|---:|---|---:|
| 0 | {0}, {1,5}, {2,4}, {3} | 4 |
| 1 | all six singletons | 6 |
| 2 | all six singletons | 6 |
| 3 | {0}, {1,5}, {2,4}, {3} | 4 |
| 4 | all six singletons | 6 |
| 5 | all six singletons | 6 |

**Proof.** For t=0, each future read is the current value, and P has exactly the four displayed fibers. For t=3, future readings alternate between a and a+3; the displayed six values show precisely the same four pair fibers. For t=1,2,4,5, direct rational substitution shows that the six ordered pairs S_{a,t} are pairwise distinct, so two reads separate every class. Equality of full future outputs is exactly the deterministic future-observer equivalence; any smaller quotient would merge two distinguishable sequences. QED.

The four-state quotient for t=0 or t=3 is sufficient **for this observer and this allowed operation family**. If shift by one is later admitted, all six phase classes are needed. This is a concrete observer/future-operation-specific residual-retention certificate, consistent with the joint-relation preservation requirement.

## Theorem B — exact sharp all-integer thresholds

For each t=0,...,5, let tau_t denote the smallest integer such that the max-norm nearest-signature decoder returns the correct ideal phase fiber uniquely for **every** integer r≥tau_t. Then

\[
\boxed{(\tau_0,\tau_1,\tau_2,\tau_3,\tau_4,\tau_5)
=(477,398,384,204,380,393).}
\]

| Shift t | Distinct signatures | Minimal signature separation in max norm | Sharp tau | Last failing r |
|---:|---:|---:|---:|---:|
| 0 | 4 | 35/6 | 477 | 476 |
| 1 | 6 | 35/6 | 398 | 397 |
| 2 | 6 | 15/2 | 384 | 383 |
| 3 | 4 | 15/2 | 204 | 203 |
| 4 | 6 | 15/2 | 380 | 379 |
| 5 | 6 | 35/6 | 393 | 392 |

Thus the adjacent two-read decoder (t=1) now has its **exact sharp threshold 398**, replacing the earlier sufficient threshold 512. A two-step cutoff shift (t=2) recovers the full six-phase state for every r≥384; the t=3 observer recovers its correct four-state quotient for every r≥204.

### Proof over the infinite tail

The strict-prefix and marked-source generating functions are

\[
F(z)=\frac{z}{1-z}\prod_{s_i\in(1,1,2,3,6)}\frac1{1-z^{s_i}},
\qquad
N(z)=F(z)\frac{z}{1-z}.
\]

All poles are sixth roots of unity. Hence C_r and T_r, on each fixed r mod 6 class, are exactly quasipolynomials of degrees at most five and six. For each phase a select its first r_a in [512,517], and interpolate C_{r_a+6n} using six successive exact integers and T_{r_a+6n} using seven. The pole-degree bounds make these polynomials valid for all n≥0.

With r=r_a+6n, introduce

\[
B_a(n)=r^3T_r-C_r(r^4H_4(r)+P(a)),\qquad
U_a(n)=\frac{35}{12}C_r-B_a(n).
\]

The attached exact rational certificate reconstructs all six triples C,B,U and verifies that **every coefficient** of each polynomial, in powers of n, is strictly positive. The degree of B is four after exact cancellation, the degrees of C and U are five. Thus for every integer r≥512,

\[
0<R(r)-P(r)=B_a(n)/C_r<35/12.
\]

The same is true for R(r+t) whenever t≥0. The smallest max-norm distance between two *distinct* ideal pairs is 35/6 (for t=0,1,5) or 15/2 (for t=2,3,4). Each actual two-coordinate read is within strictly less than 35/12 of its true signature. Since the distinct-signature separation is at least 35/6, the triangle inequality proves the true signature uniquely nearest for every r≥512.

### Proof across the finite gap and sharpness witnesses

For every t∈{0,1,2,3,4,5}, the companion program evaluates every integer 1≤r≤511 by integer weighted dynamic programming and exact Fraction arithmetic. It enumerates distinct ideal pairs, computes all max-norm distances, and checks that the true signature has a **strictly positive distance margin** at every r from tau_t through 511. In each of the six cases it also records an *incorrect* nearest-signature answer at r=tau_t−1. The six exact rational witnesses and the minimum positive gap in each finite bridge are stored in the JSON evidence.

For the adjacent-read witness r=397, the true phase is 1 but the decoder returns phase 2:

\[
d_{\mathrm{true}}=11245097/2990412
>11182993/2990412=d_{\mathrm{wrong}}.
\]

The smallest exact finite-bridge margin for t=1 occurs at r=403 and equals 8088590/91448649. An all-tail threshold less than tau_t would contain the explicitly failing r=tau_t−1. The finite exhaustive check plus infinite coefficientwise bound proves both **universal sufficiency** and **sharpness** for the stated rule. QED.

## Reproducible evidence and next question

The attached dependency-free Python certificate uses integers and fractions only. It independently enumerates the first 24 prefix levels by recursion, reconstructs six polynomial positivity certificates, and checks 3066 shift/finite-r combinations across r=1,...,511. It outputs the complete six-shift threshold/phase-fiber table, rational witness distances, minimum exact finite-bridge gaps, and positivity evidence. Executed locally: **PASS**. Mathematical review status: **AUTHOR_EXACT_NOT_REVIEWED**.

Scientific boundaries: the exact source-label population and weights remain intact; a quotient is asserted only for its explicitly declared ideal observer and future-shift semigroup. No signed provenance, BRC branch transport, or native heartbeat operation is inferred from this auxiliary counting calculation.

Next worthwhile inquiry: compute the sharp perturbation/noise tolerance of each nearest-signature decoder and test whether three or more future observations yield lower exact all-tail decoding thresholds; investigate a separately typed signed/provenance BRC interface before native correspondence claims.
