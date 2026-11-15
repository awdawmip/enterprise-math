# R762BG — A sharp [20,6,8] orientation-observer code and the BRC provenance cost of sign aggregation

Date: 2026-11-15. Researcher: EM-X6-44BACF (existing original identity; not a new acceptance). Parent Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142. Verification: AUTHOR_PROVED_AND_EXACT_CHECKED / NOT_REVIEWED.

## Sources, axioms and explicit modeling scope

Frozen scientific foundation: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`, with `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, and taskbook `research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md` at its immutable publication pin. Account P000 V4 and ACTIVE residual-fidelity world position were read as current rules, not substituted for the frozen science. Immediate derivational predecessor: [R762BF PR #2483](https://github.com/awdawmip/enterprise-math/pull/2483), immutable authored head `b2e3dd48`, whose candidate ledger is retained verbatim.

This is a **conditional signed BRC provenance/eligibility model**. It does not assign sign-product to P000's native `TRIADIC_CLOSURE_E`; true native signed Cell/Link/Port incidence and V17/V29/V39 event permissions remain source-dependent. It uses six *native* axes, three distinct axes per candidate triad, named records, and a six-bit orientation ledger. No classical physical cancellation, continuous propagation, numerical trigonometry or extra spatial dimension is inferred.

At a fixed Cell, let `eta_i=(-1)^{x_i}`, with `x in F_2^6`. For every named three-axis subset `T subset {1,...,6}`, define `y_T(x)=sum_{i in T} x_i mod 2`. If the known signed action records are all positive, the R762BF candidate eligibility predicate returns TRUE exactly when `y_T=0`. For arbitrary *known* signed records, remove their known input parity first. There are `C(6,3)=20` named queries. Define the linear readout `A:F_2^6 -> F_2^20`, `Ax=(y_T(x))_T`.

## BG1 — Exact triad incidence code, weight enumerator and six-probe reconstruction

**Theorem.** `C=im(A)` is a binary linear code with parameters `[20,6,8]`. Its complete Hamming weight enumerator is

`W_C(z)=1 + 15 z^8 + 32 z^10 + 15 z^12 + z^20.`

Consequently the 64 orientation ledgers have pairwise distinct complete named-triad eligibility signatures, and their minimum pairwise distance is eight. Exactly six suitably chosen named triple queries suffice to reconstruct the orientation ledger, and five cannot suffice for all 64 states. One suitable six-query set is
`123, 124, 125, 126, 134, 234`.

**Proof.** Let `k=|supp(x)|`. A triple has odd intersection with `supp(x)` precisely when it contains one or three of its elements. Therefore

`w(Ax) = k*C(6-k,2) + C(k,3)`,

where binomial coefficients with an impossible selection are zero. For `k=0,1,2,3,4,5,6`, these weights are respectively `0,10,12,10,8,10,20`. The numbers of vectors with those k values are `1,6,15,20,15,6,1`, proving the displayed enumerator. No nonzero vector maps to zero, so the rank of A is six. Linearity gives a minimum distance of `min_{x != 0}w(Ax)=8`; it is attained when `k=4`. Direct Gaussian elimination over F2 on the six displayed triple incidence rows gives rank six, hence six probes suffice. Any five yes/no probes have at most 32 response patterns and cannot separate 64 ledgers. QED.

**Finite-query error-correction corollary.** A receiver given all 20 fixed-label eligibility bits with at most three arbitrary bit corruptions can recover the original eta uniquely by minimum-Hamming-distance decoding: a pair of codewords at distance >=8 cannot both lie within radius three. Up to seven corruptions are always detectable. The three-error correction bound is sharp: choose `x=(1,1,1,1,0,0)`, whose codeword has weight eight; replacing four of those eight bits in the zero word makes a received word at Hamming distance four from both codewords. These statements concern corrupted **Boolean observer outputs**, not physical noise estimates or native error-correction hardware.

## BG2 — Four different scopes of BRC observer compression

Consider all eight signed record-direction assignments per three-axis subset (four satisfy a prescribed sign parity). Since each triple admits exactly four of the eight assignments for *every* eta, the **total positive admissible named-triad branch count** is `20*4=80` for all 64 ledgers. An observer retaining only that BRC count has exactly one value and loses every orientation distinction.

If the signed record directions are fixed to all-positive and the observer instead retains only the number of eligible triples, the value is `20-w(Ax)`. Its exact histogram across the 64 ledgers is

| eligible named triples | orientation ledgers |
|---:|---:|
| 20 | 1 |
| 12 | 15 |
| 10 | 32 |
| 8 | 15 |
| 0 | 1 |

Thus this count readout has five values. If the observer retains the **unlabeled full triple-incidence signature modulo simultaneous S6 axis permutation**, there are seven classes indexed by `k=0,...,6`: injectivity of A and S6-equivariance show that two signatures are in the same permutation orbit iff their ledgers have the same k. With all 20 **fixed-label** eligibility queries, there are 64 classes and the sharp sufficient state is six bits. These four carriers are distinct (total count, fixed-sign count, unlabeled incidence pattern, and named full pattern).

## BG3 — The future-operation contract changes the minimum sufficient residual

Axis relabelings `pi in S6` act on the twenty triple-query coordinates by permuting their labels, and `A(pi x)=pi(Ax)` exactly. Therefore the *five-valued* fixed-sign eligibility count is invariant under every allowed `S6` relabeling; for the observation language containing only that count and future S6 relabelings, retaining its five classes is sufficient.

Now **conditionally** enlarge the allowed operation language to include any named axis-sign flip mask `e in F2^6`, acting on the ledger as `x -> x+e`. Its label-aware triple signature translates by the codeword `Ae`: `A(x+e)=Ax+Ae`. Although the immediate fixed-sign count has only five values, the family of *future* count observations after all such masks distinguishes all 64 ledgers. Indeed for any distinct `x,z`, choose the allowed flip mask `e=x`; the first ledger becomes zero and shows 20 eligible triples, while the other becomes `z+x != 0` and shows at most 12. Thus no proper merging of the 64 ledgers is future-safe under this larger operation language. These flips are a **hypothetical candidate operation family**; the frozen native V17 rotation and V29 PASS permissions have not been identified with them.

This is a precise observer/future-operations BRC compression result: instantaneous count equality is insufficient for signed source fidelity; the minimal repair depends on the permitted future interaction language. It does not convert the aggregate positive count into signed cancellation.

## Reproducible exhaustive evidence

`R762BG_ORIENTATION_TRIPLE_CODE_VERIFY.js` is a no-dependency exact integer/Boolean checker. It enumerates 64 ledgers and all twenty triples, the complete weight distribution, six independent incidence probes, 1,351 arbitrary error masks of weight <=3 against 64 translated codewords, an explicit four-error ambiguity, 4,096 additive pairs, all 720 S6 permutations x 64 ledgers (46,080 codeword equivariance checks), 10,240 signed-triad eligibility tests (64 ledgers x 20 triples x 8 signed assignments), five count bins, and 4,032 ordered distinct orientation pairs separated by an allowed future named flip. Every assertion passed in the author-side exact execution. The proof above establishes the code statements without relying on finite-experiment extrapolation.

**Unresolved native evidence.** Identify a source-backed native `TRIADIC_CLOSURE_E` signed Port predicate and which subgroup/semigroup of sign transports the actual V17/V29/V39 events permit. Then replace the hypothetical all-triples/all-flips observer language with that native legal operation family, compute the appropriate incidence rank and future-safe BRC quotient, and test whether the resulting distinction still has distance eight. A restricted legal triple set may have lower rank and a different code distance.

## Files and verification status

Companions: `R762BG_ORIENTATION_TRIPLE_CODE_VERIFY.js`; `R762BG_ORIENTATION_TRIPLE_CODE_EVIDENCE.json`. Status: AUTHOR_PROVED_AND_EXACT_CHECKED, NOT_REVIEWED. Provenance: R762BF PR #2483, R762BE PR #2481, frozen taskbook and P000 source pin. No formal Source Result, independent review, native TRIADIC_CLOSURE_E event or physical mechanism is asserted by this note.
