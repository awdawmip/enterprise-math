# Driver Foundational Review — Origin-One / No-Zero Coordinate Supersession and Square/Root Rebuild

Driver-ID: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`
Disposition: `FOUNDATIONAL_SUPERSESSION_ACCEPTED__SQUARE_ROOT_REBUILT__ZERO_CENTERED_NATIVE_TYPING_SUSPENDED`

## 1. User decision

The user explicitly superseded the previous point/displacement split and froze:

`ENTERPRISE_COORDINATE_ORIGIN = 1`

`ENTERPRISE_ZERO_COORDINATE_EXISTS = false`.

Zero is not a native Enterprise coordinate point, component or displacement state.

## 2. Why the prior square formula cannot remain native

The superseded square definition used a zero-origin triangle and therefore identified coordinate label `n` with `n` primitive intervals from the origin.

Under the new origin-one geometry, the endpoint state `n` is separated from the origin state `1` by external primitive interval count `m=n-1`.

Therefore the old native-coordinate geometric inference

`ENTERPRISE_SQUARE(n)=n^2`

is invalid as typed. The quantity `n^2` may still occur as a point-state count or ordinary algebraic magnitude, but not as the two-dimensional cell area spanned from native origin `1` to native endpoint `n`.

## 3. Rebuilt geometry

Let `m=n-1` be the external primitive interval count.

One half-square has elementary triangle counts

`m(m+1)/2` and `m(m-1)/2`, totaling `m^2`.

The mirrored full square contains `2m^2` elementary triangular cells, hence raw normalized area

`A_raw(n)=m^2=(n-1)^2`.

Native scalar states are origin-one, so the order-preserving encoding of an external nonnegative magnitude `q` is

`ENC_E(q)=q+1`.

Hence the rebuilt native square is

`ENTERPRISE_SQUARE(n)=1+(n-1)^2`.

The exact root on the image is

`ENTERPRISE_ROOT(1+(n-1)^2)=n`.

Equivalently proof-side:

`ENTERPRISE_ROOT(y)=1+sqrt(y-1)` when `y-1` is an ordinary perfect square.

## 4. Independent shell check

The same square law follows from incremental shells:

`S_E(1)=1`

and enlarging endpoint state `n -> n+1` increases primitive side magnitude from `n-1` to `n`, so the added raw square area is

`n^2-(n-1)^2=2n-1`.

Therefore

`S_E(n+1)=S_E(n)+(2n-1)`

and summation gives exactly

`S_E(n)=1+(n-1)^2`.

This is an independent derivation from shell growth, not merely algebraic re-encoding.

## 5. Canonical first values

Native square states:

`1,2,5,10,17,26,...`

with exact roots:

`1<-1`

`2<-2`

`5<-3`

`10<-4`

`17<-5`

`26<-6`.

The first nondegenerate one-primitive-interval square has endpoint state `2`, raw area magnitude `1`, and native area state `2`.

## 6. Typing of zero

The ambient proof language may use ordinary zero as an external cardinal/algebraic value, e.g. to say that the interval count from `1` to `1` is empty. This does not put zero back into Enterprise coordinates.

Frozen distinction:

`ZERO_AS_ENTERPRISE_COORDINATE = FORBIDDEN`

`ZERO_AS_EXTERNAL_PROOF_CARDINAL = ALLOWED_IF_EXPLICITLY_NON_NATIVE`.

## 7. R059D impact

R059D W–AO contains substantial use of zero-centered signed coordinate charts.

Those results are not automatically arithmetically false, but their previous native-coordinate typing is no longer valid under the user-superseded foundation.

Freeze:

`R059D_ZERO_CENTERED_CHART_NATIVE_STATUS = SUSPENDED`

`R059D_COMBINATORIAL_LIMIT_RESULTS = PRESERVED_AS_LEGACY_AUXILIARY_CHART_RESULTS`

`R059D_NATIVE_STATUS_REQUIRES_ORIGIN_ONE_NO_ZERO_REENCODING_AUDIT`.

In particular, old claims using `(r,0)`, `(0,r)`, `(0,0,0)` or signed `Z^k` coordinates must not be cited as native Enterprise coordinates without reencoding.

The AO circle/BRC mainline remains frozen as a calibration packet, but its final native-coordinate interpretation is reopened.

## 8. Files

Canonical origin-one/no-zero definition:

`definitions/ENTERPRISE_COORDINATE_ORIGIN_ONE_NO_ZERO_20260817.md`

Canonical rebuilt square/root:

`definitions/ENTERPRISE_SQUARE_AND_ROOT_ORIGIN_ONE_20260817.md`

Machine-readable square/root:

`definitions/enterprise_square_root_origin_one.json`

Superseded historical files:

`definitions/ENTERPRISE_POINT_ORIGIN_AND_DISPLACEMENT_ZERO_20260817.md`

`definitions/ENTERPRISE_SQUARE_AND_ROOT_20260816.md`.

## 9. Driver disposition

`FOUNDATIONAL_SUPERSESSION_ACCEPTED__SQUARE_ROOT_REBUILT__ZERO_CENTERED_NATIVE_TYPING_SUSPENDED`

No attempt is made to preserve a contradicted native-coordinate interpretation merely to protect prior stages. Equally, no correct legacy combinatorial theorem is deleted before a direct counterexample is shown.

If the rebuilt square/root law fails an exact origin-one/no-zero geometric checker or is superseded by a stronger user foundation, tear it down and rebuild again.
