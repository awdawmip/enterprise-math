# T6 / maximal p=17 / vertical order 5: exact mixed-congruence exclusion of all primitive signed shapes

Date: 2026-11-23 (Asia/Hong_Kong). Research mode: TASK_RESEARCH / portable author computation; evidence status **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Mother objective `T6=2332`: OPEN. This note does not assert an authenticated winner, native semantic PROGRESS, or Driver mathematical admission.

## Frozen carrier and input provenance

- Task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`, frozen `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` at commit `d84bd940cfb093cdc60e569f15cad58772a51dca`, blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`.
- Retain the full exponent denominator `a=e+1`, exact integer signed multiplicity, each side exponent mass <=2331, and the seven BRC shape observers `H0,...,H6`. After the triangular binomial transform, the full observer equality implies the reciprocal equations `S1,...,S6`.
- Reuse the 16-dimensional p17 q0 saturated lattice from `research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json` at Git blob `d9ac014355a6a1058cc8a0cf2141a01082628881`; exact basis rows, weighted norm, determinant and six congruences are rechecked.
- Prior author proof `research_notes/portable_direct/onhour_20261123_t6_p17_high_valuation_and_global_mixed_congruences.md` @ `ae55de7df892c761c069235e51d20cf976ae2ceb` supplies cancellation of all p17 valuation >=2 atoms and the globally necessary mixed mod-17^j conditions. It is retained at author-proof strength.

After cancelling common atoms, each p17 valuation-one denominator is exactly `17(r+17q)`, with `r=1,...,16`, `q>=0`, and cost `289q+17r-1`. Its vertical order is `q`, not the count of such atoms. A q0 signed vector `u=(u1,...,u16)` has weights `wr=17r-1`. For an oriented vertical pair `V+,V-`, let `m(q,r)` be its signed count. Full-shape equality requires, for every `j=1,...,6`,

```
sum(r=1..16) u[r] * inverse(r^j,17^j)
 + sum(q>=1,r=1..16) m(q,r) * inverse((r+17q)^j,17^j)
 == 0 (mod 17^j).
```

The p17-free atoms are left unrestricted; these modular conditions are genuinely necessary for their presence, not p17-only rational moment equalities.

## Complete order-five primitive roster

Up to global sign, side vertical-order splits are exactly `(0,5),(1,4),(2,3)`. For each side, all integer partitions into positive q's and all nondecreasing residue multisets for equal q's were generated. Same named vertical atom appearing on both sides is a cancellation to a lower vertical order, so is recorded separately. The maximum admissible vertical-side cost is 2331.

| split | ordered raw side pairs | pairs with common vertical atom | primitive pairs checked | q0 weighted sphere points |
| --- | ---: | ---: | ---: | ---: |
| (0,5) | 30,040 | 0 | 30,040 | 0 |
| (1,4) | 103,360 | 17,408 | 85,952 | 0 |
| (2,3) | 165,376 | 37,248 | 128,128 | 0 |
| **total** | **298,776** | **54,656** | **244,120** | **0** |

Exact state counts at vertical orders 0,1,2,3,4,5 are respectively `1,16,152,1088,6460,30040`. Thus the table covers every primitive order-five configuration satisfying the vertical side budgets, including all q0 compensation.

## Exact finite search and completeness proof

The homogeneous q0 lattice consists of all integer `u` satisfying the six homogeneous congruences. Its supplied 16x16 integer row basis `U` passes all 6 modular tests, and its exact determinant magnitude is `17^21=69091933913008732880827217`. A 6-column inverse-power Vandermonde minor has unit determinant modulo 17; successive moduli `17^1,...,17^6` therefore give this same full kernel index. This identifies `U` as the saturated lattice, not a selected sublattice.

For each vertical atom `(q,r)`, the checker constructs an integer affine particular vector by six sequential unit-pivot modular solves; each solve is independently checked. Linearity yields an exact particular representative of each signed vertical pair. Every q0 completion lies in this representative plus the full homogeneous lattice.

Let `W=diag(16,33,...,271)`. If a q0 completion obeys the separate signed side budgets, then, with `B+=2331-cost(V+)`, `B-=2331-cost(V-)`,

```
||W u||_2^2 <= B+^2 + B-^2 = R^2.
```

The exact Gram–Schmidt decomposition of the weighted row basis has minimum squared diagonal

```
D_min =
8350069911612335617606677214061177705401058080646556447012234889468081355909
/480650972868542992444263969893692042421717754534280313801217347854273.
```

The maximal possible `R^2` for the three splits is `6,190,461`, `5,447,957`, and `5,113,873`, respectively, all *strictly less* than `D_min` (approximately 17,372,418.622). For the current affine center of each Gram–Schmidt coordinate, `D_i*(center+n_i)^2 <= residual R^2` implies `|center+n_i|<1`. Hence the only possible integer coefficients are the exact floor and ceiling of `-center`. The code enumerates both using Python `Fraction`, with back-to-front subtraction of exact squared components. Every branch pruned has a proven partial squared norm exceeding `R^2`. The recorded count of complete sphere leaves is **zero** for all 244,120 primitive cases. Thus no primitive order-five affine class has even a point inside its necessary weighted sphere.

`research_checks/T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py` is the reproducible exact checker. `research_checks/T6_P17_Q5_AUTHOR_EXACT_CERT_20261123.json` holds all split and depth counts; its local SHA-256 at execution is `d6e71d2581ea253224514e9c0b119da8255c2929fd7a8d2c8ee935c5f372fa5a`.

## Conclusion and next precise science

**Author exact finite result:** after removal of p17^2 atoms as in the previous author lemma, no *primitive* maximal-p17 vertical-order-five signed configuration under side masses <=2331 can satisfy all globally necessary mixed congruences `mod 17^j (j=1..6)`. This is a full order-five *primitive block* elimination, including q0 compensations and arbitrary lower-prime completion; shared-vertical-atom pairs reduce to the lower-order frontier and are preserved separately.

The next minimal independent unit is maximal-p17 vertical order six, with splits `(0,6),(1,5),(2,4),(3,3)`, using the same exact carrier/basis but recomputing side rosters and sphere bounds. Existing q0–q4 evidence is consumed, not republished. Full T6 and review remain open.
