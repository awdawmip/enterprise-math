# Heartbeat BRC occupancy-count extension

Status: RESEARCH_RESULT_EXTENSION / NOT_FOUNDATION
Date: 2026-09-20
Parent family: T0_BRC finite control ports + predictive quotient.

This note records two observer-specific results on a six-bit mask for the six positive native axes. It does not add a spatial dimension and does not replace the existing brc_control_port machinery.

For a pure cyclic heartbeat that only relabels which positive axis is active:
- total occupied count gives 7 classes forever;
- phase-free C6 orbit shape gives 14 classes, or 13 nonempty orbit types after removing the all-empty background;
- phase-anchored active-bit futures give 2^min(h+1,6) classes, reaching all 64 masks at h=5.

For the declared use-once update (mark the currently scanned channel occupied, then rotate), observing total occupied count through h future ticks gives exactly 2^h*(7-h) classes for 0<=h<=5 and 64 thereafter.

Proof of the latter: the current total plus each successive count increment identifies whether each of the first h scanned bits was initially 0 or 1. Once those h bits are fixed, the unvisited 6-h bits are seen only through their total, which has 6-h+1 possibilities. Hence 2^h(7-h). At h=5 the sixth bit is determined by the total.

Boundary: these are observer/future-language statements. D6 symmetry, C6 symmetry, total-count equivalence and phase-anchored equivalence are distinct quotients and must not be interchanged without a descent certificate.
