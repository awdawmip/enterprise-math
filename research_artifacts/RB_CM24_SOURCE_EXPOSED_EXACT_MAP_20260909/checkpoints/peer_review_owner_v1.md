# Owner source-exposed review of the first exact-map identity checkpoint

This is a source-exposed Driver/Owner paper and code review, not a new mathematical execution, blind reconstruction, formal Result review, or acceptance of the full task. Reviewer: EM-DVR-01E1D9. Research task: RS-RB-CM24-SOURCE-EXPOSED-EXACT-MAP-CERTIFICATE.

## Actually inspected evidence

I read the complete first `check_exact_map.py` (recorded execution hash `dea05305c92545ddbf97e521310c0ba1f103213020945750b810e2c8ebc9dd63`), the complete source freeze (`85946a8cb4e736021cef6cd311c8cfffbde1cce34fe728255db4b6703f5887f2`), the originating formula capsule, the reused integer API's addition/multiplication/curve reduction/derivation implementation, and the actual identity-v1 run receipt (`d67a19adaf231cca83394206e865d2b5a869034ffef78530e5cc1ab6b8ba7a36`). I inspected the certificate's result and boundary fields; I did not independently replay the coefficient rows. The researcher's actual run returned exit 0, with certificate SHA256 `c11db2a62c2c1926306117abcac0495ed7a518ae37e1fb6fbd27bfdd75ef6ab8`. The certificate retains INCOMPLETE and names the remaining gates.

The first script uses only the stated monic coefficient relations and `t^2=R^3-3R`. It does not call the old critical-divisor substitution. Root evaluation and integer division are not used; zero BRC executions is the appropriate reported count for that run.

## Paper verification of the cleared identity's meaning

Write D0 for the original denominator, D=2 delta for the derivation, and W=D(N)D0-ND(D0). Then delta X=W/(2D0^2). With F=(R+2)t and C=C4/4, clearing the full ODE gives exactly

`F W^2 - C4 (t+k)^2 N(N-D0)(N-lambda D0)D0 = 0`.

This is the residual constructed by the first script. With the actual source convention `Y=wW/[2(t+k)D0^2]`, the same identity and `w^2=F` give `Y^2=C X(X-1)(X-lambda)` in the function field, once its denominators/nonzero generators are justified. The chosen unsquared Y gives `dX/Y=(t+k)dR/(wt)` by direct cancellation; choosing -Y changes the differential sign while preserving the squared target equation. A meaningful sign regression must distinguish these cases.

Zero formal remainder implies an identity after the declared algebraic specialization. In contrast, a nonempty polynomial dictionary does not by itself prove nonzero evaluation in that specialization. The first checkpoint correctly leaves embedding/nonzero proof open. The full task still needs those proofs, exact special fibers, all common base points, map degree, square-class placement/descent, the exact j relation, global differential regularity, and complete evidence/return.

## Conditional local review of the differential

The following is a paper calculation for the researcher to verify and incorporate with exact nonzero conditions. It is not a separately executed certificate.

On the smooth projective normalization of the double cover, at a point over each of the three finite `t=0` branch points, the orders of `(R-r,t,w,dR)` are `(4,2,1,3)`. With k nonzero, phi therefore has order `3-1-2=0`.

At the two points with R=-2, the orders of `(R+2,w,dR)` are `(2,1,1)`; if `k^2 != -2`, t+k is a unit and phi has order zero. At O the orders of `(R,t,w,dR)` are `(-4,-6,-5,-5)` and `1+k/t` is a unit, again giving order zero. Away from these points, the only zeros can be the three simple points t=-k and their two lifts. Conditions `k != 0` and `k^2 != +/-2` give six simple zeros. These conditions can be proved in the exact real biquadratic field using `k^2=12 beta-10 alpha^2`; no numerical fit is needed. Their total degree six agrees with the genus-four double cover having six branch points.

For extending the rational map itself, I actually searched and read [Stacks Project, Lemma 53.2.2, Tag 0BXZ](https://stacks.math.columbia.edu/tag/0BXZ), specifically the statement and proof. It supplies extension from a normal curve to a proper variety. The application here is conditional on establishing the source normalization, a nonconstant rational map, and a nonsingular projective target; it does not replace the degree or divisor calculation.

## Classification convention to preserve

The frozen square-class parameterization first moves an empty special fiber to infinity by a fixed-lambda V4 transformation. The recovered original X has empty fibers at 1 and lambda, and a nonempty infinity fiber. One candidate transformation is `x_new=(X-lambda)/(X-1)`, which permutes labels by `(0 lambda)(1 infinity)`. Its new infinity and zero fibers are empty; the new one fiber contains `{T0,Tplus}` and the new lambda fiber contains `{O,Tminus,Pplus,Pminus}`. This is a paper routing check, not a certified component label. The actual frozen representative convention, transformed Y/differential factor, half-points, geometric twists, constants, and degree-three pole class must still be proved. A 4+2 count alone does not place the formula in a specific surviving component.

## Disposition of this note

No hard-target gate is lowered and no parent gap is closed. Resource enforcement and reproducible source retention are under a separate bounded peer code review. Preserve the first executed script bytes and failed generations before replacing the working checker.
