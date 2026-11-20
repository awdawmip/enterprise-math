# Fixed-slice Cell wire grammar: exact large-integer roundtrip obstruction

Task: `RS-COORD-RUNTIME-REFINEMENT-20260916`. Evidence class: scoped implementation counterexample; not a Lean theorem, full-language refinement or an independent Driver review.

## Frozen contracts, already proved scope, and missing obligation

Frozen Task inputs: `awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa`. The immutable V2 publication `TP2-CFD55C729DF6DA3A0793` pins the taskbook blob `8a8b569839e4a4988171240faae8c6fbacb50d9d`. The prior Lean fixed two-generator slice codec and runtime finite tests already exist and are retained verbatim. Its registered legal address image contains `(0,b,c,0,0,0)` for every pair of positive mathematical integers `b,c`, with no declared fixed decimal digit bound in the contract. `FINAL_CELL_ADDRESS` promises exact nonnegative integer fields; the grammar/serializer roundtrip and trust boundary remain unresolved in this task.

The current `src/enterprise_math/cell_address.py` imports standard Python `json` and uses `json.loads(..., parse_float=reject_float,parse_constant=reject_float)` without an explicit `parse_int`; its `FinalCellAddress.to_json()` uses `json.dumps(self.to_wire(),...)`. The `_cell_slice_codec.py` decoder itself permits exact arbitrary Python ints in the specified legal shapes. Lean `Nat` constructors have no decimal digit cap.

## Concrete reproducible obstruction

On locally observed CPython **3.13.5**, `sys.get_int_max_str_digits() == 4300` (interpreter default). Set `L=4300`, `b=10**L`, `c=1`. The valid registered final address is `(0,b,1,0,0,0)`. Python can construct `b` as a mathematical integer and the exact slice decoder accepts this shape; the wire JSON decimal representation of `b` contains **4301 digits**.

1. Parsing the otherwise valid wire object with the existing default `json.loads` integer parser raises `ValueError: Exceeds the limit (4300 digits) for integer string conversion`.
2. Serializing an in-memory legal address through standard `json.dumps` likewise raises `ValueError: Exceeds the limit (4300 digits) for integer string conversion`.

Both were directly reproduced with standard `json` on local CPython 3.13.5; project wrapper behavior here follows source inspection rather than import/execution of the repository package. The cap is interpreter-configuration-dependent, not a universal bound of mathematical integer semantics. The finite original test `2**512` uses only about 155 decimal digits and cannot detect this boundary.

Thus the previously proven Lean `digits`/codec bijection does not automatically establish a total JSON parser/serializer correspondence for all legal mathematical addresses in the declared scope. This is a specific implementation-level counterexample, not a refutation of the native codec, the already-proved symbolic slice equalities or the BRC path-preservation claims.

## Repair alternatives and acceptance

Either explicitly version/declare a maximum input decimal digit count and prove/check that restricted domain across schema, runtime, serializer and Lean-facing interface (a contract change requiring relevant owner agreement); **or** implement genuinely exact arbitrary-precision decimal JSON integer parse and format paths under declared realistic resource budgets, without global `sys.set_int_max_str_digits(0)` process mutation. For the latter, the parser can use bounded-width digit chunks and positional arithmetic rather than the interpreter's decimal-to-int conversion; encoding can use chunked arithmetic with zero-padded chunks. Both sides must retain duplicate-key, float, bool, version/frame and malformed-number rejection and exact input/output equality.

Next acceptance work: run the companion exact regression checker against a checkout of the pinned code, inspect JSON Schema vs runtime integer lexeme semantics, then complete all constructor and transition branches from `ThreeRegionSlice.lean` to the Python direct `code_step` table. Existing finite tests and Lean proofs are reusable; do not claim they independently establish Python interpreter correctness.

## Original single-file demonstration

```python
import json,sys
L=sys.get_int_max_str_digits()
assert L > 0, "This counterexample requires CPython's active digit limit"
b=10**L
wire='{"schema":"EM_CELL_ADDRESS_V1","codec":"three_region_slice_v1","version":1,"frame":"X6_FIXED_E1_E2_CHART","coordinates":[0,' + "1" + "0"*L + ',1,0,0,0]}'
assert len("1"+"0"*L)==L+1
for name, action in [
    ("wire parse", lambda: json.loads(wire)),
    ("wire emit", lambda: json.dumps({"coordinates":[0,b,1,0,0,0]})),
]:
    try: action()
    except ValueError as exc: print(name,"EXPECTED_BOUNDARY",str(exc)[:120])
    else: raise AssertionError(name+" unexpectedly succeeded under active limit")
```

Status: COUNTEREXAMPLE_OBSERVED_LOCALLY, REPO_WRAPPER_PENDING_AUTHORIZED_SOURCE_EXECUTION, FORMAL_PROOF_NOT_CLAIMED.
