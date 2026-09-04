# Free Research — Prime-Winding Möbius/Selberg Renormalization

Status: `FREE_RESEARCH_FRONTIER / EXACT_FINITE_CORE / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_UNVERIFIED`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V2_20260904.md`
Project: `Enterprise Math / 进取数论`

## 0. Question and answer at this checkpoint

The parent frontier asked whether the prime-number-theorem scale

\[
\psi(M)=\log\operatorname{lcm}(1,\ldots,M)\sim M
\]

can be exposed by a finite Enterprise spectral/rotation invariant rather than inserted as an external analytic theorem.

This checkpoint gives a split answer.

### Exact positive result

There is an exact finite quotient-scale determinant renormalization:

\[
\boxed{
\det K_M^+
=M!
=\prod_{k=1}^{M} L_{\lfloor M/k\rfloor},
\qquad
L_q:=\operatorname{lcm}(1,\ldots,q),
}
\]

where `K_M^+` is the positive block of the genuine finite Hamming/Krawtchouk operator whose spectrum is `1,2,...,M`.

The transform is exactly invertible by Möbius renormalization:

\[
\boxed{
L_M
=\prod_{k=1}^{M}
\bigl(\lfloor M/k\rfloor!\bigr)^{\mu(k)}
}
\]

and therefore

\[
\boxed{
\psi(M)
=\sum_{k=1}^{M}\mu(k)
\log\bigl(\lfloor M/k\rfloor!\bigr).
}
\]

Thus the saturated prime-winding envelope is not merely compatible with the integer rotation spectrum: it is the exact Möbius-primitive trace-log reconstructed from all finite quotient resolutions of that spectrum.

### Exact second-order strengthening

The first-order primitive current is supported exactly on prime powers. Its second primitive tensor obeys a finite quadratic conservation law:

\[
\boxed{
\boldsymbol\Lambda_2(n)
=\boldsymbol\Lambda_1(n)\otimes\ell(n)
+\sum_{ab=n}
\boldsymbol\Lambda_1(a)\otimes\boldsymbol\Lambda_1(b),
}
\]

where `ell(n)` is the formal prime-exponent vector of `n` and

\[
\boldsymbol\Lambda_r(n)
:=\sum_{d\mid n}\mu(d)\,\ell(n/d)^{\otimes r}.
\]

After the scalar readout `e_p -> log p`, this is the classical finite Selberg identity

\[
\boxed{
(\mu*\log^2)(n)
=\Lambda(n)\log n+(\Lambda*\Lambda)(n).
}
\]

The project-specific advance is the finite spectral/provenance interpretation: the convolution term is the weighted mass of ordered two-history prime-power recoalescences, while the left side is a Möbius-primitive quadratic energy of quotient-scale Krawtchouk spectra.

### Remaining hard gate

These exact identities expose the correct finite carrier, but they do not by themselves prove `psi(M)~M`. The remaining problem is now sharply localized:

> derive a project-native finite energy estimate and contraction for the centered current `R(M)=psi(M)-M` from the nonnegative quadratic primitive energy, without importing a zero-free zeta argument or treating the classical Selberg asymptotic step as an axiom.

There is no hard algebraic block. The block is asymptotic cancellation/stability.

---

## PWRG-T01 — Saturated winding tower determinant

For every prime `p<=M`, define its available winding height

\[
h_p(M):=\max\{a\ge1:p^a\le M\}
=\lfloor\log_p M\rfloor.
\]

Define the finite saturated winding tower operator

\[
\mathcal W_M
:=\bigoplus_{p\le M\atop p\ \mathrm{prime}}
 p\,I_{h_p(M)}.
\]

Every copy of the eigenvalue `p` is one newly available winding level in the prime-birth direction `p`. Then

\[
\det\mathcal W_M
=\prod_{p\le M}p^{h_p(M)}.
\]

The exponent of `p` in `lcm(1,...,M)` is exactly the greatest `a` with `p^a<=M`. Hence

\[
\boxed{
\det\mathcal W_M=L_M:=\operatorname{lcm}(1,\ldots,M).
}
\]

Consequently

\[
\boxed{
\psi(M)=\log\det\mathcal W_M.
}
\]

This is a literal finite determinant, not an infinite Euler product.

---

## PWRG-T02 — Prime powers are the discrete birth current

The ratio of consecutive saturated determinants is

\[
\boxed{
\frac{L_M}{L_{M-1}}
=\begin{cases}
p,&M=p^a\text{ for a prime }p\text{ and }a\ge1,\\
1,&M\text{ is not a prime power}.
\end{cases}
}
\]

Thus a new tower layer appears exactly at a prime power. Define the formal current

\[
\boldsymbol\Lambda_1(M)
=\begin{cases}
e_p,&M=p^a,\\0,&\text{otherwise},\end{cases}
\]

where `e_p` labels the primitive direction. Under `e_p -> log p`, this becomes the von Mangoldt current

\[
\Lambda(M)=\log(L_M/L_{M-1}).
\]

Therefore

\[
\boxed{
\psi(M)=\sum_{n\le M}\Lambda(n)
}
\]

is precisely accumulated prime-power winding birth.

This sharpens the parent interpretation:

- primes create new directions;
- higher prime powers create new winding levels in an existing direction;
- composites with at least two prime directions create no new saturated layer at their own integer cutoff.

---

## PWRG-T03 — Full-spectrum determinant equals quotient-scale winding product

Let `K_M^+` denote the positive Krawtchouk spectral block with exact eigenvalues

\[
1,2,\ldots,M.
\]

Then

\[
\det K_M^+=M!.
\]

The exact quotient-scale factorization is

\[
\boxed{
M!=\prod_{k=1}^{M}L_{\lfloor M/k\rfloor}.
}
\]

### Proof by prime valuations

For a fixed prime `p`, the `p`-valuation of the right side is

\[
\sum_{k=1}^{M}h_p(\lfloor M/k\rfloor).
\]

This counts pairs `(k,a)` satisfying

\[
p^a\le\lfloor M/k\rfloor
\iff kp^a\le M.
\]

Hence it equals

\[
\sum_{a\ge1}\left\lfloor\frac{M}{p^a}\right\rfloor,
\]

which is exactly `v_p(M!)`. Equality follows prime by prime.

Taking logarithms gives the finite transport law

\[
\boxed{
\log M!
=\sum_{k=1}^{M}\psi(\lfloor M/k\rfloor).
}
\]

Interpretation:

\[
\boxed{
\text{full integer-spectrum volume at scale }M
=
\text{product of saturated winding volumes at all quotient scales}.
}
\]

This is the first exact finite spectral invariant directly controlling the parent frontier's saturated envelope.

---

## PWRG-T04 — Exact Möbius inverse and quotient determinant RG

For transforms of the form

\[
F(M)=\sum_{k\le M}G(\lfloor M/k\rfloor),
\]

floor-compatible Möbius inversion gives

\[
G(M)=\sum_{k\le M}\mu(k)F(\lfloor M/k\rfloor).
\]

Indeed,

\[
\left\lfloor
\frac{\lfloor M/k\rfloor}{j}
\right\rfloor
=\left\lfloor\frac{M}{kj}\right\rfloor
\]

and grouping by `m=kj` leaves the divisor sum `sum_{k|m} mu(k)`, which vanishes except at `m=1`.

Applying this to PWRG-T03 yields

\[
\boxed{
\psi(M)
=\sum_{k=1}^{M}\mu(k)
\log\bigl(\lfloor M/k\rfloor!\bigr)
}
\]

and exponentiating yields

\[
\boxed{
L_M
=\prod_{k=1}^{M}
\bigl(\lfloor M/k\rfloor!\bigr)^{\mu(k)}.
}
\]

Equivalently, the envelope obeys the triangular quotient recursion

\[
\boxed{
L_M
=\frac{M!}{\prod_{k=2}^{M}L_{\lfloor M/k\rfloor}},
}
\]

or

\[
\boxed{
\psi(M)
=\log M!-\sum_{k=2}^{M}\psi(\lfloor M/k\rfloor).
}
\]

Every scale on the right is strictly smaller than `M`; this is a genuine finite renormalization recursion.

---

## PWRG-T05 — Möbius primitive tensor hierarchy is a Hamming provenance hierarchy

Let `V` be the free vector space on symbols `e_p` indexed by primes, and set

\[
\ell(n):=\sum_p v_p(n)e_p.
\]

For `r>=1`, define

\[
\boxed{
\boldsymbol\Lambda_r(n)
:=\sum_{d\mid n}\mu(d)\,\ell(n/d)^{\otimes r}.
}
\]

Write

\[
n=\prod_{i=1}^{s}p_i^{a_i}
\]

with distinct primes `p_i`. Because `mu(d)` is nonzero only on squarefree divisors, this is the alternating sum over the Boolean subset cube of the `s` distinct prime coordinates:

\[
\boldsymbol\Lambda_r(n)
=\sum_{S\subseteq\{1,\ldots,s\}}
(-1)^{|S|}
\left(
\sum_{i=1}^{s}(a_i-1_{i\in S})e_{p_i}
\right)^{\otimes r}.
\]

This is the `s`-fold finite difference of a tensor polynomial of degree `r`. Therefore:

### Support bound

\[
\boxed{s>r\Longrightarrow\boldsymbol\Lambda_r(n)=0.}
\]

### Top-shell formula

If `s=r`, every surviving tensor word uses each distinct prime direction exactly once, so

\[
\boxed{
\boldsymbol\Lambda_r(n)
=\sum_{\sigma\in S_r}
 e_{p_{\sigma(1)}}\otimes\cdots\otimes e_{p_{\sigma(r)}}.
}
\]

The result is independent of the positive exponents `a_i` at top support dimension.

After commutative scalarization, the top mixed coefficient is

\[
\boxed{r!\prod_{i=1}^{r}\log p_i.}
\]

Geometric meaning:

- the Boolean subset cube is the exact Möbius inclusion/exclusion carrier;
- the `r!` surviving ordered tensor words are the maximal ordered histories that add `r` distinct coordinates and recoalesce at the same endpoint;
- `r=3` is exactly the six-history `S_3` Hamming provenance fiber isolated in the parent frontier and formalized separately in PR #1228;
- `r=2` supplies the ordered-pair energy needed by the prime-number-theorem route.

Thus the previous `3!` phenomenon and the present Selberg quadratic identity are two levels of one factorial provenance hierarchy.

---

## PWRG-T06 — Exact quadratic current conservation

For `r=1`, PWRG-T05 gives

\[
\boldsymbol\Lambda_1(n)
=\begin{cases}e_p,&n=p^a,\\0,&\text{otherwise}.
\end{cases}
\]

For `r=2`, direct classification by the number of distinct prime directions gives

\[
\boxed{
\boldsymbol\Lambda_2(n)
=\boldsymbol\Lambda_1(n)\otimes\ell(n)
+\sum_{ab=n}
\boldsymbol\Lambda_1(a)\otimes\boldsymbol\Lambda_1(b).
}
\]

- If `n=p^a`, the first term contributes `a` copies of `e_p tensor e_p`, while the ordered proper prime-power splittings contribute `a-1`, totaling `2a-1`.
- If `n=p^a q^b` with `p!=q`, the only nonzero convolution terms are the two orderings `(p^a,q^b)` and `(q^b,p^a)`.
- If `n` has at least three distinct prime factors, both sides vanish.

Under the scalar readout `e_p -> log p`, define

\[
\Lambda_r(n):=\sum_{d\mid n}\mu(d)\log^r(n/d).
\]

Then

\[
\boxed{
\Lambda_2(n)
=\Lambda(n)\log n+(\Lambda*\Lambda)(n).
}
\]

This is an exact identity at every finite integer `n`.

---

## PWRG-T07 — Möbius-primitive quadratic spectral energy

Let

\[
E_2(q):=\operatorname{Tr}\bigl((\log K_q^+)^2\bigr)
=\sum_{m\le q}\log^2 m.
\]

Define its quotient-scale primitive renormalization

\[
\mathcal E_2^{\rm prim}(M)
:=\sum_{d\le M}\mu(d)E_2(\lfloor M/d\rfloor).
\]

Swapping the finite sums gives

\[
\mathcal E_2^{\rm prim}(M)
=\sum_{n\le M}\Lambda_2(n).
\]

Using PWRG-T06,

\[
\boxed{
\mathcal E_2^{\rm prim}(M)
=\sum_{n\le M}\Lambda(n)\log n
+\sum_{ab\le M}\Lambda(a)\Lambda(b).
}
\]

Both terms on the right are nonnegative. They have distinct finite meanings:

1. `sum Lambda(n) log n` is the self-energy of newly born winding layers;
2. `sum_{ab<=M} Lambda(a)Lambda(b)` is the weighted mass of ordered two-layer histories whose multiplicative endpoint lies below the cutoff.

This is the natural finite energy candidate for stabilizing the first primitive trace `psi(M)`.

---

## PWRG-T08 — The native central diamond is a dyadic carry projector on the current

For every `N>=1`, Legendre valuation gives

\[
v_p\binom{2N}{N}
=\sum_{a\ge1}
\left(
\left\lfloor\frac{2N}{p^a}\right\rfloor
-2\left\lfloor\frac{N}{p^a}\right\rfloor
\right).
\]

Each coefficient

\[
\epsilon_N(q)
:=\left\lfloor\frac{2N}{q}\right\rfloor
-2\left\lfloor\frac{N}{q}\right\rfloor
\]

lies in `{0,1}`. Consequently

\[
\boxed{
\log\binom{2N}{N}
=\sum_{p^a\le2N}\epsilon_N(p^a)\log p
=\sum_{q\le2N}\epsilon_N(q)\Lambda(q).
}
\]

This identifies the #1161 central balanced-return shell as a positive dyadic carry mask on the prime-power winding birth current. The existing exact relation

\[
v_p\binom{2N}{N}=\text{number of base-}p\text{ carries in }N+N
\]

is therefore not merely an arithmetic afterthought: it is the finite readout through which the native commuting-diamond provenance process samples the saturated winding current.

It yields linear-scale positive information and elementary Chebyshev-type control, but the family of dyadic masks is not yet inverted sharply enough to force `psi(M)/M -> 1`.

---

## PWRG-N01 — Why the exact first-order determinant RG is not yet the PNT

The first-order identity

\[
\psi(M)=\sum_{k\le M}\mu(k)\log(\lfloor M/k\rfloor!)
\]

contains strong signed cancellation across quotient scales. Knowing only the leading Stirling-scale size of each full-spectrum determinant does not automatically control that cancellation uniformly.

Likewise, the central-binomial carry projector supplies positive linear-scale averages of `Lambda`, but a bounded family of such masks gives only Chebyshev-scale upper/lower information unless a stable inversion or decorrelation theorem is added.

The exact algebra therefore rules out two premature claims:

1. `M!` plus formal Möbius inversion alone has already proved `psi(M)~M`;
2. the Wallis central binomial carrier alone pointwise determines the prime-power current.

The new quadratic energy PWRG-T07 is the first candidate with enough self-correlation information to suppress persistent linear-size oscillation.

---

## 9. Next acceptance gate

The next theorem should be stated entirely in finite terms.

Define

\[
R(M):=\psi(M)-M.
\]

Seek an explicit cutoff-uniform inequality derived from PWRG-T06/T07 of the form

\[
\boxed{
|R(M)|
\le
\eta\,\max_{M^\alpha\le t\le M}|R(t)|
+o(M)
}
\]

for some fixed `0<eta<1` and `0<alpha<1`, or an equivalent averaged contraction. Iteration would force `R(M)=o(M)`.

The classical Selberg route indicates that the necessary quadratic information exists, but this project must still:

- derive the relevant summatory estimate from the finite spectral energy rather than cite the final PNT machinery;
- keep all floor/cutoff errors explicit;
- identify whether the contraction is naturally expressed by quotient-scale RG, dyadic carry masks, or a combination;
- avoid silently importing a complex-analytic zero-free statement.

A successful finite contraction would convert the present exact carrier into the desired Enterprise derivation of the prime-number-theorem scale.

---

## 10. Artifact and status boundary

Companion checker:

- `scripts/check_free_research_prime_winding_selberg_rg.py`

It verifies with integers, `Fraction`, and formal prime tensors:

- winding tower determinant = `lcm(1,...,M)`;
- prime-power jump law;
- factorial/quotient-lcm product and Möbius inverse;
- tensor hierarchy support and top-shell permutation formula;
- exact quadratic Selberg tensor identity;
- dyadic carry-projector reconstruction of the central binomial coefficient.

No floating target for `tau`, no numerical PNT assumption, and no zeta-zero information is used.

Current classification:

- saturated winding determinant: `PROVED / EXACT FINITE`;
- quotient determinant factorization: `PROVED / EXACT FINITE`;
- floor Möbius inverse: `PROVED / EXACT FINITE`;
- factorial provenance hierarchy: `PROVED / EXACT ALGEBRAIC`;
- quadratic primitive-energy identity: `PROVED / EXACT FINITE`;
- central-diamond carry projector: `PROVED / EXACT FINITE`;
- `psi(M)~M` from project-native finite contraction: `OPEN`;
- Foundation / Working Truth promotion: `NO`.
