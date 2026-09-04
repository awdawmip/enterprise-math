# Free Research — Prime-Winding Carry Projector and Chebyshev Scale

Status: `FREE_RESEARCH_FRONTIER / EXACT_FINITE_DIVISIBILITY / LINEAR_SCALE_PROVED / PNT_CONSTANT_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PRIME_WINDING_MOBIUS_SELBERG_RG_20260904.md`

## Executive advance

The parent note exposed

\[
\psi(M)=\log L_M,
\qquad
L_M=\operatorname{lcm}(1,\ldots,M),
\]

as the determinant of the saturated prime-winding tower and identified the central balanced-return binomial coefficient as a dyadic carry projector on the prime-power birth current.

This note converts that compatibility into exact finite divisibility and then into a project-internal linear-order theorem:

\[
\boxed{
\frac{L_{2n}}{L_n}
\mid \binom{2n}{n}
\mid L_{2n}
}
\]

for every `n>=1`. Combining this with the elementary central-shell bounds gives

\[
\boxed{
(M-1)\log 2-\log(M+1)
\le \psi(M)
<4M\log 2
}
\]

for every `M>=2` (with harmless endpoint weakening in the displayed all-M form). Hence

\[
\boxed{\psi(M)=\Theta(M)}.
\]

This proves the correct **linear macroscopic scale** of the saturated winding geometry from the same finite Hamming/commuting-diamond carrier that constructs the Wallis completion. It does not yet prove the prime-number-theorem normalization `psi(M)/M -> 1`.

---

## CWCS-T01 — Prime-power carry mask

For a prime power `q=p^a`, define

\[
\varepsilon_n(q)
:=\left\lfloor\frac{2n}{q}\right\rfloor
-2\left\lfloor\frac{n}{q}\right\rfloor.
\]

Writing `n=tq+r`, `0<=r<q`, gives

\[
\varepsilon_n(q)=\left\lfloor\frac{2r}{q}\right\rfloor\in\{0,1\}.
\]

Legendre valuation yields

\[
\boxed{
v_p\binom{2n}{n}
=\sum_{a\ge1}\varepsilon_n(p^a).
}
\]

Thus every available winding layer contributes either zero or one copy of its primitive eigenvalue `p`; no layer is counted negatively and no individual layer is repeated.

Equivalently,

\[
\boxed{
\binom{2n}{n}
=\prod_{p^a\le2n}p^{\varepsilon_n(p^a)}.
}
\]

This is the exact multiplicative form of the central balanced-return carry projector.

---

## CWCS-T02 — Upper divisibility by the saturated winding determinant

The saturated determinant at cutoff `2n` is

\[
L_{2n}=\prod_{p^a\le2n}p.
\]

Here the product is over winding layers: each prime power `p^a` contributes one copy of `p`. Since every carry coefficient `epsilon_n(p^a)` is in `{0,1}`,

\[
v_p\binom{2n}{n}
\le \#\{a:p^a\le2n\}
=v_p(L_{2n}).
\]

Therefore

\[
\boxed{
\binom{2n}{n}\mid L_{2n}.
}
\]

In log language,

\[
\boxed{
\log\binom{2n}{n}\le\psi(2n).
}
\]

---

## CWCS-T03 — The newly opened winding annulus divides the central shell

The quotient

\[
L_{2n}/L_n
\]

contains precisely the prime directions whose winding height increases between cutoffs `n` and `2n`. For each prime `p`, the valuation difference

\[
h_p(2n)-h_p(n)
\]

is either zero or one, because two consecutive powers differ by a factor at least two.

If the difference is one, there is a unique prime power `p^a` satisfying

\[
n<p^a\le2n.
\]

For this layer,

\[
\left\lfloor\frac{n}{p^a}\right\rfloor=0,
\qquad
\left\lfloor\frac{2n}{p^a}\right\rfloor=1,
\]

so `epsilon_n(p^a)=1`. Hence every newly opened saturated winding layer occurs in the central carry projector:

\[
\boxed{
\frac{L_{2n}}{L_n}\mid\binom{2n}{n}.
}
\]

In log language,

\[
\boxed{
\psi(2n)-\psi(n)
\le\log\binom{2n}{n}.
}
\]

Together with CWCS-T02:

\[
\boxed{
\frac{L_{2n}}{L_n}
\mid\binom{2n}{n}
\mid L_{2n}.
}
\]

This is stronger than a real inequality: it identifies the central Hamming shell as an exact intermediate sub-ensemble between the newly born winding annulus and the full saturated tower.

---

## CWCS-T04 — Exact finite central-shell size bounds

The binomial theorem gives

\[
\sum_{j=0}^{2n}\binom{2n}{j}=4^n.
\]

The central coefficient is the largest among the `2n+1` coefficients, hence

\[
\boxed{
\frac{4^n}{2n+1}
\le\binom{2n}{n}
\le4^n.
}
\]

No asymptotic formula and no pre-known value of `tau` is required.

Combining with CWCS-T02 gives

\[
\boxed{
(2n+1)L_{2n}\ge4^n.
}
\]

Therefore

\[
\boxed{
\psi(2n)
\ge2n\log2-\log(2n+1).
}
\]

---

## CWCS-T05 — Dyadic upper bound

Set `n=2^{j-1}` in CWCS-T03 and use the upper central-shell bound:

\[
\psi(2^j)-\psi(2^{j-1})
\le\log\binom{2^j}{2^{j-1}}
\le2^j\log2.
\]

Summing from `j=1` to `m` gives

\[
\boxed{
\psi(2^m)
\le(2^{m+1}-2)\log2.
}
\]

At the integer level,

\[
\boxed{
L_{2^m}\le4^{2^m-1}.
}
\]

For arbitrary `M>=2`, choose `m` with

\[
2^{m-1}<M\le2^m.
\]

Monotonicity then yields

\[
\psi(M)\le\psi(2^m)
<4M\log2.
\]

The constant is deliberately not optimized here; the point is a direct finite proof of linear order from the native central shell.

---

## CWCS-T06 — All-cutoff lower bound and linear order

For `M>=2`, let

\[
n=\lfloor M/2\rfloor.
\]

Then `2n<=M`, and monotonicity plus CWCS-T04 gives

\[
\psi(M)
\ge\psi(2n)
\ge2n\log2-\log(2n+1).
\]

Since `2n>=M-1` and `2n+1<=M+1`,

\[
\boxed{
\psi(M)
\ge(M-1)\log2-\log(M+1).
}
\]

Together with CWCS-T05:

\[
\boxed{
(M-1)\log2-\log(M+1)
\le\psi(M)
<4M\log2.
}
\]

Consequently

\[
\boxed{
0<\liminf_{M\to\infty}\frac{\psi(M)}M
\le\limsup_{M\to\infty}\frac{\psi(M)}M
<\infty.
}
\]

In particular,

\[
\boxed{\psi(M)=\Theta(M).}
\]

This is the first macroscopic prime-distribution theorem obtained in the current line directly from an Enterprise finite branch/spectral carrier.

---

## CWCS-T07 — Geometric reading

The exact divisibility sandwich has a clean three-layer meaning:

\[
\boxed{
\text{new winding annulus}
\subseteq
\text{central balanced-return carry shell}
\subseteq
\text{full saturated winding tower}.
}
\]

More explicitly:

1. `L_{2n}/L_n` contains every prime-power layer born in the multiplicative scale doubling `n -> 2n`;
2. `choose(2n,n)` selects those layers plus additional lower layers whose base-`p` digits generate carries under doubling;
3. `L_{2n}` contains every prime-power layer visible at the final cutoff.

The balanced commuting-diamond process therefore detects enough prime-power births to force linear global mass, while remaining a strict projector rather than the full current.

---

## CWCS-N01 — Why this is not yet the prime number theorem

The bounds prove the right order of growth but leave a nontrivial interval of possible normalized limits. The carry mask

\[
\varepsilon_n(q)
=1_{\{n/q\}\ge1/2}
\]

samples prime-power layers through a discontinuous dyadic phase. A single scale-doubling family controls total mass but does not establish the equidistribution/decorrelation needed to reconstruct the unmasked current with relative error `o(1)`.

Therefore neither of the following is claimed:

\[
\psi(M)/M\to1,
\qquad
\pi(M)\sim M/\log M.
\]

The remaining normalization problem is exactly where the quadratic primitive energy from the parent Möbius/Selberg note becomes necessary.

---

## 8. Next finite theorem target

The next step should combine:

- the positive dyadic carry projectors `epsilon_n(q)`;
- the quadratic ordered-pair energy `Lambda_2`;
- quotient-scale Möbius renormalization.

A useful target is an explicit decorrelation estimate for the centered current

\[
R(M)=\psi(M)-M
\]

against the carry family, followed by a finite contraction of the normalized oscillation. One candidate form is

\[
\left|
\sum_{q\le2n}\varepsilon_n(q)(\Lambda(q)-1)
\right|
\le o(n)
\]

uniformly after averaging over a controlled finite set of dilation/translation masks. A bounded number of fixed masks is unlikely to suffice; the quadratic energy must control the aggregate family.

---

## 9. Verification artifact

Companion checker:

- `scripts/check_free_research_prime_winding_chebyshev_scale.py`

It verifies by exact integer arithmetic:

- the carry-layer product formula for `choose(2n,n)`;
- both divisibilities in the sandwich;
- the exact central-shell integer inequalities;
- the dyadic product upper bound;
- the all-cutoff finite lower and upper envelopes in exponentiated form.

Current status:

- finite carry/divisibility chain: `PROVED / EXECUTABLE_CHECKED`;
- project-native linear order `psi(M)=Theta(M)`: `PROVED`;
- exact PNT normalization: `OPEN`;
- Foundation / Working Truth promotion: `NO`.
