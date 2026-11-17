# X6 Unit84 — signed relative observer is exactly operation-safe for uniform signed BRC transitions

Date: 2026-11-17. Parent objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`. Publication: `TP2-B4A441B23DA3159232C2`.

**Classification:** AUTHOR-EXACT / LOCAL-EXACT-CHECKER-EXECUTED / BOUNDED REAL-SOURCE-CONSUMER-AUDIT / UNREVIEWED / NOT_ADMITTED. This research is retained as GitHub scientific/source evidence, not as an original-X6-authenticated Research Activity, Source PROGRESS or Result. The original 28-LP obligations remain open.

## New operation-specific theorem (not a repeat of Unit83)

Work in a chart-relative native six-axis signed displacement carrier \(\mathbb Z^6\) over an arbitrary selected Cell anchor, with exactly twelve labeled steps \(D=\{+e_i,-e_i:1\leq i\leq6\}\). Put \(\mathbf1=(1,\ldots,1)\), and define the **relative observation**
\[
 \rho(z)=z-\min_{1\leq i\leq6}(z_i)\mathbf1.
\]
Let \(K(z,z')=\#\{d\in D:z+d=z'\}\) be the native nonnegative *labeled-path-count* transition, not an absolute metric or final Cell-address map. Define, for min-zero \(r,s\in\mathbb N^6\),
\[
 \bar K(r,s)=\#\{d\in D:\rho(r+d)=s\}.
\]

**Claim (strong lumpability, every horizon):** For all \(z\in\mathbb Z^6\), every integer \(L\geq0\), and every min-zero \(s\),
\[
 \boxed{\sum_{w:\rho(w)=s} K^L(z,w)=\bar K^L(\rho(z),s).}
\]
More generally, any fixed nonnegative, axis/sign-specific transition weights that depend on the labeled step rather than the forgotten diagonal common depth satisfy the corresponding exact weighted identity. Hence for the precisely declared readout \(\rho\) and the uniform signed BRC path-count transition, the common depth \(h=\min(z)\) can be omitted for *all* future relative-observer counts without losing positive integer multiplicity.

**Proof:** The identities \(\rho(z+k\mathbf1)=\rho(z)\) and \(\rho(z+k\mathbf1+d)=\rho(z+d)\) hold for all \(k\in\mathbb Z,d\in D\). If \(\rho(z)=r\), then \(z=r+k\mathbf1\), so the multiset of the twelve observed successors \(\{\rho(z+d):d\in D\}\), with labels and positive multiplicity, equals the multiset from the canonical representative \(r\). This is exact single-step strong lumpability, including duplicate observed successors. Applying this one-step identity at each step proves the displayed all-\(L\) path-count identity by induction, with the \(L=0\) identity as base. The same argument carries fixed per-label rational/integer nonnegative weights because every corresponding labeled step retains its weight. QED.

**Explicit non-factorable native outputs:** \(\rho(0,0,0,0,0,0)=\rho(1,1,1,1,1,1)=(0,\ldots,0)\), while \(G(z)=\sum_i z_i^2\) is respectively \(0\) and \(6\), and \(T(z)=\sum_i|z_i|\) is respectively \(0\) and \(6\). Thus this exact quotient certificate does **not** cover native \(G,T\), Cell identity, signed endpoint coordinates, arbitrary future observations or ordered-word provenance. A future operation depending on one of those observables must preserve the relevant depth/provenance separately.

**Different transition language:** At \(r=0\), the twelve signed steps have twelve *different* relative successor states and total mass 12; the six-positive-step language has six different relative successor states and total mass 6. Therefore a positive-only kernel may also have its own valid relative quotient but cannot be substituted for this signed kernel. This sharpens the Unit83 length-three 20-fiber comparison by giving an all-horizon **safe** quotient inside the signed language, together with an immediate one-step cross-language obstruction.

## Completed exact finite execution

The portable checker in `research_checks/X6_UNIT84_SIGNED_RELATIVE_TRANSITION_LUMPABILITY_CHECK_20261117.py` compared direct native signed-word evolution followed by \(\rho\) with iterative \(\bar K\) from the observer. Domain: **all 63 binary min-zero six-tuples**, three distinct common depths \(-2,0,3\), and lengths \(L=0,1,2,3\). Results: **756 full multiplicity-Counter equalities**, plus total-mass \(12^L\) at each case, five exact signed-vs-positive one-step predicates, and three explicit \(G,T\) nonfactorization predicates: **1,520 integer checks, zero failures**. All 3 execution modes (Python, `-O`, `-OO`) produced the same exact JSON certificate byte SHA256: `87d973282c078b2d00c8044f471f016cdee2170e86591f496a65e00efef8faf3`. The executable uses explicit exceptions, unaffected by Python's assertion optimization. Finite checks corroborate the theorem for the declared finite test domain; the proof supplies the universal all-horizon statement.

Machine certificate: `research_checks/X6_UNIT84_SIGNED_RELATIVE_TRANSITION_LUMPABILITY_RESULTS_20261117.json`. No original native R063/Helly benchmark was run. No formal machine proof or independent scientific review was performed.

## Exact real-source consumer typing audit

The following actual code was fetched through the authenticated GitHub connector at its declared immutable/frozen versions. The types, source operation and scope were inspected rather than inferred from file names.

| Source, version and observed blob SHA1 | Actual semantic consumer | Decision |
|---|---|---|
| `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` at native frozen blob `300a96e3dc24bf6fff73743037a0347a8bc83176` | `endpoint_multiplicity`, `shortest_path_multiplicity`, `endpoint_weight` operate on six signed endpoint components; weights are positive | Correct signed-native path kernel, not LP019 cancellation |
| `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` at archive pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3` blob `405d9bc752bbf45582f2d0a6d9f91bff9cc5f89e` | `relative_endpoint_multiplicity` takes **six positive steps**, relative min-zero and fixed length; `relative_residual_depth` retains exact common depth | Valid separately typed positive kernel, not a signed-native replacement |
| `experiments/x6_centered_three_axis_slice_v19_20260905/check_centered_slice_rebase.py` blob `406b1eea574ac3235c490dc362ce76d4b072458e` | Loads signed BRC directly and tests signed three-axis embedded displacements with signed shortest path multiplicities | Correct native/slice consumer in inspected calls |
| `experiments/x6_centered_three_axis_slice_v19_20260905/check_centered_slice_crossfile.py` blob `25f520df1e29bdd466fe76c6c00e3789c5606e27` | Asserted min-zero observer is not native Cell identity, typed source distinctions | No identified wrong signed-native quotient call |
| `src/enterprise_math/diagonal_quotient.py` at archive pin, blob `3ac387c0103665943f13ba9e306a6167080c701d` | `canonical_min_zero` explicitly applies to \(\mathbb Z^3/\mathbb Z(1,1,1)\), not a six-axis signed endpoint | Separate derived representation, not LP011 native selector |
| `src/enterprise_math/_triaxial_directional_defect_core.py` at archive pin, blob `5261da8b9e7848ac5cce935f81d7e7e0381b210b` | `diff1_kernel` includes signed *finite-difference coefficients*; `triple_defect_kernel` composes these operators | Signed difference calculus is not cancellation of natural positive BRC path counts |
| `experiments/six_axis_foundation_v2_20260905/vendor/atlas_brc.py` at archive pin, blob `881a34d1919da64a85e6e06902ec3f23654a147e` | Positive `BranchKey` keeps six nonnegative counts, exact positive weights and frame; it identifies itself as typed path key | Correct positive framed BRC carrier, not signed native Cell identity |

**Disposition:** These examined calls give no validated `path:line` for a previous illegal LP011 signed-native argmax or LP019 subtraction of natural positive path multiplicity. Unit82's old bounded-source investigation and Unit83's typed counterexample remain separate, and the unlocated historical allegations stay `UNRESOLVED_PROVENANCE`. Do not edit functioning code on the basis of hypothetical misuse.

## Scientific input/source, owner and next action

- P000 signed six-axis science remains pinned to `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`; original signed BRC blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. Control/current normative main was read separately. Source X6 mother Task/publication remains OPEN pending exact consumer and independent Driver decision.
- Prior verified Unit83: `research_notes/X6_UNIT83_TYPED_BRC_QUOTIENT_CONTINUATION_20261117.json`. Original GitHub-bridge requests `onhour-20261117-1100-x6-own-recovery-status-v1` (Issue #6994) and `onhour-20261117-1103-x6-exact-task-continuation-v1` (Issue #6995) were consumed as existing completed **read** receipts. #6995 returned `SUCCEEDED` and a typed predecessor route but `execution_authorized=false`.
- Original X6 author: SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-579c8e23625448582b421831`, RUN `RUN-fb25028676f9692ab1bacaee` and Activity `RA-5E3FE1E761E4963EC461A892` (106 records), **historical provenance, not authenticated capability of this writer**. The bridge currently projects D25 SID `MCP-de3e5bafb24f43f4a5e6285e7601676a`, a different research subject. No original X6 Activity edit, session/CLAIM/open, Source PROGRESS, native benchmark, freeze, review or admission was performed here.
- **Next discriminating action:** independently inspect a concrete current downstream invocation that *actually* consumes `rho` under native signed future operations, with exact argument type/consumer/path/line and observe whether it preserves the proved \(\bar K\) rule; continue still-unread frozen executable/source branch calls before claiming the historical LP011/LP019 error. Provide precise bounded positive and missing provenance evidence to an authorized independent Driver for `REQUEST_REVISION`, and resolve X6 writer binding only through its actual Source session/conversation identity authorization, never by D25/maintenance reuse.

State: **AUTHOR-EXACT / FINITE-EXECUTED / SOURCE-INSPECTED / UNREVIEWED / NOT_ADMITTED**.
