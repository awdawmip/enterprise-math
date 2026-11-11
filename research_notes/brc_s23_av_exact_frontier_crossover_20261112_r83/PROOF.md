# R83 — Equal-obligation crossover of ephemeral class heap and persistent winner AVL

Date: 2026-11-12. Author-side auxiliary rational circular-source model ONLY. Scientific pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34` unchanged. Prior exact sources: R75 `686010c8256b83123511593f3480e581352ddee9`; R76 `352abbd17c31f146e08a77d0caa8afeb74797389`; R82 `731f9ca14e596d15f29e75ed3a89a2e0b043b65e`. Not native BRC, formal CLAIM, Result, independent Review or Foundation.

## Common decision problem

A finite set of independently identified sources (integer time t, branch) is observed at integer j, rational x, reduced anchor theta0=p/q and rational closed interval I=[L,U]. Original integer labels a,b define the directed half-open circular target arc. Return the latest source time for **every real theta in I** (STABLE/ STABLE_NONE) or, in the general algorithm, actual rational CHANGE witnesses. R75-style ephemeral heap builds a heap from each phase class maximum at query time. R76-style persistent AVL keeps those maxima as an immutable height-balanced map updated alongside sources; a query popmax uses path copying. Both query routes apply the same exact R71 group exclusion and R74 per-source classifier. This benchmark covers the certified stable subfamily and does NOT test general CHANGES witness recovery.

## Structural theorem (comparison model)

Let g be the current number of nonempty phase groups and v the classes actually visited in one query, with one distinct time per group in the benchmark. Under standard binary heapify+pop, the query frontier costs O(g+v log(g+1)) comparisons; a premaintained AVL winner frontier costs O(v log(g+1)) comparisons plus O(log(g+1)) path-copy maintenance per effective update changing a maximum. With U such updates and Q queries, their respective *frontier-only* operation models are

- R75: O(Q g + Q v log(g+1))
- R76: O(U log(g+1) + Q v log(g+1)).

All exact rational predicate work, input construction and common source/group/GCD indexing remain outside these expressions. This is not a complete integer-bit complexity or full R82 three-index bound. When every class is excluded, **both specified algorithms** necessarily perform g exact class checks, so saving heapify alone need not speed up that workload. It is not an information-theoretic lower bound on alternative globally cached certificates.

For actual per-update times M_H,M_P and matched query times H,P, the total time inequality favoring the persistent index on a fixed workload is exactly Q(H-P)>U(M_P-M_H). A measured adaptive choice, not universal speedup, is justified.

## Infinite complete-interval witness families

For each integer g>=1 set q=g+3, theta0=1/q, I=[theta0,theta0+1/(1000 q^2)], j=x=0, a=1,b=2. For r=3,...,q-1 create one source t=q+r, branch r, residue r modulo q. For theta=theta0+delta with 0<=delta<=1/(1000q^2), the source phase equals r/q+(q+r)delta, lying above the target upper endpoint 2theta and below 1. The R71 exact closed-envelope exclusion therefore succeeds for all g groups and all real theta in I. This is ALL_EXCLUDED; latest source is NONE, and both algorithms visit g groups.

For EARLY_WINNER additionally insert t*=3q+1, branch 1 (residue 1). It is greatest; its source phase is 1/q+(3q+1)delta, always in [theta,2theta), including the lower boundary at theta0. It never wraps. Hence latest time equals t* for every real theta in I, and both specified algorithms visit precisely one class. These proofs rely on strict rational inequalities, not on sampling.

## Executed validation

Local Python `check_r83.py` uses `fractions.Fraction`, integer floor/ceil, exact R71 group certificates, exact interval endpoint checks for ALL_IN, and AVL height/balance validation. All six g x scenario combinations passed; each received four extra rational point probes as secondary checks. Single-machine CPython perf_counter_ns medians, 16 repeats at 32/128 groups and 8 at 512. Heapq is C-backed whereas the AVL is pure Python. These results are illustrative, not cross-language hardware benchmarks.

| g | scenario | heap median ns | persistent AVL median ns | index-build AVL node constructions |
|---:|---|---:|---:|---:|
|32|EARLY_WINNER|29223|30205|222|
|32|ALL_EXCLUDED|487842|586904|213|
|128|EARLY_WINNER|37045|30890|1148|
|128|ALL_EXCLUDED|2089756|2393822|1137|
|512|EARLY_WINNER|66473|31892|5626|
|512|ALL_EXCLUDED|8580834|10657456|5613|

At g=512, EARLY_WINNER was ~2.08 times faster in the persistent AVL implementation; ALL_EXCLUDED was ~1.24 times faster with the ephemeral heap. Allocations count constructions (including path copies), not peak live bytes. All-real correctness comes from the displayed exact certificates, not timing or four-point probes. The executed full local checker and raw verification JSON remain in the R83 companion research bundle. The repository report preserves all scientific parameters.

## R84 continuation

Reproduce **full** R82 three-index updates versus R75 within matched general all-real latest-source obligations; count GCD and Fraction integer-bit work; compare update/query ratios, transient and retained historic nodes, branch updates, changing label arcs, multi-time classes, certificate misses and CHANGES witnesses. Do not transfer this auxiliary model to native X6/BRC without an explicit typed bridge.