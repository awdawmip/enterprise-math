# R5 — Exact thirteen-label plateau for every f = 0,...,8

Date: 2026-11-20 (Asia/Shanghai). Mode: independent portable TASK_RESEARCH; historical research provenance EM-DIRECT-4C3E47, original Activity RA-F2257922D00B2FE4C4818DBD. Evidence: **AUTHOR_EXACT_FINITE_CHECKED / INDEPENDENT_ENDPOINT_SIGNATURES / PARTIAL_INDEPENDENT_F8_BELLMAN / NOT_REVIEWED**.

## The frozen model

The scientific input remains awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551. The 1,549,048-byte EXACT_R5_ALL_101_BUDGETS.json has SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Retain its accompanying stages_18.json. There are 256 **named** scalar hypotheses h and 101 physical-cost queries k in {214,...,314}; the exact integer query-center response under h is N_h(k). At the fixed robust endpoint tau=58182461585441404127941754879, a correct answer y satisfies 2|y-N_h(k)|<=tau. Up to f arbitrary response errors occur without an error flag. Query cost is k, and objective V_f is the optimal worst-case total physical query cost needed to identify the hypothesis.

Define the twelve-label seed W=(0,16,32,48,1,64,17,80,18,24,34,82).

## New exact finite theorem (R5-13-F8)

**For every** t in {0,...,255}\W (all 244 labels) and **every integer** f in {0,...,8},

    V_f(W ∪ {t}) = 735 + 950f.

In particular, V_7=7385 and V_8=8335 for **every** thirteen-label extension of W. The already established twelve-label certificate V_8(W)=8335 therefore cannot be strengthened by merely adding one more named label. A joint two-label extension is a new problem; the full 256-hypothesis optimal value remains within the previously supported bounds 8335<=C_8*<=8343.

## Exactness of the finite state reduction

For query k and observation y the joint observation-support mask is M_k(y)={i:2|y-N_i(k)|<=tau}. Every nonempty support is included in one obtained from a doubled interval endpoint 2N_i(k)-tau. Such masks can be reconstructed with **integer** comparisons 0<=N_j(k)-N_i(k)<=tau. Keep the inclusion-maximal masks: for support M⊆M′, every previously feasible hypothesis surviving M is also surviving M′, and the minimax suffix cost under M cannot exceed that under M′. No information-reducing pairwise or per-hypothesis projection replaces these full 13-label masks.

If two physically priced actions have the same maximal joint-support family, their state successors coincide for all counter states. Keeping only the least-price representative is therefore exact.

Let e=(e_1,...,e_13), each e_i in {0,...,f+1}; label i is live iff e_i<=f. On support M, set (T_M e)_i=min(f+1,e_i+1_{i not in M}). With at most one live hypothesis V_f(e)=0. Otherwise

    V_f(e) = min_{k: no maximal mask M includes every live label}
             { k + max_{M∈maximal_supports(k)} V_f(T_M e) }.

At positive price, an action admitting an observation support covering all live hypotheses can leave the decision state unchanged and cannot help a finite worst-case terminating strategy, so skipping it is sound. Each retained action strictly advances at least one live counter on every branch. Thus the recurrence is finite, acyclic, integer exact, and fully covers adaptive strategies in this frozen scalar model.

The preceding author census established 48 **priced full joint-support signature classes** across the 244 named extensions, and exact values V_0,...,V_6=(735,1685,2635,3585,4535,5485,6435) for every class. This run computes the one representative of **each** of those 48 classes at f=7 and f=8 by the same exact recurrence (per-class cap 18,000,000 states; no cap reached). Every representative returned exactly (7385,8335); signature equality then transfers the two new values to all 244 original distinct names. The complete nine-column 244-name census and the 48-class representative ledger are saved here.

## Actual verification and scope

1. Recomputed the frozen input SHA256 locally (exact match). Generated the 101×256×256 Boolean comparison adjacency from integer centers using the previously saved frozen-source make_adj.py.
2. Ran independently reconstructed doubled-endpoint support families for **all 244** names. The independent Python verifier reported PASS_R5_THIRTEEN_244_INDEPENDENT_ENDPOINT_SIGNATURES (244 names, 48 price-aware classes).
3. Executed the exact packed-counter C++ DP at f=7 and f=8 for **all 48 representatives**. All reported normal exit and equal costs 7385 and 8335. No class is estimated by extrapolation.
4. Used a separately implemented nibble-packed, action-text C++ Bellman oracle with action sets independently generated from frozen integer centers for two classes: t=2 (class 0): V_8=8335, 2,762,736 memoized states; and t=178 (class 47): V_8=8335, 2,473,266 memoized states. Independent f8 DP for the **other 46 classes** was not executed. Mathematical independent review is NOT_REVIEWED.
5. There is no asserted native X6/Port/BRC equivalence or formal Result/Review publication. Hypothesis names, original joint observation-support masks, unflagged-error semantics and physical prices remain preserved.

## Reproduction and next unsolved question

This branch inherits the predecessor source at commit 9bda779f9ae0a4c2340d63eb8e16cc465392b896, plus new ALL244_F0_F8.csv, CLASS48_CERTIFICATE.json, executable C++ recurrence and instructions in REPRODUCE.md. The full frozen input and per-run logs are included in the delivered local reproduction bundle; the exact immutable source pin and SHA are supplied above. The six predecessor publication files remain preserved under research_notes/portable_direct/r5_thirteen_f6_plateau_20261119/ in the parent commit.

**Next:** determine whether there is a pair of extra names {u,v}, disjoint from W, with V_8(W ∪ {u,v})>8335; or certify the exact 14-label pair classification. Fresh 14-way joint-support masks are required. Distinguish any scalar bound improvement from future native BRC/X6-port transfer.
