# Exact support-change witness for the 14-edge affine F-face chart

The explicit affine chart of `RESEARCH.md` gives a feasible 14-edge transport throughout a verified nine-parameter physical box. Its **fixed support** is not sufficient for every lawful F-face source/target pair. This is witnessed exactly by a predecessor's known feasible 12-edge example.

Use the frozen R5 source and seedless F-face target from PR #1831 (`EXPLICIT_12_EDGE.md`, immutable commit `83431247dad45aba95b43125bca63c94d81e5750`):
[
x=(1,1/10,1,27/800,1/100,27/400,1/100),
]
[
y=(4673/6400,1311/6400,4673/6400,38759/512000,
47301/256000,103999/512000,1311/64000).
]

Here (g=b=1), the target satisfies (z'=a'/10) and (v'-z'=9b'/40), and both stop times agree. Substitute the exact `RESEARCH.md` 14-edge formulas (3)–(4). All 21 transport **equalities** hold, but one coefficient is negative:
[
oxed{E_{4,2}=-2109829/147200000<0.}
]
All other 13 chart entries are nonnegative; (E_{1,1}=0). Thus the chart is outside its lawful nonnegative chamber at this input.

The **same pair** has an independent, fully checked **12-positive-edge** nonnegative transport given in PR #1831. The script `VERIFY_FACET_WITNESS.py` restates all 12 rational edge masses and verifies all seven row masses, seven source column masses and seven LR-weighted column equations, as well as the negative chart coefficient. The smallest positive mass in the alternative is (1/256). Actual executed output: `FACET_OUTPUT.txt`.

**Consequence:** extending the 14-edge theorem beyond the open region requires changing the edge pattern or selecting a different seedless target; the single fixed pattern does not provide global coverage. The existence of a 12-edge alternative also shows that a failed fixed chart need not indicate a 15-edge obstruction. The full lawful physical 14-vs-15 uniform question stays open.
