# RSA-270 / PR #1330：独立提取、验证与修正

Status: `RESEARCH NOTE / INDEPENDENT SALVAGE / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-06T19:24:00+08:00`  
Source PR: `awdawmip/enterprise-math#1330` @ `26e294e23c974ce2e683b5419f522f0ede03f6e6`  
Base snapshot: `main@c98cdf1490fd79338b653ee93e766849fa7ddea3`  
Independent verifier: `experiments/rsa270_pr1330_salvage_verify.py`

## 0. Scope and assumption reset

This note does **not** adopt the PR's unpinned `P000` token as an authority. Every assumption used below is explicit:

- `H0`: `N=pq`, where `p<q` are distinct odd primes.
- `H1`: `H0` plus `p≡q≡1 (mod 3)`.
- `H2`: `H0` plus `p≡q≡2 (mod 3)`.

For RSA-270 the exact N-only residues used here are:

`N mod (3,6,8,9,16,18,24,27,36,72,144) = (1,1,7,1,7,1,7,19,19,55,55)`.

No RSA-270 factor is obtained or assumed.

Tool reuse resolution: `T0_BRC -> REUSE_APPLIED`, `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA -> REUSE_APPLIED`,
`T6_OPERATION_SAFE_QUOTIENT -> REUSE_APPLIED`, `T7_FINITE_SYMMETRY_EQUIVARIANCE -> REUSE_APPLIED`.
No new general-purpose tool family is proposed.

---

## 1. Results from #1330 that survive and can be strengthened

### 1.1 Exact two-plateau factor profile — KEEP

For odd `T`, define

`W_s(u)=sum_{j=0}^{s-2} u^(2-s+2j)`.

The bivariate coefficient identity used in #1330 gives, for `N=pq`,

`P_N(u)=2 W_((N+3)/2)(u)+2 W_((S+2)/2)(u)`, where `S=p+q`.

The first block is N-only; the second block has maximal exponent `(S-2)/2`. Hence

`S = 2*e_max + 2`

after the known outer block is removed, and then

`p,q = (S ± sqrt(S^2-4N))/2`.

This is an exact reformulation of factorization. It is valuable because it identifies the precise BRC provenance datum that must be extracted: the inner plateau boundary.

What it does **not** supply is a cheap way to compute that boundary from the product/source representation.

### 1.2 Exact coefficient-moment law — STRENGTHENED

The PR recorded only the quadratic energy

`sum_e P(e)^2 = 2(N+1)+6S`.

The complete moment family is:

**Theorem (profile moment law).** For every integer `r>=1`,

`M_r := sum_e P(e)^r = 2^(r-1) * [(N+1) + (2^r-1) S]`.

Proof: on the step-2 support, the inner overlap has `S/2` coefficients equal to `4`,
and the outer-only part has `(N+1-S)/2` coefficients equal to `2`. Therefore

`M_r = (N+1-S)/2 * 2^r + S/2 * 4^r`.

The verifier checks `r=1..6` on multiple semiprimes.

Consequence: all coefficient power moments are affine in `S`; if any one is independently observable, it is factorization-equivalent. This is a **proved family-specific statement**, not a universal “all observables” dichotomy.

### 1.3 Root-of-unity derivative law — KEEP, with a rigorous scope

At a primitive `m`-th root `zeta` (`m>=3`),

`W_s(u)=(u^(2-s)-u^s)/(1-u^2)`.

Differentiating and evaluating at `zeta`, with `r=s mod m`, gives exactly

`W'_s(zeta) = s A_m(r) + B_m(r)`

for periodic `A_m,B_m`, and

`A_m(r)=-(zeta^(1-r)+zeta^(r-1))/(1-zeta^2)`.

Therefore `A_m(r)=0` iff `4|m` and

`r = 1+m/4` or `r = 1+3m/4 (mod m)`.

More generally, for every fixed derivative order `k`,

`W_s^(k)(zeta_m)`

is a quasi-polynomial in `s` of degree at most `k` and period `m`: differentiation introduces falling-factorial polynomials in `s`, while all root-of-unity powers depend only on `s mod m`.

This is the correct replacement for the overbroad “every natural ladder family belongs to a universal dichotomy”.

### 1.4 Odd-multiplier profile lattice — NEW exact extension

Let `k` be odd with `gcd(k,N)=1`. Then the profile of `kN` decomposes exactly as

`P_(kN)(u) =
  2 * sum_{a|k} [
      W_((a+(k/a)N+2)/2)(u)
    + W_((a p+(k/a) q+2)/2)(u)
  ]`.

Thus each divisor split `k=a b` contributes a factor-bearing boundary

`L_a = (a p + b q - 2)/2`.

Paired with `L_b`:

`L_a + L_b = ((a+b)S - 4)/2`,
`L_a - L_b = (a-b)(p-q)/2`.

The verifier checks this exact decomposition for odd prime and composite multipliers, including `k=9,15,25,35`.

This rigorously generalizes the PR's prime-multiplier four-plateau formulas. Within this multiplier-profile class, all factor-bearing boundaries are rank-2 linear forms in `(p,q)`.

---

## 2. BRC V-trajectory: valuable, but it is multiplier-Fermat geometry

Define

`x_l = l p + q`,
`y_l = |l p - q|`.

Then exactly

`x_l^2 - 4 l N = y_l^2`.

So `(x_l,y_l)` is the exact Fermat endpoint for the multiplier `4lN`.

The V trajectory has

`y_l = p |l-r|`, where `r=q/p`,

and the exact distance from the Fermat square-root start is

`x_l - 2 sqrt(lN) = (sqrt(l p)-sqrt(q))^2
                   = p (sqrt(l)-sqrt(r))^2`.

Near `r=l`,

`x_l - 2 sqrt(lN) ~ p (l-r)^2/(4l)`.

Therefore:

- the V-function geometry is exact and useful as a cost coordinate;
- a fixed multiplier `l` gives a constant-factor improvement only when `r` is close to `l`;
- unless `|l-r|=o(1)` as N grows, the step count remains `Theta(sqrt(N))`;
- an `O(1)`-scale endpoint would require approximately `|l-r|=O(N^(-1/4))`.

So the V-route is not a new sub-square-root factorization method by itself; it is a precise Enterprise/BRC coordinate form of generalized Fermat/Lehman multiplier geometry.

Other exact identities survive as **certificates**:

`{x_l+y_l, x_l-y_l} = {2 l p, 2q}`,

and for `l1 != l2`,

`(x_l1-x_l2)(l1*x_l2-l2*x_l1) = (l1-l2)^2 N`.

These are useful consistency relations, but they add no independent information once exact endpoints are already known.

---

## 3. Forced residue lattice: corrected theorem

### 3.1 What N alone forces

For RSA-270, `N≡7 (mod 8)`. For odd `p,q` with `pq≡7 (mod8)`, necessarily

`S=p+q≡0 (mod8)`.

But modulo 3 there are two branches because `N≡1 (mod3)`:

- `H1`: `p,q≡1 (mod3)`;
- `H2`: `p,q≡2 (mod3)`.

Modulo 9:

- under `H1`, `S≡2 (mod9)`;
- under `H2`, `S≡7 (mod9)`.

By CRT:

- `H1 -> S≡56 (mod72)`;
- `H2 -> S≡16 (mod72)`.

Therefore the correct N-only statement is

`S mod72 ∈ {16,56}`,

not uniquely `16`, unless the additional `H2` branch is independently justified.

At modulus 144:

- `H1 -> S mod144 ∈ {56,128}`;
- `H2 -> S mod144 ∈ {16,88}`;
- without the branch bit: `{16,56,88,128}`.

The order-3 torsion / `QR(-3)` bit is precisely the kind of hidden factor bit that can select H1 versus H2; it is not automatically N-only computable.

### 3.2 “72 maximal” is salvageable only in a local model

Define the **local factor-residue model**: for a modulus `m` coprime to N, allow all unit pairs
`(a,b)` compatible with `ab≡N` modulo `lcm(m,6)` and, under H2, `a≡b≡2 (mod3)`.
A modulus is “unique-for-S” if every such local pair gives the same `a+b mod m`.

Under H2 for RSA-270:

- 2-adic uniqueness holds mod `8`, but mod `16` there are two S classes;
- 3-adic uniqueness holds mod `9`, but mod `27` there are two S classes;
- for every prime `r>=5`, `r∤N`, the map
  `f(a)=a+N a^(-1) (mod r)`
  has at least two values.

The last claim is exact because

`f(a)=f(b) <=> (a-b)(ab-N)=0 (mod r)`,

so every fiber has size at most two; for `r>=5`, the nonzero domain has at least four elements.

Hence any unique-for-S modulus in this local model divides

`2^3 * 3^2 = 72`.

Conversely H2 gives `S≡16 mod72`, so every divisor of 72 is unique.

**Correct theorem:** `72` is the maximal unique modulus in the stated H2 local factor-residue model.

This does **not** prove that 72 is a maximal modulus for every Enterprise/BRC/discrete observable.

Without H2, the corresponding unconditional forced modulus is only `8`.

---

## 4. The mod-72 alignment / “Rubik” program has a clean analytic theorem

Under H2, the complete ordered factor-residue fiber modulo 72 is

`F72 = {(5+6k, 11-6k) mod72 : k in Z/12Z}`,

12 states.

For a linear coordinate

`L_(a,b)(p,q)=a p+b q (mod72)`,

substitution gives

`L_(a,b)=constant + 6(a-b)k (mod72)`.

Therefore:

**Theorem (exact image law).**

`|L_(a,b)(F72)| = 12 / gcd(12,a-b)`.

This analytically proves all enumerated types in #1330:

- `a-b≡0 mod12` -> image size `1`;
- `a-b≡±2` -> `6`;
- `a-b≡±3` -> `4`;
- `a-b≡±4` -> `3`;
- `a-b≡6` -> `2`;
- `a-b≡±1,±5` -> `12`.

So the PR's `a≡b (mod12)` forced-coordinate criterion is correct **within this H2 mod-72 fiber**.

### Interpretation correction

A “forced coordinate” with image size 1 has **zero discrimination inside the 12-state fiber**.
It is a useful decoupled/known coordinate, not an information amplifier.

Moreover, any full unimodular `2x2` integer transform has determinant `±1`, hence is invertible modulo 72.
Applied to the pair `(p,q) mod72`, it preserves the joint 12-state fiber cardinality exactly.
A genuine SL(2,Z) change of frame can redistribute uncertainty between coordinates, but cannot create joint information.

The sum-gap map

`(p,q) -> (S,g)=(p+q,q-p)`

has determinant `2`, so it is **not** unimodular modulo 72.
On the H2 fiber it maps 12 factor states to 6 gap states:
`g mod72 ∈ {6,18,30,42,54,66}`.
The missing factor of two is a real 2-adic lift ambiguity, not new information.

Information accounting inside H2 mod72:

- factor-residue fiber uncertainty: `log2(12) ≈ 3.585` bits;
- S coordinate: constant, 0 discriminating bits;
- gap coordinate: 6 values, `log2(6) ≈ 2.585` bits;
- residual lift ambiguity: exactly 1 bit.

This replaces the PR's ambiguous “sum is optimal / 6.17-bit accounting” narrative.

---

## 5. Concrete falsifications / downgrades

### 5.1 SG4 62-point torsion “fingerprint” is not a candidate filter

The PR's torsion check compares two algebraically equivalent formulas built from the **same supplied S**.
Independent verification shows it passes deliberately wrong S values whose discriminant is not a square.

Examples checked across `m=3..64` include:

- `(N,S)=(35,100)`;
- `(35,156)`;
- `(143,168)`;
- `(391,184)`;
- `(899,204)`.

All fail the exact factor discriminant condition but pass the torsion identity.

Therefore:

`torsion_formula(S,N) == torsion_formula(S,N)`

is a formal consistency identity, not an independent fingerprint.

The original verifier rejects wrong candidates because it first performs the complete factor-recognition gate:

`(S/2)^2-N is a square -> reconstruct p,q -> check p*q=N`.

Correct verifier architecture must separate:

1. **Factor recognition** — discriminant square / product check; complete but not a search method.
2. **Derived identities** — torsion, V, Pluecker, etc.; conditional consistency only.
3. **Independent observations** — only values obtained without using the candidate S/p/q can add evidence.

### 5.2 The “one bit erased per digit” carry claim is false as stated

For the H2 3-adic local factor-residue model, exact ordered-pair counts and distinct S-class counts are:

| `3^t` | pair states | S classes |
|---:|---:|---:|
| 3 | 1 | 1 |
| 9 | 3 | 1 |
| 27 | 9 | 2 |
| 81 | 27 | 4 |
| 243 | 81 | **11** |
| 729 | 243 | **31** |
| 2187 | 729 | **92** |

Thus the shallow sequence `1,1,2,4` does **not** continue as doubling: at `3^5`, it is 11 rather than 8.

For the 2-adic tower the exact counts are:

pair states `1,2,4,8,16,...`,
S classes `1,1,1,2,4,8,...`.

After depth 3, both grow by one bit per layer; the state-count gap remains constant rather than “one new bit erased each digit”.

So the carry-automaton story should be demoted to a finite low-depth observation until a correct p-adic fiber theorem is proved.

### 5.3 “First layer is structureless” is too strong

Quantities such as

`x0(l)=ceil(2 sqrt(lN))`,
`d0(l)=x0(l)^2-4lN`

are indeed explicit N-only functions. That proves they do not use hidden factor data as input.
It does **not** prove they cannot correlate with, constrain, or algorithmically reveal the factor ratio.

The reported finite synthetic null results are legitimate empirical negatives, but not a theorem of uselessness.

### 5.4 Information-bit statement needs a convention correction

`log2(72)=6.1699` counts selection from all 72 residue classes, including the already-trivial parity restriction.

Since S is even:

- fixing one even class mod72 (H2) reduces 36 even classes to 1:
  gain beyond parity = `log2(36) ≈ 5.1699` bits;
- N-only `{16,56}` reduces 36 even classes to 2:
  gain beyond parity = `log2(18) ≈ 4.1699` bits.

So “6.17 N-only bits” is not an appropriate unconditional information statement.

---

## 6. Research direction after salvage

The strongest surviving research target is narrower and clearer than #1330's “closed observable algebra”:

> Can the factor-bearing inner boundary, or a nontrivial functional of the odd-multiplier boundary lattice, be computed from the product/source side **without already reconstructing S or an equivalent hidden-residuosity bit**?

Concrete continuation routes:

1. **Product-side boundary extraction.** Work directly on the bivariate generating object; seek coefficient transforms that retain endpoint/provenance rather than collapsing to divisor sums.
2. **Character/torsion classification with an independence gate.** A torsion value is useful only if it is computable independently from N; classify each specialization as easy congruence data, hidden character/residuosity data, or genuinely new computable data.
3. **Composite odd multipliers.** The exact `k`-multiplier profile produces a divisor-indexed family of linear forms. Search for interference/collision functionals that are computable from N and not algebraically determined by the already-known outer blocks.
4. **p-adic factor-fiber analysis.** Replace the incorrect bit-per-digit narrative with the exact image theory of `a -> a+N/a` over `Z/p^t Z`; study branch points through the discriminant `S^2-4N`.
5. **BRC operation-safe quotient.** Explicitly mark which collapses preserve independent provenance and which merely re-express a candidate S. This prevents a derived identity from being mistaken for a search observable.

Current frontier: several exact structural results survive and are stronger after correction, but no independent N-only observable has yet crossed the factorization barrier.

No RSA-270 factor was obtained.
