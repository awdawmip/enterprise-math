# PREFIX-509 — Index-free exact V-rank from the BRC mod-6 compiler

Date: 2026-11-05 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Author-side independent work, no formal CLAIM. Scientific freeze: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Current normative rules separately loaded from the canonical main entries. Direct predecessor: PREFIX-508; global index construction: PREFIX-501–503.

## Theorem and exact observer

The parent is native six-spatial-axis X6. This theorem studies its *declared five-axis restricted path family* (sixth signed axis unused). Each ordered native signed path has length n≥0, chart displacement y=(y_a,y_b,y_c,y_d,y_e), cancellation observables V=p_b+2p_d+p_e and W=p_c+p_e, and controller (q,t). Here q is the terminal prefix automaton state for g∈{aab,aba}; t∈{N,B,C} records the first b/B or c/C source, if any. We rank distinct observer states, not paths with multiplicity.

Fix n,y,W with m=(n−Σ|y_i|)/2 a nonnegative integer. Let C_g(V)=C_g(n,y,V,W) be the finite set of reachable (q,t) at V, where 0≤V≤2m. Use a fixed common lexicographic order within each fiber. PREFIX-508 explicitly compiles the exact aggregate
[
F_g(L,H)=\sum_{v=L}^{H}|C_g(v)|
]
as a finite union of mod-6 interval components with a gate-dependent *constant* number of exact integer operations per query. In the following complexity claims that published fixed-template compiler is the numerical oracle; no physical rotation/dynamics operator is invoked.

**Theorem.** The map
[
R_g(V,q,t)=F_g(0,V-1)+\operatorname{ord}_{C_g(V)}(q,t)
]
is an exact gapless bijection between all reachable states of this row and `[0,F_g(0,2m)-1]`. Given an integer r in this range, choose the **least** V∈[0,2m] with F_g(0,V)>r, and let t0=r−F_g(0,V−1). The t0-th ordered member of C_g(V) is the inverse output. In the exact-integer arithmetic-operation model, the rank takes O(1) operations and O(1) query workspace, while inverse rank takes O(log(n+2)) operations and O(1) query workspace. No V-block table, V-prefix table, or enumeration of all V values is needed.

**Proof.** The fibers indexed by V are disjoint. Their ordered concatenation yields consecutive intervals `[F_g(0,V-1),F_g(0,V)-1]`; an empty fiber contributes an empty interval. The ordinal is injective on its fiber, and disjoint intervals ensure global injectivity. Every rank in `[0,F_g(0,2m)-1]` lies in a nonempty fiber; strict comparison `F_g(0,V)>r` selects its first upper boundary, including across missing/zero-support V slots. The subtraction returns exactly the fiber ordinal, proving surjectivity and the inverse. The finite-template compiler and finite automaton yield the stated operation counts. n=0 and zero-support intermediate V are included. QED.

## W-prefix consequence and end-to-end resource construction

Reuse PREFIX-501/502 signed-coordinate symmetry and PREFIX-503's outer quotient key p=(u,v,c,s)=(y_a,y_b,|y_c|,|y_d|+|y_e|). For each p,W the total row support is **one** compiled aggregate F_g(0,2m). Let `H_p(j)=Σ_{W<j}F_g(0,2m)`. Combine the previously proved signed-coordinate outer prefix with `H_p(W)+R_g(V,q,t)`. For inversion, find W by a strict prefix binary search, then invert V as in the theorem. Reusing those proved outer layouts yields a **fixed-length** exact global index of O((n+1)^5) shared integer cells, O((n+1)^5) constant-template row-aggregate constructions, O(1) online arithmetic operations for full rank and O(log(n+2)) for full inverse rank. The earlier O((n+1)^6) individual V-support oracle calls used to build PREFIX-503's W totals are replaced by row aggregates. Actual constant factors depend on the fixed suffix/mod-6 compiler. Integers, including rank offsets, use O(log(n+2)+log S_g(n)) bits; bit complexity and multi-length prebuilding are accounted for separately.

Given a decoded observer and an appended native signed direction, update the signed displacement and corresponding V/W cancellation increments, update KMP q and first-source t, then apply this theorem at length n+1. Full global re-encoding uses the separate index for n+1, if prebuilt. This operation is for the declared path observer, preserving the source and order information relevant to the specified future append operation.

## Exact computed certificate (local execution)

The executable Python 3 source `prefix509_direct_rank_certificate.py` reuses the published `prefix508_mod6_compiler.py`. Against an *independent ordered ten-signed-direction native dynamic program*, it checks all (y,W) rows for n=0..6 and deterministic uniformly spaced row samples for n=7,8, for both aab and aba. The exact per-V reachable (q,t) sets, ranks, inverse ranks and all inclusive V-interval F/T sums match their independent native reference. This is **5,568 checked rows per gate**, **17,947 / 17,931 rank-inverse states** for aab/aba, and **51,788 F/T interval checks per gate**. A separate 2,550 native signed-direction append/reencode probes per gate independently replay the complete path and verify the updated rank. Long-row probes at n=16,32,64,128,256 compare exact expanded point sums and aggregate moments. All executed assertions passed: `ALL_CHECKS_PASS`.

The separately executed `prefix509_moment_block_integration.py` verifies the identity C(i,j)=T(i,j−1)−iF(i,j−1) against PREFIX-506 minimum-block Monge optimization and an independent native model. It checks 1,185 quotient rows per gate, 5,093 block costs per gate and 7,112 exhaustive minimum-block instances across both gates. This allows optional adaptive block layouts to be built directly from compiled interval moments, but they are not necessary for the row-ranking theorem.

Proof scope: the stated frozen five-axis path observer and its declared append operation. Independent mathematical review and admission remain open. No physical rotation law or full native six-axis evolution is promoted by this combinatorial encoding result.

## Next scientific question: PREFIX-510

Develop a second exact aggregate over W to replace or compress PREFIX-503's O(n^5) W-prefix table. Start with a small explicit (W,V) feasibility/polyhedral family under PREFIX-508's fixed suffix/first-source cases, prove any proposed constant-modulus 2D count decomposition or give a genuine witness of its failure, then benchmark eager/demand compiled index costs. Preserve P000, world/axis identity, task freeze and formal owner gates.

Sources: canonical global `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, P000 and ACTIVE worldview; current project `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `research_priorities/research_method.json`; original PREFIX-501/502/503/508 notes and the frozen science pin above.