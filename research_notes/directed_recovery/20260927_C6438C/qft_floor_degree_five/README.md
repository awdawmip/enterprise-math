# Exact degree-five single-floor moments

The new backend computes all 21 integer moments
`sum_{0<=j<n} j^p floor((a*j+b)/m)^e`, `p+e<=5`, for strict integer
`n>=0`, `m>=1` and signed `a,b`. It extends the existing source-bound actual
BRC arithmetic with one-child Euclidean reciprocity. This unit has one
completed bounded run and full author and shared-context peer readbacks.
It is not a formal independent admission or a complete Shor simulator.

Nine declared fixtures produced **189 exact equalities** against separately
executed typed finite sums, with all 44 samples, native adder cells, recursive
nodes, cache controls and failed certificate replays retained. Every one of
the eight nonempty fixtures used more production digit replays than its
finite comparator: 120,943 versus 19,294 in total. The contribution is the
wider exact moment interface, not a measured practical speedup.

Start with [EXECUTION_NOTE.md](EXECUTION_NOTE.md), then
[DEGREE_FIVE_RECIPROCITY.md](DEGREE_FIVE_RECIPROCITY.md) and
[CONTINUE.md](CONTINUE.md). [DESIGN.md](DESIGN.md) records the declared test
contract. The original source/checker headers retain their pre-execution
wording; the later result files and execution note record the actual run.
All original bytes and policy-read chronology remain unchanged.

The full run contains 40 separately charged streams and 542,296 digit replays,
58,857 typed operations and 57,809 signed operations. One actual 12-state
catalog invocation occurred in the first empty production export. It is
counted globally even though all per-instance call deltas are zero. These
counters exclude uninstrumented interpreter, allocation and serialization
work; the reported 39.7466 seconds is a whole-checker observation, not a
matched benchmark.

The complete raw gzip is 3,468,068 bytes, SHA256
`b044570bb55e81ea0ff1fe73ef35af6fa7438281c2d6dac87c1c31f3ee251c9f`.
Its 88,217,988 decoded bytes have SHA256
`da675f8e04929116dac64552775f85ad75d39c71a03f78aad7c45d571fdf267e`.
The publication's indexed base64 chunks recover those original gzip bytes,
not a summary. The ZIP additionally includes the original gzip and an exact
member index. [DEPENDENCIES.md](DEPENDENCIES.md) and its machine manifest
identify historical runtime and readback dependencies; this is not a
dependency-free environment image.

The next useful work is the separately reviewed symbolic unit-residual
reduction in `next_design/`: implement its two ordinary-table interface with
paid eligibility, coefficient and replay evidence. It does not yet have an
implementation or an actual execution. General mixed floors, growing Walsh
masks, matrix-valued chronological correlations and end-to-end Shor
dequantization remain beyond the conclusions of this package.

EM immutable source is authoritative. Publication/readback and Drive backup
receipts are attached after their actual completion; no source commit or
successful remote delivery is inferred from local packaging.

Global-Knowledge-Sync: main@8c6557d / GLOBAL_KNOWLEDGE_V1 (packaging read only).
