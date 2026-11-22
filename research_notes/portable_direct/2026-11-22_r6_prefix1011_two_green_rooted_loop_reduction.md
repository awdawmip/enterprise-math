# PREFIX-1011 — Two-Green-series exact reduction for signed X6 BRC rooted Link loops

**Date:** 2026-11-22 (+08)  
**Status:** AUTHOR_ALGEBRAIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED  
**Scientific pin:** \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\` (P000 V5).  
**Predecessor:** [PREFIX-1010](https://github.com/awdawmip/enterprise-math/blob/551b1ef560fd239a8d30536da8ea6c11abe9d0d6/research_notes/portable_direct/2026-11-22_r6_prefix1010_rooted_loop_rank_two_green.md).  
**Transport provenance:** Independent portable research artifact, with no new formal CLAIM/PROGRESS/Result/Review.

## Exact model and observer

Use the frozen six-axis native X6 Cell torsor, a chart-relative anchor Cell 0, twelve named signed directions \(\pm e_1,\dots,\pm e_6\), starting incoming-neighbour port \(h=-e_1\), and the Stage46 *candidate* signed BRC transition multiplier \(w(h,d)=1-6\mathbf1_{h=d}\), with new incoming port \(-d\). Both directed crossings of \(\{0,e_1\}\) are deleted without renormalization.

Let \(L_k\) denote the sum of **signed integer weights** of all named \(2k\)-step paths returning to Cell 0, summed over their final incoming ports; let \(\mathcal L(z)=\sum_{k\ge0}L_k z^{2k}\). This observer is not a squared probability or physical-time clock.

Define the native-axis Laurent element
\[
S(X)=\sum_{i=1}^6(X_i+X_i^{-1}),\quad
D(X,z)=1-zS(X)+36z^2,
\]
and formal Green coefficients
\[
G_j(z)=[X_1^jX_2^0\cdots X_6^0]D(X,z)^{-1},\qquad j=0,1,2.
\]
All operations take place in \(\mathbb Q[[z]]\), with the original integer BRC operator determining this exact final observer.

## Theorem 1011.1 — two-series sufficiency

Put \(F=G_0,\ J=G_2\) and
\[
\begin{aligned}
U&=(1+36z^2)F-1,\\
R&=\tfrac12[1+(1-36z^2)F],\\
P_+&=1+(1-6z)\bigl(zF+U/12\bigr),\\
P_-&=1-(1+6z)\bigl(zF-U/12\bigr).
\end{aligned}
\]
Then \(P_\pm(0)=1\), and the **full-length** rooted Link-avoiding BRC signed-loop series has the exact representation
\[
\boxed{\displaystyle
\mathcal L(z)=
\frac{R\,\bigl[1-6z^2(F-J)\bigr]}{P_+P_-}.}\tag{1011.1}
\]
Thus the previously used three Green sequences \(G_0,G_1,G_2\) can be reduced to **two independently supplied scalar series \(G_0,G_2\)** for this fixed observer. No algebraic minimality or future port-resolved equivalence is asserted.

### Proof

The identity \(D(X,z)D(X,z)^{-1}=1\), after extracting the coefficient of the chosen Cell \(X^0\), gives
\[
(1+36z^2)G_0-z\sum_{d\in\{\pm e_1,\ldots,\pm e_6\}}
[X^{-d}]D^{-1}=1.
\]
The signed-axis symmetry makes all twelve neighbour coefficients equal \(G_1\). Hence the exact **origin recurrence**
\[
\boxed{(1+36z^2)G_0-12zG_1=1.}\tag{1011.2}
\]
This identity is coefficientwise in the original Laurent ring; it uses no limiting arguments or numerical approximation.

Recall the all-grade rank-two forbidden-Link resolvent derived in PREFIX-1010, specifically its formula (1010.1). Direct multiplication of its \(2\times2\) feedback numerator and denominator, followed by cancellation of the shared formal units, yields
\[
\boxed{\mathcal L(z)=
\frac{(G_0-6zG_1)[1-6z^2(G_0-G_2)]}
{\bigl[1+(z-6z^2)(G_0+G_1)\bigr]
 \bigl[1-(z+6z^2)(G_0-G_1)\bigr]}.}\tag{1011.3}
\]
This is a rational identity in the three *formal indeterminates* \(G_0,G_1,G_2\); it can also be checked by expanding (1010.1) with its displayed \(a,b,A,B,c,d,p,q,\Delta\).

By (1011.2), \(12zG_1=U\) and
\[
G_0-6zG_1
=G_0-U/2
=\tfrac12[1+(1-36z^2)F]=R.
\]
Also, \(z(G_0+G_1)=zF+U/12\) and \(z(G_0-G_1)=zF-U/12\). Substituting these into (1011.3) gives (1011.1), proving the theorem for every \(k\ge0\). The apparent divisions by 2 and 12 are harmless exact rational coefficients. \(\square\)

## Exact reproducibility and extended coefficients

The attached Python checker constructs \(G_0,G_1,G_2\) from signed-axis word counts by exact factorial combinatorics, computes both (1011.1) and the independent earlier rank-two expression (1010.1) through \(z^{64}\), and compares their integer coefficients for **all \(k=0,\ldots,32\)**. It checks (1011.2) coefficientwise; checks against all 21 already saved PREFIX-1010 values \(k\le20\); and separately executes the *named* twelve-direction BRC Cell-and-port integer transition with both Link directions blocked for \(k=0,\ldots,8\). All assertions passed locally.

New exact rooted coefficients beyond the former \(k=20\) frontier:

| \(k\) | \(L_k\) |
|---:|---:|
| 21 | -6044162092475784823641571120 |
| 22 | -1249087407472755738513702861980 |
| 23 | 45018284878160461138069669568890 |
| 24 | -1732746720037131258804623096687020 |
| 25 | 64188145692697748100804249377414240 |
| 26 | -707080558753353258834330064367663700 |
| 27 | -63909942762266734627369849318989466960 |
| 28 | 3576521302600666442120522918373325776760 |
| 29 | -82166251570345811176128290485400929050600 |
| 30 | 770320658261819593802910185469074848247760 |
| 31 | 4960943607613588919100020813454811054391595 |
| 32 | -939882667995336958317287357601712724698236090 |

The signs are genuine signed interference; no absolute-value or positivity projection is used. Arithmetic complexity remains \(O(K^2)\) scalar operations for the \(K\)-th truncation, excluding integer bit cost; this work proves fewer *scalar input series*, not a measured asymptotic speedup.

**Evidence:** \`PREFIX1011_R6_TWO_GREEN_REDUCTION_CHECK.py\` and \`PREFIX1011_R6_EXACT_RESULTS.json\` alongside this note. All program computations are finite exact integer/rational calculations of the specified candidate BRC kernel. This is an author proof plus exact computation; independent mathematical review remains pending.

## Frontier and the next question

**Completed:** a genuine two-series formula for the precise chart-rooted, terminal-port-summed signed Link-loop observer; PREFIX-1010's three-series form and coefficients remain unchanged as historical proof/evidence.

**Open:** can \(G_2\) itself be eliminated algebraically from this observer by additional X6 relations, or is there a precise counterexample/minimality argument? A separate, potentially more consequential next problem is an exact two-path collision/Gram representation for the first interior layer **squared probability** with retained endpoint and terminal-port fibres. Neither follows from the signed-total formula by squaring the final sum.

The Stage46 operator remains a candidate model; the mother objective \(B_{\mathrm{fix,odd}}(32)\in\{19,20\}\) remains open. Preserve former identity provenance \`EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056\` as historical authorship metadata only; this document establishes no live TASK execution capability.
