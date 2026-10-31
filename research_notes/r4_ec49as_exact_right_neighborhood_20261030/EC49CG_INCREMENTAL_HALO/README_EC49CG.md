# EC49CG — exact future-window BRC residual halos and K-orbit continuation

2026-10-31; author-side, portable, UNREVIEWED / NOT_ADMITTED. GLOBAL_KNOWLEDGE_V1 main@d171cc0e7df8db282f5eb9c40c67e55ce341488b; EM main@7a46ed70b59ca823805468daab0122ac0b230a20; predecessor EC49CF at ef ea1f2b7cc37f80dd7404b55d5eefc677f831b4 (remove space). Original native `signed_brc.py` Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176. Protected P000 and ACTIVE worldview unchanged.

## Scope
Ordered native X6 words in signed ±E1,...,±E6, relative displacement z∈Z^6, nine-state DFA detecting A=(+E1,+E2), B=(+E2,+E1), weighted BRC channels W0=(2,3,3,2,1,1), W1=(3,2,3,2,1,1) for positive steps and unit negative weights, plus exact word count. Four Boolean A/B atoms × three channels = 12 terminal observations. K=C2×C2 swaps (1 2) together with DFA A/B and channel W0/W1, and swaps (5 6). Length is combinatorial depth, not physical heartbeat time.

## Theorem 1 — finite-window halo and sharp spatial cutoff
For an arbitrary finite multiset of length-n paths, let F_n(z,q) hold the two integer BRC weights and count at exact displacement z and DFA state q. Let h≤H future signed steps be appended, either a fixed word or any sum of permitted words; only closed-endpoint 12-channel observations are requested. Then F_n restricted to ||z||₁≤H is exactly sufficient: an h-step suffix can return from z only if ||z||₁≤h, while DFA and all weights update from (z,q) and the appended steps. Thus deleted states contribute zero to every declared future output. For even n, allowed future lengths 0,2,...,2k, one may take H=2k, retaining the even displacement parity.

This support cutoff is sharp for the class of arbitrary prefix multisets. Every reachable z with ||z||₁≤H admits a suffix of length ||z||₁ with displacement −z; a singleton path at z versus an empty population yields different positive *count* after that suffix. For H=2k≤n even, a concrete boundary word is (+E3)^(2k)(+E4,−E4)^((n−2k)/2), then the return suffix (−E3)^(2k). This establishes necessity of endpoint *support*, **not** the minimal number of rational-linear coordinates or DFA states. No fixed finite H suffices for all arbitrarily long future suffixes.

## Theorem 2 — one cone computes several complete closed-return checkpoints
Start from the native empty word. To compute all closed-terminal observations at lengths N,N+2,...,N+2k for even N, iterate the exact signed-letter weighted transfer T up to N+2k. At depth t retain exactly states satisfying ||z||₁≤N+2k−t. The deleted states cannot close at final horizon or any earlier checkpoint, so every 12-coordinate terminal output at all listed lengths is unchanged (induction on T). K preserves ||z||₁, and EC49CF's stabilizer-aware integer orbit transfer is exactly equivariant, so the same proof applies to orbit representatives and preserves multiplicity and swapped channel coordinates. At depth N, the stored halo has radius 2k; at depth N+2 it has radius 2k−2. This is a **predeclared finite window**, not a promise to extend the halo indefinitely. Appending one fixed non-K-invariant suffix requires lifting the K-orbit representation or reducing the symmetry subgroup.

## Theorem 3 — exact six-axis reachable-orbit counts
Write f(x)=1+2x+2x²+...=(1+x)/(1−x). The reachable endpoints at depth n are D_n={z∈Z^6 : ||z||₁≤n and ||z||₁≡n (mod 2)}: shortest paths realize the norm; backtracking pairs fill the remaining even length. Define parity-restricted coefficient sums, for 0≤m≤n with m≡n mod 2:
N_n=Σ[x^m]f(x)^6, A_n=Σ[x^m]f(x²)f(x)^4, B_n=Σ[x^m]f(x²)^2 f(x)^2.
A_n counts endpoints fixed by one coordinate transposition, B_n by both. Burnside's orbit lemma gives |D_n/K|=(N_n+2A_n+B_n)/4. These are displacement support orbit counts, **not** complete DFA/DP state counts.

n=14: (N,A,B,orbits)=(528865,52879,4369,159748).
n=16: (1110049,97937,7153,328269).
n=18: (2149033,169651,11101,624859).
Fixed future radius H yields finitely many endpoint slots independent of n, but exact accumulated coefficients still have O(n) bits and the original computation is not constant cost.

## Executed exact evidence
The accompanying VERIFY_EC49CG.py uses the EC49CF integer transfer and native BRC kernel. Full unquotiented versus lifted K-orbit state equality was checked for every layer at n=0,2,4,6. Independent brute enumeration of the geometric D_n/K orbit count covers n=0,2,4. The single n=18 cone and separately computed fixed-horizon cones at n=14,16,18 agree exactly in all twelve integer terminal outputs. Independently the three channel totals agree with original native endpoint_weight and endpoint_multiplicity at each length.

Multi-horizon checkpoints at n14: radius4, 2737 orbit states; n16: radius2, 240; n18: radius0, 5. Whole-run peak: 50594 orbit states. Native (weighted return, count): n14=(76914770549760,748315668672), n16=(14233765517623080,72729762868620), n18=(2758828096749067200,7402621930738320). Full 12-terminal vectors are in EXACT_REPORT_EC49CG.json. Single-run exact test internal recurrence 7.057s vs 11.243s for three fixed cones. Two separate cold-process benchmarks: multi 7.97s / 134980 KiB RSS, three independent cones 12.17s / 134384 KiB RSS; the multi route is faster on this host, **not** lower peak memory. Neither is a cross-host performance bound.

Run `python VERIFY_EC49CG.py` and `python BENCH_EC49CG.py multi` / `fixed` in this directory. `native_signed_brc.py` is the project's previously published source at EC49CA_CRT, unchanged; if running here, copy it without edits from that adjacent path or the archived original Git Blob before executing. Finite tests do not prove infinite-horizon safety or physical dynamics.

## Literature and status
Ivan Z. Feng, "The Dual Burnside Process", Journal of Theoretical Probability 39, article 78 (published 2026-08-27), https://doi.org/10.1007/s10959-026-01539-9, proves symmetry lumpability for particular stochastic Markov kernels. It does not prove this positive, non-normalized multi-channel BRC halo, nor P000 physical claims; the general orbit machinery is not asserted as new.

Native service v0.6.11 reports research_authority_granted=false and executor_binding_configured=false. Active-owner inventory returned CONTROL_QUOTA; no verified native session, CLAIM, Result, Driver review or admission. This GitHub evidence is a PORTABLE_DRAFT and registration remains pending.

**Next EC49CH:** For a restricted future suffix language, derive the exact smaller set of allowed suffix displacements and DFA-distinguishable residuals, prove the associated factorization/descent certificate, and show a fixed non-equivariant suffix where K lifting is required. Compare against radius-H spatial halo and native integer terminal outputs.
