# C265 author-exact: nine new strict four-free-coordinate pair hulls (160 leaves)

Date: 2026-10-23. **This is a non-canonical author research handoff, not a Task CLAIM, native GF(2)-BRC theorem, Source Result, or independent Driver review.** Preserve the original 35 basic proof leaves.

Frozen research source: `awdawmip/chatgpt-global-knowledge main@bf441dbd96e3aff7f1df531c6569d56fa048a10b`; `awdawmip/enterprise-math main@c7493e79071578d6d762ce870908f69919056af7`. Parent scientific artifact: C264 complete author-exact package, sha256 `2d2cdd57421c310827f2e727689ede5cc8dc524c3ee56c8d2e8e260d94c3de50`.

## Exact theorem in the C195/H168 external 79-node positive-rational interpolation auxiliary

Let `I=(5,50,55,56)`, `J={0,...,78}\I`, `Q=2^128`, `H=2^166`, `Z=141421356237309504880/10^20`, and `A=6912*50000^2/17^2`. Use the 79 original strictly increasing rational nodes `u_0,...,u_78` from `C195_BASE_RATIONAL_NODES.json` in the unchanged C264 parent.

For `j in J`, let

`B_j=floor((Q*A/H)/((2-u_j^2)*(3-u_j^2))^3 * product_{r!=j} (Z-u_r)/abs(u_j-u_r)) > 0`.

For order-preserving moving vector `v`, define

`F(v) = sum_{j in J} B_j * product_{p in I} [(Z-v_p)/(Z-u_p)]*[abs(u_j-u_p)/abs(u_j-v_p)] + sum_{k in I} (Q*A/H)/((2-v_k^2)*(3-v_k^2))^3 * product_{j in J} [(Z-u_j)/abs(v_k-u_j)] * product_{p in I,p!=k} [(Z-v_p)/abs(v_k-v_p)]`.

All denominators are nonzero on the following three exact closed four-variable regions:

* Root C254 boxes `(0,21)`: `v_5=[4/543,9/613]`, `v_50=[43/62,57/79]`, `v_55=[53/68,38/47]`, `v_56=[9/11,121/147]`; 42 strict leaves / 41 exact midpoint splits, minimum `floor(LB)-Q=222837823719880734794660194768903177`. New exact-contained pair hulls `(0,7),(0,21),(7,21)`.
* Root `(1,2)`: `v_5=[3/407,7/477]`, `v_50=[5/7,31/43]`, `v_55=[60/77,87/109]`, `v_56=[4/5,9/11]`; 43 strict leaves / 42 splits, minimum `66320106200372350631609665116465695`. New pairs `(1,2),(1,19),(2,19)`.
* Root `(0,5)`: `v_5=[4/543,9/613]`, `v_50=[43/62,57/79]`, `v_55=[4/5,38/47]`, `v_56=[13/16,121/147]`; 75 strict leaves / 74 splits, minimum `7051427716607632418455595386647295`. New pairs `(0,5),(0,22),(5,22)`.

Thus every real point in the union of the three complete continuous roots obeys

`F(v) >= 2^128 + 7051427716607632418455595386647295 > 2^128`.

Classification of the 363 valid legal pair hulls: **213 exact auxiliary F<Q witness hulls; 99 proven positive F>Q entire hulls; 51 unclassified four-free-coordinate hulls.** The other 232 of all 595 pairs are outside the presently valid pair-hull method domain, not silently classified. No original 15,685-candidate enumeration is newly executed, and this does not compress the original 35 single-leaf boxes.

## Load-bearing inequality, complete-cover verification, and bounded scope

For every fixed branch and moving coordinate, `T_jp(t)=[abs(u_j-u_p)/(Z-u_p)]*(Z-t)/abs(u_j-t)` has `T_jp''(t)=2*abs(u_j-u_p)*(Z-u_j)/[(Z-u_p)*abs(u_j-t)^3] > 0`, and its monotonic direction is determined exactly by the order `j<p` versus `j>p`. Taking the appropriate endpoint independently for unretained coordinates yields a valid positive lower factor. For a moving branch, after using endpoint minima of all other moving coordinates, its logarithmic second derivative is

`6*(2+t^2)/(2-t^2)^2 + 6*(3+t^2)/(3-t^2)^2 + sum_{j in J} 1/(t-u_j)^2 + sum_{p != k} 1/(t-e_p)^2 > 0`.

Consequently the corresponding 1-variable moving branch is convex. `BASE` sums endpoint lower bounds on all 75 fixed branches and unshared lower tangents on the four moving branches; `SHARED_k` instead preserves the common `v_k` dependence of the sum of 75 fixed branches and the kth moving branch, takes **one** common tangent to that convex sum, and bounds the other moving branches separately. Each leaf's resulting `LB(C)` is valid throughout its entire rational closed subbox `C`.

Three complete dyadic binary trees, with 157 interior nodes and 160 terminal boxes, cover the three roots exactly; all 160 exact `Fraction` computed margins are strictly positive. A second same-author code path reconstructs the 79 original nodes, all 75 integer floor masses and all 160 bounds using rational dual numbers; it confirms the precise margins, tree containment and nine newly contained pair IDs. Second audit: PASS; **not** independent Research Driver acceptance or formalization.

## Evidence, authority, and next unit

The complete local portable scientific archive is `EM_C265_9_NEW_STRICT_4D_PAIR_HULLS_160_LEAF_AUTHOR_EXACT_PORTABLE.zip`, 5,606,708 bytes, sha256 `1969f977454eaeffbb668dadc96c0300d600367e0b699924b4552b0d8de0debe`. It contains a full Chinese paper, 91 KB exact tree certificate, generation and second verification code, original inputs, unchanged C264 parent ZIP and source manifests. The local archive's exact audit passed, including an archive extraction and arithmetic check. **This note alone does not claim that those archive bytes have been uploaded to GitHub.**

The native task-list attempt returned `CONTROL_QUOTA`; a native researcher session-start attempt returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. Current active Owner could not be verified; no CLAIM or Source Result was obtained. As explicitly requested, no Google Drive substitute was used to bypass that access denial.

BRC scope: the 79 positive branches form an auxiliary positive-mass observable, retaining exact rational weights and shared coordinates, but no established port/label/phase/future-operation-preserving factorization to the native GF(2)-BRC six-dimensional Cell object exists. `POSITIVE_WEIGHTED_BRC != SIGNED_OR_PHASE_CANCELLATION`; P000 is unchanged.

Next smallest hard mathematical unit: derive a *two-shared-coordinate* exact rational or Hessian-assisted bound for the still-unclassified full four-free-coordinate root `(0,16)=(0,28)`, or produce an exact rational auxiliary `F<Q` counterexample. Exploratory floating-point `F/Q≈1.0037013` is **not** a strict certificate.
