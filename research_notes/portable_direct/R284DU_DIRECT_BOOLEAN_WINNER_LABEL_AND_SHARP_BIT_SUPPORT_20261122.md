# R284DU — 八个源位的直接布尔胜出标签判定及坐标支撑锐性

Date: 2026-11-22 (Asia/Shanghai)
Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED
Scope: original frozen R284CO 64 labeled arcs; only the R284DQ/R284DT 512-state minimum-gap witness subfamily. Not a general 65,536-state or native-X6 law.

## Input encoding

The eight lower skeletons are lower=1056+512X+256Y+16Z with X,Y,Z in {0,1}; r,w toggles are R,W in {0,1}. Let the original 4-bit upper index be upper=8U2+4U1+2U0+B, where U2,U1,U0,B are bits. The 512 witness states vary over all 2^9 values (X,Y,Z,U2,U1,U0,W,R,B), with B the upper-bit-0 flip pairing. Their original integer source indices use upper<<12 plus lower and W*64+R. In this frozen family the farthest arc label is **independent of B**; its other eight inputs are listed in that order.

## Theorem: exact 4-branch Boolean label circuit

For input bits X,Y,Z,U2,U1,U0,W,R define the classifier as follows. All logical operations are Boolean AND/OR, with no numerical determinant, modular arithmetic or arc search in this classifier.

1. If X=1 and W=1, the unique winning label is 55.
2. If X=1 and W=0, the label is 32 exactly when U2 AND [R OR (U1 AND (Y OR (U0 AND Z)))] is true; otherwise 56.
3. If X=0 and W=1, the label is 21 exactly when U2 OR [R AND (U1 OR Y OR (U0 AND Z))] is true; otherwise 45.
4. If X=0 and W=0, the label is 44 exactly when [U2 AND (R OR U0 OR U1 OR Y OR Z)] OR [R AND ((U1 AND Y) OR (U0 AND U1 AND Z) OR (U0 AND Y AND Z))] is true; otherwise 63.

**Claim:** For every one of the 512 frozen witness states this circuit gives the unique winning arc label of the original 64-arc distance function. The 256 representative inputs yield label counts {21:45,32:21,44:37,45:19,55:64,56:43,63:27}, and each representative's B-flipped partner retains its label.

**Finite proof:** With the source index mapping above, the 256 eight-bit tuples exhaust the entire quotient of the 512-state witness family by the B flip. For each tuple, R284DT provides an exact certified affine window containing its integer determinant residue and the B-flipped partner residue; its interval theorem certifies unique label against all 64 arcs on each entire integer window. The checker enumerates the 256 bit tuples, computes these exact residues using the pinned R284CO determinant, checks the R284DT labels and exact R284DO q3 partner increment, and evaluates the proposed Boolean circuit. All 256 representative labels and all 256 partner labels agree. Its lexicographically ordered truth-table SHA-256 (eight input bytes followed by one output-label byte each) is d173172ff35dbd6bcfb30d5841a3f4700433f4361731aafb31d1e1e71447c527. This proves the finite input-domain claim with exact integer evidence and exhaustive 256-case Boolean coverage.

## Sharp support in the declared source coordinates

For every one of the eight input positions, there are two valid representative states differing at *that one position only* whose winning labels differ. The exact numbers of sensitive undirected edges (out of 128 per coordinate) are:
X:128, Y:11, Z:5, U2:65, U1:13, U0:5, W:128, R:31.
The exact certificate includes one smallest lexicographic witness pair per coordinate. Hence any deterministic classifier on this same source-bit representation that simply drops one of these eight coordinates fails to recover every label. B, in contrast, may be omitted entirely on this 512-state domain.

This is **coordinate-support minimality** only. It is not a lower bound of eight bits on arbitrary encoded labels: seven possible labels fit in three information bits.

## Algorithmic impact and limitations

The frozen minimum-gap witness **winning arc labels** can now be produced with at most a small fixed Boolean decision formula, without first computing the 34-bit integer Port residue, 64 arcs, the 193 event slabs, or performing any circular-arc distance comparisons. Recovering the numerical farthest distance D and verifying gaps 59/60 still uses the original integer determinant or its justified equivalent (R284DT's seven affine windows); the new result eliminates residue evaluation **only for the label subproblem**.

No claim about running time on other inputs, minimal Boolean gate count, native six-dimensional dynamics or physical interpretation is made. Source pin and full science are unchanged: R284CO@acba2d8667903434aaa2a10720f43637fcc2421b, blob b46e0f682b58e47c27094b4bea6fa4e55119a3ee, frozen ordered-word SHA-256 b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4.

Reproducer: research_notes/portable_direct/R284DU_boolean_winner_classifier_checker.py.
Certificate: research_notes/portable_direct/R284DU_boolean_winner_classifier_certificate.json.
Local exact Python execution passed. The author research remains NOT_REVIEWED and no native CLAIM/Result or new Researcher authority is implied by this GitHub publication.

Next scientific target: direct Boolean/affine formulas for *numeric* four-read distances and minimum-gap states using the same eight source bits plus the necessary integer coefficient representation, with complete operation/precision and representation cost accounted for.
