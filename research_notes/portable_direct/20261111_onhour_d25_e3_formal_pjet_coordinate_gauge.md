# D25 original E3: exact p-jet coordinate-gauge law for the formal [p] coefficient

Date: 2026-11-11. Status: AUTHOR_SIDE / EXACT_ALGEBRAIC_PROOF / DIRECT_POLYNOMIAL_TESTS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6333ae3.
Research logical lane: chatgpt-research-onhour-enterprise-math-20260923 (never the separate maintenance lane).

## Theorem — strict p-jet coordinate conjugacy

Let A be any commutative ring, p>=2 an integer, and let S(z)=lambda*z+sum_(n>=2) s_n z^n in A[[z]]. For c in A, change the formal parameter by f_c(z)=z+c*z^p (a strict formal coordinate change with a formal inverse), and set S_c(w)=f_c(S(f_c^(-1)(w))). Then, **exactly in A**,

    [w^p]S_c = s_p + c*(lambda^p-lambda).

Proof: f_c^(-1)(w)=w-c*w^p+O(w^(p+1)). Thus S(f_c^(-1)(w)) agrees with S(w)-lambda*c*w^p through degree p. Composing with f_c adds c*S(f_c^(-1)(w))^p. Since the inner series has zero constant term and linear coefficient lambda, the degree-p coefficient of its pth power is lambda^p. Sum the two changes; QED.

For a formal group F over a p-local ring, S=[p]_F and lambda=p. Hence

    s_p(c)=s_p+(p^p-p)c.

Modulo p^3 for primes p>=3, s_p(c)=s_p-p*c. If the original coefficient is p-divisible (as at the frozen supersingular p=373 example), the p-divided first observed digit satisfies the exact affine law

    s_p(c)/p = s_p/p - c   (mod p).

It follows, for this explicitly declared formal-coordinate readout, that the second digit is a torsor under changes of the degree-p source coordinate; a comparison must identify that coordinate (or an equivalent connection action). A curve-isomorphism or matching j-invariant alone does not choose the coefficient.

## Frozen original E3 example (not the native H0/B0 operator)

Reuse the already published ORIGINAL E3 fixed-z calculation, without recrediting its work:
research_notes/portable_direct/20261111_onhour_d25_E3_actual_formal_p_series_zp_p3.md, Git blob f72034627cfcf03ad2d5421d2587e5ac092bc7ca.
The curve is E3(t): y^2+xy+(t/27)y=x^3, with t=(2-T)/4, T^2=2 and fixed original z=-x/y. Its source-pinned prior coefficient is

    s_373 = [z^373][373]_E3(z)
          = 42842780 + 8783031*T (mod 373^3=51895117).

The NEW theorem gives the following coordinate-comparison predictions without recomputing the original E3 formal endomorphism:

    c=0:       42842780 + 8783031*T
    c=1:       42842407 + 8783031*T
    c=T:       42842780 + 8782658*T
    c=1+T:     42842407 + 8782658*T                (mod 51895117).

At mod p^2=139129 the fixed original coefficient is 130177+17904*T, with p-divided residue 349+48*T (mod 373). Taking c=T changes that to 349+47*T, retaining an explicit odd-coordinate discriminator. All numeric operations use the actual quadratic ring with T^2=2, not an indiscriminate trace or norm.

## Independent direct-composition checks

The included pure-Python checker performs actual truncated polynomial composition, not merely the formula's right-hand side, on the multiplicative formal group [p](z)=(1+z)^p-1 for p=5,7,11,13 and c=1,2,p-1. It checks f_c o [p] o f_c^(-1) through degree p and compares the exact coefficient modulo p^3; all 12 checks passed. The theorem itself is characteristic-free algebra, stronger than these tests.

## Native acceptance boundary and next action

This is a source-coordinate calibration criterion for a candidate comparison to the fixed original H0/B0 benchmark, not a calculation of its [X]U. To apply it, the native evaluator must first identify its actual divided-power representative, module rank, semilinear Frobenius and eta, signed odd kappa and the map (if any) to the E3 fixed-z formal multiplication observer. The criterion then verifies that any coordinate changes are carried through the p-jet before comparing p-divided digits.

Native obligation stays original fixed H0/B0 divided-power [X]U mod139129, NOT_RUN / PENDING_OWNER under existing Issue #1559. No new Task, CLAIM, open run, Result or Driver review is asserted.

Ordinary Chat recovery original request onhour_d25_20261111_recovery_89ff7a, Issue #6766, returned SUCCEEDED with own historic registration failed / UPSTREAM_CODE_REVIEW_REQUIRED. Exact predecessor Source read #6762 remains SUCCEEDED at fbee999c36d3a31601256192f10b817a50329782; do not reuse old claim as current own winning claim.

BRC typing: original formal E3 z, source parameter t, signed quadratic T label, p-jet coefficient, coordinate-change morphism, observer p-adic residue. Preserving the odd T-coordinate is essential to this readout. These calculations are in an auxiliary p-adic source chart and do not purport to replace P000-native X6 coordinates.
