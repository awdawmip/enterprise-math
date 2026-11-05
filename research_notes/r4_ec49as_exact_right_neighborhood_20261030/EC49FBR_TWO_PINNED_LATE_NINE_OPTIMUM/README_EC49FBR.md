# EC49FBR — Full nine-window optimization conditional on two EC49FBQ late witnesses

Date: 2026-11-05. Research level: author-side exact **finite conditional** MILP results, with independently validated integer witnesses. Scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Predecessor EC49FBQ: `a97f61d4449bf19b511f8fba7cea7214558b6b81`.

## Question and finding

Preserve H2={fe,ge}, H3={feg,gef}, L=(4,2,1,0,0,0) at H4/H5, and M at H6–H9. For M=(6,4,1,0,0,0) or (7,3,2,0,0,0), **pin the exact six EC49FBQ optimal H8/H9 words**, and freely optimize all rank clauses at H4,H5,H6,H7. Minimize distinct full signed-six-axis native primitive-prefix edges.

| M | prepaid H2,H3,H8,H9 edges | accepted H4/H5/H6/H7 words | trie variables | exact additional MILP optimum | full nine-window optimum under pinned late witness |
| --- | ---: | --- | ---: | ---: | ---: |
| (6,4,1) | 54 | 48 / 24 / 240 / 1260 | 11078 | 62 | **116** |
| (7,3,2) | 58 | 48 / 24 / 120 / 2520 | 22394 | 108 | **166** |

For both, HiGHS gives optimal status, lower bound equal to objective, and MIP gap zero. The full reconstructed witnesses pass a separate JavaScript integer verifier of all eight horizons H2..H9, native endpoint (2,0,0,0,0,0), exact six-field positive BRC keys (five distinct), nine-state observer and all four clauses per horizon, and primitive-prefix union size.

**New discriminating observation:** The EC49FBQ H8/H9 local winner with M=(7,3,2) costs 58 versus M=(6,4,1)'s 54, and its separately optimized H7+late-root subset costs 88 versus 90 (EC49FBR local trie check). However **under the specified fixed six late witnesses** its complete nine-window optimum is **166**, versus **116** for M=(6,4,1). Thus the H7/H8/H9 local advantage can be reversed dramatically by H4–H6 compatibility. The earlier unrestricted L=(4,2,1), M=(6,4,1) schedule optimum was 112 (EC49FBI); pinning *this particular* EC49FBQ six-word optimum incurs four additional edges. This observation motivates optimizing early and late prefixes jointly rather than ranking keys by late-only costs.

## Model and proof of exact finite coverage

Primitive expansions: a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2), on signed native axes, with all six displacement coordinates preserved. For an h-operation word and key K=(x,y,z,0,0,0):
\[
\#a=z-1,\quad \#e=z,\quad \#c+\#d=x+y-h-1,\quad
\#f=h+1-y-2z,\quad \#g=h+1-x.
\]
Enumerate all nonnegative c/d splits, all ordered permutations of this exact multiset, and the frozen nine-state observer. Terminal signatures are E=1, J=2, C=4, D=8, F=16, G=32. Every H4–H8 rank-9 witness satisfies the four clauses (E or F), (C or F), (D or G), (J or G). H9 requires F,G. The fixed H8/H9 words already meet their clauses; variable words cover precisely the remaining 16 (H4–H7) clauses.

Form a trie whose nodes are complete ordered signed-native primitive prefixes of all accepted variable words. Let b_v in {0,1} indicate the edge to node v and impose b_child <= b_parent. For each of 16 clauses, at least one matching terminal node has b_v=1. Charge zero on prefixes already contained in the fixed H2/H3/H8/H9 paths, charge one otherwise; add the fixed cost (54 or 58). Each legal collection yields a feasible model of equal cost by taking its exact prefix union. Conversely, any feasible model provides sufficient terminal words; dropping unneeded edges cannot increase the cost. Therefore the MILP's integer optimum equals the minimum union size for precisely these pinned-word families.

The complete witnesses are in `EXACT_REPORT_EC49FBR.json`, including all operation words and their signatures. Python/HiGHS supplies the finite lower bound and upper-bound words; independent Node.js verifies the upper bound. The evidence does not include a stand-alone dual/branch-and-bound proof certificate, so the solver's zero-gap report is the stated lower-bound witness.

## Reproduce and carry forward

`python VERIFY_EC49FBR.py` prints the two MILP optima (Python3, NumPy, SciPy/HiGHS); `node CROSSCHECK_EC49FBR.js` separately checks the committed JSON witness. Both were executed locally on 2026-11-05. Code and report are in this folder; original frozen observation definitions and previously certified fixed late words are from EC49FBQ.

**Next EC49FBS:** Release the six-word H8/H9 pin for M=(7,3,2), and jointly optimize all H4–H9 clauses, or derive a smaller exact cutset bound before scaling. Compare the resulting complete solution with 112 and the mother benchmark E<=93. A small late-only H7 saving is not enough evidence to rank a complete key schedule.
