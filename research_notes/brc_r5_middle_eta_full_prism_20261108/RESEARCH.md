# R5 — Complete physical side-capacity prism on a new middle-ratio interval

Date: 2026-11-08 (Asia/Shanghai). Scientific status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. Source pins frozen as in R5 predecessors: global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. This document is author-side mathematical evidence, not a native Result or ownership claim.

Previous verified author frontier: `research_notes/brc_r5_eta1over40_complete_pq_theta_20261108/RESEARCH.md` and `AFFINE_G_LINEAR_REGION.md` at commit `b16791024c053bb3afd1883d008855a8fb34ed14`. The former proves the whole prism for ratios `0<=eta<=1/40`. The latter provides a 10-edge lift on a smaller mixed middle-ratio interior box. **New result:** a complete physical `p/q/theta` prism throughout a *nondegenerate interval* of middle ratios.

## Model, exact domain, and theorem

Use the frozen seven-likelihood-node P/Q-BRC statistical model. Likelihood vector
`r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`.
For flow `f=(g,a,b,u,v,w,z)`, the seven Q-terminal masses are

```text
M0=509u/900+47z/180+67(v-z)/162+w/100
M1=13a/40+b/80-u
M2=(g-a)/2
M3=1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81
M4=(g-b)/2
M5=3a/40+21b/80-w
M6=u/100+47z/180+67(v-z)/162+509w/900

TP=1+g+3a/8+5b/8+u/2+v+3w/2
TQ=1+g+(a+b)/2+u+v+w
```

Lawful flows satisfy `0<=g<=1, 0<=a,b<=g`, `0<=u<=13a/40+b/80`, `0<=w<=3a/40+21b/80`, `0<=z<=a/10`, and `0<=v-z<=9b/40`. The seedless condition is `9bz=4a(v-z)`.

**Theorem (all-real middle-ratio prism).** For every choice of real parameters

```text
33/1000 <= eta <= 1/30
0 <= s <= g <= 1
0 <= theta,p,q,h <= 1
```

define

```text
x=(g,s,eta*s, s*(13/40+eta/80)*p,
   s*(9*eta/40+theta/10),
   s*(3/40+21*eta/80)*q, s*theta/10).
```

There exist a lawful seedless-LR target flow `y` and a nonnegative 7×7 calibrated Blackwell matrix `Q`, depending only on `eta,s,g,theta,p,q`, such that for `x_h=(1-h)x+h*y` and every terminal declaration `d in [0,1]^7`, the target can use
`d'_i=(sum_j Q_h[i,j]d_j)/M_i(y)` on positive-mass rows, otherwise zero, with `Q_h=(1-h)Q+h*diag(M(y))`. The four observations `(eP,eQ,TP,TQ)` match exactly between `(x_h,d)` and `(y,d')`. No declaration-specific optimization is used. Irrational parameter values, zero rows, and all closed boundary cases are included.

## Exact rational corner certificates

The attached `CERTIFICATES.json` holds **26 rational triples** `(x,y,Q)`: at each `eta∈{33/1000,1/30}`, both `theta∈{0,1/2}`, G-face vertices `(p,q)=(0,0),(1,0),(1,1)`, F-face vertices `(0,0),(0,1),(1,1)`, and one additional F-face vertex `theta=1/2,(p,q)=(1,0)`. Each record stores seven target coordinates and all nonzero entries of `Q[target_i,source_j]`; all missing edges are zero. The set contains **265 listed positive matrix entries**.

The two seedless linear faces are

```text
G: b=0, v=z
F: z=a/10, v-z=9b/40.
```

Every record passes the exact rational identities

```text
Q[i,j]>=0,    sum_j Q[i,j]=M_i(y),
sum_i Q[i,j]=M_j(x),
sum_i r_i Q[i,j]=r_j M_j(x),
TP(y)=TP(x), TQ(y)=TQ(x),
sum_i M_i(x)=sum_i M_i(y)=1,
sum_i r_i M_i(x)=sum_i r_i M_i(y)=1.
```

Both flows are lawful and the target lies on the indicated seedless face. Thus the declaration map is stochastic on each positive target row and preserves both decision errors. `VERIFY.py` independently checks every recorded identity using Python standard-library `fractions.Fraction`.

## Exact constructive proof for the continuum

Write `C=(x,y,Q)` for a calibrated triple. **Key closure:** nonnegative convex mixtures of triples from the *same face* are lawful, remain seedless, and preserve all linear mass, P-weighted column and stop-time equations. This is why both faces are used but never mixed with one another across a face switch.

1. **Ratio interpolation.** At each anchored `(face,theta,p,q)`, mix the two records for `eta_0=33/1000`, `eta_1=1/30` with nonnegative weights `1-lambda,lambda`, `lambda=(eta-eta_0)/(eta_1-eta_0)`. For fixed `p,q,theta`, the source is exactly affine in `eta`, so the mixed triple has the required new ratio and remains on the same seedless face.
2. **Early theta regime: `0<=theta<=1/2`.** Set `t=2theta`, interpolate each chosen same-face `theta=0` and `theta=1/2` vertex triple with weights `1-t,t`. If `q<=p`, choose face G and the triangle vertices `(0,0),(1,0),(1,1)` with barycentric weights `(1-p,p-q,q)`. If `q>=p`, choose F and vertices `(0,0),(0,1),(1,1)` with weights `(1-q,q-p,p)`. Both sets are nonnegative and reconstruct the original source. Either face works along the partition boundary `q=p`.
3. **Late theta regime: `1/2<=theta<=1`.** Use face F throughout. At `theta=1/2`, all four corners `(0,0),(0,1),(1,0),(1,1)` have F records, including the extra thirteenth certificate per eta. At `theta=1`, the source itself satisfies `z=a/10, v-z=9b/40` and is seedless; use `y=x,Q=diag(M(x))`. Interpolate in `theta` with weights `2-2theta,2theta-1`, and interpolate the four square corners with `((1-p)(1-q),(1-p)q,p(1-q),pq)`. All remain on F.
4. **Scaling and early-exit mix.** At the normalized level `g=a=1`. Mix the constructed triple with identical seedless triples at `E1=(1,0,0,0,0,0,0)` and `E0=(0,0,0,0,0,0,0)`, with respective weights `s,g-s,1-g`. These two identities lie on both G and F, so the face remains unchanged; the source becomes exactly the theorem's displayed `x`.
5. **Source-to-target interpolation.** Finally set `x_h=(1-h)x+h*y` and `Q_h=(1-h)Q+h*diag(M(y))`. The second triple is a calibrated identity at y, so the same-face closure proves calibration for every `h`. On positive target masses, row normalization defines stochastic `d'`; zero target rows carry no Q or P mass. Both errors and both stop times agree for every declaration.

These steps are explicit affine formulas whose weights remain nonnegative throughout the domain. The finitely many corner identities are exact rational equalities; therefore the conclusion holds for **all real** parameters, independently of the finite regression grid.

## Reproducible verification, evidence and limits

Locally constructed the 26 corners with an LP support search and exact SymPy rational reconstruction, then checked each resulting sparse matrix with independent exact Fraction conditions. The **deliverable checker** is a standalone standard-library program, reading `CERTIFICATES.json` and never invoking an LP solver. The local executable with equivalent verifier logic returned:

```text
EXACT_ANCHOR_PASS 26 SPARSE_EDGES 265
EXACT_GLUE_REGRESSION_PASS 9052
PASS_R5_MIDDLE_ETA_INTERVAL_COMPLETE_PHYSICAL_PRISM_ALL_REAL_CONSTRUCTION
```

`EXACT_OUTPUT.txt` records the actual local run. Finite regression tests are consistency checks; the mathematical all-real proof is the positive interpolation just given. The result concerns the *specified* finite seven-node frozen P/Q-BRC statistical observer map. It asserts no new primitive native six-axis X6 physical dynamics. The latest native service read in this session returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`; no active Source owner or native CLAIM was verified, so the record is portable author-side evidence awaiting independent mathematical review.

## Next discriminating question

Find full prism certificates for an adjacent **nontrivial ratio interval** on the left of `33/1000` or right of `1/30`, by permitting the triangular `q/p` switch and the `theta` switch to vary with eta. The current proof uses a fixed partition at `theta=1/2`, `q=p`; separate floating LP probes suggest its two critical F/G corner witnesses have different feasible ratio ranges beyond the current interval. An exact alternative partition or an additional seedless face could enlarge the proved union. Preserve the independent current seedless/FULL_HIST mother objective and the frozen scientific pins.
