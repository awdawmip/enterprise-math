# D25 — Cubic Clausen correction and full signed fourth-digit interface

Date: 2026-11-05 (+08). Role: TASK_RESEARCH, portable author-side mathematics. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; immutable publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific input \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.

Status: **AUTHOR-PROVED algebraic congruence; 35-prime exact BigInt check; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM**. The pre-existing six-port and fourth-order shell identities are *inputs* to the new bridge, not new completed units.

## Theorem: third signed Q digit from a Clausen cubic correction and four source shells

Let \(p=6n+1\ge7\) be prime, work in \(\mathbb Z_{(p)}\), and set

\[
W_p=\sum_{k=0}^{p-1}(6k+1)\frac{(1/2)_k(1/3)_k(2/3)_k}{2^k(k!)^3},
\quad G(z)={}_2F_1(-n,-2n;1-p/2;z),\quad
\Psi=G(1/2)\bigl(G(1/2)+12J\bigr),
\quad J=(zG'(z))_{z=1/2}.
\]

For \(m=(3n,2n,4n)\) and \(b=(1/2,1/3,2/3)\), put \(\nu_k=\#\{j:k>m_j\}\), and use the exact p-factor-extracted coefficient

\[
d_k=\frac{1}{2^k(k!)^3}
\prod_{j=1}^3\left[
b_j^{\mathbf 1_{k>m_j}}
\prod_{\substack{0\le r<k\\r\ne m_j}}(r-m_j)\right].
\]

Define \(h_{s,k}=\sum_{j=1}^3\sum_{0\le r<k,r\ne m_j}(b_j/(r-m_j))^s\), \(s=1,2,3\), and the elementary symmetric jets

\[
e_{1,k}=h_{1,k},\quad e_{2,k}=(h_{1,k}^2-h_{2,k})/2,\quad
e_{3,k}=(h_{1,k}^3-3h_{1,k}h_{2,k}+2h_{3,k})/6.
\]

Write \(w_k=6k+1\) and retain all **six old signed source ports**

\[
S=\sum_{\nu=0}w_kd_k,\quad A=\sum_{\nu=0}w_kd_ke_{1,k},\quad
B=\sum_{\nu=1}w_kd_k,
\]
\[
C=\sum_{\nu=0}w_kd_ke_{2,k},\quad
D=\sum_{\nu=1}w_kd_ke_{1,k},\quad
E=\sum_{\nu=2}w_kd_k.
\]

The **four third-order shell coordinates** are

\[
T_0=\sum_{\nu=0}w_kd_ke_{3,k},\quad
T_1=\sum_{\nu=1}w_kd_ke_{2,k},\quad
T_2=\sum_{\nu=2}w_kd_ke_{1,k},\quad
T_3=\sum_{\nu=3}w_kd_k.
\]

All sums above run over \(0\le k<p\) subject to the indicated \(\nu_k\), and all denominators are p-units. In the \(\nu=0\) range \(d_k=(-1)^k2^{-k}\binom{2n}{k}\binom{3n}{k}\binom{4n}{k}\). Set the ordinary harmonic numbers \(H_k^{(s)}=\sum_{j=1}^k j^{-s}\), and define

\[
\alpha=\sum_{k=0}^{2n}w_kd_k\,\frac32H_k^{(1)},
\quad
\beta_*=\sum_{k=0}^{2n}w_kd_k\,\frac{9(H_k^{(1)})^2+5H_k^{(2)}}8,
\]
\[
\boxed{\gamma=\sum_{k=0}^{2n}w_kd_k\,
\frac{9(H_k^{(1)})^3+15H_k^{(1)}H_k^{(2)}+6H_k^{(3)}}{16}.}
\]

Define three typed signed observer coordinates
\(F=A+B-\alpha\), \(H=C+D+E-\beta_*\), and
\(\boxed{I=T_0+T_1+T_2+T_3-\gamma}\). Then, for **every** stated prime,

\[
\boxed{W_p-\Psi\equiv pF+p^2H+p^3I\pmod{p^4}},
\qquad
\boxed{Q_p=\frac{W_p-\Psi}{p}\equiv F+pH+p^2I\pmod{p^3}.}
\]

The second congruence is the requested source-explicit third-digit extension of the earlier two-digit \(Q_p=F+pH\bmod p^2\). The new \(\gamma\) is the **cubic terminating-Clausen denominator correction**; the other four third-order coordinates come from distinct original-216 valuation strata. This is an all-\(p\) algebraic statement about the exact original signed source and the terminating Clausen observer, not a uniform \(W_p=p\bmod p^3\) proof.

## Proof

The terminating Clausen identity gives
\[
G(z)^2={}_3F_2(-2n,-3n,-4n;1-p/2,1-p;z).
\]
The ratio of its \(k\)-th coefficient to the integer-shadow coefficient is
\(R_k=\prod_{j=1}^k(1-p/(2j))^{-1}(1-p/j)^{-1}\). Each \(j\le2n<p\) is a p-unit. Expanding the *finite* product formally through \(p^3\),

\[
\log R_k\equiv
\frac{3p}{2}H_k^{(1)}+\frac{5p^2}{8}H_k^{(2)}
+\frac{3p^3}{8}H_k^{(3)}\pmod{p^4},
\]

\[
R_k\equiv1+\frac{3p}{2}H_k^{(1)}
+\frac{p^2}{8}(9(H_k^{(1)})^2+5H_k^{(2)})
+\frac{p^3}{16}(9(H_k^{(1)})^3+15H_k^{(1)}H_k^{(2)}+6H_k^{(3)})
\pmod{p^4}.
\]

This calculation can equally be obtained by finite geometric products; all displayed rational coefficients have denominators involving only \(2,3\), hence are units for \(p\ge7\). Apply \(1+6z\,d/dz\) at \(z=1/2\) to obtain
\[
\Psi\equiv S+p\alpha+p^2\beta_*+p^3\gamma\pmod{p^4}.
\]

Independently, for each \(k<p\) the exact factor extraction
\(a_k=p^{\nu_k}d_k\prod_{j,r\ne m_j}(1+p\,b_j/(r-m_j))\)
and Newton identities yield
\[
W_p\equiv S+p(A+B)+p^2(C+D+E)+p^3(T_0+T_1+T_2+T_3)\pmod{p^4}.
\]
Subtract the two identities. This proves the bridge.

## Exact finite certificates and base-p carry integrity

The companion standard Node.js BigInt program independently computes (i) \(W\) by its original hypergeometric recurrence, (ii) \(\Psi\) by the terminating \({}_2F_1\) recurrence, and (iii) all shadow, harmonic and four shell ports from p-factor extraction. It asserts all three exact identities modulo \(p^4\) for **all 35 primes \(7\le p\le373\), \(p\equiv1\bmod6\)**, and independently matches seven pinned witnesses.

| p | W mod p^4 | Psi mod p^4 | Q mod p^3 | F mod p^3 | H mod p^2 | I mod p | gamma mod p | (T0,T1,T2,T3) mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 13 | 19786 | 7761 | 925 | 860 | 96 | 6 | 10 | (12,9,3,5) |
| 19 | 82327 | 123158 | 4710 | 5337 | 195 | 7 | 5 | (14,10,3,4) |
| 373 | 11832087049 | 14593651483 | 44491459 | 14321354 | 54775 | 70 | 245 | (343,117,323,278) |

**Carry rule:** writing the canonical residues \(F=f_0+pf_1+p^2f_2\), \(H=h_0+ph_1\), \(I=i_0\), the actual Q third digit is
\[
q_2=(f_2+h_1+i_0+\lfloor(f_1+h_0)/p\rfloor)\bmod p.
\]
For \(p=13,19,373\), this gives respectively \(5,13,319\), exactly matching the prior independently obtained signed Q samples. In particular, \(I\bmod p\) alone is **not** the third Q digit; the carry is the explicit repair coordinate preserving the signed observer.

## Mother objective and next exact unit

The frozen mother objective remains \(\Delta_p-R_p=0\bmod p\) for primes \(p=13,19\bmod24\). A new explicitly separated third-order kernel exists, but its value does not imply the all-prime second-digit cancellation. Next, seek a closed-form local evaluation or telescope of the \(I\) / \(\gamma\) correction in the Hensel branch coordinates, separately preserving \(F,H\) carries, with counterexample/regression probes at 13,19,373. The original-class native p373 H0/B0, \([X]U\bmod139129\), Frobenius direction, \(\eta,\kappa\) and independent review retain their existing Source obligations.

Canonical Source checkpoint and contributors are unchanged. This file is an **author-side portable artifact**, not role-bound CLAIM/OPEN, native experiment or mathematical admission.
