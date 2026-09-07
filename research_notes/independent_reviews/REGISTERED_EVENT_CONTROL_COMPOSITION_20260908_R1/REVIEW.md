# Independent bounded review: registered event composition, revision 1

**PASS_BOUNDED_REVISION_REVIEW.** The original three candidate defects are resolved within the reviewed scope. This is a control implementation review, not a mathematical review or an authority grant.

Public baseline: `86a04d17cbffd687b1ef74ab4990cf6b2b7e093a`, tree `7ab67689a86e47a2c0be43ca2fb5e2c4feefdfc5`.
Eleven-file candidate manifest SHA256: `3d6055a3cffc9b7de99cabeebeb1a8e2e6b92230ebe8f77dc6794984973fb266`. The JSON and script contain all eleven exact source hashes.

- Malformed scope/legacy-marker values are checked before set membership and receive deterministic rejection; both original exception cases now return the expected states.
- The primary reduction passes its already-resolved lease through the optional keyword-only hook parameter. The provisional replay uses that exact value, including task defaults and caller defaults; it does not guess 90 or 120. Both original opposite-direction renewal cases pass.
- Claim and optional researcher identity checks are shared with the original reducer through `live_claim_event_reason`; absent, matching and mismatched identity semantics retain the original boundary. The two original wrong-identity cases now agree.

Independent execution: the six original counterexamples plus four bounded consumer/scope checks all pass. The additional checks cover a 37-minute caller default through HEARTBEAT/DONE, the original five-argument direct hook, rejection of replay context without a resolved lease, and rejection of a wrong-publication CLAIM as terminal-barrier provenance. They are not a rerun of the author's 82-test or 62-test suites, or the earlier 10-test suite.

One local baseline blob collection proves 4556 tracked inputs: exactly seven specified tracked paths differ; the other 4549 are byte-identical. All eleven candidate hashes match before and after execution. The original six wrapper function spans, held-filter tail and held-aware original core call are exact. Removing the three authorized added lines from the core reconstructs its baseline bytes exactly.

The existing registration/time/held chain remains scoped to the same task and current publication before provisional authority is evaluated. The implementation review confirmed the type filter still preserves other-task/nonregistered events; immutable records, Result projections, review dispositions and mathematics remain outside the edits.

Initial failed evidence and the initial frozen manifest remain unchanged. The revision author summary hash `fea0219b3f1e42c2a5775d6eb6e8426f2ca375648502483cbf430705eac0a77f` was verified as prior author evidence; its 62-test result is not attributed to this independent run.

## Reproduction and actual evidence

Run with Git and Python 3.12 using normal assertions against the exact candidate checkout. The public baseline object must be locally present; the script performs no network access or ref mutation.

```text
python -B review.py /path/to/exact-reviewed-enterprise-math-checkout
```

The repository path is a required positional argument; no local-only commit or hard-coded local checkout is required. Execution writes only adjacent review.json and uses temporary fixture directories. A replay changes its timestamp and therefore its JSON digest.

Actual execution timestamp: `2026-09-07T19:15:26.156881+00:00`; Python `3.12.14`.
Executed script SHA256: `6ed10ea934c2a26b3f05bb31cab80f18126b7c5f98b28a25944dcfab42c5555c`.
Execution JSON SHA256: `938e107c78971995ac8626bbae92e0f3f306e6ec61cb702adc9629f738fcae2d`.

Publication of this candidate for its remaining gates is supported by this bounded review. Published exact-head reference integrity, all eight quality shards and expected-head main admission remain owner work. No source file, claim, Result, review, mathematical status, Issue or remote ref was modified by this reviewer.

Global-Knowledge-Sync: main@990d7c1 / GLOBAL_KNOWLEDGE_V1
