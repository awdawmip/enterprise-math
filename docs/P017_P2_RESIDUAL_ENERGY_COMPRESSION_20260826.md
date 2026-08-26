# P017 — Residual-Energy Compression on the A6 Root-Edge Strip

Status: `PROVED_WIP SQUARE-SPECIFIC L2 COMPRESSION + SMOOTH PARITY EXTENSION / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`;
- `docs/P017_P2_SUPERROOT_COMPLEMENT_DUALITY_20260824.md`;
- `docs/P017_P2_COLLISION_PACKET_COMPRESSION_20260824.md`;
- `docs/P017_P2_A6_FIVE_NINTH_ROOT_EDGE_PACKAGE_20260826.md`;
- `docs/P017_P2_EXPLICIT_BSPLINE_BALANCED_PACKAGE_20260825.md`.

Purpose: quantify the square-specific quadratic-energy reduction of the parity-projected Chen remainder on the live `a=6, d=5/9` root-edge level, without identifying that reduction with the already-frozen generic Lemma-4 Fourier/Cauchy exponent.

---

## 1. Sharp square-basin residual energy

For `K>=2`, let

\[
I_K=(K^2,K^2+2K]\cap\mathbb Z,
\]

\[
H_m(K)=\#\{n\in I_K:m\mid n\},
\qquad
O_m(K)=H_m(K)-H_{2m}(K).
\]

For odd `m`, the exact P017 bridge gives

\[
\boxed{
e_m(K):=O_m(K)-\frac Km
=r_K(m)-r_K(2m).
}
\]

In the super-root zone `m>K`,

\[
O_m(K)\in\{0,1\}.
\]

For an integer level `D` with

\[
K<D\le K^2,
\]

define

\[
\boxed{
E_{\rm sharp}(K,D)
=
\sum_{\substack{K<m\le D\\m\text{ odd}}}
|e_m(K)|^2.
}
\]

### Theorem P2-R15 — coefficient-free super-root energy compression

One has

\[
\boxed{
E_{\rm sharp}(K,D)
\le
\frac DK
+\frac K2\log\frac DK
+K+2.
}
\tag{R15}
\]

### Proof

Because `O_m` is Boolean,

\[
\begin{aligned}
e_m^2
&=
O_m^2-2\frac Km O_m+\frac{K^2}{m^2}\\
&\le
O_m+\frac{K^2}{m^2}.
\end{aligned}
\]

Hence

\[
E_{\rm sharp}(K,D)
\le
A(K,D)
+K^2\sum_{\substack{m>K\\m\text{ odd}}}\frac1{m^2},
\]

where

\[
A(K,D)
=
\#\{K<m\le D:m\text{ odd},\ O_m(K)=1\}.
\]

By the reciprocal-complement theorem, every active `m<=D` belongs to a unique odd window `J_a` whose label satisfies

\[
a>\frac{K^2}{D}.
\]

The root-mass reciprocity theorem gives

\[
\#\{m\in J_a:m\text{ odd}\}=O_a(K),
\]

and the exact sub-root formula gives

\[
O_a(K)\le\frac Ka+1.
\]

Therefore

\[
A(K,D)
\le
\sum_{\substack{K^2/D<a\le K\\a\text{ odd}}}
\left(\frac Ka+1\right).
\]

For positive `x<K`, odd integers have spacing `2`, so

\[
\sum_{\substack{x<a\le K\\a\text{ odd}}}\frac1a
\le
\frac1x+\frac12\log\frac Kx.
\]

With `x=K^2/D`, and with at most `K/2+1` odd labels, this yields

\[
A(K,D)
\le
\frac DK
+\frac K2\log\frac DK
+\frac K2+1.
\]

Likewise, by spacing `2`,

\[
\sum_{\substack{m>K\\m\text{ odd}}}\frac1{m^2}
\le
\frac1{K^2}+\frac1{2K},
\]

hence

\[
K^2\sum_{\substack{m>K\\m\text{ odd}}}\frac1{m^2}
\le
1+\frac K2.
\]

Combining the two estimates proves (R15). ∎

---

## 2. Exact consequence at the live five-ninth level

The current `a=6` packet has

\[
D=X^{5/9}.
\]

Writing `X=K^2` at the square scale gives

\[
D=K^{10/9}.
\]

For the integer implementation take

\[
D_K=\left\lfloor K^{10/9}\right\rfloor.
\]

Then (R15) gives

\[
\boxed{
E_{\rm sharp}(K,D_K)
\le
K^{1/9}
+\frac1{18}K\log K
+K+2.
}
\tag{R16}
\]

In particular,

\[
\boxed{
E_{\rm sharp}(K,D_K)=K^{1+o(1)}.
}
\]

The generic coefficient-uniform pointwise envelope `|e_m|<1` over a level of size `D_K` would only give

\[
\sum_{m\le D_K}|e_m|^2\ll D_K=K^{10/9}.
\]

Thus the P017 square geometry supplies the definite raw quadratic-energy ratio

\[
\boxed{
\frac{E_{\rm sharp}}{D_K}
\ll
K^{-1/9+o(1)}
=
X^{-1/18+o(1)}.
}
\tag{R17}
\]

This is a genuine fixed-power reduction of the residual quadratic energy. It is **not** yet a theorem that the final Lemma-4 bilinear amplitude gains the square root `X^{-1/36}`; that requires a separate insertion lemma identifying this energy as an independent Cauchy factor.

---

## 3. Smooth parity projection retains the same exponent

The preceding saving is not an artifact of the sharp interval indicator.

Let `J` be any real interval contained in `(K^2,K^2+2K]` with length

\[
0<L\le K,
\]

and let `f>=0` be supported on `J`. Put

\[
F=\int_{\mathbb R}f(t)\,dt,
\qquad
B=\|f\|_\infty.
\]

For odd `m` define the parity-projected weighted count

\[
O_m(f)=\sum_{q\text{ odd}}f(mq)
\]

and its centered remainder

\[
\boxed{
e_m(f)=O_m(f)-\frac{F}{2m}.
}
\]

Equivalently, if

\[
r_f(d)=\sum_{n\equiv0\pmod d}f(n)-\frac Fd,
\]

then

\[
e_m(f)=r_f(m)-r_f(2m).
\]

For `m>K`, successive odd multiples of `m` are separated by `2m>2K>L`. Therefore the support of `f` contains at most one odd multiple of each such `m`.

Let

\[
A_J(K,D)
=
\#\{K<m\le D:m\text{ odd},\ \exists q\text{ odd with }mq\in J\}.
\]

Every such `q` satisfies

\[
\frac{K^2}{D}<q\le K,
\]

and for fixed `q` the possible `m` lie in an interval of length `L/q`. Hence

\[
A_J(K,D)
\le
\sum_{\substack{K^2/D<q\le K\\q\text{ odd}}}
\left(\frac Lq+1\right),
\]

so

\[
\boxed{
A_J(K,D)
\le
\frac{LD}{K^2}
+\frac L2\log\frac DK
+\frac K2+1.
}
\tag{R18}
\]

Because `f>=0`,

\[
0\le O_m(f)\le B
\]

on the active carrier, and

\[
|e_m(f)|^2
=O_m(f)^2-\frac FmO_m(f)+\frac{F^2}{4m^2}
\le
O_m(f)^2+\frac{F^2}{4m^2}.
\]

Therefore

\[
\boxed{
\sum_{\substack{K<m\le D\\m\text{ odd}}}|e_m(f)|^2
\le
B^2 A_J(K,D)
+\frac{F^2}{8K}
+\frac{F^2}{4K^2}.
}
\tag{R19}
\]

### Existing explicit B-spline baseline

For the order-`p` B-spline already used in the P017 effectivity work,

\[
f_{p,L}(t)=p a^{1-p}u_a^{*p}(t),
\qquad a=L/p,
\]

one has exactly

\[
F=L
\]

and the elementary convolution bound

\[
u_a^{*p}(t)\le a^{p-1}
\]

gives

\[
\boxed{\|f_{p,L}\|_\infty\le p.}
\]

Thus, for fixed `p` and `L<=K`, (R19) remains `K^{1+o(1)}` at `D=K^{10/9}`.

In particular the existing order-`7` explicit smoothing does not destroy the fixed `1/9` gap between the square-specific quadratic-energy exponent and the generic level exponent.

---

## 4. A6 collision packets are confined to the Selberg small-core scale

The same root-edge exponents produce a second exact compression.

In the current terminal-prime band,

\[
p_i\ge D^{b/a}=X^{11/27}=K^{22/27}.
\]

For a distinct-prime collision the frozen packet variables are

\[
P=p_1p_2,
\qquad
Q=\operatorname{lcm}(d_1,d_2)t,
\qquad
PQ\in I_K.
\]

Hence

\[
P\ge K^{44/27}>K.
\]

Therefore the generic collision branch `P<=K` is absent throughout this a6 terminal sector. Necessarily `Q` is the sub-root packet, and

\[
Q
\le
\frac{K^2+2K}{K^{44/27}}
=
K^{10/27}+2K^{-17/27}.
\]

Since

\[
z=K^{5/27},
\qquad z^2=K^{10/27},
\]

we obtain

\[
\boxed{Q<z^2+1.}
\tag{R20}
\]

Moreover the frozen collision relation `1<=t<(d_1,d_2)` implies

\[
t^2<Q,
\]

so the shared collision depth satisfies

\[
\boxed{t<\sqrt Q\lesssim z.}
\tag{R21}
\]

Thus every distinct-prime terminal collision is confined to exactly the same small-core scale `z^2` that caps the legal Selberg auxiliary level in the a6 package.

This alignment is exact at the exponent level:

\[
2-2\frac{22}{27}
=
\frac{10}{27}
=2\frac{5}{27}.
\]

---

## 5. What is now proved and what remains open

The live support/energy question has a positive answer at the raw residual level:

\[
\boxed{
\text{P017 residual quadratic energy at }D=K^{10/9}
=
K^{1+o(1)},
}
\]

against the generic level-size envelope `K^{10/9}`.

The fixed gain is

\[
\boxed{1/9\text{ in the }K\text{-energy exponent}}
\]

or

\[
\boxed{1/18\text{ in the }X\text{-energy exponent}.}
\]

The remaining hard step is **not** to rediscover this support saving. It is to prove an insertion theorem showing how much of it survives the factorable signed bilinear form. In particular:

1. do not simply add `1/36` to the existing `delta_off`;
2. do not identify the physical same-radius collision kernel with the Fourier off-diagonal in Lemma 4;
3. first isolate an exact Cauchy/duality step in which the parity-projected energy (R19) is an independent norm factor;
4. use the a6 confinement `Q<z^2+1` to remove or explicitly enumerate the distinct-prime collision carrier before charging generic Fourier constants.

No P2-in-every-square theorem, no Legendre theorem, and no finite analytic threshold is claimed here.
