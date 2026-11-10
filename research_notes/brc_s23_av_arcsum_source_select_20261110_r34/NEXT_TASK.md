# R35 — general adaptive history-window and batched source selection

Preserve frozen S23/AV scientific pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Reuse R34's exact per-history-arc floor-sum identity, three-gap source classes, and Farey-stage boundary correction; preserve all provenance and tie counts.

1. Replace per-arc binary search with an offline/batched rank-select method. Determine if the same set of last long-gap sources can be recovered in `O(m+J)` interval queries after preprocessing, where `J` is the output count, under a declared exact parameter enclosure and source-index horizon.
2. For histories `m=64` and `m=256`, and a second unrelated certified irrational rotation, generate **entire** maximal risk-increment sections over longer horizons without relying on S23's 164-age source template. Compare independently with full phase-sort computation on a justified finite range. Analyze tie preservation and Farey boundary corrections.
3. Derive a bit complexity accounting for input rational enclosure production, Euclidean floor-sum operations, source-index search, precision branch checks, Farey jumps, and exact affine output length. Distinguish arithmetic-operation count and bit cost.
4. Obtain independent review of the source indicator identity and the 223 source-select + 2 boundary step certificate. Preserve formal task ownership; no shared CLAIM is established by author-side notes.

Deliver a complete proof or minimal exact counterexample, executable checker, finite coverage statement and source-preserving checkpoint.
