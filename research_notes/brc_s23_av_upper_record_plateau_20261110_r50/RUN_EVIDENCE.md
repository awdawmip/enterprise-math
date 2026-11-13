# R50 exact execution record (2026-11-10)

Source: frozen scientific pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34; R49 predecessor #2007@5737faa62202b633dcf7e1183d0a8480fd88222f. Local Python stdlib exact integer/rational tests, no floating point.

VERIFY_R50.py produced PASS on six families: frozen_s23_128_225 (K352, s*=225, seven quotient blocks, 13 mediants), sqrt2_minus_1_5_8 (K12, s*=12, three quotient blocks, five mediants), sqrt2_minus_1_6_12 (K17,s*=12), sqrt2_minus_1_5_1_uncovered (K5,s*=2, explicitly empty labels), sqrt2_minus_1_3_8 (K10,s*=7), sqrt2_minus_1_8_12 (K19,s*=12). Both theta interval endpoints had identical bounded-Farey state and maximal terminal plateau certificates; exhaustive one-step mediants and brute-force min over denominators 1..K agreed.

VERIFY_R50_S23_COMPILER.py produced:
PASS_R50_AUTOMATIC_TWO_STATES {61: 2, 225: 76} source_inspections_2_endpoints 778 star 225
PASS_R50_298_RUNS 298 events 9697 sha256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6

The finite JSON evidence and the fully executed source files are included in R50_RESEARCH_BUNDLE.zip. Publication is author-side storage pending independent mathematics review.