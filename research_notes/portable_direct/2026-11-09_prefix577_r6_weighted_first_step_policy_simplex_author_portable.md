# BRC-X6: the exact first-step control-policy simplex preserving a signed all-word port identity

Date: 2026-11-09 (Asia/Hong_Kong). Original scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: `AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED`. Portable author result on the original 96-port, 576-labeled-edge machine, with nine frozen roots `0,±e1,±e2,±e3,±e4`. No native Source CLAIM, Result, review, or CM experiment is asserted.

## Statement and typed observation

Six native action labels in original order are `a0=(slot0,newbit0)`, `a1=(slot0,newbit1)`, `a2=(slot1,newbit0)`, `a3=(slot1,newbit1)`, `a4=(slot2,newbit0)`, `a5=(slot2,newbit1)`. Output is the *ordered* complete seven-field vector `(R1,R2,R3,R4,R5,R6,K)` (six original spatial reward axes, plus an independent gate bit), together with the native target port.

For a signed initial port vector `ell`, let `D_ell(a)=Σ_p ell[p] δ_(target(p,a), output(p,a))`. Reuse the previously proved signed vectors `ell1=e28−e29−e30+e31` and `ell2=e6−e7−e28+e29` (prior provenance: `f20a2c42e0c8db2435215b3cf1a212e7e507644e`).

**Exact new action resolution:** For all nine roots and each original labeled action,
```text
D_ell1(a_i) = 0,                           i=0,1,2,3,4,5
D_ell2(a_i) = 0,                           i=0,2,4,5
D_ell2(a1)  = -D_ell2(a3)
             = δ_(9,(v_r,K=0)) − δ_(9,(v_r,K=1))  ≠ 0 .
```
The complete six-coordinate reward `v_r` for the roots in original source order is
```text
r:       0       -e1     +e1      -e2      +e2     -e3       +e3      -e4      +e4
v_r:    100000  100000  000000   100000   100000   101000    100000   100000   100000
```
Here the six digits are the six reward coordinates, never a quotient of spatial axes.

**Theorem (complete policy classification).** Let the first action be sampled from any common probability law `λ=(λ0,...,λ5)` with `λ_i≥0` and `Σλ_i=1`, independent of which of the four initial native source ports is used. It may be followed by an *arbitrary common continuation* that depends on subsequent native target states and observed history but does not retain hidden initial-port provenance.

Then `F6+F29=F7+F28` as an equality of probability laws for **every length of the complete ordered seven-output word** holds if and only if
```text
λ1 = λ3.
```
In fact, the signed first-step joint target/output measure is exactly
```text
D_ell2(λ)=(λ1−λ3)[δ_(9,(v_r,0))−δ_(9,(v_r,1))].
```
When the weights balance, the signed measure is annihilated at time one, so *no balancing is required at later times* for this initial signed-port law, even under subsequent fully specified native action labels. When they do not balance, the one-step outputs `(v_r,0)` and `(v_r,1)` provide a sharp witness with signed differences `+(λ1−λ3)` and `−(λ1−λ3)`. The first identity `F28+F31=F29+F30` survives every common first-step law without a balancing constraint.

The exact set of preserving stochastic first-step policies is the **four-dimensional simplex**
```text
S={λ∈R^6_{≥0}: Σ λ_i=1, λ1=λ3}
  =conv(δ_a0, δ_a2, δ_a4, δ_a5, (δ_a1+δ_a3)/2).
```
For a *uniform* distribution on a nonempty action subset `A`, the identity holds exactly when `a1∈A ⇔ a3∈A`. Thus exactly **31 of the 63** nonempty subsets preserve it, while **32 do not**. This simultaneously explains why the passive / newbit policies preserve the signed relation while an equal-newbit slot0 intervention can break it.

## Proof and verification

The exact native transition kernel gives the six displayed integer signed measures. Linear combination in the first-step weights proves the formula. Its two atoms differ by the original gate bit, hence it vanishes iff `λ1=λ3`. Signed-measure equality propagates through every **common** future continuation kernel on target and output, irrespective of its permitted action choices. The simplex has barycentric coordinates `λ0,λ2,λ4,λ5,2λ1`. The uniform-subset count is `2^4·2−1=31` after requiring inclusion of labels 1 and 3 simultaneously or exclusion of both.

The exact verifier uses the original frozen native Python kernel and source 576-edge root-zero `(source,target,gate,R5,R6)` snapshot. It verifies `ell1` for all six actions and `ell2` for all six action-resolved target/output measures in each root, and exhaustively checks all `9×63=567` nonempty action-subset cases. All integer assertions passed. Portable certificate `WEIGHTED_ACTION_BALANCE_CERTIFICATE.json` has SHA-256 `189df8c1421b764fbfbdce3038f9c4cf33bed1a772f16de383e7cfe160238420`. The self-contained six-file local research package also records the kernel/snapshot hashes, verifier and full theorem narrative.

BRC carrier: signed native port provenance; preserved observations: all six axis rewards, gate, target, ordered future word, selected action identities. Permitted reduction: only the proved target/output signed cancellation. No positive-mass argument, quotient assertion, Source admission or original-class CM conclusion is needed.

## Unfinished parent frontier and provenance

Original D25 native H0/B0 divided-power module, `[X]U mod p²`, source Frobenius normalization and `Δ_p−R_p` correspondence remain pending. D24 terminal Result/review are not reopened. The exact original 94,687-byte UR V2 bundle with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` remains to be recovered byte-for-byte. The preceding signed-port author work at commit `f20a2c42...` retains its original contribution attribution; this note contributes the *complete weighted first-step policy classification and simplex*, not those earlier identities.

The 2026-11-09 Source recovery probe had no verified private own-session execution capability, so formal task publication requires independent current Source authority and canonical claim. Next distinct portable question: classify first-step policies that explicitly depend on hidden native source-port identity, and quantify the retained BRC provenance residual rather than silently treating them as state-blind.
