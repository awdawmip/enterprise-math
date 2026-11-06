# D25: exact p=5113 third-digit outer-source law and cross-filtration bridge

Date: 2026-11-06. TASK_RESEARCH author-side portable result. **EXACT PRIME-SPECIFIC INTEGER CERTIFICATE / AUTHOR-PROVED DEGREE ARGUMENT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.

Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; unchanged scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. This is the next portable scientific unit after the proven outer-source spectral-jet and head/tail result at \`82e6e20c6e0121d10f8cdbb714e669ccbcaa9544\`.

## Exact claim

Fix the prime \`p=5113\`, \`m=852\`, \`s=(1704,2556,3408)\`. Keep these specific **integer** lifts of the original source vector
\`v=(1704,2556,3408)\`; they represent \`(-1/3,-1/2,-2/3) mod p\`. Put \`d=(1,0,1)\` and

\`\`\`
F(lambda) = sum_(j=0)^(p-1) (6j+1)*(-1/2)^j
           * product_(i=1)^3 binom(s_i+p*(v_i+lambda*d_i),j),
\`\`\`

computed in \`Z/p^4Z\`. All factorial denominators \`j!\` are units. Define the normalized difference
\`Q(lambda)=(F(lambda)-F(0))/p^2\` modulo \`p^2\`. For **every integer lambda**, the following exact congruence holds:

\`\`\`
Q(lambda) = 3118*lambda +
            5113*(1998*lambda + 141*lambda^2 + 3783*lambda^3)
            (mod 5113^2).
\`\`\`

Equivalent polynomial coefficients modulo \`p^2=26,142,769\` are
\`(A,B,C)=(10,218,892; 720,933; 19,342,479)\`. This extends the previously proved two-digit law \`Q(lambda) = 3118*lambda (mod p)\` with an **explicit, nonzero third-digit cubic correction**. It does not claim two source states collide at the second digit: \`3118\` remains invertible modulo p.

## General degree bound and source preservation

For any prime p and j<p, each \`binom(s_i+p(v_i+lambda*d_i),j)\` is a polynomial in \`p lambda\` over \`Z_(p)\`. Consequently \`F(lambda) mod p^4\` is exactly of degree <=3 in lambda; terms of degree >=4 contain \`p^4\`. Here the coefficient of lambda is divisible by \`p^2\`, as independently checked by the coefficient-domain computation. The quadratic and cubic coefficients contain \`p^2\` and \`p^3\` respectively by construction. Therefore \`Q(lambda)\` is an exact cubic modulo \`p^2\` for all integer lambda, not a polynomial guessed from selected samples. No denominator divisible by p is inverted.

The reflected-mod-p spectral calculation in the preceding note proved

\`\`\`
[t^0,t^1,t^2,t^3] F_p(t) = [0,0,0,3783] (mod p),
\`\`\`

where \`F_p(t)\` is the **unscaled** simultaneous outer-source polynomial. The p-adic cubic coefficient is \`p^3[t^3]F_p(t)\` modulo \`p^4\`, even when the expansion center moves from 0 to \`p v\`, since that movement disappears modulo p. The new exact result has \`C/p = 3783\`, providing a **cross-filtration certificate** that the third-order source component survives in the third p-adic digit. The linear lift \`1998\` and quadratic lift \`141\` are recorded at the specified integer representatives; changing the representatives can change these higher-digit coefficients.

## Exact arithmetic certificate and two independent algorithms

\`p^4=683444370987361\`; direct full 5113-term sums modulo \`p^4\` and an **independent coefficient-domain expansion** of the three labelled binomial factors yield

\`\`\`
[lambda^0,lambda^1,lambda^2,lambda^3] F(lambda)
 = [205306118938667, 267150132991948,
    18847184883477, 505665960384351]        (mod p^4).
\`\`\`

The last three entries are divisible by \`p^2\`, and after division give \`A,B,C\` above. A separate full-sum evaluation at all integer lambdas \`0,+1,-1,2,3,5,17,53\` matched the exact cubic. Representative values:

\`\`\`
lambda    F(lambda) mod p^4    Q(lambda) mod p^2
 0        205306118938667      0
 1        313525026211082      4139535
-1        134781581433206      23445100
 2         76212210619752      21204734
 3        477030321508700      10393857
 5        293266210229912      3364605
17        642048446562810      16706047
53        278732660659742      2808675
\`\`\`

The complete program \`d25_p5113_third_digit_20261106.py\` was **actually executed**, passed the full-sum sample assertions and then independently verified coefficient-by-coefficient without fitting samples. It uses standard-library exact modular integer arithmetic, with a primality check for p5113.

## Scope, BRC semantics and mother question

This is one exact auxiliary **prime-specific** result for p5113, which lies in class \`1 mod24\`; the frozen mother objective concerns \`p=13,19 mod24\` and remains open. Sources are three labelled binomial factors with their integer lifts; the observer is \`Q\` on the outer perturbation line; allowed operation is changing lambda followed by modular p-adic readout. The mod-p source triple root does **not** imply a p-adic collision: differing valuations of Taylor coefficients and the shift of expansion center matter. Retain the labelled third-order coefficient and the lift of the base source vector before any compression.

Next scientific action: attempt a closed telescoping/WZ certificate for the *general* \`[t]F_p(t)=0\` observed in finite scans, and investigate a general source-theoretic criterion for \`C_p=0\` without mistaking p5113 for a target-prime solution. Keep H0/B0, Frobenius, eta/kappa and independent review open.

Native Source state remains separate. The original r13 request IDs and existing support issue #1558 are preserved; **no current claim, run authorization, native checkpoint or Result admission** is claimed by this portable GitHub publication.
