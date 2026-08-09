# Causal Signature Product Law — Independent LEGO Systems, Signature Composition, and Additive Causal Dimension

Status: `CROSS-ROUTE RESEARCH WIP / EXACT INDEPENDENT-PRODUCT THEOREM + INTEGER SPECIALIZATION`

## 1. Goal

If the Causal Signature Core is to replace an a priori Cartesian high-dimensional ontology, independent subsystems must generate their joint state directly from their own signatures rather than requiring a fresh mathematical definition at each added dimension.

## 2. Independent causal systems

Let system `A` have state set `X`, operation language `Omega_A`, observations `O_A`, and signature `Sigma_A`. Define system `B` similarly.

Their independent composition `A ⊠ B` means:

1. operations act only within their own subsystem;
2. observations may read the two subsystems separately;
3. no cross-interaction observation is added.

## 3. CP-01 — Signature factorization

For a joint state `(x,y)`, every independent future experiment is just a pair of component experiments. Therefore

\[
\boxed{
\Sigma_{A\boxtimes B}(x,y)
=
(\Sigma_A(x),\Sigma_B(y)).
}
\]

The right side is the labeled product of the two experiment-result tables.

## 4. CP-02 — Future-equivalence factorization

It follows that

\[
\boxed{
(x,y)\equiv_{A\boxtimes B}(x',y')
\iff
x\equiv_Ax'\text{ and }y\equiv_By'.
}
\]

An independent product creates no additional hidden cross distinction.

## 5. CP-03 — Product quotient is a shadow

Hence

\[
\boxed{
(X\times Y)/\equiv_{A\boxtimes B}
\cong
(X/\equiv_A)\times(Y/\equiv_B).
}
\]

The ontology order is therefore

\[
\boxed{
\text{independent signature factorization}
\to
\text{future-equivalence factorization}
\to
\text{traditional product-quotient shadow}.
}
\]

## 6. CP-04 — Causal dimension is additive

In the integer-linear specialization, the two future-visible row modules live in disjoint LEGO slot blocks. Their joint visible module is therefore their direct block sum:

\[
\boxed{
\dim_{causal}(A\boxtimes B)
=
\dim_{causal}(A)+\dim_{causal}(B).
}
\]

Dimension addition now means adding independent future-distinguishable freedoms, not declaring more Cartesian coordinates in advance.

## 7. The unit `1` remains unchanged

Combining independent subsystems changes relation slots, operation language, and the number of independent future distinctions. It does not change the value of a unit block. Thus dimension growth is independent-distinguishability growth while `1` remains `1`.

## 8. Counting weight also multiplies

If component collapse fibers have sizes `m_A(a)` and `m_B(b)`, the independent product fiber is the Cartesian product of the two fine-history fibers, so

\[
\boxed{
m_{A\boxtimes B}(a,b)=m_A(a)m_B(b).}
\]

This is structural independence of fine-state composition. A conventional product-probability rule appears only after additional normalization/sampling semantics.

## 9. CP-06 — Interaction is failure of signature factorization

If a joint system introduces cross operations, cross observations, state-dependent coupling, or any response that cannot be reconstructed from the two component signatures, then

\[
\Sigma_{AB}\ne(\Sigma_A,\Sigma_B).
\]

This suggests a higher-level causal definition:

\[
\boxed{
\text{interaction}=
\text{failure of independent signature factorization}.
}
\]

The finite LEGO interaction spectrum should therefore be investigated as a local exact decomposition of this signature-factorization defect.

## 10. Traditional product/tensor tooling

Only the independent product has been causally derived here. Tensor products, Hilbert-space tensor products, Kronecker products as ontology, entanglement, and multilinear completions are not automatically admitted. Block/Kronecker matrices may be used as coordinate tools for already-declared independent operations.

## 11. Executable reference

- `src/enterprise_math/causal_product_system.py`
- `tests/test_causal_product_system.py`

The integer-linear tests cover block-independent operations, absence of cross-observation terms, and exact additivity of causal-visible rank.

## 12. Next

1. define a signature-coupling defect when product factorization fails;
2. connect that defect to the finite LEGO interaction spectrum;
3. reinterpret dimension contraction as a causal quotient of product signatures rather than coordinate deletion;
4. revisit A3 tagged contraction from this independent/coupled signature viewpoint;
5. introduce tensor-like traditional machinery only if a causal necessity is proved.
