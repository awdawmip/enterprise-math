# Native Enterprise mod-5 K4 breaker orbit -> C3 lane-weight bridge

Status: `FREE_RESEARCH_EXACT_NATIVE_MOD5_BRIDGE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- split-hyperbola quotient theorem;
- C3 bouquet = unfolded central filament theorem.

## 1. Two mod-5 statements previously proved separately

For native `B=3`, channel `5` is the longitudinal universal breaker because the split hyperbola has one regular `K_4` orbit.

Separately, the C3 equal-coordinate bouquet saturates every nonzero `m mod5`:

- left lane root `{1}`;
- center lane roots `{2,3}`;
- right lane root `{4}`.

This note identifies these two structures point by point.

## 2. Native breaker hyperbola

Choose the chirality/branch normalization

`3(y^2-x^2)=-1 mod5`.

A base solution is

`(x_0,y_0)=(1,2)`.

Because the breaker action is regular, the four representation points are exactly

`(+1,+2)`,

`(+1,-2)`,

`(-1,+2)`,

`(-1,-2)`.

They form one `K_4=C2 x C2` orbit.

## 3. Difference projection gives all nonzero m classes

Use the split-hyperbola linear coordinate

`m=a=y-x`.

The four sign states map to:

- `(+,+): m=2-1=1`;
- `(+,-): m=-2-1=-3=2 mod5`;
- `(-,+): m=2-(-1)=3`;
- `(-,-): m=-2-(-1)=-1=4 mod5`.

Thus

`K_4 breaker orbit -> F_5^*`

is a bijection under `m=y-x`.

So the same regular orbit that causes global breaking already parametrizes every nonzero bouquet parameter class.

## 4. Bouquet factorization modulo5

For the three native C3 lanes:

`F_-(m)=6m^2-2m+1`,

`F_0(m)=6m^2+1`,

`F_+(m)=6m^2+2m+1`.

Modulo5:

`F_-(m)=(m-1)^2`,

`F_0(m)=m^2+1=(m-2)(m+2)`,

`F_+(m)=(m+1)^2`.

Therefore:

- `m=1` kills `F_-`;
- `m=2,3` kill `F_0`;
- `m=4` kills `F_+`.

## 5. Hamming-weight lane rule

Count the number of negative signs in the breaker-orbit representation `(sign_x,sign_y)`.

The exact correspondence is:

| sign state | negative-sign count | m | vanishing C3 lane |
|---|---:|---:|---|
| `(+,+)` | 0 | 1 | `F_-` |
| `(+,-)` | 1 | 2 | `F_0` |
| `(-,+)` | 1 | 3 | `F_0` |
| `(-,-)` | 2 | 4 | `F_+` |

Hence the C3 lane index is the Hamming weight of the two-sign breaker state:

`0 negatives -> left lane`,

`1 negative -> center lane`,

`2 negatives -> right lane`.

The multiplicities

`1:2:1`

are therefore the binomial multiplicities of two independent sign bits.

Freeze:

`MOD5 C3 ROOT MULTIPLICITY 1:2:1 = K4 SIGN-WEIGHT MULTIPLICITY`.

## 6. Orientation reversal compatibility

Simultaneously flipping both signs sends

`(+,+)<->(-,-)`,

`(+,-)<->(-,+)`.

Under `m=y-x` this is

`m->-m`.

On the bouquet this swaps

`F_- <-> F_+`

and preserves the unordered center lane.

Thus the sign-orbit bridge respects the previously frozen presentation-reversal symmetry of the C3 bouquet.

## 7. Structural consequence

The mod-5 facts are now one statement rather than two:

`REGULAR K4 HYPERBOLA ORBIT`

`-> all four nonzero m classes`

`-> Hamming-weight quotient 0/1/2`

`-> three C3 lane slots with multiplicities 1/2/1`

`-> every nonzero m kills exactly one bouquet lane`

`-> mod5 bouquet saturation`.

Therefore native channel5 simultaneously acts as:

1. the longitudinal universal breaker;
2. the transverse C3 complete nonzero-residue saturation channel.

Both are two projections of the same four-state hyperbola orbit.

## 8. Relation to the 105 gate

This identifies the `5` factor inside the bouquet gate `105=3*5*7` with the same regular-orbit geometry responsible for the longitudinal breaker.

The other factors have different roles:

- `3`: native curvature coefficient / characteristic degeneration and automatic transverse core;
- `7`: terminal transverse root-slot saturation channel, but not a longitudinal breaker.

Thus the gate `105` combines three distinct small-characteristic mechanisms on one central carrier.

## 9. Prior-art boundary

Klein-four sign orbits, Hamming weights, and quadratic-residue factorizations are classical individually.

Current research claim is only the exact native identification between the mod-5 breaker orbit and the C3 bouquet lane partition.

External novelty status:

`NO_DIRECT_MATCH_FOUND / NOT PROOF OF NOVELTY`.