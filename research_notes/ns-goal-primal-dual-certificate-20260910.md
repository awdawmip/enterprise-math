# Goal-oriented BRC residual certificates with rigorous primal-dual bounds

Record-ID: FINDING-EM-PDE-GOAL-PRIMAL-DUAL-CERTIFICATE-20260910
Status: TESTING / ORDINARY_PROOFS_AND_EXACT_RATIONAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Session: local-ns-jitter-901c9f34161ce0f1 (locally assigned; not a platform-authenticated identity)
Date: 2026-09-10
Read pins: global ea23cf1c552ff824e5933eb36e44ff1606776839; EM 89f8ed2df9e7d5ebe42612e063b50f6be5ee315e.

## 0. Scope and continuation

Continue the explicit NS/BRC project downstream of unchanged P000. Native 120-degree orthogonality is not redefined. The PDE theorem here concerns the classical normalized torus T3=(R/2pi Z)^3, zero-mean real solenoidal smooth initial data, and viscosity 1 in the executed cases. A3/FCC is the inherited Fourier carrier, not a proof of native X6 dynamics.

The parent ns-greedy-temporal-certificate-20260910.md supplies the all-mode causal inverse, the critical trajectory contraction interface, the legal causal dictionary, and a first-response temporal bound. Its proof-source SHA256 is 1bdc69dcdd22760f314c6196053a81ad4edb94edefe0073e37f182da7e701a86. The current turn addresses the parent's explicit remaining unit: optimize the COMPLETE nonlinear-certification upper bound, not just the linear residual.

Established methods used: convex sum-of-norm minimization, second-order cone programming, weak duality, a posteriori approximate-solution validation, and critical-space contraction. No historical priority, new accepted BRC Foundation/tool family, or arbitrary-data regularity claim is made. The new result-specific work is the exact phase/rate-Gram composition, certified full-objective optimization, and numerical examples with both upper and lower certificates.

## 1. Fixed-reference analytic interface

Write Lambda=(-Delta)^(1/2), B(f,g)=P((f.grad)g), D0=partial_t+Lambda^2, and D_v=D0+B(v,.)+B(.,v). Let

Y=L2(0,infinity;Hdot^-1/2),
||h||_X^2=sup_t [||h(t)||_Hdot^1/2^2+(3/4)int_0^t ||h||_Hdot^3/2^2].

The inherited all-mode causal inverse G_v has ||G_v||<=L. Its bilinear composition obeys ||G_v B(f,g)||_X<=alpha||f||_X||g||_X, with alpha>=L C*/sqrt(3/2), C*=9503/1000. These are analytic infinite-frequency inputs, not finite-matrix extrapolations.

Fix the heat reference v for initial datum u0 and g=-f_v=N(v,v). Let h0=G_vg. Every finite causal d with zero initial trace has full linear defect e=D_vd-g and

||h0||_X <= ||d||_X+L||e||_Y.

A bound eta on this quantity proves a full NS solution in the radius-r trajectory ball whenever eta+alpha*r^2<=r and 2alpha*r<1. In particular 4alpha*eta<1 allows a suitable radius. The reference and its growth bound are FIXED in the optimization below; no convexity claim is made for simultaneously varying v or its inverse.

## 2. A convex complete-certificate objective

Use legal zero-initial real solenoidal trajectories psi0,psi1,...,psim. The first is the global first heat response. The others are radius groups of the next response, with all rates/powers at each conjugate frequency retained. Suppose ||psi0||_X<=w and put F_j=D0 psi_j for j>=1. Pure heat energy gives

||sum_(j>=1)c_j psi_j||_X <= ||sum_(j>=1)c_j F_j||_Y.

Thus define

U(c)=w|c0|+sqrt(c_r^T Q c_r), Q_ij=Re<F_i,F_j>_Y,
J(c)=U(c)+L sqrt(R-2b^T c+c^T G c),
G_ij=Re<D_v psi_i,D_v psi_j>_Y,
b_i=Re<D_v psi_i,g>_Y, R=||g||_Y^2.

Then ||h0||_X<=J(c) for every coefficient vector c. J is convex: it is a sum of a weighted absolute value and two Hilbert norms of linear/affine maps. Its epigraph is a second-order cone program after factoring the exact Gram matrices. This is standard convex structure, not a new convexity theorem.

For nested trial spaces with compatible U, appending zero coefficients preserves the old objective, so the optimal complete upper bound cannot increase. This statement concerns optimized objectives; least-squares coefficient choices do not enjoy it for J. Because U is a conservative norm majorant, even an infinitely rich dictionary need not make this particular envelope exact. No uniform dictionary convergence rate is asserted.

## 3. A rigorous dual lower certificate

Let A c=sum c_j D_v psi_j in Y. For any y in Y satisfying

||y||_Y<=L,
|<A0,y>|<=w,
(A_r^*y)^T Q^-1(A_r^*y)<=1,

one has, for EVERY c,

<g,y>=<g-Ac,y>+<Ac,y>
<=L||g-Ac||_Y+w|c0|+sqrt(c_r^T Q c_r)=J(c).

The last inequality is weighted Cauchy-Schwarz. Q is positive definite on the independent rest directions in the executed dictionary (indeed diagonal because their outputs have different radii). Semidefinite Q requires the corresponding range constraint and pseudoinverse; it must not be inverted as if nonsingular.

Consequently D(y)=<g,y> is a lower bound for inf_c J(c). Together with any verified primal upper value, this encloses the optimal value without trusting the optimizer's status or floating-point derivatives. Only weak duality is needed for correctness; no strong-duality or exact attainment assertion is used by the checker.

A practical finite construction is y=tau(g-A c_hat). Set

r2=R-2b^T c_hat+c_hat^T G c_hat,
v=b-G c_hat.

It is enough to certify

tau^2*r2<=L^2, tau*|v0|<=w, tau^2*v_r^T Q^-1 v_r<=1.

Then D=tau(R-b^T c_hat). The checker chooses rational tau below all three rigorous caps and evaluates both sides with outward rational radical intervals.

For numerical conditioning in the A3 examples, all psi and g are divided by amplitude squared before forming these formulas; the physical objective and dual value are both multiplied by amplitude squared. This is an exact common rescaling, not a change of PDE or norm.

A dual lower value exceeding 1/(4alpha) proves that NO coefficient vector in that fixed dictionary can pass this particular contraction test. It says nothing about PDE blow-up, another dictionary, a sharper norm majorant, a different reference, or a sharper inverse.

## 4. Data and exact information retained

The positive initial wavevectors are (1,1,0),(1,0,1),(0,1,1),(2,-2,0); negatives are conjugates. At a positive k let e be the coordinate unit vector at its zero coordinate and use h_+(k)=(e+i(k cross e)/|k|)/sqrt(2). Every coefficient has the stated amplitude a. The frequency rank is three. These are two-shell, nonlinear data; no output helicity or newly generated frequency is projected away.

The dictionary is the global first heat response plus 11 second-response squared-radius groups {2,6,8,10,14,16,18,24,26,34,42}. Every group retains zero initial trace. The first response satisfies ||psi0||_X<0.3271*a^2 by the parent's analytic temporal maxima certificate. The rest norm uses the FULL coherent Gram of D0 d_rest, not a sum of individual packet magnitudes.

All trial images and residuals include every convolution output. The coefficient field is Q(sqrt(2),i); final weighted norms are exact finite sums of radicals enclosed by rational intervals. Optimization at 85 decimal digits only proposes coefficients, rounded to denominator 10^12. Acceptance is independent of floating-point success flags. The exact same packet backend and parent checker are executed unchanged.

## 5. Executed result A: fewer packets for the same target

For a=3/20 use L=73/20 and alpha=57/2, exactly as in the parent. Select only psi0 and groups {8,6,14}: 90 correction packets instead of the parent's 118.

On this SAME four-direction space, the true least-residual coefficient solution has complete objective in an outward interval around 0.0085875047864363, which is STRICTLY ABOVE r-alpha*r^2=0.0085875 for r=3/200. The full-objective optimized coefficients give

0.00853879576640 < inf J < 0.00853879576645.

The rigorous primal-dual gap is less than 2.84e-14. Use eta=42693979/5000000000 and r=3/200. Then

r-eta-alpha*r^2=243521/5000000000>0,
2alpha*r=171/200<1.

The linear residual itself is deliberately a little LARGER: about 0.000254829715 instead of 0.000240701500. The improvement comes from reducing the norm of the correction sufficiently to outweigh that increase. Full defect: 498 packets, 132 output frequencies, maximum squared radius 42; the complete packet norm is independently checked against the Gram polynomial.

This improves computational use of the same certified data; it is not a new existence result for that already-certified datum and not a global sparsity optimality claim.

## 6. Executed result B: a new specific amplitude and an off-family neighborhood

Take a=19/125=0.152 and the five directions psi0 plus {8,6,14,2}. Certified bounds are

L=92862737/25000000=3.71450948,
alpha=1441074971/50000000=28.82149942.

The least-residual solution has J about 0.008704433252997 and 4alpha*J>1. The full-objective solution satisfies

0.00866390154360 < inf J < 0.00866390154375,

with primal-dual gap less than 1.20e-13. Set

eta=10829877/1250000000=0.0086639016,
r=17/1000.

Exact rational arithmetic verifies

r-eta-alpha*r^2=334253381/50000000000000>0,
2alpha*r=24498274507/25000000000<1.

Hence the inherited all-mode contraction theorem proves a global smooth full NS solution for this specified initial datum with ||u-v||_X<=0.017. The correction uses 118 packets; full defect has 566 packets and 136 output frequencies. This is a pointwise parameter certificate, not proof of all amplitudes in an interval or arbitrary initial data.

The strict margin also certifies a genuine open initial-data neighborhood. If an arbitrary smooth real mean-zero solenoidal perturbation delta is added, the homogeneous linear response has norm at most e^(B_infinity)||delta||_Hdot^1/2 <= sqrt(3/4)L||delta||_Hdot^1/2. Therefore the same radius remains valid provided this additional amount is smaller than the inclusion margin. The checker proves the conservative radius

||delta||_Hdot^1/2 <= 1039067/10^12 = 1.039067e-6.

Such delta need not have A3 support or one helicity. This is a local robustness result around the specified datum, not a universal basin.

## 7. Executed result C: a certificate obstruction, not a singularity

At a=4/25=0.16 include ALL 12 available directions (216 correction packets). Keep the same type of norm majorant and use

L=200630557/50000000=4.01261114,
alpha=1556725999/50000000=31.13451998.

The rational dual and primal certificates give

0.00897683884397 < inf J < 0.00897683884455,

with gap less than 5.61e-13. But 1/(4alpha) is approximately 0.008029672536, strictly below the dual lower bound. Thus no coefficient vector in this dictionary can pass eta+alpha*r^2<=r for ANY r, with these fixed bounds.

Increasing coefficient precision, performing more optimization iterations, or reordering these same columns cannot fix this gap. Enlarging the dictionary, improving the temporal norm majorant or the causal inverse, or changing the reference could change it. Failure is of this explicitly identified sufficient certificate ONLY.

## 8. BRC reuse, proof strength, and next step

REUSE_EXECUTED: exact_packets.py SHA256 0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d and certify_greedy.py SHA256 b2c662832fccd5749d6f531c17b9bbb7ed9f512c42158271076cd1c2fdfba536 unchanged. REUSE_APPLIED: all-mode inverse, temporal first-response bound, lattice C*=9.503, and critical contraction. EXTEND_EXISTING_TOOL: full-objective optimization and rational dual obstruction; no new Foundation/tool acceptance is asserted.

Keep output k, generator rate, time degree, polarization, phase and causal trace until the intended Gram operation. A controlled-error approximation is not an exact quotient. Positive Gram structure does not give off-diagonal signs or arbitrary-data dissipation.

The three numerical cases were actually executed. All dual inequalities, primal values, true least-squares comparison values, full-output identities and nonlinear margins are enclosed with rational arithmetic. The optimizer is not a proof oracle. This is computer-assisted interval verification, not independent review or proof-assistant formalization.

The next useful experiment is to target the certified obstruction: enlarge the norm model/dictionary or sharpen the inverse instead of further optimizing the same exhausted coefficient problem. The overall NS arbitrary-data question remains unclosed.

Primary context consulted: Lobo--Vandenberghe--Boyd--Lebret, Applications of Second-Order Cone Programming, Linear Algebra Appl. 284 (1998), author page https://www.web.stanford.edu/~boyd/papers/socp.html; Morosi--Pizzocchero, On approximate solutions of the incompressible Euler and Navier--Stokes equations, arXiv:1104.3832. These establish method context, not priority or independent validation of our computations.
