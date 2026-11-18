# R284S — Exact rank-one quadratic-obstruction test for a smaller Port comparison grid

Date: 2026-11-18. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK / NOT_REVIEWED**.
Frozen scientific source input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Direct predecessor: R284R, research_notes/portable_direct/R284R_OBSERVER_RELEVANCE_ADAPTIVE_PORT_GRIDS_20261118.md at 30daec7b00034bef933847b0e16b234b7c7eec5f.
Scope: exact auxiliary nonnegative-rational *named BRC Port* rank-one additive edits and declared matched outputs, following R281–R284R. P000, provenance and native X6 typing are preserved as separate prerequisites for any transfer.

## 1. A single-edit normalized difference has one explicit quadratic obstruction

Fix a named edit index \(i\), one output interface \(q\), and all other edit coordinates \(z=(x_j)_{j\ne i}\). For model \(h=1,2\), write \(T_h(z)=[I-W_h-\sum_{j\ne i}z_jE_{hj}]^{-1}\) and define the four exact rational transfer entries

\[
 A_h(z)=(T_h)_{a_hb_h},\qquad
 B_h(z)=(T_h)_{a_hu_{hi}}(T_h)_{v_{hi}b_h},\qquad
 C_h(z)=(T_h)_{v_{hi}u_{hi}}.
\]

For every admissible pair \((z,x_i)\), the rank-one resolvent identity gives
\[
 F_{h,q}(z,x_i)=A_h(z)+\frac{x_i B_h(z)}{1-x_i C_h(z)}.
\]
Each denominator \(1-x_iC_h(z)\) is nonzero on the strictly stable admissible domain; the rational identity extends formally wherever its denominators are nonzero.

Put \(\Delta A=A_1-A_2\). The *exact normalized cross-difference* is

\[
 [F_{1,q}-F_{2,q}](1-x_iC_1)(1-x_iC_2)
   =Q_0(z)+Q_1(z)x_i+Q_2(z)x_i^2,
\]
where
\[
 Q_0=\Delta A,\qquad
 Q_1=B_1-B_2-\Delta A(C_1+C_2),\qquad
 \boxed{Q_2=\Delta A\,C_1C_2+B_2C_1-B_1C_2}.
\]

The coefficient \(Q_2\) is a rational function in the other named edit variables; it can be checked exactly by rational symbolic arithmetic or a justified exact coefficient certificate. It is **not** decided by cycle reachability alone. This formula follows by multiplying out the displayed rank-one resolvents. In particular, it remains valid for repeated edit endpoints provided the labels are kept distinct.

## 2. Theorem R284S-A: two, or even one, test weights for a cycle-bearing coordinate

**Statement.** Fix one edit coordinate \(i\) for which the prior R284R shared grid calls for three points; keep R284R's original per-coordinate node choices for every other coordinate.

- If \(Q_{2,q}(z)\equiv0\) as a rational function **for every declared output \(q\)**, then use only **two distinct, jointly admissible** sample weights for \(x_i\). Equality of the two models at all reduced-grid nodes implies their full rational response equality for every declared output and every common admissible edit vector.
- If in addition \(Q_{1,q}(z)\equiv0\) for every declared output, use only **one** admissible sample weight for \(x_i\); the same full-horizon equality conclusion holds.
- If the corresponding identities hold for several coordinates simultaneously, the reductions can be made together, provided each identity is genuine in *all remaining edit variables*, not merely at a current observation vector.

**Proof.** Fix a node \(z\) in the original R284R grid for every coordinate other than \(i\). Under \(Q_2(z)=0\), the normalized output difference is a polynomial of degree at most one in \(x_i\), divided by a nonvanishing product. If two distinct samples produce equal outputs, this polynomial has two roots and is identically zero. Consequently, equality also holds at the third \(x_i\) node omitted from the reduced grid. Thus the full original R284R grid is equal, and theorem R284R-A supplies rational-function equality on the complete admissible domain.

If both \(Q_1(z)\) and \(Q_2(z)\) vanish, the normalized difference numerator is constant in \(x_i\), so one equality sample forces it to be identically zero. For multiple coordinates, restore the omitted grid layers one coordinate at a time. The global identities in *all remaining variables* ensure the argument remains valid even as other coordinates take their restored values. QED.

**Finite-data variant for one coordinate.** To reduce only a single coordinate \(i\), it suffices to have certified \(Q_{2,q}(z)=0\) (and \(Q_{1,q}(z)=0\) for the one-point variant) at each node \(z\) of the **original full R284R grid for the other coordinates**. This bounded certificate implies all omitted \(x_i\) sample equalities and then invokes R284R. It does not claim the rational identity \(Q_2\equiv0\) beyond those nodes.

**p-adic consequence.** When global rational identities eliminate the quadratic (or both nonconstant) coefficients, the original reduced cross-product polynomial really has the correspondingly lower coordinate degree. R284R-B therefore applies with two (or one) nodes for such a coordinate. With \(p=2\), each certified three-to-two reduction saves **one interpolation-loss digit** if the standard \(0,1/Q,2/Q\) node family is used. The target resonance-stratum bound \(s(x)\le T\) and matching observation precision remain necessary. The rank-one formula is an **exact coefficient test**, not a reason to erase any Port source/branch data.

## 3. Two exact examples discriminating the quadratic obstruction

Use Ports \(0,1,2\), observer \((0,0)\), the sole named edit \(1\to2\) with weight \(x\), and baselines \(0\to1=a,\ 2\to0=b,\ 2\to1=\gamma\). For all stable edits,

\[
 F(x)=\frac{1-\gamma x}{1-(\gamma+ab)x},\quad
 A=1,\quad B=ab,\quad C=\gamma+ab.
\]

**Both models cyclic, but only two nodes are needed.** Model 1 takes \((a,b,\gamma)=(1/4,1/4,0)\), model 2 takes \((1/4,1/2,0)\). Then

\[
 F_1(x)=\frac1{1-x/16},\qquad F_2(x)=\frac1{1-x/8};
 \qquad (Q_0,Q_1,Q_2)=(0,-1/16,0).
\]

The edit is relevant and lies on a transfer cycle in **both** models. R284 and R284R would use three \(x\)-nodes, but \(Q_2=0\) proves two suffice. At \(x=0\) both readouts equal 1; at \(x=1/4\), they are \(64/63\) and \(32/31\). Thus a single node at zero is insufficient for this class, while the second node detects inequality. More generally equality on any two distinct stable samples is a complete certificate for this model pair.

**Three nodes may be necessary.** Retain model 1 and take model 2 with \((a,b,\gamma)=(1/4,15/64,1/4)\). The exact coefficients are

\[
 (Q_0,Q_1,Q_2)=(0,1/256,-1/64).
\]

The two responses agree at \(x=0\) and \(x=1/4\), yet differ at \(x=1/2\):
\[
 F_1(1/2)=32/31,\qquad F_2(1/2)=448/433.
\]
This is the R282 two-node counterexample rewritten as a nonzero \(Q_2\) obstruction, verifying that the extra sample is sometimes essential.

## 4. Exact checks, dependencies and next unit

The coefficient formula and both examples were evaluated with Python standard-library Fraction arithmetic, using an independently implemented Gauss–Jordan inverse of each three-by-three rational matrix. For the two examples and an identical-model control pair, the calculated \((Q_0,Q_1,Q_2)\) triples were respectively \((0,-1/16,0)\), \((0,1/256,-1/64)\), and \((0,0,0)\). For each pair, four values \(x\in\{0,1/16,1/4,1/2\}\) satisfied exactly
\[
 (F_1-F_2)(1-xC_1)(1-xC_2)=Q_0+Q_1x+Q_2x^2.
\]
All 24 direct matrix inversions in those 12 model-pair/sample comparisons were exact; the numerical checks are examples, while the universal claim follows by the rank-one identity and polynomial root/interpolation proofs. Source formulas used are R281, R282, R284 and R284R; the rank-one identity itself is standard algebra.

**Next:** Design a joint exact certificate for all \(Q_{2,q}\) identities that avoids constructing the entire full multivariate rational response. Track numerator/denominator polynomial degrees and p-adic coefficient valuations, distinguish a graph-certified zero from an accidental cancellation, and quantify preprocessing, test count and bit complexity before claiming an end-to-end algorithmic gain.
