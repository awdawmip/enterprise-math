# EC49FDD — next exact nine-slot study

Scientific input pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Use existing source blobs `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859` (frozen_model.py), `4c74b4ee243c939494d9f7eedb3f61255e16f91f` (trie builder), `dfe7a3b596f615a26b88d48beee931459d2357eb` (exact C++ DP). Nine-state observer, 24 signed native-step slots and `L=(4,2,1),M=(7,3,2)` remain fixed.

Verified author frontier: all 768 A/B seven-base plus-one-H6-or-H7 **eight-slot** exact full-language minima equal 158 (earlier 228 + newly executed complementary 540). Additionally 18 full-language **nine-slot** cases for r=2,s=t=1 with both a distinct H6 and distinct H7 extra have minimum 158. The 540-row and 18-row exact calculation certificates and replay procedures are in README_EC49FDB_FDC.md.

Next discriminating unit: inspect nine-slot A/B at r=4,s=2,t=4, extras 6:1 and 7:2 (and extend to further signature combinations); independently enumerate the full legal languages with the labelled signed-prefix trie recurrence, preserve exact counts, and save explicit signed primitive words if any 157-or-lower witness is found. If no witness, extend to two extras within H6 or H7, a tenth varying slot, or an admissible alternate BRC multiset cache-key arrangement. Preserve P000 and complete future-relevant branch/prefix observer data.

Native owner/CLAIM and Driver acceptance remain pending separate authenticated service operation.