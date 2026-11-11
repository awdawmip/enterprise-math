# R711.3 | Exact six-axis hypergraph-to-pairwise triangle closure test

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS · **Author:** EM-X6-912721 · **Activity:** RA-54F16A1A0CB4F90FE4E40A54. Companion to R711.1 / PR #2052. Frozen scientific inputs unchanged: `a72226e2430ffa4786321ac86e7f0c599d5f0389`.

## Definition

Let `V={0,1,2,3,4,5}` and let `H⊆binom(V,3)` be **any** 3-uniform triple license on six labeled native axes. Its **pairwise shadow** is `∂₂H={ {a,b}: there exists T∈H containing a,b }`, an undirected 15-bit graph. Define the triangle closure

`Cl(H) = {T∈binom(V,3): all three pairs from T belong to ∂₂H}`.

Define the **higher-order license residual** `R(H)=Cl(H)\H`, a set of presently unlicensed triples that a pairwise-only graph would automatically license.

## R711.3 Theorem: exact representability and canonical graph

For each such `H`, the following statements are equivalent:

1. There exists a pairwise graph `G` with `H=Triangles(G)`.
2. `Cl(H)=H`.
3. `R(H)=∅`.

Moreover `G_min=∂₂H` is the unique inclusion-minimal graph representing `H` whenever representation exists.

*Proof.* Clearly `H⊆Cl(H)`. If `H=Triangles(G)`, every pair occurring in `H` is in `E(G)`, hence `Cl(H)=Triangles(∂₂H)⊆Triangles(G)=H`. Conversely, if `Cl(H)=H`, choose `G=∂₂H`, proving representability. Any representing graph contains `∂₂H`, so this one is the unique minimum under edge inclusion. Also `Cl(Cl(H))=Cl(H)`: no new pair appears in `Cl(H)` beyond `∂₂H`, while all original pairs are retained. □

Thus one can recognize a non-pairwise native triadic license by supplying **one exact missing triangle** `T∈R(H)`, together with the three licensed pair witnesses. No search over candidate graphs is needed.

## R711.4 Complete six-axis state count

There are `2^20=1,048,576` possible **labeled** triple-eligibility patterns. Exact enumeration of all 20-bit masks using the shadow/closure operator gives precisely

`|{H: Cl(H)=H}| = 6,115`.

Hence `1,042,461` six-axis triple-license patterns need genuinely higher-order triple conditions if presented verbatim as a binary support map. Exactly `6115/1048576` of all support maps are pairwise-graph representable.

Independent exact check: enumerate all `2^15=32,768` pairwise graphs and collect their distinct `Triangles(G)` sets; this produces **6,115 distinct** maps, agreeing with the fixed-point count.

The R709 Pasch family `H={012,034,135,245}` has `|R(H)|=4`: its graph shadow forces precisely the four missing complementary triples `013,024,125,345` (as in R710). The full deficit distribution for `|R(H)|=0,...,14` is persisted in the evidence JSON.

**Precise BRC scope.** `R(H)` is a structural observer residual showing information discarded by the pairwise shadow. Its cardinality describes one-time closure defect, not BRC signed cancellation, probability, event energy or the minimum number of actual physical gates. If the native eligibility carries sign, Cell, source or time, apply the closure test separately to each genuinely common state/scope; the binary 20-bit projection must be defined before evaluating the residual.

## Verification and next operation

Executed local exact standard-library Python check:

```text
R711_PAIRWISE_TRIANGLE_SHADOW_CLOSURE_EXACT_PASS 1048576 6115 6115 6115 14
```

A production native X6 test now has two exact integer outputs from the same measured 20-bit license map: `pairwise_factorizable=(R(H)==∅)` and `missing_triples=R(H)`. Fetch the precise frozen X6 Cell/Link/Port + V29 PASS/TRANSFER + V39 j rules, determine one legal complete 20-bit map and perform this closure computation. It directly decides applicability of R711.1 and retains the minimal higher-order discrepancy if factorization fails.

Scientific status: exact finite graph/hypergraph support theorem and exhaustive count; still requires independently checked native admissibility and Driver review.
