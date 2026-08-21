# R063 Stage 1 — General Path-Norm Root Driver Review

Status: `ACCEPTED / FROZEN`
Date: `2026-08-21`
Driver: `EM-DVR-R63A21 / CONTROL_PLANE`

## 1. Reviewed payload

Task-ID: `RS-R063-STAGE1-GENERAL-NON-SQUARE-PATH-NORM-ROOT-DISCOVERY`

Taskbook source:

`6a3c104f5e3a46125ccec6d591de6b824cf8dae9`

Owner branch:

`research/r063-stage1-general-path-norm-root`

Frozen owner head:

`65f4e98cd707c634d805f2a9ec7c41f24ab06185`

The owner head is 28 commits ahead of the taskbook source and preserves the frozen R061/R062/R063 Stage 0 definitions read-only. The required Stage 1 result/certificate set and deterministic checker are present on that exact head.

Mandatory discovery snapshot SHA-256:

`941169ca05595ea2282c1771358a62d0384f1c625e8dd64d2cefcfe9ca404ed3`.

General regression rows SHA-256:

`2a5855190e94eaa56e5ad6c730d523b075100a939e53116e2afbab6c49cb1bb2`.

## 2. Driver mathematical verdict

Stage 1 successfully generalizes the Stage 0 factorization-first construction from square inputs to arbitrary positive integer norms.

For positive integer `N`, the integer-addressed component-root fiber

`GRoot_E(N)={(a,b) in N_0^2 : a^2+b^2=N}`

is discovered constructively from integer factorization and arithmetic in `Z[J]/(J^2+1)`, without using brute target-fiber enumeration in the discovery path.

The exact support theorem is:

`GRoot_E(N) != empty`

iff every prime `q == 3 mod 4` occurs in `N` with even exponent.

When supported, Gaussian unique factorization with ramified/inert fixed factors, all split-prime conjugate exponent allocations and units generates the complete signed norm-root fiber; filtering to ordered nonnegative components gives the complete Stage 1 component-root fiber. Unsupported `N` returns the exact empty integer-addressed fiber.

Freeze:

`PATH_NORM_ROOT_OPERATOR_COMPLETE_EXACTLY_ON_SUM_OF_TWO_SQUARES_SUPPORT = true`.

Equivalent scope statement:

`PATH_NORM_ROOT_FACTORIZATION_OPERATOR_COMPLETE_FOR_ALL_POSITIVE_INTEGER_N_WITH_INTEGER_COMPONENT_SUPPORT = true`.

## 3. Pathification verdict

For every discovered root `(a,b)`, Stage 1 lawfully reuses the frozen R061 sector-local trace semantics:

`T_{a,b}^{(ij)}`

and

`Lambda(a,b)=[u^a v^b](uX_i+vX_j)^(a+b)`

with

`|Lambda(a,b)|=binom(a+b,a)`.

The native sector length remains the exact radical `sqrt(N)` and may be irrational. `N=13` is an explicit witness that an irrational scalar length can coexist with a fully discrete integer-addressed trace/path fiber.

Freeze:

`IRRATIONAL_SCALAR_NATIVE_LENGTH_WITH_EXACT_DISCRETE_INTEGER_ADDRESSED_PATH_FIBER = true` on the frozen R061 sector semantics.

## 4. Evidence verdict

Exact exhaustive regression covers every `1<=N<=100000` with zero root-set, support, root-count or path-cardinality mismatch. A deterministic sparse suite reaches `10^9` with zero mismatch. All sixteen Stage 1 acceptance gates pass.

The multiplicative audit also exposes the correct next frontier: signed Gaussian root multiplication is surjective in all 21 audited products from `{2,5,13,17,25,65}`, while multiplicative derivation provenance is not native path multiplicity. The smallest retained separation witness is

`A=B=2`, `AB=4`, component root `(0,2)`:

`4 multiplicative derivation pairs != 1 native path representative`.

## 5. Semantic scope freeze

This review accepts the mathematics at the exact semantic strength actually proved.

Stage 1 is sector-local to the frozen R061 two-active-axis trace/Pythagorean semantics. `Z[J]` is used as a factorization/component algebra for that sector-local construction. This review does not promote Gaussian multiplication to a global full-plane native multiplication law and does not resolve the outstanding authority difference between the project-level undirected-axis formulation and the later three-positive-ray local foundation.

Freeze:

`R063_STAGE1_CLAIM_SCOPE = FROZEN_R061_SECTOR_LOCAL_PYTHAGOREAN_TRACE_SEMANTICS`.

`GLOBAL_FULL_PLANE_MULTIPLICATIVE_STRUCTURE = NOT_CLAIMED`.

This is a scope boundary, not a falsifier of the Stage 1 theorem.

## 6. Final status

`R063_STAGE1_STATUS = COMPLETE_AND_FROZEN`.

The next research generation is authorized to study the multiplicative provenance/component-root/trace/path tower, provided it begins with an explicit semantic claim ledger and does not silently identify algebraic provenance multiplicity with native path multiplicity.
