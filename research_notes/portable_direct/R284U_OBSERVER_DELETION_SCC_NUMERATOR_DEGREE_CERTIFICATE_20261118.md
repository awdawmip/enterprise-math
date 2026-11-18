# R284U — Observer-deletion SCC certificate for numerator degree and 2-point Port grids

2026-11-18. Status: **AUTHOR_PROVED / EXACT_FRACTION_AND_EXHAUSTIVE_3PORT_CHECK_PASSED / NOT_REVIEWED**.

Scientific pin held fixed: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Immediate predecessor: R284T `research_notes/portable_direct/R284T_JOINT_BORDERED_DETERMINANT_QUADRATIC_CERTIFICATE_20261118.md` at commit `88183c11a6ad8e3c27e26e6a46fe54037e73e4c0`. Other dependencies: R281 (observer relevance), R284R (finite 1/2/3 sampling grids), R284S (rank-one quadratic obstruction), R284T (cross-difference determinant and its necessary observer-reduction step). This concerns **auxiliary, named, nonnegative-rational BRC Port matrices**, with additive named rank-one edits and *matched diagonal observers*. It does not assert a native X6 transfer.

## 1. Graph-only exact certificate for a single model

Let `V` be a finite set of named Ports; let `W(x)=W_0+sum_i x_i E_i`, where `W_0` has nonnegative rational entries and every `E_i=e_{u_i}e_{v_i}^T` is a separately named directed edge `u_i -> v_i`. Different edit names may share endpoints. Assume a nonempty parameter box containing **strictly positive values of all active edit variables** on which `rho(W(x))<1`; the baseline is also stable. In particular, strictly substochastic rows suffice in the examples. Fix a Port `p` and its diagonal readout

`F_p(x)=(I-W(x))^{-1}_{p p}=N_p(x)/D(x)`, where `N_p(x)=det(I-W(x))_{V\{p},V\{p}}` and `D(x)=det(I-W(x))`.

Construct the **potential-support digraph** `G` from the positive baseline edges and all available named edits, even when their currently sampled weights are zero. Delete the observer vertex `p` and all its incident edges, yielding `G-p`. For edit `i` define the boolean

`cycle_away_p(i) := [u_i,v_i != p AND a directed path v_i -> u_i exists in G-p]`.

A zero-length path is allowed, so a self-loop away from `p` is correctly classified as cyclic. Equivalently, the edited edge participates in a directed cycle of `G-p`; this is tested by one strongly-connected-component (SCC) decomposition of `G-p`. A path witnessing this condition can be chosen without the edited edge itself.

**Theorem R284U-A (exact structural numerator criterion).** Under the stated nonnegative, positive-interior, stable-domain assumptions, for every edit `i`:

`[x_i] N_p(x_i,z) == 0 as a polynomial in all other edits z` **if and only if** `cycle_away_p(i)` is false.

Here `[x_i]` is the coefficient in the affine polynomial `N_p`, and the equivalence is for the given fixed rational baseline weights with all nonzero baseline supports represented in `G`; symbolic independence of the baseline parameters is **not required**.

**Proof.** If either endpoint of the edit is `p`, it is absent in the principal minor `N_p`, which is therefore independent of `x_i`. Otherwise put `S=V\{p}`, `A(z)=I-W_S(0,z)`. The determinant lemma gives

`N_p(x_i,z) = det A(z) * (1 - x_i*(A(z)^{-1})_{v_i u_i})`.

The identity first holds wherever `A(z)` is invertible; stable nonnegative parameter values supply such an open set, and then extend it as a polynomial identity. Consequently

`[x_i]N_p = -det A(z) * (A(z)^{-1})_{v_i u_i}`.            (1)

For any admissible nonnegative `z`, `A(z)` is a nonsingular M-matrix. Its inverse is the convergent nonnegative walk sum `sum_{k>=0} W_S(0,z)^k`, and `det A(z)>0`. Thus the inverse entry is strictly positive **exactly when** there is a positive-weight directed walk from `v_i` to `u_i` in `S`. If no support path exists, the inverse entry vanishes for all allowed `z`; (1) vanishes as a polynomial. Conversely if a path exists in `G-p`, take a simple such path (which cannot use `i` before its first arrival at `u_i`). Assign small positive admissible weights to all other edits; every edge of that path then has positive weight, so (1) is strictly negative at this point. Hence the polynomial coefficient is nonzero. The same proof covers self-loops by the empty walk. QED.

**Computational consequence.** A single SCC decomposition on `G-p` identifies the numerator-independent edits in `O(|V|+|E_0|+e)` graph time, with only the declared support graph, no rational determinants, interpolation nodes, or symbolic multivariate expansion. For several diagonal observer Ports, repeat the SCC test once per observer (and per model); it is a supported *graph-operation bound*, not a claim about downstream exact-arithmetic bit cost.

## 2. Paired Port models: an automatic two-node certificate

As in R284T, **first perform exact R281 observer reduction separately in each model** for every output, removing edits that are irrelevant to that output in that model. Unreduced denominators may retain observer-invisible factors, invalidating degree reductions. Take the matched diagonal observers `p_1,p_2` of a declared output. Write reduced determinants/numerators as `D_h(x),N_h(x)` for `h=1,2` and `P=N_1D_2-N_2D_1`.

**Theorem R284U-B (SCC-certified degree drop).** If an edit `i` satisfies `cycle_away_{p_h}(i)=false` in **each model where it remains present**, then `deg_{x_i} P <= 1` as a global polynomial identity in every other named edit. Indeed `N_h=n_h(z)` does not depend on `x_i`, while `D_h=d_h(z)+x_i d'_h(z)` is affine by rank-one determinant multilinearity; hence

`P(x_i,z) = n_1d_2-n_2d_1 + x_i*(n_1d'_2-n_2d'_1)`.  (2)

If an edit is removed from one model by R281, the surviving model's cross-polynomial contribution has the corresponding R284R one-sided degree bound; do not reintroduce removed edits when building `P`.

Let `L` be the shared-output coordinates already certified linear by R284R and let `B` be coordinates otherwise requiring up to degree 2. For a set `C subset B` passing Theorem B for **every declared diagonal output**, the usual equality grid has only

`2^(|L|+|C|) * 3^(|B|-|C|)`                                  (3)

rational jointly stable nodes, plus irrelevant fixed zeros. Since `P` has these coordinate-degree bounds, equality at every such Cartesian node forces `P == 0` by multivariate interpolation, proving equality of the declared rational response functions wherever both denominators are nonzero. If `C=B`, all previously quadratic coordinates use 2 nodes. A reusable graph cut replaces R284T's repeated quadratic substituted-column determinant tests for these coordinates.

**Precision note.** If the existing R284R binary-adic interpolation assumptions apply, choosing the two retained nodes `0,1/Q` with `Q` odd gives a unit Vandermonde difference and hence zero *additional interpolation loss* for these coordinates. Existing denominator-valuation, stability and source-observation requirements remain exactly those of R284R.

## 3. Sharp examples and limits

**A. Nonconstant comparison, two nodes genuinely needed.** Use three Ports `0,1,2`, diagonal output `p=0`, and identical named edits `x:1->2`, `y:0->0` in both models. Model 1 has baseline weights `0->0=1/5`, `0->1=1/4`, `2->0=1/3`; model 2 has `0->0=1/5`, `0->1=1/5`, `2->0=1/4`. For `0<=x,y<=1/8` both graphs are strictly substochastic. All cycles containing either edit pass through observer 0. After deleting 0, edit `x` is acyclic and `y` disappears. Exact evaluation gives

`N_1=N_2=1`, `D_1=4/5-y-x/12`, `D_2=4/5-y-x/20`,

`P(x,y)=N_1D_2-N_2D_1 = x/30`.                         (4)

The graph-only grid falls from the two-cycle-bound `3*3=9` nodes to `2*2=4`, without evaluating any quadratic minor. The extra exact identity `P` independent of `y` would permit a further pair-specific reduction to two nodes (one `y` node and two `x` nodes). The two models **agree** at `x=0` for every `y`, while at `x=1/8` their cross numerator is `1/240`; thus one sample in `x` cannot universally replace two in this family.

**B. A surviving internal cycle can carry real quadratic obstruction.** Retain the R284S three-Port example, edit `x:1->2`, `p=0`. In model 1, `0->1=1/4`, `2->0=1/4`, `2->1=0`; in model 2, `0->1=1/4`, `2->0=15/64`, `2->1=1/4`. Deleting 0 leaves a cycle through `x` in model 2, and direct determinants yield

`P(x)=x/256-x^2/64` with `[x^2]P=-1/64`.          (5)

**C. SCC is a sufficient paired criterion, not necessary for pairwise cancellation.** Take the same edit/output and baselines `(a,b,gamma)=(1/4,1/4,1/8)` in model 1, `(1/4,1/2,1/4)` in model 2, where edges are `0->1=a`, `2->0=b`, `2->1=gamma`. Both induced graphs after deleting 0 contain a cycle through `x`; each numerator has nonzero slope in `x`, yet direct expansion yields

`N_1=1-x/8`, `D_1=1-3x/16`; `N_2=1-x/4`, `D_2=1-3x/8`,

`P(x)=-x/16` with `[x^2]P=0`.                         (6)

This exhibits cancellation across the two models not caught by the graph-only condition; R284S/R284T retain their role as exact coefficient tests.

## 4. Verification scope and next unit

Executed exact independent checker: `research_notes/portable_direct/R284U_observer_cut_scc_certificate.py`; machine-readable execution evidence: `research_notes/portable_direct/R284U_observer_cut_scc_verification.json`. Python standard-library `Fraction` and standalone fraction-preserving elimination compute actual 3x3 determinants and observer cofactors. The checks passed:

* 9 exact Cartesian nodes for Example A, confirming both determinant formulas, stable denominators and equation (4);
* 5 exact nodes each for B and C, confirming equations (5),(6) and their cycle classifications;
* **all 2,304** directed three-Port structural configurations: 9 oriented possible named edit endpoints times all `2^8` subsets of the remaining baseline edges at weight `1/16`. Comparing exact `N_p(x_i=0)` and `N_p(x_i=1/8)` agrees in every case with the deleted-observer graph reachability test. All cases are strictly substochastic at the tested weights.

The finite checks verify those cases; Theorem A follows from the determinant lemma and nonnegative walk expansion; Theorem B follows from determinant multilinearity and interpolation. No third-party independent review or native execution claim is asserted.

**Next useful question.** Extend the graph-only degree test from diagonal `F_pp` to arbitrary matched off-diagonal Port observables `F_ab`. A candidate starting point is the path-and-cycle expansion of the cofactor `adj(I-W)_{ab}`; classify edit usage on simple `a->b` paths or directed cycles disjoint from such paths, distinguish structural-zero certificates from possible cross-model cancellations, and derive sound computational costs. A second direction is full bit-complexity benchmarking of SCC preprocessing and the exact equality grid on families with many edits and many observers.
