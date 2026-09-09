# Actual R005 q78553 researcher startup and first data checkpoint

This checkpoint preserves the real worker's completed startup. It is not a Result,
catalogue-completeness assertion, seam certificate, or parent closure.

Researcher-ID: EM-R005Q53-050E43
Task: RS-R005-Q78553-EXACT-916-GAP-CATALOG-SEAM-CLOSURE
Publication: TP2-09D6ECE7F315F0766FE1
Parent: OBJ-R005-PRIME-ALGORITHM-LAB-RELAY-20260909
Session: em-local-r005q53-6d6d70dfbca44080a3b3c52398c39dc8
The session key was locally allocated by this actual worker; it is not an authenticated platform session ID.

The worker independently registered RA-0DA1C30C5794D50A34B7F18B on main at
0d0344880a4cbb2b78ae8a5a074758fc3392c70f, fully read it back, and passed the activity guard.
It independently read ASSIGN comment 5606399286, its unchanged server envelope, and the exact DA80B record.
It materialized a separate complete current checkout at the same 0d034488 commit,
tree 379c0cba6a63bc9655d049bfdd08f7dccffee093, with 5830 files.
The older e5 startup checkout was preserved.

Canonical assigned-research selection returned CLAIM_NEW_OWNER.
It validated actual release 5602494875 and the accepted RR566 / DR7605 / DFU192 binding.
Canonical prepare produced ER-8ABFD24CCC477A03ED13.
The independent execution branch was created and verified at the declared base.
The real CLAIM is [5606578580](https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5606578580),
claim_id r005q53-050e43-20260910, unchanged OWNER server envelope at 2026-09-09T18:11:48Z.

The first bare runtime CLI invocation failed on an unrelated raw publication fork.
Its actual argv, exit 1, stdout and stderr remain in startup/authorize-*.
The current documented control bootstrap was then installed in the same new Python process
before the public runtime guard. The actual second argv, exit 0 and full output are in
startup/authorize-canonical-bootstrap-*. It returned authorized=true under
CURRENT_AUTHORIZED_WINNING_ISSUE_240_CLAIM, bound to this exact claim, task, publication,
researcher and output scope. No control rule, task, scanner or isolation configuration was edited.
No duplicate CLAIM was sent. The owner lease ends at 2026-09-10T00:11:48+00:00.

The raw event input is losslessly reconstructible from a byte-pinned existing canonical
765-envelope gzip and ten newly observed original server envelopes.
startup/raw-events-reconstruction.json records the exact resulting 775-envelope SHA-256.
The reconstruction was checked byte-for-byte against this worker's independently fetched raw input.
The normalized comment wrapper was never used for authorization.

## First research frontier

The accepted scanner and DSI are consumed, not rederived or repaired.
The certified frontier remains K <= 2822453183433 and the next q remains out of scope.

The author-hosted [TOS gap table](https://sweet.ua.pt/tos/gaps/t0.txt.gz) was downloaded
with Windows TLS certificate validation. It supplies first positions and aggregate counts,
including 107483 occurrences of gap 916 across its entire stated test range [2,4e18].
Those aggregates do not locate every 916-gap inside this task's narrow band.
The [independent prime-count table](https://sweet.ua.pt/tos/primes/1d12.txt.gz) provides
pi values at the relevant 1e12 boundaries. Exact downloaded hashes are preserved.
Their roles are respectively a bound/provenance source and a possible independent count check,
not a complete local gap catalogue.

A task-isolated Python 3.9.13 / primesieve 2.3.0 / NumPy 1.26.4 environment has been
downloaded from the official Python and PyPI distribution services. Wheel SHA-256 values
matched PyPI metadata. The intended next unit is a timed pilot of unchanged primesieve
generation, followed by an auditable segmented full construction if its measured cost is feasible.
No pilot or full-band computation is claimed in this checkpoint.

## BRC / reuse decision

Applied the current BRC substrate's typed provenance and deterministic-boundary commitments.
The carrier is the explicitly labeled consecutive-gap population (start, gap, end, source, coverage interval).
The scanner's row observer is an exact set of candidate k values, not total gap count.
For disjoint coverage partitions, rowwise shadow output combines by set union after preserving
cross-boundary consecutive-prime pairs. Aggregating only counts cannot recover gap locations.
A certified zero count would support emptiness; a positive count alone cannot support shadow inversion.
No recurrent, signed-amplitude, or weighted critical-asymptotic claim is introduced.

The canonical toolbox coverage is recorded in tool-coverage.json.
The accepted R005 scanner is REUSE_APPLIED and will be REUSE_EXECUTED on any justified final catalogue.
Existing primesieve is REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE on the host's Python 3.14;
an isolated compatible official runtime is being used to resolve that execution mismatch.
This is not a new mathematical capability gap or a new general tool family.

