# T6 p13 q10 split(4,6): three more complete smooth-domain audits
2026-11-24; continuation of existing Driver lane EM-DVR-DEBB5E, r542; original author EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F. This is separate exact computation with shared inputs, not a clean-context or native Review claim.

## Scope and exact method
Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; under existing higher valuation elimination and common named atom cancellation, each side mass <=2331, maximum prime 13, signed vertical orders (4,6). For atom (q,r), denominator 13(13q+r), mass 169q+13r-1, q0 weights 13r-1. Keep all 12 q0 coordinates. Reuse the six necessary 13-adic congruences, saturated lattice and nearest path lemma at 01e1ae8e6118e439b0da0481c692ff1fdb55ac21:research_notes/driver/2026-11-24_t6_p13_q10_unique_nearest_plane_smooth_split46_audit.md and the modulo-one coset reduction at 212e6c4ba85e10602257683fda17a7371ebf629e:research_notes/driver/2026-11-24_t6_p13_q10_split37_complete_independent_smooth_nearest_audit.md. Rebuilt basis from six successive modular eliminations, HNF and rational LLL delta=3/4; directly verified every row against all six congruences and determinant 13^21. GS minimum exactly 78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349 > 4*4402474. Thus no backtracking needed. No floating comparisons.

## Executed calculation
Trial division gives allowed residue sets:
q1: 1,2,3,5,7,8,9,11,12
q2: 1,2,4,6,7,9,10
q3: 1,3,5,6,9,10,11
q4: 2,3,4,8,11,12
q5: 1,5,7,10,12
q6: 2,3,6,10,12
Positive rosters: all partitions of 4, 2535 literal or 907 smooth. Independently computed literal disjoint counts and traversed all smooth disjoint pairs; no vertical budget skips.

|negative pattern|literal rosters|literal pairs|literal disjoint|smooth rosters|smooth decoded|sphere witnesses|
|---|---:|---:|---:|---:|---:|---:|
|123|1728|4380480|3328128|441|273861|0|
|222|364|922740|839292|84|66143|0|
|1113|4368|11072880|6014736|1155|486444|0|
|total|6460|16376100|10182156|1680|826448|0|

Literal disjoint totals match the three original author certificates exactly. Actual local Python integer search including count loops took 3.51127846 s (excludes basis/positive setup); family loop times 1.12675, 0.26623, 2.06816 s. No sphere leaf reached; thus no both-budget-valid vector. Conditional complete finite exclusion for these three families and their sign reversals. The four author literal witnesses in these families are outside the smooth vertical domain: q123 witness contains (1,4) cofactor17; q1113 witnesses contain respectively (3,7) cofactor46, (1,10) cofactor23, (1,6) cofactor19. This explains why they do not appear in the smaller domain.

## Reproduction
Use original replay a466be736446891b423809b0ba23cb37ec123502:research_checks/T6_P13_Q10_SPLIT3_7_NEG1123_INTEGER_GS_REPLAY_20261124.py through particular(), then extend q to 1..6, use only the above smooth labels for c_atom and reduce each rational coordinate mod 1 before forming Q,L,B,K,T as in r542. Generate rosters by multiplicity per q with combinations_with_replacement, Cartesian product across q, and all five positive partitions [4],[1,3],[2,2],[1,1,2],[1,1,1,1]. For literal disjoint counting, if negative roster has b_q distinct labels at q, the number of positive rosters in pattern with multiplicities m_q is product_q binom(12-b_q+m_q-1,m_q). Sum over positive partitions and literal negative rosters. For each smooth pair skip common named atom, check cp,cn<=2331 and set R=(2331-cp)^2+(2331-cn)^2. Apply r542 exact nearest decoder to c=(pc-nc) mod Q. At any leaf recover integer u and check all congruences, exact weighted norm and masses. The actual search verified integer scaling B and exact lattice row membership. Completeness follows from full finite roster traversal and uniform nearest condition.

## Sources and frontier
Author immutable certificates:
- fef1fc8f8021392cd3539bc7f162a46e37ac995a:research_checks/T6_P13_Q10_SPLIT4_6_NEG123_FULL_AUTHOR_EXACT_CERT_20261124.json
- 972539587133573719405e778c5b3805d603fa8a:research_checks/T6_P13_Q10_SPLIT4_6_NEG222_FULL_AUTHOR_EXACT_CERT_20261124.json
- 39cb639638accc240cbbbce2d5d4a33083235447:research_checks/T6_P13_Q10_SPLIT4_6_NEG1113_FULL_AUTHOR_EXACT_CERT_20261124.json
All read at immutable commits. Author checkpoint r112 reports q1113 complete and q1122 next; preserve that author direction. With previous r541 five families, split(4,6) now has eight independently checked families, 1,063,688 total smooth searches, zero relaxed sphere leaves. Remaining q1122/q11112/q111111 are not covered by this audit.

## Control
Consumed original dvr-20261124-1200-t6-child-current-read-v1: SUCCEEDED, observed 2026-11-24T04:05:05Z, p17 order1 child DONE/COMPLETE/ACCEPTED, RR-81586AD70E1CEA1B7140 and DR-A550BA4AE2C2C51AA899, historical admission, no duplicate action; execution_authorized=false. Current em_status connected, checkpoint r542 read. Sites profile discovery advertised only d25 permanent researcher and driver, no verified own EM-DVR-DEBB5E custody binding; no adoption. Backlog checkpoint list r461 observed, detailed read returned UPSTREAM_OUTCOME_UNKNOWN (read operation, no mutation). No new claim, protected review, dispatch, Task/Result/mother closure or schedule change. Next: recover original own DA binding, associate actual new scope when authorized, check author-completed remaining split46 families without duplicating in-flight work. T6 OPEN, GEO6 incremental scope unchanged.
