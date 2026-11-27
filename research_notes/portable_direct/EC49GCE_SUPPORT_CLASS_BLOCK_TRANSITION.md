# EC49GCE — Equal-support block transition and full cached-basis Pareto replay

Status: AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_ALL_BUDGET_REPLAY / NOT_REVIEWED.
Predecessors read at exact refs: GCD b0ad7ae5cf30db7f597c46834d9c6b0a9504395b:research_notes/portable_direct/EC49GCD_CACHED_BASIS_TIGHT_MASK_TRANSITION.md (blob 40ef88290fee827bfb984ad6760be043418c5d6c); GCC af221487dea117f2c4cab718e7c8f8b378a8cb8a:research_notes/portable_direct/EC49GCC_FINITE_SUFFIX_RANK_PROFILE.md (blob e51e035161cdf2885007f62cc5cc69b6f5baebec), its exact replay script blob ff83f25a0c1a6457c9ca0310e1829fee66df4270. Inherited historical science identifier BRC16943 unchanged; archive bytes and exact archive pin not re-read; no native physical result. This is a finite labeled strict-Hall auxiliary matroid.

## 1. Equal-support block rank transition

Let N=(M/S)|F be GCC's residual matroid on the fixed suffix of a finite strict-Hall labeled model with positive integer port capacities, S independent. Let H be all remaining labels with one identical nonempty support E. Write F'=F minus H. Every permutation of H fixing F' is an automorphism of N, since all original Hall cut counts depend on H only through the number selected. Let R subset H be a feasible choice of t labels (t<=r_N(H)). For any Q subset F', put a=r_N(Q), b=r_N(Q union H). Then
    r_{N/R}(Q) = min(a,b-t).
Proof: take a basis B of Q. Since B spans Q, r_N(B union H)=b. In the contraction N/B, H has rank b-a, and permutations of H preserve rank. Consequently its restriction to H is the uniform matroid of that rank: there is an independent subset of size b-a, all other subsets of the same cardinality are independent by permutation, and heredity handles smaller subsets. Hence r_N(Q union R)=a+min(t,b-a). The contraction identity subtracts t because R is independent. This proves the formula, including t=0, rank-zero blocks and Q empty. The same proof applies to any matroid with a freely permutable class; no claim that arbitrary similar labels are exchangeable.

For a new GCC coordinate W in the support-union closure of F', let Q=F'_W. Since W also belonged to the old closure, if E subset W, then Q union H=F_W and b is already stored; otherwise Q=F_W and a is already stored. Thus at most one new rank query per coordinate suffices to generate *every* feasible cardinality transition, not one query per cardinality. One extra query computes r_N(H) and excludes illegal block counts. For each t the new profile is g_t(W)=min(a_W,b_W-t). It reconstructs exactly every legal fixed-suffix labeled continuation by GCC. The thresholds b_W-a_W are the largest number of selected identical-support labels that do not reduce the corresponding future rank.

Extra consequence for a coordinate with E not contained in W: if B is a cached basis of Q, b-a=min(|H|, min_{V:E subset V}(g(V)-|B intersect F_V|)). Indeed adding k arbitrary labels from H to B increases precisely those quota counts by k, and B spans Q. This gives a single-scan way to obtain the missing addition rank. Not implemented in this replay; efficient grouped deletion of a class from a cached basis remains a next problem.

## 2. Exact objective compression without discarding labels

Each original label has either nonnegative retained value p and zero savings, or nonnegative retained auxiliary release-cost savings s and zero value, as in GCB/GBU. Within H let real and auxiliary lists be sorted by their respective positive weights decreasingly (fixed original label order breaks ties). For any choice of i real and j auxiliary labels, the two sorted prefixes of lengths i,j attain at least as much p and s, with exactly the same t=i+j. The permutation proof preserves the entire suffix language. Thus for each state it suffices to consider pairs (i,j) with i+j<=r_N(H), attaching their actual original labels. All budgets and at least one attaining witness are preserved under ordinary GCC/GCB Pareto dominance. No assumption that same-support labels have equal weights. If general labels carry both objective coordinates, independent sorting is not valid; a local Pareto frontier at each cardinality would be needed. This quotient does not preserve arbitrary observations of prefix history, all optimal witnesses, arbitrary additions outside F, or reverse deletions; raw label records remain available. Full joint support unions remain in the profile.

## 3. Full GCD integration

The code below uses GCD's tight-mask deletion and fundamental-circuit contraction inside the same GCC all-budget Pareto DP, keeping a cache basis per coordinate per retained state. For merging equal profiles, choose the winning original history and keep its own cache. Every retained state in all three algorithms is checked against direct strict-Hall greedy rank; cached bases also checked for subset membership, cardinality and original Hall feasibility. No changes to GCD theorem.

## 4. Executed exact replay

Same exact xorshift generator, seed 20261128, 350 models as GCC (2..7 ports, 5..12 labels; base capacities 1..4, incremented for each singleton auxiliary; values 1..15, savings 1..9). Greedy baseline reproduces GCC finite DP operation counts exactly. Cached algorithm uses same order and same canonical rank/objective dominance; grouped algorithm processes support groups in first occurrence order, with local sorted real/aux prefixes. Independent reference exhausts all 376960 original labeled subsets using original Hall inequalities. Every integer budget from zero through total auxiliary savings tested for each algorithm: 5096 budgets, 15288 optimal label witness checks; 69662 retained rank coordinate checks, 34179 grouped-transition rank checks, zero disagreements. 278 models had repeated support and largest class had eight labels.

Metric | greedy GCC | cached GCD | grouped GCE
---|---:|---:|---:
stage visits | 2995 | 2995 | 2146
generated states | 9809 | 9809 | 7160
retained states (cumulative) | 5266 | 5266 | 2986
peak states | 26 | 26 | 12
rank queries (new, excluding initial basis) | 24722 | 0 | 17564
greedy quota tests | 1319677 | 30809 | 979528
tight-mask visits | 0 | 333525 | 0
dominance comparisons | 5670 | 5670 | 1777
retained rank entries | 26977 | 26977 | 15708
nominal cumulative extra basis bits | 0 | 165863 | 0
observed instrumented elapsed ms | 342 | 317 | 504

Timings are a single Date.now aggregate in the JS tool isolate, include stage construction, state management and in-loop direct validation; grouped mode additionally checks every generated transition. They are not clean solver-only or stable performance benchmarks, and there is no measured heap-byte comparison. The operation counts differ in cost; cached 30809 singleton tests plus 333525 tight scans versus 1319677 greedy quota visits. Grouped cumulative states are 43.30% fewer than greedy, with 68.66% fewer pair comparisons, but different stage order/count. It is not an equal-stage dominance comparison. The grouped branch still uses greedy construction for rank pairs. Full cached and grouped integration into one algorithm and controlled timings/memory remain open.

Exact executed code: 74ed2cc838161931876877645a2ce548caa82765:research_artifacts/portable_direct/EC49GCE/grouped_cached_replay.js (blob 264ea3aea07c2252bfd3e4b77fa986d7e5ee5157).
Exact output: 5ceacc719f1e5d55e3daf2d8efe291784b88dd9c:research_artifacts/portable_direct/EC49GCE/replay_output.json (blob 4fb9a8335ff97f7b908b3963f121e05cf16dadae).
Both immutable files fetched and content matched.

## 5. Frontier and provenance

Next: implement the single-scan outside-support rank pair and efficient grouped deletion; combine both accelerators, benchmark without verification in the timed region with repeat runs and actual heap measurement where available, then locate the original exact BRC16943 archive and measure its support multiplicity distribution before any frozen claim. Fourth layer next root 2046 and historical M14 interval [25,27] inherited, not replayed.

Current global canonical snapshot 5d8cadd77b805f57a22c7db9f980c0eb2ea39468 with both entry blobs verified identical (25ae05640c7920104820dba91a1df5e9fafca25e,108cd58e0458070b5f1a8171d2f66c8c3d0aa613); current research entry, P000 global V4 and Source V5, ACTIVE worldview, residual fidelity, joint preservation, portable, research method and evidence policies read. Current control c13b29b6f48d6ac6f78cf873c97280eb131a5375. em_status authenticated transport but did not grant research authority. Exact task lookup r4-20261128-0731-ec49as-read SUCCEEDED at this Source with NO_CANONICAL_PUBLICATION_DIRECTORY for RS-EC49AS; native operational owner projection not evaluated. Historical EM-DIRECT-23537B provenance not adopted as current private identity. Independent informed portable research; no shared CLAIM, substitute identity, task publication, Result/Review or promotion. Activity association pending. No change to P000, frozen inputs, sharing or scheduling.
