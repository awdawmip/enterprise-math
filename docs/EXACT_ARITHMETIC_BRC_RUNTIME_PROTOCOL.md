# Enterprise Math Exact Arithmetic / BRC Runtime Protocol

Status: `ACTIVE OPERATIONAL / NO DIVISION-OR-ROOT-COLLAPSE THEOREM CLAIM`  
Effective: `2026-09-02`

## 1. Unified runtime rule

Native research states may carry division or roots without calculating them:

```text
DIV(a,b)
ROOT_p(n)
```

Construction, storage and symbolic transport of these nodes do not materialize a quotient or a root value.

Freeze for governed research calculation paths:

```text
DIVISION_MAY_TRAVEL_UNEVALUATED
DIVISION_EVALUATION_REQUIRES_BRC
ROOT_MAY_TRAVEL_UNEVALUATED
ROOT_EVALUATION_REQUIRES_BRC
FLOAT_IS_READOUT_NOT_NATIVE_STATE
BIGINT_IS_THE_DEFAULT_HIGH_PRECISION_CARRIER
```

This protocol is operational infrastructure. It does not prove that division or root extraction is a new canonical BRC theorem, does not alter the existing Lean-checked Boolean-support BRC theorem family, and does not promote a new Foundation axiom.

## 2. Division evaluation

BRC evaluation is mandatory when code requests any quotient-derived materialization, including:

- integer quotient;
- remainder or divisibility;
- same-state-space multiple collapse;
- floor/truncation/rounding based on division;
- finite-precision digits or radix readout;
- replacement of a carried `DIV` node by a calculated value.

Minimum division trace:

```text
numerator
denominator
quotient
remainder
collapsed_numerator = denominator * quotient
evaluation_kind = BRC_DIVISION_EVALUATION
```

The reconstruction identity is:

```text
numerator = collapsed_numerator + remainder.
```

## 3. Root evaluation

For a non-negative integer radicand and positive degree `p`, the native state is:

```text
ROOT_p(n)
```

It may travel unevaluated. BRC evaluation is mandatory when code requests:

- an integer root index;
- perfect-power membership via root calculation;
- a perfect-power collapse state or residual;
- finite-precision root digits/readout;
- replacement of `ROOT_p(n)` by a calculated value.

Minimum root trace:

```text
radicand
degree
root_index
collapsed_radicand = root_index ** degree
remainder = radicand - collapsed_radicand
next_power = (root_index + 1) ** degree
evaluation_kind = BRC_ROOT_EVALUATION
```

The exact basin condition is:

```text
collapsed_radicand <= radicand < next_power
0 <= remainder < next_power - collapsed_radicand
```

This runtime reuses the existing exact integer-root and perfect-power-collapse primitives after the BRC trigger. It is tool composition, not a new proof.

Current root facade scope is non-negative integer radicands. Existing signed-root semantics remain separately typed and are not silently folded into this rollout.

## 4. Symbolic transport before evaluation

Allowed without BRC materialization includes:

- carrying `DIV(a,b)` or `ROOT_p(n)` unchanged;
- storing/transmitting either node;
- exact integer-coefficient rewrites that preserve an explicit division carrier;
- cross multiplication for division equality/order without materializing a quotient;
- attaching provenance, scale, unit, degree or precision metadata;
- retaining a root symbolically inside a larger expression when no root-derived value is requested.

Automatic gcd reduction remains outside the default division carrier. `DIV(2,4)` and `DIV(1,2)` may be value-equivalent while remaining distinct structural states.

## 5. High precision uses big integers

High precision increases integer scale; it does not introduce floating native state.

### Division

For `k` decimal places:

```text
scale = 10**k
BRC_EVAL(DIV(scale * numerator, denominator))
```

### Root

For `ROOT_p(n)` at `k` decimal places:

```text
scale = 10**k
scaled_radicand = n * scale**p
BRC_EVAL(ROOT_p(scaled_radicand))
```

The resulting root index is the scaled integer readout. For example, with `p=2`, it is the integer `q` satisfying:

```text
q**2 <= n * scale**2 < (q + 1)**2
```

All scales, scaled carriers, collapse states and residuals are arbitrary-precision integers. Python uses `int`; Lean uses `Nat`/`Int`.

There is no mathematical digit ceiling in this protocol. Memory/time limits are implementation limits and must not be silently converted into lower precision.

## 6. Decimal text is downstream readout

Decimal punctuation is inserted only after BRC has produced a scaled integer state. The text is not the native exact value.

Examples:

```text
DIV(1,3), 12 digits
-> BRC_DIVISION_EVALUATION on DIV(10**12,3)
-> quotient = 333333333333, remainder = 1
-> readout "0.333333333333"
```

```text
ROOT_2(2), 12 digits
-> BRC_ROOT_EVALUATION on ROOT_2(2 * 10**24)
-> root_index = 1414213562373
-> readout "1.414213562373"
```

The residual collapse coordinate remains explicit evidence.

## 7. Static gate

Use:

```text
python tools/check_exact_arithmetic_policy.py <new-or-modified-governed-paths...>
```

The gate rejects native `/`, direct `//`, direct `%`, float literals, direct `float`, `Decimal`, `Fraction`, `divmod`, direct `sqrt`/`isqrt`, direct P007 quotient helpers, and direct integer-root/perfect-power helpers outside the BRC facade.

The checker is intentionally migration-scoped. Historical code is not mass-reclassified by this rollout.

## 8. Reference implementation

- policy: `exact_arithmetic_runtime_policy.json`
- facade: `src/enterprise_math/exact_arithmetic.py`
- static gate: `tools/check_exact_arithmetic_policy.py`
- regression: `tests/test_exact_arithmetic_brc_runtime.py`
- dedicated CI: `.github/workflows/exact-arithmetic-runtime.yml`

Operational tool reuse classification:

```text
T0_BRC
+ T5_PRECISION_REFINEMENT
+ P007_DISCRETE_DIVISION
+ existing integer-root / perfect-power-collapse core
-> EXTEND_EXISTING_TOOL / operational facade
```

This rollout deliberately does not attempt a proof of division collapse, root collapse, or multiplicity-aware BRC.
