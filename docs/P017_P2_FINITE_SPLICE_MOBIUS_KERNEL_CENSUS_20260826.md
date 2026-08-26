# P017 — Finite-Splice Exact-Mobius Kernel Census for the A6 Terminal Core

Status: `PROVED_WIP EXACT FINITE ENVELOPE / TIER-A SPLICE ANCHOR / EXACT-MOBIUS SCOPE / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_TERMINAL_PRIME_CORE_COLLAPSE_20260824.md`;
- `docs/P017_P2_COLLISION_PACKET_COMPRESSION_20260824.md`;
- `docs/P017_P2_RESIDUAL_ENERGY_COMPRESSION_20260826.md`;
- `docs/P017_P2_A6_FIVE_NINTH_ROOT_EDGE_PACKAGE_20260826.md`.

Purpose: turn the a6 fact `Q<z^2+1` into an exact finite numerical envelope for the literal-Mobius internal collision coefficient at the conservative Tier-A finite splice. This is a splice-anchor constant, not an all-scale replacement for the Chen/Iwaniec signed remainder theorem.

---

## 1. Exact splice data

Use the conservative finite endpoint

\[
\boxed{K_0=116009280740973308}
\]

and put

\[
W_0=K_0+1.
\]

The current a6 terminal-prime lower edge in the `K=sqrt(X)` variable is

\[
p\ge K^{22/27}.
\]

Define the exact integer lower surrogate

\[
\boxed{
p_0=\left\lceil K_0^{22/27}\right\rceil
=80241952393051.
}
\]

Thus every terminal prime at the splice satisfies `p>=p_0`.

For a distinct-prime collision

\[
Q=\ell t,
\qquad
p_1p_2Q\in I_{K_0},
\]

so, without even using that `p_1,p_2` are prime,

\[
Q
\le
\left\lfloor
\frac{K_0^2+2K_0}{p_0^2}
\right\rfloor.
\]

Exact integer arithmetic gives

\[
\boxed{Q\le Q_0=2090174.}
\]

In the nontrivial exact-Mobius hard sector one has `t>1`, and `t` is odd. Hence

\[
 t\ge3,
\qquad
\boxed{\ell\le L_0=\left\lfloor Q_0/3\right\rfloor=696724.}
\]

The hard sector also has

\[
p_i<W_0/3,
\]

so with

\[
R_i=W_0/p_i
\]

one has

\[
3<R_i\le R_0:=W_0/p_0<1446.
\]

All subsequent census bounds deliberately ignore the stronger constraints

- `p_i` prime and distinct;
- `p_i>=p_0` with actual prime rounding;
- `p_1p_2\ell t in I_(K_0)`;
- `t<gcd(d_1,d_2)`;
- all prime factors of `ell` below the small-prime cutoff `z`.

Removing these constraints enlarges the census domain, so the resulting coefficient envelope is safe for every genuine a6 collision at the splice.

---

## 2. Exact cover coefficient

The frozen terminal-prime core theorem gives

\[
\boxed{
\mathcal C_{\ell}^{p_1,p_2}(K)
=
-\mu(\ell)
+
\sum_{\substack{f_1\mid\ell,\ f_1<R_1\\
                  f_2\mid\ell,\ f_2<R_2\\
                  \operatorname{lcm}(f_1,f_2)=\ell}}
\mu(f_1)\mu(f_2).
}
\]

At fixed odd squarefree `ell`, this coefficient is constant between consecutive divisor thresholds in each variable `R_i`. Therefore a complete continuous search over

\[
3<R_1,R_2\le R_0
\]

reduces exactly to a finite two-dimensional prefix table indexed by the divisors of `ell`.

No floating-point approximation to `R_i` is required: a divisor `f` can occur below the largest allowed cutoff exactly when

\[
f p_0<W_0.
\]

The strict lower hard-sector boundary `R_i>3` means that every divisor `f<=3` is already included in the minimal cutoff state.

---

## 3. Exhaustive envelope

The companion integer checker enumerates every odd squarefree

\[
3\le\ell\le696724
\]

and every possible divisor-cutoff state induced by

\[
3<R_1,R_2\le R_0.
\]

There are exactly

\[
282366
\]

odd squarefree `ell` in this enlarged domain.

The largest possible number of distinct prime factors is six. The exact maximal coefficient magnitudes by `omega(ell)` are

\[
\boxed{
\begin{array}{c|cccccc}
\omega(\ell)&1&2&3&4&5&6\\ \hline
\max |\mathcal C|&1&1&2&5&11&13.
\end{array}
}
\]

The global enlarged-domain maximum is therefore

\[
\boxed{
|\mathcal C_{\ell}^{p_1,p_2}(K_0)|\le13.
}
\tag{FS-MC13}
\]

One envelope-attaining squarefree packet is

\[
\ell=255255
=3\cdot5\cdot7\cdot11\cdot13\cdot17.
\]

The enlarged cutoff table attains coefficient `13` at divisor cutoffs represented by `1001` and `1309`. Whether a genuine prime pair realizes that exact enlarged cutoff cell is irrelevant to the upper bound.

---

## 4. Why the result is useful

Before the a6 root-edge specialization, the internal packet multiplicity was only bounded by

\[
2\cdot4^{\omega(Q)}=K^{o(1)}
\]

and the literal-Mobius hard coefficient was left as a growing truncated divisor-window kernel.

At the actual conservative splice, the a6 terminal lower edge forces the whole hard exact-Mobius kernel into a finite domain on which the signed internal coefficient itself has the uniform numerical envelope

\[
\boxed{13}.
\]

This is materially different from counting raw assignment realizations: the number `13` already includes the exact Mobius cancellation in the cover formula.

It also shows that the literal-Mobius same-state collision core is not the source of an order-thousands constant at the current splice. The remaining expensive object is the cross-state/factorable signed correlation identified in

`docs/P017_P2_CENTERED_INCIDENCE_SPECTRAL_FRONTIER_20260826.md`.

---

## 5. Boundary

`FS-MC13` is a finite-splice anchor, not an all-`K` uniform theorem. As `K` grows, the cutoff `z=K^(5/27)` and the allowed small-core domain grow, so a separate explicit growth envelope is needed before this constant can be used unchanged for every `K>=K_0`.

Likewise, the theorem is for the exact Mobius inner weight. Arbitrary Rosser/well-factorable coefficients do not inherit the cover cancellation automatically.

The correct downstream use is therefore:

1. treat `13` as the exact initial-scale internal-core constant at the Tier-A splice;
2. retain the already-proved subpolynomial asymptotic packet-multiplicity envelope beyond the splice until an explicit monotone growth bound is frozen;
3. spend generic Fourier/spectral machinery only on the cross-state residual correlation, not on a fictitious large same-state Mobius-core constant.

No P2-in-every-square theorem, no Legendre theorem, and no full finite analytic threshold is claimed here.
