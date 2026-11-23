# X6 R141 — sharp lower one-sided D rigidity and maximal asymmetric uniform BRC tube

Date: 2026-11-23 (Asia/Shanghai). Status: AUTHOR EXACT RATIONAL / POLYNOMIAL CERTIFICATE PASS; independent mathematical review pending.

## Scope, frozen inputs, and definitions

The conditional four-positive-weight all-six-pair BRC observer is unchanged: integer Port 10, q(x,y,z)=max(sum positive coordinates,sum absolute negative coordinates), ±-quotient only, heights h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z), six gaps g_ij=|h_i-h_j|, and all six weight capacities s=(136+B,312,136+D,B+176,B+D,176+D).

For any positive B,D write F_D(a)=max(g_j(a)/s_j(B,D)), eta_D(B)=min F_D(a) over the full 1,935 Port-10 unoriented integer directions, and N_D(B)={a:2F_D(a)<3eta_D(B)}.

Frozen pins: R121 optimizer at awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122 exclusion at awdawmip/enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94. Exact preceding R138 proof at e8e20fdfce40d5415e2f02b51983c7c5928d30ce, R139 at 2b1956e825436f1c0b722b2b1c511d0d1a047347 and R140 at f9b7ce6ac8523c515c350064c90f0baf5cd032b5 under their research_notes/portable_direct paths. P000 V5, ACTIVE Heartbeat X6, the exact original six-pair observer and all source-firewall pins are preserved. No formal shared-task CLAIM/Result/Review is asserted.

Let C={(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)} modulo ±.

## Theorem

**For all real B>0 and 448<=D<=500, the strict near-direction set N_D(B) equals C.** The supremal open lower one-sided radius about D=500, uniformly over B>0, is exactly 52: every D in (500-52,500] preserves C, and every proposed lower radius exceeding 52 fails.

Combining R140's sharp upper radius 28 yields the largest asymmetric open connected rigidity interval about D=500 valid for every B>0:

**448<D<528, with maximal lower/upper distances (52,28).**

At D=448 the four-direction set also persists for every B>0; on the upper side the open formulation suffices for sharpness. Relative to R139's symmetric radius 500/41, this identifies the distinct mechanisms that constrain each side.

## Proof: refined perturbation bound and exact certificates

Write F_0=F_500 and eta_0=eta_500(B). On the seven exact R138 B-chambers, eta_0=K/(L0+L1 B), with boundaries 0,316/7,320/7,46,556/7,796/7,136,+infinity. Split the first B-chamber at B=20, producing eight rational chambers. The new exact checker proves the following statements for every B>0.

First, every insider a in C obeys F_448(a)<=125 eta_0/88. Each of the 8 x 4 x 6 = 192 pairwise inequalities is affine in B and is checked at rational chamber endpoints (plus the recession slope of the final unbounded chamber):
125 K s_j(B,448)-88 g_j(a)(L0+L1 B)>=0.
Since D<=500 increases scores and D>=448 decreases them relative to D=448, F_D(a)<=F_448(a); eta_D>=eta_0. Thus every insider satisfies F_D(a)/eta_D<=125/88<3/2 throughout 448<=D<=500.

Second, put m(B)=min(B,136). For every 448<=D<=500 and every direction a, the maximal denominator-distortion ratio among the three changing channels gives
F_0(a)<=F_D(a)<=M(B,D)F_0(a), where M(B,D)=(500+m)/(D+m).
Therefore eta_0<=eta_D<=M(B,D)eta_0.

For every outsider a and each of the eight B-chambers, the checker finds one fixed pair j, uniform throughout that chamber, with
2g_j(a)(L0+L1B)(448+m)-3K s_j(B,500)(500+m)>=0.
For B<=136, m=B, so this is a quadratic polynomial in B; for B>=136, m=136 and it is affine. A quadratic's minimum on a bounded interval occurs at an endpoint or its interior vertex when convex. Both endpoints and any such exact rational vertex are checked; the infinite tail checks the affine recession slope. All 8 x 1,931 = 15,448 complete exclusion certificates pass. Consequently,
F_0(a)/eta_0 >= (3/2)M(B,448).
For 448<D<=500, M(B,D)<M(B,448), and hence
F_D(a)/eta_D >= F_0(a)/(M(B,D)eta_0) >3/2.
At D=448 the same bound is >=3/2, sufficient to exclude outsiders under the strict criterion. This establishes the complete set C on the entire stated real-parameter strip.

## Proof of sharpness (explicit new entering direction)

At B=20, for every 440<=D<=448, an additional full-population exact certificate checks all 1,935 directions and proves eta_D(20)=6/(D+20); the explicit optimizer (1,0,0) attains equality. The pairwise lower certificates use one fixed gap for each direction throughout the D interval; after cross multiplication, each inequality is affine in D and holds at both D=440 and D=448.

The previously excluded direction b=(6,-1,0) has gap vector (3,6,3,3,0,3) and F_D(b)=1/52 for all D in [440,448]. At D=448 it satisfies 2F_D(b)=3eta_D(20); for every 440<=D<448,
2F_D(b)=1/26 < 18/(D+20)=3eta_D(20),
so b **enters** the strict near set. Every proposed lower radius r>52 includes a point D=448-epsilon within this interval and with 500-D<r. Therefore no larger uniform lower radius exists.

## Verification evidence and next problem

The new standalone follow-up checker imports only the exact R140 population/gap/affine helpers, uses Python 3 standard-library Fraction and was executed locally with output:

    R141 SHARP LOWER ONE-SIDED UNIFORM D-TUBE CERTIFICATE PASS
    population 1935 inside_448 192 outsider_quadratic 15448
    sharpness_lower_witness_checks 1935 sharpness_full_optimizer_replays 4
    full_fraction_near_replays 54 D_interval (448, 500) lower_open_radius 52

Its source is research_notes/portable_direct/x6_r141_sharp_lower_D_tube_verify.py. The exact finite polynomial inequalities, not the sampled replays, prove the continuum claim; the sharp witness holds on an entire positive-length D interval.

Verification scope: AUTHOR PROOF/CERTIFICATE PASS for the conditional six-pair observer. Independent mathematical review is pending; no inference is made about native six-axis time dynamics.

Next: classify the full first-contact near-direction walls on the two sides of the maximal uniform tube, including whether the lower equality is unique at B=20 and whether the upper limit B->0 has additional coincident candidate changes. Analyze the 2D adjacent cells without assuming monotonicity outside the proven band.
