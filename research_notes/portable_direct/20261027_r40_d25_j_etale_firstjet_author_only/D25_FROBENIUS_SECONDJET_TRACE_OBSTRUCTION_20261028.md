# D25/LIFT — Exact trace-annihilator certificate for second-jet Frobenius odd squares

**Date:** 2026-10-28. **Status:** `AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`. **Contributor context:** shared author materials in Draft PR #1566, no clean-blind or independent-review claim. **Mother objective:** `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific Source:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

## Input provenance and exact scientific question

The prior author-derived auxiliary result establishes for an odd prime p and a free rank-r marked module over `(Z/p^3)[T]/(T^2-2)`, with `sigma(T)=-T`, that

`F = (I+p(A+TB)+p^2(C+TD)) sigma` has normalized odd-square second jet `K=p^-2[T]F^2 (mod p) = [B,A] := BA-AB`.

This note **reuses**, not recredits, that identity. The smallest new question is an exact inverse feasibility test: given fixed marked `A` and a proposed `K`, what independent linear equations certify whether `K` can come from *any* `B`? If so, what source information does `K` fail to distinguish?

All matrices below are over the field `k=F_p`; the scalar auxiliary quadratic coordinate `T` is **not** the six native Enterprise axes. The population is the ordered source-marked matrix entries, observer `K`, allowed operations ordinary matrix algebra and any separately declared gauge group, precision `p^3`. The signed branch order is retained until an explicitly proved observer quotient.

## Theorem 1 — exact image, annihilator and fiber

Let `A in M_r(k)`, `Z(A)={C:CA=AC}`, `d=dim_k Z(A)` and `ad_A(B)=BA-AB`. Then for every `K in M_r(k)`:

```
   exists B with [B,A]=K
   iff tr(CK)=0 for EVERY C in Z(A).
```

When feasible, the full solution set is a nonempty affine coset `B0 + Z(A)` and has **exactly `p^d` members**. The set of feasible odd-square ports has dimension `r^2-d` and cardinality `p^(r^2-d)`.

**Proof.** The bilinear trace pairing `<C,K>=tr(CK)` is nondegenerate on `M_r(k)`, for any characteristic, since for nonzero `K_{ij}` choose `C=E_{ji}`. The adjoint of `ad_A` with respect to this pairing is `C -> AC-CA`: indeed, cyclicity gives `tr(C(BA-AB))=tr((AC-CA)B)`. Hence `Im(ad_A)` is contained in `Z(A)^perp`. Rank-nullity gives `dim Im(ad_A)=r^2-d`; nondegeneracy gives `dim Z(A)^perp=r^2-d`, proving equality. Finally, fibers of a linear map are cosets of its kernel `Z(A)`, containing exactly `p^d` elements. □

This theorem is an **existence checker**, not a unique recovery map. Vanishing of all trace tests does not identify the marked `B` or `K`, and all actual source gauge restrictions must be supplied separately; replacing original signed ports by scalar traces would destroy information needed for future marked observations.

## Theorem 2 — a complete two-scalar test in rank two

If `r=2` and `A` is nonscalar, `Z(A)=span_k{I,A}` (dimension two). Consequently, for *any* nonscalar 2-by-2 `A` (split semisimple, Jordan, or nonsplit irreducible),

```
   exists B with BA-AB=K
   iff tr K=0 AND tr(AK)=0.
```

If feasible, the fiber size is **exactly `p^2`**. If `A` is scalar, the sole feasible port is `K=0`, and the fiber size is `p^4`.

**Proof.** Nonscalarity supplies a vector `v` for which `(v,Av)` is a basis; otherwise each line would be `A`-invariant and `A` would be scalar. A matrix commuting with `A` is determined by its value on `v`, since `C(Av)=A(Cv)`, so its centralizer has dimension at most two. `I` and `A` are independent commuting matrices, establishing the equality. Apply Theorem 1. In the scalar case every commutator is zero. □

In a split diagonal case `A=diag(lambda_1,lambda_2)` with distinct eigenvalues, feasible `K` has zero diagonal and the inverse off-diagonal entries satisfy `B_ij=K_ij/(lambda_j-lambda_i)`. Arbitrary diagonal `B` produces the `p^2`-element fiber. For Jordan `A=lambda I+E12`, feasibility reduces to `K11+K22=0`, `K21=0`; the result also covers the nonsplit case without introducing square roots or denominators.

## Exact p=373 observer certificate

Let `p=373`, `A=diag(0,1)` and `B=E12`. Then `K=[B,A]=E12`. It satisfies `tr K=0`, `tr(AK)=0` and has exactly `373^2=139129` source-marked preimages `B`. The alternative `K=0` satisfies the same **two scalar existence tests** but is a distinct odd-square port. Thus the two trace conditions are not an observationally lossless replacement for `K` itself.

Two falsification witnesses under the asserted auxiliary model are `K=I` (`tr K=2`) and `K=diag(1,-1)` (`tr K=0` but `tr(AK)=-1`), which cannot be the second-odd jet for this `A`. In each case an inferred original-class transfer failure would refute the **proposed transfer/normalization**, not the source-native H0/B0 mathematics.

## BRC / Enterprise-coordinate use and transfer limit

The BRC carrier is the finite source-indexed set of `B` matrices with exact observer `K`, fibers labeled by `Z(A)` elements, and preservation of integer/residue representatives, signed order and basis. Reusing the prior `K=[B,A]` map (`COMPOSE_APPLIED`) supplies an exact fiber count and necessary-and-sufficient feasibility gate. The coarser `(tr K, tr(AK))` records feasibility at rank two but does **not** recover the marked `K` or its future gauge transformations; retain `K` or an explicitly justified quotient under the real permitted gauge `H`. There is no asserted identification with a native six-dimensional Cell or original H0/B0 module.

A legitimate native application first reads the genuine fixed-class coefficient ring, matrix rank, `A` and exact original `[T]F²/p²` after basis normalization, sign conventions and permitted gauge. The rank-two test applies only if the native operator really admits the specified congruence shape. An original `K` violating the trace-annihilator certificate is a precise **interface obstruction**. Any conclusion about `Delta_p-R_p` needs a separate source-preserving mapping and same-class native data.

## Exact author-side check and open obligations

The executable standard-library file `d25_commutator_image_trace_duality_checker_20261028.py` performed full-domain image/trace-equivalence checking for **all 81 matrices `A` in `M_2(F_3)`**, six representative `M_2(F_5)` matrices and three `M_3(F_3)` matrices, with complete enumeration of all `B` and `K` in each case; additional finite-field Gaussian-elimination feasibility checks covered `p=13,19,373` at ranks 2 and 3. The generated JSON reports `PASS`, 96 case families, and the p373 witnesses. Finite verification corroborates the proof; it is author-side only and **not** a native H0/B0 run or independent review.

Remaining real dependencies: original-class same-source operator and normalization via existing support Issue #1559; independent mathematical assessment; legal Source CLAIM/OPEN/checkpoint and writer/provenance. The completed UR V2 mathematics is unaffected: its original four-file 94,687-byte bundle still requires a byte-exact `SHA-256=4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` source before provenance backfill. Do not reconstruct it as a new proof. For a Source continuation seed of state `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`, keep `completed_units=[]`.
