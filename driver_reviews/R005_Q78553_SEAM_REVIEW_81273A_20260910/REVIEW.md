# R005 q78553 exact seam — ordinary Driver review

Driver-ID: `EM-DVR-81273A`  
Disposition: **ACCEPTED**, at finite recorded-computation strength.  
Result: `RR-4C604AB2F135EDA932CB` / `TP2-09D6ECE7F315F0766FE1`.  
Raw Result SHA-256: `f8114a88ec3566fab477ea7c093ae35dec00fa53148d5f7a41c4de07cdcd5eec`.  
Raw Result blob: `dada488146abf7d728eedc2c6bf3e882e5ff888e`.  
Prepared at: `2026-09-09T20:53:05.753563+00:00`.

The hard target `R005_Q78553_EXACT_SEAM_DISPOSITION_FROZEN` is satisfied.
The accepted outcome is **Q78553_SEAM_CERTIFIED_CLOSED**, for the entire frozen
seam `2822453183434 <= k <= 2826122804521`. Combined with the previously
accepted contiguous prefix, the admitted finite R005 frontier may become
`k <= 2826122804521` when this exact report receives its actual immutable
Driver record and canonical integration. The original Result and all 105
scientific outputs remain unchanged; this report is not a replacement Result.

## Source and scope

The mathematical owner source is [2b73da21](https://github.com/awdawmip/enterprise-math/commit/2b73da21eac990abfd28593de1b552a4c3525f98).
The original Result/HANDOFF transaction is [002bf990](https://github.com/awdawmip/enterprise-math/commit/002bf990429c483c5061f8909e3e82299494c910);
final worker bookkeeping is [a8a8b325](https://github.com/awdawmip/enterprise-math/commit/a8a8b3257d3a380f5671ed6ecd9eaff12f4b84f8).
Actual unedited OWNER HANDOFF is [5607899511](https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5607899511).
Worker identity, original CLAIM and ER remain `EM-R005Q53-050E43`,
`r005q53-050e43-20260910` / `5606578580`, and `ER-8ABFD24CCC477A03ED13`.

The exact taskbook blob is `f93278bb9f3f3492e0399147a1a13dbd50291386`.
Freeze q=78553, Q=6170573809, G=916, d_max=2 and the required gap-start band
`[1291005053866735,1294364244470160]`. The accepted scanner remains
SHA256 `6fe2dc9fe05ac16ef2bbd1919d3d03fc5b36037d010ca95afeafb62f4958d3f5`;
the prior RR566 / DR7605 / DFU192 acceptance is consumed, with no scanner
repair or DSI rederivation. This is a nonblind ordinary review by a different
reviewing agent, with shared ambient context disclosed.

The complete current control snapshot was reconstructed exactly at main
`0a3de47e91ed0c8c5fd3d5ef3a36ef0e630bb7ec`, preserving all 120 new RB paths.
The final worker return was then integrated at main
`f928e6a621449aa2ff1ad920818d83c56342f015` before creation of this review
record, so its mutation parent already contains the exact RR bytes.
The live remote head and RR must still be refreshed immediately at each
actual review-record write boundary.

## Completeness and numerical audit

The production source calls the unmodified inclusive library interval
`primes(lower, upper - 1)`, receives an exact ordered int64 array below
2^63, takes every adjacent difference, and retains its exact maximum,
all rows >=916, endpoints, count and sequence digest. The complete
half-open scan `[1291000000000000,1295000000000000)` is partitioned into
4000 disjoint width-10^9 blocks. The earlier billion-integer pilot is exactly
block 0 and is counted once; the smaller overlapping pilot is not counted.

For consecutive nonempty prime blocks, each pair is either internal to one
block or the unique last-to-first pair across one boundary. These cases are
disjoint and exhaustive. The Driver restored all 4000 original records from
the four immutable archives, verified all 3513720 original bytes and hashes,
then independently recomputed the full partition, all 3999 bridges and all
threshold/max observers without rerunning the production sieve.
There are 114956492689 primes and 114956492688 pairs:
114956488689 internal pairs plus 3999 bridges.

The emitted endpoint primes are 1291000000000027 and 1294999999999943.
Their complete gap-start interval through the latter minus one strictly
contains the required band. Every block maximum and every bridge is below
916. The global maximum is 730, from 1292271366466303 to 1292271366467033;
its start is inside the target band, so the band maximum is also exactly 730.
The four cell maxima are 720,730,720,726; cross-cell gaps are 76,92,20.

The Driver separately downloaded the [author-hosted exact pi table](https://sweet.ua.pt/tos/primes.html)
with normal TLS validation. Its bytes equal the frozen table. The exact
integer pi column gives the four count differences 28739946181,28739548370,
28738840817,28738157321, all matching the restored block sums. Both cell
endpoints are even and exceed 2, so these differences match the half-open
count convention. The approximate li column is not used. Counts are an
independent consistency check of a complete generation, not a replacement
for positions or a standalone proof against every possible execution fault.

A separately written standard-library Eratosthenes implementation rebuilt
the full prime basis through 35981714, matching the recorded basis hash and
2203176 primes. It exhaustively divided each of 14 endpoint integers by its
own prefix through the integer square root and checked all seven gap
certificates. Prefix counts vary from 2200740 to 2203176; the largest basis
count is not asserted for every endpoint. All 1535 odd interior factor
witnesses and all even-interior coverage conditions pass. Their 3077
interior integers are composite. No libprimesieve or NumPy is used by that
independent certificate audit.

The actual numerical runtime files match the original distributions:
Python executable, four primesieve module/binary files, and 509 NumPy
source/binary files. A fresh official PyPI response independently confirms
the pinned wheel hash. Bounded Driver checks cover seven half-open empty/
singleton/small cases, both task-band boundary windows, a known real 916 gap
split inside its composite interior, and replay of the unmodified reducer
against all saved blocks. Missing, duplicate, threshold-drift and overlapping
partition cases are rejected. These are bounded checks, not a claimed
second execution of the entire 4e12 interval.

The independently rerun unchanged accepted scanner, without a skip option,
returns exit 0, `CERTIFIED_UNDER_ATTESTED_CATALOG`, zero rows and zero
failures. Its complete stdout is byte-identical to the original frozen
stdout (SHA256 `8eeb7a2fbf77a7fa422b5ef349b3b43fa710fa5fecd62f95d7f551198c39948c`).
The empty catalogue is supported by the full coverage argument and recorded
computation. Dangerous 916-row/candidate verification is therefore vacuous
for a proved empty set, not for a missing or sampled catalogue.

## Delivery clarifications and evidence limits

The frozen Return's `accepted_scanner_result.json` link was absent from its
science tree, although the complete JSON was already frozen in stdout.
The existing local output, frozen stdout and independent Driver output are
all the same 1205 bytes and Git blob. The intake adds that already immutable
blob at the referenced path; [the delivery supplement](scanner_result_delivery_supplement.json)
records this repair. No original scientific output, Return or RR was edited.
The initial method document's pending-run status is historical methodology;
the later completed execution and completeness certificate establish the
final returned state.

This acceptance is a finite computational result under the pinned numerical
implementation, recorded execution and ordinary arithmetic assumptions. It
is not a formal verification of the C++ library, compiler, hardware, full
retained prime arrays or the global p=2 problem. Sequence digests preserve
replay identity, not arbitrary future prime-array queries. No next-q result,
new general tool, Lean/L4 theorem, Working Truth or Foundation admission
follows from this review.

## Follow-up and exact next route

Use `TASK_SCOPE_CLOSURE_PORTFOLIO_CONTINUATION` for the successful
Research Task, with all six explicit gates in [the follow-up specification](formal_followup_spec.json)
and zero new tasks. The existing
`GV-R005-Q78553-SEAM-CLOSURE-REVIEW-AND-ROUTE / TP2-D43B87B08CE6E6D3FD41`
provides the existing terminal Driver/frontier/route obligation. This
ordinary review, exact finite frontier and route report supply its substantive
artifacts; no separate governance CLAIM, fabricated Result or DONE event is
created merely to normalize that task's bookkeeping.

The concrete route is Task-local closure followed by actual current canonical
portfolio reevaluation. Keep both original and relay mathematical parents
OPEN, preserve their distinct responsibilities, and return the bounded
q78553 completion to the existing relay portfolio. A later q or new research
task requires its own explicit justified frontier selection and lawful
publication/assignment; pass alone does not authorize it. No parent closure
or automatic successor is requested.

The exact public-source search and duplication assessment is in
[prior_art_review.json](prior_art_review.json). The established sieve, count
tables and first-occurrence literature are reused as such; no novelty follows
from the bounded absence of an exact task-label search match. BRC preserves
labels, boundary ports and the precise threshold observer before compression,
as recorded in [reuse_and_brc_review.json](reuse_and_brc_review.json).

Actual Driver command receipts, independent results and source hashes are in
`checks/` and `review_validation_manifest.json`. The scripts retained here
are the exact run-specific Driver checks; their scratch-root constants and
actual paths are explicit. Another reviewer can materialize the immutable
RR output set in a fresh root and adjust only that path configuration before
a new labeled replay; the recorded executions are not retroactively changed.
