# RSA-270 bivariate Enterprise-layer factor profile and quadratic-residuosity barrier

Progress-Event-ID: `20260906T105500+0800-rsa270-bivariate-factor-profile-qr-barrier-91ad72`
At: `2026-09-06T10:55:00+08:00`
Scope: `enterprise-math / RSA-270 / multi-layer BRC collapse`
Source: `current ChatGPT TASK research; Ramanujan/Kac-Cheung product identity; exact symbolic derivation; bounded integer probes`
Kind: `PROGRESS / EXACT REDUCTION / BARRIER`

## Event

Continued the user's low-compute multi-layer-collapse route rather than enlarging Fermat/ECM/NFS searches.

### 1. The four-layer sigma collapse admits a provenance-preserving bivariate lift

Start from the Ramanujan product identity (Kac-Cheung, Quantum Calculus, Eq. 15.7), replace the base variable by `Q^2`, set `z=Q*u`, and divide by the vanishing factor `1-u^(-2)`. After pairing the `(m-1,n-1)` term from the positive double sum with the `(m,n)` term from the negative double sum, one obtains the exact Laurent-series identity

`F(Q,u) = sum_{m,n>=1} W_{m+n}(u) Q^(2mn-m-n)`,

where

`W_s(u)=(u^(s-2)-u^(-s))/(1-u^(-2)) = sum_{j=0}^{s-2} u^(2-s+2j)`.

Equivalently the product side is

`F(Q,u)=prod_{n>=1} ((1-Q^(2n))^2 (1-u^2 Q^(2n))(1-u^(-2) Q^(2n))) / ((1-u Q^(2n-1))^2(1-u^(-1) Q^(2n-1))^2)`.

At `u=1`, `W_s(1)=s-1`, and the identity reduces to the classical four-triangular-number formula.

For odd target `N`, let `M=(N-1)/2`. The coefficient condition

`2mn-m-n=M`

is exactly

`(2m-1)(2n-1)=N`.

Therefore the coefficient profile is

`[Q^M]F(Q,u) = sum_{d|N} W_{(d+N/d+2)/2}(u)`.

This is a provenance-preserving BRC lift of the total mass `sigma(N)`: each divisor-pair branch retains a one-dimensional Laurent block instead of being collapsed to one scalar.

### 2. For a distinct odd semiprime the profile is exactly two nested plateaus

For `N=pq`, `p<q`, write `S=p+q`. The four divisors `1,p,q,N` give

`[Q^M]F(Q,u) = 2 W_{(N+3)/2}(u) + 2 W_{(S+2)/2}(u)`.

The first block is completely known from N. The second block is factor-bearing. Because `(p-1)(q-1)/2` is even, the two Laurent lattices have matching parity. Hence the coefficient profile has value 2 on the outer known block and value 4 on the central overlap.

After subtracting the known block, the unknown factor block has maximal Laurent exponent

`e_max=(S-2)/2`.

Thus

`S=2 e_max+2`,

and `p,q` follow from `x^2-Sx+N=0`.

This strengthens the earlier scalar observer `sigma(N)`: factoring is equivalent to locating one exact BRC plateau boundary in the bivariate Enterprise-layer coefficient profile.

### 3. Root-of-unity collapse reaches quadratic residuosity, not an easy local invariant

Let `omega` be a primitive cube root of unity. Then

`W_s(omega)=1` for `s=2 mod 3`, `-1` for `s=0 mod 3`, and `0` for `s=1 mod 3`.

For an RSA semiprime with `N=1 mod 6`, the prime factors are either both `1 mod 3` or both `2 mod 3`. The specialized coefficient satisfies

`[Q^M]F(Q,omega)=4` if `p=q=1 mod 3`,

`[Q^M]F(Q,omega)=0` if `p=q=2 mod 3`.

For a prime `r>3`, `(-3/r)=+1` iff `r=1 mod 3`. Therefore, under the semiprime promise and `N=1 mod 6`, this torsion specialization exactly decides whether `-3` is a genuine quadratic residue modulo N versus a Jacobi-+1 pseudosquare. This is the standard quadratic-residuosity decision problem over an RSA modulus, for which no efficient general algorithm is known without factorization.

So the first nontrivial torsion compression of the exact factor profile does retain a hidden factor bit, but that bit lands on a known cryptographic hardness boundary rather than becoming a cheap modular observable.

### 4. Low-cost RSA-270 probes were negative

RSA-270 has `N=1 mod 6`. Cheap gcd probes were performed for small bases/discriminants using exponents derived from `(N-1)/2`, `(N-1)/3`, `(N-1)/6`, and available small divisors of `N+1`; no `gcd(a^E +/- 1,N)` produced a nontrivial factor. Extending the `(N-1)/2` probe across all primes below 2000 also produced no nontrivial gcd (sub-second bounded test).

Separately, cyclic Frobenius masks aligned with X6 C6/C12 scales were checked at `r=24,30,36`; seven small instances produced no factor. For the equally spaced six-point subgroup mask, the group-algebra observer collapses exactly to the scalar condition `gcd(6^(N-1)-1,N)`, which equals 1 for RSA-270. Thus excessive X6 symmetry erases the needed provenance and reduces to ordinary Fermat/order information.

A small balanced-semiprime calibration also rejected a tempting shortcut from one four-square path: simple linear/pairwise/quaternion-like coordinate gcd statistics that had high hit rates for tiny factors fell to roughly 1-3% already when factors were only a few hundred, consistent with accidental divisibility rather than a scale-stable factor law. This route should not be extrapolated to 448-bit factors.

### 5. Current exact frontier

The multi-layer route now has a sharp target:

`FOUR_ENTERPRISE_LAYERS -> BIVARIATE_PROVENANCE_PROFILE -> KNOWN_OUTER_BLOCK + FACTOR_BLOCK -> p+q -> factors`.

What remains is not more search depth. It is an algorithm for extracting the central plateau boundary (or an equivalent marked coefficient) from the product/source side without enumerating O(sqrt(N)) or O(N) states. Root-of-unity/local-modulus compression alone cannot be assumed easy; the order-3 specialization already realizes quadratic residuosity.

No RSA-270 factor was obtained.

## Artifacts

- Previous current-turn journal: `journal/enterprise-math/2026-09-06/20260906T104500+0800-rsa270-x6-four-layer-triangular-collapse-6f8c31.md`.
- Parallel X6 Lucas/Frobenius frontier: `journal/enterprise-math/2026-09-06/20260906T103843+0800-x6-layer-gcd-lucas-frobenius-frontier.md`.
- Classical source identity: Kac and Cheung, `Quantum Calculus`, Eq. 15.7 and the subsequent proof of the four-triangular-number divisor-sum formula; classical prior art, not an Enterprise novelty claim.

## Next

Do not enlarge brute-force `k,j`, ECM curves, or cyclic ring sizes. Investigate whether the bivariate product `F(Q,u)` has any torsion/derivative specialization whose `Q^M` coefficient is both (a) provably factor-sensitive and (b) computable from N in sub-factorization cost. In particular classify low-order torsion specializations as easy congruence data, quadratic/cubic residuosity-type hard bits, or genuine new compressible observers. If all nontrivial specializations reduce to hidden-residuosity/Hecke coefficient problems, record a no-go and preserve the exact two-plateau factor profile as the terminal BRC reformulation.