# PREFIX-1074 — Linear fourth recovery via weak zero-edge scaling and the lower regular sign boundary

Date 2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Independent portable continuation of EM-DIRECT-780BBE / TASK_RESEARCH, same own session MCP-f6d93209fc8e4c5bb2c3b44f69a47174 (metadata recovered, no formal CLAIM/run authorization). Prior owner query r6-20261125-0750-owner-read SUCCEEDED, LEASED empty at 2026-11-24T23:52:13.587247Z. Fresh owner query r6-20261125-0850-owner-read last observed RUNNING / SOURCE_MATERIALIZATION. No shared task mutation.

Frozen scientific input: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json, same Stage46 chart O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve full X6 joint Cell equality, terminal ports, grade, phase, sign, multiplicity. The auxiliary scalar CT representation below is the exact paired observer only, not a new spatial carrier, physical propagation or reference model.

Parents read at immutable commits:
- cc1fa4471149037fc07977d0cc27e532e75a5f61:research_notes/portable_direct/2026-11-25_r6_prefix1073_zero_edge_sharp_positive_tail.md (zero-edge coefficientwise continuous-density expansion and exact F(4)>0).
- b0ee3a74d740af91ee1b8e59ecd38cb0542633f7:research_notes/portable_direct/2026-11-25_r6_prefix1071_second_saddle_reentrant_negative.md (negative left neighborhood of x1=1/9).
- 7fa8d53867199b47f7a27cc039cfd7ced67c69b9:research_notes/portable_direct/2026-11-25_r6_prefix1068_first_spectral_sign_boundary.md (exact observer, critical values, real analytic regular-band densities).

## 1. New results

With m=n-8 and D(n,k)=L(x^m(1-x)^k), let g be the ordinary effective density on the lower regular band (0,1/9). Under the inherited parent statements, define
    b_low = sup {x in (0,1/9): g(x)>0}.
Then 0<b_low<1/9. Put rho_low=1/b_low-1>8. There is a fixed negative witness x_- in (b_low,1/9) sufficiently close to 1/9; let rho_-=1/x_--1. For all sufficiently large m the first strictly positive integer observation after floor(rho_- m) exists and satisfies
    R(m)=min {k>=floor(rho_- m): D(m+8,k)>0}
        = rho_low m + O(1).
In fact there is a unique local continuous crossing k_real(m)=rho_low m+c_low+o(1) and R(m)=floor(k_real(m))+1. If
    g(b_low+y)=a y^r+d y^(r+1)+O(y^(r+2)),
then r is odd, a<0, and
    c_low=(r+2)(1-2 b_low)/(3 b_low)+(1-b_low)d/a.
This locates a negative-to-positive transition following the second saddle on a fixed linear scale, rather than merely at a possibly superlinear k. It is the first recovery after the specified fixed regular negative witness, not a global enumeration of all sign changes. No numerical b_low, global upper bound on sign changes, or uniform positivity for all k/n sufficiently large is asserted.

## 2. Weak zero-edge scaling avoids unjustified differentiation

Inherited exact observer:
    L(f)=c sum_(a=0)^3 integral w_a(x) (E+8)^a f(x) dx,
    c=1/(4*36^8), E=x d/dx.
Here w_a is the signed/complex-weight pushforward of K_a; the paired weights and resulting observer are real. L is a bounded functional on C^3. PREFIX-1073 proves coefficientwise
    w_a(x)=36^3 h(0) F_a x^3 + o(x^3),
    F(z)=sum F_a z^a=(12/5)L_pol(z)[C_pol(z)+L_pol(z)],
    F(4)=4283136/5>0, h(0)>0.
The notation L_pol distinguishes the parent polynomial from the observer L. The expansion is a statement of the continuous weighted densities, not their third derivatives.

For any fixed psi in C_c^3((0,infinity)), set f_e(x)=psi(x/e), e>0 sufficiently small. E f_e=(u d/du)psi at u=x/e, so the first three Euler derivatives of the rescaled test remain bounded in u, independently of e. Substituting x=e u gives
    e^(-4) L(f_e) -> c*36^3*h(0) sum F_a integral u^3 (u d/du+8)^a psi(u) du
                  = A0 integral u^3 psi(u) du,
    A0=h(0) F(4)/(4*36^5)>0.
The remainder is o(1) by uniformity of the original little-o on the rescaled compact support, with no derivative estimate of the remainder. Repeated integration by parts is exact: adjoint of u d/du on u^3 du acts by -4; compact support kills boundaries.

On the open band, the regular-level analytic-flow argument from PREFIX-1068 yields real analytic w_a and hence g=c sum (7-E)^a w_a. Thus for every 0<A<B<infinity and every sufficiently small e there is a positive point of g in (Ae,Be). Indeed choose a nonnegative nonzero C^3 test supported there after rescaling, e.g. psi=(u-A)^4(B-u)^4 on [A,B], zero elsewhere. The limit is strictly positive and L(f_e)=integral g f_e on that compact subinterval of the regular band. This establishes positive points at arbitrarily small scales, even though pointwise positivity of g near zero does not follow from the density little-o. In particular it is incorrect to differentiate the parent o(x^3) three times without additional regularity. The new result is weak convergence of e^-3 g(e u) against compact tests away from zero.

## 3. Lower regular band boundary and finite slope

PREFIX-1071 gives g(x)<0 in a left neighborhood of 1/9. Section 2 gives positive points below it. Thus b=b_low lies strictly between 0 and 1/9. By continuity g(b)=0, and by real analyticity (the band is connected and g is not identically zero) its order r is finite. There are positive points arbitrarily close below b by its definition and no positive points above b; consequently r is odd and the leading coefficient a is negative. In a sufficiently small fixed neighborhood of b, g is positive below and negative above. In the rest of (b,1/9), g<=0 with only isolated zeros. Choose x_- in the strictly negative saddle-side neighborhood and greater than b.

We use a phase-gap fact for the inherited finite-order observer. For k/m in a compact positive interval, phi_rho=log x+rho log(1-x) has a unique maximum x_rho=1/(1+rho). On a closed region away from the maximum the C^3 norms of x^m(1-x)^k times a fixed cutoff are bounded by a polynomial in m times an exponentially smaller phase envelope. This follows by differentiating at most three times (powers m,k reduced by at most three) and maximizing the resulting beta-type powers on the closed region. The same holds for one real k derivative on a fixed positive rho interval: log(1-x) factors can be bounded using a further lost power at x=1. Thus remote singular distributions are controlled by the C^3 bound of L, not integrated as nonintegrable pointwise functions. On a regular local neighborhood the observer is the ordinary g integral.

For a compact set of ratios between rho_- and rho_low-delta, all saddle positions lie in a compact subinterval of (b,1/9) where g<=0. Strict negative sign follows uniformly for large m. To see why an isolated even-order zero is harmless, use contradiction and extract a converging subsequence of ratios. In a fixed small regular neighborhood of its limiting saddle, either g is strictly negative or -g(x)>=C|x-x_z|^q with one finite even-order zero x_z. In an interval of length proportional to m^-1/2 within a bounded number of such widths of the current saddle, at least a fixed fraction of that interval has |x-x_z|>=c'/sqrt(m). The local negative integral is at least a constant times f(x_rho) m^(-(q+1)/2) in magnitude; the remainder is exponentially small by the phase gap. The same argument proves negativity with floors at the starting ratio. At a fixed ratio just above rho_low, g at the saddle is strictly positive, so eventual positivity follows by the identical local integral argument. This already proves R(m)/m -> rho_low and gives a linearly separated recovery after the second saddle. In particular the fourth witnessed sign alternation can occur at O(n), not merely at an unspecified high-order scale.

## 4. Bounded and explicit local shift

Write b=b_low, rho=1/b-1, c_shift=k-rho*m, V=b^2(1-b). For bounded real c_shift put x=b+y/sqrt(m), and normalize f=x^m(1-x)^k by f(b). The log phase near b is
    -y^2/(2V)+m^-1/2 [phi'''(b)y^3/6-c_shift*y/(1-b)]
       + O(m^-1 (|y|^2+|y|^4)),
    phi'''(b)=2(1-2b)/(b^3(1-b)^2).
Taylor expansion on |y|<=m^eta for small eta>0 and Gaussian-polynomial domination (with a phase gap off that neighborhood) justify termwise integration uniformly for bounded c_shift, including one c_shift derivative. Write I_j=integral_R y^j exp(-y^2/(2V))dy. Odd I_j vanish, and integration by parts gives I_(r+3)=(r+2)V I_(r+1). Using the Taylor expansion of g, the first nonzero scale is
    m^((r+2)/2) D(m+8,k)/f(b)
      -> I_(r+1) [ d + a*phi'''(b)*(r+2)*V/6 - a*c_shift/(1-b)].
The limit has strictly positive derivative because a<0. Its unique root is exactly c_low in Section 1. Uniform C^1 convergence on compact c_shift intervals yields a unique local zero c_m=c_low+o(1), with the expected signs on either side in a fixed compact window containing it.

To ensure there is no earlier positive value outside this bounded window but near rho, choose a nonnegative fixed smooth cutoff supported in the local one-sign-change neighborhood of b, equal to 1 near b. The normalized local integral
    J_m(k)=integral cutoff(x) g(x) (x/b)^m ((1-x)/(1-b))^k dx
is strictly increasing in k: g and log((1-x)/(1-b)) have the same sign on either side of b. For rho' in a sufficiently small fixed neighborhood of rho, the complement has an exponential gap relative to f(b) uniformly, also with one k derivative, since the maximum of phi_rho on the complement is strictly below phi_rho(b) and the gap survives small changes of ratio. At k=rho m+c_low-1 and +1, J_m has opposite signs bounded away from zero at the scale m^(-(r+2)/2). Monotonicity preserves those signs for all k farther outward within the fixed ratio neighborhood; exponentially small complement cannot reverse them. Within the bounded window, C^1 convergence gives the unique continuous zero and strict orientation. Combined with Section 3's compact negative region, the first strictly positive integer after floor(rho_- m) equals floor(k_real(m))+1, including when the continuous zero itself is integral. This proves the claimed bounded shift and its explicit limit.

## 5. Scope, next question

Analytic derivation only, based on the exact already paired BRC observer. No fresh native kernel, path enumeration, classical trigonometric or pi evaluation; no numerical claim, no independent review. The weak-scaling argument and monotone localized integral are reusable on other inherited regular BRC bands with a finite-order sign-changing zero. The proof preserves full pre-pair carrier and only uses the certified scalar observer. The next useful step is to compute or certify b and b_low and their odd multiplicities, or to derive differentiable zero-edge weighted density estimates that determine whether g is eventually pointwise positive and whether additional lower-band sign boundaries exist. Mother B_fix,odd(32) remains open.
