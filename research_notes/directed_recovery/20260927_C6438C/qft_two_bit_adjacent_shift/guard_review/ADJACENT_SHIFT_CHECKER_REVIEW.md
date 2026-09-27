# Adjacent-shift checker and execution-design review

Verdict: PASS for the declared bounded first run. This shared-context review read source and performed only standard-library source-text/AST comparison; it did not import or run any scientific module or numeric comparator.

Final on-disk SHA256 pins:

- `../check_adjacent_shift.py`: `6a7969e779800652a6143354bcbe732b670cb90128781e2f1243db91d1e6a9fe`.
- `../DESIGN.md`: `f5b85d9c7e2836259910ee9f25d16766a9a820521326c65693ff002480030cb2`.
- `../adjacent_shift.py`: `bee8a702062dfb16a75139a63b6c52b9451a02834a5b3033f5d52fcaebff9c6e`.
- `../ADJACENT_SHIFT_REDUCTION.md`: `96757c3624c69bf3ec1e313504f56bb6099d1a79e47032813084b19340c272ad`.

The coordinator clarified that the earlier advertised checker digest bfb6d5a4... was of in-memory LF text, while Windows wrote CRLF. The actual checker byte digest is 6a7969e7... above. The final DESIGN now binds those actual bytes; no executed evidence is being repinned. My source-only AST check used exactly the checker's text-reading conventions and confirmed that the comparator function equals the original aligned source. Original checker pin: `6777057a9468b673c7d58a657467c65ae1c37bd353fd55b9eb86a743efdaa969`; copied function text SHA256: `c665b55053b03bb96a0411bd5fab39ae0f7d920ec08b1cf1ee0d62ac0b4f58e7`. No old checker was imported or executed.

The six declared tuples all satisfy adjacent k=ell+1<g-1. Their full residue ranges contain 37 requests, and one ordered-pair pass per tuple contains 1,152 pairs in total. The independent comparator observes the two bits using typed quotient/remainder, forms parity through typed addition/division, and routes typed signed differences into all residue buckets. Its sign routing uses the observed parities, not a host formula for the answer. Pair work is once per tuple, not repeated for each residue.

The coverage checks match the new schema: two ordered orientation records containing the inherited single-bit progression, plus correction records only for nonempty intervals; two base and two correction tables per nonempty orientation; preserved reused displacement sum; original 2g normalization; negative outputs; empty heads; R>L; and the duplicated half-modulus head in the even-R fixture. Nonzero low remainders occur in the ell=1 fixtures. R=1 is present. The pair comparator covers finite windows shorter than V through its complete pair domain, without inventing a separate endpoint point-query receipt.

The fourteen tamper controls target nine full paid replays, one paid valid prefix followed by invalid adjacency, and four early source/schema/type/key rejections. All targeted correction/base fields exist on the declared nonempty first progression. Dropping an even-modulus orientation is tested at the correct request. The prefix test changes ell so the second request fails before mutation; the retained first request is compared with its honest original, inflight remains None, and its raw trace ends at that completed request. This is a verification failure after paid work, not a mid-arithmetic interruption. Twelve input controls and the detached pre/post production-boundary snapshots preserve ordinary invalid-input reuse.

Cost aggregation charges six production, six new pair-comparator, six positive-replay and ten paid-negative streams. Overlapping boundary snapshots and replay references are not additional streams. Native calls use contiguous process intervals; all digit, signed/typed, node and cache work is separately accounted. Maxima remain maxima. No timing comparison or superiority over earlier shortcuts is asserted.

The startup guard must identify the actual activity, startup boundary, TASK_RESEARCH mode, both permissions and no sync debt. Proof/source/design/guard bytes and comparator source are rechecked before completion. All success/failure artifact names are protected against overwrite or a second run. Failure collection retains available production, comparator, replay and control traces without completing new mathematics. Import/constructor failures before an object is returned, unreturned local semantic objects, allocation or serialization failure remain the documented limits; the grid does not inject a terminal arithmetic interruption.

No substantive defect or migration-field mismatch was found. The static verdict does not establish actual PASS, the asserted observed coverage or any cost totals: those still require the coordinator's single execution and full raw readback.

Global-Knowledge-Sync: main@52978d9 / GLOBAL_KNOWLEDGE_V1
