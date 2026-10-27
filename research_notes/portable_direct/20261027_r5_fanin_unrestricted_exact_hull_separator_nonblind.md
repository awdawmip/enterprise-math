# R5: strict unrestricted support separation on the new positive eight-leaf LR-fan-in tree

Date: 2026-10-27 Asia/Taipei. Evidence status: **NONBLIND / EXACT FRACTION-CHECKED / UNREVIEWED / NOT_ADMITTED**. This is independent nonblind algebraic checking of an earlier author's new candidate, not a native RESEARCH_DRIVER review, an admitted Result, or authorization to publish a formal V2 Task.

## Original author and exact input

The original eight-leaf positive dual-measure model, bilinear/fixed-policy-slice proofs and X6 ordered-path bridge belong to the author of:
`awdawmip/enterprise-math@3bc9cebddc821dcf38dfad011fdfc148ec47885d:research_notes/brc_r5_fanin_bilinear_rank_20261027_t11/PROOF.md` and its `AUTHOR_VERIFY.py`, `AUTHOR_EXACT_OUTPUT.txt`, `NEXT_TASK.md`. That author correctly marked unrestricted hull membership as unproved. The following is a distinct next proof unit obtained by releasing **all** decisions for this exact input.

At t=1, both A and B have stop-P, stop-Q, continue actions. At t=2, AU, AV, BU and BV have the same actions. Each t=3 terminal has either declaration. For every terminal, the **positive** Q and P mass is:

| leaf | Q | P |
|---|---:|---:|
| AU0 | 1/12 | 1/48 |
| AU1 | 1/12 | 7/48 |
| AV0 | 1/6 | 1/48 |
| AV1 | 1/6 | 1/16 |
| BU0 | 1/8 | 1/16 |
| BU1 | 1/8 | 3/16 |
| BV0 | 1/8 | 1/8 |
| BV1 | 1/8 | 3/8 |

Both measures sum to one. AU and BU share the (time=2, likelihood ratio=1) signature, and seedless LR must assign them the same local action distribution. All other time-indexed signatures are distinct. P and Q are typed positive branch masses; below signed linear costs are dual observer coordinates and **not** positive BRC masses. The paper's native X6 embedding is a separately declared observation bridge, not a native two-dimensional model.

## New exact theorem: unrestricted convex hulls differ

For the four-vector `O=(P[declare Q], Q[declare P], E_P[tau], E_Q[tau])`, define the signed support functional

```text
J(O) = 80 O_1 + 25 O_2 - 2 O_3 + 3 O_4.
```

For **all** locally randomized real-valued, unrestricted stopping/declaring policies, exact values are

```text
min_{full histories}      J = 149/6
min_{seedless LR histories} J = 301/12
LR minus full = 1/4 > 0.
```

The full-history optimum is witnessed by: t1 A,B continue; t2 AU continue, AV declare Q, BU declare P, BV continue; t3 AU0 declare Q, AU1 declare P, BV0/BV1 declare P. It has four-vector `(5/48,7/12,8/3,29/12)` and support `149/6`.

The seedless-LR optimum is witnessed by: t1 A,B continue; t2 AU and BU **both** declare P, AV declare Q, BV continue; t3 BV0/BV1 declare P. Its four-vector is `(1/12,2/3,5/2,9/4)` and support `301/12`.

These are global, not fixed-decision-slice statements. In particular,

```text
conv(O_seedless_LR) is a proper subset of conv(O_full).
```

Therefore this **second, distinct** positive eight-leaf fan-in candidate cannot witness the mother question `conv(O_seedless_LR)=conv(O_full)` but `O_seedless_LR != O_full`. This does **not** settle the general mother question.

## Exact Bellman certificate

Each row gives the total signed cost of stop-declare P, stop-declare Q, or continue with optimally chosen t3 terminal declarations:

| time-2 node | P | Q | C |
|---|---:|---:|---:|
| AU | 9/2 | 41/3 | 17/4 |
| AV | 10 | 25/3 | 25/3 |
| BU | 27/4 | 41/2 | 7 |
| BV | 23/4 | 79/2 | 11/2 |

At time 1, immediate P/Q costs are A=(27/2,21), B=(25/2,60).

Full-history Bellman gives A=`min(27/2,21,17/4+25/3)=151/12` and B=`min(25/2,60,27/4+11/2)=49/4`, total `149/6`.

In seedless LR, fix the common t2 action on AU and BU, then optimize everything else (including stopping at t1). The three unrestricted pure cases are:
`shared P -> 301/12`, `shared Q -> 26`, `shared C -> 301/12`.

**Why this covers all real randomizations:** conditional expected observation is affine in each individual local action simplex. The only shared LR action is used at the *mutually exclusive* AU and BU t2 histories, so the objective is also affine in the single shared probability vector. Thus a minimum over all real randomized policies occurs at deterministic choices; Bellman covers all those choices. No finite-grid or floating-point optimization is used as proof.

## Independent full-exhaustion check

An independent Python `fractions.Fraction` calculation reconstructed the eight leaf measures, all four-vector deterministic outcomes and every node cost. Raw deterministic policy counts:
full `3^6 * 2^8 = 186624`; seedless-LR `3^5 * 2^8 = 62208`. After collapsing unreachable branches and identical observations, there are **1402** distinct full vectors and **754** distinct LR vectors (LR vectors are included in full). Their exhaustive exact minima match Bellman at `149/6` and `301/12`. This constitutes a second independent finite-tree computation path. No extra axiom, admitted theorem or formal native review is asserted.

## Next mathematical frontier

Exclude this new candidate from the equal-hull witness pool. On a structurally different strictly positive intermediate LR-fan-in tree, first certify equality of the **complete unrestricted** four-vector convex hulls (using exact deterministic policy supports). Only then test nonattainability of a full point by **all real** seedless-LR local randomization parameters. Do not mistake a fixed-policy-slice obstruction for the unrestricted theorem.

Contribution attribution: original construction and fixed-slice proof remain the original author's; this report supplies the unrestricted signed separator and complete policy certificate. Preserve this note as source-exposed research evidence pending genuine independent review and original native Driver authorization. P000, active X6 / three-dimensional-slice terminology and observation/provenance boundaries are unchanged.
