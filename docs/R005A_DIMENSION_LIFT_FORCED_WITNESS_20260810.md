# R005-A / R005-B — Prime Dimension Lift to Forced Screening Cores

Status: `PROVED ELEMENTARY TRANSPORT + ANALYTIC COROLLARY FROM ESTABLISHED BHP / EXACT BOUNDED CHECK / NOT CANONICAL`  
Date: `2026-08-10`

## 1. T-A9 — exact prime-to-forced-core dimension lift

Let

`I_{p,k}={n:k^p<n<(k+1)^p}`.

Let `m>=1`, `r>=2`, `p=m*r`.  If a prime `q` lies in `I_{m,k}`, then monotonicity of powers gives

`k^(m*r) < q^r < (k+1)^(m*r)`.

Thus `q^r in I_{p,k}`.  The composite `q^r` has exactly one distinct prime divisor, namely `q`.  Also `q^2<=q^r<(k+1)^p`, so `q` is below the p-basin square-root screening horizon.  Hence `q^r` is an exclusive divisor-witness collision and `q` is forced in the p-basin witness language.

Therefore:

`PrimeSet_m(k) -> ForcedCore_(m*r)(k)`

by the injection `q -> q^r`, and

`|ForcedCore_(m*r,k)| >= P_m(k)`.

This is one-way.  Higher-dimensional forced cores can contain additional witnesses forced by non-pure collisions such as `q*s` with a prime cofactor `s` above the screening horizon.

## 2. Even-exponent square lift

For `r=2`:

`q prime in I_{m,k} -> q^2 exclusive collision in I_{2m,k}`.

Examples: primes `5,7` in `4<q<9` lift to the forced collisions `25,49` in `16<n<81`.

The p=2 case is degenerate: its only lower integer exponent is m=1, but `k<q<k+1` contains no integer.  So the square basin has no nontrivial inherited pure-power witness core from a smaller positive integer exponent.  This does not say square basins have no forced witnesses; semiprime-type exclusive collisions can still force them.

## 3. Coupling to R005-B prime count

R005-B already provides an exact finite formula for the m-basin prime count `P_m(k)`.  T-A9 transports that count into a guaranteed high-dimensional mandatory-observation lower bound:

`|ForcedCore_(m*r,k)| >= P_m(k)`.

Hence a lower-dimensional prime count also measures an embedded component of the higher-dimensional minimum witness language.

Ownership remains separated: R005-B owns p-power basin/factor-horizon/counting structure; R005-A owns witness-core semantics.

## 4. Exact bounded check through upper endpoint 4,004,000

The transport was checked against independently computed forced cores.

| lower m | lift power r | upper p | high basins checked | lifted prime instances |
|---:|---:|---:|---:|---:|
| 2 | 2 | 4 | 42 | 293 |
| 3 | 2 | 6 | 10 | 265 |
| 2 | 3 | 6 | 10 | 32 |
| 4 | 2 | 8 | 4 | 204 |
| 2 | 4 | 8 | 4 | 9 |

All exact assertions passed.

A forcing-saturation scan in the same bound found:

- p=2: not all candidate witnesses forced; first non-full basin k=6, missing witness 5;
- p=3: not all candidate witnesses forced; first non-full basin k=23, missing witness 109;
- p=4,5,6,7,8: every candidate witness was forced in every scanned basin.

The p=4 observation is bounded evidence only.

## 5. T-A10 — asymptotic forcing saturation for every fixed p>=5

Use Baker–Harman–Pintz, *The Difference Between Consecutive Primes, II*, Proc. London Math. Soc. 83 (2001), 532–562, DOI `10.1112/plms/83.3.532`: for all sufficiently large x, `[x,x+x^0.525]` contains a prime.

Fix integer p>=5.  For the p-basin let

- `A=k^p`,
- `U=(k+1)^p-1`,
- `F=floor(sqrt(U))`.

Take any candidate prime witness `q<=F`.

### Case 1: q^2>A

Then `A<q^2<=F^2<=U`, so q^2 itself is an exclusive collision.  Hence q is forced.

### Case 2: q^2<=A

Then q<=sqrt(A).  Seek a prime cofactor r>F with `A<q*r<=U`.  Such q*r is an exclusive collision for q.

If `A/q>=F`, the available cofactor interval has length `(U-A)/q`.  Relative to `x=A/q`, its ratio to `x^0.525` is uniformly bounded below, up to fixed-p constants, by

`k^((1-0.525)*p/2-1)=k^(0.2375*p-1)`.

If `A/q<F`, the worst case is q near sqrt(A), and the post-horizon room `U/q-F` has the same asymptotic ratio to `F^0.525`.

For every fixed p>=5, `0.2375*p-1>0`.  Thus, uniformly in q, the available cofactor interval eventually contains a full BHP short interval starting above both F and A/q.  BHP supplies a prime r>F inside it, and q*r is the required exclusive collision.

Therefore for every fixed p>=5 there exists K_p such that for k>=K_p every candidate prime q<=F_p(k) is forced.

Consequently, for fixed p>=5 and sufficiently large k:

**the unique least safe divisor-witness basis is the entire candidate prime set up to the screening horizon.**

This is a structural corollary of established prime-gap theory, not a new prime-gap theorem.  The p>=5 threshold is what the 0.525 exponent suffices to prove by this argument; no optimality claim is made.

## 6. Critical p=3 and p=4 regimes

For a near-square-root witness the cofactor interval scale behaves like `x^(1-2/p)`:

- p=3 -> exponent 1/3;
- p=4 -> exponent 1/2;
- p=5 -> exponent 3/5.

Thus the BHP 0.525 result directly yields the uniform argument only from p=5 upward.

The current exact atlas shows:

- p=3 already has non-forced candidate witnesses, though every scanned basin still has a least basis;
- p=4 has full forcing saturation in the finite scan, but no global p=4 theorem is claimed here.

These are the next transition exponents to study.

## 7. Prime Toolkit consequence

Collapse exponent now controls witness structure through two exact mechanisms:

1. **pure-power dimension lift**: lower-dimensional primes become higher-dimensional forced witnesses;
2. **large-prime cofactor forcing**: short-interval prime existence can make remaining witnesses mandatory.

For p>=5 the second mechanism asymptotically saturates the entire candidate witness universe.  For p=2 the inherited pure-power channel is empty and residual-choice hypergraphs occur repeatedly.  The p=3 and p=4 regimes remain the critical middle cases.

No Lean formalization is claimed for this checkpoint; local Lean/Lake remains unavailable.  T-A9 is an elementary future Lean target after `WitnessCover.lean` itself is compiler-validated.
