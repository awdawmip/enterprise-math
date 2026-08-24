# Native filament odd-curvature deformation master theorem

Status: `FREE_RESEARCH_EXACT_PARAMETERIZED_THEOREM_FAMILY / EXTERNAL_NOVELTY_UNRESOLVED / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

This note deforms the native coefficient `3` to an arbitrary positive odd curvature coefficient `B`. The actual Enterprise filament is the specialization `B=3`; values `B!=3` are a mathematical deformation family and are not claimed to be native Enterprise geometry.

## 1. Global odd-curvature filament

Let

`eps(r)=r mod 2` in `{0,1}`,

and for odd positive integer `B` define

`F_B(H,r)=H+(B*r^2+eps(r))/2`.

The numerator is always even, so `F_B(H,r)` is integer-valued.

Fix a start shell `R`, put

`chi=(-1)^R`,

`c=F_B(H,R)`.

Then every translated window value is exactly

`V_j=F_B(H,R+j)`

`=c+B*R*j+(B*j^2+chi*eps(j))/2`.

Thus the native `B=3` packet sits inside the one-parameter family

`quadratic drift + one C2 parity mode`.

## 2. Curvature and universal recurrence

For every `j`,

`V_j-2*V_(j+1)+V_(j+2)=B-chi*(-1)^j`.

Hence the two local curvatures are

`B-1` and `B+1`.

After centering by `B`, the curvature mode alternates by sign.

The whole sequence satisfies the `B`-independent fourth-order recurrence

`V_(j+4)-2*V_(j+3)+2*V_(j+1)-V_j=0`,

with characteristic polynomial

`(lambda-1)^3(lambda+1)`.

So changing `B` changes only the quadratic backbone, not the mode decomposition.

## 3. Exact finite-quotient cardinality

For modulus `M>=2`, let `C_(k,B)(M)` be the set of length-`k` residue words obtained from all integer `(H,R)`, with `k>=3`.

A word depends on `R` only through

`chi=(-1)^R`

and

`b=B*R mod M`.

Let

`g=gcd(B,M)`.

The exact effective period of `R` is

`L_(B,M)=lcm(2,M/g)`.

For every `M>2`, the first three coordinates recover the effective state, because after fixing the intercept the difference equations are

`Delta b + Delta s = 0 mod M`,

`2 Delta b = 0 mod M`,

where `Delta s` is `0,+1,-1`; since `M>2`, this forces `Delta s=Delta b=0`.

Therefore

`|C_(k,B)(M)|=M*lcm(2,M/gcd(B,M))` for every `M>2`.

At `M=2`, there are exactly two words:

- if `B=3 mod4`, the two constant words;
- if `B=1 mod4`, the two alternating words.

Thus

`|C_(k,B)(2)|=2`.

The count is independent of `k` once `k>=3`.

If `M|N`, reduction `C_(k,B)(N)->C_(k,B)(M)` is surjective with uniform fiber size

`(N/M)*(L_(B,N)/L_(B,M))`.

For a new prime `q` with `q` not dividing `B*M`, the fiber multiplier is exactly `q^2`.

## 4. Fixed-chirality affine MDS sheet

Let `q` be prime with

`q>max(2,k-1)`

and `q` not dividing `B`.

Fix one chirality `chi`. Since `B` is invertible mod `q`, the slope `B*R` runs over all of `F_q`.

Subtract the curvature offset

`eta_j^(B,chi)=(B*j^2+chi*eps(j))/2`.

Then

`W_j=V_j-eta_j^(B,chi)=a+b*j`.

Hence each fixed-chirality sheet is an affine translate of the `[k,2,k-1]` Reed-Solomon code.

This MDS statement is classical once the flattening identity is known; the deformation-specific content is the exact integer lock that produces it.

## 5. Exact zero-line concurrence formulas

For divisibility by an odd prime `q`, the `j`-th coordinate defines the parameter line

`L_j: a+b*j+eta_j^(B,chi)=0`.

Assume `q>k-1`, so the slopes `j` are distinct mod `q`.

### 5.1 Same-parity triples

For three distinct indices of one parity, the determinant is a nonzero Vandermonde factor times `B/2`.

Therefore a same-parity triple is concurrent mod `q^a` iff

`q^a | B`.

### 5.2 Mixed-parity triples

Let `u,v` be the two same-parity indices and `w` the opposite-parity index. Put

`e=eps(u)=eps(v)`.

Then the triple determinant is a unit Vandermonde factor times

`B*(w-u)*(w-v)+chi*(1-2*e)`.

Therefore the triple is concurrent mod `q^a` iff

`q^a | B*(w-u)*(w-v)+chi*(1-2*e)`.

## 6. Union discriminant across both chiralities

For `k>=5`, define the mixed-parity product

`D_(k,B)=B * product_T (B^2*A_T^2-1)`,

where `T` runs over mixed-parity triples and

`A_T=(w-u)*(w-v)`.

For every prime `q>k-1`:

`q is exceptional for at least one chirality`

iff

`q | D_(k,B)`.

The factor `B` records same-parity concurrence. The factors `B^2*A_T^2-1` record the two possible mixed-parity chiral concurrences.

For fixed `chi`, define the exact local depth

`nu_(q,k,B,chi)`

as the maximum of

- `v_q(B)` from same-parity triples;
- `v_q(B*A_T+chi*(1-2*e_T))` over mixed-parity triples.

Then, in the distinct-slope regime,

`defect at modulus q^a is nonzero`

iff

`a <= nu_(q,k,B,chi)`.

Thus the disappearance depth is exact, not merely bounded above.

## 7. Exceptional-prime cutoff away from divisors of B

For `k>=5`, the maximum possible absolute mixed-parity distance product is

`M_k=(k-1)(k-3)` for even `k`,

`M_k=(k-2)(k-4)` for odd `k`.

Every such product is odd. Since `B` is odd, every obstruction `B*A_T +-1` is even.

Therefore any odd exceptional prime `q` not dividing `B` satisfies

`q <= (B*M_k+1)/2`.

For the native specialization `B=3`, this recovers the cutoff staircase and, at `k=8,9`, the terminal bound `q<=53`.

## 8. Transparency formula for arbitrary B

Consider the full infinite filament modulo an odd prime `q>3` using transverse variable `H`.

Write `r=2m` or `2m+1`.

Then

`F_B(H,2m)=H+2*B*m^2`,

`F_B(H,2m+1)=H+(B*(2m+1)^2+1)/2`.

Call `H mod q` transparent if no value on either parity branch is divisible by `q`.

If `q|B`, the two branches are constant in the square variable and exactly two `H` classes are killed, so

`T_B(q)=q-2`.

If `q` does not divide `B`, the two root conditions reduce to two linear arguments of the quadratic character. Standard character sums give

`T_B(q)=[q-3 + Legendre(B/q)+Legendre(-B/q)]/4`.

Hence for every `q>=7`,

`T_B(q)>0`.

No prime `q>=7` is a universal single-channel breaker anywhere in this odd-curvature family.

## 9. Complete q=5 phase diagram

Modulo `5`:

### `B=0 mod5`

`T_B(5)=3`.

There are three transparent transverse classes.

### `B=+-1 mod5` (quadratic-residue phase)

`T_B(5)=1`.

There is exactly one transparent transverse class.

### `B=+-2 mod5` (quadratic-nonresidue phase)

`T_B(5)=0`.

Every transverse class is hit by a 5-divisible Cell.

Therefore

`5 is a universal breaker`

iff

`Legendre(B/5)=-1`.

This includes the native coefficient `B=3`.

## 10. Sharp length-nine cap in the breaker phase

Assume `Legendre(B/5)=-1`.

The sequence modulo `5` has period `10` in `r`. Since there are no transparent `H` classes, every period contains a zero, so every run of nonzero values has length at most `9`.

The bound is sharp in exactly two tangency channels:

- `H=0`: the even branch has the single double root `m=0`, while the odd branch has no root; the 9-run starts at `r=1 mod10`;
- `H=-1/2=2 mod5`: the odd branch has the single double root `2m+1=0`, while the even branch has no root; the 9-run starts at `r=6 mod10`.

Hence

`Legendre(B/5)=-1`

implies

`MAX CONSECUTIVE 5-COPRIME RUN LENGTH = 9`.

If `Legendre(B/5)=+1` or `5|B`, at least one transparent filament exists, so no finite run cap is forced by channel 5.

## 11. Finite-wheel dichotomy above the base channels

For every prime `q>=7`, at least one transparent class exists. Therefore, by CRT, any finite collection of such individually nonbreaking channels has a simultaneous transparent transverse class.

Consequently, after the base `2/3` selection:

- if `Legendre(B/5)=-1`, channel 5 alone breaks every long filament, with sharp local cap 9;
- otherwise, no finite collection of prime channels `q>=5` can break every filament.

This gives a one-parameter connectivity phase transition controlled entirely by `B mod5`.

## 12. Native interpretation

The Enterprise filament has `B=3`. Therefore

`three-sector shell geometry -> B=3`,

`Legendre(3/5)=-1`,

`-> channel 5 is the unique breaker above3`,

`-> sharp filament / island cap 9`.

So the constants `5` and `9` are not independent accidents: they are consequences of the curvature coefficient selected by the three-sector allocation.

## 13. Nonuniform p-adic depth outside the native specialization

The native `B=3`, `k<=9` exceptional channels all heal by the second residue layer because every relevant obstruction has q-adic valuation one.

This is not universal in the deformation family.

Example: `B=49`, `k=5`, `q=5`, negative chirality. One mixed-parity obstruction has 5-adic valuation two. Direct enumeration gives nonzero defect mod `5` and mod `25`, but zero defect mod `125`.

More generally, by choosing `B` in a prescribed residue class modulo `q^a`, mixed-parity obstruction depth can be made arbitrarily large while keeping `q` not dividing `B`.

Thus `q^2` healing is a rigid property of the native `B=3` packet, not of the whole odd-curvature family.

## 14. Boundary

The finite-field method, affine/MDS code theory, quadratic-character sums, CRT and arithmetic-arrangement language are classical.

No external novelty claim is made for those ingredients.

The research candidate is the exact coupled deformation law

`odd curvature coefficient B`

`-> quotient-code period`

`-> explicit arrangement discriminant / p-adic depth`

`-> Legendre(B/5) connectivity phase`

`-> sharp 9-cap in the nonresidue phase`.

External novelty remains unresolved pending independent statement-level literature review.