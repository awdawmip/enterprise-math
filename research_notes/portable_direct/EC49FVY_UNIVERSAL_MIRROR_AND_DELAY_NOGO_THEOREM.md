# EC49FVY — Universal reflection of rational-anchor certificate residues and an exact no-fixed-delay counterexample

**Line:** EC49AS; frozen scientific input BRC16943. **Parent:** EC49FVX, immutable source awdawmip/enterprise-math@9f976f78caa6b74a972b341c9bc680a6652f55f9:research_notes/portable_direct/EC49FVX_SIGNED_DELAY_RESIDUAL_THEOREM.md. **Date:** 2026-11-21. **Status:** AUTHOR_PROVED / EXACT_FINITE_RESIDUE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED. No change to P000 or native X6 dynamics.

## Frozen certificate, scope, and definitions

Use the frozen complete 11-adic/projective exclusion predicate from the parent:
\[
C_{11}(h,n)\ \Longleftrightarrow\ (h\bmod10,n\bmod10)\in P_{10}
\quad\text{and}\quad9h+10n\not\equiv0\pmod {11}.
\]
The 44-class mask P10 is reconstructed from the same 11 original projective rows, not changed. Direct comparisons against those rows pass for all 12,100 pairs 1<=h,n<=110. Its simultaneous-negation invariance
\[
(h,n)\in P_{10}\iff(-h,-n)\in P_{10}
\]
is an exact 100-class finite computation, and the linear mod-11 exclusion also respects negation. Thus C11 extends to an exactly sign-reversal-invariant integer residue predicate.

Fix any reduced a/b with 0<a<b, b>=2. Let T=110b. For signs s in {-1,+1} define periodic denominator masks
\[
R_s(a,b)=\left\{q\bmod T:\ b\mid aq+s,\quad C_{11}\left(\frac{aq+s}{b},\frac{(b-a)q-s}{b}\right)\right\}.
\]
Assume the masks nonempty (the inherited anchor-neighbor theorem gives this in its domain). Define backward deficit and forward waiting time on the periodic extension:
\[
r_s(H)=\min\{t\ge0:H-t\bmod T\in R_s\},\quad
f_s(H)=\min\{t\ge0:H+t\bmod T\in R_s\}.
\]
All residue quantities here are integers, not native X6 spatial coordinates. Expectations below refer to the **uniform finite ensemble H mod T**, not a stochastic time or physical ensemble.

## Theorem 1 — Universal mirror duality and one-sided marginal equality

For every reduced rational a/b in the stated domain,
\[
\boxed{R_+(a,b)=-R_-(a,b)\pmod{110b}},\qquad
\boxed{r_+(H)=f_-(-H)\quad(\bmod T)}.
\]
In particular R_+ and R_- have the same number of allowed residues and the same cyclic-gap multiset. Their backward deficit histograms are *identical*, not merely equal in mean.

**Proof.** Take q with b dividing aq-1, let h=(aq-1)/b and n=((b-a)q+1)/b. At q'=-q and sign +, the new pair is h'=-h, n'=-n. The frozen predicate is invariant under simultaneous negation, hence q in R_- iff -q in R_+. Reversing a cyclic finite set reverses the order of its gaps but preserves their lengths. The waiting identity is immediate because H-t belongs to -R_- iff -H+t belongs to R_-.

For a cyclic set with ordered gaps g_1,...,g_m (positive integers summing T), the backward deficit t occurs exactly as often as there are gaps longer than t:
\[
\boxed{\Pr(r_s=t)=T^{-1}\#\{i:g_i>t\}}.
\]
Consequently
\[
\boxed{\mathbb E[r_+]=\mathbb E[r_-]=
 \frac{1}{2T}\sum_i g_i(g_i-1)}
\]
and *every* one-sided moment agrees. Write
\[
\rho=(r_-+r_+)/2,\qquad A=(r_+-r_-)/2.
\]
Equal marginals give the universal identities
\[
\boxed{\mathbb E[A]=0,\qquad
\operatorname{Cov}(\rho,A)=
 \frac{\operatorname{Var}(r_+)-\operatorname{Var}(r_-)}4=0.}
\]
These conclusions require neither a fixed-lag relation nor independence of rho and A.

This also supplies a universal **one-sided reflection readout** from the minus mask, by observing its forward waiting time at the reversed height. It differs from the special EC49FVX identity r_+(H)=r_-(H-168), which involves a single constant translation at a/b=1/2.

## Theorem 2 — The fixed-delay reconstruction does not extend to every rational anchor

For the *uncertified* anchor a/b=1/7, the exact masks have T=770, |R_-|=|R_+|=60, maximum cyclic gap 42, and individual minimal period 770. The ordered gap multiset of R_- is
\[
7^{\times36},\ 14^{\times12},\ 21^{\times1},\
28^{\times9},\ 35^{\times1},\ 42^{\times1}.
\]
The cyclic ordered *adjacent-gap* pairs have the asymmetric counts
\[
\boxed{N_{R_-}(14,7)=10\ne2=N_{R_-}(7,14).}
\]
If R_+ were a fixed translate R_-+d for an integer d, the cyclic gap word of R_- would have to be a cyclic rotation of its reversal, since R_+=-R_-. Such a dihedral symmetry forces equal counts of each ordered adjacent-gap pair (x,y) and its reversal (y,x). The displayed 10 versus 2 contradiction rules out *every* fixed d modulo 770. As equality r_+(H)=r_-(H-d) for all H would give the same translated zero sets, it is also impossible:
\[
\boxed{\text{For a/b=1/7, no integer d satisfies }r_+(H)=r_-(H-d)\text{ for all H}.}
\]
This is a finite exhaustive no-go counterexample **within the frozen certificate model**; the universal mirror/forward-waiting identity of Theorem 1 still holds.

The exact 770-class finite spectrum additionally gives
\[
0\le r_\pm\le41,\quad
\mathbb E[r_\pm]=494/55,\quad
\operatorname{Var}(A)=9531/220,
\]
and 119 distinct ordered residual pairs. In particular the signed asymmetry is genuinely nonzero on many height classes although its uniform mean vanishes.

## Exact gap observer and inherited bridge

The original strict nearest-neighbor theorem EC49FVU identifies, for H>16b (subject to its frozen assumptions), the actual strict certified neighbors of a/b as
\[
x_-=\frac{a q_- -1}{bq_-},\quad x_+=\frac{a q_+ +1}{bq_+},
\quad q_\pm=H-r_\pm(H).
\]
Hence for H>16b:
\[
L=\frac1{b(H-r_-)},\quad R=\frac1{b(H-r_+)},\quad
R-L=\frac{2A}{b(H-r_-)(H-r_+)}.
\]
The signed gap midpoint M=(R-L)/2 obeys
\[
\boxed{bH^2M=A\frac{H^2}{(H-r_-)(H-r_+)}.}
\]
At fixed a/b, periodic deficits imply bH^2M approaches the height-class-dependent value A. The scalar rho is insufficient for this directed observer, while (rho,A) exactly recovers both deficits. For 1/7, C11(1,6) is false, so the strict-neighbor interval is an actual certificate-free gap when H>112. This physical or native-geometric interpretation is **not** asserted: these are auxiliary rational-phase exclusion certificates.

## Exact reproducibility and evidence

The companion EC49FVY_REFLECTION_VERIFY.py rebuilds P10 from the original 11-row projective formula; independently checks 12,100 direct cases; exhausts all 45 reduced anchors with denominators 2 through 12 for reflection, marginal and orthogonality identities; exhausts all 770 residues at 1/7 for the gap and joint statistics; checks all 770 candidate translations; and independently enumerates *all* reduced certified fractions for H=113,137,177,231,331, checking actual closest strict neighbors and exact midpoint algebra. The captured EC49FVY_REFLECTION_OUTPUT.txt ends ALL PASS. Exact integer and Fraction arithmetic throughout; no floating-point inference.

The universal theorem is symbolic after the exact finite P10 sign-symmetry check. The no-delay counterexample is a complete finite 770-residue certificate. The actual-neighbor assertion is dependent on EC49FVU; parent Bernoulli-to-projective bridge and independent mathematical review remain open provenance obligations.

**Next question:** classify exactly which reduced a/b admit an exceptional translation R_+=R_-+d, as a dihedral symmetry problem on finite cyclic masks, and use non-reflection-symmetric gap words as succinct impossibility certificates. In parallel, seek a uniform moving-anchor Farey bound for the separate global conjecture lim_{H->infty} H G_max(H)=1.