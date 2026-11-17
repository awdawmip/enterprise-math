# R5: exact third fixed-schedule cost rank for all error counts

Date: 2026-11-18 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Typed model and theorem

Frozen scalar scientific input: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551; exact table EXACT_R5_ALL_101_BUDGETS.json has SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. The model has 256 named scalar hypotheses, 101 physical budgets k=214,...,314 (each query costs k), normal real response interval [N_h(k)-eta,N_h(k)+eta], and at most f arbitrary unmarked errors. Set t=2f+1 and tau=2eta in the fifth chamber

25845652773852463277015040000 <= tau < 58182461585441404127941754880.

A fixed schedule is a predetermined full multiset of queries (order ignored), identifying all hypotheses under at most f errors. It is feasible exactly if every unordered hypothesis pair has at least t queried positions with disjoint normal-response intervals (proved in prior R5 fixed-schedule certificate).

**New theorem:** For every integer f>=0 and every real tau in this chamber, the first three distinct fixed-schedule cost ranks are exactly 735t, 735t+1, 735t+2. The first is attained by a unique multiset: t copies each of (216,223,296); the second by exactly three single changes 216->217, 223->224, 296->297 (previous theorem). At the **third cost rank 735t+2** there are exactly **six** multisets for f=0 (t=1) and exactly **nine** for all f>=1 (t odd >=3):

Six multisets exist for every t>=1: start from t copies of each budget in (216,223,296), and make exactly one of the following modifications:
(1) 216->218; (2) 223->225; (3) 296->298;
(4) 216->217 AND 223->224; (5) 216->217 AND 296->297;
(6) 223->224 AND 296->297.

For every t>=3, three additional multisets are feasible:
(7) two copies of 216->217; (8) two copies of 223->224;
(9) two copies of 296->297.

All classifications count query **multisets**, not their ordering permutations.

## Exact dual-gap proof of exhaustion

Reuse the four exact witness pairs with integer weights:
(0,64):223, separating budgets [223,290];
(1,2):1, separating budgets {214} union [216,221];
(2,8):215, separating budgets [215,221];
(16,32):296, separating budgets [296,312].
These separating sets are stable over the fifth chamber; endpoints are verified against the frozen integer center table.

Let r_k>=0 be integer query multiplicities. For each witness i let a_i be its number of separated query positions and e_i=a_i-t>=0. Define s_k=k-sum(weights of witnesses separated by query k). Exact enumeration of k=214,...,314 shows every s_k>=0 and

s_k=0 iff k in {215,216,223,296};
s_k=1 iff k in {217,224,297};
s_k=2 iff k in {218,225,298};
all other k have s_k>=3.

The exact integer identity for total query cost B is

B - 735t = sum_k(s_k*r_k) + 223e_1 + e_2 + 215e_3 + 296e_4.

For cost B=735t+2, positivity gives e_1=e_3=e_4=0 and r_k=0 for all s_k>=3. Restricted to the remaining nine candidate budgets, witness 2 separates only {216,217,218}, while witness 3 separates {215,216,217,218}. Because e_3=0, witness 2 coverage cannot exceed t; because feasibility requires at least t, e_2=0 and r_215=0.

The surviving support splits into three disjoint groups G1={216,217,218}, G2={223,224,225}, G3={296,297,298}. The tight witness equalities force exactly t selected queries in **each** group. Every group has slack costs (0,1,2), so total excess cost two is precisely one of: a single slack-two query in one group (3 choices); one slack-one query in each of two distinct groups (3 choices); or two slack-one queries in the same group (3 choices if t>=2). This proves **exhaustion** of the six/nine candidates for t=1/t>=2, with no other multiset achieving rank-three cost.

## Feasibility, finite certificate and all-f extension

The executable verifier checks every one of the 32,640 unordered pairs from the 256 named hypotheses at the worst integer chamber threshold U-1. It confirms that (216,223,296), each of the three single-slack-one replacement triples, and each of the six cost-two one-layer replacement triples separates **all** pairs. It also checks the four dual witness sets at both L and U-1, the exact slack classification over all 101 budgets, and full multiplicity coverage/cost for t=1,3,5,17.

Layer lemma: concatenating t independently pair-covering query triples gives at least t separating positions for each pair. For any t>=1, each of the six cost-two triples combined with t-1 original triples yields the stated third-rank schedule. For t>=2, each of the three double substitutions arises from two independently covering one-cost replacement triples combined with t-2 original triples. Thus **all** candidates are feasible for the required odd t=2f+1; no extrapolation from finite checks is used in the all-f proof. Since integer center differences have no threshold transition between U-1 and U, the result covers all real tau in the chamber.

## Evidence and next question

Verifier: VERIFY_FIXED_COST_GAP2.py (Python standard library; exact integers; no floating point), input frozen SHA-256 as above. Actual run prints PASS_R5_FIXED_COST_GAP2_ALL_F; RESULTS.json and EXECUTED_STDOUT.txt record the coverage. The complete 1,549,048-byte frozen input, program, proof, stdout and hashes are also packaged in the local reproduction ZIP. Prior frozen scalar source and fixed-schedule results are reused without repinning.

This theorem concerns only the *derived scalar observer*: the complete native X6 joint relation, provenance, BRC dynamics and P000 require their separate observer-preservation mapping. The 256-state **adaptive** f=8 minimax value remains in [8335,8343]. Next direction: an exact adaptive residual-preserving decomposition or a stronger multi-state adversary certificate. Formal Task CLAIM / Result / Review not asserted.
