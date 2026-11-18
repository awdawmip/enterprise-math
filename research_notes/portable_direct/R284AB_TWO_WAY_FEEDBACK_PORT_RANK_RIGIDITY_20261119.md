# R284AB — Feedback-robust gate factorization: strongly connected positive Port networks with no fixed common kernel

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASSED / NOT_REVIEWED**.
Predecessor: R284AA gate-factorization witness (its complete GitHub main publication `R284AA_GATE_FACTORIZATION_PORT_NO_COMMON_KERNEL_20261119.md`); earlier R284Y and R284Z. Frozen scientific pin remains `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The object is an auxiliary exact finite rational Port observation with distinct named paths, not a new P000 native-spatial object, BRC–Shor physical computation, CLAIM, Result or independent Review.

## New theorem AB1 — Internal feedback cannot undo the gate/core determinant certificate

Let `k>=2`. Consider disjoint input ports P, interior entrance ports A, interior exit ports B and output ports Q, each an ordered set of size k. Nonzero W blocks are:

- `W_PA=D_g` and `W_BQ=D_h`, where all g_i,h_j are positive and independently editable;
- `W_AA=L`, `W_AB=C`, `W_BA=D`, `W_BB=U`, **with unrestricted nonnegative feedback edges inside and between the two interior layers**;
- all other edges vanish; W is strictly row-substochastic.

Order S=(A,B) and form the complement A_Port=(I-W)[(S,P),(S,Q)]. Put

`G=I-W_SS=[[I-L,-C],[-D,I-U]]`, `K=I-L`, `H=I-U-D K^(-1) C`.

Both K and H are invertible because W_SS is strictly substochastic (the inverse of G exists, and the nonnegative principal L has spectral radius below one). The upper-right block of the *full feedback resolvent* is

`(G^(-1))_(A,B) = K^(-1) C H^(-1)`,

and the terminal response is therefore

`T = D_g K^(-1) C H^(-1) D_h`.

**Exact identities, with no acyclicity or diagonal-loop hypothesis:**

`rank(A_Port)=2k+rank(C)`,

`det(A_Port)=(-1)^k * (product_i g_i h_i) * det(C)`.

In particular, feedback blocks L, D, U cannot change either the complement determinant or its rank in this stated gate/core geometry. They can, and generally do, change individual nonzero transfer entries and other observations.

**Proof.** Invert K and use the block Schur complement of G:
`det G=det K det H`, and `(G^(-1))_(A,B)=K^(-1) C H^(-1)`. The Port complement has the form
`A_Port=[[G,-W_SQ],[-W_PS,0]]`; its Schur complement is -T. Hence
`det A_Port=(-1)^k det G det T=(-1)^k (prod g_i h_i) det C`.
All four flanking factors of C in T are invertible, giving rank T=rank C; the block elimination gives rank A_Port=2k+rank T. No power series is required for the algebraic argument; strict substochasticity supplies the required invertibility and nonnegative resolvent. QED.

## Corollary AB2 — Strongly connected counterexample to the previously open Port-witness question

Take k=2, choose a strictly positive singular C of rank one, and choose strictly positive L,D,U with sufficiently small row sums. With all four gate variables g1,g2,h1,h2 independently varied over a nontrivial product interval, A_Port has a support perfect matching, is **singular for every parameter value**, has rank exactly five, and has **no fixed nonzero right or left kernel** even though the internal Port graph is strongly connected.

**Proof of no-common-kernel.** Let F=K^(-1) C H^(-1). Because C>0 and the nonnegative resolvent blocks have strictly positive diagonals, F is entrywise positive and rank one. If T(z)q=D_g F D_h q=0 holds for *every* h, take the difference of two positive parameter values differing only in h_j: F e_j q_j=0, forcing q_j=0. This works for each j; thus the intersection of all right kernels of T is zero. Vary each g_i independently to deduce that the intersection of all left kernels is zero. Any constant right kernel vector (s,q) of A_Port must satisfy s=G^(-1)W_SQ q and Tq=0; similarly a constant left kernel (r,p) gives p^T T=0. Hence the corresponding full complementary-matrix kernel intersections are both zero.

A perfect support matching exists because paths p1->a1->b1->q1 and p2->a2->b2->q2 use disjoint vertices. Swapping the two b channels gives the second terminal permutation. Every row and column in the complement participates in one of these path-supported matchings. Strong connectivity of S follows by declaring all entries of L,C,D,U positive. QED.

**Exact routing explanation.** Both disjoint terminal path families must use a1,a2,b1,b2 as entrance/exit vertices; consequently a disjoint routing *cannot* use an internal feedback edge without revisiting or colliding with the other required entrance/exit vertex. Its two R284Z route sums are
`g1*g2*h1*h2*C11*C22` and `g1*g2*h1*h2*C12*C21`.
All internal feedback factors are excluded from these path-pair contributions, not discarded from the individual resolvent: they remain in T. Their signed difference is precisely the AB1 determinant formula when k=2. When det C=0, the two *positive* pairing sums cancel exactly, while the perfect matching survives.

## Fully specified nonnegative stable eight-Port example

Vertex order: P=(0,1), A=(2,3), B=(4,5), Q=(6,7). Fixed interior matrices:

`L=[[1/16,1/32],[1/64,1/24]]`,

`C=[[1/16,1/16],[1/16,1/16]]`,

`D=[[1/32,1/48],[1/40,1/64]]`,

`U=[[1/20,1/36],[1/48,1/28]]`.

Set `g1=1/8+x, g2=1/8+y, h1=1/8+u, h2=1/8+v` with **four independently named single-edge changes** and `0<=x,y,u,v<=1/16`. Every W row has sum strictly less than one, including feedback edges B->A. The internal graph has nontrivial directed cycles such as a1->b2->a2->b1->a1 (and several two-cycles).

At baseline x=y=u=v=0, the exact rational determinant of G is

`det G = 14448047/17694720 > 0`.

The complementary determinant remains zero throughout the product box; exact rank is five, while each two-point stacked left/right-kernel test has rank six.

**Discriminating edit:** Let an additional independent central edit `eta:E_(2,4)` perturb C11 alone. Then

`det A_Port(eta) = g1*g2*h1*h2*eta/16`.

At eta=1/32 and zero gate edits, this equals exactly `1/2097152` and the complement has full rank six. Thus the zero determinant is a scoped gate/edit-family identity, not a claim of invariance under arbitrary future Port perturbations.

## Exact verification and algorithmic implication

Executable: `research_notes/portable_direct/R284AB_feedback_robust_port_checker.py`; source result: `research_notes/portable_direct/R284AB_feedback_verification.json`.

Standard-library `fractions.Fraction` is used for exact Gaussian elimination, rank, full 4x4 internal inversion, 6x6 complement determinants, matching enumeration and two separately stacked left/right kernels. Actual PASS scope: **81** four-gate grid configurations checked for stability, perfect support matching, exact Schur/determinant identity and rank five; **16** configurations with positive central edit checked for nonzero determinant and rank six; exact full 6-rank left/right stacked tests. The mathematical theorem is proved algebraically; finite checks verify this implementation and explicit model.

This extends R284AA from independent self-loops to **genuine strongly connected intra- and inter-layer feedback**. Its certificate has constant control size for fixed k: inspect the typed gate/core block pattern and test det C (O(k^3) exact field operations); it does not require any tensor grid in the gate variables. This does not prove a universal fast identity test for arbitrary Port networks or a native Heartbeat/BRC physical correspondence.

## Next precise problem

Determine when arbitrary named edits **inside** the recurrent internal feedback network, including C as well as L,D,U, can retain the complementary determinant identity. Under AB1, any edits restricted to L,D,U preserve it exactly, while an independent edit to C may destroy it. Classify the largest linear subspace of allowed C-edits tangent to the determinantal variety that gives a **global** identity, not merely first-order zero derivatives. Preserve all Port identities and future-edit scopes; no native-X6 compression or physical residual attribution is asserted.
