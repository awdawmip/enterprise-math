# R063 Stage 2 — BRC Downstream Compatibility Diagram

Status: `CLASSIFIED / DOWNSTREAM ONLY`

## 1. Frozen R062 multiplication remains additive-trace concatenation

R062 freezes

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`

on the component-typed path skeleton. Its multiplication is typed **path concatenation**, extended distributively. Consequently it projects to the frozen R061 additive trace law

`T_{a,b} * T_{c,d}=T_{a+c,b+d}`.

Stage 2 norm-root multiplication instead uses the orientation-conditioned trace law

`T_r odot_i T_s=T_{r star_i s}`.

Therefore the pre-existing R062 multiplication is not silently reinterpreted as Stage 2 root multiplication.

## 2. Noncommuting N-multiplicity square for root multiplication

For `A=B=2`, `r=s=(1,1)`:

`N_BRC(r)=2`, `N_BRC(s)=2`,

while

`N_BRC(r star_i s)=N_BRC(0,2)=1`.

Thus

`1 != 2*2`.

So there is no multiplicative homomorphism law

`N_BRC(r star_i s)=N_BRC(r)N_BRC(s)`.

The `5 x 5` witness strengthens the separation:

`N_BRC(2,1)^2 = 3^2 = 9`,

but

`N_BRC(3,4)=35`.

Hence N-valued native path multiplicity is downstream information about the target trace fiber, not Gaussian factor-pair provenance multiplicity.

## 3. Boolean support survives only as a coarse shadow

Once an oriented product root/trace has already been fixed and its native path fiber is nonempty,

`BOOLEAN_BRC(target)=1`.

For two existing source path fibers,

`1 AND 1 = 1`.

This gives a coarse positivity/support compatibility:

`beta(N_BRC(target)) = beta(N_BRC(source A)) AND beta(N_BRC(source B)) = 1`

on the supported-root domain.

This does **not** select a Gaussian root, choose between `(0,2)` and `(2,0)`, construct a path representative, or prove N-multiplicity multiplication. Boolean BRC is applied only after the root/trace target exists.

## 4. Exact surviving diagram

For fixed orientation and roots `r,s`:

`Prov/SRoot/URoot product`

`        |`

`        v`

`oriented target trace T_{r star_i s}`

`        | pathify as whole fiber`

`        v`

`Path_E(r star_i s)`

`        | cardinality / augmentation`

`        v`

`N_BRC = binom(A+B,A) for target components (A,B)`

`        | positivity beta`

`        v`

`Boolean BRC = 1`.

The vertical arrows are forgetful/readout maps. There is no horizontal Stage 2 path multiplication inserted between source path fibers and the target fiber.

## 5. Classification

`R062_PATH_FORMAL_MULTIPLICATION = FROZEN_ADDITIVE_TRACE_CONCATENATION`.

`N_BRC_ROOT_PRODUCT_MULTIPLICATIVITY = FALSE`.

`BOOLEAN_BRC_SUPPORTED_TARGET_POSITIVITY = EXACT_DOWNSTREAM_SHADOW`.

`BRC_USED_TO_DISCOVER_ROOT_OR_ORIENTATION = false`.
