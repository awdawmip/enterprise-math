# R758P5B — Fully S6-covariant auxiliary-frame extension with 2,520 flat-area BRC holonomies

Date: 2026-11-13 (Asia/Shanghai). Author-side, exact candidate theorem. Frozen scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Immediate predecessor R758P5 in this branch; established R758P3/R758P4 in PR #2204/#2208. P000 six native spatial axes + one distinct time dimension are unchanged. The symbol `*` below denotes an *internal frame mark*, **not** a seventh spatial axis or the time coordinate.

## The S3 rank obstruction (precise scope)

Assume a label-only frame assignment to the six native axes has a fixed `S3` frame group, labels `T_i\in S3`, and a homogeneous, global axis-rotation action `rho:S6 -> Aut(S3)` by group homomorphisms satisfying `T_{sigma(i)}=rho(sigma)(T_i)` for every `sigma\in S6`. Then all six labels are identical. Indeed `Aut(S3)≅S3`. The restriction of `rho` to the simple, nonabelian group `A6` is trivial: an injection from `A6` into an order-six group is impossible, and its only normal kernels are `{e}` or `A6`. Since `A6` acts transitively on six axes, `T_i=T_j` for all i,j. If the common label is an involution (as in the R758P3 candidate), every closed signed-axis word has even length, and so its total frame transport is the identity.

This is an exact obstruction to an *S6-equivariant homogeneous six-axis extension of that fixed S3-label mechanism*; it does not exclude more general frame bundles, spatially dependent gauges or richer native mechanisms.

## The constructive S7 auxiliary-frame lift

Let `F={*,1,2,3,4,5,6}` be seven *frame labels*. Work in auxiliary permutation group `S(F)≅S7`. For native axis `i∈{1,...,6}`, attach `T_i=(* i)`, a transposition. For both signs of a primitive step along native axis i, apply the same involution T_i, and multiply later steps on the left: `H(w)=T_{i_n}...T_{i_1}`.

**Theorem 1 (strict S6 covariance).** Every native axis relabeling `sigma∈S6` extends to the internal frame relabeling `\tilde{sigma}` fixing `*`. Then
`T_{sigma(i)}=\tilde{sigma}T_i\tilde{sigma}^{-1}` and `H(sigma w)=\tilde{sigma}H(w)\tilde{sigma}^{-1}`. Signed native coordinate adjacency, six-axis component norm and the full six-dimensional Cell torsor retain their P000 types. This is an exact *representation-level* covariance theorem; it makes no assertion of native TRIADIC_CLOSURE_E admission.

**Theorem 2 (every A7 frame appears with zero projected area).** Let `A(w)` be the 15-component signed projected area from the chosen six-axis Cell chart, and consider arbitrary rooted *closed* native signed-unit path words. Every such word has even length, hence `H(w)` is an even permutation of F: `H(w)∈A7`.

For each distinct pair i,j define the eight-step rooted closed word
`W_ij=(+i,+j,-i,-j,+i,-j,-i,+j)`.
It has zero signed displacement and *all fifteen* signed projected areas zero, but
`H(W_ij)=(T_j T_i)^4=T_jT_i`, a nonidentity 3-cycle on `{*,i,j}`. (Products here use standard right-to-left composition.) The first four-edge square has signed area +1 in the ij projection; the second has -1, so they cancel while their rooted frame transports multiply nontrivially.

The 15 star-supported 3-cycles `T_jT_i` generate `A7`: for any distinct i,j,k, the product `(* i j)(* j k)=(i j k)` with consistent orientation, and all 3-cycles (including the star-supported ones) generate A7. Because closed paths at the same Cell concatenate with additive area and multiplicative holonomy, every group element of A7 is obtained by a zero-area rooted closed signed-unit path. Therefore

`{H(w) : w is closed, A(w)=0}=A7`  (**exact equality, 2,520 frames**).

All these examples have *one identical* native endpoint and signed projected area observation `(0,...,0)`; the true full path, source and distinct frame remain typed. Therefore any exact quotient that recovers the full final frame across this flat-area fiber needs at least **2,520 states**, equivalently **12 bits in a fixed-length binary encoding**. This lower bound is for that declared observer and future frame readout, not for every possible native dynamical observer.

## Exact finite verification

The portable verifier `R758P5B_VERIFY_S6_S7.py` uses seven-element permutation tuples and integer signed-unit words. It verifies all 15 W_ij have zero signed displacement/15 projected areas, their rooted holonomy equals T_jT_i, that 15 generators close to a group of order 2,520 by exact BFS, the parity of each element is even, and full 720 x 6 = 4,320 axis-label covariance identities. Recorded exact counts in `R758P5B_EXACT_OUTPUT.json`. No floating arithmetic. The finite group-closure verification independently supports the algebraic group-generation proof.

## Remaining native research obligation

Determine the actual admitted `TRIADIC_CLOSURE_E` Cell/Link/Port three-force incidence and event update, and whether an auxiliary-frame S7 representation descends to the appropriate V29/V39 connection while preserving full signed provenance and P000 rotation semantics. The star is a *frame degree of freedom*; it is neither spatial axis number seven nor a primitive force. No claim, Result, Driver review, or Foundation promotion is asserted solely from this author-side mathematical construction.
