# R5 — Exact global phase diagram for a ternary one-collision BRC observer

**Date:** 2026-10-27. **Status:** author-side mathematical derivation and executed exact checker; UNREVIEWED / NOT_ADMITTED.

**Frozen input:** GLOBAL_KNOWLEDGE_V1 canonical main fd68f262d614470f7aaf2b03d1591656e0dc0373, including normative bootstrap/manual, original P000 V4 (locked), ACTIVE worldview, TASK researcher and BRC/mathematics routes. Enterprise Math main 993762ba159b6b3720948d8069cf24f840e7de02, in particular the earlier exact R5 proof and executable oracle in research_notes/brc_n3_ternary_single_collision_facet_oracle_20261027_r5. No native Task/CLAIM, independent review, or admission is implied by author-side persistence.

## Model, method and target

An EXTERNAL finite positive two-measure P/Q observation tree has root (Q,r,t)=(1,1,0) with likelihood ratio r=P/Q. Histories at time one: a=(1/2,3/2,1), b=(1/2,1/2,1); at time two: ax=(1/4,1,2), ay=(1/4,2,2), bu=(1/8,1,2), bv=(3/8,1/3,2). The only distinct-history collision in nonterminal (time,LR) is ax~bu at (2,1).

At ax and bu, time-three likelihood-ratio outcomes are (1/2,1,3/2), with respective conditional Q weights K_sa=(sa,1-2sa,sa) and K_sb=(sb,1-2sb,sb). Each of ay and bv has a single child with unchanged LR. Assume 0<sa,sb<1/2. All eight leaf probabilities are strictly positive. The identity sa/2+(1-2sa)+3sa/2=1, and its sb version, ensures BOTH source measures conserve mass at each node and globally normalize to one.

At a stopping history the observer chooses P or Q; at nonterminal nodes it may instead continue. The four observable coordinates are O=(P[decide Q], Q[decide P], E_P[tau], E_Q[tau]). A full-history policy may distinguish all physical histories. A *seedless time/LR* behavioral policy must use a common action distribution at each (time,LR), with fresh private randomization, not a persistent root seed. Let the signed objective be J=298 O_1 + 375 O_2 + 37 O_3 - 17 O_4. Write Vf(sa,sb), Vc(sa,sb) for its minima over those two strategy classes.

BRC interface: REUSE_APPLIED to positive weighted branches, two source masses, exact conservation and provenance-preserving LR readout. These are external statistical time/likelihood-ratio observables; no typed native X6 spatial, rotation, Heartbeat time, or three-dimensional slice dynamics is computed. Native transfer requires a separate embedding, readout and relation-preservation proof. P000 is unchanged.

## Theorem — entire admissible parameter square

Define a=5-18sa, b=5/2-9sb. For every REAL pair 0<sa,sb<1/2,

    Vf=281+min(0,a)+min(0,b),
    Vc=281+min(0,b,a+1,a+b).

Consequently the exact all-strategy optimality gap Delta=Vc-Vf is

    Delta=min(18sa-5, 1, 5/2-9sb)  if sa>5/18 and sb<5/18,
    Delta=0                       otherwise.

Every model in the open wedge sa>5/18, sb<5/18 FAILS the necessary all-signed-linear-support / convex-hull-equality gate for complete-history versus seedless time/LR policies. The entire rectangle 1/3<=sa<1/2, 0<sb<=1/6 has *exactly* Delta=1. This extends the earlier small 1/100 neighborhood and its merely lower-bound Lipschitz certificate to an exact global classification for THIS signed normal. Zero gap elsewhere proves nothing about other normals or the underlying nonconvex images.

## Complete proof

**(1) Deterministic minimum principle.** In a finite tree, time increases strictly and a (time,LR) class occurs at most once along each trajectory. Presampling an independent action at each class induces the same trajectory law as fresh seedless behavioral randomization. Thus any behavioral objective is a convex combination of deterministic class-action objectives, so a linear minimum is attained at a deterministic class-action table. The same assertion holds for full-history randomization, with tables indexed by physical histories. Presampling here proves only a property of LINEAR support; it does not introduce a persistent shared seed into the behavioral image, nor claim that the image is convex.

**(2) Terminal decisions.** At terminal LR r the decision errors per Q mass are 298r if deciding Q and 375 if deciding P; stopping time is unaffected by this choice. The pointwise greedy rule therefore decides Q at r=1/3,1/2,1 and P at r=3/2,2. At time three, after the three-outcome kernel K_s, the optimal objective per incoming Q unit is exactly 358-72s (by multiplying each of the three terminal error-plus-time costs by its Q-conditional weight). This is an AFFINE expression over the whole real admissible parameter interval, not an approximation.

**(3) Time-two local choices.** At ay the Q mass is 1/4 and r=2. Deciding P at t=2 costs 489/4; continuing one step with unchanged ratio costs 273/2. Hence stop P is strictly optimal. At bv, Q mass 3/8 and r=1/3; continuing to t=3 and deciding Q costs 32, whereas stopping and deciding Q costs 135/4, so continuation is optimal. At the two collided LR-one histories, stop P is dominated by stop Q because 298<375 and time is the same. Therefore the relevant local comparison is

| history | stop Q | continue to greedy terminal |
| --- | ---: | ---: |
| ax | 169/2 | 179/2 - 18sa |
| bu | 169/4 | 179/4 - 9sb |

Any upstream censoring can make one history unreachable; it does not invalidate optimizing this local decision where reached.

**(4) Full-history Bellman recursion.** At time one history a, stop P costs 827/4, while continuing with ax stop Q and ay stop P also costs 827/4, and continuing from ax instead costs 847/4-18sa. Hence the full optimum at a is 827/4+min(0,5-18sa). At history b, continuing through bu stopped at Q and bv continued costs 297/4; continuing bu also costs 307/4-9sb; stopping Q at b costs 301/4. Thus the full optimum at b is 297/4+min(0,5/2-9sb). Root continuation sums these to 281+min(0,a)+min(0,b), at most 281, whereas root stopping costs 298 (decide Q) or 375 (decide P). Root continuation is always optimal. This establishes Vf.

**(5) Compressed Bellman recursion with one common collided action.** If the shared (t=2,r=1) action is *stop Q*, a's optimum is 827/4 and b's is 297/4; root continuation costs 281. If instead the shared action is *continue*, a optimizes to 827/4+min(0,a), while b can stop Q at b for 301/4 or continue b via bu and bv for 307/4-9sb: its optimum is 297/4+min(1,b). Root continuation then costs 281+min(0,a)+min(1,b). The root again prefers continuing because the first feasible common-action policy costs 281. Taking the minimum of these two alternatives, expanding, and discarding the dominated candidate 281+1 gives Vc=281+min(0,b,a+1,a+b).

**(6) Exact phase case analysis.** For a>=0 or b<=0, direct comparison of the preceding two minima yields Vc=Vf. For a<0<b the full minimum is 281+a, and subtracting it from the compressed minimum gives min(-a,b-a,1,b)=min(-a,1,b), since b>0. This expression is strictly positive precisely when sa>5/18 and sb<5/18. It equals one whenever sa>=1/3 and sb<=1/6. Boundary equality is included in the zero-gap side. This completes the proof for ALL real admissible parameters.

## Independently summed off-neighborhood witness

Take the exact positive rational pair (sa,sb)=(2/5,1/10), outside the prior 1/100 box. One full optimal policy continues root,a,b,ax,bv; stops Q at bu, P at ay; and uses greedy terminal decisions. Its exact four-observable vector is

    Of=(7/20,7/20,19/8,21/8),  J(Of)=1394/5.

One compressed optimal policy continues root,a,ax and stops P at ay, but stops Q already at b; the shared collided rule is continue, with bu unreachable. It yields

    Oc=(7/20,7/20,2,7/4),  J(Oc)=1399/5.

The classification-error coordinates coincide but stopping-time observables differ; full and compressed GLOBAL minima differ exactly by one, not merely the values of these two candidate policies.

## Independent exact execution and mathematical limits

The accompanying actually executed VERIFY.py uses Python standard-library fractions.Fraction to represent affine coefficients (constant, sa coefficient, sb coefficient). After terminal greedy dominance, it enumerates all 3^7=2187 deterministic full-history nonterminal tables and 3^6=729 seedless class tables, minimizing exact intercepts separately for each of the four possible parameter-slope pairs. The resulting exact lower-envelope triples are:

Full: (281,0,0), (567/2,0,-9), (286,-18,0), (577/2,-18,-9).
Compressed: (281,0,0), (567/2,0,-9), (287,-18,0), (577/2,-18,-9).

Because every fixed strategy's objective is affine and the finite strategy set does not depend on sa,sb, these complete coefficient envelopes certify the continuum theorem. A further 100 admissible rational pairs, exact mass-conservation checks, and an independent six-stop-vector calculation of each off-neighborhood witness pass. EXACT_OUTPUT.txt contains the unedited executed stdout. Finite grid testing is NOT the basis of the universal conclusion.

This theorem only excludes models in the stated wedge from support-hull equality via one normal. It does not prove the remainder pass all facet normals; it does not prove equality or inequality of raw real seedless behavioral images when supports do match. Any precise native X6 application and independent mathematical admission remain distinct obligations.

**Next executable research unit:** choose (sa,sb)=(1/10,2/5), outside the excluded wedge where THIS normal has zero gap. Enumerate the exact compressed four-vector convex hull, compute every rational oriented facet (plus affine-hull equations when needed), and run full-history Bellman on each. Record any different separating normal and full witness; only if ALL facets pass may an image-nonmembership search begin. Preserve all source and policy authority boundaries.
