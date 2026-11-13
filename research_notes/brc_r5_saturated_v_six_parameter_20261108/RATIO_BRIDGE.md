# R5 — Complete physical side capacities over the continuous ratio bridge 1/2 ≤ b/a ≤ 1

Date 2026-11-08 Asia/Shanghai; author-side exact theorem and executed Fraction verification. Scientific pins unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. This extends the adjacent `RESEARCH.md` (`b/a=1/2`) and the immutable `194f81437a86b5fa24947d3dedd3e0f9bfed03be:research_notes/brc_r5_full_side_rectangle_20261107/` (`b/a=1`), using their **actual rational calibrated Blackwell certificates**. All conclusions use the same frozen seven-likelihood-key four-stage P/Q-BRC observer.

## Seven-parameter all-real theorem

For **every** real `0<=s<=g<=1`, `1/2<=eta<=1`, `0<=p,q,theta,h<=1`, put

```
a=s; b=eta*s;
u=s*(13/40+eta/80)*p;            // entire physical u capacity
w=s*(3/40+21*eta/80)*q;         // entire physical w capacity
z=s*theta/10;
v=9*eta*s/40+z;                 // v-z = 9b/40 (saturated)
x=(g,a,b,u,v,w,z).
```

There exists one **legal seedless LR** target flow `y`, independent of the declaration, and a calibrated nonnegative seven-by-seven Blackwell Q-mass transport `Q` with exactly equal stopping times. For every `d in [0,1]^7`, the transformed randomized declaration matches the entire tuple `(e_P,e_Q,T_P,T_Q)` of the FULL_HIST flow `x`. The same `y` also covers every `x_h=(1-h)x+h*y` with `0<=h<=1`, using `Q_h=(1-h)Q+h*diag(M(y))`.

This covers the complete physical `(u,w)` capacity rectangle at **every intermediate real ratio** `eta=b/a in [1/2,1]`, the entire `z in [0,s/10]` saturated-v interval, the full early continuation cone `0<=s<=g<=1`, and an additional source-to-lift interpolation coordinate. At `s=0` the source and lift remain well defined.

The original source's exact historical residual and stopping times are:

```
R(x)=9*b*z-4*a*(v-z) = (9/10)*eta*s^2*(theta-1) <= 0,
T_P(x)=1+g+(15+34*eta)*s/40+u/2+3*w/2+z,
T_Q(x)=1+g+(20+29*eta)*s/40+u+w+z.
```

## Exact proof

Let `t=2*eta-1 in [0,1]` and `lambda_ij` denote the four nonnegative bilinear weights in `p,q`: `(1-p)(1-q),p(1-q),(1-p)q,pq`. The `b/a=1/2` predecessor supplies four rational corner FULL_HIST flows `c^L_ij`, seedless targets `y^L_ij` and nonnegative Q-mass matrices `Q^L_ij`. The `b/a=1` predecessor similarly supplies `c^H_ij,y^H_ij,Q^H_ij`. Their Q/P row-column identities, legal flow constraints and stopping time equalities are exact checked rational identities. Both target families lie on the **same affine seedless face**

`F={legal f: z=a/10 AND v-z=9b/40}`.

At every corner define the interpolated triple

`c_ij(t)=(1-t)c^L_ij+t c^H_ij`,
`y_ij(t)=(1-t)y^L_ij+t y^H_ij`,
`Q_ij(t)=(1-t)Q^L_ij+t Q^H_ij`.

These are legal, calibrated, stop-time matching triples. In particular `c_ij(t)` has `(g,a,b)=(1,1,eta)` and side flows equal to 0 or to the *interpolated physical capacity*. This last fact is exact because both physical side capacities are affine functions of `b`: `u_max=13a/40+b/80` and `w_max=3a/40+21b/80`. Thus bilinear interpolation with `lambda_ij` fills the entire physical rectangle independently in `u,w`.

For the positive-z endpoint put
`c^+_ij(t)=c_ij(t)+(0,0,0,0,1/10,0,1/10)`.
This flow is legal, satisfies `z=a/10`, `v-z=9b/40`, and therefore **itself lies in F**; use its diagonal identity matrix `diag(M(c^+_ij(t)))` as its calibrated transport.

Introduce two baseline seedless flows `E0=(0,0,0,0,0,0,0)` and `E1=(1,0,0,0,0,0,0)`, with identity transports. Combine the sources with weights

`1-g` on E0; `g-s` on E1; `s*lambda_ij*(1-theta)` on c_ij(t); and `s*lambda_ij*theta` on c^+_ij(t).

All weights are nonnegative and sum to one. Direct coordinate comparison gives **exactly** the displayed `x`, including `v=9*eta*s/40+z` and both independent physical side-flow maxima. Construct `y` with the *same weights*, replacing each `c_ij(t)` by `y_ij(t)`, and leaving E0,E1,c^+ unchanged. All its ingredients belong to F, so `y` is legal and seedless for arbitrary real parameters; the general quadratic seedless manifold is not assumed convex.

Construct `Q` by the *same convex combination* of the eight old corner transport matrices and the appropriate diagonal matrices. Because stopping masses `M(f)` and times `T_P(f),T_Q(f)` are affine in the flow, and because every component matrix obeys

`sum_j Q[i,j]=M_i(y)`,
`sum_i Q[i,j]=M_j(x)`,
`sum_i r_i Q[i,j]=r_j*M_j(x)`

at its own endpoints, all identities hold exactly for the new `Q`. Nonnegativity and normalization are preserved. For `x_h=(1-h)x+h y`, substitute `Q_h=(1-h)Q+h diag(M(y))` to preserve the same row target and the columns of `x_h`. Normalize the positive-mass target rows into a stochastic kernel `K_h`; zero rows can be any stochastic row. For any real `d in [0,1]^7`, `K_hd` remains a legitimate declaration, and the two calibrated column identities preserve both error probabilities. Both stopping times coincide. This proves the full **seven-real-parameter** statement, including irrational values and boundary cases.

## Explicit intermediate-ratio witness

For `g=s=p=q=1`, `eta=3/4`, `theta=1/2`, `h=0`:

```
FULL_HIST x=(1,1,3/4,107/320,7/32,87/320,1/20)
seedless  y=(79/80,233/240,61/80,6241/19200,2579/9600,4841/19200,233/2400)
(T_P,T_Q)=(291/80,37/10), R(x)=-27/80, R(y)=0.
```

Both early side-flow coordinates attain their individual physical capacity maxima for this exact intermediate `b/a=3/4` ratio. The source has `z>0` and strict negative historical residual.

## Reproduction / evidence

`BASE_CERTIFICATES.py` copies the immutable `b/a=1/2` exact rational matrices; `BASE_ETA1_CERTIFICATES.py` copies the immutable `b/a=1` exact rational matrices; `VERIFY_ETA.py` checks both sets, constructs the full interpolated seven-by-seven matrix, and validates **2187** exact Fraction cases on the six-dimensional parameter grid (`g,s,t,p,q,theta,h`, with s chosen from 0,g/2,g). Each case checks legal flow, affine seedless face, residual, full 7 row/7 Q-column/7 P-column calibration, nonnegativity, normalized measures, both times, the h extension and three declaration tests. The analytic convex proof, with the eight exact predecessor matrices, establishes all-real coverage; 2187 checks are regression evidence.

`EXACT_ETA_OUTPUT.txt` captures a locally executed reconstruction of the two predecessor certificate checkers plus the new `VERIFY_ETA.py`; the remote predecessor files were copied verbatim from immutable GitHub blobs, while the locally reconstructed predecessor code may differ in formatting. Consequently, the stdout is sourced to the local reconstruction rather than represented as an execution of the remote source bytes. Final source file readbacks establish remote preservation.

No theorem admission or authenticated current task CLAIM is asserted. This is a research proof for randomized terminal declarations and the stated four observers, while the broader R5 mother question remains open.

## Next discriminating test

The entire saturated-v physical side-capacity region for `1/2<=b/a<=1` is now covered. The next independent source family is `0<b/a<1/2`, where the `b=0` seedless edge does not automatically share the specific face F for `z<a/10`. Seek a common-face Blackwell lift at a rational `b/a=1/4`, first at `z=0`, `p=q=1`, then try the full rectangle. In parallel, vary unsaturated `v-z<9b/40` to test the face method's reach.
