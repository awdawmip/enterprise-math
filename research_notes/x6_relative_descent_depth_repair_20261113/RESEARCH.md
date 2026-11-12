# X6 — Exactly 720 signed-triad transformations descend to the joint relative observer

Date: 2026-11-13 (Asia/Shanghai). Scientific source frozen at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, especially `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` §6 (the complete twenty-observer quotient). This continues the author-side signed-C6 triad-group results of Draft PR #2211, source `13640347cecfedb940a57bae5579877eb393225a`. It is a scoped mathematical result about the joint X6 coordinate observer, not a declaration of physical rotation dynamics or a formal native Result/Review.

## Frozen geometry and group inputs

Use the full native signed Cell displacement group `G6_FULL = Z^6` in a chosen chart, the diagonal subgroup `Delta=Z D` with `D=(1,1,1,1,1,1)`, and the joint relative readout `G6_REL=Z^6/Delta`. The canonical representative is `can6(x)=x-min_i(x_i)D`, with a lossless depth repair `h=min_i(x_i)`. This is a spatial composite diagonal coordinate, not a seventh spatial axis.

For an ordered signed triad `i,j,k`, the previous exact candidate `T_ijk` sends `e_i->e_j, e_j->e_k, e_k->-e_i`, fixing the other axes; the compensated candidate `U_ijk;l=D_l T_ijk` also flips one complementary axis `l`. The earlier verified generated groups are
`G_T=(C2)^6 semidirect A6` (order 23,040) and `G_U=(C2)^5 semidirect A6` (order 11,520), interpreted as concrete signed-coordinate permutations.

## Theorem 1 — exact quotient-descent criterion

For any signed permutation `g` of the six native axes, let `epsilon(g)=gD`, a six-vector whose entries are each +1 or -1.

**Statement.** The rule `[x] -> [gx]` is a well-defined group automorphism of `G6_REL` for every signed state x if and only if the six entries of `epsilon(g)` are all equal. Equivalently, `gD=D` or `gD=-D`.

**Proof.** Two signed states have the same joint relative readout exactly when their difference equals `tD` for some integer t. Their images then differ by `t gD`. Constancy on all relative fibers is equivalent to `g(Delta) subset Delta`, i.e. `gD in Delta`. A signed permutation maps D to a vector of six ±1 entries, and such a vector is in `Delta` precisely when every sign is equal. In that case `g(Delta)=Delta` and the inverse signed permutation also descends. QED.

**Corollary 1.** Both previously computed candidate groups have exactly the same quotient-safe subgroup
```
     H = { (+I) P, (-I) P : P in A6 } = C2 × A6,
     |H| = 2 * 360 = 720.
```
For `G_T` the sign subgroup is all 64 patterns; for `G_U` it is the 32 even-parity patterns. Since the dimension is six, both all-positive and all-negative patterns have even sign parity and occur in both groups. The coordinate-permutation component is A6. The induced action of H on the five-rank relative quotient is faithful: if `[g e_i]=[e_i]` for all six i, then each sparse vector `g e_i-e_i` (at most two nonzero components) must be zero if it belongs to the all-six diagonal subgroup, forcing g=I. Thus the observer-visible group really has order 720.

**Explicit failure witness.** The two full signed vectors 0 and D have identical initial relative readout. For `T_123`, `T D=(-1,1,1,1,1,1)` in the convention of the selected oriented triad, while `T0=0`. Their canonical relative readouts are respectively `(0,2,2,2,2,2)` and 0. The two initial relative-equivalent states have distinguishable successors. This is a concrete missing-depth witness, with no assumption of noise or approximation.

## Theorem 2 — one-integer exact repair and its necessity

For `r=can6(x)` and `h=min_i(x_i)`, the original signed state is uniquely `x=r+hD`. For any signed permutation g let
```
    z = g(r) + h * epsilon(g)
    h' = min_i z_i
    r' = z - h' D.
```
Then `(r',h')` is precisely the canonical relative/depth description of `gx`, for every integer signed state and every g in either group. The map composes exactly, because it is the coordinate conjugate of the exact signed linear group action under the full-state bijection `x <-> (r,h)`.

If `epsilon(g)` has mixed signs, then the family of initial states `r+hD` with one fixed r but all integer h produces pairwise distinct relative successors: their differences are `(h_1-h_2)[epsilon(g)]`, which is nonzero in the torsion-free quotient for unequal h. Thus a globally exact successor from the relative readout alone is impossible for that g; one unbounded integer common-depth coordinate is a sufficient and faithful repair. This minimality statement refers to the missing one-dimensional diagonal fiber, not to a preferred computer encoding or to the richer BRC packet state.

## Theorem 3 — endpoint-only versus intermediate-trace readouts

For a sequence of signed-coordinate macro-operations `g_1,...,g_n`, the final relative readout depends only on the initial relative class if and only if the total product `g_n...g_1` lies in H. Every intermediate readout (the full sequence of time-ordered relative observations) descends from the initial relative class if and only if each prefix product lies in H; because H is a subgroup, this is equivalent to every individual `g_j` lying in H.

For either candidate `T_123` or `U_123;4`, the six-step cycle is the identity and hence its final readout descends, but steps 1 through 5 send D to a mixed-sign vector, so the entire observed trace requires depth repair. This is an explicit observer-horizon distinction, consistent with P000 time as ordering of relational changes.

## Exact independent local verification

An independently implemented Python standard-library verifier enumerated signed basis-image tuples and their exact products. It reconstructed `|G_T|=23040`, `|G_U|=11520`, selected and compared both quotient-safe sets (each **720** elements), checked faithfulness, verified the repair recurrence on four signed test vectors for all 23,040 elements (**92,160 exact transitions**), and checked all seven phase positions n=0..6 of both T and U. All assertions passed. This scope matches integer signed-coordinate group action and the frozen joint-relative observer. Group structure proofs and exact enumeration are distinct evidence; a true native physical rotation/triadic/C12-C24 bridge remains a separate research target.

## Further scientific work

1. Classify operation-safe **decorated BRC paths**, including boundary-marker retention, weights, phase, branch provenance and timing, for the exact H subgroup and non-H generators with common-depth repair.
2. Determine which macrostep sequences have a safe *stroboscopic* relative readout while their intermediate time trace requires repair; quantify minimal state for a finite declared observer schedule.
3. Check the explicit TRIADIC_CLOSURE_E and restricted C12/C24 carrier relations under candidate group actions when the necessary native laws are available.

The current proof is a project Draft PR scientific artifact. No CLAIM, formal Result, Review or Foundation admission follows merely from its publication.
