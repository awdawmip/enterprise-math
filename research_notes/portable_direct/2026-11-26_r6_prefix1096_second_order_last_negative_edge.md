# PREFIX-1096 — Certified second-order location of the last negative observation

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_CERTIFICATE / NOT_REVIEWED. Independent continuation of EM-DIRECT-780BBE / TASK_RESEARCH; metadata for the existing own session recovered by r6-20261126-0650-own-recovery (original registration r6-20261123-2358-session-start-own-v1, no runs). Current owner list r6-20261126-0650-owner-read SUCCEEDED / error=null, Source 7f4428ed75b89b1f525e4e24311236d6ac916c75, fixed as-of 2026-11-25T22:51:37.023550Z, LEASED filter empty, no shared Task/CLAIM mutation. No execution authority inferred from either read.

Frozen input P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. The six-axis path, port, phase, sign, ordered multiplicity and Cell equality remain in the original exact joint BRC observer; only its already-proved radial test identity is used. No classical numerical reference or new native propagation.

Exact parents:
- 08f0330096daa21d866aef04ea1db0c6d4f24384:research_notes/portable_direct/2026-11-26_r6_prefix1095_certified_lower_edge.md
- dc4fcdd14e85a886f07b6484ee67acd260e5081a:research_notes/portable_direct/2026-11-26_r6_prefix1095_frobenius_certificate.py
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md
- derivative reproduction: 2d373f42f619a15fda899f0d36b62689725b2fed:research_notes/portable_direct/2026-11-26_r6_prefix1096_edge_shift.py (blob b1843b853ed42a7d2b986d0933a79a202413071d, full text readback verified).

## 1. Result

Write D(m+8,k)=L(x^m(1-x)^k), with L the inherited finite C^3 signed observer, and b the first negative spectral edge of PREFIX-1095. At b, g(b)=0 and g'(b)<0. Define rho=1/b-1, v=b(1-b), L0=1-2b and r_j=g^(j)(b)/g'(b) for j=2,3,4. There is a unique real zero in the last-negative crossing neighborhood for large integer m, and the following refinement of PREFIX-1075 holds:
    k_*(m) = rho*m + c + d/m + O(m^-2),
    A = -v*r_2/2,
    c = (1-A)/b-2 = (1-2b)/b + (1-b)*r_2/2,
    d = -(c+2)*A + (r_2/2)*(A*L0-(c+3)*v+A^2)
                    + (r_3/6)*v*(2*L0+3*A) + (r_4/8)*v^2.
The inherited global last-negative theorem gives K_last(m)=ceil(k_*(m))-1, including integer zero. The new O(m^-2) is an asymptotic bound, not an explicitly paid finite-size error yet.

Actual rational enclosures, with endpoints specified as integers divided by the indicated powers of 10:
    rho*10^12 in [21440036717387,21440036723988]
    r_2*10^6 in [164743442,164743446]
    r_3*10^6 in [16424231512,16424232059]
    r_4*10^6 in [1222872258299,1222872360077]
    c*10^6 in [99141009,99141012]
    d*10^6 in [9690788,9690937].
In particular c is approximately 99.14101 and d approximately 9.69086, both strictly positive. The large constant c is relevant even when the leading slope is already well resolved; the sign of d gives the direction of the next real-boundary correction. Do not infer exact finite integer crossing solely from the displayed expansion or from a rounded rho.

## 2. Proof of the new second-order formula

Use the exact observer identity from PREFIX-1075 and a smooth cutoff chi supported in a small regular neighborhood of b, equal to 1 on a smaller one. The local contribution is the ordinary integral of chi*g against x^m(1-x)^k. For k=rho*m+O(1), the rest is exponentially small relative to the beta normalization B(m+1,k+1), uniformly in bounded shifts. Indeed m log x + k log(1-x) has unique maximum near b and a strict phase gap outside the smaller neighborhood; the inherited C^3 observer bound pays only polynomial factors in m,k. The same holds for a k derivative with a log(1-x) factor (near 1 absorb the logarithm into one power of 1-x). These real tests are C^3 for sufficiently large m,k. Thus normalized D and its k derivative can be computed asymptotically using a Beta(m+1,k+1) variable X and chi*g. This is an analytic identity on the scoped BRC observer, not a substitute propagation.

Put k=rho*m+c+d/m and Y=X-b. For A=1-b(c+2), v=b(1-b), the exact raw moments are E[X^j]=(m+1)_j/(m+k+2)_j, with rising factorials. Expanding the rational expression for centered moments gives
    E[Y] = b*A/m - b^2*(d+(c+2)*A)/m^2 + O(m^-3),
    E[Y^2] = b*v/m + b^2*(A*L0-(c+3)*v+A^2)/m^2 + O(m^-3),
    E[Y^3] = b^2*v*(2*L0+3*A)/m^2 + O(m^-3),
    E[Y^4] = 3*b^2*v^2/m^2 + O(m^-3),
    E[Y^5] = O(m^-3), E[Y^6] = O(m^-3).
The remainders are uniform for c,d in compact sets, since the rational functions in 1/m are analytic at zero with b fixed. A local Taylor expansion through degree 5 has remainder bounded by a constant times |Y|^6; away from the local neighborhood the beta probability is exponentially small. Hence the normalized observation through m^-2 is
    (b/m)*(g'(b)*A+g''(b)*v/2)
    +(b^2/m^2)*[-g'(b)*(d+(c+2)*A)
                 +g''(b)/2*(A*L0-(c+3)*v+A^2)
                 +g'''(b)/6*v*(2*L0+3*A)
                 +g''''(b)/8*v^2] + O(m^-3).
Cancel the first and second coefficients to obtain the stated c,d. The fifth signed moment must be used here; bounding it solely by its absolute moment would give a weaker error order.

For fixed bounded shift s=k-rho*m, the derivative in k of E[chi*g(X)] is Cov(chi*g(X),log(1-X)). Expand both functions near b. The linear terms give -g'(b)*Var(X)/(1-b), the other terms are O(m^-3/2) by centered moment bounds and phase-gap control of the complement. Var(X)=b^2(1-b)/m+O(m^-2), hence derivative = -b^2*g'(b)/m+O(m^-3/2)>0 uniformly. The normalized full observer has the same derivative to this accuracy by the differentiated phase gap. At the proposed k0=rho*m+c+d/m its value is O(m^-3). The positive derivative on a fixed bounded shift interval brackets a unique real zero at k0+O(m^-2) (take endpoints k0 +/- C/m^2 with sufficiently large C). The global last crossing and exclusion of later negatives are inherited from PREFIX-1075, with first-edge hypotheses discharged by PREFIX-1095. The proof neither assumes nor establishes that all other spectral zeros have been classified.

Local exact symbolic verification of all six centered moment coefficients (Python/SymPy):
    import sympy as s
    b,c,d,z=s.symbols('b c d z', nonzero=True)
    A=1-b*(c+2); v=b*(1-b)
    T=1/b+(c+2)*z+d*z*z
    raw=[s.Integer(1)]
    for j in range(6):
        raw.append(s.series(raw[-1]*(1+(1+j)*z)/(T+j*z),z,0,3).removeO().expand())
    expected=[b*A*z-b*b*(d+(c+2)*A)*z*z,
              b*v*z+b*b*(A*(1-2*b)-(c+3)*v+A*A)*z*z,
              b*b*v*(2*(1-2*b)+3*A)*z*z,3*b*b*v*v*z*z,0,0]
    for n in range(1,7):
        centered=sum(s.binomial(n,j)*(-b)**(n-j)*raw[j] for j in range(n+1))
        assert s.expand(centered-expected[n-1])==0
Actual execution: all six assertions passed. This is a symbolic verification of exact moment algebra, not a separate physical reference.

## 3. Rigorous derivative certificate at the first edge

Use PREFIX-1095's exact factorization, t=sqrt(36x):
    g(x)=constant * J(t) * F(t),
    J(t)=t^6/[(t^2-16)^3(t^2-4)^3].
The polynomial row N(t^2) of the nine-state observer is reconstructed from the same 66 signed Laurent terms and 28-to-7 elimination, and the four regular-singular basis series with the same rational 201-coefficient recurrence are rebuilt. The two mixed homogeneous basis terms remain included. Reuse the six exact anchor intervals and the t-root interval from the verified parent source (not independently re-anchored in this turn).
The degree <=104 truncated center polynomial uses n<=40. For each derivative j=0,...,4, use parameter half-width times absolute derivative polynomial bound, plus product-rule bounds for the omitted n=41,...,200 terms and the geometric series tail. Specifically for offset a=2*lambda and n>=J0=201, the parent analytic-factor coefficient bound is 64*T_lambda*2^-n. The j-th derivative term at Tmax=13/10 is bounded by
    u_n = 64*T_lambda*2^-n * (a+2n)_(falling j) * Tmax^(a+2n-j).
For n>=J0, the ratio u_(n+1)/u_n is bounded by
    q_j=(Tmax^2/2)*[(a+2J0+2-j+1)/(a+2J0-j+1)]^j < 1
for every j<=4 and each basis. This follows by bounding each of the j falling-factor ratios by the one with the smallest denominator. Therefore the tail is <=u_J0/(1-q_j). Multiply by the exact polynomial-row derivative norm using the Leibniz binomial coefficients; include all six parameter uncertainties. Evaluate the center polynomials by exact rational interval Horner over the parent root interval. No floating sign decision is used.

To convert the t derivatives to x derivatives without dividing an uncertain near-zero function value, define B_{0,0}=1 and
    B_{r+1,j}=(18/t)*(B'_{r,j}+(J'/J)*B_{r,j}+B_{r,j-1})
with missing entries zero. Then D_x^r(JF)=J*sum_j B_{r,j}F^(j), and at the exact root the j=0 term is identically zero. Use J'/J=6/t-6t/(t^2-16)-6t/(t^2-4). Thus
    r_j = sum_(i=1..j) B_{j,i} F^(i) / [(18/t)F'].
All rational-function denominators have interval sign excluding zero. The exact interval division yields the enclosures of section 1.

Local actual derivative output, each pair an outward-rounded integer enclosure after multiplication by 10^3:
    F:    [-11440,11592]
    F':   [-9569233632196,-9569233570362]
    F'':  [42988217567996,42988217762433]
    F''': [-10022877544777,-10022876931102]
    F'''':[ -324563199094393,-324563196764399]
F contains zero as expected, F' strictly negative. The c,d values in section 1 were produced by exact interval arithmetic applied to the proven symbolic formula. All checks of reconstructed readout dimensions, rank-28 reconstruction hash, 66 terms, polynomial degrees, indicial diagonalization, contraction constant and resonance compatibility passed in the executed local reconstruction. The saved companion uses the verbatim parent prefix through basis construction and the same derivative algorithm, with output interval assertions. That consolidated remote version has been read back but not separately executed; the local equivalent reconstruction and derivative computation were executed successfully. Parent anchors and prior complete root proof have not been independently rerun here. No independent mathematical review, no new native path enumeration, no formal checker proof.

## 4. Next

Derive an explicit computable O(m^-2) constant and activation threshold by the same local derivative certificate plus the C^3 phase-gap bound. This would allow an integer K_last certificate when the predicted real root interval avoids integer ambiguity. For ambiguous rows retain exact CT evaluation near the candidate crossing, not an asymptotic rounding guess. Further classify remaining regular-band zeros and distinguish b_last and b_low. The mother B_fix,odd(32) and global p,d (not the local expansion coefficient d above) remain open. No formal Result freeze, Working Truth promotion or Task completion.
