# EC49FRI — Evidence, reproducibility and correction index

Date 2026-11-17. Parent EC49FRH [PR #2618](https://github.com/awdawmip/enterprise-math/pull/2618).
Frozen scientific input commit: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This Draft PR is evidence storage, not a formal Result or independent Review.

## New result
The complete frozen named physical BRC identification instance admits exactly three candidate trees as unrestricted optimum for all real (x,lambda) in [1,3]x[0,1]. The proof uses **seven unrestricted Bellman corner/phase anchors** plus a nonpositive quadratic seam coefficient from every profile multiplicity m_i>=1, followed by concavity and affine interpolation. This eliminates all 127 previously uncertified parameter bands on that rectangle, without increasing the grid. See EC49FRI_SEVEN_ANCHOR_GLOBAL_THEOREM_20261117.md for full proof and exact optimal first-action classification.

A fourth legal frozen physical tree D with aggregate counts (4,296,4,707) gives a strict counterexample to the half-line x>=1 uniform regret estimate in PR #2618. At x=4,lambda=0 unrestricted Bellman V=312/141 while three-tree min=313/141, gap 1/141. All x>3,lambda=0 have gap >=(x-3)/141, showing unbounded underestimation of the earlier global-domain approximation gap. The previous *rectangle* enclosure stays valid; only the overextended half-line conclusion is corrected.

## Frozen source fingerprints

- Original BRC raw master, SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e
- Full named profile CSV, SHA256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f
- Full self-contained conversation evidence archive: EC49FRI_SEVEN_ANCHOR_GLOBAL_RECTANGLE_AND_OUTSIDE_COUNTEREXAMPLE_20261117.tar.xz
- Archive SHA256 22ee11f9727a617e94abc2ba838af68783e8f917cf6c63f573af4fefdaa84d11
- Archive contains 36 manifest-listed files and the prior self-contained EC49FRH archive, all independently checked using SHA256 plus sizes after extraction.
- The tar.xz artifact is a conversation-delivered file, **not** a GitHub blob; only these named prose/code/index files are persisted in this Draft PR.

## Eight exact anchor certificates and hashes

| x | lambda | Exact unrestricted V | Exact physical first observations | SHA256 of native JSON in archive |
|---|---|---|---|---|
| 1 | 0 | 296/141 | 32,34 | 2c219b22e5fb04688e262cb2bcfbc927a9e58a37bc07b4fe273e798551b2a759 |
| 1 | 155/1847 | 7861/3694 | 32,34,140,142 | 33a74df6e5fd26f0bac31fc034d9f1ed5dc5dace33fa499dbdb5476245eda6f3 |
| 1 | 620/3299 | 7080/3299 | 16,23,140,142 | 9772d65abf2a24139c8a6d5373b978ccf087bf555c43099646a628649f9ab05d |
| 1 | 1 | 69/31 | 16,23,124,131 | 7e4f10c069114c5944cde4123e373e3aa08f29c4312accf75bf45ea247b00464 |
| 3 | 0 | 308/141 | 32,34,140,142 | 811f94c953a951e275f332886506120a0c18e24c2487d4e144f790715bf3211a |
| 3 | 620/3299 | 7290/3299 | 16,23,140,142 | a30833f9db64ff7acdc232e705aeeced051c1f6c603470e770c6c204ea6fb69e |
| 3 | 1 | 70/31 | 16,23,59,88 | 16b8777274433d7422f64daf3c42484f2b5df565d6516697e6a1351f08503dec |
| 4 | 0 | 312/141 | 32,34,140,142 | c97644af8761c3a7f74a253675e2e40e1d83be387633b63d24b87c2f84109f11 |

Every native certificate reports all 141 original complete named profile representatives and all 228 physical action options, enumerates all tie-first optimal decision trees and verifies their exact prices. Independent second implementation recomputed all eight unrestricted optima with 209 unique response subsets, and full named-action decision-tree replay validated all displayed candidate aggregate counts and costs. The independent calculation results and logs are stored in the archive.

## Files and executable checks

In this PR:
- EC49FRI_SEVEN_ANCHOR_GLOBAL_THEOREM_20261117.md: complete analytic proof, exact physical action classification, scope correction and next question.
- EC49FRI_SEAM_AND_COUNTEREXAMPLE_EXACT_CHECK_20261117.py: standalone Python standard-library rational check for algebraic identities and recorded finite-anchor results.
- This evidence index: unambiguous archival SHA256 refs, full eight native JSON hashes and original scientific provenance.

In the complete conversation archive (path prefix EM_FRI_WORK/):
- source/frozen_original_master.txt and source/EC49FPG_PROFILE.csv;
- endpoints/*.json (eight full native Bellman certificates) and their logs;
- code/EC49FQL_ALL_FIRST_BELLMAN.py, code/EC49FQI_NATIVE_DATA.py;
- code/EC49FRI_INDEPENDENT_8_CHECKS.py and corresponding independent JSON/check logs;
- code/EC49FRI_SEAM_THEOREM_CHECK.py and EC49FRI_EXACT_CHECK_RESULT.json;
- PARENT_EC49FRH_FULL_EVIDENCE.tar.xz, README.md and MANIFEST_SHA256.json.

The local full-audit command from archive root:
python code/EC49FRI_SEAM_THEOREM_CHECK.py

The lightweight standalone rational check (no raw inputs needed):
python research_notes/portable_direct/EC49FRI_SEAM_AND_COUNTEREXAMPLE_EXACT_CHECK_20261117.py

In both cases the continuous-domain inference depends on the full proof, not on finite sampling alone.

## Control and next scientific unit
No formal TASK publication, active-owner CLAIM, Result or independent Review is inferred. Native current Source execution identity / Activity checkpoint need authorization check before protected writes. Scientific continuation can explore x>3 price-phase regions independently without resampling [1,3]. A concrete successor is to enumerate exact Bellman first-action ties at x=4 for λ in {0, Γ(4) if meaningful, β, 1} and to identify new candidate complete trees and phase seams on [3,4].
