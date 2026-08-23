# P017 — P2 Root Detector and Chen Carry Bridge

Status: `PROVED_WIP BRIDGE + PRIOR-ART IDENTIFICATION + NUMERICAL ROUTE DIAGNOSTIC / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-23`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Base seen: `main@bd10bc351dbe7c90b47a3ffba3ef7796479170f5`

Scope: consecutive-square basin `I_K={K^2+1,...,K^2+2K}`, P017 divisibility hit counts, and the exact interface to classical Chen/Iwaniec–Laborde short-interval P2 remainder terms.

## 0. Boundary and correction of the preceding exploratory route

This note supersedes one exploratory idea only: a constant extra penalty such as `lambda/2=0.415` on a selected high-prime band is **not** a complete pointwise P2 detector. In the low-low-large three-factor geometry it can leave positive weight.

The corrected route has two layers:

1. an exact square-root-normalized pointwise P2 detector with a linearly vanishing prime weight;
2. a precise reduction of the resulting odd/binary P017 remainder to the standard floor remainder already occurring in Chen-style bilinear sieve estimates.

No claim is made that this proves a P2 in every consecutive-square interval. Classical work already proves P2 existence in sufficiently large short intervals; the still-interesting project boundary is an explicit/all-K bridge and whether P017 square-root structure can simplify or sharpen the analytic remainder treatment.

Prior-art anchor: J.-R. Chen, *On the distribution of almost primes in an interval* (Scientia Sinica 18 (1975), 611–627); H. Iwaniec and M. Laborde, *P2 in short intervals*, Ann. Inst. Fourier 31 (1981), 37–56, DOI `10.5802/aif.848`.

---

## 1. Notation

For `K>=2`, put

\[
I_K=\{K^2+1,\ldots,K^2+2K\},
\qquad W=K+1,
\qquad M=K(K+1).
\]

For `m>=1`, retain the canonical P017 hit count

\[
H_m(K)
=
\left\lfloor\frac{K^2+2K}{m}\right\rfloor
-
\left\lfloor\frac{K^2}{m}\right\rfloor.
\]

Define the odd-quotient / binary-projected count

\[
O_m(K):=H_m(K)-H_{2m}(K).
\]

Let `Omega(n)` count prime factors with multiplicity and `nu_p(n)` denote the p-adic multiplicity.

---

## 2. P2-R01 — Exact square-root-normalized P2 sign detector

Define

\[
\boxed{
\omega_K(n)
=
1-
\sum_{\substack{p<W\\p\mid n}}
\nu_p(n)
\left(1-\frac{\log p}{\log W}\right)
}
\qquad(n\in I_K).
\]

### Theorem

For every `K>=2` and every `n in I_K`,

\[
\boxed{
\omega_K(n)>0
\iff
\Omega(n)\le2.
}
\]

In particular,

\[
\Omega(n)\ge3\Longrightarrow\omega_K(n)<0.
\]

### Proof

Because `n<W^2`, at most one prime factor of `n`, counted with multiplicity, can be `>=W`; otherwise the product of two such factors would be at least `W^2>n`.

Let `h` be the number of visible prime factors `<W`, counted with multiplicity, and let

\[
v=\prod_{p<W}p^{\nu_p(n)}.
\]

Then

\[
\omega_K(n)=1-h+\frac{\log v}{\log W}.
\]

If every prime factor is visible, then `h=Omega(n)` and `v=n`. Since `W<n<W^2` for `K>=2`,

\[
1<\frac{\log n}{\log W}<2.
\]

Thus `Omega(n)=2` gives positive weight and `Omega(n)>=3` gives negative weight. (The case `Omega(n)=1` cannot have its only prime factor `<W`, because `n>W`.)

If exactly one prime factor `q>=W` is invisible, then `h=Omega(n)-1` and

\[
v=n/q<W.
\]

For `Omega(n)=1`, `h=0` and the weight is `1`. For `Omega(n)=2`, `h=1` and `v` is a visible prime, so `omega_K(n)=log(v)/log(W)>0`. For `Omega(n)>=3`, `h>=2` and

\[
\omega_K(n)
=1-h+\frac{\log v}{\log W}
<2-h\le0.
\]

The inequality is strict. This proves the theorem. ∎

### Consequence

The correct high-end penalty is not a constant. It is the root-normalized linear weight

\[
\boxed{
\rho_K(p)=1-\frac{\log p}{\log(K+1)},
\qquad p<K+1,
}
\]

which tends exactly to zero at the square-root visibility boundary.

This is structurally aligned with the high-prime linear-to-zero weights in Chen/Laborde-style weighted sieves; no historical novelty is claimed for logarithmic sieve weights.

---

## 3. P2-R02 — Exact centered odd-radius representation of the P017 binary carry

Assume `m` is odd. Since

\[
I_K=M+\{1-K,\ldots,K\}
\]

and `M` is even, `H_m-H_{2m}` selects precisely those multiples `m q` for which the quotient `q` is odd. For odd `m`, this is equivalent to the state itself being odd, hence to the centered radius being odd.

Therefore

\[
\boxed{
O_m(K)
=
\#\{s:\ 1-K\le s\le K,\ s\text{ odd},\ m\mid M+s\}.
}
\]

There are exactly `K` odd radii in that centered interval. They form an arithmetic progression of step `2`, and `2` is invertible modulo odd `m`. Consequently one residue class modulo `m` is selected among a length-`K` consecutive progression, giving

\[
\boxed{
O_m(K)=\left\lfloor\frac Km\right\rfloor+\varepsilon_m(K),
\qquad
\varepsilon_m(K)\in\{0,1\}.
}
\]

Hence the pointwise discrepancy satisfies

\[
\boxed{
\left|O_m(K)-\frac Km\right|<1.
}
\]

In the super-root zone `m>K`,

\[
\boxed{O_m(K)\in\{0,1\}.}
\]

Thus the deep-level P017 object is literally a sparse single-incidence field: `one hit minus its natural density K/m`.

---

## 4. P2-R03 — Exact transfer to the standard Chen short-interval floor remainder

Define the ordinary divisibility remainder

\[
r_K(q)
:=H_q(K)-\frac{2K}{q}.
\]

Then, identically for every `m>=1`,

\[
\begin{aligned}
O_m(K)-\frac Km
&=H_m(K)-H_{2m}(K)-\frac Km\\
&=\left(H_m(K)-\frac{2K}{m}\right)
 -\left(H_{2m}(K)-\frac{K}{m}\right).
\end{aligned}
\]

Therefore

\[
\boxed{
O_m(K)-\frac Km
=r_K(m)-r_K(2m).
}
\]

This is the central bridge.

### Analytic consequence

Any bilinear estimate that is uniform for the standard short-interval floor remainder `r_K(q)` over a modulus family immediately transfers to the P017 binary/odd-quotient remainder, after applying the same estimate once at `q=m` and once at `q=2m` (with the corresponding doubled modulus range).

Thus, at the asymptotic/theoretical level, the P017 prime-lift carry remainder is **not a new species of distribution problem**. It is an odd-parity projection of the classical Chen floor remainder.

Iwaniec–Laborde explicitly identify Chen's innovation as the nontrivial treatment of double sums of such error terms, using Fourier expansion followed by exponential-sum estimates. Their linear-sieve error is organized into bilinear forms with bounded coefficients. The current P017 bridge shows exactly where the binary carry family enters that existing analytic interface.

The new project question is therefore narrower:

> can the special square-root coupling `x=K^2`, the centered numerator `M=K(K+1)`, and the P017 collision/capacity structure make the required **explicit** bilinear constants or depth cheaper than in the generic short-interval theorem?

---

## 5. P2-R04 — Super-root collision barrier

Let `m_1,m_2>K` be odd and suppose both odd-incidence events occur at the same centered radius `s`, i.e.

\[
m_1\mid M+s,
\qquad
m_2\mid M+s.
\]

Then

\[
\operatorname{lcm}(m_1,m_2)\mid M+s<(K+1)^2.
\]

Hence

\[
\boxed{
\gcd(m_1,m_2)
>
\frac{m_1m_2}{(K+1)^2}.
}
\]

So two deep moduli can reuse one odd radius only if they share a quantitatively large common divisor.

For prime-lift moduli `m_i=p_i d_i` with distinct primes `p_i>z` and `d_i` supported only on primes `<z`, one has

\[
\gcd(m_1,m_2)=\gcd(d_1,d_2),
\]

so a same-radius collision forces a large common **small-prime core** in the two sieve variables.

This is compatible with the existing P017 signed-capacity/collision geometry. It is exact but, by itself, is not yet a replacement for the classical bilinear exponential-sum saving.

---

## 6. P2-R05 — Semiprimes as primes in disjoint P017 cofactor windows

For each prime `p<=K`, define the canonical cofactor window

\[
W_p(K)
=
\left[
\left\lfloor\frac{K^2}{p}\right\rfloor+1,
\left\lfloor\frac{K^2+2K}{p}\right\rfloor
\right].
\]

Then

\[
q\in W_p(K)
\iff
K^2<pq<(K+1)^2.
\]

The canonical P017 L054 theorem gives, for `K>=4` and distinct primes `p<r<=K`,

\[
\max W_r(K)<\min W_p(K).
\]

Thus these windows are pairwise disjoint.

Every semiprime in `I_K` has two distinct prime factors (there is no perfect square strictly between consecutive squares). Writing it uniquely as `pq` with `p<q`, one has `p<=K` and `q in W_p(K)`. Conversely a prime `q in W_p(K)` produces the semiprime `pq in I_K`.

Therefore, for `K>=4`,

\[
\boxed{
\#\{n\in I_K:\Omega(n)=2\}
=
\#\left(
\mathbb P\cap
\bigsqcup_{\substack{p\le K\\p\text{ prime}}}
W_p(K)
\right).
}
\]

This is an exact no-overlap reformulation of the semiprime part of the P2 problem. It does not solve the prime-in-union problem; analytically it is another face of the short-interval semiprime distribution problem.

---

## 7. What happens to the original `H_{pd}-H_{2pd}` double remainder

Suppose a weighted sieve produces

\[
\mathcal R
=
\sum_p\sum_d c_p\lambda_d
\left(O_{pd}(K)-\frac{K}{pd}\right).
\]

Using P2-R03,

\[
\boxed{
\mathcal R
=
\sum_{p,d}c_p\lambda_d r_K(pd)
-
\sum_{p,d}c_p\lambda_d r_K(2pd).
}
\]

Therefore:

- if the level is kept below the root (`pd<K`), the aggregate remainder can often be bounded absolutely and no parity-breaking theorem is needed — but this does not cross the weighted-sieve `1/2` barrier;
- to obtain a genuine P2 result by this route, one must deliberately enter `pd>K` for part of the support;
- that super-root part is exactly the Chen bilinear-remainder zone.

This corrects the earlier wording “prove a new average-distribution theorem for the carry family”. The right statement is:

> either **consume** the established Chen/Iwaniec bilinear remainder theorem after the exact P017 transfer, or prove a genuinely stronger/simpler square-specialized version only if the P017 root coupling supplies additional saving.

---

## 8. Prior-art checkpoint: why this is the right analytic boundary

Iwaniec–Laborde (1981) record that weights alone do not reach short-interval exponent `theta<=1/2`, and describe Chen's 1975 advance at `theta=1/2` as coming from nontrivial double sums of sieve error terms with Fourier expansion and exponential-sum estimates.

They further split their weighted sum into:

- a part handled by a linear sieve whose remainder is a bilinear form
  \[
  \sum_m\sum_n a_m b_n r(mn),\qquad |a_m|,|b_n|\le1;
  \]
- a high-prime part treated separately by Selberg's two-dimensional sieve.

Their theorem obtains a P2 in intervals of length `x^0.45` for sufficiently large `x`, so asymptotic P2 existence between sufficiently large consecutive squares is already prior art. The present note does not claim otherwise.

---

## 9. Numerical route diagnostic — shallow super-root depth

**Status: `DIAGNOSTIC ONLY / NOT A THEOREM`.**

Iwaniec–Laborde publish at `theta=0.45` the rounded optimizer

\[
c=5.1828\ldots,
\quad
b=4.8698\ldots,
\quad
G(b,c)=0.00177\ldots.
\]

Using their displayed closed formulas on pp. 53–54 to infer the two constants from Laborde [1979], and then re-optimizing the same displayed main-term function at `theta=1/2` while allowing a smaller level `D=x^delta`, gives a diagnostic sign change near

\[
\boxed{\delta\approx0.52854.}
\]

The published decimal rounding moves this value only in the last few `10^-6` in the reconstruction, but the calculation remains non-authoritative until the exact constants from Laborde [1979] are directly sourced and the full hypotheses are replayed.

In square notation `x approximately K^2`, this corresponds to

\[
D\approx K^{1.05709}.
\]

So the classical weight diagnostic suggests that only a shallow super-root strip

\[
K<m\lesssim K^{1.0571}
\]

needs genuine parity-breaking remainder control at `theta=1/2`, rather than the whole modulus range up to the maximal level permitted by the 1981 argument.

At that diagnostic threshold the published high-prime endpoint is only slightly beyond the square root, suggesting a square-specific research target: re-derive the weight with the exact visibility cap `p<K+1` from P2-R01 and test whether the Selberg two-dimensional tail can be shortened or eliminated. This has **not** been proved in this note.

---

## 10. Current frontier

### Proved in this owner note

- `P2-R01`: exact root-normalized sign detector `omega_K(n)>0 iff Omega(n)<=2`.
- `P2-R02`: centered odd-radius representation and `O_m=floor(K/m)+epsilon_m` for odd `m`.
- `P2-R03`: exact transfer `O_m-K/m=r_K(m)-r_K(2m)`.
- `P2-R04`: same-radius deep-modulus collision forces a large gcd.
- `P2-R05`: semiprimes are exactly primes in the disjoint L054 cofactor-window union.

### Prior-art consumed, not re-proved here

- sufficiently-large short intervals of exponent `1/2` contain P2 (Chen 1975);
- the stronger exponent `0.45` result and the bilinear/Selberg decomposition (Iwaniec–Laborde 1981).

### Still open for this project route

1. An **explicit** bilinear remainder theorem with constants strong enough to overlap the available finite verification range.
2. Whether the P017 square numerator `K(K+1)`, odd-radius carrier, anchor/transverse split, or collision geometry improves that explicit remainder over the generic short-interval estimate.
3. Re-derive the Buchstab/Richert weight with the exact root visibility cap from P2-R01 and determine whether the tiny generic high-prime two-dimensional tail at `theta=1/2` is genuinely unnecessary.
4. If not, consume the classical two-dimensional high-prime estimate and focus effort exclusively on explicit constants in the shallow super-root band.

No Legendre theorem and no all-`K` P2 theorem is claimed.