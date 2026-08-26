# Native filament breaker capacity as quadratic ramification

Status: `FREE_RESEARCH_EXACT_RAMIFICATION_INTERPRETATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on the split-hyperbola quotient theorem.

## 1. Two branch maps

Over an odd finite field, the two parity branches have hit maps

`f_e(x)=-B*x^2/2-d_e`, `e=0,1`,

with distinct shifts `d_0,d_1` and `B!=0`.

Each branch image has `(q+1)/2` values.

Away from the critical value

`h_e=-d_e`,

a value in the image has two preimages `+/-x`.

At `h_e`, the unique preimage is `x=0`, with quadratic multiplicity two.

Thus each branch is a degree-two cover with one affine ramification value.

## 2. Universal breaker and overlap

A universal breaker means

`I_0 union I_1=F_q`.

Equivalently, because each image has `(q+1)/2` values,

`|I_0 intersect I_1|=1`.

At least one of the two distinct critical values `h_0,h_1` is outside the one-point overlap.

Choose such a critical value `h_e`.

Then:

- branch `e` hits `h_e` at exactly one residue parameter, the double root `x=0`;
- the other branch does not hit `h_e` at all.

Hence in the full parity-complete shell period of length `2q`, exactly one shell is divisible by the breaker prime.

## 3. Sharp capacity theorem

Because a breaker leaves no fully transparent transverse class, every `2q`-shell period contains at least one zero.

The critical value above produces a period containing exactly one zero.

Therefore

`MAX CONSECUTIVE BREAKER-COPRIME RUN = 2q-1`.

This is the ramification form of the previously frozen periodic cap.

For the only nonsingular odd breaker characteristics:

- `q=3 -> cap 5`;
- `q=5 -> cap 9`.

The `q=2` cap `1` remains the separate characteristic-two parity case.

## 4. Regular q=5 orbit and the two extremal classes

At `q=5`, a breaker is equivalent to the four-point split hyperbola forming one regular `K_4` orbit.

Regularity means there are no hyperbola points fixed by the tangent-exchange involution or by its signed companion.

Under the dual representation, this is exactly the statement that neither `x=0` nor `y=0` occurs on the overlap variety.

Therefore neither branch critical value lies in the overlap.

Both critical values are consequently extremal one-zero transverse classes.

For the native normalization

`d_0=0`, `d_1=1/2`,

they are

`H=0`,

`H=-1/2=2 mod5`.

Thus the two previously observed sharp-nine channels are exactly the two branch ramification values.

## 5. q=3 contrast

At `q=3`, the representation hyperbola has only two points. A one-orbit breaker action need not be regular because the symmetry group has order four.

Accordingly one of the two branch critical values can lie in the overlap while the other remains outside.

There is still at least one one-zero critical class, so the sharp breaker-coprime cap remains

`2*3-1=5`.

## 6. Structural chain

The breaker/cap mechanism can now be written as

`quadratic branch maps`

`-> split-hyperbola overlap quotient`

`-> universal covering`

`-> branch ramification value outside overlap`

`-> exactly one zero per 2q-period`

`-> sharp capacity 2q-1`.

For the native B=3 phase:

`q=5 breaker`

`-> two ramification extremals`

`-> sharp breaker-coprime capacity 9`.

This does not replace the separate full typed-Cell prime-incidence island theorem. It explains the divisibility capacity inside the odd-curvature filament family.

## 7. Prior-art boundary

Quadratic ramification, two-to-one square maps, and critical values are classical. The formula `2q-1` is therefore not promoted as a new standalone theorem.

The research-specific value is the exact identification of the native sharp-cap channels with ramification values of the same dual quadratic pair whose split-hyperbola quotient controls the breaker phase.