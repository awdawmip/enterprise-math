# DGR replacement frontier fixture correction

Status: CONTROL_FIXTURE_REPAIR / COMPLETE_CI_PENDING
Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@982a440 / GLOBAL_KNOWLEDGE_V1

On integration commit `3f3cf31fdd9fc86505ad3e1e7a7f207f754cc6ce`, quality
run `34143648841`, shard 6, completed 305 tests with two failures in
`tests/test_dgr_corrected_evidence_frontier.py`. Both expectations predated
the exact frozen Result-authority isolation already present in that commit.

The authenticated replacement from `RR-BFB7190B3C8D391C6E9D` to
`RR-AE11E20304C60C349CBD` remains valid. The corrected Result independently
has three actual frozen output-digest errors, recomputed by the existing strict
validator and pinned in `research_result_authority_quarantines.json`. Therefore
the replacement sink is withheld and the historical source must not reappear.
The old fixture incorrectly required an operational corrected Result and
`AWAITING_DRIVER_REVIEW`.

The fixture now enters through the existing canonical bootstrap and checks:

- the actual validated replacement edge still points to the corrected Result;
- all three precise digest faults are still independently validated;
- neither Result enters this publication's operational result set;
- both immutable Result files and the original review remain stored;
- the publication has `RESULT_CONTROL_AUTHORITY_WITHHELD`, a nonterminal state,
  an explicit recovery requirement and the exact withheld Result ID;
- its operational Result and review are absent;
- the existing formal objective remains OPEN at its unchanged generation.

No implementation, quarantine registry, immutable Result, review, replacement,
publication, claim or mathematical source was changed. These assertions preserve
the original nonterminal/provenance obligations and add a check against reviving
the historical generation.

Python 3.12.14 ran the updated three-test module and the seven existing control
replacement tests in one fresh process. **All 10 passed** in 8.543 unittest
seconds (8.797 seconds for the process). The existing tests include authenticated
replacement authority, cycle rejection, mathematical-verdict preservation,
strict manifest expansion and separation of distinct execution evidence.
All 195 protected source hashes matched before and after the run.

Evidence: `TEMP/owner-dgr-frontier-20260908-bx1n3czz/summary.json`, with the exact
command and timings. The stderr test log SHA-256 is
`b647cca6f74fe635a988ffe8c0cfce691054e797560b958699ae8ae466d13709`;
stdout was empty. The tested fixture SHA-256 is
`4f4792c48708399f53ef6edd8c1dcf19095c884340583583896fbb70de10b3b1`.
This focused result does not declare the remaining reference workflow or all
eight quality shards passed.
