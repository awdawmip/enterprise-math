# C54 — predictive-rank tools and theorem map

Status: AUTHOR_DERIVED / EXACT_FINITE_CHECKED / INDEPENDENT_REVIEW_PENDING.
Local preservation preparation only. Original files remain byte-for-byte unchanged; this extraction read the original proofs, code and execution receipts without running new mathematical work.

Source: [高因数原对话完成消息](https://chatgpt.com/c/6aca1804-6fac-83ec-975d-392186a6efb0?messageId=9503587d-1c4a-4767-912d-8a0afc1aa0d8), 2026-11-02 13:29:32 UTC (parent-supplied anchor). Exact Library object `libfile_c6b80acd88448191abd69219afc2f676`, file `file_000000007db88209b61374b3ff792ad8`, created 13:29:45.567898 UTC. ZIP 47,868 bytes, 15 original files; inventory and byte hashes are in `INVENTORY.json`.

## Common model and proof scope

Main population: all 3,780 different factor words of 25200 with counts `(4,2,2,1)` over `(2,3,5,7)`. `A=2(X23-X25+X27+X35-X37)-6`, `B=2X57-2`, `D=A+gamma B`. Strictly positive reference law and a shared strictly positive terminal weight `W(A,B)` are required by the rank invariant. That theorem does not require evenness or a quadratic terminal law. A particular three-state preparation supplies the constructive sharp example.

Ordinary probability-matrix rank is an observation-dependent lower bound on the number of hidden response states; it is not spatial dimension, a unique mechanism identification, or a guarantee that every preparation reaches full rank. Source proofs retain these distinctions.

## Reusable tools — `predictive_rank.py`

| Entry | Capability and caller conditions |
|---|---|
| `state_after`, `state_rates`, `reference_word` | Three-state finite preparation: consecutive visible 2 count capped at 2, 3 resets, 5/7 preserve. Four symbols encoded 0..3. Positive x/y and three positive z rates; rate of 7 fixed to 1. |
| `reference_histogram` | Exact positive DP quotient `(used counts,partial A,partial B,state)` for this proved-sufficient model. Caller must supply valid nonnegative counts/positive rates. |
| `selected_law`, `table` | Apply a strictly positive score weight with optional original BRC operations, normalize, then construct the specified history/continuation subtable. |
| `determinant`, `canonical_table` | Fraction Gaussian determinant of a square matrix; row/column normalization by first-row/column entries. Normalization assumes a positive table. |
| `signed_sums3`, `invariant_ratio`, `error_box` | Positive/negative 3×3 determinant sums, invariant Phi, and deterministic nine-entry relative-error enclosure. Shape/positivity are caller conditions; error_box checks `0<=epsilon<1`. |
| `suffix_probability`, `suffix_determinant_formula` | Repeated-5 / single-7 PL suffix probabilities and Vandermonde determinant. Formula assumes positive rate ratios and valid nonempty sequence; distinctness gives nonzero determinant, repeated rates give zero. |
| `inversion_counts`, `minimum_carrier` | Binary inversion multiplicities and minimum k×k matched-table capacity in the declared two-visible/two-hidden-prime design. Supply valid integer counts/k and a feasible upper bound; the product lower bound limits the complete candidate search. |
| `run_checks.py` | Original reproduction entrypoint; writes exact JSON/logs in `results/`. README says Python standard library plus bundled inherited sources. Original execution coverage below is retained, not rerun here. |

## Theorem / proof / original evidence map

| ID | Scoped statement | Source and original evidence |
|---|---|---|
| C54-T1 | Score-matched positive table `Q=diag(a) R diag(w)/Z` preserves rank; a K-state response factorization `R=Pi K` implies rank(Q)<=K. Selected subtable and row normalization preserve the rank relation. | `RESEARCH_NOTE.md` §2; 81 positive row/column transformations, 12 quadratic and 7 non-even terminal-weight cases. |
| C54-T2 | Normalize `Gij=Qij Q11/(Qi1 Q1j)`. For 3×3, rank<=2 requires `(a-1)(d-1)=(b-1)(c-1)`; ninth-entry prediction needs `a!=1`. | §2; constructive G has det 108, two-state predicted d=28 versus actual 64 (§4). |
| C54-T3 | Matched histories 223322/232232/322223 and suffixes 557/575/755 yield three common terminal-score columns. Three-state positive rates z=(1/4,1,4) give det(T)=1/15; thus minimum response-state count is exactly 3 for this witness. | §§3–4; 15 complete-word/DP cases, 17,532 direct reference probabilities; null comparisons 60 one-bit and 90 two-regime tables. |
| C54-T4 | For positive 3×3 tables, Phi=E+/E- is row/column invariant and det=0 iff Phi=1. Nine entrywise relative budgets imply multiplicative factor `((1+epsilon)/(1-epsilon))^3`. | §5 positive-term proof; Phi=116/71, 1% interval excludes 1; original check covers all 512 box corners, with universal inclusion supplied by proof. Deterministic probability-input bounds, not sample confidence. |
| C54-T5 | A mixture of three specified fixed PL regimes has matched-table det `19/70769988256968000`, hence minimum 3 regimes for this observation. This distribution differs from the three-state history construction. | §6; one complete mixture/DP case, 3,780 direct mixture probabilities. |
| C54-T6 | For r repeated hidden factors and one singleton, suffix probability matrix at r+1 distinct positive rate ratios has the stated nonzero Vandermonde determinant. | §7 triangular polynomial-coefficient proof; r=1..7, 21 determinant identities, 609 direct suffix products, 7 equal-rate degeneracies. |
| C54-T7 | Within the declared four-prime role design, minimum matched-table capacities 2×2,3×3,4×4 occur at 1260,25200,302400. Capacity is separate from full-rank realization. | §8 inversion multiplicity / exponent assignment proof plus product-bound-complete enumeration; 35 binary histograms / 2,989 binary words. |
| C54-W1 | Minimum identification carrier and divisor-record property separate: tau(302400)=168 while 277200 already has 180 divisors. | §8 and original sieve of 302,400 integers. |

## Original results and publication boundary

`results/run_checks.log` records `ALL_DECLARED_ASSERTIONS_PASSED`, elapsed 15.672306867999964 seconds. `results/exact_checks.json` retains rational witnesses; `results/execution_notes.md` records original exit code 0. Overlapping checks are not independent statistical observations. BRC blob `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1`, 8,138 bytes, with 7,560 original serial/recoalescence calls; inherited C53 tests are not counted as new C54 checks.

Original `PUBLICATION.json` reports self-contained summaries published/read back at EM `a244a89e6815dcff0efddff6143eae2fe71ae662`, path `research_notes/divisor_extrema/20261102_c54_predictive_rank_and_minimal_carriers.md`, and GK `8c488ae5da65fb72b22a9c5f96fb09442366932b`. Full programs and exact results are in this archive. The receipt also records C53 summary recovery `32cc8297efc3cdd91745b6dcd570d1d957496361` and native activity `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`; preserve this historical receipt unchanged.

Content inspection and credential-pattern scan found mathematical sources/results and research provenance, with no detected credentials or personal contact information. No standalone original manifest was present. Public-upload approval for this new C54 package remains separate from the earlier approved 85-file batch; this preparation has made no remote mutation.
