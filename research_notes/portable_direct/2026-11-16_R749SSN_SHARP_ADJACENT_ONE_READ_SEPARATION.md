# R749SSN — Sharp uniform one-read separation of adjacent unknown cutoffs

**Date:** 2026-11-16. **Status:** AUTHOR_EXACT_NOT_REVIEWED (exact author proof and independently executable symbolic certificate; pending independent review).

**Frozen scientific source:** \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`; five labeled weights \((1,1,2,3,6)\), carried forward from R749SSM [PR #2572](https://github.com/awdawmip/enterprise-math/pull/2572), scientific commit \`7ea79c50d4f448c515719b1f883b5fb68fe4d69a\`. Behavioral rules were read separately from this scientific pin.

## Exact model

Let \(\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\}\),
\(C_q=|\Omega_q|\), and \(T_q=\sum_{k\in\Omega_q} k_1\).
For \(q\ge6\), set

\[
 S(q)=18q^4+54q^3-345q^2+2070q-16315,\quad
 Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},
 \qquad(e,d)\in[-2,2]^2.
\]

Each candidate cutoff carries its own fixed pair of **real** count-calibration errors. The observation is a single exact scalar \(Y_q\); the observer is told that the unknown cutoff is either \(q\) or \(q+1\), not which one.

## Sharp theorem

Write \(\mathcal I_q=Y_q([-2,2]^2)\subset\mathbb R\) and \(\operatorname{dist}(A,B)=\inf_{a\in A,b\in B}|a-b|\). Then

\[
\boxed{\mathcal I_q\cap\mathcal I_{q+1}=\varnothing
\quad\text{for every integer }q\ge501.}
\]

Furthermore the **exact sharp uniform separation margin** is

\[
\boxed{\min_{q\ge501}\operatorname{dist}(\mathcal I_q,\mathcal I_{q+1})
 = g = \frac{1423720838927976185}{53569280690597608884}>0,}
\]

and it is attained at \(q=506\), between the upper endpoint of \(\mathcal I_{506}\) and the lower endpoint of \(\mathcal I_{507}\).
The threshold 501 is optimal: \(\mathcal I_{500}\cap\mathcal I_{501}\ne\varnothing\).

For nearest-image classification between the *two adjacent candidates* \(\{q,q+1\}\), a single observation with absolute additive measurement error \(<g/2\) is always classified correctly. The **uniform radius** \(g/2=1423720838927976185/107138561381195217768\) is optimal by the midpoint ambiguity at \((506,507)\).

## Interval reduction

For \(q\ge6\), \(C_q>2\) and \(T_q>2\). Since \(Y_q\) increases strictly with \(e\) and decreases strictly with \(d\), continuity on the square gives

\[
\mathcal I_q=[L_q,U_q],\quad
L_q=\frac{q^3(T_q-2)}{C_q+2}-\frac{S(q)}{108},
\quad U_q=\frac{q^3(T_q+2)}{C_q-2}-\frac{S(q)}{108}.
\]

The high-cutoff orientation by \(r=q\bmod6\) is: \(q\) is higher for \(r\in\{0,3,4\}\); \(q+1\) is higher for \(r\in\{1,2,5\}\).
Define the oriented interval gap \(G_r(n)\) as \(L_q-U_{q+1}\) in the first case and \(L_{q+1}-U_q\) in the second, where \(q=6n+r\).

## Infinite integer-tail proof by rational quasi-polynomials

The labeled generating functions for \(C_q\) and \(T_q\) are

\[
 \sum_{q\ge0}C_q z^q
 =\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\qquad
 \sum_{q\ge0}T_q z^q
 =\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

The coefficients of these generating functions are quasi-polynomials of period 6 and residue-wise degrees at most 5 and 6, respectively. Thus \(C_{6n+r}=c_r(n)\) and \(T_{6n+r}=t_r(n)\) for integer \(n\ge1\), where each \(c_r\) is fixed by six consecutive exact source counts and each \(t_r\) by seven. The companion certificate constructs their coefficients by rational interpolation and verifies additional independent source positions.

Put \(p=q+1\), \(c=C_q\), \(t=T_q\), \(c'=C_p\), \(t'=T_p\), all regarded as the above polynomial functions of \(n\). For the high-\(q\) case,

\[
 A=(c+2)(c'-2),\quad
 P=108q^3(t-2)(c'-2)-108p^3(t'+2)(c+2)
 -(S(q)-S(p))(c+2)(c'-2).
\]

For the high-\(q+1\) case,

\[
 A=(c-2)(c'+2),\quad
 P=108p^3(t'-2)(c-2)-108q^3(t+2)(c'+2)
 -(S(p)-S(q))(c-2)(c'+2).
\]

Then \(G_r(n)=P_r(n)/(108A_r(n))\) and \(A_r(n)>0\). The coefficient certificate proves the exact polynomial identity

\[
 P_r(t+84)-108gA_r(t+84)
 =\sum_{j=0}^{10} a_{r,j}t^j\qquad(t\ge0),
\]

with the following **complete signs**, in *ascending* coefficient order \(j=0,\ldots,10\):

| residue \(r\) | signs of \(a_{r,0},\ldots,a_{r,10}\) |
|---:|:---|
| 0 | \`+++++++++++\` |
| 1 | \`+++++++++++\` |
| 2 | \`0++++++++++\` |
| 3 | \`+++++++++++\` |
| 4 | \`+++++++++++\` |
| 5 | \`+++++++++++\` |

The program uses only exact integers/rationals in the proof assertions; it reconstructs all 66 coefficients, checks their signs, the degree-10 identities and multiple original source-count instances. Consequently \(G_r(n)\ge g\) for all \(n\ge84\), i.e. all \(q\ge504\). Equality occurs only for \(r=2,n=84\), namely \(q=506\). Direct exact rational evaluation gives \(G_r(n)>g\) at \(q=501,502,503\). This proves the uniform minimum over all integers \(q\ge501\).

(The generating functions above use indexing \(\sum_{q\ge0}C_q z^q\), \(C_0=0\); the shifted powers of \(z\) account for \(\le q-1\).)

## Exact boundary collision: cutoff 500 versus 501

At \(q=500\), the lower endpoint of \(\mathcal I_{501}\) is below the upper endpoint of \(\mathcal I_{500}\):

\[
 L_{501}-U_{500}=
-\frac{718752908383402165}{17856626610048875568}<0.
\]

An explicit interior-error collision is obtained at

\[
 y_*=\frac{518977395929101571945}{107139759660293253408}
\]

with

\[
 Y_{500}\left(\frac{88846406643319567}{116298494160000000},-2\right)
 =y_*=
 Y_{501}\left(-\frac{439730328340660223}{579241618362031194},2\right).
\]

Both numerator-error values are strictly between \(-2\) and \(2\); both denominator errors belong to the permitted closed interval. Hence no tail threshold \(\le500\) can work for every adjacent pair.

## Boundary, reproducibility, and next questions

The theorem is a *binary adjacent-cutoff* observer result under a single frozen smooth ratio and bounded **real common-in-time calibration errors**. It does not classify arbitrary nonadjacent cutoffs. It uses precise rational source counts, not a native signed-X6 Cell/Link/Port evolution or a new BRC physics law. The labels, count moments, error pairing and observer map are explicitly retained, so future typed embedding has a clear invariant to preserve.

Reproduce with \`python R749SSN_ADJACENT_SINGLE_READ_CERT.py\` (SymPy required); compare the printed JSON to \`R749SSN_ADJACENT_SINGLE_READ_RESULTS.json\`. All positivity assertions are exact, without numerical root isolation. Author proof is pending independent review.

**Next scientific questions:** classify nonadjacent phases and cutoffs in the exact scalar image model; derive a multicutoff minimum-error decision rule; test whether two or more scheduled observations preserve unknown-cutoff distinction with a smaller tail threshold, retaining common calibration across reads; develop a typed joint-source BRC carrier preserving all future-observer fibers.