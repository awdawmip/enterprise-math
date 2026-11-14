# EC49FGC addendum — 104-edge fixed-background H7-low exact extension of the original 24-label target

Date 2026-11-10; frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: **author-side exact finite computational result; no formal CLAIM or independent Driver acceptance**.

## Exact question

Unlike the separate four-key LHLHLH auxiliary model, this addendum restores the **actual frozen mother observation-signature pattern**:
- H2: high 16=`fe`, high 32=`ge`.
- H3: high 16=`feg`, high 32=`gef`.
- H4: low 1=`gefd`, 2=`fegd`, 4=`cefg`, 8=`gefc`.
- H5: high 16=`feggf`, 32=`geffg`.
- H6: low 1=`gefdfg`, 2=`fegdgf`, 4=`feggfc`, 8=`geffgc`.
- H8: low 1=`geffgfgd`, 2=`feggffgd`, 4=`feggfcfg`, 8=`geffgcgf`.
- H9: high 16=`feggffggf`, 32=`geffgfggf`.

Hold **these 20 operation words fixed**, with their *literal ordered signed six-axis* primitive prefix set B. Direct expansion yields **|B|=89**. At H7 require all four low signatures `1,2,4,8` and fix their one shared positive full BRC key to `K7=(6,4,1)`. All operation words with horizon 7, `#a=0,#e=1,#c+#d=2,#f=2,#g=2` and the required terminal nine-state-DFA signature are admitted, across every ordering.

## New precise finite result

The complete H7 word pools contain **360,270,360,270** words for signatures 1,2,4,8, respectively, or **1,260** total. Over *every* choice of four H7 paths, the minimum number of additional nonempty literal signed-native prefixes outside B is **15**:

`C_min(B + H7-low | K7=(6,4,1)) = |B|+15 = 104 native prefix edges.`

An explicit achieving H7 assignment is `1=gefdfgd, 2=fegdgfd, 4=feggfcc, 8=geffgcc`. The 24-path signed-native expansion has exactly 104 distinct nonempty prefixes, preserves every terminal signature and the endpoint. Each of these H7 paths has the complete positive BRC key `(6,4,1)`.

**Two independent exact optimizations agree.** A full literal native-prefix 16-mask trie subset-convolution DP (the checker `h7_original_scan.py` preserved in the author's local evidence) returns 15 fresh edges. Independently, the published `H7_FIXED_BACKGROUND_MILP.py` uses four demand constraints and 1,260 word binaries plus 9,916 new-prefix binaries, with `y_word<=x_prefix` for every prefix not already in B. There are 21,964 total constraints. SciPy/HiGHS returned `OPTIMAL, primal=15, dual=15, MIP gap=0`; its selected 24-path family recomputed to 104 literal signed-X6 prefixes. The integer program is exact for this explicitly bounded input because every feasible word must activate all its new prefixes, and every demand must select at least one word. The baseline and candidate languages have complete enumeration over the given operation counts.

This addendum is closer to the frozen 24-label mother template than the separate LHLHLH four-key classification. Its fixed-word and fixed-K7 assumptions are stronger than the mother constraints. Accordingly 104 excludes ≤93 for **this exact fixed-background subfamily**, not for all legal original 24-label assignments. The parent target remains ≤5 full keys and ≤93 primitive prefixes; the H2 high seed's zero-key semantics must be interpreted from the frozen source, not silently folded into this addendum's key counts.

Next: let the 20 fixed background paths and H7 full key vary jointly across the exact mother key budget; seek a ≤93 witness or a complete finite candidate-class lower-bound certificate. No P000 or ACTIVE-worldview modifications.
