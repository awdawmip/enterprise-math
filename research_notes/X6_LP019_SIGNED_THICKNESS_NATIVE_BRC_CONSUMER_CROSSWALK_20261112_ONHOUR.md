# X6 LP019 — signed-thickness residual and native BRC consumer crosswalk (2026-11-12)

**Evidence:** AUTHOR_PROVED / EXACT_INTEGER_CHECK_EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED / PORTABLE_RESEARCH_ONLY. Existing accepted R063 results, prior X6 ownership, HRI and Driver REQUEST_REVISION are unchanged.

**Mother:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, objective `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Frozen native X6 input: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`; frozen old comparison: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. P000 has six signed native spatial axes, not a native two-dimensional plane.

## A. Exact current consumer/source distinction

The historical 28-row ledger `claim_ledger.json` (blob `5881055c0801ca5bb0970756d500daa0114d36b0`), LP-019, archives the claim that **native BRC occurrence multiplicity may be cancelled by opposite signs**. Its corrected nonnegative BRC interpretation is sound, but its independent *original historical caller* remains unlocated.

Read two actual current sources (immutable Git blob and exact line range):

1. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` blob `97ab1403ab04b4fa80034625fb1b2e3ed115e59b`, lines 19–49, 51–74, 153–175. It uses signed Cell-to-Cell *primitive-step labels* with positive `PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC` coefficients, preserving path multiplicity independently from endpoint sign. **Disposition: PRESERVE_PATH_BRC / CORRECT_NATIVE.**
2. `driver_reviews/R063_STAGE3_PAIRWISE_INTERACTION_SIGNED_CANCELLATION_DRIVER_REVIEW_20260822.md` blob `32ab69b84c479f34846ae9addf4a601f80645194`, lines 23–39 and 56–66. Its ACCEPTED `C4={+Xi,+Xj,-Xi,-Xj}` process has a *derived Gaussian interaction signed-count* law `(ac-bd,ad+bc)` with confluent count-level opposite-sign reduction; position-retaining cancellation is nonconfluent. Its type is `N1_DERIVED_OPERATIONAL`, not global native X6 signed-step multiplication. **Disposition: PRESERVE_DERIVED_SIGNED_INTERACTION / CORRECT_DERIVED.**

A matching token `signed cancellation` across these interfaces is not evidence of a broken current consumer. The previously identified positive `PathSqrt_E` consumer in `research_notes/TOOL_DISCOVERY_NATIVE_GEOMETRY_OF_NUMBERS_MINIMA_CALCULUS_RESULT_20260822.md` `10 remains a typed positive-two-generator finite-fiber application. LP019's *old historical source/caller* remains `UNRESOLVED_PROVENANCE`. No frozen theorem is edited by this note.

## B. New exact residual law for the four-label count carrier

The theorem concerns a declared finite multiset of four labels `C4={+i,-i,+j,-j}`, not a physical identification of R063 Gaussian cells with native X6 signed primitives.

Write the histogram `h=(p_i,m_i,p_j,m_j) in N_0^4`. The signed net is `s=(p_i-m_i,p_j-m_j) in Z²`; the unsigned thickness is `u=(p_i+m_i,p_j+m_j)`; total length `N=u_i+u_j`.

**Theorem LP019-T1 (bijective count repair).** The map `h -> (s,u)` is bijective onto the integer domain with `u_a >= |s_a|` and `u_a ≡ s_a mod 2` for `a=i,j`, with inverse

`p_a=(u_a+s_a)/2,  m_a=(u_a-s_a)/2.`

For fixed `(s,N)`, let `K=(N-|s_i|-|s_j|)/2`. There is no compatible histogram if `N<|s_i|+|s_j|` or the difference is odd. Otherwise **exactly `K+1` distinct histograms** have this same signed net and length.

**Proof.** Every nonnegative solution of `p_a-m_a=s_a` uniquely has `p_a=max(s_a,0)+k_a` and `m_a=max(-s_a,0)+k_a` with `k_a>=0`. Summing gives `N=|s_i|+|s_j|+2(k_i+k_j)`. The equation `k_i+k_j=K` has `K+1` solutions. Inverse formulas and parity feasibility are immediate. QED.

For a fixed `(s,N)`, the extra axis-pair thickness index `k_i in {0,...,K}` is a sufficient *and minimal count-recovery label*: different `k_i` give distinguishable `h`, so any recovery scheme allowing every histogram query must distinguish `K+1` cases (at least `ceil(log₂(K+1))` bits for a fixed-width code, if `K>=1`). This is observer-relative: ordered paths or source-position posets need further evidence.

**Sharp counterexample:** `h_i=(1,1,0,0)` and `h_j=(0,0,1,1)` have the same signed net `s=(0,0)` and the same `N=2`, but thicknesses `u=(2,0)` and `(0,2)`. The empty histogram also has signed net zero but `N=0`. Hence signed-count cancellation may erase *net amplitude*, not positive event/path population.

## C. Existing signed-X6 BRC kernel, actually exercised

For a **separately declared** free signed-step X6 alphabet restricted to two chosen native axes, let `B_N(s)` count ordered words of total length `N` and signed endpoint `s=(s_i,s_j)`. For integral `K=(N-|s_i|-|s_j|)/2>=0`, with `s_a^+=max(s_a,0)` and `s_a^-=max(-s_a,0)`:

`B_N(s)=Σ_{k=0}^{K} N!/[(s_i^++k)!(s_i^-+k)!(s_j^++K-k)!(s_j^-+K-k)!].`

It is zero outside the feasibility domain; each summand counts a distinct hidden histogram fiber and is nonnegative. At `K=0` this specializes to the established shortest signed-axis multinomial BRC coefficient. For six axes, if `z∈Z^6` and `K=(N-Σ|z_a|)/2>=0`, the **exact number of nonnegative six-axis cancellation-thickness histograms** is

`binom(K+5,5)`,

and the endpoint-word count is the sum of `N!/Π_a[(z_a^++k_a)!(z_a^-+k_a)!]` over all `k_a>=0` with `Σk_a=K`. This is a residual/fiber interpretation of the *existing* `endpoint_multiplicity` implementation in `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, not a replacement implementation.

At the *native zero displacement*, `N=2` gives six admissible return-axis histograms and **12 positive two-step ordered return words**; `N=4` gives `binom(7,5)=21` histograms and **396 positive words**. In the two-axis restriction, the corresponding totals are **4** and **36**. A signed net of zero therefore cannot be interpreted as cancellation of BRC route multiplicity; retaining only the endpoint also loses length and path order.

This is directly relevant to LP019 and LP026: it preserves a legitimate signed algebraic channel alongside the native positive-branch path-count channel, without equating them or reopening R063 Stage 3's accepted positional nonconfluence theorem.

## D. Executed exact regression

The new checker `research_checks/X6_LP019_SIGNED_THICKNESS_AND_BRC_FIBERS_20261112_ONHOUR.py` was locally executed on 2026-11-12 with Python exact integers. It verifies:

- All **625** histograms in `{0,1,2,3,4}^4` against the signed/thickness inverse.
- Independent four-signed-step dynamic programming for all lengths `0..12`, with **2,925** exact formula comparisons; `B_2(0)=4` and `B_4(0)=36`.
- The actual, unmodified Source `signed_brc.py` imported at the repository path and blob-checked to `300a96e3...`, versus *independent* twelve-signed-step six-axis recurrence for all lengths `0..6`: **10,364** exact endpoint/length comparisons; `return_multiplicity(2)=12` and `return_multiplicity(4)=396`.

Result: **PASS**, with source blob match, no floats. The finite coverage validates implementation. The stated general count-repair and fiber formulas have the separate algebraic/combinatorial proof above. BRC reuse decisions: **REUSE_EXECUTED** current native signed endpoint kernel; **COMPOSE_APPLIED** its existing law to the LP019 current-consumer typing.

## E. Frontier and owner/control limits

**Completed/do not repeat:** source-pinned signed X6, 72 historical sector subtotal, 111/carrier kernel and closed disk, LP011 signed chamber and median/typed-guard, full signed N=25 and N=2500 restricted shell counts, prior R063 signed fiber theorem, accepted R063 Stage 3 tensor, and prior 72 historical definition + 38 research-note readbacks. This note resolves a *specific LP019 current-consumer ambiguity* and supplies a new exact lost-thickness classification; it does not claim the historical LP019 original independent calling location was recovered.

**Still open:** the historical LP011/LP019 original caller provenance where available, the remaining 28-row source/type/downstream/action crosswalk, and the declared current consumer dependency manifest under the existing `REQUEST_REVISION`. Next science: source-line audit of remaining LP026 quadratic/parity/affine rules and real active consumers; issue a precise crosswalk row per mathematical formula and typed readout, without replacing valid lower-layer formulas.

**Native lane:** The current Research-only conversation identifier remains `chatgpt-research-onhour-enterprise-math-20260923`; old own session `MCP-de3e5bafb24f43f4a5e6285e7601676a` is ACTIVE according to the original read-only #6844 receipt but has no verified winning X6 CLAIM/open. Successful original continuation `onhour-research-20261112-0422-x6-continuation-v1` (#6827) requested exact old evidence; original #6845 artifact query returned `ARTIFACT_NOT_IN_CONTINUATION_PACKET`. The standing repair/owner support item is `awdawmip/enterprise-math#2141`. This note is portable scientific evidence, not a native semantic checkpoint, accepted Result or independent Driver review. The existing Research Activity is `RA-629C868A22A736334628BEFA`; source-side activity checkpoint may record the new artifact without conferring CLAIM.

