# EC49FDS — Exactly-two-word H2/H3 BRC seed classification and four full extensions

Date: 2026-11-07. Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Scientific predecessor: EC49FDR, author branch head a270b8da692429e546eb1dd17bf0efd06e475601. P000 and ACTIVE Heartbeat X6 worldview remain unchanged.

## Exact finite theorem (two selected words at each of H2,H3)

Use the frozen six operation letters a,c,d,e,f,g with their *ordered signed native X6 primitive expansions*, zero displacement except +2 E1, the unchanged nine-state T4/T2 observer and the six allowed signature bits 1,2,4,8,16,32. Require rational observer rank exactly 9 separately at H2 and H3. Count the complete positive BRC key from positive primitive steps (x,y,z,0,0,0); count every nonempty ordered signed native primitive prefix edge once, not letter prefixes.

An exhaustive literal scan of all 6^2=36 H2 and 6^3=216 H3 operation words produces respectively **6** and **38** allowed endpoint/observer words. Among 15 H2 word pairs, **exactly one** has rank 9: H2={fe,ge}. Among 703 H3 word pairs, **exactly 16** have rank 9. Hence this exactly-2+2 subfamily has **16** possible signed-native H2/H3 seeds.

Of those 16, **12 use four distinct complete BRC keys**, and **four use three distinct keys**. Every early key in all 16 seeds satisfies x+y<=4, while any endpoint-feasible horizon h has x+y>=h+1. Thus none of those early keys can occur at H4 or later. A key feasible at H4 has x<=5 and y+2z<=5 with z>=1, hence x+y<=8; a key feasible at H9 requires x+y>=10. Consequently **at least two fresh complete BRC keys** are necessary for a full H4–H9 extension. Under the exact global five-key budget, all **12 four-early-key seeds are excluded**. The remaining four three-early-key seeds are as follows:

| H2 | H3 | Complete early BRC keys | H2/H3 primitive-prefix edges |
| --- | --- | --- | ---: |
| fe,ge | feg,gef | (2,1,1),(3,0,1),(3,1,1) | 16 |
| fe,ge | feg,gfe | same three | 20 |
| fe,ge | fge,gef | same three | 20 |
| fe,ge | fge,gfe | same three | 24 |

The 16/20/20/24 costs are direct cardinalities of signed primitive-prefix unions. The 12 excluded seeds are individually retained in the JSON report. H2/H3 pairs with different numbers of selected paths, including the four H2 paths used in the existing 94-edge global construction, are outside this finite classification.

## Four explicit, fully legal five-key H2–H9 systems

Retain the EC49FAV later horizon lists, with H2=fe,ge, and substitute each of the four admissible three-key H3 pairs above. The four resulting explicit 24-path complete systems have exactly five *distinct full positive BRC keys* (2,1,1),(3,0,1),(3,1,1),(4,2,1),(6,4,1), permitted signatures and rational rank nine in every horizon. Direct complete signed-native primitive-prefix counts:

| H3 | Full H2–H9 cost | Cumulative native-prefix edges at H2..H9 |
| --- | ---: | --- |
| feg,gef | 112 | 12,16,32,38,70,82,106,112 |
| feg,gfe | 118 | 12,20,38,44,76,88,112,118 |
| fge,gef | 118 | 12,20,38,44,76,88,112,118 |
| fge,gfe | 124 | 12,24,44,50,82,94,118,124 |

The 112-edge case was previously published by EC49FAV. The other three are additional explicit legal variations with a fixed later schedule. These are constructive upper bounds for specified seeds/later words, not globally optimal values.

## Actual computation, independent validation and reproducibility

The delivered EC49FDS_seedpairs.py generates the complete literal candidate pools, all 16 two-pair seed certificates, early keys and exact prefix costs. The separate EC49FDS_independent_fraction_audit.py recomputes the **literal nine-history observer along signed native steps**, checks all 15 H2 and all 703 H3 pair rank predicates by exact Fraction row elimination against the four-clause rank classifier, and verifies all 16 selected seeds. The EC49FDS_full_witness_extension.py checks all 24 complete words and the four full witnesses, using Fraction rank and direct X6 prefix recount. These programs were executed locally in this research turn. Primary and independent outputs agreed. The sibling JSON certificate records all 16 finite seeds, and another JSON records the four full witnesses. No floating-point optimization is involved in the new result.

To reproduce from the study directory, run:

    python EC49FDS_seedpairs.py > EC49FDS_seedpairs_report.json
    python EC49FDS_independent_fraction_audit.py > EC49FDS_fraction_audit.json
    python EC49FDS_full_witness_extension.py > EC49FDS_full_witness_report.json

## Next EC49FDT

Search jointly over the four surviving 2+2 early seeds and **two late keys** using complete allowed H4–H9 words, rational-rank constraints and native signed primitive-prefix costs, and compare against the different **three-path H2, two-key early 31-edge** family established by EC49FAV. The mother target remains a complete <=93-edge H2–H9 five-key system; the existing upper bound remains 94 from EC49FAJ. EC49FDR separately excludes all 60 single critical late-key exchanges of the fixed 42-edge seed. This EC49FDS result is a narrower but distinct exact seed classification.

## Authority and evidence class

Author-side exact finite theorem and explicit constructions, with independent *method* cross-check but not independent Source Driver admission. GitHub research files on the PR #1730 draft branch preserve reproducibility. Native Source task owner and CLAIM not authenticated: current Sites upstream status returned STATUS_DATABASE_UNAVAILABLE with operation_sent=false. No Source-native Result or Review is asserted; P000 and protected worldview files were not modified.
