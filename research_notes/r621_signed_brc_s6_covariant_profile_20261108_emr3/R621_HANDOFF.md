# R621 author research handoff

2026-11-08; author-side, UNREVIEWED / NOT_ADMITTED; continuing R620 on Draft PR #1708. Frozen R462 science: `18783e01e3646c72b7aab3b16d3f565e83e6446f`, original K blob `7fa7a762f758b30c6090468ac43487daa34abad8`, theta=0.

**Mother objective:** determine exact native X6 joint state, future observer, and signed BRC branch provenance correspondence. **This increment:** a fully proved S₆-covariant formal signed-K path decoration and exact graded closed-source generating functions.

The fixed K assignment to six native signed directions breaks full S₆ axis permutation symmetry. Introduce an internal orientation π∈S₆ and assign K_(2π⁻¹(j)−1) to +e_j, K_(2π⁻¹(j)) to −e_j. Rotating both path and profile gives T_(ga)(gH)=g(T_a H). The six ordered K-pairs are distinct; every S₆-equivariant profile interface containing this frozen profile has at least 720 states, attained by π (10-bit minimum fixed-width code). π is not an additional spatial axis; native joint-field dynamics remains to be checked.

Closed B₀-source word grade: R=∑r_j, h=∑(j−1)r_j, s=3R+4h, valuation v=R+4h. C_(R,h) counts words; L_(R,h) sums their individual signed leading coefficients; both have exact factorial generating functions and insertion DP. C_(R,h)=C_(R,5R−h). At s=21: v7 C3432/L−439296, v15 C920/L−17585440. For each fixed h, signed leading coefficient sum eventually never cancels, with sign (−1)^(R+h), by degree-2h polynomial argument. All exact sources, assumptions and proofs: R621_PROOF.zh-CN.md.

Actual author-side Python exact validation: 43,200 single-step and 518,400 two-step equivariance checks, all balanced counts R≤27; see R621_VERIFY.py / R621_EVIDENCE.json. The local validation used a logically identical verifier; the published program is reconstructible from frozen formula and evidence numbers.

Native Enterprise Math identity/control observed failure: BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false. Native Researcher-ID, active owner and formal CLAIM remain unconfirmed; GitHub user awdawmip (admin) has repository write permission. A branch research note is not an authenticated Result/Review.

**Next smallest test:** locate Source-registered X6 internal joint field/update and test an actual legal nontrivial field operator against the orientation-rotation commuting square; retain exact typed counterexample if this representation fails. Preserve frozen pins and P000.
