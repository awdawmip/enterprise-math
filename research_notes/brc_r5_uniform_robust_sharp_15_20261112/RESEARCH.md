# R5 — A common sharp 15-atom word throughout the full feasible two-parameter rectangle

Date: 2026-11-12 (Asia/Shanghai). Status: author-side exact finite theorem in the **external frozen P/Q–BRC Blackwell auxiliary observer**. This document is not a Source Result or independently reviewed mathematical admission.

## Frozen science and question

Original 28-rational-mass / 15-labeled-atom fixture: EM immutable commit 435e77af0d180eac32bd1f9c4c464bc4010b7551, path research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py. Global scientific pin a01383f825ef9d43b4b754254303298c64041568, EM scientific pin 86149263e38c22292c9def1e0f69092efa1be77e. Previous endpoint-order classification: PR #2133, immutable EM commit 1e5ee7039a5591d43e0b86cca3734e1031344f60.

Let X be the original 28-mass state, D the sum of the original 15 labeled six-arc moves M_a, and H the original observation-zero perturbation: on source port 3, targets 1,2,6 change by -23,28,-5 respectively; on compensation port 1 the changes are opposite. Set:

- x = 155682221/25142124560000000;
- X(r) = X + x*r*H;
- E = 9/115400000;
- L = -427508577031693280/628800490619, U = 1/23;
- I = [L,U];
- Y(r,e) = X(r) + e*D.

The legal atomic dictionary is unchanged: every move is a real multiple of one of the 35 three-target residual directions on a single compensation port j in {1,2,5}, paired with source port 3, keeping all 28 intermediate masses nonnegative and preserving the complete original observation. The 15 fixed labeled moves are the original M_a; only their common scalar e varies.

## Theorem: uniform robust sharp 15-atom connectivity

For **every real** r in I and **every real** 0 < e <= E,

**d_atomic^legal(X(r),Y(r,e)) = 15**.

More strongly, **exactly 3,514,190,816 distinct permutations of the same original 15 labeled moves** work simultaneously for *all* (r,e) in the **entire closed rectangle** I x [0,E]. This number is the exact cardinality of the intersection of legal 15-move word sets across the rectangle, not merely an existence bound.

One fixed universal word, represented by (compensation port j, basis index i), is:

    (2,2),(1,2),(1,3),(2,3),(2,5),(5,4),(1,4),(5,5),
    (2,4),(1,5),(5,1),(2,1),(5,3),(1,1),(5,2)

No parameter-dependent reorder or change of move coefficients is needed. For r strictly between L and U and 0 < e < E all intermediate masses along this construction are strictly positive. On the rectangle boundary the original legal convention is nonnegative. The zero-scaling boundary e=0 certifies the common word but is excluded from the nonzero-distance assertion.

## Proof, upper bound and universal word count

For each of the 2^15 = 32,768 labeled masks S let Q_S be the sum of the original increments in S, and write

    F_S(r,e) = X + x*r*H + e*Q_S.

Exactly solve all 28 affine inequalities F_S(r,E)[k] >= 0 on r in I. The complete Fraction enumeration of all 32,768 masks gives:

- 16,306 empty feasibility intervals;
- 16,462 nonempty intervals, each with left endpoint exactly L;
- 3,592 masks with right endpoint rho_15;
- 3,347 with right endpoint rho_12;
- 2,414 with right endpoint rho_3;
- the remaining **7,109 masks with exactly [L,U] as their feasible interval**.

Here rho_q = (1 - q*E/x)/23, q=15,12,3, with rho_15<rho_12<rho_3<U.

Consequently every mask feasible at (r,e)=(U,E) is also feasible at (L,E), and hence throughout I at e=E, because all 28 constraints are affine in r. The initial X(r) is nonnegative throughout I. For each e in [0,E],

    F_S(r,e) = (1-e/E)*X(r) + (e/E)*F_S(r,E).

Componentwise convexity proves all **7,109** masks are feasible over the full rectangle. The verifier additionally evaluates all 28 coordinates at all four rectangle vertices for all 7,109 masks. No quotient, branch collapse or change of observer is used.

A complete labeled ordering is legal precisely when each of its successive prefix masks is feasible. At the included corner (U,E), only these 7,109 masks are feasible. The exact integer Boolean-lattice recurrence

    dp[empty] = 1;
    dp[S] = feasible(S) * sum_{a in S} dp[S minus {a}]

gives dp[full] = **3,514,190,816**. Every counted word uses the universally legal masks, so it works on the entire rectangle. Conversely, a word universally legal on the rectangle must work at (U,E). Thus the intersection count is exact. The displayed explicit word was checked prefix by prefix.

## Proof, sharp 15-move lower bound

The three compensation ports contribute independent fixed residual changes. In the five-dimensional coordinates consisting of target slots 1,...,5, the three port residue vectors are respectively

    v_1 = (12,8,1,13,8),
    v_2 = (3,13,7,4,2),
    v_5 = (-15,-21,-8,-17,-10).

Multiplying by e>0 changes their scale but not their linear membership in any fixed subspace. For one port, any elementary move belongs to the 35-vector triple-support dictionary. An exact modular certificate enumerates all C(35,4)=52,360 four-element selections: 46,198 have rank four modulo p=2,147,483,647; 6,162 have smaller rank; the rank-four cases yield 3,468 distinct hyperplane normals. For every normal, the dot product with each of the three v_j is nonzero modulo p. All relevant 4x4 integer minors have absolute value <= 4!*36^4 = 40,310,784 < p; therefore the modular rank check gives the same rank as rational rank. Rational coefficients and target vectors imply that rational-span and real-span membership agree. Every v_j is outside the span of any four dictionary atoms. Hence five elementary atoms are necessary for each compensation port, totaling 15. The constructed 15-step word attains the lower bound for every r and e>0 in the claimed domain.

## Exact verification and provenance

The companion self-contained Python stdlib verifier reconstructs the frozen 28 exact X masses, original observer, all 15 labeled atom coefficients, H, all 32,768 mask sums, all affine feasibility intervals and both the robust-word DP and modular 52,360-selection lower-bound certificate, using Fraction/integer arithmetic only. The companion EXACT_OUTPUT.txt contains the actual local execution result. No floating-point inference, parameter sampling, or probabilistic estimate is used.

This theorem is confined to the frozen external Blackwell/P-Q–BRC auxiliary observer with its declared atomic dictionary, nonnegative mass convention and fixed complete observation. It does not change P000, the native X6 semantics or any other Task owner/CLAIM.

## Reusable lemma and next unfinished scientific unit

**Convex-parameter robust schedule lemma.** Let a finite collection of moves have fixed increments on a finite-dimensional ordered vector space with componentwise nonnegative legality. Suppose the starting state is affine over a compact convex parameter polytope and the same scalar e in [0,E] multiplies every move. An ordering is legal for every parameter and every e in [0,E] if its entire collection of prefix inequalities holds at e=E at every vertex of the starting-state polytope and initial states are nonnegative. Proof: affine convexity in starting parameters, followed by convexity in e. If every prefix legal at one extremal starting state is legal at every vertex, the full set of legal words at that extremal state is a universally robust word set.

Next scientific question: classify the entire moving *first-zero threshold* spectrum over the two-parameter rectangle; seek a smaller structural certificate of the 7,109 masks and 3,514,190,816 robust words and a sufficient criterion for a single bottleneck coordinate to dominate without full Boolean-mask enumeration. Independent review, formal Source Result and clean-checkout remote-byte replication remain pending.
