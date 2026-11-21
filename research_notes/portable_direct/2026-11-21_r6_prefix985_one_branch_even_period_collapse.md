# PREFIX-985 — Even-period one-branch collapse (signed-source residual observer)

Date: 2026-11-21 Asia/Shanghai  
Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED_p3_p6 / INDEPENDENT_P4_CHECK / NOT_REVIEWED  
Predecessor: PREFIX-984 (four-phase 8-step versus 4-step cycles)  
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json

## Model

For p≥3, x is an odd p-bit input. A named source (i,j,s), with 0≤i<p, 1≤j<p and s∈{+1,-1}, belongs to nonzero residual c=2^i-s2^j. It is legal iff bit_j(x)=(1-s)/2; the next state is x XOR 2^j, and the phase advances through a fixed L-word. A *singleton phase* has one source port j and its required bit is fixed (mask 1 or 2). Source signs, order, and multiplicities are retained in the named paths; this is an auxiliary model, not a native X6 dynamical system.

## Theorem 985.1 — one-branch even-period collapse

For any even L≥2, suppose L−1 stages are singleton phases, and the remaining stage has any nonempty finite set of eligible named source ports (possibly just one, possibly mask-3 on a port). Then:

1. Every legal 2L-move path from any starting phase already returns to its initial x and phase at move L.
2. Infinite legal paths exist iff an L-step phase-aligned closed path exists.
3. If no such L-step closed path exists, all legal paths, from all phases and odd inputs, have length at most 2L−1.

**Proof.** Rotate to make the chosen starting phase zero. Let F be the union of ports in the L−1 singleton stages, and let D be the XOR of 2^j over those stages. As L−1 is odd, D≠0, and its support is contained in F. Denote the port chosen at the exceptional stage of the *first* period by r. Its total input flip is D XOR 2^r. Choose, for every j∈F, any singleton-stage occurrence requiring a fixed bit at j. The corresponding occurrence in the second period is also reached in a legal 2L-step path, and therefore requires exactly the same bit. The parity of changes to j in the first period must be even. Thus (D XOR 2^r) restricted to F is zero. Because D is nonzero and supported in F, this forces r∈F and D=2^r. All coordinates, including those outside F, have net zero change. Therefore the first L moves end at the exact original x and phase, so repeating those named sources produces an infinite closed path. The converse is immediate. If no L-step return exists, a legal 2L-step path is impossible. Cyclic rotation proves the claim from every starting phase. QED.

The theorem is valid even if the exceptional phase contains several source signs or positive branch weights: the selected named source is preserved, and the proof uses singleton bit consistency rather than cancellation of positive weights.

## Corollary 985.2 — four nonzero residuals

If a four-phase residual word contains at most one residual with two nonzero source ports, then an infinite legal path exists iff there is a 4-step closed path, and every finite path has at most **7** moves. Consequently a genuine 8-step cycle without 4-step return (as in PREFIX-984) requires at least two multiport phases.

The bound 7 is sharp at p=4. Choose w=(4,-1,3,-7), x=3, and ports (1,1,1,3,2,1,1). The exact state sequence is

3 → 1 → 3 → 1 → 9 → 13 → 15 → 13.

The named sources are respectively (1,1,-1), (0,1,+1), (0,1,-1), (0,3,+1), (3,2,+1), (0,1,+1), (0,1,-1). For the next step, residual −7 requires bit_3(13)=0, whereas bit_3(13)=1. Complete graph checking confirms this word is acyclic. The theorem rules out any 8-step path.

## Exact reproducible census

The C++ program PREFIX985_R6_ONE_BRANCH_CHECK.cpp constructs sources directly from c=2^i−s2^j and scans every ordered four-word with 0 or 1 double-port residual, every odd start, and every legal branch through depth 8. “Cyclic” in the table means a depth-8 path exists, which is equivalent to a 4-step return by Theorem 985.1. Starting phase is zero; the proof covers all phases.

| p | eligible words | cyclic | finite | 8-step but no 4-return | maximum finite path |
|---:|---:|---:|---:|---:|---:|
| 3 | 6,144 | 896 | 5,248 | 0 | 4 |
| 4 | 48,384 | 5,160 | 43,224 | 0 | 7 |
| 5 | 291,600 | 19,758 | 271,842 | 0 | 7 |
| 6 | 1,370,928 | 59,324 | 1,311,604 | 0 | 7 |

An independently written Python graph-topology implementation checked all 48,384 p=4 words: exactly 5,160 cyclic and maximum acyclic length 7. All arithmetic is integer exact. The analytic theorem is all-width; the census is p=3..6 only. No independent mathematical review was performed.

## Next question

Treat four-phase words with **at least two multiport residuals**: determine whether arbitrary-width infinite paths always admit an 8-step return and whether the 18-step finite bound from PREFIX-984 persists. A canonical port-overlap reduction must preserve the unique successor pairing of mask type (2,3), the actual arithmetic residual dictionary, and the joint signed-source path. Native BRC/X6 transfer still requires a typed observation/update bridge.

Historical provenance: Researcher EM-DIRECT-FBEA5D; Source Session MCP-45ad6d29cd534c1aad25595a72e3c532; Activity RA-3FB2D033BE6048D8712FF056. This file is scientific Source evidence, not a new CLAIM, PROGRESS, Review, or P000 update. The mother question B_fix,odd(32)∈{19,20} remains open.