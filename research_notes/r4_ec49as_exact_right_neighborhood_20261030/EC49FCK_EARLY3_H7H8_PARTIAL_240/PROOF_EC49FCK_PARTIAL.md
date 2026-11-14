# EC49FCK — 240 early3+H7+H8 five-slot exact rigidity results
Date: 2026-11-06. Classification: AUTHOR_EXACT_FINITE_CHECK / PORTABLE_DRAFT / UNREVIEWED.
Scientific input (frozen): `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Parent EC49FCJ: immutable commit `207334742b28a05cc69d8213c9f279acc48a77ec`; retain its original 24 native signed-X6 words, nine-state automaton and full BRC cache keys L=(4,2,1), M=(7,3,2). Reuse its exact source `frozen_model.py`, Git blob `c21336ba1f3719cfa03b07c3a7e9722e4cd1e84b` under this new directory.

## Exact finite proposition
Let E be the ten H4–H6 slots in their frozen order; H7 and H8 each have four observation-signature slots. Order the 1,920 selected quintets lexicographically by `itertools.combinations(E,3)`, then the H7 signature, then the H8 signature. For **every index i with 0 <= i < 240**, fix the other nineteen frozen word paths and replace precisely the five selected slots by any words from their exhaustive legal candidate pools (same window, observation signature, and full BRC key). The minimum number of distinct native signed-six-axis primitive-prefix edges is **158**.

## Exhaustive proof algorithm
For fixed slots S, let F be the set of all nonempty primitive prefixes on the nineteen unmodified paths. A legal replacement w in selected slot s contributes the exact residual `R_s(w)=P(w)\\F`, where P(w) contains all primitive signed-axis prefixes. Every candidate cost is
`|F| + | union_{s in S} R_s(w_s) |`.
The fixed reference construction has 158 distinct edges and is feasible in each selected group. To rule out a strict improvement set `c=158-|F|` and retain only residual candidates with cardinality <c. Starting from `{empty_set}`, iteratively form every distinct union with the next legal residual and reject precisely unions of size >=c. Because union cardinality is monotone, every rejected prefix is incapable of a later strict improvement. Eliminating duplicate residuals/union states is lossless because all future decisions depend only on the retained set. If the final state family is empty, no 157-or-fewer-edge replacement exists. Otherwise its minimum yields any valid improvement. The program includes the reference 158-edge construction for the upper bound.

The published code implements these operations with integer bitsets, one bit per literal primitive prefix. The reused frozen model builds all 16,156 legal unique words and 109,972 distinct primitive prefixes, and verifies that the fixed witness costs 158. It does not replace signed/ordered path prefixes by endpoint coordinates.

## Actual executed evidence
Batches [0,40), [40,120), [120,180), [180,240) were run with `VERIFY_EC49FCK.py` (the core exact decision algorithm is identical to the executed local program). Every batch reported `minimum=158`, `strict_improvement_groups=0`. Total candidate Cartesian products (pre-pruning): **1,185,137,049,600**, which is not the actual number of set-union operations. Maximum intermediate DP state count: **1,020**. All 240 consecutive indices were covered exactly once and no group has an improved witness. Compact per-index certificate is `EC49FCK_240_COMPACT.json.gz.b64`; decode with `base64 -d | gzip -d`; decoded canonical JSON SHA-256: `9c638ff356336831016082e85c1287d3613b9a000362a60d3c1b9003e72e0a16`. Compressed gzip SHA-256: `60e8da49b844f27fa0f5fe8eae28557a03f04d1c92b7225fa59a605878fb6861`.
An independent literal signed-prefix string-set checker (separate from integer bitset representation) passed **16** indexed groups: 0,1,15,39,40,63,79,119,120,143,159,179,180,199,219,239. Its exact per-group optimum and fixed prefix cardinalities matched the bitset reports.

## Scope and next question
This is a 240/1,920 partial exact result of the EC49FCK H7+H8 quintet neighborhood, not yet a statement about remaining indices [240,1920), six-slot substitutions, alternate legal cache schedules, or the 93-edge full nine-window mother objective. Next resume at [240,1920) using bounded batches or improve residual-state dominance. A candidate with cost <=157 would supersede local rigidity claims for its own group. Independent Driver review and Source Result remain governed by actual authority.
