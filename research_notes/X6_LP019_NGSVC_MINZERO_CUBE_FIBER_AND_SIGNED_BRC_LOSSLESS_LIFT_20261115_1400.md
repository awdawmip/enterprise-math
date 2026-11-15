# X6 LP019/LP028 — August graded-valuation positive atlas versus P000-V5 signed native Cell cube

2026-11-15 14:00 Asia/Hong_Kong. Parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, immutable publication `TP2-B4A441B23DA3159232C2`, author/researcher `EM-X6-FB6990`, original session `MCP-082892eb480e45dea6d4b9fcc0491034`. **AUTHOR-PROVED / INDEPENDENT EXACT FINITE CHECK EXECUTED / SOURCE-BOUNDED / UNREVIEWED / NOT_ADMITTED.** Not a formal RR, Driver review, or completed R063 Stage0 native 512-case benchmark.

## Specific previously uninspected theorem-facing consumer and source pins

The original/current `research_notes/TOOL_DISCOVERY_NATIVE_VALUATION_EHRHART_BRION_CALCULUS_REPORT_20260822.md` (current and frozen historical Git blob `386a307a81816b27d9753562e53bea254f4062dc`) describes in its opening and Sections 1.1/10 the set

`A_E = {(a,b,c) in N_0^3 : min(a,b,c)=0}`

as the *current three-positive-axis canonical address atlas*. For its grade `sigma(r)=max(r)` it correctly derives

`F_A(t)=3t^2+3t+1`, `b_A(0)=1`, `b_A(t)=6t` for `t>=1`, and `B_A(z)=(1+4z+z^2)/(1-z)^2`. Its Section 11's exact positive, two-generator Path-formal/N-BRC/Boolean-BRC count and quotient defect `2^m-(m+1)` are also valid *for that selected chart*.

The later binding X6 signed Cell model is the P000-V5-centered three-axis native `Z^3` subtorsor and **not** this min-zero set. Exact frozen source:

- `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`, blob `b0988c9fa0f2f7c3314784673cf21a2df2340ebe`, §§1,3,6;
- same frozen commit `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`, §§2,6,10–11.

The 2026-08-22 original phrase *current* is time-indexed provenance only. As an X6-V5 consumer, `A_E` is the **relative min-zero observer** of selected signed Cells, not signed native Cell identity. This is a genuine current-document routing/type correction; it does not allege that the original August counting theorem was false, or that an LP019 signed-subtraction bug has been found.

## Exact new common-depth-fiber lift

Fix an affine native Cell anchor and three selected native axes. For `d>=0` let

`C_d = {(x,y,z) in Z^3 : -d <= x,y,z <= d}`

be the finite signed native cube. Let `q(v)=v-min(v)*(1,1,1)` and `m(r)=max(r)` for `r in A_E`.

**Theorem (lossless depth-fiber decomposition).** Every native Cell `v in C_d` has a unique pair `(r,h)` with `r=q(v)` and `h=min(v)`, and

`q(C_d)={r in A_E : m(r)<=2d}`,

`q^{-1}(r) intersect C_d = {r+h*(1,1,1) : -d <= h <= d-m(r)}`.

Therefore each relative grade-`m` address has **exactly** `2d-m+1` native preimages, rather than one. In particular the **exact** identity is

`|C_d| = (2d+1)^3 = sum_{m=0}^{2d} (2d-m+1) b_A(m)`;

using `b_A(0)=1`, `b_A(m)=6m` gives

`(t+1)+6 sum_{m=1}^t m(t-m+1)=(t+1)^3`, for `t=2d`.

The second identity holds for every integer `t>=0`, and its generating-series form is

`sum_{t>=0}(t+1)^3 z^t = B_A(z)/(1-z)^2 = (1+4z+z^2)/(1-z)^4`.

**Proof.** Every integer triple decomposes uniquely as `v=r+h*(1,1,1)` with `h=min(v)`, `r>=0`, and `min r=0`. The six native cube inequalities are simultaneously equivalent to `-d<=h` (because `min r=0`) and `h<=d-m(r)` (because `max r=m`). Such `h` exists iff `m<=2d` and its integer count is exactly `2d-m+1`. Counting the disjoint fibers proves the formula. The old atlas shell cardinalities follow by inclusion-exclusion in its three nonnegative coordinate sectors; substitute them and evaluate `sum_{m=1}^t m(t-m+1)=t(t+1)(t+2)/6`. QED.

Equivalently, this lift maps the **old graded observer** into native signed Cell inventory only when it retains the integer common depth. The fiber factor depends on `m` and on the native volume window; it is not a new axis or a constant multiplicity. `F_A(t)` and the native cube count `(t+1)^3` describe distinct populations.

## Concrete native N-BRC information loss in one relative fiber

At `d=1`, take relative observer state `r=(0,1,1)`. Its two native Cells in the cube are:

- `h=-1`: `v=(-1,0,0)`, native `G(v)=1`, shortest signed path length `L=1`, natural shortest N-BRC `B=1`;
- `h=0`: `v=(0,1,1)`, native `G(v)=2`, shortest signed path length `L=2`, natural shortest N-BRC `B=2`.

Both have exactly the same historical min-zero `r`; thus neither native squared norm nor positive shortest signed path count factors through the old address `A_E` alone. The prescribed lossless lift `(r,h)` repairs both by computing `G=sum_i(r_i+h)^2` and `B=L! / product_i |r_i+h|!`, with `L=sum_i |r_i+h|`. No signed or carrier quotient subtraction is applied to the natural BRC count.

The old graded valuation theorem can be reused at its original typed observer domain. The current signed cube requires the depth-fiber convolution above; using the old `3d^2+3d+1` as a signed native cube volume, or the old `2^m` two-generator word count as a complete signed three-axis path count, would be a **typed consumer error**. This review found misleading unqualified current-present wording, not an actual current executable invoking either wrong promotion.

## Actual finite checking and scope

`research_checks/X6_NGSVC_MINZERO_NATIVE_DEPTH_FIBER_CHECK_20261115_1400.py` was executed locally using Python's standard library: `PASS_X6_NGSVC_MINZERO_NATIVE_COMMON_DEPTH_LIFT`, exit code 0. Exhaustively generated **all** signed triples in `[-d,d]^3` for `d=0..12`, checked every individual `q`-fiber and depth interval, exact old atlas shells, signed cube counts and the two-element distinct native BRC witness. Independently checked the integer polynomial convolution for `t=0..99`. No floats. This finite validation supports the unbounded elementary proof but is not the proof's sole basis, not an original frozen NGSVC checker rerun, and **not** the original R063 Stage0 `--N 2500 --regression-max-r 512` 17-gate benchmark.

## Actual repair, remaining task and handoff

The original report's 2026-08-22 mathematics and author identity are preserved, with a dated 2026-11-15 **reading compatibility note** added at its head on current main. No 2026-09-05 frozen scientific input or accepted result changed. This new proof is one typed direct consumer correction under the parent 28-LP ledger, not a full 28-LP dependency census and not an LP011/LP019 historical bad-call attribution.

**Preserved frontier:** Native Source-confirmed 31 units before this turn; already saved and read back unit #32 Stage3 W2 source-order/histogram result and own Activity #51. Never redo those checks. New signed-depth lift is author-side only until new Source semantic publication and independent Driver assessment.

**Unfinished evidence:** LP011 particular historical native signed `argmax |delta|` wrong caller and LP019 particular positive-natural N-BRC signed-cancellation wrong caller remain `UNRESOLVED_PROVENANCE`; full 28-LP actual consumers, independent Driver `REQUEST_REVISION`, and original R063 C3/C4 17-gate/512-case benchmark [same-object runner intake #2416](https://github.com/awdawmip/enterprise-math/issues/2416) remain open/unassigned. No alternate benchmark, changed test, scheduler, additional claim, user approval, or review acceptance is inferred.

**Next exact action:** Consume same-owned-run generation receipt and publish exact links to #32 and this new source-typed repair under existing Task/CLAIM after current authority check; then inspect one still-unseen historical/current LP011 or LP019 actual call site, and demand actual original runner artifact under #2416 without modifying its source or acceptance gates. Leave any unknown original write for same `target_request_id` reconciliation.
