# C53 — tool and theorem extraction index

Status: AUTHOR_DERIVED / EXACT_FINITE_CHECKED / INDEPENDENT_REVIEW_PENDING.
This index organizes the unchanged C53 package; original results below are author-run receipts, not a new execution or independent proof certification.

Source: [研究高因数规律, completed response](https://chatgpt.com/c/6aca1804-6fac-83ec-975d-392186a6efb0?messageId=3f54ad9d-319f-44aa-94d4-d453de876d9a), 2026-11-02 02:18:33 UTC. Event `prime-c53-history-memory-20261102-a1`. Package `prime_quantum_history_memory_c53.zip`, 17 files. Source-relative paths below are inside its `prime_quantum_history_memory_c53/` directory.

## Model and domain

1260 population: 180 distinct words with prime counts `(2,2,1,1)` over `(2,3,5,7)`. Scores are `A=2(X23-X25+X27+X35-X37)-4`, `B=2X57-1`, `D=A+gamma*B`. Complete path provenance and positive probability are separate records.

The general rectangle result permits any common strictly positive `W(A,B)`. The constructive inverse additionally assumes the declared preparation rates `(x,y,z*theta^ell,1)`, positive `x,y,z,theta`, and (for all six parameters) `q^(D^2)` with `0<q<1`, real `gamma`. `ell=0` before any 2/3, then `+1/-1` for the most recent 2/3; 5/7 preserve it. These different scopes must travel with reused results.

## Reusable tools

| Source / entry | Purpose and implementation boundary |
|---|---|
| `history_memory.py`: `memory_probability`, `reference`, `state_rates`, `last_visible` | Positive finite preparation probabilities; code validates four positive rates and positive theta. Symbols are internal indices 0..3 for 2,3,5,7. |
| `history_memory.py`: `cross_ratio` | Four matched words remove common positive terminal weighting. Expects positive probabilities for the fixed C53 words. |
| `history_memory.py`: `recover_preparation`, `preparation_corrections`, `infer`, `predict_all` | Six neutral reads recover preparation, eight reads recover `u,v` and predict all 180 probabilities. Rate of 7 normalized to 1. Exact `rational_sqrt` inherited from C52 rejects nonsquare rational roots; noisy/general irrational inputs use interval inversion. `infer` returns `u,v`, not explicit exact logarithmic q/gamma values. |
| `history_memory.py`: `memory_histogram`, `scores_for_counts`, `prefix_state`, `completion_kernel` | State-aware positive DP and selected-prefix prediction. Safe state is `(counts, partial A, partial B, ell)`. Exact kernel requires integral relative terminal exponents; general mathematical sufficiency is broader than this rational implementation. |
| `history_memory.py`: `inverse_box` | Outward rational interval inversion using inherited root/log bounds. Requires positive probability boxes and a log-sum upper bound below zero; deterministic input containment, not sampling confidence. |
| `diagnostics.py`: `mixture`, `four_cross`, `mixture_prefix_likelihood`, `mixture_state_next` | Two-fixed-regime alternative and posterior-state prediction. Module includes top-level finite checks and writes results when run/imported; reuse should account for those side effects. |
| `run_checks.py`, `diagnostics.py` | Original reproduction entrypoints, Python 3.10+ / SymPy; write `results/`. Original inherited C52/BRC files retained unchanged. |

## Theorem / proof map

| Claim | Exact premise / conclusion | Proof and original checks |
|---|---|---|
| C53-T1: matched rectangle invariant | Strictly positive reference law; final score depends on continuation column, not history row. Positive row/column factors cancel from cross ratios and preserve rank. All cross ratios one implies identical normalized continuation rows when all admissible continuations are included. | `RESEARCH_NOTE.md` §2; 63 rectangle checks, 96 arbitrary-score-weight checks, 24 count-dependent null checks. |
| C53-T2: one-bit predictive repair | In the specified last-visible preparation, `(counts,A,B,ell)` is future-sufficient; when theta differs from 1, histories 2332/3223 show ell is needed at this state. One bit refers to after a visible factor has occurred. | §3 induction; 32 DP/full-word comparisons, all 343 example nonterminal-prefix predictions. |
| C53-T3: six-neutral / eight-word inverse | Six fixed neutral words recover positive preparation under positive even terminal law; two extra words determine q/gamma for the quadratic family. `u,v>0`, `uv<1`; arbitrary frequencies must still pass family prediction. Eight reads are sufficient, with no global minimality claim. | §4 cancellation formulas and unique positive roots; 6 symbolic identities, 320 full calibrations, 55,040 held-out predictions, 96 even nonquadratic preparation recoveries. |
| C53-T4: deterministic sensitivity enclosure | Four positive probability errors bounded relatively by epsilon give cross-ratio factors `((1-epsilon)/(1+epsilon))^2` and its reciprocal. Full inverse carries outward interval arithmetic. | §5; two input budgets, 12 parameter containments. |
| C53-T5: limited-design minimum carriers | Two visible types, same counts/inversion, two distinct hidden types once each: minimum 1260. Add same last-visible type: minimum 2520. | §6 short-word classification; 20 binary collision populations and 90 bounded prime configurations support the stated proof/design. |
| C53-T6: mixture-state sufficiency and discrimination | For the specified two fixed PL regimes, remaining counts plus posterior regime odds suffice for reference continuation; add partial scores for terminal selection. Its 2520 cross ratio `5617/5358` differs from the last-visible family's 1. | §7 Bayes recurrence; 1,189 prefix conditionals and 1,187 posterior updates. |
| C53-W1: score histogram information loss | Redistribution within fixed score fibers preserves every `(A,B)` aggregate while changing the particular history cross ratio from 4 to 1 for arbitrary reference preparations. | §5; explicit witness in `diagnostics.py` and `results/diagnostics.json`. |
| C53-W2: nonquadratic holdout | Quartic terminal weight matches preparation recovery but gives corrected held-out odds `2^-256` against quadratic fitted `2^-64`. | §5; exact quartic witness in `diagnostics.py` and `results/diagnostics.json`. |

## Evidence and publication handling

`results/exact_checks.json` and `results/diagnostics.json` both record `ALL_ASSERTIONS_PASSED`; their counts overlap and are finite computational evidence. `RESEARCH_NOTE.md` §8 records the 8,138-byte inherited BRC blob `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1` and 11,520 positive serial/recoalescence calls. Generic odds-ratio invariance and Plackett–Luce are credited prior work (§9); scoped arithmetic construction is the author's contribution claim.

Keep original `PUBLICATION.json` and `PENDING_JOURNAL.md` intact as historical snapshots. Their original unfulfilled destinations are EM `research_notes/divisor_extrema/20261102_c53_history_memory_and_eight_read_inverse.md` and GK `journal/enterprise-math/2026-11-02/20261102-c53-history-memory-a1.md`; a new preservation receipt should record actual later commits separately. Original activity registration remains `NOT_REGISTERED`.

The package has no standalone manifest; preservation may supply an external inventory without altering these 17 original files. Local read inspection and a credential-pattern scan found mathematical content, public scholarly URLs and source commit identifiers; no credentials or personal-contact data were identified. This is a scoped content inspection, not a security certification.
