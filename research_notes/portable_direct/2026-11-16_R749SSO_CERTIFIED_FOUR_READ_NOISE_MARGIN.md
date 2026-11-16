# R749SSO — Certified positive four-read noise margin for cutoffs 7 and 8

**Date:** 2026-11-16. **Status:** AUTHOR_EXACT_NOT_REVIEWED.  
**Independent portable research; scientific pin:** \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`.  
**Predecessor:** R749SSM, [PR #2572](https://github.com/awdawmip/enterprise-math/pull/2572), immutable commit \`7ea79c50d4f448c515719b1f883b5fb68fe4d69a\`. The earlier result proved exact four-read separation but did not give an explicit numerical gap. Concurrent R749SSN [PR #2573](https://github.com/awdawmip/enterprise-math/pull/2573) treats a distinct adjacent-cutoff, one-read tail theorem.

## Model and new theorem

Retain five distinct labeled sources of weights \(w=(1,1,2,3,6)\) and
\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]
With \(S(q)=18q^4+54q^3-345q^2+2070q-16315\), define
\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},\quad
F_q(e,d)=(Y_{q+6j}(e,d))_{j=0}^3.
\]
Within each four-read state, the same real error pair is reused. The two cutoff states have *independent* \((e,d),(E,D)\in[-2,2]^2\).

**Theorem (uniform explicit separation).** For every such pair,
\[
\boxed{\|F_7(e,d)-F_8(E,D)\|_\infty\ \ge\
\frac{40028915051766416168336192988259455494375902399536945123683205120}
{2385528822152469524812195767070353196847512054610269204964931381755904}
=\frac{6362424699746198045148244379084818441768630727058560867895}
{379169594788943850964259428512311489875715900200250817134369434}
> \frac1{100000}.}
\]
Numerically the *certified* lower bound is \(\approx 1.6779891603\cdot10^{-5}\), not a claim of optimal separation.

Consequently, for additive measurement error bounded independently in every coordinate by
\[
\boxed{\eta < \frac{6362424699746198045148244379084818441768630727058560867895}
{758339189577887701928518857024622979751431800400501634268738868}}
\]
(approximately \(8.3899458\cdot10^{-6}\)), the two four-read cutoff classes can be distinguished by minimum sup-norm distance. Each candidate family is compact, and measurement balls of this strict radius do not intersect.

## Proof: residual determinants directly control observed distance

For \(j=0,1,2,3\), set \(q_j=7+6j\), \(p_j=8+6j\) and
\[
V_j=p_j^3(C_{q_j}+d),\quad
U_j=q_j^3(T_{q_j}+e)+\frac{S(p_j)-S(q_j)}{108}(C_{q_j}+d),
\]
\[
L_j=(V_j,-U_j,C_{p_j}U_j-T_{p_j}V_j).
\]
As in R749SSM, define two polynomial determinants
\[
f(e,d)=H_2=\det(L_0,L_1,L_2),\quad
g(e,d)=H_3=6\det(L_0,L_1,L_3).
\]
Let \(\Delta_j=Y_{q_j}(e,d)-Y_{p_j}(E,D)\) and \(\delta=\max_{0\le j\le3}|\Delta_j|\). A direct algebraic identity gives
\[
L_j\cdot(E,D,1)=(C_{q_j}+d)(C_{p_j}+D)\Delta_j.
\]
Replacing a determinant's last column by that column plus \(E\) times the first plus \(D\) times the second preserves its determinant. For all \(j\), write
\[
v_j=p_j^3(C_{q_j}+2),\quad
u_j=q_j^3(T_{q_j}+2)+
\Big\lceil \frac{|S(p_j)-S(q_j)|(C_{q_j}+2)}{108}\Big\rceil,\quad
k_j=(C_{q_j}+2)(C_{p_j}+2).
\]
The exact anchors, reconstructed from the weights rather than postulated, yield

| \(j\) | \(v_j\) | \(u_j\) | \(k_j\) |
|---:|---:|---:|---:|
| 0 | 34304 | 54562 | 6700 |
| 1 | 1393952 | 3714061 | 337312 |
| 2 | 16864000 | 62500309 | 5434424 |
| 3 | 111308808 | 526629079 | 47136519 |

For an ordered triple \(J=(j,k,\ell)\), write
\[
B_J=\sum_{s\in J}k_s(v_tu_u+u_tv_u)
\quad\text{where }\{t,u\}=J\setminus\{s\}.
\]
The determinant expansion yields, *with no sign or floating-point assumptions*,
\[
|f|\le D_2\delta,\quad |g|\le D_3\delta,\qquad
D_2=B_{(0,1,2)}=\boxed{3142649593132974464},
\]
\[
D_3=6B_{(0,1,3)}=\boxed{152526800932915943616}.
\]

## Proof: resultant and explicit residual-to-distance bound

Use the exact coefficient polynomials of R749SSM:
\(f=a(d)e^2+b(d)e+c(d)\), \(g=A(d)e^2+B(d)e+C(d)\), reconstructed and checked in the companion certificate. Let
\[
P=a\,g-A\,f,\quad Q=b\,g-B\,f,\quad J=aB-Ab.
\]
The quadratic resultant identity is
\[
R(d)=\operatorname{Res}_e(f,g)=P^2-2eJP-JQ.
\]
This is a **polynomial identity at every \((e,d)\)**, even when the observation vectors differ. From the full coefficient lists and \(|d|\le2\), the certificate computes these integer upper bounds:
\[
a_* =30340270353216,\quad A_* =2599609466397312,
\]
\[
b_*=33336615367594160,\quad B_*=2778763591581391760,
\]
\[
J_*=a_*B_*+A_*b_*=170970619503496799045436202798080.
\]
Further put \(f_*=4a_*+2b_*+c_*\), \(g_*=4A_*+2B_*+C_*\), where \(c_*,C_*\) are the coefficient absolute-sum bounds for the constant-in-\(e\) polynomials. Define
\[
P_*=a_*g_*+A_*f_*,\quad
P_\delta=a_*D_3+A_*D_2,\quad
Q_\delta=b_*D_3+B_*D_2.
\]
Thus \(|P|\le P_*\), \(|P|\le P_\delta\delta\), \(|Q|\le Q_\delta\delta\), and \(|J|\le J_*\). Because \(|e|\le2\),
\[
|R(d)|\le \underbrace{[(P_*+4J_*)P_\delta+J_*Q_\delta]}_{K}\delta,
\]
where the exact, fully reconstructed integer is
\[
K=\boxed{2385528822152469524812195767070353196847512054610269204964931381755904}.
\]

R749SSM supplies an exact factored resultant
\[
R(d)=-67436544(d+65)(d+506)(234443938d+1569882365)\mathcal Q(d),
\]
and its coefficient triangle bound \(\mathcal Q(d)\ge16979397777109496872916184850765128499562660\) for all \(|d|\le2\). Therefore
\[
|R(d)|\ge 67436544\cdot63\cdot504\cdot1100994489\cdot
16979397777109496872916184850765128499562660
=40028915051766416168336192988259455494375902399536945123683205120.
\]
Combining this with \(|R(d)|\le K\delta\) proves the theorem. The companion certificate *independently reconstructs* the source anchors, bivariate determinant coefficients, quadratic resultant factorization, interval bounds and \(K\) using exact rational and integer arithmetic. Its actual local execution returned \`PASS\`.

## Observer and BRC relevance; open questions

This provides an **explicit quantitative observer-fiber separation** for the pair \((q,p)=(7,8)\). In the typed BRC language, keep the cutoff label, five-source provenance, common-within-state error relation, four-read order and sup-norm observation distance as separate coordinates. The positive margin is robust to measurement perturbations at the declared horizon; no native X6 time dynamics or BRC Port identification is inferred.

The result is conditional only on the precisely specified scalar source model and rational observer, not on a global injectivity assumption. The guaranteed margin is conservative. Next, optimize the bound (e.g. certified interval branch-and-bound on the two error squares), classify other cutoff pairs, and determine whether a finite observation horizon separates every pair across the whole infinite cutoff domain. Preserve frozen science; do not confuse bounded-pair stability with a global theorem.

**Verification:** Standard-library Python 3 exact arithmetic, no numerical solver. Run \`python3 R749SSO_EXPLICIT_FOUR_READ_NOISE_CERT.py\` in the material directory; it writes \`R749SSO_FOUR_READ_EXPLICIT_GAP_RESULTS.json\` and asserts exact identities. Reviewer status: AUTHOR_EXACT_NOT_REVIEWED. GitHub PR is durable independent portable research; formal shared CLAIM/Result/Review require separate native authorization.
