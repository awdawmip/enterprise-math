# Endpoint identities and implementation review

Status: shared-context author review of the separate root derivation and a static source audit. The two new Python files have been compiled only; they have not been imported or executed for scientific arithmetic. No new provider query, native activity mutation, or remote publication was performed here. This is not formal independent admission.

The exact reviewed derivation is `../ENDPOINT_IDENTITIES.md`, SHA-256 `e43e061fa0e04022daeb14aa30d9956ebe5ba9365b2aaa9c569d762a29e912c0`. No substantive mathematical defect was found.

## Set identity and all endpoint boundaries

For `L=2^g`, write `A={x in [0,L): bit_k(x)=0}` and `B=A+2^k`. Translation gives the same modular-difference count `J` on `A x A` and on `B x B`. The cross-block count is `T(L,R,r)-2J`; its sign is negative. Consequently the exact signed count is `K=4J-T(L,R,r)` for every positive counting modulus, with no assumption that it is a certified multiplicative order.

For the highest bit, `A=[0,L/2)`. Thus `J=T(L/2,R,r)` with the original, canonical residue. This is valid for odd or even `R`, whether or not `R` divides the interval length.

For the lowest bit, the sign of a pair is `(-1)^(x+y)=(-1)^(y-x)`. If `R` is even, all differences in the fixed residue class have parity `r`, so multiplication of the entire unsigned count by `(-1)^r` is exact. Negative values cannot be clipped.

If `R` is odd, write the zero-bit pairs as `(2a,2b)` in an interval of length `H=L/2`. The map `d -> 2d mod R` is bijective. For even `r`, the representative is `r/2`; for odd `r`, it is `(r+R)/2`. The latter numerator is even and lies strictly below `2R`, so both cases produce a representative in `[0,R)`. This proves both directions of the transformed constraint; it is not merely a necessary filter. The low odd-modulus formula follows by substituting this `J` in the four-block identity.

At `R=1`, the only residue is zero, both interval counts are squares of their interval lengths, and both endpoint formulas give zero. There is no request for an inverse modulo one. At `g=1`, the two endpoint descriptions have the identical zero-bit set `{0}`; therefore they agree for every `R`. Highest-bit priority is a valid implementation choice. The raw matrix-correlation normalization remains `4^(-g)` (denominator exponent `2g`); no count is normalized by the number of selected pairs or by `J`.

## New implementation contract

`endpoint_signed_gap.py` defines `EndpointSignedGapObserver.one_negative(g,k,R,r,stride=1)` and `verify_endpoint_certificate(certificate,replay_capture=...)`. Inputs are exact non-Boolean integers in the frozen range contract. The new schema is `BRC_ENDPOINT_SIGNED_GAP_V1`.

Highest-bit selection is tested first. Both interval lengths are built with the inherited actual typed doubling routine. In the low-bit cases, modulus parity and residue parity are actual `floor_div(...,2)` results. The odd-residue numerator and its division by two are typed; the even-residue quotient is reused from that same recorded division. The even-modulus sign is produced as actual signed arithmetic `1-2*parity`, followed by signed multiplication of the count. Host decisions only choose the finite branch, route already produced labels, validate ranges, or record resource metadata.

Interior requests call the frozen `OneWindowSignedGapObserver.one_negative` directly. Its runner is shared with endpoint requests in their original request order; its complete original request is nested in the new record. The inherited request is not represented as a stand-alone old certificate: such a certificate would omit any preceding endpoint operations on this shared runner. Instead the new complete certificate replays every new request in order, reconstructs branch choices, and compares the entire request/operation/moment evidence. Only the inherited nondeterministic native-call delta is excluded from semantic equality. Wrong branch names, extra mathematical fields, altered results, and altered trace positions do not control replay.

Every endpoint interval record includes its inputs, returned integer, and signed-operation range. Complete BRC arithmetic traces and native source pins are retained by the existing runner. Source and proof hashes are checked. These guards do not promise protection against arbitrary in-process Python monkeypatching.

## Declared bounded run, not yet performed

`check_endpoint_signed_gap.py` is limited to the same nine `(g,k,R)` tuples and all their 31 residues. It reads the complete frozen one-window raw payload, verifies both compressed and decompressed hashes, and checks its linkage to the already executed three-window evidence. It does not re-execute that old exhaustive comparator or the old one-window production. The historical input/answer/operation records remain explicitly historical.

Each new case gets one fresh full certificate replay. Eight new tamper cases cover branch selection, odd half-residue, even parity sign, interval value, Boolean input, source, frozen interior request and denominator metadata. Eight range/type/stride rejections must occur before new arithmetic work. The checker preserves current production work, current replay captures, all native call records, and completed cases in a separately named `ENDPOINT_FAILED_EXECUTION.json.gz` on an unexpected failure. Before reading the historical payload or starting arithmetic, it refuses to restart if either success artifact or the failure artifact already exists; exclusive output creation additionally prevents overwriting an artifact that appears later. The failure-artifact startup check was added after root's pre-execution review; it changes no mathematical path.

The 31-record scope covers all four dispatcher branches, highest-bit priority at `g=1`, even-modulus highest and lowest branches, signed negative results, and an interior `R=1` case. Endpoint `R=1` is proved above but is **not** a newly executed endpoint fixture in this declared grid. No branch-completeness claim should silently turn it into such a fixture.

## Costs and limits

Highest and low odd branches make two interval-count calls; the low even branch makes one. They make no floor-window or floor-moment call. Interior requests retain exactly the old one-window arithmetic route. Counts are polynomial-bit integer observations using inherited addition, multiplication and long division; the new interface introduces no order search or state evolution. Powers require a public number of typed doublings, not a host-computed power used as a scientific answer.

Actual production, positive replay and failed replay digit counts must be reported separately after the authorized run. The frozen one-window reference cost is 137,611 production digit replays over these 31 values. A saving in some query families is not a timing result or an overall Shor simulation complexity result. Stride certificates, multiple negative bits, arbitrary free-gap convolution and complete Gram integration remain outside this implementation.

## Exact static sources

- New dispatcher: SHA-256 `c75e7e82cc0ef2413048153716f5100f3a9d1d4f50c375b7cb1690c3cfe6e036`.
- New checker after the failure-artifact startup guard patch: SHA-256 `7b78fe98620531be6fd552887cc00a53d338adbbe9676662d4198fe692ac3d8f`.
- Frozen one-window implementation: `c15e80d580fc8aa52821cb8b0526ada4cd31933cd089bdb1fa1199d1de1ff8b7`; baseline helper: `86ea28956fa7ac9c41fb38a8c63f4ba00b0377f3264b5a525c46c5335faff90a`.
- Frozen typed floor observer: `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`, retained through its unchanged source bindings.
- Historical one-window evidence: compressed `d465513608449d40b081a6ae62acff51f75ef5990f7bc911cec632a5b705e3de`, payload `37ec0d4b7939a70d9157239bfebec7c88a387ff6a2f046a2701f87641d5d78f9`. The original archive member is `signed_gap/ONE_WINDOW_RESULTS.json.gz`; its complete readable chunk representation is pinned by the published readable index at EM `56b191519b036c6890cae328c3b3812fbc1debb7`, prefix `research_notes/directed_recovery/20260927_C6438C/qft_signedgap/`. This is not a claim that the original gzip is stored as a GitHub text file.

The next action is root source review and the new stage's actual startup guard, then the single declared bounded run. Mathematical discussion of the identities can continue in any dialogue without requiring this execution environment.

Global-Knowledge-Sync: main@bd2873d / GLOBAL_KNOWLEDGE_V1
