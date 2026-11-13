# GEO6 Mahler dual-support — independent exact finite and semantic audit

Date: 2026-11-13 (Asia/Shanghai). Review lane: current RESEARCH_DRIVER, supporting mathematical evidence only (not a new Native DR).
Task `RS-GEO6-MAHLER-PRIOR-ART-SYNTHESIS`; publication `TP2-EFB8751B437EF5B5A5BA`; frozen Result `RR-EC0502A82AD5DC3995F4`; original researcher `EM-G6MAHPA-B65BDB`; accepted scientific input author `EM-G6MAH-91C2AF`. Audit reads exact GitHub Source at `a79e65d2c91daff7293beab567b96bddf4ce1e60`.

## Exact propositions and proof check

Let `C` be a finite set, `R subseteq C×C` a declared support relation, and
`D(A)={y in C: R(x,y) for every x in A}`. This map is antitone and
`D(A union B)=D(A) intersect D(B)`. If `D^2=id` on **all subsets**,
then `D` is an order anti-automorphism of the Boolean powerset `P(C)`.
Compose with complement `c`: `c o D` is an order automorphism and thus
permutes the atoms uniquely, giving `D(A)=C\pi(A)`.
As complement commutes with permutations, `D^2=pi^2`, so `pi^2=id`.
Conversely, every involutive `pi` gives the declared common-support relation
`R(x,y) iff y!=pi(x)` and an all-subset involution.

This directly verifies the *logical reduction* of the original theorem.
Its assumptions include the entire powerset and a declared relation;
it does not select a canonical P000 support relation or a native Mahler product.

## Independent exhaustive finite check

Implemented independent integer-bitmask enumeration of **every binary
relation** `R subseteq C×C` for `|C|=1,2,3,4`. For each relation,
computed `D(A)` for all subsets and checked `D(D(A))=A` for all
subsets. Independently checked whether its row incidence is exactly
`R(x,y) iff y!=pi(x)` for an involutive permutation. Results:

| n | All relations | All-subset involutive relations | Complement-of-involution forms | Classification disagreements |
|---|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 0 |
| 2 | 16 | 2 | 2 | 0 |
| 3 | 512 | 4 | 4 | 0 |
| 4 | 65,536 | 10 | 10 | 0 |
| **Total** | **66,066** | **17** | **17** | **0** |

Original Mahler author reported typed-context enumeration through n=3
(530 relations). This independent audit adds an exhaustive 65,536-relation
n=4 layer. The *general theorem* is the preceding algebraic proof; the
finite enumeration is an extended regression, not a substitute for proof.

## Independently reproduced six-point models

For n=6, enumerated all 64 subsets and exact common-support duals:

| Declared incidence | D²-closed subsets | Products on nonempty proper closed subsets (value: multiplicity) |
|---|---:|---|
| `R(i,j) iff i!=j` (complement) | 64 | 5:12, 8:30, 9:20 |
| `R(i,j) iff i==j` (diagonal) | 8 | 1:6 |
| `R(i,j) iff i==j or adjacent modulo 6` | 20 | 3:12, 4:6 |

For the six-cycle, `D({0,2})={1}` but
`D²({0,2})={0,1,2}`. Thus the closure-vs-raw-involution distinction
is explicit. Under direct inclusion `C_n -> C_m`,
`D_m(i(A))=i(D_n(A)) union (C_m\i(C_n))`;
exhaustively checked subset instances at n=1,2,4 and m=n+3,
with defect cardinality exactly m-n.

## Result/claim provenance and limit

The frozen Result pins the original return blob SHA-1
`c58ea457a9ec8da1083b5b0b7745b5798444a7a9` and exact claim/source
matrix SHA-1 `b69e313b88adb6395406011b5477dfe9fee6a74b`,
both independently read on the pinned source. Its prior-art
claim matrix records 10 entries: 2 `EXACT_DUPLICATE`,
3 `STRICT_ANTECEDENT`, 1 `ADJACENT_METHOD`,
4 `NO_MATERIAL_MATCH`; the last category is not a novelty certificate.

The four P000 questions explicitly preserved are
`SUPPORT_RELATION_SELECTOR`, `SELF_DUAL_IDENTIFICATION_SELECTOR`,
`COMPLEXITY_FUNCTIONAL_SELECTOR`, and `REFINEMENT_TRANSPORT_SELECTOR`.
Finite relation enumerations do not establish novel literature precedence,
a canonical support selector, or classical convex-body Mahler transfer.
Original author credits and published immutable Result are retained.
Native review set, follow-up packet validity, task closure and mother
objective closure require their own current Source decisions.

This note constitutes supplementary independent exact mathematical and
source-pin checking; not a new Claim, formal Driver Review or theorem
promotion.

## 2026-11-13 exact existing Native Review reconciliation

Original `rd11-20261113-0818-geo6-mahler-review-flow-v1` completed
`SUCCEEDED`, exposing the existing immutable accepted historical review
`DR-6A6587387463AE326117` (original Driver `EM-DVR-G6K2P9`,
`reviewed_at=2026-08-30T13:50:00Z`,
`disposition=ACCEPTED`, destination
`RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS/TP2-B531F3BB4A597B7D3EAF`).
This genuine DR predates this supplementary audit. No new formal review
is required to establish its historical acceptance.

The corresponding `DFU-80FF80D580C7C2C48D29` presently has
`FOLLOWUP_PACKET_INVALID / ready=false` with the exact validator result:
`Driver follow-up packet must consume the exact result next_control_plane_recommendation`.
The DFU records a generic second-wave recommendation, whereas the frozen
RR recommendation begins `Driver-review the source-backed classification
and accept only the cleaned provenance boundary`.

The open unit is therefore typed follow-up binding/reconciliation, not a
second first review, an unsaved mathematical result, or a missing author.
The present task projection still displays `FROZEN_RETURN / AWAITING_REVIEW`
despite the historical accepted DR. A bounded backend recovery issue,
[em-research-mcp #71](https://github.com/awdawmip/em-research-mcp/issues/71),
records both this and the parallel first-wave case. The immutable original
RR, DR, author credit and second-wave Task must be preserved.
