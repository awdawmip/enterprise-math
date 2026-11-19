# R762FP — Partial triad-incidence gates are themselves future-observer information

Date: 2026-11-19 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_ENUMERATION_PASS / NOT_REVIEWED.
Mother Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`.
Frozen scientific taskbook: `awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md`.
Frozen P000 source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Current rules: `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`.
Direct antecedent: R762FO (PR #2785, commit `a38211262314394b7f42cdacf117cb9a4f03b251`).
Researcher role this run: independent portable research; native CLAIM/owner authority NOT CONFIRMED by the queued current continuation request.

## Question and exactly typed construction

R762FO proves a graph-ball formula for reversible source-pair swaps on **every** pair of permutations. Its proof treats each proposed swap as a total operation. Actual native Cell/Link/Port licenses may make an operation unavailable for some source-incidence configurations. Can a restriction to legal triads be analyzed without losing the information carried by operation availability?

Fix three distinct signed native X6 axes within a declared three-axis slice of the full six-dimensional Cell substrate. On each axis let there be k *named* positive source tokens `A_i,B_j,C_l`. A grouping history is `s=(sigma,tau) in S_k x S_k`, representing k candidate three-source events `(A_i,B_{sigma(i)},C_{tau(i)})`. A fixed binary tensor `M[i,j,l]` declares a **candidate combinatorial incidence license**; the legal history set is
`L_M={s: M[i,sigma(i),tau(i)]=1 for all i}`. The tensor is a proposed typed admissibility input, not evidence of native X6 permission.

This uses the positive, provenance-retaining BRC branch algebra: the coefficient
`[x_1...x_k y_1...y_k] prod_i (sum_{j,l:M[i,j,l]=1} x_j y_l e_{i,j,l})`
in `N[e_{i,j,l}]` is the sum of distinct named monomials for precisely the legal histories. Forgetting all `e` labels and retaining only the total positive coefficient returns `|L_M|`, but discards which source triple belongs to which event. There is no signed cancellation or Euclidean force-vector premise.

Let G be a simple graph on the A-row slots and a its visible root. A proposed swap `U_{uv}` exchanges the **complete** B/C partner pairs attached to rows u and v. This swap is enabled at state s exactly when `U_{uv}(s) in L_M`; otherwise it reports `BLOCK`. Enabled swaps are involutions. A successful known sequence starting from s yields the named root pair `Q_a(s)=(sigma(a),tau(a))`. Every finite-word experiment starts from a fresh copy of the same initial s; an attempted word that encounters a disabled operation returns the observable `BLOCK` marker. Failure is an observed gate result, not a silent state change.

Define `s ~_h t` if the complete outputs of **every known word** of length <=h coincide, including `BLOCK`; the empty word reads the present Q. The full observation map and the admissibility-conditioned operations are fixed. No physical time or native clock is inferred from word length.

## Theorem 1 — Exact finite-horizon quotient by transition refinement

For every finite k>=1, every binary incidence tensor M with nonempty L_M, every G, root a and h>=0, define recursively

`E_0(s)=Q_a(s)`

`E_{h+1}(s)=(Q_a(s), ( E_h(U_e(s)) if U_e(s) in L_M else BLOCK )_{e in E(G)})`,

with a **fixed canonical ordering** of edges. Then

`E_h(s)=E_h(t) iff s ~_h t`.

Thus the exact number of distinguishable histories is
`N_h=|{E_h(s):s in L_M}|`,
the exact fiber size for signature z is `F_h(z)=|{s:E_h(s)=z}|`, and the minimal extra fixed-length source-relation code that reproduces all declared horizon-h experiments is

`b_h=ceil(log_2 N_h)` bits.

The fiber sizes need **not** be uniform. Once `E_h` stabilizes as a partition it remains stable, and stabilization occurs by `h<=|L_M|-1`. A finite exact checker can compute the sharp horizon-specific code without enumerating exponentially many future words: each refinement inspects at most `|E(G)|*|L_M|` transitions, plus canonical grouping cost.

**Proof.** For h=0 both observations equal Q. Each word of length <=h+1 is empty, or consists of an initial edge e followed by a word of length <=h. An initial illegal e returns the same sentinel BLOCK for all its extensions; an enabled e produces exactly the h-horizon response family from U_e(s). Induction proves the recursive signature equivalence. Any lossless fixed-length representation distinguishes N_h inequivalent signatures, requiring ceil(log2 N_h) bits; a canonical integer index realizes this bound. The partitions refine monotonically because the current Q and all shorter experiments remain observed. If a refinement fails to split any class, the resulting equivalence is stable under every observable partial successor, so no later refinement can split it. At most |L_M|-1 strict splits can occur, proving the finite stabilization bound. QED.

## Theorem 2 — Precise condition for using the R762FO graph-ball reduction

If the proposed operations are *total on L_M*, i.e. `U_e(L_M)=L_M` for every graph edge e, then no BLOCK outcome can arise. Under the same resettable known-word observer, `s~_h t` exactly when the two partner-pair assignments agree for all rows within graph distance <=h from a.

**Proof.** Every edge word is executable and moves original labelled row-pairs by a slot permutation. One observation after <=h swaps can reach only an original row within distance h; conversely a shortest path from a to any such row transports that row to a. Hence the complete response family is equivalent to reading those rows, as in R762FO. QED.

The restriction to L_M changes the *set of realizable row restrictions* and generally the fiber sizes; the unrestricted formula `(k!/(k-r_h)!)^2` and uniform fibers `((k-r_h)!)^2` are recovered for the full population `L_M=S_k x S_k`. The theorem makes no claim that an actual native license is total.

## Sharp counterexample — a remote gate reveals hidden provenance

Take k=3, root A1, graph containing **only** the edge A2--A3. Let the allowed triples (1-indexed) be:

`(1,1,1), (2,2,2), (2,3,3), (2,2,3), (3,3,3), (3,2,2), (3,3,2)`.

The exactly three legal histories are

`H0=[(1,1),(2,2),(3,3)]`,
`H1=[(1,1),(2,3),(3,2)]`,
`H2=[(1,1),(3,3),(2,2)]`.

Every history has root observation (B1,C1). At h=0 the unique observation class has fiber 3. At h=1, the remote swap A2--A3 is enabled for H0 and H2 (which exchange), but is blocked for H1, because its exchanged A2 row would be (B3,C2), an excluded triple. Therefore there are **two** observable classes, of fiber sizes 2 and 1. They remain the two classes at every later horizon. The R762FO graph ball is always `{A1}` and predicts no new root-pair labels; **permission visibility makes the hidden class distinguishable even though the swapped edge is disconnected from the visible port**.

Consequently the h=1 minimal memory here is 1 bit, rather than zero. A BRC representation retaining only the common root pair (or the total positive mass 3) is insufficient for the declared gate-aware observer. This is a concrete structure-residual witness, not a physical-force measurement.

## Verification, limits and next exact problem

`R762FP_VERIFY.mjs` runs without dependencies: (1) all simple graphs and roots for k=1..4 on the unrestricted population, checking the R762FO graph-ball count and uniform fiber formula across 1105 graph/root/horizon cases and 592449 history-signature comparisons; (2) the complete 3-history remote-gate counterexample at horizons 0..3; (3) twelve deterministic sampled k=3 incidence tensors, all eight simple graphs, all roots and horizons 0..3, comparing 1152 partition cases with an **independent enumeration of every known experiment word**, for 26400 pairs of history signatures. Result: PASS. This is exhaustive over unrestricted graphs k<=4, not exhaustive over all ternary incidence tensors. General results above are proved by induction, independent of finite enumeration. Independent mathematical review: NOT_REVIEWED.

Next: extract the *actual* permitted native Cell/Link/Port triad-incidence updates from frozen source and deployed current contract. Check whether enable/disable itself is observable, whether experiments can reset the same initial state, and whether candidate swaps preserve P000 signed axes, path provenance and triadic closure. If the physical operation is irreversible or unresettable, define the causal single-run observer and recompute its exact partition. Continue the independent positive-BRC provenance research without treating this candidate M tensor as native authorization.
