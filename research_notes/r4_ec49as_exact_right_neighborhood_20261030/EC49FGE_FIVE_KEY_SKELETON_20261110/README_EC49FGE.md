# EC49FGE — Original 24-label BRC: exact five-cache-key skeleton and a 112-edge witness

Date: 2026-11-10 (Asia/Shanghai). Researcher: EM-DIRECT-479DE1 / TASK_RESEARCH; activity RA-0518F7787B5D53F8663F5533.
Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Original model: `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, verified Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`.
Status: AUTHOR_EXACT_FINITE_DERIVATION_AND_WITNESS, awaiting independent mathematical review. No current immutable EC49AS publication or formal CLAIM as of this run.

## 1. Precise model and result

Reuse the **original** 24 terminal demands on windows H2 through H9:
`H2={16,32}; H3={16,32}; H4={1,2,4,8}; H5={16,32}; H6={1,2,4,8}; H7={1,2,4,8}; H8={1,2,4,8}; H9={16,32}`.
Each word has length h over `a,c,d,e,f,g`, follows the frozen 9-state transition table, ends at its stated signature, and has `#e=#a+1`, the original six-axis signed endpoint (+2,0,0,0,0,0). A *raw full cache key* is the triple of positive occurrences of the original signed native axes 1,2,3. Count distinct raw triples, **including keys with a zero component**. Primitive-prefix cost counts distinct nonempty ordered signed native microstep prefixes, not numerical displacements.

**Theorem (five-key skeleton, exact).** Every valid complete 24-word family needs **at least five distinct raw full keys**. If it uses *exactly five*, its key set has precisely the form

```text
{ (3,0,1), (2,1,1), (3,1,1), K45, K69 }

K45 in { (3,3,1), (4,2,1), (5,1,1), (5,1,2) }
K69 in { (5,5,1), (6,4,1), (7,3,1), (7,3,2) }.
```

All **16 combinations** are feasible at the level of exact DFA-signature and full-key coverage. The first three keys are forced by H2/H3; the fourth serves **all** H4/H5 signatures; the fifth serves **all** H6/H7/H8/H9 signatures. Therefore the joint original mother objective `#K<=5 && C_native<=93` can be decided by optimizing native prefix cost within these 16 exact classes. This is a reduction of the mother search space, not a determination of its 93-edge feasibility.

**Constructive upper bound with five raw keys.** The following 24 words attain exactly **112 different ordered signed-native microstep prefixes**, satisfy all original terminal signatures, and retain rank 9 of the fixed rational nine-history readout at every window.

| Window | Signature = operation word |
|:--|:--|
| H2 | 16=`fe`; 32=`ge` |
| H3 | 16=`feg`; 32=`gef` |
| H4 | 1=`gefd`; 2=`fegd`; 4=`fegc`; 8=`gefc` |
| H5 | 16=`feggf`; 32=`geffg` |
| H6 | 1=`gefddd`; 2=`fegddd`; 4=`fegccc`; 8=`gefccc` |
| H7 | 1=`gefddgf`; 2=`fegddgf`; 4=`fegccfg`; 8=`gefccfg` |
| H8 | 1=`geffgfgd`; 2=`feggfgfd`; 4=`feggfgfc`; 8=`geffgfgc` |
| H9 | 16=`feggfgffg`; 32=`geffgfggf` |

The five keys are `(3,0,1)`, `(2,1,1)`, `(3,1,1)`, `(4,2,1)`, `(6,4,1)`. Four are strictly positive. The cumulative native-prefix counts after H2,H3,H4,H5,H6,H7,H8,H9 are saved in the exact checker report.

## 2. Exhaustive proof of key skeleton

Let `E=#e, A=#a, B=#c+#d, F=#f, G=#g`. For legal words `E=A+1`. The full key and length obey
```text
(x,y,z)=(2E+B+F, B+G, E)
h=A+E+B+F+G
G=h-x+1, B=x+y-h-1, F=h+1-y-2z, A=z-1.
```
Every coordinate in the final line is a nonnegative integer. Thus all legal key triples can be enumerated exactly at each h. Retain the original nine-state DFA state `q`, and perform a **finite exact reachability DP** on `(q,E,A,B,F,G)`. Each operation increments its matching count, while `c` and `d` both increment B but have their **different DFA transitions**. At depth h retain only states with `E=A+1` and one of that window's required terminal signatures. This quotient is exact for key and signature support; neither approximation nor floating-point optimization is involved.

The resulting forced options are:
- H2/16 only `(3,0,1)`, H2/32 only `(2,1,1)`;
- to serve both H3/16 and H3/32 with one new key: only `(3,1,1)`;
- H4 four signatures and H5 both high signatures jointly: exactly the four `K45` triples above;
- H6/H7/H8 four low signatures and H9 both high signatures jointly: exactly the four `K69` triples above.

The key sets needed for H2, H3, H4 and H6 are pairwise disjoint. Consequently two keys for H2, at least one new for H3, one new for H4, and one new for H6 force **five** distinct raw keys. At budget five all these windows use exactly their allotted keys. No H5 signature can be supplied by the H2/H3/H6 keys; similarly H7,H8,H9 have no reachable demand on the H2/H3/H4 keys. Hence the `K45` and `K69` intersections above are necessary. For every pair of keys in these intersections the reachability DP confirms every assigned terminal signature, proving sufficiency for **key coverage**.

Independent direct enumeration of the displayed 24 words checks every DFA output, `E=A+1`, ordered native signed path, terminal displacement, key, exact rational rank and the 112-element prefix union. The project BRC-only scientific arithmetic constraint is respected: all scientific operations here are the frozen native BRC operation words and their original observer.

## 3. What this changes

The previous EC49FGD fixed-20-word background had six raw keys before completing H7; its relaxed 93-edge construction required eight. The new 112-edge witness satisfies the stronger **five-raw-key** constraint in an altered complete family, and the 16-class theorem makes the remaining 93-edge question a finite class-by-class native-prefix minimization.

Next discriminating action: compute a certified lower and upper bound for each of the 16 classes using the full literal native-prefix trie. A preliminary fractional native-prefix-tree LP for `K45=(4,2,1),K69=(6,4,1)` returned 110.0 using SciPy/HiGHS (exploratory optimizer output; exact dual certificate not yet extracted). An actual 112-edge integer witness for the same class is given above. To claim a no-go for `C_native<=93`, prove a valid **global** lower bound in each class (e.g. independently checked exact rational dual certificates, or exact integer-trie DP). The 93-edge mother question remains OPEN at this checkpoint.

## 4. Verification and provenance

Run `python VERIFY_EC49FGE.py` with Python standard library; expected line:
`EXACT_16_CLASS_PASS ... witness 112 edges keys 5`.
The generated `EXACT_REPORT_EC49FGE.json` includes exact state counts, key options and the witness. Enumeration has 2,832 distinct compressed reachable states at h9, 94 distinct keys reaching at least one required terminal across H2..H9, and precisely 16 complete five-key classes.

This is an author-side mathematical checkpoint, not a Source Result, Working Truth, Foundation promotion, an assertion of independent review, or a claim on any active owner. Scientific freeze and P000 remain unchanged.
