# 相位分辨的线性化增长率、无限 Fourier 尾部与改进的 NS 参考流证书

Record-ID: FINDING-EM-PDE-SPECTRAL-REFERENCE-20260909
Status: TESTING / ANALYTIC_DERIVATIONS_AND_VALIDATED_FINITE_CORE / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Date: 2026-09-09
Read authority: GLOBAL_KNOWLEDGE main@8acfeac504eee85f6fbb66018470ad233ef33ff7; enterprise-math main@9d7c4c6eafc5479a6795a128fc0288fc893bed3c.
Session key: local-ns-jitter-901c9f34161ce0f1, locally assigned, not an authenticated platform session ID.
Publication state: PROJECT_REPOSITORY_DURABLE_FRONTIER. The note was first produced locally and later persisted through the connected GitHub write path; persistence does not imply theorem acceptance.

## 0. Exact scope and recovered frontier

Continue the direct-user NS/BRC research. P000 is unchanged. The A3/FCC root vectors and the Hilbert-space orthogonality below are the established classical carrier, not a replacement of native 120-degree orthogonality or a construction of native X6 dynamics.

All NEW PDE estimates in this note are on the normalized fixed torus (R/2pi Z)^3, for real smooth divergence-free mean-zero fields, nu>0. The smallest nonzero Fourier radius is one. In particular the coefficient majorant below uses this lower radius; no unchanged R3 extension or all-scale scale-invariant estimate is asserted.

The actual current activity contains a third checkpoint, NS-CAUSAL-REFERENCE-MHD-20260909-03. Its source note is research_notes/ns-causal-reference-mhd-20260909.md at 6b8b49d6fa9da6d14ce18ade92ab8514ca2478a6 (blob bc1c8f14e20bbdbe01c97f97fd1f29c275e9d0ee). Its verification is research_notes/ns-causal-reference-verification-20260909.json at df3ba43d94851be596d330070847fc27bdc70ac1 (blob 697cf19be3de85df59d7c09fe33ce9765db1b07e). These were read in the current run. They supersede the chat's uncertainty about whether that preceding checkpoint had reached the project repository. They are consumed, not republished here.

The selected unfinished unit is its final target: replace the coarse reference-growth cost by the actual signed linearized quadratic form, with a sound bound for all omitted Fourier modes. This note does NOT claim that arbitrary NS data satisfy the resulting error certificate.

Prior art: approximate-solution/control-inequality validation for Euler/NS is established (Morosi–Pizzocchero, arXiv:1104.3832); nonnormal transient growth and the inadequacy of eigenvalues alone are established (Trefethen et al., Science 261 (1993), DOI 10.1126/science.261.5121.578). The result-specific contribution here is the explicit critical-Fourier block, its elementary cutoff-independent bound, a convergent finite-core/infinite-tail upper certificate, and the initial-error estimate below. No historical priority is asserted for the general method.

## 1. The exact growth operator

Use Lambda=(-Delta)^(1/2), B(f,g)=P((f.grad)g), N(u)=-B(u,u), and a valid domain constant C0 with

||B(f,g)||_(Hdot^-1/2) <= C0 ||f||_(Hdot^1)||g||_(Hdot^1).

For a prescribed reference v(t), let

f=v_t+nu Lambda^2 v+B(v,v), w=u-v,
X=||w||_(Hdot^1/2)^2, Y=||w||_(Hdot^3/2)^2, r_f=||f||_(Hdot^-1/2).

Then the full error equation is

w_t+nu Lambda^2w+B(w,w)+B(v,w)+B(w,v)=-f.                 (1)

Put z=Lambda^(1/2)w and, initially on finite Fourier fields, define

L_v z=-Lambda^(1/2)[B(v,Lambda^(-1/2)z)+B(Lambda^(-1/2)z,v)],
S_v=(L_v+L_v*)/2.                                        (2)

Only the Hermitian part enters the instantaneous norm growth:

-Re <Lambda w,B(v,w)+B(w,v)> = <z,S_v z>.                (3)

The unbounded skew transport part cancels in (2). We will prove S_v bounded under an explicit Fourier summability assumption. No diagonalizability or normality of L_v is assumed.

Define the viscously shifted numerical abscissa

beta_v=sup_(||z||_2=1) [<z,S_v z>-(nu/4)||Lambda z||_2^2]. (4)

The supremum is over the solenoidal Fourier Hilbert space and the H1 form domain. For real v, using its complexification for the computation is safe. This is NOT the largest real part of an eigenvalue of L_v. The inequality

<z,S_v z> <= (nu/4)||Lambda z||_2^2+beta_v||z||_2^2       (5)

is the input required by the nonlinear certificate.

## 2. Exact phase-sensitive Fourier blocks

Let p=k-q, K=|k|, Q=|q|, d=sqrt(K/Q), and P_k=I-kk^T/|k|^2. Nonzero k,q are understood. The linearized block is

(L_v)_(kq)=-i*d*P_k[(vhat(p).q)I+vhat(p)p^T]P_q.        (6)

Reality gives vhat(-p)=conj(vhat(p)), and incompressibility gives p.vhat(p)=0. Therefore the exact Hermitian block is

(S_v)_(kq)=-i/2 P_k{(d-d^(-1))(vhat(p).q)I
                     +d vhat(p)p^T+d^(-1)p vhat(p)^T}P_q. (7)

The transpose in vhat(p)^T is bilinear, not Hermitian; the required conjugation has already entered through vhat(-p). Formula (7) is checked against the derivative of the inherited full Fourier convolution, and against (L_(kq)+L_(qk)*)/2.

Equivalently its energy pairing before polar basis coordinates has block

-i/2[(K-Q)(vhat(p).q)I+K vhat(p)p^T+Q p vhat(p)^T].       (8)

This retains phase, direction and polarization. In particular, one must not replace the original blocks by absolute values before taking the Hermitian part: that would throw away the transport cancellation which made (7) bounded.

## 3. A direct all-frequency coefficient majorant

For L>0 set

M_L(v)=sum_(p!=0) |p|[1/2+sqrt(1+|p|/L)] |vhat(p)|.     (9)

For k,q with both K,Q>=L, the block norm in (7) is bounded by the corresponding p summand in (9).

Proof for the transport part: since vhat(p).q=vhat(p).k,

|d-d^(-1)| |vhat(p).q|
=|K-Q| |vhat(p).q|/sqrt(KQ)
<=|p| sqrt(min(K,Q)/max(K,Q)) |vhat(p)|
<=|p| |vhat(p)|.

The outer factor 1/2 accounts for the 1/2 in (9). Each stretching ratio satisfies d or 1/d <=sqrt(1+|p|/L), by K<=Q+|p| and Q<=K+|p|. The two stretching terms, with their factor 1/2, contribute the other part of (9). Orthogonal Leray projections do not increase norms.

Young's convolution inequality on l2 now proves

||S_v||_(l2->l2)<=M_1(v)=:M(v).                           (10)

If Q_L projects onto modes |k|>L, then

||Q_L S_v Q_L||<=M_L(v).                                 (11)

This controls ALL perturbation frequencies, not merely those in the reference support. Sufficient input regularity is finiteness of (9), automatically true for the finite exponential-polynomial Fourier references used here. The bound has an extra half-radius cost for far-separated input/output scales on this fixed torus; it is not advertised as a sharp scale-invariant norm of arbitrary backgrounds.

## 4. Full nonlinear reference theorem with the new growth rate

Let b(t)>=max(beta_v(t),0) be an integrable, verified scalar upper bound. On X<h^2, h=nu/(4C0), the self-interaction obeys

|<Lambda w,B(w,w)>|<=C0 sqrt(X)Y<=nu Y/4.

The forcing obeys r_f sqrt(Y)<=nu Y/4+r_f^2/nu. Apply (5) to the linear reference terms. Equation (1) gives

X'+(nu/2)Y <= 2b(t)X+(2/nu)r_f(t)^2.                    (12)

All self and mixed feedback terms are retained. Define

B_t=2 int_0^t b(s)ds,
Z(t)=exp(B_t)[X(0)+(2/nu)int_0^t exp(-B_s)r_f(s)^2ds].  (13)

The integrating factor proves

X(t)+(nu/2)int_0^t exp(B_t-B_s)Y(s)ds<=Z(t).             (14)

If B_T<infinity and Z(T)<h^2, first exit excludes loss of the bootstrap condition. Since b>=0, (14) controls X and int Y. Assuming the reference itself has bounded Hdot^(1/2) norm and finite L2_t Hdot^(3/2) norm, the true solution inherits these properties. Interpolation gives int||u||_6^4<infinity, so standard Prodi–Serrin continuation applies. For an infinite reference horizon satisfying these bounds, the conclusion is global smoothness.

Available nonnegative bounds which can be minimized pointwise include

b_old=108 C0^4 nu^(-3)||v||_(Hdot^1)^4,
b_coef=(M(v)-nu/4)_+,
b_core=positive part of the verified core-tail upper bound in Section 6. (15)

The old bound follows from the exact Young inequality already proved in the parent. Thus min(b_old,b_coef,b_core) never worsens the prior certificate. It is also safe to use M(v) as a simpler envelope. No derivative of an optimizing frame, eigenvector or cutoff is used: only a verified pointwise quadratic-form inequality is inserted.

## 5. Analytic improvement for a fixed-shape large background

For v(t)=exp(-nu t Lambda^2)u0,

2int_0^infinity M(v(t))dt
=(2/nu)sum_(p!=0) [1/2+sqrt(1+|p|)] |uhat0(p)|/|p|.     (16)

Denote this explicit quantity by E_W(u0). The original full heat-residual Gram Rcal(u0)=int_0^infinity||N(exp(-tau Lambda^2)u0)||_-1/2^2dtau is unchanged. A sufficient initial-data certificate is

Rcal(u0)*exp(E_W(u0)) < nu^4/(32 C0^2).                 (17)

Unlike the previous exponent 54 C0^4 K(u0)^2/nu^4, (16) is homogeneous of degree one in the amplitude of a fixed Fourier shape. The two envelopes should be minimized rather than asserting pointwise superiority for every input.

A cleaner large-background corollary uses an exact reference. Let a be a positive-helicity one-shell field Lambda a=kappa a, curl a=kappa a. For initial data

u0=Aa+w0, A>=0,

use v=A exp(-nu kappa^2t)a. Its residual is zero, without any constraint on the helicity or Fourier support of w0. Therefore

||w0||_(Hdot^1/2)^2 exp[2A M(a)/(nu kappa^2)]
<nu^2/(16 C0^2)                                          (18)

implies global smoothness of full NS. w0 is smooth real mean-zero and solenoidal; the theorem allows all of its later feedback.

For the inherited A3 shape with unit positive-helicity coefficients at (1,1,0),(1,0,1),(0,1,1), and conjugate coefficients at their negatives, kappa=sqrt(2), K(a)=6sqrt(2). All six coefficients have length one. Hence

2M(a)/kappa^2=6sqrt(2)[1/2+sqrt(1+sqrt(2))]
=17.426850048733... .                                    (19)

The older estimate for the SAME exact reference has exponent

3888 C0^4 (A/nu)^4,

whereas (18) uses 17.426850048733...*(A/nu). For sufficiently large A/nu this is a strict enlargement of the certified perturbation ball. Its radius still decreases exponentially in A/nu; arbitrary-data regularity has not been obtained. Large Beltrami-background stability is a known research theme; no historical novelty for that theme is claimed.

## 6. Finite core plus an analytic infinite tail

Let P_L be the projection onto 0<|k|<=L and T_v=S_v-(nu/4)Lambda^2. Define

C_L=P_L T_v P_L,
E_L=P_L S_v Q_L,
a_L=lambda_max(C_L), e_L>=||E_L||,
c_L=M_L(v)-(nu/4)L^2.                                    (20)

The tail quadratic form is <=c_L||z_tail||^2. Consequently

beta_v <= [a_L+c_L+sqrt((a_L-c_L)^2+4e_L^2)]/2.           (21)

A verified UPPER enclosure of a_L can replace it. Proof: split z=z_core+z_tail, retain the exact core form, and bound the off-diagonal term by 2e_L||z_core||||z_tail||. Then take the top eigenvalue of this REAL TWO-BY-TWO comparison matrix. This is a rigorous bound on the entire infinite operator, not a truncation assumption.

If v has finite Fourier support, E_L is a finite matrix: only tail modes q=k-p with |k|<=L and vhat(p)!=0 can couple to the core. All those modes, including q outside the core, are included by the implementation. Sound choices are e_L<=M(v), the Frobenius bound, or sqrt(matrix 1-norm times matrix infinity-norm), with outward interval arithmetic.

Even using e_L=M(v), the analytic tail defect converges to zero. Since v has zero mean, C_L has diagonal entries -nu|k|^2/4 in any transverse Fourier basis and a_L>=-nu/4 for L>=1. For nu(L^2-1)/4>M(v),

0 <= RHS(21)-a_L
<= M(v)^2/[nu(L^2-1)/4-M(v)].                            (22)

This is O(L^-2) for a FIXED reference and nu. Finite Fourier form cores are dense and a_L increases to beta_v. Thus certified finite-core eigenvalue bounds plus (22) can approximate beta_v from above with a controlled infinite-tail error. It does not supply a uniform bound as the reference itself develops unbounded frequency content.

An equivalent practical certificate for a chosen beta>c_L is

beta I - C_L - E_L E_L*/(beta-c_L) >=0.

Using the scalar e_L gives the simpler condition (beta-a_L)(beta-c_L)>=e_L^2, with beta>=a_L,c_L.

## 7. Executed interval example, not merely a floating spectrum

Take nu=1 and the real rank-three A3 reference state

v_*=(1/40)[(1,-1,0)cos(x1+x2)+(1,0,-1)cos(x1+x3)
          +(0,1,1)cos(x2-x3)+(0,1,-1)cos(x2+x3)].        (23)

All four positive frequencies have radius sqrt(2); each listed polarization is orthogonal to its wavevector. Three of the frequencies span R3. Use L=2. The core contains 32 signed wavevectors and two transverse complex polarizations each, dimension 64. Certifying on the full complexification also certifies the real field subspace.

The executable iv_certify.py constructs the exact algebraic matrix (7) with directed interval square roots, then performs interval LDL* on (-31/125)I-C_L. Every pivot has a strictly positive lower endpoint. Separately it encloses every nonzero core-tail entry, bounds the coupling via row/column sums, and bounds the entire tail by (11). It proves

a_L <= -31/125,
e_L <= 53/1000,
c_L <= -319/500.

For beta=-6/25,

(beta-a_L_bound)(beta-c_L_bound)-e_L_bound^2=3/8000>0.

Therefore the ALL-FREQUENCY quadratic form satisfies

boxed: S_(v_*)-(1/4)Lambda^2 <= -(6/25)I.                (24)

The coefficient-only bound would give M(v_*)-1/4=0.1607547948...>0, so it charges positive growth; (24) proves that no such positive charge is needed for this reference at this moment. This is not a claim about eigenvalues of a nonnormal unshifted operator.

For the heat reference v(t)=exp(-2t)v_*, linearity of S gives

T_(v(t))=exp(-2t)T_(v_*)+(1-exp(-2t))[-Lambda^2/4]
<= [-1/4+exp(-2t)/100]I<0.                               (25)

Hence b(t)=0 is valid for this entire reference trajectory in (12). The reference residual remains nonzero and must still meet the error threshold. No numerical value of the nonlinear Sobolev constant C0, and thus no unconditional numerical all-feedback pass for arbitrary data, is asserted by (24).

The interval proof uses mpmath interval arithmetic at 45 decimal digits and an explicitly defined complex conjugation (the installed interval complex method raised an implementation exception). It depends on the correctness of interval arithmetic; it is not a formal proof in a proof assistant. The exact determinant comparison uses rational arithmetic. Diagnostic SciPy eigenvalues and larger finite cutoffs are recorded separately, not used as proof premises.

## 8. BRC and the six-channel carrier

The retained object is the matrix of signed/complex couplings, NOT the list of magnitudes of branches. Form (7) only after assembling the adjoint pair. The finite core retains all polarization blocks and their phases; only the analytically controlled tail is compressed to scalar bounds. This is a justified coarse observer for a specified FUTURE OPERATION: bounding the error-energy quadratic form.

Let N have the six normalized FCC direction columns. N N^T=2I. Thus T=N^T/sqrt(2) is an isometry and the compatible six-channel state is Tz. The equivalent six-channel operator is T S_v T*, restricted to ran(T) and the transformed solenoidal constraints. The unused complementary channels are not extra physical modes; including them would add spurious zero eigenvalues. The code verifies N N^T=2I exactly. This is the prior effective carrier, not a redefinition of native project orthogonality.

REUSE_EXECUTED: unchanged inherited_fourier.py, SHA256 ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59, used to verify the full derivative energy on an explicit nonzero example.
REUSE_APPLIED: the current critical reference theorem, causal integrating factor, error self-interaction threshold, and established Prodi–Serrin interface.
EXTEND_EXISTING_TOOL: the result-specific residual certificate now accepts a verified Hermitian-growth envelope and its analytic infinite-tail certificate. No new top-level BRC family or accepted Foundation result is claimed.
NOT_APPLICABLE: use of a mere finite numerical spectrum, collapse of complex matrix entries before symmetrization, or removal of high-frequency modes without a bound.

## 9. Certified time windows, not sample-only eigenvalues

The shifted numerical abscissa is Lipschitz under a known background perturbation:

|beta_v-beta_w| <= ||S_v-S_w|| <= M(v-w).                 (26)

This follows directly from the variational definition, since the negative Laplacian term is the same. Suppose a reference is a finite packet sum

vhat(p,t)=sum_j a_(p,j) t^(m_j) exp(-lambda_j t),

with lambda_j>0. On I=[t0,t1], h=t1-t0, a safe all-time variation envelope is

Delta_I=h sum_(p,j) |p|[1/2+sqrt(1+|p|)] |a_(p,j)|
 *[m_j t1^(m_j-1)+lambda_j t1^m_j] exp(-lambda_j t0),     (27)

where the m_j term is zero for m_j=0. The derivative product rule and the fundamental theorem of calculus prove M(v(t)-v(t0))<=Delta_I for every t in I. Sharper interval enclosures may replace (27). Thus a node certificate beta_v(t0)<=beta0 provides the UNIFORM interval bound

b_I=max(0,beta0+Delta_I).                                 (28)

It is not legitimate to omit Delta_I merely because time samples look stable.

With piecewise constant verified b_I, the causal error envelope can be integrated exactly on each finite interval. If r_f(t)^2=sum_(lambda,m) d_(lambda,m)t^m exp(-lambda t), keep signed coefficients after the coherent Fourier norm expansion. Define

T_m(c,t)=exp(-ct) sum_(j=0)^m [m!/(m-j)!] t^(m-j)/c^(j+1),

so -partial_t T_m(c,t)=t^m exp(-ct). Then the exact scalar recurrence is

Z(t1)=exp(2b_I h)Z(t0)
 +(2/nu)sum_(lambda,m) d_(lambda,m) exp(2b_I t1)
   [T_m(lambda+2b_I,t0)-T_m(lambda+2b_I,t1)].              (29)

All denominators are positive. The coefficients d may have either sign; positivity belongs to the total residual norm/Gram, not its expanded terms. causal_windows.py implements (29) with SymPy and tests it against direct integration and subdivision of the same certified window. It requires an EXTERNALLY VERIFIED b_I and does not infer it from samples. Thus it can consume (28) once the node matrix and coefficient intervals are certified.

This closes the logical sampling gap. A general automated optimizer choosing time windows, cutoffs and reference corrections is still not implemented, and no claim is made that its certificates will succeed for all initial data.

## 10. Checks, limits and the smallest remaining step

Actual checks in this run:
- inherited file hash equality;
- nonzero exact Fourier derivative-energy identity, value 1/3-7sqrt(5)/9 on the chosen test;
- exact six-channel isometry and viscosity allocation;
- 800 random complex solenoidal block tests (regression only);
- a 64-dimensional directed-interval LDL* certificate;
- exact rational 2x2 whole-space block comparison;
- floating larger-core comparisons (diagnostic only);
- 15 exact polynomial-exponential antiderivative checks, a coherent signed residual cross-term identity, and exact causal subdivision/direct-integration agreement.

The next mathematical/computational unit is to combine the validated node matrices, the proven time-window envelope (27)-(28), and the exact causal integrator (29) for the damped reference v1+eta v2. The analytic interfaces and a concrete all-time heat-reference certificate are present; a robust automatic optimizer and a numerically certified domain constant C0 are not. A low residual alone is still insufficient without its growth and error budgets.

General regularity still requires a certificate for arbitrary initial data or another uniform argument. This work improves a specific sufficient criterion and supplies a reusable sound finite-core/infinite-tail computation; it does not remove the need for small certified error.

## Primary external references

- Morosi and Pizzocchero, On approximate solutions of the incompressible Euler and Navier–Stokes equations, arXiv:1104.3832. Prior a posteriori framework, not independent validation of this note.
- Trefethen et al., Hydrodynamic Stability Without Eigenvalues, Science 261 (1993), DOI 10.1126/science.261.5121.578. Prior nonnormality/transient-growth boundary.
- Zhang, Li and Yao, A remark on the global regularity criterion for the 3D Navier–Stokes equations based on end-point Prodi–Serrin conditions, DOI 10.1016/j.aml.2018.04.003. Introduction states the standard non-endpoint criterion used here with time exponent 4 and space exponent 6.
