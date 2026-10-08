# P11 independent cross-branch audit — line Driver review

Driver EM-DVR-59E7AD, session MCP-e10e9b09793a43aeadbe763836a35c04, DA-3C861959D835533878BE. Task RS-P000-P11-ARITHMETIC-LINE-INDEPENDENT-AUDIT / TP2-4E0EE03CCD6B6126A1D7.

Result reviewed: RR-29AA6AA5CC2CEBB893CA, Source 5e49e7384ea0659ec187cec44d52dcb6c9ee74d8, path research_result_records/RS-P000-P11-ARITHMETIC-LINE-INDEPENDENT-AUDIT/RR-29AA6AA5CC2CEBB893CA.json, SHA256 14dd4c98879ab228d96c8ef0d13fc0fdf13263da635bf2b37c25ca13de5ac5b5, Git blob d7840cc213344c783717515da2e2ca5fd58dcd5b. The native terminal verdict is AUDIT_COMPLETE/SATISFIED; the mathematical audit verdict is VERIFIED_COMPATIBLE. Current Result bytes and reviewer authority must be freshly checked again at the native review write boundary.

## Decision and evidential role

ACCEPTED at the precise derived-arithmetic compatibility scope in AUDIT_PROOF.md and CLAIM_MATRIX.json. The original ten outputs are satisfied. Both exact accepted branch Results survive the independent implementation/derivation and compose through the labeled P11 sum/product and sixteen-root interface. No unresolved task-specific defect requiring a revision or narrower replacement theorem was found. Existing explicit domain and quotient restrictions remain binding.

The verifier EM-P000-37E795 was a fresh-context agent with its own RA, claim and authorized run. It had no prior material contribution to either branch, received no proof constructions or prescribed audit verdict, and read exact formal mathematical inputs after its own authorized open. Its disclosure is SHARED_AMBIENT_CONTEXT_DISCLOSED / NONBLIND_DISCLOSED, not blind discovery or platform-attested isolation. The static metadata helper indexed immutable hashes/citations/assert locations only. The verifier authored the new derivations and independent checker without importing or executing either author implementation. These disclosed conditions satisfy this Task's actual independent-verifier requirement.

This reviewing Driver had earlier routed and reviewed off-diagonal work and had accepted-branch/control context. The Driver did not construct the audit proof or verifier checker and first read this audit mathematics after NEW Result freeze. reviewer_contribution_ids is empty. This is the line review of an independent audit, not a claim that the Driver's earlier checks were that audit.

## Exact evidence and reproduction

The Driver fetched the complete RR and all eleven declared outputs from immutable Source through the connector and independently recomputed SHA256 and Git blob for each. All matched. MANIFEST_VERIFIED.json records those bindings; artifacts are at owner head ddc70bac138ec8eb8fd1dbaf68b6ed03d86d2652 under research_artifacts/mcp/RS-P000-P11-ARITHMETIC-LINE-INDEPENDENT-AUDIT/MCP-195e2b6e160143c9941fbbd8bdefdfdb/94e220b937c6eb5a38ac/.

SOURCE_INPUTS.json's six formal RR/DR/DFU records and all 23 branch manifest entries were compared against this Driver's independently held exact Source678dc5be4e0ff642cd55e34cbac2b85042e28cd4 readbacks. The control bindings and artifact hashes agree with accepted diagonal RR-C1F5BD75CF29E3970097 / DR-2F805343ED6728A5CD35 / DFU-832FD239C5CBEBCC2310 and off-diagonal RR-2DAA0B408E99259119BE / DR-87CC4E7C0CAC3757C377 / DFU-13354F28F9A0EBBC9E21. Unchanged earlier verdicts are consumed, not replaced by a new historical review.

After inspecting both delivered programs, the Driver ran byte-identical copies in a separate reexecution directory. The two source data files used by the comparator were independently connector-fetched and hash-verified. Python3.12.14 / SymPy1.14.0 reproduced all ten exact symbolic identities, diagonal n=1..8, off-diagonal odd n=1..13, all nine published family-row matches and both old witnesses. Both commands returned PASS. The comparison output is byte-identical. INDEPENDENT_CHECKS.json is semantically identical as parsed JSON; its bytes differ only because the published output was whitespace-compacted, as RUN_SUMMARY explicitly discloses. DRIVER_REEXECUTION.json preserves both hashes and this distinction. No frozen evidence was overwritten.

The static checker inventory explicitly does not claim dynamic coverage. Its absence of universal routines in an author checker is not used to discredit or prove a theorem; the audit supplies the needed written derivations separately. Historical ARITHMETIC.md, optional REFERENCE_APPLICABILITY.md, temporary REPRODUCED.json and external PDF byte history are not independently reproduced. The new source-complete proof and exact computation replace reliance on historical PASS statements for the audited obligations. This limitation is retained in acceptance.

## Load-bearing scope checks

The common reconstruction derives K=4hd and both middle-row square cuts directly from cell discriminants. Necessity and sufficiency concern the eight outer cells with ordered positive cores; actual sixteen roots determine integrality and parity. The middle cell is not silently included. K=0 with d>0 gives h=0 and identical ordered positive factors; K!=0 gives h=K/(4d). This does not extend the off-diagonal theorem over a forbidden parameter boundary.

On the diagonal branch, the explicit rational map/inverse, the four D=0 two-torsion points, excluded xi=±PQ poles and absence of rational projective points at infinity are accounted for. The strong Fermat descent argument excludes |D|=Q; hence all non-torsion multiples give strict nonzero cuts and no zero product roots. Two-division plus Mazur leaves precisely the declared (2,2)/(2,6) alternatives, with the exact psi3/integer-divisor test deciding three-torsion per core. The valuation argument proves finite squareclass support, not Selmer completeness or a local-global theorem. The seed's odd-prime Nagell-Lutz obstruction and short-model check prove infinite order. Absolute-value normalization has at most eight preimages, while the actual sixteen-root gcd and retained core scale prevent collapse to finitely many primitive outputs. No injectivity in the diagonal multiplier is accepted.

On the off-diagonal branch, the smoothness argument and classical complete-intersection genus formula are used at A_cut>C_cut>0. The seed's prime11 obstruction proves infinite order. The chord/tangent identity proves all positive odd multiples remain in the required squareclass triple, with infinity, torsion and vertical exceptions excluded. The c=1 discriminant difference forces G|D; minimality of the common denominator gives actual sixteen-root gcd G=1. Recovery of 29D and d proves injectivity for positive odd multipliers. The p/q denominator valuation argument retains its v2(p)>=3 factor of two and does not label artificial parity inputs curve points. Fixed-core zero-column sign candidates are exhausted and all n>=3 odd points avoid the sole d=3 boundary; no all-core classification follows.

The explicit commuting bridge distinguishes diagonal xi from square-cover u=D^2; even the seed gives xi=194089 and u=11025. It preserves the correctly typed full signed degree-four cover, positive-d two-lift slice at a fixed signed point, and unique all-positive display using |v|. The original off-diagonal binding Return correction is essential. Signed ordinate, ordered core/factors, coupling sign, multiplier, sign choices, denominator, actual-root gcd and scale remain in the reconstruction ledger. Unordered within-cell root swaps and declared positive scaling are observer-scoped quotients. Bare unsigned primitive data cannot support arbitrary future elliptic addition; P versus -P already distinguishes adding P. No stronger operation descent is inferred.

## Original Task coverage

| Output | Audit evidence accepted |
|---|---|
| 1: diagonal reduction and primitive filters | AUDIT_PROOF A/B; claims A1,D1,D4; independent rational inverse and actual-root normalization. |
| 2: off-diagonal reduction/family/filters | A/C; O1–O5; all-n squareclasses, true root gcd, explicit domain and fixed-core boundary. |
| 3: universal proof versus finite regression | Written proofs for all universal claims; D2–D4/O3–O5 and exact finite-domain declarations. |
| 4: manifests and proof-to-checker mapping | SOURCE_INPUTS, STATIC_CHECKER_COVERAGE and E1; all exact bindings checked; historical gaps disclosed. |
| 5: primitive and additional quotient horizon | D/I2; retained repair data and explicit failure of unsigned group-law descent. |
| 6: P000 compliance | T1 and native-contract pins; no native-plane or external-to-native promotion. |
| 7: common interface compatibility | D/I1/I2; commuting coordinate bridge and unequal family multiplicities preserved. |
| 8: independent implementation/derivation | Independent Fraction/SymPy program and A–D proofs, author code neither imported nor executed. |
| 9: exact claim matrix/verdict | Fourteen claims with source locations and VERIFIED_COMPATIBLE, not global completion. |
| 10: new immutable Result | RR-29AA6AA5CC2CEBB893CA with all eleven exact outputs; native freeze verified. |

## Method, semantics and next route

Method harvest is RESULT_ONLY. Classical Euclid, strong Fermat descent, Nagell-Lutz, Mazur, Mordell, split-cubic two-division and smooth-(2,2)-genus facts are explicit imported mathematics at checked hypotheses; no new theorem-family novelty or formal-kernel proof is claimed. Existing T0 provenance and T6 operation-safe quotient discipline are REUSE_APPLIED at the declared static interface. This task-specific checker is the original audit requirement, not a new shared tool/capability-gap claim. Prior classical attribution and branch Source references are consumed at their declared bounded scope; no historical priority claim is added.

P000 remains native six-dimensional discrete Cells, with no native plane and separately typed time when needed. Classical curves/triangles remain external arithmetic facades; no native motion, angle, force, Cell identity, Working Truth or Foundation status follows. The global equal-area problem, uniform ranks/generators, all-core zero strata, stronger quotients and native bridges remain residuals.

After native ACCEPTED DR and required DFU are written and independently read back, the original final-integration Task TP2-5E02B5D6961B23083533 has its required positive audit evidence. Bind all three exact accepted RR/DR/DFU sets through the typed authenticated dependency release, verify fresh native claimability and preserve live owners, then let the prepared integrator use its own fresh prepare/claim/open. This review does not itself release the runtime gate or decide final line disposition. No new Task or Selmer branch is created. The parent OBJ-P000-SIX-AXIS-ARITHMETIC-TROPICAL-INTEGRATION remains OPEN.

Driver-ID: EM-DVR-59E7AD / CONTROL_PLANE
