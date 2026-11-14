# R749SPD–SPE: two exact post-half Walsh minimax phases on s = 3/5

Date: 2026-11-14. Status: AUTHOR_EXACT_NOT_REVIEWED. Scientific input pinned to awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor R749SPC: https://github.com/awdawmip/enterprise-math/pull/2420 at ac0189ff6e472b699f6d8abc52dda478541a7bff.

## 1. Model, domain, theorem

In the frozen auxiliary sixteen-atom Walsh model, let K = F_2^4 and χ_m(k)=(-1)^popcount(k&m). Define

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

For fixed (t,s), the compatible source fiber F(t,s) consists of every *nonnegative normalized* such p. Total variation TV(P,Q) is half the sum of the sixteen absolute coordinate differences. Let ρ(t,s) be the minimax source-fiber radius over unrestricted 16-atom probability prediction centers and ρcal(t,s) the radius for prediction centers restricted to F(t,s). Set g=ρcal−ρ.

**Theorem (all real parameters).** For s=3/5 and 1/2≤t≤3/5,

\[
\boxed{\rho(t,3/5)=\frac12-\frac{3t}{10}.}
\]

The exact calibrated radius and gap have two phases:

\[
\boxed{\rho_{\mathrm{cal}}(t,3/5)=
\begin{cases}
\frac{14}{25}-\frac{2t}{5},&1/2\le t\le19/35,\\
\frac{27}{55}-\frac{3t}{11},&19/35\le t\le3/5,
\end{cases}}
\]

\[
\boxed{g(t,3/5)=
\begin{cases}
\frac3{50}-\frac t{10},&1/2\le t\le19/35,\\
\frac{3t-1}{110},&19/35\le t\le3/5.
\end{cases}}
\]

The formulas agree at t=19/35. The gap is positive throughout, decreases from 1/100 at t=1/2 to 1/175 at t=19/35, and increases to 2/275 at t=3/5. Thus **19/35 is a certified interior calibrated-center phase switch, but not a zero-gap transition**. The free-radius slope switches at t=1/2 relative to the R749SPC predecessor.

A common explicit optimal unrestricted center on the entire interval is q_f(t)=p_{a(t),1,a(t),0,0,0,0}, a(t)=8t/5−3/5. Optimal compatible centers are q_c(t)=p_{t,3/5,h(t),0,0,0,0} with h(t)=9(t−2/5)/5 on the first phase, and h(t)=(85t−32)/55 on the second. Both values coincide at t=19/35, where h=9/35. Their probabilities are exactly nonnegative at each phase endpoint, and hence throughout each interval by affine interpolation.

## 2. New free minimax lower bound: weighted event certificate

Define two source families (the same exact sources previously used in R749SPC):

\[
P_-(t)=p_{t,3/5,t-2/5,-2/5,-2/5,t-1,t-1},\quad
P_2(t)=p_{t,3/5,t+2/5,0,0,t-3/5,t-3/5}.
\]

Each of their 16 atoms is affine in t, and direct exact checks at t=1/2 and t=3/5 show nonnegativity and normalization, so both are compatible for **all real** t in the interval. Let E_A={7,11,13,14,15} and E_B={0,3,5,6,9,10,12,15}. Exact expansion gives P_-(E_A)=19/20−t/2 and P_2(E_B)=7/10+t/2.

Translations d in G={d∈K:χ_3(d)=χ_12(d)=1} act as a four-element symmetry group on the source fiber. TV is translation-invariant and worst-case TV risk is convex in the prediction center. Consequently averaging any unrestricted center over G cannot increase its risk. A G-invariant probability center has constant per-atom masses x_0,x_1,x_2,x_3 on sign classes (χ_3,χ_12) ordered as (--),(-+),(+-),(++), with x_j≥0 and 4Σx_j=1.

E_A contains respectively (0,2,2,1) atoms in those classes; E_B contains (4,0,0,4). Since TV(P,q)≥P(E)−q(E), any invariant free center has worst-case risk

\[
\begin{aligned}
R(q)&\ge\frac45[P_-(E_A)-q(E_A)]
+\frac15[P_2(E_B)-q(E_B)]\\
&=\frac12-\frac{3t}{10}+\frac45x_0
\ge\frac12-\frac{3t}{10}.
\end{aligned}
\]

This is a new **weighted multi-event lower certificate**. The older source-pair diameter/2 bound need not be tight once t>1/2. This argument is valid for *all* free centers by the above symmetrization, not just a parametrized guess.

## 3. Two calibrated lower bounds

Under the same fiber symmetry, any calibrated center may likewise be symmetrized to q_h=p_{t,3/5,h,0,0,0,0}. Write E_1={7,11,12,13,14,15}.

For 1/2≤t≤19/35, the source/event witnesses (P_-,E_1) and (P_2,E_B) satisfy, identically in real t and h,

\[
R(q_h)\ge
\max\left\{\frac{13}{20}-\frac{5t}{8}+\frac h8,
\frac15+\frac t2-\frac h2\right\}.
\]

The two affine lines intersect at h=9(t−2/5)/5 with value 14/25−2t/5, establishing the first calibrated lower bound without assuming an optimal h.

For 19/35≤t≤3/5, replace E_1 by E_A:

\[
R(q_h)\ge
\max\left\{\frac35-\frac{9t}{16}+\frac{3h}{16},
\frac15+\frac t2-\frac h2\right\}.
\]

The lines intersect at h=(85t−32)/55 with value 27/55−3t/11. Every source and event used in these inequalities is explicit. Their affine identities are verified exactly at the four (t,h) corners per phase.

## 4. Matching upper bounds: complete exact arithmetic

For each interval, use the full six-dimensional **joint source polytope** J in variables (t,h,u,v,w,z), fixed s=3/5, subject to all 16 atom nonnegativity conditions and two endpoint bounds on t. All 18 facets are integer-linear after clearing the denominator 35. It is bounded and full-dimensional; an interior t, a strict feasible h and u=v=w=z=0 give a strict interior point.

The attached pure-standard-library Python checker enumerates *all* C(18,6)=18,564 potential active bases per phase; integer Bareiss elimination and Fraction back-substitution solve each, while singular/infeasible candidates are discarded. Every distinct exact vertex is checked for source normalization/positivity, both predicted centers' positivity, and both total-variation upper bounds. The verified results are:

| Check | SPD [1/2,19/35] | SPE [19/35,3/5] |
|---|---:|---:|
| Active six-facet combinations | 18,564 | 18,564 |
| Nonsingular bases | 9,536 | 9,536 |
| Feasible bases (including repeats) | 392 | 424 |
| Distinct exact vertices | 40 | 37 |
| Parameter endpoint counts | 20 + 20 | 20 + 17 |
| Maximum free / calibrated risk excess | 0 / 0 | 0 / 0 |

Each atom difference between a source p_x and a candidate q_f(t) or q_c(t) is affine in all joint variables. Therefore TV(p_x,q(t)) minus the proposed *affine* radius is convex on J. All feasible points are convex combinations of exact vertices, so checking **every vertex** proves the upper bounds for all real source coefficients and parameter values in each interval, not merely finitely many sampled t. Combined with Sections 2–3 this completes the exact minimax proof.

Reproduce by running Python 3 from this directory: python3 R749SPD_SPE_WALSH_POST_HALF_EXACT_CERT.py. The program prints a structured JSON result; no numerical solvers, external dependencies or floating arithmetic are used. A separately executed local exact calculation also obtained both PASS results with the vertex counts shown above.

## 5. Meaning, evidence and continuation

All claims in this note are for the **complete auxiliary Walsh compatible-source family**; they are author-side exact results with independent mathematical review NOT_REVIEWED. This is not native X6/V29/V39 BRC event acceptance, and no theorem about native six-axis dynamics or physical interpretation follows without a provenance- and operation-preserving map. The frozen science pin, P000, active worldview and task-owned source firewall remain unchanged.

This is independent portable research evidence, **not** a shared-task CLAIM, authenticated Result, Driver Review, or promotion. If stored on a GitHub research branch/PR it is published proposed source and has not thereby entered canonical main. The existing research source Activity must only be updated through an actually authorized route and checked receipt.

**Next exact question:** continue beyond t=3/5 on the s=3/5 line; the free minimax radius enters another phase. Extract a candidate center and an exact opposing event lower certificate, then prove a closed real interval using joint-polytope rational vertices. The source-to-native X6/V29/V39 signed-port and provenance bridge remains a separate open mathematical objective.
