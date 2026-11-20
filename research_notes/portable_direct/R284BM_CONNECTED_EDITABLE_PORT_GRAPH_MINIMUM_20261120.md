# R284BM — Sharp editable-Port graph connectivity obstruction and the n−1 control-edge threshold

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. Role: independent portable TASK_RESEARCH. No formal CLAIM, Result, or independent review is asserted.

## Scientific lineage and scope

Continue the frozen auxiliary star-Port determinant observer from R284BJ (`ba9ac42ee03c61e34a057ede0d57561d0c418f6b:research_notes/portable_direct/R284BJ_FINITE_FIELD_INFORMATION_OPTIMAL_PORT_SCALAR_20261120.md`) and the fixed n=3,H=2 witness R284BL-FX1 (`42cd735e6fe3e806079e94616a14e821da4c4d76:research_notes/portable_direct/R284BL_COMPACT_17BIT_THREE_PORT_MODULAR_NOISE_FIXTURE_20261120.md`). This theorem addresses the **number and connectivity of independently editable off-diagonal Port positions**, rather than the modulus or transmission bits.

All matrices below belong to an auxiliary algebraic observer and are not asserted to be a full native X6 three-dimensional slice or BRC physical process. P000 and the frozen scientific hypotheses remain unchanged.

## Exact observer

Let n≥2, V={0,…,n−1}, and E⊆{(i,j):i≠j} be a set of independently editable directed off-diagonal positions. For C∈{1,…,H}^{n×n}, H≥2, define

```text
F_C^E(d,z) = det(diag(d_0,...,d_{n-1}) - C - sum_{(i,j) in E} z_{ij} E_{ij}).
```

The complete response is the formal polynomial in independent variables d_i and z_{ij}. The undirected support graph U(E) forgets edge orientation. A query may choose arbitrary control values and later queries may adapt to previous readings. Equality of the formal response polynomials implies equality of every exact query transcript, also after reducing outputs modulo any integer p.

## Theorem BM1 — Disconnected Port graph gives an exact binary gauge pair

If U(E) is disconnected, there exist two distinct matrices C,C'∈{1,2}^{n×n} satisfying

```text
F_C^E(d,z) == F_C'^E(d,z) in Z[d_0,...,d_{n-1},(z_{ij})_{(i,j) in E}]
```

for every choice of the controls.

**Proof.** Pick a nonempty proper union A of connected components (the component containing vertex 0 suffices), and let B=V\A. Put s_i=2 for i∈A and s_i=1 for i∈B, with S=diag(s_i). Define C by setting every diagonal and within-block entry to 1, every A→B entry to 1, and every B→A entry to 2. Then C'=SCS^{−1} has A→B entries 2, B→A entries 1, and all other entries unchanged. Thus C and C' are distinct strictly positive binary matrices. The matrix D=diag(d) commutes with S. Every editable edge has both endpoints in the same block, hence S E_{ij} S^{−1}=E_{ij} for (i,j)∈E. Consequently

```text
D - C' - sum z_ij E_ij = S (D-C-sum z_ij E_ij) S^{-1},
```

so the two determinants are equal over Q and therefore as integer-coefficient polynomials. This also proves the equality modulo every integer p, including p=2, by reduction of the integer identity. QED.

**Consequence.** With fewer than n−1 editable directed off-diagonal positions, U(E) has fewer than n−1 undirected edges and is disconnected. Thus no finite or infinite number of exact, adaptive determinant reads can distinguish every C in {1,2}^{n×n}. The same obstruction holds for every H≥2, since the binary pair remains in the population. A source-side modular reduction cannot repair this equality.

For arbitrary strictly positive rational C, the underlying diagonal-similarity gauge varies continuously: choose positive constant s independently on each component and conjugate C; this describes a (number_of_components−1)-parameter family after removing common scale. The binary construction above is an exact finite-alphabet witness, not merely a dimension-count argument.

## Theorem BM2 — An n−1-edge directed star is sufficient

Take E_star={(0,i):1≤i<n}. For every n≥2 the map C↦F_C^{E_star} is injective on strictly positive rational matrices (hence on strictly positive integer matrices).

**Proof by coefficient reconstruction.** Write [monomial]F for the coefficient of the indicated monomial, with all unspecified variables of exponent zero. The determinant expansion yields, for i≠j,

```text
u_i  = [product_{k!=i} d_k] F                      = -C_ii
v_ij = [product_{k notin {i,j}} d_k] F             = C_ii C_jj - C_ij C_ji
w_i  = [z_i product_{k notin {0,i}} d_k] F          = -C_i0   (i>0)
t_ij = [z_i product_{k notin {0,i,j}} d_k] F       = C_i0 C_jj - C_ij C_j0
                                                     (i,j>0, i!=j).
```

In the t_ij line the monomial still contains z_i when n=3. These formulas isolate the indicated cycle and transposition terms of the Leibniz determinant. Thus C_ii=−u_i, C_i0=−w_i, and for i>0,

```text
C_0i = (C_00 C_ii - v_{0i}) / C_i0,
C_ij = (C_i0 C_jj - t_ij) / C_j0   (i,j>0, i!=j).
```

All denominators are nonzero by strict positivity. The t_ij family is empty for n=2, where the earlier formulas already recover all four entries. Every matrix entry is therefore uniquely reconstructed. QED.

## Corollary BM3 — Sharp minimum number of Port locations, including one noiseless finite-field reading

For n≥2 and H≥2, the smallest number of independently editable off-diagonal Port positions that permits **universal exact identification of C∈{1,…,H}^{n×n}** using arbitrary diagonal controls and determinant readings is exactly n−1. The lower bound holds even for unlimited adaptive reads; the upper bound holds for one noiseless modular scalar with a sufficiently large prime and a fixed nonadaptive star setting.

For the one-scalar assertion, let N=H^{n²}, J=binom(N,2), and M=n!(H+2)^n. The polynomial F_C for a star has coefficient ℓ¹ norm at most M. For every distinct C,C', Q=F_C−F_C' is a nonzero integer polynomial by BM2, with total degree at most n−1 because the common highest term product_i d_i cancels. For any prime

```text
p > max(2M, (n−1) J),
```

Q remains nonzero over F_p. If all 2n−1 controls are independent uniform F_p variables, Schwartz–Zippel bounds a pairwise collision by (n−1)/p. Union bounding over J pairs gives collision probability <1, hence a fixed successful setting exists. One observed noiseless residue determines C by a finite candidate table. This argument includes n=2; for n≥3 R284BJ already supplies a stronger bounded-noise construction. This is an existence result; candidate-table decoding may be exponential.

The connected-support condition is necessary for *any* allowed directed Port graph. The matching sufficiency here is demonstrated by a directed star; BM1/BM2 do not assert that every orientation of every connected graph is sufficient.

## Exact reproducible checking

The accompanying Python standard-library checker expands determinant polynomials with integer coefficients via Leibniz permutations. For **every** directed E with |E|<n−1 for n=2,3,4 it constructs the above binary pair and compares the complete polynomial coefficient dictionaries (1,7,79 graph families respectively). For full directed stars, it enumerates all C∈{1,2}^{n×n} and verifies pairwise distinct polynomial signatures for n=2 (16 matrices) and n=3 (512 matrices). These are exhaustive finite tests in the declared domains; BM1–BM3 are established by the algebraic proofs, not extrapolation from those tests.

Files: `R284BM_connected_port_graph_checker.py` and `R284BM_connected_port_graph_verification.json`. Source math is author-checked; independent review remains NOT_REVIEWED.

## Next scientific question

Characterize which connected **non-star** editable-Port graphs have a fully injective formal determinant observer, and whether a spanning tree of arbitrary edge orientations is always sufficient under strict positivity. If counterexamples exist, classify their residual gauges beyond diagonal similarity. Independently, seek 3×3 binary prime-modulus witnesses below R284BL-FX1's p=100003 without weakening the ±3 error guarantee.
