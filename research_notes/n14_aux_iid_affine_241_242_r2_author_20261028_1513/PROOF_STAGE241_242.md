# Stage241–242: exact all-real optimality in external N=14 ternary IID testing

**Status:** AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. Researcher local ID: EM-R2-20261028-1513-PORTABLE (not a native service ID). Scientific predecessor: Stage240 in PR #1571 at commit cc4bd0367d139582d8f7333bd03e9f8f75efd4e6. Date: 2026-10-28.

## Exact model and theorems

Independent observations have laws P=(3,1,20)/24 and Q=(2,2,20)/24. At an ordered-history-dependent randomized stopping time τ≤14, decide P or Q. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P τ, tQ=E_Q τ and

V14(α) = inf {max(tP,tQ) : eP≤α, eQ≤α}.

The optimization includes **every randomized rule depending on the complete ordered history**.

**Stage241.** For every real number

0 ≤ δ ≤ 5004659375/5851190919168,

V14(α240+δ) = V240 − (936523032/8007455) δ,

with

α240=362608860595/975198486528,  V240=2682386241371/365699432448,

α241=311522546135/835884417024,  V241=755943802981/104485552128.

**Stage242.** For every real number

0 ≤ δ ≤ 1210883875/1950396973056,

V14(α241+δ) = V241 − (5609763192/48435355) δ,

with new exact endpoint

α242=1092145237285/2925595459584, V242=2619507545471/365699432448.

Both results include irrational α and irrational randomized mixing weights.

## Bellman lower bound and exact dual data

For state s=(n,a,b) counting 0 and 1 occurrences in n observations, the exact prefix likelihood ratio is r(s)=Q(w)/P(w)=2^(a+b)/3^a. For positive non-symmetric multipliers λP,λQ, minimize J=tP+λP eP+λQ eQ with Bellman recurrence

B(s)=min{ λQ r(s), λP, 1+ Σ_j P_j B(next(s,j)) }

(the third action is omitted for n=14). The first option decides P, the second decides Q. Thus, for all complete-history randomized rules obeying eP,eQ≤α,

max(tP,tQ) ≥ tP ≥ H−λP eP−λQ eQ ≥ H−(λP+λQ)α,

where H=B(0,0,0). Each recurrence is evaluated with exact rational arithmetic over all 680 states.

Stage241: λP=452793624/8007455, λQ=483729408/8007455, H=265760568220237397/5229145980094464. Exactly 11 two-action ties and 1229 strictly positive action gaps; minimum positive gap 78125/57653676. Ties: (4,1,0), (5,1,1), and (n,1,0) for n=5,...,13. All are P/continue except the Q/continue tie at (5,1,1).

Stage242: λP=2707386744/48435355, λQ=2902376448/48435355, H=1594127315973221257/31629967560566784. Exactly 12 two-action ties and 1228 strictly positive action gaps; minimum positive gap 390625/348734556. Ties: (3,1,0), (4,1,1), and (n,1,0) for n=4,...,13. All are P/continue except the Q/continue tie at (4,1,1).

No triple ties exist. The exact values and strict gaps were computed, not inferred from floating-point samples.

## Full ordered-history coverage

For every ordered prefix w with the same count state s, P(w) and Q(w) depend only on the counts. Therefore Q(w)=r(s)P(w). After including any preceding randomized survival factors, the conditional distribution of surviving histories at a fixed count state is identical under P and Q. Replace the history-dependent action distribution by its conditional average given state and survival. This **exact occupancy Markovization** preserves all four measures (eP,eQ,tP,tQ), not merely the P objective.

Any Markov randomized finite-horizon policy is a convex mixture of deterministic Markov action tables: draw all state-action coins independently before the run. No state can be visited twice because n strictly increases. If the Bellman lower bound is attained, only Bellman-minimizing actions can occur on reached states. Consequently the complete dual-equality face is the convex hull of the deterministic tie tables; there are exactly 2^11=2048 for Stage241 and 2^12=4096 for Stage242. This is an external IID conditional-sufficiency proof; it is **not** permission to collapse P000 native X6 joint information.

## Global exact supporting-line certificate

For every optimal deterministic table, let D=24^14 and let integer coordinates be X=D(eP−eQ), Y=D eP. For line segment A=(x1,y1), B=(x2,y2), with x1<x2, define

M_AB(X,Y)=(Y−y1)(x2−x1)−(y2−y1)(X−x1).

For each stage, the attached standard-library executable checks **all** 2048/4096 tables against two exact inequalities: M_lower≥0 and M_upper≤0. By convexity these inequalities hold for the whole dual-equality face. The line intersections with X=0 therefore give exact lower and upper attainable balanced errors. Each is realized by a convex mixture of the two explicitly identified endpoint deterministic policies.

Stage241 lower support pair, binary masks (least-significant tie bit first) 5 and 2047:

A=(-1650540247273963520,7114354836803420160),
B=(3022680865353236480,9117163885072220160).

Stage241 upper support pair 2043 and 0:

A=(-2134840366092779520,6924789982596956160),
B=(3130145635544596480,9181212554727260160).

Stage242 lower support pair 5 and 4095 uses the same geometric edge as Stage241 upper support, proving α241 endpoint gluing. Stage242 upper support pair 4091 and 0 is:

A=(-2591590131664158720,6742099893273231360),
B=(3205984270082375680,9226774636878888960).

The exact mixing weights in each policy pair's stated order are:

* Stage241 left: (144132655399,78703892101)/222836547500; right: (29084891811,42644849989)/71729741800.
* Stage242 left: (42644849989,29084891811)/71729741800; right: (123576647361,152873242859)/276449890220.

The script verifies eP=eQ exactly at the edges, the specified exact α and tP values, and **tP>tQ for every single deterministic dual-optimal table**, hence for their mixtures. Thus max(tP,tQ)=tP at the endpoint witnesses. Mixing the two balanced endpoint policies with any real mixing fraction realizes the affine lower bound for every real α in each claimed interval. The support-line inequalities also prove that these are the complete balanced-equality ranges for the two specified dual supports.

## Executed evidence and reproducibility

Run from this directory:

python3 PORTABLE_REPRO_STAGE241_242.py

The program uses only Python standard library: exact Fraction Bellman, an exact suffix-integer DP, and a second implementation traversing **unmerged full ordered histories**, carrying separate positive integer P and Q branch masses. Every root four-measure vector agrees for **all 6144 deterministic optimal tables** (not only selected examples).

Observed exact results:

STAGE241_EXACT_PASS policies=2048 ordered_nodes=1064948 gaps=1229 left=362608860595/975198486528 right=311522546135/835884417024 slope=-936523032/8007455

STAGE242_EXACT_PASS policies=4096 ordered_nodes=1189882 gaps=1228 left=311522546135/835884417024 right=1092145237285/2925595459584 slope=-5609763192/48435355

STAGE241_242_PORTABLE_EXACT_PASS 2254830

Total: 2,254,830 ordered-history DFS nodes. This is **author-side exact math and computational cross-check**, not an independent researcher review, proof-assistant formal check, native Source Result or P000 physical correspondence. The BRC-relevant operation is exact positive branch-mass and provenance preservation; no native BRC engine was claimed as executed. Stage242 multiplier discovery used a floating LP only to generate the candidate; **every theorem-producing validation is exact**.

## Source pins, role, and next question

At this author run, GLOBAL_KNOWLEDGE_V1 canonical-main snapshot was d187403bc326173dddf8248b59b48990dba6d3eb, Enterprise Math main read was cea56a0309506eac575f7604256c464c0caa21ba. The applicable P000 V5, ACTIVE native X6 worldview, joint-observer preservation, BRC preference, portable research protocol and GitHub PR handoff were consulted. Native research_authority_granted=false; active Owner query returned CONTROL_QUOTA. No formal native CLAIM, Source research Result, service-issued researcher identity, independent Driver acceptance or X6 correspondence is asserted. PR storage does not alter those separate statuses.

**Stage243:** identify the first nonzero-width dual support to the right of α242=1092145237285/2925595459584. Reconstruct *exact* positive asymmetric dual multipliers from Bellman ties; calculate complete four-observation measures for every dual-optimal deterministic policy; prove balanced feasible interval with global exact support lines or give a precise rational infeasibility certificate. Preserve full ordered-history semantics, and do not count unreachable zero-width Bellman changes as primal progress. See NEXT_TASK_PACKET_243.md.
