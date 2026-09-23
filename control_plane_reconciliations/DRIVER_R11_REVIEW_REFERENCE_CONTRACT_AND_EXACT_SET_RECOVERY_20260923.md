# Driver R11 review-reference contract and exact-set recovery — 2026-09-23

Status: `NONCANONICAL_DRIVER_RECOVERY_RECORD / NOT_A_REVIEW / NOT_A_SYNTHESIS / NOT_A_FOLLOWUP_PACKET`

Driver conversation: `chatgpt-driver-hourly-20260923-0727-r11`
Driver-ID: `EM-DVR-A5A686`
Session: `MCP-98288d02291d47c9b0ebffd45b7e3be7`
Driver authority: `DA-4E5BB7BCF18B04D2F225`
Source head inspected: `56259052bd629b7e16224212ea431268d11f762a`

## 1. Current contract change consumed

Current `docs/DRIVER_FLOW_OPERATIONS.md` now exposes the closed `review_reference.independence_status` enum:

- `CLEAN_INDEPENDENT_CONTEXT`
- `SHARED_CONTROL_CONTEXT_DISCLOSED`
- `NOT_INDEPENDENT`
- `NOT_APPLICABLE`

This removes the prior client-side ambiguity that caused `INVALID_REFERENCE_INDEPENDENCE`. This Driver has shared project/control context and therefore must use `SHARED_CONTROL_CONTEXT_DISCLOSED`, not infer `CLEAN_INDEPENDENT_CONTEXT` merely from a new session.

## 2. Factor single-review flow: bounded diagnostic completed

Result: `RR-C5769D6B237D02BFF025`
Result request: `artifact-factor-result-20260923-r11-08`
Current exact review set from `review_flow_state`: `{DR-B819FB64CA4E7836CA35}`.
Result SHA-256: `1149fb488e66bdff40cd52b79b1566400c4691b8254ec884aa113a4a4d7c934f`.
Follow-up state: `AWAITING_FOLLOWUP_TASKSET_PUBLICATION`.

A single bounded `review_reference` attempt was made after the enum became public:
`review-reference-factor-p1-20260923-r11-11`.
Native result: `FAILED / CANONICAL_REJECTED: review intake requires at least two immutable reviews`.

Conclusion: Factor is a `SINGLE_REVIEW_FLOW`; `review_reference` / exact-review synthesis is not its next legal unit. Do not retry reference passes, do not write another review, and do not treat this as an independence or mathematical failure. The remaining Factor unit is canonical follow-up materialization for the existing accepted review, subject to the current follow-up contract.

## 3. GEO6 second-wave exact two-review set: independent intake judgment

Result: `RR-B5DB25EC13BF1C42DC9B`
Task: `RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS`
Result record SHA-256 pinned by both reviews: `aeca468aa264da22c75c4fdabeeb88fa9640db0481d7661ed4baeadcb9f6daea`.
Exact current review IDs:

- `DR-4187E7655E4E30A30253` — `ACCEPTED`, destination `FOLLOWUP_TASK` -> `RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS/TP2-6866CB3F890F6563C474`;
- `DR-B36C8071BB5E68A81A32` — `ACCEPTED`, destination `NONE`.

Both reviews bind the same Result bytes and agree on the mathematical boundary: the exact-set prior-art audit is accepted only at its bounded audit scope; no P000/full-cell resolver has been established and no theorem-strength/native mathematical successor follows from the audit alone. The substantive disagreement is routing, not the audited mathematical boundary.

The frozen Result itself records `NO_SUCCESSOR` and leaves four selectors unresolved (`NONOVERLAP_SELECTOR`, `TRANSLATION_FOLNER_SELECTOR`, `PHYSICAL_REFINEMENT_SELECTOR`, `MIXED_DIRECTION_SELECTOR`) until an accepted typed P000/full-cell datum resolves at least one. Therefore a future exact-review synthesis must not turn the earlier `FOLLOWUP_TASK` route into an unauthorized mathematical successor. Any compatible continuation must be typed as control/semantic reconciliation only, unless new accepted source evidence changes the Result-level successor condition.

Current own-session request `continuation-geo6-secondwave-20260923-r11-12` is still queued at this checkpoint. Do not replay it. Once it reaches `SUCCEEDED`, continue with own-session Result `artifact` -> `review_flow_state`; if the exact review set and Result SHA remain unchanged, execute pass 1 and pass 2 with `SHARED_CONTROL_CONTEXT_DISCLOSED`, then synthesize without creating a third review.

### Planned pass-1 finding (not yet canonical)

Semantic pass: both reviews accept the same bounded exact-set audit and preserve the no-P000/no-theorem-promotion boundary. Their only material conflict is destination routing. The synthesis must preserve the frozen Result's `NO_SUCCESSOR` mathematical guard.

### Planned pass-2 adversarial finding (not yet canonical)

Stress-test the earlier `FOLLOWUP_TASK` destination against the Result's explicit `NO_SUCCESSOR` and the unresolved-selector condition. Reject any interpretation that treats selector synthesis as new native mathematics or as evidence that any selector has been resolved. A control-only semantic synthesis may remain compatible; a mathematical successor is not justified by the existing review set.

## 4. Independent mathematical frontier retained

The already-published portable task `RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923 / TP2-33BFE7DD84657DAB803C` remains the clearest information-gain mathematical unit. The smallest unclassified pattern is `q2-1`: one positive vertical atom `(q,r)=(2,1)`, denominator `595`, exponent `594`, q0 budgets `1737` and `2331`; use the common portable basis and six congruences to prove exclusion or retain an exact kernel. The sixteen order-one classes are already complete and must not be repeated. No new q2-1 Result was observed in this Driver run.

## Resume rule

1. Consume the durable receipt of `continuation-geo6-secondwave-20260923-r11-12`; do not resubmit it.
2. If successful, create the own-session Result artifact and read `review_flow_state`.
3. Require exact set `{DR-4187E7655E4E30A30253, DR-B36C8071BB5E68A81A32}` and unchanged Result binding before reference passes.
4. Run exactly two reference passes with the now-public enum `SHARED_CONTROL_CONTEXT_DISCLOSED`, then canonical synthesis if admitted.
5. Do not create a third review.
6. Keep Factor on its single-review follow-up/materialization route; do not retry `review_reference` there.
7. Preserve P000, source pins, theorem strength, author provenance, and all no-sorry/no-admit/no-custom-axiom guards.
