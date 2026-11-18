# R5 — Fixed query order with optional stopping: an exact minimax no-gain theorem

Date: 2026-11-18 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Frozen model and question

Science pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551. The exact input EXACT_R5_ALL_101_BUDGETS.json (SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b) specifies 256 named scalar hypotheses h=0,...,255 and legal physical query budgets k=214,...,314. A good response is any real y in [N_h(k)-eta,N_h(k)+eta], and at most f unmarked answers can be arbitrary. Every requested query has positive cost k. Set tau=2eta.

A *fixed-order optional-stop* policy specifies its entire query-budget sequence before seeing responses. Only stopping and final decoding may depend on observations. A *fully prepaid batch* executes a preselected finite sequence and then decodes. The objective is certain correctness for all true hypotheses, all allowed correct responses and all <=f corruptions, minimizing worst-case accumulated cost.

## General minimax theorem

Let H be any finite hypothesis set, K any finite action set with positive costs c(k), and G(h,k) nonempty good-response sets. Up to f responses may be arbitrary and unmarked.

**THEOREM.** Among deterministic, globally fixed action sequences, permitting arbitrary response-dependent stopping and decoding does not change the optimal *worst-case* cost:

C_f(fixed order, optional stop) = C_f(fully prepaid fixed batch).

This statement holds for all eta>=0 and f>=0 in the frozen R5 scalar model.

**Proof.** A query k *separates* a pair (a,b) when G(a,k) and G(b,k) are disjoint. In a finite fixed prefix s, let d_s(a,b) count separating positions.

**Pair-distance lemma.** The prefix supports guaranteed correct identification under <=f arbitrary unmarked corruptions exactly when d_s(a,b)>=2f+1 for every distinct pair. For the forward direction, if there were a single transcript compatible with a and b with <=f bad answers for each, then every separated position would be bad for at least one of a,b; therefore d_s<=2f, contradicting the proposed bound. Conversely if some pair has d_s<=2f, split its separated positions into two groups of size at most f. At nonseparated positions choose a good response in the intersection. At separated positions choose a good response for a on one group and for b on the other. The same transcript is compatible with both with <=f bad answers under either, making guaranteed decoding impossible.

Fix any observation-independent query schedule s_1,s_2,... and define t* as the first prefix satisfying the pair-distance lemma. For every t<t*, there exists a pair admitting a common length-t transcript with at most f corruptions under either member. Each earlier subprefix of this transcript is also ambiguous. Hence no sound stopping rule can stop on that transcript by time t. The transcript is realizable under one fixed true candidate with at most f total corruptions; extend the run with good future responses. Since all query prices are positive, the schedule's worst-case stopping cost is at least the cost of prefix t*. Conversely, a policy that executes exactly t* queries and decodes is correct, achieving this worst-case cost. If no globally decodable prefix exists, no sound finite worst-case guarantee exists under the schedule.

Every first globally decodable prefix is a legal fully prepaid batch; every legal prepaid batch is the prefix of some fixed schedule. Minimizing over schedules yields exactly the fixed-batch minimum. QED.

This is a worst-case theorem, with no assumed probability distribution. Observation-dependent *future query choice* is genuinely adaptive and not subject to this equivalence. Actual decoder state still retains named hypotheses and their possible distinct mismatch counts.

## Consequence 1: fifth chamber, all f

For real tau in

25845652773852463277015040000 <= tau < 58182461585441404127941754880,

the earlier source-pinned exact fixed-batch theorem gives 735(2f+1). The new equivalence therefore proves

**C_f(fixed-order optional-stop; tau)=735(2f+1)**

for every integer f>=0. The optimal nonadaptive multiset contains exactly 2f+1 repetitions each of budgets 216,223,296, in any order (apart from a never-used suffix). In particular f=8 requires worst-case 51 observations and cost **12495**. The prior full-256 adaptive bound 8335<=C_8^*<=8343 is unchanged: real adaptive query selection saves **4152–4160** cost units relative even to optimally stopped fixed-order querying.

## Consequence 2: near-critical final chamber, all f

For real tau in

1876919155234970890319953920000 <= tau < 1882951873548292168718745600000,

the source-pinned near-critical *all-f* dual witness theorem gives an exact fully prepaid cost of 957(2f+1), with unique optimal multiset consisting of 2f+1 copies each of 217,218,224,298. Thus

**C_f(fixed-order optional-stop; tau)=957(2f+1)**

for every integer f>=0. At f=8 the worst-case total is **16269** in 68 observations. The pre-existing sharp full-alphabet identification limit D=1882951873548292168718745600000 remains valid for this scalar observer.

## Finite exact corroboration

The accompanying VERIFY_R5_FIXED_ORDER_EARLYSTOP.py takes the unchanged frozen integer JSON, validates the source SHA-256, enumerates all 32,640 unordered pairs of named hypotheses, checks selected action-support separation at both integer chamber endpoints, confirms query-exclusive witness pairs and simulates prefix pair-distance counts for f=0,1,8. A cyclic order of the cited optimal multiset is globally decodable only after the last query, with an explicit indistinguishable pair at the penultimate prefix. The observed completed run exited 0, with stderr PASS_R5_FIXED_ORDER_EARLYSTOP_MINIMAX_EQUAL_PREPAID. All gap comparisons use unbounded integers.

This checker validates two corollaries and their distinguishing witnesses. The general theorem is proved logically above; the two full-batch baseline optima are inherited from their previously preserved dual certificates, not reconstructed in this run. The upstream 954-event integer source derivation is not rerun.

### Existing evidence and references

- Frozen science input: commit 435e77af0d180eac32bd1f9c4c464bc4010b7551, exact JSON SHA-256 above.
- Earlier fifth-chamber fixed-batch theorem and dual certificate: PR #2427 commit 06450ad3a3b37fef64d32bcd0a5bf89143c904ac, research_notes/portable_direct/r5_f8_nonadaptive_batch_all_f_20261118/RESEARCH.md.
- Near-critical four-disjoint-witness all-f theorem and exact verifier: THEOREM_ALL_F_FIXED_BATCH.md and VERIFY_R5_NEAR_CHAMBER_ALLF.py in the earlier reproducibility package EnterpriseMath_R5_sharp_identifiability_and_allf_fixed_batch_20261118.zip, associated with PR #2427 source history around 20c2b210c6d6ea4ed41caf6efd311c4a2c039a0d.
- Query-alphabet phase diagram: PR #2427 commit c129960c3edef77dba6213420f7d2b9ba410f840, research_notes/portable_direct/r5_256_query_alphabet_phase_diagram_20261118/RESEARCH.md.

## Native X6 typing and next research unit

The quotient is strictly the declared frozen scalar observation language and fixed future-query horizon. P000/Heartbeat World six-dimensional signed native structure, joint-observer preservation, and potentially relevant signed/branch/time/provenance residuals remain intact. This work is independent GitHub research, not a Task CLAIM, formally authorized Result, Activity mutation or independent Review. Historical predecessor attribution: EM-DIRECT-AEEFF0 / RA-B1A5102AD1877F18B4C40118. Current scientific review: NOT_REVIEWED.

**Next:** determine the full-256 fifth-chamber adaptive eight-error minimax exactly (currently 8335..8343). Since early stopping alone cannot lower the minimax cost of a fixed schedule, search must exploit observation-dependent next-budget choice or an explicitly changed error/observer model. Preserve all 256 named mismatch counters and the shared low/high fiber-product residual.