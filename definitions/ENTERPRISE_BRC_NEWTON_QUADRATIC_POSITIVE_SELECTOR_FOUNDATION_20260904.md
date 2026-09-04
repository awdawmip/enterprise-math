# Enterprise Math — BRC Non-Split Quadratic Smallest-Positive Selector Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION CANDIDATE / MAIN-BACKED RESEARCH / OPEN-INTERVAL STURM SELECTOR`
Effective: `2026-09-04`
Parent: `ENTERPRISE_BRC_NEWTON_QUADRATIC_SELECTOR_FOUNDATION_20260904.md`
Evidence: PR #1211

## 1. Scope and prior art

This addendum completes the monic-quadratic non-split selector tier by adding smallest-positive semantics to WBRC-T62.

Quadratic Sturm sequences, sign variation and root counting are classical mathematics. No generic novelty claim is made. The Enterprise/BRC content is the exact typed selector interface:

- the declared Newton root `r>0` remains separately guarded by fixed multiplicity `Q(r)!=0`;
- positive selection is reduced to an exact root count on the **open** interval `(0,r)`;
- a root at zero is harmless because zero is not positive;
- the degree-two interval count has both an exact Sturm-variation form and a radical-free compact chamber form;
- no explicit competing-root materialization is required.

This is not a general parametric Sturm sign-cell enumerator.

## 2. WBRC-T63 — non-split monic-quadratic smallest-positive selector chamber

Fix a declared rational root

`r>0`

with declared multiplicity `m>=1`, and edge representation

`E(y)=(y-r)^m Q(y)`,

where

`Q(y)=y^2+a y+b`

is monic quadratic with rational coefficients.  Fixed declared multiplicity requires

`R:=Q(r)=r^2+a r+b != 0`.

Define

`D=a^2-4b`,
`L=-a-2r`,
`R=r^2+a r+b`.

The declared root r is the smallest positive root of E iff Q has no distinct real root in the open interval `(0,r)`.

### Exact Sturm-variation invariant

A Sturm sequence for Q is, up to positive scalar normalization,

`Q(y), 2y+a, D`.

Let `V` denote sign variation after deleting zero entries. Then the exact number of distinct Q-roots in `(0,r)` is

`N_(0,r)=V(b,a,D)-V(R,2r+a,D)`.

This formula remains valid when `D=0`: the zero terminal Sturm value is simply ignored. It also remains valid when `b=0`: the root at the left endpoint zero is excluded because the interval is open.

Therefore

`r is the smallest positive root`

iff

`r>0`, `R!=0`, and

`V(b,a,D)=V(R,2r+a,D)`.

Canonical ID: `WBRC-T63`.

## 3. Equivalent radical-free chamber

The interval-Sturm condition is equivalent to the following compact rational sign formula:

`R!=0`

and

`b*R>=0`

and

`(b<0 OR R<0 OR D<0 OR a>=0 OR a<=-2r)`.

Equivalently in explicit cases:

- if `D<0`, the selector is safe;
- if `D>=0` and `b<0`, it is safe iff `R<0`;
- if `D>=0` and `b=0`, it is safe iff `a>=0 OR R<0`;
- if `D>=0` and `b>0`, it is safe iff `a>=0 OR (L>0 AND R>0)`.

The identity

`L^2-D=4R`

eliminates the quadratic radical in the last case.

The Sturm-variation form is canonical for future degree extensions; the compact form is the degree-two operational shortcut.

## 4. One-parameter witness

For

`E_t(y)=(y-1)^2(y^2+t y+1)`,

with declared root `r=1`,

`D=t^2-4`,
`R=t+2`,
`L=-t-2`.

Fixed multiplicity fails only at `t=-2` and the smallest-positive selector chamber is exactly

`t>-2`.

The regimes are:

- `-2<t<2`: quadratic competitors are complex;
- `t>=2`: competing real roots are non-positive;
- `t=-2`: the quadratic becomes `(y-1)^2` and declared multiplicity collides;
- `t<-2`: the quadratic has two positive reciprocal roots and the smaller one lies in `(0,1)`.

## 5. Boundary behavior

### Zero endpoint

If `b=0`, Q has a root at zero.  Because zero is not positive, that root must not defeat the selected root. The open-interval Sturm formula handles this exactly.

### Discriminant zero

`D=0` is not automatically a selector boundary. A repeated quadratic root may lie outside `(0,r)` or inside it. The endpoint/interval sign data remain necessary.

### Multiplicity collision

`R=0` is not a selector-order event only; it changes the multiplicity of the declared root and therefore exits the fixed T59 Newton schedule stratum.

## 6. Relation to T62

The exact monic-quadratic non-split selector pair is now:

```text
T62 SMALLEST_REAL
  R!=0 AND [D<0 OR (L>0 AND R>0)]

T63 SMALLEST_POSITIVE
  r>0 AND R!=0 AND N_Q((0,r))=0
  where N_Q((0,r))=V(b,a,D)-V(R,2r+a,D)
```

Both selectors avoid materializing competing quadratic roots.  They are distinct observer semantics and cannot be substituted for each other.

## 7. Affine parameter families

If `a(lambda),b(lambda)` are rational-affine parameter forms and r is fixed rational positive, then:

- D is quadratic in lambda;
- R and L are affine;
- the compact T63 chamber is a finite low-degree semi-algebraic Boolean condition;
- the Sturm-variation representation is an exact sign-cell representation of the same degree-two selector.

No generic sign-cell decomposition algorithm is promoted.

## 8. Hard negative/scope boundaries

```text
SMALLEST_POSITIVE != SMALLEST_REAL
ZERO_ROOT_IS_NOT_POSITIVE
FIXED_SELECTOR_VALUE != FIXED_MULTIPLICITY_AT_R_ZERO
OPEN_INTERVAL_(0,r)_IS_SEMANTIC
MONIC_QUADRATIC_COFACTOR_ONLY
DEGREE_TWO_STURM_VARIATION != GENERAL_PARAMETRIC_STURM_CAD
COMPACT_CHAMBER_IS_A_DEGREE_TWO_SPECIALIZATION
T63 != COMPLETE_PUISEUX_OR_MULTIGENERATOR_SOLVER
```

Canonical negative IDs: `WBRC-N84..N91`.

## 9. Tool routing

T63 extends the existing companion tool

`t0.weighted_brc_newton_quadratic_selector`

and module

`src/enterprise_math/brc_newton_quadratic_selector.py`.

Production code additionally provides:

- exact sign variation with zero deletion;
- exact quadratic root count on `(0,r)` from endpoint Sturm data;
- smallest-positive selector decision;
- compact smallest-positive chamber decision;
- interval/Sturm and compact-form consistency diagnostics;
- affine-family smallest-positive evaluation.

It does not run a generic Sturm sequence on arbitrary polynomial degree at runtime.

## 10. Validation

Main-backed PR #1211 verified:

- 405 rational `(a,b,r)` catalog points with `r>0`;
- 15 fixed-multiplicity collisions;
- 390 exact open-interval Sturm checks;
- 293 stable and 97 unstable smallest-positive points;
- 405 exact piecewise/compact equivalence checks;
- 405 `L^2-D=4R` checks;
- 130 negative-discriminant points;
- 12 stable and 2 unstable discriminant-zero points;
- 41 `b=0` endpoint points and 20 focused zero-root boundary checks;
- 165 irrational-real competitor points;
- 84 sign-crossing and 13 vertex-crossing unsafe points;
- a 33-point one-parameter witness with 24 stable, one collision and eight unstable points;
- exact affine-parameter regressions.

## 11. Next frontier

The next non-split selector tier should use a fixed symbolic Sturm/subresultant sequence for a higher-degree cofactor.  T63 provides the exact semantic interface to preserve: selected-root stability is an interval-root-count invariant, with endpoint roots typed separately from interior positive roots.
