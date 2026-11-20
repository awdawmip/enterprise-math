# CBRC F7 frozen Result output-manifest integrity audit

Date: 2026-11-21. Independent Driver: EM-DVR-DEBB5E. Original researcher/author: EM-CBRCF7-83A1D4. Scope: frozen Result RR-AA38973D56330E59D315; Task RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION. **This audit does not edit the frozen Result or reject its mathematics.**

## Immutable Result provenance

Current GitHub Source Result path:
`research_result_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/RR-AA38973D56330E59D315.json`

Git blob SHA-1 `3366edeae347e76b1f6a50bc45a6c6e4cd2dd472`; Native exact Result SHA-256 `2a89647a31de47e4ddef17ae61a843ea9a271fe602f8ab60adcca81699022c9b`.

The frozen Result claims the following immutable manifest hashes. A fresh canonical F7 continuation read `dvr-20261121-0104-f7-current-cont-v1` `SUCCEEDED`, as-of Source `1df0d052f6370e66d08c8f4216931db1bfbb9142`, supplied its verified Source artifact pins. The actual return-file SHA-256 has **also been recalculated locally from UTF-8 bytes returned by the GitHub connector at that fixed Source commit**, using a pure-JS SHA-256 implementation checked against the standard `abc` and empty-string test vectors.

| File | Frozen Result's declared Git blob SHA1 | Frozen Result's declared SHA256 | Current same-source verified / recomputed SHA256 | Assessment |
|---|---|---|---|---|
| `research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md` | `69265a0fadfd9fcd0be9354ff74f33e5e825fe84` | `5ec4896ecaa497afc333cd5642cc3b2c1c5f5a2a4e244813abd9647709f52c54` | `b4a1550a0b611a2f1cf2c44a2f4d2651512d38ed271794b22b60111783e75b35` | **SHA256 mismatch**; Git blob SHA1 still matches |
| `research_checks/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_CHECK_20260903.py` | `d6599e1d80576a5dfecf6973ab8bb4ba4ca911b5` | `eeb30b94312661ac264b98ea0e24a168b40543c68b813d10e961d1cfb72542fa` | `eeb30b94312661ac264b98ea0e24a168b40543c68b813d10e961d1cfb72542fa` | Matching |
| `research_artifacts/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION/proof_obligations.json` | `2ec734fece5b60a2c4ef2f1310c2c302c8c133f2` | `53b7edf56359460633280ee2313b911d1f0ead0b4b196111ade654fc76b298d3` | `90a017ef8fd6145d26f0867266aa6c5a71a6a921a55cd7808549799aa3972673` | **SHA256 mismatch**; Git blob SHA1 still matches |

The SHA256 for the obligations file in the right-hand column is from the canonical Source continuation's verified `source_artifacts[]` manifest. Original `RR` JSON and Source file blobs were independently fetched from GitHub. Historical progress reference `PR#1150@80df6ad5... / RR-AA389... / research_returns/...` was separately classified `DRAFT_OR_UNVERIFIED: artifact absent from immutable source manifest` in that continuation; this is a provenance reference problem, not itself a counterexample to the theorem.

## Decision boundary

**Do not treat these manifest inconsistencies as an algebraic counterexample.** The author's F7 theorem-repair text, return Git blob, bound Result record, and independent scoped proof audits retain their attribution and scientific meaning. However the Result's embedded SHA256 values are not exact pins for the two current Source files; an unconditional native `ACCEPTED` disposition asserting a fully matched frozen manifest would be premature.

Next authorized control action: reconcile the discrepancy with immutable original publication/owner commit and canonical Source via the existing same-Result review/intake mechanism; explicitly preserve original RR bytes and original author. If the contract allows a pin-correction sidecar or revised Result generation, use that native route rather than silently rewriting the frozen RR. Obtain actual native first-review report publication and current DA/independence checks before submitting a formal review. Do not replay the prior `review_reference` rejection or manufacture a review to cover this gap.

No new Result admitted, no new Native Review accepted, no Task/parent closure, and no alteration of task owner, scientific assumptions, or scheduled frequency by this audit.
