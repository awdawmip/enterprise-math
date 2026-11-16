# X6 Unit75 — current executable inverse-orbit BRC mass and typed cancellation consumer audit

Date: 2026-11-17 (Asia/Hong_Kong 05:xx). Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905 / Task RS-X6-LEGACY-PLANE-RECONCILIATION / publication TP2-B4A441B23DA3159232C2.

Author provenance: own TASK_RESEARCH EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034; Research conversation chatgpt-research-onhour-enterprise-math-20260923. Scientific pins: P000 V5 source 59538f585d037d09ef687b28715c4bc1a3f9fe03, historical corpus fd2bcff10ca6e147348b6c1236027fc0d2877df3. Current executable-source audit snapshot: repository main 0b4ea2999a48055d1f3c4cc6b7a352670fa4f03c, with exact Git blob identities below. The current audit supplements, rather than replaces, the historical 28-LP matrix. Independent review/admission are pending.

## 1. Exact conditional theorem for the live inverse-orbit mass consumer

Let U be a finite abelian group, g in U, and write [u]={u,u^{-1}}. For nonnegative integer directional weights p and q, consider a **positive-mass** kernel on U whose outgoing multiset from u consists of 2 copies of u, p copies of ug, and q copies of ug^{-1}. The inverse-orbit quotient retains only the destination orbit [v] and total nonnegative multiplicity.

For u and u^{-1}, the exact difference of their quotient destination-mass rows is

  Kbar(u,.) - Kbar(u^{-1},.) = (p-q) (delta_[ug] - delta_[ug^{-1}]).

Consequently the inverse-orbit quotient is well-defined for **every source u** if and only if

  **p=q, or g^2=e.**

Proof: Invert the three targets from the inverse source; inversion turns [u^{-1}g] into [ug^{-1}] and [u^{-1}g^{-1}] into [ug], proving the row difference. If p=q the difference vanishes, and if g^2=e the two destination classes coincide. Conversely if p!=q and g^2!=e, take u=g. Then [ug]=[g^2] and [ug^{-1}]=[e]={e} are distinct, giving a nonzero difference. All weights and masses remain nonnegative. This is a theorem about the stated finite group BRC operator, not a statement about signed-native six-axis X6 step paths.

## 2. Exact source:line classification of previously unlisted current consumers

All seven listed current production bodies and two test bodies were fetched through the connected GitHub reader; this is a bounded current-executable source slice, not all repository executables.

| Current source (Git blob SHA-1) | Decisive lines and actual operation | LP011/LP019 disposition |
| --- | --- | --- |
| `src/enterprise_math/group_ring_inverse_quotient.py` (`cf34a9d48e36fae5bbb8c9538864cddf8315690e`) | 1–12 specify modular-unit inverse-orbit **mass-only** specialization; 88–113 transfer 2[e]+[g]+[g^-1] using additions and check positive 4^depth total; 135–177 expose the nonnegative p/q certificate, including biased weights as an unsafe-partition test. | KEEP: positive nonspatial branch mass; the "negative_weight" argument is the weight of the inverse **direction**, never a negative path count. |
| `tests/test_group_ring_inverse_quotient.py` (`d963d85215d377dfe4a6f54131395a9a111b3a4d`) | 64–76 verify existing unchanged BRC quotient and explicitly reject p=2,q=1 for U(7),g=3; 79–85 shows source 3/5 share orbit but a tagged positive atom separates them. | Existing executable rejection of unsafe observer compression, not an LP019 violation. |
| `src/enterprise_math/brc_newton_fiber_quotient.py` (`f9db29609e74b8f2a7202a1f626a138eb716fa29`) | 123–139 sums rational **polynomial coefficients** in each Newton fiber, possibly cancelling to zero; 169–187 applies a signed coefficient transfer `values[anchor]-=delta; values[moved]+=delta`. | KEEP: signed rational coefficient algebra, **not** subtracting positive native N_BRC path multiplicities. |
| `src/enterprise_math/brc_residue_port.py` (`9b0314b272843431af9f170897c95be608ccef16`) | 29–32 demands six signed integer coordinates; 158–165 evaluates actual endpoints and recoalesces **WeightHistogram** without signed mass subtraction; 167–172 reads total mass solely for the stochastic property; 174–185 retains six-coordinate moments. | KEEP: six-coordinate port is a typed congruence/fiber carrier, neither a seventh dimension nor an asserted complete path-state quotient. |
| `src/enterprise_math/brc_control_port.py` (`44def6b8ac787e798d3cc2c6be16f873f91b9db8`) | 1–10 nonspatial control-state qualification; 123–141 compares exact target-class `EffectHistogram.entries`; 141–161 refines future-safe control partitions while preserving effects. | KEEP: effect-valued future safety and declared observer, not scalar signed-axis argmax. |
| `src/enterprise_math/operation_quotient.py` (`758a65de02a434446936cd7e37b2ae604eade863`) | 1–11 exact finite deterministic endomap family; 105–152 refines observational partition under **all named operations**. | KEEP: general operation-safe partition, a potential adapter tool only after native signed domain and operation family are declared. |
| `src/enterprise_math/partial_operation_quotient.py` (`d1f86491ce07279c058a4c99f40cabb1f96da0de`) | 1–43 explicit partial action enabledness; 175–194 tracks `(enabled,next-class)`; 197–232 computes stable refinement. | KEEP: preserves branch legality and absent transitions; not a native positive-BRC negative coefficient. |
| `src/enterprise_math/signed.py` (`46386899c59483a9d83f8fe23387dbf8d20e18ec`) | 33–72 ordinary-order odd roots versus scalar signed-magnitude collapse. | KEEP: scalar integer-root model, not signed native path-mass implementation. |
| `tests/test_p023_operation_quotient.py` (`89f93a312b4aaa40aac855de3691c445f7645019`) | 31–46 crosschecks all operation-word signatures; 48–70 checks coarsest compatible partition in a finite domain. | Existing direct operation-descent check; not evidence of a native X6 erroneous consumer. |

## 3. New exact executed U(7) distinguishing certificate

Use U(7)={1,2,3,4,5,6}, g=3, inversion orbits [1]={1}, [2]={2,4}, [3]={3,5}, [6]={6}. The full source row for u=3 and inverse u^{-1}=5 under symmetric p=q=1 is identical: [1]:1, [2]:1, [3]:2. Under asymmetric p=2,q=1, rows differ: source 3 gives [1]:1,[2]:2,[3]:2; source 5 gives [1]:2,[2]:1,[3]:2. This is **failure of directional quotient descent**, not cancellation of positive mass.

An independent exact-integer Python checker enumerated all six unit sources and all 16 pairs (p,q) in {0,1,2,3}^2, with the row-difference formula evaluated at each of the four quotient target classes: 96 source/inverse comparisons and 384 exact destination-class identities. Exactly four symmetric pairs are future-safe and twelve asymmetric pairs are not. Explicit non-assert validation ran in CPython normal/-O/-OO with byte-identical JSON SHA-256 `fa356a3c74b497158c8f9e37dead69262b5735909a16dcfc75e6da7d3a6e5bcf`. This independent checker does not execute or replace the original frozen R063 / Helly native experiments; it checks the present precisely named control quotient mechanism.

## 4. Scope, disposition and continuation

For these nine exact current source/test bodies there is **no located erroneous historical LP011 singleton signed-native argmax** and **no located erroneous historical LP019 natural-positive-N_BRC signed subtraction**. This finite source-level classification is a genuine increment to the remaining 28-LP consumer dependency graph. It is not a repository-wide absence claim and does not revise frozen P000, the old R063 benchmark, or another owner's PR.

Next exact action: search remaining specifically X6/path-facing active call sites or frozen historical claims for an actual source:line that **uses** a relative/positive-sector argmax as native signed-axis dominance, or uses signed algebraic cancellation to subtract positive natural N_BRC paths; determine the direct callee, input type, observer and required repair before alleging a bug. Continue 28-LP live dependency closure and the independent Driver REQUEST_REVISION.

Native Unit74 original request `onhour-20261117-unit74-full6-shortest-equal-plus2-native-progress-v1` has been consumed as SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED, Source `cc3368100f8de3b00c89b7f4d1567f008b9944c4`. Own subsequent same-SID resume request `onhour-20261117-0536-x6-own-run-resume-unit75-v1` must be reconciled on its original ID before any new Native semantic Unit75 publication. Preserve own same CLAIM/RUN and all previous source/Activity results.

Scientific status: AUTHOR-PROVED conditional theorem / independently EXACT FINITE-EXECUTED / current-source BLOB-VERIFIED / UNREVIEWED / NOT_ADMITTED. No change to scheduler, notification, source pin, other owner, or P000.
