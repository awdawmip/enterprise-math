# Native Enterprise affine-code survivor basins: logarithmic thinning law

Status: `FREE_RESEARCH_EXACT_LOCAL_PRODUCT_ASYMPTOTIC / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_CURVATURE_FLATTENED_AFFINE_MDS_CODE_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_ARRANGEMENT_DISCRIMINANT_STAIRCASE_20260824.md`;
- `NATIVE_ENTERPRISE_SHARP9_AFFINE_CODE_CRT_TOWER_D3_D19_20260824.md`.

## 1. Local survivor fraction

For a fixed length-k filament code and chirality chi, let

`N_k(q,chi)`

be the number of parameter states in `F_q^2` for which no coordinate vanishes modulo q.

Beyond the finite arrangement-discriminant support, the affine-MDS weight spectrum gives exactly

`N_k(q,chi)=q^2-k*q+C(k,2)`.

Hence the generic local survivor fraction is

`delta_k(q)=1-k/q+C(k,2)/q^2`.

## 2. Exact second-order match to k independent unit conditions

The ordinary independent-unit factor is

`(1-1/q)^k`.

Its binomial expansion begins

`1-k/q+C(k,2)/q^2-C(k,3)/q^3+...`.

Therefore the geometry-selected affine-MDS factor agrees with the independent k-coordinate factor through order `q^-2`:

`delta_k(q)/(1-1/q)^k = 1+O(q^-3)`.

Because the sum over primes of `q^-3` converges, the infinite product of these ratios converges absolutely.

This stronger `O(q^-3)` tail is selected by the no-triple-concurrence/MDS geometry; a generic unrelated local model would only be guaranteed to match at first order.

## 3. Product law

Let

`D_k^chi(x)=product_{q<=x} N_k(q,chi)/q^2`,

with the finite small-prime conditioning appropriate to the chosen native filament channel.

There is a positive finite constant `S_k^chi` such that

`D_k^chi(x) ~ S_k^chi * product_{q<=x}(1-1/q)^k`.

By Mertens' product theorem,

`D_k^chi(x) ~ S_k^chi * e^(-k*gamma)/(log x)^k`.

Thus the local CRT survivor basin has logarithmic thinning exponent exactly equal to the number k of Cell values required to survive.

Freeze:

`FILAMENT WINDOW SIZE k -> COLLAPSE-BASIN DENSITY EXPONENT k`.

## 4. Collapse-channel dimension

At arithmetic collapse dimension d, take `x=p_d`, the d-th prime channel.

Then

`D_k^chi(p_d) asymptotic (constant)/(log p_d)^k`.

Using the prime-number growth `p_d~d log d`, this is equivalently a `log(d)^(-k)` thinning law up to lower-order logarithms.

The absolute CRT state count still grows rapidly because the ambient parameter plane has size approximately the square of the primorial modulus; the theorem concerns the shrinking fraction occupied by all-channel survivor states.

## 5. Maximal sharp-nine law

For the sharp global island `k=9`:

`D_9^chi(x) ~ constant_chi/(log x)^9`.

The two chiral constants differ only through q=13 and q=23. Their exact ratio is

`S_9^+/S_9^- = 29736/30005`.

Every later generic channel contributes the same factor to both chiralities, so the ratio is frozen while the common density continues to thin as `log(x)^(-9)`.

The finite d=19 basin table is the initial exact segment of this asymptotic product law.

## 6. General island hierarchy

For the realized long-island sizes

`k=5,6,7,8,9`,

the corresponding high-dimensional local basin exponents are

`5,6,7,8,9`.

Therefore the native tight-path island hierarchy carries a matched density hierarchy:

`longer exact prime-incidence packet -> higher logarithmic collapse codimension`.

## 7. Boundary

Mertens products and singular-series normalization are classical. This note does not claim a new prime-tuple asymptotic for actual all-prime islands.

The exact research-specific input is the native affine-MDS local count

`q^2-kq+C(k,2)`

beyond a finite geometry-selected exceptional spectrum, which forces the logarithmic thinning exponent of the high-dimensional candidate basin.
