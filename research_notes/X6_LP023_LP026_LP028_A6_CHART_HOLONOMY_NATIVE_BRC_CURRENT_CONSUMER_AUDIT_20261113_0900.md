# X6 LP023/026/028 — chart-loop holonomy preserves signed BRC but is not native Cell return

Date: 2026-11-13 (Asia/Hong_Kong on-hour research). Parent Task `RS-X6-LEGACY-PLANE-RECONCILIATION`; canonical publication `TP2-B4A441B23DA3159232C2`. Existing author-side lane: `EM-X6-FB6990`, session `MCP-082892eb480e45dea6d4b9fcc0491034`. Source exposure: NONBLIND; author-side exact derivation and standalone execution only; UNREVIEWED / NOT_ADMITTED. No independent mathematical review, Result freeze or current native execution authorization is asserted.

## Frozen scientific scope and exact current executable consumer

- Frozen centered signed X6/P000 V5: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Current behavior rules read separately.
- Actual current executable consumer: `experiments/x6_chart_a6_unification_v3_20260906/check_chart_a6_unification.py`, Git blob `480a4522705851ac22678ba670d55293014608f5` at Source main observed 2026-11-13, relevant `even_lift`, `loop`, triangle classification and `A6` group closure. This source already established 20 charts, 90 undirected chart edges, 45 even lifts, 120 chart triangles, and 60 identity / 60 double-transposition holonomies. **Consume those existing facts**; do not report their original discovery anew.
- New author-side proof and discriminating BRC-extension checker: `research_checks/X6_LP28_CHART_A6_BRC_TYPED_HOLONOMY_20261113_0900.py`, immutable commit `681de5cdbd85deafb05a4afd3548666d5e521064`, Git blob `6a6a4580a6403d1664a9339d6f44e16794e6d88e`. Its source body was confirmed exactly equal to the locally executed checker, with separate complete remote GitHub readback.

## Precise proposition — native length/BRC invariant under selected even chart holonomy

Let `X6` use one chosen Cell anchor and signed displacement `z in Z^6`. Let `S,T` be neighboring 3-of-6 axis charts, whose two axes overlap. The current `even_lift(S,T)` permutes the leaving axis `a` with entering axis `b` and swaps the two complementary axes `c,d`; it is `(a b)(c d)` in `A6`, not a translation of the native Cell anchor.

For every chart loop `S -> T -> U -> S` from the 120 pairwise-adjacent chart triples, let `H` be the ordered product of the three actual even lifts. Then for **every** signed native displacement `z in Z^6`, the coordinate relabelling `w=H.z` obeys

```text
G(w) = G(z),          G(z) = sum_i z_i^2,
T(w) = T(z),          T(z) = sum_i |z_i|,
M(w) = M(z),          M(z) = T(z)! / product_i |z_i|!.
```

The last formula counts ordered shortest words over the 12 **unweighted, unconstrained** signed native primitive letters, preserving letters and their labels under the `H` permutation. It does not assert invariance of arbitrary weighted/channel/restricted-path programs or an admitted physical rotation law. The bijection maps each `+e_i` or `-e_i` to `+e_{H(i)}` or `-e_{H(i)}` and extends letterwise to shortest words. All three invariants therefore follow algebraically for all signed integers, with no finite-experiment generalization needed.

For a concrete curved loop, choose `S=(0,1,2)`, `T=(0,1,3)`, `U=(0,2,3)`. The exact current-even-lift composition yields `H=(1 2)(4 5)` (zero-based axes). A native signed displacement `z=(0,3,4,0,0,0)` maps to `w=(0,4,3,0,0,0)`; these are *different* six-coordinate displacements, yet both have `G=25`, `T=7` and `M=35`. The chart name returns after three edges while the **chart's axis-label transport** need not be the identity; a chart loop alone is not a native Cell-return or physical endpoint-identity certificate.

For a curved double transposition `H`, a vector in `[-2,2]^6` is unchanged iff the two swapped pairs each have equal entries; there are `5^4=625` fixed and `15,625-625=15,000` changed vectors. Thus the 60 curved loops yield `37,500` fixed and `900,000` changed, while the 60 flat loops fix every vector. This is a complete finite-family count on that declared cube, not a count of all native states.

## Executed precise certificate

The separately authored checker enumerated every `z in [-2,2]^6` (15,625 vectors) for all 120 chart triangles and compared native `G,T,M` with exact integer arithmetic: **1,875,000 triplet comparisons PASS**; **60 flat**, **60 curved**; **900,000 changed coordinates** and **37,500 fixed coordinates under curved holonomy**. Actual local execution output begins `PASS_X6_LP28_CHART_A6_BRC_TYPED_HOLONOMY` and includes these exact totals, with no floating point arithmetic, `sorry`, `admit`, or custom target axioms. This is a standalone recomputation transcribing the actual GitHub consumer's `even_lift` and composing it with signed native free-shortest BRC; it is **not** a full original project/source-import regression.

## Seven additional exact current consumer source classifications

These seven **complete current Source program bodies** were individually read on 2026-11-13, separate from the nine earlier audited current executables, and their Git blobs were verified:

| Exact executable file (under `experiments/`) | Git blob | New typed consumer classification |
|---|---|---|
| `x6_centered_three_axis_slice_v19_20260905/check_centered_slice_crossfile.py` | `25f520df1e29bdd466fe76c6c00e3789c5606e27` | Explicit P000 V5 anchor, signed slice and relative observer checks; KEEP. Direct static token crossfile source check also performed (26 relevant tokens on nine exact file bodies), all PASS; original project program not executed this round. |
| `x6_chart_a6_unification_v3_20260906/check_chart_a6_unification.py` | `480a4522705851ac22678ba670d55293014608f5` | Even chart-lift holonomy is a *coordinate-label transport*, not Cell-return or physical rotation; KEEP with new exact signed shortest-BRC invariant and nonidentity witness above. |
| `x6_channel_frame_gauge_v2_20260906/check_channel_frame_gauge.py` | `3110c7017462ed65dbdf887a488dab8b65749450` | S6 channel-frame stabilizer and centralizer, identity fully equivariant transport; KEEP channel-gauge algebra, not native Cell identity. |
| `x6_integral_isometry_v7_20260906/check_integral_isometry_ori6.py` | `77be98e3dce15aac48bc64db6a6fc4e6bbb48f2a` | Signed X6 isometry B6 and even-permutation subgroup algebra typed separately from translation; KEEP. |
| `x6_chart_holonomy_ori6_bridge_v16_20260906/check_chart_holonomy_ori6_bridge.py` | `547a5a6008ba5989b55c067e49ae30e42b11ba4e` | S3 chart-label holonomy and signed Ori6 lift; physical transport not claimed; KEEP. |
| `x6_branch_selector_context_v3_20260906/check_branch_selector_context.py` | `bb8fd71bafa5b8c53c5170d2347baa0f2c06f5fb` | Exact INNER/OUTER event-kind distinction and path history; KEEP, no endpoint-only universal selector claimed. |
| `x6_active_triad_holonomy_v17_20260906/check_active_triad_holonomy.py` | `3d0d8d59b012ed0c58f2cb732be6c62f3140fc9` | Holonomy S3/C2 factor and same endpoints/count different charge: observation compression is distinguished from physical law; KEEP. |

The exact originally audited nine bodies remain in `research_notes/X6_LP28_CURRENT_EXECUTABLE_NINE_CONSUMER_AUDIT_20261113_0630.md` (Git blob `3e1661cccbf9d1ee4b0edda4f6baaf6cc1ee51e5`). This new pass extends bounded actual current-code inspection from nine to **16 nonoverlapping executable bodies**, not the 820 filename-selected candidate paths. The separately read 14 current research checker modules were triaged for relevant native/relative/import semantics, but have **not** all received the same full per-site audit and should not be added to the 16 count.

## Exact continuation and acceptance obligations

- Mother objective: finish the pre-rebase 28-claim ledger's actual current consumer/dependency coverage at frozen scientific Source pins and produce appropriately typed live repairs only for proved misuses. Existing full-original `check_x6_coordinate.py`, `check_x6_cover.py`, LP019 FCC 48-return, LP028 60 signed pair charts, historical 72 and signed selected shell 30/846 are already completed; **do not repeat**.
- This unit directly addresses the LP023 chart-transport/observer-safety, LP026 native metric preservation, and LP028 path-BRC observer-typing consumer branches. Current seven additional checked live consumers are correct at their declared scopes, so no speculative patches were made.
- Residues: original wrongly attributed LP011 native sign/tie selector and LP019 positive-count sign-cancellation callers remain `UNRESOLVED_PROVENANCE`; remaining candidate semantic coverage and Driver `REQUEST_REVISION` still OPEN. Original canonical Source 28-row matrix at `research_notes/X6_LP28_SOURCE_CONSUMER_ACTION_CROSSWALK_20261112_ONHOUR_1400.md` remains the parent index.
- Last verified Source native checkpoint: request `onhour-20261113-0745-own-x6-cover-lp026-source-progress` **SUCCEEDED** at commit `15fc9964038ecf443786064b5e32f6ed364d3a2c`, author `EM-X6-FB6990`. Existing run `RUN-1e81bbcb1938961eb41db249`, generation 6 / revision 7 are **historical recovered pointers**, not current ownership. Fresh exact continuation request `onhour-20261113-0907-x6-canonical-continuation` was `SUCCEEDED` with Source `80bec0054fabbc72c4ab3b495caa37a3c66e56c9`, `route=VERIFY_LIVENESS_THEN_PREPARE_EXPLICIT_TAKEOVER`, `dispatch_state=LEASED`, `execution_authorized=false`. No live winning Researcher claim or current native write permission was established for this new author-side result; **new semantic checkpoint / PROGRESS, Result, freeze and independent Driver admission not claimed**. Preserve old session/request/claim provenance, do not reuse maintenance lane or bypass selector. Next native step is fresh Source liveness/owner verification, then permitted typed continuation if exact route authorizes; otherwise retain author-side GitHub note and report the unbound Source checkpoint.
- Next scientific action: prioritize typed actual-code uses of `Sigma_O^(ij)`, `R061/R062`, `can3/can6` and `positive_return_count` as native X6 endpoint/path semantics among remaining named candidates, with immutable caller blob and source-line evidence; separately search frozen historical LP011/LP019 exact original callers without conflating valid quotient inverses and positive BRC.
