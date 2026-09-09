# BRC 临界格点 Gram 常数与因果 Newton 参考流下降工具

Record-ID: `FINDING-EM-PDE-CRITICAL-LATTICE-GRAM-NEWTON-20260909`
Type: `FINDING / RESULT-SPECIFIC TOOL EXTENSION`
Status: `TESTING`
Mathematical status: `ORDINARY_PROOFS + EXACT_FINITE_ENUMERATION / NOT_INDEPENDENTLY_REVIEWED / NOT_ARBITRARY-DATA_REGULARITY`
Date: `2026-09-09`
Researcher-ID: `EM-DIRECT-F00A51`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Project: `Enterprise Math / 进取数论`
Sensitivity: `confidential`

## 0. Purpose, scope, and theorem strength

This record continues the user-selected Navier–Stokes/BRC program downstream of P000. P000 remains unchanged. The Fourier torus, Euclidean helical vectors, and A3/FCC carrier used below are effective classical slices; none of the estimates redefines native 120-degree orthogonality or proves the full native X6 dynamics.

The preceding reference-flow certificate required a valid constant `C0` in

`||P((f.grad)g)||_(Hdot^-1/2) <= C0 ||f||_(Hdot^1)||g||_(Hdot^1)`.

Leaving `C0` unspecified prevented a fully numerical certificate. This note supplies an explicit certified value on the normalized three-torus and then derives a causal Newton reference correction which is a universal strict residual descent direction. The same constant and correction interface transfer to equal-diffusivity incompressible MHD and to skew-linear perturbations such as rotating Navier–Stokes.

No claim is made that `9.503` is sharp. No claim is made that Newton correction succeeds for every initial datum. The results turn previous conditional inequalities into executable numerical theorems and enlarge the class of rigorously certifiable references; they do not solve arbitrary-data 3D Navier–Stokes.

General a posteriori approximate-solution methods and Newton–Kantorovich ideas are established. The result-specific contribution is their composition with the phase/rate-resolved BRC carrier, the critical `Hdot^(1/2)` error norm, the exact lattice-convolution constant below, and the infinite-tail numerical-range certificate inherited from the parent record.

## 1. BRC carrier and operation order

For the bilinear estimate, the population is the set of labeled Fourier input pairs `(p,q), p+q=k`, with output `k`, vector polarization, and complex amplitude retained. For reference correction, the population is extended by time/generator-rate labels.

The safe operation order is

`LABELED INPUT PAIRS -> preserve divergence-free contraction -> coherent sum at output k -> weighted l2 Gram -> global norm bound`.

For exact residuals the order is

`OUTPUT k + GENERATOR RATE sigma + TIME POWER m + COMPLEX AMPLITUDE -> coherent packet formation -> Gram integration -> causal error envelope`.

Positive branch totals before coherent output formation are `NOT_APPLICABLE`: they erase phase cancellation. The lattice constant below is a positive majorant only after the exact divergence-free identity has been used.

Reuse resolution:

- `T0_BRC`: `REUSE_APPLIED` for labeled provenance and coherent-before-square ordering;
- operation-safe quotient: `COMPOSE_APPLIED` to retain output/rate/time labels until the future heat/reference operations are completed;
- preceding critical reference-flow and infinite-tail certificate: `EXTEND_EXISTING_TOOL`;
- a new top-level accepted toolbox family: `NOT_CLAIMED`.

## 2. A dimension-general critical lattice-Gram lemma

Let `d>=3` and work on the normalized torus `T^d=(R/2pi Z)^d`. Fourier norms are

`||h||_(Hdot^s)^2 = sum_(k!=0) |k|^(2s) |hhat(k)|^2`.

Let `f` be mean-zero and divergence-free, and let `g` be mean-zero. Put `B(f,g)=P((f.grad)g)`, where `P` is the Leray projection. Define

`s_c=d/2-1`, `r=(d-1)/2`.

### Theorem LG-d

`||B(f,g)||_(Hdot^(s_c-1)) <= C_d ||f||_(Hdot^r)||g||_(Hdot^r)`,

with the explicit valid constant

`C_d^2 <= a_d^(2d-2) I_d`,

`a_d=1+sqrt(d)/2`,

`I_d=pi^(d/2+1) Gamma(d/2-1)/Gamma((d-1)/2)^2`.

### Proof

For `p+q=k`, incompressibility gives `fhat(p).q=fhat(p).k`. The Leray projection has norm at most one, so

`|Bhat(k)| <= |k| sum_(p+q=k)|fhat(p)||ghat(q)|`.

Set `F_p=|p|^r|fhat(p)|`, `G_q=|q|^r|ghat(q)|`. Then

`|k|^(s_c-1)|Bhat(k)| <= sum_p [|k|^(d/2-1)/(|p|^r|q|^r)] F_p G_q`.

Cauchy–Schwarz in `p` gives a factor `S_d(k)^(1/2)`, where

`S_d(k)=|k|^(d-2) sum_(p!=0,k) 1/(|p|^(d-1)|k-p|^(d-1))`.

After squaring and summing in `k`, the other factor is exactly

`sum_(k,p)F_p^2G_(k-p)^2=||F||_2^2||G||_2^2`.

Associate to every lattice point `p` its unit cube `Q_p=p+[-1/2,1/2]^d`. For nonzero integer `p` and `q=k-p`, and every `x in Q_p`,

`|x|<=|p|+sqrt(d)/2<=a_d|p|`,

`|k-x|<=|q|+sqrt(d)/2<=a_d|q|`.

Therefore

`1/(|p|^(d-1)|q|^(d-1)) <= a_d^(2d-2) int_(Q_p) dx/[|x|^(d-1)|k-x|^(d-1)]`.

The cubes are disjoint. Summing and enlarging to all of `R^d` gives

`S_d(k)<=a_d^(2d-2)|k|^(d-2) int_(R^d) dx/[|x|^(d-1)|k-x|^(d-1)]`.

The continuum integral equals `I_d |k|^(2-d)`. A direct derivation uses the beta/Feynman parameter identity with both exponents `(d-1)/2`, completes the square, integrates `(y^2+m^2)^(-(d-1))`, and then uses `Beta(1/2,1/2)=pi`.

For `d=3`, this general estimate gives the valid but nonsharp constant

`C_3 <= (1+sqrt(3)/2)^2 pi^(3/2)=19.3892...`.

## 3. The explicit three-dimensional constant C*=9.503

For `k in Z^3\{0}`, define

`S(k)=|k| sum_(p!=0,k) 1/(|p|^2|k-p|^2)`.

The Fourier proof above shows that any `C_*` with `sup_k S(k)<=C_*^2` is valid in

`boxed: ||B(f,g)||_(Hdot^-1/2) <= C_* ||f||_(Hdot^1)||g||_(Hdot^1)`.

Let

`P_6={p in Z^3:0<|p|<6}`

and

`N_6(k)=|k| sum_(p in P_6, p!=k)1/(|p|^2|k-p|^2)`.

The exact finite certificate proves

`boxed: N_6(k)<2321/125=18.568 for every k!=0`.             (1)

For `|k|<13`, octahedral symmetry reduces the check to 277 triples

`0<=k1<=k2<=k3`, `0<|k|^2<169`.

Every sum is evaluated with exact rational arithmetic. The largest observed class is `(0,2,2)`, with value `18.56782474525311...`, strictly below `2321/125`.

For `|k|>=13`, put

`A_6=sum_(p in P_6)1/|p|^2=67048852231/1012647636`.

Since `|k-p|>|k|-6` and `K/(K-6)^2` decreases for `K>6`,

`N_6(k)<=13 A_6/49=17.5662988...<2321/125`.

The remaining branches satisfy `|p|>=6` and `|k-p|>=6`. A cube comparison with factor `1+sqrt(3)/12` and the exact integral

`int_(R^3) dx/(|x|^2|k-x|^2)=pi^3/|k|`

gives

`S(k)<2*(2321/125)+(1+sqrt(3)/12)^4*pi^3`.                 (2)

Using the exact rational upper bounds `sqrt(3)<1351/780` and `pi<355/113`, rational arithmetic verifies that the right side of (2) is strictly less than `(9503/1000)^2`. Therefore

`boxed: C_*=9503/1000=9.503`.                              (3)

The finite certificate `certify_lattice_constant.py` covers the entire near part by symmetry; the remaining infinite part is analytic. No sampling-to-infinity inference is used.

## 4. Immediate numerical consequences

All preceding periodic reference-flow theorems may now use `C_*=9.503`.

The critical error bootstrap radius becomes

`h=nu/(4C_*)=nu/38.012=0.02630748... nu`,

and

`h^2=nu^2/(16C_*^2)=0.0006920836... nu^2`.                (4)

The heat-residual initial-data theorem becomes

`Rcal(u0) exp[54 C_*^4 K(u0)^2/nu^4] < nu^4/(32C_*^2)`,   (5)

whose right side is `0.0003460418... nu^4`.

The large one-shell reference theorem is more useful because its numerical-range exponent does not contain `C_*`. Let `a` be the inherited three-line A3 positive-helicity one-shell field with `kappa=sqrt(2)`, and let `u0=Aa+w0`. The exact reference `A exp(-2nu t)a` gives the fully numerical sufficient condition

`boxed: ||w0||_(Hdot^1/2) < 0.02630748... nu * exp[-8.7134250243... A/nu].` (6)

No restriction is placed on the helicity or Fourier support of `w0`; only its critical norm is restricted. The full NS feedback is controlled. Equation (6) is a restricted large-background theorem, not arbitrary-data global regularity.

For equal-viscosity/resistivity MHD in Elsasser variables, the direct-sum bilinear map obeys the same `C_*`; the previous MHD thresholds are therefore numerical as well.

## 5. Causal Newton correction: exact residual homotopy

Let `v` be a prescribed reference on `[0,T]` with full residual

`f_v=v_t+nu Lambda^2v+B(v,v)`.

Let `h` solve the FULL linearized causal problem

`h_t+nu Lambda^2h+B(v,h)+B(h,v)=-f_v`,

`h(0)=0`.                                                   (7)

For `0<=theta<=1`, set `v_theta=v+theta h`.

### Theorem CN1

`boxed: f_(v_theta)=(1-theta)f_v+theta^2 B(h,h).`          (8)

This follows by expanding the quadratic residual; the coefficient of `theta` is exactly the left side of (7), namely `-f_v`.

For any nonnegative time weight `w(t)`, let

`R_w(theta)=int_0^T w(t)||f_(v_theta)(t)||_(Hdot^-1/2)^2dt`.

Then

`R_w(theta)=(1-theta)^2R_w(0)`
`+2theta^2(1-theta) Re int w <f_v,B(h,h)>_-1/2 dt`
`+theta^4 int w||B(h,h)||_-1/2^2dt`,                       (9)

and

`boxed: R_w'(0)=-2R_w(0).`                                (10)

Thus every nonexact reference for which (7) can be solved has a strict causal residual-descent direction. At `theta=1`, the new residual is exactly `B(h,h)`.

This is a Newton–Kantorovich mechanism, not a historical novelty claim. The BRC-specific requirement is to retain output, generator rate, time power, phase, and polarization until the coherent residual Gram is formed.

## 6. Certified descent of the complete causal error score

Residual decrease alone is insufficient because changing the reference may increase its linear error-amplification rate. Let

`beta_v(t)=sup_(||z||=1)[<z,S_vz>-(nu/4)||Lambda z||^2]`.

The preceding coefficient majorant gives

`|beta_(v+theta h)-beta_v|<=theta M(h(t))`.                (11)

Assume the reference matches the exact initial datum. Choose `b_0>=max(beta_v,0)` and let

`m(t)=M(h(t))`, `M_T=int_0^T m(t)dt`.

The causal score is

`Z_theta(T)=(2/nu) int_0^T exp[2 int_s^T b_theta(tau)dtau] ||f_(v_theta)(s)||_-1/2^2 ds`, (12)

with the verified envelope `b_theta<=b_0+theta m`.

Use the base causal weight `w_0(s)=exp[2 int_s^T b_0]`, and define

`rho=||B(h,h)||_(L^2(w_0dt;Hdot^-1/2))/||f_v||_(L^2(w_0dt;Hdot^-1/2))` (13)

when the denominator is nonzero. Then

`boxed: Z_theta/Z_0 <= exp(2theta M_T)[1-theta+rho theta^2]^2`. (14)

Consequently

`limsup_(theta down 0) d/dtheta log Z_theta <= -2+2M_T`.   (15)

If `M_T<1`, the full certificate—not only the residual—has a strict descent direction. An explicit safe step is

`theta_safe=min{1/2,(1-M_T)/(2rho)}`                      (16)

for `rho>0`, and `theta_safe=1/2` for `rho=0`. For every `0<theta<=theta_safe`,

`boxed: Z_theta/Z_0 <= exp[-(1-M_T)theta]<1`.             (17)

Proof: use `log(1+x)<=x` with `x=-theta+rho theta^2`; the step restriction makes the positive quadratic remainder at most half the available linear margin.

The condition `M_T<1` is sufficient, not necessary. If it fails, one may use a shorter certified window, a different Lyapunov metric/preconditioner, or direct interval optimization. A restart may never reset a pre-existing unknown error to zero.

## 7. Quadratic residual convergence under a verified inverse

Suppose the causal linearized solver has a verified trajectory-space bound

`||h||_X<=L||f_v||_Y`,

and

`||B(h,h)||_Y<=C_B||h||_X^2`.

For a full Newton step, (8) gives

`||f_new||_Y<=C_B L^2||f_v||_Y^2`.                        (18)

If the inverse and numerical-range bounds remain valid in a certified neighborhood and `C_B L^2||f_0||_Y<1`, the residual sequence follows the usual quadratic majorant. The finite-core/infinite-tail numerical-range machinery gives one route to verify the linear neighborhood without treating a finite matrix as the complete PDE.

This is conditional on the inverse and neighborhood bounds; it is not an all-data theorem.

## 8. Transfer to other quadratic dissipative systems

### 8.1 Equal-diffusivity incompressible MHD

For Elsasser variables `Z=(z_+,z_-)`,

`B_E(U,V)=(B(U_-,V_+),B(U_+,V_-))`.

The direct-sum norm obeys

`||B_E(U,V)||_-1/2^2 <= C_*^2[||U_-||_1^2||V_+||_1^2+||U_+||_1^2||V_-||_1^2] <= C_*^2||U||_1^2||V||_1^2`. (19)

Thus the explicit constant, causal Newton identity, and numerical-range reference certificate transfer with the same `C_*`.

### 8.2 Rotating or skew-linearly perturbed NS

Consider

`u_t+nu Lambda^2u+Omega R u+B(u,u)=0`,                     (20)

where `R` is skew-adjoint in the critical Hilbert space and commutes with `Lambda`; the Leray-projected Coriolis operator on a periodic domain is the standard example. Then `Re<Lambda w,Rw>=0`. If the same linear term is included in the reference residual and Newton equation, all energy, residual, and bilinear constants above are unchanged. Any oscillatory phase gain must be retained in the phase/rate-resolved Gram.

### 8.3 Finite direct sums

The calculus applies to a finite direct sum whenever the component coupling tensor has a verified Hilbert norm and the concrete equation supplies local existence plus a continuation principle. The lattice constant controls the spatial convection block; the finite component tensor contributes its own explicit norm. Merely being “quadratic plus dissipative” is insufficient.

## 9. Relation to the 120-degree/BRC program

The lattice-Gram constant is not itself the 120-degree cancellation. It is the explicit global safety envelope used after the exact branch structure has been retained.

The 120-degree/A3 layer creates smallness:

- equal-shell homochiral 120-degree branches vanish;
- near-120 outward branches carry angular and radial defects;
- phase/rate-resolved references can be much smaller than branchwise positive totals;
- the numerical-range core retains the full A3 phase/polarization matrix.

The certification layer then converts smallness into a complete-PDE theorem:

`STRUCTURAL CANCELLATION -> EXPLICIT LATTICE GRAM -> NUMERICAL RANGE + INFINITE TAIL -> CAUSAL NEWTON DESCENT -> FULL ERROR CONTROL`.

## 10. Verification and remaining target

`certify_lattice_constant.py` performs exact enumeration of 894 near lattice points, reduction to 277 octahedral output classes, exact rational verification of the near and large-output bounds, and rational certification of `C_*=9.503`.

`newton_descent_check.py` verifies the residual polynomial and runs diagnostic regressions of the safe-step inequality. The proof is analytic; random tests are not theorem evidence.

The next high-value units are:

1. certify the full causal Newton solve with a finite-core/infinite-tail inverse bound, not only a numerical-range upper bound;
2. reduce `C_*` using divergence-free polarization rather than the scalar lattice majorant;
3. prove a uniform Newton/reference basin for a nonperturbative class broader than the current small-residual families;
4. extend the packet/inverse certificate to unequal-diffusivity MHD, where two different heat generators must be retained.

No arbitrary-data conclusion is claimed.

## Primary literature context

- Morosi–Pizzocchero, *On approximate solutions of the incompressible Euler and Navier–Stokes equations*, arXiv:1104.3832.
- Morosi–Pizzocchero, *On the constants in a basic inequality for the Euler and Navier–Stokes equations*, arXiv:1007.4412.
- Pizzocchero–Tassi, *On approximate solutions of the equations of incompressible magnetohydrodynamics*, arXiv:1905.13722.

These references establish surrounding methods; they do not independently verify the critical constant or the BRC packet calculus above.
