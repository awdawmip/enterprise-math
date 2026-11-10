# R5: sharp lawful-half-cube radius and a 14-edge/capacity-facet intersection

Date: 2026-11-10 (Asia/Shanghai). Author-side exact-rational result; separate native Result/review not asserted.

## Scientific provenance and question

Keep the frozen seven-likelihood-ratio P/Q–BRC inputs of PR #1939 (GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`). In particular use its rational lawful center `p0`, 8 physical tangent directions `P`, its 15-edge fixed-basis coupling, the ten mandatory-edge dual inequalities and finite quotient-support exclusions. The present contribution sharpens the local 14/15 support phase diagram of PR #1939 without changing the scientific input or the X6/P000 ontology. Seven likelihood ratios label statistical observations, not native spatial axes.

Let `r*=23/17050000`, `t*=(0,0,0,-r*,r*,0,0,-r*)`. Set `p(z)=p0+P(t*+z)` for real `z in [-rho,rho]^8`. The target's second observation mass is
`m(z)=mu_1(z)=z_3/80-z_4+(13/4)z_7` (zero at `z=0`).
PR #1939 certified the complete 14/15 dichotomy on `rho=10^-7`. How large a symmetric eight-parameter box admits the **exact physical-legality criterion `m(z)>=0`**, and does the Blackwell support transition remain the same on that larger box?

## New exact theorem

Define
`rho_+ = 273/225912500 = 0.0000012084324683229127...`.

For **every real** `z` with `|z_k|<=rho_+`:

1. All original capacity constraints, `g=b`, seedless-F, and both matched stopping-time equalities hold **if and only if** `m(z)>=0`.
2. At every physically lawful point there is a Blackwell transport; its minimum number of strictly positive edges is **exactly 14 when `m(z)=0`**, and **exactly 15 when `m(z)>0`**.
3. This is the **largest** `rho` for which `m(z)>=0` alone characterizes physical legality at *every point* of the entire eight-dimensional cube `|z_k|<=rho`. For each `rho>rho_+`, the point with `z=rho*(0,0,0,-1,-1,1,0,-79/260)` satisfies `m(z)=0`, while violating the source-defined 26th capacity slack.

The guaranteed cube radius grows from `1/10000000` to `273/225912500`, an exact factor of `(273/225912500)*10000000 = 218400/18073`. Its interior contains an 8D 15-edge lawful half-chamber and a 7D 14-edge boundary chamber.

At the critical parameter `z=rho_+*(0,0,0,-1,-1,1,0,-79/260)`, the two *independent* faces `mu_1=0` and target capacity `z_y+9 b_y/40-v_y=0` meet. The fixed 14 positive edges stay positive and all 13-edge candidates remain excluded: this is a lawful **14-edge/capacity-facet intersection**, not a 13-edge transition.

## Proof: sharp conditional cube via exact one-dimensional duality

For every capacity slack other than `mu_1`, write `s_i(z)=c_i+a_i.z`, `c_i>0`; the three permanent zero slacks are indices `4,15,23` and have identically zero tangent. Index `19` is precisely `mu_1=m(z)`. All these claims follow by differentiation of the immutable seven-node physical mass/capacity formulas in PR #1939. The 8D observation map still has rank 8.

For a positive-centered slack and the half-cube `m.z>=0`, exact finite-dimensional LP duality gives
```
min_{||x||_inf<=1, m.x>=0} a_i.x
  = - min_{lambda>=0} sum_{k=0}^7 |a_{ik}-lambda*m_k|
  =: -H_i .
```
The last one-dimensional convex piecewise-linear minimum is attained at `lambda=0` or a nonnegative breakpoint `a_{ik}/m_k`. Thus the exact sharp conditional radius for that slack is `c_i/H_i` (when `H_i>0`); all 26 slacks are handled by finite rational arithmetic.

The exhaustive 26-slack rational audit gives
```
min_{i != 19, c_i>0, H_i>0} c_i/H_i
 = 273/225912500, at i=25.
next smallest ratio = 17073/93775000, at i=2.
```
Here `s_25(0)=63/34100000`,
`a_25=(0,0,0,9/40,0,-1,0,1)`,
`m=(0,0,0,1/80,-1,0,0,13/4)`, and
`lambda=4/13` yields
`H_25=|23/104|+|4/13|+1=159/104`.
Consequently
`(63/34100000)/(159/104)=273/225912500` exactly. The normalized direction
`x=(0,0,0,-1,-1,1,0,-79/260)`
has `m.x=0` and `a_25.x=-159/104`, so the bound is attained; beyond it physical legality differs from `m>=0`.

For transport, preserve PR #1939's exact certificates:
- Other 14 fixed-basis weights are strictly positive throughout the cube, because their 8D positive-weight radius `50915668197609/1202833246639750000` exceeds `rho_+`. The remaining fixed-basis weight is `E_(1,3)=m(z)`.
- The ten edge-forcing dual inequalities hold when `||t*+z||_inf <= r*+rho_+ < 18052765669/423284426970000`.
- Every one of 3814 remaining four-column quotient supports is excluded on this cube by PR #1939's exact separation margin `49948501046391/3920403670319950000 > rho_+`; the 1031 support spans containing the central target impose precisely `m(z)=0`.
- On `m(z)=0`, use the PR #1939 seven-coordinate parametrization `u=(z0,z1,z2,z3,z5,z6,z7)`. It satisfies `||u||_inf<=rho_+`. Every three-column quotient support stays excluded because its exact separation margin `49948501046391/841518836618948125 > rho_+`.

Hence the 15-edge fixed basis is legal with all weights positive for `m>0`, and has exactly 14 positive weights for `m=0`. The finite exact exclusions prove those cardinalities are minimal for every lawful point. The locus `m=0`, `s_25=0` has two linearly independent normals within the eight tangent coordinates, so around the critical point it contains a six-dimensional affine slice of physically admissible fourteen-edge solutions.

## Reproduction and status

`VERIFY_HALF_CUBE.py` reproduces the physical linearization from the frozen rational `p0` and RREF tangent, verifies all 26 physical-slack conditional LP margins, the sharp rational radius and its explicit realizing direction, and compares the independently inherited Blackwell certificate radii. `EXACT_OUTPUT.txt` records the actually executed local Python/SymPy/Fraction audit. The full 4845+1140 quotient-support enumeration remains the cited immutable evidence in PR #1939; it is reused at the exact bound, rather than claimed to have been rerun here.

BRC use: retained all 30 candidate transfer-branch identities and exact rational masses in the parent model; quotient projection is used only for the scoped support-feasibility observation with its separately proved dual/linear-algebra certificates. The one-dimensional physical observer fiber and native X6 spatial directions are not identified or discarded.

Next discriminating unit: study the codimension-two `mu_1=s_25=0` junction and classify which further physical capacity faces or rank-two quotient support strata can meet it while preserving 14-edge minimality; construct a first *lawful* 13-edge contact if one exists. Formal owner/CLAIM and independent mathematical review require their own authority and remain separate from this author-side result.
