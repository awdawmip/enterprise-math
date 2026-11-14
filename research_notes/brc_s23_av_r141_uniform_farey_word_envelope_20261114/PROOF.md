# R141 — Uniform exact per-word Farey-gap horizon

Date: 2026-11-14 (Asia/Shanghai). Status: AUTHOR-SIDE MATHEMATICAL PROOF / NOT_REVIEWED.
Scientific input pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Scope: external tied-phase S23 observer (a scalar Sturmian readout); no native X6 or signed-port equivalence is asserted.
Dependencies: R137B (Farey intercept-gap enumeration), R138 (\(D_g\ge\min(b,d)\)), R139 (individual-gap permanent threshold \(T_g=\max(2,bd-D_g+2)\)).
R140 established the following equality only for \(4\le m\le64\); this note supplies a uniform argument for **all** \(m\ge5\), conditional on the cited author-side predecessor lemmas.

## Statement

For integers \(m\ge5\), \(K\ge2\), let \(V(K,m)\) contain the words
\[
S_i^{(K)}(\theta)=\lfloor(K+i)\theta\rfloor-\lfloor(K+i-1)\theta\rfloor,\quad i=0,\ldots,m-1,\quad 0<\theta<1.
\]
Let \(\mathcal W_m\) be the length-\(m\) finite Sturmian language. For each \(w\in\mathcal W_m\), denote its open Farey intercept-gap representations by \(\mathcal G_m(w)\) and put
\[
U_w=\min_{g\in\mathcal G_m(w)}T_g,\qquad
U_{\rm rep}(m)=\max_{w\in\mathcal W_m}U_w,\qquad
T_g=\max(2,b_gd_g-D_g+2).
\]

**Theorem R141.** For every integer \(m\ge5\),
\[
\boxed{U_{\rm rep}(m)=(m-2)^2+1.}
\]
Moreover the two extremal patterns \(e_m=10^{m-2}1\) and \(\overline{e_m}=01^{m-2}0\) satisfy
\[
U_{e_m}=U_{\overline{e_m}}=(m-2)^2+1.
\]
Every other word possesses a Farey-gap representation with a permanent threshold at most the same bound. Consequently
\[
\boxed{K\ge(m-2)^2+1\quad\Longrightarrow\quad V(K,m)=\mathcal W_m.}
\]
This bound is for permanent **pattern** saturation. It improves the sufficient uniform bound \(K\ge(m-1)^2+2\) from R138, but does not assert equality for the minimal eventual pattern threshold \(T(m)\). The exact smaller \(T(m)\) remains open for unrestricted \(m\).

## 1. Exact slope-support interval

Write a binary word as \(w=w_0\cdots w_{m-1}\) and its prefix counts as \(s_0=0,\ s_j=\sum_{i<j}w_i\). A pair \((\theta,\rho)\), \(0<\theta<1,\ 0\le\rho<1\), realizes the mechanical word \(w\) precisely when
\[
s_j\le\rho+j\theta<s_j+1\quad(0\le j\le m).
\]
The intersection of the \(m+1\) half-open intercept intervals is nonempty exactly when
\[
\max_{0\le j\le m}(s_j-j\theta)-\min_{0\le j\le m}(s_j-j\theta)<1.
\]
Equivalently the possible slopes form the *open* interval \(I_w=(\alpha_w,\beta_w)\) (intersected with \((0,1)\)), where
\[
\alpha_w=\max\left(0,\max_{0\le i<j\le m}
 \frac{s_j-s_i-1}{j-i}\right),\qquad
\beta_w=\min\left(1,\min_{0\le i<j\le m}
 \frac{s_j-s_i+1}{j-i}\right).
\]
For a Sturmian word \(\alpha_w<\beta_w\); both endpoints are reduced fractions with denominator at most \(m\). Conversely every \(\theta\in I_w\) admits an intercept realizing \(w\).

A reduced endpoint \(p/q\) with \(q>m/2\) has the following useful exact interpretation: if it is a lower endpoint, some length-\(q\) consecutive subword has \(p+1\) ones; if upper, some length-\(q\) subword has \(p-1\) ones. Indeed the unreduced denominator \(j-i\le m\) must be a multiple of \(q\), hence equals \(q\).

## 2. Farey small-denominator support lemma

**Lemma.** For every integer \(m\ge6\), any \(w\in\mathcal W_m\) other than \(e_m,\overline{e_m}\) has a reduced fraction \(p/q\in[\alpha_w,\beta_w]\), \(0\le p\le q\), with \(q\le m-3\).

**Proof.** Set \(n=m-3\ge3\), and suppose the closed slope-support interval avoids the Farey fractions \(F_n\). Since both \(\alpha_w,\beta_w\in F_m\) and \(\alpha_w<\beta_w\), they are two distinct fractions newly inserted between the same consecutive neighbors \(a/b<c/d\) of \(F_n\). Their denominators obey \(b+d>n=m-3\), so \(b+d\ge m-2\).

Every new reduced fraction in that old Farey cell is of the form \((ra+sc)/(rb+sd)\) with positive integers \(r,s\), because \(bc-ad=1\). The first candidate is the mediant \((a+c)/(b+d)\); the next possible denominator is at least \(b+d+\min(b,d)\). For two distinct new fractions of denominator at most \(m\), necessarily \(\min(b,d)\le2\).

**Case A: \(\min(b,d)=1\).** A denominator-1 fraction in \([0,1]\) is 0 or 1, so the old cell is \((0,1/(m-3))\) or its reflection about \(1/2\). For \(m\ge6\), the only order-\(m\) fractions strictly inside the left cell are
\[
\frac1m<\frac1{m-1}<\frac1{m-2};
\]
an interior fraction with numerator at least 2 has denominator at least \(2(m-3)+1>m\).

If \((\alpha,\beta)=(1/m,1/(m-1))\), the lower endpoint forces two ones in the entire length-\(m\) word, while the upper forces an all-zero length-\((m-1)\) substring. Contradiction: at most one position lies outside that substring.

If \((\alpha,\beta)=(1/(m-1),1/(m-2))\), the former forces a length-\((m-1)\) substring with two ones and the latter an all-zero length-\((m-2)\) substring. Both ones must lie in the two positions outside the zero substring. If these positions are opposite ends of the whole word, no length-\((m-1)\) substring includes both; otherwise they are adjacent and the word has \`11\`, which forces \(\alpha\ge1/2>\beta\). Contradiction.

Thus \((\alpha,\beta)=(1/m,1/(m-2))\). The word contains exactly two ones, and an all-zero length-\((m-2)\) substring. As a \`11\` factor is excluded by \(\beta<1/2\), the only arrangement is \(w=10^{m-2}1\).

The right edge old cell is the bitwise complement under \(\theta\mapsto1-\theta\); directly \(s'_j=j-s_j\) gives \((\alpha_{\bar w},\beta_{\bar w})=(1-\beta_w,1-\alpha_w)\), so its sole exception is \(\overline{e_m}\).

**Case B: \(\min(b,d)=2\).** To have two new fractions, necessarily \(b+d=m-2\) and the second lies at denominator \(m\); hence the other old denominator is \(m-4\). Such a cell, if present, borders \(1/2\) and occurs only for odd \(m\ge7\). On the left of \(1/2\), its two new fractions have the form
\[
\alpha=\frac r{m-2},\qquad\beta=\frac{r+1}m.
\]
The lower endpoint forces \(r+1\) ones in some length-\((m-2)\) subword, whereas the upper forces only \(r\) ones in the whole word: impossible. On the reflected right side, the two endpoints are
\[
\alpha=\frac{m-r-1}m,\qquad
\beta=\frac{m-r-2}{m-2}.
\]
The lower forces \(m-r\) ones in the length-\(m\) word and the upper forces \(m-r-3\) ones in a length-\((m-2)\) subword. Removing only two positions cannot remove three ones, again impossible.

The old Farey cell therefore cannot contain a slope-support interval without a fraction of \(F_{m-3}\), apart from the two patterns found in Case A. \(\square\)

For \(m=5\), the same conclusion follows from a complete 24-word exact finite check (the special \(F_2\) edge cells contain one extra inserted fraction); see the finite checker below. This is a finite base case, not an extrapolation.

## 3. Transfer to permanent gap availability

Fix a nonextremal word \(w\) and a fraction \(p/q\in[\alpha_w,\beta_w]\), \(q\le m-3\). Since \(I_w\) is open and its endpoints belong to \(F_m\), at least one Farey cell of order \(m\), adjacent to \(p/q\), lies inside \(I_w\). Choose any intercept gap in this cell representing \(w\). If the cell's neighboring denominators are \(b,d\), one equals \(q\), the other is at most \(m\).

By R138, \(D_g\ge\min(b,d)\). Thus
\[
b d-D_g\le b d-\min(b,d)
\le q(m-1)\le(m-3)(m-1)=(m-2)^2-1,
\]
where the middle estimate holds whether the other denominator is larger or smaller than \(q\). Applying R139,
\[
U_w\le T_g\le(m-2)^2+1.
\]

## 4. Extremal gaps attain the bound

The word \(e_m=10^{m-2}1\) has slope-support interval
\[
I_{e_m}=(1/m,\,1/(m-2)).
\]
Its only two order-\(m\) slope cells are \((1/m,1/(m-1))\) and \((1/(m-1),1/(m-2))\), each with exactly one intercept gap for this word. In the R137B/R139 gap format, the two \((b,d,D_g)\) triples are respectively
\[
(m,m-1,m)\quad\text{and}\quad(m-1,m-2,m-1).
\]
Their \(bd-D_g\) values are \(m(m-2)\) and \((m-1)(m-3)\). Therefore
\[
U_{e_m}=\min\{m(m-2)+2,(m-1)(m-3)+2\}
=(m-2)^2+1.
\]
The complement involution preserves individual gap realizability for all \(K\), hence its \(U_w\) agrees. Combining this with Section 3 proves the theorem. \(\square\)

## Verification and boundaries

The exact checker \`check_r141.py\` adapts the validated Farey-intercept enumeration from R140 and independently checks the new low-denominator classification and every word's minimum R139 permanent threshold for **all** integer \(m=5,\ldots,64\). It found 466,474 distinct word records and 1,370,486 gap records, with precisely the two extremal low-denominator exceptions for each \(m\), and equality \(U_{\rm rep}=(m-2)^2+1\) in every instance. The checker does not replace the all-\(m\) argument above.

The conclusion uses R138/R139 as named author-side dependencies; independent theorem review remains pending. The mechanical phase is an external one-parameter observer. No assertion about full native X6 state, provenance, signed ports, or later operations is derived from this pattern-level quotient.

## Next research frontier

The minimal eventual pattern threshold \(T(m)\) is strictly smaller than \(U_{\rm rep}(m)\) in general (for example R140 proves \(T(20)=163\), \(U_{\rm rep}(20)=325\)). The next question is to show, for every \(m\ge5\), that every nonextremal word is realizable at **each** coefficient \(K\ge E(m)=(m-2)\lfloor(m-1)/2\rfloor+1\), even before its selected permanent Farey gap activates. The R137B modular criterion supplies the exact finite complementary-gap condition. R140 proves this only for \(m\le64\); a symbolic word-covering argument is still needed for all \(m\).
