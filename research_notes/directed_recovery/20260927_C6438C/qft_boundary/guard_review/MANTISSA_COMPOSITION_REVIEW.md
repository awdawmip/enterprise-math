# Shared-context review of omission and mantissa composition

Status: SOURCE_SPECIFIC_SYMBOLIC_REVIEW / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

Reviewed `next_design/OMISSION_AND_MANTISSA_COMPOSITION.md`, SHA-256 `5fb6b7f43d3b026c0c31f2b4f74376b689532ac714602981c871ff2e768e7e5c`, in full. No substantive mathematical defect remains within its stated premises.

The direct-sum argument is valid: each public-history block uses the same selected CPTP instrument in the exact and rounded laws, instrument application contracts trace distance, and rounding contributes the approximate child mass times the conditional ray distance. Triangle inequality therefore composes the omission and rounding budgets. The final version explicitly extends selection to every public history and distinguishes an exact-zero block from a positive approximate block. It correctly identifies the current exact sampler's mass-gated `advance` method as insufficient for that total selector; the required adapter is not claimed to exist.

The displayed ray-distance bound follows from orthogonal projection onto the rounded ray and does not confuse ray distance with Euclidean distance between normalized vectors. The common-scale nonzero guarantee, possible one-bit carry, and conservative coordinate-count bound are consistent. The six-coordinate bound remains conditional on the exact invariant coordinate subspace at the selected-child boundary; no assertion transfers it to the other branch's bank or to a mid-instrument representation. Entrywise Gram rounding is explicitly excluded because it need not preserve positivity or consistency with one underlying field.

The source inspection supporting this review included the current uniform selector and its exact-zero admission gate, the exact carrier codec's encode/decode and complete-word restriction checks, and the bounded adaptive checker describing the actual selected-child boundary. The inspected sources were:

| Source | SHA-256 |
| --- | --- |
| `sep27-qft-uniform/uniform_execution/uniform_feedback.py` | `755d398a19881508112c9e360c94bf10133681af8d3cbdbb103accdecc306e28` |
| `sep26-shor-general/optimization/carrier_codec/carrier_codec.py` | `c25149e0ab4ce92a59d2ca40cb697fe6505cd1dc8d406e9c5a2d92cb2b28c953` |
| `sep27-qft-adaptive/adaptive_execution/check_adaptive_feedback.py` | `cd77bc2ff17a6b2938665a622a74c332e7e24cbe362ba359225fc071716510d3` |

## Signed-gap source inspection boundary

`gram_structure/SIGNED_GAPS_REFINEMENT.md` remains frozen at SHA-256 `1a84d09ed1fecdf7a42de9c1b1e48da881c820e544214011703c79a688938776`. Its scalar sign extraction, signed pair-count recurrence, multiple-window normalization, and the one-negative-bit identity `K = 2 J_0 - J_+ - J_-` were checked symbolically. In particular, the final signed coefficient may be negative although each component `J` is a nonnegative count; the raw normalization stays `4^-g`.

For the proposed executable boundary, I read `sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py` (SHA-256 `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`) and its existing checker. The inspected interface includes signed `add/sub/mul`, Euclidean `floor_div`, the degree-three floor-moment path, `window_weight`, and evidence/resource export. This establishes an existing typed path for the three nonnegative weights and their signed external combination. It does not itself execute that new combination, validate a strided adapter, certify an order/address, or connect the observer to a full Gram sampler.

This review performed no scientific arithmetic, no new query, no recovery or replay of the separate RP2 bundle, and no admission. Earlier finite executions remain their authors' source-bound evidence. The reviewed scientific files were not changed.

Global-Knowledge-Sync: main@a462f7a / GLOBAL_KNOWLEDGE_V1
