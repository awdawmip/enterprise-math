# EM-FREE-F6D046 R105 state-machine handoff

Status: `DURABLE_HANDOFF / DERIVED / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`

Date: `2026-09-09`

Researcher source identity: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Parent objective: `EM-FREE-F6D046-RAMANUJAN-GEOMETRY`

Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN` — remains `REJECT_AS_NEW_AXIOM`.

## 1. Canonical evidence location

The full R1-R105 evidence chain is intentionally not copied to main. It remains on the research evidence branch:

- branch: `research/em-free-f6d046-ramanujan-period-wronskian-20260904`
- pinned evidence head: `574f53c7b37ae6703ade390df851d8822af6364c`
- review thread: `#1229`

New researchers should treat this file as the main entry point and read only the minimal chain below before opening individual proofs or verification ledgers.

## 2. Minimal read order

Read in this order:

1. `research_notes/EM_FREE_F6D046_LATEST_FRONTIER_R105_20260904.md`
2. `research_notes/EM_FREE_F6D046_RESEARCH_CHAIN_INDEX_R85_20260904.md`
3. `research_notes/EM_FREE_F6D046_CHAIN_CONTINUATION_INDEX_R96_R105_20260904.md`
4. `research_notes/EM_FREE_F6D046_P46_TWO_ADIC_SCALAR_AUTOMORPHISM_ORDER_REFINEMENT_R100_20260904.md`
5. `research_notes/EM_FREE_F6D046_P46_PRINCIPAL_RING_CLASS_DEFECT_R104_20260904.md`
6. `research_notes/EM_FREE_F6D046_P46_PRINCIPAL_VS_WEIL_RESTRICTION_CENTER_R105_20260904.md`

All six paths are on the pinned research branch above. Follow their own source/evidence pointers only when a proof detail is needed.

## 3. Frozen research status

The original Ramanujan coefficient candidate is not a new axiom. The derived chain has nevertheless produced a precise arithmetic-geometric model. Frozen facts through R105 include:

- `P46/Qbar` is geometrically simple with `End^0=Q(i)` and `End=Z[i]`;
- the characteristic-zero Mumford-Tate/Sato-Tate structure is unitary, with connected Sato-Tate `U(4)` and component group `C2`;
- at `p=7`, after `F49`, `P46 ~ B^2`, and `B` has an explicit genus-two Jacobian realization;
- the quartic primitive CM field has real subfield `Q(sqrt(417))`; its primitive reflex has real subfield `Q(sqrt(6))`;
- Newton slopes are `0^2,(1/2)^4,1^2`, with `p-rank=2`, `a-number=2`, and EO final type `(1,2,2,2)`;
- the Prym polarization kernel is `E[2]`; the three degree-two principalizations first split over `F_(7^3)`;
- the geometric `Q(i)` outer character is killed over `F_(7^2)`, and simultaneous strictification first occurs over `F_(7^6)`;
- at two, `F tensor Q2 = Q2(sqrt(-2)) x Q2(sqrt(5))`, the unramified factor has residue field `F4`, and the polar kernel is integrally `O_unr/2 O_unr = F4`;
- selecting a principalization line lowers the unramified scalar order to `Z2+2 O_unr`; the Frobenius scalar order has index `14`, the principal scalar order index `28`, and the scalar local-global/ring-class defect is `C3`;
- the canonical Weil-restriction fourfold has maximal unramified scalar center, so no Prym principalization is geometrically isomorphic to it even after forgetting polarization.

## 4. Exact current hard frontier

The smallest unresolved object is the **full rank-two integral Hermitian lattice at the unramified two-adic CM place, including its non-scalar unitary automorphism group**.

Scalar units and Frobenius/CM/Newton/EO data are exhausted and cannot decide the orbit of the three principalization lines. The next computation must recover the actual integral Hermitian Gram/module data and determine the full `U(L)` action.

## 5. State-machine tasks published from this handoff

- `RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY`: primary next task; exact `U(L)` and action on three `F4` lines.
- `RS-EMF6D046-R107-PPAV-THETA-JACOBIAN`: continuation after R106; global ppav classes and rigorous genus-four Jacobian test.
- `RS-EMF6D046-R108-HONDA-TATE-CORRESPONDENCE-REDUCTION`: parallel residue; explicit rank-one Honda-Tate correspondence and scoped reduction-stratification theorem.

Dependency structure:

`R105 handoff -> R106 -> R107`

and independently

`R105 handoff -> R108`.

## 6. Frozen corrections and scope limits

- Do not reopen P000; it is unchanged.
- Do not promote the original period-Wronskian candidate; it remains rejected as a new axiom.
- Do not equate local two-adic principalization orbit with global ppav isomorphism.
- Do not treat an indecomposable principal ppav as automatically a genus-four Jacobian; exact theta/Schottky or explicit-curve evidence is required.
- Do not identify the Honda-Tate square decomposition with a new special-fiber curve automorphism quotient.
- The recovery placeholder `EM_FREE_F6D046_R40_R44_CM_REFLEX_REDUCTION_STRATIFICATION_20260904.md` has no theorem authority; use the authoritative P46 CM/reflex note referenced by the R105 index.

Classification: `DERIVED_CHAIN_R105 / EXACT_DURABLE_FRONTIER / STATE_MACHINE_DELEGATED / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.
