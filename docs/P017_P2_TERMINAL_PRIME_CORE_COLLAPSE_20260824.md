# P017 — P2 Terminal-prime Möbius Core Collapse

Status: `PROVED_WIP + EXECUTABLE_CHECKED_IN_SESSION / NOT CANONICAL / EXACT-MOBIUS SCOPE`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_SUPERROOT_COMPLEMENT_DUALITY_20260824.md`;
- `docs/P017_P2_COLLISION_PACKET_COMPRESSION_20260824.md`.

Scope: exact further collapse of the squarefree Möbius-weighted small-core coefficient in a distinct-prime super-root collision. The result applies to literal Möbius inner weights; extension to Rosser/well-factorable weights is a separate analytic question.

---

## 1. Starting coefficient

Let

\[
W=K+1.
\]

Fix distinct odd primes `p_1,p_2<W`, an odd squarefree small-core lcm packet `ell`, and an odd `t` such that

\[
n=p_1p_2\ell t\in I_K.
\]

The previous supplement proved that the exact Möbius-weighted coefficient of the super-root assignments is

\[
\mathcal C_{\ell}^{p_1,p_2}(K)
=
\sum_{\substack{u_1u_2\mid\ell\\(u_1,u_2)=1\\
 u_1W\le p_2\ell\\
 u_2W\le p_1\ell}}
\mu(u_1u_2).
\]

Put

\[
R_i=\frac W{p_i}.
\]

The present note shows that this apparently three-state core assignment sum is actually a finite small-divisor cover correction to the single baseline coefficient `-mu(ell)`.

---

## 2. P2-R15 — Normalized Möbius covariance identity

For squarefree `D`, define

\[
\mathfrak M_D(y)
=
\sum_{\substack{e\mid D\\e\le y}}\mu(e).
\]

Using

\[
\mathbf 1_{(u_1,u_2)=1}
=
\sum_{r\mid(u_1,u_2)}\mu(r),
\]

write

\[
u_1=ra,
\qquad
u_2=rb.
\]

Because `ell` is squarefree, `a,b` are divisors of `ell/r` and are coprime to `r`; moreover

\[
\mu(ra)\mu(rb)=\mu(a)\mu(b).
\]

Therefore

\[
\boxed{
\mathcal C_{\ell}^{p_1,p_2}(K)
=
\sum_{r\mid\ell}
\mu(r)
\mathfrak M_{\ell/r}
\!\left(\frac{p_2\ell}{Wr}\right)
\mathfrak M_{\ell/r}
\!\left(\frac{p_1\ell}{Wr}\right).
}
\]

Changing variables `D=ell/r` and using

\[
\mu(\ell/D)=\mu(\ell)\mu(D)
\]

gives the normalized form

\[
\boxed{
\mathcal C_{\ell}^{p_1,p_2}(K)
=
\mu(\ell)
\sum_{D\mid\ell}
\mu(D)
\mathfrak M_D\!\left(\frac{p_1D}{W}\right)
\mathfrak M_D\!\left(\frac{p_2D}{W}\right).
}
\]

The cutoff ratio is now scale-free: it is only `p_i/W`.

This is a direct arithmetic bridge to the truncated divisor-Möbius kernels already present in the P017/P018 Walsh route.

---

## 3. P2-R16 — Small-divisor complement and exact cover formula

For `D>1`, divisor complementation `e<->D/e` gives

\[
\begin{aligned}
\mathfrak M_D\!\left(\frac{pD}{W}\right)
&=
\mu(D)
\sum_{\substack{f\mid D\\f\ge W/p}}\mu(f)\\
&=
-\mu(D)
\sum_{\substack{f\mid D\\f<W/p}}\mu(f),
\end{aligned}
\]

because

\[
\sum_{f\mid D}\mu(f)=0.
\]

Define

\[
B_D(R)
=
\sum_{\substack{f\mid D\\f<R}}\mu(f).
\]

The `D=1` term in P2-R15 is zero because `p_i<W`. Hence

\[
\boxed{
\mathcal C_{\ell}^{p_1,p_2}(K)
=
\mu(\ell)
\sum_{\substack{D\mid\ell\\D>1}}
\mu(D)B_D(R_1)B_D(R_2).
}
\]

Now include the `D=1` term temporarily and expand both `B`-sums. For divisors `f_1,f_2|ell`,

\[
\sum_{\substack{D\mid\ell\\\operatorname{lcm}(f_1,f_2)\mid D}}
\mu(D)
\]

vanishes unless

\[
\operatorname{lcm}(f_1,f_2)=\ell,
\]

in which case it equals `mu(ell)`. Removing the `D=1` term therefore yields the exact cover formula

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

### Meaning

The entire internal small-core multiplicity has collapsed to:

1. one baseline sign `-mu(ell)`;
2. an exceptional correction only when two **small divisors**
   \[
   f_1<\frac W{p_1},
   \qquad
   f_2<\frac W{p_2}
   \]
   can jointly cover every prime of `ell` through their lcm.

Thus the exceptional set is a finite two-bin multiplicative cover problem, not a generic `3^{omega(ell)}` assignment family.

---

## 4. P2-R17 — Exact top-third terminal collapse

Assume

\[
p_1\ge\frac W3.
\]

Then

\[
R_1=\frac W{p_1}\le3.
\]

Every nontrivial divisor of the odd number `D` is at least `3`, while the inequality in `B_D(R_1)` is strict. Hence, for every `D>1`, the only divisor below `R_1` is `1`, and

\[
B_D(R_1)=1.
\]

The identity

\[
\sum_{D\mid\ell}\mu(D)B_D(R)
=
\mathbf 1_{\ell<R}
\]

follows by reversing the divisor sums: all inner Möbius sums vanish except when the small divisor already equals `ell`.

Therefore

\[
\boxed{
\mathcal C_{\ell}^{p_1,p_2}(K)
=
\mu(\ell)
\left(
\mathbf 1_{\ell<W/p_2}-1
\right).
}
\]

If a super-root realization exists, then some `d_2|ell` satisfies

\[
p_2d_2\ge W.
\]

Since `d_2<=ell`, necessarily

\[
\ell\ge\frac W{p_2}.
\]

The indicator vanishes, and we obtain:

\[
\boxed{
\text{if at least one of }p_1,p_2\ge\frac{K+1}{3},
\text{ then every nonempty collision has }
\mathcal C_{\ell}^{p_1,p_2}(K)=-\mu(\ell).
}
\]

In particular,

\[
\boxed{
\left|\mathcal C_{\ell}^{p_1,p_2}(K)\right|=1
}
\]

throughout the nonempty top-third collision sector.

### General terminal-band form

The number `3` appears only because all small cores are odd. More generally, if every nontrivial divisor of the permitted small-core packet is at least `q_0`, then the same proof applies as soon as

\[
p_i\ge\frac W{q_0}.
\]

For the current odd binary-carry family, `q_0=3`.

### Consequence

All genuinely nontrivial exact-Möbius core coefficients are confined to

\[
\boxed{
p_1<\frac{K+1}{3},
\qquad
p_2<\frac{K+1}{3}.}
\]

The top third of the visible prime range does not require a growing internal core estimate: its small-core assignment sum has already collapsed to one sign.

---

## 5. P2-R18 — Dual gcd boundary of the exceptional cover

Suppose an exceptional cover pair `(f_1,f_2)` occurs in P2-R16. Put

\[
r=(f_1,f_2).
\]

Since

\[
\operatorname{lcm}(f_1,f_2)=\ell,
\]

one has

\[
f_1f_2=r\ell.
\]

The small-divisor bounds imply

\[
r\ell
<
R_1R_2
=
\frac{W^2}{p_1p_2}
=
\ell t\frac{W^2}{n}.
\]

Therefore

\[
\boxed{
r<t\frac{W^2}{n}.}
\]

Whenever a super-root realization exists,

\[
t\le\frac K{\min(p_1,p_2)}\le\frac K3.
\]

Also

\[
0<W^2-n\le2K.
\]

Hence

\[
t\frac{W^2}{n}-t
=
\frac{t(W^2-n)}n
<
\frac{2t}{K}
\le\frac23<1.
\]

Since `r` is an integer,

\[
\boxed{r\le t.}
\]

This is dual to the physical super-root assignment condition

\[
(d_1,d_2)>t.
\]

The original collision uses a shared core strictly **above** `t`; the exceptional correction to its Möbius collapse can only use an auxiliary cover overlap at or **below** `t`.

### Exact overlap-shell expansion

Write

\[
f_1=ra,
\qquad
f_2=rb,
\qquad
\ell=rab,
\qquad
(a,b)=1.
\]

Then the cover correction is

\[
\boxed{
\sum_{\substack{r\mid\ell\\r<tW^2/n}}
\mu(\ell/r)
\#\left\{
 a\mid\ell/r:
 \frac{\ell}{R_2}<a<\frac{R_1}{r}
\right\}.
}
\]

On a nonempty super-root packet, the outer range may be replaced by `r<=t`.

---

## 6. P2-R19 — Unit-packet parameter `t=1`

If

\[
t=1,
\]

then P2-R18 forces

\[
r=1.
\]

The exceptional correction is therefore controlled by divisors `a|ell` in the single interval

\[
\frac{\ell}{R_2}<a<R_1.
\]

Its length is

\[
R_1-\frac{\ell}{R_2}
=
\frac W{p_1}-\frac{p_2\ell}{W}
=
\frac{W^2-p_1p_2\ell}{p_1W}
=
\frac{W^2-n}{p_1W}
<
\frac2{p_1}
\le\frac23.
\]

Thus the interval contains at most one integer and hence at most one divisor of `ell`. Consequently

\[
\boxed{
 t=1
 \Longrightarrow
 \mathcal C_{\ell}^{p_1,p_2}(K)
 \in\{0,-\mu(\ell)\}.
}
\]

So the first packet layer is already a Boolean correction to the baseline sign.

---

## 7. Analytic consequence and exact remaining hard sector

The distinct-prime exact-Möbius collision coefficient now has three layers:

\[
\boxed{
\begin{array}{ll}
\text{top-third prime present}
&\Rightarrow \mathcal C=-\mu(\ell),\\[1mm]
 t=1
&\Rightarrow \mathcal C\in\{0,-\mu(\ell)\},\\[1mm]
 p_1,p_2<W/3,\ t>1
&\Rightarrow \text{finite small-divisor cover correction}.
\end{array}
}
\]

Thus the exact-Möbius analytic frontier is no longer the whole visible-prime range. It is confined to the doubly sub-terminal prime sector and to packet parameters with nontrivial cover overlap.

This does not automatically extend to arbitrary Rosser or well-factorable coefficients. The next correct comparison is:

1. determine whether the well-factorable coefficient decomposition preserves enough of the cover cancellation to remove the top-third internal multiplicity;
2. if not, consume the exact-Möbius result as a model kernel and identify the precise coefficient defect;
3. apply the existing Chen/Iwaniec bilinear machinery only to the residual doubly sub-terminal cover sector.

No all-`K` P2 theorem, explicit Chen threshold, or Legendre theorem is claimed.

---

## 8. Validation

The companion verifier

`experiments/p017_p2_terminal_prime_core_collapse.py`

checks the normalized covariance identity, divisor complement, exact cover formula, top-third collapse, dual gcd boundary, and the `t=1` Boolean correction over finite squarefree packets and prime ranges.
