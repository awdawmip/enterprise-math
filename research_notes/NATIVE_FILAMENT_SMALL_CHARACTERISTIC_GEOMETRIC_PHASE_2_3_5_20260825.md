# Native filament small-characteristic geometric phase: parity, degeneration, regular orbit

Status: `FREE_RESEARCH_EXACT_PHASE_REINTERPRETATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on the split-hyperbola quotient theorem.

## 1. Why the breaker spectrum is not three copies of one phenomenon

The audited breaker classification says that only the prime channels

`2,3,5`

can be universal breakers in the odd-curvature family.

The split-hyperbola bridge shows that these three channels have genuinely different geometric meanings.

## 2. Channel 2: parity singularity

Characteristic two lies outside the odd-field split-hyperbola theory because `2` is not invertible and the difference-of-squares linear bridge

`(x,y)->(y-x,y+x)`

collapses.

For odd `B`, the exact native sequence modulo `2` is controlled by `B mod4`:

- `B=1 mod4`: the two shell parities cover both residues, so channel2 is a breaker;
- `B=3 mod4`: one transparent residue remains.

Thus channel2 is a **parity/chirality singularity**, not a nonsingular hyperbola orbit collapse.

## 3. Channel 3: automatic nonsingular breaker versus B-degeneration

Assume first `3 does not divide B`.

The translated-parabola split hyperbola has exactly

`q-1=2`

points over `F_3`.

The local symmetry group has order four, so the two-point hyperbola necessarily forms one symmetry orbit in the quotient relevant to dual overlap.

Equivalently the overlap count is one and transparency count is zero.

Hence every nonsingular translated quadratic pair is automatically breaking at `q=3`.

Now suppose

`3|B`.

Then the quadratic square-variable coefficient vanishes modulo3. The two parity branch hit maps degenerate to two singleton values rather than a nonsingular two-parabola pair.

Their union has only two of the three field elements, so exactly one transparent transverse class survives.

Thus:

`q=3 breaker iff 3 does not divide B`.

Geometric interpretation:

`B divisible by3` **turns off** the otherwise automatic two-point hyperbola breaker by degenerating the quadratic backbone.

## 4. Channel 5: first possible regular K4 breaker

Assume `5 does not divide B`.

The nonsingular split hyperbola has

`q-1=4`

points, exactly the order of the local symmetry group

`K_4`.

Therefore `q=5` is the first characteristic in which a nonsingular hyperbola can be one **regular** local-symmetry orbit.

The action is regular exactly when neither exchange nor signed-exchange has a fixed point, equivalently when the relevant square tests are both negative.

For the native unit vertical shift this is

`Legendre(B/5)=-1`.

If the condition holds, the quotient has one value and channel5 breaks.

If it fails, the four hyperbola points split into multiple symmetry orbits and at least one transparent class remains.

If `5|B`, the quadratic backbone degenerates to the two singleton hit values and three transparent classes remain.

Thus:

`q=5 breaker iff Legendre(B/5)=-1`.

## 5. No later breaker

For every nonsingular odd characteristic `q>=7`,

`|H(F_q)|=q-1>4=|K_4|`.

Therefore the complete hyperbola cannot be one local-symmetry orbit.

If instead `q|B`, the square dependence degenerates and only two transverse classes are hit, again leaving transparency.

Hence no prime `q>=7` can break.

## 6. Native B=3 phase chain

The actual tri-sector coefficient is

`B=3`.

It satisfies three geometrically distinct conditions:

### At 2

`3=3 mod4`, so the parity layer leaves one transparent class.

### At 3

`3|B`, so the quadratic backbone degenerates and switches off the automatic nonsingular q=3 breaker.

### At 5

`B` is invertible and

`Legendre(3/5)=-1`,

so the four-point split hyperbola becomes one regular `K_4` orbit.

Therefore

`FIRST BREAKER(B=3)=5`.

Freeze the geometric reading:

`SURVIVE PARITY AT2`

`-> DEGENERATE THE AUTOMATIC HYPERBOLA BREAKER AT3`

`-> REGULAR K4 ORBIT AT5`.

## 7. Why 3 is extremal in the odd-sector family

Under the odd-sector allocator, `B=s`.

To postpone a finite breaker until5, an odd sector count must simultaneously:

1. avoid the parity breaker at2: `s=3 mod4`;
2. degenerate the automatic nonsingular breaker at3: `3|s`;
3. enter the regular-orbit breaker at5: `Legendre(s/5)=-1`.

The smallest positive odd `s` satisfying all three is

`s=3`.

Thus the extremality of the tri-sector count is not only a residue-table fact. It is the smallest parameter that passes through three different geometric regimes in the required order.

## 8. Prior-art boundary

Characteristic degeneration, finite group orbits, quadratic residues and conic duality are classical.

The research-specific candidate is the exact selection of this three-stage phase sequence by the native/odd-sector shell allocation.