# R751 — Signed-support orbit obstruction for R747/R748 replacement versus native V1R

Date: 2026-11-12. Parent RS-X6-TRIADIC-CLOSURE-DYNAMICS. Existing run RUN-aea48b2b684b1204bf7fd828, resumed generation 2, prior checkpoint revision 3. Original Researcher EM-X6-BD7DE5 and CLAIM MCP-aa543cb564e2a231d3fe6017. Frozen P000 science @a72226e2430ffa4786321ac86e7f0c599d5f0389.
Status: author-side exact theorem and exhaustive finite validation; no native coupled event authorization asserted.

## Exact premises
1. V1R (research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md, current main) defines signed frame F=(ordered three DISTINCT axis labels, ordered signs) and R_can(F)=(cyclic shift axes, negate token signs), with alternating SHELL/CLOSURE mode and R_can once per two steps.
2. R747 (research_notes/portable_direct/2026-11-12_R747_C1_framed_port_connection_exact_S3_holonomy.md at ed44c4e1f6c7bd2adc545fa60047619f71a59992) defines a candidate signed one-port replacement with two identical surviving ports and the new port on an axis NOT already in the source.
3. R748 adaptive selection is prior author-side evidence; no unverified assertion about its full branch legality is used here. The theorem applies to every R748 branch satisfying premise 2.
4. V29 PASS updates only count M; V39 (j,h) is an operation-safe quotient for its declared loop future language, not an event-admission predicate.
5. R750 corrected R749 theorem 2: distinct V1R modes with equal V29 counts are legal, but no opposite TRIADIC_CLOSURE_E truth assignment has been established.

## Theorem: exact orbit-disjointness
Let supp(F) be the unordered three-element set of unsigned native axes in F. Every V1R internal update preserves supp(F), since R_can only cyclically permutes these three axes and reverses token signs. Therefore every finite V1R update word preserves supp(F). By contrast every R747 candidate replacement of one signed port by a signed port on an unused axis changes supp(F). Thus NO R747 replacement edge can be realized by any finite sequence of the declared V1R internal updates alone.

Proof: support invariance under each V1R generator, induction on word length; a one-port replacement removes one support element and inserts a different one. The two support sets differ. This is a sharp, unconditional theorem in the cited declared V1R and R747 candidate grammars, not a claim that all future coupled events are impossible.

## Consequences for native coupled permission
- Even though V1R supplies a genuine internal C12 update, it cannot serve as a hidden realization of the R747/R748 support-changing one-port selector.
- V29 PASS alone also fixes the frame. Any support-changing triadic update must use a further explicitly declared event law (or a separately authorized coupled transition) whose target support differs.
- If a proposed R748 branch keeps the SAME unsigned support but changes signs, this particular obstruction does not apply; it must be tested against the exact signed V1R orbit and closure/Link permissions separately.
- For the R747 grammar, the obstruction is stronger than the R749 count-only argument: it rules out even arbitrarily many V1R internal steps, without relying on any closure true/false labels.

## Exhaustive check
The accompanying Python program enumerates all 960 ordered signed frames. Each frame has 3 choices of removed slot, 3 unused axes, 2 signs: 18 distinct candidate replacements. For all 960*18=17,280 replacements, none belongs to the six-frame R_can orbit of its source. Output:
{"status":"PASS","frames":960,"candidate_one_axis_replacements":17280,"V1R_reachable_replacements":0,"native_coupled_permission_proved":false}.
This exhaustive check independently confirms the general support proof. It is not a finite search over unspecified future native event laws.

## Exact unresolved research
The real missing object is a source-backed support-changing Cell/Link/Port event guard with (i) declared source/target signed port incidence, (ii) triadic closure preservation certificate, (iii) BRC source/provenance transfer, (iv) event dependency order, and (v) compatibility with V29 count updates. R748 adaptive branch choice cannot be promoted to a native event without such a guard. Absence of this guard in the inspected V1R/V29/V39 sources does not prove nonexistence elsewhere or mathematical impossibility.

Next useful independent unit: compare R748's exact saved branch definitions to the support-invariant versus support-changing partition; check whether any branch is already a V1R orbit step. If all change support, all require an additional law; if some retain support, test their exact signed orbit.
