# X6 R242 — closure of every real reducible quadratic as the sole nonlinear root

2026-11-26. AUTHOR DERIVATION + COVERAGE AUDIT / NOT_REVIEWED. Frozen Port 10, 1935 integer directions, six-pair BRC, weights (17t,B,22t,D)>0, strict 3/2 near set and legal optimum, 47 necessary supports and 49 components. Auxiliary coefficient chart, P000 V5 unchanged. Informed unclaimed research; native read r2-20261126-2008-x6-read, Source dca8f0a50de4fd8b3d2ca325b379c41023198f30, NO_CANONICAL_PUBLICATION_DIRECTORY (no owner projection). Researcher binding unconfirmed. No shared task mutation.

## Theorem
Conditional on the inherited necessary-wall premise and rank-three complete linear germ partition enumeration, no correct depth-six binary tree for this frozen output problem can use a real reducible homogeneous quadratic Q=LM as its only nonlinear query at the root, followed by arbitrary real linear queries. Here L,M are arbitrary real nonzero linear forms, with no restriction to necessary supports. In a normalized positive chart this also covers products of arbitrary real affine forms.

Proof. If either factor is proportional to a necessary support, apply R238. Otherwise every directed germ of the base bank has nonzero eventual sign under both factors, and their root partition is the XOR (up to complement) of their full linear masks. R239 exhausts the unordered factor pairs and direct plus one-step capacity screens. R240 exhausts the full depth-five pure-linear suffix relaxation on every survivor. Exactly three coarse masks remain, each of multiplicity one. R241 refines all 49 intervals at their positive projective midpoint, projects the endpoint germs to the original bank and recovers the three unique unordered coarse factor pairs. The fine factor groups have sizes (1,3),(5,3),(1,1), yielding 19 fine root partitions, all excluded by exact pure-linear suffix recursion. Every true root in one of the three coarse residual classes induces one of these refined partitions, by exact eventual sign preservation and complete linear bank enumeration. Thus there is no remaining real product root. QED.

Corollary: Any successful unique nonlinear root of degree at most two must, after homogenization in three variables, have a nonsingular indefinite real symmetric coefficient matrix. A rank-two indefinite quadratic factors into real linear factors; rank-one or semidefinite forms have only one strict sign away from their zero set. Since a degree-two nonzero form vanishes on at most two distinct necessary supports, at least 45 supports still require one pure-linear depth-five branch (capacity 31); impossible. The zero polynomial or constant query cannot help because it supplies no split. Nonsingular indefinite forms are not declared feasible; their exclusion is open. This corollary concerns the root only, not an arbitrary internal placement. Unrestricted K6 remains in [1,2].

## Coverage readback
All four immutable sources below were read, output summaries parsed and pair counts reconciled without recomputing the mathematics. R239 initial 2372931 pairs = 2296890 direct + 55868 next + 20170 full recursive + 3 refined coarse pairs. R241 3+15+1 fine pairs, 19 excluded, no cutoff. The former support-factor family R238 remains closed within its inherited evidence scope. The figures are discrete partition counts, not a probability on the continuum. The three new computational rounds count 79278995 checks (exact sum of new child/suffix/refinement checks; direct pair loop counted separately); no new full-direction scoring. This is author coverage audit, not independent scientific review.

```json
{"factorPartitions":2178,"totalPairs":2372931,"excludedDirect":2296890,"excludedNext":55868,"excludedRecursive":20170,"finalCoarsePairs":3,"refinedPairs":19,"refinedExcluded":19,"unresolvedCoarsePairs":0,"allChecks":79278995}
```

Sources and observed blob IDs:
- a64888948bdacb5ba4e691d3eb2b783ed43f56ea:research_notes/portable_direct/2026-11-26_r2_x6_r238_one_support_factor_root_family_closure.md (blob 9b05af42eef4b4351130e2a6f8a53f8995b749e9)
- 13b49598c381b21e899704d21e8498071c852565:research_notes/portable_direct/2026-11-26_r2_x6_r239_factor_free_reducible_root_xor_capacity.md (blob 71121d6188c86a4971cd4b0d69defcc617ac24b6)
- 4bc3061af929f51a8dca388738fe3d3a6dc957d6:research_notes/portable_direct/2026-11-26_r2_x6_r240_factor_free_reducible_suffix_capacity.md (blob 59bdf24e772dfd65958aec0bd92c29025df52bb2)
- 0019f97b2d329305c963ddfd6ec8ea622bbd7e15:research_notes/portable_direct/2026-11-26_r2_x6_r241_reducible_root_midpoint_refinement.md (blob 55e1be57f6923e6b00076442d26d5c49fb89c2e7)

Next: restrict the six-coefficient R233 lifting to nonsingular indefinite forms; design a lazy exact sign feasibility and linear suffix exclusion strategy rather than enumerate a Cartesian product of ternary signs. The sole nonlinear observation below linear ancestors remains separate. Activity association and independent review pending.
