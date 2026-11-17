# R5 fifth noise chamber — exact adaptive cost with four unmarked errors

**Theorem (f=4).** For the frozen derived scalar integer observer with 256 named closure masks, all 101 integer query budgets k=214,...,314, at most four arbitrary unmarked corrupted readings, and normal real observations satisfying |y-N_h(k)|≤η, put τ=2η and

- L=25845652773852463277015040000
- U=58182461585441404127941754880.

For **all real L≤τ<U**, the minimum over finite adaptive policies of the worst-case sum of query budgets is exactly

\[
\boxed{C^*_4(\eta)=4535.}
\]

Frozen scientific source commit: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`. Source-derived full 256×101 count table has SHA-256 \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\`. This is a result for the *derived* integer count observer, not a new assertion about native P000 geometry.

## Exact proof

**Lower:** restrict the true state to the five actual masks H=(18,24,82,34,17), keep all 101 possible physical query budgets, and evaluate at τ=L. Exhaustive integer Bellman recursion with four unmarked-error allowances returns **4535**, visiting **4,321** memoized nonterminal states. A state restriction can only simplify identification, while increasing the noise bound cannot improve guaranteed decoding. Thus C*_4(τ)≥4535 for τ≥L.

**Upper:** retain **all 256 states**, but permit only the five physical budgets \`216,223,296,214,215\`. At the threshold τ=U−1, the exact Bellman solver returns **4535**, with **18,193,706** memoized nonterminal states and five distinct action families. The resulting recursive minimizers define a terminating adaptive policy for all real τ<U: all count centers and gaps are integral, so any normal-support family at τ<U is a subset of the support possibilities at U−1. Thus C*_4(τ)≤4535. Lower and upper match throughout the chamber.

**Recurrence and exhaustive coverage.** Let S=(S_0,...,S_4) track disjoint sets of true masks consistent with the transcript using exactly j corrupted answers, with states requiring over four dropped. Every maximal normal-answer support A for query k is the set of centers falling into an interval of length τ; all such maximal sets are enumerated from the distinct integer centers. Successors are

\[
S'_0=S_0\cap A,\qquad S'_j=(S_j\cap A)\cup(S_{j-1}\setminus A),\quad j=1,\ldots,4.
\]

With V(S)=0 when the union of the tiers contains at most one mask, the exact worst-case optimal decision value is

\[
V(S)=\min_k\left(k+\max_A V(S'(k,A))\right).
\]

Actions admitting a zero-progress answer S'=S cannot occur in a finite minimum-cost policy. Maximal supports suffice because an answer having a smaller compatible set can only be easier for the decoder. The implementation uses 256-bit support masks and exact integer operations. The lower computation enumerates all 101 k on five actual states; the upper checks all branch answers on five genuine physical k over all 256 states.

## Reproduction and actual execution

- Frozen count table SHA-256: \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\`.
- Generate maximal U−1 normal-support masks from the frozen exact count table for budgets \`216,223,296,214,215\`. Generated compact action file SHA-256: \`091d7f80f6cb7b0983fb2a3659c4e9a334d53d99746b5523c24cdc9a138b0925\`.
- Compile the C++ exact Bellman solver with \`g++ -O3 -std=c++17\`. Actual output: \`EXACT_F4_COST=4535 MEMO_STATES=18193706 ACTION_COUNT=5\`.
- Actual C++ solver source SHA-256: \`872d86c714e1bb7186f376374e2fdd66fce26180cd526ef88c21c1fcb0d48632\`.
- Regression with four tiers (three errors) reproduces the earlier exact result \`3585\`, with \`1,704,343\` nonterminal states.
- Lower five-state f=4=4535 and f=5=5485 were separately recomputed using standard-library Python and exact integers.
- A scoped finite search checked all 251 six-state one-element extensions of H plus a fixed-seed sample of 160 seven-state extensions; none raised the 4535 lower. The full-256 upper computation, not these sample searches, establishes the theorem.

The reproducible package contains exact count input, Python generator, C++ source and compiler replay, lower checker, logs, result JSON and SHA-256 manifest. The scientific evidence is **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. The research branch publication is not a formal Task/CLAIM/Result/Review.

## Next

The exact sequence in this chamber is now \`C*_f=735+950f\` for \`f=0,1,2,3,4\`. Determine f=5 for all 256 masks: current five-state lower bound is 5485, previously available general construction upper bound is 5490. Explore an analytic universal-f recurrence or an explicit first counterexample. The previously proved eight-budget uniform domination theorem remains valid for arbitrary finite f; the present five budgets are only a sufficient f=4 policy alphabet.
