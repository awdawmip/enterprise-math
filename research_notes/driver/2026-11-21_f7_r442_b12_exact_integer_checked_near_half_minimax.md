# CBRC F7 Driver r442 — B=12 near-half exact integer-verified finite minimax bound

2026-11-21 (+08:00). Auxiliary computation by the original Driver line `EM-DVR-DEBB5E`. Preserve CBRC F7 original scientist `EM-CBRCF7-83A1D4`, frozen Result `RR-AA38973D56330E59D315`, and its native-review status. This is a finite optimization result in the original F7 two-slot scalar model, not a changed P000 premise.

## Exact statement

Use the F7 integer matrix
```text
A = [ 2 -2 -1  2
      1 -1 -1  2
     -1  2  2 -2
     -1  2  1 -1 ] .
```
For `q: Z^2 -> R_{≥0}` satisfying `q(0,0)=0`, `q(n,m)=q(-n,m)`, `q(t,0)=1` for every nonzero integer `t`, `q(n,m)>=1/2` for nonzero pairs, and marked constraints `q(2,1)=q(-1,-1)=1/2`, set
`D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(z_1,z_2)-q(z_3,z_4)`.
Let `E_B=inf_q max_{z in [-B,B]^4 intersect Z^4}|D_q(z)|`.

**Result:**
```text
1/2 <= E_12 <= 50,000,001 / 100,000,000 = 0.50000001.
```
The same upper bound holds for every `1<=B<=12`. For `B<=8` the earlier r436 result already attains the exact `1/2`.

## Constructive and proof-check evidence

The mathematically equivalent r438 sparse epigraph LP for `B=12` has 60,000 inequalities, 3,046 free J-even scalar classes and 2,352 auxiliary variables. Search was restricted to the permissible subfamily `1/2<=q<=1`. SciPy/HiGHS returned a numerically feasible candidate for `epsilon=1/2`; each free scalar class was rounded **once** to an integer numerator with denominator `DEN=100000000`. Origin/axis/mark and all off-table values are given by exact case definitions, so the result specifies a total, admissible rational `q`.

An **independent integer-only four-term conservation scan** then checked all `25^4=390,625` integer inputs of the complete cube, rather than relying on numerical LP residuals. Exact observed integers:

- `B=12`; `DEN=100000000`;
- free scalar classes used: **3,046**, every numerator in `[50,000,000,100,000,000]`;
- maximal absolute conservation-defect numerator: **50,000,001**;
- number of equality inputs: **466**;
- an integer witness: `(-12,0,-11,-2)`.

The analytic lower bound `E_12>=1/2` is inherited from r436's exact marked witness `(1,-1,0,0)`. Combining this with the verified rational candidate yields the displayed interval.

Published deterministic search-and-exact-check code:
`research_checks/CBRC_F7_R442_B12_EXACT_INTEGER_VERIFIED_PRIMAL_20261121.py`, Source commit `737ae32a106d7773f8cc5d48b38e3b3f1fbb81ee`.
The checker generates the LP candidate with SciPy/HiGHS and thereafter applies integer arithmetic to every 4-tuple, asserting `max_abs_D<=50,000,001 / DEN`.

The particular 3,046-value table was generated in the local verified run. **The immutable checker currently embeds the generation algorithm rather than a static coefficient table**, so replay with a different solver version/basis must itself pass the exact integer assertions; it should not be treated as the same frozen candidate unless the table bytes are separately pinned. This is a reproducible, solver-assisted exact-integer-checked finite construction, not an independent static-table certificate or a theorem of exact `E_12=1/2`.

## Consequences and next problem

r442 expands the finite near-half verified radius from r439's `B=10` to `B=12`. The new r441 theorem has proved the exact **unrestricted** relation `E_infty=sup_B E_B` and existence of a global minimizer. r442 therefore strengthens the finite exploration but does not settle the global optimum: presently `1/2<=E_infty<=4/7`.

The next discriminating mathematics is either a rational `E_B>1/2` dual certificate at some finite radius, or a proof of uniform exact half feasibility across all radii. If the latter holds, r441 now guarantees a global uncapped exact half-defect scalar.

Native Review, Result, Source/Activity provenance, formal Task and parent Objective remain separately unclosed; no original author contribution or owner status is changed.

### Source lineage

- r438 sparse LP proof: `research_notes/driver/2026-11-21_f7_r438_exact_sparse_epigraph_lp_and_b12_exploration.md` @ `5260880f50468bd6aa9ef232e28b49dcd36504bb`.
- r439 finite B10 predecessor: `research_notes/driver/2026-11-21_f7_r439_b10_integer_verified_near_half_minimax.md` @ `cd06e875df3300f715c36301cb8e4b9990570e10`.
- r441 uncapped compactness: `research_notes/driver/2026-11-21_f7_r441_uncapped_compactness_from_old_axis_coercivity.md` @ `82027a566a0b9b84069fba9a4d3616027a3b4660`.
