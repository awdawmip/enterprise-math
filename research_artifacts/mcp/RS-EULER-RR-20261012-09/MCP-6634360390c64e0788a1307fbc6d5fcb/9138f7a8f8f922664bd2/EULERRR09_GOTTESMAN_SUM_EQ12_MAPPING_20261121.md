# Euler RR-09: original-source SUM gate bridge (2026-11-21)

Status: AUTHOR-DERIVED FIRST-PASS PRIOR-ART MAPPING; NOT INDEPENDENTLY REVIEWED. Task RS-EULER-RR-20261012-09, publication TP2-D6320792C26EFAD4DDCD.

## Primary-source locator
Daniel Gottesman, "Fault-Tolerant Quantum Computation with Higher-Dimensional Systems", arXiv:quant-ph/9802007, originally submitted 1998-02-02, Section 2 ("Higher Dimensional Generalization of the Pauli Group and Other Structures"), equation (12): the d-dimensional SUM gate maps |i>|j> to |i>|(i+j) mod d>. Source: https://arxiv.org/abs/quant-ph/9802007 ; HTML text readable from the arXiv indexed source. The claim here uses only the permutation of basis labels, not a quantum superposition or physical implementation. This exact equation locator is stronger provenance than a generic citation to reversibility.

## Exact classical-label specialization
For j,a,r in Z/3, define S_(x→r): (x,r) ↦ (x,r+x) and S_(x→r)^{-1}: (x,r) ↦ (x,r-x). Gates acting on distinct controls j and a, same receiver r, commute. Therefore
E(j,a,r)=(j,a,r+j-a)=S_(j→r) ∘ S_(a→r)^{-1}(j,a,r).
Each factor is a direct specialization (d=3) of the SUM gate's basis-label map, with the second inverse. E is bijective, inverse E^{-1}(j,a,r)=(j,a,r-j+a), and E^3=identity. These are algebraic consequences of the prior standard operation, not independent novelty claims.

## Relative-record identity and calibration
Let ω^3=1, ω≠1 and C_XY:=Σ_w p(w) ω^{label_X(w)-label_Y(w)}, with p(w)>0 summing to one, and world weights preserved by E. Since r'-j=r-a mod3 for each world, C_RS(after)=C_RA(before) for any correlated joint distribution (no independence assumption). If r=a on each world, then r'=j. Conversely for positive normalized weights, C_RS(after)=1 forces every phase ω^{r'-j}=1, equivalently r=a. Proof: Re Σ_w p(w)ω^{r'-j}=1 and the real part of either nonzero 3rd root is -1/2, so all nonzero-difference weight must vanish.

The correlation identity is an elementary downstream specialization of the finite permutation and positive weighting, not asserted to have appeared verbatim in Gottesman's paper. Project-specific additions: realization via existing typed positive BRC contact/hold operations, single shared-field preservation, and source projection commuting with the allowed subsequent source dynamics; each requires its own implementation/semantics certificate.

## Reverse applicability / scope check
Gottesman's equation (12) is a quantum computational gate on d-dimensional basis kets; it does not by itself establish a native 6D Heartbeat World physical readout, local channel-selector derivation, undisturbed measurement, environmental cost bound or stability of a continuously engaged latch. Conversely the BRC paper's correlated positive-world identity does not instantiate a general quantum no-cloning or universal fault-tolerant quantum computing theorem. The operation E with no disengagement is order 3; after three applications it returns to the initial state, so a permanently stable autonomous latch is not obtained.

## Distinct prior-art and next question
Toffoli 1980 MIT-LCS-TM-151 discusses invertible computing primitives and reversible composition (https://hdl.handle.net/1721.1/148978). Bennett 1973 IBM J. Res. Dev. 17(6):525-532 DOI 10.1147/rd.176.0525 gives logical reversibility and history-preserving/uncomputation ideas, not a by-itself exact proof of the project's typed-BRC contact mapping. The precise external algebra antecedent is Gottesman 1998 Sec 2 Eq (12). Verify the original paper/version pages and identify an original theorem-level source for the separate finite-environment history bound; preserve that part as UNRESOLVED. Distinguish the earlier staged first-pass note from this incremental equation-level source mapping; do not duplicate its already completed checks.

Frozen source: enterprise-math@a6627d28d1e02f16ec5ca4d5118801c005cca583 research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md; canonical taskbook at enterprise-math@5ef6c9e7459d3c2155f9a26273683f244a4b7826 research_tasks/RS-EULER-RR-20261012-09_C01_GEN2.md. P000 native ontology preserved. Source publication and review pending; this staging statement grants no CLAIM.
