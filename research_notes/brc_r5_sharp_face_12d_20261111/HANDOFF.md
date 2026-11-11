# R5 exact sharp common-face handoff — 2026-11-11

## Current question
Given the immutable PR #2017 exact 30-arc physical witness \`E0\` and exact 21-observer \`C\`, which affine face contains all length-four K2,3 atom edges, and what is the exact face dimension?

## Verified author-side increment
- Previous PR #2049: complete 14,832 signed candidate circuits, exactly 49 physically realized sharp edges with 58 endpoints.
- This run: source 3 has target support **exactly \`(2,3,4,5)\` on all 49 edges and all endpoints**. The common exposed face is \`E[(0,3)]=E[(1,3)]=E[(6,3)]=0\`, of dimension **12** (rank restricted matrix 15, 27 available columns).
- Exact existence witness: average the 49 rational edge midpoints; this mean has 26 positive arcs, missing \`(0,3),(1,3),(6,1),(6,3)\`. Add the rational signed K2,3 repair at source ports \`(1,2)\`, target labels \`(4,5,6)\`, source1 weights \`(8,-13,5)\` and opposite source2 weights, multiplied by \`227917436204790631/867449622094929995520\`. Result is positive in all 27 face coordinates and exactly zero on the three excluded arcs. Every observer equality remains exact.
- For comparison, **exactly 7 of 35** four-target masks are feasible for source 3 when **only** source3 mass, first moment and target capacities are retained. The sharp edges within the entire joint fiber select precisely one of these seven. The other six remain a question for full-fiber extensions.

## Reproduction
\`\`\`bash
python3 research_notes/brc_r5_sharp_face_12d_20261111/VERIFY_SHARP_FACE.py
\`\`\`

Inputs are embedded exact decimal rational strings from frozen PR #2017 witness and original frozen ratio numerators. Python standard library Fraction + SymPy for rank only. Exact 15,120-configuration and 35-mask finite enumeration, all reported comparisons rational, no random/floating-point LP. Expected final marker \`PASS_R5_EXACT_SHARP_FACE_12_DIM\`. Full stdout \`EXACT_OUTPUT.txt\`. Original local program and stdout were executed twice and second stdout matched first; repository's saved verifier uses those same input equations and evidence. Independent mathematical review/formal Source Result remains open.

## Authority and provenance
GLOBAL frozen science pin \`a01383f825ef9d43b4b754254303298c64041568\`, EM frozen science pin \`86149263e38c22292c9def1e0f69092efa1be77e\`. Current source normative docs were loaded separately. Real native identity \`EM-DIRECT-DD0221 / TASK_RESEARCH\` with activity \`RA-BD2749C34A6F95132C288680\`; persisted original session+activity Source \`19575ab03ffe1d7fb1ea0ceba2d224a3b6e56ab8\`. This author artifact changes no P000, TASK, owner, CLAIM, Review or Foundation state.

## Next smallest uncompleted unit
1. At the same frozen physical fiber, determine whether each of the six remaining row-only four-target supports occurs in **any complete admissible** transfer. Work via exact finite affine feasibility preserving all source/target joint constraints.
2. Analyze full 12-dimensional face G: all vertex support sizes, adjacency paths connecting nine sharp-only trees by non-sharp edges; compare PR #2026's radius-4 1775 vertex frontier.
3. If a useful new lemma appears, preserve executable rational certificates and register as author-side progress pending formal review.