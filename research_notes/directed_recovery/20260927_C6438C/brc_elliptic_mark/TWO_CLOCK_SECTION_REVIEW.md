# Two-clock translated section: symbolic review

Status: **PASS / PURE SYMBOLIC / SHARED CONTEXT / NOT EXECUTED / NOT ADMITTED**.

Reviewed complete `TWO_CLOCK_TRANSLATED_SECTION.md`, SHA-256 `2294c28339c1de5b40d1a3012ad7762c063229a684676d35dff78821b7ea4a9b`. This review uses the already read translated Kummer and trace proofs. It performs no new numerical calculation, experiment, provider query or external source verification. The draft's cited ECM stage-two page is an author-provided prior-art pointer; this reviewer has not independently fetched it.

No substantive mathematical defect was found under the stated odd smooth ring, coherent-point and primitive-coordinate hypotheses.

For the elliptic assertion, the derivative with respect to y is a unit at both P and -P because 2, B and b are units. Consequently x-a is a simple local parameter at each of those two points. Its homogeneous section W has no additional zero at infinity: there Z1 lies in the maximal ideal while X1 is a unit, so W is a unit. Away from these two finite points W is again a unit. Translation takes the two simple-zero neighborhoods to Q=O and Q=-2P. The frozen local-parameter proof with P, respectively -P, identifies each zero's full truncated prime-power depth with the corresponding primitive return ideal. This is stronger than checking the residue-field zero sets alone.

The neighborhoods cannot overlap over any residue field: overlap would give 2P=O, contradicting b being a unit in odd characteristic. Thus the two integer divisors d(Q) and d(Q+2P) have disjoint prime support. Each divides N and their product still divides N. Combining local depths proves the exact integer product for gcd(N,W), not merely an equality of radicals. The joint observation with Z0 selects d(Q), and exact division then recovers d(Q+2P). The latter division has not been executed in the saved elliptic unit and must be separately charged if implemented.

For the companion assertion, the discriminant-unit hypothesis makes the quadratic extension finite etale and makes the eigenbasis invertible. Expanding the displayed product gives exactly V_(E+1)-epsilon*k for either epsilon, using epsilon squared equal to one. Lambda is a unit, so its denominator is legal. The two factors cannot simultaneously be nonunits at a given residue component: their simultaneous vanishing forces lambda squared equal to one, contradicting the discriminant condition. In the split case the conjugate factors have equal valuation, since lambda^(-n)-epsilon is the unit multiple `-epsilon*lambda^(-n)*(lambda^n-epsilon)`. Hence a partial valuation in one split factor cannot be misread as an arbitrary base-ring ideal. In the nonsplit case the unramified extension preserves the base p-adic filtration. These facts justify descent of the exact primitive ideals and their primewise disjointness, including prime powers and saturated returns.

The section may be saturated because different CRT components hit different branches; the joint mark can then separate them. Neither product theorem supplies a favorable exponent, an inexpensive parameter selector, or a general success probability. The draft preserves these limitations and distinguishes established collision-test mathematics from this project's new native observation contract. It also correctly avoids treating the typed elliptic register program as an already admitted nonlinear HBW move.

This is a source-bound proof review only. The previously saved three elliptic fixtures do not by themselves execute the new exact quotient or establish its cost.

Global-Knowledge-Sync: shared-author reused canonical context, with the reviewed author's marker retained; no new independent handshake or scientific execution is claimed.
