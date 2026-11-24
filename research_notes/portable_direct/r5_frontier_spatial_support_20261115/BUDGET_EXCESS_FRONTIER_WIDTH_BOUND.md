# R5: frontier rank diversity bounded by excess center budget

Date: 2026-11-15. Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Context: derived strictly increasing integer 1D indexed-center radius-two observer of 954 frozen events. This lemma also holds for arbitrary ordered feasible consecutive-center path languages, and is **not** a native-X6 theorem.

## Theorem (feasible rank slack)

Let `m0` be the *minimum* number of indexed centers needed for radius-`rho` coverage of all events of a fixed integer coordinate instance. Suppose `K>=m0`. For each candidate center index `i`, define `a_i` as the minimum number of centers strictly before `i` among feasible selections containing `i`, and `b_i` as the analogous minimum strictly after `i`. Both minima are computed on the acyclic graph of feasible consecutive-center arcs; paths can be glued at the common center `i`. Define `m_i=a_i+1+b_i >= m0`.

Any feasible `K`-center solution containing `i` at zero-based rank `r` must have at least `a_i` preceding centers and at least `b_i` following centers. Thus
```
a_i <= r <= K-1-b_i,
number of possible ranks of i <= max(0,K-a_i-b_i)
                           = max(0,K-m_i+1)
                           <= K-m0+1.
```

For the old optimizer path DAG, let `d_K(j)` be the greatest rank multiplicity at a single original event index among active crossing-arc tails at cutoff `j`; let `W_K(j)` be its total rank-labeled crossing-tail frontier width. Reusing the independently proved sharp geometric bound on distinct crossing tails, `|T_j|<=2*rho+1`, yields the universal parameterized bound

```
W_K(j) <= (2*rho+1)*(K-m0+1).
For radius two, W_K(j) <= 5*(K-m0+1).
```

Consequently the existing Pareto antichain bound `A(j,h) <= (h+2)^(W_K(j)-1)` for nonempty frontiers gives
```
A(j,h) <= (h+2)^((2*rho+1)*(K-m0+1)-1).
```
This is an **XP-style polynomial bound at fixed radius and center-budget excess epsilon=K-m0**. Since the exponent depends on epsilon, no fixed-parameter tractability claim follows from this inequality. It improves the earlier unspecified old-frontier-width exponent to a concrete geometric/budget parameter.

**Proof of gluing and rank lower bounds.** The center-path graph has a source prefix-coverage cost, feasible consecutive-center edges that certify coverage of the points between their endpoints, and a tail-coverage condition. A feasible prefix ending at `i` and a feasible suffix starting at `i` concatenate, sharing exactly `i`; all events are covered. Hence `a_i+1+b_i` is the minimum feasible center count among solutions containing `i`, and certainly at least `m0`. The rank inequalities now follow immediately. Summing multiplicities over at most `2*rho+1` distinct spatial tails gives the width inequality. QED.

## Exact R5 finite audit

`VERIFY_R5_RANK_SLACK_BOUND.py` computes minimal center counts on the feasible consecutive-center graph, then independently reconstructs the exact minimum-cost optimizer DAG from the original frozen generator and checks all active tail vertex ranks against `a_i<=r<=K-1-b_i`. Tested all 32 effective closure configurations, K=214..221, 256 full optimizer instances over 954 events. Observed `PASS_R5_FEASIBLE_RANK_SLACK_BOUND`; greatest feasible per-tail slack `K-1-a_i-b_i` is 9; greatest optimizer per-tail rank multiplicity is 5. Original 66,429-byte JSON digest: SHA-256 `8d2824cc02b85de9a3e7da84ba43fd68a741dac7c54d98b3172bec12d62f29b2`. Complete compressed JSON is stored as `R5_RANK_SLACK_RESULTS.json.zlib.b64` (decode base64, then zlib).

Separate earlier local checks, preserved in this directory, establish spatial bound 5 on 19,683 small gap sequences plus all 32 effective masks and independently evaluate 256 optimizer frontiers, observing width 19. The prior saved R5 optimizer-family support theorem is still needed to extend these 32 effective masks to all 28 original closure bits; this work does not independently re-prove that quotient.

## Next

Seek a stronger optimizer-specific bound on `d_K(j)` than the feasible budget slack bound, exploiting minimal objective cost and the common-anchor decomposition, and independently audit the Pareto-vector dominance/old-path frontier transition. Keep model-observer scope and frozen pin.

Provenance: existing Draft PR #2427; full spatial theorem `FRONTIER_SUPPORT_AND_RANK_MULTIPLICITY_THEOREM.md`, prior `PARETO_FRONTIER_PARAMETRIC_BOUND_AND_BACKGROUND_REVERSALS.md`. Author proof and exact finite checks, independent mathematical review `NOT_REVIEWED`. Formal Task-ID/active CLAIM unconfirmed; no protected Activity mutation asserted.
