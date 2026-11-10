# PREFIX-659-R6 — Exact BRC boundary competitor, eightfold region dominance and slot-dependent slope transition

Date: 2026-11-10 (Asia/Shanghai).
Mode: independent portable TASK_RESEARCH.
Status: AUTHOR_PROVED / EXACT_FRACTION_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Researcher-ID: EM-DIRECT-BFB9C8. Research-Activity-ID: RA-3B833E392DFA46C3DBFC96E4.

## Model, question and predecessor

The frozen BRC signed two-informative-direction first-stop statistical observer has parameters (p,z) in [0,1]^2, and 189 survivor layers, numbered n=0,...,188, followed by extinction at n=189. Here these parameters are statistical observer probabilities, not native spatial axes or a native two-dimensional plane.

Let Y=max(Y_p,Y_z) for two independently Poissonized first-stop clocks, μ=E[Y], H=E[Y²]/2, W=2H−μ², V_q(p,z)=Var(T_q)=q²W−qμ. The actual slot counts are q=12 and q=24; previous results permit analytic interpolation over real 12≤q≤24.

PREFIX-657 exact replay certified P=(3/20,1/8), V_12(P)<51525.771, V_24(P)<208463.104. PREFIX-658 established full [0,1]^2 eightfold reflection/swap symmetry and eight pairwise disjoint squares S around P's orbit, with S=[3/20−r,3/20+r]×[1/8−r,1/8+r], r=61/2^24. This note tests a different branch, p=0, and compares its continuum against the old eight squares.

## Theorem 659.1 — Exact boundary Gamma reduction and stronger variance witness

For the frozen binomial survivor row counts A_n(k), the original recurrence has complete rows for 0≤n≤24, loses both same-sign paths at n=25 and never restores them. Thus the all-zero-sign path contributes s_n(0)=1 for n<25 and s_n(0)=0 for 25≤n≤188. At p=0 the first Poissonized clock is exactly Gamma(shape=25,rate=1).

With s_m(z)=Σ_k A_m(k) z^k(1−z)^(m−k) and w(n,m)=binom(n+m,n)/2^(n+m+1), define

    a_m = 1 − Σ_(n=0)^24 w(n,m),
    b_m = (m+1) − (1/2) Σ_(n=0)^24 (n+m+1) w(n,m).

Substitution into the exact two-clock moment kernels gives the one-dimensional identities

    μ(0,z) = 25 + Σ_(m=0)^188 a_m s_m(z),
    H(0,z) = 325 + Σ_(m=0)^188 b_m s_m(z),
    W(0,z) = 2H(0,z) − μ(0,z)^2.

A new independent full recurrence replay using only Python integers and Fraction proves, for Q=(0,19/128), the strict rational bounds

    89.455 < μ(Q) < 89.456,
    605.010 < W(Q) < 605.011,
    86048.098 < V_12(Q) < 86048.099,
    346339.323 < V_24(Q) < 346339.324.

Hence Q exceeds the earlier P by >34522.327 for q=12 and >137876.219 for q=24. The full original [0,1]^2 parameter domain includes Q.

## Theorem 659.2 — Eight new boundary rectangles strictly dominate eight prior squares

Set z0=19/128, hp=2^(-17), hz=2^(-16), and

    J=[0,hp]×[z0−hz,z0+hz].

For EVERY x∈J, y∈S and real q∈[12,24],

    V_q(x)−V_q(y) > 2600.

By PREFIX-658 symmetry this holds for every x in any of the eight reflected/swapped images of J and every y in any of the eight images of S. The new eight rectangles are mutually disjoint. Each rectangle has area 2^(-32), which is exactly 16384/3721 ≈4.403 times the area of an old square S. This gives a strict exclusion certificate for the previous eight-square candidate orbit.

Proof. Write f_n(k)=A_n(k)/binom(n,k)∈[0,1]. The Bernstein difference identity holds on the closed probability interval, including u=0:

    s'_n(u)=n Σ_(k=0)^(n−1) (f_n(k+1)−f_n(k))
                    binom(n−1,k)u^k(1−u)^(n−1−k).

Thus |s'_n(u)|≤n for all u∈[0,1]. On the z band about z0, and on the old S, the established binomial covariance score bound gives |s'_n(u)|<21 because n≤188 and u(1−u)>47/441. The exact nonnegative Poisson kernel coefficients multiplying s_n in μ lie in [0,1], and those in H lie in [0,n+1]. As μ≤378, these yield:

    |μ_p|≤17766, |H_p|≤2250360, |W_p|≤17931816;
    |μ_z|<3969,  |H_z|<377055, |W_z|<3754674.

Here the p bounds apply including the boundary p=0; the z bounds apply along the specified interior bands. Consequently with

    Kp(q)=q²·17931816+q·17766,
    Kz(q)=q²·3754674+q·3969,

the path integral gives V_q(x)>V_q(Q)−hp Kp(q)−hz Kz(q) for x∈J. For y∈S, V_q(y)<V_q(P)+2r Kz(q). Combining these two estimates with exact point enclosures yields:

    V_12(x)−V_12(y) > 691399957213/262144000 > 2600;
    V_24(x)−V_24(y) > 1355577599893/131072000 > 10000.

For fixed x,y, [V_q(x)−V_q(y)]/q=q(W(x)−W(y))−(μ(x)−μ(y)) is affine in q. Endpoint positivity and q≥12 imply the uniform >2600. Symmetry transfers comparisons to all orbit pairs. Distinct rectangle bands lie around 0,z0,1−z0,1, and the ratio of areas is (hp·2hz)/(2r)^2=16384/3721. QED.

## Theorem 659.3 — Slot-dependent boundary slope transition

At p=0, direct polynomial differentiation yields s'_n(0)=A_n(1)−n A_n(0), equal to 25 precisely for n=25,...,33 and zero elsewhere for 0≤n≤188. Use this in the differentiated exact two-clock moments. Independently differentiate the one-dimensional z kernels by the exact score formula. The companion certificate establishes

    4<μ_p(Q)<5,        −535<W_p(Q)<−534,
    547<μ_z(Q)<549,   42<W_z(Q)<43,

and the sharpened strict intervals

    −77041 < ∂p V_12(Q) < −77039,
    −308046 < ∂p V_24(Q) < −308044,
    −451 < ∂z V_12(Q) < −449,
    11344 < ∂z V_24(Q) < 11347.

The exact rational slot threshold q0=μ_z(Q)/W_z(Q) obeys 12<q0<13. Since ∂zV_q(Q)=q W_z(Q)(q−q0), the q=12 scheme increases when z moves a little *left* of z0 while q=24 increases when z moves a little *right* of z0. For every real 12≤q≤24, ∂pV_q(Q)<0 by the endpoint-affine formula ∂pV_q/q=qW_p−μ_p. Thus the same boundary candidate has a strictly inward-decreasing p direction while the preferred z adjustment changes with q.

## Exact verification, reuse and continuation

The companion `PREFIX659_R6_EDGE_SLOT_CERTIFICATE.py` reconstructs every row by the frozen integer predicate and dyadic bisection, verifies first removal and 189-layer extinction, evaluates the boundary moments and derivatives exactly, and checks 37 integer/Fraction assertions: `ALL_CHECKS_PASS 37`. `PREFIX659_R6_RESULTS.json` records strict intervals, exact margins, derivative caps and the next reproducibility coordinates. The arithmetic is exact; no floating-point comparisons are used as proof premises. This is an independent finite frozen statistical observer replay, not a new original 96-port dynamics run.

BRC method: COMPOSE_APPLIED. Carrier retains integer signed-path multiplicities and first-stop survival; observer comprises Poisson maximum, first-stop sampling moments and probability derivatives. Its boundary reduction is justified by an exact path identity, not by a lossful quotient of native six-axis state. P000, ACTIVE worldview and frozen source pins are unchanged.

Predecessor exact source paths: PREFIX-657 competitor at `research_notes/portable_direct/2026-11-10_prefix657_r6_external_competitor_rectangle.md` (04c8f9a231545af52e2888d255dcfe54143587e9), PREFIX-658 symmetry and S at `research_notes/portable_direct/2026-11-10_prefix658_r6_full_domain_octant_competitor_orbit.md` (e421d6090a4550333f969eca1ecba55c05b5811a). Scientific pin is f42f2906d77f24085c123f3ccfe9667d41caa96d.

Mother objective: full-domain maximization of V_12,V_24 on [0,1]^2. Next discriminating unit: certify second-derivative intervals for z↦V_q(0,z), isolate q=12 and q=24 one-dimensional stationary points on opposing sides of 19/128, then test ∂pV_q across the isolated boundary bands. Feed new edge lower bounds into triangular-chamber Bernstein elimination. Mathematical status remains AUTHOR_PROVED/EXACT_FRACTION_REPLAY_CHECKED/UNREVIEWED/NOT_ADMITTED; formal CLAIM/Result/Review was not created.
