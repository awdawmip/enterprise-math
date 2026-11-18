# EC49FMA — global forced cache keys and exact radius-three BRC key-support census

Date: 2026-11-12. Exact frozen scientific input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Author-side finite research, independent review pending.

## Exact model

Unchanged nine-state BRC, 178,850 legal original words, 24 distinct observation labels (window, DFA signature), 94 complete raw cache keys (x,y,z), ordered signed six-axis native prefixes. Existing 84-prefix seven-key construction has seed:

K0={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}.

Define L(k) to be the set of original observer labels supported by at least one legal word whose complete raw key is k. The union of L(k) over a key set K must equal the entire 24-label set before K can possibly yield an eligible signed-native prefix solution.

## New theorem 1 — two globally forced keys

Across the full 178,850-word original catalogue, the only raw key supporting label (2,16) is (3,0,1), and the only raw key supporting label (2,32) is (2,1,1). Therefore both keys occur in *every* valid seven-key construction, not merely in a neighborhood of K0. This shrinks the globally possible distinct seven-key sets from C(94,7)=10,235,867,928 to C(92,5)=49,177,128 before prefix-cost optimization: **99.51956% excluded on label support alone**. The premise is the specified frozen nine-state BRC model, not every conceivable BRC extension.

## New theorem 2 — complete three-key swap label-support classification

Exactly C(7,3) C(87,3)=3,709,825 seven-key sets are obtained by removing three keys from K0 and inserting three other full keys. Exhaustive exact enumeration establishes:

- 38,169 sets cover all 24 label demands;
- 3,671,656 sets cannot cover all demands;
- among the 35 dropped-key triples, exactly 26 allow no coverable three-key insertion;
- precisely 9 dropped triples allow some completion.

All 25 dropped triples containing either globally forced key fail. The nine nonzero removal classes are:

| Removed raw keys | Coverable insertions |
|---|---:|
| (3,1,1), (4,2,1), (5,3,1) | 3 |
| (3,1,1), (4,2,1), (5,4,1) | 3 |
| (3,1,1), (5,3,1), (5,4,1) | 85 |
| (3,1,1), (5,3,1), (6,4,1) | 15 |
| (3,1,1), (5,4,1), (6,4,1) | 8 |
| (4,2,1), (5,3,1), (5,4,1) | 10,719 |
| (4,2,1), (5,3,1), (6,4,1) | 3,465 |
| (4,2,1), (5,4,1), (6,4,1) | 2,468 |
| (5,3,1), (5,4,1), (6,4,1) | 21,403 |

The exceptional 26th zero class retains both globally mandatory keys but removes (3,1,1),(4,2,1),(6,4,1). Missing h=3 label (3,16) forces the new key (4,0,1), while label (3,32) forces distinct new key (2,2,1). After these two insertions, labels (5,16) and (8,1) remain missing. No available third outside key simultaneously supports those two labels. Therefore every three-key insertion for that class fails. This gives a short independent structural obstruction for the otherwise surprising zero class.

## Finite proof and execution evidence

Assign one bit to each of the 24 (h,signature) labels. Enumerate the unchanged original legal word generator and OR bits into the support masks L(k). For each of C(7,3)=35 deleted-key triples, compute the labels not supported by the four retained keys and test each C(87,3)=105,995 distinct inserted-key triples. One Boolean mask union per candidate, without floating point, establishes the exhaustive counts.

Independently, for each dropped-key class, group outside keys by intersection of their label mask with the missing-label mask M. For each sorted triple of mask classes (a,b,c) with a OR b OR c=M, count its distinct key selections using products of frequencies, C(f,2)f for one repeated class, or C(f,3) for a triple repeated class. The separately implemented grouped calculation matches the direct enumeration for all 35 classes. As a regression, the earlier two-key census is recovered: 78,561 total, 6,315 coverable, 13 zero deletion-pair classes.

Two actual local validation runs produced EC49FMA_TRIPLE_KEY_SUPPORT_TWO_METHODS_PASS and EC49FMA_FULL_TRIPLE_SUPPORT_EXACT_PASS. The associated executable script VERIFY_EC49FMA.py uses the already published frozen EC49FGW original-word generator and emits the 35-row report; EXACT_REPORT_EC49FMA.json stores the removal-class counts. A standalone generator and full mask-source evidence also exist in the local research reproduction package.

## Next research unit and admission state

This is a complete finite **key-level demand-support** theorem. The 38,169 coverable three-key swaps have not been assigned exact ordered signed native-prefix costs here; the unchanged 84-prefix lawful construction continues to establish C_min(7)<=84. The next discriminating unit is to run the existing exact signed-native trie DP on those 38,169 candidates, prioritize the nine nonzero deletion classes and search for a lawfully verified <=83-prefix witness. Maintain the existing radius-0/1/2 optimum and the frozen model pin.

Publication is author-side evidence only. Native CLAIM/Result and independent Driver review are not asserted; P000 and ACTIVE worldview remain unchanged.