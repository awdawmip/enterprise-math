# 黏性三元放大预算与零点安全的 BRC 抖动能量

Record ID: `FINDING-EM-PDE-VISCOUS-JITTER-BUDGET-20260909`
Type: `FINDING`
Status: `TESTING`
Mathematical status: `ORDINARY_PROOFS + EXACT_FINITE_FOURIER_CHECKS / NOT_INDEPENDENTLY_REVIEWED / NO_ARBITRARY_DATA_REGULARITY_CLAIM`
Effective: `2026-09-09`
Projects: `enterprise-math`
Researcher-ID: `EM-DIRECT-F00A51`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Scope: isolated viscous helical triad; smooth full incompressible NS on normalized 2pi-periodic torus, with the stated critical inequalities on R3 as well.
Sensitivity: `confidential`
Authority snapshot: global `177139aafc2abe6884329ed993531b4fcd614cf6`; EM source `bd7196df29f427fe2fbb90ef2616cd416fcf6d00`.
Session key is locally assigned; it is not an authenticated platform session ID. This is direct user research, not a formal task claim, review, or Foundation promotion.

## 0. Question and inherited boundary

Continue the proposed residual-amplification / delayed-flip mechanism mathematically. P000 remains the project premise. The Fourier vectors, helical projectors, and 120-degree carrier triangles below are effective classical objects, not a construction of the complete native X6 dynamics.

The verified parent frontier includes:

- `pde-helical-triad-intermediate-shell-instability-20260908.md`: homochiral middle-shell instability and the frozen viscous eigenvalue;
- `pde-helical-triad-heteroclinic-flip-20260908.md`: inviscid tanh/sech separatrix;
- `pde-brc-latent-jitter-gram-lyapunov-20260908.md`: the positive latent Gram and exact balance;
- `pde-brc-latent-jitter-local-metric-response-control-20260908.md`: the zero-jitter Hessian;
- `pde-helical-radial-commutator-action-continuation-20260908.md`: finite commutator action implies continuation.

These parent paths are in `knowledge/projects/enterprise-math/` of `awdawmip/chatgpt-global-knowledge`. The helical triad framework and intermediate-shell instability are established theory, notably Waleffe (1992), DOI `10.1063/1.858309`; no novelty claim is made for them.

This note adds: a finite amplification budget for the FULL nonlinear isolated viscous triad; an exact smooth PDE witness showing that a logarithmic jitter rate can diverge merely at residual birth; and a globally positive, zero-safe combined critical energy. No infinite Fourier network is replaced by an isolated triad.

## 1. Full viscous triad, including pump feedback

Let `0<k<p<q` be the radii of a nondegenerate closed Fourier triangle. Set

`a=q-p>0`, `c=p-k>0`, `b=a+c=q-k`.

After a constant phase gauge choose the common helical coupling `G>0`. The complex homochiral triad is

`x'=-nu*k^2*x-a*G*conj(y)*conj(z)`,
`y'=-nu*p^2*y+b*G*conj(z)*conj(x)`,
`z'=-nu*q^2*z-c*G*conj(x)*conj(y)`.

All three amplitudes evolve. In particular the pump `y` is not held constant.

Its energy `E=|x|^2+|y|^2+|z|^2` satisfies exactly

`E'=-2nu(k^2|x|^2+p^2|y|^2+q^2|z|^2)`.

The nonlinear terms cancel because `-a+b-c=0`. Consequently

`E(t)<=E0*exp(-2nu*k^2*t)`

and `|y(t)|<=sqrt(E0)*exp(-nu*k^2*t)`.

Finite-dimensional polynomial local existence, this bounded energy, and the ordinary ODE extension theorem give global existence of this isolated system. That fact alone is not a PDE regularity statement.

## 2. A single fixed metric makes the side dynamics Hermitian

Define

`eta=(sqrt(c)*x, sqrt(a)*conj(z))`,
`W=|eta|^2=c|x|^2+a|z|^2`,
`g=G*sqrt(a*c)`.

The FULL nonlinear solution obeys the exact side equation

`eta'=M(y(t))*eta`,

where

`M(y)=[[-nu*k^2, -g*conj(y)],[-g*y,-nu*q^2]]`.

This is Hermitian at every time, even when the pump phase changes. No commutation of matrices at different times is assumed. Its largest eigenvalue is

`mu(y)=-d+sqrt(e^2+g^2|y|^2)`,
`d=nu*(k^2+q^2)/2`, `e=nu*(q^2-k^2)/2`.

The Rayleigh bound proves

`W'<=2mu(y(t))*W`.

The fixed metric is essential: an eigenvalue estimate for a general nonnormal matrix would not imply this norm bound. The weights `a,c` degenerate at a shell collision, so this is not a uniformly equivalent Euclidean metric through arbitrary gap degenerations.

## 3. Theorem V1: finite window and finite gain

Put `alpha=nu*k^2`, `Gamma0=g*sqrt(E0)`, and

`chi=Gamma0/(nu*k*q)`.

Then

`mu(y(t))<=mu_bar(t):=-d+sqrt(e^2+Gamma0^2*exp(-2alpha*t))`.

Since `d^2-e^2=nu^2*k^2*q^2`, the upper rate is positive exactly while

`Gamma0*exp(-alpha*t)>nu*k*q`.

Thus if `chi<=1`, `W` is nonincreasing at every time. If `chi>1`, all possible positive growth in this metric ends no later than

`t_end=log(chi)/(nu*k^2)`.

This bounds positive SIDE-NORM growth, not the last possible zero crossing or phase reversal of `y`.

For every time,

`|eta(t)|<=|eta(0)|*exp(L)`,

where

`L=int_0^infinity max(mu_bar(t),0)dt<infinity`.

An explicit formula is useful. Let `rho=q/k`, `D=(1+rho^2)/2`, `F=(rho^2-1)/2`, and `S=sqrt(F^2+rho^2*chi^2)`. For `chi>1`,

`L=S-D-D*log(chi)+F*log(chi*(D+F)/(S+F))`.

For `chi<=1`, set `L=0`. Proof: substitute `tau=alpha*t`, then `v=chi*exp(-tau)`, and integrate

`int_1^chi [sqrt(F^2+rho^2*v^2)-D]dv/v`.

This calculation provides a closed form of the norm bound, not the exact nonautonomous propagator.

### Simpler conservative form

Since `sqrt(e^2+s^2)<=e+s`,

`|eta(t)|<=|eta(0)|*exp[X*(1-exp(-alpha*t))-alpha*t]`,

with `X=Gamma0/alpha`. Define

`Psi(X)=0` for `X<=1`, and `Psi(X)=X-1-log(X)` for `X>1`.

Then

`sup_t |eta(t)|<=|eta(0)|*exp(Psi(X))`.

For any specified absolute exit level `eta_exit>0`,

`|eta(0)|*exp(L)<eta_exit`

is a rigorous sufficient condition for never reaching that level. Equivalently any such excursion requires an initial seed at least `eta_exit*exp(-L)`. This does NOT by itself prohibit an eventual sign change of a pump whose magnitude also decays.

### Exact decaying-base refinement

For linearization around the exact single-mode NS orbit `y(t)=U0*exp(-nu*p^2*t)`, use `alpha=nu*p^2` and `Gamma0=g*|U0|`. The corresponding positive-window endpoint is `log(chi)/(nu*p^2)`, and the closed form for `L` is multiplied by `k^2/p^2`. It would be incorrect to apply this faster decay to the FULL nonlinear triad without controlling its pump feedback; V1 instead used the valid full energy envelope.

### Scaling and the 120-degree limit

The triad scaling sends radii to `lambda` times radii, amplitudes to `lambda` times amplitudes, and time to `lambda^-2` times time. Both `chi` and `L` are invariant. For fixed bounded amplitude as both radial gaps close, `g=G*sqrt((q-p)(p-k))` tends to zero. The equal-radius closed triangle is 120 degrees, and its homochiral source vanishes. This cancels this particular triad's amplifier, not every normal perturbation of the whole zero-jitter set.

## 4. Why finite local gain is not a full-network theorem

Overlapping NS triads receive energy from modes outside each selected triple. Their separate `E(t)` need not obey V1's closed energy law. Moreover different triads use different side weights and their outputs recombine coherently. Summing local positive eigenvalues can count the same mode repeatedly. A valid extension needs one common positive network metric, explicit inter-triad fluxes, and bounds uniform in the frequency cutoff. Finitely bounded gains for each separate triple do not establish a summable bound for infinitely many interacting triples.

## 5. Exact smooth birth exposes a logarithmic-rate false alarm

Use the normalized torus Fourier convention `u=sum_k uhat(k) exp(i*k.x)`, so `||u||_2^2=sum_k|uhat(k)|^2`. Define

`C(v)=[Lambda,v cross]v=-v cross Lambda v`,
`A(u)=sum_s ||C(u_s)||_(Hdot^-1/2)^2`,
`J(u)=sum_s int_0^infinity ||C(exp(-tau*Lambda^2)u_s)||_(Hdot^-1/2)^2 dtau`.

All derivatives here are first established for smooth fields. The parent product/heat estimates show that `J` is a continuous nonnegative quartic functional on the critical space. Along full NS,

`J'+nu*A=I`,
`I=sum_s D J_s(u_s)[P_s N(u)]`.

A previous proposed sufficient test uses `I_+/J`. It is usable on intervals separated from zeros of `J`, but zero births can give a nonintegrable quotient on a perfectly smooth trajectory.

Take the actual finite Fourier initial field

`u0=(1,1,0)cos(x1-x2)+(0,0,1)cos(x1+x2)`.

It is real, mean zero and divergence free. Every initial frequency has radius `sqrt(2)`. Both helical sectors are therefore individual curl eigenblocks, and `J(u0)=A(u0)=0`.

Exact full Fourier convolution (with no Galerkin truncation of its output) gives

`N(u0)=(0,0,1)[sin(2x1)+sin(2x2)]`.

Set `a_s=P_s u0`, `h_s=P_s N(u0)` and

`L_s=-(2-sqrt(2))*a_s cross h_s`.

At auxiliary heat time tau, the differential of C in the nonlinear direction is `exp(-6tau)*L_s`. The viscous direction is tangent to the initial shell and contributes zero to this first differential. Consequently the local smooth full PDE solution has

`J(u(t))=j2*t^2+O(t^3)`,
`A(u(t))=12*j2*t^2+O(t^3)`,

where exact symbolic convolution yields

`j2=-sqrt(5)/40-1/32+sqrt(2)/32+23sqrt(10)/1280`.

In particular `j2>13/1280>0`, using `sqrt(5)<9/4`, `sqrt(2)>7/5`, and `sqrt(10)>3`. Its decimal readout is approximately `0.0138646510928150`.

The exact balance now implies

`I=2*j2*t+O(t^2)` and `I/J=2/t+O(1)`.

Thus positive logarithmic-rate action diverges at this smooth birth. This does not refute the old one-way sufficient criterion; it refutes interpreting that divergence alone as a singularity diagnosis or demanding its integrability through every zero birth. The example is even of two-dimensional spatial dependence; no 3D singularity is asserted.

## 6. Theorem V2: globally positive, zero-safe combined energy

Use the full critical energy and dissipation

`K=||Lambda^(1/2)u||_2^2`, `Q=||Lambda^(3/2)u||_2^2`.

The exact helical identity is

`Pcrit=2<Lambda u_+,C(u_-)>-2<Lambda u_-,C(u_+)>`.

Duality plus Young's inequality gives

`Pcrit<=nu*Q/2+2*A/nu`.

Together with `K'/2+nu*Q=Pcrit` and `J'+nu*A=I`, define

`F(u)=J(u)+(nu^2/4)*K(u)`.

Then

`F>=nu^2*K/4>=0`, and

`F'+(nu^3/4)*Q<=I`.

Proof: differentiate F, substitute the two exact balances, and use the stated Young inequality. The A terms cancel: `-nu*A+(nu^2/2)*(2*A/nu)=0`.

Unlike the earlier cubic normal form, F is globally positive for every amplitude. Unlike `J` alone, F is positive at every nonzero smooth velocity, including a zero-jitter one-shell state. This does not prove F decreases: I still has either sign.

Define the zero-safe normalized injection

`Gamma_safe=I_+/[J+nu^2*K/4]`,

with value zero for the identically zero solution. If on `[0,T)`

`B_T=int_0^T Gamma_safe(t)dt<infinity`,

then for each `t<T`, the integrating-factor inequality proves

`F(t)+(nu^3/4)*int_0^t Q(s)ds<=F(0)*exp(B_T)`.

Consequently `sup K<infinity` and `int Q<infinity`. Since

`||u||_6^4<=C||u||_(Hdot^1)^4<=C*K*Q`,

the solution belongs to `L_t^4 L_x^6` and the standard Serrin continuation theorem excludes a finite singular endpoint.

No purity hypothesis, time-varying projection, or small amplitude is assumed in this conditional theorem. The unproved arbitrary-data step is a uniform bound on B_T from the initial data. This is an integrated norm argument, not a claim that local spectra are everywhere stable.

For the smooth birth in Section 5, K(0)>0 and therefore `Gamma_safe=O(t)`, whereas `I/J~2/t`. Thus the new criterion removes an explicitly verified coordinate singularity. On J>0 one has `Gamma_safe<=I_+/J`.

### Bounded source-norm alternative

Let `Phi_s(v)(tau)=Lambda^-1/2 C(exp(-tau Lambda^2)v)` as an element of `L_tau^2 L_x^2`. Then J is the sum of squared Phi norms. Put

`B_response=sum_s ||D Phi_s(u_s)[P_s N(u)]||_(L_tau^2 L_x^2)^2`.

The exact differential gives `|I|<=2sqrt(J)*sqrt(B_response)<=2sqrt(F)*sqrt(B_response)`. Hence

`sqrt(F(t))<=sqrt(F(0))+int_0^t sqrt(B_response(s))ds`.

This provides another birth-safe sufficient condition if the last integral is finite. It is not claimed to have an automatic a priori bound for arbitrary data.

## 7. BRC use and observer limits

`REUSE_APPLIED`: the exact triad radial-gap equations, latent heat Gram, and commutator-action implication.

`REUSE_EXECUTED`: the inherited full Fourier convolution implementation from `NS_四次修正正性与反手性平方完成_20260907.zip`, SHA256 of its complete Python file `ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59`.

`COMPOSE_APPLIED`: a fixed Hermitian side-mode metric with the nonlinear pump energy ledger; the positive latent Gram with the actual critical energy.

Retained labels: ordered radii, helicity, complex phase, pump vs side branch, and in the heat observer the physical output and input heat rates. Passing to W is safe for a norm upper bound because the matrix is Hermitian in that declared metric. Passing to J happens only after coherent same-output, same-rate summation. Neither observer predicts the complete trajectory or its phase.

`NOT_APPLICABLE`: treating positive local Lyapunov rate as a proof of PDE singularity; treating pairwise Gram positivity as automatic cancellation of cross terms; treating separate finite triad budgets as a uniform full-network bound.

## 8. Verification and return frontier

The accompanying checker executes exact symbolic identities for triad energy, weighted side energy and the combined PDE cancellation; an exact finite Fourier computation for j2; 120 quadrature checks of the closed-form gain; and 18 full nonlinear isolated-triad trajectories compared to the analytic gain envelope. Numerical trajectories are regressions, not proof of the analytic lemmas or of the full PDE.

Observed regression maximum energy-ledger error: about `3.14e-9`; maximum quadrature discrepancy: about `1.43e-14`. All tests passed. No independent review or formalization is claimed.

The smallest unresolved network unit is now: bound the positive injection into the common nondegenerate energy F, rather than count macro flips or normalize only by J. A candidate proof must control overlapping comparable-frequency interactions and the injection I without assuming beforehand that the full solution is regular. The isolated V1 budget supplies a local diagnostic and a finite-source model, not that missing network estimate.

## 9. References and source boundaries

- Waleffe, F. (1992), *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4, 350-363, DOI `10.1063/1.858309`. Primary archival record: https://ntrs.nasa.gov/citations/19920038608 . This supplies established helical triad context, not validation of this note's new calculations.
- Zhang, Z., Li, J., Yao, Z. (2018), *A remark on the global regularity criterion for the 3D Navier-Stokes equations based on end-point Prodi-Serrin conditions*, DOI `10.1016/j.aml.2018.04.003`, introduction states the classical criterion `2/p+3/q=1`, `q>3`. https://doi.org/10.1016/j.aml.2018.04.003 . Only that established continuation interface is used here.
- Exact project-local parents listed in Section 0, read at the global authority snapshot above. Their TESTING status is retained.
