# CBRC F7 Driver r436 — exact finite-cube minimax at radius eight

Date: 2026-11-21 (+08:00). New auxiliary proof/certificate: Driver logical line `EM-DVR-DEBB5E`. Original F7 matrix, model and frozen Result: researcher `EM-CBRCF7-83A1D4`. This is a **finite-domain, exact rational result**, distinct from a Native Review.

## Theorem and domain

Retain the original F7 matrix
```
A = [[ 2,-2,-1, 2],
     [ 1,-1,-1, 2],
     [-1, 2, 2,-2],
     [-1, 2, 1,-1]]
```
and let `q: Z² -> R_{>=0}` obey `q(0,0)=0`, `q(n,m)=q(-n,m)` (the F7 `J` parity), `q(t,0)=1` for all nonzero integers `t`, `q(n,m)>=1/2` on all nonzero pairs, and exact marks `q(2,1)=q(-1,-1)=1/2`.

For `z=(n,m,p,l)`, let
```
D_q(z) = q((Az)[0],(Az)[1]) + q((Az)[2],(Az)[3])
       - q(n,m) - q(p,l).
E_B = inf_{admissible q} max_{z in [-B,B]^4 ∩ Z^4} |D_q(z)|.
```

**Exact theorem:** for every integer `1 <= B <= 8`,

```
                        E_B = 1/2.
```

This uses the full F7 exact mark/parity/positivity hypotheses but a **truncated input cube**. The infinite-input infimum `E_∞` is still open between `1/2` and r435's global construction upper bound `4/7`.

## Proof of the lower bound

The fixed witness `z0=(1,-1,0,0)` gives `Az0=(4,2,-3,-3)`. `J`-evenness and the second exact mark force `q(1,-1)=1/2`. Both output pairs are nonzero, hence `D_q(z0) >= 1/2 + 1/2 - 1/2 = 1/2` for every admissible `q`. This witness belongs to every stated input cube.

## Constructive upper bound and full integer certificate

The self-contained static certificate is at:
`research_checks/CBRC_F7_R436_B8_FINITE_CUBE_HALF_CERT_20261121.py`, commit `f62febc5777c2b78f3b5edf3528f7f540000c88a`, blob `33ee4867cfcb8321dcc7a304bcaa976fb8ebf088`.

It defines one explicit `q` globally using denominator 40: origin 0; nonzero old-axis pairs 40/40; the two marked `J` orbits 20/40; all other off-axis pairs default 20/40, except for a fully enumerated table of **524** distinct `(|n|,signed m)` pairs, where integer values in [21,40]/40 are fixed. Thus `q` is a total function on `Z²`, exactly `J`-even, and has the required nonzero positivity floor.

An exact, standard-library Python checker enumerates **all 17⁴ = 83,521** input integer four-tuples with every coordinate between -8 and 8 inclusive, calculating all four scalar terms as integers `40q`. The observed exact certificate is:

- exceptional `J`-orbits: 524; all default/exceptional marked invariants checked;
- exact `max |40 D_q| = 20`, with **3,176** input tuples attaining that absolute maximum;
- witness `D_q(1,-1,0,0) = 20/40`.

The same fixed GitHub checker bytes were **independently recomputed from the remote commit in a second implementation**, yielding 83,521 inputs, 524 exceptions, exact maximum 20, 3,176 equality points and zero violations. Therefore `E_8 <= 1/2`, and its restriction certifies all smaller cubes. Combine with the analytic lower bound.

A finite linear program over **1,374** free pair classes was used only to *discover* the candidate. The theorem relies exclusively on the published static rational table, the explicit analytic witness and the all-integer complete enumeration. LP floating-point optimality or numerical tolerances are not proof premises.

## Scope and research next step

r435 established `4/7` as the sharp defect within a **signed-angular scale-homogeneous class**, using a six-witness inequality that includes magnitude-46 coordinates and same-ray cancellation. The unrestricted scalar class may vary with integer scale. This r436 finite result proves that no proposed universal lower bound larger than `1/2` can be certified solely from all input inequalities with `|z_i|<=8`, because the explicit counter-candidate satisfies them all.

Next discriminate `E_∞=1/2` versus `E_∞>1/2`: search larger exact finite certificates/dual witnesses or a scale-dependent global construction, preserving positivity and both marks. Do not generalize finite cube coverage to all integer inputs.

Formal state remains unchanged: original frozen `RR-AA38973D56330E59D315` has independent SHA256 declaration discrepancies; the original first Native Review remains `FAILED/NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` ([engineering issue #2874](https://github.com/awdawmip/enterprise-math/issues/2874)). This auxiliary result neither revises the original Result nor asserts new Review, CLAIM, Task completion or parent closure.