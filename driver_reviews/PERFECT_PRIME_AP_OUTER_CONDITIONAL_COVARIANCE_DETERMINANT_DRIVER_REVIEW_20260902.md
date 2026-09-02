# Perfect Prime AP outer conditional-covariance determinant — Driver Review

Status: `ACCEPTED / TERMINAL TASK NEGATIVE BOUNDARY / PARENT OBJECTIVE OPEN`

- Task-ID: `RS-PERFECT-PRIME-AP-OUTER-CONDITIONAL-COVARIANCE-DETERMINANT`
- Publication-ID: `TP2-C4B48A416649C9324011`
- Result-ID: `RR-F5AB0AF5F544393896D9`
- Researcher-ID: `EM-PPTAPOCD1-8F31A2`
- Driver-ID: `EM-DVR-P8H4Q2`
- Parent Objective: `OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M`
- Disposition: `ACCEPTED`
- Terminal: `true`

## 1. Decision

Accept the Result exactly as an **exact negative boundary for one proof mechanism**:

`EXACT_CANONICAL_MONOMIAL_FLAG_SIGN_REGULARITY_OBSTRUCTION`.

The accepted statement is not a counterexample to the mother determinant conjecture. It closes only the route that tries to prove all-m nonvanishing from a fixed sign pattern for every canonical leading principal minor, equivalently a globally strict alternating one-by-one LDL pivot pattern in the quotient monomial basis.

The parent statement

`det S_m(t) != 0` for every `m>=2` and `0<t<=1`

remains OPEN.

## 2. Exact witness accepted

For `m=15`, `t=4/5`, in the canonical quotient monomial basis `X,...,X^14`, the exact leading-principal-minor signs are

`[-,-,+,+,-,-,+,+,-,-,+,-,-,-]`.

The previously conjectured universal flag pattern would be

`[-,-,+,+,-,-,+,+,-,-,+,+,-,-]`.

Thus the unique mismatch at this witness is order `k=12`:

`Delta_(15,12)(4/5) < 0`

where the rejected flag theorem requires it to be positive.

All fourteen leading principal minors are nevertheless nonzero at `t=4/5`, and the full determinant is nonzero:

`det S_15(4/5) = Delta_(15,14)(4/5) < 0`.

The one-by-one LDL pivot signs are

`[-,+,-,+,-,+,-,+,-,+,-,-,+,+]`,

so the twelfth/thirteenth pivots exchange signs as a pair while the total inertia remains exactly

`(7 positive, 7 negative, 0 zero)`.

This establishes the structural distinction

`FIXED_INERTIA_POSSIBLE != FIXED_CANONICAL_1x1_LDL_FLAG`.

## 3. Interior crossing audit

The exact checker also gives

- `Delta_(15,12)(3/4) > 0`,
- `Delta_(15,12)(4/5) < 0`,
- `Delta_(15,12)(1) > 0`.

The accepted denominator factors stay positive on the admissible interval, so the relevant matrix entries and minors are continuous. Therefore the twelfth canonical flag minor has at least one zero in `(3/4,4/5)` and at least one zero in `(4/5,1)`.

Accordingly, the failed flag mechanism cannot be repaired by claiming that the observed sign mismatch is an isolated arithmetic accident at one rational parameter.

## 4. Driver verification

The Driver independently reconstructed the frozen witness from the exact `fractions.Fraction` formulas for the accepted outer covariance matrix and rechecked:

1. the fourteen leading-minor signs;
2. the unique order-12 mismatch;
3. nonvanishing and negative sign of the full determinant at `m=15,t=4/5`;
4. exact numerator/denominator bit lengths `17954/17720` for the full determinant;
5. the `7+/7-` LDL pivot count;
6. the sign sequence `+,-,+` for `Delta_(15,12)` at `3/4,4/5,1`.

The Result manifest and exact certificate therefore support the declared negative boundary.

## 5. Scope boundary

This review does **not** accept any of the following stronger claims:

- that `det S_m(t)` vanishes for some admissible `m,t`;
- that the conjectured balanced inertia is false;
- that no noncanonical congruence or block factorization can prove nonvanishing;
- that the double-endpoint residual Bernstein/Mobius route fails;
- that finite computation proves an all-m theorem.

It also does not reopen the already-closed inner-block definiteness, factorwise total-positivity, generic common-measure, or generic order-map routes.

No Working Truth, Foundation authority, L4 destination, canonical theorem promotion, or historical novelty claim is granted.

## 6. Parent Objective decision

The parent Objective remains OPEN.

Its closure criteria require either a rigorous all-m proof of the actual AP critical cofactor/nonvanishing statement or an exact full-determinant counterexample. The present Result supplies neither; it only removes one structural mechanism.

Therefore no Objective closure generation is issued.

## 7. Successor gate

A justified successor exists because the witness exposes new structure rather than mere failure: the canonical one-by-one pivots exchange signs in an adjacent pair while preserving the total signature and full determinant.

The next task isolates whether this phenomenon can be controlled by a noncanonical congruence or a mixed `1x1/2x2` symmetric-indefinite block factorization. A successful theorem must exclude determinant zero independently, not by continuity from an assumed inertia.

The alternate all-m residual Bernstein/Mobius interface remains open, but is not bundled into this successor; it is preserved as the fallback route if the block mechanism is exactly obstructed.

Successor:

`RS-PERFECT-PRIME-AP-OUTER-BLOCK-HYPERBOLIC-CONGRUENCE`.

Hard target:

`OUTER_BINOMIAL_COVARIANCE_BLOCK_HYPERBOLIC_CONGRUENCE_NONVANISHING_PROVED_OR_EXACTLY_OBSTRUCTED`.
