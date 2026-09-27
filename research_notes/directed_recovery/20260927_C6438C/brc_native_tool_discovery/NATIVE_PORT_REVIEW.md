# Native relative-port execution: shared-context source and saved-record review

Verdict: **PASS for the declared four-case finite correspondence experiment, with the accounting and re-entry limits below.** No mathematical or saved-record contradiction was found. This is a shared-context review, not formal independent admission. The reviewer did not import scientific modules, run the instrument, invoke a provider, or repeat native arithmetic. Only source reads, standard-library saved-record consistency checks and review-file I/O were performed.

## Bound artifacts and complete readback

* `native_relative_port.py`: SHA256 `0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8`.
* `EXPERIMENT_PLAN.md`: `931d7b7659c3e62707f10d20a2312cb03c945e6354f715c1ebda5d72fdb178a6`.
* Entire uncompressed results: 4,063,019 bytes; `6a111ca626f3330d16d513a15bfc31923a8c990723108e99c65b61fa5d229d28`.
* `RELATIVE_PORT_RESULTS.json.gz`: 215,047 bytes; `5a9c055dc879a9a8b33620055183b41131d739d03c735ff37a1ed67704aeca26`.
* Reproducible standard-library reviewer: `read_native_port_review.py`, `dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825`.
* Complete reviewer output: `NATIVE_PORT_REVIEW_RECORD.json`, `647c25acfea366f3ac7400a34a2435db10dff54e9f48f613ad70c7080401de6f`.

The reader parsed every byte of the gzip payload, matched the published summary hashes, checked current source/plan hashes against the executed binding, and checked pinned lazy arithmetic, full-adder source, typed integer transducer, histogram blob and vendor source bytes. It consumed 407 separately charged arithmetic streams containing 2,841 top-level operations and 69,443 full-adder digit cells. Every retained digit's input wiring and output were checked against the saved eight-column native catalog. Comparison, shift-add, division, modular column, inverse-product and gcd links were checked using their saved outputs; no host pow, modular arithmetic or gcd reference was substituted.

The outer audit consumes each route's recorded arithmetic operations in the source's actual order, resolves modular requests only through saved queried-column outputs, and checks cache keys, request counts, factor-division references and complete exhaustion of those operation lists. It reassembles histogram packets from retained branch weights/multiplicities. Both projections match after all three layers in all four cases: 24 complete histogram equalities, plus the three final output laws per case. This is a source-specific recorded-execution audit; it is not a fresh primitive-core verification or an independently implemented factor-search algorithm.

## Mathematical and native interface review

The paired-to-relative quotient is justified by unit endpoints and `gcd(x-y,N)=gcd(x*y^-1-1,N)`. The source obtains all scheduled action/inverse columns through existing typed certificates. Gcd equal to N remains live; only a proper gcd creates a factor port. Every factor port is connected to a typed division of N with zero remainder and nontrivial cofactor.

The reciprocal quotient is valid under this experiment's **symmetric** kernel: inversion exchanges the two nonidentity microscopic branches, whose weights are both [1/4]. It fixes the two unchanged-ratio branches separately. Thus outgoing full histograms, not merely mass, agree on the folded classes. Typed inverse and comparison implement the canonical representative. There is no order, factor or orbit-table input. Fixed points of inversion are stored once, while distinct coincident branches retain their multiplicities.

The source correctly uses `DOUBLE=2[1/4]`, not `[1/2]`; these are different `WeightHistogram` elements. `FACTOR(g,first_hit_depth)` states take one `[1]` identity transition in subsequent layers, so stopped-history weights are preserved without manufacturing later branching. First-hit depth and factor value remain distinct output labels. This is a first-hit positive BRC instrument, not the final-depth unstopped pair law, signed quantum evolution or a reproduction of Shor's QFT output law.

The actual state propagation uses unchanged native `brc_histogram` serial/recoalescence operations, with modular/gcd labels supplied by typed full-adder composition. The saved global `recurrent_mass_power` catalog invocation occurs exactly once (12 states, depth 1); subsequent digit uses are replays of that catalog. This is not evidence that the entire new modular kernel was independently passed through a dense recurrent matrix-power call, nor that each logical branch invoked that core anew. The histogram and arithmetic source provenance is genuine at the stated interface scope.

## Outcomes and full arithmetic costs

The third-layer live-state counts include the declared N35 case's `38 -> 7 -> 4` reduction from paired to relative to inversion-folded states. The N15/a14 control retains only FAIL at completion, with all its mass. Successful cases retain unsuccessful branches alongside the factors; none is discarded or renormalized away.

The following counts include each route's direct observation/comparison arithmetic, all table inverse setup, requested modular columns, standalone reciprocal certificates, and cached gcd computations. They do not count validation work as production or count shared schedule construction three times.

| N,a | Paired digits | Relative digits | Folded digits | Shared schedule | Validation |
|---|---:|---:|---:|---:|---:|
| 15,2 | 2,825 | 1,504 | 1,960 | 92 | 2,358 |
| 21,2 | 4,639 | 2,633 | 3,162 | 106 | 5,384 |
| 35,2 | 9,257 | 6,706 | 8,384 | 122 | 14,810 |
| 15,14 | 1,123 | 720 | 1,122 | 122 | 1,012 |

Both paid negative routes are additional: 693 digits for the gcd-key counterexample and 709 for the missing-identity mutant. Across the whole saved experiment the ledger is 69,443 digit replays, 2,841 top-level typed operations, 747,884 modeled host bit-wiring operations and 15,294 modeled bit-length calls. The single global native catalog call is separate, not multiplied by the 407 streams.

**The folded version costs more typed digits than the relative version in every case.** Its standalone reciprocal certification costs are respectively 598, 773, 2,754 and 388 digits; the saved reduction in other work does not repay them. State-count reduction is therefore not a runtime or arithmetic-speed claim. The relative version has fewer measured digits than the paired reference on this small declared grid, but there is no scaling theorem or wall-clock benchmark here.

## Negative controls and limitations

The gcd-key negative retains equal initial gcd 1 for the two declared pairs, then observes different future gcds N and 3 under the same left multiplication. It demonstrates why current gcd alone does not define a future-safe quotient. The paid mutant drops one of the two identity alternatives and has recorded mass 3/4 rather than 1. The readback checked both from their saved arithmetic and branch records. These two controls are not an exhaustive adversarial-input or source-tamper suite.

Three reporting boundaries must remain explicit:

1. `calls.histogram_serial` and `calls.histogram_recoalesce` count calls made by `Route.deposit`. Auxiliary merges in projection, final observation and total-packet checks are not included in that counter. The model also excludes general hash/index/allocation/serialization overhead and library-internal rational arithmetic cost. Those fields are **not** complete application-operation or total-cost totals.
2. The successful run script writes its outputs without exclusive preflight and has no standalone FAILED-execution preservation or resumable cursor protocol. It does not itself consume the external startup guard. The coordinator supplied the actual guard and controlled this single successful execution. This does not invalidate the recorded result, but the file must not be advertised as a safe unattended/reentrant runner; a future execution wrapper must address those operational obligations without overwriting this frozen record.
3. The native catalog binding and invocation record are audited as saved provenance, with no fresh core run. Source-specific consistency and finite agreement do not establish independent admission, unknown-order compression in general, practical factorization performance, polynomial classical Shor, or a physical/hardware advantage.

The meaningful demonstrated result is a correct, paid positive BRC quotient under a factor-witness observer, with an honest failed-base control and an unfavorable extra-fold arithmetic result. The remaining structural task is to reduce future factor-relevant state or readout cost without a supplied factor/order and without moving the work into an uncharged partition oracle.

Global-Knowledge-Sync: main@8c6557d / GLOBAL_KNOWLEDGE_V1.
