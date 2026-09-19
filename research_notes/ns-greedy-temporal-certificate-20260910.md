# Residual-guided causal branch selection with temporal response bounds

Record-ID: FINDING-EM-PDE-GREEDY-TEMPORAL-CERTIFICATE-20260910
Status: TESTING / ORDINARY_PROOFS_AND_EXACT_RATIONAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Session: local-ns-jitter-901c9f34161ce0f1 (locally assigned, not a platform ID)
Date: 2026-09-10
Read pins: GLOBAL_KNOWLEDGE 247b7633a368f1821ee311dc91758399ade19d32; EM 4e93f879f252ffcdd76152b45f0cf23139be7a9e.

## 0. Scope, recovery, and attribution

This is direct continuation of the user-selected NS/BRC investigation. P000 is unchanged. Native 120-degree orthogonality and native triadic closure are not replaced by Euclidean definitions. The following rigorous calculations concern the classical normalized torus T3=(R/2pi Z)^3, not a derived complete native X6 dynamical system. Fourier data are real, mean zero, solenoidal. Viscosity is 1 in the executed example. No arbitrary-initial-data regularity or historical novelty claim is made.

The previous adaptive graph-Gram note was pending remotely. It has now been preserved byte-for-byte at EM commit 51841f6c4abb33e31e8152d9fa8b381dec0f1b28, path research_notes/ns-adaptive-graph-gram-20260909.md, SHA256 493640f0a5cb35fa1f783b49a04b37e388c0689abbd777b7dc570575af271dc7, Git blob 3db39c096f3c27bacab6d914c9540849987fe55b. Its historical pending wording describes its original run, not this recovery. Its original adaptive checker was rerun unchanged and reproduced the three residual ratios. Recovery is not counted as new mathematics.

Analytic dependencies: ns-causal-inverse-newton-basin-20260909.md (all-mode causal inverse and contraction); brc-critical-lattice-gram-newton-20260909.md (C*=9503/1000); ns-spectral-reference-20260909.md (Hermitian form bound); the previous adaptive graph-Gram note. These remain TESTING, not independent validation. General orthogonal least squares and a posteriori PDE certification are established: Hashemi-Vikalo, arXiv:1602.06916; Morosi-Pizzocchero, arXiv:1104.3832. Their cited results supply context, not verification of our constants.

## 1. Parent interface and the actual objective

Let B(f,g)=P((f.grad)g), N=-B, Lambda=(-Delta)^(1/2), and D_v=partial_t+Lambda^2+B(v,.)+B(.,v). The zero-initial causal inverse G_v satisfies ||G_v||_(Y->X)<=L, where

Y=L2_t Hdot^-1/2,
||h||_X^2=sup_t[||h(t)||_Hdot^1/2^2+(3/4)int_0^t||h||_Hdot^3/2^2].

The trajectory product constant is C_B=C*/sqrt(3/2). For a heat reference v and g=N(v,v), h0=G_v g is the exact first linear correction. Any finite zero-initial d has full defect e=D_v d-g and

||h0||_X <= U(d)+L||e||_Y                                  (1)

whenever U(d) is a proved bound for ||d||_X. If alpha>=L C_B and eta bounds (1), the parent theorem gives a unique full NS trajectory in a ball of radius r when

eta+alpha r^2<=r, 2alpha r<1.                               (2)

All generated frequencies and both helicities are included. This is a sufficient certificate, not a singularity diagnostic when it fails.

## 2. Certified weak-greedy selection in the causal graph metric

Choose finite causal trajectories psi_j with zero initial trace and put A_j=D_v psi_j. Define G_ij=Re<A_i,A_j>_Y, b_i=Re<A_i,g>_Y, R=||g||_Y^2. The exact error polynomial is

E(c)=R-2b^T c+c^T Gc.                                      (3)

For a selected independent set S, the exact minimizer solves G_SS c=b_S. A new direction j has Schur denominator and corrected correlation

D_j=G_jj-G_jS G_SS^-1 G_Sj,
N_j=b_j-G_jS G_SS^-1 b_S.

If D_j>0, its exact marginal reduction after reoptimizing all coefficients is

Delta_j=N_j^2/D_j.                                        (4)

This is the ordinary orthogonal least-squares law applied to complete causal PDE images. In the implementation all candidate Delta_j are enclosed by outward rational interval LDL solves. A direction is accepted as weak-greedy only if its lower gain is at least half the largest upper gain of any unselected candidate. This handles ties without relying on floating-point ordering. Rounded rational coefficients are then checked in (3), and actual strict residual decrease is independently verified.

Rounding loss is also bounded: writing s=G_SS c-b_S, the exact excess over the optimal residual is s^T G_SS^-1 s. The checker encloses this quantity by interval solves and verifies it is below 10^-6 of the actual residual square at each visited stage.

Important limitation: lowering E does not by itself monotonically lower (1). Every stopping decision therefore checks the complete nonlinear ball (2), not only a prescribed residual percentage. No globally sparsest or fastest dictionary claim is made.

### Fixed-dictionary convergence law, not an infinite-network bound

Let P_S and P_D denote the orthogonal projections onto selected and full dictionary images. Set z=(P_D-P_S)g and normalize the remaining nonzero projected directions u_j=(I-P_S)A_j/||(I-P_S)A_j||. If their frame operator on their span has lower eigenvalue lambda_S>0, then sum_j Delta_j>=lambda_S||z||^2. A theta-weak-greedy step, theta=1/2 here, reduces the gap to the dictionary optimum by at least theta*lambda_S/m of that gap, where m is the number of remaining directions. This follows directly from the frame inequality. It gives no uniform infinite-dimensional bound: lambda_S can deteriorate with growing dictionaries, and the dictionary-optimal residual can be nonzero.

## 3. Legal branch units must preserve the initial trace

A nonresonant heat response to exp(-sigma t) is

phi_(lambda,sigma)(t)=(exp(-sigma t)-exp(-lambda t))/(lambda-sigma).

The two exponentials cancel at t=0. Selecting just one exponential generally changes the initial condition. Thus individual exponential packets are not automatically legal causal trial directions. Our candidates group all rates and time powers at a conjugate Fourier pair (in the executed dictionary, at a whole squared radius), preserving zero initial trace, reality, and solenoidality. The checker tests every candidate and includes an explicit unsafe single-exponential split witness. This is the concrete BRC information boundary used here.

## 4. Sharper temporal bound for the first heat response

The unit A3 datum used below has first nonlinear source g_k(t)=z_k exp(-10t), with squared output radii lambda=6,10,14. Coherent output sums give

sum_(|k|^2=6)|z_k|^2=6,
sum_(|k|^2=10)|z_k|^2=28/5,
sum_(|k|^2=14)|z_k|^2=24/7.                                (5)

Let c=3/4. For one output define

E_lambda(t)=phi(t)^2+c lambda int_0^t phi(s)^2 ds.

Its derivative is exactly

E_lambda'=phi[2exp(-10t)-(2-c)lambda phi].                   (6)

For lambda!=10 the unique maximum is at

t_lambda=log[(10-c lambda/2)/(lambda(1-c/2))]/(10-lambda).

For lambda=10, phi=t exp(-10t) and t_lambda=1/[10(1-c/2)]=4/25. Positivity and uniqueness follow from the monotonic exponential ratio in (6), with 10>(1-c/2)lambda for each of the three lambdas.

The integral of phi^2 is elementary. The verifier checks its derivative symbolically, brackets each nonresonant maximum by rational times with opposite rigorous derivative signs, and uses rational exponential enclosures across the entire bracket. Summing modal suprema is a valid upper bound for the supremum of their sum. It yields

||psi1_unit||_X < 3271/10000=0.3271.                         (7)

The interval readout is at most 0.327002768174. In contrast, the older generic heat-source estimate was sqrt(cR)=0.506788392254. This is a response-specific improvement, not a universal optimal heat inverse norm. There is no sampling-to-all-time inference.

For amplitude a, psi1=a^2 psi1_unit. For a candidate d=c1 psi1+d_rest, pure heat energy gives ||d_rest||_X<=||D0 d_rest||_Y. Therefore use

U(d)=|c1|a^2(3271/10000)+||D0 d_rest||_Y.                    (8)

The second term is evaluated by the complete coherent Gram, not separate absolute packet masses.

## 5. Preserve the available viscous gap in the inverse bound

For the heat reference of this fixed shape,

M(v(t))=a[m_A exp(-2t)+m_B exp(-8t)],
m_A=6sqrt(2)(1/2+sqrt(1+sqrt(2))),
m_B=4sqrt(2)(1/2+sqrt(1+2sqrt(2))).

The inherited Hermitian estimate is ||S_v||<=M(v). The torus spectral gap implies a valid parent growth envelope

b(t)=(M(v(t))-1/4)_+.

This uses an already available parent bound rather than introducing a new stability theorem. There is a unique zero t_* when M(v(0))>1/4. Exact rational bisection and nested-radical/exponential intervals give its enclosing times. Integrate M to the upper time and subtract one fourth of the lower time to obtain a rigorous upper bound on int b.

At a=3/20,

int b < 1.149159341614,
L=exp(int b)/sqrt(3/4) < 73/20=3.65,
L C_B < 57/2=28.5.                                         (9)

Neither the unreserved M bound nor the actual linearized propagator is silently identified with this positive-part upper envelope.

## 6. Executed branch selection and full NS certificate at amplitude 0.15

Use k=(1,1,0),(1,0,1),(0,1,1),(2,-2,0), and conjugate negative frequencies. At each positive k use the unit positive-helicity vector [e+i(k cross e)/|k|]/sqrt(2), where e is the coordinate unit vector at the zero coordinate. All coefficients have amplitude a=3/20, nu=1. The frequency rank is three. This is a two-shell nonlinear datum, not an exact Beltrami heat solution or a helical-decimated equation.

Let psi1=D0^-1 g and psi2=D0^-1[N(v,psi1)+N(psi1,v)]. The dictionary consists of global psi1 and the 11 groups of psi2 with squared radii

{2,6,8,10,14,16,18,24,26,34,42}.

Every image D_v psi is formed without a Fourier output cutoff. Starting with psi1, the verified weak-greedy sequence chooses squared-radius groups

8, 6, 14, 2.

Visited correction packet counts are 20,42,58,90,118. The complete second response would use 216 packets when combined with psi1. The actual selected final linear defect has 566 packets, 136 output frequencies, and maximum squared radius 42. None of those unselected or outside-core contributions is discarded.

Each coefficient proposal uses 80-decimal arithmetic but is rounded to a denominator of 10^12; all acceptance checks use rational intervals. The final all-output residual norm is recomputed directly and agrees symbolically with (3).

Using (1),(7)-(9), the successive eta enclosures are

0.008918,
0.008826,
0.00870893,
0.00858751,
0.00844964.

The first trial fails even the 4alpha eta<1 test with the chosen certified alpha. The third trial already satisfies that sufficient discriminant test, but requires a larger admissible error radius than our prescribed target. To avoid overstating necessity: the fifth trial is the first visited trial to certify the fixed target r=3/200=0.015. We do NOT claim four added groups are necessary for existence or globally optimal.

At the accepted trial take

eta=211241/25000000,
alpha=57/2,
r=3/200.

Exact rational checks give

4alpha eta=12040737/12500000=0.96325896<1,
r-eta-alpha r^2=6893/50000000>0,
2alpha r=171/200=0.855<1.                                   (10)

The inherited all-mode nonlinear contraction theorem now proves a global smooth full NS solution for this specified datum, and

sup_(t>=0)[||u(t)-v(t)||_Hdot^1/2^2+(3/4)int_0^t||u-v||_Hdot^3/2^2]<= (3/200)^2. (11)

This extends the previously certified amplitude 0.12 to this point 0.15 within the same shape family. It is not an arbitrary-data theorem, an optimal threshold, a new priority claim for global smooth examples, or a proof of every amplitude between two certificates without separate reasoning. The remaining full NS problem is unchanged.

## 7. Verification and BRC resolution

REUSE_EXECUTED: canonical exact_packets.py byte-for-byte, SHA256 0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d; original adaptive checker rerun for recovery. REUSE_APPLIED: parent inverse, product, Hermitian form and contraction theorems. T0_BRC and T6 operation-safe quotient: coherent rates, causal initial traces and explicit nonzero errors retained. EXTEND_EXISTING_TOOL: certified weak-greedy decisions plus a response-specific temporal norm certificate. No top-level toolbox or Foundation promotion.

Actual checks: source helicity/rank, exact heat equations, 12-direction full-output Gram, rational interval Schur gain comparisons, positive LDL pivots, coefficient rounding loss, direct final residual Gram, reality and solenoidality, analytic derivative/integral identities, rational peak brackets, inverse growth integration and nonlinear ball inequalities. The executable recomputes its inputs deterministically; it loads no external pickle and uses no PDE time stepping.

The next unresolved unit is a guaranteed dictionary enlargement policy that optimizes the COMPLETE nonlinear certificate, including U(d), rather than residual alone. A growing-dictionary frame constant and a uniform all-data basin are not proved. Near a zero or a nearly dependent direction, precision refinement and explicit trace preservation remain mandatory.
