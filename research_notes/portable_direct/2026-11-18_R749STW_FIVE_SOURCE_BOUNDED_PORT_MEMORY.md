# R749STW — Five-source bounded Port observation and sharp memory

Date: 2026-11-18 (+08:00). Evidence class: **AUTHOR_EXACT_NOT_REVIEWED**. Independent portable research, no shared Task CLAIM/Result/Review and no native event admission. Predecessor R749STV: immutable commit 8d0ace56daa4cfc9fd2a78c9341681acc8f4b92e. Frozen scientific pin remains awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.

## Typed population and candidate interface

Retain P000, six distinct native spatial axes, six-dimensional X6 affine Cell torsor, one separately typed time dimension, the ACTIVE joint-relation observer-preservation rule, and the five *distinct named source positions* A,B,C,D,E with weights (1,1,2,3,6). In a restricted symbolic path adapter only, attach source i to signed raw X6 axis step +e_i for i=1,...,5 relative to a selected real Cell anchor o. The sixth raw chart coordinate is zero relative to o, **not an omitted spatial dimension**, not a native final-address encoding, and not an independent 3D universe. Cross-axis paths remain composed primitive steps. Nothing here licenses a physical triadic event.

For any nonnegative composition vector n=(n_A,...,n_E), let ell=sum n_i and let W(n) consist of all length-ell ordered five-source words of composition n. All have identical raw endpoint o+sum n_i e_i and terminal scalar total n_A+n_B+2n_C+3n_D+6n_E. Historical scalar-prefix readouts are outside this declared observer.

Define the formal positive source-branch carrier B(n)=sum over w in W(n) of [w], with distinct unit branches and no cancellation. Candidate typed operations are APPEND_i([w])=[wi] and POP([wi])=(i,[w]), including the removed source label in the POP output. This is an explicitly defined **candidate BRC-compatible provenance-Port interface**, not a claim that a live native BRC kernel or Cell/Link/Port event admits POP. No phase, signed amplitude, heartbeat evolution, or physical residual is computed.

For a nonnegative integer resource budget r, observer O_r sees the raw endpoint and terminal scalar total, then may perform any adaptive finite sequence of known APPEND_i operations and POP operations subject to **at most r POP calls in the entire experiment**. Each POP is legal only on a nonempty path and reveals its source label; budgets never reset, cloned states and historical-prefix access are excluded. This is a lifetime operation budget, not physical heartbeat time.

## Theorem: exact future-observer quotient

Set s=min(r,ell). Two words w,v in W(n) produce the same outputs and legalities under **every O_r future experiment** if and only if their final s labels agree.

The number of distinct future-observation equivalence classes in the fixed-endpoint fiber is exactly

\[
N_s(\mathbf n)=
\sum_{\substack{0\le a_i\le n_i\\\sum_i a_i=s}}
\frac{s!}{\prod_i a_i!}.
\]

Consequently the optimal additional **fixed-width** memory given the full raw endpoint is

\[
b_s(\mathbf n)=\lceil\log_2 N_s(\mathbf n)\rceil,
\]
with b_s=0 when N_s=1. All five source labels are distinguished, even A and B of equal scalar weight. The formula covers empty histories, zero counts, r=0 and r greater than ell.

### Proof: necessity and sufficiency

If the final s labels differ, s successive POP calls expose them in reverse order, distinguishing the words. For sufficiency, represent each word as a stack. No execution with at most r total POP calls can remove more than s original labels. Interspersed APPEND operations add identical, publicly known letters to both compared stacks and any POP removing those letters spends rather than replenishes budget. If the final s original labels agree, induction over every allowed action sequence proves that every removed original label, current source inventory, raw endpoint, scalar total and legality agrees. Thus no authorized future output distinguishes the words. This is an exact operation-descent certificate for O_r only.

### Counting and optimal codec

A suffix of length s with counts a_i is feasible precisely when 0<=a_i<=n_i and sum a_i=s, because the remaining inventory can be placed in a prefix. There are s!/prod a_i! different suffix orders. Summing produces N_s. A b-bit code has at most 2^b values, so b>=ceil(log2 N_s).

Construct a matching code by lexicographic rank among feasible suffixes. Define F(c,0)=1 and, for 1<=t<=sum c_i,

\[
F(\mathbf c,t)=\sum_{i:c_i>0}F(\mathbf c-\mathbf e_i,t-1).
\]

When the next suffix letter is i, skip all lexicographically smaller allowed first letters j<i by adding F(c-e_j,t-1); then decrease c_i and t. Decode by the same subtree sizes. Induction on t proves exact rank/unrank inversion and maps the N_s classes bijectively to integers 0,...,N_s-1. Storing the rank in ceil(log2 N_s) bits attains the lower bound. When POP consumes budget, the kept suffix and remaining budget can be updated; the theorem does not authorize resetting the budget while retaining the old compressed state.

## Exact consequences

1. N_0=1; N_ell=ell!/prod n_i!; and N_s is nondecreasing in s. The suffix-truncation map from feasible (s+1)-suffixes onto feasible s-suffixes is surjective whenever s<ell.

2. N_{ell-1}=N_ell for ell>=1: the single unobserved first source is determined by the endpoint composition and final ell-1 labels. If ell>=2 and at least two distinct source types occur, N_{ell-2}<N_ell, as two different leading source types may be transposed with all other letters held fixed. Thus the **smallest** POP budget exposing every complete mixed-source history is exactly ell-1; for one-source histories it is 0.

3. For 0<=s<=ell, N_s=5^s **iff** all five inventory counts satisfy n_i>=s. The five constant suffixes i^s prove necessity; when all counts exceed s, every one of the 5^s words is feasible. In this regime b_s=ceil(s log_2 5).

4. Setting n=(k,ell-k,0,0,0), s=ell recovers the earlier R749STV result N_ell=binomial(ell,k). The new theorem interpolates exactly between endpoint-only (r=0) and full-source recovery.

## Five-source examples

| Composition n | ell | N_s for s=0,...,ell | Optimal extra bits |
|---|---:|---|---|
| (2,1,1,1,1) | 6 | 1,5,21,72,192,360,360 | 0,3,5,7,8,9,9 |
| (2,2,2,2,2) | 10 | 1,5,25,120,540,2220,8100,25200,63000,113400,113400 | 0,3,5,7,10,12,13,15,16,17,17 |

## Verification, evidence and limitations

The accompanying Python standard-library checker executes exact finite branch enumeration for all five-source words of length 0..7 (**97,656** words); checks **792** endpoint composition vectors and **5,412** composition/pop-budget cases; independently compares exact feasible-suffix sets, multinomial formula, recurrence, exhaustive rank/unrank and saturation assertions; and rechecks the binary predecessor specialization through length 14. Author local execution: **PASS**. Companion JSON reports inputs, coverage and examples. The all-length theorem follows from the proofs above; finite tests are a regression check on the exact proposed branch interface.

This research is an observer-scoped **source-label information theorem**, not an observed physical residual. A real native BRC Port guard may inspect older source history, branch, sign, phase, triadic closure, resources, time or nonlocal Cell/Link incidence. If such operations are admitted, the observer equivalence must be established again for their actual semantics. Positive branch counts never substitute for signed or phase cancellation.

## Next executable scientific dependency

Take an actually licensed native two-Cell Cell/Link/Port event, retaining source/target, triadic/resource guard, signed/phase/branch and causal order. Specify its genuine readout and permitted future operations and test whether the O_r quotient is a congruence for those operations or requires a more complete residual. Preserve the native time/phase/refinement separation. Do not infer shared RS-X6-NATIVE-TIME-DYNAMICS task ownership from this portable paper.

Inputs: frozen P000 and five-source pin above; source provenance: R749STV; results: this paper, R749STW_BOUNDED_PORT_SUFFIX_CERT.py, R749STW_BOUNDED_PORT_SUFFIX_RESULTS.json. Project acceptance: not independently reviewed.
