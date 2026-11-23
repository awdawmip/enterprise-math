# X6 R154 — exact two-parameter fourfold BRC entry cusp near (B,D)=(20,188)

Date: 2026-11-24 (Asia/Shanghai). Evidence: **author analytic affine-vertex proof + complete 1,935-direction exact rational certificate PASS**; independent mathematical review **NOT_REVIEWED**. Native Result/Review not submitted.

## Frozen model and scope

Continue R153 at `enterprise-math@c45b2c84c88b29df510c79186840ab24103295cd:research_notes/portable_direct/2026-11-24_r2_x6_r153_B20_complete_lower_D_ray.md`. Frozen science inputs remain R121 `8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd` and R122 `0687aa24f5402da3b35f914dd6907967a9805b94`. P000 V5 and ACTIVE Heartbeat World apply. This is the existing *conditional static centered-three-axis, six-pair joint BRC observer*, not native time dynamics or physical residual attribution. The experiment uses only exact rational arithmetic on declared observer gaps.

As in R153, the complete population is the 1,935 unoriented nonzero integer triples `(x,y,z)` of Port `q<=10`, identifying only `v,-v`; for `h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)` use **all six** pair differences. For weight vector `(136,B,176,D)`, capacities are `s=(136+B,312,136+D,B+176,B+D,D+176)`. The score is `F_v=max_j(g_j(v)/s_j)`, optimum `eta=min_v F_v`, and strict-near set `N={v:2F_v<3eta}`.

## R154 local cusp theorem (all real parameters, including boundaries)

On the closed rectangle

```
19 <= B <= 21,          187 <= D <= 189
```

the **exact optimum** is

```
eta(B,D) = max(3/(136+B), 1/52)
         = 3/(136+B)  for 19<=B<=20,
         = 1/52       for 20<=B<=21.
```

Let `U=(4,-4,1)`, `V=(6,-1,0)` and the four directions
`A=(1,0,0)`, `C=(5,-4,1)`, `K=(5,-1,0)`, `H=(9,-5,1)`. Define

```
T(B) = (B+544)/3   for 19<=B<=20,
     = 208-B       for 20<=B<=21.
```

Then the complete strict-near set is exactly

```
N(B,D) = {U,V} union ( {A,C,K,H} if D>T(B), else empty ).
```

All four directions A,C,K,H enter **simultaneously** throughout both branches. At D=T(B) they have score exactly `(3/2)eta`, hence are excluded by the strict criterion. The two walls meet at **(20,188)** with slopes **+1/3** on the left and **-1** on the right, providing a genuine two-parameter cusp in the entering-member boundary. Throughout this rectangle the near-count is only 2 or 6; the point `(20,188)` is the R153 fourfold contact.

## Proof — finite uniform affine certificates

(1) The direction `V=(6,-1,0)` has gap vector `(3,6,3,3,0,3)`; all its score terms are at most `max(3/(B+136),6/312)` throughout the rectangle, and those two terms attain the maximum. Thus `F_V=eta_{candidate}` everywhere.

(2) Divide the rectangle into two closed subrectangles `R_-=[19,20]x[187,189]`, `R_+=[20,21]x[187,189]`. On each, the candidate eta is a single rational quotient with affine denominator or the constant `1/52`. For a fixed gap component `g_j/s_j`, either comparison `g_j/s_j >= lambda*eta` or `g_j/s_j < lambda*eta` (lambda=1 or 3/2) becomes an **affine inequality in (B,D)** after multiplying by its positive denominators. An affine inequality verified at the four rectangle vertices holds throughout the rectangle. Strict inequalities at all vertices are strictly valid throughout the rectangle, too.

(3) For every one of the **1,934** vectors other than V, the checker finds a fixed gap index j with `g_j/s_j>=eta` at all four corners of each subrectangle. Hence `F_v>=eta` globally. Together with V, this proves the optimizer formula without sampling extrapolation.

(4) Exclude the six named candidate vectors from the full 1,935 population. For each of the remaining **1,929** vectors, the checker finds a fixed gap index j with `g_j/s_j >= 3eta/2` at all four vertices, separately for R_- and R_+. This is an exact and complete no-outsider certificate. The lexicographically first witnessing component histograms by subrectangle are:

```
R_-: [1709,139,77,1,2,1]  (sum 1929)
R_+: [1709,162,56,0,2,0] (sum 1929)
```

(5) Each of the six components of U,V is `<3eta/2` at every subrectangle vertex, so U,V are near everywhere. For each A,C,K,H, all components **except the fifth pair** are uniformly strictly below `3eta/2` by the same vertex test. Their fifth-pair gap equals six, and their only remaining condition is `6/(B+D)<3eta/2`. Substituting the piecewise exact eta yields `D>(B+544)/3` on the left and `D>208-B` on the right. This proves the complete set formula and the exact strict-equality behavior.

## Actual exact execution / reproducibility

Self-contained Python standard library Fraction checker:
`research_notes/portable_direct/x6_r154_B19_21_D187_189_cusp_verify.py`, Git blob SHA1 `132792d2b54a096544feb612ae5ca91ac65ade00`.

Executed locally on 2026-11-24 and the identical exact Git blob verified on remote main:

```
R154 EXACT TWO-PARAMETER CUSP CERTIFICATE PASS
complete_directions 1935 outsider_fixed_gap_certificates 3858
witness_histograms_by_B_rectangle [[1709,139,77,1,2,1], [1709,162,56,0,2,0]]
entry walls: D=(B+544)/3 for 19<=B<=20; D=208-B for 20<=B<=21
```

The proof of all-real parameters is the positive-denominator affine-vertex criterion plus the exhaustive fixed-gap integer certificate. Rational point replays additionally check the exact cusp and boundary equalities.

## Relation to earlier work and next question

R153 first identified the fourfold entry at the fixed B=20 ray. R154 shows it persists as a two-parameter simultaneous entry on an explicit positive-area rectangle, rather than splitting under these small B perturbations; the *entry threshold surface* acquires two affine slopes at B=20. The six-pair static observer/Port remain unchanged. Next: maximize the rectangular parameter domain or resolve other lower-D chambers for variable B, then connect to R152's D>=528 atlas. Independent mathematics review and any native physical transfer remain separate open tasks.
