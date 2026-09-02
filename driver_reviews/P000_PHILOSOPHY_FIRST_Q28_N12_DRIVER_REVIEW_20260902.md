# Driver Review — P000 Philosophy-First Q28 n=12 Return-Profile 1-WL Frontier

Driver: `EM-DVR-VPSKLD`  
Result: `RR-D277A62E967320225132`  
Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N12-COLLISION-FRONTIER`  
Publication: `TP2-C74E704488CBF01A602D`  
Execution: `ER-AED46EF41615532B2F46`  
Claim: `chatgpt-p000q28-reexec-20260902-1920-8c7a2d`

## Disposition

`ACCEPTED AT DECLARED SCOPE`

Accepted terminal class:

`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N12`

Accepted mathematical strength:

`FROZEN_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_EXACT_GRAPH_LEVEL_INJECTIVITY_ON_U_BR_FOR_4_LE_N_LE_12_ONLY`

## Evidence audit

The Q22/Q25/Q27 observable remains unchanged. At `n=12`, handshaking leaves exactly the six degree-3 sectors `r in {2,4,6,8,10,12}`. The accepted re-execution certificate covers the exact normalized connected counts

- `r=2`: `63,504,000`, with `29` representatives;
- `r=4`: `161,965,440`, with `351` representatives;
- `r=6`: `423,705,600`, with `1,373` representatives;
- `r=8`: `1,183,502,880`, with `1,892` representatives;
- `r=10`: `3,561,440,400`, with `835` representatives;
- `r=12`: `11,543,439,600`, with `85` representatives.

Hence the total exact normalized connected count is `16,937,557,920`, covered by `4,565` graph-isomorphism representatives. The current checker recomputes every representative from adjacency, verifies connectivity and degree sector, recomputes the frozen primitive-return profile and ordinary 1-WL packet, recomputes the exact automorphism order, and checks sector-by-sector orbit-stabilizer completeness. The sector orbit sums equal independently computed connected labeled counts exactly.

All `4,565` complete stabilized packet serializations are pairwise distinct, including across sectors. SHA-256 values only pin the already checked packet images; packet equality is not replaced by hash equality. Therefore the accepted bounded conclusion is zero nonisomorphic equal-packet collisions at `n=12`.

## Control-integrity resolution of the withdrawn Q28 execution

The present acceptance binds only to the current authenticated execution:

- Researcher `EM-P000-AED46E`;
- Claim `chatgpt-p000q28-reexec-20260902-1920-8c7a2d`;
- Execution `ER-AED46EF41615532B2F46`;
- Result `RR-D277A62E967320225132`.

The re-execution did not read the surviving prior-Q28 return/checker/artifacts until its own `n=12` count/orbit certificate had frozen. Post-freeze comparison reproduced every one of the six sector counts, the total `4,565` representatives, all six packet-image SHA-256 values, and the combined packet-image SHA-256 exactly.

Accordingly, the prior Q28 withdrawal is classified as a claim/result control-binding defect, not evidence that the bounded `n=12` mathematical conclusion was false. This review nevertheless accepts the mathematics through the new independently rebound Result above, not by restoring authority to the withdrawn execution.

## Discovery versus completeness

The deterministic seeded configuration-model search is accepted only as a countermodel-first discovery route. In particular, the first `r=6` discovery seed left an orbit deficit `32,400 = 6!6!/16`; the second seed found one additional representative of automorphism order `16`, closing that discovery deficit. None of this sampling is used as completeness authority.

Completeness rests on the independent exact connected degree-count recurrence plus the exact automorphism/orbit-stabilizer cover and complete packet separation, matching the proof architecture already accepted in Q27.

## Method harvest / reuse

`RESULT_ONLY / REUSE_APPLIED`

The accepted Q27 primitive-return, ordinary 1-WL packet, exact degree-count recurrence, automorphism backtracking and orbit-stabilizer completeness core are reused. Q28 adds only the `n=12` execution/certificate binding and exact finite census. No new general-purpose observable or project-wide tool family is accepted.

## CI baseline separation

PR #1111 changes exactly the five declared Q28 output files relative to the contemporaneous `main`. Its failing repository-wide checks are not caused by those paths:

1. the post-cutover publication-envelope gate fails on the pre-existing `RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE` publication because four mandatory body sections are absent;
2. the unit-test baseline fails because `tests/test_research_control_p0_v2.py` still imports the physically removed `tools.research_scheduler` module.

These are independent control-plane baseline defects and do not weaken the Q28 mathematical disposition.

## Strength boundary

This review proves no statement for `n>=13`, no universal finite-graph reconstruction theorem, no vertexwise canonical identification, no canonical-label algorithm and no stronger observable. Ordinary 1-WL remains prior mathematics; no historical novelty claim is accepted.

No Working Truth, Foundation status, L4 status, or other mathematical promotion is granted by this review.

## Successor decision

Q28 is terminal at `n=12` by its taskbook. The first possible stable equal-packet nonisomorphic collision is now unresolved beginning at `n=13`. Because the parent objective is still the exact first-failure frontier, `n=13` is the smallest unresolved size, and the accepted Q28 result contains no theorem propagating injectivity beyond twelve Cells, one bounded continuation is justified with the observable frozen bit-for-bit.

Successor task to be separately published:

`RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N13-COLLISION-FRONTIER`

It must stop on the first exact `n=13` collision, an independently complete exact `n=13` collision-free certificate, or an explicitly partial structural-search boundary. It must not continue to `n=14` inside the same task.
