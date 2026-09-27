# Hybrid signed-gap: shared-context static review

Status: `PASS_STATIC_REVIEW_NO_BLOCKING_FINDING`. I read the complete design, implementation and checker without importing a scientific module or running an experiment. This is a shared-context review, not independent admission or an execution result.

| Reviewed file | SHA-256 |
|---|---|
| `DESIGN.md` | `0e83c68d171313896d5c1c872d64fe5c2079bace52c6b529469198ee8ae0e2e9` |
| `hybrid_gap/hybrid_signed_gap.py` | `7daf2e04be83ed9a9124c1a2bcc79ae2cc8feb5334c4b675ed19f7a2bc918fb8` |
| `hybrid_gap/check_hybrid_signed_gap.py` | `ed54ddc3ffb9735e1610ae363b69cd58d426adb4b9c1d0cc6ba85fcf11de1da7` |

## Routing and arithmetic

Endpoint routing happens before any divisibility work. The overlap `g=1,k=0` reaches the frozen endpoint implementation, which retains its highest-bit priority. Every other endpoint request incurs zero routing arithmetic. Interior requests actually construct `U` by typed doubling, divide `U` by `R`, and preserve the quotient/remainder and exact signed-operation index. A zero remainder triggers the typed subtraction `U-U`; otherwise the unchanged direct observer executes, including its repeated scale work.

The zero identity is valid for all declared inputs: toggling bit `k` is a sign-reversing involution on the complete length-`2^g` interval and changes its label by `+U` or `-U`. If `R` divides `U`, each residue histogram cancels. Every modular signed correlation is then zero. This uses the certified divisibility premise and the exact interval structure, rather than a fixture-specific zero. Returned negative values and the unchanged raw `4^-g` normalization are retained on the other routes.

No ordinary host modular, multiplication or floor arithmetic replaces the scientific route. The host performs strict input checks, public bit-index tests, routing on an observed remainder, and metadata/accounting. The supplied counting modulus remains an input; this observer does not discover a multiplicative order or target address.

## Full provenance and strict replay

The routing, endpoint and direct runners are separate objects. Every request links the routing interval and, when present, the nested request's kind, index and complete returned record. Export deep-copies the whole hybrid certificate, including unused empty runner records. Nested request copies are provenance references, not additional executions. The checker verifies that nested indices are consecutive within their respective streams and that every nested request is referenced exactly once.

Fresh verification checks strict JSON and all top-level inputs before arithmetic, reconstructs the original ordered input list, and compares the complete result. It normalizes only the three named, strictly nonnegative integer primitive-cache call counters. All mathematical values, source pins, routes, remainder witnesses, nested records, moment evidence, typed-digit counts and other statistics remain bound. It is correct not to separately rerun each nested verifier after a complete hybrid replay: the fresh hybrid observer has already executed those frozen methods and exports their full evidence for comparison.

The checker declares eight invalid inputs and fifteen mutations. Four mutations should reject before arithmetic: schema, own source, dependency pins and boolean input. Eleven should retain paid fresh replay: the zero-route changes and endpoint/direct nested value/provenance changes. Boolean zero is not equivalent to integer zero under the strict serialization comparison. These are static expectations; no pass counts or cost improvement are established until the bounded actual run and its raw evidence exist.

## Failure preservation and accounting

The `LIVE` registry keeps the active observer, completed cases, active forged certificate, completed negative attempts and replay captures. Ordinary replay mismatch captures the full fresh certificate before rejection; interruption captures available incomplete runner arrays without calling evidence generation. The outer handler isolates serialization errors per captured field and retains global native calls, and artifacts use exclusive writes. Existing success/failure files refuse a rerun before new work. Import-time failures, incomplete constructors, primitive errors before trace retention, and filesystem failure remain outside a universal recovery guarantee; the design states this available-object boundary.

Cost aggregation adds the three disjoint runner streams once per actual execution. Production, positive replay and paid negative replay are separate. The original pure-direct evidence is read by exact hash and supplies reference values and historical cost metadata; its saved arithmetic is not added to this run's bill. The global full-adder column observation is counted once through `CALLS`, whereas repeated digit composition and routing work remain chargeable. A whole-checker duration will not be a matched timing benchmark.

The nine declared tuple certificates each select one route for all their residues. All three routes are covered collectively, but a mixed-route sequence in one observer is only statically supported by this checker plan; it must not be reported as an executed mixed-route fixture. No aligned route, two-bit family, full Gram contraction, ideal propagation or general Shor guarantee is included.

No blocking static defect was found in the exact reviewed versions. Actual execution remains subject to the root's new guard and the resulting source-bound receipts.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
