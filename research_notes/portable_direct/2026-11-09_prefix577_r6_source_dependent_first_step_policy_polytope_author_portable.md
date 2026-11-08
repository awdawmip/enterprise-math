# BRC-X6: the exact 12-dimensional source-dependent first-step cancellation polytope

Date: 2026-11-09 (Asia/Hong_Kong). Status: `AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED`. Scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. The original 96-port model, six original labeled actions and nine frozen roots `0,±e1,±e2,±e3,±e4` are unchanged.

## Statement and new certificate

The signed starting-port law `ell2=e6−e7−e28+e29` was established in preceding author research `f20a2c42e0c8db2435215b3cf1a212e7e507644e`. Now allow the **first action law to depend on the hidden initial native port**. Write
```text
u_i = Pr(action i | start port 6)
v_i = Pr(action i | start port 7)
s_i = Pr(action i | start port 28)
t_i = Pr(action i | start port 29)
```
for native actions `a0=(slot0,newbit0), a1=(slot0,newbit1), a2=(slot1,newbit0), a3=(slot1,newbit1), a4=(slot2,newbit0), a5=(slot2,newbit1)`, i=0,...,5. Each of `u,v,s,t` is an arbitrary nonnegative six-component probability vector, with row sum 1. Keep the **full seven-component ordered output** `W=(R1,...,R6,K)`, where K is the event gate rather than another spatial axis, plus the exact native target port.

**Theorem (exact target/output one-step annihilator).** For every one of the nine roots, the signed joint distribution of `(native target, W)` after one action is zero if and only if:
```text
u0 − v0 − s2 + t2 = 0       (target 8)
u1 − s3           = 0       (target 9, gate 0)
−v1 + t3          = 0       (target 9, gate 1)
−s4 + t4          = 0       (target 16)
−s5 + t5          = 0       (target 17)
u2 − v2           = 0       (target 32)
u3 − v3           = 0       (target 33)
u4 − v4 − s0 + t0 = 0       (target 40)
u5 − v5 − s1 + t1 = 0       (target 41)
```
The native reward associated with each atom may change with root, but **all nine linear coefficient equations are identical for all nine roots**. These are exactly the full target/output cancellation equations, rather than assumptions about coarser state-language equivalence.

Together with the four probability normalizations `Σ_i u_i=Σ_i v_i=Σ_i s_i=Σ_i t_i=1`, the exact rank of the 13 linear constraints in 24 variables is **12**. One dependency is the total signed conservation equation. The all-positive policy `u_i=v_i=s_i=t_i=1/6` is feasible. Hence the nonnegative source-dependent cancellation polytope has **relative affine dimension 12**. It contains the previously determined four-dimensional source-blind policy simplex as a subpolytope.

Full target/output signed cancellation at the first action implies `F6+F29=F7+F28` for **all later ordered complete seven-observation words**, with any common continuation kernel acting on the same next state/history. Later interventions can be arbitrary and state/history-dependent, provided they do not independently retain hidden initial-port provenance. The nine equalities characterize this strong one-step certificate; a coarser future observer could admit additional coincidences.

## Deterministic policy census and witness

There are `6^4=1296` pure first-step controllers choosing one action independently at each of the four signed source ports. Exactly **38** satisfy all nine integer equations for each of the nine roots. For instance the action tuple `(a0,a1,a2,a3)` on ports `(6,7,28,29)` gives paired native atoms `port6/a0=port28/a2` at target 8 and `port7/a1=port29/a3` at target 9 with gate 1, with each pair carrying opposite signed masses. This is a nontrivial source-dependent controller, not representable by a single common action distribution across all four starts.

Every one of these 38 deterministic solutions remains a vertex of the policy subpolytope, since it was a vertex of the ambient product of four action simplices. Fractional-vertex completeness is an open separate question.

## Exact proof and reproducibility

The original native kernel gives precisely nine target/output atoms for the 24 edge choices from the signed support. Grouping them proves the nine explicit equations, with their necessity and sufficiency immediate by linear independence of distinct target/output atoms. For every root the nine unnormalized signed kernel rows have exact rational rank 9; after adding four normalization rows, exact rational elimination gives rank 12, confirmed independently modulo both `1000000007` and `998244353`. Exhaustive exact integer enumeration compares the nine equations with the separately computed direct signed target/output distribution for all `9×1296=11664` root/controller combinations. Exactly 38 pure controllers survive for each root.

The complete local self-contained portable package includes the original frozen native kernel, original root-zero 576-edge snapshot, `verify_source_dependent_first_step_polytope.py`, `SOURCE_DEPENDENT_FIRST_STEP_CERTIFICATE.json` (SHA-256 `92f6434b6f2a45dbceb2612ac7baec774d37f7c9b7f5b79c9faa0f3a6d5651d4`), theorem narrative and manifest. All exact checks passed. BRC residual/provenance scope: source-port-specific action laws, signed masses, native target, complete six reward axes, gate and subsequent ordered observations. No sign-erasing positive quotient or native spatial-axis collapse is used.

The new contribution is the complete source-dependent one-step cancellation **polytope, dimension, nine equations, 38-point pure-policy census and exact source-dependent witness**. It is distinct from the prior signed-port identities/49–50 predictive ranks and from the immediately preceding source-blind first-step balance simplex (GitHub author commit `4be2072ee6fd5ea81e67cb5a241b55f696b2a741`).

## Native Source/UR status and next math frontier

Original D25 retains missing native H0/B0 divided-power module, `[X]U mod p²`, semilinear Frobenius/normalization, `κ` and `Δ_p−R_p` comparison and original CM experiment `NOT_RUN`; D24's original Result/Driver Review are terminal. The required exact original four-file UR V2 bundle is 94,687 bytes with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, still unrecovered. This author note makes no native CLAIM, Source task checkpoint, Result or independent review. Formal work requires verified original session capability and winning canonical claim.

Next distinct mathematical unit: characterize potentially fractional extreme first-step policies of this 12D polytope, or derive their complete finite parametrization; preserve the present exact nine-equation operator interface and frozen kernel.
