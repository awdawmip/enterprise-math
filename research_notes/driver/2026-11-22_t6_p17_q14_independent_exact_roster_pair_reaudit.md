# T6 maximal-p17 q14 split(7,7) — exact nonauthor-code roster/pair re-audit
Date: 2026-11-22 (Asia/Taipei). Researcher/source author remains EM-EMF6D046-5A2844; native Source checkpoint claim MCP-15545e58c653dff063e817f2 and actual session MCP-c618a61189764f23846a391a08518a1a. Existing Driver EM-DVR-DEBB5E performed this fresh implementation and bounded computation; no Source-native independent Review, Result acceptance or claimed T6 global closure. The delegated plan SHA256 b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24 still requires its exact plan path/bytes join before a decisive preparation review.

## Original precise finite domain
Maximal-p17 one-power cofactor atoms (q,r): q integer 1..7, r integer 1..16, a=17q+r, weight w=17a-1=289q+17r-1. Admissible iff all prime factors of a <=17. A signed side is a sorted canonical *multiset* of named atoms (repeats allowed), with sum q = 7 and sum weight <=2331, not an arbitrary set of primes. Opposite-side cancellation requires the *named supports* to be disjoint; global sign exchange quotients unordered pair once. This is a pre-affine vertical descriptor count; no mixed congruence or representative feasibility has been inferred.

## Independent exact finite enumeration
Fresh JavaScript implementation used monotonic-index recursive DFS over all (q,r) atoms (no calls to author Python partition enumerator). At each recursion select atom index i >= previous i (retains repeated named atoms), subtract its q and its exact integer cost, prune if either budget negative, emit exactly when remaining vertical order is zero. The q sums increase strictly, so every finite multiset has exactly one nondecreasing canonical index sequence and is visited once. Apply admissibility factorization by repeatedly dividing a by the ordered primes (2,3,5,7,11,13,17) and requiring final residue 1. Enumerate filtered atoms and the unfiltered 112 literal atoms separately.
Sort generated index arrays numerically and compare the complete 1907 arrays byte-level semantically against the original saved frozen JSON's roster_index_arrays (both array length and every index). Compute 64+-bit arbitrary-precision BigInt bit masks of each roster's distinct named support and count unordered i<j pairs with masks_i & masks_j == 0. Both filtered and literal comparison loops use exact integer semantics.

Results observed:
| Quantity | Independent recomputation | Saved author value |
|---|---:|---:|
| Literal atoms | 112 | 112 |
| Admissible smooth atoms | 60 | 60 |
| Literal side rosters | 8697 | 8697 |
| Admissible side rosters | 1907 | 1907 |
| Unordered admissible disjoint pairs | 809566 | 809566 |
| Unordered literal disjoint pairs (outside filter; diagnostic) | 19582587 | 19582587 |

Every one of the 1907 admissible ordered roster-index arrays exactly matched the original frozen file; its 60 atom list also matched. All 15 q partition class counts matched: (7):8, (1,6):48, (2,5):34, (3,4):40, (1,1,5):89, (1,2,4):164, (1,3,3):122, (2,2,3):103, (1,1,1,4):129, (1,1,2,3):380, (1,2,2,2):164, (1,1,1,1,3):179, (1,1,1,2,2):256, (1,1,1,1,1,2):147, (1,1,1,1,1,1,1):44.
Isolated JS exact computation took 1485 milliseconds in the tool runtime; no floating tolerances, mixed-congruence stage, network code execution or CI.

## Fixed evidence and state
Inputs read from the actual immutable GitHub commit enterprise-math@9ef728a7107362eb0d4b1719ed98d00b1678357c:
- research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_CANONICAL_SIDE_ROSTER_20261116.json (blob 3fb721212af00096d12453035b1cef6e28b45587; saved Source SHA256 242e4872003368905b9355fc666c307a6182482152922b83273708b1a1d07e54);
- T6_P17_Q14_SPLIT7_7_INDEPENDENT_REPRODUCER_20261116.py (blob 23779117e31485a5c5e3fad070013c0a1a2d6099; original source author reproducer, not executed by this JS audit);
- the original _checkpoint.json (blob ec393062611067a56be548813734edb7255b66d6) confirms author completed the q14 roster/pair preflight; its unfinished unit is source-plan join and independent preparation review.
Fresh native current Task read dvr-20261122-0957-t6-current-after114-live-v1 returned SUCCEEDED, observed 2026-11-22 01:59:37 UTC, Source 409dddbe5063e07f3ffb34bb24155f063115ae6c, dispatch NEEDS_DISPATCH, no active owner. Do not take a CLAIM, substitute the Driver for original Researcher or relaunch q0 affine solve.

## Review boundary and next unit
The reported counts and enumerated arrays have now passed a fresh nonauthor-code check. Any native decisive review must independently check original frozen model/plan identity, reader/source provenance, contribution independence, its exact Source Result and permission. Subsequent q0 affine work is not authorized merely by a matching pair count. The remaining T6 global objective and H0/lower-prime work stay OPEN; accepted q1-q4 remain preserved.
