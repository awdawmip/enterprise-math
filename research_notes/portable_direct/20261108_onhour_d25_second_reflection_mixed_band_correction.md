# D25 — Second reflection digit: the mixed-valuation Clausen cutoff

**Date:** 2026-11-08 (Asia/Hong_Kong). **Evidence:** author-side TASK_RESEARCH exact algebraic theorem; exact finite arithmetic checked at 77 frozen primes; **UNREVIEWED / NOT_ADMITTED**. Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923. Maintenance lane excluded: chatgpt-hourly-enterprise-math-20260921.

**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Immutable scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.

This proof consumes the earlier source-port alignment of the original reflected scalar, the first-digit cutoff and the finite Green/adjoint results. The new, discriminating question is whether the established first-digit congruence \(Q_p/p^2\equiv R_p\pmod p\) extends to its next digit. **A two-source correction is required**, with an independently surviving middle-high band.

## Definitions and the exact valuation partition

Let \(p=6m+1\) be a prime, \(p\ge13\). In the localization \(\mathbb Z_{(p)}\), define

\[
b_k=\frac{(1/6)_k(1/3)_k}{2^k(k!)^2}\quad(0\le k<p),\qquad
q_i=2^{-i}\binom mi\binom{2m}i\quad(0\le i\le m).
\]

Set \(c_1=1/10\), \(c_{a+1}/c_a=36a^2/((6a+5)(3a+2))\) for \(1\le a<2m\), and \(w(i,a)=1+6(i-a)\). The frozen original reflected scalar, now retained as an exact rational lift, is

\[
\mathcal R_m=2\sum_{i=1}^{m}\sum_{a=1}^{i}q_i w(i,a)c_a.
\]

Its reduction mod \(p\) is the original frozen \(R_p\). The exact finite Clausen cutoff retains the separate Gauss source:

\[
\mathcal Q_p=\sum_{\substack{0\le i,j<p\\i+j\ge p}}
 (6(i+j)+1)b_i b_j.
\]

The valuation of every \(b_k\) for \(k<p\) is **exactly**

\[
v_p(b_k)=
\begin{cases}
0&0\le k\le m,\\
1&m<k\le 2m,\\
2&2m<k<p.
\end{cases}\tag{BANDS}
\]

Indeed, the numerator recurrence has a unique multiple of \(p\) at \(j=m\) in \(6j+1\), and a unique multiple at \(j=2m\) in \(3j+1\). All factorial and 36-denominators are \(p\)-units in this range.

For \(0\le i\le m\), \(b_i\equiv q_i\pmod p\), by substitution of \(m=(p-1)/6\) in the binomial products. An extended upper-band relation also holds:

\[
b_{p-a}/p^2\equiv c_a\pmod p,\qquad 1\le a\le2m. \tag{BASE}
\]

**Proof of BASE.** At \(a=1\), the two numerator factors equal to \(p\) occur exactly once each. In the remaining products, the residues \(6j+1\) for \(0\le j\le p-2\), \(j\ne m\), run over \(\mathbb F_p^\times\setminus\{-5\}\), whose product is \(1/5\) by Wilson. Similarly \(3j+1\), excluding \(j=2m\), has product \(1/2\). The denominator is \(36^{p-1}((p-1)!)^2\equiv1\); hence \(b_{p-1}/p^2\equiv1/10=c_1\). The exact backward ratio

\[
\frac{b_{p-a-1}}{b_{p-a}}
=\frac{36(p-a)^2}{(6p-6a-5)(3p-3a-2)}
\equiv \frac{36a^2}{(6a+5)(3a+2)}\pmod p
\]

has unit denominators for \(a<2m\), proving the stated continuation.

Retain three *different* source lifts, with division in \(\mathbb Z_{(p)}\) before reducing:

\[
d_i=\frac{b_i-q_i}{p}\bmod p\ (1\le i\le m),\quad
v_a=\frac{b_{p-a}/p^2-c_a}{p}\bmod p\ (1\le a\le2m),\quad
u_i=\frac{b_i}{p}\bmod p\ (m<i\le2m).
\]

## Theorem: the second reflection digit

The quotient \(\mathcal Q_p/p^2\) is \(p\)-integral, and

\[
\boxed{\frac{\mathcal Q_p}{p^2}\equiv
\mathcal R_m+p(S_{\mathrm{low}}+S_{\mathrm{mid}})\pmod{p^2}.}
\tag{SECOND-REFLECTION}
\]

The independently observable corrections are

\[
\begin{aligned}
S_{\mathrm{low}}&=
2\sum_{i=1}^{m}\sum_{a=1}^{i}
\bigl[w(i,a)(d_ic_a+q_iv_a)+6q_ic_a\bigr],\\
S_{\mathrm{mid}}&=
2\sum_{i=m+1}^{2m}\sum_{a=1}^{i}w(i,a)u_ic_a.
\end{aligned}\tag{PORTS}
\]

**Proof.** The condition \(i+j\ge p\) and (BANDS) leaves just two kinds of ordered pairs with total \(p\)-valuation below four: low-high \((0\le i\le m,\ j=p-a,\ 1\le a\le i)\), whose valuation is two, and middle-high \((m<i\le2m,\ j=p-a,\ 1\le a\le i)\), whose valuation is three; both include symmetric reversals, giving the factor 2. A low-low, low-middle or middle-middle pair has sum below \(p\). A high-high pair has valuation at least four and vanishes modulo \(p^4\). For \(j=p-a\) the weight is **exactly** \(6(i+j)+1=w(i,a)+6p\).

On low-high pairs insert \(b_i=q_i+pd_i\pmod{p^2}\) and \(b_{p-a}/p^2=c_a+pv_a\pmod{p^2}\); the constant term is \(\mathcal R_m\), and the order-\(p\) contribution is \(pS_{\mathrm{low}}\). On middle-high pairs insert \(b_i/p=u_i\pmod p\) and \(b_{p-a}/p^2=c_a\pmod p\), giving \(pS_{\mathrm{mid}}\). All other contributions vanish modulo \(p^2\) after division by \(p^2\). QED.

## The next exact original-LIFT interface

Retain the original low Gauss \(M=\sum_{k<p}b_k\), its moment \(N=\sum_{k<p}kb_k\), \(h=M+12N\), \(G=M/p\), weighted original \(W\), and original \(\Delta=(Gh-1)/p\). Under the already established first-digit divisibilities \(p\mid M\), \(p\mid(Gh-1)\), the exact Clausen convolution \(W=Mh-\mathcal Q_p\) yields

\[
\Delta-\mathcal Q_p/p^2=(W-p)/p^2.
\]

Consequently,

\[
\boxed{\Delta-\mathcal R_m\equiv
(W-p)/p^2+p(S_{\mathrm{low}}+S_{\mathrm{mid}})\pmod{p^2}.}
\tag{LIFT-2}
\]

When \(W\equiv p\pmod{p^3}\) at a declared prime, the next divided observation is

\[
\boxed{\frac{\Delta-\mathcal R_m}{p}\equiv
\frac{W-p}{p^3}+S_{\mathrm{low}}+S_{\mathrm{mid}}\pmod p.}
\tag{NEXT-DIGIT}
\]

The target \(\Delta_p-R_p\equiv0\pmod p\) remains the original mother objective. The equations above precisely quantify the extra mixed-band information required for its second-digit extension; they neither rename the original \(R_p\) nor rely on native CM substitution.

## Independent reproducible finite witnesses

The standalone checker **d25_second_reflection_digit_check_20261108.py** computes both Gauss and weighted \(3F_2\) coefficient streams modulo \(p^4\), the Clausen cutoff using independent suffix zeroth/first moments, and the original rational reflected \(\mathcal R_m\) without using the cutoff. It checks valuation bands, extended BASE, both corrections, and LIFT-2 for all **77 primes** \(p\le2000\), \(p\bmod24\in\{13,19\}\). All 77 passed; each sampled \(S_{\mathrm{low}},S_{\mathrm{mid}},S_{\mathrm{total}}\) is nonzero.

| p | R mod p² | Q/p² mod p² | S_low | S_mid | S_total | (W-p)/p³ | (Delta-R)/p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 130 | 104 | 9 | 2 | 11 | 9 | 7 |
| 19 | 202 | 221 | 18 | 2 | 1 | 12 | 13 |
| 37 | 122 | 1084 | 23 | 3 | 26 | 19 | 8 |
| 43 | 789 | 1563 | 13 | 5 | 18 | 19 | 37 |
| 67 | 1227 | 4443 | 33 | 15 | 48 | 55 | 36 |
| 211 | 6238 | 19742 | 43 | 21 | 64 | 192 | 45 |
| 373 | 52416 | 65844 | 252 | 157 | 36 | 228 | 264 |

For \(p=373\): \(S_{\mathrm{low}}+S_{\mathrm{mid}}=252+157=409\equiv36\pmod{373}\);
\((65844-52416)/373=36\);
\((228+36)\bmod373=264\).
The independent middle-high contribution is material even though the original first-digit identity remains valid.

## Continuation and authority

This is an author-side proof and independently checkable arithmetic, **UNREVIEWED / NOT_ADMITTED**, not a Source-native checkpoint. The native same-original-class \(p=373\) H0/B0 divided-power \([X]U\), Frobenius direction and signed Hesse \(\kappa\) remain pending under issue #1559; its owner remains unassigned in the last read. The frozen publication and scientific pin are unchanged. Next exact inquiry: compare the explicit low-high, middle-high and original reflected ports against original signed \((ZH_0-1)/p\), \(SH_0\), \(ZH_1\), \(\Phi_{xx}\), first for \(p=19,373\), then seek a Fricke/Cartier proof.

Native target request **onhour11-20261106-1400-exact-research-lane-continuation** is preserved. On this turn status/reconcile returned **BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE**, operation_sent=false; Site reported **CONFIGURED_NOT_LIVE_VERIFIED**, research_authority_granted=false. No own Source session/claim/run/checkpoint is verified. Current required execution configuration is the authorized Site-bound backend client and secure credential, distinct from the maintenance lane identity.


## Second research unit — explicit normalized middle-high kernel

The newly identified middle band has an independent closed, reusable normalization in terms of the original terminal Hasse coefficient, **without using any full b-series or fitted Delta**. For \(1\le r\le m\), write \(u_{m+r}=b_{m+r}/p\bmod p\), and \(q_m=2^{-m}\binom{2m}{m}\), which is a unit. Then

\[
\boxed{u_{m+r}=\frac{q_m}{50}K_r\pmod p,\qquad
K_1=1,\qquad
K_{r+1}=\frac{3r(6r+1)}{(6r+5)^2}K_r.}
\tag{MID-KERNEL}
\]

Equivalently,
\[
K_r=\frac{(r-1)!(7/6)_{r-1}}{2^{r-1}(11/6)_{r-1}^{\,2}}\pmod p.
\]

**Proof.** The exact b-series recurrence is \(b_{k+1}/b_k=(6k+1)(3k+1)/(36(k+1)^2)\). At \(k=m\), the factor \(6m+1=p\) gives
\[
u_{m+1}=\frac{b_m(3m+1)}{36(m+1)^2}
\equiv\frac{q_m}{50}\pmod p,
\]
since \(3m+1\equiv1/2\), \(36(m+1)^2\equiv25\). For \(k=m+r\) with \(1\le r<m\), reduce the b ratio:
\[
\frac{u_{m+r+1}}{u_{m+r}}\equiv
\frac{(6r)((6r+1)/2)}{(6r+5)^2}
=\frac{3r(6r+1)}{(6r+5)^2}\pmod p.
\]
The product formula follows by elementary Pochhammer multiplication. Every denominator is a unit for \(1\le r<m\). QED.

Extend the *original* reflected H-observer, without changing its definition, from \(0\le i\le m\) to \(0\le i\le 2m\):
\[
H_i=\sum_{a=1}^{i}(1+6(i-a))c_a.
\]
The entire middle-high source becomes the one-dimensional exact finite-field readout
\[
\boxed{S_{\mathrm{mid}}=\frac{q_m}{25}\sum_{r=1}^{m}K_rH_{m+r}\pmod p.}
\tag{MID-READOUT}
\]
This gives a direct bridge from the earlier original reflected/adjoint H-kernel to the previously unseen middle-high cutoff sector, retaining the extension \(H_{m+1},\ldots,H_{2m}\) as distinct observable data.

The updated checker evaluates MID-READOUT with **only** \(q_m\), the c recurrence, \(K_r\) and finite prefix moments for H, and compares against the independently obtained full-cutoff S_mid for all 77 target primes \(p\le2000\); every comparison passes. In particular:

| p | q_m | sum(K_r H_(m+r)) | S_mid |
|---:|---:|---:|---:|
| 13 | 8 | 3 | 2 |
| 19 | 12 | 1 | 2 |
| 43 | 8 | 21 | 5 |
| 67 | 5 | 8 | 15 |
| 373 | 13 | 15 | 157 |

The next proof interface can now consume the independent normalized K-H middle port and the low-high d/v correction simultaneously; the native p=373 requirements remain exactly those listed above.
