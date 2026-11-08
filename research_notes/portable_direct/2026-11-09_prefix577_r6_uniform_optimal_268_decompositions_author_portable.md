# BRC-X6: all 268 optimal decompositions of the uniform native first-step policy

**Date**: 2026-11-09 Asia/Hong_Kong. **Research role**: TASK_RESEARCH, author-only portable incremental result; **UNREVIEWED / NOT_ADMITTED**, no native Source claim, Result or independent review. **Frozen science pin**: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original 96 ports, six labeled actions, complete seven-component step rewards `R1,...,R6,K` and the next native port; nine frozen roots `0, ±e1, ±e2, ±e3, ±e4`.

## New exact finite classification theorem

Preserve the four native source ports `P=(6,7,28,29)` with signs `(+,-,-,+)`. A deterministic preserving controller is a four-tuple of actions in `{0,...,5}^4` whose signed dictionary of original output atoms `(next port,R1,...,R6,K)` cancels *termwise*. Previous author-side exact work established there are 38 such pure controllers for each of the nine roots, the same 38 across all roots, and proved that the uniform policy `u[p,a]=1/6` requires **exactly six** preserving pure controllers.

**New result**: The uniform policy has **exactly 268 distinct unordered convex decompositions of minimal length six**. Each of the six coefficients is necessarily `1/6`. Classifying each selected controller as *nondiagonal* when `a_6 != a_7` or `a_28 != a_29`, the 268 optimal decompositions have exactly `0,2,3,4` nondiagonal controllers with counts respectively `120,90,40,18`; all other counts vanish. All 38 pure controllers occur in at least one optimal decomposition. Their participation-frequency histogram is `{20:6,30:6,42:21,71:4,142:1}`, totaling `6*268=1608` vertex occurrences.

## Proof and reproducible exact certificate

A pure controller has exactly four nonzero original action coordinates, one for each source port; uniform `u` has all 24 original coordinates positive. Exactly six pure controllers offer exactly 24 coordinate-coverage positions. Therefore every source action at every port occurs exactly once, and its unique controller weight must equal `1/6`. Conversely, any six preserving pure controllers whose actions are a permutation of `0,...,5` at **each** of the four source ports constitute an optimal decomposition. Ordering these six by first-source action `a_6=0,...,5` canonically removes the `6!` permutation ambiguity.

From the frozen native transition/reward function `edge(p,(slot,newbit),root)`, evaluate all `6^4=1296` candidate four-tuples, and retain exactly the 38 whose signed exact output-atom counts cancel. Verify the 38-element set is identical at all nine frozen roots. Let `V_i` consist of preserving four-tuples whose first action is `i`. For the remaining three ports use six-bit occupied-action masks `m1,m2,m3`. The integer recurrence

```
C(i,m1,m2,m3) =
    sum(C(i+1,m1|1<<v[1],m2|1<<v[2],m3|1<<v[3])
        for v in V_i
        if all((m[j] & (1<<v[j+1])) == 0 for j in range(3)))
C(6,63,63,63) = 1
C(6,anything_else) = 0
```

visits exactly **89 memoized states** and returns `C(0,0,0,0)=268`. Its branches are in bijection with all unordered optimal decompositions via the canonical first-action order, proving completeness and nonduplication. A separately implemented exhaustive set-cover backtracker reconstructs the native four-tuples from the frozen `edge` function without consulting the DP; it independently recovers all 268 decompositions and verifies equality of the complete six-tuple collection and the distribution. No floats, sampling, or approximate tolerances are involved.

For the 120 purely diagonal decompositions there is also an analytic count: the sole all-diagonal controller with first action 1 is `(1,1,3,3)`; first actions `0,2,3,4,5` match their second actions, and the common third/fourth actions freely permute `{0,1,2,4,5}`. Hence `5!=120). The other `148=90+40+18` optimal decompositions involve nondiagonal controllers and are certified by exhaustive exact native enumeration.

**Source-side reproducible package** (author-only): `frozen_native_kernel_prefix577.py`, `native_edge_snapshot.csv`, `verify_uniform_optimal_268.py` (integer DP plus independent enumeration), `independent_verify_uniform_268.py` (separate native exact-cover enumeration), `UNIFORM_OPTIMAL_268_CERTIFICATE.json` (entire explicit set of 268 six-tuples), this theorem, and `UNIFORM_OPTIMAL_268_MANIFEST.json`. Both programs passed fresh-directory rerun and file-hash verification. SHA-256 of the compact canonical matching array: `5cd0bcd92b514bf3685c3888c3a626e3a899d53eb5b03898ef6f654783e4b5c3`; exact JSON certificate SHA-256: `57d8d80680b14ef4c6061ca81ee2fe470f3412962156d860fa4e9cf65d5f9055`. Package SHA-256: `83e525ef121bd9b6ec50ca6ff08d8f8d196d69b696d1eea376df9fb28df4c4ef`.

**Novelty scope**: An exhaustive exact classification of *all* uniform-minimal mixtures, refining the prior theorem that the uniform point needs six and the full rational polytope has a sharp 13-term upper bound. No claim of arbitrary-network complexity or native D25 completion. Next portable scientific unit: exact minimum-support certificates for a supplied nonuniform rational policy; original D25 native H0/B0, Frobenius, kappa, CM and byte-exact UR-V2 writer/provenance remain distinct outstanding fronts.

## NEW parametric corollary: all 38 uniform-to-vertex rays, with exact optimal multiplicities

Fix any one of the 38 native preserving pure controllers `v`, and any real (in particular rational) parameter `0<t<1`. Define the original 24-coordinate policy
```
x_t(v) = (1-t)*u + t*v,   u[p,a] = 1/6.
H = (1+5*t)/6, L = (1-t)/6, 0<L<H.
```

**Theorem**: For **every** `v` and **every** `0<t<1`, the exact minimum number of preserving deterministic controllers representing `x_t(v)` is **six**. Every optimal decomposition is obtained by taking an optimal uniform six-controller perfect cover **containing `v`**, assigning weight `H` to `v` and weight `L` to each of the remaining five controllers. Thus the numbers of optimal representations, across all 38 choices of `v`, have the exact histogram **`20:6,30:6,42:21,71:4,142:1`**. For `t=0`, all 268 uniform optimal covers exist; for `t=1` only the single pure vertex remains.

**Proof**: Every coordinate of `x_t` is positive, hence at least six four-action pure controllers are required as for the uniform point. If six are used, their 24 selected action slots cover all 24 coordinates exactly once. Therefore at each port the six controller coefficients must be a permutation of `{H,L,L,L,L,L}`. The unique controller having coefficient `H` must choose the unique high-weight action at **each** of the four ports, which precisely identifies the original pure controller `v`. The other five controllers cover the remaining actions bijectively and have coefficient `L`. Thus optimal representations are in bijection with uniform optimal perfect covers containing `v`. The exact complete 268-cover certificate establishes every `v` is included in at least one cover and yields the displayed multiplicity histogram. Assigning these coefficients produces `x_t(v)` for all real `0<t<1`, proving sufficiency and completeness algebraically.

**New exact checker**: `verify_38_uniform_to_vertex_rays.py` tested `t=1/13,2/5,4/7` × all 38 native preserving vertices × all 9 frozen roots, enumerated every cover containing each `v`, and verified the 24 exact rational output coordinates and the original signed seven-reward/next-port observation; PASS. The finite checks validate implementation while the argument above proves the complete parameter range. Clean ZIP rerun including all three programs and hash-manifest checks passed.

**Updated eight-file portable package SHA-256**: `6fd35e44ca64e7a4b2120d2cfd1df570504f16003a5f0bd054439a837962fc9c`. Same frozen scientific input, origin, nine roots, and `UNREVIEWED / NOT_ADMITTED` status. This parametric family is a new local mathematical extension, not a new canonical Source task claim.

## NEW quadratic BRC residual: certified exactly seven terms for a nonuniform full-support policy

**General exact lower-bound theorem.** For any full-support `x` in the frozen 38-vertex preserving policy polytope, define each source port's *native labeled-action marginal second moment* `M2(p)=sum_{a=0}^5 x[p,a]^2`. If two source ports have different `M2` values, any preserving deterministic convex decomposition has **at least seven terms**. Proof: as all 24 action coordinates are positive and every pure preserving controller covers exactly four (one per source), at least six terms are necessary. With exactly six terms, the 24 source-action slots must be covered exactly once, so each port's six action probabilities are the same multiset of the six mixture weights. Their sums of squares must therefore all be equal. A nonzero second-moment contrast excludes six or fewer terms by a short exact rational certificate.

**Explicit original-native optimal seven-term input.** Take the six-preserving perfect cover
```
v0=(0,0,0,0)  v1=(1,1,3,3)  v2=(2,2,1,1)
v3=(3,3,2,2)  v4=(4,4,4,4)  v5=(5,5,5,5)
```
and a seventh different preserving controller `v6=(0,1,2,3)`, with weights `(1,2,3,4,5,6,7)/28`. All seven original four-tuples pass the exact signed full-seven-component reward/next-port test at all nine frozen roots. The resulting policy `x=sum_i w_i v_i` has all 24 original coordinates positive. The seventh controller overlaps base controllers numbered `(0,1,3,1)` at the four source ports. Thus, by direct exact integer computation, the four second moments have numerator `(154,168,196,168)` over `28^2=784`, namely
```
M2(6)  = 11/56
M2(7)  = 3/14
M2(28) = 1/4
M2(29) = 3/14
```
The moments differ, proving the seven displayed controllers are *provably minimum*: `min_support(x)=7`. This is a complete positive construction and matching lower bound with a constant-length rational certificate; no exhaustive search over all six-controller subsets is necessary.

**Parametric exact-seven family.** For *any* six-controller perfect cover `v0,...,v5`, an extra preserving pure controller `v_*`, positive masses `a0,...,a5,h`, and `S=sum_i a_i+h`, let `c_p` be the index of the base controller that uses `v_*`'s selected action at source port `p`. The resulting seven-term policy has
```
M2(p) = (sum_i a_i^2 + 2*h*a[c_p] + h^2) / S^2.
```
Whenever `a[c_p] != a[c_q]` for two ports, `M2(p)-M2(q)=2*h*(a[c_p]-a[c_q])/S^2` is nonzero, so the given seven-term representation is exactly optimal for **all positive real masses** satisfying that explicit condition. This uses second-moment source contrast as a signed native BRC observation; positive-mass aggregate compression would erase the distinguishing source label.

**Exact implementation check:** `verify_seven_term_moment_obstruction.py` reproduces the rational policy and its four moments, verifies all seven original controllers on all nine roots with complete native signed seven-reward and target atoms, and verifies the complete weighted 24-action policy. Exact certificate `SEVEN_TERM_MOMENT_OBSTRUCTION_CERTIFICATE.json`, SHA-256 `ada20a18a33ce0f5abb8fc7b3e44b4f733d002eb8727e78b7bf0fc5c94755a03`. All four author-side programs passed in a clean extracted directory. Updated **10-file complete portable bundle** SHA-256 `093467fdd8e47611abc7f0003bd76cab1018f90dce35d98d7386ca4260321f7e`.

**Status:** exact model-internal author proof / exact rational verification / no Source-native CLAIM or writer / UNREVIEWED / NOT_ADMITTED. The original Source D25, native CM, and authentic UR V2 provenance remain separate unchanged obligations.
