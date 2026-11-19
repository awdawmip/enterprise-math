# EC49FUC-S — Sharp minimax theorem for a finite-width clipping detector

Date: 2026-11-20. Status: **AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

This is a same-line extension of [EC49FUC observer/minimax paper (PR #2819)](https://github.com/awdawmip/enterprise-math/pull/2819), using the frozen BRC16943 scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Price-prior postprocessing only, not a new native Bellman computation.

## Theorem: worst-case one-sample discrimination for every finite-width top bin

At the previously established one-sided clipping interface take
```
m = 1469/64,  L = 951/1280,  U = 3/4,  W = U-L = 9/1280,
E = 1048576/18958647,   epsilon in (-infinity,E].
```
The conditional continuous law is `nu_epsilon` with density proportional to `1-epsilon*m*z` on `[L,U]`. The two phase laws are `mu_minus=nu_epsilon` and `mu_plus=(1-q_epsilon)nu_epsilon + q_epsilon delta_U`; the exact `q_epsilon` is in EC49FUB and EC49FUC.

Let the **single observed bit** be `Y_delta=1_{Z>=U-delta}`, where the instrument resolution `0<=delta<=W` is fixed and known. Distinguishing the left/right weak-limit phases with equal priors and *unknown common* admissible epsilon has exact minimax risk
```
inf_{tests based only on Y_delta} sup_{epsilon<=E}
  (P_{minus,epsilon}(decide plus)+P_{plus,epsilon}(decide minus))/2

 = [1 - V_E(delta)]/2,

V_epsilon(delta) = q_epsilon*(1-rho_epsilon(delta)),
rho_epsilon(delta)
   = delta*(1-epsilon*m*(U-delta/2)) /
     (W*(1-epsilon*m*(L+U)/2)).
```

For every `0<=delta<W`, `V_epsilon(delta)` is **strictly decreasing** in `epsilon` over the entire real admissible half-line. The universal minimax rule is the fixed one-bit rule **decide plus iff `Y_delta=1`**, independent of epsilon. At `delta=W`, the instrument is constant, `V=0` and minimax risk is exactly `1/2`. No finite epsilon is excluded except those above the original positivity endpoint E.

In the special exact rational instance `delta=W/4`,
```
rho_E = 1547881/6614596,
V_E   = 16772065588485375/53791779891391364,
minimax risk =
       37019714302905989/107583559782782728
       ≈ 0.34410196481368416.
```
For delta=0, this reduces to the exact-atom one-sample minimax result of EC49FUC. For delta>0 it gives the exact detector-induced loss without presuming the top-atom port is individually resolved.

## Proof of global strict monotonicity (not a sampling argument)

Write `A_e,B_e` for the inherited continuous and clipped masses at the interface. Let `C_e(delta)` be the continuous mass in the *lower* observed bin `[L,U-delta)`. For `delta<W`, all three masses are positive for every finite `epsilon<=E`, and
```
V_e = B_e*C_e / ((A_e+B_e)*A_e).
```
Each factor is a positive affine function of `e=epsilon`: `X_e = X_0*(1-e*mu_X)`. The exact price-observer means are
```
mu_A = 2807259/163840,
mu_B = 41217719/2359296,
mu_T = 45529434409/2630615040  (T=A+B),
mu_C = m*( (L+U)/2-delta/2 ).
```
They obey `mu_B>mu_T>mu_A>=mu_C>=mL>0`. For `f_e(x)=x/(1-e*x)`, taking a logarithmic derivative gives exactly
```
d(log V_e)/de = -(f_e(mu_B)-f_e(mu_T))
                 +(f_e(mu_A)-f_e(mu_C)).
```

The first difference is strictly positive. For `delta>0`, the ratio of differences is
```
[f_e(mu_B)-f_e(mu_T)]/[f_e(mu_A)-f_e(mu_C)]
   = (mu_B-mu_T)/(mu_A-mu_C) *
     ((1-e*mu_A)*(1-e*mu_C))/
     ((1-e*mu_B)*(1-e*mu_T)).
```
Because `mu_A-mu_C=m*delta/2<=mW/2`,
```
(mu_B-mu_T)/(mu_A-mu_C)
   >= (mu_B-mu_T)/(mW/2)
   = 3965947/1965522.
```

For positive numbers `x>y` and `e<1/x`, one has
`(1-e*x)/(1-e*y) <= x/y`: for `e<=0` by cross multiplication, and for `0<=e<1/x` because the left side is at most 1. Apply this to `(mu_B,mu_A)` and `(mu_T,mu_C)`. All denominators are strictly positive for the admitted parameter half-line, so
```
((1-e*mu_B)*(1-e*mu_T))/
((1-e*mu_A)*(1-e*mu_C))
    <= (mu_B*mu_T)/(mu_A*mu_C)
    <= (mu_B*mu_T)/(mu_A*mL)
    = 9383097168495465355/9067439094875650944.
```
The exact inequality
```
3965947/1965522
    - 9383097168495465355/9067439094875650944
  = 8912797192394315189/9067439094875650944 > 0
```
proves that the negative term in the logarithmic derivative strictly dominates the positive term. Hence `V'_e<0` on `delta in (0,W)`. At `delta=0`, `V=q_e` and `q'_e<0` by EC49FUB, completing `0<=delta<W`. At `delta=W`, `C_e=0` and `V=0`.

For any fixed epsilon, the observed top-bin probabilities satisfy `P_plus(Y=1)-P_minus(Y=1)=V_e>=0`; therefore the likelihood-ratio optimal equal-prior decision is always "plus iff top bin", with Bayes risk `(1-V_e)/2`. It is the *same test for every epsilon*. Strict decrease shows its worst-case risk occurs at `epsilon=E`. Conversely, choosing `epsilon=E` gives a simple-versus-simple subproblem whose Bayes risk lower-bounds every nuisance-robust test. This proves the exact minimax equality. QED.

## Verification and scientific scope

All constants and the strict rational comparison were checked with exact Python `Fraction` arithmetic, including `rho_E(W/4)` and `V_E(W/4)`. The proof covers **all real epsilon<=E** and every real detector width `0<=delta<=W`. The numerical instance is a regression/witness, not the proof. Inherited optimality and branch geometry remain PARENT_DEPENDENT and NOT_REVIEWED. No independence beyond one trial is needed. Multi-trial finite-bin minimax with the *same unknown epsilon* is a distinct open question, because its optimal threshold can depend on binomial count and nuisance parameter.

For BRC-style residual-fidelity interpretation, the deterministic top-bin readout collapses mass `rho_epsilon(delta)` of the continuous branch onto the clipped port; this is exactly the observer quotient's `q*rho` lost total variation. This does not assert that a one-bit readout is sufficient for future native six-axis Cell operations.

**Next:** solve the multi-trial binomial composite-hypothesis minimax problem at finite detector width, or independently reconstruct frozen native Bellman `z<11/16` switching branches.
