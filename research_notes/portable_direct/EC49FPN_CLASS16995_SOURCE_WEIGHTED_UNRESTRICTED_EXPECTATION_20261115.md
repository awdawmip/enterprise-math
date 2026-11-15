# EC49FPN — Exact source-configuration-weighted optimal BRC terminal sensing, class 16995

Date: 2026-11-15. **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.** Continuation of [EC49FPM and EC49FPL](https://github.com/awdawmip/enterprise-math/pull/2479), without changing the scientific model.

## Exact input and new prior

Keep pinned native source `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` with original corpus SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e` and original native rooted-cost table SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. The complete original legal-root-domain containing configuration16995 has **242 source configurations, 112 distinct named-root cost profiles, and 324 legal complete-allocation terminal scalar queries**. The native byte Trie, named roots, optional-demand assignments and terminal sum semantics remain unchanged.

**Changed statistical condition:** Give each of the original **242 source configurations** probability `1/242`. The target remains identification of its **named-root cost profile**, not identification of the raw configuration ID. Two source configurations with equal rooted P-profile cannot be told apart by any of these terminal observations; aggregate their prior weight rather than deleting their multiplicity. Since this original class has terminal-profile equality iff rooted-profile equality, 112 profile weights `w_i` (positive integers, sum 242) faithfully represent the original 242-point prior.

## Theorem: unrestricted globally optimal expected terminal probes

For unit-cost exact terminal scalar observations and deterministic adaptive query choice, allowing **any finite worst-case depth**, the exact minimum expected number of terminal observations under this 242-configuration prior is

\[
\boxed{\inf_{\mathcal T}\mathbb E_{\mathrm{source}}[N(\mathcal T)]
=\frac{641}{242}\approx2.648760330578512.}
\]

The **only minimizing first-query indices** among the original 324 legal terminal queries are **150, 209, 290, 312** (zero-indexed frozen action enumeration). A complete constructive decision tree beginning with `T(150)` distinguishes all 112 rooted states, and its **242 original configurations** are distributed by leaf depth as `{1:12, 2:138, 3:15, 4:77}`. The exact sum is `12+2·138+3·15+4·77=641`; worst-case depth is **4**.

This is a genuine prior-sensitivity result. With prior uniform over the 112 *distinct* rooted profiles (EC49FPM), the unrestricted optimum was `238/112=119/56`, and its six optimal first-query indices were `118,119,124,201,203,204`. Under the source-config prior, all four optimal first indices are different. The two fractions describe different declared probability spaces over exactly the same original finite native BRC observations.

## Exact proof and finite verification

For any nonempty set `S` of distinct rooted profiles, let `W(S)=Σ_{i∈S}w_i`. For a legal terminal query q let `F_q(S)` be its equal-exact-integer-response fibers. Define the optimal weighted sum of future query lengths:

\[
C_w(S)=
\begin{cases}
0,& |S|\le 1,\\
W(S)+\min_{q:,|F_q(S)|>1}\sum_{G\in F_q(S)} C_w(G),&|S|>1.
\end{cases}
\]

Every informative q partitions S into strictly smaller subsets. This is a well-founded exact recursion over the original complete 324-query menu, so induction on |S| gives the unrestricted optimum; its first-query cost under the original 242-point population is `242+Σ_{G}C_w(G)`. Exact integer DP enumerates every first query, resulting in minimum **641** and optimal indices **150,209,290,312**.

The DP may safely initialize each subproblem with `4·W(S)`: the previously certified depth-four decision tree (EC49FPL) for the entire 112-state set, restricted to S, provides a valid depth-≤4 solution under any nonnegative weights. A candidate query is skipped only if its lower bound `W(S)+Σ_{|G|>1}W(G)` already meets that feasible upper bound, or if it is uninformative or duplicates an identical response partition. Each nonsingleton fiber necessarily needs at least one more query per possible underlying configuration. None of these prunings alters the minimum, and **no worst-depth constraint** is imposed on the new weighted search.

Rebuild all native rooted/terminal data from the complete frozen original master; take exact multiplicities of each distinct terminal/rooted profile among the **242 original configurations**; recompute the 112 positive integer weights; evaluate the weighted Bellman recurrence and every legal initial query; generate the complete exact-response tree; traverse the 112 distinct rooted profiles and verify uniqueness of each path and its source-configuration-weighted cost. The standard-library executable `VERIFY_EC49FPN.py` performs this check after executing the predecessor frozen-input/hash verifier `VERIFY_EC49FPL.py`. A local exact run passed `EC49FPN_SOURCE_WEIGHTED_PASS 641 242 [150, 209, 290, 312]` with 20,692 cached weighted subproblems.

The complete 324-query cost array, all profile weights, an explicit 112-leaf optimal tree and its weighted depth histogram are in the generated machine certificate; original frozen inputs and run log are held in the comprehensive handoff archive.

## Scope and next frontier

Original625 legal-root-domain classification stays at **565 classified / 60 remaining**; EC49FPN advances the exact optimal observation economics within the already classified class16995. Scientific result is finite, original native BRC, terminal-only, integer exact, source-config-uniform prior and unit observation costs; independent mathematical review remains pending. Portable GitHub research is not a formal shared Task/CLAIM/Result. `RS-EC49AS` current exact lookup (2026-11-15T05:34:48.950537Z) returned `NO_CANONICAL_PUBLICATION_DIRECTORY`.

Next: characterize observer choice as root/terminal query costs vary, solve mixed-observer weighted expectation, and search the 60 remaining original native legal-root classes.
