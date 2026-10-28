# D25 — original weighted-216 middle/high p-adic unit reciprocity under n ↦ p−n

Date: 2026-10-28 Asia/Hong_Kong. Research lane: chatgpt-research-onhour-enterprise-math-20260923 (NOT CONTROL_PLANE_MAINTENANCE chatgpt-hourly-enterprise-math-20260921).

Classification: **AUTHOR-SIDE / EXACT ALL-p≡1 (mod 6) REFLECTION PROVED / 23 EXECUTED EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED.** Mother objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**.

## Exact question and novelty boundary

The previously proved original-class high-tail reflection (20261028_onhour_d25_original216_p3_middle_tail_reflection.md) computes the high-index digit Theta_p through its own factorial recurrence. A separate source-aligned proof identifies the *different* frozen Clausen cutoff R_p=Q/p² mod p. Neither earlier lemma is re-proved here. The present contribution is the multiplicative **n ↔ p−n pair-unit law**, which connects every original high-tail second-order digit to the *first-order digit of its original middle-band partner*, with index, sign, weight and invertible bridge retained. This is an exact, all-prime arithmetic theorem, but **not** the desired third-digit cancellation proof.

For p=6m+1>3 prime, work in Z_(p) and define the original immutable summand

\[
t_n=\frac{(2n)!(3n)!}{216^n(n!)^5},\qquad
w_n=(6n+1)t_n,\qquad W_p=\sum_{n=0}^{p-1}w_n.
\]

The frozen LIFT is \(W_p\equiv p\pmod{p^3}\) for p≡13,19 mod24, equivalently the original Source \(\Delta_p-R_p\equiv0\pmod p\) through the already proved source-port alignment. Accepted UR establishes the first digit \(W_p\equiv p\pmod{p^2}\), not this target.

## Theorem A: paired factorial-unit reflection for every original index

For every n in 1,...,p−1, put a=floor(2n/p), b=floor(3n/p). The following statements are **proved for all p=6m+1>3**:

\[
v_p(t_n)=a+b,\qquad v_p(t_nt_{p-n})=3. \tag{R1}
\]
\[
\boxed{\frac{t_nt_{p-n}}{p^3}
\equiv \frac{(-1)^{1+a+b} b!(2-b)!}{36n^3}\pmod p.} \tag{R2}
\]
\[
\boxed{\frac{w_nw_{p-n}}{p^3}
\equiv \frac{(-1)^{1+a+b} b!(2-b)!(1-36n^2)}{36n^3}\pmod p.} \tag{R3}
\]

The left quotients are p-integral, including when the weighted term has an additional p-factor. In particular at n=m or its reflected partner the weight is p-divisible and R3 correctly predicts zero. The lemma never divides by an arbitrary weighted term.

### Exact proof, without assuming LIFT

For 0≤r<p and 0≤q≤2, separate the complete nonmultiple blocks in (qp+r)! and apply Wilson's theorem:

\[
\boxed{\frac{(qp+r)!}{p^q}\equiv(-1)^q q!\,r!\pmod p.}\tag{R4}
\]

Here 2n and 3n have nonzero least residues r_2=2n-ap, r_3=3n-bp. Their reflected companions at p−n have quotient/remainder (1−a,p−r_2) and (2−b,p−r_3). Hence factorial valuations total a+b+(1−a)+(2−b)=3. Because 1≤n<p, the n! and (p−n)! denominators are p-units.

Wilson reflection also gives r!(p−r)!≡(−1)^r r mod p. Applying it twice to the 2n-factorials and once to the 3n-factorials, while retaining the **five** original n-factorials, produces the scalar factor

\[
\frac{(-1)^{1+a+b}b!(2-b)!}{36 n^3},
\]

since r_2 r_3≡6n² and 216^p≡216 mod p. This proves R2. Multiplying the original signed weights gives

\[
(6n+1)(6(p-n)+1)\equiv(6n+1)(1-6n)
=1-36n^2\pmod p,
\]

proving R3. This proof uses no numerical regression or proposed LIFT identity.

## Theorem B: reversible original middle-to-high unit bridge

Index the actual original middle band by 0≤r<m and n_r=2m+1+r. Its reflected original high-band index is p−n_r=4m−r. Define **independently labeled source digits**

\[
\mu_r=\frac{w_{n_r}}p\bmod p,\qquad
\tau_r=\frac{w_{p-n_r}}{p^2}\bmod p.
\]

Their exact weighted valuations are respectively 1 and 2, so both are units modulo p in the declared range. In R3, a=0 and b=1. Using original weights

\[
6n_r+1\equiv6r+5,\qquad
6(p-n_r)+1\equiv-3(2r+1)\pmod p,
\]

gives the **uniform all-prime pair law**

\[
\boxed{
\mu_r\tau_r\equiv-\frac{(6r+5)(2r+1)}
{12(2m+1+r)^3}\pmod p,} \tag{R5}
\]

and its permitted inversion

\[
\boxed{
\tau_r\equiv-\frac{(6r+5)(2r+1)}
{12(2m+1+r)^3}\,\mu_r^{-1}\pmod p.} \tag{R6}
\]

Every listed denominator and both μ_r, τ_r are nonzero mod p in 0≤r<m. This is an **observer-scoped and index-preserving bijection** between two original valuation bands; the proof cannot be replaced by unsigned valuation statistics.

The middle source itself has the exact factorial-unit formula

\[
\boxed{\mu_r\equiv-(6r+5)
\frac{(4m+2+2r)!(3r+2)!}
{216^{2m+1+r}((2m+1+r)!)^5}\pmod p,} \tag{R7}
\]

because the only p-factor in (3n_r)! leaves −(3r+2)! modulo p after p-division. Dividing consecutive R7 units produces the first-order recurrence

\[
\boxed{
\frac{\mu_{r+1}}{\mu_r}\equiv
\frac{(6r+11)(4m+3+2r)(4m+4+2r)
(3r+3)(3r+4)(3r+5)}
{216(6r+5)(2m+2+r)^5}\pmod p
}\tag{R8}
\]

for 0≤r<m−1, every denominator being a p-unit. The existing high-tail factorial recurrence remains valid independently; this is a new bridge that eliminates high factorial computation from its evaluation once original middle digits have been retained.

## Exact remaining original third-digit obligation (OPEN)

Consume the already proved source-preserving original-tail equation

\[
W_p\equiv W_{\rm bulk}+p^2\Theta_p\pmod{p^3},
\quad W_{\rm bulk}=\sum_{n=0}^{3m}w_n,\quad
\Theta_p=\sum_{r=0}^{m-1}\tau_r\pmod p.
\]

R6 now gives an equivalent, still unproved uniform target, for p≡13,19 mod24:

\[
\boxed{
\frac{W_{\rm bulk}-p}{p^2}\stackrel{?}{\equiv}
\sum_{r=0}^{m-1}
\frac{(6r+5)(2r+1)}
{12(2m+1+r)^3\mu_r}\pmod p.
}\tag{R9}
\]

The numerator divided by p² is p-integral on these two target classes by **previously accepted first-digit UR** and the proved tail valuation. R9 is **equivalent to** W_p≡p mod p³ / frozen Delta_p−R_p≡0, not a derivation of its zero. In particular the reflected Clausen cutoff R_p is a distinct source object and is **not** renamed Theta_p here.

## Real executed independent exact computation

Companion source file: research_notes/portable_direct/d25_original216_middle_high_reciprocal_reflection_20261028.py. It was **actually run** with Python standard library integer operations, no floating point. It independently computes **all original n** via (i) exact integer binomial coefficients and (ii) modular rational recurrence mod p⁴. For each of **23** primes 7,13,19,31,37,43,61,67,73,79,97,103,109,127,139,151,157,163,181,193,199,211,373, it checks R3 at every n, precise unit valuations on the middle/high bands, R5, the exact middle recurrence R8 and full original high-tail reconstruction. This comprises **2610 original n-to-(p−n) index checks**, not a statement about an infinite prime range.

Execution ended with:

    PASS_D25_ORIGINAL216_ALL_N_REFLECTION_AND_MIDDLE_HIGH_RECIPROCITY
    primes_checked= 23 pairs_checked= 2610
    p13= (13, 2, 10, (5, 10, 9, 12))
    p19= (19, 3, 9, (7, 13, 13, 17))
    p373= (373, 62, 266, (125, 108, 203, 290))

At p=373, m=62 and n_0=125: μ_0=108, τ_0=203 and 108×203≡290 mod373, agreeing with the **signed** R5 kernel. All 62 middle/high pairs yield Θ_373=266. The independently saved original W_bulk≡14887176 mod 373³ has divided defect (W_bulk−373)/373²≡107≡−266 mod373. This is a precise fixed-prime check of R9, **not** a proof of uniform vanishing.

## BRC, source boundaries, research continuation

BRC declared carrier: (p,m,r,n_r,p−n_r,w_{n_r}/p,w_{p−n_r}/p², valuations, signed 6n+1, source-index order, original Delta/R provenance). Permitted observer: original W_p mod p³, then the already proven bridge to Delta−R mod p. The bijective unit reflection preserves enough information for this restricted scalar sum; it does not identify any native H0/B0 operator, Frobenius, X6 dynamics, or all future observables. Native project substrate remains the P000 Heartbeat six-dimensional discrete Cell space (six axes plus separately typed time as needed); these rational finite sums are explicitly **external auxiliary scalar arithmetic**, not an independent native plane or full-X6 theorem.

NEXT MATHEMATICS: search a provable finite telescoping/WZ certificate that couples the signed middle-unit inverse sum of R9 to the **full** p² bulk quotient for BOTH p≡13 and 19 mod24, retaining all low/middle/high p-adic ports. A true counterexample is also admissible. Do not restart accepted UR/CM0, previous Cauchy p² units, or broad finite-prime scans.

HIGHEST NATIVE EVIDENCE remains issue awdawmip/enterprise-math#1559 (read OPEN/PENDING_OWNER/NOT_EXECUTED). Its required original p=373 H0/B0 divided-power benchmark is actual [X]U mod139129, native module rank, sigma-semilinear Frobenius direction/eta, signed odd Green/Hesse observer, original kappa and Delta_p−R_p, and raw reproducible source-bound evidence. No executor ownership has been established. **This author-side theorem and scalar checker are NOT the native experiment.**

CURRENT CONTROL: live Site 0.6.11 reports research_authority_granted=false, write_relay_enabled=false and active native job quota 5/5, with upstream code review still required. Historical ordinary Chat bridge #6575 recovery was only an ACTIVE pointer and #6576 dispatch failed TimeoutExpired; their namespace is not a current native request receipt and cannot prove a winning claim/run. No new CLAIM/open/Source publication, Result, review or frozen-state mutation was attempted. The three old staging sources remain independent. Only author-side GitHub persistence is requested here; formal Source checkpoint and Research-Activity registration remain REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NOT_ADMITTED.

NO-REPEAT SOURCES: the earlier 20261028 original weighted216 high-tail reflection and explicit harmonic-jet notes; the 20261026 source-aligned frozen Clausen observer identity; current immutable TP2 task publication. Frozen science pin unchanged; all earlier admitted mathematical Results unchanged.