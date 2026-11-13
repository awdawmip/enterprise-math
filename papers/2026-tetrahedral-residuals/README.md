# Publication manuscripts

Author: **YUAN X**, Enterprise Math. Revised November 13, 2026.

| Manuscript | Contents |
|---|---|
| [Tetrahedral Endpoint-Sum Residuals and a Non-split Affine 2-Torsion Extension](YUAN_X_Tetrahedral_Endpoint_Sum_Submission.tex) | Integral normal forms, the mod-two action of the tetrahedral group, its non-split torsion line, and the affine support description of the six edges. |
| [Pell Units and Sharp Positive Tails in Ramanujan's N=58 Series](YUAN_X_Pell_Units_and_Sharp_Tails.tex) | The least uniform ratio within omitted tails of a positive hypergeometric family and the least first-omitted-term multiplier. Ramanujan's class invariant gives the paired Pell equations and the specialization at 99. |

The two manuscripts have independent hypotheses. The [September 3 combined manuscript](https://github.com/awdawmip/enterprise-math/blob/2d00986d8ec4a094c9e83b436a8efe0c5a39b76c/papers/2026-tetrahedral-residuals/YUAN_X_Tetrahedral_Residuals_Double_Pell_Full.tex) preserves the FCC realization, metric calculations, finite generating lifts and majorization material from the original draft.

## Verification

| Scope | Checked source and successful Lean build |
|---|---|
| Integral residual classification, tetrahedral symmetry and mod-two non-splitting | [Original stack at `95a9cd418f6a`](https://github.com/awdawmip/enterprise-math/actions/runs/33657478048). |
| Linear equivalence with affine functions, arbitrary vertex relabelling, six edge supports and complements | [Affine module at `06d221facd0d`](https://github.com/awdawmip/enterprise-math/blob/06d221facd0d0323dc1b08e13422b500a0eaa8cd/EnterpriseMath/PrecisionPi/PaperIIAffineFunctions.lean) · [strict build](https://github.com/awdawmip/enterprise-math/actions/runs/43376204148/job/131723174697). |
| Paired Pell identities, arithmetic at 99 and original finite geometric bound | [Original arithmetic stack at `ca2b30c7ef45`](https://github.com/awdawmip/enterprise-math/actions/runs/33659295408). |
| Positive sequences with the stated hypergeometric ratio law, sharp ratios, strict infinite upper tail bound, normalized remainder limit and least multiplier, with identification of the actual factorial summands at N=58 | [Sharp-tail module at `798b86a30418`](https://github.com/awdawmip/enterprise-math/blob/798b86a30418df4ae24bd678e01df3ed0a62b0d9/EnterpriseMath/Precision/SharpPositiveTail.lean) · [strict build](https://github.com/awdawmip/enterprise-math/actions/runs/43376958085). |

Ramanujan's modular evaluation of the complete series and the CM evaluation of the class invariant enter the arithmetic manuscript as classical inputs. The subsequent [unit-signature research note](https://github.com/awdawmip/enterprise-math/blob/efdf00267767145c0c186294576de1a05f7137ef/research_notes/tetrahedral_pell_signatures_20261113/NOTE.md) gives a separate arithmetic realization of the tetrahedral mod-two residual on the four real embeddings of the biquadratic Pell field.

Both manuscripts compile separately with pdfLaTeX. Each source contains its own bibliography and author disclosure.
