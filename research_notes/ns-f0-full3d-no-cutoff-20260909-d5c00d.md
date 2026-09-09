# Full-output three-direction transport, a finite residual Gram, and a cutoff-independent small-data budget

Record-ID: FINDING-EM-NS-F0-FULL3D-20260909-D5C00D
Progress-Event-ID: NS-F0-FULL3D-20260909-D5C00D-07
Researcher-ID: EM-DIRECT-D5C00D
Research-Activity-ID: RA-D5C00DF7D77F4AA2ACE0
Session: local-chat-ns-openai-audit-d5c00df7d77f4aa2ace0 (local continuation key, not a platform-authenticated ID).
Status: ORDINARY_FINITE_ALGEBRA_PROOFS / EXACT_RATIONAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED
P000 unchanged. No Lean verification, Foundation promotion, continuum Navier-Stokes theorem, or native six-dimensional dynamics is claimed.

## 0. Continuation and provenance

Continue the unfinished unit in `research_notes/ns-f0-discrete-transfer-20260909-d5c00d.md`, rather than repeating its restricted tridiagonal experiment. Its immutable source is `006e72f9cd3358881e5bf99a02ae9f7ca515a6a1`. The exact arithmetic implementation at `9fd171fef6efeb60df9b717fd2354cef62beee6d:experiments/ns_f0_discrete_transfer_d5c00d.py` is reused unchanged; The full expected SHA256 is `b3feb31d191fe17148a7c14505ddbb98aa5eb274a31c9053158a680a26460bdb`, and the checker verifies it.

Read snapshots: EM `142a178b96ea99f704994e696139e2b88f5f8199`; GLOBAL_KNOWLEDGE `48b078097d17f96423749529cf8c90d7a7761c87`.

The selected research question is whether the preceding finite phase-aware budget survives genuinely three-direction coupling while keeping every generated port, and what uniform conclusion can actually be closed. It does not take over the other NS activity or its initial-data-certificate task.

REUSE_EXECUTED: parent Gaussian-rational arithmetic, radical bounds and toward-zero scalar quantizer.
EXTEND_EXISTING_TOOL: full-output packet/rate residual Gram, now with arbitrarily many contributions per output.
REUSE_APPLIED: BRC observer-fiber discipline; preserve signed complex Cartesian vector coefficients, which retain rather than discard the information needed to reconstruct helicity. No positive energy observer replaces the underlying phase-resolved state.

The full system below does not retain the parent's special linear midpoint solve. In three-direction coupling that nonlinear midpoint problem is no longer the proved tridiagonal rational solve. We instead freeze an explicit adaptive rule, record its temporal defect, and prove only results for that exact rule. Neither algorithm is asserted to be nature's native update.

## 1. Fixed algebraic law with no spectral cutoff

Let a state be a finitely supported family of Gaussian-rational three-vectors

    u_k in Q[i]^3, k in Z^3 minus {0},
    u_-k=conj(u_k), k dot u_k=0.

This is a typed classical three-dimensional Fourier carrier, not the project's native six-dimensional ontology. All sums below are finite at each actual step. No fixed maximum frequency is imposed.

For k!=0 define the rational orthogonal projector

    P_k v = v - k (k dot v)/|k|^2,

and the ordered bilinear transport

    B(a,b)_k = -i P_k sum_{p+q=k} (a_p dot q) b_q.

Set

    N(u)=B(u,u), D u_k=|k|^2 u_k,
    F(u)=-nu D u + N(u), nu>0.

F denotes the discrete generator, NOT an external force. There is no external-force argument in the law. A zero-frequency product vanishes because q=-p and p dot u_p=0.

Every ordered (k,p,q) contribution is calculated. The support of F is contained in supp(u) union (supp(u)+supp(u)); contributions at coincident outputs are added coherently. Cancellation is not deletion by a frequency boundary.

Define

    E(u)=1/2 sum_k |u_k|^2,
    D_E(u)=sum_k |k|^2 |u_k|^2.

Finite rearrangement of the convolution, conjugate symmetry, and a_p dot p=0 prove

    Re <c,B(a,b)> = -Re <b,B(a,c)>.

For example replace (k,q,p) by (q,k,-p); a_-p=conj(a_p) and a_p dot q=a_p dot k. The projection can be removed when paired with a solenoidal output. Consequently

    Re <u,N(u)>=0, Re <u,F(u)>=-nu D_E(u).                 (1)

These are identities of finite sums, not deductions from a smoothness assumption.

Fix a positive rational step cap h_cap. At nonzero u choose the first halving h=h_cap/2^m satisfying BOTH

    h |F(u)|_2^2 <= nu D_E(u),
    h nu max_{k in supp(u)} |k|^2 <= 1.                   (2)

F(u)!=0 follows from (1). Thus the halving terminates by rational comparison. Define the raw update

    v=u+h F(u).                                          (3)

There is no implicit terminal-state selection. The rule, including (2), is fixed before choosing the examples.

## 2. Quantization must preserve the solenoidal constraint

Independent rounding of Cartesian velocity components is invalid in general. At k=(1,2,0), v=(2/5,-1/5,0) is solenoidal; coordinatewise quarter-grid truncation gives (1/4,0,0), whose k-dot-product is 1/4.

For each representative of the pair {k,-k}, choose deterministic primitive integer vectors e_k,f_k with

    e_k perpendicular k, f_k perpendicular k, e_k perpendicular f_k.

The implementation chooses a coordinate direction not parallel to k, takes k cross that direction and divides by the gcd, then takes k cross e_k and divides by its gcd. These are orthogonal, not necessarily normalized, vectors. Write uniquely

    v_k = alpha_k e_k + beta_k f_k, alpha_k,beta_k in Q[i].

Round real and imaginary parts of alpha,beta toward zero to delta Z, with fixed rational delta>0; restore the conjugate partner. Call this Q_delta and set

    u^+=Q_delta(v).                                      (4)

Orthogonality gives

    |Q_delta(v)_k|^2 <= |v_k|^2,

and exactly preserves reality and zero divergence. The choice of integer basis is part of the declared algorithm; quantization is basis-dependent, and no rotationally invariant physical interpretation is asserted.

All raw generated ports are evaluated. Quantization may erase a port, but its amplitude and budget defect are explicitly retained in the report. Thus NO SPECTRAL CUTOFF is not the same as NO INFORMATION LOSS.

## 3. Exact energy law and a no-go for fixed-grid unlimited growth

Expansion of (3) and (1) gives

    E(v)-E(u)=-h nu D_E(u)+(h^2/2)|F(u)|_2^2
             <=-(h nu/2)D_E(u)<0                         (5)

for u!=0. Quantization only decreases E further.

On the grid, conjugate-pair summation and integer e_k,f_k imply

    E(u)/delta^2 in N_0.

Every nonzero step strictly lowers this nonnegative integer. Therefore every orbit of THIS law reaches zero after at most

    E(u_0)/delta^2                                       (6)

nonzero updates, even though its frequency support is not fixed in advance.

This conclusion is stronger than the parent's fixed-cutoff extinction result, but it is still a theorem about the chosen quantizer/update, not nature or the continuum PDE. The bound diverges as delta decreases. Strict energy descent plus fixed-grid energy discreteness is precisely why this algorithm cannot prove unlimited autonomous instability. Changing that fact requires an explicitly different model or a justified refinement limit, not a rhetorical relabeling of transient amplification.

For the large example below the bound is 25,165,824 steps. Only 12 steps were executed, and extinction was NOT observed in that run.

## 4. Exact critical-weighted transfer and a genuine three-direction witness

Define the finite algebraic readout

    K(u)=1/2 sum_k |k| |u_k|^2,
    D_K(u)=sum_k |k|^3 |u_k|^2,
    T(u)=Re sum_k |k| conj(u_k) dot N(u)_k.

In the classical torus interpretation K is one half of the squared homogeneous H^(1/2) norm. No such interpretation is required for the finite identities. Square roots |k| are algebraic weights, with signs decided by rational enclosures.

The exact raw-step identity is

    K(v)-K(u)=h[T(u)-nu D_K(u)]
              +(h^2/2) sum_k |k| |F(u)_k|^2.             (7)

For the grid update add the precision defect K(Q_delta v)-K(v)<=0. This splits true signed generator transfer from the positive explicit-step defect and the negative modewise rounding defect.

### Explicit paired initial states

Let e1,e2,e3 denote coordinate vectors, and define positive-frequency coefficients

    u_(1,0,0)=32 e2, u_(0,1,0)=32 e3, u_(0,0,1)=32 e1,
    u_(1,1,0)=sigma 32 i e3,
    u_(0,1,1)=sigma 32 i e1,
    u_(1,0,1)=sigma 32 i e2,

with sigma=-1 or +1 and conjugate negative frequencies. These supports span all three frequency directions, all three velocity components participate, and their interactions are coupled; this is not a two-variable shear ansatz.

Fix nu=1, h_cap=1/4096, delta=1/64. Both states satisfy the guards at the SAME h=1/4096. Both have E_0=6144 and identical modal energies at every frequency.

For sigma=-1,

    T=196608(sqrt(2)-1),
    h(T-nu D_K)=45 sqrt(2)-99/2 >14.                     (8)

The positive signed-generator contribution is already present before the numerical h^2 term. The exact grid result is

    Delta E=-1259/256,
    Delta K=-208029/4096+185763/4096 sqrt(2)
              +227/2048 sqrt(3)+3/16 sqrt(5)+225/1024 sqrt(6),
    14 < Delta K < 15.                                  (9)

For sigma=+1,

    T=-196608(sqrt(2)-1),
    Delta E=-1259/256,
    Delta K=184995/4096-207261/4096 sqrt(2)
              +227/2048 sqrt(3)+3/16 sqrt(5)+225/1024 sqrt(6),
    -26 < Delta K < -25.                                (10)

All inequality signs were certified with rational square-root bounds. Each raw and rounded first-step field has 36 nonzero modes: all 24 newly generated frequencies are retained. The initial 72 nonzero ordered convection packets occupy 38 output ports, of which two cancel exactly, leaving 36 nonzero nonlinear output modes. Zero after coherent addition is distinguished from a deleted port.

As an additional 3D diagnostic, with omega_k=i k cross u_k, the signed vortex-stretching production is exactly

    Re <omega,(omega dot grad)u>=+196608 (sigma=-1),
                                 -196608 (sigma=+1).

The checker verifies it equals Re <D u,N(u)>. This diagnostic does not by itself prove instability or singularity.

### Actual continuation, not a first-step-only example

For sigma=-1, 12 full-output updates were executed. Their total discrete physical-time label is 3/1024; the final field has 74 modes and

    E_12=6201937/1024 < 6144,
    183 < K_12-K_0 < 184.

There is no spectral cutoff at any step. However, beginning at step two quantization erases newly generated small coefficients. The erased-port counts are

    0,168,168,172,172,170,170,250,284,278,318,362.

At step twelve 436 raw generator modes are evaluated before the 74-mode quantized state is produced. The report records the exact rounding energy loss, state error, weighted-readout loss and full output count at every step. This is not an unquantized NS trajectory.

The paired witness proves that a complete list of modal energies is not a sufficient observer for the next K under the SAME 3D law and time step. It is not a proof that one phase sign must remain positive at all later times.

## 5. A cutoff-independent all-step small-data budget

Define finite Fourier absolute-mass readouts

    X_s(u)=sum_{k!=0} |k|^s |u_k|, s=-1,0,1.

Because u_p dot q=u_p dot k and P_k is orthogonally contractive,

    |N(u)_k|/|k| <= sum_{p+q=k}|u_p||u_q|.

Summing all outputs and applying finite Cauchy-Schwarz gives

    X_-1(N(u)) <= X_0(u)^2 <= X_-1(u) X_1(u).            (11)

No phase cancellation is silently used: (11) is an explicitly conservative absolute-value majorant. The phase-resolved state and packets remain available for sharper analysis.

The second step guard in (2) makes 1-h nu |k|^2 nonnegative on the old support. At newly generated modes u_k=0. Triangle inequality, (11), and modewise contractivity of Q_delta therefore give

    X_-1(u^+) <= X_-1(u)
       -h[nu-X_-1(u)] X_1(u).                            (12)

If X_-1(u_0)<=a<nu and epsilon=nu-a, induction and finite telescoping yield, for EVERY finite horizon m,

    X_-1(u_m)+epsilon sum_{n<m} h_n X_1(u_n)
      <= X_-1(u_0) <= a,                                (13)

    sum_{n<m} h_n X_-1(N(u_n)) <= a^2/epsilon.           (14)

The constants do not depend on a spectral cutoff, the number of generated frequencies, delta, or m. This closes a genuine all-step cumulative nonlinear bound in a SMALL-DATA domain of the selected discrete law. It does not control arbitrary data or prove a continuum limit.

The proof is the finite discrete analogue of the classical Lei-Lin Fourier X^-1 small-data mechanism; it is NOT claimed as a new small-data principle. Lei and Lin established the corresponding continuous NS result in 2011, and the periodic setting has also been studied. See references below. What is explicitly verified here is compatibility with the full-output adaptive recurrence and the solenoidal fixed-grid quantizer, using finite algebra rather than using smoothness to infer a physical result.

The checker executes 16 small-data steps with initial amplitude 1/64, nu=1, delta=1/8192, a=1/5 and epsilon=4/5. It certifies (13)-(14) by rational norm enclosures. The horizon-independent upper bounds are

    sum h_n X_1(u_n)<=1/4,
    sum h_n X_-1(N(u_n))<=1/20.

The large phase witness is outside this small-data region. No extrapolation from (13) to that witness is made.

## 6. Arbitrarily many packets per output: a finite residual Gram

Fix a reference eta>0 ONCE for the whole orbit, independently of adaptive h_n. Let

    r_k=(1+eta nu |k|^2)^-1, H_eta u_k=r_k u_k.

This is a rational backward-Euler reference, not the actual nonlinear update. It differs from the parent's Cayley reference. The choice prevents high-frequency reference multipliers from approaching -1 and keeps

    0<r_k<=r_1=(1+eta nu)^-1<1.

For every ordered packet a=(k,p,q), p+q=k, retain

    c_a=-i P_k[(u_p dot q)u_q], rho_a=r_p r_q.

Define the finite quartic form

    J_eta(u)=sum_k |k|^-1 sum_{a,b at k}
               Re[conj(c_a) dot c_b]/(1-rho_a rho_b).    (15)

The complete amplitude contraction is formed BEFORE any positivity claim. Equal rho values may be grouped by coherent VECTOR addition for this reference observer, but their (k,p,q) records are retained for future nonlinear operations.

For distinct real r_i in (-1,1), the finite Cauchy determinant identity is

    det[1/(1-r_i r_j)]
      =product_{i<j}(r_i-r_j)^2 /
       [product_i(1-r_i^2) product_{i<j}(1-r_i r_j)^2].   (16)

Every leading principal determinant is positive. Thus the matrix is positive definite on distinct-rate groups. Repeated rates give a positive semidefinite matrix by exact grouping. This proves J_eta>=0 for ANY finite number of packets, without an infinite-series or smoothness argument. Equation (16) is standard Cauchy algebra, not a novelty claim.

Moreover J_eta(u)=0 iff every output/rate group's coherent vector sum is zero. The Vandermonde matrix for distinct rates shows the same groups determine every finite linear-reference response. Equal-rate grouping is licensed for this observer; it is not claimed to preserve general nonlinear futures.

Under H_eta, c_a becomes rho_a c_a. Direct subtraction of finite fractions yields

    J_eta(u)-J_eta(H_eta u)
       =sum_k |k|^-1 |N(u)_k|^2 = R(u).                 (17)

All generated outputs are present, including ports not initially occupied. Denominators have the uniform scalar bound

    1-rho_a rho_b >= 1-r_1^4>0.

This controls denominators only; it does not remove the growth in number, magnitude or coherent arrangement of packets.

For the actual adaptive explicit step put L_h u=(1-h nu D)u and v=L_hu+hN(u). There are now THREE separate defects:

    I_NL=J_eta(v)-J_eta(L_hu),
    I_time=J_eta(L_hu)-J_eta(H_eta u),
    I_precision=J_eta(Q_delta v)-J_eta(v).

Exactly,

    J_eta(u^+)-J_eta(u)+R(u)
       =I_NL+I_time+I_precision.                         (18)

No forcing is introduced into the evolution by defining these diagnostic quantities. No sign or summability of the three defects is assumed. Keeping eta fixed avoids an additional changing-metric term; choosing eta=h_n without accounting for J_{h_(n+1)}-J_{h_n} would be an error.

This full-convection residual Gram is NOT automatically the earlier helicity-sector heat-jitter functional. The old continuum inequality for F=J+nu^2 K/4 cannot be transferred to (15) without a new bridge proof.

For the actual first large-data step the complete Gram identity and (18) are verified exactly, with 72 ordered initial packets and 44 output/rate groups. Twelve additional 3D rational fields verify (17); six exact determinant tests include distinct, negative, zero and repeated nodes.

## 7. The temporal defect is also explicitly nonzero

Even with zero spectral cutoff defect, the explicit recurrence is not an exact continuous NS solution. As a finite algebraic diagnostic define the affine within-step expression w(s)=u+sF(u), 0<=s<=h, before the quantization jump.

Its equation defect expands EXACTLY as

    w_s+nu Dw-N(w)=s R1+s^2 R2,
    R1=nu D F-B(u,F)-B(F,u), R2=-B(F,F).                 (19)

This is a polynomial identity in s with finite coefficients; it is not a claim that a smooth interpolation realizes the discrete law physically. The checker evaluates the identity at s=0,h/2,h as independent algebraic regression tests. The displayed formula itself is obtained by bilinear expansion and holds for every s.

A finite bound is

    |s R1+s^2 R2|_2^2 <=2h^2 |R1|_2^2+2h^4 |R2|_2^2.

The bound is not assumed to be small. The quantization jump e=Q_delta(v)-v is a SEPARATE defect, not absorbed into an admissible smooth external force. Convergence would require cumulative control of both time and precision defects in the chosen topology, plus a justified bridge. None is asserted here.

## 8. Conclusions and exact unfinished frontier

Completed:
- full-output 3D rational transport with preserved reality/divergence;
- same-step, same-modal-energy opposite-transfer witness with all first-step new modes;
- explicit 12-step transport/precision ledger, no spectral cutoff;
- all-step small-data X^-1 budget with cutoff-independent constants;
- arbitrary-finite-packet positive residual Gram and three-defect identity;
- no-go: strict fixed-grid energy descent forces extinction even without fixed support.

Not completed:
- arbitrary-data cumulative signed nonlinear control;
- a discrete-to-classical NS bridge or a physical/native-state bridge;
- a proof of Lyapunov instability, unlimited growth or finite-time singularity;
- an independent proof review or Lean validation.

Next proof-bearing unit: outside X_-1<nu, retain output/input-rate and full signed vector provenance and seek a cumulative bound for I_NL+I_time+I_precision (or an exact counterexample) without hiding quantization or reference-metric changes. The phase-majorant route (11) is deliberately too conservative there. Merely adding modes or repeating one-step positive K cases does not close that unit.

## References and attribution

1. Parent EM note and exact checker pinned in section 0.
2. Zhen Lei and Fang-Hua Lin, Global mild solutions of Navier-Stokes equations, Communications on Pure and Applied Mathematics 64 (2011), 1297-1304, DOI 10.1002/cpa.20361; author preprint https://arxiv.org/abs/1203.2699 . Used for attribution of the X^-1 small-data mechanism, not as a substitute for the finite proof (11)-(14).
3. D. M. Ambrose, M. C. Lopes Filho and H. J. Nussenzveig Lopes, Existence and analyticity of the Lei-Lin solution of the Navier-Stokes equations on the torus; https://arxiv.org/abs/2205.12383 . Periodic prior-art boundary.
4. NIST DLMF, section 1.3(ii), equation 1.3.14, Cauchy determinant: https://dlmf.nist.gov/1.3.E14 . Finite identity underlying (16).
5. V. Carlier, M. Campos Pinto and F. Fambri, Mass, momentum and energy preserving FEEC and broken-FEEC schemes for the incompressible Navier-Stokes equations; https://arxiv.org/abs/2306.13778 . Context: preserving divergence and energy in discrete NS is established numerical-analysis practice. The present certificate is not claimed to originate that principle.

The earlier use of same-witness assembly and explicit defect bookkeeping does not require accepting any external blow-up construction.
