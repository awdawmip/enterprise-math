# PREFIX-600-R6 — Native BRC 48-phase sparse inverse and minimal full-seven codec

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_NATIVE_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Native implementation: research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py (verified Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41).
Frontier: PREFIX-598/599, current read at enterprise-math/main@a1f9c1acc906f56b77be59c6805ca5151df23bb2.

## Exact question and scope

The frozen native kernel has 48 signed phases, 96 original ports (phase,source-bit), six equiprobable labeled actions, nine allowed roots, six original axis-BRC rewards, and one gate reward. O7 observes the entire seven-reward vector jointly with the exact next original port. O7act additionally observes the native action (slot,newbit). Initial laws may be arbitrary rational or real probability distributions. The goal is a **combinatorial**, root-uniform proof of the one-step observer ranks 49/50 reported by PREFIX-599, plus an explicit reconstructing codec.

## Theorem 1: combinatorial determinant

Let M be the 48x48 integer adjacency matrix counting the three native phase successors in NEXT. Native phase signs reverse on each move. After ordering the 24 positive-c phases and the corresponding sign-inverted negative-c phases,

$$M\sim\begin{pmatrix}0&B\\B&0\end{pmatrix}.$$

Identify a positive-c phase with (a,p,c), where p and c are distinct positive magnitudes in its three-element star S_a. If k is the third member of S_a, and b is the *other* star containing edge c, the sign-relabelled successor list is

$$(a,p,c)\longmapsto (a,c,k),\quad (b,c,k_1),\quad(b,c,k_2),$$

where {k_1,k_2}=S_b\setminus{c}. Let W be the internal successor permutation; it consists of eight disjoint 3-cycles, hence det W=1. Let E={(a,c):c in S_a} be the 12 incidences of four stars with their six shared edges. Define U (24x12) to mark the outgoing incidence (a,c) and V (12x24) to mark the two cross-star successors. Then B=W+UV.

The involution J on E sends (a,c) to (b,c). It has six transpositions. Each cross-star successor (b,c,k_i) has a unique W-predecessor with outgoing incidence (b,c). Thus exactly:

$$\boxed{VW^{-1}U=2J,\quad J^2=I_{12}.}$$

The determinant lemma now gives

$$\det B=\det W\det(I+VW^{-1}U)=\det(I+2J)=(-3)^6=729,$$

and therefore

$$\boxed{\det M=(\det B)^2=3^{12}=531441.}$$

This proves phase-background independence *uniformly over all nine roots* without any of the eighteen PREFIX-599 rational rank eliminations, since M contains only the original phase successor relation.

## Theorem 2: 4-sparse exact inverse

Since (I+2J)^{-1}=(2J-I)/3, Woodbury yields

$$\boxed{3B^{-1}=3W^{-1}-W^{-1}U(2J-I)VW^{-1}.}$$

For this exact four-star incidence, each row of 3B^{-1} has precisely four nonzeros, with multiset (-2,+1,+1,+1). The same pattern holds for 3M^{-1}. This follows from the displayed native integer incidence construction and is independently checked as a finite 24-row identity by the companion executable certificate, including *both* left and right inverses.

For any normalized initial law pi on all 96 ports, let a_p=pi(2p)+pi(2p+1) be its initial phase marginal. The observable next-phase marginal z satisfies

$$z=aM/3,\qquad\boxed{a=z(3M^{-1})}.$$

The exact recovery uses 192 nonzero integer-coefficient contributions instead of the 2304 positions in a dense 48x48 matrix.

## Theorem 3: sharp, physically interpretable linear codecs

Exactly three source phases P={3,14,15} feed the gate target phase 4. Their target slots are 0,1,1, and all share source signed component +1 and target signed component -3. Thus their six native axis-BRC rewards agree for every allowed root; the starting branch bit can only turn the sole gated (target-slot,newbit=1) event from gate 0 to gate 1.

Let H_r(a) be the **actual frozen native O7 output law** with the above a phase masses, represented using source bit 0 in each phase. Put gamma=pi(7)+pi(29)+pi(31). Let e^0_r and e^1_r be the two output atoms at next original port 9, with identical six-axis BRC reward and gate 0/1. Then

$$\boxed{L_r(\pi)=H_r(a)+\frac{\gamma}{6}(e^1_r-e^0_r).}$$

Since h=Pr(gate=1)=gamma/6, the **nonnegative observable summary** (z,h) is sufficient to reconstruct the *entire* O7 joint law at every root. z sums to one, so this is 48 independent variable coordinates.

For O7act, put gamma_0=pi(7), gamma_1=pi(29)+pi(31). Their observable counterparts are h_s=Pr(gate=1,slot=s)=gamma_s/6 for s=0,1. With action-aware atoms e^b_{r,s}, the exact law is

$$\boxed{L^{act}_r(\pi)=H^{act}_r(a)+\sum_{s=0}^1\frac{\gamma_s}{6}(e^1_{r,s}-e^0_{r,s}).}$$

Thus (z,h_0,h_1) gives 49 independent normalized coordinates for O7act. Both formulas call the original six-axis BRC edge function; they preserve *all* components and the exact next original port under their stated output languages.

These dimensions are sharp. The 48 phase-background source rows project to linearly independent next-phase marginals by det M != 0. All 45 non-gate phases have zero source-bit contrast. The remaining three contrasts span exactly one output direction without action labels and exactly two with slots 0/1 retained, with zero next-phase projection. Therefore:

$$\operatorname{rank}L_r=48+1=49,\qquad
\operatorname{rank}L_r^{act}=48+2=50.$$

Normalization removes one degree of freedom: the sharp variable-coordinate counts are 48/49. This argument applies to each of nine roots individually, without rational Gaussian elimination. The one-step joint law includes exact next original port, so by conditioning on that port and applying the original Markov kernel the same summary preserves every future ordered output/terminal-port law at length >=1, including root-selection policies depending on the respective observed history and independent exogenous randomness.

## Reproducibility

Companion program: research_notes/portable_direct/PREFIX600_R6_compact_native_certificate.py. It checks the original frozen PREFIX-565 Python source against Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41; builds M,W,U,V,J directly from the original PHASES/NEXT/edge; checks eight 3-cycles, B=W+UV, VW^{-1}U=2J, J^2=I, both inverse orders, every row's (-2,1,1,1) pattern, all 48 pure-phase recovery identities, and 9 roots x 2 observer alphabets x 96 ports = **1728 complete native seven-reward/output histogram identities**. Runtime: stdlib Python exact integer/Fraction, no floats. Observed result: ALL_CHECKS_PASS; det B=729; det M=531441. All 96 source-port linear basis cases were checked; linearity yields the formulas for any initial mixture. The supporting full-length local proof and longer independent verification program are also preserved in the handoff evidence bundle.

Reuse: REUSE_EXECUTED PREFIX-565 typed native edge; REUSE_APPLIED PREFIX-598/599 gate-predecessor geometry and observer scope. The sparse phase inverse uses 192 integer scaled additions; emitting a complete one-step law requires up to 48x6=288 original action contributions plus gate correction(s), and multi-step history output retains its support/bit cost. This is a model-internal exact result, pending independent mathematical review and formal Source Result/Review.

Next: examine unrestricted positive latent realizations for the full-seven O7/O7act languages, multi-depth branch-support/bit complexity, and whether the same W+UV/J sparse inverse pattern persists for enlarged native BRC phase graphs and gate target sets.
