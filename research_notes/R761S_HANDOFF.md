# R761S portable research handoff — 2026-11-13

## Parent and immutable input

Parent RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable task publication TP2-8B7E13C5904A2D6F1142; frozen science Source awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Protected P000 and ACTIVE worldview unchanged. Author-side continuation of R761 Draft PR #2241.

## Completed mathematical work (reuse, do not recompute without need)

R761S_SPARSE_TRIAD_PORT_GENERATORS_20261113.md proves connected 3-uniform support incidence yields the full alternating group on that component. With six labelled candidate port slots, the minimum number of support triples producing A6 is three. Of 1140 unordered triples of supports, 60 generate A4, 600 A5, 480 A6. The A6 triples split into three S6 orbits with sizes 180, 180, 120; Cayley diameters under each generator and inverse are 7, 7, 5. Exactly 120 three-support alphabets achieve diameter five. Thus a five-event worst-case bound is available in the stipulated legal alphabet, using just six signed/oriented event types. The full-alphabet three-event bound of R761 remains a separate tradeoff.

The BRC final-state carrier g in A6 needs exactly 360 states (nine fixed-width bits) for the declared observer of six provenance-distinct final port labels and future compositions. Retain complete ordered event provenance for broader observers.

## Artifacts and evidence

- Proof: research_notes/R761S_SPARSE_TRIAD_PORT_GENERATORS_20261113.md.
- Runnable Python 3 stdlib exact checker: research_notes/R761S_VERIFY.py.
- Output evidence: research_notes/R761S_EVIDENCE.json.
- Local verification: actual execution on 2026-11-13 Asia/Shanghai, success (all asserts passed). Each of 1140 generator triples is checked by exact BFS, and all 480 A6 cases are independently checked against orbit-member depth histograms. No probabilistic or approximate inference.
- Remote state: committed to author research branch and read back by GitHub connector. Branch/PR is durable author-side material, not Source canonical-main formal Result or independent mathematical acceptance.

## Next uncompleted scientific question

Obtain actual native Cell/Link/Port triadic event admission and the V29/V39 transition/readout predicates from the frozen source. Test each of the six orientations of the three supports 012,034,135 with source-labelled equal-q tokens, including signed port conditions, time ordering, third-force visibility, and allowed native rotations. If the six event types pass, formulate a provenance-preserving simulation of the native event monoid into the R761S candidate. If they do not, record the first concrete rejected predicate, choose the genuinely allowed alphabet, and compute that alphabet's generated subgroup and observer sufficiency.

Current control owner should be read from a completed native continuation packet before a new CLAIM; unresolved QUEUED/REVALIDATING requests grant no task ownership. An author-side GitHub branch or Activity record is not a CLAIM. Formal Result and independent Driver review remain separate work.
