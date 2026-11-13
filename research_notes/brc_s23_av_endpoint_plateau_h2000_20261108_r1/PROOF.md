# S23/AV: exact 1,491-horizon plateau from one endpoint certificate

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR_SIDE_ANALYTIC_PROOF + EXACT_FINITE_CERTIFICATE; independent mathematical review pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged).
Predecessor: Draft PR #1777@ff597f1e19648b3d1fb1f594d6f26f3730fcd0cf; `research_notes/brc_s23_av_unimodular_first_entry_20261108_r1/{PROOF.md,FULL_SATURATION.md,PLATEAU_H510_535.md,VERIFY_H510_535_PLATEAU.py}`.

## Theorem and exact domain

For the two-point S23/AV iid auxiliary experiment with P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28) on labels (1,3,4), define T_h={10^i/7^s : 0<=i<=s<=h}. A prefix with k label-1 occurrences and ell label-4 occurrences has likelihood ratio Lambda=7^(k+ell)/10^k; label 3 allows arbitrary padding. Let N(h) be the least common padded prefix length hitting every open cell in the threshold partition T_h. Then

**N(h)=2,455,069 for every integer 510<=h<=2000.**

This extends the previously certified plateau 510..535 by 1,465 further integer horizons.

## Reduction: one endpoint suffices

T_h is nested in h. Any prefix length hitting every open cell of T_H also hits every open cell of T_h (h<=H), by choosing a finer open cell contained in a given coarser cell, then padding with label 3 if needed. Thus N(h) is nondecreasing. The preceding proof established N(510)=2,455,069, so it suffices to give a complete upper witness at H=2000; a single certified endpoint establishes the entire intervening plateau.

## Complete exact certificate at H=2000

Write r=ln(7)/ln(10/7), Q=10^26. The companion executable derives the strict rational enclosure

545569623581288298975349314/Q < r < 545569623581288298975349315/Q

from exact 45-term Fraction intervals for 2atanh(1/3), 2atanh(1/9), 2atanh(1/15) and the explicit positive geometric remainder 2*z^(2N+1)/((2N+1)*(1-z*z)). The identities are ln7=3ln2-2atanh(1/15), ln(10/7)=2atanh(1/9)+2atanh(1/15), ln2=2atanh(1/3). No floating point is used.

Each threshold is represented in reflected coordinates t(v,k)=r*v-k, with v,k>=0 and v+k<=2000. There are 2001*2002/2=2,003,001 distinct thresholds (7 and 10 are multiplicatively independent), hence 2,003,002 open cells including both unbounded cells. The verifier sorts all thresholds by rational key, then checks all 2,003,000 successive *strict* comparisons against the adverse enclosure endpoints. This is a complete ordering certificate.

Use the inherited determinant-one pair u=(79,431) and w=(380295,2074774), determinant 1, with 0<d=2074774-380295*r<eps=79*r-431 proved by the predecessor's exact integer power comparisons and repeated in the executable. For every shift v0,k0>=0 with v0+k0<=1490, the checker verifies that (v0,k0) and (v0+79,k0+431) are adjacent thresholds at H=2000. There are 1491*1492/2=1,112,286 such cells. The explicit prefix counts

(k,ell)=(2074774-k0, 380295-v0)

are nonnegative, have length <=2,455,069, and their strict membership is checked with the adverse rational bounds.

For every *other* cell, the checker searches integer prefix pairs with k+ell<=15,000 (the larger budget accommodates the extreme right tail at H=2000). A candidate's lookup index uses a rational key only as an accelerator; each accepted witness satisfies **exact integer inequalities**:

- for lower endpoint (vl,kl): (k+kl)*Q > hi*(ell+vl);
- for upper endpoint (vr,kr): (k+kr)*Q < lo*(ell+vr).

An outer cell uses its applicable one-sided test. Its actual run certifies exactly 890,716 other cells, with maximum encountered ell=384. The disjoint total is 1,112,286+890,716=2,003,002; all open cells are covered. Hence N(2000)<=2,455,069, establishing the claimed exact plateau by monotonicity. QED.

## Scope, verification and BRC reuse

The source carrier is the joint count (#label1,#label4) plus label-3 padding. Its declared future operation is likelihood-sign discrimination for suffix length <=h. The threshold partition is a scope-typed safe quotient; Bernoulli z=1/4 compression erases the relevant joint relation. This is an auxiliary statistical experiment, not a native X6/Heartbeat realization, the full-lawful delta4 minimax value or the six-source ten-label mother model. P000/worldview remain unchanged.

`VERIFY_H2000.py` adapts the previously executed exact checker with **only the endpoint range (2000) and short-prefix search budget (15,000) changed**; it preserves all logical tests. Local execution of the equivalent parameterized extension (`python3 verify_extend_15000.py 2000 2000`) returned exact counts in RUN_EVIDENCE.txt, and the published fixed-endpoint checker reproduces the same deterministic counts. Execution time is not part of the mathematical certificate. Native control reads in this research turn returned BACKEND_IDENTITY_OR_VERSION_MISMATCH/STATUS_DATABASE_UNAVAILABLE, operation_sent=false; Owner, CLAIM and Research-Activity-ID are unconfirmed. Independent review pending.

Next: locate the first h>2000 where N(h) exceeds 2,455,069, or derive a scalable determinant-one/continued-fraction covering theorem. Retain full-lawful delta4 and original mother-model bridge as independent tracks.
