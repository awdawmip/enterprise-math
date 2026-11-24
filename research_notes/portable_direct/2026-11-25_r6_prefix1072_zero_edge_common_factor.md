# PREFIX-1072 — Exact zero-edge common factor and high-order residual decay

Date 2026-11-25. AUTHOR_CONDITIONAL_EXACT_IDENTITY / HUMAN_RECHECKABLE_ANALYTIC_PROOF / NOT_REVIEWED. Independent informed continuation of EM-DIRECT-780BBE / TASK_RESEARCH; own session metadata recovered (MCP-f6d93209fc8e4c5bb2c3b44f69a47174), no formal CLAIM/run authority. Previous LEASED query r6-20261125-0550-owner-read completed SUCCEEDED with an empty filtered list as of 2026-11-24T21:52:08Z; current r6-20261125-0650-owner-read last observed RUNNING. No shared task mutation.

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Stage46 X6 candidate chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, precisely two negative steps. Retain full six-coordinate paired Cell equality, terminal ports, grade, phase, branch multiplicity. Parent exact BRC algebra: d91f254e8f1fc36e8f974fd5452a91144e46f570:research_notes/portable_direct/2026-11-24_r6_prefix1062_no_finite_shift_complete_monotonicity.md (executed checker defines N,H); e22d153b377149d9052d2395e9a4e288a74b8d8c:research_notes/portable_direct/2026-11-24_r6_prefix1065_cubic_observer_slope_bound.md (K4=0); 7fa8d53867199b47f7a27cc039cfd7ced67c69b9:research_notes/portable_direct/2026-11-25_r6_prefix1068_first_spectral_sign_boundary.md (exact CT observer); b0ee3a74d740af91ee1b8e59ecd38cb0542633f7:research_notes/portable_direct/2026-11-25_r6_prefix1071_second_saddle_reentrant_negative.md (remaining zero-edge problem). The analytic character readout is not a native spatial slice or physical time evolution.

## Main results

Let H_j denote the doubled terminal polynomial (j=1,2 in parent notation; 0,1 in the checker), S=sum z_i, S*=sum z_i^-1, x=SS*/36. In the Laurent coefficient ring, for every n,

    H_j=S^2 Q_j,   Q_1-Q_2 is divisible by S,
    H_1-H_2 is divisible by S^3.

In particular each port's paired polynomial is O(x^2) on the character quotient, and every coefficient K_a of H_1 H_1* - H_2 H_2* is O(x^(5/2)). This is exact joint BRC cancellation at the zero spectral coordinate, before taking any integral or approximation. The result does not erase any native state.

For each fixed integer n>=8 (m=n-8), the high-order signed difference obeys

    |D(n,k)|=O_n(k^(-m-7/2)) = O_n(k^(-n+9/2)), as k -> infinity.

The earlier PREFIX-1062 bound O_n(k^(-m)) required n>=9 for decay; this improvement also proves decay for n=8. It is an upper bound on magnitude, not a claim of eventual sign or a nonzero leading coefficient. In particular the zero-level observation cannot be treated as another copy of either nonzero saddle singularity.

## 1. Factorization directly from the frozen BRC numerator

Use the checker's zero-based axis labels i,h,j in {0,...,5}, j=0,1, distinguished blocked edge axis 0. Work in the commutative Laurent polynomial ring in the six z_i with formal t. Write b_i=z_i^-1, R=1-tS, delta=1 if j=0 and 0 otherwise. In the parent numerator:

    L_i=S-6z_i,
    A_i=1-6R*1_(i=0)-6tz_i,
    C_i=1-6R*1_(i=j)-6tz_i,
    K_ih=S-6z_i-6z_h+36*1_(i=h) z_i,
    B_ih=t R K_ih+t^2 L_i L_h.

Define U=sum b_i A_i, V=sum b_i C_i, W=sum b_i A_i C_i. Direct sums yield sum A_i=sum C_i=0 and

    U=S*-6R b_0-36t,
    V=S*-6R b_j-36t,
    W=S*-6R(b_0+b_j)+36 delta R^2 b_0-36t^2 S.

In the parent u=sum_(i,h) b_i b_h A_i C_h (R+B_ih), the K_ih term contracts to S UV+36 W, because the two sums of A and C vanish. The L_i L_h term contracts to S^2 UV. Thus

    u= [R+RtS+t^2 S^2] UV+36Rt W = UV+36Rt W.

Substitution in the exact parent numerator gives the compact identity

    N_j(t)=(1-z_0 t) UV + Rt(36-11z_0 t) W
           -10t^2 R^2 C_0 -390 z_0 t^3 R^2 -390 delta t^2 R^3.

This is an algebraic contraction of the already proven numerator, not a new propagation kernel. It keeps the distinguished axis and both port labels. It is valid in the whole Laurent ring, not just on a balanced character.

Let N_d=[t^d]N_j. The parent H routine is exactly

    H_j(n)=sum_(d=0)^5 (n-d-1)(n-d-2) N_d S^(5-d).

For d<=3 the explicit factor has degree at least two in S. For d=4,5 use the compact N identity. The t^2 coefficient of W is 36 delta S^2 b_0-36 S; its t coefficient is 6S(b_0+b_j)-72 delta S b_0. Hence W's t and t^2 coefficients are divisible by S. The t^3 coefficient of Rt(36-11z_0t) is 11Sz_0. The other terms in N give the same S-divisibility by their explicit R factors. Consequently N_4 is divisible by S, and the exact t^5 coefficient is

    N_5=726 S^2(delta S-z_0).

For clarity, N5 comes from four pieces: 396 delta S^3-396 z_0 S^2, -60 delta S^3+60 z_0 S^2, -390 z_0 S^2, +390 delta S^3. Thus H_j is divisible by S^2, with a polynomial quotient, without division at a zero of S.

To determine its common residue mod S, use the compact N identity:
    N_3 = -1626 z_0 mod S,
    N_4/S = 1056 z_0 mod S,
    N_5/S^2 = -726 z_0 mod S.

The N3 terms mod S are -1296 z_0, +60 z_0, -390 z_0. For N4/S mod S the nonzero terms are +396 z_0 from W's t^2 coefficient, -120 z_0 from -10t^2 R^2 C_0, and +780 z_0 from -390z_0t^3R^2. Terms with delta or W's t coefficient vanish at this order. These reductions are independent of j and valid even before setting S*=0.

It follows exactly that

    Q_j = H_j/S^2 = z_0 P(n) mod S,
    P(n)=-1626(n-4)(n-5)+1056(n-5)(n-6)-726(n-6)(n-7).

The same polynomial residue holds for both terminal ports. Therefore H_1-H_2 has a third factor S. No cancellation across different native final Cells has been used.

## 2. Improved bound on the signed joint observation

Set H_j=S^2 Q_j and Q_1-Q_2=S T with Laurent-polynomial coefficients in n. With the star reversing all displacement exponents, use the exact difference-of-products identity

    H_1 H_1* - H_2 H_2*
      = S^2(S*)^2 [ S T Q_1* + S* Q_2 T* ].

The coefficients of this polynomial in n are the K_a used in the existing observer (K4=0). All finite Laurent coefficient polynomials are bounded on the unit character torus. Hence for each a=0,...,3 there exists a finite C_a with

    |K_a(z)| <= C_a |S|^5 = 6^5 C_a x^(5/2).

This bound is on the exact signed paired observation, not a comparison of two unrelated positive branch counts. The same bound holds at every balanced collinear character (three plus, three minus) and on every noncollinear zero of S. Individually, the paired port weights vanish at least as |S|^4; the joint difference has an extra vanishing factor in magnitude.

## 3. Unweighted zero-edge mass bound

For the auxiliary unit character measure, x=|S|^2/36 has a bounded density on [0,1] (it suffices here to prove an upper bound for its pushforward measure). This can be shown without evaluating any trigonometric value or pi, by using the exact measure of the sum of two independent uniform unit characters. The sum of two has radial two-dimensional auxiliary density proportional to

    1/(r sqrt(4-r^2)),  0<r<2,

and zero outside. To derive the expression, condition on the relative character, whose real part has density proportional to (1-u^2)^(-1/2) on (-1,1) by the unit-circle change of variable. The squared radius is 2+2u. Rotation invariance then gives the displayed radial density by dividing the radial measure by the radial Jacobian r. All omitted normalizations are finite positive constants; none is numerically evaluated. This is auxiliary harmonic measure for the established CT, not a physical plane or native update.

This two-character density is in L^(3/2): the polar integrand near zero behaves as r^(-1/2), and near r=2 as (2-r)^(-3/4), both integrable. Three independent such pairs produce the six-character sum; convolution of two L^(3/2) functions is L^3 by Young's inequality, then convolution with the third L^(3/2) is L^infinity by Holder. Thus the auxiliary sum has bounded density. In particular for a radial nonnegative measurable test phi,

    integral phi(|S|^2/36) dHaar <= C integral_0^1 phi(x) dx.

The diagonal quotient leaves this radial expectation unchanged; all K_a have zero net displacement. This bound bypasses the singular rank of the S=0 map at balanced collinear characters without dropping their contribution.

## 4. High-order difference bound and a new endpoint consequence

The exact prior observer reads D(m+8,k)= (4*36^8)^(-1) sum_a CT[K_a (E+8)^a f], f=x^m(1-x)^k and E=x d/dx. For fixed m>=0 expand the operator by conjugating x^m; each term is a fixed coefficient times (k)_l x^(m+l)(1-x)^(k-l), l<=a<=3. For k>=6 use (k)_l<=k^l and (1-x)^(k-l)<=exp(-kx/2). Combining section 2 and the unweighted density bound of section 3 gives

    |D(m+8,k)| <= C_m sum_(l=0)^3 k^l integral_0^1 x^(m+l+5/2) exp(-kx/2) dx
               <= C'_m k^(-m-7/2).

The final inequality follows by changing u=kx and extending the nonnegative integral to infinity; its constant is finite. This improves the previous upper bound by a factor O(k^(-7/2)) in asymptotic order for fixed n>=9. It also proves convergence to zero for n=8. Thus the PREFIX-1062 telescoping identity holds at n=8 as well:

    D(n,k)=sum_(j=k)^infinity D(n+1,j),   n>=8,

with absolute convergence, and the omitted tail after j=K is exactly D(n,K+1)=O_n(K^(-n+9/2)). This identity is inherited from finite difference propagation, but the endpoint and decay rate are new.

## Evidence and next problem

Human-recheckable exact symbolic derivation from the frozen paired BRC numerator and an analytic bound on its proven CT observer. No newly executed path enumeration, native physical kernel, classical reference computation, pi evaluation, quadrature, or numeric fitting. No claim of a sharp exponent, eventual zero-edge sign, or additional sign window. Prior source evidence remains at original pins; independent review pending. Next: exploit Q_j's common residue and compute the first noncancelled joint term after averaging on the zero fiber S=0, including the balanced critical characters. This is needed to determine the sign at k much larger than n. Continue the independent regular-boundary b location and middle-band classification; mother B_fix,odd(32) remains open.
