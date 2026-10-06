# EM-FREE-F6D046 latest durable frontier after R13

Status: `ACTIVE_HANDOFF / CORRECTION_AWARE / ARITHMETIC_EVIDENCE_STAGE / NOT_AXIOM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Root candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`

## Highest verified theorem frontier

1. `R8`: signatures `3/4/6` share the explicit projective elliptic cover
   `v^2=(t+6)(t^3+18t^2+84t+24)`, with Weierstrass model
   `y^2=x^3-12x+20`, `j=-3072`.
2. `R10`: strict common cover
   `r^4=A(t)/144`, `q^2=D(t)/24`, geometric deck group `C4 x C2`,
   degree `8` over `X0(6)`, compact genus `9`.
3. `R11`: Jacobian/Hodge refinement
   `J(X) ~ E_346 x E_i^2 x J(H_4) x P_46`, dimensions `1+2+2+4`,
   where `H_4:h^2=A(t)D(t)/3456`; `P_46` has `Q(i)` Hodge signature `(3,1)`.
4. `R12`: character/Hodge symmetry alone cannot decide the isogeny decomposition of
   `P_46`, because the relevant Hermitian deformation space has complex dimension `3`.
5. `R13`: exact finite-field arithmetic has begun. For good primes `5,7,11,13`,
   all point counts over `F_{p^n}` for `n=1..4` were computed; Newton identities and
   the weight-one functional equation recover four complete degree-8 Prym Frobenius
   polynomials, with exact `Z[T]` factorization attempted by the verifier.

## Current evidence status

`R13` is computational arithmetic evidence, not yet a theorem of geometric simplicity
or splitting. It is strong enough to falsify proposed stable decompositions that conflict
with a listed local polynomial. A global decomposition statement still requires one of:

- a good-reduction absolute-simplicity certificate;
- a cross-prime common Tate-module factor with a proved global correspondence;
- an explicit algebraic correspondence or quotient;
- a certified period matrix and endomorphism computation.

## Correction state

- `R5` direct-`X0(12)` actual signature-6 character cube remains conditional only.
- Actual standard signature-6 projective marking is controlled by `R7/R8`.
- Genus `9` is unconditionally attached to the signatures `3/4/6` strict cover of
  `R8/R10`, not to the superseded direct-marking interpretation.

## Smallest unfinished unit

`P46_ABSOLUTE_SIMPLICITY_OR_SPLITTING_CERTIFICATE`:

1. read the four R13 local polynomials as exact inputs;
2. test rigorous finite-field absolute-simplicity criteria at each good prime;
3. search for factor patterns stable under the `Q(i)` action;
4. extend the census to additional good primes only if the first four remain
   non-discriminating;
5. produce either an explicit global correspondence/splitting certificate, an
   absolute-simplicity proof, or an exact statement that the current arithmetic
   window remains undecided.

## Do not repeat

Do not reopen the bare first-jet invariant search, the direct signature-6-on-X0(12)
marking, the even-readout reconstruction route, or the symmetry-only P46 splitting
route. Each is closed by a proof, correction, or information-boundary theorem.

## Axiom gate

All current units remain `DERIVED / NOT_NEW_AXIOM / NOT_FOUNDATION`; P000 is unchanged.
