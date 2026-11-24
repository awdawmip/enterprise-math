# PREFIX-1073 — Sharp positive zero-edge tail from exact exchange cancellation

Date: 2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_SYMBOLIC_COEFFICIENT_CHECKED / NOT_REVIEWED. Independent continuation of the existing EM-DIRECT-780BBE / TASK_RESEARCH scientific line; source session metadata MCP-f6d93209fc8e4c5bb2c3b44f69a47174 read back, no formal CLAIM/run authority asserted. Prior owner query r6-20261125-0650-owner-read SUCCEEDED, empty LEASED list at 2026-11-24T22:51:51.086766Z. New owner read r6-20261125-0750-owner-read last observed RUNNING / SOURCE_MATERIALIZATION. No shared task mutation.

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Same Stage46 candidate, chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full six-axis joint Cell equality, ports, grade, phase, sign and multiplicity retained. Source: d91f254e8f1fc36e8f974fd5452a91144e46f570:research_notes/portable_direct/2026-11-24_r6_prefix1062_no_finite_shift_complete_monotonicity.md; e0f2b98af08e22ba965ccee820c395b7ab776e6c:research_notes/portable_direct/2026-11-25_r6_prefix1072_zero_edge_common_factor.md (read back in full, exact compact N and observer); b0ee3a74d740af91ee1b8e59ecd38cb0542633f7:research_notes/portable_direct/2026-11-25_r6_prefix1071_second_saddle_reentrant_negative.md (prior reported second saddle). Auxiliary character integral is only the exact CT readout, not a spatial carrier or propagation kernel.

## Result

Write m=n-8, S=sum z_i, B=S*=sum z_i^-1, x=SS*/36. Let h(x) be the unweighted pushforward density of x in the normalized character CT observer, with continuous extension h(0)>0. For each fixed integer n>=8,

    D(n,k) ~ [h(0)/(4*36^5)] * (4283136/5) * Gamma(n-4) * k^(-(n-4)).

In particular D(n,k)>0 for all sufficiently large k at every such fixed n. This sharpens the PREFIX-1072 magnitude bound by an extra half power and determines a strictly positive leading coefficient. Together with the prior conditional saddle results (PREFIX-1068/1070/1071), for sufficiently large n there are at least four strict-sign alternations as k increases: positive, negative, positive, negative, positive (zeros may intervene). No global sign-count upper bound, explicit finite onset or uniform joint n,k tail asserted.

## 1. First surviving polynomial term

Use zero-based port labels j=0,1 as in parent checker. Put z=z_0, b=z_0^-1, c=z_j^-1, delta=1_(j=0), R=1-tS. PREFIX-1072's exact contraction is

    U=B-6Rb-36t, V=B-6Rc-36t,
    W=B-6R(b+c)+36 delta R^2 b-36t^2 S,
    C0=1-6R delta-6tz,
    N=(1-zt)UV+Rt(36-11zt)W-10t^2R^2 C0
        -390zt^3 R^2-390 delta t^2 R^3,
    H_j(n)=sum_(i=0)^5 (n-i-1)(n-i-2) [t^i]N S^(5-i).

Factor H_j=S^2 Q_j. Extraction of the constant and linear powers of formal S in Q_j yields the exact Laurent-ring identity

    Q_j=z P(n)+S A_j+S^2 V_j,
    P=-1296 n^2+12456 n-31332,
    A_j=B z J+z(b+c)L+C,
    J=72 n^2-526 n+952,
    L=-432 n+1860,
    C=1296 n^2-11664 n+28492.

Here V_j denotes a finite Laurent polynomial, not the earlier V in N. S,B can be handled as formal independent symbols for this coefficient calculation and then substituted by their six-character sums. Indeed all negative S powers in Q cancel by the exact divisibilities in PREFIX-1072. The first-order coefficients are independent of delta; the formula above is checked below by exact polynomial arithmetic.

Consequently A_0-A_1=z(b_0-b_1)L. On the unit torus z z*=1. Write K(n)=H_0 H_0*-H_1 H_1*=sum_(a=0)^3 n^a K_a (quartic vanishing from PREFIX-1065). Expand:

    K(n)/|S|^4 =
       P L [S(b_0-b_1)+S*(z_0-z_1)]
       + |S|^2 (A_0 A_0*-A_1 A_1*)
       + S^2 P z* (V_0-V_1) + (S*)^2 P z (V_0*-V_1*)
       + O_n(|S|^3).

This expression is a polynomial identity with bounded higher-degree remainder (interpreted before division at S=0). The first line is antisymmetric under exchange of axes 0 and 1, while S and every radial test remain invariant. Thus its CT integral against every radial function is exactly zero, coefficientwise in n. This does not erase branch identity: it applies only after the already-established full signed pair observer, within its scalar radial test family.

## 2. Weighted character densities at zero

For any finite Laurent polynomial W on the six unit characters, its pushforward under S has a bounded continuous complex density p_W on the auxiliary complex coordinate. For a monomial, split its weight into the product of weights on three independent pairs. Each weighted two-character sum has a density dominated in absolute value by the unweighted pair density from PREFIX-1072 (Radon-Nikodym domination follows from absolute weight one). The latter belongs to L^(3/2), including both radial endpoints. Young's inequality gives the first two pair convolution in L^3; Holder and continuity of translations in L^(3/2) give a bounded continuous convolution with the third pair. Extend by finite linearity. This argument covers the balanced critical characters without assuming a regular zero fiber.

In particular p_1(0)>0: unweighted pair densities are positive almost everywhere on the open radius-two disk. In the triple convolution integral at zero, restrict both integration variables to a small disk, excluding the measure-zero locations with zero radius. The third argument then lies inside the positive disk as well, yielding strictly positive integral. With normalized Haar, h(x) is the radial pushforward of p_1, continuous at zero and h(0)>0. The radial coordinate Jacobian is constant for x=|S|^2/36; its actual numeric normalization is not needed.

For any homogeneous weight W of nonzero character degree q, rotate all six characters by a common unit multiplier eta. The pushforward transforms covariantly, so continuity at zero implies p_W(0)=eta^q p_W(0) for all eta, hence p_W(0)=0. This is a statement about the auxiliary CT representation, not a native spatial rotation or update. In the above expansion, z*(V_0-V_1) has degree -2: H has degree 3, Q degree 1, and its S^2 remainder degree -1. Therefore both S^2 terms contribute o(x^3) to the radial density of K(n), including at balanced critical characters. For the O(|S|^3) remainder, finite polynomial weights and bounded p_1 give O(x^(7/2)) after the outer |S|^4.

The B z J term in A_j is O(|S|), so it does not affect the x^3 coefficient. At the zero endpoint the remaining A_0=C+2L and A_1=C+L+L z_0 z_1^-1. By symmetry of the unweighted measure and the exact identity

    |S|^2=6+sum_(i!=j) z_i z_j^-1,

the continuous weighted densities at S=0 satisfy p_(z_0 z_1^-1)(0)=-p_1(0)/5. Indeed all 30 off-diagonal weights have identical densities and the left side is |w|^2 p_1(w), zero at w=0. Thus the zero-edge density ratio for |A_0|^2-|A_1|^2 is

    (C+2L)^2-[(C+L)^2+L^2-(2/5)L(C+L)]
       = (12/5)L(C+L) = F(n).

This is a relation between continuous densities, not an unproved conditioning on a probability-zero event.

Since |S|^6=36^3 x^3, the radial density of K(n) is

    36^3 h(0) F(n) x^3+o_n(x^3).

By polynomial interpolation in n this holds coefficientwise for K_a with F(n)=sum_a F_a n^a. In particular no derivative regularity of the weighted density at zero is required.

## 3. Observation and actual leading sign

The exact parent CT observer is

    D(m+8,k)=(4*36^8)^(-1) sum_a CT[K_a (E+8)^a f],
    f=x^m(1-x)^k, E=x d/dx.

The crucial point is that the coefficient polynomial F must be evaluated at 4, not the fixed path index n. For k>3, integrating by parts with respect to dx gives exactly

    integral_0^1 x^3 (E+8)^a f dx = 4^a B(m+4,k+1).

Boundary terms vanish at zero (m>=0) and one (k>3); E adjoint on x^3 is -4. For the little-o(x^3) remainders, expand (E+8)^a f as a finite sum of constants depending on m,a times (k)_l x^(m+l)(1-x)^(k-l), 0<=l<=a. On a sufficiently small zero-edge neighborhood the remainder is bounded by epsilon x^3, yielding O_m(epsilon k^(-m-4)); away from zero the bounded polynomial weights have exponentially small contribution as k grows. Thus the total remainder is o_m(k^(-m-4)). Beta asymptotic now gives the stated result since

    F(4)=(12/5)*132*2704=4283136/5>0.

The contrast is meaningful: F(n) is negative for n>=8, but the high-order observed sign is positive because its coupled derivative observer evaluates the coefficient polynomial at 4. Taking a sign before applying the complete observer would give the wrong conclusion. This argument uses no new native propagation or classical numerical reference.

## 4. Executed exact symbolic coefficient check

The following standalone code was executed using SymPy polynomial arithmetic on the inherited BRC numerator. It checks the new coefficients and F(4) exactly (not a new reference model or path enumeration).

```python
import sympy as s
t,S,B,z,b,c,d,n=s.symbols('t S B z b c d n')
R=1-t*S
U=B-6*R*b-36*t
V=B-6*R*c-36*t
W=B-6*R*(b+c)+36*d*R**2*b-36*t**2*S
C0=1-6*R*d-6*t*z
N=s.Poly(s.expand((1-z*t)*U*V+R*t*(36-11*z*t)*W
    -10*t**2*R**2*C0-390*z*t**3*R**2-390*d*t**2*R**3),t,S)
w=lambda i:(n-i-1)*(n-i-2)
P=-1626*w(3)+1056*w(4)-726*w(5)
Q0=s.expand(sum(w(i)*N.coeff_monomial(t**i*S**(i-3))
                for i in range(3,6)))
assert s.expand(Q0-z*P)==0
A=s.expand(sum(w(i)*N.coeff_monomial(t**i*S**(i-2))
               for i in range(2,6)))
L=-432*n+1860
C=1296*n*n-11664*n+28492
J=72*n*n-526*n+952
assert s.expand(A-(B*z*J+z*(b+c)*L+C))==0
F=s.expand(s.Rational(12,5)*L*(C+L))
assert F.subs(n,4)==s.Rational(4283136,5)
print('PREFIX1073_ZERO_EDGE_ALGEBRA_PASSED')
```

Actual output: P=-1296*n**2+12456*n-31332; A=B*z*J+z*(b+c)*L+C; F=-6718464*n**3/5+91632384*n**2/5-427327488*n/5+135491328; F(4)=4283136/5; PREFIX1073_ZERO_EDGE_ALGEBRA_PASSED.

## Next

The fixed-n high-order limit and the two earlier saddle windows now imply at least four alternations, conditional on the parent saddle proofs. Obtain a positive zero-edge effective density on an explicit interval or a uniform joint n,k estimate to locate the fourth transition, then classify the regular bands, including the first upper sign boundary b. The present little-o estimate is for each fixed n, not a uniform claim about k/n. No new path enumeration, classical trigonometric/ pi evaluation, or physical inference; review pending. Mother B_fix,odd(32) remains open.
