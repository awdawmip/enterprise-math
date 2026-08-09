# Legendre Pressure Test — Supplement 16

Status: `ACTIVE RESEARCH NOTE`  
Scope: stable-range disjointness of lower-band quotient-root channels  
Depends on: P017 L051 and canonical P018-T110–T113  
Discipline: this note does **not** prove Legendre's conjecture. It sharpens L051 by elementary integer inequalities. No asymptotic prime-distribution theorem is used.

## 1. L051 is uniform but not asymptotically sharp

For a lower-band prime

\[
p^2<2k,
\]

write

\[
j_p=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right),
\qquad
C_p(k)=\{j_p,j_p+1\}.
\]

L051 proves that every target root belongs to at most two candidate pairs `C_p(k)`.

Finite pressure tests show that the double overlaps are a small-root phenomenon only. The last one occurs at

\[
k=14,
\qquad p=2,\ q=3,
\]

where

\[
C_2(14)=\{9,10\},
\qquad
C_3(14)=\{8,9\}.
\]

From `k=15` onward the candidate pairs are pairwise disjoint.

The next theorem proves this exactly.

---

## 2. L052 — Stable lower-band root channels are disjoint

Status: `PROVED`.

For every

\[
\boxed{k\ge15}
\]

and every pair of distinct lower-band primes

\[
p<q,
\qquad p^2<2k,\ q^2<2k,
\]

one has

\[
\boxed{j_p\ge j_q+2.}
\]

Therefore

\[
\boxed{C_p(k)\cap C_q(k)=\varnothing.}
\]

Equivalently, for `k>=15`, every descended root index receives at most **one** lower-band least-prime shell channel.

The threshold is sharp for a uniform statement because of the `k=14` example above.

---

## 3. Setup

Fix

\[
p<q
\]

and put

\[
u=j_q.
\]

By definition,

\[
\boxed{qu^2\le k^2.}
\]

It is enough to prove

\[
\boxed{p(u+2)^2\le k^2,}
\]

because then

\[
(u+2)^2
\le
\left\lfloor\frac{k^2}{p}\right\rfloor,
\]

and hence

\[
j_p\ge u+2=j_q+2.
\]

The proof splits into one uniform large-`q` argument and four small values `q=3,5,7,11`.

---

## 4. The uniform case q >= 13

Assume

\[
q\ge13.
\]

The lower-band condition gives

\[
q^2<2k,
\]

so

\[
q^4<4k^2.
\]

For `q>=13`,

\[
\boxed{q^3>4(2q-3)^2.}
\]

A completely integer verification is obtained by writing `q=13+h`, `h>=0`:

\[
q^3-4(2q-3)^2
=h^3+23h^2+139h+81>0.
\]

Multiplying by `q` and combining with `q^4<4k^2` gives

\[
4q(2q-3)^2<4k^2,
\]

hence

\[
q(2q-3)^2<k^2.
\]

Therefore

\[
(2q-3)^2
\le
\left\lfloor\frac{k^2}{q}\right\rfloor,
\]

and so

\[
\boxed{u=j_q\ge2q-3.}
\]

Since `q>=13` is odd and `p<q` is prime,

\[
p\le q-2,
\]

thus

\[
\boxed{u\ge2p+1.}
\]

Also `q-p>=2`. Hence

\[
\begin{aligned}
qu^2-p(u+2)^2
&=(q-p)u^2-4pu-4p\\
&\ge2u^2-4pu-4p\\
&=2(u^2-2pu-2p).
\end{aligned}
\]

Because `u>=2p+1`,

\[
u^2-2pu
=u(u-2p)
\ge u,
\]

so

\[
u^2-2pu-2p
\ge u-2p
\ge1.
\]

Therefore

\[
\boxed{p(u+2)^2<qu^2\le k^2.}
\]

This proves the theorem for every `q>=13`.

---

## 5. Small case q=11

Now

\[
p\in\{2,3,5,7\}.
\]

Since `q^2<2k`,

\[
k\ge61.
\]

Thus

\[
11\cdot18^2=3564<61^2\le k^2,
\]

so

\[
u=j_{11}\ge18.
\]

For the largest possible `p=7`,

\[
11u^2-7(u+2)^2
=4u^2-28u-28.
\]

At `u>=18`,

\[
4u^2\ge72u,
\]

so the difference is at least

\[
44u-28>0.
\]

Hence the desired inequality holds for all smaller `p` as well.

---

## 6. Small case q=7

Here

\[
p\in\{2,3,5\},
\qquad k\ge25.
\]

The worst case is `p=5`.

From

\[
7\cdot9^2=567<25^2,
\]

we have

\[
u=j_7\ge9.
\]

If `u>=11`, then

\[
7u^2-5(u+2)^2
=2u^2-20u-20>0.
\]

For the only smaller possibilities:

- if `u=9`, then `k>=25`, so
  \[
  5(9+2)^2=605<625\le k^2;
  \]
- if `u=10`, the definition of `u` gives
  \[
  k^2\ge7\cdot10^2=700,
  \]
  hence `k>=27`, and
  \[
  5(10+2)^2=720<729\le k^2.
  \]

Thus `q=7` is settled.

---

## 7. Small case q=5

Now

\[
p\in\{2,3\}.
\]

The theorem assumes `k>=15`, so

\[
5\cdot6^2=180<225\le k^2,
\]

and therefore

\[
u=j_5\ge6.
\]

For the worst case `p=3`:

- if `u>=7`,
  \[
  5u^2-3(u+2)^2
  =2u^2-12u-12>0;
  \]
- if `u=6`, directly
  \[
  3(6+2)^2=192<225\le k^2.
  \]

So `q=5` is settled.

---

## 8. Small case q=3

The only prime below `3` is

\[
p=2.
\]

Again `k>=15`. Since

\[
3\cdot8^2=192<225\le k^2,
\]

we have

\[
u=j_3\ge8.
\]

If `u>=9`,

\[
3u^2-2(u+2)^2
=u^2-8u-8>0.
\]

If `u=8`, then

\[
k^2<3\cdot9^2=243.
\]

Together with `k>=15`, this forces

\[
k=15.
\]

Then

\[
2(8+2)^2=200<225=k^2.
\]

Thus `q=3` is also settled.

This completes the proof of L052. ∎

---

## 9. Sharpness at k=14

At

\[
k=14,
\]

both `2` and `3` are lower-band primes. One computes

\[
j_2
=R_2(98)=9,
\qquad
j_3
=R_2(65)=8.
\]

Therefore

\[
C_2(14)=\{9,10\},
\qquad
C_3(14)=\{8,9\},
\]

and the target root `9` lies in both.

Hence the uniform threshold `k>=15` cannot be reduced to `k>=14`.

---

## 10. Structural consequence

L051 already gave constant cross-shell multiplicity. L052 removes even that factor in the stable range:

\[
\boxed{
\text{for }k\ge15,
\quad
\text{one descended root scale}
\longleftarrow
\text{at most one lower-band least-prime shell}.
}
\]

Thus the lower-band quotient windows form separate root-scale channels before T113 even chooses the actual upper/lower branch.

This is stronger than a generic well-founded recursion statement. It says the root coordinate can be used as a **nonoverlapping shell label** for all sufficiently large roots.

---

## 11. Relation to exact cofactor windows

Each least prime `p` has the exact open cofactor window

\[
W_p(k)
=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

T110 places this window in at most two adjacent square-root basins. L052 says that for `k>=15` no other lower-band prime has either of those candidate root indices.

Therefore each lower target root basin receives candidate cofactor-window material from at most one lower-band least-prime shell.

The exact window occupies only a subinterval of that lower basin; replacing the subinterval by the full basin remains too coarse. The gain of L052 is elimination of cross-shell multiplicity, not permission to discard subwindow geometry.

---

## 12. Relation to T113 and mirror gating

T113 gives the statewise switch inside the unique L052 channel:

\[
R_2\!\left(\left\lfloor\frac np\right\rfloor\right)
=j_p+\mathbf1[s\ge\tau_p].
\]

So in the stable range the lower-band route now has:

1. exactly one possible shell channel per target root (L052);
2. one exact offset threshold choosing the actual root inside that channel (T113);
3. strict descent of the actual root (T112).

For mirror states, `s=k\pm r`, hence the branch selector is a radius half-interval. This can be intersected with the existing mirror CRT progression without any ambiguity about competing lower-band shell channels at the same root scale.

---

## 13. Executable validation

`lower_band_root_disjoint_bound(k)` checks the L052 stable-range statement.

Regression tests cover:

- every `15<=k<1000`;
- larger roots through `k=200000`;
- pairwise endpoint separation `j_p>=j_q+2`;
- the sharp `k=14,p=2,q=3` overlap witness.

Finite tests audit implementation only; the proof is the integer argument above.

---

## 14. Next target

The lower-band structural problem is now much narrower.

For `k>=15`, cross-shell root collisions are gone. The next question is whether the **exact p-rough subwindow inside each unique descended root channel** has a recursive composite capacity smaller than generic least-factor/Buchstab bookkeeping predicts.

The hardest surviving case is expected to be singleton small-prime support with a large prime tail; this is the parity-sensitive branch and should be isolated explicitly rather than hidden inside a general recursion.
