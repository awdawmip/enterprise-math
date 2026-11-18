# R5: exact full-256 zero-error global alphabet-cost Pareto frontier

Date: 2026-11-18 (Asia/Shanghai). Scientist: EM-DIRECT-18A068 / TASK_RESEARCH, session MCP-9c93e13b980740308ab87e082de4dd3f. Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Frozen input and exact scope

Original frozen science commit: 435e77af0d180eac32bd1f9c4c464bc4010b7551. Frozen count table: EXACT_R5_ALL_101_BUDGETS.json, SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. It supplies exact integer centers N_h(k) for 256 distinct named hypotheses h=0,...,255 and the 101 legal physical query budgets k=214,...,314.

Correct real responses y obey |y-N_h(k)| <= eta; tau=2 eta. This theorem permits NO corruptions (f=0), adaptive queries, repetitions and response-dependent stopping. A strategy must use one fixed global alphabet of at most m different budget values; physical cost is the sum of performed budgets.

Define:
T = 1876919155234970890319953920000
D = 1882951873548292168718745600000.

## Theorem: exact cost versus global number of query types

For every real tau in [T,D), the minimax identification cost C_0^(<=m)(tau) equals

    +infinity       m <= 3
    957             m = 4
    955             m >= 5.

The unique four-type cheapest alphabet is {217,218,224,298}, with restricted adaptive cost 957. A five-type alphabet that attains the unrestricted optimal cost 955 is {215,217,218,224,298}; query type 216 can be omitted from the predecessor six-type optimum. Thus five different globally available physical query budgets are both necessary and sufficient to attain cost 955.

## Exact finite proof

Two hypotheses a,b can be separated at budget k iff |N_a(k)-N_b(k)| > tau. If every allowed budget fails this test, an adversary can keep both hypotheses consistent forever by returning a value in their good-response interval intersection. Conversely, an alphabet covering every pair of distinct hypotheses identifies them by performing each budget once with f=0.

The complete frozen table has no center gap strictly between T and D. Therefore throughout [T,D), the separation bitset for budget k contains precisely pairs with gap >= D. In particular (11,14) is separable only at k=217, which every identifying alphabet must include. Exhausting all 32,640 pairs gives no identifying alphabet with <=3 types. The exact complete class of four-type identifying alphabets is

    {217,a,m,v},  a in {218,219}, m=224,...,290, v=298,...,311.

There are 2*67*14=1,876 such alphabets, and no other identifying four-type alphabets.

For zero errors, let M_k be all inclusion-maximal response supports at query k, and let S be the set of named candidates consistent with observations. The exact minimax recurrence is

    V_A(S)=0 when |S|<=1;
    V_A(S)=min_{k in A} (k + max_{M in M_k, S & M nonempty} V_A(S & M)) otherwise.

For a positive-cost query whose outcomes include unchanged S, that query cannot improve worst-case cost; omit it. Every remaining successor strictly decreases the number of candidates, making the recursion finite and acyclic. All other responses are contained in maximal supports and cannot increase the worst continuation value. The verifier enumerates maximal supports by sorted center windows of width tau, uses arbitrary-precision 256-bit candidate masks, and exactly evaluates the recurrence.

All 1,876 four-type identifying alphabets were evaluated independently. In every case the adaptive restricted value is exactly

    V_A(H_256)=217+a+m+v.

Consequently its minimum is 957, attained uniquely at (217,218,224,298). The same exact solver gives V(H_256)=955 for the five-type alphabet (215,217,218,224,298) and also for all 101 budgets. Those values and the four-type obstruction prove the full Pareto frontier.

The maximal support families are exactly the same at both integer thresholds tau=T and tau=D-1, by direct exhaustive verification. Since their defining inequalities are monotone, the result extends to every real tau in [T,D).

## Executed certificate and verification range

The published standard-library Python script verify_r5_f0_pareto_compact.py is directly reproducible using the previously preserved frozen count table. Command:

    python3 verify_r5_f0_pareto_compact.py EXACT_R5_ALL_101_BUDGETS.json

Local execution on 2026-11-18 completed with exit code 0, approximately 4.2 seconds elapsed time and 114 MiB peak resident memory, printing PASS_R5_FULL256_F0_NEARCRITICAL_GLOBAL_ALPHABET_PARETO. Checks cover all 101 budget supports at both chamber endpoints; 32,640 state pairs; 4,950 possible additional two-budget choices with compulsory 217; 161,700 three-budget choices with compulsory 217; all 1,876 successful four-budget alphabets; and unrestricted plus five-budget exact Bellman recursions.

The larger discovery verifier additionally reconstructed an optimal five-type policy using 112 distinct nonterminal candidate masks with depth at most 4, all five physical budget values occurring in the witness.

This is a proof about the frozen indexed-center scalar observer and its explicitly permitted future queries. It neither identifies nor discards the signed, path, provenance, port, phase or joint-relation state of native Heartbeat X6. P000 and the joint-relation observer-preservation contract remain in force. GitHub research preservation is separate from a formal CLAIM, independent review or Foundation promotion.

## Source lineage and next research question

Predecessors: enterprise-math Draft PR #2427; r5_256_adaptive_f0_two_chambers_20261118 (unrestricted 955); r5_256_identifiability_threshold_20261118 (T,D); r5_256_query_alphabet_phase_diagram_20261118 (cardinality threshold). Keep original count-table bytes and freeze pin unchanged.

Next: test the f>=1 full-256 near-critical Pareto frontier using an exact error-count Bellman solver or a new lower/upper certificate. The five-action zero-error witness is a smaller seed alphabet for robust decision-tree construction. Independently, the fifth-chamber full-256 f=8 cost gap remains [8335,8343] and is the main open optimization objective.
