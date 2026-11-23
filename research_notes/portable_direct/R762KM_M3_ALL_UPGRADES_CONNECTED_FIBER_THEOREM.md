# R762KM — Universal connected fiber sum and exact provenance budget for all upgraded M3 cube subsets

Date: 2026-11-23. Status: AUTHOR_ANALYTIC_PROOF + EXACT_FINITE_CHECKED / NOT_REVIEWED.
Role: independent informed TASK_RESEARCH portable continuation; historical R762KL attribution is EM-X6-B1684F / RA-6F2C09233DC4F142A2F7795A, not a claim of an authenticated RUN in this conversation.
Scientific predecessor: awdawmip/enterprise-math@39c2d4037949102f2bdd249a7f66aadd34b53e44:research_notes/portable_direct/R762KL_M3_CONNECTED_FIBER_CENSUS.md
P000 frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json

## Exact model and counting convention

This is the **unsigned auxiliary six-axis M3 Port–Euler observation model**, with inactive Ports 01,23,45 and active Port order
02,03,04,05,12,13,14,15,24,25,34,35. The twelve forced three-axis supports have a single legal internal edge type each and strictly positive integer multiplicities. Their aggregate twelve-bit GF(2) boundary is any element b of the 512-element subspace F (even parity independently within each of the three four-Port components A,B,C). The eight flexible cube supports in order are 024,025,034,035,124,125,134,135. Each has the three legal edge types AB,AC,BC, with actual Port endpoints determined by the support's cube coordinates.

Choose any subset U of the eight flexible supports. Supports in U each occur **twice**, represented by an **unordered multiset** of two legal edge types (six possibilities, including repeats). Each support outside U occurs once (three possibilities). Thus the full inventory has 20+|U| events if forced supports occur once; arbitrary positive forced multiplicities change that total but do not change the fiber classification below. The count distinguishes support-indexed edge multisets, not the ordering of two events on a repeated support.

For b in F, let Q_U(b) count support-indexed choices with total flexible boundary b and a connected graph after adding all positive-multiplicity forced edges. Connectivity is equivalent to using at least two quotient edge types among AB,AC,BC.

## Theorem KM.1 — location-independent exact connected total (analytic proof)

For **every** U with k=|U| (k=0,...,8), the total number of connected, forced-boundary-compatible choices is independent of which particular supports are upgraded:

    C_k = sum_{b in F} Q_U(b)
        = 2^k (3^8+3)/4 - 3       if k is even,
        = 2^k (3^8-3)/4           if k is odd.

Proof: The twelve forced edges form connected four-cycles on each of A,B,C, and their GF(2) boundary span F is exactly the subspace with even parity on each component. On the three-vertex quotient A,B,C, a flexible edge is of type x=AB, y=AC, or z=BC. A flexible boundary belongs to F exactly when the three *type occurrence counts* have the same parity. Since the total flexible event count is 8+k, the required parity vector is (0,0,0) for even k, and (1,1,1) for odd k.

Compute in the integral group ring Z[(Z/2)^3], where x²=y²=z²=1. A single flexible support has generating polynomial S=x+y+z. A doubled support, with unordered edge multisets, has polynomial D=3+xy+xz+yz. Its three equal-type choices produce the constant 3; each of the three distinct-type pairs produces one mixed term. The whole parity enumerator is S^(8-k) D^k. The desired parity coefficient can be extracted by the exact eight-character Fourier average on the group. At the two characters where all three signs agree, the signed contribution is 3^(8-k)6^k each. At the six mixed-sign characters it is +2^k for even k and -2^k for odd k. Hence the parity-compatible count is 2^k(3^8+3)/4 for even k or 2^k(3^8-3)/4 for odd k.

A quotient graph on A,B,C is disconnected exactly when every chosen event edge has the same quotient type. There are three such configurations (all x, all y, all z). They are parity-compatible only for even k, so subtract exactly three in that case. All required forced components are internally connected and all involved vertices have positive degree, completing the proof.

This is a symbolic identity over the full declared model, not an extrapolation of the finite census.

## Theorem KM.2 — complete 256-subset fiber census (exact computation)

For each k, exhaustive 12-bit GF(2) boundary/type-mask DP evaluates Q_U(b) for all C(8,k) labeled U and every b in F. The independent character formula above verifies every connected total C_k. Direct tuple enumeration separately verifies the complete per-boundary distribution for U=empty, {024}, {024,025}, {024,135}.

| k | # U | reachable b per U | C_k per U | distribution of minimum positive Q_U (min: number of U) | largest Q_U across U,b |
|---:|---:|---:|---:|---|---:|
| 0 | 1 | 465 | 1638 | 2:1 | 8 |
| 1 | 8 | 495 | 3279 | 2:8 | 12 |
| 2 | 28 | 508 | 6561 | 2:28 | 37 |
| 3 | 56 | 512 | 13116 | 2:24, 3:24, 6:8 | 80 |
| 4 | 70 | 512 | 26253 | 4:6, 6:32, 7:24, 8:6, 9:2 | 204 |
| 5 | 56 | 512 | 52464 | 26:24, 30:24, 39:8 | 351 |
| 6 | 28 | 512 | 105021 | 48:12, 54:16 | 987 |
| 7 | 8 | 512 | 209856 | 176:8 | 1096 |
| 8 | 1 | 512 | 420093 | 288:1 | 7197 |

**All 256 upgraded subsets have no unique connected fiber**: whenever Q_U(b)>0, Q_U(b)>=2. For k>=3 all 512 boundaries are reachable, rechecking the earlier three-upgrade existence threshold with explicit stronger multiplicity data. Among four-, five-, six-, seven- and eight-upgrade patterns, the minimum positive fiber grows respectively to at least 4,26,48,176,288. These are finite exhaustive conclusions, not additional analytic formulas for individual fibers.

## Corollary — exact residual/observer lower bounds in this auxiliary model

Let the coarse observer keep the full support multiplicity inventory, twelve forced-boundary bits and connectedness (but discard which legal edge multiset occurred on each flexible support). For fixed U and boundary b, any lossless provenance annotation distinguishing all possible legal source assignments must have at least ceil(log2 Q_U(b)) bits in a binary fixed-length representation at that b. A single fixed-width annotation valid for every reachable b at this U requires at least ceil(log2 max_b Q_U(b)) bits.

Across each k, the largest such required bit widths among its labeled U are 3,4,6,7,8,9,10,11,13 bits for k=0,...,8. In particular, at k=8 and b=0, Q_U(0)=7197, requiring 13 bits even though the coarse parity and support counts are fixed. This is a provenance-fidelity benchmark for assessing proposed compressed observers, not a claim about the yet-unproved native signed/BRC transfer.

## Exact verification and next frontier

Run the companion standard-library Python script R762KM_M3_UPGRADE_FIBER_VERIFY.py. It enumerates the 512 forced boundaries, checks the 256 labeled upgraded subsets, validates every C_k against the analytical formula, compares four whole per-boundary spectra against independent direct tuple enumeration, and prints R762KM_M3_UPGRADE_FIBER_EVIDENCE.json. All assertions passed in the local run on 2026-11-23; the JSON stores the complete k-level census.

Remaining mathematical questions: obtain a non-enumerative formula for the finer fiber spectrum Q_U(b) (especially k=1,2 and the three distance classes); characterize shortest sufficient source residual coordinates, and establish a typed bridge preserving signed TRIADIC_CLOSURE_E, event order, native Cell/Link/Port updates and BRC source branches. Shared Task CLAIM/PROGRESS and independent review have their separate authority; this notebook does not report either as completed.
