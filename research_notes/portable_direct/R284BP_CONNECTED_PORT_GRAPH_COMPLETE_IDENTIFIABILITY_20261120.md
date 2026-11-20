# R284BP — Complete connectivity theorem: every connected editable-Port graph identifies a positive matrix

Date: 2026-11-20 (Asia/Shanghai). Research status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. This is independent portable TASK_RESEARCH material, not a formal Task CLAIM, Result, or Review.

## Frozen scientific lineage

Continuing the same typed auxiliary determinant observer:
- R284BM (sharp n−1 edit-location obstruction and directed-star sufficiency), immutable proof `a2537fde3598cef07a8a31eca0b0a676d143f29e`;
- R284BN (connectedness iff identifiability for n=3), immutable proof `6448f2061ecf5154d5999d2b014747f6c724410b`;
- R284BO (directed-path coefficient and semiconnected sufficiency), immutable proof `8c95416c799483c7d921b920643e0d7505e99ecc`.

This result resolves their stated open problem for arbitrary n and any mixed orientation. No P000 axiom, X6 coordinate, BRC native carrier, or physical measurement assertion is changed.

## Model

Let n≥2 and let E be any set of directed editable off-diagonal positions among n named vertices. Write U(E) for the undirected support graph and define the formal determinant polynomial

```text
F_C^E(d,z) = det(diag(d_0,...,d_{n−1}) − C − sum_{(a,b) in E} z_ab E_ab).
```

The entries C_ij are strictly positive rational numbers (in particular, they may be positive integers). Every d_i and every z_ab is an independently labeled formal variable. For a monomial m, write [m]F for its coefficient with all unspecified variable exponents zero.

## Theorem BP1 — Exact if-and-only-if graph criterion

**For every n≥2, the map C↦F_C^E is injective on the set of strictly positive rational n×n matrices if and only if U(E) is connected.** The same iff criterion holds on the entire bounded integer population `{1,...,H}^{n×n}` for every integer H≥2.

**Necessity.** When U(E) is disconnected, R284BM constructs a pair of distinct {1,2}-matrices C,C' with exactly the same formal response polynomial using diagonal similarity across a component cut. The pair belongs to every H≥2 positive-integer population.

**Sufficiency via an explicit spanning-tree induction.** Let T be any directed choice of a spanning tree in E (one of the available directed arrows for each undirected tree edge). Use these coefficient identities, valid for all a≠b and w outside {a,b}:

```text
U_i       = [product_{k != i} d_k] F
          = -C_ii

V_ab      = [product_{k notin {a,b}} d_k] F
          = C_aa C_bb − C_ab C_ba

W_ab      = [z_ab product_{k notin {a,b}} d_k] F
          = -C_ba               for (a,b) in E

T_ab,w    = [z_ab product_{k notin {a,b,w}} d_k] F
          = C_ba C_ww − C_bw C_wa.
```

The W/T identities result from the transposition and three-cycle terms in the relevant 2×2 or 3×3 determinant expansion; all other rows select their diagonal variable. Only monomials containing zero or one editable Port variable are required.

From U recover all diagonal entries. From U,V recover every reciprocal product `P_ab=C_ab C_ba`. Root T at any vertex, initialize its one-vertex induced matrix, and attach vertices along tree edges. Suppose entries inside the already attached set S are known. Let v be a new vertex joined to an old vertex u by editable arrow (a,b), either (u,v) or (v,u).

First W_ab gives `C_ba=-W_ab`, and `C_ab=P_ab/C_ba`. Thus both connections between u and v are determined. For each w∈S\{u}, the coefficient T_ab,w gives one of the two remaining connections:
- If a=u and b=v, `C_vw=(C_vu C_ww − T_uv,w)/C_wu`; then `C_wv=P_vw/C_vw`.
- If a=v and b=u, `C_wv=(C_uv C_ww − T_vu,w)/C_uw`; then `C_vw=P_vw/C_wv`.

All denominators are nonzero by strict positivity. This completes every row and column involving v, so induction reconstructs all n² entries. The only property used is the existence of a connected spanning tree. QED.

## Theorem BP2 — Exactly n² coefficients suffice

Fix a spanning tree and an order of vertex attachment. The preceding reconstruction uses the following **n² separately identified polynomial coefficient values**:

```text
n diagonal coefficients U_i
+ binom(n,2) principal-pair coefficients V_ab
+ (n−1) spanning-tree edge coefficients W_ab
+ binom(n−1,2) three-vertex coefficients T_ab,w
= n².
```

All selected Port-dependent monomials are linear in one z_ab (no z_e z_f terms). Given their exact values, recovery needs O(n²) rational arithmetic operations and divisions by positive matrix entries. This is a **coefficient-access** complexity bound, not a claim that an arbitrary physical or black-box determinant instrument supplies n² coefficients at that cost. The count is a constructive sufficiency certificate, not a proved minimum for arbitrary encodings.

## Corollary BP3 — Edge-count-optimal one noiseless modular scalar

For any connected E, n≥2 and H≥2, there exists a prime p and a fixed nonadaptive setting of every diagonal/Port control in F_p, such that **one noiseless residue** F_C^E(d,z) mod p uniquely identifies every C∈{1,...,H}^{n×n}. To prove existence, let N=H^{n²}, J=binom(N,2), M=n!(H+2)^n. For each C≠C', BP1 gives nonzero `Q=F_C−F_C'` over Z. The homogeneous degree-n part of F_C is `det(diag(d)−sum z E)`, independent of C; hence deg Q≤n−1. The coefficient ℓ¹ norm of each F_C is at most M, so any p>2M preserves Q as a nonzero polynomial in F_p. Schwartz–Zippel over uniformly sampled controls gives pairwise collision probability ≤(n−1)/p. Choosing any prime p>max(2M,J(n−1)) makes the global union bound <1. A collision-free setting therefore exists.

R284BM's disconnected binary pair shows that no number of adaptive exact reads can rescue a disconnected E. Consequently **connectedness is necessary and sufficient for universal noiseless single-scalar existence under sufficiently large finite-field controls**, and the sharp minimum number of editable locations is n−1, attained by **every orientation of every spanning tree**. The candidate-table decoder can require exponential time; noisy recovery, minimal p, and native modular instrumentation remain separate optimization questions.

## Reproducible author verification

The standard-library Python checker `R284BP_connected_graph_reconstruction_checker.py` uses exact integer Leibniz determinant polynomials from R284BM, extracts the stated n² coefficients, and reconstructs C with exact Fraction arithmetic:

- n=2: all 2 directed trees × all 16 binary matrices = 32 reconstructions, 4 coefficients each.
- n=3: all 12 oriented trees × all 512 binary matrices = 6,144 reconstructions, 9 coefficients each.
- n=4: all 128 oriented labeled spanning trees × 4 fixed-seed positive matrices = 512 reconstructions, 16 coefficients each.
- n=5: first 50 oriented spanning-tree instances × 2 fixed-seed positive matrices = 100 reconstructions, 25 coefficients each.

Every reconstructed entry matched its input exactly. These are exhaustive in the specified n≤3 families and stated finite sampled families at n=4,5. BP1–BP3 are proved algebraically and probabilistically, respectively, independent of finite experimental coverage. Independent mathematical review remains NOT_REVIEWED.

## New research frontier

With polynomial identifiability settled for every connected support graph, compare graph orientations and spanning-tree topology under *one fixed scalar* at finite p: separation margin against bounded adversarial noise, deterministic compact controls, and coefficient/readout cost. Test whether the spanning-tree reconstruction coefficients can be encoded or queried with significantly less instrumentation or precision than the R284BG/BJ constructions while preserving the exact named-Port observer and provenance.
