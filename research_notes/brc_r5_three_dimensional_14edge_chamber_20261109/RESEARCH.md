# R5 — An exact three-dimensional 14-edge physical Blackwell chamber

Date: 2026-11-09 (Asia/Shanghai). Status: **author-side exact derivation and Fraction vertex tests; independent review pending**.

## Provenance and frozen scientific input

This is an incremental extension of the precise two-dimensional construction and endpoint certificates in [PR #1845](https://github.com/awdawmip/enterprise-math/pull/1845), immutable predecessor commit `0fe08cc4c1a30b9c5e898eedb01f2e0ba7238c7f`, notably `research_notes/brc_r5_two_dimensional_14edge_fan_20261109_t11/VERIFY_2D.py`. The predecessor pins its science at GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`; these remain the input pins. Applicable current behavioral rules are read separately. This statistical seven-LR-node P/Q-BRC problem is a declared observer/restricted model within Enterprise Math, not an identification of all X6 internal states.

## New exact theorem

Let the source and target flow coordinates be `(g,a,b,u,v,w,z)`; take the predecessor's exact `X0,X1,Y0,Y1,A0,AH,SA,DX,DY,K` with the same seven likelihood-ratio nodes
`r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`.
Write `DX2=DX-K` and the signed diagonal transport direction
`D_{0,0}=D_{6,6}=-1/2, D_{3,3}=1`.

Define two new rational physical-flow increments:

```text
HX = (-821541312/1111424393, -3044390098/1111424393,
      -821541312/1111424393, -3998784193/4445697572,
      -339119685/1111424393, -1775935407/4445697572, 0)
HY = (-7832/11283, -30398/11283, -7832/11283,
      -13303/15044, -4802/11283, -5781/15044, -15199/56415)
```

Let `H` have exactly three nonzero entries:

```text
H[0,0] = -23/36
H[6,6] = -13/36
H[2,2] = 1
```

**Theorem.** For every real triple in the closed box

```text
1/5 <= lambda <= 3/10
1/480 <= delta <= 1/160
-1/1000 <= eta <= 1/1000
```

the following flows are physically lawful FULL_HIST source and seedless F-face LR target, respectively:

```text
x = (1-lambda)*X0 + lambda*X1 + delta*DX2 + eta*HX
y = (1-lambda)*Y0 + lambda*Y1 + delta*DY  + eta*HY
```

The 14-entry coupling `E` on the predecessor support `SA` is

```text
E = (1-2*lambda)*A0 + 2*lambda*AH + delta*D + eta*H.
```

Every one of these 14 edges is **strictly positive** throughout the box. The coupling fulfills the 21 exact mass/likelihood-ratio moment equations, both P/Q normalizations, and equal stopping times. Hence all seven-node randomized terminal declarations are matched by a declaration-independent Blackwell transport (with the predecessor's established transport orientation).

The image in the marginal-pair observer space is genuinely three-dimensional: with `nu=M(x)` and `mu=M(y)`, the selected-coordinate Jacobian is

```text
det d(nu[0],mu[1],nu[2]) / d(lambda,delta,eta)
  = -367/48000 != 0.
```

This extends the previously constructed 2D statistical region to a positive-volume 3D local chamber.

## Exact proof

1. **Affine coupling direction.** The exact frozen mass and time maps give
   `M(X0+HX)-M(X0)=M(Y0+HY)-M(Y0)=(-23/36,0,1,0,0,0,-13/36)` and `T(X0+HX)-T(X0)=T(Y0+HY)-T(Y0)`.
   Moreover `HX[g]=HX[b]`, `HY[z]=HY[a]/10`, and `HY[v]-HY[z]=9*HY[b]/40`. Thus the source remains `g=b` and the target remains on the seedless F face. The signed `H` has zero total mass and likelihood-ratio weighted sum:
   `-23/36-13/36+1=0` and `-(1/10)*(23/36)-(19/10)*(13/36)+3/4=0`.
   Since `H` is diagonal, all its column moment constraints hold entrywise. In particular its support is a subset of `SA`.

2. **Eight exact corners.** At the 8 Cartesian products of the 2 endpoints in each of `lambda,delta,eta`, the companion script `VERIFY_3D.py` checks all source and target physical-capacity inequalities, target F-face identities, two stopping-time equalities, P/Q normalization and the entire 21-equation coupling system with exact rational fractions. At every corner the 14 weights are strictly positive. The smallest of all 112 corner weights is exactly `36079/6240000>0`. All nonstructurally-zero physical slacks are nonnegative.

3. **All-real interpolation.** Each physical capacity slack, each coupling weight, each mass/time equality and each face equation is affine in the 3 parameters; vertexwise nonnegativity propagates to the entire convex box. The equalities were also verified as directions and therefore hold as affine identities. Since every corner edge is positive, the same 14-edge support stays strictly positive on the complete closed box.

4. **Three independent statistical directions.** For the selected observer coordinates, the derivative columns for `lambda,delta,eta` have the form
   ```text
   lambda: (-59719/1080000, -367/24000, 203/6000)
   delta:  (-1/2,             0,             0)
   eta:    (-23/36,           0,             1)
   ```
   Their determinant is `-367/48000`. The image has dimension three in this affine marginal coordinate projection.

All mathematical calculations use the standard-library `fractions.Fraction` code in `VERIFY_3D.py`, importing only exact frozen predecessor certificates from the adjacent predecessor research directory. No floating-point feasibility solver or numerical extrapolation is used in this proof.

## Scope, control state and next problem

The theorem constructs one explicit, nondegenerate 3D physical chamber with exactly 14 positive edges. It advances the R5 physical sparsity atlas question: determine whether several such chambers cover the full lawful `g=b` time-matched seedless class or whether a lawful pair requires 15 edges. A concrete next exact test is to seek an additional independent diagonal mass-preserving direction, or a mixed edge direction supported by `SA∩SB`, that remains feasible at a chart interface. Independent audit of the full-model R5 author proof in PR #1831 is a separate outstanding work unit.

This note and verifier are research evidence on a noncanonical review branch. A native service-issued session and formal Task CLAIM were still pending when the mathematical work was performed; no operational Result or admission is inferred.
