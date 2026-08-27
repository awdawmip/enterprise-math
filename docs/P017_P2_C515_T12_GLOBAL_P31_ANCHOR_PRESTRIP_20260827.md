# P017 — c=103/20 T1–T2 Global P(31)-Length Anchor Prestrip

Status: `PROVED_WIP EXACT GLOBAL PRESTRIP + EIGHT-FACTOR HARD DEPTH / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_ADAPTIVE_PRIMORIAL_LENGTH_ANCHOR_20260823.md`;
- `docs/P017_P2_C515_T12_SUPERROOT_PAIR_ABSORPTION_20260827.md`.

Purpose: use one common target interval for the entire remaining sub-root ordered-pair sector, while stripping every small Rosser factor through 31 with zero floor error. This avoids the invalid idea of choosing a different target interval for every least-prime anchor.

---

## 1. One common anchored interval

At the Tier-A scale put

\[
K_0=116009280740973308,
\qquad W=K_0+1,
\qquad L=2K_0.
\]

Let

\[
\boxed{
Q_0=P(31)=2\cdot3\cdot5\cdots31=200560490130.
}
\]

Choose the largest `Q_0`-multiple not exceeding the full basin length:

\[
\boxed{
L_0=Q_0\left\lfloor\frac{2K_0}{Q_0}\right\rfloor.
}
\tag{A1}

Exact integer arithmetic gives

\[
L_0=232018403006890500
\]

and

\[
\boxed{
2K_0-L_0=158475056116<Q_0.
}
\tag{A2}

In particular

\[
K_0<L_0<2K_0,
\]

so

\[
J_0=(K_0^2,K_0^2+L_0]
\]

is one fixed interval contained in the square basin. A P2 in `J_0` is enough for the full basin.

The relative discarded tail is

\[
\frac{2K_0-L_0}{2K_0}<7\times10^{-7}.
\tag{A3}

---

## 2. Exact mixed-modulus stripping

For the remaining sub-root ordered-pair carrier, let

\[
z\le r<p,
\qquad rp\le W,
\]

and let `d` be an odd squarefree upper-Rosser modulus supported on primes below `r`. Write

\[
e=(d,Q_0),
\qquad d=e b.
\]

Because `r,p>z>31`, both are coprime to `Q_0`, and because `e|Q_0|L_0`, the exact anchor identity gives

\[
\boxed{
H_{rpd}(K_0^2,L_0)
=H_{rpb}\!\left(\left\lfloor\frac{K_0^2}{e}\right\rfloor,\frac{L_0}{e}\right).
}
\tag{A4}

Equivalently for sharp floor discrepancies,

\[
\boxed{
r_{rpd}(K_0^2,L_0)
=r_{rpb}\!\left(\left\lfloor\frac{K_0^2}{e}\right\rfloor,\frac{L_0}{e}\right).
}
\tag{A5}

Thus every prime factor of `d` in

\[
\{3,5,7,11,13,17,19,23,29,31\}
\]

is removed from the hard modulus with **zero floor-error cost**.

All prime factors of the remaining `b` are at least `37`.

The factor `2` in `Q_0` is used only to make the target length even and keep the odd-population normalization exact; the hard Rosser moduli themselves are odd in the parity-projected model.

---

## 3. The remaining hard Rosser depth is at most eight

For every sub-root pair,

\[
r,p\ge z=D^{1/6},
\]

so

\[
rp\ge D^{1/3}.
\]

The upper-sieve level for the remaining cofactor modulus is

\[
Q=\frac{D}{rp}\le D^{2/3}.
\tag{A6}

Any Rosser modulus `d` is below `Q`, hence so is its stripped hard part `b`. Since every prime factor of `b` is at least `37`, nine distinct hard prime factors would imply

\[
b\ge37^9.
\]

At the Tier-A scale, with `D=W^(10/9)`, exact integer exponentiation proves

\[
\boxed{37^9>D^{2/3}=W^{20/27}.}
\tag{A7}

Therefore

\[
\boxed{
\omega(b)\le8.
}
\tag{A8}

This is a uniform statement over the entire remaining sub-root T1–T2 carrier.

---

## 4. What this does and does not solve

The global anchor accomplishes three things simultaneously:

1. it keeps one common target interval, so no target-changing argument is hidden in the proof;
2. it removes all small Rosser factors through `31` exactly before any analytic estimate;
3. it converts the remaining Rosser factorization problem to fixed depth at most `8`.

It does **not** by itself bound the aggregate T1–T2 remainder. The Rosser coefficients are still indexed by the full modulus `d`, and stripping its small part changes the descended interval scale `L_0/e`; one must still exploit either the fixed-depth hard factorization or a well-factorable variant of the upper sieve.

The next comparison is therefore finite and explicit:

- direct fixed-depth factorization of at most eight hard primes; versus
- Iwaniec's well-factorable upper-sieve variant, for which modern formulations give only `O(1/epsilon)` convolution pieces for a prescribed factorization scale.

No finite P2 theorem or all-K claim is made here.
