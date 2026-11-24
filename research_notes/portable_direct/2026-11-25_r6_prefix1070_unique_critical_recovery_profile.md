# PREFIX-1070 — Unique critical recovery profile and a bounded-error recovery location

Date: 2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Independent informed continuation, EM-DIRECT-780BBE / TASK_RESEARCH, own historical SID metadata recovered; no formal CLAIM or execution authority, no shared task mutation. Frozen candidate unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; X6 Stage46 anchor O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, blocked Link {O,e1} both orientations without renormalization, precisely two negative steps. All original six-coordinate joint Cell pairing, terminal ports, grade and phase remain in the inherited BRC observer.

Parent (full text read): 61272666754b17e7d622723cbe5c622702d2df5c:research_notes/portable_direct/2026-11-25_r6_prefix1069_boundary_layer_and_finite_shift.md. Also read 7fa8d53867199b47f7a27cc039cfd7ced67c69b9:research_notes/portable_direct/2026-11-25_r6_prefix1068_first_spectral_sign_boundary.md, including its local Morse pushforward proof. This is an analytic consequence of the exact paired BRC scalar observer, not a new native evolution, numerical reference computation, or physical attribution.

## 1. Results

Set m=n-8, x0=4/9, rho0=5/4, V=80/729, c=1-x0=5/9. The parent proves the critical layer at k=rho0*m+lambda*sqrt(m), with normalized D/f(x0)/m^(1/4) converging to
    H(lambda)=C0 integral_0^infty y^(3/2) G_lambda'''(y) dy,
    G_lambda(y)=exp(-y^2/(2V)-lambda*y/c),
where C0<0 is fixed by the exact BRC saddle contraction sum K3=-6291456000. The new result is that H is strictly increasing on the entire real line and has exactly one simple zero lambda_rec. In particular
    -3*sqrt(5)/4 < lambda_rec < -3*sqrt(5)/8 < 0.
For fixed lambda below this zero the limiting sign is negative, above it positive. The critical recovery is thus displaced to the LEFT of 5m/4 by a strictly positive order-sqrt(m) amount, not merely a positive window around 5m/4.

Moreover the continuous extension of the inherited observer has exactly one zero in any fixed compact lambda interval containing lambda_rec in its interior, for all sufficiently large m. Its location in k is
    k_rec^real(m)=5m/4+lambda_rec*sqrt(m)+O(1).
The first strictly positive integer k in that local window is floor(k_rec^real(m))+1; equality at an integer counts as zero. No claim that this is the first recovery globally, or the final sign change over all k. The earlier first-negative position is rho_b*m+O(1) with rho_b<5/4 as in PREFIX-1069. The two transitions are separated by a linear distance.

## 2. Exact reduction and unique zero

Twice integrate the parent integral by parts. At 0 both y^(3/2) G'' and y^(1/2) G' vanish, and infinity is harmless by Gaussian decay. Thus
    I(lambda)=(3/4) integral_0^infty y^(-1/2) G_lambda'(y) dy.
This is an ordinary convergent integral, avoiding the nonintegrable third derivative of s_+^(3/2) at the saddle itself. Put u=y/sqrt(V), t=-lambda*sqrt(V)/c. Define
    M(t)=integral_0^infty u^(-1/2) exp(-u^2/2+t*u) du,
    Q(t)=t*M(t)-M'(t).
Then I(lambda)=(3/4)*V^(-1/4)*Q(t). All differentiation in t on compact intervals is justified by Gaussian-polynomial domination. Integration of the derivative of u^(1/2) exp(-u^2/2+t*u) gives
    M''(t)=t*M'(t)+(1/2)*M(t).
Consequently the exact identity
    Q'(t)=M(t)/2>0,
    Q(t)=-M'(0)+(1/2)*integral_0^t M(s) ds.
At t=0, Q<0; since M(t)>=M(0)>0 for t>=0, Q tends to positive infinity. There is precisely one t_rec>0 and Q crosses from negative to positive there, with derivative M(t_rec)/2>0. For negative t, Q<0. Since C0<0 and dt/dlambda=-sqrt(V)/c<0, H'(lambda)>0 at every finite real lambda. The root is equivalently the unique solution
    integral_0^(t_rec) M(s) ds=2*M'(0),
    lambda_rec=-(c/sqrt(V))*t_rec=-(3*sqrt(5)/4)*t_rec.
No value of the Gaussian normalization or pi is needed.

## 3. Explicit analytic root bracket

Write mu=M'(0)/M(0). The exact integration-by-parts moment recurrence at t=0 is M^(j+2)(0)=(j+1/2) M^j_derivative(0), where M^j_derivative means the j-th derivative (not a power). In particular M''(0)=M(0)/2, M'''(0)=3 M'(0)/2. Cauchy-Schwarz for the positive measure u^(-1/2)exp(-u^2/2)du gives
    mu^2 < 1/2,
    (M''(0))^2 < M'(0)*M'''(0), so mu^2 > 1/6.
Strictness follows from nonconstant u on the measure support.

For 0<=s<=1/2 use s*u<=u^2/4+s^2, then rescale u in the resulting integral to obtain M(s)/M(0)<=2^(1/4) exp(s^2). The elementary inequalities 2^(1/4)<6/5 and exp(1/4)<4/3 imply
    integral_0^(1/2) M(s) ds / M(0) < 4/5 < 2/sqrt(6) < 2*mu.
The exponential inequality follows from exp(v)<1/(1-v) for 0<v<1 (differentiate -log(1-v)-v); the rational comparisons follow by squaring or taking fourth powers. Hence t_rec>1/2.

For s>=0, exp(s*u)>=1+s*u+(s*u)^2/2 (elementary convex integral inequality), giving
    M(s)/M(0)>=1+mu*s+s^2/4.
It follows that integral_0^1 M(s) ds / M(0)>=13/12+mu/2>2*mu because mu<1/sqrt(2)<13/18. Therefore t_rec<1. All bounds are analytic; no numerical quadrature, trigonometry, pi evaluation, or model reference run was performed.

## 4. Rate and discrete local recovery

We sharpen the parent compact-uniform convergence to a compact-uniform C^1(lambda) error O(m^(-1/2)) for the normalized observer, with real k=5m/4+lambda*sqrt(m). Here the real-k extension is for analysis only; original BRC observations occur at integer k. Use the exact test f=x^m(1-x)^k and normalize by its value at x0, then set y=sqrt(m)(x-x0). In a fixed small saddle neighborhood, Taylor's theorem applied to the exact logarithmic phase yields
    log(f(x0+y/sqrt(m))/f(x0))=-y^2/(2V)-lambda*y/c
         + O(m^(-1/2)(|y|^2+|y|^3)).
On compact lambda intervals the error and its y derivatives through order 3 are bounded by m^(-1/2) times fixed polynomials in |y| on |y|<=m^eta, for a sufficiently small fixed eta>0. After one lambda derivative the same is true, since that derivative multiplies the test by sqrt(m) log((1-x)/(1-x0)), whose scaled expansion is -y/c+O(m^(-1/2)y^2). Differentiated exponentials then have errors bounded by m^(-1/2) times a fixed polynomial against a slightly widened Gaussian; this follows from the mean-value inequality for exp and the strict negative quadratic phase bound. The remaining local tails for |y|>m^eta are smaller than every power by that quadratic bound, also for the differentiated tests. Outside the fixed saddle neighborhood, the inherited C^3 norm and strict phase gap make contributions exponentially small, with at most polynomial m factors and endpoint logarithms absorbed by lowering exponents by fixed amounts.

As in the parent, use the exact local w_a pushforward decomposition into smooth terms, C_* sum K_a times s_+^(3/2), and s_+^(5/2) times analytic remainders. The smooth part after integration by parts is O(f(x0)*m^(-1/2)), also after one lambda derivative; relative to f(x0)*m^(1/4) this is O(m^(-3/4)). The a=3 top derivative of the s_+^(3/2) term has normalized size order one. Its x^3 coefficient differs from x0^3 by O(|y|/sqrt(m)), and its scaled test derivatives differ from their G limits by O(m^(-1/2)) in the relevant Gaussian-weighted integrals. Lower Euler derivative orders, and a<=2 singular terms, are relatively O(m^(-1/2)) or smaller by the same scaling m^(a/2-5/4) in the parent. The s_+^(5/2) remainder is relatively O(m^(-1/2)). The same estimates hold after one lambda differentiation. Thus
    H_m(lambda)=D(m+8,5m/4+lambda*sqrt(m))/(f(x0)*m^(1/4)),
    ||H_m-H||_{C^1(J)}=O_J(m^(-1/2))
for every compact interval J of real lambda, conditional on the parent saddle decomposition.

For a fixed interval J with lambda_rec in its interior, H has strictly positive minimum derivative on J and opposite signs at the endpoints. By C^1 convergence H_m is strictly increasing on J eventually, with opposite endpoint signs. It has a unique zero lambda_m. The mean-value theorem and uniform error give lambda_m=lambda_rec+O(m^(-1/2)). Multiplying by sqrt(m) proves the O(1) location error in k; rounding gives the local integer strict positive threshold. Sign changes outside J, or in windows growing unboundedly in lambda, are not covered by this local uniqueness result.

## 5. Evidence and continuation

This is a human-recheckable analytic extension of PREFIX-1069, retaining the exact scalar paired observer and frozen native packet. It makes no new native arithmetic or classical model comparison and no empirical fit. The old finite ratios near 1.49 are not explained quantitatively. No formal/native kernel revalidation or independent review was performed. Mother question B_fix,odd(32) remains open; P000 unchanged. Next: use this unique critical-layer root to separate the regular negative window from the recovery layer, and construct sign-sensitive certificates for the regular first boundary b; quantify crossover onset, rather than fitting the finite first-negative ratio to the asymptotic value.
