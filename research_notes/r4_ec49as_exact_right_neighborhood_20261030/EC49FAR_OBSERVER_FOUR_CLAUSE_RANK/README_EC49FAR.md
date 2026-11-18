# EC49FAR — Four-clause normal form for rank-nine BRC observers

Date: 2026-11-04. Author-side exact theorem and finite certificates. Parent: EC49FAQ at 1755991c2822510733913494883132fe37b7f50b. Scientific input remains pinned to fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. No change to P000, ACTIVE native six-axis worldview or the current frozen task.

## Statement and scope

Use the original seven ordered signed X6 operations, nine initial-history states, five observation buckets and six allowed final signatures from EC49FAQ. Denote the final nine-history signatures by D=de, E=ed, C=ce, J=ec, F=feg, G=gef. These labels describe final observer signatures, *not necessarily the operation-word prefixes* of the paths producing them. Bucket encoding is N=0, A=1, B=2, AB=3, BA=4.

D=(2,3,2,3,3,2,4,3,4)
E=(2,2,2,3,3,2,2,3,4)
C=(1,1,4,1,3,4,4,3,4)
J=(1,1,1,1,1,4,4,3,4)
F=(0,0,2,1,3,2,2,3,4)
G=(0,1,0,1,1,2,4,3,4)

For every subset S of these six permitted signatures, let M(S) be the matrix formed by stacking the five 0/1 bucket-membership rows of each signature, with nine columns for the initial histories. Repeating a signature does not change rank. Then, **over Q and at every horizon**:

    rank M(S) = 9
    iff (E or F) and (C or F) and (D or G) and (J or G).

Equivalently, S contains one of exactly four inclusion-minimal rank-nine sets:

    {F,G}, {D,J,F}, {E,C,G}, {D,E,C,J}.

## Complete proof

Necessity is explicit: if E and F are absent, initial-history pairs (2,4) and (7,9) have identical columns under all remaining signatures. If C and F are absent, the pairs are (1,3) and (4,5). If D and G are absent, the pairs are (1,2) and (6,7). If J and G are absent, the pairs are (3,6) and (5,8). Each pair gives a rational kernel vector e_i-e_j. Two disjoint pairs give two independent vectors, hence rank <= 7. All four assertions are direct coordinate comparisons with the six displayed signatures.

Sufficiency: if F and G are present, {F,G} is contained in S. If F is present but G absent, clauses three/four force D,J, giving {D,J,F}. If G is present but F absent, clauses one/two force E,C, giving {E,C,G}. If neither is present, all four D,E,C,J are required. Four explicit 9x9 indicator minors with nonzero integral determinant certify each case:

* {D,E,C,J}, rows (D,2),(D,3),(D,4),(E,2),(E,3),(C,1),(C,3),(J,1),(J,3): determinant -1.
* {D,J,F}, rows (D,2),(D,3),(D,4),(J,1),(J,3),(F,0),(F,1),(F,2),(F,3): determinant +1.
* {E,C,G}, rows (E,2),(E,3),(E,4),(C,1),(C,3),(G,0),(G,1),(G,2),(G,3): determinant +1.
* {F,G}, rows (F,0),(F,1),(F,2),(F,3),(F,4),(G,0),(G,1),(G,2),(G,3): determinant -1.

Rank is monotone under addition of rows. Therefore all supersets of these four sets have rank nine, completing the proof. The portable code reconstructs the signatures from native primitive signed X6 steps, checks 36 initial-history pair separation sets and 64 signature subsets with exact Fraction arithmetic and checks all four determinants by fraction-free integer elimination. The exact rank histogram is rank0:1, rank3:4, rank5:14, rank7:20, rank9:25; exactly 25 of 64 subsets have full rank. For nonempty S, rank also equals the number of distinct joint nine-history observer profiles in this frozen six-signature vocabulary.

## Cost corollaries in four previously frozen fixed H2-H7 schedules

In schedules 1512,1513,2200,2203, the fixed H2-H7 native primitive prefix trie has 72 edges and maximal depth 16. Each H2 root de,ed,ce,ec has 8 native primitive steps; extending it into an H8 operation word adds at least six operations, each with at least two signed steps, so at least 12 steps beyond its H2 terminal. The four subtrees after these distinct H2 roots are disjoint. Existing H2-root extensions prepaid in the fixed trie are (de,ed,ce,ec)=(4,4,0,0) for 1512/1513, and (0,0,0,0) for 2200/2203. These facts were independently rechecked in the executed full verifier.

If H8 contains words rooted at **three distinct actual H2 operation roots**, its nine-window total has at least 72+3*12-8=100 edges (1512/1513), or 72+3*12=108 edges (2200/2203). This applies also when additional H8/H9 paths are present.

If H8 contains actual de-root and ec-root extensions, plus a non-H2-rooted word with final signature F, the nine-window cost is at least 95 (1512/1513) or 99 (2200/2203). The same holds with actual ed and ce roots plus a non-H2 word of final signature G. The two H2-rooted suffixes cost at least 24-4=20 or 24. The non-H2-rooted H8 path has at least 18 primitive steps, hence has at least two new terminal edges beyond the depth-16 earlier trie, disjoint from all H2-rooted new suffix edges. A legal H9 word sharing the complete positive BRC cache key and signed net with the H8 words has the same total primitive length and cannot equal an H8 word's primitive expansion: the first two native signed steps uniquely identify each operation, so a different operation count yields a different full path. H9 therefore contributes at least one more edge. This proves the displayed 72+20+2+1=95 / 72+24+2+1=99 bounds.

These results exclude explicit low-cost mixed-root subfamilies. A signature label alone does not identify an actual H2 source root. The unrestricted nine-window mother problem retains its earlier author-side 80 <= E*_H9 <= 94 interval.

## Validation, source and next research

Reproducible native signature/rank verifier: VERIFY_EC49FAR_PORTABLE.py (Python 3 standard library; exact rational rank, exact integral 9x9 determinants). Adjacent EXACT_REPORT_EC49FAR.json records the actual validated signatures, exact histogram, minors, pair masks and fixed-prefix corollaries. The more extensive executed local checker and report are available in the same run's working artifacts; the portable verifier was independently executed and produced PASS.

Next EC49FAS: use the **four** rank-nine alternatives, instead of a generic 64-mask rank search, to partition the mixed H2/H3-H6 candidates for H8/H9. Apply the 3-root and specific 2-root mixed exclusions, then minimize their shared native signed-prefix trie jointly with exact full BRC cache keys and observation ranks; seek <=93 or a stronger scoped bound. The exact global H9 optimum remains open. Native CLAIM/Result and independent Driver mathematical admission require current Source authority; this is author-side research evidence.