# PREFIX-1071 — Second critical BRC layer: reentrant negativity and reflected recovery profile

Date 2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Independent informed continuation of EM-DIRECT-780BBE / TASK_RESEARCH; own session metadata recovered (MCP-f6d93209fc8e4c5bb2c3b44f69a47174); no formal CLAIM or run authority. Current LEASED inventory request r6-20261125-0550-owner-read last observed RUNNING, no shared task mutation.

Frozen input unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 candidate chart anchor O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, precisely two negative steps. Preserve full six-coordinate Cell pairing, terminal ports, grade, phase and branch multiplicity. No new native arithmetic or classical comparison. The continuous character quotient below is solely the already established exact paired scalar observer, not a native spatial slice or a time evolution.

Parents (full scientific text read):
- 7fa8d53867199b47f7a27cc039cfd7ced67c69b9:research_notes/portable_direct/2026-11-25_r6_prefix1068_first_spectral_sign_boundary.md, sections 1–3,5: exact cubic observer, all critical values, two-negative-character contraction, first saddle decomposition.
- d5c0155e1f73ad47cace43d903b9dd8b76f455ef:research_notes/portable_direct/2026-11-25_r6_prefix1070_unique_critical_recovery_profile.md: Q monotonicity, root bracket, C^1 layer error technique.

## Main results

Let m=n-8, x1=1/9 and rho1=8. There is a positive constant B such that the effective density on the regular band immediately LEFT of x1 satisfies
    g_eff(x1-s) = -B s^(-3/2)+O(s^(-1/2)), s -> 0+.
In the second critical window k=8m+lambda sqrt(m) the normalized continuous observer has a strictly DECREASING limit profile with exactly one simple zero lambda_2, where
    lambda_2=6 sqrt(2) t_*,
    3 sqrt(2)<lambda_2<6 sqrt(2).
Here t_* is exactly the same unique scalar root from PREFIX-1070, not an independently fitted constant. Thus the first strictly negative integer after the local zero in any fixed scaled window containing lambda_2 is floor(k_2^real(m))+1, with
    k_2^real(m)=8m+lambda_2 sqrt(m)+O(1).
The integer threshold is local, not necessarily the next global negative after the first recovery. At k=8m+O(1), D>0 eventually. At fixed ratios slightly greater than 8, D<0 eventually. Combining the earlier first-negative and first-saddle recovery proves at least three changes of sign along k for all sufficiently large n (counting changes across zero entries), hence at least two separated negative windows.

## 1. Second-saddle signature from the same BRC character

Use PREFIX-1068's x=SS*/36, S=sum z_i, L(f)=(4*36^8)^(-1) sum_(a=0)^3 CT[K_a (E+8)^a f], E=x d/dx, D(n,k)=L(x^m(1-x)^k). K4=0. There are 15 critical characters with two negative coordinates, modulo common rotation, at x1=1/9. Write sigma_i=+1 on four labels and -1 on two, S0=2. In a local additive chart modulo the diagonal, the quadratic term of 36(x-x1) is
    (sum sigma_i theta_i)^2 - 2 sum sigma_i theta_i^2.
Choose the sum-zero gauge (only on the character quotient). The within-positive-group sum-zero subspace has dimension 3 and eigenvalue -2. The within-negative-group sum-zero subspace has dimension 1 and eigenvalue +2. The remaining group-constant direction has values a on the four positives, b=-2a on the two negatives; its norm squared is 12a^2 and quadratic term 72a^2, eigenvalue +6. These subspaces are orthogonal and have no quadratic cross terms, by the displayed quadratic form. The signature is (2 positive,3 negative). In general the nonzero critical character with p positives and q negatives, p+q=6, p>q>0, has eigenvalues -(p-q) with multiplicity p-1, +(p-q) with multiplicity q-1, and +6 on the relative group mean: setting b=-pa/q gives the same quotient by the diagonal. This classifies both internal critical values without changing the six-dimensional native model.

The real analytic Morse lemma gives local auxiliary coordinates u in R^2 and v in R^3 with x-x1=|u|^2-|v|^2. The Jacobian at zero is positive and equal across the 15 characters by permutation symmetry of the scalar x and Haar measure. The signed K_a weights retain their labels. The inherited exact sum of the K3 values at these 15 characters is -1610612736 (PREFIX-1068 section 2 and reproduction, not newly executed here).

## 2. Left-sided density singularity, including its sign

Let s=x-x1 and w_a be the pushforward density of K_a under x on a regular band. In the above Morse chart, localize by smooth radial cutoffs in v and u, with the v support sufficiently smaller than the region where the u cutoff equals one. For small |s| and r=|v| in the support, integrate out the u radial variable with |u|^2=s+r^2. Since u has dimension 2, its radial Jacobian is constant after this substitution; v has dimension 3 and supplies r^2 dr. Averaging the analytic amplitude over the two spheres produces an analytic function B_a(r^2,s+r^2), whose value at (0,0) is a common positive Jacobian times the labeled K_a at that critical character. The local density is therefore a positive constant times
    integral_(r>=0,r^2+s>=0) eta(r) r^2 B_a(r^2,s+r^2) dr.
For s<0 subtract the missing interval [0,sqrt(-s)] from the full fixed-domain integral using the analytic extension of B_a. Its leading term is (1/3)(-s)^(3/2) times the amplitude at zero. Rescaling r by sqrt(-s) proves that the remaining removed contribution is (-s)^(5/2) times an analytic function. For s>=0 there is no missing interval. Away from the 15 points the localized pushforward is smooth by the submersion argument. Summing yields, near s=0,
    w_a(x1+s)=A_a(s)-C_1 sum_crit K_a (-s)_+^(3/2)+(-s)_+^(5/2) R_a(s),
where A_a is smooth, R_a analytic and C_1>0 common to the weights. This is the opposite side and opposite signed missing-volume term compared with the first saddle (signature 1,4). In particular the coefficient of (-s)_+^(3/2) in w3 is
    W_3=C_1*1610612736>0.
On the open regular band s<0 the density of L is (4*36^8)^(-1) sum (7-x d/dx)^a w_a. The third ordinary derivative with respect to x of (x1-x)^(3/2) equals +(3/8)(x1-x)^(-3/2). Thus its leading contribution is
    g_eff(x1-h) = -(4*36^8)^(-1) (3/8) x1^3 W_3 h^(-3/2)+O(h^(-1/2)).
All other terms have lower singular order. This proves strict negativity on some (x1-epsilon,x1). No ordinary integrable density claim is made across the saddle. The entire observer remains a C^3-bounded distribution. In particular the sign argument must retain the singular part rather than integrate this nonintegrable function across x1.

## 3. Second critical layer and exact relation to the first layer

Set c=1-x1=8/9, V=x1^2 c=8/729. For real k=8m+lambda sqrt(m) and f=x^m(1-x)^k, put y=sqrt(m)(x1-x) on the left of x1. The exact normalized phase has leading limit
    G_lambda(y)=exp(-y^2/(2V)+lambda*y/c).
The third x derivative introduces a minus sign relative to the third y derivative; f normalization is f(x1). The leading term of L is therefore
    D(m+8,k)/(f(x1)m^(1/4)) -> H_2(lambda)
    H_2(lambda)=C_2 integral_0^infty y^(3/2) G_lambda'''(y) dy,
    C_2=-(4*36^8)^(-1) x1^3 W_3<0.
The exponent 1/4 follows from three derivatives (m^(3/2)), the density factor m^(-3/4), and the integration length m^(-1/2). The smooth portion after integrating by parts is O(f(x1)m^(-1/2)). The a<=2 and lower Euler derivatives are relatively O(m^(-1/2)); the analytic (-s)_+^(5/2) remainder is also relatively O(m^(-1/2)). For compact lambda intervals the exact logarithmic phase differs from its displayed Gaussian limit on |y|<=m^eta (small fixed eta>0) by O(m^(-1/2)(|y|^2+|y|^3)), with corresponding derivative bounds through order three and one lambda derivative, as in PREFIX-1070 after replacing x0 by x1 and reversing y. Gaussian-polynomial domination on this interval and quadratic phase decay on the remaining saddle neighborhood control all these errors; outside the neighborhood the phase gap and the bounded C^3 observer give exponential suppression. Hence convergence is C^1 on every compact interval with error O_J(m^(-1/2)). This argument uses the exact observer and the analytically derived local decomposition, not a new model reference computation.

Twice integrating by parts gives (3/4) integral y^(-1/2)G_lambda'(y)dy, with vanishing boundary terms. Substitute u=y/sqrt(V) and t=lambda sqrt(V)/c=lambda/(6 sqrt(2)). Then
    H_2(lambda)=C_2*(3/4)*V^(-1/4)*Q(t),
    Q(t)=t M(t)-M'(t), M(t)=integral_0^infty u^(-1/2)exp(-u^2/2+t*u)du.
PREFIX-1070 proves Q'=M/2>0 and its unique root t_* in (1/2,1). Thus H_2 is strictly decreasing on the real line, with one simple zero lambda_2=6 sqrt(2)t_*. It is positive for lambda<lambda_2 and negative for lambda>lambda_2. In contrast the first saddle at 4/9 has H_1 increasing, root lambda_1=-(3 sqrt(5)/4)t_*. The exact ratio of the offsets is
    lambda_2/(-lambda_1)=8 sqrt(2/5).
Both transitions are governed by the same root; the change in direction comes from the signature and the signed BRC coefficient, not a separate fit.

For any fixed compact scaled interval with lambda_2 in its interior, C^1 convergence gives one unique simple zero lambda_m for the continuous extension for sufficiently large m; the uniform derivative lower bound in magnitude gives lambda_m=lambda_2+O(m^(-1/2)). This proves the stated bounded-error location and floor-plus-one strict negative integer threshold. It does not classify windows growing unboundedly in lambda or the entire lower regular spectrum.

## 4. Consequences for sign alternation

By the inherited positive upper edge, D(n,0)>0 eventually. Choose a fixed regular negative point immediately to the right of 4/9 (PREFIX-1068), so that at k=floor(rho_a m), rho_a<5/4 and rho_a>0, the strict phase gap localizes D to a negative contribution. PREFIX-1070 gives D at k near 5m/4 strictly positive eventually. The present result gives D at k near 8m strictly positive eventually. Choose any fixed x in the negative interval immediately left of 1/9; its rho_c=1/x-1>8. The same strict phase-gap argument localizes the scalar observer to this regular negative region, and D at k=floor(rho_c m) is strictly negative eventually. More explicitly, multiply f by a nonnegative cutoff supported on the negative regular neighborhood and equal to one near its maximum. The localized integral has a negative magnitude bounded below on a fixed subinterval with phase larger than the maximum on the complement. The C^3 norm of the complement is exponentially smaller, because derivatives change the polynomial factors and shift k by at most 3 but preserve the strict phase gap. This handles all other critical distributions.

The ordered integer witnesses with signs +,-,+,- prove at least three sign changes ignoring exact zero entries, and two distinct negative runs separated by a positive witness, for every sufficiently large n. The second critical window is an additional mechanism of negativity, not a monotone continuation of the first. The full sign diagram between 5/4 and 8 and beyond 8 remains open. No quantitative onset n is asserted. In particular these results do not locate the first regular boundary b or explain the historical small-n ratios quantitatively.

## Evidence and continuation

Analytic extension only, using the frozen exact signed BRC paired observer and the previously executed integer sum over 15 labeled two-negative characters. No new path enumeration, native kernel execution, classical pi/trigonometry, external comparison or numerical quadrature. All signs, signatures, scaling factors and root relation follow by the displayed human-recheckable argument. Independent review and native physical attribution remain pending. P000 unchanged; mother B_fix,odd(32) open. Next: locate the regular sign boundary b with sign-sensitive certificates, classify the entire middle band (1/9,4/9), and analyze the zero critical level to determine any further high-order windows. Quantitative finite onset still open.
