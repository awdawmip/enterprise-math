# R5: a genuine two-dimensional physical family of ≤14-edge Blackwell transports

**2026-11-09, author-side exact proof.** Model: frozen seven-LR-node P/Q-BRC statistic, a restricted observer of Heartbeat/X6. Frozen science pins: global `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`, unchanged. Direct predecessor: [PR #1843](https://github.com/awdawmip/enterprise-math/pull/1843), scientific commit `7244646fed297cc29e2af74755c3fe909c21ff01` and its four exact 14-edge endpoint coupling certificates. This construction reuses them without modifying their claims.

## Theorem: closed 2-dimensional 14-edge atlas wedge

For every pair of **real** parameters
[
0lelambdale 1,qquad 0ledeltale (1-lambda)/1000,
]
there are lawful FULL_HIST source and lawful seedless LR target strategies
[
x(lambda,delta)=(1-lambda)X_0+lambda X_1+delta D_X,quad
y(lambda,delta)=(1-lambda)Y_0+lambda Y_1+delta D_Y,
]
such that both stopping times match and there exists a nonnegative, declaration-independent seven-node Blackwell Q transport with **at most 14 positive edges**. Hence every random terminal declaration on these LR nodes has the same observer tuple ((e_P,e_Q,T_P,T_Q)) under the transported experiment.

The two existing source/target pairs ((X_0,Y_0),(X_1,Y_1)), LR ratios (r=(1/10,1/2,3/4,1,5/4,3/2,19/10)), and literal 14-edge rational vectors `A0, AH, BH, B1` are bundled in the self-contained `VERIFY_2D.py` (original exact predecessor script followed by this extension).

The new transverse flow directions in coordinate order ((g,a,b,u,v,w,z)) are
[
D_X=rac1{1111424393}(-1802718000,-1802718000,-1802718000,-608417325,-496963350,-608417325,0)
]
and
[
D_Y=rac1{3761}(-6000,-6000,-6000,-2025,-1950,-2025,-600).
]
Define a signed diagonal matrix (D) with (D_{00}=D_{66}=-1/2, D_{33}=1) and all other entries zero. Since the LR nodes satisfy ((r_0+r_6)/2=r_3=1), this center-concentration operation preserves normalization and the LR weighted mean.

**Explicit certificate atlas.** On (lambdain[0,1/2]), use support (S_A) with
[
E^A(lambda,delta)=(1-2lambda)A0+2lambda AH+delta D.
]
On (lambdain[1/2,1]), use support (S_B) with
[
E^B(lambda,delta)=(2-2lambda)BH+(2lambda-1)B1+delta D.
]
Here `A0,AH,BH,B1` denote their matrices, with the source script's explicit ordered supports. (D)'s three diagonal positions occur in both supports.

## Exact proof

1. The predecessor verifies all 21 row/column/LR-moment equalities for the four unperturbed rational matrices and the lawful source, seedless target, P/Q normalization and two stopping times.
2. By direct substitution into the frozen affine mass map (M),
[
M(X_0+D_X)-M(X_0)=M(Y_0+D_Y)-M(Y_0)=(-1/2,0,0,1,0,0,-1/2).
]
The two stopping-time increments agree. The source direction retains (g=b); the target direction retains the **linear F-face seedless constraints** (z'=a'/10) and (v'-z'=9b'/40). Consequently the two transport matrices above satisfy all 21 equalities **identically for every real ((lambda,delta))** whenever their entries are nonnegative.
3. Nonnegativity and all physical capacities are affine inequalities. Check the seven rational chart vertices: `A0, AH, BH, B1` at ((0,0),(1/2,0),(1/2,0),(1,0)), `A0top` at ((0,1/1000)), and the two chart copies `AHtop,BHtop` at ((1/2,1/2000)). The bundled Fraction checker confirms every vertex satisfies the complete physical inequalities and the exact 21 transport equations.
4. The left region (0lelambdale1/2, 0ledeltale(1-lambda)/1000) is the convex quadrilateral with vertices ((0,0),(0,1/1000),(1/2,1/2000),(1/2,0)), handled by (S_A). The right region (1/2lelambdale1) is the triangle ((1/2,0),(1/2,1/2000),(1,0)), handled by (S_B). Affinity and convexity extend the exact corner checks to **all real parameters**, including irrational points and the common chart interface.
5. The family has genuine dimension two even after retaining only marginal information. Let (
u=M(x)), (mu=M(y)). Directly:
[
rac{partial 
u_0}{partialdelta}=-rac12,quad
rac{partialmu_1}{partialdelta}=0,quad
rac{partialmu_1}{partiallambda}=-rac{367}{24000}.
]
Thus
[
detrac{partial(
u_0,mu_1)}{partial(lambda,delta)}
=-rac{367}{48000}
e0.
]
So this is a two-dimensional family in the statistical marginal pair itself, beyond a mere reparameterization of the predecessor's segment. The domain has nonempty relative interior.

This completes the exact author-side proof in the frozen statistical model; independent mathematical review and project Result admission are separate.

## Reproduction and evidence

`VERIFY_2D.py` is **standalone** and imports only Python's standard-library `fractions.Fraction`. Execute `python VERIFY_2D.py`. It contains the full preceding certificate table plus this independent analytic extension and seven exact vertex checks; the saved `EXACT_OUTPUT.txt` is the local execution output. Every 21-equation test is exact rational arithmetic. The continuum follows from the displayed affine identities and verified convex vertex coverage, not an inference from sampling.

## Next discriminating scientific unit

Extend the fan into a positive-width region at (lambda=1) by finding an independent lawful transverse direction compatible with the active (gle1) and (zle a/10) facets, with a nonnegative (S_B) or a new ≤14-edge support. If this is obstructed on a fixed support, seek a second support chart or a precise facet certificate. The stronger mother question remains a finite ≤14-edge atlas for all physically lawful (g=b) pairs (or an exact physical 15-edge lower-bound witness). Frozen R5 full-model coverage PR #1831 still awaits independent verification.

## Research/control status

This is an **author proof with executed exact arithmetic**, not a native Task Result. The private backend `em_session_start` and `em_control_tasks` returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE`, `operation_sent=false` in this run, so live Owner/CLAIM, native Researcher-ID and canonical activity registration could not be verified. Source publication here is scoped to an author evidence branch/PR.
