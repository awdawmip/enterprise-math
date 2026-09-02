# Enterprise Math Exact Arithmetic / BRC Runtime Protocol

Status: `ACTIVE OPERATIONAL / NO DIVISION-COLLAPSE THEOREM CLAIM`  
Effective: `2026-09-02`

## 1. Runtime rule

The native research state may carry division without calculating it:

```text
DIV(a,b)
```

Construction, storage and exact integer-coefficient transport of this node do not materialize a quotient.

Freeze for governed research calculation paths:

```text
DIVISION_MAY_TRAVEL_UNEVALUATED
DIVISION_EVALUATION_REQUIRES_BRC
FLOAT_IS_READOUT_NOT_NATIVE_STATE
BIGINT_IS_THE_DEFAULT_HIGH_PRECISION_CARRIER
```

This protocol is operational infrastructure. It does not prove that division is a canonical BRC theorem, does not alter the existing Lean-checked Boolean-support BRC theorem family, and does not promote a new Foundation axiom.

## 2. What counts as division evaluation

BRC evaluation is mandatory when code requests any quotient-derived materialization, including:

- integer quotient;
- remainder;
- divisibility;
- same-state-space multiple collapse;
- floor/truncation/rounding based on division;
- finite-precision digits;
- decimal or other radix readout;
- replacement of a carried `DIV` node by a calculated numerical value.

The minimum BRC trace contains:

```text
numerator
denominator
quotient
remainder
collapsed_numerator = denominator * quotient
evaluation_kind = BRC_DIVISION_EVALUATION
```

The exact reconstruction check is

```text
numerator = collapsed_numerator + remainder.
```

The current executable facade reuses P007 quotient/remainder and multiple-collapse primitives. This is tool composition, not a new proof.

## 3. Operations that may keep division unevaluated

The following do not require quotient materialization:

- carrying `DIV(a,b)` unchanged;
- exact addition by cross multiplication;
- exact multiplication of numerator/denominator carriers;
- exact equality or ordering by cross multiplication;
- attaching provenance, scale, unit or precision metadata.

Automatic gcd reduction is deliberately not part of the default carrier. `DIV(2,4)` and `DIV(1,2)` may be value-equivalent while remaining distinct structural states.

## 4. High precision

High precision increases integer scale; it does not introduce a floating native state.

For a decimal readout with `k` digits:

```text
scale = 10**k
scaled_division = DIV(scale * numerator, denominator)
BRC_EVAL(scaled_division)
```

`scale`, `scale*numerator`, quotient, remainder and collapsed numerator are arbitrary-precision integers. In Python the reference carrier is `int`; in Lean the corresponding exact carriers are `Nat`/`Int`.

There is no mathematical digit ceiling in this protocol. Memory/time limits are implementation limits and must not be silently converted into lower precision.

## 5. Decimal text is downstream readout

After BRC has produced the scaled integer quotient, decimal punctuation may be inserted by text formatting. That text is not the native state.

For example, at twelve decimal places:

```text
DIV(1,3)
scale = 10**12
BRC_EVAL(DIV(10**12,3))
-> quotient = 333333333333
-> remainder = 1
readout -> "0.333333333333"
```

The explicit residual remains part of the evidence. The readout must not be represented as if it were the exact native value.

## 6. Static gate

Use:

```text
python tools/check_exact_arithmetic_policy.py <new-or-modified-governed-paths...>
```

The gate rejects native `/`, direct `//`, direct `%`, float literals, direct `float`, `Decimal`, `Fraction`, `divmod`, and direct calls to P007 quotient helpers outside the BRC facade.

The checker is intentionally migration-scoped: supply new or materially modified research calculation paths. Historical code is not mass-reclassified by this first operational rollout.

## 7. Reference implementation

- policy: `exact_arithmetic_runtime_policy.json`
- facade: `src/enterprise_math/exact_arithmetic.py`
- static gate: `tools/check_exact_arithmetic_policy.py`
- regression: `tests/test_exact_arithmetic_brc_runtime.py`
- dedicated CI: `.github/workflows/exact-arithmetic-runtime.yml`

Operational tool reuse classification:

```text
T0_BRC + T5_PRECISION_REFINEMENT + P007_DISCRETE_DIVISION
-> EXTEND_EXISTING_TOOL / operational facade
```

The first rollout deliberately does not attempt a proof of division collapse or multiplicity-aware BRC.
