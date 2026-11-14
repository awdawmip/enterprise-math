# R150 — Exact lag-difference inverse of joint CRT residue covariance

Date: 2026-11-14 (Asia/Shanghai).  
Scientific pin (unchanged): 43ec6098b1330ae86d0a7863be336c5d97f6ef34.  
Scope: external S23 scalar tied-phase Sturmian integer-phase-fiber observer.  
Status: author-side exact proof plus finite exact verification; NOT_REVIEWED.  
Predecessor: R149 / R149C at enterprise-math commit c17e4a8974b696b614a96b38f5f27dacecdd2615, research_notes/brc_s23_av_r149_cross_word_correlation_20261114/PROOF.md and R149C_GCD_FULL_LAG_SPECTRAL_SUPPORT.md.  
Publication route: independent research_notes/portable_direct, not a Task CLAIM, Result or Review. P000/native X6 remains unchanged.

## Definitions

Fix positive integers n,m and integers s,t,u,v with gcd(s,n)=gcd(t,m)=1. Put g=gcd(n,m), q=(g-1)/2, and use least nonnegative residues. Define

\[
A_j=((sj+u)\bmod g)-q,\qquad
B_j=((tj+v)\bmod g)-q,\quad j\in\mathbb Z/g\mathbb Z.
\]

Both A and B traverse the complete centered residue system, hence have zero sum. R149 proves that the exact lagged covariance of the normalized original modulo-n and modulo-m residue sequences equals

\[
F(h)=\frac1{gnm}\sum_{j=0}^{g-1}A_j B_{j+h}.
\tag{1}
\]

The full-period joint sampling here uses the original single clock and generalized CRT. We retain the joint CRT observer. When g=1, F=0. Assume g>=2 below. Set \(\ell=s^{-1}\pmod g\) and \(j_*=-u\ell\pmod g\).

## R150.1 — Exact first-difference inverse

**Theorem.** For every integer lag h,

\[
\boxed{F(h+\ell)-F(h)=
\frac{((t(j_*+h)+v)\bmod g)-(g-1)/2}{nm}
=\frac{B_{j_*+h}}{nm}.}
\tag{2}
\]

Hence the full centered second joint-residue sequence is exactly recovered from the lag signature:

\[
\boxed{B_j=nm\,[F(j-j_*+\ell)-F(j-j_*)].}
\tag{3}
\]

**Proof.** Since \(s\ell\equiv1\pmod g\),

\[
A_{j-\ell}-A_j=-1+g\,{\bf1}_{j=j_*}.
\]

In the sum for \(F(h+\ell)\), change variable \(j'=j+\ell\). Subtraction gives

\[
F(h+\ell)-F(h)
=\frac1{gnm}\sum_j(A_{j-\ell}-A_j)B_{j+h}
=\frac{-\sum_jB_j+gB_{j_*+h}}{gnm}
=\frac{B_{j_*+h}}{nm}.
\]

Replacing h by \(j-j_*\) proves (3). QED.

**Stronger linear statement.** The proof only requires \(\sum_j B_j=0\); the second signal need not be an affine residue permutation. For fixed A, the circular-correlation map on rational zero-mean g-vectors is a bijection of that \((g-1)\)-dimensional space. Formula (3) is its constructive inverse. The output F has zero mean because A has zero mean. Thus retaining the *entire* lag signature is an exact information-preserving interface for this specific joint-gcd observer and arbitrary zero-mean second signals.

## R150.2 — Recovery of affine residue coefficients

If the second signal has the specified residue form, set \(R_j=B_j+q\). Reconstruction yields

\[
v\bmod g=R_0,\qquad t\bmod g=(R_1-R_0)\bmod g.
\tag{4}
\]

Thus the lag signature plus known n,m,s,u determines the second signal's slope and offset **modulo g**. It is not asserted to recover coefficients modulo m from their common-gcd projection. Proof: evaluate \(R_j=(tj+v)\bmod g\) at j=0,1.

## R150.3 — Universal jump multiset and quadratic energy

The g shifted increments form a complete centered residue system:

\[
\{F(h+\ell)-F(h):0\le h<g\}
=\left\{\frac{j-(g-1)/2}{nm}:0\le j<g\right\}
\quad\text{as multisets}.
\tag{5}
\]

Consequently, for every choice of unit coefficients and offsets,

\[
\boxed{\sum_{h=0}^{g-1}(F(h+\ell)-F(h))^2
=\frac{g(g^2-1)}{12n^2m^2},}
\tag{6}
\]

and the largest absolute jump is \((g-1)/(2nm)\), with zero jump sum. Proof: apply (2), note that B is a permutation, and use \(\sum_{j=0}^{g-1}(j-(g-1)/2)^2=g(g^2-1)/12\).

The increment *order*, not merely its multiset, preserves the actual coupling. When g>1 the values B_j are distinct. If F had a proper positive period p<g, (3) would make B p-periodic, contradicting distinct entries. Hence F has exact minimal lag period g. This gives an elementary constructive alternative to R149C's Fourier argument, and does not assume statistical independence of coupled residues.

## R150.4 — Exact O(g) waveform construction

Let \(h_i=i\ell\bmod g\) for i=0,...,g-1 (one traversal of all lags). Define

\[
P_0=0,\quad
P_{i+1}=P_i+\frac{B_{j_*+h_i}}{nm},\quad
M=\frac1g\sum_{i=0}^{g-1}P_i.
\]

Then

\[
\boxed{F(h_i)=P_i-M.}\tag{7}
\]

The increments are (2), and their sum is zero, so \(P_g=P_0\). Any two waveforms with these increments differ by a constant; the zero-mean condition fixes that constant to \(-M\). This constructs the complete lag waveform in O(g) rational/integer arithmetic operations and O(g) output size, without summing g terms separately for each of g lag values. Bit complexity additionally depends on the integer input sizes and exact rational representation.

## R150.5 — Actual Sturmian specialization

For a finite Sturmian word w with reduced strict slope-support endpoints \(a/b<c/d\) and R149 intercept offsets U,V, take

\[
(n,s,u;m,t,v)=(b,a,-U;d,-c,V),\quad g=\gcd(b,d).
\]

For g>1 let \(\ell=a^{-1}\pmod g\) and \(j_*=U\ell\bmod g\). Its mixed lower/upper-endpoint covariance then satisfies

\[
\boxed{\Gamma_w(h+\ell)-\Gamma_w(h)
=\frac{((V-c(j_*+h))\bmod g)-(g-1)/2}{bd}.}
\tag{8}
\]

This is exact for the mixed \(\Gamma_w\) component; the total discrepancy autocovariance also has the two same-endpoint terms from R149.3. This establishes an inverse for the specified joint-gcd observable, not an X6 ontology transfer or a pointwise fiber-presence theorem.

**Exact witnesses:**

- w=00100100: (b,a,U;d,c,V)=(4,1,2;8,3,0), g=4, ell=1; \(\Gamma=(-3,-1,5,-1)/128\), successive jumps \((1,3,-3,-1)/64\).
- w=00001000010000: (6,1,2;14,3,0), g=2; \(\Gamma=(1,-1)/336\), jumps \((-1,1)/168\).
- General kernel n=m=5,s=t=1,u=0,v=1: \(F=(0,-1,-1,0,2)/25\), despite F(0)=0; increments \((-1,0,1,2,-2)/25\) recover all five centered second residues.

## Exact validation and reproducibility

The companion R150_check.py runs exclusively with Python integers and fractions (no floats), verifying (2)-(7), cyclic mean, jump multiset and energy. Exhaustive cases: g=1..12, every unit pair s,t mod g, all offsets u,v mod g: **22,357** configurations. A further **1,200** deterministic seed-150 configurations sample n,m in 1..24, arbitrary unit multipliers and signed offsets; for each, the reduced-gcd kernel is independently compared at every tested lag against the direct full-lcm covariance over the original mod-n/mod-m sequence. Three named witnesses are independently rechecked. Output marker: R150_EXACT_LAG_DERIVATIVE_INVERSE_PASS. Counts and exact fractions are in R150_verification.json. These tests verify their finite domain; the universal claim uses the proof above.

## Next scientific question

Seek a pointwise bridge from the reconstructed joint-gcd residue factor, together with the full exact integer phase-fiber count C_w(K), to a shorter presence/loss certificate around the candidate all-length Sturmian threshold \(E(m)=(m-2)\lfloor(m-1)/2\rfloor+1\). The presently proved inverse concerns the mixed covariance lag signature, not pointwise survival of a fiber. Under the Enterprise Math joint-relation observer rule, retain CRT coupling and any later-relevant phase, multiplicity and provenance until a scope-specific observer factorization has been proved.
