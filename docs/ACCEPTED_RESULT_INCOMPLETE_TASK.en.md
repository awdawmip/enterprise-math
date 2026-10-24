# Accepting a result while its Task remains incomplete

`RESULT_ACCEPTED_TASK_OPEN_CONTINUATION` consumes a genuine `ACCEPTED/NONE`
scientific review of an unchanged raw `NO_GO` Result. It records the scientific
scope and the unresolved original process obligations separately. It does not
reinterpret the Result as PASS, certify the process, complete the Task, close
the parent, publish a successor Task, or reopen execution.

The decision requires the current Task publication, the existing current
Driver/session/DA and exact Result/review authority binding, all six existing
follow-up gates, and no new Tasks or `REQUIRED` gates. The first immutable review
still preflights its explicit follow-up before it is written. A second review
reopens the existing exact-set intake/reference/synthesis lifecycle. A synthesis
must consume that entire current canonical set, with its raw record pinned.

The actual scientific Driver supplies `accepted_result_scope` as an exact unique
quotation from a selected accepted immutable report. `scope_evidence` identifies
that immutable `scientific_review_id` and pins its report and complete interface
by exact path, Git blob and SHA256. The complete DR-pinned report must contain
one `ENTERPRISE_MATH_ACCEPTED_RESULT_SCOPE_BINDING_V1` HTML comment. Its nine
exact fields bind the scientific Driver, Result/publication, historical locator,
entire interface content pin, exact scope quotation SHA256, `FULL_DOCUMENT` and
the covered scope/statement/hypotheses/unresolved fields. The hash covers the
exact UTF-8 body quote without normalization or an added newline; the comment
stores only the hash, so it does not repeat the unique quotation. Parsing rejects
unknown or duplicate JSON keys, missing/multiple blocks and mixed versions.

That immutable scientific report supplies the interface binding. The interface
JSON's `reviewer` string alone supplies no scientific author attestation. A
successor cannot replace interface content or choose another scope quotation by
updating its own spec or the current Source manifest. An old DR whose report has
no binding is unsupported for this new branch; its report and existing routes
remain unchanged. A new report cannot be appended under that old DR's hash.

The writer uses the existing `artifact_pin`
and `verify_source_snapshot` contracts to verify current Source membership,
then records its actual `scope_source_snapshot`. Native snapshots contain no
Git history; their actual current trusted loader manifest is required. The
separate `historical_source_commit` is an original publication provenance
locator, not a claim that this runtime rechecked its historical tree. The
interface must identify the scientific reviewer and exact Result/publication;
its scope, statement, all hypotheses and unresolved boundaries are consumed as
one document. Code verifies identity and bytes; it does not evaluate the theorem
or infer process chronology from wording. An authorized current successor Driver
may materialize this same scope evidence under its own DA/session, preserving
the scientific author's identity. It need not reuse the original session.

The exact typed `result_continuation` fields are listed in
`research_driver_followup_contract.json`. Original process status is `UNKNOWN`,
and each explicit `ORIGINAL_PROCESS_PROVENANCE` obligation remains `UNKNOWN`
with its actual residue and evidence references. Artifact existence, a clean
self-report, and actual read chronology are separate facts. No missing-file
claim is inferred from unknown chronology.

Canonical Task state is `ACCEPTED_RESULT_TASK_INCOMPLETE`, `terminal=false`.
Dispatch freezes it as `AWAITING_TASK_CONTROL_CONTINUATION` and routes current
Driver control work. Fresh task-global CLAIMs, execution/adoption, completion
dependency release, and a parallel result synthesis cannot turn it into READY
or DONE. Independent explicitly active cohort lanes retain their own existing
authority lifecycle. The parent liveness/final gate remains independently
mandatory. Future evidence requires a separate authorized control action; the
immutable packet never automatically upgrades to Task completion.

This repository patch is not a service deployment. Before any client sends the
new decision, the native adapter must advertise and validate the schema, supply
the exact published artifacts and real current trusted Source blob manifest,
preserve current DA/session/contribution checks and Source CAS, and
expose the new nonterminal state through all runtime projections. A different
adapter repository or release is a deployment dependency. Existing native
clients must continue using advertised enums until that release is verified.
