# HODGE H0J Semantic Checkpoint

Date: `2026-08-22`
Researcher-ID: `EM-HODGE-H0J-4E8C31`
Task: `RS-HODGE-H0J-CUBIC-FOURFOLD-BRC-MULTIPATH-CORRESPONDENCE-LIFTING`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Owner branch: `research/hodge-h0j-cubic-fourfold-brc-correspondence`
Taskbook source: `769435a951030da4281a5d342752ce4651bfae5d`
Canonical BRC authority: `b5bdc33578f324b55a57e5bdff9cf9c3acc30034`

## Frozen disposition

`H0J_BRC_CORRESPONDENCE_SOURCE_INHERITED`

Hard target:

`BRC_MULTIPATH_ADDS_ROBUST_PROOF_LEVERAGE_BEYOND_CLASSICAL_INCIDENCE_CORRESPONDENCE = NOT_ESTABLISHED`

Preferred stronger target:

`CUBIC_FOURFOLD_CLASS_FIRST_ENTERPRISE_R3_PRESEED = NOT_ESTABLISHED`

`H1_ADMISSIBLE = false`
`Hodge_proved = false`

## 1. Exact cubic source

Freeze the smooth cubic fourfold over `Q`

`X: x0^3+x1^3+2x2^3+2x3^3+x4^3+x5^3+x0*x4^2+x2*x5^2=0`.

Smoothness is deterministic from the six partial derivatives.  The `x1` and `x3`
partials force `x1=x3=0`; the pairs `(d0,d4)` and `(d2,d5)` then force
`x0=x4=0` and `x2=x5=0`, so there is no projective critical point.

On the Grassmannian chart `U_02`, use the row frame

`[[1,a,0,b,c,d],[0,e,1,f,g,h]]`.

Substitution into `X` gives exactly four Fano equations:

- `a**3 + 2*b**3 + c**3 + c**2 + d**3 + 1`
- `3*a**2*e + 6*b**2*f + 3*c**2*g + 2*c*g + 3*d**2*h + d**2`
- `3*a*e**2 + 6*b*f**2 + 3*c*g**2 + 3*d*h**2 + 2*d*h + g**2`
- `e**3 + 2*f**3 + g**3 + h**3 + h**2 + 2`

The explicit line

`L0=[s:-s:t:-t:0:0]`

is a point of this Fano chart.  The Fano Jacobian has rank `4` there, hence
the declared local Fano source is smooth of dimension `4`.

The same line lies in `U_13` because `p13(L0)=1`.  Reframing by the exact
inverse of the `(1,3)` pivot matrix gives the identical geometric line, providing
the frozen presentation-overlap check.

## 2. Actual incidence / surface source

Freeze three Plucker-linear cuts on `F`:

`A=p24` (local function `c`),
`B=p25` (local function `d`),
`C=p04` (local function `g`).

At `L0`, the four Fano equations plus `c=d=g=0` have Jacobian rank
`7` in `A^8`, so their local intersection is a regular curve.

The incidence chart with `lambda=t/s` maps to affine `x0=1` by

`(x1,x2,x3,x4,x5)=(a+e lambda, lambda, b+f lambda, c+g lambda, d+h lambda)`.

At `L0, lambda=1` the image is

`[1:-1:1:-1:0:0]`.

The differential on the curve tangent together with the line-fiber tangent has
rank `2`.  Thus the frozen incidence family has a genuine local
two-dimensional image; denote the proper pushforward cycle germ by `S0`.

## 3. Two independent multiplicities

The canonical BRC occurrence count and algebraic intersection multiplicity must
not be identified.

For the regular triple `(A,B,C)`, each route occurrence has algebraic
multiplicity `1`.

Replacing `A` by `A2=p24^2` keeps the same Boolean support but the local normal
slice is `Q[c]/(c^2)`, of length `2`.  Therefore each `A2,B,C` route occurrence
has algebraic cycle evaluation `2*S0`, although it is still only one BRC path
occurrence.

Freeze:

`PATH_OCCURRENCE_MULTIPLICITY != SCHEME_INTERSECTION_MULTIPLICITY`.

## 4. Exact BRC correspondence typing

H0J does not rename an arbitrary correspondence graph as BRC.  Its typed edges
are actual algebraic operations:

`CUT_f`, `INC_PULL`, `INC_PUSH`.

A path witness records section labels, intermediate ideals, chart, incidence
fiber parameter and target.  The path-formal carrier is the finite free
`N`-sum on these typed witnesses; composition is typed concatenation extended
distributively.

Concatenation is strictly associative.  Algebraic evaluation is compatible
because iterated fiber products are canonically associative and the local cut
evaluation is ordinary scheme intersection/ideal composition.

Therefore:

`ALGEBRAIC_CORRESPONDENCE_PATH_FORMAL_CARRIER_IS_WELL_TYPED = true`.

## 5. J1 — provenance is real, but not an Enterprise proof normal form

The frozen path grammar contains:

- `6` permutations of `(A,B,C)`, all evaluating to `S0`;
- `6` permutations of `(A2,B,C)`, all with the same support but evaluating to `2*S0`;
- `6` permutations of `(A,Bp,C)`, where `Bp=B+A`, all generating the same final
  ideal `(c,d,g)` and hence `S0`;
- `3` distinct permutations of `(A,A,B)`, which leave only the codimension-two
  ideal `(c,d)` and fail the codimension-three curve obligation.

Thus path provenance, support, algebraic multiplicity and validity are all
genuinely distinct observables.

But the presentation-invariant Hodge/cycle obligation cannot use raw path count:
six cut orders describe the same scheme/cycle, and changing `B` to `B+A` changes
the path presentation without changing the ideal.

## 6. J2 — Z/Q completion is source-inherited

The `Z` group completion is well typed after J1, with bilinear composition.
For example

`[A,B,C]-[A,C,B]`

is nonzero provenance but evaluates to zero in the ordinary cycle group.

The rational lane is also exact:

`(1/2)[A2,B,C] -> S0`.

However these are precisely the standard free-abelian cycle group and its
rational extension after evaluation.  They are not canonical R062 BRC and they
add no Hodge-special attribution.

## 7. J3 — strict future quotient, exact no-go

For the frozen 21-path grammar, unique raw prefix counts at cuts 1,2,3 are

`5, 15, 21`.

The complete downstream future-signature class counts are

`5, 5, 3`.

Keeping full incidence and final X-cycle provenance gives the predeclared raw
reusable-interface measure

`83`.

After exact future recoalescence the interface is

`19`.

Hence J3 has strict abstract leverage:

`83 -> 19`.

But `B_std^corr` independently computes exactly the same behavior kernel from
ordinary ideal normal forms, codimension, scheme multiplicity, proper
pushforward and cycle/Chow evaluation.  The Enterprise quotient therefore
recovers the source normal form rather than creating a new one.

`J1/J3 attribution = SOURCE_INHERITED_LEVERAGE`.

## 8. Classical incidence control remains separate

The Beauville-Donagi incidence transform has genuine classical layer-lowering
leverage from primitive degree-four cohomology of the cubic to primitive
degree-two cohomology of the Fano variety.  Lefschetz `(1,1)` / Picard then
belongs to classical source mathematics.

H0J assigns this:

`CLASSICAL_PRIOR_ART_TRANSFORM_WITH_REAL_LAYER_LOWERING`.

It receives zero Enterprise incremental credit.

## 9. Attribution result

Against `B_raw^corr`, the path/future construction has strict operational
compression.

Against fair `B_std^corr`, the load-bearing normal form is already present in:

- ordinary algebraic correspondence composition;
- scheme-theoretic fiber products/intersections;
- ideal and presentation normalization;
- intersection multiplicity;
- proper pushforward;
- cycle/Chow groups;
- free-abelian and rational cycle coefficients.

Therefore no candidate reaches

`ROBUST_TRANSFORM_ATTRIBUTED_ENTERPRISE_INCREMENT`.

Hard target: `NOT_ESTABLISHED`.

## 10. R3 / H1 firewall

No independent exact cubic Hodge-class input carrier was frozen, and no robust
Enterprise incremental R2 component exists.  J4 was therefore not attempted.

`CUBIC_FOURFOLD_CLASS_FIRST_ENTERPRISE_R3_PRESEED = NOT_ESTABLISHED`.

`H1_ADMISSIBLE = false`.

No generalization beyond the frozen cubic/local source is claimed.

## 11. Route decision

Do not rerun H0J with more Fano lines, more Plucker charts or a larger path
bound while keeping the same mechanism.

The frozen no-go is:

> for theorem-critical obligations that factor through ordinary algebraic
> correspondence/cycle evaluation, BRC path provenance is an information
> enrichment, but presentation-invariant future recoalescence collapses exactly
> to the source correspondence/Chow normal form.

Next work, if any, must change the Enterprise mechanism or find a
Hodge-critical obligation that genuinely depends on provenance not already
represented by classical correspondence mathematics.

`CI_NOT_REQUIRED_FOR_RESEARCH`

## 12. Checker / digest

Deterministic checker:

`329/329 PASS`

Semantic core SHA-256:

`4e2a08ab7d0e7d7c8f3672cd33eac11112308157e917fd2051c2c1902267dc74`

Checker script SHA-256:

`1321795922b3599c4ec34e4a525d61f4c199ab8326d6b075557954465e384641`

`CI_NOT_REQUIRED_FOR_RESEARCH`
