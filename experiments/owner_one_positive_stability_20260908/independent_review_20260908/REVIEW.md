# Independent finite consumer review: one-positive raw X6 stability

Status: **PASS_BOUNDED_INDEPENDENT_CONSUMER_REVIEW**.

This package reviews the executable consumer's input/output contract and selected independent boundaries. It does not add a mathematical proof, replace the existing limited paper audit, or issue a formal V2 review, claim, Result, or promotion authority.

## Frozen inputs and actual execution

The reviewed consumer and its author evidence have these SHA256 pins:

| File in the parent consumer directory | SHA256 |
| --- | --- |
| `check_one_positive_stability.py` | `283c0b64e995077d01e5b42114ffd5791bafadeb5f175b4df17118ee1a9d5878` |
| `certificate.json` | `11fd30fcc2894ffdcd7ed43e1266b65dc063aa12b57f9f5b653eb9d437bc3010` |
| `README.md` | `91f4c918eead64e0efb32f24577c9e4db081412131ccf4b22313a0ae96e4d820` |

The consumer's 12 exact source/dependency pins, including the paper and its independent paper audit, are recorded in `review.json`. All three author inputs and all 12 source pins were verified before and after execution.

The actual run completed at `2026-09-07T19:31:21.344390+00:00` (`2026-09-08` in Asia/Shanghai), using Python `3.12.14`, `-B`, and enabled assertions. It exercised 10 finite cases, independently checked all 20 raw tables per case (200 tables), and observed one intended input rejection.

The executed script SHA256 is `785f60ee9f66445e1675c19f7a93981355819c674001ad4eb85bf26c09c1d010`. The resulting `review.json` SHA256 is `2bb0c93ce92aff98f7f5e3dc2d1cfb74481bbbc1121288ab54b0512ef29ae47c`.

## Independent oracle and contract

The oracle separately aggregates the two positive input populations by raw Cell and forms the positive and negative parts of their signed difference after exact cancellation. For each coordinate triple, it projects those two parts directly and calculates L1 as total positive mass plus total negative mass minus twice their projected overlap. It does not reuse the consumer's single-positive-site L1 formula, raw projection function, or distinguishing-count bound.

For every table, the review also compares the complete original-population address set, each mu/nu/signed mass row, and the native joint `(can3, common_offset)` reconstruction. The original input ledger, cancelled difference, positive support count, P/N totals, overall norm and D, sharp flags, and literal symbolic DIV payloads are checked against independently derived expectations.

The accepted contract uses positive exact integer input weights and a positive exact integer common denominator. The difference may be signed; its positive support is counted only after Cell aggregation and cancellation. A common external anchor and labelled frame remain caller premises: integer coordinates cannot independently prove those premises. Signed analytical mass bookkeeping does not introduce negative BRC primitives.

## Finite checks and outcomes

All numeric norm and D entries below are integer numerators in the common symbolic denominator.

| Independent boundary | Outcome |
| --- | --- |
| Six balanced axis aggregates `[9,9,9,9,9,9]`, with unequal weights at several positions on the same axis | P=27, N=54, norm=81, D=540; generic `DIV(3,20)` sharp flag true. |
| Same P and N, but axis aggregates `[8,10,9,9,9,9]` | Norm=81, D=552; generic sharp flag false. N=2P alone is insufficient. |
| Equal mass P=N=53 with axis aggregates `[5,7,0,11,13,17]` and unequal position weights | Norm=106, D=1060; `DIV(1,10)` sharp flag true without uniform axis weights. |
| Add the same population to both sides, including the positive Cell, a negative Cell, and duplicate entries at a fresh Cell | The aggregated difference, all 20 table L1 values, and D are unchanged. |
| Translate both populations by `(-101,37,-11,0,25,-8)` | All table L1 values and D are unchanged; translated raw and joint addresses also agree. |
| Permute axes by `(5,2,0,4,1,3)` in the unequal-aggregate case | Each table matches the corresponding relabelled original table; D remains 552. |
| Scale the balanced case by `M=(1<<2053)+113`, with denominator `1009*M` | Literal ratio `DIV(81*M,540*M)` and norm `DIV(81*M,1009*M)` remain unreduced and UNEVALUATED. The 2063-bit denominator survives JSON encoding. |
| Duplicate, multi-Cell input populations cancel exactly | Positive support is zero; norm and D are zero; ratio is absent and sharp flags are false. |
| Overcancellation leaves a nonpositive, nonzero difference | Positive support is zero; norm=12 and D=240. |
| Two positive input Cells, with one exactly cancelled | Accepted with one remaining positive support; norm=10 and D=184. Reducing the cancellation by one unit leaves two positive sites and is rejected. |

Each case's table norms or their compact hash, plus a hash of its complete consumer output, are retained in `review.json`. The large-integer check establishes only the tested finite size; it does not claim arbitrary-size serialization.

## Runtime observation and limits

The selected post-import runtime observation recorded actual canonical DIV construction and integer cross-multiplication comparison, signed BRC support counting, and native joint-slice reconstruction. No forbidden selected Fraction, quotient/root readout, or legacy multiplicity call was observed. The interpreter's decimal conversion limit remained 4300.

This is a finite observation of selected Python/C calls together with source review, **not a transitive static arithmetic-compliance certificate**. Canonical module initialization occurs before the observation and is explicitly outside its scope. This review did not rerun the author's 12 fixed cases, static gate, or four negative callguard probes. It makes no general p<=7 assertion and no new all-input mathematical proof.

## Reproduction

From the repository root, with the pinned sources available:

```text
python -B experiments/owner_one_positive_stability_20260908/independent_review_20260908/review.py
```

An optional positional repository-root argument selects another checkout. By default the script discovers the repository from this directory layout. It rejects `python -O`, checks exact source hashes, and writes only the adjacent `review.json`. A rerun changes the execution timestamp and therefore the JSON hash; its receipt records the script bytes actually executed. No local-only Git commit or hardcoded checkout path is needed.

Only this independent three-file package was added. Author code, certificate, README, paper, and canonical arithmetic/native sources retain their verified bytes. Publication and mathematical admission remain separate owner actions.

Global-Knowledge-Sync: main@990d7c1 / GLOBAL_KNOWLEDGE_V1
