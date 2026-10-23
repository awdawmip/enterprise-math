# BRC four-label observer: sharp round-6 two-episode counterexample after one added action

**Author-side exact mathematical result, 2026-10-23. UNREVIEWED / NOT ADMITTED / NOT NATIVE-X6.** The pinned prior author theorem at commit 3f9f112e83838e65c599b844bf26095e0f949ddd covers ONLY the original public alphabet {0,2}. The present result is about an **expanded alphabet** and does not refute the original, narrowly quantified claim.

## Typed model

Independent hidden labels lie in {0,1,2,3}. At parameter z in [0,1], the original actions retain exactly

q_0 = (0,1+z,1-z,1)/3;  q_2 = (1,1,0,1)/3.

An occupied hidden-label mask D_t is **good** iff it is exactly one of {0,1},{1,2},{1,3},{2,3}. Define delta_t=P(D_t good), delta_0=delta_1=0, Delta_t=delta_t-delta_{t-1}, M_t=max_{0<=s<=t}delta_s, and

R_t = sum_{j=2}^t max(0,Delta_j) - M_t.

A strict residual growth time t has R_t>R_{t-1}; separated growth episodes have at least one intervening round without strict growth. These are positive rational masses of labeled branches; no signed cancellations, heuristic simulation, or P000-native dynamics are assumed.

## Theorem A: exact six-round counterexample with one additional public action

Add exactly one action symbol N, leaving the four labels, their mask evolution, and the good-set observer unchanged. Put

z=3/4, q_N=(0,1/4,0,3/4), word p=0N20NN.

Here q_0=(0,7/12,1/12,1/3), q_2=(1/3,1/3,0,1/3). Exact pair-inclusion/exclusion yields:

| t | public action | delta_t | Delta_t | M_t | R_t | R_t-R_{t-1} |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | N | 29/48 | 29/48 | 29/48 | 0 | 0 |
| 3 | 2 | 5/9 | -7/144 | 29/48 | 0 | 0 |
| 4 | 0 | 481/864 | 1/864 | 29/48 | 1/864 | **1/864** |
| 5 | N | 239/432 | -1/288 | 29/48 | 1/864 | **0** |
| 6 | N | 7657/13824 | 1/1536 | 29/48 | 25/13824 | **1/1536** |

Thus G(p,z)={4,6}, TWO SEPARATED strict residual-growth episodes in a length-six word. Direct proof of every table entry: for any independent time-varying categorical vectors q^(s) and good pair {i,j},

P(D_t={i,j}) = prod_{s<=t}(q_i^(s)+q_j^(s)) - prod_{s<=t}q_i^(s) - prod_{s<=t}q_j^(s).

Indeed every draw must lie in {i,j} but neither i nor j can be absent. Sum this rational identity over the four mutually exclusive good exact pairs. The displayed delta values follow by direct substitution. At rounds 4 and 6, the new positive occupancy increments remain below the running maximum 29/48 and consequently increase the residual, while round 5 decreases occupancy.

## Theorem B: six is universally the first possible separated-episode length

For ANY one-hidden-label-per-round occupied-set process with the above residual definition and an observer selecting only EXACT two-label sets, delta_0=delta_1=0. Then

R_2 = delta_2 - max(0,delta_2) = 0,

R_3 = delta_2 + max(0,delta_3-delta_2) - max(delta_2,delta_3) = 0.

These are algebraic identities for all nonnegative delta_2,delta_3; no distributional independence is required for this bound. Therefore the first possible strict residual gain is round 4, and a second **separated** gain cannot occur before round 6. Theorem A attains that universal lower bound: **minimum possible length is exactly 6** within this observer/residual class once appropriate additional public actions are permitted. This does not assert a bound for other residual definitions or other target observers.

## Theorem C: extra action may have full positive label support at interior z

A second independent witness uses z=19/20, q_N=(1,1,1,997)/1000 (the NEW action is strictly positive on all four labels), and word p=0N2020. The original sparse q_0,q_2 are not modified. The exact occupancy values are

(delta_1,...,delta_6)=(0,13333/20000,32987/60000,1319063/2160000,541979/1296000,813588041/1944000000).

M_t=13333/20000 for t=2,...,6, and the precise residual gains are

R_4-R_3=131531/2160000>0;
R_5-R_4=0;
R_6-R_5=619541/1944000000>0.

Thus the phenomenon does not require an endpoint parameter or a deterministic added action. "All-positive" refers only to q_N; q_0 and q_2 are as originally specified with some zero entries.

## Verifier and mathematical scope

The companion standalone Python file uses ONLY fractions.Fraction. It checks every prefix of every word of lengths 1 through 6 over {0,2,N}, comparing two independent exact algorithms: (a) the good-pair product/inclusion-exclusion formula above and (b) a full 16-mask branch dynamic program. This is 1,092 full words per model, **2,184 exact word-level crosschecks**. It checks all claimed fractions/gains and emits a JSON report. Under z=3/4 the six-round two-episode count is 4 of 729 words; under z=19/20 with all-positive q_N it is 22 of 729. Counts for shorter lengths are zero, corroborating rather than proving the universal lower bound.

The original author-side "one growth episode" theorem remains restricted to exactly the alphabet {0,2}; this example demonstrates an **operation-language preservation obstruction**, not a contradiction to that restricted claim. The finite rational mask is a typed positive-weight BRC carrier. The current delta_t alone discards the entire hidden mask distribution; a future-operation-preserving quotient requires preservation against the stated action language, not only equality of present delta.

**Open problem:** characterize all additional vectors q for which the one-episode result remains true over all words on {0,2,q}, uniformly in z; a tractable first target is the exact semialgebraic region in the length-six case with gains at rounds {4,6}. Separately, any native X6 assertion requires an explicit six-dimensional Cell state, three-dimensional slice/third-coordinate semantics, full readout, and future-operation-preserving simulation. No such bridge or physical attribution is asserted.

### Provenance and admission

- GLOBAL_KNOWLEDGE_V1 fixed verified main 674c44f8c3c194a82c63f0bba6da995d1d307ad3, with P000_STARTUP matching original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc and ACTIVE worldview.
- Enterprise Math read pin 4fe67f915d52a563825757c8d6e9e199f2eb4b64; applicable PORTABLE_RESEARCH_PROTOCOL and weighted BRC substrate read.
- Predecessor author-only result: 3f9f112e83838e65c599b844bf26095e0f949ddd / research/unreviewed/brc_one_growth_episode_20261023/ONE_EPISODE_AUTHOR_PROOF.en.md.
- Native control requests this turn: em_control_tasks -> CONTROL_QUOTA; em_session_start -> STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No verified active owner, CLAIM, independent Driver review or canonical mathematical admission. GitHub publication here is an **unreviewed research artifact only**.

Status: EXACT_COUNTEREXAMPLE / SHARP_MINIMUM_6 / TWO_INDEPENDENT_RATIONAL_CHECKERS / OWNER_UNVERIFIED / DRIVER_UNREVIEWED / X6_TRANSFER_OPEN / NOT_ADMITTED.
