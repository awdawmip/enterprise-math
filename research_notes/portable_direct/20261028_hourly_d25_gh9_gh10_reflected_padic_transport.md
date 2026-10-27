# D25/LIFT GH-9 and GH-10 — reflected GH-3 carrier and its first p-adic defect

Date: 2026-10-28 Asia/Hong_Kong. TASK_RESEARCH logical lane: chatgpt-research-hourly-enterprise-math-20260923. Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / D25-LIFT-JT2. Parent OPEN at last verified Source frontier. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.

Input reuse: GH-3 defines the exact auxiliary C carrier and reduces original S-labelled MM/LH ports to T_p in the 19 mod 24 class. GH-7/GH-8 established its coefficient recurrence and a different regularizing decomposition. These are consumed, not recredited. The statements here concern the exact auxiliary rational carrier; all original W/S terms, separate MM/LH source labels, actual cutoff, and native X6 obligations remain in the parent task. This is an author-side portable result, not Source-authenticated completed predecessor research.

## Setup

For prime p=4d+3>3 and 0<=r<=d, retain

$$
 C_r=9^r\frac{(1/4)_r^3}{(1/2)_r(3/4)_r r!},\qquad
 T_p=\sum_{r=0}^{d}(8r+1)C_r,
$$

$$
 q_r=\frac{C_{r+1}}{C_r}
 =\frac{9(4r+1)^3}{(4r+2)(4r+3)(4r+4)}.
$$

Every C_r for 0<=r<=d is a p-adic unit. In particular C_d is a legal normalizer through modulo p^2. GH-3's G_MM/G_LH identities still require p congruent to 19 modulo 24; the present coefficient lemmas apply to the larger p congruent to 3 modulo 4 class.

## GH-9 — exact rank reflection and a finite-field binomial bridge

**Theorem GH9.1.** For each 0<=r<=d,

$$
\boxed{C_r\equiv(-9)^r
 \frac{\binom{d+r}{r}^{3}}{\binom dr\binom{2d+1+r}{r}}\pmod p.}
$$

All binomial denominators are p-units. Indeed 1/4=d+1, 1/2=2d+2 and 3/4=-d in F_p. Convert those three Pochhammer factors to ordinary binomial coefficients. All needed integer factorial arguments are smaller than p.

Define the source-preserving reversed coefficient

$$
 \mathcal B_0=1,\qquad
 \mathcal B_r=9^{-r}\prod_{i=1}^{r}
 \frac{(4i-1)(4i)(4i+1)}{(4i+2)^3}
 =9^{-r}\frac{(3/4)_r(1)_r(5/4)_r}{(3/2)_r^3}.
$$

**Theorem GH9.2.** The following is an *exact rational equality*, before any modular reduction:

$$
\boxed{\frac{C_{d-r}}{C_d}=9^{-r}\prod_{i=1}^{r}
\frac{[p-(4i+1)](p-4i)[p-(4i-1)]}{[p-(4i+2)]^3}.}
$$

It follows that C_{d-r}/C_d is congruent to B_r modulo p and

$$
\boxed{\frac{T_p}{C_d}\equiv-\sum_{r=0}^{d}(8r+5)\mathcal B_r\pmod p.}
$$

Proof: telescope C_{d-r}/C_d as the product of inverse recurrences q_{d-i}, where 4d+3=p. The denominators in the displayed product are p-units for every 1<=i<=d. In the weighted finite sum let k=d-r and keep the exact identity 8(d-r)+1=2p-(8r+5). No term at either end is discarded. The last congruence is an equivalence of finite source observations; it does not establish that either sum vanishes.

## GH-10 — the first p-adic reflection defect

Define the p-integral harmonic carrier

$$
\Lambda_r=\sum_{i=1}^{r}
\left(\frac1{4i-1}+\frac1{4i}+\frac1{4i+1}-\frac3{4i+2}\right),
\qquad \Lambda_0=0.
$$

**Theorem GH10.1.** For all 0<=r<=d,

$$
\boxed{\frac{C_{d-r}}{C_d}\equiv
 \mathcal B_r(1-p\Lambda_r)\pmod{p^2}.}
$$

Proof: factor the exact GH9.2 ratio into its p=0 term B_r times three factors 1-p/(4i-1), 1-p/(4i), 1-p/(4i+1), and the inverse cube of 1-p/(4i+2). All factors are p-integral units. Their product has first-order coefficient minus the displayed summand of Lambda_r; products of two first-order errors vanish modulo p^2.

**Theorem GH10.2.** The *next-digit original weighted cutoff* is

$$
\boxed{
\frac{T_p}{C_d}\equiv
-\sum_{r=0}^{d}(8r+5)\mathcal B_r+
p\left[2\sum_{r=0}^{d}\mathcal B_r+
 \sum_{r=0}^{d}(8r+5)\mathcal B_r\Lambda_r\right]
\pmod{p^2}.}
$$

Proof: insert GH10.1 into the exact reflected sum with rank weight 2p-(8r+5), retaining all terms through order p. Both the 2p endpoint-weight moment and the joint harmonic moment are necessary to preserve the next p-adic digit. This is not a claim that a zero-order reflected sum may be divided by p without checking its divisibility.

**Nonzero defect certificate.** At p=19 and reflected rank r=1,

$$
\mathcal B_1=\frac5{162},\quad \Lambda_1=\frac{17}{60},\quad
\frac{C_{d-1}}{C_d}=\frac{1120}{6591}.
$$

The exact original quotient is 276 modulo 361, whereas B_1 alone is 29 modulo 361; B_1(1-19 Lambda_1) restores 276. The lost correction is 247 modulo 361. Independent original finite-sum witnesses are T_19=342 modulo 361 and T_43=1634 modulo 1849. They do not establish the uniform T_p=0 conjecture.

## Proof scope, exact author checks, and next research problem

The companion standard-library Python checker (same-date filename ending in reflected_padic_transport_check.py) independently executes exact Fraction coefficients and exact rational inverse products for every rank in 18 primes 7<=p<=151, p congruent to 3 mod 4. It separately executes a direct modular p^2 recurrence and every-rank / full-sum congruences for all 154 such primes p<2000. All actually executed assertions passed. The universal GH9/GH10 statements follow from the displayed algebra, not from the finite checks. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

Typed BRC method: REUSE_APPLIED to the ordered finite GH-3 scalar carrier, its valuations and two boundary ranks. Intended observer is the actual weighted T_p and next operation is normalized reflection plus a p-adic second-digit readout. GH-9 collapses the joint p*Lambda residue; GH-10 supplies the missing repair coordinate. This auxiliary scalar transport is not a theorem about Heartbeat World native X6 dynamics; a claimed native application would require a declared embedding/readout preserving the appropriate original sources and allowed operations.

**Next exact step:** attempt an actual finite-field or p-parameter WZ certificate for
$$\sum_{r=0}^{d}(8r+5)\mathcal B_r\equiv0\pmod p$$
for all primes p congruent to 19 mod 24. This would resolve GH-3's still-open T_p obstruction. Subsequently compare GH-10's *two distinct p-adic moments* with GH-5's MM next-digit corrections C_p,K_p, then revisit R23/R36 without collapsing original W/S sources, six Hasse J/E channels, finite and positive-infinity boundaries.

Control source read at 2026-10-27 18:14 UTC returned gateway 0.6.11 with research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, CODE_REVIEW_REQUIRED; it supplied no current own winning claim, opened run or native Source checkpoint. Historical predecessor/claim conflict remains tracked by enterprise-math issue #1558. This portable proof is not Research-Activity registration, formal Result, independent Driver review, native p=373 validation, H0/B0, [X]U, or Frobenius acceptance.
