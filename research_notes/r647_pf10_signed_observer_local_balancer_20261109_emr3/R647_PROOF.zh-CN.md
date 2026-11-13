# R647 — PF10 signed-observer local PASS balancing and odd X6 triad holonomy
Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_SIDE_EXACT_THEOREM; DRIVER_UNREVIEWED, NOT_ADMITTED.
Frozen scientific input: signed R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Source-defined V23/V27/V17/V29@b62110008321d9147212cb89f2627ff613c2550d; precursor R645/R646 under PR #1708. P000 and native X6 meanings remain unchanged.

## Typed model

One Cell with four internal ports 0..3; V29 internal PASS(a→b) increments a nonnegative count M_ab. No TRANSFER, reverse PASS, or additional PASS types in the model. Retain the four edge types B=(01,20,23,30) from R645 and an integer seed M_0=m M_B (m>=1), where M_B is one occurrence of every B edge. Define signed PF10 outputs u=M1−Mᵀ1, Ω=M−Mᵀ and Q=1ᵀu=0. Six native axes still supply all 20 active three-axis subsets. Use exact V23 code c(S), nine-neighbor |S∩T|=2 and V27 score Φ_M(S,T)=u·c(T)+c(S)ᵀΩc(T).

A NEW deterministic auxiliary event-selector (not a source-native time law) uses ONLY the currently observed four signed Ω coordinates: choose the least value among Ω_01, Ω_20, Ω_23, Ω_30; break ties by a fixed priority permutation w of B. Since reverse edges never occur, Ω_ab=M_ab for every a→b in B. After computing the unique V27 triad successor, execute ONE V29 PASS according to this selector; no external four-step schedule is provided. The selected event sequence will be proved rather than imposed.

## Theorem A — exact autonomous controller classification

For any integer m>=1 and fixed priority w, the selected events are w,w,w,..., because every group of four minimum-counter choices increases each counter by exactly one. For n=4l+j (0<=j<4),

M_n=(m+l)M_B + P_j(w),   P_j(w)=Σ_{i<j}E_{w_i}.

Consider the intended triad cycle S_0=012→S_1=024→S_2=124→S_0. The complete nine-neighbor score check at M_B has minimum strict score advantages (1,1,3); thus for every individual competitor V in the nine-neighbor set, Δ_B(S_i,V)>0. At n=12k+r, 0<=r<12, the desired winner's advantage over V is EXACTLY

Δ_{m,12k+r}(V) = Δ_{1,r}(V)+(m−1+3k)Δ_B(S_{r mod 3},V).

The equality is for each competitor, not necessarily for the minimum of several advantages (whose lower bound follows immediately). A complete check of 24 priorities × 12 residues × all eight competitors finds that at m=1 exactly 18 priorities preserve the unique desired successor at every n>=0. Their precise classification is w[0] != (0→1); all six others tie already at n=1. At m>=2 all 24 priority orders preserve the same unique cycle for all n>=0, by the same formula and the complete m=2 base check. At m=0 all 24 have a first-step V27 tie under the zero ledger. A representative winning priority (20,01,23,30) at m=1 gives minimum gap vector for r=0..11:
(1,1,3,1,2,7,2,2,9,3,3,8).

V17 shared-member slot inheritance along the proved cycle yields the odd holonomy (1,0,2) after three steps; after six it is the identity. Q=0 at every original primitive PASS.

## Theorem B — exact local rebalancing

For an arbitrary four-count nonnegative initial vector b=(b_e), let T=max b_e. The same current-Ω least-count selector reaches (T,T,T,T) after exactly N=4T−Σ b_e PASS events. Proof: while some count is below T, at least one minimum is below T, so the selector never increments an already-T count. At event N, every count <=T and their total is 4T, hence all equal T. If T>=1 and the triad is aligned to 012 at this synchronization, Theorem A applies from then on (for T=1 choose w[0]!=01). This does not assert automatic triad alignment from arbitrary initial active triads.

## Observer and evidence scope

On the B-only event submonoid, Ω along B recovers all event counters, controls future event choice and, using u=Ω1, preserves V27 score updates. Ordered V17 slots are carried separately; their history is not equated with event counts. Reverse PASS and inter-Cell TRANSFER are next-interface tests. No new physical heartbeat time, six-dimensional Cell move, multi-Cell network closure, or official theorem admission is asserted.

R647_VERIFY.py is a standard-library integer checker of all 24 priorities at m=0,1,2,3,7 for 120 primitive steps (14,400 scored states), 12-phase analytic inequalities, exact balancing examples, and V17 holonomy. The universal all-index conclusion uses the displayed individual-competitor linear identity plus the finite 24×12 base check.

Next research unit: introduce two typed X6 Cell identities, V29 TRANSFER and V28/V30 continuity/order rules; test whether Ω-only closure survives and construct a minimal stock/provenance repair if it fails.
