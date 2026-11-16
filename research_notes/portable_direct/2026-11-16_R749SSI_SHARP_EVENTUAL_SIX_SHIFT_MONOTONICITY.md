# R749SSI — Sharp eventual six-shift monotonicity and a finite-resolution obstruction

Date: 2026-11-16 (Asia/Shanghai). Mathematical status: AUTHOR_EXACT_NOT_REVIEWED.
Mode: independent portable auxiliary-source research, no native shared Task CLAIM.
Frozen scientific input: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Direct predecessor: R749SSF–SSH, immutable commit d980a326e3036d9d1f821e1b8c56dfdfdaaa5b47, Draft PR #2557.
Prior exact smooth-observer collision check reached q=300. This paper extends it to q=10000 and proves an infinite, sharp direction theorem.

## Observer and question

Keep five distinct labeled positive sources, weighted w=(1,1,2,3,6), marking the first weight-one source. For integer q≥1 let

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:\;k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]

For integer errors e,d∈{-2,-1,0,1,2} and q≥6, the original smooth-subtracted readout is

\[
Y(q;e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},\quad
S(q)=18q^4+54q^3-345q^2+2070q-16315.
\]

Study the q→q+6 comparison while keeping each source label and both error values fixed. This is a typed future operation, distinct from comparing observations across arbitrary unknown error labels.

## Theorem 1: sharp eventual six-step direction

Define the exact residue coefficients

\[
(A_0,A_1,A_2,A_3,A_4,A_5)=
(3335/3,\;13780/9,\;12845/9,\;3740/3,\;11485/9,\;12980/9).
\]

For EVERY integer q≥5067 and every legal e,d,

\[
\boxed{\operatorname{sgn}[Y(q+6;e,d)-Y(q;e,d)]
=\operatorname{sgn}(720d-A_{q\bmod6})\neq0.}
\]

The least universal starting cutoff is exactly **5067**. At q=5066, residue 2, e=d=2, the true difference is negative while 720d-A_2=115/9 is positive. This is an exact strict counterexample to lowering the starting cutoff.

### Proof

The exact known generating functions (also derived in R749SSF) are

\[
\sum_{q\ge1}C_qz^{q-1}=\frac1{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\qquad
\sum_{q\ge1}T_qz^{q-1}=\frac{z}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

After conversion to denominators (1-z^6)^6 and (1-z^6)^7, respectively, their numerator degrees are at most 22 and 28. For each residue r modulo 6, therefore, C_q and T_q are *exact* polynomials in q of degrees at most 5 and 6 once q≥36.

Put C=C_q, C'=C_{q+6}, T=T_q and T'=T_{q+6}. For fixed r,e,d define the exact **integer** difference numerator

\[
D_{r,e,d}(q)=
108\left((q+6)^3(T'+e)(C+d)-q^3(T+e)(C'+d)\right)
-\left(S(q+6)-S(q)\right)(C'+d)(C+d).
\]

Then

\[
D_{r,e,d}(q)=108(C+d)(C'+d)[Y(q+6;e,d)-Y(q;e,d)].
\]

The multiplier is strictly positive for q≥6. By the preceding exact polynomial count formulas, D on each fixed residue is a polynomial of degree at most 14 for q≥36 (the naive first product degree is 3+6+5=14 and the second is at most 3+5+5=13).

Use the six residue-compatible bases b_r=5070+r. For all 6×5×5=150 choices (r,e,d), let σ=sgn(720d-A_r). Evaluate the 15 exact integer values σ D(b_r+6j) for j=0,...,14 and compute their Newton differences Δ_6^i[σD](b_r), i=0,...,14. The supplied standard-library certificate establishes for every choice:

* the zeroth difference is strictly positive;
* differences 1 through 8 are nonnegative, with difference 8 strictly positive;
* differences 9 through 14 vanish exactly.

Because the degree is at most 14, the expansion

\[
\sigma D(b_r+6j)=\sum_{i=0}^{14}
\Delta_6^i[\sigma D](b_r)\binom ji
\]

holds for every integer j≥0. All binomial factors are nonnegative. Consequently σD>0 for every q≥5070 in the relevant residue class. The positive eighth difference also independently checks the exact leading coefficient

\[
[q^8]D_{r,e,d}(q)=-(A_r-720d)/28800,
\]

which is independent of numerator error e.

For q from 6 through 5069 the certificate evaluates all 5064×25=126600 exact signed differences directly from integer source counts. The *last* wrong-direction instance is q=5066,e=d=2. Positions 5067–5069 are valid and all q≥5070 are covered by the Newton certificates. Thus the theorem holds globally from 5067, and the q=5066 strict failure makes the threshold sharp. QED.

## Theorem 2: four accumulation values and nonuniform cutoff resolution

For fixed residue r and error pair e,d, the residue-wise rational count expansion gives

\[
Y(q;e,d)=P_r+\frac{A_r-720d}{q}+O(q^{-2})
\quad(q\to\infty,\;q\equiv r\bmod6)
\]

with

\[
36(P_0,\ldots,P_5)=(455,-295,-25,185,-25,-295).
\]

The six phases have exactly four different limits:
455/36, 185/36, -25/36 (residues 2,4), and -295/36 (residues 1,5).
The term -720d/q follows from C_q=q^5/4320+O(q^4) and T_q/C_q=q/6+O(1); the numerator error e enters first at order q^-2. The exact A_r come from the six residue-wise rational expansions, previously computed in R749SRX. None of the A_r-720d vanish for integer -2≤d≤2.

**No fixed δ>0 can guarantee recovering an unknown exact cutoff q from one smooth Y observation under additive absolute error |η|<δ, uniformly over unbounded q.** Fix any legal r,e,d. Both Y(q;e,d) and Y(q+6;e,d) tend to P_r as q→∞ along the residue class. Their distance is eventually <2δ, so the midpoint of those two distinct-cutoff outputs has admissible errors <δ relative to either one. QED.

This is a finite-resolution observability obstruction, not a claim of exact collisions. The raw-ratio observer studied in R749SSG is a different output interface and does have an earlier proved positive uniform cutoff-only radius 1/402.

## Extended exact finite check

A separate pass of the same dependency-free certificate constructs, normalizes and compares all smooth readouts for 6≤q≤10000 and all 25 legal integer error pairs. The **249875 exact rational values are distinct**, with **zero exact collisions**. This statement is explicitly finite, while Theorem 1 is an infinite result proved by the analytic degree bound and exact Newton positivity.

## Reproduction, scope and continuation

Run Python 3 on R749SSI_SIX_SHIFT_EVENTUAL_MONOTONICITY_CERT.py. It generates R749SSI_SIX_SHIFT_EVENTUAL_MONOTONICITY_RESULTS.json with status PASS and the complete boundary summary. Standard-library integers and fractions.Fraction are used throughout; the finite checks cannot replace the generating-function degree argument for the infinite tail. The results are author-checked mathematical evidence awaiting independent audit.

Source labels, numerator/denominator error labels, cutoff and future-shift operation remain part of the typed carrier. Collapsing q to its limiting phase value loses cutoff information and also collapses two pairs of phases; that is safe only for an observer whose declared output is this limit. No native signed BRC port, X6 state transition or Heartbeat World time interpretation has been claimed.

Next: prove or disprove **global exact unknown-cutoff injectivity** of the original Y readout with varying e,d and arbitrary q. Use the exact six residue-class polynomial ratios to analyze Diophantine equality between distinct traces. A second direction is a scale-adaptive q-dependent noise bound, and a third is an actual source-label- and future-operation-preserving BRC interface.
