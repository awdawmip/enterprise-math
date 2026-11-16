# PREFIX-808 — relative cotangent lengths at the joint-zero Reeve canonical-cover fibers

Date: 2026-11-16. Status: **PROVED in the pinned Reeve observer algebra, DRIVER AUTHOR-SIDE extension, Native Result not admitted**.

## Exact model, scope, and attribution

Original named TU/Reeve 0/1 observations: **EM-DIRECT-4660FF**. Reeve observer semigroup, canonical-cover presentations, and earlier relative-flatness/fiber theorem: **EM-DVR-DEBB5E**. The present cotangent-length theorem and proof are an additional author-side result of **EM-DVR-DEBB5E**, not an independent review.

Use the exact existing finite canonical-cover map `C_h^can/R_h`, field `K`, integer `h>=2`, `g=gcd(h,2)`, `r=h/g`. Let `s in Spec(R_h)` satisfy `A=U_1U_2=B=U_0U_3=0`, and set `kappa=kappa(s)`. The previously proved fiber identity, with no characteristic restriction, is

```text
F_h = C_h^can tensor_(R_h) kappa
    = [kappa[u,v]/(u,v)^h]^(mu_g).
```

Source pins:
- `b6543b101537be8fbd068e2349d6c1d785d8c0d8:research_notes/driver/2026-11-16_r6_prefix808_canonical_cover_relative_flatness_joint_zero_fibers.md` (corrected fiber/socle census).
- `43b9cb3ba76404104b384c1e46a3e6eb7e56e0fc:research_notes/driver/2026-11-16_r6_prefix808_even_index_one_cover_complete_intersection.md` (even-height complete-intersection presentation).

All relative differentials below are the actual `Omega_(C_h^can/R_h)`; standard base change gives `Omega_(C_h^can/R_h) tensor_(C_h^can) F_h = Omega_(F_h/kappa)`. Reported dimensions are **length over the residue field** `kappa`, not generic rank or length over `R_h`.

## Theorem (all heights and all field characteristics)

Write `p=char(kappa)`, with `p=0` allowed.

1. If `h=2`, then `F_2=kappa` and `dim_kappa Omega_(F_2/kappa)=0`; its embedding dimension is zero.

2. If `h>=3` is odd, then

```text
dim_kappa Omega_(F_h/kappa) =
    h^2 - 1,                     if p=0 or p does not divide h;
    h^2 + h/p,                   if p>0 and p divides h.
```

The local embedding dimension is 2 in every characteristic.

3. If `h=2k>=4` is even, `k>=2`, then

```text
dim_kappa Omega_(F_(2k)/kappa) =
    2k^2 - 2,                    if p=0 or p does not divide k;
    2k^2 - 2 + (2k/p + 1),       if p>0 and p divides k.
```

The local embedding dimension is 3 in every characteristic. In particular `h=6`, `p=2` has dimension `16`, whereas `h=6`, `p=3` has dimension `19`. These are **relative observer-to-canonical-cover** differentials: the characteristic-sensitive jump is governed by the relative generic degree `r=h/g` (where `r=h` for odd heights and `r=k` for even heights), not merely by whether the characteristic divides `h`.

## Proof

**Odd h.** Here `g=1` and `F_h=kappa[u,v]/m^h`, `m=(u,v)`, of vector-space length `L=h(h+1)/2`. The conormal presentation of Kahler differentials starts with two free copies of `F_h`; the only nonzero relations arise from the differentials of the degree-`h` monomials, with coefficients in degree `h-1`. Thus the relation rank is the rank of the homogeneous gradient map

```text
d : kappa[u,v]_h -> (kappa[u,v]_(h-1)) du + (kappa[u,v]_(h-1)) dv.
```

Its domain has dimension `h+1`. In characteristic zero, or in characteristic `p` not dividing `h`, its kernel is zero. When `p>0` divides `h`, the kernel consists of the `h/p+1` distinct monomials `u^(pa)v^(h-pa)` for `0<=a<=h/p`: both formal partial derivatives vanish exactly when both exponents are multiples of `p`. Therefore

```text
dim Omega = 2L - ((h+1) - delta)
          = h^2 - 1 + delta,
delta = (h/p + 1) if p divides h, else 0.
```

The cotangent space `m/m^2` is generated freely by the classes of `u,v` since `h>=3`.

**Even h=2k.** Here `g=2`. With `x=u^2,y=uv,z=v^2`, the invariant fiber is the truncated second Veronese algebra

```text
S=kappa[x,y,z]/(y^2-xz),
F_(2k) = S / S_(>=k),
dim_kappa S_n=2n+1.
```

The grading on `S` assigns degree one to `x,y,z`. The equality follows by matching each even-degree monomial of `u,v` with the normal forms `x^a z^b` and `y x^a z^b` and truncating total `u,v` degree at `2k`.

Use the grading `deg(dx)=deg(dy)=deg(dz)=1`. At degree one, `dim Omega_(F/kappa)_1=3`. For `2<=n<k`, the only conormal relation is `d(y^2-xz)=2y dy-z dx-x dz`, multiplied by `S_(n-2)`. Multiplication by this nonzero gradient is injective because `S` is a domain (including in characteristic two). Consequently

```text
dim Omega_(F/kappa)_n
  = 3 dim S_(n-1) - dim S_(n-2)
  = 3(2n-1) - (2n-3) = 4n.
```

At degree `n=k`, the new truncation relations are the images of `d:S_k->Omega_(S/kappa)_k`. Thus, setting `delta=dim_kappa ker(d|S_k)`,

```text
dim Omega_(F/kappa)_k
  = 4k - ((2k+1)-delta) = 2k-1+delta.
```

We now compute this kernel in every characteristic. In characteristic zero it is zero. In odd characteristic `p`, substitute `x=u^2,y=uv,z=v^2`; if `dF=0` in `Omega_S`, then its image in `Omega_{kappa[u,v]}` vanishes. A degree-`2k` polynomial in `u,v` has zero gradient precisely when every surviving exponent is divisible by `p`. Since `p` is odd and the total exponent is `2k`, this occurs only when `p|k`, yielding `2k/p+1` independent terms. Conversely, every such monomial is the `p`th power of an even-total-degree monomial, hence lies in `S` and has zero differential already in `Omega_S`. So the bound is exact.

In characteristic two, every degree-`k` element of `S` is uniquely `P(x,z)+yQ(x,z)`, with `P` homogeneous degree `k` and `Q` degree `k-1`. As the conormal relation `df=-z dx-x dz` has no `dy` component, `dF=0` implies `Q=0`. If `k` is odd, the Euler identity `xP_x+zP_z=kP` forces `P=0` whenever `dP` is a multiple of `df`. If `k` is even, every monomial `x^a z^(k-a)` has both exponents even (and hence zero differential), or both odd (and hence its differential is a multiple of `z dx+x dz=-df`). All `k+1` such monomials are therefore in the kernel. This agrees with `2k/p+1=k+1` for `p=2|k`. Hence in every characteristic `delta=2k/p+1` if `p>0` divides `k`, and zero otherwise.

Summing all grading pieces gives

```text
dim Omega = 3 + sum_(n=2)^(k-1) 4n + (2k-1+delta)
          = 2k^2-2+delta.
```

For `k=2`, the intermediate sum is empty. The maximal ideal modulo its square has the independent generators `x,y,z` since `k>=2`. Finally `k=1` separately gives `F_2=kappa`. QED.

## Exact finite matrix crosscheck

Reproduction: run `python experiments/reeve_relative_cotangent_20261116.py` from the repository root; it constructs the two conormal matrices explicitly and prints the 56-case PASS verdict.

An integer-exponent sparse conormal matrix was assembled over each prime field `F_p`, `p in {2,3,5,7}`. For odd `h in {3,5,7,9,11,13}`, the matrix includes the `h+1` degree-`h` gradient relations inside the `2L` free differentials. For even `h=2k` with `1<=k<=8`, it includes all `df * S_(<=k-2)` and `dS_k` in the `3k^2` free module. Each rank was computed by exact modular row elimination, with no floating point or sampling. All **56** characteristic/height instances match the displayed formulas, including:

| h | char 2 | char 3 | char 5 | char 7 |
|---:|---:|---:|---:|---:|
| 3 | 8 | 10 | 8 | 8 |
| 4 | 9 | 6 | 6 | 6 |
| 6 | 16 | 19 | 16 | 16 |
| 8 | 35 | 30 | 30 | 30 |
| 10 | 48 | 48 | 51 | 48 |
| 12 | 77 | 75 | 70 | 70 |

The arbitrary-height proof above is the theorem certificate. These exact finite checks corroborate its arithmetic and boundary cases.

## Portfolio significance and next live obligation

The exceptional cotangent-length jumps at the joint-zero fibers occur precisely in residue characteristics dividing the *relative* degree `r`. The zero-fiber embedding dimensions remain stable, while torsor/etale behavior off `V(A,B)` is already pinned in the relative-flatness theorem. No native path-algebra realization is implied for X6 without a separately specified, provenance-preserving map under P000.

Contributors remain distinct: the original named observations `EM-DIRECT-4660FF`, the preceding Reeve structural proofs and this extension `EM-DVR-DEBB5E`. This proof is an **author-side mathematical result**, not a new authenticated Result record, independent Driver review, Task completion, or mother-objective closure.
