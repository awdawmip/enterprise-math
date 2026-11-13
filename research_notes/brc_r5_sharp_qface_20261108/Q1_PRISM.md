# New R5 result: entire low-ratio q=1-capable three-parameter prism at negative residual

**Status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Date 2026-11-08. Scientific pins unchanged from PR #1802 (Global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`).

## Full all-real theorem

In the fixed seven-likelihood-ratio P/Q-BRC observer, for **every real**

```text
0 <= t <= 1/5,    0 <= p <= 1,    0 <= q <= 1
theta = 1/4,      kappa = 3/4,    g = b = 1, a = t,
```

the lawful source

```text
x(t,p,q) = (1, t, 1,
    (13t/40 + 1/80)*p,
    t/40 + 27/160,
    (3t/40 + 21/80)*q,
    t/40)
```

has a lawful seedless LR target `y` on the single **common** chart

`C_(3/4) = {z'=3a'/40, v'-z'=27b'/160}`

and a nonnegative declaration-independent `7x7` Blackwell matrix whose seven Q-mass rows, seven source columns, seven r-weighted source columns, and two stopping times match exactly. Thus all `(eP,eQ,TP,TQ)` are preserved for arbitrary terminal declarations, including along the source-target convex interpolation.

The source history residual is

`R = 9*b*z - 4*a*(v-z) = 9*t*(theta-kappa)/10 = -9t/20`,

strictly negative for `t>0`. This is a nontrivial **three-parameter full physical (p,q) capacity rectangle**, including `q=1` previously beyond the PR #1802 box `q<=3/4`; it is not merely a single extremal corner.

## Eight exact endpoint witnesses and all-real extension

At `t=0`, every source `x(0,p,q)` lies on `C_(3/4)` and is already seedless. For `p,q in {0,1}`, take `y=x` and the diagonal kernel `Q_ij=delta_ij*M_i(x)`. These are four exact vertices.

At `t=1/5`, `p,q in {0,1}`, the companion `VERIFY_Q1_PRISM.py` supplies **four fully explicit rational targets and kernels**, with respectively 10, 9, 9 and 9 strictly positive transport entries (37 total). A self-contained exact Fraction runner imports only the frozen observer definitions from the adjacent `VERIFY.py` and checks every physical bound, seedless equation, all Q/P mass equations and stopping times. All eight vertices passed.

The source is separately affine in `t,p,q`: the only products are `tp`, `tq`, so the source admits the standard three-fold multi-affine corner decomposition

```text
x(t,p,q) = sum_(e_t,e_p,e_q in {0,1}) W_e * x_e
W_e = (s if e_t else 1-s)*(p if e_p else 1-p)*(q if e_q else 1-q)
s = 5t.
```

Set `y=sum W_e*y_e`, `Q=sum W_e*Q_e`. The common chart is linear in target-flow coordinates, physical inequalities are affine, masses and times are affine, transport equations are linear, and all `W_e>=0` sum to one. Therefore this proves the stated **entire real prism**, not just rational samples. The same diagonal mixture construction applies for any `h in [0,1]`.

The executed `VERIFY_Q1_PRISM.py` checked the eight exact vertices and 601 additional rational triples; actual stdout is in `EXACT_Q1_OUTPUT.txt`. These checks validate the witnesses and implementation; universal quantification is justified by the displayed analytic multi-affine proof.

## Boundary and next unit

This result fixes `theta=1/4,kappa=3/4`. No full `[0,1]^2` theta/kappa extension or all legal FULL_HIST claim is made. For `kappa=1/4`, the fixed chart `C_(3/4)` has the sharp q threshold in `RESEARCH.md`, while another chart is needed above it. Next test neighboring `theta` values and find a common chart or a rigorously justified chart partition; preserve the exact source/target, observation and future-operation scope. No P000/worldview edits; no native CLAIM, mathematical review or admission implied.
