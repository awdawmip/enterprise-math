# EC49GCC — Canonical finite-suffix rank profile and exact observer-typed Pareto DP

Status: AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_BRUTE_REPLAY / NOT_REVIEWED.
Predecessor actually fetched: b8f5bb8f7d3cd3f701845d982baf6c990d241c12:research_notes/portable_direct/EC49GCB_ALL_BUDGET_PARETO_FRONTIER.md (blob 97dcccde31fd4f50af9931a51ae9c0814d34dd07).
Science: inherited BRC16943 identifier unchanged; archive pin bytes not re-read. This is an auxiliary finite labeled strict-Hall model, not a native physical calculation or admission. No P000 alteration.

## 1. Finite future observer

Let C be a finite port set, c_i positive integer capacities; every label x has a nonempty support E_x subset C. A selected set S is strict-Hall independent iff f_S(U)<c(U) for all nonempty U subset C, where f counts selected labels with support contained in U. Use the established GBP/GBU strict-Hall matroid M. Let F be the fixed remaining finite labeled suffix, disjoint from S. Each label may be selected once; skips and insertions are the only future operations. Identical support masks do not identify distinct labels. The remaining boundary B is the union of supports of F.

GBX gives h_S(U)=min_{V superset U}(c(V)-f_S(V)) for nonempty U; feasibility of S union Q (Q subset F) is f_Q(U)<=h_S(U)-1 on nonempty U subset B. GBX/GCA/GCB preserve arbitrary insertions supported in B. The present observer is narrower: insertion of only the declared remaining labels F, with known multiplicities.

Define the union closure W(F)={union_{x in L} E_x: L subset F}, excluding empty in stored coordinates. Define F_W={x in F:E_x subset W}. The finite-suffix rank profile is
    g_S^F(W)=r_{M/S}(F_W), W in W(F) nonempty.
Here r_{M/S}(Q)=r_M(S union Q)-|S| since S is independent. Every coordinate is an integer in [0,|F_W|]. The empty coordinate is always 0 and may be omitted. Distinct support masks k give at most min(2^k-1,2^|B|-1) nonempty coordinates, including all needed joint unions, not only singleton supports.

## 2. Exact reconstruction, canonical comparison and separating witness

Theorem. For any Q subset F,
    S union Q independent iff |Q intersect F_W| <= g_S^F(W) for every nonempty W in W(F).
Necessity follows from rank monotonicity on independent subsets. For sufficiency, consider any nonempty U subset B. If Q has no label supported in U, its count there is zero and the independent S has h_S(U)>=1. Otherwise let W be the union of the supports of labels of Q contained in U. Then W belongs to W(F), W subset U, and f_Q(U)=f_Q(W). Every independent subset of F_W over S is subject to the cut W; therefore g_S^F(W)<=h_S(W)-1<=h_S(U)-1. This proves every GBX cut inequality. Hence the profile reconstructs the full finite-suffix independence language, not merely optimum value.

For two independent states S,T at the same prefix, the inclusion of feasible suffix families
    {Q subset F:S union Q independent} superset {Q subset F:T union Q independent}
holds iff g_S^F(W)>=g_T^F(W) for every W in W(F). Sufficiency uses reconstruction. Necessity: choose a basis Q of F_W in M/T; if the T rank is larger than S rank, Q is feasible from T and not from S. This provides a labeled separating witness directly by greedy insertion over T, even when the two states have different counts or extending bases.

Equality of profiles iff equality of finite-suffix independence languages. The profile is consequently a canonical complete invariant for this observer (no claim of minimal coordinate count). Every sequence of skip/take choices is covered because independence is hereditary and the final chosen subset determines legality of all take prefixes. Future rewards/savings attach to the original labels; they are not quotientable unless the objective permits it.

Strict improvement over arbitrary boundary-credit dominance: ports a,b both capacity 2; S={x}, E_x={a}; T={y}, E_y={b}; the suffix consists of a single label z with E_z={a,b}. Both profiles equal (rank 1), and both accept exactly empty or {z}. But h_S(a)=1<h_T(a)=2 and h_T(b)=1<h_S(b)=2. Thus GCB's arbitrary insertion observer distinguishes states that can be merged for this fixed suffix. Even a union-coordinate credit can be strictly overinformative: capacity c_a=3, S empty, T contains one singleton at a, suffix has one other singleton at a. h_S(a)=3, h_T(a)=2, both finite ranks 1. Allowing additional future labels invalidates the quotient; original label data remains preserved.

## 3. Closed exact transition without storing h

Process label x in F and let F'=F minus {x}. Every W in W(F') belongs to W(F). Put Q=F'_W. The old rank oracle on arbitrary R subset F is reconstructed by ordinary matroid greedy: insert labels of R in fixed order if the reconstruction inequalities in section 2 remain valid. Count of inserted labels equals r_{M/S}(R).

Skip transition: g_S^{F'}(W)=r_{M/S}(Q).
Take allowed iff r_{M/S}({x})=1, equivalently the reconstructed independence test accepts {x}. Then
    g_{S union {x}}^{F'}(W)=r_{M/S}(Q union {x})-1.
These formulas follow from restriction and contraction rank identities, and only the previous profile and suffix labels are required. If E_x is contained in W, the take formula is old g_S^F(W)-1. Otherwise the skip formula is old g_S^F(W). The other branch requires at most one fresh rank query per coordinate. The unknown rank is within one of the known rank: deletion decreases rank by at most 1, addition increases by at most 1.

With u=|W(F)|, u'=|W(F')|, m=|F|, explicit rank-oracle evaluation by greedy uses at most O(u' m u) coordinate tests per state for both branches combined (assuming constant cost subset population count; account separately for label-bitset words or incremental counts, union construction, sorting, keys, objectives and witness). No polynomial global state count or runtime bound in input length is asserted; union closure can be exponential in distinct support count.

## 4. All-budget exact optimization

Reuse GCB objective: p is total retained real-label value, s is retained auxiliary-label savings, D total auxiliary release cost. State=(profile,p,s,one original label witness). If g_S>=g_T coordinatewise, p_S>=p_T and s_S>=s_T, discard T; every T suffix remains feasible from S with no worse additive objective. Same profile and same s can be merged by maximum p. This is exact for all budgets simultaneously and at least one attaining label witness. At empty suffix use F(Budget)=max{p:s>=D-Budget}. This proof holds for arbitrary processing order with fixed remaining F at each step. It does not preserve all historical labels or every optimum witness; raw original inputs remain available.

## 5. Actual replay and limitations

Exact deterministic JS synthetic replay, same generator/seed 20261128 and 350 model inputs as GCB (2..7 ports, 5..12 labeled items, base capacities 1..4 plus one for each singleton auxiliary; positive integer values 1..15 and costs 1..9). The dense comparator uses GCB's original full restricted h and direct coordinate tests, not the GCB cube implementation. The finite comparator stores only the new profile; initial rank computed directly, then all transitions through reconstructed rank oracle with old coordinate reuse. Both use same Pareto order and keep one witness. Reference independently enumerates all original labeled subsets and checks strict-Hall cut inequalities. All integer budgets compared; both witnesses checked against original inequalities, cost and value. Two end-of-stage surviving states per stage (duplicates permitted) have ranks directly checked by original strict-Hall greedy. Extra finite dominance/merge counts use independent dense h computed from the corresponding original witness labels. Counts are operation and logical retained-coordinate counts, not actual bytes or wall-clock benchmarks.

Final corrected output (immutable code 5455a6e46647404491372a6e0d1a5abaa8e4c5ee, blob ff83f25a0c1a6457c9ca0310e1829fee66df4270; output 8cb0e2efdfa0bc55e35084785054975de333c3e6, blob 76b325da350563ac051304002e6b813f5a26fc73):
- models 350; budgets 5096; brute subsets 376960; witness checks 10192; sampled rank-coordinate checks 36138; disagreements 0.
- GCB dense Pareto: 40618 cumulative states, 79761 generated, 1090270 dominance comparisons, 1965319 comparison coordinate tests, 1247687 logical retained coordinate entries (including empty), peak 640.
- finite rank DP: 5266 cumulative states, 9809 generated, 5670 dominance comparisons, 17078 comparison coordinate tests, 26977 logical retained coordinate entries (empty omitted), peak 26.
- finite rank construction: 24722 newly computed greedy rank calls and 1319677 independence-coordinate tests. Additional finite-only dominance events 714 and finite-equal merge collisions with unequal dense h 2024. These are events, not unique pairs across all stages.
- Initial published script had a statistics-only bug: pop array indexed by port mask when it could exceed its label-mask length, so baselineEntries was nonfinite. Corrected to independent port-mask population count; also optimized old-coordinate reuse. Corrected replay was actually executed, zero disagreements again. Use corrected output and code, not initial statistics. No timing or actual memory measurement; transformation/union construction, sorting, witness and validation costs not included in comparison counts.

Next: replace generic greedy fresh rank with a single insertion/coloop test using a cached basis of F_W, study support-class count or closure-based compressed rank oracle, then paired actual timing and frozen archive replay. GBY cut-network remains valuable for unknown future labels. Investigate whether the finite suffix structure of BRC16943 gives a small union closure; do not claim without reading exact archive. Physical root 2046 remains next historical unresolved root; no new physical calculation, M14 historical [25,27].

## 6. Provenance and control

Current canonical GK snapshot fc9863da6ec5a572d446353afd2101ca1176dbd3, verified entry blobs 25ae05640c7920104820dba91a1df5e9fafca25e and 108cd58e0458070b5f1a8171d2f66c8c3d0aa613. Current EM control main 8c6defc13ce3b8de164a0a00558da4f8327a9914; applicable portable, continuation, P000 V4/V5 and ACTIVE worldview, joint preservation and method sources read. Native control receipt r4-20261128-0530-ec49as-read SUCCEEDED, NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated, no shared authority. Current private session identity unconfirmed; predecessor historical researcher EM-DIRECT-23537B is provenance only. Independent informed portable research; no new session, CLAIM, task, Result, review or promotion. Activity association pending. Branch scientific persistence separate from canonical integration.
