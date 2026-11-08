# R5 — all-lawful FULL_HIST to seedless LR: exact complementary triangular bridge and author-side closure

2026-11-09 (Asia/Shanghai). Evidence: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED / PORTABLE_ONLY**.

Frozen science: Global Knowledge `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current rule snapshots (not science pins): Global main `ae28c03db2bfeac4fac5c66cc73c1f7588e9acd2`, EM main `9ed5882e3e38c54bef259a90b28c595076e76123`. P000, ACTIVE worldview and native X6 physics are unchanged. This is **only** the frozen seven-LR-node P/Q-BRC terminal-observer model.

## Exact model and new theorem

Let (r=(1/10,1/2,3/4,1,5/4,3/2,19/10)) and for a lawful `FULL_HIST` flow `f=(g,a,b,u,v,w,z)` use the Q-node masses (M_i(f)) and two stopping-time maps (T_P,T_Q) coded in `VERIFY_PGEQ.py`. Lawfulness means
[
0le a,ble gle1,quad 0le ule13a/40+b/80,quad
0le wle3a/40+21b/80,quad
0le zle a/10,quad0le v-zle9b/40.
]
Seedless LR means (9bz=4a(v-z)).

Normalize ((g,b)=(1,1)), set (a=t), and write all capacity coordinates with ((p,q,	heta,kappa)):
[
x(t,p,q,	heta,kappa)=ig(1,t,1,(13t/40+1/80)p, 9kappa/40+t	heta/10, (3t/40+21/80)q, t	heta/10ig).
]

**New theorem (complementary high-p triangular prism):** For every real
[
oxed{quad 1/13le tle1/5,qquad 0le qle ple1,qquad0le	heta,kappale1quad}
]
there is a lawful seedless F-face target (y) with (z'=a'/10, v'-z'=9b'/40), identical (T_P,T_Q), and a nonnegative declaration-independent (7	imes7) martingale Blackwell coupling from (M(y)) to (M(x)). Thus all seven randomized terminal declarations, and hence ((e_P,e_Q,T_P,T_Q)), are preserved.

### Exact 24-corner proof

Index the triangle by (j=0,1,2), corresponding respectively to ((p,q)=(0,0),(1,0),(1,1)). Take (tin{1/13,1/5}) and ((	heta,kappa)in{0,1}^2), giving (2cdot3cdot4=24) corners. `VERIFY_PGEQ.py` contains all 24 **exact rational** triples ((g',a',b')). With (P=T_P(x)), (Q=T_Q(x)), reconstruct the remaining four target coordinates on F by
[
egin{aligned}
u'&=-17a'/40-19b'/80-g'/2-P+3Q/2-1/2,\
w'&=-7a'/40-39b'/80-g'/2+P-Q/2-1/2,\
z'&=a'/10,qquad v'=a'/10+9b'/40.
end{aligned}
]
The checker validates for **each** corner: all physical capacity and mass bounds, (sum M_i=1), (sum r_iM_i=1), both stopping times, the F seedless equality, and five exact hinge differences
[
H_k(y)-H_k(x)ge0,qquad H_k(f)=sum_i(r_i-r_k)_+M_i(f),quad kin{r_1,ldots,r_5}.
]
No float LP or tolerance appears in this proof-facing checker; all arithmetic is Python standard-library `fractions.Fraction`.

For arbitrary real parameters in the prism, interpolate the two (t)-endpoints, triangle vertices with **nonnegative** barycentric weights
[
eta_{00}=1-p,quadeta_{10}=p-q,quadeta_{11}=q,
]
and the (	heta,kappa) endpoints. Since the source is multiaffine in ((t,p,q,	heta,kappa)), the convexly interpolated source equals the requested (x); the interpolated target is on the **same linear F-face**. Target legality, masses, both time equalities, and convex-order hinge comparisons are affine and remain satisfied. Finite-grid convex order (finite Strassen martingale-coupling theorem) gives a nonnegative matrix (E) with
[
sum_jE_{ij}=M_i(y),quad sum_iE_{ij}=M_j(x),quad
sum_i r_iE_{ij}=r_jM_j(x).
]
This statement holds for **all real and irrational** parameters, including the boundaries. Reference: Leskelä–Vihola, *Conditional convex orders and measurable martingale couplings*, Bernoulli 23(4A), 2017, DOI 10.3150/16-BEJ827 (finite ordered-support case).

For any (0le ble gle1), (b>0), set (t=a/b) and scale each normalized source and target by (b), adding ((g-b)E_1+(1-g)E_0), where (E_1=(1,0,ldots,0)), (E_0=(0,ldots,0)); use corresponding identity martingale couplings on these two flows. This preserves the flow, capacities, seedless F-face, terminal mass and time equalities.

### Author-side corollary: full frozen R5 source domain

For every lawful real (x=(g,a,b,u,v,w,z)) with (0le a,ble gle1), a seedless LR Blackwell realization preserving all seven randomized declarations and ((e_P,e_Q,T_P,T_Q)) follows from the following **exact existing author-side certificates plus this new theorem**:

1. (ble a): PR **#1798** (immutable head `74d31afd03a303eea866ce25fcf4ec192e538b1a`).
2. (ale b, t=a/bin[0,1/13]): PR **#1821** (`edd5391600d24eade7958aeb794f78f0f15caa68`).
3. (tin[1/13,3/20]): (ple q) via PR **#1823** (`4cfa1ca9af363bc6800aaafd62c23e305811c045`); (qle p) via this theorem.
4. (tin[3/20,7/39]): full capacity box via PR **#1829** (`82b9565c79be2521cc5d1c292651ba4a33c301c0`) and predecessor #1827.
5. (tin[7/39,1/5]): (ple q) by PR **#1823** (`F_HIGH_T_BRIDGE.md`), (qle p) by this theorem.
6. (a/bge1/5, ale b): PR **#1800** (`58f1444c42d487ac8d2c9a1801f3c3adfade003f`).
The (b=0) sector belongs to case (1). Every (p,qin[0,1]) satisfies (ple q) or (qle p). The stated cases exhaust the full physical domain.

**Precisely scoped conclusion:** this supplies an **author-side complete covering proof conditional on the cited earlier exact certificate banks**. This run executed and checked the 24 *new* corners; it did **not** re-execute every earlier PR. This has not received independent project mathematical review, formal Task CLAIM, accepted Result, or Working Truth / Foundation promotion. The model-internal theorem makes no native X6 dynamical/physical claim.

## Executed evidence

Command: `python -S VERIFY_PGEQ.py`; executed on 2026-11-09 Asia/Shanghai in the current local sandbox, using only `Fraction`. Exit code 0, output captured as `EXACT_OUTPUT.txt`:
```
PASS_EXACT_24_F_FACE_TRIANGLE_CORNERS
MIN_HINGE_GAPS 0 0 0 0 0
PASS_EXACT_251_NORMALIZED_AND_SCALED_REGRESSIONS
THEOREM_ALL_REAL_T_1_13_TO_1_5_P_GE_Q_F_FACE_STRASSEN
```
251 rational samples are regressions, **not** the all-real proof; the complete corner set and analytic interpolation/Strassen are.

## Next unresolved unit

First independently reproduce the **entire stitched proof**, including predecessor PRs #1798, #1800, #1821, #1823, #1829 with their frozen pin and seven-node observers. Check statement and logic, every edge case, nonnegative endpoint matrices and the coupling orientation. Audit whether all cited exact predecessors are mutually source-compatible. Then attempt independent mathematical review / formal Task Result via genuine current Owner/CLAIM and reviewer authority. An additional useful direction is extracting a small single algorithm generating F/G targets and an explicit matrix (E) for arbitrary rational inputs; establish bit-costs and conditioning rather than mistaking finite Strassen existence for a fast construction.
