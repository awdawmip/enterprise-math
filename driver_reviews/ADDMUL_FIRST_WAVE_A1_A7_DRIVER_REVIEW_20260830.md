# ADDMUL First-Wave A1–A7 Driver Review

Driver-ID: `EM-DVR-P8H4Q2`
Parent objective: `OBJ-ADDMUL-BRIDGE-STRUCTURE`
Date: `2026-08-30`

## Disposition

`A1 ACCEPTED / A2 ACCEPTED / A3 ACCEPTED / A4 ACCEPTED / A5 ACCEPTED / A6 ACCEPTED / A7 ACCEPTED`

All seven results are accepted at their exact declared task strength. This review grants no Working Truth, Foundation status, L4 status, canonical promotion, or global-tool promotion. In particular it does not assert that addition and multiplication are globally the same operation.

## Result-by-result audit

### A1 — `RR-8AD9BCE1EB29FFFCB145`
Accept the exact binomial cross-effect calculus: `cr_k Q_k=prod x_i`, in particular `cr_2 Q_2=xy`; lower arities are generally filtered/non-multilinear. Accept the finite-precision filtered correction and exact reuse of existing graded precision at top arity. Preserve the firewall that definability from `(+ ,Q_2)` is not universal primitive elimination. Method harvest: `RESULT_ONLY`.

### A2 — `RR-A09C0A8B7DC0D8291F8D`
Accept `D_2=-xy`; for odd primes accept unique product recovery from `(s=x+y,D_p)` on the semantic image for `s!=0`, with `s=0` the unique infinite product-loss fiber. Accept the p-adic unequal-valuation law, finite-log/Mirimanoff first cancellation residue, and zero raw holonomy because `D_p` is a coboundary. Preserve the non-rational-inverse and no-Foundation boundaries. Method harvest: `RESULT_ONLY`.

### A3 — `RR-DDEA1AE4685D68564D55`
Accept exact associativity of `F_c=x+y+cxy`, shifted multiplicative transport `T_c=1+cx`, exact kernel/fiber and inverse-locus classification, finite nilpotent jet cells, naive-truncation associator obstruction, and the primorial integer-depth criterion. Preserve the distinction between exact shifted multiplication and finite/local formal linearization. Method harvest: `RESULT_ONLY`.

### A4 — `RR-2D4C28F07DE2B14AB18D`
Accept the finite divisor-closed Witt/ghost packet: triangular injectivity, exact integral-image gate, componentwise ghost operations on the valid image, divisor-closed locality, exact p-typical subinterfaces, and irreducible composite-index information. Do not create a second scale/holonomy engine. `WITT_LITE_BRIDGE` remains a thin task-local adapter pending a concrete consumer. Method harvest: `RESULT_ONLY`.

### A5 — `RR-F7153E3A62F1A6511D53`
Accept valuation-vector multiplication, min-plus plus exact cancellation excess for addition, CRT finite-window no-descent, residue-depth precision consumption, and bracket-invariant root excess versus presentation-dependent local ledgers. Preserve `UNIT_DATA_REQUIRED_FOR_OPERATION_SAFETY`; local ledger path dependence is not genuine holonomy. Method harvest: `RESULT_ONLY`.

### A6 — `RR-C9A39F44A8E80B085434`
Accept the zero-completed invertible finite Gauss/Jacobi coordinate bridge, exact codimension-one unit-only image, sparse Jacobi cross-law and zero-resonance defect, together with the obstruction to natural convolution-algebra intertwining. Linear spectral invertibility is not an operation-algebra isomorphism. Method harvest: `CANDIDATE_NOT_TOOL`; no tool promotion.

### A7 — `RR-E6D2C2B7B97E730DE744`
Accept the L1–L5 bridge-strength hierarchy, elementary zero/absorber and congruence no-go lemmas, fiber-aware sum-product pressure test, the cost dimensions `DOMAIN/COLLISION/HIDDEN_COORDINATE/PARTIALITY/ERROR`, and task-local `BRIDGE_AUDIT_PACKET_V1`. Preserve the 2026 correction that the former near-quadratic real sum-product conjecture is false; only proved lower bounds may be used under their exact hypotheses. Reuse existing operation-safe quotient machinery; no new generic tool is accepted.

## Cross-route classification

A1/A2 are exact defect-reconstruction routes; A3 is an exact law-reparametrization route; A4 is an exact hidden-coordinate/image route with an integrality/locality gate; A5 is a deliberately lossy invariant route requiring unit/residue refinement for addition; A6 is an exact typed linear spectral bridge without natural operation intertwining; A7 is the shared negative-control language.

No route currently dominates the others under a single operation-safe cost order. The genuinely new information gap is to compare all accepted routes under one exact strength/information-cost signature and determine which routes compose, which are redundant, and which are irreducibly incomparable.

## Routing

Close A1–A7 individually at task scope. Do not open seven mechanical continuations.

Publish exactly one cross-route Integration task:
`RS-ADDMUL-BRIDGE-INTEGRATION-STRENGTH-COST-ATLAS`.

The Integration task must apply the A7 audit packet to A1–A6, classify law transport, fibers, hidden state, partiality, exceptional loci, precision/refinement cost, pairwise composability, and minimal operation-safe state augmentation. It must reuse current precision, quotient, valuation, holonomy and finite-difference machinery before proposing any new mechanism.

Destination class for all seven reviews: `FOLLOWUP_TASK`, pointing to that single Integration publication.
