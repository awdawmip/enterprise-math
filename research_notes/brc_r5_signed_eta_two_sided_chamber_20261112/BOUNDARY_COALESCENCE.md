# R5 — Exact first resonance coalescence at both signed-eta chamber boundaries

Date: 2026-11-12, author-side exact rational finite result; **same frozen external P/Q–BRC auxiliary observer, X, H and 15 labeled moves** as the accompanying `RESEARCH.md`. This note continues that work at the two excluded parameter endpoints. The project-native/P000 model is unchanged.

## Statement

Let `x=155682221/25142124560000000`, `epsilon_max=9/115400000`, and retain the original target-0 one-coordinate spectrum `E0` of 1,144 distinct interior values. Let

```
eta_left = -155682221/311686918170320000000
eta_right = +155682221/312843455900080000000
t15(eta) = (x-23 eta)/15
```

At `eta_left`, the moving target-1 phase coalesces with fixed target-0 phase `36x/539`. At `eta_right`, it coalesces with `36x/541`. Both endpoints remain strictly positive initial transfers with observer invariant `AX(eta)=AX` and the same maximal nonnegative ray endpoint. No other moving phase collides there. Therefore, **at either exact boundary the complete interior first-zero spectrum has 1,146 distinct phases**, versus 1,147 in each open adjacent sign chamber and 1,144 at eta=0.

The merged phase is an **actual order-count discontinuity**, not just duplicate numerical threshold values. Exact 15-label subset DP and 28-coordinate prefix tests give:

| chamber boundary | merged phase epsilon | newly forbidden prefix subsets | legal orders before | after | total loss |
|---|---|---:|---:|---:|---:|
| negative `eta_left` | `1401139989/3387901284460000000` | **4,108** | **850,075,412,400** | **469,532,537,808** | **380,542,874,592** |
| positive `eta_right` | `1401139989/3400472346740000000` | **4,109** | **852,167,301,216** | **471,427,082,208** | **380,740,219,008** |

## Exact decomposition and proof

Choose a rational point just inside each side of the established chamber: `eta_inner=999 eta_edge/1000`. At these points the colliding phases separate into adjacent values: the moving `t15` and the fixed `36x/k`.

On the negative side, the **moving phase occurs first**; its 4,096 forbidden subsets cost 379,627,579,392 orders, followed by the fixed phase's 12 newly forbidden subsets costing 915,295,200 orders. Exact sums: `4096+12=4108` and `379627579392+915295200=380542874592`.

On the positive side, the **fixed phase occurs first**; its 13 subsets cost 959,619,024 orders, followed by the moving phase's 4,096 subsets costing 379,780,599,984. Exact sums: `13+4096=4109` and `959619024+379780599984=380740219008`.

The exact full-prefix classification at the boundary confirms that these subset families are disjoint and that the merged cut has precisely the sum of the two nearby losses. These additive losses are specifically along each ordered two-cut chain; they do not assign independent causal weights to all possible unrelated masks.

The underlying chamber proof in `RESEARCH.md` established all initial and endpoint positivity and nonminimizing-line bounds strictly beyond both boundary magnitudes. Thus its affine first-zero classification remains valid at the two closed endpoints; only the advertised single collision becomes an equality. All other 1,144 E0 values retain exact witnesses, the other two moving values are distinct and outside E0, and the fixed endpoint is unchanged.

## Independent finite replication

`VERIFY_EDGE_COALESCENCE.py` reads/decompresses the sibling published `VERIFY_R5_SIGNED_ETA.py.gz.b64`, executes its exact rational source in a private Python dictionary, then checks each boundary and its 999/1000 interior neighbor, including 32,768 subset minima, both order counts, mask totals, first-zero equality and jump additivity. The actual execution result is `EXACT_OUTPUT_EDGE_COALESCENCE.txt`.

This is exact finite coverage of the **fixed frozen 28-mass/15-atom model**, with no floating-point thresholds. The work is researcher-side and has not undergone separate Source scientific review.

**Next unit:** extend the affine phase arrangement immediately *outside* each first-collision boundary and classify when the single-coordinate threshold generator loses or regains values, whether 15-step path feasibility changes, and which other phase families coalesce; preserve original frozen scientific pins.
