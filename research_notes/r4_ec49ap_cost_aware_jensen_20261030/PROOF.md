# EC49AP — a cost-aware Jensen certificate for the unrestricted causal observer

Date: 2026-10-30 (Asia/Shanghai). Author-side mathematical continuation of EC49AO PR #1721, exact source commit `bed26d2d7349fdc1173cc6822696e85b60143cb6`. Status: `AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

## 1. Exact scope and new theorem

Use the *auxiliary strictly positive 18+18-leaf BRC observer* from EC49AO. Hidden `w in {0,1,2}`, observed `u in {0,1}`, optional purchased `z in {0,1,2}`; for `0 <= eta < 1/2`,

\[
 t(w,u)=\frac12+(2u-1)(1-w)\eta,\quad
 P(w,u,z)=t(w,u)\begin{cases}1/6&z=w,\\1/12&z\ne w,\end{cases}
 \quad Q(w,u,z)=t(w,u)/9.
\]

Here fix `eta=1/25`, first-stage expected cost `C1=43/48`, second-stage expected purchase cost `C2=13/16`, and `k=177/172`. The hidden `w` is **erased** after the first-stage action. At `w` select `c in {A0,A1,B0,B1,STOP}` with probabilities `x[w,c]`; its costs are `(1,1,2,2,0)`. Row sums are one and `sum_{w,c} cost(c) x[w,c] = 43/16`. After observing `(c,u)` alone, a fresh independent coin with probability `r(c,u)` either buys observation `z` or does not; terminal acceptance uses only realized observations and fresh independent behavioral coins. The exact expected second cost is `C2`. Write `alpha=P(accept)`, `beta=Q(accept)`, `H=alpha-k beta`.

**Theorem (EC49AP).** For *every* lawful real-valued causal behavioral policy satisfying these equalities,

\[
\boxed{\frac{77}{688}\ \le\ H_{\max}\ \le\ \frac{1875833}{16649600}.}
\]

In particular the new all-policy upper certificate improves EC49AO's bound `1715013/15136000` by exactly `106813/166496000`. Its exact gap over the existing legal full-purchase witness is `12433/16649600`. This theorem is a **strictly stronger upper bound**, not an assertion that unrestricted `Hmax=77/688`.

## 2. Typed BRC observer and the dual reduction

Define `q_z(c,u)=x[z,c] t(z,u)/3` for paid actions `c<4`, `T(c,u)=sum_z q_z(c,u)` and

\[
 V(q)=\sum_z[43q_z-16T]_+,\quad
 F(x)=\sum_{c<4,u}\frac{V(q(c,u))}{172},\quad
 c(x)=\sum_{c<4,u}T(c,u).
\]

The exact observed purchased-leaf source weights are `P(c,u,z)=(T+q_z)/4` and `Q(c,u,z)=T/3`. Their support score is `[43q_z-16T]/172`. If the sensor is not purchased, `P=Q` on the resulting observation `(c,u,no_sensor)`; `k>1`, so rejecting is optimal. Thus for any lawful purchase and terminal rule,

\[
 H\le\sum_{c<4,u}r(c,u)\frac{V(q(c,u))}{172}\le F(x),\qquad c(x)\ge C_2.
\]

Importantly `r(c,u)` cannot depend on erased `w`. The construction above keeps this restriction. It retains the complete joint branch distribution until the specified `(c,u,z)` readout; no positive-weight total is silently interpreted as native signed BRC cancellation.

Set the previously verified support data

\[
 \lambda=-\frac{7047}{23650},\quad
 B=\frac{21519}{60544},\quad
 D(x)=F(x)-\lambda c(x),\quad
 S=B+\lambda C_2=\frac{171531}{1513600}.
\]

With `s=c(x)-C2>=0` and `kappa=-lambda=7047/23650`,

\[
 S-H=(B-D(x))+(F(x)-H)+\kappa s\ge B-D(x)+\kappa s.\tag{1}
\]

`D` is convex in `x`: each `V` is a sum of positive parts of linear forms; the cost is linear.

## 3. Complete finite domain and the NEW cross-class certificate

The feasible first-stage polytope is the product of three four-dimensional simplices cut by the single cost hyperplane `43/16`. This noninteger cost cannot pass through any deterministic vertex. Every cut vertex therefore lies on an original product edge (only one row mixes exactly two actions, while two rows are deterministic). The script exhausts these crossings with exact rational arithmetic, deduplicating to **168 vertices**. These vertices constitute a complete finite support for continuous-real `x` by convexity, not a numerical grid.

For each vertex `v`, the exact checker confirms `B-D(v)>=0`. Divide the 168 vertices into **three disjoint sets**:

- `L0`: the 12 tight vertices with `c(v)=L=25/32` and `B-D(v)=0`;
- `U`: all 24 vertices with `c(v)=U=43/48`, four of which are tight;
- `N`: the remaining 132 vertices, all with `43/96<=c(v)<=L` and `B-D(v)>=a=7173/137600`.

The decisive *new* computation checks all **12×24=288** ordered low-tight/high-cost midpoint pairs and finds

\[
 J(v,w)=\frac{D(v)+D(w)}2-D\!\left(\frac{v+w}2\right)\ge j=\frac1{600}>0,
 \quad (v\in L0,w\in U).\tag{2}
\]

The minimum `1/600` occurs at 32 pairs. Unlike EC49AO's 48 **tight-low versus tight-high** comparisons, this new 288-pair inequality covers **all 24 high-cost vertices**, including the 20 nontight high-cost competitors. Exact per-cost vertex counts and all finite checks are in `VERIFY.py` and its executed `EXACT_REPORT.json`.

For an arbitrary real feasible `x`, take any convex decomposition `x=sum_i theta_i v_i`, `theta_i>=0`, `sum theta_i=1`. Put `l=sum_{L0} theta_i`, `h=sum_U theta_i`, `n=sum_N theta_i`, so `l+h+n=1`. Observe the exact identity

\[
 x=\sum_i\theta_i^2 v_i+\sum_{i<j}2\theta_i\theta_j\frac{v_i+v_j}{2}.
\]

Convexity of `D`, nonnegative Jensen defects for all pairs, the individual vertex slacks, and (2) give

\[
 B-D(x)\ge a n+2j l h.\tag{3}
\]

This is an all-real inequality with an exact finite certificate; it does not assume that the mixture is itself a randomized hidden-state policy chosen with a shared persistent seed.

## 4. Resource-aware analytic closing argument

The six exact vertex paid-cost values are `43/96,9/16,59/96,2/3,25/32,43/48`. They establish both cost comparisons below for any convex decomposition:

\[
 c(x)\le L(l+n)+Uh=L+(U-L)h,
\quad c(x)\ge C_2\Longrightarrow h\ge\frac{C_2-L}{U-L}=\frac3{11}.\tag{4}
\]

Also, writing `c_min=43/96`,

\[
 c(x)\ge Ll+Uh+c_{min}n
 =U-(U-L)l-(U-c_{min})n.
\]

Since `U-C2=8/96`, `U-L=11/96` and `U-c_min=43/96`, the surplus `s=c(x)-C2` obeys

\[
 \boxed{11l+43n+96s\ge8}.\tag{5}
\]

Choose the exact rational *resource price* `tau=1/12100`. The independently checked inequalities

\[
 a\ge43\tau,\qquad
 2j\frac3{11}=11\tau,\qquad
 \kappa\ge96\tau
\]

combine with (1), (3), (4), (5):

\[
 S-H\ge a n+2j l h+\kappa s
 \ge \tau(43n+11l+96s)
 \ge8\tau=\frac2{3025}.
\]

Consequently

\[
 \boxed{H\le\frac{171531}{1513600}-\frac2{3025}
 =\frac{1875833}{16649600}}.
\]

This proof handles **every real first-stage policy and every real fractional sensor-purchase/acceptance policy**, with causal erasure and independent behavioral coins intact. The finite vertex/Jensen checks are load-bearing and explicitly exhaustive by the preceding polytope argument.

## 5. Lower witness, arithmetic checks, limitations

The exact EC49AO policy remains lawful: `w=0` picks `(3/16)A1+(1/4)B0+(9/16)STOP`, `w=1` picks `A0`, `w=2` picks `A1`; buy every positive-mass paid sensor, accept precisely `(A0,z=1)`, `(A1,z=2)`, `(B0,z=0)` for either `u`. Its costs are `C1=43/48`, `C2=13/16` and `H=77/688`. Its rule uses only observed `(c,u,z)`; no access to erased `w`.

`VERIFY.py` (Python standard-library `Fraction`) was actually executed on 2026-10-30. It regenerated 168 vertices, all vertex gaps, 12/24/132 class sizes, 288 cross-class midpoint Jensen defects (32 at `1/600`), 18+18 strictly positive normalized source leaves, witness costs and H, all rational resource-price coefficient inequalities, the new bound, and comparison against EC49AO. `EXACT_REPORT.json` is the captured stdout. These checks certify the finite rational subclaims; universal quantifiers use the stated convexity and cost arguments. No Lean/formal-proof-assistant run or independent mathematical review is claimed.

**Interpretation boundary.** The model is a *positive probability* auxiliary BRC observer, with a stated one-step observation horizon and `(c,u,z)` readout. It does not establish a theorem of native signed/phase BRC, the native six-axis X6 coordinate system, or heartbeat dynamics. Any transfer requires an explicit typed state/observer/future-operation preservation map respecting P000 and the ACTIVE residual-fidelity worldview. Original P000 and worldview bytes were left untouched.

## 6. Smallest remaining question (EC49AQ)

At the same exact `eta,C1,C2,k`, seek either an **explicit lawful rational partial-purchase policy with H>77/688** or an **all-real equality certificate** `H<=77/688`. A nearer target is to strengthen the midpoint certificate with cost-class conditional Jensen defects or an exact support dual for the 24 high-cost vertices. The remaining certified interval width is `12433/16649600`. The next result should keep the full `r(c,u)` causal purchase restriction and classify discovery vs independent verification separately.
