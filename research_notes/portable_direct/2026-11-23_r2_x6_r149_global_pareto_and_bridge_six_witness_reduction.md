# X6 R149 — Port-10 global gap-Pareto kernel and exact six-witness optimizer

2026-11-23 (Asia/Shanghai). Status: author complete finite-integer certificate and analytic continuum proof PASS; independent mathematics review NOT_REVIEWED.

## Frozen provenance and model

Continue R148 at enterprise-math@444363f2f8bc670c9fbc0d94a52ca165bb6f69a8:research_notes/portable_direct/2026-11-23_r2_x6_r148_all_positive_B_sharp_eventual_singleton_tail.md. Preserve frozen scientific input R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md and R122@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json.

This is a conditional static centered-three-axis joint six-pair BRC observer theorem in the P000 X6/Heartbeat World setting. The three components are three-dimensional-slice observer variables, not replacements for six native space axes. The conclusion concerns optimizer scores, not native time dynamics, residual attribution, or final Cell addresses.

For a nonzero integer triple a=(x,y,z), put q(a)=max(sum of positive components, sum of absolute negative components). Use all q<=10, identifying a and -a but **not** nonzero multiples. Canonically retain the orientation whose first nonzero component is positive. The population consists of exactly 1,935 directions.

Define h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z), and the ordered six-pair gap vector
g(a)=(|h1-h0|,|h2-h0|,|h3-h0|,|h2-h1|,|h3-h1|,|h3-h2|).
Fix weights (136,B,176,D), B>0,D>0; capacities
s=(136+B,312,136+D,B+176,B+D,176+D).
Let F(a;B,D)=max_j g_j(a)/s_j and eta_10(B,D)=min_a F(a;B,D).

## Theorem 1: exact global 12-vector Pareto kernel

For **every pair of real B>0,D>0**, the optimizer *value* equals the minimum of F over precisely these 12 gap-componentwise minimal Port-10 directions:

P12 = {
(1,0,0), (3,-7,2), (3,-4,1), (4,-4,1),
(4,-1,0), (5,-4,1), (5,-1,0), (6,-4,1),
(6,-1,0), (7,-1,0), (7,2,-1), (9,-5,1)
} / ±.

Every other one of the 1,935 directions is componentwise dominated in the six gaps by one of P12. This is a complete **optimizer-value** certificate; it does not exclude tied minimizers outside P12.

## Theorem 2: exact six-witness reduction for B>=20,D>=528

For **every real B>=20,D>=528**, including all boundary equalities,

eta_10(B,D) = min { F(a;B,D) : a belongs to W6 },

W6 = {(1,0,0),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(9,-5,1)} / ±.

The six fixed gap vectors, in the same order, are:
- (1,0,0): (1,3,7,2,6,4)
- (4,-1,0): (1,0,11,1,12,11)
- (5,-4,1): (1,3,5,2,6,8)
- (5,-1,0): (2,3,4,1,6,7)
- (6,-4,1): (0,0,12,0,12,12)
- (9,-5,1): (0,3,6,3,6,3)

Each score is explicitly the maximum of its six table entries divided by the six displayed capacities. Their minimum is a finite **exact** formula valid on the whole unbounded real quadrant. In particular it solves the previously open optimizer-value calculation for 20<B<136 and 528<=D<1872-B. Full strict 3/2 near-member classification on that strip remains open.

## Complete proof

1. If u_j<=v_j for all six coordinates and all capacities are positive, then max_j(u_j/s_j)<=max_j(v_j/s_j). Exhaustively enumerate all integer triples in [-10,10]^3, rejecting zero, q>10 and negative-first-nonzero orientations. Exactly 1,935 remain. Compute the six displayed **integer** gaps. Checking each pair for six-coordinate weak dominance yields exactly the P12 minimal elements and covers every other direction with a P12 dominator. This proves Theorem 1 uniformly for all positive real B,D. The attached checker implements the complete loops and assertions, not a sample search.

2. The fixed second gap is g1=3|x+4y+10z|, and s1=312. The full exact population splits into **1,890** with g1>=6 and **45** with g1<=3. Every first-group direction has F>=6/312=1/52. At the lower corner B=20,D=528, the witness (1,0,0) has F=max(1/156,3/312,7/664,2/196,6/548,4/704)=3/274. All capacities are monotone nondecreasing as B,D increase. Therefore throughout B>=20,D>=528,
eta<=F((1,0,0);B,D)<=3/274<1/52.
Thus none of those 1,890 directions can minimize.

3. Among the 45 small-gap directions, exactly six are W6. Each of the remaining 39 is six-coordinate weakly dominated by an element of W6. Lexicographically first dominator assignment gives (1,0,0):16, (4,-1,0):18, (6,-4,1):5 (total 39); these integer counts are asserted in the checker. Their scores cannot beat W6 for any positive capacities. Combining this with step 2 gives Theorem 2 for **all real parameters** in the stated quadrant.

The six-witness representation is not claimed to be irredundant on each smaller region. To determine all near-optimal members rather than only eta, all 1,935 original directions and strict F<(3/2)eta conditions must be considered.

## Verification and next question

Companion independently runnable Python standard-library Fraction verifier: research_notes/portable_direct/x6_r149_global_pareto_six_witness_verify.py. Actually executed 2026-11-23:

R149 GLOBAL PARETO AND SIX-WITNESS PORT-10 CERTIFICATE PASS
port_unoriented 1935 global_pareto 12
B>=20,D>=528 fixed-gap-excluded 1890 small-gap 45 six_witnesses 6
small-gap other 39 witness assignment [((1, 0, 0), 16), ((4, -1, 0), 18), ((6, -4, 1), 5)]
monotone_upper 3/274 fixed-channel_floor 1/52
exact_fraction_full_population_crosschecks 100

The 100 rational replays cover fractional and integer weights, lower boundary, large parameters, and serve as a crosscheck; the continuum proof is the finite exact dominance certificate plus the explicit monotonicity inequality.

Next: use the six-witness envelope to identify optimizer branch walls on 20<B<136,528<=D<1872-B; then classify strict 3/2 near-members and potential simultaneous exits/entries there. Frozen R121/R122 pins and P000 unchanged. Independent review NOT_REVIEWED, formal Result/Review NOT_SUBMITTED; this file grants no shared-task CLAIM.
