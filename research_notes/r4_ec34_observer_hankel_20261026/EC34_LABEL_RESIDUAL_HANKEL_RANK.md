# R4-EC34 — Exact minimal BRC source-label residual dimension

**Author-side exact mathematics; not independently Driver-reviewed or mathematically admitted.** Date: 2026-10-26, Asia/Shanghai. Native attribution: `NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION`.

## Frozen sources and current authority

- GLOBAL_KNOWLEDGE_V1 canonical main: `596508231dcc5d8cf66c6b991a311dd5d89c2ba0`. At this immutable commit, read the `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, Enterprise Math project router, P000, P000_STARTUP and ACTIVE worldview. P000 original file has blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` and `ACTIVE_LOCKED`.
- Enterprise Math project main at the scientific source freeze: `c5902704247dcbecf47b24981935c623db607653`, including `docs/PORTABLE_RESEARCH_PROTOCOL.md` and Heartbeat BRC-only arithmetic constraints.
- Exact predecessor: R4-EC33 at commit `0f84db42704c6e107adb9fd99d5e64cb77589e9d`; original `EC33_verify.py` blob `6131d73404536133ed4a93a0fd14afe78d2acd78`, SHA-256 `c2c5b183f88e7856c006f6b9ca954d603ac4e2cfd25d65a5558c67c91bc69856`. This predecessor proved full scalar-count agreement and quantified a total-variation label defect; EC34 newly determines the *minimal source-history dimension* required by a refined observer.
- Authenticated GitHub identity: `awdawmip`. Native task inventory returned `CONTROL_QUOTA`; native researcher session attempt returned `STATIC_READONLY_SCOPE_DENIED` and `operation_sent=false`. No current native task owner or CLAIM was established; these are independent author-side research notes, not an adopted task or native Result.

## Exact positive-source BRC object

Fix any integer `H>=1`. In the same EC33 auxiliary model, there is one operation symbol `A`, two observable source labels `R,B`, and `H+1` history states `q=0,...,H`. The initial state is 0 and all terminal states have readout weight 1.

For `q<H`, exactly one microscopic `R` edge and one microscopic `B` edge go to `q+1`. At `q=H` there are exactly two **distinct positive microscopic R alternatives** looping at `H`, and no `B` edge. These two sources share only the *observed* class R; their microscopic provenance remains distinct. Ordered composition multiplies path choices and alternative branches add as nonnegative integers. No signed amplitudes, physical phases, numerical roundoff or P000-native heartbeat evolution enter the claim.

Let `F_H(w)` denote the count of microscopic source paths with observed label word `w∈{R,B}*`. Let `T_H(n)=Σ_{|w|=n} F_H(w)` be the label-blind total.

## Theorem A — Exact refined Hankel rank H+1

For every `H>=1`, the infinite label-refined Hankel matrix `K_H[p,s]=F_H(ps)` over the rational field has **rank H+1**. Accordingly, *every* rational linear weighted representation of the full labelled source-count series has at least `H+1` states. The explicit positive-integer EC33 carrier has exactly that many; hence its minimum dimension among rational realizations **and** among nonnegative-rational source-count realizations equals `H+1`.

**Proof.** The observed path `B^k` has exactly one microscopic source path for `0<=k<=H`, and has none for `k>H`: before the saturated state a unique B edge exists, while at state H all B edges are absent. Thus

`F_H(B^k)=1_{0<=k<=H}.`

Choose the `H+1` prefixes `B^i` and `H+1` suffixes `B^j`, `0<=i,j<=H`. Their explicit Hankel minor is `K_{ij}=1_{i+j<=H}`. Reversing its columns gives `K'_{ij}=1_{i<=j}`, upper triangular with unit diagonal. Column reversal has sign `(-1)^{H(H+1)/2}`; therefore

`det K=(-1)^{H(H+1)/2}`, so `|det K|=1`.

Consequently the full refined Hankel rank is at least `H+1`. For any `d`-state rational weighted representation `F_H(ps)=α M_p M_s β`, the Hankel matrix factors into a prefix-row and suffix-column matrix through a `d`-dimensional space, so its rank is at most `d`. The existing `H+1`-state EC33 positive source carrier provides the upper bound. The refined rank and both claimed minimal dimensions equal `H+1`. QED.

## Theorem B — Scalarization hides arbitrarily much exact history state

In the same `V_H` source model, the label-blind total is exactly `T_H(n)=2^n` for all `n>=0`. Its scalar Hankel matrix `S_{ij}=T_H(i+j)=2^i2^j` has rank **1** and a one-state nonnegative realization (`α=[1], M_A=[2], β=[1]`). Thus:

`minimal_refined_dimension(H)=H+1`,

`minimal_scalar_dimension(H)=1`,

`exact_lost_linear_state_dimension(H)=H.`

**Proof.** From each residual state exactly two microscopic source alternatives exist in aggregate: one R and one B before saturation, or two R after saturation. Summing all label choices gives `T_H(n)=2^n`, and the claimed outer-product rank-one Hankel factorization follows. Theorem A fixes the refined dimension. Since H is arbitrary, the lost dimension is unbounded despite **perfect scalar agreement at every depth** with the one-state model U. QED.

**Sharper obstruction to an unsafe native lift.** Moreover U and V_H agree on **every** labelled word of length ≤H (proved already in EC33), but disagree at `B^(H+1)` with counts `F_U=1` and `F_V=0`. Therefore neither all-depth scalar agreement nor a known scalar Hankel rank of 1 supplies a valid finite-horizon bound for label/source-fibre equivalence. EC32/EC33 finite equivalence cutoffs require a proven **closed refined state dimension**, not the dimension of its collapsed observer.

## Reproducible exact BRC checks

`EC34_GITHUB_VERIFY.py` actually executed with the pinned EC33 source and separately implemented positive microscopic branch traversal. For `H=1,...,18`, it passed 432 B-only word checks, 333 aggregate-source count checks, 2,469 refined Hankel-entry checks, 18 exact determinant checks, 18 refined rank checks, and 18 scalar rank checks. Re-execution gave a byte-identical `EC34_GITHUB_REPORT.json`. Finite testing only cross-checks the carrier; the quantified all-H claims are algebraically proved above.

The verification entrypoint is `python EC34_GITHUB_VERIFY.py --upstream EC33_VERIFY_UPSTREAM_PINNED.py --max-h 18 --out EC34_GITHUB_REPORT.json`. For offline replay, the attached ZIP includes the exact SHA-256-pinned unchanged EC33 upstream; the GitHub directory references that existing immutable source instead of duplicating it.

## Scope / remaining problem

These are BRC **positive-source ordered-path** results about the explicitly declared auxiliary EC33 carrier. They do not identify a P000-native fixed Heartbeat World update, P000's X6 time/third-coordinate/slice bridge, signed phase, physical residual or an independently accepted theorem. P000 remains `ACTIVE_LOCKED` and currently declares `fixed_heartbeat_program=null`. The extra H memory states are nonspatial, future-relevant provenance state, **not new spatial axes**.

**Next EC35 problem:** obtain a fully specified authorized native X6 *labelled* source transition system with closed future-operation/port types and a justified residual dimension bound, or independently prove a label-respecting compositional relation. Only then apply an EC33 refined finite test. If native transitions remain undefined, derive checkable labelled-observer quotient criteria within explicit auxiliary BRC carriers, preserving microscopic identity as a separate type.
