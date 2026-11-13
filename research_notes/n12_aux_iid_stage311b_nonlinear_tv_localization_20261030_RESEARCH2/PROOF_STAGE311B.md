# Stage311-B — nonlinear TV localization extends the full eight-rate Pareto interval

Status: PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Pinned global main: ed4a632e398d681d4baf437fd16cfb38883fdef9 (verified 2026-10-30).
Pinned Enterprise Math main: 89776e25a79ccba39ece5b31cc7ac67d1935cf5c.
Direct parent: Stage310-B proof on PR #1736 commit 9d1b435ea7278eeb6b67472970cca56a3958aac0.
Author scope: scheduled Researcher2 portable work, not a native Source role/CLAIM/Result. Current control owner lookup returned CONTROL_QUOTA and Site configuration reports research_authority_granted=false.

## Frozen auxiliary positive-rational model

S is fair. Conditional on S, J matches S with probability 7/8, W matches S with probability 3/4, and Y has Bernoulli(p_S), with p0=1/4, p1=3/4, independently. Private h=(J,W,Y) has source-pair counts (a_h,b_h)/256:
000:(63,1), 001:(21,3), 010:(21,3), 011:(7,9), 100:(9,7), 101:(3,21), 110:(3,21), 111:(1,63).
Public G=(W,Y); future F returns Bernoulli(p_S) in the target, while H is independent fair. The approximation fixes arbitrary eight t_h in [0,1], one per private h, throughout three F calls. H/F can adapt using public history. P(t) is worst TV of (G,trace), T(t) worst TV of tagged (S,J,G,trace). All-F attains each worst risk: any adaptive H/F policy is a common source-preserving randomized map from three presampled F bits (insert independent H bits), so data processing upper bounds its TV by all-F. MAP t_h*=p0 if a_h>b_h, else p1 has P0=11/256 and T*=77/1024. F_P(p)=min{T(t):t in [0,1]^8, P(t)<=p}.

## Theorem

Let
q(u)=9u/128+3u^2/32-u^3/8,
g(u)=117u/4096-123u^2/1024+23u^3/256,
r=9/400 and U=51/5000.
Define E_new=q(U)=726808599/1000000000000.

For EVERY REAL epsilon in [0,E_new], write u for the unique point in [0,U] solving q(u)=epsilon. Then the full unrestricted eight-real-rate optimum is

F_P(11/256-epsilon) = 77/1024+g(u).

At epsilon>0 there are EXACTLY TWO global minimizers: MAP except t_100=1/4+u, or MAP except t_011=3/4-u. MAP alone minimizes at epsilon=0. The previous Stage310-B interval was [0,9/20800]; the new interval is exactly 1049834643/625000000 = 1.6797354288 times as wide.

## New global entry-barrier lemma (the proof increment)

Let D3(p,t)=TV(Bern(p)^tensor3,Bern(t)^tensor3) and c=3(3/4-r)^2=254043/160000. For EVERY p in {1/4,3/4} and t in [0,1],

D3(p,t) >= c min(|p-t|,r).                                      (L)

For p=1/4 project the three-bit law onto the all-zero event with probability (1-t)^3. Inside |t-p|<=r, the derivative magnitude of (1-t)^3 is >=3(3/4-r)^2, hence the mean-value inequality proves (L). Outside that interval, monotonicity makes the event-probability difference at least its value at the boundary; the same c*r lower bound applies. For p=3/4 use the all-one event of probability t^3. Event projection cannot increase TV, so (L) is valid for the original full three-bit TV. Importantly the bound is GLOBAL, truncated only on its right side.

Stage310-B's source-tagged fiberwise TV triangle inequality is

T(t)-T* >= sum_h |a_h-b_h| D3(t_h,t_h*) /256.                    (1)

The least |a_h-b_h| equals 2. Thus ANY displacement |t_h-t_h*|>=r entails

T(t)-T* >= c*r/128 = 2286387/8192000000.                      (2)

The single-light-fiber witness at epsilon=q(u) costs g(u), and q,g are strictly increasing on [0,r]. Exact rational identities at U show

g(U)=8926584723/32000000000000,
c*r/128-g(U)=18457983/128000000000000 > 0,
q(U)<q(r)=833571/512000000.

For every epsilon<=E_new a candidate with P=P0-epsilon and T=T*+g(u) exists, and its cost is STRICTLY BELOW the outside-radius barrier (2). Any true global minimizer exists by compactness and costs no more than this witness, so EVERY minimizer lies in the OPEN cube max_h |t_h-t_h*|<r. No assumption of prior localization is used. When epsilon=0, (1) already gives the unique MAP minimizer.

## Full eight-dimensional exchange proof (unchanged inner-radius certificate)

For |t-t*|<r the four public G=00 signs at MAP have residuals (13,3,-3,-13)/1024 for k=0,1,2,3 ones. On [p0-r,p0+r]=[91/400,109/400], the exact maxima of |d/dz(z^k(1-z)^(3-k))| are L=(286443,39243,51557,35643)/160000. Multiply by maximum total public fiber mass 5/16 and r: the four strict remaining sign margins are
(22013,246813,135987,2279213)/204800000.
G=11 follows by complement symmetry; the initially zero residual for G=01 and G=10 can only add nonnegative TV. Therefore public gain P0-P(t) is no greater than the sum of inward outer-fiber gains: light h=100,011 gain q(v) and heavy h=000,111 gain 4q(v); outward or middle changes produce no positive gain. Tagged excess cost is fiberwise additive; inward light cost is g(v), heavy cost H(v) (the explicit Stage310-B polynomial), while all other rate changes have nonnegative, and unless zero strictly positive, costs by (1).

The exact Stage310-B derivative certificates on the SAME radius r establish: q'>0; C(x)=g(q^(-1)(x)) is increasing strictly concave with C(0)=0, C'(x)<=13/32<1; heavy M(x)=H(q^(-1)(x/4)) satisfies M(x)>x for x>0. Because E_new=q(U)<q(r), all four inverse branches needed for trimming gains are within the same certified radius. For any feasible competitor, trim its positive inward gains to nonnegative x_i summing to epsilon. Then
T-T* >= C(x_light1)+C(x_light2)+M(x_heavy1)+M(x_heavy2)
      >= C(sum x_light)+sum x_heavy
      >= C(epsilon).
The strict inequalities unless all gain is in one light fiber, and strict positive cost of every other deviation, leave precisely the two claimed minimizers. Equality is attained by the two witnesses, proving the continuum theorem.

## Verification / boundaries / continuation

The standard-library Fraction program (REPRO_STAGE311B.py, executed stdout alongside this file) independently checks the strictly positive eight source pairs, the exact nonlinear barrier and four public sign margins, and all 128 (S,h,three-F-output) rational atoms for MAP and four light-fiber witnesses including U. It prints STAGE311B_NONLINEAR_TV_LOCALIZATION_EXACT_PASS. That FINITE verification is evidence for the listed rational identities; the continuum conclusion rests on lemma (L) and the inherited Stage310 analytic exchange proof, not on finite enumeration.

BRC is used as an exact positive-rational weighted, provenance-preserving branch carrier. No signed-amplitude cancellation or native P000 X6/triadic/time/Cell-address correspondence has been established. The latter are separate proof obligations. No native CLAIM, Source Result, review or admission was acquired. Next Stage312-B: replace the single-event D3 bound by the exact piecewise three-bit TV; sharpen the all-eight localization/sign certificate or isolate the first genuine Pareto active-set transition without relying on floating search.
