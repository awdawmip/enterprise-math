# X6 Unit96 — Signed native Weighted-BRC exact-input boundary and versioned consumer check

**2026-11-17 · AUTHOR-SOURCE-EXECUTED / EXACT-RATIONAL-EXECUTED / UNREVIEWED / NOT_ADMITTED.** Mother goal `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`, Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`.

Scientific pins preserved: P000 signed X6 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, legacy comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, original signed-BRC source Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. The original source was not modified.

## Actual current-source defect, type and witness

`experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, line **62**, contains `wp=tuple(map(Fraction,positive_weights)); wm=tuple(map(Fraction,negative_weights))`. Although the interface declares `Sequence[Fraction|int]`, this eagerly accepts `True`, binary `float`, `str`, and `Decimal` input as positive-rational native signed-path weights. It is an actual **source API input-type boundary inconsistency**, compared with the already-strict `x6_coordinate.brc_endpoint_weight` contract; **no existing downstream consumer passing an invalid value has been demonstrated**.

For one named positive primitive step on axis 0, at signed endpoint `e_0=(1,0,0,0,0,0)`, all negative and remaining positive branch weights 1, the original with `positive_weights[0]=0.1` (binary float) returns

```
Fraction(0.1) = 3602879701896397 / 36028797018963968
Fraction(0.1) - Fraction(1, 10) = 1 / 180143985094819840
```

The literal exact rational `Fraction(1,10)` has the mathematically intended branch weight one tenth. This discrepancy is from *input semantics*; it does not invalidate the exact computation for a genuinely supplied rational `Fraction`. Positive path mass and signed direction labels must remain distinct from signed amplitudes.

## Implemented opt-in source and actual integer/rational execution

An independent version `[signed_brc_strict_v2.py](https://github.com/awdawmip/enterprise-math/blob/aebc38455061d07cee8b441a2fd91ff737dfcae2/experiments/x6_signed_native_spatial_v16_20260905/signed_brc_strict_v2.py)` (Git blob `5b66765c9fb0865684c468d4c93604bd1e9b004b`) retains every original formula and rejects types other than exact `int` or `Fraction` in the 12 branch-weight entries. `bool` is explicitly rejected despite Python's `bool` subclassing `int`. The immutable frozen `signed_brc.py` remains unchanged.

The full actual-source checker `[Unit96 checker](https://github.com/awdawmip/enterprise-math/blob/712143b1f3b66c80217e18e39ec39149c1e57616/research_checks/X6_UNIT96_SIGNED_BRC_EXACT_WEIGHT_INPUT_BOUNDARY_CHECK_20261117.py)` reconstructs the original source by its pinned Git blob and imports both original and versioned modules. Three independent legal positive-rational profiles were accumulated by a direct 12-direction named-step dynamic recurrence and checked against both implementations and their signed endpoint exact formula for every reachable endpoint at lengths 0 through 5.

- Distinct reachable endpoint counts per depth: **1, 12, 73, 304, 985, 2,668**; **4,043** per profile, **12,129** exact endpoint equalities in total.
- Four invalid examples (`True`, `0.1`, `"1/10"`, `Decimal("0.1")`) are accepted by the old coercing interface and rejected by the strict version.
- Independent native signed length-6 zero return: **19,920**; retained from the source kernel and checked.
- Executed CPython normal, `-O`, `-OO` against this same pinned reconstructed source set; stdout bytes identical, SHA256 `e029c1fe55ac3f038dda9e02c197860d99965b4e2825c2774bcfaf0324d00171`.
- `[Machine-readable result](https://github.com/awdawmip/enterprise-math/blob/6450b56d57c047f4808693053fc03cc980823765/research_checks/X6_UNIT96_SIGNED_BRC_EXACT_WEIGHT_INPUT_BOUNDARY_RESULTS_20261117.json)` (blob `d85f17195aeb5355ded14d4350ab35a6aa31b39b`).

The equality proof for valid weights is direct: after preserving and validating 12 exact positive rational inputs, both code paths run the same sum over six nonnegative backtrack counts `k_i` with `sum k_i=(L-||z||_1)/2` and multinomial factorial coefficients. The independent dynamic recurrence checks the asserted interpretation, rather than proving every possible length by finite enumeration.

## Bounded current downstream consumer check (additional same-turn source reading)

Three concrete executable source bodies were read on current `main` after the independent Unit96 test; their observed immutable Git blob identifiers, exact operation and input types are:

| Source / blob | Observed call and input contract | Classification |
|---|---|---|
| `research_checks/X6_LP026_SIGNED_LAURENT_QUOTIENT_CONSUMER_CHECK_20261112_ONHOUR.py` · `e2bc083f1832b8eae2d8887095912da0e0e8984f` | Line 39 `quotient_walks` uses `map(Fraction,wp/wm)`; lines 53–69 independently calculate native weighted paths; lines 140–151 supply only `Fraction`/integer inputs; separate positive-only test deliberately supplies zero negative weights. This is **not** a direct `signed_brc.endpoint_weight` call. | `KEEP_DECLARED_EXACT_INPUTS`; potential permissive coercion at a different test-helper boundary, **no bad real call**; do not impose strict positivity on the separate zero-weight positive-sector model |
| `research_checks/X6_LP019_FCC_SIGNED_BRC_PUSHFORWARD_20261113_ONHOUR.py` · `a82b8cfb6039531aec2266e283a5277ab20f7c4c` | Its `advance_native` and `advance_carrier` propagate nonnegative **integer unweighted** counts for twelve signed steps. No imported `signed_brc.endpoint_weight` or rational input conversion. | `KEEP_TYPED_INTEGER_PUSHFORWARD` |
| `research_checks/X6_LP026_SIGNED_RELATIVE_C6_PARITY_BRC_20261112_ONHOUR.py` · `08d0cd5c2720410d9a938c49df830d90573b408f` | `signed_relative_brc` uses exact factorial integers and sums over native lifts; no rational weight caller. | `KEEP_TYPED_INTEGER_RELATIVE_BRC` |

These are **three bounded full-body source inspections, not executed regressions on their original frozen harnesses and not a repository-wide caller closure**. At present no demonstrated bad downstream call consumes a float, Boolean or string as a signed-BRC branch weight. The concrete repaired interface and the 12,129 exact rational comparisons remain the Unit96 executed increment.

## Source and admission boundary

Existing actual current LP019/LP026 typed signed-path consumers and earlier Unit93–95 strict CoverState tests remain valid, completed and not repeated. The new interface is *opt-in* and changes only input validation, not the original frozen science or original benchmark object. No original R063/Helly benchmark was rerun. No Native Source CLAIM, RUN, PROGRESS, independent Driver review, Result or P000 promotion is claimed.

The existing Source #6994 `recovery_status` returned a D25 service session under the stable Research logical conversation; #6995 returned typed X6 continuation with `execution_authorized=false`. Preserve original X6 SID `MCP-082892eb480e45dea6d4b9fcc0491034`, Researcher `EM-X6-FB6990`, Activity `RA-5E3FE1E761E4963EC461A892`, CLAIM `MCP-579c8e23625448582b421831`, RUN `RUN-fb25028676f9692ab1bacaee` solely as authenticated-history locators, not present owner proof.

## Next minimum scientific action

Inspect a bounded set of **actual downstream callers** of `signed_brc.endpoint_weight`, weighted native/relative operators and any coercion boundary, recording exact caller path/blob/line and argument type. Patch a consumer only when a real wrong call is established. Separately continue the unresolved frozen historical LP011 signed dominant-selector and LP019 cancellation `file:line` provenance and 28-LP type graph, with independent Driver REQUEST_REVISION. Use valid Source continuation and original request IDs for Native execution authority; no borrow from the maintenance lane. The mathematical parent task remains open.
