# Local-Law Modulus Design by Difference Spectra

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

Once a bounded local-law codebook has been identified, choosing a reflective modulus is a finite arithmetic problem. The key object is not the absolute size of the coefficients but the divisibility pattern of their **pairwise differences**.

This note develops the arithmetic layer independently from the weighted-machine semantics that consume it.

## 1. Difference-spectrum criterion

For a finite integer codebook S define

`D(S)={|u-v| : u,v in S, u!=v}`.

Reduction modulo M is injective on S iff

`M does not divide d`

for every `d in D(S)`.

Indeed,

`u==v mod M`

iff

`M | (u-v)`.

With contextual codebooks `{L_c}`, apply the criterion independently inside every context. Cross-context differences do not participate.

## 2. Bad moduli are finite divisor down-sets

For one finite contextual family, the bad-modulus set is

`B = union_c union_(d in D(L_c)) Divisors_ge_2(d)`.

Therefore B is finite.

The reflective moduli are its complement among integers `M>=2`.

If M is reflective and `M|N`, then N is reflective: if N divided one bad difference, M would divide it too.

Hence exact moduli form an upward-closed set in divisibility order.

## 3. Reflective moduli have no divisibility-least element

The upward-closed set is generally **not principal**.

Choose two distinct primes larger than every codebook difference. Both are reflective. Any divisibility-least reflective modulus would have to divide both primes, hence would have to be1, which is outside the nontrivial modulus world.

Thus every finite codebook family has:

- a least modulus under the external numeric cost order;
- no least element under the intrinsic divisibility precision order.

This is another instance where “minimum precision” depends on the chosen cost/order rather than being an intrinsic single object.

Meet closure can fail. For codebook `{0,6}`, mod4 and mod10 are reflective while their gcd2 is not.

## 4. Numeric optimization is bracketed by cardinality and width

For contextual codebooks `{L_c}` let

`K=max_c |L_c|`.

Any one modulus reflecting every codebook must have at least K residue classes:

`M >= K`.

A universal upper bound is

`M > max_c (max L_c - min L_c)`.

So the least numeric reflective modulus lies between a coding-cardinality lower bound and an interval-width upper bound.

Gaps in the codebook can make the lower end attainable. Example `{0,2,4}` has three values and is already reflected by mod3 even though its width is4.

## 5. Exact p-adic collision depth

Fix a prime p. For one difference d, mod `p^e` merges its endpoints exactly when

`e <= v_p(d)`.

Therefore the first p-adic exponent that reflects **all** contextual codebooks is

`e_p^* = 1 + max_(c,u!=v in L_c) v_p(u-v)`.

If all codebooks are singletons, exponent1 is already enough.

Thus a local-law codebook has a finite p-adic collision-depth spectrum across primes.

Example `S={0,2,4}`:

- at p=2, max valuation is2, so first exact level is mod8;
- at p=3, every nonzero difference has valuation0, so mod3 is exact immediately.

## 6. Repeated single primitive has a closed capacity law

Let the only primitive contribution be nonzero integer w and let at most d copies enter one local aggregate.

The codebook is

`{0,w,2w,...,dw}`.

The additive order of w modulo M is

`ord_M(w)=M/gcd(M,|w|)`.

Hence mod M is reflective exactly when

`M/gcd(M,|w|) > d`.

Equivalently, the maximum universally reflectable local multiplicity is

`capacity_M(w)=M/gcd(M,|w|)-1`.

This explains why absolute magnitude is not the controlling resource. For w=2 and d=2, mod3 is exact on `{0,2,4}` even though3 is smaller than the interval width+1 bound5.

## 7. Closed p-adic depth for one primitive

Write

`a=v_p(w)`.

For d>=1, the first p-adic exponent satisfying the single-primitive capacity condition is

`e_min = a + floor(log_p d) + 1`

or equivalently

`e_min = a + ceil(log_p(d+1))`.

Thus primitive p-divisibility consumes the first a p-adic layers before multiplicity resolution begins.

For example `w=12`, p=2, d=3:

`v_2(12)=2`,

so mod16 (`e=4`) is the first 2-adic level reflecting `0,w,2w,3w`.

## 8. Unit scaling does not change reflection

For any finite codebook S and integer scale c with

`gcd(c,M)=1`,

multiplication by c is a permutation of `Z/MZ`. Therefore

`S is reflected mod M`

iff

`cS is reflected mod M`.

So rescaling all primitive coefficients by a modular unit can change absolute magnitude drastically without changing the required residue precision at that modulus.

Scaling becomes relevant only through the prime factors shared with M.

## 9. CRT sensor families depend only on lcm

For moduli `M_1,...,M_k`, two integers have the same complete residue tuple iff they are congruent modulo

`L=lcm(M_1,...,M_k)`.

Therefore a pure modular sensor family reflects the contextual codebooks iff mod L does.

The lcm is the exact arithmetic content of the sensor family.

Redundant noncoprime sensors add carrier/storage overhead but no extra residue distinction beyond their lcm.

## 10. Modular sensor synergy

Several individually insufficient sensors can be jointly exact.

For codebook

`S={0,1,4}`:

- mod2 merges0 and4;
- mod3 merges1 and4;
- the pair `(mod2,mod3)` has lcm6 and distinguishes all three values.

Thus local-law precision can exhibit CRT synergy:

`insufficient channel + insufficient channel -> exact joint code`.

This is the pure-modular analogue of earlier semantic capability synergy.

## 11. Same lcm, different resource allocations

Although a modular sensor family has the same arithmetic content as one mod-L channel, their implementation costs differ.

A single large modulus concentrates numeric range in one channel. A CRT family distributes that range across several smaller channels that may be processed in parallel.

Thus arithmetic exactness depends only on lcm, while storage width, channel count, parallel execution and synchronization cost define an additional Pareto problem.

This is the natural bridge to the project's storage/execution-depth resource axis.

## 12. Precision-geometry contrast

Different exactness questions produce different up-set geometries.

Earlier affine uniform certification produced a principal up-set `{M:E|M}` with a unique divisibility-least modulus E when the free obstruction vanished.

Finite local-code reflection instead produces the complement of a finite divisor union. It is upward closed and cofinite but has no divisibility-least modulus.

So the phrase “higher modulus precision” is not enough to determine the geometry of exactness. The governing property decides which lattice region is admissible.

## 13. Next complexity boundary

If the available modular sensors are restricted to a declared prime set, choosing the smallest sensor subset whose joint lcm reflects all contextual differences becomes a covering problem.

Each prime sensor separates exactly the differences it does **not** divide. This turns constrained precision design into a finite set-cover/hitting problem and is the next owner-local frontier.

## Owner-local assets

- `src/enterprise_math/local_law_modulus_design.py`;
- `tests/test_local_law_modulus_design.py`;
- this bilingual theorem note.

## Prior art / status

Modular injectivity, divisibility lattices, p-adic valuations, additive order and CRT are standard prior number theory. P023/A2 retains precision/future-signature ownership. This Draft owns only the explicit finite-difference modulus-design specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
