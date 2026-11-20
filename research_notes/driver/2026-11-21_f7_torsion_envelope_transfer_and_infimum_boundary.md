# F7 scoped mathematical synthesis — exact torsion-fiber envelope transfer

Date: 2026-11-21 (+08:00). Contribution: original RESEARCH_DRIVER logical line `EM-DVR-DEBB5E`; status: author-side analytic reduction, **not** an independently admitted Native Review or Result. Existing F7 theorem-repair authorship remains `EM-CBRCF7-83A1D4`.

## Question and provenance

The frozen F7 theorem repair reduces the carrier `Z^2 ⊕ Z/3` to a free `Z^2` scalar by minimizing over the three torsion labels. Determine whether the reduction really depends on torsion order three, and identify the precise condition required for a possibly infinite torsion fiber.

- Original theorem repair: `research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md`, particularly §§2, 5–8 (original Git blob `69265a0fadfd9fcd0be9354ff74f33e5e825fe84`).
- Existing Driver review evidence: `driver_reviews/mcp/MCP-9b4714dc46b948afa4875a86c89c713c/8eb536d638aaf7b65a26/F7_RR_AA389_INDEPENDENT_SCOPED_AUDIT_20261121.md`, source commit `1ae5aa1721b13c1050b4f5d24880f1e6e44de5cf`.
- Exact frozen Result: `RR-AA38973D56330E59D315`, result SHA-256 `2a89647a31de47e4ddef17ae61a843ea9a271fe602f8ab60adcca81699022c9b`.

The result below is a *new general transfer lemma*. Its F7 no-go corollary uses the earlier free-obstruction proposition at precisely its stated assumptions, without silently granting formal acceptance of that Result.

## Theorem 1 — torsion-fiber infimum commutes with exact separable conservation

Let `L=Z^d`, let `K` be **any torsion abelian group** (finite or infinite), and put `C=L⊕K`. Fix an integer number of slots `s≥1`. Let `q:C→[0,∞)` be finite-valued, and let `Φ∈Aut(C^s)` obey the exact conserved sum

```
Σ_{i=1}^s q((Φz)_i) = Σ_{i=1}^s q(z_i)      for every z ∈ C^s.
```

Since the torsion subgroup of `C^s` is exactly `K^s`, `Φ` induces an integer unimodular linear automorphism `A∈GL_{ds}(Z)` on the free quotient `L^s`.

Define `f:L→[0,∞)` by `f(x)=inf_{k∈K} q(x,k)`. Then for **every** `x=(x_1,…,x_s)∈L^s`,

```
Σ_i f((Ax)_i) = Σ_i f(x_i).                    (T)
```

If `K` is finite, the infima are attained minima. If an involution `J_C:C→C` maps each fiber over `x` bijectively to the fiber over `J_L x` and `q∘J_C=q`, then `f(J_Lx)=f(x)`; in particular `J_L(n,m)=(-n,m)` yields exact old-coordinate evenness.

**Proof.** Torsion elements are characterized by finite order, so every group automorphism preserves `K^s` and induces a free quotient automorphism `A`. For each fixed `x∈L^s`, the map `k↦Φ(x,k)` bijects the entire input torsion fiber `{x}×K^s` with the output fiber `{Ax}×K^s`: the restriction of `Φ` to `K^s` is an automorphism, and the map on a fiber is its translate. Taking the infimum over the input fiber of the stipulated pointwise conservation identity therefore gives
```
inf_{k∈K^s} Σ_i q((Φ(x,k))_i)
 = inf_{k∈K^s} Σ_i q(x_i,k_i).
```
The left side equals `Σ_i f((Ax)_i)` and the right side equals `Σ_i f(x_i)`: a finite sum of independently minimized, bounded-below functions has infimum equal to the sum of its individual infima (approximate each individual infimum within `ε/s`). This proves (T). The assertion about `J_C` follows by the same fiber bijection and invariance of `q`. QED.

## Corollary 2 — finite-torsion F7 obstruction is torsion-order independent

Specialize to `d=s=2`, `q(0)=0`, `J_L(n,m)=(-n,m)` and the inherited involution above. Suppose

```
q((n,m),k)>0   for every n≠0, m∈Z, k∈K.
```

If `K` is **finite**, then `f(0,0)=0`, `f(-n,m)=f(n,m)`, and `f(n,m)>0` for every `n≠0`. Theorem 1 gives exactly the free two-slot preservation identity used by the corrected F7 A0/J-aware theorem. Consequently, **assuming that previously proved free obstruction**, there is no such exact `Φ` whose induced free matrix `A=[P Q; R S]∈GL_4(Z)` satisfies A0: the first old input `e=(1,0)` has nonzero old coordinates in *both* `Pe` and `Re`.

This applies to any finite abelian torsion summand `K`, regardless of its exponent, cardinality, or coupling to free inputs under `Φ`. The proof neither introduces a new F7 physical assumption nor reopens the original clean-blind execution.

For **infinite torsion** `K`, the same conclusion follows under the explicit additional hypothesis `inf_{k∈K} q((n,m),k)>0` for every `n≠0,m∈Z` (uniform positivity across each torsion fiber).

## Sharp boundary of the reduction (not an existence counterexample)

Pointwise positivity alone is insufficient to transfer the required strict old-coordinate positivity through an *infinite* torsion infimum. For example take the countably infinite torsion group `K=Q/Z`, enumerate it as `{k_j:j≥1}`, and set

```
q((n,m),k_j) = 0                if n=0,
              = 1/j              if n≠0.
```

Every `q((n,m),k_j)` with `n≠0` is strictly positive; the scalar is nonnegative, has `q(0)=0`, and is even under `n↦-n`. But `f(n,m)=inf_j q((n,m),k_j)=0` for **all** `n,m`. Thus the free F7 obstruction cannot be invoked from these weaker assumptions alone. This example diagnoses a lost hypothesis in the reduction; it does **not** construct an A0-preserving automorphism.

## Research consequence and completion boundary

The torsion-three order in the frozen F7 envelope is not an algebraically essential ingredient of the finite-fiber conservation reduction. Any F7-analog with finite torsion and the stated inherited positivity/evenness reduces to the same free A0 obstruction. For infinite torsion the fiberwise uniform-positivity test is the exact additional requirement for this proof route.

This note is an exact proof of a transfer mechanism and a scoped conditional corollary, not an independent reproduction of the original full block-rank proof. Keep existing owner/author attribution, blind provenance, and the separate original frozen Result SHA-256 manifest divergence. Native first-review write remains blocked at original terminal request `dvr-20261121-0214-f7-first-review-source-integrity-request-revision-v1` (`NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED`), tracked in Issue #2874. No new Review, Result admission, task completion, F8 dispatch, or Foundation promotion follows from this mathematical note.

Status: **one author-side exact mathematical transfer lemma**, one conditional F7 corollary, zero new Native Review/Result/Task completion.
