# EC49FAI — Horizon-adjunction law and an exact signed-X6 BRC prefix-demand jump

Date: 2026-11-04. Status: **AUTHOR_PROOF / EXECUTED_FINITE_CHECK / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**.

Parent: EC49FAH at immutable commit `8efee24f0fbc5e270b5f24749e06296b3b80836d`, Draft PR #1730. Frozen scientific input remains Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; current behavioral policy was read separately. P000 and ACTIVE worldview are unchanged.

## Precise question

EC49FAH proves the author-side finite H8/M5/S<=6 signed-X6 optimum `E*=76`. Before extending to H9, determine which facts about the exact horizon-tagged BRC prefix-cover demand `q_K(d)` transfer unchanged, and whether a legal complete BRC key at horizon h remains legal at h+1. This manuscript establishes a general set-cover adjunction law, the exact key feasibility interval, an actual signed-X6 observation-admissible witness, and a conditional global H8-to-H9 cost transfer.

## Theorem 1 — exact raw-key horizon interval and word length

Use the pinned six operation letters `a,c,d,e,f,g` with signed native X6 operation lists in `VERIFY_EC49FAI.js`. For a fixed full positive-step cache key `K=(u,v,w)` and horizon h, the pinned generator `SCREEN_H5_EC49EXJ.py:words` uses exactly

`r=u+v-h-1,quad n_a=w-1,quad n_f=h+1-v-2w,quad n_g=h+1-u,quad n_e=w,quad n_c+n_d=r.`

All counts are integers. There are raw primitive-operation words with this key iff `w>=1` and

`max(u-1,v+2w-1) <= h <= u+v-1`

(the h domain must also be within the declared research horizon). This is a **raw feasibility** criterion: the frozen T2/T4 nine-history observer can eliminate all words at some h. The common signed primitive-step length, however, is independent of h:

`L_K = 2n_a+4(n_c+n_d)+4n_e+2n_f+2n_g = 2(u+v+w-1).`

Proof: nonnegative integrality of each displayed count is necessary and sufficient to form at least one permutation; all signed-operation lengths are respectively 2,4,4,4,2,2. Substitute the count identities to obtain the closed interval and length.

## Theorem 2 — exact local observation-cover adjunction

Fix a **single full BRC key** K, a depth d<=L_K and a set A of horizon-tagged mandatory observer signatures. Let `P_c(d)` be the nonempty set of actually admissible signed primitive-step prefixes at depth d that can realize signature c. The exact demand is

`q_A(d)= min{|S|: S intersects P_c(d) for every c in A}.`

Append t new horizon-tagged signatures T with nonempty admissible prefix sets; leave old signatures, their allowed native words and their observation contract unchanged. Then

`q_A(d) <= q_(A∪T)(d) <= q_A(d)+t.`

For one new signature c, equality at the lower end holds **iff** some old minimum-cardinality prefix cover intersects `P_c(d)`; otherwise `q_(A∪{c})(d)=q_A(d)+1`.

Proof: every cover of A∪T covers A; a minimum cover of A extends to cover T by choosing one legal prefix for each added signature. For t=1, an unchanged-size new optimum is also an old optimum, giving the iff. These are exact finite statements, not heuristic observer compression. They preserve horizon labels, signed order, cache identity and provenance.

## Theorem 3 — precise H8-to-H9 whole-model lower-bound transfer

Consider a newly declared H9 optimization model which retains *all* H8 per-horizon signature and signed-word obligations, uses the same prefix cost and requires **exactly five distinct full BRC keys** across h2,...,h9 and at most six distinct observer matrices. Deleting h9 from an H9 witness yields a valid H8 restriction with **either four or five** distinct full keys. For any such compatible models:

`E9*(M=5,S<=6) >= min{E8*(M=4,S<=6), E8*(M=5,S<=6)}.`

Proof: deleting paths never increases the number of distinct nonempty ordered signed prefixes; the old restriction retains all H8 obligations and at most six observers. At most one full key disappears by deleting the single new horizon, so exactly five keys become four or five. Apply the appropriate H8 exact-key minimum. The author-side EC49FAH equality `E8*(M=5)=76` supplies only the five-key term; a **verified** four-key bound is still needed for an unconditional H9 numerical inference. No H9 optimum is claimed here.

## Executed native signed-X6 witness and full local q profile

Take `K=(4,5,1)`. Its raw horizon interval is [6,8] and `L_K=18`. At h=7, counts are `r=1,n_a=0,n_f=1,n_g=4,n_e=1`; the actual nine-history T4 observer admits **420** words and all four required signature labels. At h=8, counts are `r=0,n_a=0,n_f=2,n_g=5,n_e=1`; the T2 observer admits **147** words and both mandatory labels. Two genuine ordered native operation words are `fefggggg` (signature 1836425) and `geffgggg` (signature 1866380); each expands through the signed-X6 primitive OPS table. At h=9, `r=-1`, so the same complete key has **no raw word**, independent of observation type.

Exact set-cover over the full observed word enumeration yields:

| Signed primitive depth d | q(h7 T4) | q(h7 T4 + h8 T2) |
|---|---:|---:|
| 1–14 | 2 | 2 |
| 15 | 4 | 4 |
| 16–18 | 4 | **6** |

Thus the same-key addition of two actual horizon-tagged signed-X6 observer colors produces a **sharp +2 demand jump** from d=16 onward; the same key cannot simply be continued to h9. This supplies concrete information for new H9 schedule pruning and observer-aware prefix-demand transfer.

## Exact execution and limits

The committed standalone `VERIFY_EC49FAI.js` was executed as the same source text using the JavaScript evaluator; all 567 observed word instances were enumerated and every depth 1–18 solved by integer-mask exact set cover. `EXACT_REPORT_EC49FAI.json` is the actual resulting output, including each depth, observed color IDs, raw word witnesses and unique prefix counts. A separately composed local Python permutation enumerator gave the same 420/147 counts and depth profile; this is author-side cross-validation, not Source-native independent Driver review.

The verification is exhaustive for the stated K/h7/h8 family and the bounded exact typed observer. It does not enumerate all H9/M5 schedules, settle H8/M4 globally, or alter the previous H8/M5 frozen optimum. The H9 transfer lemma requires its declared compatible model assumptions.

## Next discriminating unit

EC49FAJ: retrieve the precise accepted/author-side H8/M4 lower-bound frontier; test whether its minimum reaches 76 under the **same** complete-key/observer signature convention, then derive a sound unconditional H9 numeric lower bound. Independently derive a count of H9 feasible K intervals and an exact horizon-tagged q update for one representative schedule; no blanket H9 optimum claim until complete search or proof.
