# R5 — Second exact partial-control separation: the six-cycle has 10 dynamic states versus 13 inert states

Date: 2026-11-16 (Asia/Shanghai).
Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Evidence: AUTHOR_PROVED / FINITE_EXHAUSTIVE_INTEGER_CERTIFICATE / NOT_REVIEWED.
Scope: auxiliary indexed-centre, genuine source-labelled ring of six triangles. Original P000, ACTIVE X6 worldview and frozen science are unchanged.

## Theorem

For the cyclic observer q(u)=sum_(i mod 6) u_i u_(i+1), raw masks u in {0,1}^6, genuine source-library cost 30+q(u), additive slack s=2, and only the two named commands Set_0(0), Set_0(1):

    M_stat(6,2) = N_dyn(6,{0},2) = 10
    N_inert(6,{0},2) = 13.

Here M_stat is the exact minimum number of distinct static source outputs; N_dyn is the minimum number of states of any deterministic source-labelled Moore transducer (arbitrary initial state choice, all finite command words); N_inert restricts both named commands to be self-loops on every controller state. The last gap grows from the previously established k=5 gap 8-7=1 to 13-10=3 in this next exact instance.

## Ten-state construction with real source labels

Set r_i to the following integers, and define B_i={u≤r_i : Delta_{J={0}}(r_i,u)≤2}, where Delta_J is the exact inherited partial-control future-loss expression. State i emits the canonical labelled library L(r_i), of size 30+q(r_i). The complete transition table is:

| i | r_i | q(r_i) | |B_i| | Set0→ | Set1→ |
|---|---:|---:|---:|---:|---:|
| 0 | 23 | 2 | 16 | 0 | 0 |
| 1 | 29 | 2 | 16 | 1 | 1 |
| 2 | 43 | 2 | 16 | 2 | 2 |
| 3 | 46 | 2 | 7 | 3 | 4 |
| 4 | 47 | 4 | 9 | 3 | 4 |
| 5 | 53 | 2 | 16 | 5 | 5 |
| 6 | 58 | 2 | 7 | 6 | 7 |
| 7 | 59 | 4 | 9 | 6 | 7 |
| 8 | 62 | 4 | 6 | 8 | 9 |
| 9 | 63 | 6 | 7 | 8 | 9 |

The union of all ten B_i is the complete 64-mask universe. The verifier checks exact Boolean inclusion T_b(B_i)⊆B_(delta(i,b)) and exact slack 0≤q(r_i)-q(u)≤2 for every raw u in every state. Since these inclusions are closed under induction on command length, this witnesses ten states with every output a real source-labelled library.

## Exact static lower certificate

For v=0,...,63 define C(v)={u≤v:q(v)-q(u)≤2}. The prior shared-source theorem implies any feasible common library can be replaced by a canonical source L(v), so a nine-output solution would be a nine-set cover using these 64 candidates.

The accompanying standard-library checker proves no cover of size ≤9 exists through the exhaustive recurrence f(R,m): choose an uncovered raw mask u, branch on **every** candidate v containing u, and call f(R\C(v),m-1). It memoizes failed (R,m) states, eliminates candidates C(v) strictly contained in another candidate, and prunes only when |R|>m×max_v |R∩C(v)|. All three transformations are exact. The actual completed proof has 22 undominated candidate centres, 932 recursion nodes, 311 memoized failed states, and no nine-set cover. A ten-output upper witness follows from the ten-state construction. Thus M_stat=N_dyn=10.

## Exact inert-controller lower certificate

A self-loop state must be invariant under flipping raw bit0. Encode the 32 raw pairs {2t,2t+1}, t=0,...,31. For each odd source centre v=1,3,...,63, define P(v) to contain t exactly when both raw states of that pair are contained in the static coverage C(v). Every inert state is contained in some P(v) by the same genuine-source common-library theorem.

The identical exact cover recurrence, now on the 32 pair indices, rules out 12 or fewer inert states: 16 undominated odd centres, 12 recursion nodes, 11 memoized failures. Conversely the explicit 13 source centres

    23,27,31,39,43,45,47,51,53,55,59,61,63

cover all 32 pairs by their P(v) sets; each corresponding labelled-source state may self-loop for both commands. Hence N_inert=13.

## Verification and scope

Execute the accompanying R5_K6_SINGLE_CONTROL_EXACT.py with Python 3 standard library (no SciPy, floating point, MILP or external solver). It prints the accompanying R5_K6_SINGLE_CONTROL_EVIDENCE.json, including all ten full raw belief member lists, source costs, transitions, exact coverage and search statistics. All finite assertions run successfully on the declared 64-element raw universe. These are exact finite claims for (k,s,J)=(6,2,{0}); mathematical review remains NOT_REVIEWED.

Prior source: R5_K5_SINGLE_CONTROL_SEVEN_VS_EIGHT_THEOREM.md; PARTIAL_NAMED_SET_FUTURE_SAFETY_THEOREM.md; SLACK_SOURCE_COVER_AND_DYNAMIC_BELIEF_THEOREMS.md; inherited common labelled-source family at the frozen pin. Historical contributor: EM-DIRECT-B78E55; Activity RA-33C87C2B703418F0706695E9. Formal current Task/CLAIM binding is separate.

Next: test k=7. The static cover has a candidate 17-output optimum, while the canonical maximal-future-safe-belief construction currently has a 19-state example, so investigate whether a non-maximal belief selection closes this 2-state gap. Preserve exact actual sources and command-action scope.