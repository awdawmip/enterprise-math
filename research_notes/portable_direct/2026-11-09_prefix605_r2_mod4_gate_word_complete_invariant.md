# PREFIX-605-R2: Four residue-class products completely classify finite gate words on the native X6-BRC 16D tail

**Date:** 2026-11-09 (Asia/Shanghai). **Status:** AUTHOR-SIDE EXACT PROOF + EXECUTED VERIFICATION; INDEPENDENT DRIVER REVIEW PENDING. **Frozen science:** f42f2906d77f24085c123f3ccfe9667d41caa96d, unchanged. **Exact dependency:** PREFIX-602/603 and PREFIX-604 (PRs #1826, #1828). No change to P000, X6 world, or formal task CLAIM.

## 1. Original BRC source and observation

This research retains the original 48 STAR phases, 96 bit ports, 576 individually tagged actions, six native source axes, gate target phase g=4 (zero based), and fixed axis weights (1,1,1,1,0,0). For each native-derived 48-phase transition Q(z), PREFIX-602 proves that after any two updates Q(a)Q(b) with a,b>=0, the image is a common 16-dimensional subspace V, with exact full 48-phase reconstruction E:Q^16→Q^48 and left inverse K.

PREFIX-604 proves the simultaneous splitting V=U4 ⊕ Z12. The gate-insensitive part on Z12 has fourth power 16I12. The gate-sensitive part has, in a fixed common basis,

\[
B(q)=\begin{pmatrix}
0&0&0&4(q+3)\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
\]

The 48-phase **final linear readout after a common two-step transient** is the observer being classified. This is not an equivalence of raw 96-port tagged histories or intermediate-time readouts. Gate step indices encode order, not calibrated physical time.

## 2. Theorem 605.1 — complete all-horizon four-class formula

For an ordered word q=(q1,...,qn), n>=0, define four products, with empty product 1:

\[
p_r(q)=\prod_{\substack{1\le t\le n\\t\equiv r\pmod4}}(q_t+3),\qquad r=1,2,3,4
\]

where r=4 represents t divisible by four. Let m_r(n) be the number of positions of residue r. With one-based four-coordinate basis e_j, put r(j)≡5-j (mod 4), taking values 1..4, and j'=1+(j+n-1 mod 4). Then

\[
\boxed{B(q_n)\cdots B(q_1)e_j
=4^{m_{r(j)}(n)}p_{r(j)}(q)e_{j'}.}
\]

**Proof.** B(q)e_1=e_2, B(q)e_2=e_3, B(q)e_3=e_4 and B(q)e_4=4(q+3)e_1. Before the t-th step, a trajectory starting at e_j lies at coordinate 1+(j+t-2 mod 4). Therefore a weighted wrap occurs exactly when t≡5-j (mod 4). Each wrap contributes 4(q_t+3); every other step contributes 1. Multiplying the factors gives the formula for every length n including all remainders. This identity holds for any real q_t, including -3; admissible native gates use q_t>=0. □

The four statistics and the known n determine the entire 4x4 monomial transfer. At n=4 the result specializes to PREFIX-604's exact diagonal four-cycle identity.

## 3. Theorem 605.2 — necessary and sufficient endpoint word equivalence

For two words q and q' of the same length n, the following are equivalent:

1. p_r(q)=p_r(q') for every residue r.
2. B(q_n)...B(q_1) = B(q'_n)...B(q'_1).
3. The corresponding 16D tail operators are equal.
4. For every nonnegative original 48-phase source y0 and every common two-step transient Q(a)Q(b) with a,b>=0, the resulting complete final 48-phase vectors coincide.

**Proof.** In Theorem 605.1, the four coefficients occupy distinct matrix entries, and their known scalar factors 4^{m_r(n)} are nonzero. Thus (1) iff (2) even at degenerate gates. The 12D action is exactly the same for both words of length n, and the 4D component is a direct invariant summand with injective embedding W and left inverse L; hence (2) iff (3). Full phase reconstruction E is injective. PREFIX-602 proves rank Q(a)Q(b)=16 and im(Q(a)Q(b))=V for every a,b>=0. Thus equal final 48-phase maps on all initial sources are equivalent to equal operators on V. Finally, nonnegative standard basis sources span the original 48D linear input space; so agreement on every nonnegative source is agreement of linear maps. □

**Consequences.** Any permutation of gates among positions congruent modulo four leaves the full final 48-phase transfer unchanged. An arbitrary permutation can change it. This carefully refines PREFIX-603's order-sensitive rank-two defect: *order is relevant between four position classes*, while all within-class ordering is invisible to this final observer after the transient. Intermediate outputs can distinguish such words and are outside this equivalence.

## 4. Theorem 605.3 — smooth exact endpoint summaries require min(n,4) scalar coordinates

Suppose an encoder maps positive n-gate words differentiably into k real scalars, and a differentiable decoder reconstructs the full exact 48-phase endpoint linear operator for all words in an open parameter domain. Then

\[
\boxed{k\ge \min(n,4).}
\]

The p_r statistics use exactly min(n,4) nonconstant scalars, so this lower bound is sharp **in the declared differentiable endpoint-summary class**.

**Proof.** Let h=min(n,4). Fix q_t for t>h at positive constants. The first h positions belong to distinct residue classes and their respective p_r functions are positive nonzero constants times (q_t+3), so the h×h Jacobian is nonsingular. The full 4D transfer exposes p_r in distinct entries, while the full 48-phase observer exposes the 4D transfer injectively by Theorem 605.2. Therefore the differential of the full endpoint operator with respect to those first h parameters has rank h. A differentiable factorization through R^k has derivative rank at most k, giving k>=h. □

No bound is claimed for arbitrary discontinuous encodings, fixed-bit compression, raw tagged histories, or time-indexed observations.

## 5. Exact counterexample and executed checks

Take a common two-step native-derived transient Q(0)Q(1). Let the eight successive gate words be

q=(0,2,1,5,3,4,7,6);
q_same=(3,2,1,5,0,4,7,6), swapping steps 1 and 5;
q_cross=(2,0,1,5,3,4,7,6), swapping steps 1 and 2.

Then q and q_same have the same four class products and their **complete 48x48 final endpoint transfer matrices are exactly equal**. The q_cross word has different class products, and a concrete nonnegative source phase gives a different result: with zero-based final output row 4 and initial basis phase column 32,

\[
[M(q)-M(q_\mathrm{cross})]_{4,32}=-384.
\]

The self-contained program PREFIX605_R2_residue_gate_word_checker.py reconstructs the original native-derived Q matrix from the four STAR triads and the gate source. Its executed checks include: symbolic four-coordinate transfer for n=0..13 inclusive (14 lengths); 30 exact integer/rational nonstationary words of lengths 0..14; exact 16D split/intertwining; exact full 48x48 matrices for the three eight-step words (three times 48 original basis columns); and exact Jacobian ranks for n=1,2,3,4,7,10. All assertions passed with SymPy integer/rational/symbolic arithmetic. Results are stored in PREFIX605_R2_residue_gate_word_results.json.

The theorem's universal force comes from the algebraic induction and the inherited exact native-derived 16D observer/splitting; finite tests check the implementation and examples, not every possible gate word. There is no matrix-exponential or classical pi/trigonometry fallback. This is an exact BRC-derived phase observer theorem, not a physical residual attribution.

## 6. Computational usefulness and next unit

A single pass computes the four residue products using O(n) exact multiplications and four scalar accumulators. For any fixed horizon, these are complete sufficient statistics for every **final phase endpoint query**, reusable across many initial sources. Bit complexity, initial two-step conversion, final 48-phase/96-port recovery and source provenance must be counted separately; no unsupported end-to-end speedup claim is made.

Next discriminator: investigate whether the whole native-derived 48-phase nonnegative cone admits a simultaneous 16D **nonnegative input/transition/output** realization for all z>=0, and compare exact batch workloads with the optimized 96/48/16 algorithms. Retain full original source history when required by future operations.

**Control state:** independent author-side portable research only. No formal task CLAIM, Native Result, independent Driver approval, or Foundation promotion follows from publication.
