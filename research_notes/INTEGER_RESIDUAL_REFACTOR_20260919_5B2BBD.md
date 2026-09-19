# Integer + typed residual refactor: first verified implementation slice

Status: `IMPLEMENTED_AND_SLICE_TESTED / FULL_MIGRATION_PENDING / NOT_FOUNDATION`
Researcher-ID: `EM-DIRECT-5B2BBD`
Research-Activity-ID: `RA-5B2BBDD75F5F4C299409A74F`
Progress-Event-ID: `integer-residual-refactor-20260919-5B2BBD`
Source: direct user request on 2026-09-19; connector-pinned code; local tests.
Base source: `awdawmip/enterprise-math@c62b1472db2e6ad90e988247f9590e2cf62957e1`.

## Direction and corrected inventory

用户要求将之前的研究和代码彻底重构为“整数加残差”。落实为权威状态、运算、决策和持久化链路的精确化，不是把小数乘一个大数后丢弃尾数。

已核对 core/division/exact_arithmetic 本来就是整数与残差；brc_transport 使用精确 Fraction 而非 float；最新 collision_engine 也是整数模剩余和矩。brc_logarithm 已读前190行明确符号源及有理区间。该定点核对不是全仓浮点审计。保留既有精确实现，不声称旧工作全错，不机械替换 Fraction 或所有 `/`。

## Laws and implementation

For signed n, d>0, S>0:

`n*S=q*d+r`, `0<=r<d`, hence `x=q/S+r/(d*S)`.

Negative q uses floor, not truncation: -1/7 at S=1000 has q=-143,r=1. Positive 1/7 has q=142,r=6. Under S'=kS, `k*r=c*d+r'` gives `q'=k*q+c`. Original unreduced source is preserved. Numeric equality is explicit, separate from structural equality.

For nonnegative x=(n/d)^(1/p): `n*S**p=d*q**p+R`, with `0<=R<d*((q+1)**p-q**p)`. R has polynomial/radicand units, NOT additive root-error units. sqrt(2),S=1000 yields q=1414,R=604. Root floor of floor(n*S**p/d) is valid because candidate p-th powers are integers.

Added `src/enterprise_math/integer_residual.py`: SignedDivisionExpr, IntegerResidual, RationalRootResidual, exact-endpoint RationalEnclosure, and CertifiedOrder with explicit UNRESOLVED. Float/bool/implicit conversion inputs are rejected. Integer wire fields are canonical decimal strings with reconstruction verification. The original three BRC dependencies execute unchanged; this extends their family, not a new calculus.

Structural residuals such as common depth, path labels and weight/action correlations remain separate caller-owned carriers. The scalar does not preserve complete expression DAGs or BRC path provenance. Interval overlap does not prove equality; the endpoint type validates consistency, while producers must justify containment. General analytic evaluation, arbitrary algebraic operations and negative odd roots are not implemented here. Old logarithm truncation requires explicit adaptation, not reinterpretation.

## Executed evidence

15 test methods passed, with 38,371 parameter checks: signed division 18,150; refinement 6,156; rational roots 9,150; random signed arithmetic 2,500; unchanged positive-facade comparisons 1,500; unchanged root-facade comparisons 915. Also tested 4096-bit inputs, source/value distinction, native six-axis common-depth witness, forged-state rejection and 4-file integer-core AST inventory.

Execution command in the delivered standalone package: `python tools/run_local.py`. The runner checks the three original Git blobs/SHA256, then deliberately bypasses the full package initializer and executes the dependency slice. Full repository tests, full package import, production migration, Lean, independent review and controlled performance benchmarks were NOT run. Fraction is used only as an independent arithmetic oracle in the new tests; this is not independent researcher review.

Exact implementation SHA256: `9dbe8caa37410ce97cf062d0253ff829c7b4783224a009b00930e79c57b5f1ef`.
Exact test SHA256: `70d8581bc3eee8def79f1fc8746939abc87ec2cd9cc23079f278eb967ab50ff0`.
Unchanged dependency Git blobs: core `cdb8ace10e4cc8bba13b70f4da306313efb24819`; division `bf0b1a6b6aeccc94578d11509c5bcd12ff930cb5`; exact_arithmetic `35ea95b0916494b83a92386e3e313928362dd79e`.

## Migration acceptance and smallest unfinished unit

Complete current-source callsite inventory; classify float by presentation, heuristic proposal or authoritative predicate; migrate one real normalization/boundary caller; explicitly adapt negative truncation and exact Fraction values; retain source/provenance; replay float-dependent experiments with exact certificates. A new class alone is not completion.

No production caller or existing core function has been replaced. No Nollm deployment or Shor algorithm change. Authority state must not depend on an unmarked lossy float. Presentation-only exports may remain named one-way boundaries; they cannot feed core decisions back. Historical float bits cannot recover an unknown originally intended decimal/fraction.

For each residual specify carrier, reconstruction/containment proof, scale, future-operation lease and refinement. Keep exact source vs value cache distinct. No unproved coalescence of branches, implicit epsilon equality, hidden phase cancellation, or symbolic-size-as-bit-complexity claim. Integer bit growth, denominator growth, unresolved comparisons and runtime remain real costs.

Next executable integration unit: inspect complete current core decision callsites and connect the signed exact state to one normalized-coordinate/boundary path with exact old/new comparison. Preserve the already-exact collision engine. This candidate is neither a formal task CLAIM nor Working Truth/Foundation admission.
