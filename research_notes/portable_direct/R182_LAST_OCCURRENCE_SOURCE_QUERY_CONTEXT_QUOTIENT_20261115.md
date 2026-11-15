# R182 — Exact last-occurrence source-query quotient and BRC affine transport

Date: 2026-11-15. Status: **AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED**.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Research lineage: [R181 source-presence quotient](https://github.com/awdawmip/enterprise-math/blob/1379c31db9285808a28636e567aa23f5c83126d6/research_notes/portable_direct/R181_SOURCE_PRESENCE_OBSERVER_AND_AFFINE_DIMENSION_20261115.md).
The project retains P000 / Heartbeat World native X6; this is a typed metadata observer on complete BRC branch histories, not a change to the six spatial axes, heartbeat time, or native physical dynamics.

## 1. Precise population, observer and future operations

Fix `k >= 1` and a list of distinct target source IDs `T={t_0,...,t_(k-1)}`. A **complete atom** is `(branch_id, source_id, ordered_signed_X6_path)` as in R180, with arbitrary nonnegative integral IDs and an ordered finite native path over twelve signed primitive X6 directions. Histories are finite concatenations of whole atoms. All other metadata is retained in the uncompressed original, but the *declared* observer below looks only at membership of the source ID in T and chronology of last occurrences. No atom is split into characters of its source encoding.

For every nonempty `U subseteq T`, define `q_U(w)` to be the source ID in U of the **last** atom of history w having a source ID in U, or `NONE` if absent. The declared observation is the joint family of all q_U. Future operations: prepend and append complete histories an arbitrary finite number of times; positive rational-weight alternatives and independent serial branch composition using exact weight, affine action and multiplicity. A query about branch identity, an unselected source name, the original signed path or hidden native port state must retain the full carrier or an additional certified observer.

## 2. R182A — Exact finite quotient and free right-regular-band law

Define `lambda_T(w)` as the list of *distinct* targets occurring in w, ordered by increasing position of their **last** occurrence (oldest last-occurrence first). For example, with T=(a,b,c): `lambda(a b a c b)=(a,c,b)`; unselected source atoms are ignored.

On lists with distinct entries from T define

`a star b = (entries of a not in support(b), preserving their order) followed by b`.

**Theorem A.** For all complete histories u,v,
`lambda_T(uv) = lambda_T(u) star lambda_T(v)`.
The empty list is the identity. The operation is associative, every element is idempotent, and
`a star b star a = b star a`.
The exact quotient consists of every partial permutation of the k targets, and has

`N_k = sum_{r=0}^k k!/(k-r)! = k! sum_{j=0}^k 1/j! = floor(e k!)` for every `k>=1`.

**Proof.** Every target occurring in v has its last occurrence inside v. Those targets occur at the end, in the order given by lambda(v). A target not occurring in v keeps the last occurrence and relative order assigned by u. This is precisely the star formula. Associativity follows by applying the formula to three concatenated histories, while the empty list is the empty history. In a repeated list a star a, all earlier entries are overwritten and the second copy is a; hence idempotence. In a star b star a, the final a overwrites every a-entry in the earlier factors, leaving only b-entries outside a and then a: exactly b star a. Any partial permutation is represented by the history of its own distinct target atoms, proving surjectivity and the count.

For the floor identity, the positive remainder
`e k! - N_k = sum_{j=k+1}^infinity k!/j!`
is less than `(k+2)/(k+1)^2 < 1` for k>=1 by bounding subsequent consecutive denominator factors by k+2. Therefore N_k is its integer part. QED.

This quotient is a (free) **right regular band** on the target sources. It is noncommutative when k>=2: `(a) star (b)=(a,b)` and `(b) star (a)=(b,a)`.

## 3. R182B — Necessary and sufficient for every latest-source subset query

**Theorem B.** Two complete histories u,v yield equal q_U values for every nonempty U subseteq T, including after every left/right complete-history context, **if and only if**
`lambda_T(u)=lambda_T(v)`.
Moreover the singleton queries q_{ {a} } and pair queries q_{ {a,b} } already determine every q_U, so they give a finite separating observation family.

**Proof.** Every query q_U(w) is the last element of lambda(w) that belongs to U, or NONE. Thus equal lambda states give identical queries; Theorem A shows all future left/right concatenations descend through star. For necessity, compare the states with empty left/right contexts. A singleton q_{ {a} } detects whether a belongs to the state. If supports are the same but their orders differ, two targets a,b have opposite relative order; q_{ {a,b} } returns the more recent one and distinguishes the states. Hence the full query family, indeed its singleton/pair subfamily, separates all N_k states. QED.

The information-theoretic minimum for a fixed-length binary encoding of this **semantic state** is `ceil(log2(N_k))` bits; this is distinct from the dimension of a linear/affine action and from the bit complexity of a chosen implementation. For k=4: N=65 and at least 7 bits; for k=6: N=1957 and at least 11 bits. R181's presence-only observer has 2^k states and therefore does not preserve latest-source comparisons.

**Useful one-query specialization.** If just one fixed nonempty subset U is ever queried, the exact quotient has `|U|+1` possible values. Its concatenation rule is `q_U(uv)=q_U(v)` if q_U(v) exists, otherwise `q_U(u)`. This stronger compression is safe for that fixed query family and arbitrary left/right contexts.

## 4. R182C — Explicit exact affine representation and packet homomorphism

Let `S_k` be the N_k partial permutations with empty state indexed 0. In `Q^(N_k-1)`, assign vertex `v_empty=0` and each nonempty s its own standard basis vertex `v_s`. For each s define the unique rational affine transformation F_s by

`F_s(v_t)=v_(t star s)` for every t in S_k.

The k independent variables are *source selectors*, not native spatial directions. This affine map exists uniquely because N_k vertices are affinely independent. It is described explicitly by offset `b_s=v_s` and matrix column indexed by nonempty t equal to `v_(t star s)-v_s`; all coefficients are integers in {-1,0,1}.

**Theorem C.** `F_s.then(F_t)=F_(s star t)` under the actual `brc_transport.Affine.then` chronological convention, and the representation is faithful. In particular, its output on the empty vertex is `F_s(0)=v_s`.

**Proof.** Both sides agree on each vertex v_p:
`F_t(F_s(v_p))=v_((p star s) star t)=v_(p star (s star t))`.
Affine maps agreeing on a full affine basis are equal. Distinct s give different outputs at v_empty, establishing faithfulness. QED.

Let a positive BRC packet be a finite multiset of tuples (positive rational weight, whole-atom history, positive integer multiplicity). Convert each history w to F_(lambda(w)) and coalesce entries with identical exact (weight, action). Because lambda is a monoid homomorphism, this conversion **commutes exactly** with multiset alternatives and Cauchy serial composition, including multiplication of weights and multiplicities. Thus the existing `EffectHistogram.from_terms`, `.alternatives` and `.then` API can model this declared observer in dimension N_k-1. This dimension is an **explicit upper bound**, not a minimal-affine-dimension claim.

This is an abstract affine adapter theorem, based on the source interface `src/enterprise_math/brc_transport.py` (observed main Git blob `be1debe367263931bd5e93fd750be3ed54624fe1` in the R181 read); direct installed-package execution remains pending. Unlike its compact semigroup state, a dense N_k-1 dimensional matrix adapter is expensive and should not be used as a scalability claim.

## 5. R182D — Exact resource bounds and observer-specific compression

Store each state as an ordered list of <=k distinct source indices. It uses O(k log(k+1)) bits with fixed-size target indices and admits star composition in O(k) expected time using a target membership table. A sequential atomic update moves its target to the end (or does nothing for a source outside T); a straightforward array implementation takes O(k), while a doubly linked list plus a target-to-node index supports O(1) update after source lookup. Query q_U by scanning the list backwards costs O(k) worst case, or O(|U|) after maintaining target rank information; preprocessing the target-ID index and maintaining rank data have their own costs. These are complexity bounds for the declared observer alone, not the total cost of BRC computation or arbitrary provenance recovery.

The full R180 fixed-radix history remains available whenever original source IDs outside T, signed native paths, branch IDs or different observers are needed; scope-specific projection does not erase the original by default. This is a concrete observer/future-operation preservation certificate consistent with P000's retention requirement.

## 6. Verification, provenance and next problem

Exact independently reproducible script: `R182_last_occurrence_context_check.py`. Result: `R182_verification.json`, status `R182_EXACT_REFERENCE_PASS`. It checks k=1,...,5 exhaustive state pairs (110,786), every nonempty subset query on those pairs (3,359,802), every distinct-state witness through singleton/pair queries (55,186), 5,461 complete-atom words of lengths 0..6 using k=3 and an irrelevant symbol, 173 explicit rational affine matrix compositions in small k, and 80 positive rational packet pair comparisons. No floating-point approximations. These finite tests corroborate but do not replace the universal symbolic proof.

Control source: earlier exact `RS-S23-AV` continuation request `em-r1-20261115-1900-r181-s23-continuation-read` was `FAILED / CANONICAL_REJECTED: unknown current immutable task publication`; this study is independently preserved portable research without asserting a CLAIM. Historical SID `MCP-46f202db13e64ad6b4c8860e06908245`, researcher `EM-DIRECT-BF4AD7`, Activity `RA-7A118452894D2600AE7DE5A2` are provenance, not a new Task owner assertion. Native Activity checkpoint is still pending.

**Next scientific question:** determine the minimum faithful affine dimension of the free right regular band S_k, or construct a substantially smaller typed BRC adapter while preserving q_U and all future port selections. Separately test the actual installed enterprise_math module under a pinned project environment and measure packet creation/composition/query costs against R180/R181 carriers. Maintain any native hidden source/coupling information separately until a matching scope-typed certificate is established.
