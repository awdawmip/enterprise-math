# PREFIX-1069 — Boundary layer and finite-size displacement of the first negative BRC difference

Date: 2026-11-25. Informed independent continuation of PREFIX-1068; author analytic proof, not independently reviewed. Own registration metadata recovered for EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322; no formal run or CLAIM. No shared task mutation. Frozen candidate unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; X6 Stage46 anchor O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, blocked Link {O,e1} in both orientations without renormalization, exactly two negative steps. Full six-coordinate joint Cell pairing, ports, grade and phase retained by the inherited packet.

Parent: 7fa8d53867199b47f7a27cc039cfd7ced67c69b9:research_notes/portable_direct/2026-11-25_r6_prefix1068_first_spectral_sign_boundary.md (read full proof, including the one-positive four-negative saddle and K3 sum). Also inherited through that parent: PREFIX-1062, 1065, 1067. This is an analytic consequence of the exact BRC scalar observer, not a new physical coordinate system, classical propagation, or reference calculation. No new native path enumeration or numerical trig/pi evaluation.

## Results

Set m=n-8, x=SS*/36, E=x d/dx, f=x^m(1-x)^k. The parent gives D(n,k)=L(f), L=(4*36^8)^(-1) sum CT[K_a(E+8)^a f] for a=0..3; L is bounded on C^3([0,1]). On the regular band (4/9,1), L has analytic density g. Parent establishes g<0 just right of 4/9, g>0 near 1, b=sup{x in (4/9,1):g(x)<0} in (4/9,1), and k_min(n)/n -> rho_b=1/b-1.

1. Sharpen this limit to k_min(n)=rho_b(n-8)+O(1), without assuming a simple zero. More precisely there is a real c_m=c_*+O(1/m) such that, for sufficiently large integer m,

    k_min(m+8)=floor(rho_b*m+c_m)+1,

where r is the odd order of the zero of g at b, a=g^(r)(b)/r!>0, d=g^(r+1)(b)/(r+1)!, and

    c_* = (r+2)(1-2b)/(3b) + (1-b)*d/a.

2. At the internal critical ratio rho_0=5/4, D(m+8,k)>0 eventually for any integer k=5m/4+O(1), even though the first negative occurs at a strictly smaller limiting ratio. This is a second, distinct sign recovery region; it does not require a numerical value of b. More generally k=5m/4+lambda*sqrt(m)+O(1) has an explicit boundary-layer leading term. This gives a finite-width transition mechanism at the saddle. It does not yet predict the observed n<=88 ratios quantitatively.

## A. First-negative boundary, including multiple odd zero

Analyticity and nonidentity of g on the connected regular band imply that b is an isolated zero of finite order. There are negative points arbitrarily near b from below and none above b. The local Taylor expansion is g(b+y)=a*y^r+d*y^(r+1)+O(y^(r+2)), with r odd and a>0. Choose epsilon>0 so the sign agrees with y on this neighborhood and the closed interval lies strictly inside the regular band. Use a nonnegative smooth cutoff chi supported there, identically one near b. For k real and m,k>4, the observer extends by the same C^3 formula to f; integer values are unchanged. Let rho=rho_b, k=rho*m+c, V=b^2(1-b), phi(x)=log x+rho log(1-x). Then phi'(b)=0, phi''(b)=-1/V, phi'''(b)=2(1-2b)/(b^3(1-b)^2).

Normalize by the positive f(b). With x=b+y/sqrt(m), bounded c, local phase exponent is
    -y^2/(2V) + m^(-1/2)*phi'''(b)*y^3/6 + O(m^(-1)*y^4);
amplitude (1-x)^c/(1-b)^c has first correction -c*y/((1-b)*sqrt(m)). Taylor-expand g and multiply. The leading term integrates to zero by odd parity; the next is
    D(m+8,rho*m+c)/f(b)
    = m^(-(r+2)/2) * a*I_(r+1)/(1-b) * (c_*-c)
      + O(m^(-(r+4)/2)),
where I_j=integral over R of y^j exp(-y^2/(2V)) dy for even j. Integration by parts gives I_(r+3)=(r+2)V I_(r+1); hence the stated c_* exactly. No value of the Gaussian normalization is needed.

Remainder justification: take a fixed symmetric smaller neighborhood on which chi=1 and the phase has a negative quadratic upper bound. Expand through order m^-1 in the scaled integrand after factoring m^(-(r+1)/2); the order zero and order m^-1 terms are odd polynomials times the even Gaussian. Taylor with remainder, for |y|<=m^eta with any sufficiently small fixed eta>0, bounds the order m^-3/2 remainder by m^-3/2 times a fixed polynomial in |y| times exp(-y^2/(4V)), uniformly on compact c intervals. The remaining local Gaussian tail is smaller than every power of m; the transition cutoff and global complement are exponentially small by the parent strict phase-gap C^3 bound. Thus the displayed error is uniform for bounded c. Differentiating in c is legitimate and gives the same uniform expansion for the derivative: the extra factor log((1-x)/(1-b)) is smooth in the local interval and its endpoint growth in the complement is absorbed by decreasing k by a fixed amount, leaving the exponential gap. In particular the normalized derivative is strictly negative on any fixed bounded c interval for sufficiently large m.

To ensure this is the FIRST crossing, not merely one crossing: select fixed c_-<c_*<c_+ (e.g. c_* +/-1). At those c the normalized observer has opposite strict signs of polynomial magnitude. For the entire near-boundary range |k/m-rho|<=delta, choose delta small so that on the complement of the region where chi=1, the phase relative to b still has a uniform strictly negative gap. The C^3 norm of f(1-chi)/f(b) is exponentially small uniformly in that range (endpoint derivatives are controlled by powers with exponents reduced by at most three). The localized normalized integral
    J_m(k)=integral chi(x)g(x)(x/b)^m ((1-x)/(1-b))^k dx
is strictly decreasing in k: its derivative integrand has sign <=0 pointwise because g and log((1-x)/(1-b)) have opposite signs on the support. Therefore J_m(k)>=J_m(rho*m+c_-) for all smaller k in this range. That lower bound is positive of polynomial magnitude; the exponentially small complement cannot change it. For k/m<rho-delta use the already proved liminf of k_min(n)/n=rho, with a slightly smaller delta to account for the fixed offset 8. Thus no earlier negative integer can occur. The continuous normalized observer has one strictly decreasing zero c_m in [c_-,c_+] by the derivative expansion, and c_m=c_*+O(1/m) by the expansion and positivity of its prefactor. There are negative integers in the bounded window if it is widened, say to c_* +/- 2; rounding yields floor(rho*m+c_m)+1, including exact integer zero (zero is not negative). The proof does not claim a uniform computable onset without explicit bounds on the analytic density. This also yields a bounded finite-size discrepancy from the limiting slope, beyond the parent's o(n) statement. For a simple zero r=1, c_*=(1-2b)/b+(1-b)g''(b)/(2g'(b)).

## B. Critical saddle boundary layer and reentrant positivity

Let x0=4/9, rho0=(1-x0)/x0=5/4, V0=x0^2(1-x0)=80/729. Parent gives for each pushforward w_a near x0 a smooth part plus C_* (sum of K_a at six saddles) s_+^(3/2) + O(s_+^(5/2)), s=x-x0. Here C_*>0 is the common geometric coefficient, and sum K3=-6291456000. The same local proof in the parent gives this two-sided expansion: for s<0 the u integral has no missing interval, so only its smooth analytic continuation remains. The remainder on the positive side is s^(5/2) times a bounded analytic function, and a smooth cutoff can localize it. No ordinary globally integrable effective density is asserted at the saddle.

For k=rho0*m+lambda*sqrt(m)+O(1), real fixed lambda (also valid uniformly on compact lambda intervals), f(x0+y/sqrt(m))/f(x0) tends to
    G_lambda(y)=exp(-y^2/(2V0)-lambda*y/(1-x0)).
Its first three scaled y derivatives converge locally uniformly, with integrable Gaussian-polynomial bounds in the local saddle interval. This follows by differentiating the exact log phase, using strict negative quadratic curvature and bounding the bounded lambda tilt by a linear function of |y|. Contributions outside the fixed saddle interval are exponentially small relative to f(x0) by the C^3 bound. Smooth parts of w_a can be integrated by parts on a compact cutoff, reducing all their contributions to O(f(x0)/sqrt(m)). The singular s_+^(3/2) term of w_a multiplied by the top a-th derivative of f scales as m^(a/2-5/4); lower derivatives and s_+^(5/2) remainders are smaller by at least m^-1/2. Thus only a=3 contributes at scale m^(1/4). In (E+8)^3 the top ordinary derivative has coefficient x^3; its variation contributes lower order. Dominated convergence yields
    D(m+8,k)/(f(x0)*m^(1/4))
      -> C_* x0^3*(-6291456000)/(4*36^8)
         * integral_0^infty y^(3/2) G_lambda'''(y) dy.
All derivatives here act on the smooth test, NOT the nonintegrable s^(-3/2) density, so the expression is well-defined. This is a new scaling law for the inherited BRC paired observer, not a change of native model.

At lambda=0, G'''=(3y/V0^2-y^3/V0^3)G. Integration by parts gives integral y^(9/2)G=(7/2)V0 integral y^(5/2)G over the positive half-axis. Consequently
    integral_0^infty y^(3/2)G_0'''(y)dy
       = -1/(2V0^2) integral_0^infty y^(5/2)G_0(y)dy <0.
The saddle coefficient is negative, so the limiting normalized D is strictly positive. This proves eventual positivity at k=round(5m/4), and by continuity of the profile for a fixed nonzero-width interval |lambda|<eta (eta>0 not quantified). Since rho_b<5/4, a negative integer strictly earlier is guaranteed for all sufficiently large m by part A or the parent slope theorem. In particular the sign sequence in k is not a single irreversible positive-to-negative transition. The singular saddle produces positive recovery in a window of order sqrt(m), at a distance linear in m from the first crossing. This is an exact asymptotic distinction between the regular zero and the internal singularity. No claim about the sign for all k after that window.

## C. Evidence and next problem

Analytic proof using the frozen exact BRC joint observer and parent integer saddle contraction; no new numerical runs or formal/native kernel check. Rounding rule and two scaling exponents follow from the displayed integrals; no new external comparison, no evaluation of pi or trigonometric functions. Status AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED; conditional on inherited candidate packet and parent observer/density proofs. Mother problem B_fix,odd(32) remains open. P000 unchanged.

Next: bracket b and its zero order by sign-sensitive exact localized observer certificates, quantify the onset of part A, and analyze the boundary-layer profile zeros in part B. The finite data near 1.49 may lie before the first-crossing asymptotic regime; this paper supplies two mechanisms and exact asymptotic laws, not a fitted explanation of those finite values.
