# Reducer results — valley-band benchmark ablation

## Reduced correctness witnesses

1. **Recurrence-sign negative control.** Starting from `C^2 - A*B = T`, replacing
   the derived cross-term sign in the second transition breaks the invariant.
   `verify.py` reports `recurrence_sign_invariant_failure=true`.
2. **Band-root negative control.** Replacing the exact root
   `(A*t+C)/x (mod N)` by that root plus one fails the required congruence and is
   rejected before GF(2) insertion. The checker reports
   `invalid_band_root_rejected=true`.
3. **Raw-count/rank negative control.** Two identical parity-zero relations give
   raw count 2, rank 0 and dependencies 2. This is the minimal witness that raw
   relation count cannot replace rank-aware accounting.
4. **Post-hoc selection negative control.** Choosing a threshold after inspecting
   outcomes is classified `INVALID_BY_FROZEN_CONFIG`.

## Reduced performance failures

- The smallest complete comparison unit is R96-00/01/02 with both point paths
  and three repeats. All 18 runs completed; paired mathematical and rank digests
  agree. Closed point is locally 1.68–1.71 times slower.
- The smallest threshold grid witness is one R96-00 run at each frozen threshold
  32/64/128/256/512. All five timed out with full/rank 3/3, so none may be
  selected as best.
- The smallest LP cost witness is R96-00, threshold 256, one run each for none,
  SLP and DLP. All timed out. None produced 30 rank while SLP and DLP produced 3;
  DLP accumulated 223 edges and zero cycles. This reduces the observed failure
  to cofactor-classification cost, not relation-root or matrix correctness.
- Timeout granularity is reduced to threshold 256: one in-flight band made wall
  time 24.5933169 seconds under a nominal 20-second check-between-states limit.
- The adaptive holdout opened zero bands and still timed out because SLP point
  classification dominated. It reached rank 102, five dependencies and no
  factor against factor-base dimension 108 and target 116.
- All QS context rows and 49 total planned rows are explicitly
  `NOT_RUN_BUDGET`; none was imputed, dropped or converted to a null success.

## Terminal reducer classification

`INCONCLUSIVE_AFTER_VALIDATED_PARTIAL_MATRIX`

The checker and implementation equivalence are closed locally. The full
threshold-by-instance-by-repeat surface, completed DLP cycle evidence, executed
QS context, and factorization success/crossover claims remain open.

Reproduce the reducer inputs with:

```powershell
python experiments\valley_band_benchmark\corpus.py --check
python experiments\valley_band_benchmark\verify.py
python experiments\valley_band_benchmark\aggregate.py
```
