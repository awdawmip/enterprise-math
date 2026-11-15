# R762BK — Exact arbitrary-row errors and erasures for the native X6 fixed-Port coordinate observer

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Date: 2026-11-15. Research lineage: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable Task publication TP2-8B7E13C5904A2D6F1142. This is a new row corruption problem continuing R762BJ, not a repeat of its known-erasure enumeration.

## Scientific inputs and observer

Preserve the frozen input from awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. Reuse R762BJ at immutable fe20cdc6efe53b241493d1be775e8ca0725e56bd.

Take a signed native X6 Cell chart z in Z^6 relative to a chosen Cell anchor. For each 2<=i<j<=6 define the *coordinate* Port-1 star observer O_1ij(z)=can3(z_1,z_i,z_j), where can3 subtracts the minimum of the three integer components. Its information is exactly the pair (d_i,d_j), where d_i=z_i-z_1, because the normalized triple and these two differences determine one another. Let H be any subset of the ten named star rows, and G_H the graph on the five leaves {2,3,4,5,6}, with row 1ij represented by edge ij. A corrupt row can contain an arbitrary different normalized triple, and a known erased row is unavailable. Corruption is measured per named *row* rather than per integer component.

These are native Cell-coordinate observations, distinct from a signed force TRIADIC_CLOSURE_E event. The force law, Link, Port and path provenance are not inferred from a coordinate triple.

## Theorem 1: exact minimum distance over the infinite signed alphabet

Define the code C_H: Z^5 -> (Z^2)^H by C_H(d) = ((d_i,d_j))_(ij in H), with Hamming distance equal to the number of differing named rows. Its minimum distance over distinct relative Cell states is

δ(H) = min_v deg_G_H(v).

The code is injective iff δ(H)>=1. For any distinct d and d', let U be their nonempty set of differing leaf coordinates. Row ij differs exactly when {i,j} intersects U, so the row distance is the number of edges incident with U. This is at least the minimum degree of G_H. Equality holds for the pair d and d+e_v, with v a minimum-degree vertex. Thus the equality holds for every signed integral chart, with no bounded alphabet hypothesis.

## Theorem 2: sharp mixed row-error and row-erasure criterion

For all integers t,e>=0, **every** received dataset with at most t arbitrarily corrupted named rows and at most e known erased named rows determines the original relative signed native Cell uniquely if and only if

2t + e < δ(H).

Sufficiency: Every vertex v appears on deg(v) rows. At most e of these are erased and at most t are corrupted, so at least deg(v)-e-t surviving occurrences carry the correct integer d_v; at most t surviving occurrences may carry an erroneous value. The inequality deg(v)>2t+e makes d_v the unique strict majority. Decode each vertex by integer majority, then reconstruct complete z by retaining one common integer depth z_1. The decoder uses only exact integer equality and a linear number of row incidences.

Necessity: Choose a vertex v of minimum degree δ. The valid relative charts d and d+e_v differ on precisely δ incident rows. Under δ<=2t+e, erase up to e of these differing rows and partition the other differing rows into two sets, each with at most t members. Copy the first source's correct row values onto one set and the second source's onto the other; use their identical values elsewhere. The same received dataset then differs in at most t non-erased rows from either legitimate source. Both possibilities have valid normalized-triple row values. Hence worst-case unique decoding is impossible. This proves necessity including δ=0.

## Corollary 1: exact optimal resource thresholds for the six-axis star

For the complete K5 star, δ=4. It corrects any one arbitrary corrupted row, including in the presence of at most one additional known erased row. It detects any 1, 2 or 3 genuinely altered rows with no erasure, and recovers from up to three known erased rows when errors are absent. Two arbitrary corrupted rows are impossible to correct uniformly from any subset of the ten star rows.

The least number of rows for t=1,e=0 is 8. Exactly 15 eight-row families attain it, each the K5 graph with two disjoint edges removed. For t=1,e=1 all ten rows are necessary. The general minimal row count for a fixed (t,e) is the least size of a graph on five labelled vertices with minimum degree at least 2t+e+1. For required degrees 1,2,3,4, the optimal row counts are 3,5,8,10, with 30,12,15,1 distinct optimal graphs. Those optimal-graph counts reuse the exact graph proof from R762BJ.

Explicit sharp 2-error ambiguity: compare d=(0,0,0,0,0) and d'=(1,0,0,0,0). In K5 their ten-row codewords differ on exactly four rows, those containing the first leaf (native axis 2). Construct a dataset that agrees with d on two of those rows and with d' on the other two, using the common readings elsewhere. Its row distance from each codeword is exactly two.

## Corollary 2: exact coordinate consistency redundancy

For m rows with u isolated vertices, the 2m reported integer components have exactly 5-u independently readable relative coordinates and 2m-5+u independent scalar equality constraints. Each nonisolated leaf's repeated reported values must all agree. For the complete K5, the 20 scalar row entries contain precisely five independent relative Cell coordinates and 15 independent consistency equalities.

The recovered relative chart becomes a complete native signed Cell chart only when one common integer depth is also retained. Coordinate-only future operations consisting of simultaneous signed native axis steps and S6 axis relabellings preserve this information, by the already-proved R762BJ descent. However, paths (+E1,+E2) and (+E2,+E1) have the same Cell endpoint and two different ordered BRC branches. The row decoder is therefore a coordinate observer, not a Link/Port/force/history reconstruction algorithm.

## Evidence and verification coverage

The companion Node.js exact-integer verifier enumerates all 1024 subsets of K5 edges and all 496 pairs of 32 binary relative charts for each subset: 507,904 row-distance comparisons. It additionally checks 12,288 graph/mixed-budget cases with 0<=t<=2, 0<=e<=3; 7,872 single-row-error majority-decoder cases; all optimal graph counts; and one exact distance-two ambiguous received dataset. Those are finite crosschecks. The theorems over all signed Z^6 are proved by the incidence and adversarial ambiguity arguments above. No formal checker or independent Driver review was performed.

Run: node R762BK_STAR_ROW_FAULT_VERIFY.js R762BK_STAR_ROW_FAULT_EVIDENCE.json

## Remaining problem

Obtain Source-authenticated native signed-force TRIADIC_CLOSURE_E Cell/Link/Port event admissibility and V17/V29/V39 allowed operations. Define the actual force-incidence observer, then test whether its error/erasure geometry has an analogous distance theorem. Preserve complete BRC ordered path and source history until an exact future-operation-safe quotient is proved. This research unit does not assert an additional native force-closure law.
