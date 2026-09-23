# P000 P11 fixed-twist Selmer cover and exact rank-or-Sha dichotomy

Status: `PORTABLE_STAGED_RESEARCH / NO_CURRENT_CLAIM / NOT_SOURCE_CHECKPOINT / NOT_RESULT / UNREVIEWED`

Task: `RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC`
Publication: `TP2-FB7F5A1D6B6C6BCCD62D`
Contributor lineage: `EM-DIRECT-C4D02C`, stable conversation `em-auto-staggered-20260923-r11`, session `MCP-5ff2a3263c5c4ca2b556ebe8e47e5624`.

This note is noncanonical durable persistence. It consumes without promotion the same-session staged exact fiber/Kummer interface and the portable identification

`eta_2 = chi_2 tensor T0 = (1,2,2)`

with `eta_2 in Sel_2(E/Q)` exactly on TYPE-5+. None of those inputs is represented here as Source-published predecessor completed research.

Let
`E: W^2=X(X-P^2)(X-Q^2)`,
with
`A=r^2-s^2`, `B=2rs`, `C=r^2+s^2`,
`P=A+B`, `Q=|A-B|`,
`P^2+Q^2=2C^2`, `P^2-Q^2=4AB`.

## 1. Exact 2-cover attached to eta_2

The full-2-torsion Kummer class `(1,2,2)` is represented by

`C_eta:`
`U^2 - 2 V^2 = P^2 H^2`,
`U^2 - 2 Z^2 = Q^2 H^2`.

If `H=0`, then `U^2=2V^2` over Q, forcing `U=V=0`, and then `Z=0`; thus every rational point has `H!=0`. Set `H=1`.

The map

`X=U^2`,
`W=2UVZ`

lands on E because `X-P^2=2V^2` and `X-Q^2=2Z^2`. Its labeled Kummer triple is `(1,2,2)`. Conversely every rational E-point representing eta_2 supplies rational U,V,Z. Hence

`C_eta(Q) != empty iff eta_2 lies in the image E(Q)/2E(Q)`.

No exceptional rational coordinate is hidden. `U=0` and `Z=0` are impossible. If `V=0`, then `Z^2=2AB`. But `2AB=4rs(r^2-s^2)`. If this were a rational square, pairwise coprimality of `r`, `s`, and `r^2-s^2` would force all three to be squares, giving a nontrivial `a^4-b^4=c^2`, excluded by the same Fermat descent already consumed in the staged TYPE-5+ proof.

## 2. Complete biquadratic quartic model

Parameterize the first norm conic from `(U,V)=(P,0)` by

`q=V/(U+P)`.

The exceptional point `U=-P,V=0` again requires `2AB` square and does not occur rationally. Thus every rational point is covered by

`U=P(1+2q^2)/(1-2q^2)`,
`V=2Pq/(1-2q^2)`.

For rational q, `1-2q^2` never vanishes. Set
`Y=Z(1-2q^2)`.
Then the second quadric becomes

`Y^2 = 8AB q^4 + 4C^2 q^2 + 2AB`

and factors exactly as

`Y^2 = 2(2Aq^2+B)(2Bq^2+A)`.

Conversely any rational `(q,Y)` on this quartic reconstructs

`U=P(1+2q^2)/(1-2q^2)`,
`V=2Pq/(1-2q^2)`,
`Z=Y/(1-2q^2)`,

so this is an exact rational model of the eta_2-cover, not merely a necessary condition.

The factorization keeps the A/B provenance separate. Erasing that factor split is not justified for future local-norm or reciprocity operations.

## 3. TYPE-5+ rank-or-Sha dichotomy

The preceding all-place theorem gives

`eta_2 in Sel_2(E/Q) iff TYPE-5+`.

Hence for every TYPE-5+ core, C_eta is everywhere locally soluble. For this canonical class there are then two exact cases.

If `C_eta(Q) != empty`, eta_2 is in `E(Q)/2E(Q)`. It is not a rational 2-torsion class. With the fixed root ordering, the three nonzero rational 2-torsion Kummer classes have squareclasses

- `T0: (1,-1,-1)`,
- `TP: (1,AB,AB)`,
- `TQ: (1,-AB,-AB)`.

Equality with TP would force `2AB` square, already excluded; equality with TQ would force `-2AB` square; equality with T0 would identify the Q-squareclasses 2 and -1. Thus a rational point of C_eta yields a non-torsion point on E and

`C_eta(Q) != empty -> rank E(Q)>=1`.

Furthermore `X=U^2=P^2+2V^2>P^2`, so this point automatically lies on the strict `+++` real component used by the P11 reconstruction. Denominator/parity/recovered-root-gcd filters remain separate.

If `C_eta(Q)=empty`, then because the cover is everywhere locally soluble, eta_2 maps to a nonzero element of `Sha(E/Q)[2]`:

`TYPE-5+ and C_eta(Q)=empty -> 0 != [eta_2] in Sha(E/Q)[2]`.

Thus the fixed-twist direction is an explicit Hasse-principle test on TYPE-5+:

`Y^2=2(2Aq^2+B)(2Bq^2+A)`.

A rational point gives actual target rank; global failure despite local solubility gives an explicit Sha[2] class. No finiteness of Sha is assumed for this elementwise exact-sequence statement.

On TYPE-4 the same cover fails at Q2 and is not a Sha candidate there; the Pfaffian/Pluecker residue obstruction remains the appropriate route.

## 4. BRC / residual-faithful interpretation

For the fixed-twist observer on TYPE-5+, the selector bit epsilon safely refines to the explicit genus-one carrier C_eta. The retained state is `(A-port,B-port,q,Y; TYPE-5+; eta_2 provenance)`. The boolean “locally soluble” is not a safe final quotient for the next operation because it erases the global rational-solubility/Hasse residual.

The typed residual chain is

`local survival of eta_2 -> explicit 2-cover C_eta -> MW realization or nonzero Sha[2]`.

This is a state-completeness refinement, not a world axiom and not a claim that every Selmer residual lies in Sha.

## 5. Next exact unit

Do not redo the fixed twist point, Galois no-transfer theorem, common E[2] normalization, local Selmer gate, or this cover derivation. Control rational points on the biquadratic cover for an infinite primitive TYPE-5+ family:

- construct an infinite primitive family and rational q making `2(2Aq^2+B)(2Bq^2+A)` square, yielding an infinite target-rank family; or
- prove an infinite locally-soluble subfamily with no rational point by an exact Cassels/local-norm obstruction, yielding an infinite explicit Sha[2] family.

Finite searches remain falsification/heuristic only.

BRC resolution: `COMPOSE_APPLIED / ETA2_COVER_EXPLICIT / TYPE5_RANK_OR_SHA_DICHOTOMY / P11_REAL_BRANCH_PRESERVED`.
