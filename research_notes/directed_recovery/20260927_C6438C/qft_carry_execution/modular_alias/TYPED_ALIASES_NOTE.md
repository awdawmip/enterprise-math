# Complete bounded aliases from typed modular columns

This unit implements the modular address-discovery dependency of the published dyadic carry correlation lemma. It discovers every signed displacement in the requested finite interval, including repeated residues. It performs no phase propagation, supplies no order or factors as input, and makes no polynomial input-bit complexity claim.

Status: actual bounded author execution with shared-context review; not independent admission. The current run uses GK policy `06788df022dbd11720132b4ed0882ce8e41b3b8a`, the saved policy readback, and the successful parent `STARTUP_GUARD.json` for activity `RA-CAAAC604CB513AEA8BBC1DFC` at EM `e64ddb8f564c2084aff3f1ea9ea6dbc01451eea0`.

## Interface and completeness

`discover_aliases(program, depth, targets, baby_width)` returns `status`, `aliases`, `short_period`, `evidence`, and `metrics`. For `depth=i>=1`, the multiplier is the existing certified schedule entry `b=program.modular_powers[i-1]`; the corresponding complete-domain permutation certificate is actually replayed. For each requested canonical unit residue `z`, the output is the sorted tuple

`A_i(z) = { d : |d| < 2^i and b^d = z mod N }`.

Duplicate target requests coalesce. At depth zero the only possible displacement is zero: target one gets `(0,)`; every other valid unit target gets `()`. Invalid inputs raise `AliasDiscoveryError` with the available evidence and cost. The phase bank is independent of this alias operation; the verifier binds the modular multiplier/source, not a new claim about phase words.

Put `L=2^i` and `B=baby_width`, with `1<=B<=L`. The baby dictionary stores **every** exponent `u` in `[0,B)`, grouped by the actual residue `b^u`. Repeated labels retain a list rather than a single representative. The positive giant query at block `v` is `z*b^(-vB)`. A dictionary match with exponent `u` therefore gives exactly `d=vB+u`; the explicit range comparison discards the final block's `d>=L` candidates. Every nonnegative `d<L` has a unique such block/exponent decomposition, so the positive search is both sound and complete.

The second search starts from the certified inverse `z^-1`. Its nonnegative magnitude `e` satisfies `b^e=z^-1`, hence gives negative displacement `-e`. Only the second search's zero is discarded, so zero is present exactly once and every negative solution is retained. An actual assertion rejects duplicate signed displacements. Unit targets outside the cyclic subgroup produce an empty list without a discrete-log membership oracle.

`short_period` is the first return to one observed among consecutive baby preparation powers through exponent `B`. When present, it is the exact order of this `b`: every smaller positive exponent was already observed not to return. `None` means that this prefix did not find a return; it does not assert that no period exists. Discovery of a short period does not suppress enumeration or the potentially large output `J`.

## Arithmetic and verification boundary

Residue multiplication, inverses, unit checks, displacement addition, and final-block comparison use the frozen actual typed arithmetic and lazy modular columns. The payload retains inverse/permutation proofs, all computed columns, auxiliary operation traces and native source bindings. Dictionary equality, loop/exponent indices, sign tagging, ordering and certificate hashing are explicitly host wiring. There is no ordinary modular `pow`/remainder reference, ideal Fourier evolution, higher-precision phase calculation, or discarded residual mode.

`verify_alias_result` recomputes the complete discovery and compares the output and scientific evidence, including current source hashes. It ignores only the process-dependent native-kernel cache delta inside otherwise identical replay receipts. JSON integer-key normalization rejects colliding keys before comparison; an integer key and its string spelling cannot shadow an omitted alias. The inherited certificate is saved and its existing hash checked before native replay; legitimate certificates still receive actual typed replay. The API supplies full evidence for the tested rejected requests, but does not claim recovery of arbitrary exceptions or interrupted internal dependency calls.

Let `T` be the number of distinct targets and `G=ceil(L/B)`. Preparation uses `B` forward column requests; each target uses `G` dictionary queries for each sign and at most `2(G-1)` giant-column requests, plus paid inverse/setup and unit tests. Matched exponents, including discarded candidates, and every output alias are separately counted. Host dictionary/routing, exact bit operations, proof construction, certificate replay and output storage remain additional costs. Choosing a square-root-sized `B` does not eliminate target count, output `J`, the bit cost, or certificate storage. In small-order cases `J` can itself be exponential in depth.

Per discovery the metrics separate setup digit replays, computed-column digit replays, actual permutation-verification digit replays (including the inherited table), and auxiliary arithmetic digit replays. A fresh local factory prevents inherited column caches from concealing discovery work. The global checker also retains program setup, independent reference tables, replay work and all actual native call receipts. The per-discovery counters alone are not the total cost of the checker or an integrated simulator.

## Bounded execution

The checker constructs actual full-61-dimensional `LazyStreamingProgram` fixtures `(N,a,t)=(21,2,4)` and `(65,3,4)` with the existing direct-word bank. It compares all requested aliases against independent consecutive forward/inverse **typed** column enumeration for depths zero through four, plus width-eight depth-three cases that force repeated baby labels. These are finite same-arithmetic comparisons, not an independent scientific oracle.

All **12 cases** match completely. The positive data include negative displacements, identity and nonidentity subgroup targets, units outside the subgroup, duplicate target requests, repeated baby labels, zero deduplication and an actual final-block out-of-range rejection (N21, depth four, B3). The repeated-label cases discover periods three and six from their actual return traces. One full result receives complete typed replay.

All **12 negative controls** reject: invalid depths/types/widths, out-of-domain or nonunit targets, schedule/table mismatch, a changed inverse certificate, an omitted alias and the mixed integer/string-key shadowing attack. The nonunit case retains the failed typed gcd trace; the mixed-key attempt is stored as explicit typed key entries because ordinary JSON maps cannot represent that attempt faithfully.

The final run records **244 actual native core calls** and 3.438359299907461 seconds on this machine. This bounded wall-clock observation includes warm implementation caches and is not a comparative speedup claim.

Frozen bindings:

| Item | SHA-256 |
|---|---|
| `typed_aliases.py` | `da19ef459e722ccf03326c77e4e67bd2597c7c5c3deb9fde75879f2cef79bfa1` |
| `check_typed_aliases.py` | `0ceebafccd4cc5da6468218b3bca65dcd8a2795a1928a5920e4f71f20640f5c9` |
| Frozen `lazy_modular.py` | `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4` |
| `TYPED_ALIASES_RESULTS.json.gz` | `bb6c6b0cd9ec678ac0239bc318e735ecb5b4ee011b133ad584a0b44260d52c07` |
| Decompressed complete payload | `0f4b8618ca2cf7a8ebdfe37cc7a56e48ae857a25d4eb992b28b573653ed305c4` |

The gzip is 276,710 bytes; its complete payload is 4,597,609 bytes. `TYPED_ALIASES_SUMMARY.json` carries the detailed per-case resource counts; the gzip carries all evidence. No new phase propagation was run.

An initial serialization-only failure is honestly recorded in `INITIAL_SERIALIZATION_FAILURE.json`. The subsequent pre-hardening successful run, its exact scripts and complete evidence are retained under `prior_validation_run/` and are **superseded** by the final bindings above. They are historical records, not the recommended importer or current evidence.

## Next use

Consume only `COMPLETE` discovery records, bind them to the same program multiplier, and pass the complete signed displacement tuple to the two-carry matrix contraction. The immediate integration question is whether its exact aggregate agrees with the existing native Gram query for fixed histories. Neither this module nor its finite checks establish a low-cost alias mechanism at arbitrary depth; paid period aggregation is a separate route with additional certified inputs.
