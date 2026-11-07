# EC49FBT — Unpinned H8/H9: a 159-edge signed-X6 nine-window construction

Date: 2026-11-05. Frozen science input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent: EC49FBS at `434c6630154090dbce84df5a417c68903307f5e9`. Evidence status: **constructive author-side finite upper bound**.

## Exact question and answer

Fix H2=`{fe,ge}`, H3=`{feg,gef}`. On H4–H5 use full positive BRC cache key L=(4,2,1,0,0,0); on H6–H9 use M=(7,3,2,0,0,0). All words are ordered operations in {a,c,d,e,f,g}, expanded into the signed native six-axis primitive steps used by EC49FBS and observed by the frozen nine-state machine. All eight H2–H9 windows must satisfy the four rank-9 coverage clauses and the distinct full BRC keys must total at most five.

**Constructive result:** a legal 24-word collection has exactly **159** distinct ordered signed-native primitive-prefix edges. Consequently the unrestricted nine-window optimum over this *specified L/M schedule* satisfies `E*(L421,M732) <= 159`. In the same schedule, EC49FBR previously proved cost **166** conditional on a specific fixed six-word H8/H9 witness. Releasing those six pinned choices therefore gives an explicit **seven-edge saving** against that conditional construction. The larger nine-window mother bound previously reported as 80 <= E* <= 94 has a broader candidate family, so the new 159-edge schedule is a structural comparison, not an improvement of its 94-edge upper bound.

## Witness

The JSON file `EXACT_REPORT_EC49FBT.json` contains every operation word and observed signature. In compact form:

| Window | Required words (operation word : observed signature) |
| --- | --- |
| H2 | fe:16; ge:32 |
| H3 | feg:16; gef:32 |
| H4 | cefg:4; defg:1; fegd:2; gefc:8 |
| H5 | feggf:16; geffg:32 |
| H6 | aeeccc:8; aeeddd:2; ceceac:4; deedad:1 |
| H7 | aeeccfg:8; aeeddgf:2; ceceafg:4; deedagf:1 |
| H8 | feggfeac:4; feggfead:2; geffgaec:8; geffgaed:1 |
| H9 | feggfeafg:16; geffgaefg:32 |

H8/H9 are explicitly free choices, not the fixed late paths in EC49FBQ or EC49FBR. All 24 paths end at chart-relative signed native displacement (2,0,0,0,0,0); the observer and BRC key are validated from each complete primitive path.

The independent direct-prefix checker returned the following horizon-by-horizon cumulative primitive edge counts: **12, 16, 46, 52, 113, 125, 153, 159** for H2–H9. The incremental costs are 12, 4, 30, 6, 61, 12, 28, 6. Exactly **five distinct positive BRC keys** occur. A second independent cost identity using EC49FBS compression yields weighted operation-edge cost 170 minus seven c/f and four d/g one-step collisions, again **159**.

## Method and reproducibility

An executable Python 3 search locally enumerated all 16,152 valid H4–H9 candidate words (48, 24, 120, 2,520, 10,080, 3,360 by horizon) using the frozen operation-count equations and nine-state transition table. It ran **500 seeded multi-start incremental-prefix greedy searches**, followed by local word replacements, and retained the lowest found feasible witness. This is a feasible search; no global branch-and-bound lower-bound certificate is claimed. The explicit 24-word certificate is self-contained.

From this folder, run `node CROSSCHECK_EC49FBT.js`. The checker reconstructs the signed six-axis primitive stream independently of the greedy search, verifies every terminal signature and rank clause, all final native endpoints, full positive cache keys and five-key budget, directly counts distinct primitive prefixes, and separately applies the exact EC49FBS weighted-operation trie formula.

**Executed verification:** Node.js returned `status=PASS`, `union_edges=159`, `distinct_BRC_keys=5`, and compressed/direct cost agreement on 2026-11-05.

## Next discriminating unit

Run the EC49FBS 45,844-variable lossless compressed MILP over the full 16,152 accepted candidates for this exact L/M schedule, preserving the six-axis signed objective and H2/H3 root. Use 159 as a constructive incumbent and seek either a stronger witness or a matched exact lower bound. In parallel compare alternative L/M schedules and H2/H3 roots against the mother 93-edge target. Retain original source/exposure/claim authority; publishing this author-side research note does not create a Source Result or independent mathematical admission.

BRC reuse: exact native primitive word encoding, full positive cache key and frozen observer preserved; EC49FBS prefix-compression identity **REUSE_APPLIED**, no quotient of signed path provenance.
