# EC49BA — η=43/100 的全实数因果观察精确点最优值

Date: 2026-10-30. Author-side portable mathematical certificate. `UNREVIEWED / NOT_ADMITTED`.

## Theorem and model

For the **auxiliary strictly positive 18+18-leaf P/Q probability-BRC observer only**, not native signed/phase BRC or X6: hidden `w∈{0,1,2}` uniform; first action `c∈{0,1,2,3,STOP}` with costs `(1,1,2,2,0)` and row-stochastic `x[w,c]`, subject to `Σwc cost(c)x[w,c]/3=43/48`. The observation `u∈{0,1}` has conditional probability `1/2+(2u−1)(1−w)η`; the purchase coin `p(c,u)∈[0,1]` is measurable only with respect to `(c,u)` and obeys `Σc,u p(c,u)T(c,u)=13/16`. Terminal acceptance depends only on bought `(c,u,z)`, where `z∈{0,1,2}`. `q_z=x[z,c]Pr(u|z)/3`, `T=Σ_z q_z`, and `V=Σ_z[43q_z−16T]_+/172`. Then `H=α−177β/172=ΣpV`, where `α,β` are the corresponding two-source acceptance rates, as in EC49AV–AZ.

**Claim (conditional on the previously established sparse vertex/edge representative lemma EC49AV):** for all legal real randomized causal policies, at `η=43/100`,

\[
\boxed{H_{\max}=\frac{267209}{2132800}-\frac{7\sqrt{782}}{44640}=0.1209004630660925872776\ldots.}
\]

This is a *single parameter point*, not a theorem over the interval `[21/50,43/100]`.

## Full upper-bound certificate

`VERIFY_EC49BA.py` imports the existing `VERIFY_EC49AX.py` at the same PR branch. It exactly enumerates the 168 vertices and 924 edges of the 15-coordinate first-stage polytope after four independent affine equalities. Under total paid-observation mass at least `13/16`, exactly 720 edges are infeasible, leaving 204 clipped edges. The inherited sparse representative lemma restricts optimal real first-stage `x` to one such clipped edge (a key nontrivial dependency; **independent review pending**).

For each edge endpoint and λ≥0 define the purchase-aware bound

\[
D_\lambda(x)=\lambda\frac{13}{16}+\sum_{c,u}[V(c,u)-\lambda T(c,u)]_+.
\]

For fixed λ, `Dλ` is convex in `x`; the expression dominates every feasible causal purchasing policy. Search the exact breakpoints `{0,1}∪{V/T:T>0}` and intersect both endpoint λ-intervals satisfying `Dλ≤151/1250`. The **same λ for both endpoints** exists on exactly 196 of the 204 feasible clipped edges. The program checks each resulting exact rational λ and hence bounds the entire continuum of policies on those 196 edges by `151/1250`.

The remaining **eight** edges, with supports `{0,2,4,6,10}`, `{0,3,4,6,10}`, `{0,6,10,12,14}`, `{0,6,10,13,14}` and their four corresponding label symmetries, share the same full affine q-fiber signature. One representative is

\[
x[0,:]=((11-8t)/16,0,t/4,0,(5+4t)/16),\quad
x[1,:]=(0,1,0,0,0),\quad x[2,:]=(1,0,0,0,0),\quad 0\le t\le1.
\]

Its paid mass before dropping is `(43−4t)/48`; reaching exact cost `13/16` requires withholding `(1−t)/12`. At η=43/100, all 24 event scores `43q_z−16T` have constant signs along the edge (verified exactly at each endpoint). Positive fiber 1 `(c,u)=(0,1)` has mass `T1=(d−ft)/96` with `d=227/10`, `f=372/25`; its positive-reward density is no greater than any other positive-mass fiber. To prove this for **every real** `t∈[0,1]`, compute the degree-≤2 polynomials `V_j T1−V1 T_j`: all three Bernstein coefficients on `[0,1]` are nonnegative for each of the eight fibers (exact values in the regenerated JSON report). Also `T1>(1−t)/12` throughout, so only fiber 1 is partially purchased, optimally.

Define the previously proven affine benchmark `h(η)=77/688+(674η−175)/16512` (not claimed optimal here). Exact Fraction checks at `t=0,1/2,1` plus the fixed score signs establish the **polynomial identity**, valid at every real `t`:

\[
h(43/100)-H_{\rm best}(t)=\frac{at^2+bt+c}{2064(d-ft)},
\quad a=\frac{55986}{625},\quad b=-\frac{190859}{2500},\quad c=-\frac{20693}{500}.
\]

Set

\[
t_* = \frac{1135}{744}-\frac{5\sqrt{782}}{186},\quad
H_* = \frac{267209}{2132800}-\frac{7\sqrt{782}}{44640}.
\]

The exact identity in `Q(√782)[t]` reads

\[
at^2+bt+c+2064(H_*-h)(d-ft)=a(t-t_*)^2.
\]

Since `a>0`, `d-ft≥d-f=391/50>0`, we obtain **`Hbest(t)≤H*` for every real `t∈[0,1]`**. The same applies to all eight signature-equivalent edges. Because `27<√782<28`, an elementary rational lower bound gives

\[
H_*> \frac{2320601}{19195200}>
\frac{151}{1250},\qquad
\frac{2320601}{19195200}-\frac{151}{1250}=\frac{45521}{479880000}>0.
\]

Thus the 196 ordinary edges are strictly below the eight-edge maximum. Combining their certificates with the inherited all-real edge-reduction lemma proves the global upper bound.

## Attaining lawful policy

Use the displayed row-stochastic `x` with `t=t*`. Buy all positive-mass `(c,u)` fibers except `(0,1)`; at `(0,1)` use the independent purchase probability

\[
p_* =\frac{43}{93}+\frac{5\sqrt{782}}{372}\in(0,1).
\]

Accept only the observable bought events `(0,0,2)`, `(0,1,0)`, `(1,0,1)`, `(1,1,1)`, `(2,0,0)`, `(2,1,0)`. Direct exact algebra verifies both costs and

\[
\alpha=\frac{10019}{24800}-\frac{7\sqrt{782}}{44640},\qquad
\beta=\frac{13}{48},\qquad
\alpha-\frac{177}{172}\beta=H_*.
\]

Buying and acceptance never condition on the hidden `w`. Strict positivity holds at η=43/100<1/2. Invariant model scope only; no X6, signed/phase BRC or heartbeat native transfer has been established.

## Reproduction and integrity

Run `python VERIFY_EC49BA.py > EXACT_REPORT_EC49BA_REPRODUCED.json` with its sibling `VERIFY_EC49AX.py`, Python 3 and SymPy. The reporter includes 196 exact rational edge prices, eight supports, all density Bernstein coefficients, algebraic optimizer, costs and acceptance set. This run actually executed locally on 2026-10-30, produced `168 / 924 / 720 / 196 / 8` and exact algebraic values. Exact report SHA-256 (original full local JSON): `138b5a27ec9ac562fed157d9bcfd445cf8076cde63ec6bc312fa8f96a289d52f`; source checker SHA-256: `77cdb023a563ff12dff70a1a7a692d9b1e7bf4d075ae73ef5c67f1bfce0deed0`. Any derivative/shortened published checker must be distinguished from this exact executed file. Existing sparse-representative and symmetry premises, math novelty and formal admission still require independent checks.

Fixed inputs: GLOBAL_KNOWLEDGE_V1 canonical main `a1c745d55ac076092afe465e69a04ad5f026463e`; EM canonical main `6bdc43671fe686d4f88cea8e2a3eb320583a0f3e`; predecessor candidate PR head `57aebb67a4e27d3618d2974dcae3ec0767701922`. P000/ACTIVE worldview read only. Service `0.6.11`: `research_authority_granted=false`; `CONTROL_QUOTA` and `UPSTREAM_CODE_REVIEW_REQUIRED` for native owner/claim routes. GitHub archival is **portable author-side research**, not Source-native Result or Driver admission.
