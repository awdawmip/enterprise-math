# P000 P11 pairability-filtered collision locus - Revision V2 Return

Researcher-ID: `EM-P000P11C2-8D4F27`
Task: `RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR`
Publication: `TP2-E899F20BC1B62973D07C`
Claim: `chatgpt-p000p11c2-20260831-1341-8d4f27`

## Verdict

`SUCCESS / EXACT_PAIRABILITY_FILTERED_COLLISION_LOCUS_WITH_ONE_BIT_ONLY_ON_ADMISSIBLE_DOUBLETONS`

Generation 1's algebraic `C1/C2` classification and Gram/Vandermonde `P21/P12` resolvents are retained. The corrected terminal law is

`cost(H,T,p)=log2 |F_adm(H,T,p)|`.

For an observed admissible `p=P11`, this is `0` bits for a singleton and `1` bit exactly for an admissible doubleton. An algebraic collision with only one pairable packet is not a one-bit state.

## Exact criterion

On the fully distinct sorted stratum write

`A=h1-h0`, `B=h2-h1`, `C=t1-t0`, `D=t2-t1`

and `Qij = PAIRABLE(h_i,t_j)`, where

`PAIRABLE(h,t) <=> h^2-4t is a nonnegative perfect square and sqrt(h^2-4t) == h (mod 2)`.

The retained combinatorial equal-`P11` classes are exactly:

- `C1: A*C=B*D`, colliding packets `132/213`;
- `C2: A*D=B*C`, colliding packets `231/312`.

Their filtered cardinalities are

`|F_adm(p_C1)| = 1_ADM(132)+1_ADM(213)`

with

`ADM(132) <=> Q00 & Q12 & Q21`,
`ADM(213) <=> Q01 & Q10 & Q22`;

and

`|F_adm(p_C2)| = 1_ADM(231)+1_ADM(312)`

with

`ADM(231) <=> Q01 & Q12 & Q20`,
`ADM(312) <=> Q02 & Q10 & Q21`.

Therefore the exact two-admissible loci are

`C1_TWO <=> C1 & Q00 & Q12 & Q21 & Q01 & Q10 & Q22`;

`C2_TWO <=> C2 & Q01 & Q12 & Q20 & Q02 & Q10 & Q21`.

Equivalently, every listed discriminant must be a nonnegative square with the required parity. Every algebraic double level is therefore exactly `ZERO_ADMISSIBLE`, `ONE_ADMISSIBLE`, or `TWO_ADMISSIBLE`.

Repeated-`H` or repeated-`T` strata remain one-orbit whenever valid: Generation 1 already proved combinatorial `P11` injectivity there, and filtering cannot create collisions. Simultaneous `C1+C2` still gives two separate algebraic double levels and never a triple fibre. Since filtering only removes candidates, `|F_adm|<=2` globally.

## Mandatory falsifier

For

`H=(-2,0,2)`, `T=(-1,0,1)`

both algebraic equations hold.

At `P11=2`, the `C1` candidates are `132/213`. Packet `213` is admissible; `132` is not because `(-2,-1)` has discriminant `8` and `(0,1)` has negative discriminant. Thus `|F_adm|=1`, cost `0`.

At `P11=-2`, the `C2` candidates are `231/312`. Packet `312` is admissible; `231` is not because `(0,1)` has negative discriminant and `(2,-1)` has discriminant `8`. Thus `|F_adm|=1`, cost `0`.

Hence

`ALGEBRAIC_P11_COLLISION_LOCUS != ADMISSIBLE_TWO_ORBIT_LOCUS`.

## Simultaneous collisions are filtered per P11 level

The two doubled levels need not have the same admissible cardinality.

Small valid witness:

`H=T=(-2,-1,0)` gives both `C1,C2`, with filtered counts `(0,1)`.

Stronger witness:

`H=(1,4,7)`, `T=(-60,-30,0)` has `A=B=3`, `C=D=30`, so both equations hold.

- `C1`, `P11=-270`: `132` fails (`disc(1,-60)=241`); `213` passes with discriminants `121,256,49`. Count `1`, cost `0`.
- `C2`, `P11=-450`: `231` passes with discriminants `121,16,289`; `312` passes with discriminants `1,256,169`. Count `2`, cost `1`.

Thus selector cost is attached to the observed `P11` fibre, not globally to `(H,T)` or to `C1 union C2`.

## Resolvent filtering

The Generation-1 Gram/Vandermonde quadratics remain exact algebraic candidate resolvents.

For distinct `H`, a candidate `x=P21` together with `sum(T)` and `P11` solves the nonsingular Vandermonde system

`sum u_i=sum(T)`,
`sum h_i u_i=P11`,
`sum h_i^2 u_i=x`.

Hence each quadratic `P21` root reconstructs one unique labeled algebraic `T` assignment. Retain that root iff all three reconstructed `(h_i,u_i)` pairs pass `PAIRABLE`.

Dually, each `P12` root reconstructs one unique labeled `H` assignment on the distinct `T` nodes, and is retained iff all three reconstructed pairs are pairable.

Therefore a one-admissible algebraic collision has one surviving root and one algebraic ghost root; a two-admissible collision has exactly two surviving roots. On genuine doubletons the retained root-order relation remains `SAME` on `C1` and `OPPOSITE` on `C2`.

No separate collision flag is needed: the decoder computes the filtered candidate set from `(H,T,P11)` and consumes a branch bit iff that set has size `2`.

## Exact verification

The V2 checker reuses only the already-validated Generation-1 task-local algebraic checker and adds exact pairability filtering plus exact `Fraction` Vandermonde reconstruction. It passed:

`PASS P000_P11_PAIRABILITY_FILTERED_REVISION_V2 checks=5226 valid_inputs=2634 filtered_levels=244 class_hist=0:204,1:40,2:0 resolvent=668 reconstruction=1336 branch=320 scale=24 repeated_valid=1714 control_max=1 rootbox=C1:0,0,0,0,0,1|C2:0,0,0,0,0,1 adm_fibre_max=2 selector_bits=log2|F_adm|=0_or_1 simultaneous_levels=cardinality_can_differ`

The bounded direct filter enumerates all `H,T` multisets in `[-4,4]`:
- `2634` valid inputs;
- `244` algebraic collision levels on valid inputs;
- filtered histogram `ZERO=204`, `ONE=40`, `TWO=0`;
- `1714` valid repeated-marginal inputs, all singleton.

The absence of a doubleton in this small value box is expected. The retained root-box control finds the first genuine pairable doubletons at `B=6`, exactly:

- `C1`: `H=(-1,1,4)`, `T=(-30,-12,0)`;
- `C2`: `H=(-4,-1,1)`, `T=(-30,-12,0)`,

with census `0,0,0,0,0,1` for each class. Scaling `H->mH`, `T->m^2T` preserves pairability and supplies infinite two-admissible families. These witnesses attain the sharp global bound `|F_adm|=2`.

## Reconciliation and firewalls

Retained: exact `C1/C2` algebraic equations; repeated-stratum injectivity; no algebraic triple fibre; `P21/P12` quadratic resolvents; SAME/OPPOSITE root ordering on genuine doubletons; `B=6` minimal genuine pairable witnesses and scaling families.

Corrected: `C1 union C2` is only the algebraic candidate-collision locus; algebraic double levels may have `0/1/2` admissible packets; nonpairable resolvent roots are discarded; selector cost is `log2|F_adm|`; simultaneous doubled levels are filtered independently.

Attribution remains classical finite assignment geometry, Vandermonde/Gram elimination, and symmetric/multisymmetric invariant theory. No historical novelty claim is made for those ingredients.

This Result is derived `K/Gamma` arithmetic only. It does not select native orientation, the Pfaffian negative slot, native dimension, factorization, or Full-Cell dynamics. The Researcher lane creates no downstream task.

## Return disposition

Hard target satisfied as

`EXACT_PAIRABILITY_FILTERED_COLLISION_LOCUS_WITH_ONE_BIT_ONLY_ON_ADMISSIBLE_DOUBLETONS`.

Next control action: Driver review at exactly this corrected arithmetic strength.
