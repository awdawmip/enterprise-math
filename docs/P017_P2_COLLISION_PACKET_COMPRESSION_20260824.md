# P017 — P2 Prime-lift Collision Packet Compression

Status: `PROVED_WIP + EXECUTABLE_CHECKED_IN_SESSION / NOT CANONICAL / NO P2 CLOSURE CLAIM`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`;
- `docs/P017_P2_SUPERROOT_COMPLEMENT_DUALITY_20260824.md`.

Scope: exact compression of distinct-prime super-root carry collisions from four sieve variables to a two-packet square-basin factor pair, together with the Möbius-weighted small-core assignment kernel.

---

## 1. Starting point

Let `p_1,p_2` be distinct odd primes above a small-prime cutoff `z`, and let `d_1,d_2` be odd squarefree products of primes below `z`. Put

\[
m_i=p_i d_i>K.
\]

The preceding supplement proved that a same-state collision is equivalent to the existence of a unique odd integer `t` such that

\[
1\le t<(d_1,d_2)
\]

and

\[
n
=
p_1p_2\operatorname{lcm}(d_1,d_2)t
\in I_K.
\]

The present note compresses this formula before attempting any analytic estimate.

---

## 2. P2-R11 — Two-packet collision compression

Define the **prime packet** and **small-core packet**

\[
\boxed{
P=p_1p_2,
\qquad
Q=\operatorname{lcm}(d_1,d_2)t.
}
\]

Then every distinct-prime collision satisfies

\[
\boxed{n=PQ\in I_K.}
\]

Since

\[
K^2<PQ<(K+1)^2,
\]

`P,Q` cannot both be at most `K`, and cannot both exceed `K`. Therefore exactly one packet lies below the root and the other lies above it:

\[
\boxed{
\min(P,Q)\le K<\max(P,Q).
}
\]

By P2-R06/P2-R07, if

\[
a=\min(P,Q),
\qquad b=\max(P,Q),
\]

then

\[
\boxed{b\in J_a(K),}
\]

and the packet factor pair belongs to one unique odd complement window.

Thus the non-diagonal collision geometry factors as

\[
(p_1,d_1,p_2,d_2)
\longrightarrow
(P,Q)
\longrightarrow
(a,b),
\]

where the last carrier is the same disjoint reciprocal-window family already governing every super-root odd carry.

### Packet-side dichotomy

There are only two cases:

1. `P>K`: the two-prime packet is super-root and the small-core packet `Q` is the unique sub-root label;
2. `P<=K`: the prime packet is the sub-root label and the small-core packet `Q` is super-root.

In the second case, since

\[
Q=\operatorname{lcm}(d_1,d_2)t<d_1d_2,
\]

the inequality `Q>K` forces

\[
\boxed{d_1d_2>K.}
\]

Hence the `P<=K` collision sector is necessarily a genuine two-large-core/Type-II sector; it cannot be produced by two very small sieve variables.

---

## 3. P2-R12 — Subpolynomial internal packet multiplicity

Fix an odd integer `Q`. Consider ordered squarefree pairs `(d_1,d_2)` and an odd `t` satisfying

\[
Q=\operatorname{lcm}(d_1,d_2)t.
\]

For a fixed squarefree

\[
\ell=\operatorname{lcm}(d_1,d_2),
\]

the value `t=Q/ell` is determined. Every prime of `ell` has exactly three possible incidence states:

- in `d_1` only;
- in `d_2` only;
- in both.

Therefore the number of ordered pairs with lcm `ell` is

\[
3^{\omega(\ell)}.
\]

Summing over the squarefree divisors `ell` of `Q` gives

\[
\boxed{
\#\{(d_1,d_2,t):Q=\operatorname{lcm}(d_1,d_2)t\}
\le
\sum_{\ell\mid\operatorname{rad}(Q)}3^{\omega(\ell)}
=
4^{\omega(Q)}.
}
\]

The actual support restrictions, the inequalities `m_i>K`, and `t<(d_1,d_2)` only reduce this count.

For a fixed distinct-semiprime packet `P`, there are at most two ordered prime decompositions `P=p_1p_2`. Hence a fixed packet pair `(P,Q)` has at most

\[
\boxed{2\cdot4^{\omega(Q)}}
\]

ordered prime-lift collision realizations.

Since `Q<=U_K<K^2+2K+1`, the standard maximal-order divisor bound gives

\[
4^{\omega(Q)}=K^{o(1)}.
\]

### Critical-scale collision support bound

The number of odd packet factor pairs across the root is

\[
\sum_{\substack{a\le K\\a\text{ odd}}}O_a(K)
\ll K\log K.
\]

Combining this with the packet multiplicity bound yields

\[
\boxed{
\#\{\text{distinct-prime super-root collision tuples}\}
\le K^{1+o(1)}.
}
\]

Consequently, for coefficients of modulus at most `1`, the absolute distinct-prime off-diagonal incidence energy is bounded by

\[
\boxed{K^{1+o(1)}.}
\]

This is an unconditional critical-scale envelope, not a fixed-power saving. It matches the existing P017/P018 lesson that raw `L^2` control at exponent `1+o(1)` is structurally available but does not by itself cross the sieve parity boundary.

---

## 4. P2-R13 — Exact Möbius core-assignment transform

Now assign the exact squarefree Möbius coefficient `mu(d_i)` to each small-core variable. Fix distinct primes `p_1,p_2`, an odd squarefree lcm packet `ell`, and an odd `t` such that

\[
n=p_1p_2\ell t\in I_K.
\]

Every ordered pair `(d_1,d_2)` with

\[
\operatorname{lcm}(d_1,d_2)=\ell
\]

can be written uniquely as

\[
d_1=gu_1,
\qquad
d_2=gu_2,
\qquad
\ell=gu_1u_2,
\]

where `g,u_1,u_2` are pairwise coprime and squarefree. Equivalently,

\[
d_1=\frac{\ell}{u_2},
\qquad
d_2=\frac{\ell}{u_1}.
\]

The super-root conditions are

\[
p_1d_1\ge K+1,
\qquad
p_2d_2\ge K+1,
\]

or exactly

\[
\boxed{
 u_2(K+1)\le p_1\ell,
 \qquad
 u_1(K+1)\le p_2\ell.
}
\]

Moreover

\[
\mu(d_1)\mu(d_2)=\mu(u_1u_2),
\]

because the shared component `g` occurs twice.

Therefore the full Möbius-weighted core coefficient of the super-root collision is

\[
\boxed{
\mathcal C_{\ell}^{p_1,p_2}(K)
=
\sum_{\substack{u_1u_2\mid\ell\\(u_1,u_2)=1\\
 u_1(K+1)\le p_2\ell\\
 u_2(K+1)\le p_1\ell}}
\mu(u_1u_2).
}
\]

The parameter `t` no longer appears explicitly in this rectangular divisor sum. Its role is to select the square basin through

\[
K^2<p_1p_2\ell t<(K+1)^2.
\]

The previously derived condition `t<g` is automatic from the two super-root inequalities, because

\[
p_1d_1\,p_2d_2\ge(K+1)^2>n=p_1p_2\ell t.
\]

### Divisor-window form

Put

\[
A_1=\frac{p_1\ell}{K+1},
\qquad
A_2=\frac{p_2\ell}{K+1}.
\]

For

\[
h=u_1u_2=\frac\ell g,
\]

every divisor `u_1|h` determines `u_2=h/u_1`, and the Möbius sign is the constant `mu(h)`. Hence

\[
\boxed{
\mathcal C_{\ell}^{p_1,p_2}(K)
=
\sum_{h\mid\ell}
\mu(h)
\#\left\{
 u\mid h:
 \frac{h}{A_1}\le u\le A_2
\right\}.
}
\]

Equivalently, with the truncated divisor Möbius sum

\[
\mathfrak M_D(y)=\sum_{\substack{e\mid D\\e\le y}}\mu(e),
\]

one may write

\[
\boxed{
\mathcal C_{\ell}^{p_1,p_2}(K)
=
\sum_{\substack{u_1\mid\ell\\u_1\le A_2}}
\mu(u_1)
\mathfrak M_{\ell/u_1}(A_1).
}
\]

This is an exact two-dimensional truncated Möbius divisor-window kernel. It is the same analytic species as the truncated Möbius hyperbolas already isolated on the P017/P018 Walsh route, but with endpoints forced by the square-root inequalities.

### Untruncated cancellation

If all three prime-incidence states are summed without the super-root rectangle, then each prime of `ell` contributes

\[
(+1)+(-1)+(-1)=-1.
\]

Thus

\[
\boxed{
\sum_{\operatorname{lcm}(d_1,d_2)=\ell}
\mu(d_1)\mu(d_2)
=(-1)^{\omega(\ell)}
=\mu(\ell).
}
\]

So the lcm assignment algebra itself collapses completely. The nontrivial object is exactly the root-truncated rectangle.

---

## 5. P2-R14 — The square-root rectangle lies strictly inside the collision hyperbola

Because

\[
n=p_1p_2\ell t<(K+1)^2,
\]

the rectangle endpoints satisfy

\[
\boxed{
A_1A_2
=
\frac{p_1p_2\ell^2}{(K+1)^2}
=
\frac\ell t\frac{n}{(K+1)^2}
<
\frac\ell t.
}
\]

Thus every divisor pair admitted by the super-root rectangle automatically obeys

\[
u_1u_2<\frac\ell t,
\]

or equivalently

\[
g=\frac\ell{u_1u_2}>t.
\]

This gives a precise low-height diagonal constraint: the two independent root thresholds form a rectangle whose area is just below the ambient collision hyperbola, by the exact factor

\[
\frac{n}{(K+1)^2}=1-O(1/K).
\]

The square-basin coupling is therefore not an arbitrary CRT shift. It enters the Möbius kernel as a near-critical rectangular truncation.

### One-shell overlap boundary

Consider the two excluded tails

\[
u_1>A_2,
\qquad
u_2>A_1.
\]

If both occur while `g>t`, then

\[
t<g<t\frac{(K+1)^2}{n}.
\]

Whenever a super-root realization exists,

\[
t\le\frac K{\min(p_1,p_2)}\le\frac K3.
\]

The width of the displayed `g`-interval is therefore less than

\[
\frac{t((K+1)^2-n)}n
<
\frac{2t}{K}
\le\frac23.
\]

Hence the simultaneous overlap of the two unbalanced tails is supported on at most one integer `g`, and therefore on at most one gcd shell.

This is the collision-kernel analogue of P2-R08's one-window cutoff defect.

---

## 6. Exact packetized off-diagonal form

For bounded coefficients `beta_{p,d}`, define the distinct-prime super-root incidence form

\[
\mathcal E_{\times}
=
\sum_{p_1\ne p_2}
\sum_{d_1,d_2}
\beta_{p_1,d_1}\overline{\beta_{p_2,d_2}}
\mathcal K_K((p_1,d_1),(p_2,d_2)).
\]

P2-R11 gives the exact packet reindexing

\[
\boxed{
\mathcal E_{\times}
=
\sum_{\substack{P,Q\text{ odd}\\K^2<PQ\le U_K}}
\Gamma(P,Q),
}
\]

where `Gamma(P,Q)` sums only the internal realizations

\[
P=p_1p_2,
\qquad
Q=\operatorname{lcm}(d_1,d_2)t.
\]

By root duality this becomes a disjoint-window sum

\[
\boxed{
\mathcal E_{\times}
=
\sum_{\substack{a\le K\\a\text{ odd}}}
\sum_{\substack{b\in J_a(K)\\b\text{ odd}}}
\widetilde\Gamma(a,b).
}
\]

For exact Möbius inner weights, `Gamma` is governed by the truncated divisor-window coefficient `mathcal C` above. For Rosser or well-factorable weights, the same packet carrier remains exact, but the internal coefficient is the corresponding weighted three-state assignment sum rather than literal Möbius inversion.

---

## 7. Research consequence and honest boundary

The original object

\[
\sum_p\sum_d c_p\lambda_d
\left(H_{pd}-H_{2pd}-\frac K{pd}\right)
\]

has now been reduced through the following exact chain:

\[
\boxed{
\begin{aligned}
&\text{binary carry}\\
&\to\text{standard Chen remainder difference}\\
&\to\text{unique super-root complement windows}\\
&\to\text{two-packet collision factorization }PQ\in I_K\\
&\to\text{root-truncated Möbius divisor-window kernel}.
\end{aligned}
}
\]

This removes the need to invent a generic new sieve or a free two-dimensional carry-distribution hypothesis.

It does **not** yet supply the required signed power saving. The unconditional packet multiplicity/energy bound remains at the critical scale `K^{1+o(1)}`. The next valid analytic target is now exact:

> prove cancellation for the near-critical rectangular divisor-window coefficients `mathcal C_ell^{p_1,p_2}(K)`, or show that established Chen/Iwaniec well-factorable bilinear estimates already control their packetized sum with usable explicit constants.

No P2-in-every-square theorem, no explicit all-`K` constant, and no Legendre theorem is claimed.

---

## 8. Validation

The companion finite verifier

`experiments/p017_p2_collision_packet_compression.py`

checks:

- packet factorization and root straddling;
- the `4^{omega(Q)}` internal multiplicity envelope;
- equality of the direct Möbius assignment sum, rectangular coprime-divisor sum, and divisor-window form;
- untruncated lcm Möbius collapse to `mu(ell)`;
- automatic `g>t` and the one-gcd-shell overlap boundary.

Finite replay is regression evidence only; the displayed identities are proved by the exact divisor parametrizations above.
