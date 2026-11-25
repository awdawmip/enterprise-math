# PREFIX-1075 — Differentiable zero-edge BRC observer, uniform positive tail and last negative boundary

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Existing independent line EM-DIRECT-780BBE / TASK_RESEARCH, own session MCP-f6d93209fc8e4c5bb2c3b44f69a47174 metadata recovered; no formal CLAIM/run authority. Prior owner read r6-20261125-0850-owner-read SUCCEEDED, LEASED empty as of 2026-11-25T00:52:04.261808Z; current r6-20261125-0950-owner-read last observed RUNNING / NATIVE_RUNNER. No shared task mutation.

Frozen scientific input: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve full X6 joint Cell equality, ports, grade, phase, sign, multiplicity. The continuous character and Fourier coordinates below are analytical representations of the already paired exact CT observer only, not native spatial coordinates, a propagation rule, a classical numerical reference or a new physical attribution.

Parents read at immutable commits:
- cc1fa4471149037fc07977d0cc27e532e75a5f61:research_notes/portable_direct/2026-11-25_r6_prefix1073_zero_edge_sharp_positive_tail.md (exact exchange cancellation, continuous weighted densities and F(4)>0).
- d1a1617597c9d7872998a58ab8f590a58d71c0ac:research_notes/portable_direct/2026-11-25_r6_prefix1074_lower_band_linear_recovery.md (weak scaling, first lower-band recovery, regular phase-gap and local crossing).
- inherited through these: b0ee3a74d740af91ee1b8e59ecd38cb0542633f7 (negative left neighborhood of 1/9), 7fa8d53867199b47f7a27cc039cfd7ced67c69b9 (regular-band analyticity and exact CT observer). These parent mathematical claims retain their author-conditional, unreviewed status.

## 1. New claims

Let m=n-8, E=x d/dx and D(n,k)=L(x^m(1-x)^k), using the exact inherited observer
    L(f)=c sum_{a=0}^3 integral w_a(x)(E+8)^a f(x) dx,
    c=1/(4*36^8).
Write F(z)=sum F_a z^a=(12/5)L_pol(z)[C_pol(z)+L_pol(z)], as in PREFIX-1073. For each fixed 0<alpha<1 and 0<=j<=3, we prove
    E^j [w_a(x)-36^3 h(0) F_a x^3] = O_alpha(x^(3+alpha/2))   (x -> 0+).
Consequently the effective ordinary density on (0,1/9) obeys
    g(x)=A0 x^3+O_alpha(x^(3+alpha/2)),
    A0=h(0)F(4)/(4*36^5)>0, F(4)=4283136/5.
Thus g is strictly positive on an entire interval (0,delta), strengthening PREFIX-1074's positive points on every sufficiently small rescaled window.

There exists a finite constant C>0 such that for ALL integers m>=0 and k>=C(m+1),
    D(m+8,k)>0.
C is existential, not a certified numerical constant. Thus all high-order negative observations are confined to a uniform linear envelope, not just fixed-n eventual positivity. The lower regular band has finitely many density zeros. Let
    b_last=inf{x in (0,1/9):g(x)<0}, rho_last=1/b_last-1.
Then 0<b_last<=b_low<1/9, and for all sufficiently large m the globally last negative integer observation exists and satisfies
    K_last(m)=max{k>=0:D(m+8,k)<0}=rho_last*m+O(1).
More precisely, if g(b_last+y)=a y^r+d y^(r+1)+O(y^(r+2)), then r is odd, a<0, and
    k_real=rho_last*m+c_last+o(1),
    c_last=(r+2)(1-2b_last)/(3 b_last)+(1-b_last)d/a,
    K_last=ceil(k_real)-1.
Here b_low is the earlier sup of positive points from PREFIX-1074; b_last need not equal it unless intervening sign changes are excluded. This result bounds the last negative observation globally, not just the recovery from a selected witness.

## 2. A scale-derivative lemma for the exact six-character pushforward

Let S=sum_{i=1}^6 z_i for six independent normalized Haar unit characters, w in the auxiliary complex character-sum coordinate, and p_W(w) the density of the pushforward weighted by any fixed finite Laurent polynomial W. Existence and continuity were established in PREFIX-1073 by the three-pair convolution. Let R=w dot grad_w, acting only in this auxiliary coordinate. For every fixed nonnegative integer j and 0<alpha<1,
    p_W(w)-p_W(0)=O(|w|^alpha),
    R^j p_W(w)=O(|w|^alpha) for j>=1,
as w approaches zero. The derivatives here are classical off zero in a sufficiently small punctured disk. In particular the estimates hold uniformly in angular direction.

Proof: by finite linearity consider a monomial prod z_i^{l_i}. Its Fourier transform factors into six one-character integrals. With Fourier variable xi=t omega (t>=1, unit omega), rotating the integration character gives a harmless smooth unit character factor omega^{l_i}. For each fixed integer l_i the remaining integral has phase -Re(z) times t and a smooth character amplitude. It has exactly two nondegenerate stationary points at z=+1,-1. Partition the circle near these and the nonstationary complement. The one-dimensional stationary-phase expansion yields
    I_l(t,omega)=sum_{sigma=+1,-1} exp(i sigma t) a_{l,sigma}(t,omega),
    |partial_t^q partial_omega^v a_{l,sigma}| <= C_{q,v} t^(-1/2-q).
Here partial_omega is any smooth angular derivative. For clarity the symbol estimates follow by using the local Morse coordinate with phase sigma plus or minus a quadratic; differentiating q times after removing exp(i sigma t) inserts the quadratic to power q, so the stationary expansion starts at order t^(-q-1/2). On the nonstationary complement repeated integration by parts gives arbitrarily fast decay with derivatives; this piece can be assigned to either symbol after removing its oscillation. This is an analytic estimate of the exact character integral; no numerical evaluation of a classical function is involved.

Multiply the six expansions and group by sum sigma. After smooth radial cutoff t>=1, the transform is a finite sum
    sum_{ell in {-6,-4,-2,0,2,4,6}} exp(i ell t) A_ell(t,omega)
plus a smooth compact-frequency remainder, with |partial_t^q partial_omega^v A_ell| <= C_{q,v} t^(-3-q). Cutoffs are absorbed into A. For ell nonzero, inversion is smooth in |w|<1: on the inversion phase t(ell+omega dot w) the radial derivative has absolute value at least 1. After any finite w differentiation, repeated integration by parts in t gives an absolutely integrable symbol bound (the radial measure contributes t). This can be justified with a smooth large-frequency cutoff and then by convergence of the differentiated oscillatory integral; no boundary at infinity is retained. The low-frequency term is smooth as well.

For ell=0, the inverse of A_0 is a continuous function, since A_0=O(t^-3) is integrable in two auxiliary Fourier variables. It is smooth away from w=0 by integration by parts in the Fourier variable using the symbol bounds (Cartesian derivatives of order q decay as t^(-3-q)). In Fourier variables, R corresponds to -(2+xi dot grad_xi), so the inverse representing R^j of this term uses B_j=[-(2+xi dot grad_xi)]^j A_0, still an order -3 symbol. The formula holds distributionally by Fourier duality and pointwise off zero by smoothness. Each inverse is Holder-alpha, since |exp(i xi dot w)-1|<=C_alpha |xi|^alpha |w|^alpha and integral |xi|^alpha |B_j| dxi is finite for alpha<1. For j>=1 its value at zero is zero: integral B_j=0 by the divergence theorem on a ball of radius T with boundary flux O(T^-1), with the low-radius cutoff smooth. The smooth pieces have R^j value zero at zero for j>=1 and variation O(|w|). Combining terms proves the claim. The analytic proof is confined to the exact paired observer, retaining the original BRC branch carrier before the CT identity.

## 3. Propagation through the exact exchange cancellation

Use PREFIX-1073's exact Laurent identities (z=z_0, B=S*, b=z_0^-1, c_j=z_j^-1):
    H_j=S^2 Q_j,
    Q_j=z P+S A_j+S^2 V_j,
    A_j=B z J+z(b+c_j)L_pol+C_pol.
The first-order cross term in K(n)=H_0 H_0*-H_1 H_1* is exactly antisymmetric under exchange of axes 0,1 and vanishes on every radial test. The surviving expansion is a finite sum of S^u (S*)^v times Laurent weights, with u+v>=6 after that exact cancellation. (Use the same expansion as parent section 1; B terms in A can be absorbed as additional powers.) The degree-six terms are |S|^6(|A_0^(0)|^2-|A_1^(0)|^2) and the two |S|^4 S^2 P z*(V_0-V_1) conjugate terms. The latter weights have nonzero common rotation degree and hence p_W(0)=0 by continuity and rotation covariance. The remaining degree-six constant is precisely F(n) p_1(0) by the exchange identity p_(z_0 z_1^-1)(0)=-p_1(0)/5. Higher degree terms are bounded with all fixed scale derivatives.

To make the passage to x precise, if a term is S^u (S*)^v W, its radial pushforward density is a fixed positive Jacobian times
    r^(u+v) integral_{unit omega} omega^(u-v) p_W(r omega) d omega,  r=6 sqrt(x).
The x Euler derivative equals one half the radial Euler derivative in r. By section 2 and Leibniz, for every fixed j<=3, replacing p_W(r omega) by p_W(0) in this expression costs O(r^(u+v+alpha)) after j Euler derivatives. For higher degree u+v>=7 the whole term is O(r^7), including these derivatives. Radial exchange cancellation is exact as a distribution on this observer family and so also on the regular band. Thus the stated coefficientwise derivative estimate follows, using polynomial interpolation in n of the degree-at-most-three K(n), or applying the same argument to its coefficients. No differentiation of an uncontrolled little-o is used.

On the lower band the adjoint of E for dx is -(1+E), hence
    g=c sum (7-E)^a w_a
      =c*36^3*h(0) sum 4^a F_a x^3+O(x^(3+alpha/2)).
The inherited positive exact coefficient F(4) proves an open positive zero-edge neighborhood. In fact the same proof gives the scale estimates at every fixed finite derivative order, although order three suffices.

## 4. Uniform positivity for the complete BRC observation

Choose 0<delta<1/9 so that g(x)>=c1*x^3 on (0,delta), c1>0. Let chi be a smooth nonnegative cutoff equal to 1 on [0,delta/2] and zero on [delta,1]. The exact observer decomposes as
    L(f)= integral chi(x)g(x)f(x) dx + L((1-chi)f).
The first identity is integration by parts also at zero: w_a and its first three Euler derivatives are O(x^3), so the boundary expressions at x=0 vanish for polynomial f with m>=0; the cutoff kills the other boundary. The local integral for f=x^m(1-x)^k is bounded below by a positive constant times
    (delta/8)^m (1-delta/4)^k
by restricting to [delta/8,delta/4]. The constant includes the lower g bound and interval length and is independent of m,k.

The complementary term is bounded by the inherited finite C^3 norm of L. For integers m>=0,k>=3, differentiation up to order 3 on x>=delta/2 bounds it in absolute value by
    C2 (1+m+k)^3 (1-delta/2)^(k-3).
Terms in derivatives of x^m with order exceeding m vanish, so this bound includes m=0,1,2. All cutoff derivatives have fixed constants. Put q=(1-delta/2)/(1-delta/4)<1 and B=8/delta>1. The ratio of complement bound to local lower bound is at most
    C3 (1+m+k)^3 B^m q^k.
Choose C sufficiently large that k>=C(m+1) forces B^m<=q^(-k/2), m<=k, k>=3, and C3(1+2k)^3 q^(k/2)<1 for every k>=C. This is possible because q<1. This proves uniform strict positivity. It is valid for every integer n>=8, including small n, with the same existential constant C. No asymptotic interchange in n and k is used.

## 5. The last negative observation is linearly localized

By section 3 and the inherited strict negative left neighborhood of 1/9, the lower regular band has opposite definite signs at its two ends. Its density is real analytic in the open band; its zeros are isolated and all lie in a compact subinterval. Therefore there are finitely many zeros there. Define b_last as in section 1. It lies strictly in the band; g>=0 below b_last and is negative immediately above it. The order r is odd and a<0.

Fix a negative witness just above b_last. For its ratio rho=1/x-1, the exact observer is eventually negative by the regular-band phase localization from PREFIX-1074, so the last negative integer exists for large m by section 4. The localized Gaussian expansion and monotonicity argument of PREFIX-1074 section 4 applies to this same orientation (positive below, negative above) at b_last; it yields a unique local continuous crossing with the stated shift and strict sign on either side. To exclude later negatives: for ratios in a compact interval above rho_last plus any fixed small margin, the saddle lies in a compact subinterval of (0,b_last) where g>=0. Even-order isolated zeros are harmless: the local positive integral has a polynomial lower bound after dividing by the peak beta weight, and the C^3 phase-gap bound on the complement is exponentially smaller, exactly as in PREFIX-1074 section 3 with signs reversed. This is uniform on the compact interval by the finite-order local estimates and compactness. For ratios near rho_last but outside the bounded shift window, the monotone localized integral and exponentially small complement in PREFIX-1074 section 4 exclude extra crossings; the derivative convergence proves uniqueness in the bounded shift window. For all remaining larger ratios choose a fixed ratio bound greater than 2C, where C is from section 4, which covers k>=C(m+1) for m>=1. Thus no later negative integer exists and the last one is ceil(k_real)-1, including an integral zero. The proof does not assume that b_last=b_low; additional sign changes between them remain possible.

## 6. Scope and next

Analytic proof conditional on the inherited BRC paired-observer and polynomial identities plus regular-band/saddle results. No new native kernel or classical reference run, no numerical evaluation of trigonometric functions or pi, no finite-path re-enumeration, and no independent review. The new ingredient is scale-derivative regularity of the exact finite Laurent-weighted six-character CT readout, which removes the endpoint differentiation gap of PREFIX-1074. The uniform tail closes the possibility of a superlinear last negative window. Next: obtain certified numerical bounds for the two extremal lower-band boundaries b_last and b_low, determine whether they coincide, and classify middle/upper band zeros. The explicit constant C is not yet quantified. Mother B_fix,odd(32) remains open.
