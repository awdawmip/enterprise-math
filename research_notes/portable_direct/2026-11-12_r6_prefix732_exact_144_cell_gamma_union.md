# PREFIX-732-R6 — Exact deduplication of PREFIX-731's 144 Gamma whole-grid cells

Date: 2026-11-12 (Asia/Shanghai).
Mother objective: PREFIX-675. Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: AUTHOR_EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Result
PREFIX-731 proves that the square `[38/384,50/384]^2` (144 entire fine cells) satisfies
`V_q(0,73/500)-V_q(p,z)>40 q^2` for every real `q>=2`. PREFIX-730 already
added 58 cells from the nested `[40,48)^2` block. The new exact overlap count is:

| Part | Cells |
|---|---:|
| PREFIX-731 larger block | 144 |
| Already covered by PREFIX-729/730 inner block | 64 |
| PREFIX-712 all-q base overlap outside that inner block | 16 |
| PREFIX-713/716/718 overlap inside the larger block | 0 |
| New, previously uncertified complete cells | **64** |

In the full 144-cell block, PREFIX-712 covers exactly 22 cells; six are in the
old 64-cell inner block and sixteen outside. All 36 candidate 2×2 old-base
coarse parents fail the PREFIX-712 old certificate; the individual exact
child checks recover the 22 cells. The four later explicit all-q sources
contain no cell in this square. Thus the exact **duplicate-free** update is

```
prior PREFIX-730 all-q certified = 139076
new outside old union             =     64
new all-q certified total         = 139140 out of 147456
                                  = 3865/4096 = 94.3603515625%
unexcluded whole-cell complement  = 8316
```

The outer 80-cell annulus is the difference of two nested axis-aligned
grid blocks; its 16 old-base cells and 64 genuinely new cells partition
it. This union is *of certified exclusions*, not a count of all actual
nonglobal-maximizer cells.

## Exact membership decision
For a fine cell rectangle `R=[a/384,c/384]×[b/384,d/384]`,
let `l=mu(a/384,b/384)`, `H=M2(c/384,d/384)`,
`U=H-l^2`. For the original PREFIX-712 comparator `e0=(0,3/20)`,
write `mu0=mu(e0)`, `W0=M2(e0)-mu0^2`.
The old all-real-q certificate is exactly the conjunction

```
W0-U > 0,
W0-mu0/2 - (U-l/2) > 0.
```

Both are strict rational inequalities. The accompanying checker
reconstructs the frozen 189-layer integer Gamma moments via the pinned
PREFIX-731 module and applies the original PREFIX-712 coarse-then-fine
membership procedure to the 144 indices; it reads the exact four later
certificate lists and PREFIX-730 prior union. It asserts the counts,
overlaps, and rational `3865/4096` identity.

## Evidence and scope
A local independently written standard-library Python integer/Fraction
checker reproduced all 189 survivor rows (9,529 nonzero count cells),
the old-comparator moments, the old-base 22-cell overlap, and the
six-cell inner check. Current GitHub connector reads of
`PREFIX713_R6_RESULTS.json`, `PREFIX713_R6_MULTICOMPETITOR_RESULTS.json`,
`PREFIX716_R6_RESULTS.json`, `PREFIX718_R6_RESULTS.json`, and
`PREFIX730_R6_RESULTS.json` verified zero later overlaps and the
previous 139076 total. The new modular aggregate checker is published
for reproduction; its complete standalone rerun after publication
is a separate outstanding check. No independent mathematical review
or canonical Result/Review admission is asserted.

## Next scientific unit
Attempt adaptive corner-moment subrectangles on the boundary of
`[38,50)^2`, prioritize candidate complete grid cells not already in
the 139140 certified union. Before reporting a new union total,
perform the same exact overlap subtraction. Preserve frozen Gamma
model and distinct current shared Task owners.
