# R726 handoff — X6 joint-relative diagonal fiber coding and signed N-BRC repair

Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Frozen scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Prior author-side R725 PR #2100; preserve its exact 20 permanent diagonal pairs and 284 future-safe net classes.

New general exact theorem for all integer L>=0: the maximal number of reachable length-L signed six-axis Cell endpoints over the SAME COMPLETE JOINT RELATIVE `can6` class is `floor(L/3)+1`. Optimal finite-length fixed index needs `ceil(log2(floor(L/3)+1))` bits. The 20 R725 L3 pairs have equal unweighted signed-axis N-BRC counts for all odd path lengths M>=3, while signed orientation character `sum_i v_i` separates them (+3 vs -3), so one bit lifts the ambiguous L3 quotient. Existing P000 common-depth repair is reused; the new result is the sharp length-L bit budget and the unsigned-vs-signed BRC separation.

Verified exact finite checks: enumerate all W_L for L=0..7; all 20 complementary triple pairs; N3=6 and N5=540 for each pair. Read the proof, Python checker and JSON evidence in this same PR. Run `python3 research_notes/R726_X6_Diagonal_BRC_20261111_verify.py`; expected `R726_DIAGONAL_BRC_FIBERS_EXACT_PASS`.

Scientific next: recover ONE genuine frozen `Cell/Link/Port` + V29 PASS/TRANSFER or V39 loop flow j event and test both complementary net-state histories. Observer quotient+unsigned BRC predict equality; typed signed orientation readout predicts difference. The native event must be defined from its actual rules, not invented by treating a coordinate step as a force/heartbeat. No formal CLAIM, semantic checkpoint, or independent review is inferred from author-side GitHub storage.

Control: original native task/continuation reads `em-r3-20261111-2223-tasks` and `em-r3-20261111-2223-cont` respectively; new session start `em-r3-20261111-2228-native-start` remains a separate identity/admission event. Keep pending receipt IDs and reconcile before any claim or Source mutation.
