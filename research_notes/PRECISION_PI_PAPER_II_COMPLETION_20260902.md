# Precision-pi paper II: completion and proof ledger

Researcher-ID: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Date: `2026-09-02`

Paper title:

> Four-slice, six-line precision-pi structure II: tetrahedral residuals, affine two-torsion, and double-Pell shells

Chinese title:

> 四切片六线族载体上的精度 π 结构（二）：四面体残差、仿射二扭结与双 Pell 壳层

## 1. Manuscript boundary

The manuscript is organized in three proof levels.

1. **Unconditional finite layer.** Exact `K4` incidence, FCC carrier angles, integral residual classification, real completion, tetrahedral covariance, mod-two cocycle, Pell identities, arithmetic certificates, finite majorization arithmetic, positive reciprocal monotonicity, and geometric tail estimates.
2. **Classical analytic input.** The Ramanujan-CM identity for the `N=58` series is not derived from the finite carrier or from Pell arithmetic. It is stated explicitly as an external input.
3. **Conditional precision theorem.** Given the classical identity and positivity, reciprocal partial sums decrease strictly to `pi` from above, with an explicit ratio-based tail certificate.

The paper therefore does not claim that the finite tetrahedral carrier proves the classical CM identity, and it does not identify the carrier's six lines with any unformalized native six-axis ontology.

## 2. Strictly accepted residual stack

Branch: `formalization/precision-pi-paper-ii-kernel-v1`

PR: `#1125`

Accepted layers:

- minimal carrier and parity kernel: run `33635733994`;
- exact integral quotient `ZeroResidualQuotient ≃ ((Z × Z) × Bool)`: run `33638242117`;
- real completion and torsion loss: run `33639326606`;
- exact `K4` covariance: run `33641687121`;
- adjacent-transposition cocycle, Coxeter relations, hidden double swap, and absence of an invariant additive torsion retraction: run `33657478048`.

The last run compiled all five modules with `--wfail` and passed the static rejection gate for `sorry`, `admit`, and custom axioms.

## 3. Arithmetic and precision stack

Branch: `formalization/precision-pi-paper-ii-v3`

PR: `#1126`

The branch contains the finite arithmetic side of the paper: Smith certificates, rational splitting, residual metric, square half-trace algebra, double-Pell fusion, the `P=99` and `N=58` certificates, finite generating lift, positive reciprocal acceleration, and geometric tail bounds. At manuscript freeze, the final aggregate `lake build --wfail -KCI EnterpriseMath` repair cycle was still being completed; the manuscript and validation report must quote the actual terminal run rather than infer status from the PR badge.

## 4. Main mathematical statements

- `E0 / delta(V0)` has the constructive residual code `Z^2 x C2`.
- Over coefficients in which `2` is invertible, the parity obstruction disappears and only the two-dimensional free residual remains.
- The torsion line is invariant under the tetrahedral action, but no additive torsion retraction is invariant under the adjacent transpositions; hence the displayed `Z^2 x C2` splitting is not `S4`-equivariant.
- Modulo two, the complete residual admits a human-level affine-function interpretation on `F2^2`; the six nonconstant affine functions recover the six edges, and addition of the nonzero constant function exchanges opposite edges. This coordinate-free interpretation is the next formalization target.
- A square half-trace `P^2` forces the paired shell factorization `P^4 - 1 = (P^2 - 1)(P^2 + 1)`.
- At `P=99`, the positive and negative Pell equations recover the integral skeleton behind the constants `396`, `9801`, `26390`, and `1103`.

## 5. Next exact target

Formalize the affine-function model

`ResidualF2 ≃ Aff(F2^2, F2)`

and compare its translation character with the signed double-Pell shell selection, without promoting the comparison to a CM theorem until the required analytic bridge is proved.
