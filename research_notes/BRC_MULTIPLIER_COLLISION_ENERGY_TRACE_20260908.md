# BRC Multiplier Collision-Energy Trace — General Second-Moment Reduction

Status: `RESEARCH FRONTIER / EXACT TRACE IDENTITY + EXACT RESIDUE SHADOW + FINITE COMPRESSION COUNTEREXAMPLES / NO FACTORIZATION SPEEDUP CLAIM`
Date: `2026-09-08`
Parent: `research_notes/BRC_MULTIPLIER_BOUNDARY_COLLISION_SPECTRUM_20260908.md`
Project source parent: `main@c5d6e6ed4aa4c899706e2a895f55733dc2eb3cb8`

## 0. Purpose

The parent note showed that the hidden boundary distance spectrum of only `m in {1,3}` is already factorization-equivalent. This continuation asks whether the full spectrum is actually necessary.

Answer: **no**. On every symmetric odd-multiplier horizon, the complete pairwise squared-distance spectrum collapses to one known affine form in `S^2=(p+q)^2` and `N=pq`. A single exact second moment is enough to factor.

This is an oracle reduction and observer audit, not an N-only factorization algorithm.

## 1. Centered coefficient lattice

Let `N=pq` with distinct odd coprime `1<p<q`, and

`L_(a,b)=(ap+bq-2)/2`

for positive odd multiplier-split coordinates `(a,b)`.

Use the baseline

`A=L_(1,1)=(p+q-2)/2`.

Write

`a=2r+1`, `b=2s+1`,

with `r,s>=0`. Then the centered hidden boundary is exactly

`X_(r,s)=L_(a,b)-A = r p+s q`.

For horizon `K`, define the known coefficient domain

`C_K={(r,s) in N_0^2 : (2r+1)(2s+1)<=K}`.

It is symmetric under `(r,s)<->(s,r)`.

This exposes the core geometry directly: the hidden multiplier-boundary family is the image of a known two-dimensional integer coefficient set under the unknown linear functional

`(r,s) -> rp+sq`.

Already at `K=3`, `C_3` contains the basis simplex

`{(0,0),(1,0),(0,1)}`,

whose images are `{0,p,q}`. Thus any observer that preserves that centered three-point geometry is factorization-equivalent.

## 2. General collision-energy trace theorem

Let

`n_K = #C_K`,

`U_K = sum_(r,s in C_K) r = sum s`,

`V_K = sum r^2 = sum s^2`,

`W_K = sum rs`.

The equalities follow from coordinate-swap symmetry.

Define the full pairwise squared-distance energy

`E_K = sum_{i<j} (X_i-X_j)^2`.

Using the standard identity

`sum_{i<j}(x_i-x_j)^2 = n sum_i x_i^2-(sum_i x_i)^2`,

we obtain

`sum X_i = U_K(p+q)=U_K S`,

and

`sum X_i^2 = V_K(p^2+q^2)+2W_Kpq`

`=V_K(S^2-2N)+2W_KN`.

Therefore exactly

`E_K = A_K S^2+B_K N`,

where

`A_K = n_K V_K-U_K^2`,

`B_K = 2 n_K (W_K-V_K)`.

For every `K>=3`, `C_K` contains coefficient values with distinct first coordinate, so

`A_K=n_K^2 Var(r)>0`.

Hence

`S^2 = (E_K-B_K N)/A_K`.

**Conclusion:** for every symmetric odd-multiplier horizon `K>=3`, one exact scalar collision-energy trace is sufficient for factor recovery.

## 3. Small-horizon checks

### `K=3`

`C_3={(0,0),(1,0),(0,1)}`.

Then

`n=3, U=1, V=1, W=0`,

so

`A_3=2`, `B_3=-6`,

and

`E_3=2S^2-6N`.

This is the parent note's three-boundary identity.

### `K=5`

`C_5={(0,0),(1,0),(0,1),(2,0),(0,2)}`.

Then

`n=5, U=3, V=5, W=0`,

so

`A_5=16`, `B_5=-50`,

and

`E_5=16S^2-50N`.

This matches the five-boundary distance calculation independently.

A finite coefficient check also produced, for example,

`K=100: n=155, U=1474, V=42418, W=598`,

`A_100=4402114`, `B_100=-12964200`.

The large coefficients do not create additional factor information; they only rescale the same unknown `S^2`.

## 4. Multi-horizon second moments are rank one over the unknown factor data

For any two horizons `i,j`,

`E_i=A_i S^2+B_iN`,

`E_j=A_j S^2+B_jN`.

Eliminating `S^2` gives the exact N-only consistency identity

`A_j E_i-A_i E_j=(A_j B_i-A_i B_j)N`.

Therefore a whole trajectory of exact second moments across many `K` values contains only **one unknown scalar degree of freedom** once `N` is known.

This kills the idea that second-moment growth across `K` could independently triangulate `(p,q)`: one exact horizon already suffices, and further horizons are redundant consistency checks.

The earlier multi-`K` multiplicity-growth idea remains potentially useful only for a **partial/unlabeled line spectrum**, where the goal is to identify which coefficient vector generated a line. It adds nothing to the full second-moment trace.

## 5. Pure-split homothety: larger odd multipliers do not improve the three-point shape

For any odd `k`, consider only the baseline and the two pure splits

`(1,1)`, `(k,1)`, `(1,k)`.

Let

`c=(k-1)/2`.

After centering at `L_(1,1)`, the three positions are

`{0, cp, cq}`.

Thus every such three-point spectrum is a homothetic copy of the `k=3` spectrum, and its squared-distance energy is simply

`c^2 E_3`.

So expanding through prime multipliers or pure factor splits alone cannot generate a new independent collision coordinate. New shape enters only through genuinely mixed composite splits `(a,b)` with both coordinates above one, and even their **global second moment** still collapses to the same `S^2` trace above.

## 6. First exact N-only shadow of hidden collision energy — but only a classical residue facade

There is nevertheless a small exact part of the hidden energy that can be computed from `N` alone.

Observe

`(N+1)^2-S^2`

`=(pq+1)^2-(p+q)^2`

`=(p^2-1)(q^2-1)`.

### Arbitrary odd factors

For every odd integer `x`, `x^2-1` is divisible by `8`. Hence

`64 | (p^2-1)(q^2-1)`,

so

`S^2 == (N+1)^2 (mod 64)`.

For `K=3`, this gives the exact N-only hidden-energy shadow

`E_3 == 2(N^2-N+1) (mod 128)`.

### Distinct odd prime factors above 3

For every prime `p>3`, `p^2-1` is divisible by `24`. Therefore

`576 | (p^2-1)(q^2-1)`,

and

`S^2 == (N+1)^2 (mod 576)`.

Consequently

`E_3 == 2(N^2-N+1) (mod 1152)`.

More generally, the energy-trace theorem gives

`E_K == A_K (N+1)^2+B_K N (mod 576 A_K)`

for prime factors above 3.

The apparently growing modulus `576 A_K` is deceptive. After dividing by the known scale `A_K`, it supplies only the fixed congruence

`S^2 == (N+1)^2 (mod 576)`.

Thus increasing `K` does **not** accumulate new hidden bits through this universal residue shadow.

This is a useful exact regression baseline but remains classical modular arithmetic, not a new BRC factoring leak.

## 7. Precision barrier for approximate collision energy

Suppose an N-only proxy returns `E_K` only approximately. Since

`S^2=(E_K-B_KN)/A_K`,

an energy error `delta E` induces squared-sum error `delta E/A_K`.

Because `p,q` are odd, `S` is even. The nearest distinct admissible even square below `S^2` is `(S-2)^2`, separated by

`4S-4`.

A sufficient unique-rounding condition is therefore

`|delta E| < A_K(2S-2)`.

For balanced semiprimes, `S=Theta(sqrt(N))` while the energy scale is `Theta(A_K N)`, so a generic approximate observer needs relative accuracy on the order of

`N^(-1/2)`

to close the factor exactly. This is roughly half the modulus bit-length in effective precision. Coarse spectral averages are therefore not enough merely because they correlate with the exact energy.

## 8. Finite compressed-state counterexamples

The current project already recorded that cheap BRC shadow classifiers did not retain stable held-out multiplier-routing gain. The collision-energy target gives a sharper observer-loss test.

### One-state shadow at modulus 256

Using the exact shadow tuple

`(N mod 256, floor(sqrt(N)) mod 256, R_1 mod 256, phase_quartile)`,

both prime semiprimes

`N_1=131*149=19519`

and

`N_2=167*937=156479`

produce the same tuple

`(63,139,198,2)`,

but their hidden three-point energies satisfy

`E_3(N_1) == 6 (mod 256)`,

`E_3(N_2) == 134 (mod 256)`.

So that compressed shadow cannot determine the next 2-adic lift of the collision energy.

### Enriched `m=1,3` root/remainder residues at modulus 127

The two prime semiprimes

`N_1=2503*10079=25227737`,

`N_2=1327*19009=25224943`

share the residue tuple

`(N mod127, J_1 mod127, R_1 mod127, J_3 mod127, R_3 mod127)`

`=(76,69,14,63,69)`,

but

`E_3(N_1) == 87 (mod127)`,

`E_3(N_2) == 56 (mod127)`.

Thus even this enriched fixed-modulus root/remainder compression does not determine the hidden collision-energy residue.

These are exact finite collision witnesses for the declared compressed signatures, not general lower bounds against every possible N-visible BRC algorithm.

## 9. Near-collision scaling checkpoint

If no aggregate hidden-spectrum observer exists and one instead searches a known coefficient pair `(r,s)` with

`|rp-sq|`

small, then `r/s` approximates `q/p`.

For balanced factors, recovering `p` by rounding from an estimated ratio requires ratio error on the order of `1/p`. Generic continued-fraction/Dirichlet quality at denominator horizon `H` is on the order of `1/H^2`, suggesting

`H ~ sqrt(p) ~ N^(1/4)`.

This is a scaling diagnostic, not an asymptotic lower-bound proof. It explains why a near-collision-only search naturally falls back into classical Lehman/Diophantine territory rather than producing an obvious polylogarithmic RSA shortcut.

## 10. Revised research frontier

The collision line now has four sharply separated levels:

1. `EXACT_COLLISION_COUNT` — first nontrivial event occurs only at `K=2q+1`, factor scale.
2. `NEAR_COLLISION_SEARCH` — classical rational balancing; generic horizon suggests `N^(1/4)` behavior.
3. `FULL_OR_SECOND_MOMENT_HIDDEN_SPECTRUM` — already factorization-equivalent at `K=3`.
4. `UNIVERSAL_N_ONLY_RESIDUE_SHADOW` — exact but collapses to fixed classical congruence `S^2=(N+1)^2 mod 576` for RSA-type primes.

The only genuinely open BRC attack surface is therefore:

> construct an N-visible operator that recovers **more than the universal residue shadow** of the hidden three-point energy, without materializing a factor-equivalent boundary, and quantify whether that extra information can be lifted faster than `N^(1/4)`-scale rational balancing.

Kill any candidate that merely rescales the fixed modulo-576 congruence, reuses the known coarse `N/J/R` shadow, or requires already-known factor-split provenance.

No Foundation promotion, Working Truth promotion, or factorization-complexity improvement is claimed.