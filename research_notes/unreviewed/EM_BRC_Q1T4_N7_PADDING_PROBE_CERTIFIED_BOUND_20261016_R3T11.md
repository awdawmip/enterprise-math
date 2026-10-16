# Enterprise Math / BRC Q=1,T=4 — seven-source padding probe and quotient bound (UNREVIEWED)

Date: 2026-10-16 (Asia/Shanghai). Status: SELF_CHECKED_EXACT_FINITE / UNREVIEWED / NO_NATIVE_CLAIM / NOT_ADMITTED. This is an auxiliary positive-support labeled-source BRC model, NOT a theorem about native six-dimensional P000 dynamics.

## Frozen inputs and control status

- GLOBAL_KNOWLEDGE_V1 canonical main e65113bf772ba7579ce9a04be9aeeb3e63e68c76; account bootstrap/manual, Enterprise Math router, original P000, ACTIVE worldview, BRC method reviewed at this immutable ref.
- Enterprise Math source input main df5869771ff760a0b57a5d757934f0ab9f56f07e. Existing exact finite predecessor: f7bf02298376084b246985017dc00cd4e585f867, research_notes/unreviewed/EM_BRC_Q1T4_N5_COMPLETE_N6_FIRST_PROFILE_COLLISIONS_20261016_R3T11.md.
- Native task inventory/dispatch attempts: CONTROL_QUOTA. Native session_start attempted: STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No verified current active Owner, service-issued Researcher identity, CLAIM, Research Activity or Result/Driver review. This file is an author-origin unreviewed branch note, not a canonical state-machine result.

## Observation lease

n=7 labeled sources with nonnegative integer remnant masses a_i, clipped exactly to 0..4. Public operation G_j secretly resets ANY i!=j to zero, including already-zero/reset sources; the public feedback bit AFTER the action is b=1[sum remaining >=4]. Initial feedback is absent. An adaptive finite public-feedback policy may stop. Its terminal result Safe=1 means ALL positive-support secret histories have remaining sum >=1. Comparing all finite policies gives adaptive equivalence ~. No branch counts/weights/signed amplitudes are being inferred.

A complete STATIC subset profile records for every survivor mask S the pair (1[sum_{i in S}a_i>=1], 1[sum_{i in S}a_i>=4]). Static-profile equality implies adaptive equivalence but can be strictly finer.

## New twenty-pair seven-source classification

Use the four six-source blind generators:

1. (112233,121233)
2. (112234,121234)
3. (112233,221133)
4. (112234,221134)

For each, append the same last mass c in {0,1,2,3,4} to both states. Exact unbounded directed public-belief graph search was done in BOTH X-safe/Y-unsafe and Y-safe/X-unsafe orientations. The result for ALL FOUR pairs:

| appended c | exact observation | full closed-belief nodes per direction, generators 1/2/3/4 |
|---|---|---|
| 0 | permanently equivalent | 361 / 430 / 361 / 430 |
| 1 | distinguishable, SHORTEST depth 7 in BOTH directions | separating spines at step 7 |
| 2 | permanently equivalent | 348 / 460 / 349 / 461 |
| 3 | permanently equivalent | 346 / 458 / 346 / 458 |
| 4 | permanently equivalent | 458 / 457 / 458 / 457 |

Thus there are 16 certified blind padded pairs and 4 certified depth-seven distinguishable padded pairs. No finite horizon restriction was imposed on blindness assertions. The profile contrasts remain real by restricting to subsets not containing the new source.

For X=1122331 safe vs Y=1212331 unsafe, one seven-step spine is:
    G_0:1, G_0:1, G_0:1, G_0:0, G_1:0, G_1:0, G_1:0.
On ANY bit not indicated, STOP immediately. The reverse orientation uses:
    G_0:1, G_0:1, G_0:1, G_0:0, G_2:0, G_2:0, G_2:0.
All secret-choice paths in the claimed safe state were replayed; each unsafe state has a counterhistory. Breadth-first search and an independent Python frozenset search both give minimal depth 7. For all four c=1 examples, the independently coded search agrees in BOTH directions.

**Scientific interpretation:** feedback observability is nonmonotonic under equal addition of one labeled source: appending mass 1 unlocks a previously blind distinction; appending 0,2,3,4 does not for these 4 base cases. This is a finite n=7 statement, not a universal padding theorem.

## Rigorous new seven-source quotient upper bound

Full exact static census over all 5^7=78,125 clipped states and every 2^7=128 subset yields P_7(1,4)=42,949 STATIC threshold profiles. This matches the predecessor symbolic formula. Each of the 16 confirmed permanently equivalent pairs remains equivalent under SIMULTANEOUS label permutation; every action G_j and hidden-choice history is carried to its relabeled counterpart.

Generate all 7!=5,040 label permutations for each of the 16 blind pairs and join corresponding static-profile vertices by an edge. This yields:
- 80,640 raw input edge occurrences; 11,235 DISTINCT undirected profile edges;
- union-find induces EXACTLY 3,367 profile component mergers;
- generated component sizes: 38,959 singleton components, 560 components of size 6, and 63 components of size 10;
- number of generated components = 38,959+560+63 = 39,582.

Every generating edge relates actually adaptively equivalent states and all static-profile fibers are themselves equivalent; by transitivity, the true adaptive quotient must be COARSER than this generated partition. Therefore:

    A_7(1,4) <= 42,949 - 3,367 = 39,582.

This is a certified **UPPER BOUND ONLY**, NOT a full A_7 count. Additional undiscovered blind pairs can cause further merging. The 560 size-six and 63 size-ten components are exact only for the equivalence relation generated by the specified 16 seed orbits.

## Exhaustiveness argument

Represent each reachable remnant by a 7-bit survivor mask (128 possibilities). Every public belief is a finite set of masks. Action G_j enumerates ALL i!=j and partitions next masks into feedback 0 and 1, preserving zero/reset-source repetitions. A belief is unsafe iff it contains a mask with total 0. Any policy that is X-universally-safe but Y-has-an-unsafe-history has an unsafe Y feedback spine: stop immediately on all deviating feedback branches. Such prefix stops preserve X safety because reset mass is monotone nonincreasing: an X unsafe prefix would force an unsafe leaf of the original policy. Hence breadth-first graph search over PAIRS of public beliefs, retaining only actions with BOTH X-bit successors safe, is complete for policy separation. A Y-bit successor containing a zero-mass remnant is a separator; otherwise continue on the corresponding paired belief. If the finite graph closes with no separator, no finite adaptive policy separates. Repeat with X/Y reversed. Breadth-first order proves minimal length when a separator is found.

Independent implementation paths: (a) C++20 packed 128-bit survivor-belief BFS for all 20 pairs, plus C++ four-word static profile + DSU bound; (b) Python frozenset belief BFS with separate reset map and Python arbitrary-precision integer static-profile census/DSU. All 20 verdicts and closed-graph node counts match; both bound computations agree at P7=42949, 11235 distinct edges, 3367 merges and 39582 upper bound. Arithmetic is exact; no floating-point thresholding.

## Evidence manifest / preservation

Portable evidence bundle:
    EM_BRC_20261016_Q1T4_N7_PADDING_PROBE_CERTIFIED_BOUND_EVIDENCE.zip
    SHA256 d95009f89a068c2df08b4f572c96a63faacbbc22398265a6e26ae531c23a212b

It contains a longer technical note, both exact C++20 sources, both independent Python programs, per-pair results, validation_summary.json, hash manifest and logs. At publication, this ZIP and executable source scripts are preserved in the conversation artifact store, **not** asserted uploaded to Enterprise Math Source. The present Markdown is the actual Source branch persistence.

## Next precise research unit

Test whether there is a new n=7 permanently equivalent pair of different static profiles not generated by the above 16 padded seed orbits. Such a witness would strictly sharpen A7<=39582. Start from the 560 six-profile and 63 ten-profile generated components with a source-label-symmetry-reduced search; retain exact certificate and independent replay. If no additional relation is found with a full and bounded search, attempt complete seven-source class counting only with explicit exhaustion evidence. H_7 and equality in the present upper bound remain OPEN. Independent Driver review and native Source registration are pending; no Working Truth/Foundation/P000 change is claimed.

BRC method reuse: existing cutoff-subset profile and single-unsafe-feedback-spine law REUSE_APPLIED; six-source public-belief search EXTENDED to seven-source 128-bit masks, with independent exact Python crosscheck. No new top-level BRC family is claimed.
