# P017 — P2 Super-root Complement Duality and Prime-lift Collision Kernel

Status: `PROVED_WIP + EXECUTABLE_CHECKED_IN_SESSION / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Parent note: `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`

Scope: exact finite integer structure of the P017 odd/binary carry above the square root, and the distinct-prime collision kernel for prime-lift moduli `m=pd`.

---

## 0. Why the super-root zone should be inverted rather than treated as a free modulus family

The parent note proved that

\[
O_m(K)=H_m(K)-H_{2m}(K)
\]

counts multiples `ma` in the open square basin for which the quotient `a` is odd. When `m>K`, the quotient is automatically at most `K`; moreover two admissible odd quotients would differ by at least `2`, while the corresponding multiples would differ by more than the entire basin width.

Thus every nonzero super-root carry column has one and only one complementary sub-root label. The correct exact carrier is therefore not an arbitrary two-dimensional `(m,s)` incidence table. It is a reciprocal family of disjoint cofactor windows.

This is an elementary divisor-hyperbola inversion. No historical novelty claim is made for divisor complementation or the hyperbola method; the project-specific point is the exact P017 odd-carry and prime-lift collision interface.

---

## 1. Notation

For `K>=2`, write

\[
I_K=\{K^2+1,\ldots,K^2+2K\},
\qquad
U_K=K^2+2K=(K+1)^2-1.
\]

Retain

\[
H_m(K)
=\left\lfloor\frac{U_K}{m}\right\rfloor
-\left\lfloor\frac{K^2}{m}\right\rfloor,
\qquad
O_m(K)=H_m(K)-H_{2m}(K).
\]

For every positive `a<=K`, define the complementary modulus window

\[
\boxed{
J_a(K)
=
\left[
\left\lfloor\frac{K^2}{a}\right\rfloor+1,
\left\lfloor\frac{U_K}{a}\right\rfloor
\right].
}
\]

Equivalently,

\[
m\in J_a(K)
\iff
K^2<am<(K+1)^2.
\]

---

## 2. P2-R06 — Exact super-root complement duality

### Theorem

Let `m>K` be odd. Then

\[
\boxed{
O_m(K)
=
\sum_{\substack{1\le a\le K\\a\text{ odd}}}
\mathbf 1_{m\in J_a(K)}
\in\{0,1\}.
}
\]

If the value is `1`, the corresponding odd `a` is unique and

\[
K^2<am<(K+1)^2.
\]

### Proof

`O_m(K)` counts those multiples `ma` in `I_K` for which the quotient `a` is odd. Since `m>K`, hence `m>=K+1`, and `ma<(K+1)^2`, one has

\[
a<K+1,
\]

so `a<=K`.

If two odd quotients `a_1<a_2` occurred, then `a_2-a_1>=2`, and therefore

\[
m(a_2-a_1)\ge2m>2K=|I_K|,
\]

which is impossible inside one interval of width `2K`. Hence at most one odd quotient occurs. The window equivalence is the definition of `J_a(K)`. ∎

### Interpretation

Above the root, the binary carry is a sparse Boolean incidence:

\[
\text{super-root modulus }m
\longleftrightarrow
\text{unique sub-root odd complement }a.
\]

There is no super-root column multiplicity.

---

## 3. P2-R07 — Odd complement windows are strictly separated

### Theorem

Let `1<=a<b<=K` be odd. Then

\[
\boxed{
\max J_b(K)<\min J_a(K).
}
\]

Thus the family

\[
\{J_a(K):1\le a\le K,\ a\text{ odd}\}
\]

is pairwise disjoint and strictly ordered in reverse `a`-order.

### Proof

Because `a,b` are distinct odd integers,

\[
b-a\ge2.
\]

Since `a<=K`,

\[
K(b-a)\ge2K\ge2a,
\]

or equivalently

\[
a(K+2)\le bK.
\]

Therefore

\[
\frac{K(K+2)}{b}\le\frac{K^2}{a}.
\]

Taking floors gives

\[
\left\lfloor\frac{U_K}{b}\right\rfloor
\le
\left\lfloor\frac{K^2}{a}\right\rfloor,
\]

while the lower endpoint of `J_a(K)` is one larger than the right-hand floor. ∎

### Relation to canonical P017 L054

Canonical L054 proves the same separation for distinct prime first-factor labels. P2-R07 observes that the proof only needs odd-label spacing, so it extends to every odd complement label. This is a WIP specialization/generalization statement on the owner branch, not a canonical renumbering of L054.

### Corollary — exact root-mass reciprocity

For odd `a<=K`, the number of odd moduli in `J_a(K)` is exactly `O_a(K)`. Every such modulus is greater than `K`. Consequently

\[
\boxed{
\sum_{\substack{K<m\le U_K\\m\text{ odd}}}O_m(K)
=
\sum_{\substack{1\le a\le K\\a\text{ odd}}}O_a(K).
}
\]

This is the exact factor-pair symmetry of the odd carry across the square root.

---

## 4. P2-R08 — A modulus cutoff has at most one complement-window defect

Fix an integer cutoff

\[
K<L\le U_K.
\]

For an odd label `a<=K`, one has the exact threshold equivalences

\[
\boxed{
J_a(K)\cap(K,L]\ne\varnothing
\iff
a>\frac{K^2}{L},
}
\]

and

\[
\boxed{
J_a(K)\subseteq(K,L]
\iff
a>\frac{U_K}{L+1}.
}
\]

Indeed, the first condition is equivalent to

\[
\left\lfloor\frac{K^2}{a}\right\rfloor+1\le L,
\]

and the second to

\[
\left\lfloor\frac{U_K}{a}\right\rfloor\le L.
\]

Therefore a window can straddle the cutoff `L` only when

\[
\boxed{
\frac{K^2}{L}<a\le\frac{U_K}{L+1}.
}
\]

The width of this transition interval is

\[
\frac{U_K}{L+1}-\frac{K^2}{L}
=
\frac{K(2L-K)}{L(L+1)}
<
\frac{2K}{L}
<2.
\]

Distinct odd labels differ by at least `2`. Hence:

\[
\boxed{
\text{at most one odd complement window straddles any cutoff }L>K.
}
\]

### Exact cutoff decomposition

Let

\[
\mathcal A_{\mathrm{full}}(K,L)
=
\left\{a\le K:a\text{ odd and }a>\frac{U_K}{L+1}\right\}.
\]

There is either no odd straddling label or a unique one, say `a_*`. Then

\[
\boxed{
\sum_{\substack{K<m\le L\\m\text{ odd}}}O_m(K)
=
\sum_{a\in\mathcal A_{\mathrm{full}}(K,L)}O_a(K)
+B_{K,L},
}
\]

where `B_{K,L}=0` if no straddler exists, and otherwise

\[
B_{K,L}
=
\#\{m\in J_{a_*}(K):m\le L,\ m\text{ odd}\},
\qquad
0\le B_{K,L}\le O_{a_*}(K).
\]

Thus a hard modulus cutoff reverses to a hard complementary-factor cutoff with a defect supported on at most one exact window.

### Shallow super-root localization

If

\[
L=K^{1+\eta},
\]

then every incidence with `K<m<=L` has

\[
a>\frac{K^2}{L}=K^{1-\eta}.
\]

So a shallow super-root band is exactly localized, up to the single cutoff window above, to a near-root complementary band.

---

## 5. P2-R09 — Exact distinct-prime factor-exchange collision kernel

Let `z>=2`. Let `p_1,p_2>z` be distinct odd primes, and let `d_1,d_2` be positive odd integers all of whose prime factors are `<z`. Put

\[
m_i=p_i d_i>K.
\]

Suppose the two super-root columns hit the same odd state `n in I_K`, so

\[
n=m_1a_1=m_2a_2,
\qquad
a_1,a_2\le K\text{ odd}.
\]

Write

\[
g=(d_1,d_2),
\qquad
d_1=gu_1,
\qquad
d_2=gu_2,
\qquad
(u_1,u_2)=1.
\]

### Theorem

There is a unique positive odd integer `t` such that

\[
\boxed{
\begin{aligned}
a_1&=p_2u_2t=p_2\frac{d_2}{g}t,\\
a_2&=p_1u_1t=p_1\frac{d_1}{g}t,\\
n&=p_1p_2\operatorname{lcm}(d_1,d_2)t,
\end{aligned}
}
\]

and necessarily

\[
\boxed{1\le t<g.}
\]

In particular,

\[
\boxed{(d_1,d_2)=1\Longrightarrow\text{no distinct-prime same-state collision}.}
\]

### Proof

Because `p_1>z` while every prime factor of `p_2d_2` is either `p_2` or below `z`,

\[
(p_1,p_2d_2)=1.
\]

The equality

\[
p_1d_1a_1=p_2d_2a_2
\]

therefore forces `p_1|a_2`; symmetrically `p_2|a_1`. Write

\[
a_1=p_2b_1,
\qquad
a_2=p_1b_2.
\]

After cancellation,

\[
d_1b_1=d_2b_2,
\]

or

\[
u_1b_1=u_2b_2.
\]

Coprimality of `u_1,u_2` gives

\[
b_1=u_2t,
\qquad b_2=u_1t
\]

for a unique positive integer `t`. All displayed factors except `t` are odd and `a_i` are odd, so `t` is odd.

Moreover

\[
n
=
\frac{m_1m_2}{g}t.
\]

Since each integer `m_i>K` satisfies `m_i>=K+1`,

\[
m_1m_2\ge(K+1)^2>n.
\]

Hence `t/g<1`, proving `t<g`. ∎

### Boolean kernel formula

Put

\[
C(p_1,p_2;d_1,d_2)
=
p_1p_2\operatorname{lcm}(d_1,d_2).
\]

The cross-prime same-state incidence kernel is exactly

\[
\boxed{
\mathcal K_K((p_1,d_1),(p_2,d_2))
=
\sum_{\substack{1\le t<g\\t\text{ odd}}}
\mathbf 1_{K^2<Ct\le U_K}.
}
\]

This sum contains at most one nonzero term. Indeed,

\[
Cg=m_1m_2>K^2,
\qquad
\frac Cg=p_1p_2u_1u_2\ge p_1p_2\ge15,
\]

so

\[
C^2>15K^2,
\qquad
C>\sqrt{15}K>2K.
\]

The admissible real interval for `t` has length

\[
\frac{U_K-K^2}{C}=rac{2K}{C}<1.
\]

Thus every distinct-prime off-diagonal kernel entry is Boolean and, when nonzero, is represented by one unique shared-core parameter `t<g`.

### Structural consequence

A distinct high-prime collision has three compulsory features:

1. each lifted prime crosses into the opposite complementary factor;
2. the two sieve variables share a nontrivial small-prime core `g`;
3. the remaining collision coordinate is a unique odd `t` strictly below that core.

This strictly sharpens the large-gcd necessary condition P2-R04 from the parent note.

---

## 6. P2-R10 — Exact weighted super-root reindexing

Let `(alpha_m)` be any finitely supported coefficient sequence on odd `m>K`. Then

\[
\boxed{
\begin{aligned}
&\sum_{\substack{m>K\\m\text{ odd}}}
\alpha_m\left(O_m(K)-\frac Km\right)\\
&\qquad=
\sum_{\substack{1\le a\le K\\a\text{ odd}}}
\sum_{\substack{m\in J_a(K)\\m\text{ odd}}}
\alpha_m
-
K\sum_{\substack{m>K\\m\text{ odd}}}\frac{\alpha_m}{m}.
\end{aligned}
}
\]

This follows immediately from P2-R06; P2-R07 ensures that the incidence part has no double counting.

For prime-lift coefficients

\[
\alpha_{pd}=c_p\lambda_d,
\]

with `p>z` and `d` supported below `z`, the representation `m=pd` is unique. Hence the original carry bilinear form is exactly a weighted prime-lift count in disjoint reciprocal windows minus its harmonic density term.

The coefficients remain inside the windows. Therefore this identity is an exact structural reduction, not by itself an analytic cancellation estimate.

---

## 7. Consequence for the remaining analytic frontier

The super-root part of the P2 carry problem can now be represented in two exact, compatible ways:

\[
\boxed{
\text{standard Chen floor remainder difference}
\quad\Longleftrightarrow\quad
\text{disjoint complement-window discrepancy}.
}
\]

For second moments, the distinct-prime off-diagonal part has the explicit shared-core kernel

\[
\sum_{\substack{p_1\ne p_2\\d_1,d_2}}
\beta_{p_1,d_1}\overline{\beta_{p_2,d_2}}
\sum_{\substack{t<(d_1,d_2)\\t\text{ odd}}}
\mathbf 1_{
K^2<
 p_1p_2\operatorname{lcm}(d_1,d_2)t
\le U_K
}.
\]

Every inner `t`-sum is `0` or `1`, and it vanishes whenever `(d_1,d_2)=1`.

The next nontrivial target is therefore no longer a generic average-distribution theorem for `H_{pd}-H_{2pd}`. It is the following sharply typed estimate:

> exploit well-factorability or Möbius structure of the sieve coefficients against the Boolean shared-small-core collision kernel above, with only one reciprocal cutoff-window defect.

This may still require the classical Chen/Iwaniec exponential-sum machinery. What has been removed is the ambiguity about the arithmetic carrier and where off-diagonal reuse can occur.

---

## 8. Validation and boundary

The companion verifier

`experiments/p017_p2_superroot_complement_duality.py`

checks:

- P2-R06 unique super-root complements;
- P2-R07 strict odd-window separation and mass reciprocity;
- P2-R08 exact cutoff thresholds and the one-window defect;
- P2-R10 weighted reindexing with exact rational arithmetic;
- P2-R09 factor exchange, `t<g`, and the Boolean collision kernel for finite prime-lift families.

The exact verifier was replayed in-session through `K=160`; the collision census was replayed through `K=120` for several small-prime cutoffs. This is finite regression evidence, not an asymptotic proof.

No P2-in-every-square theorem, no explicit Chen constant, and no Legendre theorem is claimed here.
