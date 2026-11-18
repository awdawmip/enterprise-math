# EC49FHA — exact 19-edge replacement budget, seven-key witness A

**Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

**Model:** Original 9-state BRC observer with 24 window/signature demands H2–H9; source witness A from EC49FGJ; native cost is the number of distinct nonempty **ordered signed six-axis microstep prefixes**, not terminal-coordinate cardinality. Original witness A has exactly seven complete raw cache keys and 94 native edges.

## New scoped theorem (2026-11-10)

Let Q be a five-element subset of the 24 demand labels, fix all 19 paths outside Q exactly as in EC49FGJ witness A, and suppose the fixed paths still exhibit all seven original cache keys. Denote their native prefix union by F(Q). For **every** such Q for which `93-|F(Q)|=19`, no five valid replacement paths using at most seven complete raw cache keys can reach cost 93 or less.

The finite domain contains **exactly 144** distinct choices of Q satisfying these hypotheses. Exhaustive exact-integer/bitset evaluation gives **zero feasible 93-edge completions**.

This improves the A-witness, non-key-release, five-path neighborhood audit beyond EC49FGZ, which covered budgets 16–18. The B-witness at budget 19, other budget groups and cache-key-release cases remain separate unfinished tests. The global seven-key minimum remains bounded above by 94, without a proved global lower bound of 94.

## Finite proof and exact algorithm

For each original prefix p, define its support set S(p) as the indices of paths containing p. The fixed background retains p iff S(p) is not contained in Q. Thus the exact 93-edge extension budget is

`B(Q)=93-|F(Q)| = #{p:S(p) ⊆ Q}-1`.

For each label i∈Q enumerate every legal BRC operation word w from the frozen finite observation model, filter to the seven keys already present in the 19 fixed paths, and compute its new native prefix set `D_Q(w)=P(w)\F(Q)`. A legal 93-edge completion exists exactly when five choices w_i have

`|⋃_{i∈Q} D_Q(w_i)| ≤ 19`.

The supplied verifier uses a complete catalog of **178850** legal observation words (of which **9838** use A's seven keys). It does not sample a subset of words. It creates an antichain of inclusion-minimal union bitsets after each demand. If X⊆Y then X∪Z⊆Y∪Z for every later choice Z, so removing the dominated state Y is exact. The empty-antichain decision is therefore a complete finite infeasibility certificate for each Q under the stated model.

The published program explicitly asserts the 144 positions and zero feasible completions; the actual local execution printed:

`EC49FHA_A_B19_EXACT_PASS: 144 positions, zero 93-edge completions`

The executed run produced a 33 KB per-position report with Q and candidate counts, locally packaged for handoff. The script regenerates its own report.

## Reproduction

Run `python VERIFY_EC49FHA.py` with the pre-existing sibling folders `EC49FGW_RADIUS5_EXACT_SCREENS_20261110/` and `EC49FGX_RADIUS5_PAIR_FIVE_DP_20261110/` on this research branch. This checker imports the previously published frozen legal-word generator and exact five-way union DP, rather than approximating path order or recoding the mathematical model.

Dependency refs: EC49FGJ original construction, EC49FGW observed catalog / 24 labels and EC49FGX exact DP, all on PR #1730. The locally executed original witness has the same 48 A/B labeled words as the GitHub EC49FGW reproduction witness; it is a different JSON serialization. Project formal Result/Driver approval is separate from this author-side exact finite audit.

**Next discriminating unit:** finish witness B at budget 19 and both witnesses at budgets 20–25; then tackle 4898 cache-key-release positions per witness. The underlying mother question remains whether seven keys admit 93 native edges.
