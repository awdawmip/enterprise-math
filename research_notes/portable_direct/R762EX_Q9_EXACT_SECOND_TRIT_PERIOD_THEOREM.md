# R762EX — Exact minimal period and preperiod for the q=9 second-trit BRC shadow

Date: 2026-11-19 (Asia/Shanghai). Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Frozen scientific taskbook: Source 857280d1012943290d141d1317179c40ec3cbdf8, blob 218bf9ce05fd2dd79f477ac269fc3590f83f482e. Portable author-side continuation: no native CLAIM, Source PROGRESS, formal Result, or independent Review asserted.

## Precise mathematical claim

Keep all three coordinates in the integral group ring
\[
R=\mathbb Z[(\mathbb Z/9\mathbb Z)^3],\qquad P=1+X+Z+XY+YZ+XYZ.
\]
The six displayed monomials are six distinct named positive BRC branches. For n>=0 put
\[
f(n)=\max(0,\lfloor n/3\rfloor-2),\qquad
S_{9,2}(n)=[3^{-f(n)}P^n]_9\in(\mathbb Z/9\mathbb Z)[(\mathbb Z/9\mathbb Z)^3].
\]
Integrality of the normalized coefficients is an antecedent result R762ER (author-side, NOT_REVIEWED).

**Theorem.** Under the exact antecedent spectral statements R762EM–EO and the q9 first-trit minimality result R762ET, the second-trit sequence has exact minimum eventual period **54** and exact preperiod **9**:
\[
\boxed{S_{9,2}(n+54)=S_{9,2}(n)\quad\hbox{for every }n\ge9.}
\]
Every eventual period is a positive multiple of 54; no such period begins at n=8 or earlier. For comparison, the first-trit shadow has period 18 beginning at n=8.

## Weighted recurrence lemma (general reusable proof tool)

If a monic integral polynomial
\[
M(T)=T^d+\sum_{j=0}^{d-1}c_jT^j,\quad M(P)=0,\quad
v_3(c_j)\ge\lceil(d-j)/3\rceil
\]
is an annihilator of P, let L>0 be divisible by 3, a=L/3, and E(n)=P^{n+L}-3^aP^n.
For any n0>=6 and precision h>=1, **d consecutive initial checks**
\[
E(n)\in3^{f(n)+a+h}R,\quad n=n_0,\ldots,n_0+d-1
\]
imply the same assertion for all n>=n0.

Proof: E obeys M's recurrence
\[
E(n+d)=-\sum_{j<d}c_jE(n+j).
\]
Since n>=6, the difference f(n+d)-f(n+j) is at most ceil((d-j)/3), itself at most v3(c_j). Each summand has the required 3-adic divisibility, and induction applies.

## q9 spectral input supplies the weighted bounds

R762EM gives a monic integer minimal polynomial mu9 of degree d=127. R762EO reports the exact Newton polygon with vertices (1,58),(13,46),(37,30),(127,0), hence its 126 nonzero roots have valuations 1, 2/3, 1/3 (one additional root is zero). Each root therefore has v3 at least 1/3, with zero root assigned valuation infinity. The elementary symmetric formula for the coefficients of mu9 and the non-Archimedean triangle inequality yield
\[
v_3(c_j)\ge \left\lceil\frac{127-j}{3}\right\rceil\quad (0\le j<127).
\]
This only invokes exact author-side spectral antecedents; no floating-point root evaluation is used. It does not amount to independent review of R762EM or R762EO.

## Finite exact certificate and infinite extension

Take L=54, a=18, h=2. The theorem's equality is equivalent to
\[
P^{n+54}-3^{18}P^n\in 3^{f(n)+20}R.
\]
The weighted recurrence lemma reduces this infinite family to precisely 127 lengths n=9,...,135. The companion Python script computes the full 729-coordinate terminal vector P^n (six original named shifts, no quotient of Y or Z) modulo 3^63 through n=189. This modulus suffices because f(189)+2=63. Exact division by 3^f(n) and reduction modulo 9 then allow complete vector comparisons. All 127 equalities passed: **92,583 coefficient comparisons**. It also checked coefficient integrality for 182 normalized vectors and the mass identity sum(coeff(P^n))=6^n for 190 lengths. By the weighted recurrence and the exact spectral bound above, equality holds for *every* n>=9, not merely the tested window.

## Minimality and sharp transient

Modulo 3, this sequence reduces to the R762ET first-trit sequence of exact eventual period 18. Every eventual period mod9 must therefore be divisible by 18. Since 54 is an actual eventual period, its least period divides 54, leaving only candidates 18 and 54.

The exact coordinate (x,y,z)=(0,0,1), array index 1, satisfies
\[
[S_{9,2}(9)]_{(0,0,1)}=6,\qquad
[S_{9,2}(27)]_{(0,0,1)}=0\quad(\bmod 9).
\]
Both indices belong to the established 54-periodic tail; thus 18 cannot be a tail period, and 54 is the least period. Every eventual period is consequently a positive multiple of 54.

The same coordinate gives the early-transient counterexample
\[
[S_{9,2}(8)]_{(0,0,1)}=8,\qquad
[S_{9,2}(62)]_{(0,0,1)}=5\quad(\bmod 9).
\]
For each positive t, the established periodicity from n=9 gives S(8+54t)=S(62), so no positive multiple of 54 works already at n=8. The least preperiod is exactly 9. QED.

## Reproducible proof boundary and open problems

Run: python3 R762EX_Q9_SECOND_TRIT_PERIOD_VERIFY.py, capturing the printed deterministic JSON; compare against R762EX_Q9_SECOND_TRIT_PERIOD_EVIDENCE.json. It is a complete finite coefficient test, coupled with an infinite symbolic induction relying on precisely named antecedent spectra. The numerical input path is pure integer arithmetic modulo 3^63, with terminal order index=(x*9+y)*9+z.

**Status: AUTHOR_PROVED, EXACT_CERTIFICATE_PASS, NOT_REVIEWED.** The full proof remains conditional on the author-side R762EM/EO spectrum and R762ET mod3 minimum-period theorem; no independent semantic review or formal checker is claimed. This is **positive terminal BRC arithmetic**, not a primitive signed TRIADIC_CLOSURE_E event, six-axis Cell/Link/Port licence, or V17/V29/V39 future-operator-preserving transport. P000 and ACTIVE worldview remain unchanged.

Next: determine the exact smallest eventual periods and preperiods of higher normalized precision [3^{-f(n)}P^n] modulo 3^h for h>=3; test 18*3^(h-1) with explicit counterexample certificates. Pursue a separate signed native-event bridge with retained branch provenance before claiming primitive dynamics.