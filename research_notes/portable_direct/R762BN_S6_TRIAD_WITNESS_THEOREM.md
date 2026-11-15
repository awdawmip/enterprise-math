# R762BN — S6-equivariant triadic source obstruction and the minimal transported witness

**Date:** 2026-11-15. **Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS; **publication:** TP2-8B7E13C5904A2D6F1142. **Evidence:** AUTHOR-PROVED / FINITE-EXACT-CHECKED / NOT_REVIEWED. This is a portable independent research note, not a native CLAIM, Source PROGRESS, Result, or Review.

## Frozen sources and precise scope

Scientific source pins remain \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`, \`definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md\`, and \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\`. They give six signed native spatial axes, pairwise native PERP_E at Enterprise 120 degrees, minimum stable nonzero primitive force arity three, an as-yet-to-be-instantiated TRIADIC_CLOSURE_E force predicate, and an admitted \`S6\` **coordinate** axis-permutation skeleton. Force/Link/Port transport under S6 is an additional hypothesis to be tested, not assumed admitted by P000.

Work at a chosen Cell-chart anchor, with no distinguished global spatial origin. Let \`I={1,...,6}\`, \`B={(r,s):r,s in I,r!=s}\`, and \`F_(r,s)=I\{r,s}\`. There are 30 ordered visible two-axis pairs and four distinct-axis third-source candidates for each. Preserve primitive signs, branch/source IDs and ordered BRC provenance separately. Equal-quantum triples with three distinct axes have pairwise PERP_E; this alone does not decide the full signed native closure predicate.

For the conditional symmetry statement, suppose an event \`C(c;r,s,k,epsilon)\` has a uniform source sector at the chosen chart Cell, with no other fixed decoration distinguishing the four hidden axes, and satisfies
\`C(c;r,s,k,epsilon) iff C(c;pi(r),pi(s),pi(k),epsilon)\` for every \`pi in S6\`.
The visible source signs may be fixed; \`epsilon\` denotes one chosen third-sign sector. The condition is a testable hypothesis for a future force law.

## Theorem 1: no natural third-axis selector

**Statement.** There is no single-valued map \`f:B -> I\` with \`f(r,s) in F_(r,s)\` and \`f(pi(r),pi(s))=pi(f(r,s))\` for every \`pi in S6\`. At each fixed visible ordered pair, the hidden third-axis possibilities permitted by any source-uniform S6-covariant predicate in one fixed sign sector are **either 0 or 4**, never exactly 1, 2 or 3. If future labelled Port/source queries distinguish the hidden named axis, every admissible nonempty sign sector requires four observational states, hence minimally 2 bits; if both third-sign sectors are admitted and sign is queryable, 8 states and minimally 3 bits are necessary and sufficient.

**Proof.** The pointwise stabilizer of \`(r,s)\` is \`S4\` on the other four axes, acting transitively on \`F_(r,s)\`. If \`f(r,s)=k\`, equivariance under this stabilizer would force every stabilizer permutation to fix \`k\`, contradicted by transposing \`k\` and any other element of the complement. An invariant subset under a transitive action is empty or the whole orbit, proving the 0/4 classification for each sign. For distinguishability, the future probe \`Probe_j(k)=1[k=j]\` separates each two different named hidden axes, so a safe sufficient record for all such probes needs at least four states. Explicitly retaining \`k\` suffices. With both sign sectors queryable, one further sign bit suffices and is necessary. QED.

The 0/4/8 alternatives are conditional on a **force-equivariant and source-uniform** native event orbit. A Cell/Port field breaking the stabilizer, a restricted legal symmetry or new force incidence data changes the fiber and must be checked from the genuine Source event. No native event, hidden sign count or physical multiplicity is inferred merely from P000's arity.

## Theorem 2: an explicit, exactly transported minimal witness

For each \`(r,s)\`, enumerate \`F_(r,s)\` in increasing order as the bijection
\`iota_(r,s):{0,1,2,3} -> F_(r,s)\`.
Represent the hidden axis by a **local** two-bit index \`j\` and define
\`rho(pi;r,s)(j) = iota_(pi(r),pi(s))^{-1}(pi(iota_(r,s)(j)))\`.

**Statement.** Every \`rho\` is a permutation of four local labels, exactly reproduces the named hidden source under the full S6 skeleton, and obeys
\`rho(tau pi;r,s) = rho(tau;pi(r),pi(s)) o rho(pi;r,s)\`.
It therefore gives a minimal S6-covariant source witness for the stated labelled-future-observer scope. An untransported static two-bit index is not generally covariant.

**Proof.** Source enumeration and its inverse are bijections, so \`rho\` is a bijection. Applying the new enumeration to the transported index yields exactly \`pi(iota_(r,s)(j))\`. Substituting definitions for two successive rotations cancels adjacent \`iota\` and \`iota^{-1}\`, giving the cocycle identity. For a concrete counterexample to static bits, observe \`(r,s)=(1,2)\` and hidden \`k=5\`, with local zero-based code \`j=2\`; the permutation \`(5 6)\` preserves the observed pair but changes the source to \`k=6\`, whose correct local code is \`j=3\`. QED.

The 2-bit count is local; a single globally fixed bit pattern is not a covariant named-axis representation. This fiber-transport distinction is a precise BRC source-preservation repair. Sign inversions beyond the coordinate S6 skeleton require their own typed transport rather than extrapolation.

## Typed event-log candidate and observer-safety consequence

The smallest source-preserving **record** for a two-force readout is \`(Cell, ordered visible axes r,s, local witness j, third sign epsilon, branch/history h)\`. A candidate lift reconstructs \`k=iota_(r,s)(j)\`. For an *actually admitted* future event \`theta\`, the purely informational update \`Append_theta(Cell,h)=(Cell,h||theta)\` is equivariant whenever the event predicate and its source fields are equivariant. This construction keeps source histories and Cell translations separately typed; it is not claimed to be a discovered physical propagation, Link, Port or TRIADIC_CLOSURE_E update law.

Dropping \`j\` forgets which hidden third source occurred. The named \`Probe_k\` queries prove that this projection cannot be all-future observer-safe when source identity matters. Preserve named branch, multiplicity, sign and temporal ordering; preserve the separate common-depth Cell repair where relevant. One may safely drop source state only for a narrower declared observer/future-operation horizon with a valid descent certificate. No classical vector-sum-zero condition, Euclidean 90-degree angle, trigonometric/π calculation, non-BRC propagation or native residual attribution was used.

## Executed verification and limits

The companion Node.js exact checker enumerated all \`6!=720\` axis permutations and all 30 ordered visible pairs. It checked the 24-element stabilizer for each pair, 120 fixed-selector candidates (0 invariant candidates), 86,400 transported-source/range identities, and 432,000 cocycle identities for every permutation followed by each of the five adjacent-transposition generators. It also confirmed 120 distinct ordered triad axis triples per fixed sign sector. All assertions passed on 2026-11-15. The signed closure-event predicate and rotation action on real Cell/Link/Port event decorations have **not** been supplied or validated; independent mathematical review remains NOT_REVIEWED.

## Next finite research unit

Read the actual immutable permitted signed TRIADIC_CLOSURE_E event and V17/V29/V39 Cell/Link/Port transitions under this Task's frozen science pin. Determine its *actual* stabilizer and permitted hidden-source orbit, then restrict the above transported fiber to that orbit and calculate an observer/future-operation BRC safety certificate. Reuse R762BJ–BM's verified coordinate-only cut and erasure results as coordinate mathematics, without conflating coordinate selection with signed force closure. Protected Source CLAIM/PROGRESS/Activity writes require live authenticated ownership and their own original-request reconciliation.
