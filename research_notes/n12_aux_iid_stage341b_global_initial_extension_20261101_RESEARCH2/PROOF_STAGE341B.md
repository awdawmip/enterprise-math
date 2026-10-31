# Stage341-B — exact enlargement of the full-domain BRC Pareto interval

2026-11-01 (Asia/Shanghai). **Classification:** PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_BERNSTEIN_EXECUTED / UNREVIEWED / NOT_ADMITTED. Authored in the same ongoing research context; **not** an independent review or a native Source Result.

## Frozen source and observer scope

- GLOBAL_KNOWLEDGE_V1 canonical `main@6f405b5977bced88a276d67a47d9d87c220dad2c` (bootstrap, operating manual, ACTIVE worldview, mathematical/BRC/code policies).
- Enterprise Math canonical `main@c8a23c3049786196117d590abdc90560199f6911` (project AGENTS, P000 V5 `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`, joint observer-preservation, current portable/autonomous research route).
- Predecessor PR head `51ec3d8d6af154e3afb520ab20adfaa094f4ee94`, Stage340-B (exact 139-leaf global theorem for `E<=3/10000`); explicitly reused Stage329-B's rational Bernstein two-chamber *strict-concavity* certificate for the right `r1=0` branch. The latter is author-level / unreviewed, and its verified hypothesis rectangle is used without enlargement.
- `BRC` observer semantics: two **source-labelled** Bernoulli groups, all 16 atom-level tagged comparisons and source identity preserved. This is a four-real-rate auxiliary observer, **not** a proof for native P000 X6, 3D slice, triadic closure, time, or Cell address. Bernoulli weights are classical positive rational probabilities, not signed amplitude cancellation.

## Fully specified model and result

For `k=0,1,2,3`, let `B_k(z)=z^k(1-z)^(3-k)`, `w=(1,3,3,1)`, and `m=(61,21,9,9)`. With `q=(x,y)` in `[0,1]^2` define

\[
r_k(q)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\quad
b(q)=\frac5{32}\sum_{k=0}^3w_k|r_k(q)|,
\]
\[
D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,\quad
c(q)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

For two unconstrained source groups `(q1,q2)` put `P=b(q1)+b(q2)`, `T=33/1024+c(q1)+c(q2)`. Let `q*=(x*,y*)` be the unique global minimum of `b`, equivalently the unique `r0=r1=0` double zero in `x* in (231083/10^6,231085/10^6)`, `y* in (5554961/10^7,5555202/10^7)`, and put `beta*=b(q*)`. On the right-hand `r1=0` branch let `q_s` be the unique point with `b(q_s)=beta*+s`, and write `phi(s)=c(q_s)`.

**Stage341 theorem (full four-rate domain):** for **every real** `0<=E<=29/50000` (that is `E<=0.00058`),

\[
\boxed{\min_{\substack{q_1,q_2\in[0,1]^2\\P\le2\beta_*+E}}
T=\frac{33}{1024}+c(q_*)+c(q_E).}
\]

For `E=0`, `(q*,q*)` is the unique minimizer. For `0<E<=29/50000`, the entire optimizer set is **exactly** `{(q*,q_E),(q_E,q*)}`. Consequently there is no *global* first deviation from one-group-active allocation at or below `E=0.00058`. This extends the Stage340 interval (`0.00030`) by `0.00028`, or `93 1/3%` of its prior length. The theorem **depends** on the precise upstream Stage329 strict-concavity lemma and on the declared auxiliary model; all components remain subject to independent mathematical review.

## New Lemma A: a continuous 193-leaf global localization certificate

Define exact rational threshold and rectangle

\[
Q=\frac{109}{25000}=0.00436,\qquad
R=\left[\frac{29}{128},\frac{15}{64}\right]\times
\left[\frac{69}{128},\frac{39}{64}\right].
\]

Then

\[
\boxed{\forall (x,y)\in[0,1]^2,\quad b(x,y)\le Q\implies (x,y)\in R.}\tag{A}
\]

This holds over the **entire continuum**, not just a discrete mesh. For each nonempty mask `S subset {0,1,2,3}`, put `F_S(z)=sum_{k in S}w_k B_k(z)`. On an interval `[u,v]`, all values of `F_S` are bounded below by the minimum of its four exact cubic Bernstein coefficients:

\[
L_S[u,v]=\min\left\{F_S(u),F_S(u)+\frac{v-u}3F'_S(u),
F_S(v)-\frac{v-u}3F'_S(v),F_S(v)\right\}.
\]

The residual mass conservation `sum w_k r_k=0` gives `b=(5/16)*sum_k w_k (r_k)_+`, hence any rectangle `[a,b]x[c,d]` has the proven continuous bound

\[
 b(x,y)\ge\frac5{16}\left[\frac{4L_S[a,b]+L_S[c,d]}5
-\frac{\sum_{k\in S}w_km_k}{160}\right].\tag{A1}
\]

The committed `CERTIFICATE_STAGE341B.csv` comprises a **complete, recursively checked quadtree** of 193 dyadic closed squares: 184 `HIGH` leaves carry a concrete subset mask and an exact rational (A1) lower bound **strictly greater than Q**; 9 `INNER` leaves are fully contained in `R`. All four children of every nonterminal node are present, no unlisted leaf exists, and the sum of exact leaf areas is 1. Max depth: 14. Its independently reread SHA256 is `6859896024fb5aea1f154b806dc340a9de0007da5c15c3591058ae71adf0c3fe`. Equation (A) follows immediately.

Stage338's double-zero rational root isolation gives the strict upper bound

\[
\beta_*<\frac{60478550833982446319}{16000000000000000000000}
\quad\text{and}\quad
\frac{60478550833982446319}{16000000000000000000000}+\frac{29}{50000}<Q.\tag{A2}
\]

Thus once the global fact `b>=beta*` is established below, every source in any feasible two-group pair with `P<=2beta*+E` and `E<=29/50000` has `b(q_i)<=beta*+E<Q` and hence lies strictly inside `R` (the boundary cannot contain a point with `b<Q`, by continuity and (A)).

## New Lemma B: all tagged gradients and chamber descents remain valid on the larger rectangle

On `R`, exact monotonicity of the cubic atoms yields

\[
r_2\ge\frac{24111}{10485760}>0,\qquad
r_3\le-\frac{909}{1310720}<0.
\]

The entire 16-comparison sign census has rows `(x,1/4):-+++`, `(x,3/4):--++`, `(y,1/4):++--`, `(y,3/4):--sigma+` in ascending `k`. The only variable sign is the `k=2` term of `(y,3/4)`, changing at the **retained** algebraic cusp `y_dagger=(1+sqrt(13))/8`. Direct symbolic derivation from all sixteen labelled absolute values gives

\[
 c_x=-p(x),\quad p(x)=\frac{(1-x)(189-183x)}{256}>\frac25,\qquad
0<c_y<\frac1{40},
\]

with the one-sided exact formulas `c_y=3y(1-y)/64` below the cusp and `c_y=3y(18-25y)/256` above it. As in Stage340,

\[
b=\frac5{16}\bigl[-r_3+(-r_0)_++3(-r_1)_+\bigr].\tag{B}
\]

The four strict `(sign r0, sign r1)` chambers all have a feasible descent in `c` without increasing `b`:

* `(+,+)`: `b=-5r3/16`, and both `b_x,c_x<0`; increase `x`.
* `(+,-)`: `b=-5(r3+3r1)/16`, `b_x=-3(1-2x)^2/4<0`, `c_x<0`; increase `x`.
* `(-,-)`: `b=15r2/16`, `b_y=3y(2-3y)/16>0`, `c_y>0`; decrease `y`.
* `(-,+)`: `b=-5(r3+r0)/16`, `b_x=3(1-2x)/4>0`, `b_y=-3(2y-1)/16<0`. Move `x,y` **up** along its constant-`b` curve, which strictly decreases `c`, since the ratio `c_y*b_x/(-b_y)` is `<21/64` below the tagged cusp and `<35/96` above it, while `p(x)>2/5`. One-sided integration covers the cusp exactly.

These inequalities hold **uniformly** on the enlarged `R` because its lower `y` endpoint is unchanged and its upper endpoint remains below `2/3`; every comparison was rechecked against the new endpoints.

## New Lemma C: both zero curves exhaust all remaining constrained minimizers

For `r0=0` let `y=Y0(x)`; differentiation gives `Y0'=-4(1-x)^2/(1-y)^2<0`. The function `r1(x,Y0(x))` is strictly increasing and has just the inherited root `q*` in `R`. Left of `q*`, `r1<0`, `b=15r2/16` and

\[
\frac{dr_2}{dx}=\frac45(1-x)^2\{f(x)-f(y)\}<0,
\qquad f(z)=\frac{z(2-3z)}{(1-z)^2}.
\]

The new enlarged upper endpoint **does not invalidate** this inequality: `f(x)<=f(15/64)=1245/2401<429/625=f(39/64)<=f(y)` on `R` (`f` is decreasing for `z>1/2`). The tagged cost derivative `c_x+c_yY0'<0`, so the entire left zero arm is dominated toward `q*`. Right of `q*`, nearby points inside the `(-,+)` chamber have the same public error and smaller tagged cost; `b` also increases to the right along `r0=0`, since `dr3/dx=(12/5)[x^2-y^2(1-x)^2/(1-y)^2]<0`.

For `r1=0` let `y=Y1(x)`, where

\[
0<Y_1'=\frac{4(1-x)(1-3x)}{(1-y)(3y-1)}\le\frac{16236}{4661}<5.
\]

Thus `d c/dx=-p(x)+c_yY1'<-2/5+(1/40)*5<0`, with both tagged sides covered. Left of `q*`, `r0>0`, and `b=-5r3/16` strictly decreases as `x` rises to `q*`; this whole arm is dominated. Right of `q*`, `r0<0`, and `b=-5(r3+r0)/16` strictly **increases**, because

\[
\frac{d[-r_3-r_0]}{dx}>
\frac{12}{5}(1-2\cdot6/25)-\frac35(2\cdot2/3-1)\cdot5
=\frac{31}{125}>0.
\]

The complete chamber and zero-curve exhaustion together with (A) proves that `q*` is the unique global minimizer of `b`, and that the only possible `c`-minimizer at each individual budget `beta*<=B<=beta*+29/50000` is the **right-hand** `r1=0` point spending the whole budget. That point exists: at `x=15/64`, the unique `r1` root lies between `y=565/1000` and `566/1000`, and the exact lower estimate for its public error is

\[
 b(q_{x=15/64})>\frac{1244037}{256000000}
>\beta_*+\frac{29}{50000}.
\]

Its entire needed segment lies inside the **unchanged** Stage329 strict-concavity rectangle `[231/1000,239/1000] x [555/1000,577/1000]`, so this extension does **not** enlarge the inherited curvature lemma's hypotheses. Consequently, `c(q)>=phi(b(q)-beta*)` for the budget interval, with equality only on that right branch.

## Two-source allocation and exact competing-boundary witness

For any feasible pair set `s_i=b(q_i)-beta*>=0`, so `s1+s2<=E`. Lemma C gives `c(q_i)>=phi(s_i)`; because `phi` is strictly decreasing, equality for a two-source optimum requires `s1+s2=E`. Stage329's strictly negative `phi''` on the unchanged right branch implies that `phi(t)+phi(E-t)` is strictly concave on `[0,E]`; its only minima are endpoints `t=0,E`. This proves the full two-source result and uniqueness.

**Explicit new obstruction for the next extension:** set `y0=771/1250=0.6168`, `x-=56671/250000=0.226684` and `x+=45337/200000=0.226685`. Exact rational evaluation gives `r3(x-,y0)<0<r3(x+,y0)`. For fixed `y=y0`, the continuous `r3(x,y0)` is strictly increasing, so a real `x0` in `(x-,x+)` satisfies `r3(x0,y0)=0`. The total-error map is globally `3`-Lipschitz in `x` (since `|B_k'|<=3`, `sum w_k=8` and the x-weight is `4/5`); with the strict exact check `b(x-,y0)<4407/10^6`, it follows that

\[
\boxed{b(x_0,y_0)<\frac{441}{100000}=0.00441.}\tag{C}
\]

Thus an extension beyond `Q=0.00441` **cannot** rely on a uniform `r3<0` sign throughout the admitted low-error set; it must handle the `r3=0` stratum and adjacent sign reversal, or use a different exclusion argument. The witness does *not* assert that `0.00441` is the first obstruction or that this stratum is globally Pareto competitive.

## Verification, authority and smallest open unit

`REPRO_STAGE341B.py` uses Python `Fraction` and SymPy to construct the 193-leaf certificate, parse and re-verify every exact rational Bernstein witness and its complete quadtree, check the area identity, 16 tagged signs, one cusp, exact gradient polynomials, enlarged rectangle inequalities, double-zero bracket, endpoint, and the rational `r3` sign witness. It was actually executed twice; stdout matched byte for byte and ended in `STAGE341B_GLOBAL_INITIAL_INTERVAL_EXTENSION_EXACT_PASS`. All mathematical quantified steps on the continuum are the algebraic inequalities above and the complete Bernstein cover, **not** finite-grid inference. The Stage329 49+49 coefficient strict-concavity proof is reused within its original range, not newly audited in this run.

As actually observed at the beginning of this research unit, native Enterprise Math v0.6.11 reported `research_authority_granted=false`, `UPSTREAM_CODE_REVIEW_REQUIRED`, and control job quota 5/5. The active Source owner was not authoritatively established; no CLAIM, execution, formal Result, review, or admission is inferred from a GitHub commit. A PR branch is durable evidence but not canonical main or native Source acceptance. Original P000 X6 dynamics, triadic closure, separately typed time and final Cell-address preservation remain separate unproved bridges.

**Next Stage342-B:** classify the real `r3=0` low-error arc and its intersection with `r0/r1` boundary strata in a piecewise, source-tagged exact semialgebraic cover; test whether the full-domain candidate still dominates for a budget `E>29/50000` or produce a strict rational competing pair. Extend the Stage329 curvature use only within its original rectangle unless a new exact curvature certificate is obtained. Preserve the same frozen model, proof dependency and authority disclosure.
