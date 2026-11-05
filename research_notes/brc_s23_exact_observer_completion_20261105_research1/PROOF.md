# S23 exact observer completion and sharp information-repair radius

Date: 2026-11-05. Frozen source: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34, research_notes/brc_n4_s23_asymmetric_hull_gap_sqrt43_20261101_research1/PROOF.md. Prior three-tag Chebyshev theorem: enterprise-math@a20b81e9766502f6d8ca17a72fc898e0d26ae3c7, PR #1772. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Source and four tagged Bernoulli events

Let Q=[1/2,7/8]×[1/8,1/2]×[1/2,7/8], theta=(a,b,c). The frozen six source preparations, retaining the A/B branches' *common* b, are
- AU0=AU1=(a,(1-a)b,(1-a)(1-b)/2,(1-a)(1-b)/2);
- AV=(a,0,(1-a)c,(1-a)(1-c));
- BU0=BU1=(1/4,3b/4,3(1-b)/8,3(1-b)/8);
- BV=(1/4,1/4,1/4,1/4).

Write P(theta) for the six-row law, with D(P,P')=max_source TV(P_source,P'_source), TV=(sum_stop absolute differences)/2.

Four source-tagged Bernoulli event probabilities are
p=AV:stop1=a,
q=AU0:stops3+4=(1-a)(1-b),
r=BU0:stop2=3b/4,
w=AV:stop3=(1-a)c.

The prior three-tag result used J=(p,q,r) to preserve the restricted legal and hull Chebyshev radii. This new result classifies *pointwise full-source reconstruction*, which is a distinct declared operation.

## Theorem A: exact continuum source metric

For EVERY theta,theta' in the real box Q, with Δ meaning value(theta)-value(theta'),

    D(P(theta),P(theta')) =
    max(|Δp|, |Δq|, |Δr|, |Δw|, |Δp+Δq|, |Δp+Δw|).     (A)

Proof: Group AU's equal third/fourth atoms, obtaining three effective categories (p,1-p-q,q). For two three-category probability laws, TV equals the largest absolute coordinate difference, since three signed coordinate differences sum to zero. Thus AU-TV=max(|Δp|,|Δq|,|Δp+Δq|). AV has three effective categories (p,w,1-p-w), hence AV-TV=max(|Δp|,|Δw|,|Δp+Δw|). BU-TV=3|b-b'|/4=|Δr| and BV-TV=0. Taking the maximum over the six tagged rows proves (A) over the entire real box.

Equation (A) makes the *joint-event contrast* explicit: a maximum of individual Bernoulli-coordinate TV distances may miss the coupled Δp+Δq and Δp+Δw directions.

## Theorem B: complete observer bases among the four designated events

Exactly the following three-tag subsets of {p,q,r,w} determine the entire six-source law (and uniquely its legal parameters):

- (p,q,w): a=p; b=1-q/(1-p); c=w/(1-p).
- (p,r,w): a=p; b=4r/3; c=w/(1-p).
- (q,r,w): b=4r/3; a=1-q/(1-b); c=w/(1-a).

Every denominator is positive on Q: 1-a>=1/8 and 1-b>=1/2. Substitute recovered a,b,c into the frozen formulas above. The remaining triple (p,q,r) fixes a,b but has no dependence on c; choose (a,b)=(1/2,1/8), and c=1/2 versus 7/8.

No two among these four designated tags recover the full law. Any pair without w has the preceding c counterexample. For (p,w), fix a=c=1/2 and compare b=1/8,1/2. For (q,w), compare theta=(1/2,1/2,1/2) and theta'=(2/3,1/4,3/4): both have (q,w)=(1/4,1/4), but a differs. For (r,w), compare (1/2,1/4,1/2) and (2/3,1/4,3/4): both have (r,w)=(3/16,1/4) but a differs. All examples belong to Q, and their P laws differ. Any singleton inherits a failing pair.

Hence, within these **four designated event kernels**, the inclusion-minimal complete readout families are exactly (p,q,w), (p,r,w), (q,r,w), all with three tags. The old (p,q,r) was already sufficient for the earlier *Chebyshev optimum* but is not a full-law sufficient statistic.

## Theorem C: sharp minimax source reconstruction from the old triple

Allow ANY deterministic reconstruction G mapping the observed triple J=(p,q,r) to six probability rows, including nonlawful output rows. Define

    E(G)=sup_{theta in Q} D(P(theta),G(J(theta))).

Then

    inf_G E(G) = 3/32.                                      (B)

Lower bound: theta_-=(1/2,1/8,1/2), theta_+=(1/2,1/8,7/8) have identical J, yet D(P(theta_-),P(theta_+))=(1-a)|c_+-c_-|=(1/2)(3/8)=3/16. They must receive the SAME reconstruction G(J). The triangle inequality for D implies max of their errors >=3/32.

Upper bound: recover a=p and b=4r/3 from J, choose lawful c_*=11/16 (midpoint of [1/2,7/8]), and output G_*(J)=P(a,b,c_*). Its sole varying source is AV, and for every real theta in Q

    D(P(a,b,c),G_*(J(a,b,c)))=(1-a)|c-11/16|
                              <=(1/2)(3/16)=3/32.

Equality holds at a=1/2,c=1/2 or 7/8, proving sharpness even among lawful reconstructions. Consequently, the sharp largest D-diameter of a J-fiber is 3/16. This is a quantitative exact repair certificate: w recovers the discarded c-sensitive relation.

## Evidence, reuse, and next interface

BRC: REUSE_APPLIED; exact frozen positive four-stop source carrier with provenance, deterministic event kernels, shared b, and full-source TV. The theorem distinguishes (i) preservation of a specified optimization radius and (ii) faithful reconstruction under later declared source operations.

VERIFY.py executed using Python standard-library Fraction. It checks 8 legal-box vertices, 64 ordered vertex-pair metric equalities, all three triple inverse formulas at vertices, six explicit noninjective two-tag witnesses, the sharp fiber and 8 midpoint reconstruction endpoint identities. The displayed analytic arguments prove the stated real-continuum claims.

The unrestricted original ten-decoder R_beh(k,10) question requires the lawful decoder/encoder interface and actual risk objective to test a composition or hypothesis-independent Markov kernel. This theorem supplies source-exact event coordinates and distance formulas for that next bridge, without changing the previous [1/2,2/3] bracket for k=4,6. Native formal CLAIM/independent review remain pending.
