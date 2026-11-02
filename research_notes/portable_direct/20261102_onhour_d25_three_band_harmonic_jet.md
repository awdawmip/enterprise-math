# D25 — Explicit pole-free three-band harmonic jet factors (2026-11-02)

**Evidence status:** AUTHOR-DERIVED / EXACT ALGEBRA / FINITE EXACT REGRESSION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, immutable publication TP2-B6F4FC938FF94941C1B7, scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3, ordinary Research lane chatgpt-research-onhour-enterprise-math-20260923. Consume the separately persisted three-root polynomial theorem, do not reprove accepted D24 first digit.

## Exact harmonic factor theorem

Let prime p=6m+1>3. Define H_n=sum_(j=1)^n 1/j, H_n^(2)=sum_(j=1)^n 1/j², H_0=H_0^(2)=0. All denominators below are p-adic units, since indices are <=4m<p. The previously proved three-root polynomial is

\[
F_{p,k}(t)=\frac{6k+1}{2^k(k!)^3}\prod_{j=0}^{k-1}
(j-3m+t/2)(j-2m+t/3)(j-4m+2t/3).
\]

Its original source coefficients are the six ports A0,A1,A2,B1,B2,C2 in bands [0,2m], [2m+1,3m], [3m+1,4m]. The following are **exact rational identities** (therefore valid mod p to the permitted precision).

### Low band 0 <= k <=2m

Let

\[
T_k=(6k+1)\frac{(-1)^k}{2^k}\binom{3m}{k}\binom{2m}{k}\binom{4m}{k},
\]
\[
s_k=-\frac12(H_{3m}-H_{3m-k})-\frac13(H_{2m}-H_{2m-k})-\frac23(H_{4m}-H_{4m-k}),
\]
\[
q_k=\frac14(H_{3m}^{(2)}-H_{3m-k}^{(2)})
+\frac19(H_{2m}^{(2)}-H_{2m-k}^{(2)})
+\frac49(H_{4m}^{(2)}-H_{4m-k}^{(2)}).
\]

Then [t^0]F=T_k, [t^1]F=T_k s_k, and [t²]F=(T_k/2)(s_k²-q_k). Thus

\[
\boxed{A_0=\sum_{k=0}^{2m}T_k,\quad
A_1=\sum_{k=0}^{2m}T_ks_k,\quad
A_2=\tfrac12\sum_{k=0}^{2m}T_k(s_k^2-q_k).}\tag{L}
\]

Proof: for factors c_j+d_j t with c_j!=0, the first Taylor coefficient of the product is (product c_j) sum d_j/c_j; the second is half the product times [(sum d_j/c_j)^2-sum (d_j/c_j)^2]. Each negative-integer factor gives the displayed harmonic difference.

### Middle band 2m < k <=3m

Exactly the factor j=2m of (j-2m+t/3) vanishes at t=0. Remove that single t/3 root and define the explicit nonzero rational factorial coefficient

\[
Y_k=
\frac{(6k+1)(3m)!(4m)!(2m)!(k-2m-1)!}
{3\cdot2^k(k!)^3(3m-k)!(4m-k)!}.
\]

Set

\[
e_k=-\tfrac12(H_{3m}-H_{3m-k})
-\tfrac23(H_{4m}-H_{4m-k})
+\tfrac13(H_{k-2m-1}-H_{2m}).
\]

The removed product has log derivative e_k at zero, since negative factors j<2m yield -H_{2m} and positive factors j>2m yield H_{k-2m-1}. Therefore

\[
\boxed{[t^1]F_{p,k}=Y_k,\quad[t^2]F_{p,k}=Y_ke_k,\quad
B_1=\sum_{k=2m+1}^{3m}Y_k,\quad B_2=\sum_{k=2m+1}^{3m}Y_ke_k.}\tag{M}
\]

### High band 3m < k <=4m

There are exactly two roots: j=2m in the middle factor and j=3m in the first factor. Remove their product t²/6. Its constant cofactor is

\[
Z_k=
\frac{(-1)^{3m+k}(6k+1)(3m)!(k-3m-1)!(2m)!(k-2m-1)!(4m)!}
{6\cdot2^k(k!)^3(4m-k)!}.
\]

Hence

\[
\boxed{[t^2]F_{p,k}=Z_k,\quad C_2=\sum_{k=3m+1}^{4m}Z_k.}\tag{H}
\]

All three formulas preserve original W216 weights and coefficient signs, k-interval source, valuation 0/1/2, and the finite truncation. The high port matches the earlier Wilson-reflected B2W modulo p, but the factorial display is **exact as a rational Taylor coefficient**.

## What this advances

Combining (L),(M),(H) with the previously persisted exact observer gives

\[
\Delta_p-R_p\equiv
\frac{\left[\sum_{k=0}^{2m}T_k+p\left(\sum_{k=0}^{2m}T_ks_k+\sum_{k=2m+1}^{3m}Y_k\right)-p\right]}{p^2}
+\frac12\sum_{k=0}^{2m}T_k(s_k^2-q_k)
+\sum_{k=2m+1}^{3m}Y_ke_k
+\sum_{k=3m+1}^{4m}Z_k\pmod p. \tag{O}
\]

The quotient is p-integral under the frozen accepted D24 first-digit theorem in target residue classes. Formula (O) is an exact **single-index terminating harmonic-and-factorial certificate** for the original scalar LIFT observer; its final cancellation for *all* target primes remains the hard open research unit. A candidate finite WZ/contiguous transformation can now work with explicit harmonic factors and no singular Pochhammer roots. The next action is to produce an exact telescoping certificate for the three low/mid ports versus the signed high Z_k/Wilson U_r, and verify it at p=13,19,373 before proposing a uniform proof.

## Actually performed finite checks

Independently evaluated (L),(M),(H) by factorials and modular harmonic sums for all 107 primes p<=3000 with p≡13,19(mod24). This checks **535 port comparisons** (A1,A2,B1,B2,C2; 142715 original k positions) against an independently implemented three-jet recurrence in the preceding research unit; zero mismatches. At p373 the five reduced values modulo p are A1=138, A2=82, B1=27, B2=158, C2=266; the high port matches the original Wilson tail, and the prior divided digit remains D0=240, so 240+82+158+266=746=0 modulo373. Also p13 gives A2=5, B2=8, C2=10; p19 gives A2=1, B2=17, C2=9.

The checker is retained as d25_three_band_harmonic_jet.py with its output JSON in the author evidence bundle; finite verification supports these exact formulas but is not a uniform cancellation proof or Source review.

## Native and control debts (not reclassified)

Separate original-class fixed p373 H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius, normalization eta, odd signed Green/Hesse kappa and independent replication: NOT_EXECUTED / PENDING_OWNER at existing GitHub issue #1559. The connected Sites gateway reports Research write grant disabled as observed 2026-11-02 07:11 UTC. The research lane has no authenticated native session, CLAIM, run, Source checkpoint or review; old dispatch request research-onhour-20261031-0205-dispatch-r15 was not resent.

**Provenance:** frozen task publication and D24/Clausen scientific inputs at c47e13e4aba0e006366f989d6334d443f6333ae3; preceding author-side note 20261102_onhour_d25_three_root_terminating_jet_bridge.md; these harmonic formulas are this research unit's author-derived consequences of the same exact finite polynomial.
