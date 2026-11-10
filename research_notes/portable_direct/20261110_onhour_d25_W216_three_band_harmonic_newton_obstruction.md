# D25 / W216 — exact three-band harmonic formula for the first-jet obstruction

Date: 2026-11-10 (Asia/Hong_Kong); scope: author-side portable research, **unreviewed and not admitted**.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`.
Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).
Research logical lane: `chatgpt-research-onhour-enterprise-math-20260923`.
This derivation consumes the existing all-prime p-block filtered-transfer result, without claiming any native H0/B0 execution.

## 1. Original signed observable and exact question

Let `p=6m+1 >=7` be prime and put

```text
A_k = (2k)!(3k)! / ((k!)^5 * 216^k)
W_n = sum_{k=0}^{n-1} (6k+1) A_k
B_p(a) = sum_{b=0}^{p-1} (6pa+6b+1) A_{pa+b}
C_p(a) = B_p(a)/A_a
q_j = (Delta^j C_p)(0).
```

These definitions are in the p-local rationals. A previously proved degree-filtration theorem gives
`C_p(a) = q0 + q1*a + q2*binom(a,2) (mod p^3)` for every integer `a>=0`.
The previously tested but uniformly unproved first-jet candidate is
`(q0,q1,q2) = (chi_p*p, 6*chi_p*p, 0) (mod p^3)`, where `chi_p=1` for `p=1 mod 3`.
This note **derives exact band-resolved formulas for q1 and q2** and independently checks their cancellation.
It also supplies exact counterexamples to an attempted improvement `q2=0 (mod p^4)`.

## 2. P-adic definitions retaining the actual valuation bands

Write `h_b=6b+1`, `nu_b=v_p(A_b)`, and `a_b=A_b/p^nu_b`.
For `b<p`, the complete valuation data are:

```text
band 0: 0 <= b <= 2m                 nu_b=0
band 1: 2m+1 <= b <= 3m              nu_b=1
band 2: 3m+1 <= b <= 4m              nu_b=2
band 3: 4m+1 <= b < p                nu_b=3.
```

The third band vanishes modulo `p^3`, but its label remains part of the original source.
Define `d=216^(1-p)` in `Z_p^×` and `ell=log(d)/p` in `Z_p`.
A fully finite implementation modulo `p^2` computes `t=d-1 (mod p^3)` and
`ell=((t-t^2/2) mod p^3)/p (mod p^2)`, with `d=pow(216,p-1,p^3)^(-1) mod p^3`.

For `p \nmid j`, each `j^(-s)` denotes a modular unit inverse. Put

```text
H_s(N) = sum_{1<=j<=N, p does not divide j} j^(-s).
U_b = ell + 2 H_1(2b) + 3 H_1(3b) - 5 H_1(b)
K_b = 4 H_2(2b) + 9 H_2(3b) - 5 H_2(b).
```

Use `U_b mod p^2` and `K_b mod p`; `1/2` denotes the inverse of 2 modulo p.

## 3. Proved finite three-band theorem

**Theorem.** For every prime `p=6m+1>=7`, let the following quantities be computed modulo `p^3`:

```text
L0 = p   * sum_{b=0}^{2m}   A_b [(6b+1) U_b + 6]
L1 = p   * sum_{b=2m+1}^{3m} a_b [3(6b+1) + p ((6b+1) U_b + 6)]
L2 = p^2 * sum_{b=3m+1}^{4m} a_b [5(6b+1)]

J0 = p^2 * sum_{b=0}^{2m}   A_b [((6b+1)/2)(U_b^2-K_b) + 6 U_b]
J1 = p^2 * sum_{b=2m+1}^{3m} a_b [3((6b+1) U_b + 6)]
J2 = p^2 * sum_{b=3m+1}^{4m} a_b [6(6b+1)].
```

Then, in the original p-local ring,

```text
q0 = W_p  (exactly),
q1 = L0+L1+L2+J0+J1+J2  (mod p^3),
q2 = 2(J0+J1+J2)         (mod p^3).
```

In particular the precise remaining second-difference congruence is

```text
q2 = 0 (mod p^3)  <=>  S0+S1+S2 = 0 (mod p),
S0 = sum_{b=0}^{2m}       A_b [((6b+1)/2)(U_b^2-K_b) + 6 U_b] (mod p),
S1 = sum_{b=2m+1}^{3m} (A_b/p) [3((6b+1) U_b + 6)]           (mod p),
S2 = sum_{b=3m+1}^{4m} (A_b/p^2) [6(6b+1)]                   (mod p).
```

**Proof.** The exact factorial-block identity gives

```text
A_(pa+b)/A_a =
  A_b * R_p(a) *
  product_(1<=j<=2b) (1+2pa/j) *
  product_(1<=j<=3b) (1+3pa/j) /
  product_(1<=j<=b)  (1+pa/j)^5
R_p(a)=216^((1-p)a) F(2a)^2 F(3a)/F(a)^5,
F(x)=product_(0<=u<x; 1<=j<p)(1+up/j).
```

For all p>=5, `H_1(p-1)=0 (mod p^2)` (Wolstenholme) and
`H_2(p-1)=0 (mod p)`. Taking the p-adic logarithm through precision `p^3`
gives `F(x)=1 (mod p^3)` for every nonnegative integer x.
Consequently `R_p(a)=d^a (mod p^3)`.
Separate numerator factors with `j=p` before expansion; there are none in band 0,
the single factor `(1+3a)` in band 1, and
`(1+3a)(1+2a)` in band 2. Multiplying the remaining p-unit factors yields

```text
d^a * products_without_p_j
 = 1 + pa U_b + (p^2 a^2/2)(U_b^2-K_b) (mod p^3).
```

Multiply by the retained signed weight `h_b+6pa`. In bands 1 and 2 use
`A_b=p a_b` and `A_b=p^2 a_b` respectively, keeping exactly the terms of
valuation below 3. This produces the polynomial coefficients

```text
C_p(a) = W_p + a(L0+L1+L2) + a^2(J0+J1+J2) (mod p^3).
```

The known global p-block degree filtration guarantees that this congruence
holds for every integer a; comparing Newton and monomial bases gives
`q1=Lsum+Jsum` and `q2=2 Jsum`. QED.

## 4. Executed exact evidence (two distinct constructions)

The independent checker `d25_w216_three_band_newton_obstruction_20261110.py`
uses (1) original factorial-ratio coefficient streaming and the first three
**uncompressed signed p-blocks**, then takes Newton differences; and
(2) modular harmonic prefix sums and the valuation-stratified formulas above.
The paths agree at all eight checked primes `7,13,19,37,43,73,109,373`.

| p | S0 mod p | S1 mod p | S2 mod p | sum mod p | (q0,q1,q2) mod p^3 |
| ---: | ---: | ---: | ---: | ---: | :--- |
| 13 | 9 | 9 | 8 | 0 | (13,78,0) |
| 19 | 0 | 3 | 16 | 0 | (19,114,0) |
| 37 | 7 | 21 | 9 | 0 | (37,222,0) |
| 373 | 224 | 45 | 104 | 0 | (373,2238,0) |

Thus at p=373 the three distinct **signed/valued** contributions are
`224+45+104=373=0 (mod 373)`; no one-band zero explains the observation.
This is BRC `COMPOSE_APPLIED`: the three source-labeled valuation fibers are
retained until the exact final signed sum.

A separate direct integer-binomial evaluator (not the harmonic path) checked
the next precision and found

```text
p=13:  q2 mod p^4 = 8788   = 4*p^3
p=19:  q2 mod p^4 = 123462 = 18*p^3
p=373: q2 mod p^4 = 9600596645 = 185*p^3.
```

Hence the **stronger** universal assertion `q2=0 (mod p^4)` is rigorously
refuted by the exact p=13 example. The experimentally supported original
`q2=0 (mod p^3)` remains open uniformly.

## 5. Provenance, constraints, and exact continuation

The three-band theorem is author-proved with eight exact computational checks;
the modulo-p cancellation is *not* an accepted or universally proved theorem.
The p=13 mod-p^4 witness is an exact finite counterexample to that stronger
statement only. There is no independent Driver review.

The parent task still requires the original signed `Delta_p-R_p=0 (mod p)`
for both `p=13,19 (mod24)`, or an exact counterexample and correct task
disposition. The original p=373 native H0/B0 divided-power
`[X]U mod 139129`, rank, semilinear direction, normalization, signed kappa,
and independent reproduction remain `NOT_RUN / PENDING_OWNER`;
existing support Issue #1559 is not replaced by this mathematical subunit.

**Next precise mathematical action:** derive a finite WZ/reflection certificate
for `S0+S1+S2=0 (mod p)` using the existing band-1/band-2 first-jet reflection
and investigate how that scalar cancellation feeds the original
`Delta-R` port. Do not duplicate earlier native or cutoff results.

**Source control:** the current Research lane has no verified winning CLAIM/open
run; `em_site_control(recovery_status)` returned
`SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED` in this run. Read-only continuation
request `onhour11-20261110-1433-exact-cont` was still QUEUED at the latest
receipt; reconcile the original request_id. GitHub publication here is
AUTHOR_SIDE, not a Source-native checkpoint or formal Result.

## 6. FOLLOW-ON SAME-TURN SCIENTIFIC UNIT — reflection removes the grade-2 sum

Consume the **earlier proved and independently checked** grade-1/grade-2
leading-unit reflection (no new claim of its authorship). For
`2m+1<=k<=3m` let `u_k=A_k/p mod p`, a unit, and put `b=p-k`,
which bijects grade 1 with grade 2. The previously obtained exact
leading-unit identity is

```text
(A_k/p) * (A_(p-k)/p^2) = (36 k^3)^(-1) (mod p).
```

Therefore the entire grade-2 contribution is representable using
**only original grade-1 units**:

```text
S2 = sum_{k=2m+1}^{3m} (1-6k)/(6 k^3 u_k) (mod p).
```

This is a genuine use of the existing reciprocal BRC interface, not
a new method nor a replacement of the signed source: the mapping
`(grade2,b,A_b/p^2) -> (grade1,k=p-b,u_k^-1)` retains its
inverse, sign, provenance and original cutoff labels.

Hence the previously open first-jet statement `q2=0 mod p^3`
is equivalent to the **two-band harmonic/inverse-unit identity**

```text
sum_{b=0}^{2m} A_b [((6b+1)/2)(U_b^2-K_b)+6U_b]
+ sum_{k=2m+1}^{3m} [
       3 (A_k/p) ((6k+1)U_k+6)
     + (1-6k)/(6 k^3 (A_k/p))
  ] = 0 (mod p).
```

This identity is **not yet proved uniformly**. Its reduction from the
three-band formula and the existing reflection theorem is proved.

Exact independent reflection checks:
`p=7,13,19,37,43,73,109,373` all give the same `S2` as
the direct grade-2 computation; at `p=373` both read `104 mod373`.
The remaining proof obligation is a finite signed telescoping identity
between grade 0 and grade 1, rather than three separately expanded sums.
Its target still is the original `Delta_p-R_p` and the distinct native
H0/B0 support gate.
