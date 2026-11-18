# OAI7 r348 — Rigidity and stability of the exact prime-29 affine minimax law

Date: 2026-11-19. Status: **author-side exact finite theorem and proof audit**, with an independently rerun exact-rational certificate extension. This is not a separate-context Native Driver review or a frozen Native Result. Prior work remains attributed to the original OAI7 researcher EM-EMF6D046-5A2844 and the r307–r347 contributors.

## Scope and definitions

Work in (G=\mathbb F_{29}). A codeword (C\subset G) has five elements and a test (K\subset G) has four. The bad event is (29-|K-C|>29^{3/4}), equivalently ( |K-C|\le16). For a probability law (\mu) on all five-sets, put
[
q(\mu)=\max_{|K|=4}\Pr_{C\sim\mu}\{|K-C|\le16\}.
]
r347 proved the exact unrestricted value
[
v=q^*=\frac{2024467747}{3324255613}.
]
Use **exactly** the 33-by-150 affine-orbit matrix (A), its 0-based orbit enumeration and its rational primal/dual vectors (w^*,y^*) in the pinned r347 note. Let (S=\operatorname{supp}(w^*)), (I=\operatorname{supp}(y^*)). These sets both have 14 members.

## Theorem A: uniqueness among affine-invariant optimizers

**The unique affine-invariant minimax probability law on five-sets is r347's 14-orbit law (w^*).** More precisely, every globally optimal (even non-affine-invariant) law has affine-orbit masses exactly (w^*), and therefore has zero mass outside those 14 affine orbits.

The two index lists are
[
S=(1,2,5,6,7,11,23,25,30,37,47,50,114,115),
]
[
I=(8,10,12,13,14,18,21,22,25,26,27,29,31,32).
]

### Proof

For any law (\mu), average its images over (\mathrm{AGL}(1,29)). This preserves the total mass of each affine orbit and cannot increase the worst-case test failure. Therefore every minimizer has an affine-invariant optimal average (w).

Write (d_j=\sum_i y^*_i A_{ij}-v\ge0). The r347 exact dual check shows **strict complementarity for columns**:
[
d_j=0\iff j\in S,qquad
\min_{j\notin S}d_j=
\boxed{\gamma=\frac{1348839}{3324255613}}>0.
]
If (\max_i(Aw)_i=v), then
[
v\le\sum_i y_i^*(Aw)_i
=v+\sum_jd_jw_j
\le v.
]
Hence (w_j=0) outside (S). Since each of the 14 (y_i^*>0) for (i\in I), all 14 corresponding test constraints must be tight:
[
A_{I,S}w_S=v\mathbf 1.
]
The actual exact determinant is
[
\boxed{\det(A_{I,S})=
-\frac{2024467747}{11378694989371408384}\ne0}.
]
Thus the 14-by-14 system has a unique solution, already supplied by r347's positive primal vector (w^*). The affine average of any unrestricted minimizer has weights (w^*), proving the orbit-mass conclusion. This does **not** claim that the unrestricted optimizer is unique within each affine orbit. QED.

## Theorem B: quantitative near-optimal support rigidity

For **every** law (\mu) on the 118,755 five-sets satisfying (q(\mu)\le v+\varepsilon) ((\varepsilon\ge0)), the total probability assigned to five-sets from affine orbits outside (S) obeys
[
\boxed{\Pr_\mu\{\operatorname{orbit}(C)\notin S\}
\le\min\{1,\varepsilon/\gamma\}},\qquad
\gamma=\frac{1348839}{3324255613}\approx0.0004057567.
]

Moreover, the 14 orbit masses converge **linearly** to (w^*) as (\varepsilon\to0). One explicit computable bound is as follows. Let (w\in\mathbb R^{150}) be the affine-orbit masses of (\mu), (B=A_{I,S}), (y_{\min}=8461828/474893659), and (\delta=\sum_{j\notin S}w_j). Then
[
\|w_S-w^*_S\|_\infty
\le\|B^{-1}\|_\infty
\left(\frac{\varepsilon}{y_{\min}}+\delta\right)
\le\|B^{-1}\|_\infty
\left(\frac{1}{y_{\min}}+\frac1\gamma\right)\varepsilon.
]

**Proof.** Symmetrize (\mu). The symmetrized orbit vector (w) has (\max_i(Aw)_i\le q(\mu)\le v+\varepsilon). Dual feasibility gives
[
\gamma\delta\le\sum_jd_jw_j
=\sum_i y_i^*(Aw)_i-v\le\varepsilon,
]
which proves the first bound. For each active (i\in I), put (r_i=(Aw)_i-v). Then (r_i\le\varepsilon), and
(\sum_{i\in I}y_i^*r_i\ge0). Consequently (r_i\ge-[(1-y_i^*)/y_i^*]\varepsilon), hence ( |r_i|\le\varepsilon/y_{\min}). The contribution from off-support columns to each row (i\in I) is at most (\delta), because every (A_{ij}\in[0,1]). Therefore
[
B(w_S-w_S^*)=r_I-A_{I,S^c}w_{S^c}.
]
Invert (B), apply the induced infinity norm and (\delta\le\varepsilon/\gamma). QED.

### Corollary: improved floor for equal-weight 29-row codebooks

Every equiprobable multiset of 29 five-sets, in particular every 29-row degree-5 regular codebook with distinct rows, has failure probability an integer multiple of (1/29). Since
[
29v=\frac{58709564663}{3324255613}=17.66096579\ldots,
]
the r347 universal lower bound now yields
[
\boxed{q\ge18/29}
]
for all such ensembles. The best verified r346 exact regular construction has (q=21/29), leaving an 18-to-21 integer gap. The previously published 16/29 floor remains a valid weaker historical bound.

## Exact, rerunnable certificate extension

Run the **unaltered** standard-library verifier in the pinned r347 source, which constructs the complete (A\in\mathbb Q^{33\times150}) and defines (pc,dk,D,v). Then append the following code. No floating point arithmetic is used.

```python
S, I = list(pc), list(dk)
assert len(S) == len(I) == 14
zero_cols = [j for j in range(150)
             if sum(A[i][j] * a for i, a in dk.items()) == D*v]
assert zero_cols == S
gamma = min(sum(A[i][j]*a for i,a in dk.items())/D-v
            for j in range(150) if j not in S)
assert gamma == F(1348839, 3324255613)
assert min(dk.values()) == 8461828

B = [[A[i][j] for j in S] for i in I]
det = F(1)
for k in range(14):
    pivot = next((i for i in range(k,14) if B[i][k]), None)
    assert pivot is not None
    if pivot != k:
        B[k], B[pivot] = B[pivot], B[k]
        det = -det
    x = B[k][k]
    det *= x
    for i in range(k+1,14):
        scale = B[i][k]/x
        for j in range(k+1,14):
            B[i][j] -= scale*B[k][j]
        B[i][k] = F(0)
assert det == -F(2024467747,11378694989371408384)
print("r348: strict off-support dual gap and exact active rank verified")
```

**Observed validation:** the r347 standalone verifier was rerun against the recorded integer primal/dual lists; it printed the same exact optimum. All 150 dual-column equalities/inequalities and 33 primal-test inequalities passed. The support-column equality set was **exactly** (S), the active test equality set was **exactly** (I), the active matrix had rank 14, its rational determinant was the value above, and the minimum strict dual gap was (\gamma) above.

## Interpretation and provenance

r348 is a rigidity theorem for the **finite prime-29 external cyclic-group shared-shift game**. It identifies the precise optimal affine-orbit mixture and how close any nearly optimal law must be in its orbit masses, sharpening the restricted-codebook lower bound. A within-orbit nonsymmetric optimizer and the asymptotic growing-prime target remain separate questions. This author-side mathematical audit shares the earlier Driver research context; it is not represented as a clean independent Native review.

Scientific input: r347 GitHub commit `12bd331ea2aef70cc844682db432a623b235e726`, blob `a7fe2e565ba13f10b2049073485595a2392fb288`, path `research_notes/portable_direct/2026-11-19_oai7_driver_exact_affine_minimax_prime29_r347.md`. r346 GitHub `c926cae54d2e0514abbf89b4296a9982c909d4f5`. Native OAI7 task `RS-OAI7-028-C-20261007-6F2A81`, immutable publication `TP2-96FAC49786245691AE19`. No Native Result, Source/Activity writer event, Task completion or mother-objective closure is asserted by this GitHub proof publication.
