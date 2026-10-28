# D25/LIFT — length-two local-ring opposite-weight gauge classification and the surviving nilpotent joint jet

**Date:** 2026-10-28. **Evidence:** AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. This is a declared **auxiliary coefficient-ring theorem**, not a source-native H0/B0 operator calculation, a theorem about its actual gauge group, or a new claim of priority in classical local-ring representation theory.

## Scope, observer and source boundary

The preceding author-side work on the same Draft PR established opposite-weight orbits and invariant polynomials over a *field*. The original-class p=373 benchmark instead demands a coefficient ring modulo `p^2`, so its nilpotent ideal may retain distinctions destroyed by reduction to a field. The smallest independent unresolved mathematical unit is to classify **two oriented source ports** over an arbitrary finite commutative principal local ring `R` of **length exactly two** and residue field `k=R/m` of cardinality `q`.

Assumptions: `m=(pi)` is the unique maximal ideal, `m^2=0`, `m != 0`, and `m` is one-dimensional over `k`. Then `|m|=q`, `|R|=q^2`. The **declared auxiliary** gauge group is the full unit group `H=R^times` acting

`u·(x,y)=(ux,u^(-1)y)`.

The two source ports, their order, valuations/unit strata and future operations are part of the typed carrier. The BRC interface applied here is exact *joint-observer fiber constancy*: first classify actual `H`-orbits; then identify what the product-only observer `c=xy` erases. No assumption identifies this full unit group with the genuine H0/B0 allowed gauge.

## Theorem — complete orbit classification

Every `H`-orbit contains exactly one of the following kinds of normal-form data:

1. **`x` unit:** `(1,c)` with `c=xy` ranging over all `R`: `q^2` classes.
2. **`x` nonunit and `y` unit:** `(c,1)` with `c=xy` ranging over `m`: `q` classes.
3. **`x,y` both in `m`:** three distinct zero-support types `(0,0)`, `(nonzero,0)`, `(0,nonzero)`; and, when both are nonzero, one class for each nonzero tensor `J=x⊗_k y in m⊗_k m` (a one-dimensional `k`-space): `3+(q−1)=q+2` classes.

The tensor `J` is **intrinsic** and gauge invariant because the unit action on `m` factors through `bar u in k^times`, and `(bar u x)⊗(bar u^(-1)y)=x⊗y`. The two zero-support flags are needed when `J=0`.

Consequently the number of full-unit opposite-weight orbits is

\[
\boxed{N_R=q^2+2q+2.}
\]

### Complete proof

If `x` is a unit, use `u=x^(-1)` to send `(x,y)` to `(1,xy)`. Two such normal forms are equivalent only if their products agree. If `x` is nonunit while `y` is a unit, use `u=y` to send the pair to `(xy,1)`; here `xy∈m`. These strata cannot mix with one another, or with the last, because multiplication by a unit preserves the unit/nonunit status of each port.

For `x,y∈m`, the `H`-action factors through the surjective reduction `R^times→k^times`. (Every nonzero residue class lifts to a unit.) Multiplication on `m` is canonical scalar multiplication over `k` because `m^2=0`; as an `k`-space `m` has dimension one. Hence the induced action is `(x,y)→(a x,a^(-1)y)` for `a∈k^times`. It preserves which port is zero. All nonzero elements on a single axis are transitively related; the origin is fixed. For two nonzero ports, equality of `x⊗y` and `x'⊗y'` implies the unique scalar `a∈k^times` with `x'=a x` also satisfies `y'=a^(-1)y` (use the isomorphism `m≅k` given by any nonzero basis vector). Such an `a` lifts to a unit of `R`, proving equivalence. Every nonzero tensor occurs, giving exactly `q−1` double-nonzero classes and the claimed count. `QED`.

**Normal-form observer:** `c=xy` together with the unit-status flags and, on the double-nonunit stratum, the intrinsic tensor `J` plus zero-support flags completely separates orbits. The model does not claim these are global polynomial generators for `R[x,y]^H`.

## Sharp product/valuation failure and minimum repair

Let `q>2` and choose distinct `1,lambda in k^times`. With a chosen generator `pi` of `m` and a unit lift `lambda_tilde`, compare

`(x,y)=(pi,pi)` and `(x',y')=(pi,lambda_tilde*pi)`.

Both pairs have exactly the same (nonzero) ideal/valuation types `(m\{0},m\{0})` and the same product `c=0` because `m^2=0`. But their tensors are distinct: `pi⊗pi` and `lambda·(pi⊗pi)`. Thus no full-unit gauge relates them. This is a concrete two-port **first nilpotent joint-jet** information-loss witness. Product plus valuations alone is insufficient, even for maximal allowed unit gauge; a smaller actual gauge group cannot erase this distinction.

For `R=Z/p^2Z` with `pi=p`, write `x=p a, y=p b` on the double-nonunit stratum. The repaired scalar is

\[
\boxed{j=(a\bmod p)(b\bmod p)\in\mathbb F_p,}
\]

with the oriented zero-support flags. The formula `xy mod p^2=0` hides `j` completely. Example at `p=3`: `(3,3)` and `(3,6)` have equal product zero and equal valuations, but `j=1` versus `j=2`. Their full-unit orbits are distinct.

This repair is **minimal as a classifying datum on the double-nonzero stratum** in the sense that there are exactly `q−1` inequivalent states there, indexed by `J∈(m⊗_k m)\{0}`. It is not a claim about minimal bit length or polynomial degree over the whole ring.

## Coefficient-ring bridge at p=373 (conditional auxiliary application)

At `p=373`, `2` is a quadratic nonsquare modulo `p` because `p≡5 (mod8)`. Thus

`R=(Z/373^2 Z)[T]/(T^2−2)`

is an unramified quadratic **local** ring of length two, with `m=373R`, residue `k=F_(373^2)` and `q=139129`. Under the *declared full-unit opposite-weight gauge*, the exact count is

\[
\boxed{N_R=139129^2+2\cdot139129+2=19,357,156,901.}
\]

In this same ring, `(373,373)` and `(373,746)` have identical modulo-`373^2` products (zero) and equal port valuations, but their intrinsic first-jet scalars are respectively `1` and `2` in `F_(373^2)`. They are therefore **not** gauge equivalent, even under all units `R^times`.

These are exact consequences of the *coefficient ring and stipulated auxiliary group*. They are **not** 19,357,156,901 native H0/B0 states or a native `Delta_p−R_p` result: the original class module, actual Frobenius action, allowed gauge group, signed source ports and true observer must be furnished by its authorized owner (existing support Issue #1559). In particular `Z/373^2` and `F_(373^2)` are different rings; this local-ring result deliberately keeps the nilpotent ideal absent from the previous finite-field computations.

## Exact checks performed

`d25_length2_local_ring_gauge_checker_20261028.py` was executed with only the Python standard library. It enumerates **every ordered pair** and **every full-unit gauge action** for `Z/9`, `Z/25`, `Z/49`, `Z/121` and `(Z/9)[T]/(T²−2)`. It independently recomputes the complete orbit invariant on each action, verifies all claimed class counts, class sizes, and strata. Exact coverage: **24,309 source pairs and 2,196,730 gauge actions**, all assertions passed. Direct orbit cardinalities are justified by the action stabilizers, and the checker exhausts each class size. The `p=373` large-ring figure is evaluated by the proven closed formula plus a quadratic-residue test; there was no full `p=373` enumeration.

Output: `d25_length2_local_ring_gauge_author_check_20261028.json` (`overall=PASS`). This is author-side exact falsification and computation, not independent review, Lean formalization or Source native execution.

## Dependency, BRC judgment and next exact scientific step

- BRC method decision: `COMPOSE_APPLIED`. Exact observer `xy` is a safe quotient only for future operations `F` proved constant on every full-unit orbit/fiber appropriate to their use; on the double-nilpotent branch it erases `J=x⊗y`. Preserve `J`, support flags and raw source provenance whenever future signed/odd/jet operations can inspect them.
- Source math dependency: earlier field opposite-weight orbit classification and graded invariant-ring result are reused at their declared scope (Draft PR #1566, pre-unit head `5ddd7ab5e6fe5dbefc1f607dd38b0731e2f02ed1`). This proof **does not** extend the finite-field invariant-ring presentation to a ring with nilpotents.
- Frozen scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`, unchanged. P000 is retained as the project's starting worldview; these auxiliary two-coordinate ports are not a claim of a native 2D plane or X6 slice.
- Next scientific test: obtain the actual original-class H0/B0 `373^2` coefficient module, gauge action on its marked source ports and the precise signed observer via the responsible path in `awdawmip/enterprise-math#1559`. If a two-port subquotient over this `R` is proved to exist, test whether its genuine gauge action is the stipulated opposite-weight subgroup and whether the signed observer is constant on its proposed quotient. A negative match is a valid scoped obstruction. Avoid native-experiment claims without genuine execution.
- Source writer/provenance: author evidence remains `UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`; the Source connection requires a legitimate bound executor and exact claim/continuation/receipt before native checkpoint or Result publication. The separate completed UR portable proof awaits an exact 94,687-byte original V2 four-file bundle matching SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` and lawful writer/provenance. This unit does not redo UR mathematics.
