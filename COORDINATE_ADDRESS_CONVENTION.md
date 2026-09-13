# Enterprise Math coordinate and address convention

Status: ACTIVE / DIRECT USER COORDINATE CONSTRAINT / ADDRESS INTERFACE V1
Effective: 2026-09-13
Machine authority: `coordinate_address_contract.json`.

## 1. Required final representation

Every final, public or persisted **Cell address** uses six nonnegative integer
fields, a declared codec/version and an unambiguous fixed chart or namespace.
Calling a value a coordinate does not exempt an address from this contract.
The output is a valid codec image, not an assertion that every natural six-tuple
is a legal native Cell. Six fields do not define extra spatial dimensions.

Do not introduce twelve positive/negative address slots by default. A decrease,
an inverse operation, and a negative internal difference are distinct from a
negative final address field. Inactive fields may be zero only when the codec
proves that full identity remains recoverable. Unknown, omitted, projected or
unobserved data must never be silently replaced by zero.

## 2. References and the several meanings of zero

The display origin and display axis lines are reference objects, not Cells,
path vertices, transition operands, or physical source states. A display origin
may be placed in a gap and its lines need not pass through Cell centers.
No auxiliary physical dimension, metric source or origin-to-Cell edge is implied.

The old raw-chart-zero Cell remains present. Zero displacement, an empty path,
and scalar zero remain legal in their respective types. The existing signed
integer charts and their algebra are retained as internal mathematical carriers,
not exported directly as final Cell addresses. A raw Cell anchor is not forced
to coincide with the display origin. A layer number is a replaceable observer,
not a unique Cell identity or automatically a radial distance.

## 3. Boundary transitions

Crossing a display boundary does not impose an increment. Equal-value transfer
is allowed when the declared transition table supports it. Neither `+1` nor a
pure field permutation is a universal crossing law.

For recharting the same Cell, require `D_new(T(a))=D_old(a)`. For actual motion F,
require `D_new(K(a))=F(D_old(a))`. Preserve physical edge identity, order, ports,
branch multiplicity and weights. Do not add an edge for a chart change, or erase
an actual edge because a displayed value stays equal. Finite boundaries, initial
states, caches and update ordering must be transported explicitly.

## 4. Operational and formal scope

The implemented codec `three_region_slice_v1` covers one **fixed two-generator
slice**, with displayed forms `(0,b,c,0,0,0)`, `(a,0,c,0,0,0)`, `(a,b,0,0,0,0)`;
active entries are positive. Its regions are recovered from the unique inactive
field. The all-zero six-tuple is invalid for this codec. The three previously
proved decode maps are unchanged. `EnterpriseMath/CellAddress/ThreeRegionSlice.lean`
is the exact kernel-checked proof, SHA256
`2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02`.

This is not a codec for arbitrary full X6 states. The universal nonnegative
address requirement is active, while other codecs require their own complete
valid domain, identity/transition proof and registry entry. Unknown codecs or
out-of-slice inputs must fail closed. No hidden component or common depth may be
dropped to make an unsupported input appear valid.

The public Python type `FinalCellAddress` is not an integer sequence. The
JSON schema is `schemas/cell_address.schema.json`; the executable validator is
`python tools/validate_cell_address.py`. Runtime additionally rejects bool,
floating-point values, duplicate JSON keys and unknown versions. JSON Schema
accepts mathematical integral values such as 1.0; the exact runtime wire grammar
is deliberately stricter. Consumers must preserve large integers exactly.

## 5. Compatibility and precedence

This convention supersedes older **final-address/display-origin** requirements
on all current surfaces. It does not change P000's spatial axioms, native signed
operations, internal raw charts, decoded metric, or historical theorem scopes.
Existing coordinate-zero keys remain compatibility aliases for RAW_CHART_ZERO,
not instructions to put the display origin at a Cell center. Read the raw X6 and
slice definitions for their mathematical content and this contract for final
address publication. Signed examples in proofs remain signed raw/displacement
examples; their signs are not to be deleted or converted mechanically.

Current root summaries that still describe obsolete native-origin/coordinate
rules are rerouted. Historical records, archived generations and explicitly
conditional experiments retain provenance and are not retrospectively rewritten.
This adoption changes interface constraints; it does not claim new physical laws,
full-X6 atlas verification, all-caller migration or mathematical Foundation admission.
