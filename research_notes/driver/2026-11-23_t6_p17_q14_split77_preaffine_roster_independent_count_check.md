# T6 p17 q14 split(7,7): nonauthor exact count/readback check

Date: 2026-11-23. Checking Driver: `EM-DVR-DEBB5E`, original SID `MCP-9b4714dc46b948afa4875a86c89c713c`. This is a separately executed **finite mathematical count check** under directed/shared context, **not** a clean-blind independent review, formal Native Driver Review, Result admission, or new q14 research CLAIM. Original roster/preflight author: `EM-EMF6D046-5A2844`; prior T6/q1–q4 contributors retain their historical credit.

## Exact source and domain

Frozen Source checkpoint: [own original researcher checkpoint](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/_checkpoint.json).

Frozen canonical [q14 roster](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_CANONICAL_SIDE_ROSTER_20261116.json) has Git blob SHA-1 `3fb721212af00096d12453035b1cef6e28b45587`, and its original manifest claims SHA-256 `242e4872003368905b9355fc666c307a6182482152922b83273708b1a1d07e54`. The immutable GitHub fetch and content parse succeeded; this check uses the returned immutable bytes, without recopying or changing the author's record.

For each side, enumerate multisets of *named* atoms `(q,r)` where `q=1,...,7`, `r=1,...,16`, `a=17q+r` has no prime factor greater than 17, and `sum q=7`. Each atom contributes the exact exponent mass `w=289q+17r-1`. The side budget `sum w <= 2331` is equivalent to `sum (17r-1) <= 308`. Repetitions on one side are allowed; opposite equal atoms cancel, so admissible pairs must have disjoint named supports; positive/negative exchange is identified once.

This verifies the finite **pre-affine vertical-descriptor domain** only, using the declared maximal-p17 cofactor rule.

## Separate exact enumeration

A new in-turn JavaScript integer computation reconstructed `(q,r)` atoms in lexicographic order and used trial division by exactly `2,3,5,7,11,13,17` for the smoothness predicate. It generated multisets by monotone index DFS with state `(minimum_atom_index, remaining_q, remaining_budget)` and counted each completed `remaining_q=0` leaf. Unlike the author's published partition-by-q reproducer, no integer-partition generator was used in this check.

It then compared the **entire 1,907-element ordered array of index arrays** element-by-element, via exact serialization, against the frozen canonical file. For each profile, it built a BigInt support bitmask, retaining duplicates in the original roster. All pairs `i<j` were enumerated; disjointness was tested exactly by `(mask_i & mask_j) == 0`.

| Quantity | Independently recomputed |
|---|---:|
| Literal atoms before smoothness | 112 |
| Smooth admitted atoms | 60 |
| Literal budget-feasible single-side profiles | 8,697 |
| Admitted budget-feasible single-side profiles | **1,907** |
| Unordered disjoint-support admitted pairs | **809,566** |
| Ordered sign pairs | 1,619,132 |
| Literal unordered disjoint-support pairs (outside-domain diagnostic) | 19,582,587 |
| Canonical atom list matches actual immutable file | **yes** |
| Complete canonical side-roster index arrays match | **yes** |
| All six reported count values match canonical record | **yes** |

Each side has at least one atom (`sum q=7`), so a disjoint pair cannot be equal to itself; the exchange involution has no fixed point. Thus the ordered signed-pair total is exactly twice the unordered total.

The separate count establishes the stated finite enumeration and frozen roster byte-level semantic content, **not** affine mixed-congruence feasibility. The existing author's [Python reproducer](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_INDEPENDENT_REPRODUCER_20261116.py) is a further reproducible implementation; this turn did not run that file or claim a measured 120-second/1-GiB performance certificate.

## Decision and preserved frontier

**Count check: PASS for the declared (7,7) side-roster and disjoint-pair enumeration.** In particular, no loss of composite-cofactor names, side repetitions, or budget constraints was observed in the frozen roster. This is a nonauthor computational checking step with shared prior context; do not relabel it as an independent blind review or accepted Result.

The author's preflight still calls for joining the immutable q14 delegation-plan digest `b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24` to its exact Source bytes and verifying the complete design and actual specified resource run. Preserve the original q14 Researcher owner and existing native CLAIM. The next downstream scientific unit remains the exact mixed-congruence q0 affine preflight if the current owner is authorized and its frozen preparation requirements are met. Global `T6=2332`, p19 orders 9–12, lower primes, H0 and lower-prime completion remain open at their separate prior scopes.

No mutation of Task owner, immutable Result, native Review, Activity, or scheduling was performed by this note.
