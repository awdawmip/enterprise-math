# D25/LIFT — all-rank gauge orbit stabilization for an `(m+2)` two-eigenvalue block

**Status:** AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. 2026-10-28. This is an auxiliary finite-field theorem, not a native H0/B0 Frobenius evaluation or a formal Source Result. Prior established inputs: the `(m+1)` plateau, the `(2+2)` all-rank classification, and the commutator realization lemma. The distinct new unit is the **all-rank `(m+2)` classification for all `m>=3`**, including the first dimension at which the orbit count stabilizes.

## Exact question, provenance and allowed observer

Let `k=F_q` be any finite field (`q>=2`) and `m>=2`, and let

`A=diag(a I_m,b I_2)`, with `a!=b`. For `B` of size `(m+2)x(m+2)` consider `K=[B,A]=BA-AB`. Since `b-a` is a unit, the set of such `K` is exactly the set of off-diagonal block matrices

```
      [ 0   X ]
  K = [       ],    X:k^2 -> k^m,  Y:k^m -> k^2.
      [ Y   0 ]
```

In a chosen basis there are `q^(4m)` such `K`, and each has exactly `q^(m^2+4)` preimages `B`, because the commutator kernel is the block-diagonal centralizer of dimension `m^2+4`. The **complete centralizer gauge** acts by

`(g,h).(X,Y)=(g X h^{-1}, h Y g^{-1})`, for `(g,h) in GL_m(k) x GL_2(k)`.

This theorem classifies its orbits; it **does not assert** that the original CM/H0/B0 class has this rank, spectrum, or gauge group. A smaller native gauge subgroup has at least as many orbits. The ordered, signed source ports `X` and `Y` and the two directed composites `XY` and `YX` must not be silently replaced by a single norm or positive-mass observer. Only gauge-invariant future readouts descend through this quotient; arbitrary source-marked operations need not.

## Theorem

For all finite fields `k=F_q` and integers `m>=2`, the number of orbits of the above action is

```
N(m,q) = q^2+3q+6,   m=2;
         q^2+4q+8,   m=3;
         q^2+4q+9,   m>=4.
```

In particular, the orbit count **stabilizes at `m=4`**, not already at `m=2` or `m=3`. The stratified counts, where `r=rank X`, are

| `r` | `m=2` | `m=3` | `m>=4` |
|:--:|:--:|:--:|:--:|
| `0` | `3` | `3` | `3` |
| `1` | `2q+3` | `2q+4` | `2q+4` |
| `2` | `q^2+q` | `q^2+2q+1` | `q^2+2q+2` |

Every stratum and case is proved below; no finite computation is used to infer the universal claim.

## Proof, rank zero

If `X=0`, the action is independent change of domain and codomain bases on `Y`, so `Y` is classified by rank `0,1,2`. There are exactly three orbits because `m>=2`.

## Proof, rank one

Choose bases so that `X: k^2 -> k^m` has matrix with its only nonzero entry `X_11=1`. Split its codomain into `k e_1 + U`, `dim U=m-1`, and its domain into `k f_1 + k f_2`. Every stabilizing gauge pair has the form

```
  g = [ alpha   b ]      h = [ alpha   0 ]
      [   0     D ]          [   c    delta ]
```

where `alpha,delta` are nonzero, `b` is a row of length `m-1`, `c` is a scalar and `D in GL_(m-1)(k)`. Write

```
  Y = [ u   v ]
      [ w   z ]
```

with `u,w in k` and `v,z in U^*`. Under `Y' = h Y g^{-1}` the scalar `u` is invariant. Explicit block multiplication gives

```
  u' = u,
  v' = (alpha v-u b) D^{-1},
  w' = (c u+delta w)/alpha,
  z' = (c v+delta z-w' b) D^{-1}.
```

When `u!=0`, choose `b` and `c` to eliminate `v` and `w`, respectively; the residual `z` is classified by zero versus nonzero. This produces `2(q-1)` orbits.

When `u=0`, zero/nonzero of `v` and `w` is separately invariant. If `v=w=0`, `z=0` or `z!=0` gives two orbits. If `w!=0` (regardless of `v`), the free `b` eliminates `z`, and the cases `v=0` versus `v!=0` give two more orbits. If `v!=0,w=0`, the free `c` changes `z` by a multiple of `v`; the remaining class of `z` in `U^*/k v` is zero or nonzero when `dim U>=2`, but is necessarily zero when `dim U=1`. The `GL(U)` stabilizer is transitive on its nonzero quotient covectors. This gives five `u=0` orbits for `m=2`, six for `m>=3`. Total: `2q+3` or `2q+4` respectively.

## Proof, rank two

When `rank X=2`, choose `X` to be the standard inclusion `k^2 -> k^2 ⊕ U`, where `dim U=d=m-2`. Write `Y=(C,D)` with `C in M_2(k)` and `D:U -> k^2`. The stabilizer satisfies

```
  g = [ h  R ] , h in GL_2(k), S in GL_d(k), R:U -> k^2.
      [ 0  S ]
```

The induced transformation is

```
  C' = h C h^{-1},
  D' = (h D-C' R) S^{-1}.
```

Thus first classify `C` up to similarity, and then classify the induced map `bar D:U -> coker C` under the actual stabilizer of `C` and `GL(U)`. This is a **gauge-typed quotient**, not permission to erase the source map `D` in stronger observers.

All `2x2` matrices have `q^2+q` similarity classes: one for each monic quadratic characteristic polynomial, with one additional class for each of the `q` repeated-root polynomials. Partition by matrix rank:

- `rank C=2`: `q^2-1` similarity classes, all with trivial cokernel; each contributes one orbit for any `d`.
- `rank C=1`: `q` similarity classes (`q-1` split semisimple matrices with eigenvalues `0,lambda!=0`, and one nonzero nilpotent Jordan block). Their cokernel is one-dimensional, and the invertible centralizer acts by all nonzero scalars on it. For `d=0` the induced map is zero; for `d>=1` it has two orbits (zero, nonzero).
- `rank C=0`: only `C=0`. Its centralizer is the whole `GL_2(k)`; `bar D=D` is classified by its rank `0,...,min(2,d)`, hence `1+min(2,d)` orbits.

Therefore the `rank X=2` counts are

```
  d=0: (q^2-1) + q   + 1 = q^2+q,
  d=1: (q^2-1) + 2q  + 2 = q^2+2q+1,
  d>=2:(q^2-1) + 2q + 3 = q^2+2q+2.
```

Summing the three ranks proves the theorem. All transformations use invertible matrices and are valid in every characteristic.

## Exact boundary witness and BRC interface

The jump from `m=3` to `m=4` has a concrete source: in the `rank X=2, C=0` stratum the map `D:U -> k^2` gains rank-two possibilities only when `dim U>=2`. Once present, there are no further possible ranks. This accounts for exactly **one additional gauge orbit** between `m=3` and `m=4`. Conversely, the `rank X=1, u=0, v!=0, w=0` stratum gains a nonzero cokernel class at `m=3` and remains stable afterward. These are actual joint/source-observer coordinates, not numerical fitting parameters.

In BRC terms, the carrier is the ordered, source-marked pair `(X,Y)`, the operation is two-sided gauge conjugation, and the finite-horizon observer is its full orbit. The proof supplies an exact fiber/orbit certificate only **for this gauge action**. It does not certify erasure of `X,Y`, `bar D`, signed Green/Hesse ports or original basis normalization under a different family of future operations. P000/Heartbeat X6 remains a separate native project ontology: this ordinary vector-space calculation is an auxiliary algebraic representation without an established X6 embedding.

## Exact arithmetic evidence

Standard-library integer-only checker `d25_m_plus_2_gauge_orbit_checker_20261028.py` enumerates every `(X,Y)` for `q=2, m=2,3,4` and `q=3, m=2,3` and computes orbits using generators of the **full** product general linear group. In characteristic 2, neighboring transvections generate the full group; in characteristic 3 the checker includes determinant-changing diagonal scalings. Every orbit state is visited exactly once. Output is `d25_m_plus_2_gauge_orbit_author_check_20261028.json`.

| `q` | `m` | matrix pairs examined | orbit count | stratification `rank X = 0,1,2` |
|---:|---:|---:|---:|---|
| 2 | 2 | 256 | 16 | `3,7,6` |
| 2 | 3 | 4096 | 20 | `3,8,9` |
| 2 | 4 | 65536 | 21 | `3,8,10` |
| 3 | 2 | 6561 | 24 | `3,9,12` |
| 3 | 3 | 531441 | 29 | `3,10,16` |

Total: **607,890 complete states** and **4,840,782 explicit directed generator applications**. This is same-author exact checking; not independent verification, formal proof checking or original CM experiment.

At the conditional target prime `p=373`, the theorem gives `140254` orbits for `m=2`, `140629` for `m=3`, and `140630` for each `m>=4`. These are mathematical substitutions of the auxiliary formula, not H0/B0 outputs.

## Dependencies and next falsification

1. A real native evaluator must supply the exact original fixed-class Frobenius, rank, eigenvalue structure and allowed gauge subgroup `H` under the frozen source `c47e13e4aba0e006366f989d6334d443f6333ae3`; the native benchmark remains at Issue #1559.
2. Only if `A` has exactly the required two scalar blocks and native `H` acts as the full centralizer may this orbit count be transported. Otherwise retain actual matrices and determine the smaller actual group, with its preserved odd observer and `Delta_p-R_p` readouts.
3. No Source CLAIM/OPEN/checkpoint/Result/admission is asserted. Existing UR V2 four-file original (`94687` bytes; SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) is a separate provenance recovery item; do not re-prove or reconstruct its bytes.
