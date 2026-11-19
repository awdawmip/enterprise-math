# R762FZ — The K4 STAR frame is the exact missing symmetry datum for candidate X6 triadic BRC rotation

Date: 2026-11-19. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, frozen publication TP2-8B7E13C5904A2D6F1142.
Status: AUTHOR_PROVED / FINITE_EXACT_VERIFICATION_PASS / NOT_REVIEWED.

Scientific input remains frozen at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, corresponding signed X6 Cell torsor, and immutable taskbook @857280d1012943290d141d1317179c40ec3cbdf8. Current normative rules do not change those pins. Antecedent: R762FT oriented 3-cycle obstruction; R762FU unique inverse-paired BRC kernel; R762FX four STAR A6 generation; R762FY three STAR A6 generation, PR #2800@2ac181d4a588824f03c53b28072c594f47bf4f49.

## Question and exact model

The six native axes remain six distinct signed spatial directions, and a permutation of their labels belongs to the established S6 *kinematic skeleton*. The FCC/K4 STAR carriers, in contrast, identify those six axis labels with the six edges of an auxiliary K4; the four STAR triples are the sets of three edges incident to each K4 vertex. An auxiliary frame is not a seventh spatial axis or an admitted physical event.

Let X={1,...,6}. Let C be the set of 20 unordered 3-subsets of X and let C+/- be the 40 oriented 3-cycles whose support has exactly three axis labels. For a four-STAR family F, define B(F) as its eight oriented branches (both inverse 3-cycles on each STAR), and let K_F be the positive BRC kernel with weight 1/8 for each *source-named* branch. For a marked family (F,m), where m is one excluded STAR, let B(F,m) comprise the six oriented branches from the three retained STARs and weight each 1/6. Under permutation sigma in S6, F and m are transported by their axis labels; the BRC branch identities and ordered histories are retained.

## Theorem A — exact orbit/stabilizer and symmetry obstruction

The 720 permutations of X act transitively on the 20 unoriented triples and on the 40 oriented 3-cycles. Therefore an S6-invariant nonnegative normalized kernel on these oriented 3-cycles has weight exactly 1/40 on each. Its support is necessarily either all 40 (for a probability kernel) or empty (for an unnormalized invariant subset). In particular, the six-branch three-STAR and eight-branch four-STAR kernels cannot be unframed S6-invariant nonzero probability kernels.

Let F0 be the four K4 vertex STAR triples carried by an identified edge frame. Its stabilizer in S6 has order exactly 24 and is the induced K4 vertex-permutation group S4. Consequently the orbit of F0 has 720/24=30 distinct unmarked four-STAR frames. If one STAR is marked as excluded, its stabilizer has order 6 and there are 720/6=120 distinct marked frames, with six oriented branches each.

For a *fixed* F0, S4 acts transitively on its eight oriented STAR branches. Hence the unique S4-invariant normalized kernel supported on all eight is uniform 1/8. No proper three-STAR support of F0 is S4-invariant: S4 acts transitively on its four STARs. After choosing and retaining an excluded STAR m, the stabilizer S3 acts transitively on the six retained oriented branches; hence the unique marked-frame-stabilizer-invariant normalized kernel is uniform 1/6.

**Proof.** S6 transitivity on unordered triples is immediate by relabeling; the stabilizer of an oriented 3-cycle consists of rotations of its three moved symbols (order 3) and arbitrary permutations of the three fixed symbols (order 6), so the orbit has 720/18=40. An invariant probability measure is constant on a transitive finite orbit. For the K4 frame, any axis permutation preserving its four STAR triples induces a permutation of the four K4 vertices, since each edge label is the unique intersection of the two STARs at its endpoints. Conversely every K4 vertex permutation induces such a six-edge permutation. Thus the stabilizer is exactly S4 of order 24, giving 30 frames. Marking one STAR restricts to the order-six subgroup fixing its associated vertex, yielding 120 marked frames. In S4 the stabilizer of a chosen vertex is S3, whose full action on its three incident K4 edges reverses the orientation of a cycle when two edges are interchanged; S4 is therefore transitive on 4x2=8 oriented STAR branches. With a marked excluded vertex, the order-six S3 transitively permutes the three other vertices, and its subgroup fixing one retained vertex has a transposition that reverses the orientation at that vertex. Its orbit is all 3x2=6 branches. The invariant-weight statements follow. QED.

## Theorem B — frame-dependent covariance and uniform marginal

The family-valued kernel is exactly S6-equivariant:

  sigma_* K_F = K_(sigma F), and sigma_* K_(F,m) = K_(sigma F,sigma m),

where sigma_* relabels the axis support and acts by conjugation on oriented 3-cycles, including possible orientation reversal. The same identity holds letter-by-letter for source-named signed-axis BRC words and for the candidate affine Cell/Link transport of R762FT; path order, signed flags, source IDs, multiplicity and positive branch weights remain typed and uncollapsed.

When the 30 four-STAR frames are uniformly averaged and the frame coordinate is then **explicitly pushed forward to the branch endpoint observer**, every unordered triple appears in exactly six frames and every oriented 3-cycle has total weight 6/(30x8)=1/40. Likewise, among the 120 marked frames, each unoriented triple appears among the three included STARs exactly 18 times, giving each oriented branch weight 18/(120x6)=1/40. Both unconditional marginals are the uniform 40-branch kernel R762FV. This is an identity only of the declared branch marginal; it is not a safe quotient for arbitrary future frame/source-dependent operations.

**Proof.** Relabeling transports each STAR triple to the corresponding triple and each of its two 3-cycles by conjugation. It bijects the eight (or six) equally weighted source branches, proving covariance. S6 acts transitively on 20 triples, so each triple occurs equally often among all 30x4=120 unmarked incidences, exactly 120/20=6 times. Each is included in 3 of 4 markings of its frame; therefore the marked incidence count is 6x3=18, in agreement with 120x3/20. Both orientations are present per incidence, proving the two stated weights. QED.

## Corollary — symmetry price of the three-STAR reduction

The R762FY six-branch three-STAR kernel is algebraically sufficient to generate A6 **after a frame and excluded STAR are fixed**, but it breaks the original unmarked S4 atlas symmetry if the marking is discarded. The R762FX eight-branch four-STAR kernel is S4-invariant for a given frame, but still breaks S6 invariance unless the frame is included in the transforming state. A conditional frame carrier admits 30 states (minimum 5 fixed-length bits), and a conditional frame plus excluded-STAR carrier admits 120 states (minimum 7 bits), when the entire exact frame identity is an observable/relevant attribute. Averaging these states recovers the unframed 40-branch kernel but does not prove that frame provenance is irrelevant to later legal-event tests.

Consequently, for an **unframed, sign-independent S6-covariant candidate permission predicate** whose only inputs are a three-axis support and a cycle orientation, allowing one oriented 3-cycle forces allowing all 40. If signed Port patterns, source IDs or additional event metadata also enter, the transitivity argument applies only within the corresponding full typed-input orbit; the 40-orbit conclusion cannot be transferred across distinct sign/source patterns. A legal-only-STAR rule therefore requires an actually declared frame, an actual symmetry reduction or another typed constraint; S6 kinematic covariance by itself cannot grant native event permission.

## Exact finite evidence

The accompanying Python standard-library verifier enumerates all 720 permutations of six axis labels, all 30 frames, 120 marked frames and 40 oriented cycles. It checks stabilizer sizes 24/6, S4 and marked-S3 branch orbit sizes 8/6, equal incidence frequencies 6/18, and 21,600 unmarked plus 86,400 marked kernel covariance comparisons. Every check passes. This is an exhaustive six-label combinatorial certificate, not an external physics law. The written proofs above establish each asserted combinatorial consequence; independent review is NOT_REVIEWED.

## Sign/source/native boundary and next problem

P000 fixes nonzero primitive stable force arity three, Enterprise PERP_E pairwise 120 degrees, and the existence requirement of TRIADIC_CLOSURE_E. It has not supplied a complete formal predicate for the signed incoming Port/Link/source incidence, time and legal Cell update. Existing FCC/K4 STAR realizations are carrier readouts, not native permission certificates. The exact next discriminating research unit is: determine whether native event metadata already includes a K4 frame/marked source and which signed triads are legal; construct and verify a source-preserving morphism from legal native updates into this framed BRC kernel, or exhibit a witness that the candidate rotation fails an actual native rule. Preserve BLOCK semantics and future-operation dependence. Do not silently promote group generation, a positive BRC marginal or a carrier triangle to primitive signed force cancellation or native Cell return.
