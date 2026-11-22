# PREFIX-1000 — Exact scalar law for positive-terminal first-interior X6 BRC probability

Date: 2026-11-22 (+08). Evidence: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Portable research continuation of PREFIX-996/997/998/999. No shared CLAIM, native PROGRESS, independent review, physical calibration, or change to P000.

## Frozen input and precise observer

Frozen project P000 V5: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\`. The native X6 Cell torsor has six axes, twelve signed primitive neighbours, and one independent ordered update count. The already studied Stage46 candidate has 12-port real scattering amplitude \`C[incoming,outgoing] = 1/6 - 1[incoming=outgoing]\`, with initial incoming directed edge \`x0-e_i -> x0\` for one fixed axis \`i\`. Each path carries its signed numerator, Cell displacement, and final directed incoming port. Amplitudes in a common endpoint/terminal-port fibre are combined *before squaring*. At length \`n\`, the first interior grade \`sum(k)=n-2\` comprises precisely one negative primitive step; it is not a two-dimensional plane or a physical-time claim.

The preceding PREFIX-999 scalar identity evaluates only **negative-terminal** mass (first-negative flux). PREFIX-998 evaluates both terminal signs by an endpoint/port marked-word formula. Here we eliminate all endpoint and port state storage **for the total positive-terminal scalar**, retaining their interference exactly in the derivation.

## Theorem 1000.1 — Laurent-polynomial amplitude compression

Take six commuting indeterminates \`x_1,...,x_6\`, let \`S=sum_r x_r\`, \`R=sum_r x_r^(-1)\`, \`Z=SR\`, and let \`f(a,r)=1-6*1[a=r]\`. These variables merely encode the six signed native Cell displacements, not a new geometric model or an alternative dynamical operator.

Let \`N_r(n)\` denote the integer numerator amplitude Laurent polynomial for length-\`n\`, exactly-one-negative histories whose **last step is -e_r**; let \`P_j(n)\` denote the same for histories whose last step is **+e_j**. The coefficient of \`x^k\` is exactly the total signed BRC numerator at Cell displacement \`k\` and that final incoming port. Then

\`N_r(1) = f(i,r) x_r^(-1)\`,

\`N_r(n) = x_r^(-1) (S-6x_r) S^(n-2)\`, for \`n>=2\`.             (1)

For \`n=1\`, \`P_j(1)=0\`; for \`n=2\`,

\`P_j(2) = sum_r f(i,r) f(j,r) x_j/x_r\`.                         (2)

For every \`n>=3\`,

\`P_j(n) = x_j S^(n-3) [(n-1) Z - 6S/x_i - 6S/x_j -36(n-3)]\`.  (3)

**Proof.** The all-positive word of length \`n-1\` has numerator one at each labelled word because none of its positive outgoing ports equals its negative incoming neighbour port; its generating polynomial is \`S^(n-1)\`. Taking the last negative step applies the exact Stage46 factor \`f(a,r)\` to the previous positive label \`a\`, proving (1) for \`n>=2\`. For \`n=1\` it uses the initial incoming edge. Formula (2) follows from one negative followed by one positive. Write \`A(n)=sum_j P_j(n)\`. The 12-port update, with no second negative permitted, gives

\`P_j(n)=x_j[A(n-1)+sum_r f(j,r)N_r(n-1)]\`,

\`A(n)=S A(n-1)+sum_r(S-6x_r)N_r(n-1)\`.                      (4)

At \`n=2\` we have \`A(2)=S(R-6/x_i)\`. For \`n>=3\` the inhomogeneous term in (4) equals

\`S^(n-3) sum_r (S-6x_r)^2/x_r = S^(n-3)(S^2 R-36S)\`.

Induction therefore gives

\`A(n)=S^(n-2)[(n-1)Z-6S/x_i-36(n-2)]\`, \`n>=2\`.          (5)

Substituting (1) and (5) into (4) proves (3). Every recurrence and identity is directly induced by the typed Stage46 BRC step and preserves terminal-port distinctions until the final scalar observation. QED.

## Theorem 1000.2 — Three-collision-number exact positive-terminal mass

Let \`A_6(m)=sum_(h_1+...+h_6=m) (m!/(h_1!...h_6!))^2\`, with \`A_6(0)=1\`. Define integer scalar numerators

\`E_n^+ = sum_(k,j) ([x^k]P_j(n))^2\`,
\`E_n^- = sum_(k,r) ([x^k]N_r(n))^2\`.

The exact positive-terminal coherent probability at grade \`n-2\` is \`E_n^+/36^n\`. The small cases are

\`(E_1^+,E_1^-)=(0,30)\`, \`(E_2^+,E_2^-)=(900,180)\`.

For \`n>=3\`, setting \`t=n-2\`, we have the **all-length scalar identities**

\`E_n^+ = 6(t^2-2t-1) A_6(t+1) - 432t(t-2) A_6(t) + 7776(t-1)^2 A_6(t-1)\`,    (6)

\`E_n^- = 216 A_6(t) - 6 A_6(t+1)\`.                         (7)

Consequently \`M_(n,1)=(E_n^+ + E_n^-)/36^n\` is computed by just three adjacent values of the collision sequence, with **no Cell/terminal-port fibre storage**. Identity (7) is the independent PREFIX-999 flux law; (6) is the new result.

**Proof.** Give Laurent polynomials the involution \`x_r^*=x_r^(-1)\`. The squared coefficient norm is the constant term \`CT(F F^*)\`; therefore \`E_n^+=CT sum_j P_j(n)P_j(n)^*\`. For \`n>=3\` write \`t=n-2\`, \`D=(t+1)Z-36(t-1)\`, \`U=S/x_i\`; equation (3) is

\`P_j=x_j S^(t-1)[D-6U-6S/x_j]\`.

Expanding the terminal-port sum and using \`sum_j S/x_j=sum_j R x_j=Z\`, \`U U^*=Z\` gives

\`sum_j P_jP_j^* = Z^(t-1)[6D^2-12DZ+432Z+36(Z-D)(U+U^*)]\`.

The constant-term functional is invariant under permutation of the six axes. Since \`sum_i S/x_i = sum_i R x_i = Z\`, it follows *exactly* that

\`CT[Z^(t-1)(U+U^*)]=(1/3)CT[Z^t]\`.

Thus

\`E_n^+=CT\, Z^(t-1)[6D^2-24DZ+12Z^2+432Z]\`.

Using \`CT Z^m=A_6(m)\` and expanding \`D\` yields (6). The sign-matched negative-terminal result (7) follows from (1), or the independently established first-exit identity \`F_n=M_(n-1)-M_n\`. Direct evaluation of the two exceptional starting lengths proves the stated small cases. QED.

## Exact computation, complexity and evidence

The collision recurrence, already established in PREFIX-996,

\`A_1(m)=1\`, \`A_d(m)=sum_(r=0)^m binom(m,r)^2 A_(d-1)(m-r)\` for \`d=2,...,6\`,

provides \`A_6(0),...,A_6(N-1)\` with \`O(6N^2)\` arithmetic operations and \`O(N)\` stored big integers (sequential dimension rows; bit-complexity depends on integer length). The scalar observable at any \`n<=N\` follows from (6)–(7) with a fixed number of operations. Alternating signs in (6) must be evaluated with exact integers; its nonnegativity is certified by the prior sum-of-squared-fibres identity.

Companion checker \`PREFIX1000_R6_POSITIVE_TERMINAL_SCALAR_CHECK.py\` runs entirely with integer BRC numerators and \`fractions.Fraction\`. Actual local execution verified all \`n=1..70\` scalar values, independently propagated the full signed 12-port Cell/terminal-port recurrence with at most one negative for \`n=1..7\`, and reproduced the previously saved PREFIX-997 total exact numerators for \`n=1..10\`. All checks passed. Examples, with mass denominator \`36^n\`:

| n | E_n^+ | E_n^- | E_n^++E_n^- |
|---:|---:|---:|---:|
| 1 | 0 | 30 | 30 |
| 2 | 900 | 180 | 1080 |
| 3 | 1800 | 900 | 2700 |
| 4 | 40680 | 8280 | 48960 |
| 5 | 981720 | 105300 | 1087020 |
| 6 | 22573080 | 1649160 | 24222240 |
| 7 | 531480240 | 29888280 | 561368520 |
| 8 | 13031031600 | 602974800 | 13634006400 |

The direct n<=7 run is a mathematical regression check; the proof of the all-length formula is algebraic. The reduction concerns **this scalar probability readout**, not lossless compression of the state when arbitrary future interactions, nontrivial port gates, Link occupancy or triadic feedback are admitted. It reuses the established Stage46 native BRC update rather than a classical surrogate. It does not establish a physical lifetime or solve \`B_fix,odd(32) in {19,20}\`.

## Provenance and next problem

Scientific sources: P000 frozen pin above; \`research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md\`; PREFIX-996 outer collision theorem; PREFIX-997 first interior signed path rule; PREFIX-998 all-length endpoint amplitude and 35/4 ratio; PREFIX-999 exact first-negative flux. Historical provenance: \`EM-DIRECT-FBEA5D\`, original managed session \`MCP-45ad6d29cd534c1aad25595a72e3c532\`, original research activity \`RA-3FB2D033BE6048D8712FF056\`. The session has not been closed or custody-revoked; the separate current inventory read \`r6-20261122-0850-owner-inventory-prefix1000\` returned \`FAILED/SOURCE_TREE_TRUNCATED\` during event materialization. No formal CLAIM, Activity association, Result or independent Review is asserted.

**Next:** derive the first finite-size correction to the PREFIX-998 ratio \`M_(n,1)/M_n -> 35/4\` directly from the new three-collision scalar formula, using a rigorously controlled asymptotic of \`A_6(n)\`. Then add an actual X6 Link/Port occupancy/triadic feedback instance to test exactly which terms of the scalar collapse remain valid. The mother objective remains open.
