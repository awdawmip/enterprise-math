# 进取路径值平方根算子

Status: `ACTIVE / CANONICAL / FROZEN`
Date: `2026-08-21`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Canonical acceptance source:

`driver_reviews/R063_STAGE0_PATH_VALUED_SQRT_2500_DRIVER_REVIEW_20260821.md`

## 1. Scope

This definition freezes the algebraic path-valued square-root construction for square native norms

`N=r^2`, `r in N`.

It does not change the frozen R061 native line/trace/path semantics. It supplies an algebraic discovery operator that constructs the component-root branches before those branches are realized as R061 native traces.

## 2. Sector-local algebraic carrier

Use

`A_E = Z[J]/(J^2+1)`

with norm

`N_E(a+bJ)=a^2+b^2`.

`J` is a sector-local algebraic component marker for the two Enterprise-orthogonal native components. It is not a claim that the carrier drawing has a classical 90-degree geometry.

## 3. Scalar root versus component-root fiber

Ordinary square root returns only

`sqrt(r^2)=r`.

The path-valued construction retains the full ordered nonnegative component-root fiber associated with the same squared native norm.

Define `GRoot_E(r^2)` constructively by either of the two equivalent square-scope routes below.

## 4. C3 scaled-square route

Enumerate factor channels

`r=k(m^2+n^2)`

with `k|r` and canonical component parameters:

- axis channel: `(m,n)=(1,0)` and `k=r`;
- nondegenerate channel: `m>n>0`, `gcd(m,n)=1`, and opposite parity.

Form

`alpha = k(m+nJ)^2`

so

`alpha = k(m^2-n^2) + 2kmn J`.

Retain both ordered nonnegative orientations when the two components differ.

Then

`GRoot_E(r^2) = { ordered (a,b)>=0 : a^2+b^2=r^2 }`.

Freeze:

`C3_SCALED_SQUARE_LIFT_COMPLETE_FOR_SQUARE_NATIVE_NORMS = true`.

The unscaled special case `N_E(beta)=r -> beta^2` is not complete in general.

## 5. C4 Gaussian factorization route

Alternatively factor `r^2` in `Z[J]`:

- prime `2` ramifies through `1+J`;
- primes `q=3 mod 4` remain inert and require even norm exponent;
- primes `p=1 mod 4` split as `pi_p * conjugate(pi_p)` and their norm exponents are distributed across the conjugate pair;
- multiply by Gaussian units and retain the ordered nonnegative sector representatives.

For the validated square scope this produces exactly the same `GRoot_E(r^2)` as C3.

Freeze:

`C3_ROOT_SET = C4_ROOT_SET` for the frozen square-native-norm theorem.

## 6. Pathification

For each component root `(a,b)` define

`Lambda(a,b)=[u^a v^b](uX_i+vX_j)^(a+b)`

with commuting scalar markers `u,v` and noncommuting native path generators `X_i,X_j`.

`Lambda(a,b)` is exactly the formal family of all words containing `a` copies of `X_i` and `b` copies of `X_j`.

Cardinality:

`|Lambda(a,b)|=binom(a+b,a)`.

After attaching the frozen typed start incidence `Sigma_O^(ij)`, the branch realizes the native component trace

`T_{a,b}^{(ij)}=[X_i^aX_j^b]`.

## 7. Path-valued square root

Freeze:

`PathSqrt_E(r^2)=disjoint_union_{(a,b) in GRoot_E(r^2)} Lambda(a,b)`.

This is a fiber-valued algebraic square-root operator, not a replacement for the scalar identity `sqrt(r^2)=r`.

It refines the scalar root by retaining every algebraically discovered native component branch and then the full native multipath fiber inside each branch.

Native branch length remains

`sqrt(a^2+b^2)=r`.

`a+b` is only path-letter count and is not native length.

## 8. Canonical N=2500 discovery

For

`N=2500`, `r=50`,

freeze

`GRoot_E(2500)={(0,50),(14,48),(30,40),(40,30),(48,14),(50,0)}`.

The two nondegenerate unordered component shapes are

`{14,48}` and `{30,40}`.

Canonical scaled-square discovery channels include

`50=2(4^2+3^2)`

which gives

`2(4+3J)^2 = 14+48J`,

and

`50=10(2^2+1^2)`

which gives

`10(2+J)^2 = 30+40J`.

Thus `sqrt(2500)=50` contains more than one nondegenerate algebraic path direction.

## 9. N=2500 path cardinalities

In one fixed native right sector:

- `(0,50)` -> `1` path;
- `(14,48)` -> `29,078,984,349,975` paths;
- `(30,40)` -> `55,347,740,058,143,507,128` paths;
- `(40,30)` -> `55,347,740,058,143,507,128` paths;
- `(48,14)` -> `29,078,984,349,975` paths;
- `(50,0)` -> `1` path.

Total:

`110,695,538,274,255,714,208`.

Astronomical fibers are represented by exact coefficient-extraction formulas, binomial cardinalities and deterministic combinadic rank/unrank certificates rather than explicit word expansion.

## 10. Derivation provenance versus native path multiplicity

A component root can be produced by more than one algebraic derivation channel before canonicalization.

This algebraic derivation multiplicity is not the native path multiplicity of the resulting trace.

Freeze:

`ALGEBRAIC_ROOT_DERIVATION_MULTIPLICITY != NATIVE_PATH_MULTIPLICITY`.

Return policy:

`DEDUP_COMPONENT_ROOT_AND_TRACE; RETAIN_DERIVATION_PROVENANCE_AS_HIGHER_ENRICHMENT`.

## 11. BRC boundary

BRC is downstream only.

After a path fiber is constructed, the frozen R062 bridge may project

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

BRC is not an input to root discovery and cannot reconstruct roots from Boolean support.

## 12. Reproducibility

The R063 deterministic checker separates discovery and brute verification.

Frozen discovery SHA256:

`6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d`.

General square regression:

`1<=r<=512` with C3 mismatch count `0` and C4 mismatch count `0`.

Regression SHA256:

`51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae`.

## 13. Open boundary

The Gaussian factorization route suggests a possible extension to general non-square norm inputs `N`, whenever `N` is representable as a sum of two squares.

That broader `PathNormRoot_E(N)` construction is not frozen here.

Freeze only:

`PATH_VALUED_SQUARE_ROOT_FACTORIZATION_OPERATOR_COMPLETE_FOR_SQUARE_NATIVE_NORMS = true`.

`R063_STAGE0_STATUS = COMPLETE_AND_FROZEN`.
