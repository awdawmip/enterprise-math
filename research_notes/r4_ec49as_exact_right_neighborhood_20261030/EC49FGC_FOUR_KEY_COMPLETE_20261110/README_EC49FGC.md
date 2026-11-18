# EC49FGC — Exact census of all 105 four-key minimal-r LHLHLH schedules

2026-11-10 (Asia/Shanghai). **Author-side finite computational result, not independently reviewed or admitted.** Scientific input remains frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Real native Researcher-ID: `EM-DIRECT-B6D73E`; Research-Activity-ID: `RA-E3415DCDC06A9DF8F27FD51A`.

## Statement and exact scope

Use original signed-native X6 operation codes `a=(-1,-1)`, `c=(1,2,-1,-2)`, `d=(2,1,-2,-1)`, `e=(3,1,1,-3)`, `f=(1,-1)`, `g=(2,-2)`, ordered with the frozen nine-state DFA. Fix H2's four *low* labels `1=de, 2=ed, 4=ce, 8=ec`, and H3's two high labels `16=feg, 32=gef`; all six use positive key `(3,1,1)`. Require H4/H6/H8 to realize four low labels and H5/H7/H9 to realize two high labels, i.e. mode **LHLHLH**. At H4–H9 each word uses `#a=0,#e=1`, and `#c+#d=1` for L or 0 for H. Each adjacent pair H4/H5, H6/H7, H8/H9 shares exactly one full positive integer BRC key. The 24 terminal (h,label) demands are met by arbitrary admissible orderings of these precise multisets, respecting the DFA. Four distinct full keys are used in total. Cost is the number of distinct nonempty **ordered signed-six-axis microstep prefixes** across the selected paths.

**Exact scoped computational classification:** All 105 key schedules have a certified zero-gap MIP optimum in the complete finite formulation. The **unique minimum of these optima is 108** primitive prefixes, attained for `K45=(4,2,1), K67=(5,3,1), K89=(6,4,1)` plus `K23=(3,1,1)`.

The exact full-key count equations for horizon h and K=(x,y,z) are `a=z-1,e=z,c+d=x+y-h-1,f=h+1-y-2z,g=h+1-x`. Shared keys for an L horizon h and subsequent H horizon h+1 necessarily have form `(x,h+2-x,1)`. Complete DFA-terminal feasibility yields 3 keys at H4/H5 (x=3..5), 5 at H6/H7 (x=3..7), and 7 at H8/H9 (x=3..9), hence **3×5×7=105** configurations.

### Complete 105-entry matrix

Columns are x=3,4,5,6,7,8,9 for K89. Each row is (x for K45, x for K67) followed by exact integer optimum.

| x45 | x67 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|3|3|114|112|114|120|124|128|147|
|3|4|125|112|110|112|122|126|145|
|3|5|132|120|114|112|114|128|147|
|3|6|138|126|126|120|118|120|142|
|3|7|149|137|137|137|131|129|131|
|4|3|124|122|124|130|130|136|152|
|4|4|134|112|110|112|118|122|140|
|4|5|138|120|110|**108**|110|120|138|
|4|6|140|122|118|112|110|112|134|
|4|7|152|136|130|130|124|122|124|
|5|3|131|129|131|137|137|137|149|
|5|4|142|120|118|120|126|126|138|
|5|5|147|128|114|112|114|120|132|
|5|6|145|126|122|112|110|112|125|
|5|7|147|128|124|120|114|112|114|

### Complete signed-prefix formulation and finite proof

The published `VERIFY_EC49FGC.py` computes complete ordered operation words for each of the 24 requirements, evaluates the pinned DFA, expands each candidate operation word to the literal ordered signed native-axis steps, and inserts every distinct nonempty step-prefix in a trie. Each nonempty prefix p carries binary x_p. Add x_child<=x_parent, and for every (h,label) requirement demand that the sum of its eligible terminal x's be at least one. Minimize the sum of the prefix variables.

Every legal word assignment yields precisely its primitive-prefix union as a feasible integral solution. Conversely every feasible binary solution contains at least one admissible terminal for each label, and retaining one such terminal per label cannot increase its prefix cost. Therefore the integer optimum equals the model's native prefix minimum. The 105 schedules exhaust every legal integer key within the declared mode/count family; there is no sampled-word approximation.

All 105 HiGHS integer optimizations actually returned status 0 (OPTIMAL) with MIP gap 0 and primal/dual agreement within 1e-5 (IEEE floating reporting tolerance). The minimizer contains **3,358 candidate operation words, 18,742 distinct native-prefix variables**. A separately formulated *word-indicator plus prefix-indicator* MILP, checked using `INDEPENDENT_AUDIT.py`, independently returns optimum 108 with gap zero, with 64,616 constraints; its chosen explicit path set was re-expanded and checked for DFA terminal labels, native six-axis endpoints, full keys and exactly 108 prefixes. This is a **finite computer-assisted mathematical result based on the specified MIP optimization**, not a formal Lean proof or independent Driver acceptance.

### One complete 108-edge witness

```text
H2:  1=de         2=ed          4=ce         8=ec
H3: 16=feg       32=gef
H4:  1=gefd       2=fegd        4=cefg       8=gefc
H5: 16=feggf     32=geffg
H6:  1=gefdfg     2=fegdgf      4=feggfc     8=geffgc
H7: 16=feggffg   32=geffgfg
H8:  1=geffgfgd   2=feggffgd    4=feggfcfg   8=geffgcgf
H9: 16=feggffggf 32=geffgfggf
```

## Provenance, scope boundary, next question

Frozen semantic code: `research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, immutable Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`. EC49FGB supplied the exact 64-mode census and identified this sole four-key LHLHLH profile. The 105-case raw execution report `SCAN_REPORT.json` (SHA256 `30354bcd068162699a1b3b8f5d10191b7dfe325f1e7d6678e17b2edd1a2fe26a`), exact compact matrix `EXACT_MATRIX_EC49FGC.json` (SHA256 `20392799ba82569573e137707665c46549b0c1dd676c29127f7a29e31abc0075`), independent audit, executed source and replay records are preserved in this run's downloadable evidence package. This GitHub directory includes the self-contained verifier source and exact 105-value matrix.

The **original frozen 24-label mother problem** instead has H2 and H3 **high** outputs and H7 **low** outputs, with at most five complete keys and native prefix budget at most 93. Thus this result excludes ≤93 only for the *different* specified four-key minimal-r mode family, **not** for the original mother objective. Next: admit H7-low under the original quota, allow a fifth full key or z≥2, and test an explicitly defined finite candidate class with the same exact signed-prefix objective. No formal CLAIM, canonical Source Result, independent Driver review, or Foundation promotion is asserted.
