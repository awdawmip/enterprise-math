# P000 six-axis P11 admissible collision locus and conditional selector — Revision V2 Return

Researcher-ID: `EM-P000P11C2-8D4F27`  
Task: `RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR`  
Publication: `TP2-E899F20BC1B62973D07C`  
Claim: `chatgpt-p000p11c2-20260831-1341-8d4f27`

## Terminal verdict

`SUCCESS / EXACT_PAIRABILITY_FILTERED_COLLISION_LOCUS_WITH_ONE_BIT_ONLY_ON_ADMISSIBLE_DOUBLETONS`

Generation 1's algebraic collision classification and Gram/Vandermonde resolvents survive unchanged, but its terminal information law must be filtered through the frozen integer-pairability gate. The exact law is

\[
\boxed{\operatorname{cost}(H,T,p)=\log_2 |F_{\rm adm}(H,T,p)|}
\]

for an observed admissible `p=P11`. Hence an admissible singleton costs `0` bits and an admissible doubleton costs `1` bit. Algebraic collision levels with zero admissible packets are unreachable for an actual packet and do not receive a selector bit.

## 1. Frozen notation

Let

`H=(h0<h1<h2)`, `T=(t0<t1<t2)`

on the fully distinct stratum, and write

`A=h1-h0`, `B=h2-h1`, `C=t1-t0`, `D=t2-t1`.

A permutation `sigma` denotes the packet

`K_sigma={(h_i,t_{sigma(i)}): i=0,1,2}`.

The frozen local gate is

`PAIRABLE(h,t) <=> Delta(h,t)=h^2-4t is a nonnegative perfect square and sqrt(Delta) == h (mod 2)`.

Define

`ADM(sigma) <=> AND_i PAIRABLE(h_i,t_{sigma(i)})`

and

`F_adm(H,T,p)={K_sigma : ADM(sigma) and P11(sigma)=p}`.

For compactness let `Q_ij` denote `PAIRABLE(h_i,t_j)`.

## 2. Retained algebraic collision theorem

The exact combinatorial equal-`P11` equations on the fully distinct stratum remain:

- `C1: A*C=B*D`, with the unique colliding pair `132/213`;
- `C2: A*D=B*C`, with the unique colliding pair `231/312`.

Repeated-`H` or repeated-`T` strata are combinatorially `P11`-injective on distinct alignment orbits, so pairability filtering cannot create a collision there.

Simultaneous `C1+C2` forces `A=B` and `C=D`. It still produces two separate algebraic double levels, never a triple algebraic fibre.

## 3. Exact admissible two-orbit locus

Because the two members of each algebraic collision class are distinct packets, pairability filtering gives the exact cardinality directly.

For the `C1` level,

`|F_adm(H,T,p_C1)| = 1_ADM(132) + 1_ADM(213)`,

where

- `ADM(132) <=> Q_00 & Q_12 & Q_21`;
- `ADM(213) <=> Q_01 & Q_10 & Q_22`.

Therefore

`C1_TWO_ADMISSIBLE <=> A*C=B*D & Q_00 & Q_12 & Q_21 & Q_01 & Q_10 & Q_22`.

Equivalently, the six discriminants

`D_00,D_12,D_21,D_01,D_10,D_22`

must each be nonnegative squares with square root congruent to the corresponding `h_i` modulo `2`.

For the `C2` level,

`|F_adm(H,T,p_C2)| = 1_ADM(231) + 1_ADM(312)`,

where

- `ADM(231) <=> Q_01 & Q_12 & Q_20`;
- `ADM(312) <=> Q_02 & Q_10 & Q_21`.

Therefore

`C2_TWO_ADMISSIBLE <=> A*D=B*C & Q_01 & Q_12 & Q_20 & Q_02 & Q_10 & Q_21`.

These are necessary and sufficient. No extra global compatibility condition is needed because each packet is admissible exactly when its three local `(h,t)` pairs pass the frozen gate.

Thus every algebraic collision level is classified exactly as:

- `ZERO_ADMISSIBLE`: neither colliding packet passes;
- `ONE_ADMISSIBLE`: exactly one passes;
- `TWO_ADMISSIBLE`: both pass.

On a valid task input the actually observed `P11` level has cardinality `1` or `2`; a zero-admissible algebraic level may coexist with a different admissible level but is not an observable state.

## 4. Mandatory Driver falsifier

Take

`H=(-2,0,2)`, `T=(-1,0,1)`.

Here `A=B=2`, `C=D=1`, so both algebraic equations hold.

At `P11=2`, the `C1` candidates are `132/213`.

- `213` is admissible.
- `132` is not: `(-2,-1)` has discriminant `8`, and `(0,1)` has negative discriminant.

Hence `|F_adm(H,T,2)|=1` and the selector cost is `0` bits.

At `P11=-2`, the `C2` candidates are `231/312`.

- `312` is admissible.
- `231` is not: `(0,1)` has negative discriminant and `(2,-1)` has discriminant `8`.

Hence `|F_adm(H,T,-2)|=1` and the selector cost is again `0` bits.

This exactly falsifies the Generation-1 identification

`ALGEBRAIC_P11_COLLISION_LOCUS = ADMISSIBLE_TWO_ORBIT_LOCUS`.

## 5. Simultaneous C1+C2 levels can have different admissible cardinalities

The two algebraic doubled levels must be filtered independently.

A small valid example is

`H=(-2,-1,0)`, `T=(-2,-1,0)`.

Both `C1` and `C2` hold. The `C1` level has `0` admissible candidates, while the `C2` level has exactly `1` (`312`). Thus simultaneous algebraic collision does not force equal admissible cardinality.

More strongly, take

`H=(1,4,7)`, `T=(-60,-30,0)`.

Again `A=B=3`, `C=D=30`, so both equations hold.

- `C1`, `P11=-270`: `132` fails because `(1,-60)` has discriminant `241`, not a square; `213` passes with discriminants `121,256,49`. Therefore the level is an admissible singleton and costs `0` bits.
- `C2`, `P11=-450`: `231` passes with discriminants `121,16,289`; `312` passes with discriminants `1,256,169`. Therefore the level is an admissible doubleton and costs `1` bit.

So even for the same `(H,T)`, selector cost is a function of the observed `P11` level, not of membership in `C1 union C2` alone.

## 6. Resolvent roots are algebraic candidates, then pairability-filtered

Generation 1's symmetric Gram/Vandermonde quadratics for `P21` and `P12` remain exact algebraic resolvents.

For distinct `H`, a candidate `x=P21` together with the known data

`sum(T)`, `P11`, `x`

solves the Vandermonde system

`sum u_i=sum(T)`,
`sum h_i*u_i=P11`,
`sum h_i^2*u_i=x`.

Because the Vandermonde determinant is nonzero, this reconstructs a unique labeled candidate vector

`u=(t_{sigma(0)},t_{sigma(1)},t_{sigma(2)})`.

On an algebraic double level the two quadratic roots reconstruct exactly the two colliding algebraic packets. The root is retained in the admissible candidate set iff all three reconstructed pairs pass `PAIRABLE`. Hence on a one-admissible collision the other quadratic root is an algebraic ghost branch whose reconstructed packet fails the frozen gate.

Dually, distinct `T` and a candidate `y=P12` reconstruct the labeled `H` assignment through the analogous Vandermonde system on the `T` nodes. The same pairability test filters its two roots.

On a genuine admissible doubleton, both roots survive and reconstruct exactly the two admissible packets.

The retained root-order relation is unchanged on genuine doubletons:

- `C1`: `P21` and `P12` root-order bits are `SAME`;
- `C2`: they are `OPPOSITE`.

## 7. Exact selector

Given `(H,T,p=P11)`, compute the finite algebraic candidate fibre, apply `ADM` to each candidate, and retain

`F_adm(H,T,p)`.

For an actually observed packet this set is nonempty. The direct combinatorial classification gives `|F_adm|<=2`, so:

- `|F_adm|=1`: no side information is needed;
- `|F_adm|=2`: one conditional branch bit is necessary and sufficient.

No separate collision flag is required: the decoder can compute `|F_adm|` from the public marginal data and `p` itself. A branch bit is consumed only when the filtered set has two members.

This branch bit remains derived `K/Gamma` alignment information only. It is not native orientation, not the Pfaffian negative-slot choice, and carries no dimension-reduction, factorization, or Full-Cell conclusion.

## 8. Genuine doubletons, minimality, and scaling retained

The Generation-1 root-box search remains valid because it explicitly required both packets of the class to consist of pairable states.

The first genuine two-admissible witnesses remain at root box `B=6`:

- `C1`: `H=(-1,1,4)`, `T=(-30,-12,0)`;
- `C2`: `H=(-4,-1,1)`, `T=(-30,-12,0)`.

No such witness exists for root boxes `B=1,...,5`.

For every positive integer `m`, the homogeneous scaling

`H -> m H`, `T -> m^2 T`

preserves pairability, the collision equation, and the two-admissible status, giving infinite families.

## 9. Deterministic verification

The V2 checker directly enumerates pairability-filtered fibres on the bounded control box `[-4,4]`, not merely algebraic fibres. It found:

- `2634` valid `(H,T)` inputs;
- `244` algebraic collision levels on those valid inputs;
- filtered collision histogram in that box: `ZERO=204`, `ONE=40`, `TWO=0`;
- `1714` valid repeated-marginal inputs, all with admissible fibre size `1`;
- direct bounded-control maximum admissible fibre `1` (the first genuine doubleton lies outside this small value box);
- `668` retained quadratic-resolvent checks;
- `1336` exact Vandermonde reconstruction/filter checks;
- `320` SAME/OPPOSITE branch-sign checks;
- `24` scaling-family doubleton checks;
- root-box census `C1: 0,0,0,0,0,1` and `C2: 0,0,0,0,0,1`.

The separately verified `B=6` witnesses attain admissible fibre size `2`, while the retained algebraic theorem proves no algebraic `P11` fibre exceeds `2`; filtering can only decrease cardinality. Therefore the exact global bound is

`|F_adm(H,T,p)| <= 2`

and is sharp.

Checker terminal line:

`PASS P000_P11_PAIRABILITY_FILTERED_REVISION_V2 checks=5226 valid_inputs=2634 filtered_levels=244 class_hist=0:204,1:40,2:0 resolvent=668 reconstruction=1336 branch=320 scale=24 repeated_valid=1714 control_max=1 rootbox=C1:0,0,0,0,0,1|C2:0,0,0,0,0,1 adm_fibre_max=2 selector_bits=log2|F_adm|=0_or_1 simultaneous_levels=cardinality_can_differ`

## 10. Reconciliation with Generation 1

Retained without change:

1. exact algebraic `C1/C2` collision equations;
2. repeated-stratum combinatorial injectivity;
3. no algebraic triple fibre;
4. Gram/Vandermonde quadratic candidate resolvents;
5. SAME/OPPOSITE root ordering on genuine doubletons;
6. `B=6` minimal genuine pairable witnesses and scaling families;
7. classical attribution to assignment geometry, Vandermonde/Gram elimination, and symmetric/multisymmetric invariant theory.

Corrected:

1. `C1 union C2` is only the algebraic candidate-collision locus, not the admissible two-orbit locus;
2. an algebraic double level may have `0`, `1`, or `2` admissible candidates;
3. the second quadratic root may be nonadmissible and must be discarded;
4. side-information cost is `log2 |F_adm(H,T,P11)|`, hence `0` for a singleton and `1` exactly for a genuine admissible doubleton;
5. simultaneous `C1+C2` levels are filtered independently and may require different selector costs.

## 11. Attribution and firewalls

The collision equations are finite assignment geometry. The reconstruction argument is classical Vandermonde interpolation / Gram elimination. The polynomial packaging is symmetric/multisymmetric invariant theory. No historical novelty claim is made for those ingredients.

No conclusion here selects native P000 orientation, the Pfaffian negative slot, native dimension, factorization, or Full-Cell dynamics. No downstream task is created from the Researcher lane.

## Return disposition

Hard target satisfied as

`EXACT_PAIRABILITY_FILTERED_COLLISION_LOCUS_WITH_ONE_BIT_ONLY_ON_ADMISSIBLE_DOUBLETONS`.

Recommended next control action: Driver review this immutable Result at exactly the corrected arithmetic strength. Any strengthening beyond the pairability-filtered `P11/P21/P12` facade requires separate authorization.
