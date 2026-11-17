# X6 Unit100 — signed orientation lost by the historical FCC six-line permutation consumer

**Date:** 2026-11-18 (Asia/Hong_Kong). **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. **Frozen historical source:** `fd2bcff10ca6e147348b6c1236027fc0d2877df3`; current mathematical baseline remains frozen P000 V5 `59538f585d037d09ef687b28715c4bc1a3f9fe03`.

**Status:** AUTHOR-PROVED / EXACT-INTEGER-EXECUTED / UNREVIEWED / NOT_ADMITTED. This is a precise derived-FCC-carrier representation result, **not a new native P000 six-axis rotation law**.

## Actual historical caller and the missing information

The full pinned historical file `research_checks/P000_6D_AXIS_MIXING_ROTATION_ALGEBRA_CHECK_20260829.py` (Git blob `f4bca58531d9a1df542d6e053b636f698e117084`) at lines 4–8 names six unordered edges of a tetrahedron and gives each an oriented three-coordinate FCC carrier vector. Lines 41–71 compute the 24 determinant-positive signed coordinate permutation matrices, but take an unoriented-line key `lk(v)` that identifies `v` and `-v`. The resulting six-element `eact` is a permutation of **unoriented carrier lines**.

For the six named edges in source order `AB, AC, AD, BC, BD, CD`, use the exact vectors

- AB=(1,1,0), AC=(1,0,1), AD=(0,1,-1);
- BC=(0,1,1), BD=(1,0,-1), CD=(1,-1,0).

These are **derived three-dimensional FCC carrier vectors**, not the six independent signed primitive X6 axes. For every matrix `M` among the 24 source transformations and every named carrier edge `e`, precisely one named edge `f` and one sign `eps` satisfy `M v_e = eps v_f`. The original `eact` retains `f` while its canonical line key discards `eps`.

## Exact signed-lift theorem

Let `G` be the source's finite group of 24 determinant-positive signed-permutation 3×3 matrices. Define the signed carrier lift by the unique relation

`M v_e = eps_M(e) v_{sigma_M(e)}`, with `eps_M(e) in {-1,+1}`.

Then `sigma_M` is the original 24-element faithful unoriented FCC edge action; the enriched pair `(sigma_M,eps_M)` gives an exact **group representation on the six formal signed *carrier* directions**. For any `M,N in G`,

`sigma_{MN}(e) = sigma_M(sigma_N(e))` and
`eps_{MN}(e) = eps_N(e)*eps_M(sigma_N(e))`.

**Proof.** The six source vectors determine six distinct unoriented FCC lines. Each source matrix preserves this finite line set; the vector equality fixes the target and sign uniquely. Applying `M` to the defining relation for `N` yields the two composition identities by linearity. These are identities of the *derived FCC representation*.

**Minimal concrete witness.** Set `M=diag(-1,-1,1)`, which has determinant +1 and belongs to the source's 24 matrices. The AB carrier vector `v_AB=(1,1,0)` obeys `M v_AB=(-1,-1,0)=-v_AB`. Thus the original unoriented six-line `eact` says `AB→AB`, while the signed carrier lift says `+AB→-AB`. This is an exact input/output witness that the six-line permutation alone does not retain signed orientation under later composition or observation.

It is a **data-loss witness**, not evidence that the historical author incorrectly asserted full P000 native rotation. Source lines 148–154 explicitly keep an HCP/native limitation, so the source deserves a typed `PRESERVE_CARRIER` classification.

## Executed finite certificate

The independent Python checker was actually executed in regular CPython, `-O` and `-OO`, with explicit `require` guards whose checks remain active in all three modes. Outputs were byte-for-byte equal (certificate SHA256 `af192bba169238315c086c71a1c320f2eddfa7676b6bb982bd7581cff9a2e7f4`).

| Exact integer item | Observed result |
| --- | ---: |
| Distinct determinant-positive source matrices | 24 |
| Distinct unoriented carrier line permutations | 24 |
| Named carrier direction images | 144 |
| Negative-orientation images | 72 |
| Same-line but reversed-orientation images | 12 |
| Transformations with at least one sign reversal | 23 |
| Exact pair compositions | 576 |
| Basis-direction composition equalities | 3,456 |

The full checker is `research_checks/X6_UNIT100_FCC_SIGNED_CARRIER_LIFT_CHECK_20261118.py` at immutable commit `b6245eed154573848c37f99b7a8f408a301fcfc4`, with machine result `research_checks/X6_UNIT100_FCC_SIGNED_CARRIER_LIFT_RESULTS_20261118.json` at `bfa0956483ce7e6f92c076127fb81d3032cfd280`. The source checksum of the executed checker is SHA256 `582abd44f34be4f7c2b63b6d8d5e46198afe159cb494cd17e418dd89cf1655b4`. The original 2026-08-29 script remains unchanged.

## Related source dispositions

Six other pinned `research_checks/` programs were read as positive/negative typed cross-checks:
- `P000_L1_NATIVE_FCC_CARRIER_BRIDGE_CHECK_20260829.py` blob `de645d6de3b85165fe8943aa6566e050ec47c623`, lines 47–68: local star closures and nontrivial holonomy, explicitly finding **zero** global 120-degree orientation sections;
- `P000_NATIVE_FCC_BRIDGE_COHOMOLOGY_PRIOR_ART_AUDIT_V5_CHECK_20260829.py` blob `e2223b067528104de9f158776294a53d617f4ca3`, lines 119–160: signed K4 double cover and cube combinatorics, a carrier groupoid;
- `P000_FULL_CELL_AXIS_HANDLE_REALIZATION_V9_CHECK_20260829.py` blob `31105bb103998c4bf5fc6157668c3c1bb6aebb79`, lines 173–182: explicit native Cell identity is distinct from same carrier readout and omitted coordinates;
- `P000_PHILOSOPHY_FIRST_BARE_SLICE_DESCENT_SEMANTICS_CHECK_20260830.py` blob `575aa3d9ab803c1bebc94d809769a2c80ee432cb`, a finite gauge/globalization abstraction;
- `P000_PHILOSOPHY_FIRST_NATIVE_MODEL_CHANGE_ARROW_AUDIT_CHECK_20260901.py` blob `fbfdfd5abc9d56a436b36c55adb3070e54162fee`, lines 104–126: observer/reduct does not become a Full-Cell arrow;
- `P000_THREE_AXIS_A2_HEXAGONAL_CUBIC_THETA_BRIDGE_REVISION_V2_CHECK_20260830.py` blob `9974b1da9a88fc48040ca176fa486e3b8ef24559`, lines 59–107: the diagonal difference collision `(1,1,1)` versus `(2,2,2)` is **representation-only**, with an explicit NOT_DERIVED admissible PF-10 quotient.

These are source observations, not original benchmark executions. The typed signed-orientation extension offers a precise compatibility test if a future *actual* downstream consumer passes unsigned `eact` images where signed carrier direction is needed.

## Mother task and execution controls

Unit99 source audit has 54 fully read historical `src/tests` candidates. LP011's alleged wrong signed native dominant-axis caller and LP019's alleged subtraction of positive natural N-BRC remain `UNRESOLVED_PROVENANCE` after this additional scoped evidence. The independent Driver's existing `REQUEST_REVISION` is the appropriate evidence-review route.

Original Research SID `MCP-082892eb480e45dea6d4b9fcc0491034`. The original same-ID read `onhour-20261118-0004-x6-own-exact-cont-read-v1` finished **SUCCEEDED** and returned `TYPED_FRONTIER_REQUIRED` plus previous claim `MCP-579c8e23625448582b421831`; its `execution_authorized=false` is a read-only status. No protected CLAIM, open, resume, PROGRESS, or maintenance conversation mutation occurred. New GitHub artifacts are research sources only; the original R063/Helly benchmarks were not rerun.

**Next exact action:** trace whether the derived 6-line permutation from this frozen consumer is imported as a *signed* six-direction action in any active theorem-facing interface, with a concrete source:line and retained sign flag. Continue the 28-LP crosswalk and separate independently supported repairs from unsupported historical blame. No Source replacement is needed absent an actual erroneous consumer.
