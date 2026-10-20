# P017×P018 square diagonal — Generation 3D parity transport frontier

Status: `PROVED_WIP STRUCTURE / PARITY ENDPOINT ISOLATED / analytic transport open`

This note consolidates the current square-diagonal frontier after the
Generation-3 prior-art correction.  It does not supersede the exact earlier
identities; it supersedes only any interpretation that another unsigned sieve
refinement, or another bilinear form applied *after* the P2 rough cutoff, is the
remaining prime mechanism.

No statement below claims a proof of Legendre's conjecture.

## D1. Root-P3 is the last state-Möbius-active bilinear layer

Let

\[
U=k^2+2k,
\qquad
z_3=\lfloor U^{1/4}\rfloor,
\qquad
z_2=\lfloor U^{1/3}\rfloor.
\]

At `z_3`, rough states have `Omega<=3`.  Nontrivial multiplicative
factorizations still see more than one factor-depth class, so pre-sieve
Möbius-signed bilinear information can be nontrivial.

At `z_2`, every rough state is either a prime or a squarefree semiprime.  If

\[
t=mn,\qquad m>1,\ n>1,\qquad (t,P_{z_2})=1,
\]

then `Omega(t)<=2` forces `m,n` to be distinct primes.  Hence

\[
\boxed{\mu(mn)=+1}
\]

on every nontrivial factorization of the final P2 rough support.  Prime states
have no nontrivial factorization and are absent from these bilinear ranges.

This is `P2_BILINEAR_MOBIUS_SIGN_FREEZE`.

Therefore a Friedlander--Iwaniec-shaped state-Möbius bilinear form must be
consumed **before** the final P2 rough restriction, or through an equivalent
descent identity which retains mixed factor depths.  Reapplying the same state
sign after `z_2` cannot be the parity-breaking step.

## D2. Root-P3 sign has an exact aliasing defect

On squarefree root-P3 states,

\[
\mu(n)=(-1)^{\Omega(n)}.
\]

Consequently

\[
\boxed{
\mu(n)=-1
\iff
n\text{ is prime or a squarefree triple-prime state}
}
\]

on the `z_3` rough shell.  Prime and squarefree triple are exactly **in phase**
for the Möbius sign.

By contrast, after the `z_2` descent,

\[
\boxed{
\mu(n)=-1\iff n\text{ is prime}
}
\]

because the only other rough states are squarefree semiprimes with `mu=+1`.

Thus the root-P3 sign resource is not enough by itself: the transport theorem
must separate the prime part from the **same-sign squarefree triple core**.
This is `ROOT_PARITY_ALIASING_LADDER`.

## D3. The P3-only contaminant is exactly the P017 fully-k-smooth core

Every root-P3 rough semiprime has

\[
z_3<p\le k<q,
\]

so it is a one-large-prime-tail state.

Every root-P3 rough triple

\[
n=abc,\qquad a\le b\le c
\]

satisfies

\[
ab\ge(z_3+1)^2>\sqrt U,
\]

which gives

\[
c<\sqrt U<k+1.
\]

Hence

\[
\boxed{z_3<a\le b\le c\le k.}
\]

Conversely, a `z_3`-rough fully-`k`-smooth state cannot be prime and cannot be a
semiprime, because two factors at most `k` have product at most `k^2`.  Since
`Omega<=3`, it must be exactly a triple-prime state.

Therefore

\[
\boxed{
\{\text{root-P3 triple contaminants}\}
=
\{\text{z3-rough survivors}\}
\cap
\{\text{fully k-smooth states}\}.
}
\]

This is precisely the P017 complete-core semantic layer.  The existing
complete-core/tail theorem classifies the same rows as
`FULLY_K_SMOOTH` versus `ONE_LARGE_PRIME_TAIL`; it does not by itself provide a
uniform analytic upper bound for the smooth core.

## D4. Exact P3 -> P2 parity-defect transport

For `j=2,3`, define

\[
R_j(k)=\#\{n\in I_k:(n,P_{z_j})=1\},
\qquad
M_j(k)=\sum_{n\in I_k\atop(n,P_{z_j})=1}\mu(n),
\]

and

\[
D_j(k)=R_j(k)-M_j(k)
=
\sum_{n\in\mathcal R_j(k)}(1-\mu(n)).
\]

At root-P3 precision the contributions are exactly:

- prime: `2`;
- squarefree semiprime: `0`;
- squarefree triple: `2`;
- repeated-factor triple: `1`.

At root-P2 precision,

\[
D_2(k)=2\,\pi((k+1)^2)-2\,\pi(k^2).
\]

Every root-P3 triple is removed by the descent `z_3 -> z_2`.  Semiprimes may
also be removed, but contribute zero to `D`.  Therefore

\[
\boxed{
D_2(k)
=
D_3(k)-2T_{\rm sf}(k)-T_{\rm rep}(k),
}
\]

where `T_sf` counts squarefree root-P3 triples and `T_rep` repeated-factor
triples.

Equivalently,

\[
\boxed{
2\,[\pi((k+1)^2)-\pi(k^2)]
=
D_3-2T_{\rm sf}-T_{\rm rep}.
}
\]

This is `ROOT_P3_TO_P2_PARITY_DEFECT_TRANSPORT`.

It is not merely a restatement of the unsigned P3->P2 sieve: deleting a
semiprime has **no effect at all** on this signed defect.  The entire parity
loss in the descent is carried by the triple core.

## D5. Repeated triples and anchor-singular rows are finite-capacity lower-order layers

A repeated root-P3 triple has some `p>z_3` with `p^2|n`.  Since

\[
p^2\ge(z_3+1)^2>\sqrt U>k,
\]

odd parity plus `p^2`-divisibility is a single residue class modulo `2p^2` with
period greater than the shell width `2k`.  Each such prime column is therefore
single-use.  Also `p^3<=U` forces `p<=z_2`.  Hence

\[
\boxed{
T_{\rm rep}(k)
\le
\pi(z_2)-\pi(z_3).
}
\]

The root-P3 anchor-singular layer is similarly sparse.  A root-rough state
sharing a prime with `M=k(k+1)` must use a prime `p>z_3`.  Each of `k` and
`k+1` has at most one distinct prime factor above `z_3`, so there are at most
two such anchor columns.  P017 signed capacity gives

\[
\boxed{
N_{\rm singular}^{(P3)}(k)
\le
2\left(
\left\lfloor\frac{k-1}{z_3+1}\right\rfloor+1
\right)
=O(\sqrt k).
}
\]

Thus in any regime with root-P3 mass of order `k/log k`, the singular layer is
strictly lower-order.  The main same-sign contaminant is the **transverse,
squarefree, fully-k-smooth triple core**.

## D6. P017 signed capacity and Chen/Iwaniec bilinear remainder meet at one finite gate

For an odd divisor `D`, odd shell states divisible by `D` occupy the one class

\[
n\equiv D\pmod{2D}.
\]

Its exact count is

\[
g_k^{\rm odd}(D)
=
\left\lfloor\frac{U+D}{2D}\right\rfloor
-
\left\lfloor\frac{k^2+D}{2D}\right\rfloor.
\]

This is simultaneously:

- the P017 rule `parity + divisibility = one class modulo 2D`;
- a parity-refined short-interval divisor remainder;
- for root-P3 pair products `D=ab>k`, the exact `0/1` gate for the unique
  possible odd third factor.

Hence the P017 finite-capacity language and the Chen/Iwaniec short-interval
bilinear-remainder language now share one exact boundary object.  The missing
resource is not the residue-class description; it is **Möbius-sensitive
cancellation and its transport through the triple-core removal**.

## D7. Root-P3 triple geometry has only two free variables

For any root-P3 triple, the first two factors satisfy

\[
ab>(z_3+1)^2>k.
\]

The third-factor interval has length

\[
\frac{2k}{ab}<2.
\]

All factors are odd.  Writing

\[
U=q(ab)+s,
\qquad
\varepsilon=1_{\{q\text{ even}\}},
\]

the unique possible odd third factor is

\[
\boxed{c_*=q-\varepsilon}
\]

and it lies in the shell exactly when

\[
\boxed{s+\varepsilon ab<2k.}
\]

Thus the entire root-P3 triple core is already a **two-free-variable signed
bilinear remainder problem**.  The balanced `X^(1/3)` box of Generation 2 was a
useful localization, but the thin-shell two-variable collapse actually holds
globally across root-P3 triples.

## D8. Matomäki--Radziwiłł gives an exact mother geometry for the half-cutoff terminal tail

Define the completely multiplicative function

\[
f_k(n)=\lambda(n)1_{(n,P_{\lfloor k/2\rfloor})=1}.
\]

For `k>=9`,

\[
\boxed{
f_k(n)=-1_{\mathbb P}(n)
\qquad(k\le n\le2k).
}
\]

Therefore the `h=2` Matomäki--Radziwiłł-shaped product sum

\[
\sum_{\substack{k^2\le n_1n_2\le k^2+2k\\k\le n_1\le2k}}
 f_k(n_1)f_k(n_2)
\]

is exactly the central half-cutoff prime-prime terminal count, up to the lower
square endpoint and the doubled orientation of `k(k+2)`.  The remaining
half-cutoff semiprime tail has `q>2k` and can use only the two boundary primes
`2k+1,2k+3`.

Matomäki--Radziwiłł Theorem 2 treats the same product geometry for normalized
width `h>=10`; consecutive squares require

\[
\boxed{h=2.}
\]

Moreover their published fixed-`h` error is not of the `O(1/log^2 k)` strength
which would be needed to deduce the expected `O(k/log^2 k)` terminal bound from
this specialization.

Thus G3C remains a precise auxiliary endpoint problem, not a completed tail
estimate.

## D9. Current active theorem target

The strongest current formulation is:

> **Square-diagonal parity transport theorem.**  Obtain a Möbius-signed
> bilinear estimate on the root-P3/pre-P2 descent layer, in the moving
> square-shell geometry, which distinguishes the prime part from the
> same-sign squarefree fully-k-smooth triple core and survives the descent as
> a strict endpoint inequality
> \[
> M_2(k)<R_2(k).
> \]

The exact transport identity shows what such a theorem must beat:

\[
D_3(k)>2T_{\rm sf}(k)+T_{\rm rep}(k).
\]

This inequality is **equivalent** to prime existence and is not itself a new
bound.  Its value is architectural: `T_rep` and the anchor-singular part have
finite-capacity bounds, while the unresolved main loss has been isolated as the
squarefree transverse fully-k-smooth complete core.

The analytic problem is therefore no longer "get P2" and no longer "estimate
Möbius on the final rough set".  It is to produce **sign × factor-depth
coupling before the P2 sign freezes**.

## D10. Parallel fronts retained

Generation 3D keeps three independent fronts:

1. **primary multiplicative:** pre-P2 Möbius parity transport versus the
   squarefree transverse complete core;
2. **primary Archimedean:** covering height `h(y)>y`, using moving cutoff/lift
   information rather than fixed-wheel phase norms;
3. **auxiliary terminal:** MR `h=2` / prime-on-floor-prime correlation to bound
   the half-cutoff semiprime tail.

The balanced Chen mirror remains a separate additive route and has not been
shown by the prior art inspected here to reach its required centered
`sqrt(N)`-scale localization.

Do not return to unsigned precision refinement, final-z2 rough bilinear
state-Möbius sums, or asymptotic P3->P2 existence as primary frontiers.
