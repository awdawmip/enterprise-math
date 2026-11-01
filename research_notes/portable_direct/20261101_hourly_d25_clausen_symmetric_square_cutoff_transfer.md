# D25 — Exact Clausen symmetric-square source transfer and first omitted coefficient

Date: 2026-11-01. TASK_RESEARCH author-side portable result; logical lane `chatgpt-research-hourly-enterprise-math-20260923`. Parent: original 216 weighted-sum objective, Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific source `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_RUN / SOURCE_CHECKPOINT_PENDING.

**Consumed, not recredited:** `research_notes/portable_direct/20261101_hourly_d25_original_216_weighted_terminal_resonance.md` and `research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md`. The former gives the original weighted terminal source 5/9, the latter preserves the signed Clausen cutoff and its original Δ−R connection.

## Definitions

For a prime p≥7, p≡1 mod 6, in Z_(p)[z] let θ=z d/dz,
u_n=(1/6)_n(1/3)_n/(n!)², v_n=(1/2)_n(1/3)_n(2/3)_n/(n!)³,
Y=Σ_{0≤n<p}u_n z^n, U=Σ_{0≤n<p}v_n z^n, W=(6θ+1)U, K=Y²−U.
The exact infinite Clausen identity `_2F1(1/6,1/3;1;z)^2=_3F2(1/2,1/3,2/3;1,1;z)` implies [z^n]K=0 for 0≤n<p; K consists of degrees p,...,2p−2.

Write
L₂=θ²−z(θ+1/6)(θ+1/3),
L₃=θ³−z(θ+1/2)(θ+1/3)(θ+2/3),
D_W=(6θ−5)θ³−(6θ+1)z(θ+1/2)(θ+1/3)(θ+2/3)
(where (6θ+1) acts AFTER multiplication by z),
e=−(p−5/6)(p−2/3)u_(p−1).

## Theorem I: exact polynomial-level source and intertwiner

In Q[z] one has
(1) L₂Y=e z^p;
(2) L₃(Y²)=2e z^p(pY+3θY);
(3) D_W(6θ+1)=(6θ−5)(6θ+1)L₃, as an operator identity;
hence
(4) **D_W W=(6θ−5)(6θ+1){ 2e z^p(pY+3θY) − L₃K }.**

Proof: the u_n hypergeometric recurrence cancels every coefficient of L₂Y below p, leaving the single omitted-index source (1). Set y=Y, P=(1−3z/2)/(z(1−z)), Q=−1/(18z(1−z)), R=e z^(p−2)/(1−z); then y''+P y'+Q y=R. Direct differentiation gives the symmetric-square identity
S(y²)=2yR'+6y'R+4PyR
for S=D³+3PD²+(P'+2P²+4Q)D+(2Q'+4PQ). Expanding shows z³(1−z)S=L₃, and substitution simplifies exactly to (2). For (3), apply θz=z(θ+1) and commute polynomials in θ. Finally W=(6θ+1)(Y²−K), giving (4). These are exact, not merely modular identities.

## Theorem II: high cutoff, explicit first-band source

Set r=(p−1)/6 and s=(p−1)/3. For 0≤i<p,
val_p(u_i)=1_{i>r}+1_{i>s}.
For i+j≥p either both indices are >r or one ≤r forces the other >s. Thus every coefficient of K lies in p²Z_(p).

Since D_W W has degree exactly p and (6n−5)(6n+1) ≠0 in Q for n≥p+1, equation (4) forces, *for every n=p+1,...,2p−1*,
(5) **[z^n]L₃K=2e(3n−2p)u_(n−p).**
Writing k_n=[z^n]K and k_(2p−1)=0, the explicit conservation recurrence is
n³k_n−(n−1/2)(n−2/3)(n−1/3)k_(n−1)=2e(3n−2p)u_(n−p).

Wilson's theorem applied separately to affine residue permutations 6j+1 and 3j+1 (j=0,...,p−2), after removing their unique p-factors and the omitted j=p−1 residues −5 and −2, gives
u_(p−1)/p² ≡ 1/10 (mod p), and e/p² ≡ −1/18 (mod p).
Since u_1=1/18, n=p+1 in (5) yields the **universal nonzero cutoff obstruction**
(6) **[z^(p+1)]L₃K /p² ≡ −1/54 (mod p)**.
Thus ignoring K corrupts the high-band operator identity already modulo p³, even when the terminal z^p source is correctly recovered modulo p⁴.

At n=p, [z^p]L₃K=p³k_p with val_p(k_p)≥2, so (4) gives
[z^p]D_W W ≡(6p−5)(6p+1)·2ep ≡ (5/9)p³ (mod p⁴),
recovering, not recrediting, the prior universal original-216 terminal formula.

## Corollary: the first omitted Clausen-index supercongruence

Here u_p and v_p denote the *untruncated* rational hypergeometric coefficients at index p, both p-local units. Comparing coefficient z^p in the infinite Clausen identity with Y² gives the exact identity
v_p−2u_p = k_p = Σ_(i=1)^(p−1) u_i u_(p−i).
Consequently
(7) **(1/2)_p(1/3)_p(2/3)_p/(p!)³ − 2(1/6)_p(1/3)_p/(p!)² ≡ 0 (mod p²).**
The exponent two is sharp at p=13 and p=19: k_p/p² ≡1 in both cases. No stronger uniform congruence is claimed.

## Exact evidence and source separation

A standard-library modular checker (`d25_clausen_symmetric_square_cutoff_check_20261101.py`) computed every Clausen coefficient, the entire inhomogeneous symmetric square, every high-cutoff band, p²-integrality, nonzero p+1 witness, and weighted p³ terminal source in Z/(p⁴) for **37/37 primes p≤397, p≡1 mod 6**. Independent rational Fraction checks at p=7,13,19,37 verified the exact omitted-index identity. Selected (p,k_p/p², [z^(p+1)]L₃K/p², [z^p]D_WW/p³), all modulo p:
p=13: (13,1,6,2); p=19: (19,1,13,9); p=373: (373,315,297,42). Infinite scope rests on the displayed algebra, not finite testing.

BRC resolution COMPOSE_APPLIED: the exact sources are the Gauss input e, high signed cutoff K, and weighted output D_WW, at future operator horizon L₃/D_W. A terminal-only observer discards the provably nonzero p+1 high-band source; no claim of native X6 or H0/B0 transfer follows.

**Next exact research unit:** carry the differential source/cutoff pair from the 1/6,1/3 Gauss model into the DISTINCT 1/8,3/8 Gauss auxiliary by a correctly normalized quadratic change of variable, preserving p mod24, conjugate branches, the signed K cutoff and all high-index/endpoint ports; then test whether it closes the original Δ−R third-digit obligation. Native p373 H0/B0 remains NOT_RUN (#1559).

Control status at 2026-11-01 ~10:23Z: Gateway 0.6.11, research_authority_granted=false, executor_binding_configured=false, upstream CODE_REVIEW_REQUIRED, 5/5 active jobs. Existing exact ordinary-control request `hourly-d25-continuation-20261101T1530p0800-r11` at bridge issue #6638 has definitive UPSTREAM_CODE_REVIEW_REQUIRED, tracked in project issue #1558. No native claim, open, checkpoint, review, Result or ownership succession is claimed from this portable note. Preserve the existing logical lane and its historical service session without re-registering or closing it.
