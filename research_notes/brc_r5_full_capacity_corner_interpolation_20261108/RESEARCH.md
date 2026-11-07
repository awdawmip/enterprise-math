# R5 — exact full-capacity Blackwell rectangle

Date: 2026-11-08 (Asia/Shanghai). Frozen scientific input pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`, unchanged. Direct predecessor: `935e1ca8111ed76b7cccbf4d928978da2eb9a5ba` at `research_notes/brc_r5_positive_residual_two_edge_20261108/SIDE_RECTANGLE.md`. P000/worldview unchanged. Author mathematical evidence, not independently reviewed or canonically admitted.

## All-real theorem

In the frozen four-stage seven-likelihood-key P/Q-BRC model, use `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. For every real `0<=u<=U=1571/4960`, `0<=w<=W=951/4960`, `0<=t<=1`, let
```
x(u,w)=(1,1,1/2,u,9/80,w,0)
y(u,w)=(89/93,89/93,85/186,u,1477/7440,w,89/930)
x_t=(1-t)x+t*y
```
(coordinates `g,a,b,u,v,w,z`). The source `x_t` and one legal seedless LR target `y` achieve **exactly the same four observations `(e_P,e_Q,T_P,T_Q)` for every real declaration `d in [0,1]^7`**, after a stochastic target declaration map. The same target flow and calibrated kernel work for all declarations. The `(u,w)` region strictly contains the predecessor's rectangle `U_old=503/1600, W_old=32383/175840` in both directions.

## Complete mathematical proof

The legal flow inequalities, seven stopping Q-mass formulas `M_i`, and times are reproduced verbatim from the predecessor in `VERIFY.py`. In particular,
```
0<=a,b<=g<=1; 0<=u<=13a/40+b/80; 0<=w<=3a/40+21b/80;
0<=z<=a/10; 0<=v-z<=9b/40
T_P=1+g+3a/8+5b/8+u/2+v+3w/2
T_Q=1+g+(a+b)/2+u+v+w
R=9bz-4a(v-z).
```
At each of the four `(u,w)` corners, `x` and `y` are legal, their stopping times agree, and `R(x)=-9/20, R(y)=0`. The new target saturates its *two side-flow capacities simultaneously* at `(U,W)`:
```
13*(89/93)/40+(85/186)/80 = 1571/4960
3*(89/93)/40+21*(85/186)/80 = 951/4960.
```
All flows and mass maps are affine in the side-flow parameters.

`VERIFY.py` contains four explicit nonnegative rational 7x7 matrices `Q00,Q10,Q01,Q11` (target rows, source columns) stored as sparse lists of respectively 14,13,13,10 nonzero edges. For each corner, exact rational arithmetic verifies:
```
sum_j Q[i,j]         = M_i(y)
sum_i Q[i,j]         = M_j(x)
sum_i r_i * Q[i,j]   = r_j * M_j(x).
```
For arbitrary real `u,w`, write `p=u/U`, `q=w/W` and set
```
Q(u,w)=(1-p)(1-q)Q00+p(1-q)Q10+(1-p)q Q01+p q Q11.
```
This matrix is nonnegative. Each calibration identity is affine in `u,w`, so exact agreement at four corners implies exact agreement for every real point by bilinear interpolation. Legality at the corners implies legality throughout their convex rectangle. The target is seedless because `z=a/10` and `v-z=9b/40`, hence `9bz=4a(v-z)`.

For `t in [0,1]`, let `Q_t=(1-t)Q(u,w)+t diag(M(y(u,w)))`. Its rows are `M(y)`; its Q and likelihood-weighted P columns are precisely `M(x_t)` and `r*M(x_t)`. Set `k_i=(sum_j Q_t[i,j] d_j)/M_i(y)` when `M_i(y)>0` and `k_i=0` otherwise. By positivity and row sums, `k_i in [0,1]`. The column identities prove equality of both Q and P declaration probabilities; times match by affinity. This proves the claim for **all real `u,w,t,d`**, not merely sampled rational parameters. Direct substitution yields `R(x_t)=-3(t-1)(8t-93)/620 < 0` for `0<=t<1`.

## Restricted-face maximality

Within the specific target ansatz `y=(g,a,b,u,a/10+9b/40,w,a/10)`, matching the source's two stopping times forces `a-b=1/2` and `g=89/40-(53/40)a`. The bound `g>=a` forces `a<=89/93`. Both side capacities are strictly increasing in `a`, so `U,W` are simultaneous maxima **within this ansatz**. The four exact matrices establish attainment. Targets with redistributed side flows or other seedless faces remain open.

## Computation, provenance and next

The corner certificates were discovered through a numerical feasibility search then solved exactly over rationals and independently checked by exact row/Q-column/P-column identities. The local `fractions.Fraction` checker was actually run, and its captured output is `EXACT_OUTPUT.txt`: four exact certificates and 125 exact rational regression triples. The universal proof is algebraic, not inferred from testing. This is model-internal P/Q-BRC arithmetic, with no native-heartbeat π/trigonometric/propagator computation. Status: `AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

Next: allow target `u',w'` to differ from source `u,w` and search a strictly larger flow/transport region toward the physical capacities `53/160,33/160` or a scoped exact obstruction. The mother question remains pointwise four-observer FULL_HIST versus seedless LR equivalence or strict separation.
