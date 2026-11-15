# R749SQR — Simultaneous cyclotomic source phases and a minimal future-shift carrier

2026-11-16 (Asia/Shanghai). **AUTHOR_EXACT_NOT_REVIEWED**.

Scientific lineage: R749SQQ, draft PR #2519 at immutable commit \`3dfef5ca3ae9352e2cecafe3a36d735a89a07b92\`. Frozen Walsh auxiliary model pin: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. The following is an **independent positive labeled-source** counting model. It does not identify an original X6 spatial coordinate, a native three-dimensional slice, a signed amplitude or a native BRC port.

## Definitions and exact generating functions

For weights \(s_1,\ldots,s_d\in\mathbb Z_{>0}\) (equal weights retain distinct labels), mark a source \(j\) of weight \(h=s_j\) and put
\[
\Omega_r=\{k\in\mathbb Z_{\ge0}^d:\sum_i s_i k_i\le r-1\},\quad
C_r=|\Omega_r|,\quad T_{j,r}=h\sum_{\Omega_r}k_j,\quad
E_{j,r}=\frac{T_{j,r}}{rC_r}\quad (r\ge1).
\]
The correct *strict-prefix* generating functions, with \(C_0=T_{j,0}=0\), are
\[
F_s(z)=\frac{z}{1-z}\prod_{i=1}^d(1-z^{s_i})^{-1},
\qquad N_{j,s}(z)=F_s(z)\frac{hz^h}{1-z^h}.
\]
Let \(H_{j,q}(r)=\sum_{\ell=0}^q a_{j,\ell}r^{-\ell}\) denote the truncation of the **smooth \(z=1\) coefficient-ratio expansion** of \(E_{j,r}\).

## Theorem 1. A simultaneous order-2/order-3 correction

For \(s=(1,1,2,3,6)\), \(d=5\), mark one unit source (\(h=1\)). Uniformly along all integer residues as \(r\to\infty\),
\[
\boxed{
E_{1,r}=\frac16+\frac{1}{2r}-\frac{115}{36r^2}
+\frac{115}{6r^3}-\frac{16315}{108r^4}
+\frac{P_1(r)}{r^4}+O(r^{-5})
}
\]
with the exact, nonconstant period-six coefficient
\[
\boxed{
P_1(r)=\frac{15}{4}(-1)^r+\frac{40}{9}S_3(r),\qquad
S_3(r)=\begin{cases}2&3\mid r,\\-1&3\nmid r.\end{cases}
}
\]
In order \(r\bmod6=0,1,2,3,4,5\), the values are
\[
\boxed{P_1=(455,-295,-25,185,-25,-295)/36.}
\]

**Proof.** For a nontrivial root \(\zeta\), let \(I_\zeta=\{i:\zeta^{s_i}=1\}\), \(m_\zeta=|I_\zeta|\), \(W=\prod_i s_i\), and
\[
A_\zeta=\frac{\zeta}{(1-\zeta)\prod_{i\in I_\zeta}s_i
\prod_{i\notin I_\zeta}(1-\zeta^{s_i})}.
\]
In the local variable \(w=1-z/\zeta\), \(F_s(z)=A_\zeta w^{-m_\zeta}+O(w^{1-m_\zeta})\). The first contribution of this pole to the normalized mean is order \(r^{-(d-m_\zeta+1)}\). When \(\zeta^h\ne1\), its coefficient is
\[
-\frac{d!WA_\zeta\,\zeta^{-r}}{(d+1)(m_\zeta-1)!}.
\]
When \(\zeta^h=1\), the coefficient instead equals
\[
\frac{d!WA_\zeta(d+1-m_\zeta)\zeta^{-r}}{(d+1)m_\zeta!}.
\]
These follow by extracting \([z^r](1-z/\zeta)^{-p}\), using the leading \(C_r=r^d/(d!W)+O(r^{d-1})\) and \(E_{j,r}=1/(d+1)+O(r^{-1})\), and forming the first-order ratio correction. The leading marked multiplier has an extra pole if and only if \(\zeta^h=1\).

Here \(W=36\). The maximal nontrivial multiplicity is \(m=2\), attained at \(-1\) (weights 2 and 6) and at the two primitive cubic roots \(\omega,\omega^2\) (weights 3 and 6). Primitive sixth roots have \(m=1\) and enter only at order \(r^{-5}\). At \(-1\), \(A_{-1}=-1/192\); at each primitive cubic root,
\[
A_\omega=\frac{\omega}{18(1-\omega)^3(1-\omega^2)}=-\frac1{162},
\quad A_{\omega^2}=-\frac1{162},
\]
using \((1-\omega)(1-\omega^2)=3\) and \((1-\omega)^2=-3\omega\). Since the mark has \(h=1\), the coefficient factor is \(-5!\,36/(6\cdot 1!)=-720\). Thus the parity contribution is \((15/4)(-1)^r\), while the cubic contribution is \((40/9)(\omega^{-r}+\omega^{-2r})=(40/9)S_3(r)\). Exact Taylor/Laurent extraction at \(z=1\) gives smooth coefficients
\[
(a_{1,0},\ldots,a_{1,4})=(1/6,1/2,-115/36,115/6,-16315/108).
\]
Rational generating functions have finitely many root-of-unity poles. Their exact quasipolynomial coefficients and subsequent rational division give a uniform \(O(r^{-5})\) remainder. QED.

For any one of the marks \(h\in\{1,2,3,6\}\) the first periodic coefficient is
\[
P_h(r)=a_2(h)(-1)^r+a_3(h)S_3(r),\quad
a_2(h)=\begin{cases}15/4&2\nmid h,\\-15/2&2\mid h,\end{cases}\quad
a_3(h)=\begin{cases}40/9&3\nmid h,\\-80/9&3\mid h.\end{cases}
\]
In particular,
\[
\boxed{P_1-P_2=(45/4)(-1)^r,\qquad P_1-P_3=(40/3)S_3(r).}
\]
The nonzero primitive order-two and order-three Fourier coefficients imply that the **least period of each \(P_h\) is six**. The differences isolate two frequency channels.

## Theorem 2. Minimal carrier for future boundary shifts

**Finite-cyclic observability lemma.** Let \(f:\mathbb Z/L\mathbb Z\to V\) be any function and allow future operations \(r\mapsto r+t\) for \(t\ge0\). Declare \(u\sim v\) iff \(f(u+t)=f(v+t)\) for every \(t\ge0\). If \(p\) is the least positive period of \(f\), then
\[
\boxed{u\sim v\iff u\equiv v\pmod p.}
\]
Hence \(\mathbb Z/p\mathbb Z\) is the smallest exact deterministic future-sufficient phase state (by number of states) for this observation/operation family.

**Proof.** A difference divisible by \(p\) preserves every shift. Conversely the future equality covers all arguments of the cyclic domain because the set of nonnegative shifts traverses it; therefore translation by \(v-u\) preserves \(f\) everywhere. Translation symmetries form a subgroup generated by the least positive period \(p\). Distinct cosets must remain distinct in any sufficient deterministic quotient, and the quotient modulo \(p\) suffices. QED.

For the displayed \(P_1\), **one instantaneous value takes only four distinct values**, merging residues \((1,5)\) and \((2,4)\). Nevertheless
\[
\boxed{\big(P_1(r),P_1(r+1)\big)}
\]
has the following six **distinct ordered pairs**:

| \(r\bmod6\) | \(36P_1(r)\) | \(36P_1(r+1)\) |
|---:|---:|---:|
|0|455|-295|
|1|-295|-25|
|2|-25|185|
|3|185|-25|
|4|-25|-295|
|5|-295|455|

Their minimum pairwise \(L_\infty\) distance in unscaled values is \(35/6\). One future increment is enough to recover all six phase classes; no smaller shift-invariant state quotient preserves this observation family.

At finite precision define \(R(r)=r^4(E_{1,r}-H_{1,4}(r))\). Theorem 1 implies \(R(r)=P_1(r)+O(1/r)\), also at \(r+1\). Therefore some finite \(r_0\) exists such that the nearest one of the six signatures to \((R(r),R(r+1))\) identifies \(r\bmod6\) for all integers \(r\ge r_0\); an error strictly below \(35/12\) in pair \(L_\infty\) norm suffices. The explicit uniform bound \(r\ge512\) is established in Theorem 3 below. This future increment is an auxiliary change of boundary parameter, not an asserted physical heartbeat/time update.

## Exact checks, status, and next research

The companion dependency-free Python \`R749SQR_SIMULTANEOUS_CYCLOTOMIC_CERT.py\` calculates strict-prefix counts by weighted dynamic programming and independently enumerates \(r=1,\dots,32\) by recursion, with exact integer/Fraction arithmetic. It checks 4,000 marked-source deletion identities at \(r\le1000\), four marked-observer phase tables, both channel-isolating differences, the six ordered future signatures, smooth coefficients and exact finite means at \(r=120\ldots125,\ 600\ldots605,\ 6000\ldots6005\). Stored JSON results: \`PASS\`. The universal theorem depends on the rational-pole proof above, not finite extrapolation. Independent review, formalization and native BRC typed-port correspondence remain open.

**Next:** obtain an explicit finite decoding threshold or exact finite error bound; classify minimal phase quotients for a restricted semigroup of future source operations; construct and test an actual BRC provenance-port/observer map with retained labels, branch information and signed/amplitude typing before claiming native transport. P000/worldview and the immutable scientific pin remain unchanged.

Provenance: R749SQQ@3dfef5ca3ae9352e2cecafe3a36d735a89a07b92; frozen science@a72226e2430ffa4786321ac86e7f0c599d5f0389. This research note is not a shared Task CLAIM or a formal Result/Review.

## Theorem 3 — an explicit exact finite phase-decoding threshold

The asymptotic existence statement above can be strengthened to the following **all-integer bound** for the same alphabet, marked unit source, smooth fourth-order truncation and \(P_1\):
\[
\boxed{\text{For every integer }r\ge512,\qquad
0<R(r)-P_1(r)<\frac{35}{12}.}
\]
Consequently the exact six-state nearest-pair decoder, based on \((R(r),R(r+1))\) and the displayed signatures, correctly recovers \(r\bmod6\) **for every integer \(r\ge512\)**. The bound \(512\) is the smallest threshold for this particular uniform scalar error inequality: \(r=511\) fails its upper inequality. This does not claim optimality of \(512\) among all possible decoders.

**Exact proof certificate.** Since the weights \(1,1,2,3,6\) divide six, the generating functions have only sixth roots of unity as poles. Their pole orders show that, on each residue class modulo six, \(C_r\) is exactly a polynomial of degree at most five and the marked \(T_{1,r}\) is exactly a polynomial of degree at most six. Six and seven exact equally spaced values therefore determine these respective polynomials by the Newton forward-difference formula; the degree bounds make this valid at *all* subsequent points, not merely the interpolation samples.

For each residue \(a=0,\ldots,5\), set
\[
 r_a=(516,517,512,513,514,515)_a,\quad r=r_a+6n,\quad n\in\mathbb Z_{\ge0}.
\]
Define the exact polynomial numerator
\[
N_a(n)=r^3T_{1,r}-C_r\big(r^4 H_{1,4}(r)+P_1(a)\big).
\]
Then \(R(r)-P_1(r)=N_a(n)/C_r\). Exact interpolation and cancellation give \(\deg N_a=4\). The companion dependency-free certificate computes the coefficients in powers of \(n\) and shows that every coefficient of all three polynomials
\[
 C_{r_a+6n},\quad N_a(n),\quad U_a(n)=\frac{35}{12}C_{r_a+6n}-N_a(n)
\]
is **strictly positive**. The full rational coefficient arrays for all six residue classes are recorded in \`R749SQR_FINITE_DECODER_BOUND_RESULTS.json\`. Hence \(0<N_a(n)<(35/12)C_r\) for all nonnegative integer \(n\), proving the universal displayed bound. Independently computed exact finite prefixes for \(1\le r<512\) identify \(r=511\) as the last failure of this scalar sufficient bound. QED.

The extra certificate \`R749SQR_FINITE_DECODER_BOUND_CERT.py\` imports the first R749SQR certificate, performs all polynomial operations with \`Fraction\` using no third-party libraries, checks additional sample values beyond the interpolation degree, and returns \`PASS\`. The paper's main theorem still has scientific status **AUTHOR_EXACT_NOT_REVIEWED**; no formal reviewer is claimed.

The finite error theorem completes the previously posed question of an explicit sufficient decoding threshold. The next question is whether a smaller threshold is attainable for the actual joint pair classifier (which is less restrictive than the scalar \(35/12\) bound), and the minimal carrier for other allowed future source-operation semigroups.
