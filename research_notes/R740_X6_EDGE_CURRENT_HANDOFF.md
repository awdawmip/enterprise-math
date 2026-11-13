# R740 — Research3 handoff: rooted native X6 edge-current BRC census

Parent: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / `PO-X6-UPPER-STRUCTURE-20260906` / exact publication `TP2-8B7E13C5904A2D6F1142`.

Immutable scientific pin: `a72226e2430ffa4786321ac86e7f0c599d5f0389`; relevant sources are P000 V5 and frozen X6 native Cell torsor. Current behavior rules read independently. Author-side precursors: R735 PR #2132, R738 PR #2138. Concurrent complementary source-triad channel candidate: R739 PR #2140.

**Completed mathematical contribution:** 720 signed six-step closed paths on a chosen three-axis X6 slice (each of three axes has one + and one - step) generate exactly 265 distinct rooted signed primitive edge currents. Complete fiber sizes: 240 singleton currents, 24 currents of multiplicity 10, one current of multiplicity 240. The 240 no-adjacent-inverse paths have **injective** edge-current observer: 192 simple hexagons and 48 shifted-square cycles with a one-step stem. Proof, explicit witnesses and standard-library integer verifier are in this PR.

**Typed BRC:** positive-counted ordered source-labelled paths; signed edge-current and signed circulation are readout maps, not positive BRC mass or actual signed force cancellation. A general closed native-axis path satisfies `J_ij=sum_u u_i*j(u,j)`, anchor independent and S6-covariant. The true V39 current `j_V39` has not been identified with this candidate `j_X6`; that is the next scientific dependency.

**Files**:
- `research_notes/R740_X6_EDGE_CURRENT_THEOREM_20261112.md` — definitions, exact propositions, complete proofs, boundaries and native next test.
- `research_notes/R740_X6_EDGE_CURRENT_VERIFY.py` — executable exact integer enumerator; `python3 research_notes/R740_X6_EDGE_CURRENT_VERIFY.py`.
- `research_notes/R740_X6_EDGE_CURRENT_RESULTS.json` — expected exact census and fully located collision witness.
- `research_notes/R740_X6_EDGE_CURRENT_HANDOFF.md` — this independent continuation packet.

**Verifier expected:** `R740_X6_EDGE_CURRENT_BRC_EXACT_PASS`, `720` paths, `265` edge currents and `72,000` checks of S6 adjacent-transposition generators across all twenty native 3-axis selections. The author also executed a separate local first-principles integer probe, obtaining the same count distribution.

**Next discriminating experiment:** Fetch the *frozen scientific* V39 signed loop-current definition, including Cell/Link/Port attachment, spatial location, path provenance and update law. For one genuine P000 legal `TRIADIC_CLOSURE_E` event construct a typed observation map `Phi:j_V39 -> j_X6` and test exact commutation with V29 PASS and V39 update. If the interface retains only total flux or Cell divergence, use the 240-fold zero-current fiber to show exactly what must be recovered. Then find a minimal event-level BRC state or a lawful loss certificate.

**Control:** The fresh native task snapshot observed `HANDOFF_READY / NEEDS_DISPATCH`, owner `taskbook/unassigned`, no active CLAIM. New `em_session_start` returned `SESSION_ISSUANCE_QUOTA`; no new identity, authenticated CLAIM, task Result or independent Driver review was issued for R740. Research branch/PR is durable author-side science, not formal Source acceptance. P000 and task scientific pin were not modified.
