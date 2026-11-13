# R5: exact five-parameter mixed low-ratio Blackwell box (2026-11-08)

Status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.
Original frozen scientific inputs (unchanged): global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Source baseline: PR #1801 at `fa4859f223f54bc91ea5ee54fdca7ba955085d90` and the seven-node observer definitions there. P000 and the ACTIVE worldview are retained. This is a **typed statistical observer model**, not a claimed native Heartbeat X6 space/time operation.

## Main theorem (exact all-real quantified scope)

Let the seven Q-terminal masses `M(f)`, P/Q likelihood ratios
`r=(1/10,1/2,3/4,1,5/4,3/2,19/10)` and stopping times `TP(f),TQ(f)`
be precisely the affine maps in `VERIFY.py` (also in PR #1801). A legal
FULL_HIST flow `f=(g,a,b,u,v,w,z)` satisfies
`0<=a,b<=g<=1`,
`0<=u<=13a/40+b/80`,
`0<=w<=3a/40+21b/80`,
`0<=z<=a/10`, and
`0<=v-z<=9b/40`.
It is seedless LR exactly when `9*b*z=4*a*(v-z)`.

For **every real tuple**
```
0 <= t <= 1/5,       0 <= p <= 1,       0 <= q <= 3/4,
1/4 <= theta <= 3/4, 1/4 <= kappa <= 3/4
```
define
```
x(t,p,q,theta,kappa) =
(1, t, 1,
 (13t/40+1/80)*p,
 t*theta/10 + 9*kappa/40,
 (3t/40+21/80)*q,
 t*theta/10).
```
Then there exist an explicitly reconstructible legal seedless target `y`
on the **single common affine face**
```
C_(3/4) = { z' = 3a'/40, v'-z' = 27b'/160 },
```
and a nonnegative declaration-independent rational/real `7x7`
transport `Q`, for which
```
sum_j Q[i,j]     = M_i(y)                   (all target rows)
sum_i Q[i,j]     = M_j(x)                   (all source columns)
sum_i r_i Q[i,j] = r_j M_j(x)               (all source columns)
TP(y)            = TP(x)
TQ(y)            = TQ(x).
```
For any terminal decision vector `d in [0,1]^7`, the row-normalized
pullback `d'_i = sum_j Q[i,j]*d_j/M_i(y)` for positive-mass rows (0
otherwise) preserves the two terminal error rates and both expected stopping
times. The same is true for each source-target mixture
`x_h=(1-h)x+h*y`, `0<=h<=1`, with
`Q_h=(1-h)Q+h*diag(M(y))`.

The source's exact history residual is
`9*b*z-4*a*(v-z) = 9*t*(theta-kappa)/10`, which has both signs in this
box and is nonzero for `t>0,theta!=kappa`.
This proves a **full five-real-parameter solid box** of nontrivial mixed
capacity flows, much larger than either previously known saturated
one-parameter corner. The unrestricted R5 mother question is still open.

## Exact certificate (32 rational vertices, no floating-point dependency)

Put `tau=3/4` and parameter order `(p,q,t,theta,kappa)`.
The Cartesian vertices use respectively
`p in {0,1}`, `q in {0,3/4}`, `t in {0,1/5}`,
`theta in {1/4,3/4}`, `kappa in {1/4,3/4}`.
The companion `VERIFY.py` carries 32 compact *support/active-bound/zero*
triples in lexicographic `itertools.product` order. For each vertex,
the support mask bit `7*i+j` declares a potentially nonzero `Q[i,j]`.
The five active-bound mask bits correspond to
```
1-g',  g'-a',  g'-b',  (13a'/40+b'/80)-u', (3a'/40+21b'/80)-w'.
```
The optional third mask fixes chosen target coordinates `(g',a',b',u',w')`
at zero when the rational vertex does so. These exact linear equalities,
the common face equations, the 7 row, 7 column, 7 weighted-column and 2
stopping equations yield a *unique rational solution* by the embedded
standard-library-only Fraction Gauss-Jordan checker. The checker verifies
consistency, full column rank, every entry's nonnegativity, all five
physical target inequalities, both other physical capacity pairs from
the common face, normalization under P and Q, every calibrated equality
and both stop times. Thus each compact support mask is a complete
deterministic reconstruction certificate, not a float approximation.
Some vertices repeat a support, but each is independently reconstructed
from its own exact source parameters.

An executed local run verified all **32** vertex certificates with
**284 positive transport entries in aggregate**, and a distinct exact
interior five-parameter reconstruction with
`(p,q,t,theta,kappa)=(7/13,7/11,3/25,7/13,5/11)`.
Its full stdout is preserved in `EXACT_OUTPUT.txt`.
The all-real conclusion relies on the following algebraic argument rather
than treating that one interior test or finite sampling as a proof.

## Why finite exact vertices imply all real points

Let `s_1,...,s_5` be the normalized affine coordinates of
`(p,q,t,theta,kappa)` in the closed unit box. Each source-flow
coordinate is **multi-affine**: its degree in *each separate variable*
is at most 1, even though `t*p,t*q,t*theta` can occur. Hence
```
x = sum_{epsilon in {0,1}^5} w_epsilon * x_epsilon,
w_epsilon = product_l (s_l if epsilon_l=1 else 1-s_l),
w_epsilon >= 0, sum_epsilon w_epsilon = 1.
```
For every corner the exact rational certificate provides a seedless
`y_epsilon` and calibrated nonnegative `Q_epsilon`. Set
`y=sum w*y_epsilon` and `Q=sum w*Q_epsilon`.
All `y_epsilon` lie in the **same** linear `C_(3/4)` face, so `y`
remains exactly seedless; the target's physical inequalities are affine
and preserved by convexity. The mass map and stopping-time maps are affine
in the flow, and the three families of transport equalities are linear.
Therefore the required identities hold exactly for *every real* input
including irrational and all boundary parameters. Nonnegative row
normalization gives valid declarations; the h-interpolation follows by
the explicit diagonal kernel above. This completes the proof in the
declared seven-node statistical model.

## Verification, lineage and scientific interpretation

Run `python3 VERIFY.py` using Python 3 standard library `fractions`
and `itertools`. No SciPy/NumPy/SymPy is needed for the certifier.
Floating LP was used privately to discover candidate supports, and
rational linear algebra is used to check the published proof. The
published algorithm itself reconstructs all coefficients exactly;
there is no dependence on those exploratory floating computations.

The claim is an exact result **in the frozen seven-node P/Q-BRC observer**:
the retained observer is `(eP,eQ,TP,TQ)`. It does not silently quotient
away historical branch distinctions for other future operations. It
does not assert native X6 dynamical equivalence, an unrestricted Blackwell
equivalence for unreported observables, or independent review/admission.
GitHub author-side preservation is distinct from Source native
Owner/CLAIM and Result/Review authority.

## Next discriminating unit

Extend the box in the `q` direction, or expand `theta,kappa` to their
full capacity square, by precise new fixed-face vertices and alternative
tau charts where a chosen face fails. The first unproved adjacent vertex
candidate is `t=0, p=0, q=1, theta=kappa=1/4` on `C_(3/4)`;
a fixed-face failure must be evaluated as a **face-specific** obstruction
while searching a distinct seedless chart. Then seek a multi-chart
covering of the full low-ratio four-capacity prism and ultimately the
unrestricted R5 four-observable reachable-set problem.

## Control and source boundary

The connected GitHub identity is `awdawmip` with repository admin
permission. On this run the native `em_status`, `em_control_tasks`
and `em_session_start` actions each returned
`BACKEND_IDENTITY_CHECK_UNAVAILABLE; operation_sent=false`.
The Site gateway reported `research_authority_granted=false`.
Thus active Owner/CLAIM/native Researcher-ID could not be established;
this is a separately preserved author-side research source for later
authorized intake. No native task ownership or mathematical approval
is claimed.
