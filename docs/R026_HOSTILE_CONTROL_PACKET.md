# R026 Hostile-Control Counterexample Packet

Status: `EXECUTABLE_CHECKED / NEGATIVE-BOUNDARY PACKET / NOT CANONICAL`

Purpose: prevent any collapse policy from winning by definition. Every positive-looking pattern is paired with an observable on which it should fail or become conditional.

## Minimal semantic kill test — Anchor Necessity

Use residual `r=1/4` at anchors `a1=0`, `a2=10`. The absolute states are `1/4` and `41/4`. Under the permitted future observable `F(x)=x^2`, the futures are `1/16` and `1681/16`. Therefore equal residual does **not** imply equal future. Residual-only state is unsound unless the future language factorizes through the residual coordinate.

## Quantitative hostile controls

| Control | Winner / failure | Evidence |
|---|---|---|
| Non-midpoint stochastic rounding | 50/50 is biased; distance-weighted is nearly unbiased | constant `x=0.37`: uniform bias `-0.026621933`, distance-weighted bias `-1.251221e-05` |
| Repeated coarse summation | residual carry repairs drift but at extra state/work | 1000×0.01: DOWN error `10`, NEAREST `5.625`, stochastic-unbiased `0.00170898438`, residual `1.687539e-13` |
| Residual precision boundary | residual-only correction fails when residual is quantized away | ill-conditioned exact-residual error `0` vs quantized-residual `0.00141662446` |
| Multigrid state restriction | coarse state is not a substitute for residual equation | residual correction rel-L2 `7.309253e-08` vs state-only `0.0427306612` |
| Far convex projection | feasible endpoint can still violate optimization ground truth | squared-distance objective gap `1.28` |
| Long-horizon oscillator | local rounding semantics do not guarantee energy/phase behavior | combined error: DOWN `2.99806348`, NEAREST `0.331802127`, unbiased stochastic `0.263640293`, residual-feedback `0.0172923356` |
| Collision conservation | coordinate-wise unbiased expectation is not pathwise nonlinear conservation | mean combined bias/error `0.00380310059`, mean absolute invariant violation `0.133578491` |
| Rasterization far endpoint | FAR maximizes local endpoint error | classified `FAILS_CONVERGENCE_OR_INVARIANT` |

## Negative boundary frozen

- `FAR_PROJECTION` is retained as an adversarial control, not a general computational policy.
- `UNIFORM_ENDPOINT_RANDOM` must not be called unbiased away from a basin midpoint.
- `RESIDUAL_COLLAPSE` is conditional: residual precision and operator/anchor context are part of the correctness contract.
- `ANCHOR_PLUS_RESIDUAL` is exact but not a resource win unless a separate compression/factorization argument exists.
- `BRC_SUPPORT` is exact only for its declared set/result-support observable; scalar numerical objectives do not inherit that guarantee.
