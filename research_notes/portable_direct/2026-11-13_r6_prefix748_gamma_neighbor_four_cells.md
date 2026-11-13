# PREFIX-748-R6 — Four neighboring complete Gamma cells excluded by exact 8×8 envelopes

Date: 2026-11-13 (Asia/Shanghai). Mother objective: PREFIX-675; prior frontier: PREFIX-747-R6.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Author-side result status: `AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED`.
The control session-start request `r6-20261113-132101-prefix748-registration-v1` was RUNNING at the last observation preceding publication; registration, activity binding and shared CLAIM must be checked separately. This document does not assert an authenticated Researcher-ID.

## Model and proposition

Retain the frozen 189-layer stopped-survivor BRC integer recurrence, its two independent unit-rate Gamma clocks `T_p,T_z`, and `Y(p,z)=max(T_p,T_z)`. Put
`mu=E[Y]`, `M2=E[Y^2]`, `W=M2-mu^2`, and `V_q(p,z)=q^2 W(p,z)-q mu(p,z)`.
Use comparison point `e=(0,73/500)`, and closed cells
`R_ij=[i/384,(i+1)/384] × [j/384,(j+1)/384]`.

**Theorem (frozen Gamma auxiliary model).** For every real `q>=2` and every continuous `(p,z)` in each of the four *closed* cells
`R_(11,51)`, `R_(12,52)`, `R_(51,11)`, `R_(52,12)`,
the uniform strict inequality
`V_q(e)-V_q(p,z)>7*q^2>0` holds.
Thus these four complete parameter cells are excluded from global maximizers of this precise auxiliary objective.

## Load-bearing bound and proof

The frozen 189-row survivor integer kernel has 9,529 nonzero coefficient positions and an empty row 189. The nonnegative, symmetric, center-nondecreasing normalized Bernstein coefficients are checked in the companion exact script; as in PREFIX-731 and PREFIX-741 they imply coordinatewise nondecreasing survivor tails, hence coordinatewise nondecreasing `mu` and `M2` on `[0,1/2]^2`.

For a rational closed subrectangle `Q=[a,c]×[b,d]` let `L=mu(a,b)>=0` and `H=M2(c,d)`. At every `(p,z)∈Q`, both `mu(p,z)>=L` and `M2(p,z)<=H`. Write `t=1/q∈(0,1/2]`; then
`[V_q(e)-V_q(p,z)]/q^2 = W(e)-M2(p,z)+mu(p,z)^2-t*(mu(e)-mu(p,z))`
`>= W(e)-H+L^2-t*(mu(e)-L)`.

The right side is affine in `t`. Its minimum on the enclosing closed interval `[0,1/2]` is the smaller of its values at `t=0` and `t=1/2`; call this exact rational bound `B(Q)`. Subdivide each full `R_ij` into `s×s` closed rational rectangles and let `G_s(i,j)=min_Q B(Q)`. The full continuous-cell bound is `[V_q(e)-V_q]/q^2>=G_s(i,j)`; transposition uses exchangeability of the clocks.

The companion exact Python checker computes the Gamma moment kernel with integer sums and `fractions.Fraction`, using `s=2,4,8`. Its floors `floor(10^6 G_s)` are:

| Original cell | s=2 | s=4 | s=8 |
|---|---:|---:|---:|
| (11,51) | -80,983,623 | -21,911,219 | **7,714,155** |
| (12,52) | -82,633,603 | -22,525,720 | **7,614,806** |

For each original cell the *exact* `G_8>7`; reported floors are displayed results, not the proof's rounding rule. The two transposed cells inherit the same exact result. This establishes the theorem, including the cell boundaries and all real `q>=2`.

**Refinement lemma.** If `s'` is an integer multiple of `s`, every subrectangle of the `s'×s'` partition is contained in a unique `s×s` parent. On a child, `L_child>=L_parent>=0` and `H_child<=H_parent`. For every `t∈[0,1/2]`, `W(e)-H+L^2-t(mu(e)-L)` is nondecreasing as `L` grows and `H` falls. Thus `G_(s')(i,j)>=G_s(i,j)`. Strict positivity first observed at `s=8` is therefore compatible with the negative coarser lower bounds; those negative values were inconclusive, not counterexamples.

## Verification and provenance

On 2026-11-13 the author independently reimplemented the exact moment formulas from the connector-read `PREFIX741_R6_INNER_STRIP_194.py`, rebuilt all 190 rows (0..189), checked row 189 empty and 9,529 nonzero coefficient positions, asserted the Bernstein symmetry/center inequalities and matched the frozen witness-moment SHA256 regressions:
`797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e` (mu numerator),
`814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae` (W numerator).

A complete two-child-process local replay using this mathematically identical reimplementation yielded:
`PASS 11 51 (-80983623, -21911219, 7714155)`;
`PASS 12 52 (-82633603, -22525720, 7614806)`;
`ALL_CHECKS_PASS PREFIX748-R6 2+2=4`.
The published compact checker imports the original `PREFIX741` dependency; that exact repository dependency plus the new published checker remains to be rerun together independently.

The old comparison point `(0,3/20)` with unrefined 1×1 envelope has exact millionth floors `-199177623` at (11,51) and `-202919029` at (12,52); its old sufficient test therefore did not certify these cells. GitHub connector reads of the exact historical result JSONs `PREFIX713_R6_RESULTS.json`, `PREFIX713_R6_MULTICOMPETITOR_RESULTS.json`, `PREFIX716_R6_RESULTS.json`, `PREFIX718_R6_RESULTS.json` found no listed matching candidate coordinates or enclosing old coupled parent; the new coordinates were also checked against the read PREFIX-742 through PREFIX-747 results, and are outside the spatial ranges of PREFIX-729/730/731 and PREFIX-737/738/739/740/741 as specified by their predecessor notes.

Relative to PREFIX-747's documented **author-level** certified union, the four additional cells give
`141976+4=141980` of `147456` complete cells, or `35495/36864 = 96.286349826388...%`, leaving `5476` complete cells outside that author's union. A comprehensive *independent* full-history union audit is still pending; this inherited denominator/baseline is not promoted to a canonically admitted global theorem.

## Next scientific unit

Replay the published compact checker verbatim with the exact GitHub `PREFIX741` module and audit the full historical certificate union; investigate adjacent `(10,50)`, `(10,51)` or `(11,52)` by bounded exact subdivisions or adaptive bounds. One separate `(10,50)` test was interrupted before finishing; it supplies no numerical certification. Preserve this provenance, frozen scientific pin and the separate claim/review authority boundaries.
