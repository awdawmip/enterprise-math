# D25 / Original W216: exact grade-1 / grade-2 reflection reciprocity

Date: 2026-11-10 (Asia/Hong_Kong). Classification: AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Research lane: chatgpt-research-onhour-enterprise-math-20260923. Other lane identities and sessions are not used.

## Theorem (all primes p = 6m+1 > 3)

Retain the ORIGINAL signed 216 coefficient and weight:

$$
A_k=\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k}
=\frac{(2k)!(3k)!}{(k!)^5\,216^k},\qquad
W_p=\sum_{k=0}^{p-1}(6k+1)A_k.
$$

For every integer $2m+1\leq k\leq3m$, set $\iota(k)=p-k$. The map $\iota$ bijects the original valuation-one range $[2m+1,3m]$ with the original valuation-two range $[3m+1,4m]$, reversing their order. In $\mathbb F_p$ write
$$L_k=A_k/p\bmod p,\qquad H_k=A_{p-k}/p^2\bmod p.$$
Both are nonzero. The exact multiplicative reflection formula is
$$
\boxed{36k^3 L_kH_k=1\quad\hbox{in }\mathbb F_p,\qquad2m+1\le k\le3m.}\tag{R}
$$
Equivalently $H_k=(36k^3L_k)^{-1}$, without losing either band or the original index/weight.

The resulting original signed grade-two observer is
$$
\boxed{\frac{W_{2,p}}{p^2}\equiv
\sum_{k=2m+1}^{3m}\frac{1-6k}{36k^3L_k}\pmod p.}\tag{S}
$$
This is a genuine coupling to the preceding grade-one port. It is a finite-field *multiplicative* duality, not by itself a proof of cancellation of grade-zero and higher p-adic jets.

## Proof (including endpoint and sign)

The coefficient recurrence is exactly
$$
\frac{A_{k+1}}{A_k}=
\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.\tag{1}
$$
Legendre factorial valuation yields $v_p(A_k)=1$ for $2m<k\le3m$ and $v_p(A_{p-k})=2$ for $2m<k\le3m$. All factors used in (1) and in its reverse at the paired indices are p-units for $k=2m+1,\ldots,3m-1$.

Set $B_k=(A_k/p)(A_{p-k}/p^2)\bmod p$. For an interior step, compare (1) with its reversed reflection:
$$
\frac{B_{k+1}}{B_k}=
\frac{A_{k+1}}{A_k}
\frac{A_{p-k-1}}{A_{p-k}}
\equiv
\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}
\frac{36k^3}{(2k+1)(3k+1)(3k+2)}
=\left(\frac{k}{k+1}\right)^3\pmod p.\tag{2}
$$
The three negative signs in the reversed denominator cancel the negative sign from $(p-k)^3$. Thus $k^3B_k$ is constant across the entire paired interval.

Determine that constant from $k_0=2m+1$ and $p-k_0=4m$. Since $3k_0=p+2$, $8m=p+(2m-1)$, and $12m=2p-2$, Wilson's theorem gives
$$
\frac{A_{k_0}}p\equiv
-\frac{2(4m+2)!}{((2m+1)!)^5\,216^{2m+1}}\pmod p,
$$
$$
\frac{A_{4m}}{p^2}\equiv
\frac{(2m-1)!}{((4m)!)^5\,216^{4m}}\pmod p.
$$
Indeed $(p+2)!/p\equiv-2$, $(p+2m-1)!/p\equiv-(2m-1)!$, and $(2p-2)!/p\equiv-1$ modulo $p$; the last two negatives multiply to positive. Use
$$
(4m+2)!(2m-2)!\equiv-1,\quad (4m)!(2m)!\equiv-1,\quad216^{p-1}\equiv1\pmod p.
$$
It follows that
$$
B_{k_0}\equiv-\frac{2m-1}{108(2m+1)^5}
\equiv\frac{3}{32}\pmod p,
$$
because $2m-1\equiv-4/3$ and $2m+1\equiv2/3\pmod p$.
Therefore $k_0^3B_{k_0}\equiv(2/3)^3(3/32)=1/36\pmod p$, proving (R) via (2). Summing the original weights $(6(p-k)+1)\equiv1-6k$ proves (S), including both endpoints.

## Concrete reuse of the existing grade-one terminating port

The preceding proved grade-one first-jet theorem (20261110_onhour_d25_W216_grade1_short_firstjet.md) supplies, with $k_j=2m+1+j$,
$$
L_{k_j}=u_0g_j\pmod p,\quad
u_0=A_{2m+1}/p\bmod p,\quad
g_0=1,\quad
\frac{g_{j+1}}{g_j}=\frac{3(6j+7)(j+1)(3j+4)}{4(3j+5)^3}\pmod p.
$$
The recurrence is applied only for $0\le j<m-1$; all denominators are units. Substituting into (S) gives the *single-port reciprocal hypergeometric observer*
$$
\boxed{\frac{W_{2,p}}{p^2}\equiv
-\frac9{4u_0}\sum_{j=0}^{m-1}
\frac{2j+1}{(3j+2)^3g_j}\pmod p.}\tag{T}
$$
Together with the older independent grade-two bridge $W_{2,p}/p^2=K_p\mathcal H_{m-1}$, (T) supplies a same-original-class equality between two length-$m$ terminating descriptions of the grade-two readout.

## Executed arithmetic / BRC observation scope

The attached standard-library checker validates (R), (S), and (T) by exact integer modular arithmetic for every one of the 148 primes $p\le2000$, $p\equiv1\bmod6$: 22,952 individually paired coefficients. For $p=7,13,19,373$ an independent original integer-binomial construction checks both coefficients of every pair (138 original terms across these samples). No floating-point calculations.

Selected outputs: $p=13$, $(u_0,W_{2,p}/p^2)=(2,10)$; $p=19$, $(14,9)$; $p=373$, $(320,266)$; $p=997$, $(377,27)$, all modulo their own $p$. At $p=373$, $L_{125}=320$, $H_{125}=181$, and their product is $105=1/(36\cdot125^3)$ modulo 373.

BRC carrier = labeled pair $(k,p-k)$ plus original $A_k,A_{p-k}$, valuation $(1,2)$, unit pair $(L,H)$, and signed original weights $(6k+1,6(p-k)+1)$. Observer = $W_{2,p}/p^2\bmod p$; future operations = the existing grade-1 first jet, grade-0 second jet, and original signed total divided by $p^2$ at mod-$p^3$ precision. Formula (R) proves a reversible *leading-unit* coordinate change on this paired domain. It does not identify the $p^2$ first jet of grade one, does not reconstruct the signed total without the grade-zero and cross-grade carries, and does not change native H0/B0 requirements.

The still-open mother target is $\Delta_p-R_p=0\bmod p$ for $p\equiv13,19\bmod24$. Next precise action: test/derive a signed finite telescoper combining the grade-zero second jet, the grade-one first jet and this one-port grade-two reciprocal observer, retaining both parities of $m$. The original p=373 H0/B0 divided-power rank, $[X]U\bmod139129$, semilinear direction, normalization $\eta$, odd observer, $\kappa$, $\Delta_p-R_p$, independent reproduction remain NOT_RUN/PENDING_OWNER in Issue #1559.

Source boundary: this proof is author-side UNREVIEWED/NOT_ADMITTED; there is no current authenticated winning native claim/run for this Research lane.
