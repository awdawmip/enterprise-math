# R5: Explicit ten-edge affine G-face Blackwell lift for a full-dimensional middle-ratio region

Date: 2026-11-08 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. Scientific pins unchanged: global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Source model, seven likelihood nodes `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`, branch masses M and TP/TQ are in `RESEARCH.md`. This complements `LOW_RATIO_ALL_THETA.md`, which solves the full physical p/q/theta rectangle for eta<=1/40 by a different piecewise construction.

## Theorem: simple affine seedless lift and exact sharp inequalities for this map

Let `0<=eta<=85544/451695` and choose real `u,w,z` satisfying

```text
0 <= u <= min(13/40+eta/80, (556036-401539*eta)/1710880)
0 <= w <= min(3/40+21*eta/80, (128316-650499*eta)/1710880)
0 <= z <= min(1/10, (85544-451695*eta)/855440).
```

Define the lawful, saturated FULL_HIST flow
```text
x=(1,1,eta,u,9*eta/40+z,w,z).
```
Then the following **affine map** is a lawful G-face seedless LR flow:
```text
g'=a'=1-4469*eta/21386,    b'=0
u'=u+3357*eta/20128,        w'=w+124737*eta/342176
z'=v'=z+433819*eta/855440
y=(g',a',0,u',z',w',z').
```

Let `m_j=M_j(x)`, `c=140975*eta/1026528`, `d=16917*eta/42772`. Set the ten entries of the 7×7 matrix `Q[target_i,source_j]` as

```text
Q[0,0]=m0,        Q[0,1]=c,
Q[1,1]=m1-9*c/5,
Q[3,1]=4*c/5,     Q[3,3]=m3,
Q[4,4]=m4,        Q[4,5]=d,
Q[5,5]=m5-13*d/8,
Q[6,5]=5*d/8,     Q[6,6]=m6.
```

All other entries are zero. Then `Q>=0`, the seven **row masses** equal `M(y)`, the seven **column masses** equal `M(x)`, the seven likelihood-weighted P column masses equal `r_j M_j(x)`, and `TP(y)=TP(x)`, `TQ(y)=TQ(x)`. Consequently, for **every** `D in [0,1]^7`, transport `D'_i=sum_j Q[i,j]D_j/M_i(y)` on positive target rows (zero on empty rows) reproduces `(eP,eQ,TP,TQ)` exactly. The kernel is chosen independently of D. All real parameters including irrational and boundary values are covered.

For `0<=s<=g<=1`, combine this normalized triple with seedless identities at `E1=(1,0,0,0,0,0,0)` and `E0=(0,0,0,0,0,0,0)` using weights `s,g-s,1-g`, giving a corresponding theorem for `x_s=(g,s,s*eta,s*u,s*(9eta/40+z),s*w,s*z)`. All three target flows lie on G. The source-to-target interpolation `x_h=(1-h)x_s+h*y_s` for any `h in [0,1]` is handled with `Q_h=(1-h)Q_s+h*diag(M(y_s))`.

## Algebraic proof

For source column 1, `Q[0,1]+Q[1,1]+Q[3,1]=m1`, while the likelihood-weighted sum is `(1/10)c+(1/2)(m1-9c/5)+(4/5)c=(1/2)m1`. For column 5, `d+(m5-13d/8)+(5d/8)=m5`, and weighted sum `(5/4)d+(3/2)(m5-13d/8)+(19/10)(5d/8)=(3/2)m5`. Columns 0, 3, 4 and 6 transport diagonally; empty source column 2 has zero mass. Thus all Q and P column equations hold exactly.

The source branch mass formula substituted into the affine y above yields the seven exact row equations
```text
M(y)=(m0+c, m1-9c/5, 0, m3+4c/5,
      m4+d, m5-13d/8, m6+5d/8).
```
The same direct substitution yields the **identities in independent symbolic parameters** `TP(y)-TP(x)=0` and `TQ(y)-TQ(x)=0` for arbitrary real eta,u,w,z. No finite-grid assumption enters these equalities.

The target has `a'=g'`, `b'=0`, `v'=z'`, hence seedless residual zero. Its three potentially binding lawful/transport inequalities reduce **exactly** to
```text
13*g'/40-u' = m1-9c/5 = (556036-401539*eta-1710880*u)/1710880
3*g'/40-w'  = m5-13d/8 = (128316-650499*eta-1710880*w)/1710880
g'/10-z'    = (85544-451695*eta-855440*z)/855440.
```
These are nonnegative by hypotheses. All other target lower bounds hold because eta,u,w,z>=0, and `0<g'<=1` throughout the stated eta interval. All remaining Q entries are nonnegative because source x is lawful, c,d>=0. This proves the theorem; the three extra inequalities are necessary and sufficient for **this explicit map** given original source lawfulness.

## New middle-ratio open box

The theorem contains the entire four-dimensional rational box
```text
29/900 <= eta <= 31/900,
19/40 <= theta,p,q <= 21/40,
u=(13/40+eta/80)*p,
w=(3/40+21eta/80)*q,
z=theta/10.
```
This box lies inside the formerly uncovered ratio interval `1/40<eta<46/705`. At its worst-case upper corner `eta=31/900,theta=p=q=21/40`, the three lawful margins are strictly positive:
```text
13*g'/40-u' = 4498192477/30795840000,
3*g'/40-w'  = 182536139/10265280000,
g'/10-z'    = 1504501/51326400.
```
Each margin is monotone decreasing in eta and its associated p, q or theta coordinate, so the stated box is wholly covered, including its nonempty open interior. A separate certificate at `eta=1/30,theta=p=q=1/2` was independently found on **both** G and F faces (`MIDDLE_RATIO_TWO_FACE.md`).

`VERIFY_LINEAR_G.py` executes exact Python standard-library Fraction checks of **448** boundary/interior triples, all **16** box corners and the fixed double-witness mixed source; output is `EXACT_LINEAR_G_OUTPUT.txt`. The displayed algebraic row/column/time identities supply the proof for all real parameters. The theorem lives in the frozen finite P/Q-BRC statistical model with labeled branch masses; no new native six-axis X6 physical model is asserted. Formal Source Owner/CLAIM, review and mathematical admission remain unconfirmed.

## Next

Determine whether the overlapping G/F lift regions can be glued into the **entire** physical p/q/theta rectangle for `1/40<eta<46/705`. This exact ten-edge map provides an explicit interior core and inequality boundary for a broader face-switch search.
