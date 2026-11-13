# R762N — Sparse and positively weighted pair observers for signed X6 triads

Research date: 2026-11-13 (Asia/Shanghai). Status: author-side exact theorem and exhaustive integer check; independent review not performed.

Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, unchanged. Taskbook: e01d91db2ad6e45fbfbb8360837cbf78a2bc5e11. Predecessor: R762M PR #2305, research commit a3379bb566cb196d7c50859c57a239cc98815060.

## Model and relationship to P000

Fix one native X6 Cell. Three independently named primitive force-source slots occupy different native axes, with three signed source bits s=(s0,s1,s2) in Q3={0,1}^3. The source names and signed axes remain typed. There are (6)_3=120 injective placements per sign pattern, hence 960 candidate triads. An S6-axis-relabeling-invariant Boolean *candidate* incidence law is any a:Q3->{0,1}, giving 256 laws.

If source j is hidden, the two named source signs t are fixed. The positive N-BRC pair-count observer is B_j(t)=4[a(t,j=0)+a(t,j=1)]. Four is the number of unused native axes for the third source. The twelve orbit-reduced pair counts are the twelve edges of the binary cube Q3, while physical signed visible source pairs give 360 instances under S6 symmetry. R762M established that all twelve pair totals give only 255 distinct signatures, with the complementary even/odd parity laws in a unique double fiber.

This model preserves the P000 starting frame: six native spatial axes, PERP_E of 120 degrees, primitive stable force arity three and typed triadic closure. It assumes neither that every signed incidence is truly admitted by TRIADIC_CLOSURE_E nor any V29/V39 dynamics. An observation theorem here identifies candidate admission *laws*, not source history or force cancellation.

## Theorem 1: exact signatures for an arbitrary sparse subset

Select any subset E of the 12 pair-count channels. Regard E as edges of a graph G=(Q3,E). Suppose its connected components have vertex sizes m1,...,mr. The exact number of different signatures on the full Boolean law set is

N(E) = product over i of (2^(mi)-1).

**Proof.** Two laws a and b have equal observations iff d=a-b satisfies d(u)+d(v)=0 on every selected edge. On a connected component, every vertex can be reached from an anchor along edges. Because the cube is bipartite, d must alternate signs on the two color classes: d=c*chi, with chi the unique sign bipartition and c the anchor difference. For Boolean a,b, c is 0,+1,-1. If c=0, a=b on this component. If |c|=1, both laws are forced to be the two opposite checkerboard indicators. Thus among the 2^mi assignments on a component exactly one unordered pair collides, giving 2^mi-1 distinct observations. Componentwise observations and assignments factor as Cartesian products, proving the formula. This includes an isolated vertex mi=1, whose value is never observed and therefore produces one signature. QED.

**Corollary (sharp unweighted reduction).** Exactly the same 255-signature partition as all twelve channels is obtained if and only if G is connected. Connectivity needs at least 7 of the 12 edges, and every spanning tree of Q3 attains the bound. The exhaustive census yields exactly 384 seven-channel spanning trees. Consequently five of the twelve aggregate channels can be removed for the *law-identification-only* observer with no further identification loss. The parity ambiguity remains. One additional absolute triple-sign bit a(000) distinguishes the two parity laws. Seven unweighted edge channels plus one absolute source-sign query are optimal within this architecture: with at most six edges, G has two or more components, and an absolute query in one component leaves a separate checkerboard ambiguity elsewhere.

Enumeration of all 4096 subsets gives connected-observer counts by edge number: 7 edges:384; 8:408; 9:212; 10:66; 11:12; 12:1. For every subset the verifier directly enumerates signatures of all 256 laws and independently checks the component formula.

## Theorem 2: positive hidden-sign weighting repairs parity with four channels

Fix one named hidden source j=2 and retain its sign as a typed branch property. Assign positive integer weights u to hidden sign zero and v to hidden sign one, identically across its four possible unused axes. The weighted N-BRC count is

W_(u,v)(t)=4[u*a(t,0)+v*a(t,1)], for t in {0,1}^2.

**Claim.** The four values W_(u,v)(t) reconstruct all eight law bits for every Boolean law iff u and v are distinct positive integers.

**Proof.** For fixed t the Boolean pair (a(t,0),a(t,1)) produces exactly one of 0, 4u, 4v, 4(u+v). Positive weights make these four values pairwise distinct precisely when u≠v. The four choices of visible t partition Q3 into four disjoint pairs, so their independent inversions recover every law bit. With u=v the pairs (1,0),(0,1) collide. QED.

The smallest possible maximum positive integer weight is 2, achieved by (u,v)=(1,2) or (2,1). Then each observation belongs to {0,4,8,12}; four quaternary channels reconstruct 256 laws, exactly eight bits of law identity. Within local pair measurements, any channel depends on at most two independent law bits. At least four channels are required to cover eight bits: with at most three channels at least one bit does not influence any observation. Four is therefore sharp for this measurement class, not a claim about unrestricted global nonlinear observers.

Count values have minimum separation 4. Each channel tolerates additive real observation error with absolute value strictly below 2 under nearest-value decoding, recovering the exact law; equality is not guaranteed because of ties. All weights are nonnegative BRC branch masses. No signed or phase cancellation is involved. This weighting is S6-axis-permutation invariant because it is determined by a *named source sign*, not by a selected axis. Invariance under independent axis sign reversal is an additional, unassumed condition.

## Theorem 3: repeatability is conditional on the candidate sign update

Use either parity candidate law a_eps(s)=1 iff sum(s) mod 2 equals eps. Define an explicit *candidate* event transition T_v(s)=s XOR v for a fixed three-bit sign-flip mask v. Keep Cell anchor, axis assignment, named sources and a separate event-history ledger; admit each event only while a_eps(s)=1. This hypothetical update commutes with S6 axis-name relabelings.

**Claim.** Given one admitted event, its identical second application is legal if and only if the flip mask v has even Hamming weight. If v has even weight, every successive application remains legal; if v has odd weight, the first update makes a second identical event illegal.

**Proof.** parity(s XOR v)=parity(s) XOR parity(v). The admission class is therefore invariant precisely when parity(v)=0. Repetition follows by induction; odd parity leaves the accepted class immediately. QED.

The verifier checks both parity laws, all 8 masks and all 8 states (128 combinations; 64 initially admitted, split into 32 legal even-mask repeats and 32 rejected odd-mask repeats). The result displays a precise missing input to the native task: specifying candidate triad incidence alone does not determine whether a post-event repeat is legal. A true TRIADIC_CLOSURE_E implementation must supply an actual Cell/Link/Port update, source history and state-dependent legality predicate; V29 PASS/TRANSFER and V39 frame transport require their real typed mappings rather than analogy to this sign-flip toy update.

## Evidence, reproduction and current unresolved unit

Companions:
- research_artifacts/R762N_SPARSE_WEIGHTED_OBSERVER.py — Python standard-library exact checker.
- research_artifacts/R762N_EVIDENCE.json — deterministic counts, explicit tree channels, arithmetic and scope.
- research_notes/R762N_HANDOFF.md — exact portability and open next unit.

The original local exhaustive checker examined all 4096 edge subsets × 256 Boolean laws, all four-channel weighted signatures, the 7-edge-plus-1-bit observer and all candidate sign-flip cases; all assertions passed. A compact independent checker was also executed and reproduced the same counts. Finite exhaustion proves the 3-source domain; the graph proof establishes its general component formula without relying on numerical extrapolation.

**Next research question.** Under the *actual* frozen X6 source semantics, construct one type-correct TRIADIC_CLOSURE_E event, including named force quantum, Cell, Link, Port, signed branch, state and time. Check first and second applications, S6 covariance and genuinely sourced V29/V39 transitions. If native admission restricts the sign cube, recompute its pair observer fibers; the graph and weighted theorems above provide exact candidate checkers. Preserve provenance, BRC counts, source pins and full accepted/rejected evidence.

Author-side GitHub storage is not native CLAIM, formal Source Result, independent Driver review or Foundation admission. No P000 or ACTIVE worldview mutations are proposed.