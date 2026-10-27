# D25 / SECOND-DIGIT-LIFT — original E3 formal p-multiplication: nonzero quadratic second-digit defect

Date: 2026-10-27. Research logical lane: \`chatgpt-research-onhour-enterprise-math-20260923\` (not maintenance). Mother objective \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\`, task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` is frozen and unchanged.

**AUTHOR-SIDE PROVEN GENERAL CONDITIONAL LEMMA / EXACT FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0B0 / NOT_SOURCE_CHECKPOINT / NOT_LIFT_PROOF.**

## Narrow new mathematical question

Prior author-side D25 proofs computed the original E3 invariant-differential coefficient a_(p-1) modulo p^3 and its second-kind companion. Determine, in the SAME original formal parameter, whether a_(p-1) also equals the *elliptic formal-group multiplication-by-p* coefficient [xi^p][p]_E modulo p^3. The two objects have distinct observer definitions; no identification is assumed.

Use the actual original E3 curve and local parameter

\[
E_c:\ y^2+xy+cy=x^3,\quad c=(2-T)/108,\quad T^2=2,\quad \xi=-x/y.
\]

The original formal differential is omega = -H(xi) dxi, where the square-root branch is fixed by H(0)=1 and

\[
H(\xi)=((1-\xi)^2-4c\xi^3)^{-1/2}=\sum_{n\ge0}a_n\xi^n,\qquad
a_n=\sum_{j=0}^{\lfloor n/3\rfloor}\binom{2j}{j}\binom{n-j}{2j}c^j.
\]

The **normalized** invariant differential is -omega=H dxi; its formal-group logarithm is
\[
L(\xi)=\int_0^\xi H(u)\,du=\sum_{j\ge1}\ell_j\xi^j,
\quad \ell_j=a_{j-1}/j,\quad \ell_1=1,\quad\ell_2=1/2.
\]
Thus [p]_E(xi)=L^(-1)(p L(xi)). The choice -omega merely makes the logarithm's linear coefficient 1 and does not alter the multiplication map.

## New exact conditional all-p identity, with proof

**Lemma.** For a prime p>3 in any commutative p-adically integral coefficient ring containing c, assume a_(p-1) is divisible by p. Then coefficientwise in the fixed original E3 parameter, modulo p^3:

\[
\boxed{[\xi^p][p]_E(\xi)\equiv
 a_{p-1}-\frac{p^2}{2}\,C_p\pmod{p^3}},
\qquad
\boxed{C_p=\sum_{j=1}^{p-1}
 \frac{a_{j-1}a_{p-j-1}}{j(p-j)}\pmod p.}
\]

**Proof.** For j<p, the denominators j are units. For j=p, the explicit hypothesis p|a_(p-1) guarantees that ell_p=a_(p-1)/p is integral. All coefficients of L and its inverse through degree p are therefore p-integral. As ell_2=1/2, inversion gives L^(-1)(Y)=Y-Y^2/2+O(Y^3) with p-integral remainder through degree p. Substitute Y=p L(xi): terms Y^3 and higher vanish mod p^3. The pth coefficient of p L is a_(p-1), and the pth coefficient of L^2 is precisely C_p. This proves the formula. The symmetry reduction

\[
\boxed{C_p\equiv-\sum_{j=1}^{p-1}j^{-2}a_{j-1}a_{p-j-1}\pmod p}
\]

independently follows from p-j ≡ -j mod p and provides a second integer-only implementation. The lemma is conditional on p-divisibility; it does not independently prove supersingularity for arbitrary p.

## Executed original E3 p=373 exact witness

All numbers below are in R=(Z/373^3 Z)[T]/(T^2-2), with sigma(T)=-T, and 373^3=51,895,117. The original first-kind coefficient is **recomputed, not credited as new**:

\[
a_{372}=46,042,747+33,130,606\,T\pmod{51,895,117}.
\]

The **new signed bilinear correction** is

\[
C_{373}=46+350\,T\pmod{373},\qquad
C_{373}/2=23+175\,T\pmod{373}.
\]

Therefore

\[
\frac{373^2}{2}C_{373}
=3,199,967+24,347,575\,T\pmod{51,895,117},
\]

and the fixed-original-coordinate elliptic formal p-series yields

\[
\boxed{[\xi^{373}][373]_{E_c}(\xi)
 =42,842,780+8,783,031\,T\pmod{51,895,117}.}
\]

The divided coefficient is 114,860+23,547 T modulo 139,129. The nonlinear correction has **exact p-adic valuation two**: its divided-by-p^2 coefficient has nonzero norm

\[
N(23+175T)=23^2-2(175)^2\equiv78\not\equiv0\pmod{373}.
\]

Hence the naive equality between a_372 and [xi^373][373]_E at precision p^3 is **false**. This is a direct original-curve negative-control witness, not a counterexample to LIFT nor an H0/B0 calculation.

## Reproducible executable and scope of checks

Author code \`research_notes/portable_direct/d25_e3_formal_p_series_second_digit_20261027.py\`, separately persisted at GitHub commit \`a853be8bdef2d457f7d272ad11d3d31a6aeb8c60\`, was executed using Python's exact integer arithmetic on p = (13,19,37,43,61,67,211,373), both target classes. Two independent coefficient paths matched at *every index* a_0,...,a_(p-1): binomial closed form and the original differential ODE 2 D H'+D' H=0. Two independently reorganized C_p formulas matched, and explicit p=373 checks passed. Final observed marker: \`D25_ORIGINAL_E3_FORMAL_P_SERIES_SECOND_DIGIT_PASS\`.

Selected output pairs (p, C_p, p-series coefficient mod p^3): p=13 -> (10+8T,1209+793T); p=19 -> (13+3T,931+2831T); p=373 -> (46+350T,42842780+8783031T). The eight finite runs verify the stated inputs and arithmetic, not a universal LIFT theorem or a native benchmark.

## Actual BRC application, type boundary, and next exact action

BRC classification: **COMPOSE_APPLIED**. Carrier is the labeled sequence of original a_n with p-adic valuations, signed T branch and involution, **plus** the joint convolution C_p. Operation: fixed E3 formal p-multiplication; observer: coefficient [xi^p] modulo p^3; permitted future operations: same-parameter formal group substitution and Frobenius-basis comparison only after an independently established map. The map (a_(p-1),C_p) -> a_(p-1) alone is not observer-safe: C_373/2 is a nonzero unit. The exact information lost is the bilinear joint second-digit term. This external E3 algebra is an auxiliary task-local representation; it does not establish a Heartbeat native-X6 relation or an original H0/B0 isomorphism.

**Unfinished mother scientific target:** The frozen, same-original-class native H0/B0 divided-power benchmark at p=373 still needs the actual [X]U mod 139129, module rank, Frobenius direction/eta and normalization, odd signed Green/Hesse observer, original kappa and Delta_p-R_p. Existing support issue: https://github.com/awdawmip/enterprise-math/issues/1559, OPEN, PENDING_OWNER / NOT_EXECUTED as read on 2026-10-27. The new computed E3 p-series coefficient does not replace any of those native outputs.

Next exact action: a legitimate authorized native H0/B0 executor runs the original frozen input and persists raw reproducer plus p=373 results; if and only if its native representation is proven to match the original E3 formal group with this exact xi/basis, check the above p-series nonlinear correction and signed two-digit coefficient as a negative-control observer. An exact disagreement is itself evidence and is not coerced into a rank-one/norm shortcut.

Source/control at this run: \`em_control_continuation\` for this exact Task returned \`CONTROL_QUOTA\`; gateway status has \`research_authority_granted=false\` for this read-only Site identity; previous actual bridge dispatch issue #6576 was historically FAILED / TimeoutExpired. No new service session/CLAIM/open, no replayed mutation, no Source-native publish/Result/Driver review, and no maintenance identity was used. Old staging and prior accepted D24 evidence remain separate; the existing hourly task/schedule/notification configuration and the frozen scientific pin were not altered.

Consumed without redoing: source publication \`TP2-B6F4FC938FF94941C1B7\` at frozen c47; original E3 first/second differential note \`research_notes/portable_direct/20261027_onhour_d25_original_E3_second_kind_closed_coefficient_p373.md\`; prior signed CM/isogeny results; native support #1559. Registration and admissibility remain pending actual Source permission and independent review.
