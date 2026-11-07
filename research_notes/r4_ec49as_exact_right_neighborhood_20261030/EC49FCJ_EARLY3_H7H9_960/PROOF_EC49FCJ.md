# EC49FCJ — 960 exact H4–H6/H7/H9 five-path replacement minima

Date: 2026-11-06. Classification: AUTHOR_EXACT_FINITE_COMPUTATION / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.
Frozen science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Source model: EC49FCF_EARLY1_LATE3_150/frozen_model.py, Git blob d262d4a06da862823cce2e34684a59bb081f20c2; frozen_model.py here reproduces the exact core extracted from EC49FCI's previous evidence bundle.

## The finite statement

Retain the frozen 24 observation slots (H2–H9), the 9-state observer, complete cache keys L=(4,2,1) for H4–H5 and M=(7,3,2) for H6–H9, and ordered signed six-axis primitive prefixes. The fixed original 24 words have 158 distinct nonempty signed prefixes.

Let E be the ten H4–H6 slots, J7 the four H7 slots, and J9 the two H9 slots. For every S formed by choosing 3 distinct slots in E, one in J7, and one in J9, simultaneously replace the five words by arbitrary legal words preserving each original length, cache-key multiset and terminal signature; keep the other 19 words unchanged. There are exactly C(10,3)*4*2=960 such S.

**Theorem (finite exact): for each of the 960 sets S, the minimum number of distinct nonempty native signed primitive prefixes is 158.**

## Exhaustive exact proof

For S let F be the prefix set of the 19 fixed words. Let P_i(w) be the complete prefix set of a candidate in selected slot i, and R_i(w)=P_i(w) minus F. Then the exact edge count for any candidate 5-tuple is |F| + |R_1(w_1) union ... union R_5(w_5)|. Put d=158-|F|. Strict improvement is equivalent to a five-residual union of size <d.

The finite candidate generator enumerates all multiset words with the frozen cache key; it rejects sink transitions in the nine-state automaton, and retains exactly the required terminal signatures. All complete ordered signed prefixes are assigned distinct bit positions. Thus bitwise OR computes exact set union and integer popcount its cardinality, without numerical approximation. For each slot, duplicate residual masks are removed; masks of size >=d are dropped (a monotone lower bound). Selected slots may be reordered because union is commutative.

Starting with D0={0}, for each slot j compute D_j={u OR r: u in D_(j-1), r in V_j, popcount(u OR r)<d}. Induction shows any strict-improvement 5-tuple survives through every stage. Equal residual masks have identical continuation sets, so deduplication loses no strict improvement. Consequently D5 empty proves the exact lower bound 158; the original 24-word witness provides the matching upper bound.

The executed exact checker found **D5 empty for all 960 sets**. Nine consecutive disjoint batches cover indices [0,40), [40,120), [120,240), [240,360), [360,480), [480,600), [600,720), [720,840), [840,960) in lexicographic E-triple then J7×J9 order. All completed without approximation. The sum of raw candidate Cartesian products is 6,693,829,632,000 (not actual DP join count); maximum retained intermediate state count is 534; all 960 groups reach depth five and finish with zero strict-improvement states.

## Evidence

The program VERIFY_EC49FCJ.py with frozen_model.py regenerates any batch and reports the exact canonical rows SHA256. EC49FCJ_SUMMARY.json provides aggregate counts, ranges, and SHA256 of the complete 960-row canonical JSON, b5a36a689b518adc12a935caaeba2469fb7701cfb25f0c79bf0b6374620bd8a7; reproducible gzipped bytes hash to c47939f0b3e6c276136eeacfdd50217d3ac8cbe307988a149c5d0111244bcd0b. The original complete 960-row certificate, all nine executed slice reports, source, and direct-prefix independent crosscheck are also delivered as EC49FCJ_960_evidence_bundle.zip in the conversation artifact. The independent checker used sets of literal signed prefix strings on 18 boundary/representative groups and returned minimum 158 for all 18, matching the main calculation.

Previously EC49FCH+EC49FCI covered 2,352 distinct fixed-schedule five-slot groups. The present disjoint 960 make **3,312 specifically certified five-slot groups**. This is a native signed X6 combinatorial path/observer result in a fixed BRC cache-key model, with independent mathematical admission pending.

## Next EC49FCK

Test three early slots plus H7 and H8 (C(10,3)*4*4=1,920 groups), preserving the same frozen pin and exact DP. Continue seeking an explicit 157-edge or smaller legal witness in other five/six-slot configurations or alternative legal complete-cache-key schedules; the unrestricted nine-window mother benchmark is 93 edges.
