# RB stage review: bounded external prior-work check

Review date: 2026-09-08 UTC (2026-09-09 Asia/Shanghai). Reviewer: Driver EM-DVR-01E1D9. This is a completed, bounded literature check for the first review of RR-34B2213BDFE75A5795CC, not a novelty certificate or an independent mathematical replay.

The fixed source snapshot is Enterprise Math `bdef46f3f0309f41c8c9837a2be55c3523328058`. The Result SHA256 is `dc6839fa2d039415d6e5e4021b5476057038512abf28c7fc6ae886ab587dfd3f`. The recovered explicit-map capsule is `research_notes/RB_CM24_ORIGIN_EXPLICIT_MAP_20260827.md`, SHA256 `d72563af774b53ba25518e5768ee1c986b82e3fb935e4f35efdef74f4ac82291`. Its historical PASS statements are claims awaiting the new source-exposed map check.

## Search actually performed

The reviewer used the available web search tool and followed primary sources at Cambridge University Press, the MPIM archive, arXiv, Numdam, an author-hosted book PDF and an author bibliography. The following twelve task-specific queries were actually issued; no Google Scholar, MathSciNet or exhaustive repository search is claimed:

1. `"Fermat" "CM" "24" "degree 6" elliptic curve`
2. `"R+2" "R^3-3R" elliptic`
3. `"35" "24" "20" "14" elliptic lambda square root 6`
4. `Fermat curve degree 24 elliptic factors Jacobian CM 24 Aoki`
5. `"Fermat" "Prym" "degree 6"`
6. `"elliptic" "4+2" "Riemann" cover`
7. `"Ramanujan" "Borwein" "sqrt(6)" elliptic singular modulus`
8. `"Simple Factors in the Jacobian of a Fermat Curve" Koblitz Rohrlich Cambridge`
9. `"Legendre" "singular modulus" "6" Villarino`
10. `"Gamma function identities and elliptic differentials on Fermat curves" Koblitz`
11. `"genus four" "degree six" elliptic subcover`
12. `"Fermat" "24" "1,5" elliptic`

Formula queries did not establish an exact match for the recovered N/D. This observation is limited to these returned and inspected candidates. Search-result snippets were used for discovery, not as proof of a mathematical claim. An initial DOI open failed; the same Koblitz--Rohrlich paper was then found and read on its publisher's PDF. The failed access is not evidence of absence.

## Candidate assessment

| Candidate and actual reading | Classification | Consequence for this review |
| --- | --- | --- |
| Koblitz and Rohrlich, *Simple Factors in the Jacobian of a Fermat Curve* (1978), introduction and initial CM-type/stabilizer setup, printed pp. 1183–1185. [Publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FA59F28D1BA4D2FB8E6830ADDAAF1A7F/S0008414X0002825Xa.pdf/simple-factors-in-the-jacobian-of-a-fermat-curve.pdf). | Partial antecedent. | Fermat period lattices, isogenies and CM-type decomposition are established prior methods. The initial numbered theorems assume degree coprime to 6, so they cannot simply be applied to degree 24. The passages read do not verify this N/D, its basepoint cancellation, degree or cycle normalization. |
| Aoki, *Simple factors of the Jacobian of a Fermat curve and the Picard number of a product of Fermat curves*, MPIM preprint 1989/82, introduction and initial theorem setup. [Archive and primary PDF](https://archive.mpim-bonn.mpg.de/id/eprint/1240/). | Partial antecedent. | This develops the Fermat simple-factor/isogeny classification beyond the earlier cases. Degree 24 occurs in the exceptional set displayed in the setup. The scanned OCR and these introductory passages do not justify asserting a general theorem settles this degree-24 map. No exact project formula or period-index match was established. |
| Bauer, Coste, Itzykson and Ruelle, *Comments on the Links Between su(3) Modular Invariants, Simple Factors in the Jacobian of Fermat Curves, and Rational Triangular Billiards* (1997), Section 3, especially scanned PDF pages 19–20 and equations (3.34)–(3.36). [Numdam primary PDF](https://numdam.org/item/RCP25_1997__48__1_0.pdf). | Partial antecedent; directly relevant degree-24 caution. | The paper explicitly treats degree 24 and distinguishes its decomposition from a product consisting entirely of elliptic curves. Thus a blanket elliptic-decomposition shortcut is unavailable. This supplies relevant CM/isogeny context; it does not certify the project's particular quotient, recovered degree-six map or its normalization. |
| Carvacho, Hidalgo and Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903v1, abstract and Sections 2.2–2.5. [Primary HTML](https://arxiv.org/html/1507.02903v1). | Adjacent method and partial homology antecedent. | The paper treats quotient curves, induced maps on Jacobians and integer cycle lattices. Its main generalized-Fermat hypotheses are not asserted for this project's curve. The reviewer infers that a differential identity and a selected period's integer cycle/index normalization require separately stated evidence; the latter is not supplied by merely citing a Jacobian factor. |

Additional candidates remain explicitly unread or insufficient: the author-hosted [Borwein and Borwein *Pi and the AGM* PDF](https://carmamaths.org/jon/Preprints/Papers/Submitted%20Papers/Elliptic%20moments/pi-agm.pdf) opened but yielded no parsed text, and no singular-modulus table was visually checked. Koblitz's [author bibliography](https://sites.math.washington.edu/~koblitz/pbl.html) identifies his 1978 Duke paper on Gamma identities and elliptic differentials on Fermat curves; its full article was not read in this check. These are follow-up leads, not verified formulas. Generic genus-four degree-six embedding hits do not by themselves address a degree-six elliptic subcover and were classified as no material match to that asserted implication.

## Review decision and retained uncertainty

An exact duplicate of the pinned N/D certificate was **not established by this bounded check**. Partial antecedents and adjacent methods were found. This is neither proof that no duplicate exists nor evidence of novelty. No external source read here proves the corrected four-checkpoint reduction or the restored map.

The external gate can be satisfied for **archive acceptance of the explicitly INCOMPLETE / RESULT_ONLY stage**, with these references and limitations retained. It grants no independent-blind label, Working Truth or theorem promotion. It does not close `RB_ENTERPRISE_THEOREM_PACKAGE_V2_INDEPENDENT_VALIDATION`.

The source-exposed successor must check the entire pinned algebraic target: special-fiber divisor/square-class placement, all common basepoints, map degree, target equation, complete frozen ODE, and unsquared pullback differential. Keep the integer homology/index underlying the claimed period ratio and the remaining 1980 parameter problems as separate OPEN gaps. A successful algebraic identity must not be reported as a period proof. No new tool family or native-coordinate identification is inferred from these classical antecedents.

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@177139a / GLOBAL_KNOWLEDGE_V1
