# Driver Review — Enterprise Helly / Radon Finite-Certificate Tool Discovery

Driver-ID: `EM-DVR-ZX1UEJ`
Date: `2026-08-22`
Task: `RS-TD-HR-ENTERPRISE-HELLY-RADON-CERTIFICATE-CALCULUS`
Owner branch: `research/tool-enterprise-helly-radon-certificates`
Researcher: `EM-TDHR-DDC766`

## Verdict

`ACCEPT_DERIVED_TOOL_WITH_PRIOR_SPECIALIZATION_NOTE`

Frozen tool classification:

`ENTERPRISE_BLOCK_FINITE_CERTIFICATE_CALCULUS_ACCEPTED`

This return clears the taskbook's `NEW THEOREM != NEW TOOL` gate.

## Accepted reusable interface

The accepted core is a block-factorized finite-certificate calculus. For independent blocks with local certificate numbers `h_b`, the global incompatibility certificate number is bounded by

`H = max_b h_b`,

with equality when a sharp local witness is realized. The tool must expose:

- local compatibility predicates;
- global block product assembly;
- bounded obstruction extraction `(bad_block, original constraint indices)`;
- success-witness assembly from nonempty block intersections;
- explicit certificate number / bound;
- a coupling detector that refuses to apply the independent-block theorem outside its premises.

## Prior-specialization boundary

Enterprise Math already contained the special fact that finite axis-aligned integer boxes have Helly number `2`, together with extremal/facet witnesses. That result is therefore **not** new in this task.

What is accepted as new tool structure is the abstraction:

`INDEPENDENT_BLOCK_COMPOSITION -> GLOBAL_CERTIFICATE_NUMBER = MAX_LOCAL_CERTIFICATE_NUMBER`

plus reuse outside integer boxes and the exact negative boundary for coupled relational chains.

The report's Boolean path-chain family is decisive: bounded domain size, bounded local arity, or a path/tree interaction graph alone do **not** force a bounded global certificate number. Minimal obstructions may grow with chain length. Hence the tool is sound only after either block factorization or another certified local-to-global theorem.

## Tool status

- semantic level: `DERIVED_COMBINATORIAL_CERTIFICATE_TOOL`
- Foundation mutation: `NONE`
- prior box-Helly specialization: `ABSORBED_AS_SPECIAL_CASE`
- cross-domain reuse: `PASS` (integer chart feasibility; typed Boolean/BRC consistency)
- bounded-certificate no-go boundary: `PASS`
- reusable witness extractor: `PASS`

## Successor gate

No generic Helly Stage 2 is authorized. Future use should occur inside selected compatibility/gluing problems. A successor theory task requires a concrete coupled class whose certificate number remains unresolved after the accepted block-factorization test.
