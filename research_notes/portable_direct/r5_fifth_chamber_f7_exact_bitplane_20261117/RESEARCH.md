# R5 fifth-chamber adaptive unmarked-error tomography: seven corruptions

Source: frozen scientific pin 435e77af0d180eac32bd1f9c4c464bc4010b7551; original exact integer observer table SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Continuation of Draft PR #2427 (prior f=0,...,6 exact).

## Theorem (AUTHOR_PROVED, EXACT_FINITE_CHECKED, NOT_REVIEWED)

In the frozen derived model there are 256 named hypotheses h and 101 legal integer-cost queries k=214,...,314, each returning an integer center N_h(k). An uncorrupted real response y obeys |y-N_h(k)| <= eta, while at most seven responses can be arbitrary, unmarked errors. Finite adaptive decision trees minimize worst-case sum of physical query costs.

For every real tau=2 eta with 25845652773852463277015040000 <= tau < 58182461585441404127941754880, the exact minimax value is C*_7(tau)=7385. Together with the prior verified f=0,...,6 results, C*_f(tau)=735+950f holds for each integer 0<=f<=7 in this chamber.

## Lower certificate

At tau=L restrict to the five actual named masks (18,24,82,34,17) and allow *all 101 query budgets*. The exact integer Bellman minimax recurrence in VERIFY_R5_FIVE_STATE_LOWER.py (already saved in preceding PR #2427 work) returns 7385 with 32,379 cached states for f=7. Restricting hypotheses weakens the adversary, and increasing tau only makes identification harder. Hence all 256-state problems throughout the interval require >=7385.

## Upper certificate

At the integer endpoint tau=U-1, retain *all 256* named masks. Enumerate all inclusion-maximal normal-response supports for the five admissible physical budgets (296,223,216,215,214). Their source action-file SHA-256 is e7af68961ab468ef8af90d6976a35435c71b8f27bacb0a67fd1d96dde0c182ac. Every real response support lies inside a maximal one; the decoder's feasibility is monotone under shrinking a support, so checking maximal supports suffices.

For a fixed transcript, each named hypothesis h has one mismatch count ell_h in 0,...,7, or is eliminated. A response support A increments ell_h exactly for h not in A, eliminating it at count 8. The previous eight mutually disjoint 256-bit tier masks can therefore be encoded losslessly by four 256-bit bitplanes, one binary digit per mask. At f=7, bit pattern 1000 means eliminated. The precise bit-sliced update increments active hypotheses only, by XOR carry. This is a scoped representation bijection for the derived scalar observer, not an erasure of native X6/provenance state.

The complete C++17 exact bounded-cost Bellman solver is in VERIFY_R5_F7_BITPLANE.cpp. It uses full collision-checked keys, monotone winning/losing cost thresholds, and tests OR over queries / AND over each maximal possible answer, with a strictly decreased remaining budget for each recursive step. Terminal success is reached only when at most one named hypothesis remains. The actual compiled and executed run at budget 7385 returned:

    EXACT_R5_BITPLANE f=7 feasible=YES budget=7385 memo=17308349 decisions=29792843
    ELAPSED=129.87 SEC RSS_KB=2898412

Since integer differences at tau<U are bounded by supports at tau=U-1, this strategy covers the entire half-open real interval; upper 7385 meets lower 7385.

## Reproducibility and crosschecks

- Frozen count input: 101 x 256 = 25,856 exact integer entries, table SHA-256 above; no floating-point arithmetic in the Bellman calculations.
- Exact five-mask all-101 lower: f=7 -> 7385, memo=32379.
- Original full 256-state action family consists of all 5 legal query support partitions at tau=U-1; action-file SHA-256 above.
- C++ f=6 regression: budget 6435 feasible YES, memo 5,539,141 and decisions 9,043,443, exactly matching preceding eight-layer solver.
- Deterministic Python bitplane/disjoint-tier equivalence regression: 136,000 response transitions across f=0,...,7, seed 20261117, PASS_BITPLANE_LAYER_EQUIVALENCE.
- The source code, f7 output JSON, and complete execution evidence are supplied in this directory and in the locally assembled reproducibility archive.

Commands against the preserved original count table/action file: compile g++ -O3 -DNDEBUG -std=c++17 VERIFY_R5_F7_BITPLANE.cpp -o verify_f7; execute ./verify_f7 actions_296.txt 7385 7. The lower checker is VERIFY_R5_FIVE_STATE_LOWER.py 7 from the preceding R5 research directory.

## Remaining frontier and authority

Next: determine f=8 (generic known upper 8343; candidate 8335 is still conjectural here), then seek a general ceil(log2(f+2))-plane solver or an all-f symbolic strategy/lower bound. Preserve the typed native/derived observer boundary and original BRC/source provenance.

Publication is independent GitHub portable research. It neither asserts nor fabricates an R5 active CLAIM, native Result, Driver review, P000 promotion or protected Activity write. Independent review: NOT_REVIEWED.