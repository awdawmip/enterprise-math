# Critical Hermitian linearization, infinite-tail bounds, and sharper residual certificates

Record-ID: FINDING-EM-PDE-HERMITIAN-TAIL-CERTIFICATE-20260909
Status: TESTING / ORDINARY_PROOFS_AND_INTERVAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Date: 2026-09-09
Scope: real, smooth, divergence-free, mean-zero fields on the normalized torus (R/2pi Z)^3; nu>0.
Authority: global 8acfeac504eee85f6fbb66018470ad233ef33ff7; EM 9d7c4c6eafc5479a6795a128fc0288fc893bed3c.
Parent: research_notes/ns-causal-reference-mhd-20260909.md, blob bc1c8f14e20bbdbe01c97f97fd1f29c275e9d0ee.
Earlier certificate: research_notes/ns-jitter-initial-data-certificate-20260909.md, blob db3a72e6203398e3a876b31a0285679a21e6e131.

## 0. Exact continuation and scope

The parent estimates reference-flow amplification using 216 C0^4 nu^-3 ||v||_H1^4. This note replaces that coarse bound with the Hermitian part of the ACTUAL linearized operator in the critical energy norm. It supplies a global Fourier bound, a finite-core plus rigorously bounded infinite-tail interface, a stronger initial-data certificate for fixed Fourier shapes, and a verified rank-three example.

The 120-degree/native-six-axis premise P000 is unchanged. Fourier vectors below are the previously used classical A3/FCC carrier. The code verifies sum_i n_i n_i^T=2I for its six line readings; this is not a construction of native X6 dynamics. The new result does not assert that the entire linearization vanishes at equal shell or at 120 degrees.

Logarithmic norms, approximate-solution control inequalities, and controlled Galerkin tails are established methods. This is a result-specific extension/composition, not a claim of historical priority or a new accepted BRC Foundation family. There is no arbitrary-data NS or MHD regularity claim.

## 1. Reference-flow energy and the exact target

Use Lambda=(-Delta)^(1/2), B(f,g)=P((f.grad)g), and N(u)=-B(u,u). Fix a PROVEN C0 for

||B(f,g)||_H^-1/2 <= C0 ||f||_H1 ||g||_H1.

For a prescribed smooth reference v, put f=v_t+nu Lambda^2 v+B(v,v) and w=u-v. Its full error equation is

w_t+nu Lambda^2 w+L_v w+B(w,w)=-f,
L_v w=B(v,w)+B(w,v).

Write X=||w||_H1/2^2, Y=||w||_H3/2^2, r=||f||_H^-1/2. Let x=Lambda^1/2 w and

T_v=Lambda^1/2 L_v Lambda^-1/2,
S_v=-(T_v+T_v^*)/2.

For smooth w, the exact reference contribution to X'/2 is <x,S_v x>. This uses the Hermitian part, not the eigenvalues of the generally nonnormal full linearized operator. The latter eigenvalues alone would not control norm growth.

The self-interaction and forcing satisfy

|<Lambda w,B(w,w)>| <= C0 sqrt(X)Y,
r sqrt(Y) <= nu Y/4+r^2/nu.

The smallness bootstrap is X<h^2, h=nu/(4C0). No modes or feedbacks are omitted.

## 2. Exact Fourier Hermitian blocks

Let k,l be nonzero integer wavevectors, m=k-l, kappa=|k|, ell=|l|, and v_m the Fourier coefficient of the real reference. Set P_k=I-kk^T/|k|^2. Inputs satisfy m.v_m=0 and v_-m=conj(v_m).

The raw weighted linearization block is

(T_v)_(k,l)=i sqrt(kappa/ell) P_k[(v_m.l)I+v_m m^T]P_l.

Taking its adjoint reverse block BEFORE estimating gives exactly

(S_v)_(k,l)=-(i/2)P_k[
 ((kappa-ell)/sqrt(kappa ell))(v_m.l)I
 +sqrt(kappa/ell) v_m m^T
 +sqrt(ell/kappa) m v_m^T]P_l.                         (1)

Here v_m^T is a transpose, not a conjugate transpose; reality entered through the reverse Fourier coefficient. The assembled operator is Hermitian. Longitudinal directions may be included with the P_k factors for a conservative finite-matrix bound.

The transport term has gained the exact radial difference kappa-ell. This is the cancellation lost if the two directions of a Fourier interaction are bounded separately. The last two deformation terms remain; equal radii do NOT make the whole block zero.

A constant reference mode has m=0 and contributes S_v=0. This is consistent with uniform translation producing no norm amplification.

## 3. Theorem H1: a bound uniform over ALL perturbation frequencies

For M>0 define

D(M)=(M/2)[1+sqrt(1+M)+1/sqrt(1+M)],
beta(v)=sum_(m!=0) D(|m|)|v_m|.                         (2)

If beta(v)<infinity, then S_v extends to a bounded Hermitian operator on the critical energy coordinates and

||S_v||_(ell2->ell2) <= beta(v).                           (3)

Proof. The projectors are contractions. For the first term of (1), v_m.l=v_m.k, so

|v_m.l|<=|v_m|min(kappa,ell),
|kappa-ell|<=M.

Its norm is at most M|v_m|/2. Since kappa,ell>=1 on the normalized torus,

1/(1+M)<=kappa/ell<=1+M.

Thus sqrt(kappa/ell)+sqrt(ell/kappa) is at most sqrt(1+M)+1/sqrt(1+M). This bounds the last two terms by the rest of D(M)|v_m|. Consequently

|(S_v x)_k| <= sum_m D(|m|)|v_m| |x_(k-m)|.

Young's ell1*ell2 convolution inequality proves (3), initially on finite sequences and then by density. This proof is not a finite-cutoff extrapolation.

The minimum frequency 1 is essential to this particular weight. No identical estimate on homogeneous R3 is claimed. The amplitude dependence is linear for a FIXED Fourier shape, not a universal scale gain for all shapes.

Reserve one quarter of viscosity for the reference operator:

mu(v)=sup_(x!=0) [<x,S_v x>-(nu/4)||Lambda x||_2^2]/||x||_2^2. (4)

Then mu(v)<=beta(v)-nu/4. A simple nonnegative valid coefficient is

a_beta(t)=2 max(beta(v(t))-nu/4,0).                         (5)

## 4. Theorem H2: a finite core with a controlled infinite tail

Let P_N retain all 0<|k|<=N, N>=1, and Q_N=I-P_N. Define

A_N=P_N(S_v-(nu/4)Lambda^2)P_N,
B_N=P_N S_v Q_N.

Let a_N>=lambda_max(A_N) and b_N>=||B_N|| be VALIDATED upper bounds. When v has Fourier support |m|<=M0, B_N has only finitely many nonzero columns: every such high column satisfies N<|l|<=N+M0. This is an exact finite-boundary fact.

For the high-high block use

beta_tail(v,N)=sum_m (|m|/2)[1+sqrt(1+|m|/N)+1/sqrt(1+|m|/N)]|v_m|,
h_N=beta_tail(v,N)-(nu/4)N^2.                              (6)

The proof of H1 with kappa,ell>N gives the high-high form bound h_N. For x=l+h in the orthogonal core/tail split,

<x,(S_v-(nu/4)Lambda^2)x>
<=a_N||l||^2+2b_N||l||||h||+h_N||h||^2.

Therefore

mu(v)<=U_N(v):=(a_N+h_N+sqrt((a_N-h_N)^2+4b_N^2))/2.        (7)

One may take the minimum with beta(v)-nu/4. No neglected Fourier mode is set to zero.

Validated choices include scalar/blocked Gershgorin for a_N, and

b_N<=sqrt(max_i sum_j |(B_N)_ij| * max_j sum_i |(B_N)_ij|).

Sharper validated Hermitian eigenvalue bounds may replace Gershgorin. Unvalidated floating-point eigenvalues are diagnostics only.

For fixed v, b_N<=beta(v), whereas h_N tends to -infinity quadratically. Thus the analytic high-tail correction can vanish as N grows if the finite-core eigenvalue bound is sharpened adequately. This does NOT assert convergence of a coarse Gershgorin estimator to the optimal eigenvalue.

## 5. Full nonlinear causal certificate

The estimate <x,S_v x><=mu(v)X+nu Y/4, the bootstrap C0 sqrt(X)<=nu/4, and the forcing allocation yield

X'+(nu/2)Y <=2mu(v)X+(2/nu)r^2.

Any nonnegative a(t)>=2mu(v(t)) may be used. In particular

a_new=min{216 C0^4 nu^-3||v||_H1^4,
          2[beta(v)-nu/4]_+,
          2[U_N(v)]_+}                                   (8)

is valid whenever the indicated bounds are available. The first entry follows from the parent estimate rather than requiring it to bound mu directly. All entries give the SAME displayed error inequality, so taking their pointwise minimum is legal.

Set A(t)=int_0^t a(s)ds and

Z(t)=exp(A(t))[X(0)+(2/nu)int_0^t exp(-A(s))r(s)^2ds].      (9)

An integrating factor gives

X(t)+(nu/2)int_0^t exp(A(t)-A(s))Y(s)ds<=Z(t).

If A(T)<infinity and Z(T)<h^2, first exit prevents violation of the bootstrap. With the parent's required regularity bounds on the known reference, the exact solution has bounded H1/2 norm and integrable squared H3/2 norm. Interpolation gives ||u||_6^4<=C K(u)Q(u), and the standard (4,6) Prodi-Serrin criterion gives continuation. For T=infinity this proves global regularity of every initial datum that passes the sufficient certificate.

Because a_new can include the old coefficient in its minimum, its causal scalar estimator can never be larger than the old estimator for the SAME reference and residual. Failure to pass is not a blow-up test.

## 6. Initial-data version: linear rather than quartic amplitude penalty

For v(t)=exp(-nu t Lambda^2)u0, let

Rcal(u0)=int_0^infinity ||N(exp(-tau Lambda^2)u0)||_H^-1/2^2dtau.

The parent full heat-rate Gram computes Rcal from the initial data. Since

int_0^infinity 2beta(v(t))dt
=(1/nu)sum_(m!=0) [1+sqrt(1+|m|)+1/sqrt(1+|m|)] |uhat0(m)|/|m|
=:E_F(u0),                                                (10)

H1 and (9) give the sufficient condition

Rcal(u0) exp(E_F(u0)) < nu^4/(32C0^2).                     (11)

The viscosity threshold (5), causal weights, and the finite-core bound can further improve (11). For a fixed Fourier shape u0=Aa, E_F is linear in |A|/nu. The parent heat-reference exponent was 54 C0^4 K0^2/nu^4, quartic in |A|/nu. The improvement is quantitative within the sufficient-condition method; it is not arbitrary-data regularity or a claim of a new scaling-critical space.

For the previously VERIFIED rank-three two-shell positive-helicity A3 family u0=Aa+Bb, with six unit coefficients on radius sqrt(2) and two on radius 2sqrt(2), the inherited exact source is

Rcal=c_R A^2B^2,
c_R=3sqrt(14)/245+7sqrt(10)/250+sqrt(6)/20.

Formula (10) becomes

E_F=d_A A/nu+d_B B/nu,
d_A=6[1+sqrt(1+sqrt(2))+1/sqrt(1+sqrt(2))]/sqrt(2),
d_B=[1+sqrt(1+2sqrt(2))+1/sqrt(1+2sqrt(2))]/sqrt(2).

Numerically d_A=13.5652845313..., d_B=2.45204675146.... For q=A/nu>0, r=B/nu, one explicit sufficient choice is

0<r<=min{1, exp[-(d_A q+d_B)/2]/(8 C0 sqrt(c_R) q)}.        (12)

Indeed c_R q^2 r^2 exp(d_A q+d_B r)<=1/(64 C0^2), strictly below the required 1/(32 C0^2). The previous background penalty had an A^4 exponent; this one has an A exponent at fixed geometry. New helicity and all nonlinear feedback are allowed. The constants c_R and the initial family are inherited, not newly discovered here.

## 7. One validation controls an entire single-shell heat trajectory

For fixed v0, the exact function s -> mu(sv0) is convex, since (4) is a supremum of affine functions of s. Also mu(0)=-nu/4. Therefore, if M0 is a valid upper bound for mu(v0), then for 0<=s<=1,

mu(sv0)<=(M0+nu/4)s-nu/4.                                 (13)

If v0 lies on one Laplacian shell |m|=kappa, its heat reference is v(t)=exp(-nu kappa^2t)v0. Let x=(M0+nu/4)/nu. The total positive coefficient in (9) has the explicit upper bound

E_lin=0, if M0<=0;
E_lin=(2/kappa^2)[x-1/4-(1/4)log(4x)], if M0>0.            (14)

This integrates 2[(M0+nu/4)exp(-nu kappa^2t)-nu/4]_+ exactly. It controls the norm of a nonautonomous linearization without assuming time matrices commute. Convexity, not frozen eigenvalues treated as a propagator, is the required step.

### Verified rank-three A3 reference

At nu=1 take

v_star=(1,1,0)cos(x1-x2)+(0,0,1)cos(x1+x2)
        +(1/3)(1,0,0)cos(x2+x3).

All six nonzero Fourier modes lie on |m|=sqrt(2); their three positive wavevectors have rank three and are FCC root directions. The code uses rational Fourier coefficients 1/2 and 1/6.

At N=8, 2108 nonzero low modes give 6324 ambient component coordinates. The outward-interval Gershgorin/boundary calculation proves

a_N < 2.219269,
b_N < 1.130230,
h_N < -10.158696,
U_N < 2.321623 < 2.322.                                   (15)

These are bounds on the INFINITE operator through H2, not only on its truncation. Using the rational M0=2.322 in (14), kappa^2=2, gives the outward interval

E_lin in [1.73925545812618410678011934366808831590655,
          1.73925545812618410678011934366808831590663],
exp(E_lin) < 5.694.                                       (16)

The analytic Fourier-only exponent is E_F=6.21187590056..., while the old quartic background exponent is (784/3)C0^4. This comparison does not assign an unproved numerical value to C0.

The exact heat residual of this reference's initial datum is

Rcal=1/16+sqrt(2)/384+5sqrt(6)/10368 >0.

The number 5.694 certifies the background amplification, NOT the full nonlinear sufficient inequality for this datum: residual action and a proven C0 must still pass the threshold. No claim that this example passes the complete global test is made.

## 8. Executed checks and reusable implementation

The tool `linearized_certificate.py` contains Fourier block assembly, the analytic beta bound, finite-boundary Schur construction, outward-interval finite-core/tail certification, and the convex single-shell time budget. Its interval entrypoint accepts exact rational real/imaginary components, checks conjugate symmetry and divergence-free input, and uses 40-decimal interval arithmetic. Eigenvalues calculated by ordinary scipy are labeled DIAGNOSTIC, never substituted for validated spectral enclosures.

`verify_linearized_certificate.py` imports the inherited full Fourier routine unchanged (complete file SHA256 ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59). Independent exact convolution agrees with the Hermitian energy form, both giving -1+sqrt(3)/3 for the specified test. It also tests the opposite sign, the scalar energy allocation, and the six-axis frame identity. 800 random complex block checks are regression only; the infinite estimate is proved in Sections 2-4. The N8 interval certificate and single-shell all-time bound are executed, not only specified.

BRC: REUSE_EXECUTED for inherited convolution; EXTEND_EXISTING_TOOL for the causal residual certificate's background observer; COMPOSE_APPLIED for radial-difference symmetrization, Hermitian numerical range, finite boundary and dissipative tail. Retain (k,l,m,polarization,complex phase,conjugate reversal,reference time) until the Hermitian form is assembled. Positive per-triad worst-case rates are not summed as if they were independent amplifiers.

The rank-three spectral certificate is not a proof of all higher-mode dynamics by finite testing. Its rigorous link to the full operator is the explicit analytical tail bound, independently of the diagnostic spectra.

## 9. Boundaries and smallest next unit

1. A fixed normalized torus and smooth prescribed reference are assumed; the beta weight uses the minimum frequency 1.
2. A bound for the linearized error generator does not remove the nonlinear small-error bootstrap or the residual threshold.
3. Better finite references need not exist uniformly for arbitrary data. No monotone success theorem as N or response order grows is proved.
4. General time-dependent, multi-shell references require time enclosures for their validated spectral bound. Only the single-shell scalar heat path is integrated explicitly here.
5. More accurate finite-core eigenvalue enclosures can improve Gershgorin; they remain to be implemented with validation. Floating spectra alone are insufficient.

Next mathematical/computational unit: certify a damped two-generation, multi-shell A3 reference over time, using the new infinite-tail operator bound and the parent's phase-resolved causal residual Gram. Compare the COMPLETE residual score, not just the linear rate or residual separately.

## References and attribution

- Morosi and Pizzocchero, *On approximate solutions of the incompressible Euler and Navier-Stokes equations*, arXiv:1104.3832: established approximate-solution/control-inequality framework.
- Morosi, Pernici and Pizzocchero, *Large order Reynolds expansions for the Navier-Stokes equations*, arXiv:1402.0487: finite reference expansions and a posteriori estimates.
- Zgliczynski and Mischaikow, *Rigorous Numerics for Partial Differential Equations: the Kuramoto-Sivashinsky equation*, arXiv:math/0005247: established principle that Galerkin use needs a rigorously controlled neglected tail; a different PDE and method.
- Pizzocchero and Tassi, arXiv:1905.13722: existing MHD approximate-solution estimates; no new MHD theorem is added in this turn.

References establish context, not independent review of the calculations here. All new findings remain TESTING.
