# R5 — maximal right-persistence intervals for all 2,935 dual-zero collision witnesses

Date: 2026-11-12 (Asia/Shanghai). Mode: author-side exact finite mathematical continuation in the frozen **external** 28-coordinate / 15-labeled-atom P/Q–BRC Blackwell auxiliary model.

## Frozen scientific input and immediate frontier

Original immutable fixture: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551:research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`. Original science pins: Global `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. The immediate prerequisite is PR #2149 at `f40960e285be90937aad827ce46446a1f777f1bc`, which proves that 2,935 masks distributed across 1,065 collision pairs have at least one legal ordered word at their exact collision parameters. Its same frozen verifier and 28-dimensional data are embedded at the start of the accompanying extended verification script.

Let `X` be the 28-component rational nonnegative state; let `P_A=36 sum_{a in A}M_a` be the integral 28-component labeled subset sum, and let `H` be the fixed hidden perturbation. Define the two distinct tracked source-port coordinates `k0=(target0,source3)` and `k1=(target1,source3)`. The relevant exact identities are

\[
x=X_{k0}=X_{k1}=\frac{155682221}{25142124560000000}>0,\quad
H_{k0}=0,\ H_{k1}=-23,\quad U=\frac1{23}.
\]

The hidden-state domain is `I=[L,U]`, where `L=-427508577031693280/628800490619`; the ray endpoint is `E=9/115400000`.

## New theorem: maximal right-persistence of every collision-specific word

For `q in {15,12,3}` and `n` in the previously verified 1,144-value fixed spectrum, put

\[
r_{q,n}=\frac{1-36q/n}{23},\qquad
u_q(r)=\frac{x(1-23r)}{q}.
\]

Fix any ordered word `w` on a labeled operation mask `S` such that:

1. `P_{S,k0}=-n` and `P_{S,k1}=-36q`;
2. at `(r_{q,n},u_q(r_{q,n}))`, every prefix of `w` has all 28 masses nonnegative;
3. `r_{q,n}` is one of the actual admissible interior collision points (`L<r_{q,n}<U`, `0<u_q(r_{q,n})<E`).

**Theorem.** The *same entire ordered word*, without any reordering, is legal at `(r,u_q(r))` for **every real** `r in [r_{q,n},U]`. This is its exact **maximal** legal interval inside `I` when the moving time `u_q(r)` is used and zero-scale endpoint is permitted. If one requires strictly positive operation scale, the maximal interval is `[r_{q,n},U)`.

For any prefix `A` of `w`, define

\[
F_A(r)=X+x rH+\frac{x(1-23r)}{36q}P_A.
\]

Let `r_c=r_{q,n}` and `\lambda=(r-r_c)/(U-r_c)`. The function `F_A` is affine and `u_q(U)=0`, hence

\[
F_A(r)=(1-\lambda)F_A(r_c)+\lambda X(U),\qquad
0\le\lambda\le1.
\]

By hypothesis, `F_A(r_c)\ge0` coordinatewise. The frozen hidden-state interval gives `X(U)\ge0`. Consequently every prefix remains legal throughout `[r_c,U]`. The moving coordinate remains exactly zero after the complete word:

\[
F_{S,k1}(r)=x(1-23r)+\frac{x(1-23r)}{36q}(-36q)=0.
\]

For the fixed coordinate of that same final state,

\[
F_{S,k0}(r)=x-\frac{nx(1-23r)}{36q}
=\frac{23xn}{36q}(r-r_c).
\]

Since the prefactor is strictly positive, `F_{S,k0}(r)<0` for every `r<r_c`. Therefore no legal ordering of that **same mask** at the moving time can extend the validity interval left of the crossing; the entire nonnegative domain is exactly the stated interval. This completes the proof.

The theorem applies to **every** legal ordering of a collision-specific dual-zero mask (not merely the particular deterministic ordering reconstructed by the verifier), since the proof uses only the legality of its prefixes at `r_c`.

## Exact complete census and a new zero-parameter statistic

Applying the theorem to the exact complete PR #2149 candidate census yields:

| q | collision pairs with a dual-zero word | qualifying masks and associated right-persistent words | collision pairs with r_c ≤ 0 | qualifying masks legal at r=0 along u_q |
|---:|---:|---:|---:|---:|
| 15 | 229 | 504 | 229 | 504 |
| 12 | 298 | 749 | 276 | 721 |
| 3 | 538 | 1,682 | 100 | 424 |
| **Total** | **1,065** | **2,935** | **605** | **1,649** |

At `r=0`, the two collision pairs `(12,432)` and `(3,108)` sit exactly at their activation points and contribute respectively three and two candidate masks. The `(15,540)` pair has none. The 1,649 count includes those five threshold-endpoint masks. It counts one canonical reconstructed word per mask, not all distinct legal permutations of a mask.

Each candidate has exactly one left activation threshold `r_c` and is never lost when `r` increases toward `U`. Thus a certificate-aware event sweep can attach this per-mask legal-order certificate at the corresponding collision event and retain it thereafter. At each event, store `(q,n,mask,word)`, the exact rational `r_c`, and the two endpoint conditions above; after ordering the already-known collision events, **no interval re-solving or new path search is needed on the right**. The 1,144 globally uniform fixed-value witnesses and the three shortest globally uniform moving words remain separate existing interfaces.

## Reproduction and evidence scope

The accompanying verifier extends the exact, previously published 28-coordinate PR #2149 source script with new code. It recovers every collision-specific legal word, asserts the 2,935-mask census, checks all its prefixes at the collision and at the rational midpoint, checks `X(U)\ge0`, and verifies the exact negative `k0` value for a point to the left of each crossing. The *whole real interval* is proven by the affine convex-combination identity above; the midpoint checks are an independent implementation regression, not a substitute for that proof.

Run `python3 VERIFY_RIGHT_PERSISTENCE.py` (Python 3 standard library only). A separate local equivalent-fixture Python script was executed on this run and reproduced the summary numbers in `EXACT_OUTPUT.txt`. After publication, independently executing the exact remote file bytes in a clean environment remains a separate verification step.

This result concerns the frozen external auxiliary transport model with its full labeled operation/port information; no projection to a native X6 research slice, broader physical claim, formal Source Result or independent review is asserted. Existing task ownership and original scientific pins are unchanged.

## Next unit

Exploit the one-sided persistence to compute **minimal-size persistent certificate covers**: determine, separately for each `q`, whether the 2,935 masks can be represented by a smaller number of word templates with explicit threshold/activation intervals, preserving ordered provenance and full 28-coordinate legality. A concrete next calculation is to group words by identical labeled prefix sequences and compare their threshold multisets, then derive exact irredundant coverage for the active `(q,n)` events.


## Further theorem — exact minimum dual-zero collision-pair cover

Demand a collection of ordered words such that **every one of the 1,065 labeled pairs (q,n) admitting a dual-zero certificate** has at least one word whose final state vanishes at both k0 and k1 at that pair's collision point. Each word is tied to its full labeled mask S; it does not change mask between events.

**The minimum number of distinct masks/words is exactly 1,065.** A mask's integral vector P_S uniquely fixes n=-P_{S,k0} and q=-P_{S,k1}/36 whenever a dual-zero collision occurs. The same mask therefore cannot witness two distinct labeled (q,n) pairs, even if their parameter walls coincide. Each of the 1,065 pairs requires a separate mask. Selecting any one previously verified legal candidate per pair proves that 1,065 suffice.

Selecting the smallest-cardinality mask for each pair also minimizes the **total number of labeled operations across all 1,065 independently stored words**, since each word uses precisely |S| operations and no word covers two pair labels. Exact enumeration of the 2,935 eligible masks yields the minimum **6,379 total operations**, with maximal individual length **10**. The minimal word-length histogram (length: number of collision pairs) is

\`2:4, 3:32, 4:116, 5:244, 6:289, 7:227, 8:114, 9:34, 10:5\` (total 1,065).

This replaces the 2,935-mask collection by a minimal **1,065-entry cover**, omitting 1,870 redundant choices while retaining one exact simultaneous-zero witness at every eligible pair event. Every chosen word inherits the maximal right-persistence interval proved above. This is a minimal cover of *dual-zero collision-pair evidence*, not a lower bound for the generic first-zero spectrum, whose three uniform moving witnesses remain an existing interface.

**Next scientific question:** construct a compressed prefix-sharing representation for these 1,065 words, measure stored bit/operation cost against the 6,379-symbol flat representation, and prove that sharing preserves each labeled operation and its exact 28-coordinate legality certificate.
