# Import of the previously local two-phase boundary experiment

Status: IMPORTED_RESEARCH_PROVENANCE / NOT_PROMOTED
Progress-Event-ID: NOLLM-TWO-PHASE-BOUNDARY-IMPORT-20260909-C6C82
Original local event: NOLLM-TWO-PHASE-HEX-CARRY-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Date: 2026-09-09

## Why this is separate

The source already contains nollm_local_carry_field_20260909_c6c82.md, a RIGHT-prefix nested-chain construction with stable labels. The preceding chat also supplied a different LEFT-affine expansion plus even-step folding experiment in nollm_two_phase_carry_bundle.zip. Do not overwrite or merge their matrix conventions. This note preserves the latter's resumable content and source hashes; its original large boundary run was not rerun during the mixed-5/7 continuation.

## Recovered local artifacts

SHA256:
- research_note.md: 427439eb28d48037bc345f09689e72bbd2b6f2b9eac9e611d9a600eef35a2831
- core_results.json: d43e7cae5076fef4cf13bf39f046273b815dc14a694ea9a5231825137ad7978c
- core_experiment.py: 5ae9fae6373c390b27df740fcb2ad1fe70befb9577f9d4f0f7cbdad731f8633d
- reproduce_local_carry.py: 491cae426bb4a2ce4e6d780649195ec08cbe54c343e82a2934110ddd4ca845a6

These were read from the user-visible prior bundle. Hash identification is provenance, not independent verification of every claim in those files.

## The distinct construction

Use M=[[2,-1],[1,2]], N=[[1,-2],[1,3]], W=[[0,-1],[1,1]], with NM=5W. At both phases use D={(0,0),(1,0),(-1,0),(1,-1),(-1,1)}. Expand by x -> Mx+d, then x -> Nx+d. At even step 2t fold the result to the canonical nearest representative modulo m=5^t. The Voronoi inequalities are |2q+r|<=m, |q+2r|<=m, |q-r|<=m; on an equal-distance side retain the representative with positive oriented determinant of its outward lattice normal and its coordinate. Since gcd(m,6)=1 there is no integer vertex or midpoint ambiguity.

The original derivation gives m^2 distinct representatives, C6 symmetry and no missing integer sites inside the convex hull at every even step. Quotient compatibility, not positive-mass cancellation, makes the folding reversible. This changes fine-plane coordinates, unlike the separately persisted stable-address right-prefix model.

## Preserved finite observations and unresolved pattern

Full expansion through depth eight recorded 5^k distinct points. Even-depth carry counts at depths 2,4,6,8 were 4,76,340,1756. Boundary-only counting at depths 10,12,14,16 recorded 8740,43756,218740,1093756. The largest run examined 234372 boundary parents, not all 152587890625 states at depth sixteen.

The completeness argument for the boundary search is: macro digits B=D+ND have hex gauge at most 7. With previous period s, a parent of gauge <=s-2 produces children of gauge <=5s-3, strictly inside the next cell. Only the gauge-s and gauge-(s-1) strips can carry. Consequently the carry fraction is O(1/s), under this declared construction. Movement is one adjacent COARSE period in the observed runs, not one finest-lattice step.

The eight recorded scales match C_t=14*5^(t-1)-2+8*(-1)^t. The original record explicitly leaves this fine closed formula CONJECTURAL; preserve that status. The boundary order bound is a separate derived statement.

Additional original controls: radius-2 digits could make a frozen old endpoint rounder (axis ratio 1.105223841305) while reducing hull occupancy to 0.467332487100. For the fixed old eight-step matrices with bounded independent radius-1 digits and no carries, the pulled-back future covariance tail after the first block has trace at most 74203/38146875000; after the old compact prefix this prevents later block-boundary axis ratio from dropping below approximately 1.726342975873. These are explicitly frozen-prefix/observer statements, not general no-go results for adaptive carries.

## Continuation

The current mixed-5/7 note uses the VERIFIED source right-prefix nested chain, not this left-prefix carry clock. Its CRT refinement diamonds therefore do not automatically extend the boundary count formula above. Investigate that extension only after specifying which carrier and representative rule is being transported. This import closes loss-prevention capture for the historical local frontier; it does not retroactively mark an unperformed replay as executed or grant mathematical acceptance.
