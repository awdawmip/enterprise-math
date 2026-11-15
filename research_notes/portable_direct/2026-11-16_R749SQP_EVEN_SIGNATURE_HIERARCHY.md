# R749SQP — Even-power source signatures and a sixth-order Walsh provenance witness

Date: 2026-11-16 (Asia/Shanghai). **Status: AUTHOR_EXACT_NOT_REVIEWED.** Independent auxiliary positive labeled-source multiset model, not native X6 or a shared Task CLAIM. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor: R749SQO, Draft PR #2513, head 776f6edee135015d80c42338b3c72bbb0083d2eb. Predecessor paper and code were actually read through GitHub PR file patches; direct immutable-ref file reads returned 404. This work preserves scientific provenance without reinterpreting shared owner state.

## Definitions and exact source observer

Let \(s=(s_1,\ldots,s_d)\) be a labeled list of positive integers with a marked index \(j\), of weight \(h=s_j\). For \(r\ge1\), uniformly sample the finite **labeled multiplicity** set

\[
\Omega_r(s)=\{k\in\mathbb Z_{\ge0}^d:\sum_i s_i k_i\le r-1\},
\qquad X_r(s)=\frac{h k_j}{r}.
\]

Equal weight values at distinct labels remain different coordinates. Let \(S_q(s)=\sum_i s_i^q\), \(m_\zeta(s)=\#\{i:\zeta^{s_i}=1\}\) for any nontrivial root of unity \(\zeta\), and let \(B_{2m}\) be the Bernoulli numbers (\(B_2=1/6,\ B_4=-1/30,\ B_6=1/42\)). The falling factorial is \((d)_k=d(d-1)\cdots(d-k+1)\).

## Theorem 1 — all-order even-signature hierarchy

Fix \(m\ge1\) and \(d\ge2m\). Let \(s,t\) each have \(d\) labeled positive integer weights and marked coordinate weights both equal to \(h\). Assume

1. \(S_1(s)=S_1(t)\);
2. \(S_{2q}(s)=S_{2q}(t)\) for \(1\le q<m\);
3. \(m_\zeta(s),m_\zeta(t)\le d-2m\) for all nontrivial roots of unity \(\zeta\).

Then uniformly over **all positive integer precision levels** as \(r\to\infty\),

\[
\boxed{\mathbb E_s X_r-\mathbb E_t X_r=
-\frac{B_{2m}(d)_{2m-1}}{(d+1)(2m)!}
\frac{S_{2m}(s)-S_{2m}(t)}{r^{2m}}
+O_{s,t}(r^{-2m-1}).}
\]

Thus, in the smooth \(z=1\) component, genuinely new power-sum information first enters at **even** inverse-resolution orders; intervening odd-order coefficients are determined by already present even-power sums together with \(d,S_1,h\). Cyclotomic pole multiplicities control when this is also an assertion about the *complete* source mean rather than only its smooth component.

### Proof

Let \(C_r(s)=|\Omega_r(s)|\). Its exact rational generating function is

\[
F_s(z)=\sum_{r\ge0} C_r(s) z^r
=\frac1{1-z}\prod_{i=1}^{d}\frac1{1-z^{s_i}}.
\]

The marked source count moment has generating function \(F_s(z) z^h/(1-z^h)\), so

\[
\mathbb E_s X_r=
\frac h r\frac{[z^r]\big(F_s(z)z^h/(1-z^h)\big)}
{[z^r]F_s(z)}.
\]

Near \(z=1\), use the analytic local parameter \(u=-\log z\). The identity

\[
\frac1{1-e^{-a u}}
=\frac{e^{a u/2}}{a u}\frac{a u/2}{\sinh(a u/2)}
\]

yields, with \(W_s=\prod_i s_i\),

\[
F_s(e^{-u})
=\frac{e^{(1+S_1(s))u/2}}{W_s u^{d+1}}
\exp\left[-\sum_{q\ge1}
\frac{B_{2q}}{2q(2q)!}\big(1+S_{2q}(s)\big)u^{2q}\right].
\]

The marked multiplier is

\[
\frac{h e^{-h u}}{1-e^{-h u}}
=\frac1u e^{-h u/2}
\exp\left[-\sum_{q\ge1}
\frac{B_{2q}h^{2q}}{2q(2q)!}u^{2q}\right].
\]

Under the hypotheses, after factoring out the common pole and each harmless \(W_s^{-1}\), both alphabets have identical local terms through \(u^{2m-1}\), with first logarithmic difference

\[
\delta c\,u^{2m},\qquad
\delta c=-\frac{B_{2m}}{2m(2m)!}\big(S_{2m}(s)-S_{2m}(t)\big).
\]

Since \(u=(1-z)+O((1-z)^2)\), the first difference in the normalized Laurent expansions is also \(\delta c(1-z)^{2m}\). A pole of order \(d+1\) gives a principal coefficient asymptotic to \(r^d/d!\). Consequently the normalized denominator-count coefficient changes by \((d)_{2m}\delta c\,r^{-2m}\). The marked numerator has pole order \(d+2\); after division by \(r\), its normalized coefficient changes by \((d)_{2m-1}\delta c\,r^{-2m}\). The common leading mean is \(1/(d+1)\). Dividing these two series gives

\[
\left[(d)_{2m-1}-\frac{(d)_{2m}}{d+1}\right]\delta c
=\frac{2m}{d+1}(d)_{2m-1}\delta c,
\]

precisely the stated coefficient. Lower smooth terms coincide; the displayed exponential has no new odd power sum.

For any \(\zeta\ne1\), \(F_s\) has a pole of order \(m_\zeta(s)\); marking can add at most one to the pole order. Root-of-unity coefficient extraction therefore contributes at most \(O(r^{m_\zeta-1})\) to the counted denominator or to the marked numerator *after division by \(r\)*. Relative to the leading order \(r^d\), this is \(O(r^{-(d-m_\zeta+1)})\). The uniform hypothesis \(m_\zeta\le d-2m\) makes every such contribution \(O(r^{-2m-1})\). The rational generating functions have finitely many poles, giving a uniform remainder on all residue classes. QED.

## Theorem 2 — explicit sixth-order separation with seven source labels

Mark the first unit source in each of the alphabets

\[
A=(1,1,1,2,7,11,15),\qquad
B=(1,1,1,3,5,13,14).
\]

They have common \(d=7,h=1,S_1=38,S_2=402,S_4=67686\) but

\[
S_6(A)-S_6(B)=907200.
\]

The four nonunit weights in **each** alphabet are pairwise coprime, so all nontrivial root-of-unity pole orders satisfy \(m_\zeta\le1=d-6\). With \(m=3\), the theorem gives

\[
\boxed{\lim_{r\to\infty}r^6
\big(\mathbb E_A X_r-\mathbb E_B X_r\big)=-9450.}
\]

Independent exact formal Laurent expansion determines the six common coefficients (orders 0 through 5) as

| Order | Both alphabets |
|---:|---:|
| 0 | \(1/8\) |
| 1 | \(29/16\) |
| 2 | \(-2765/96\) |
| 3 | \(102305/192\) |
| 4 | \(-5066369/384\) |
| 5 | \(282255869/768\) |

The sixth coefficients are \(-50406501643/4608\) for \(A\) and \(-50362956043/4608\) for \(B\), whose difference is \(-9450\). Finite scaled differences may oscillate around the limit due to terms of order \(r^{-7}\) and below.

## Reproducibility and evidence scope

The companion dependency-free Python certificate computes the complete smooth expansion through order 6 with exact fractions, enumerates both alphabets by integer dynamic programming through \(r=12000\), checks **24,000** exact marked-deletion identities, and independently checks **64** small-bound recursively enumerated source totals/moments. All checks returned **PASS** locally. Eight scaled samples are also saved as exact rational fractions in the results JSON. Reproduction:

    python3 R749SQP_EVEN_MOMENT_SIGNATURE_CERT.py > R749SQP_EVEN_MOMENT_SIGNATURE_RESULTS.json

The universal assertion follows from the rational pole proof above, rather than extrapolation from the finite program. This is an independent positive labeled-source/multiplicity observer result; no unproved map to the full Heartbeat-X6 state, signed Walsh amplitude collapse or global observer-safe quotient is invoked. No source activity association, independent review, mathematical admission or formal Task/CLAIM authorization is claimed by this note.

**Next discriminating question:** classify first periodic interruptions of the even-power hierarchy at orders 5 and 6 when cyclotomic pole multiplicity exceeds the theorem's threshold; then determine minimal *observer- and operation-scoped* periodic data needed alongside even-power signatures.
