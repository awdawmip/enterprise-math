# X6 R56 — Complete sharp positive-BRC Port ambiguity radius through the equal-source endpoint

Date: 2026-11-20 (Asia/Shanghai). Research line RS-X6-NATIVE-TIME-DYNAMICS.
Historical author lineage EM-X6-214D9C; existing portable Activity RA-545183ADD4EF71C3E4698AEE.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_RATIONAL_NAMED_BRC_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.

## Model, provenance and scope

Retain the **conditional R44 named, once-only whole-triad** A_i/B_i branch grammar with proposed release R, reoccupation T and root observer F erasing the source and Port names. R44/R55 verify the four short-word **positive BRC path masses** (not amplitudes or signed cancellation). For any integer Port count q >= 1, strictly positive source weights, sum s and product t with s>0 and 0<t<=s²/4,

\[
A_q(s,t)=(q s,(q-1)s,2(q^2-1)t,2qt)
\]

records F, FT, FF and FRF. Each model may have its own unknown common additive offset, and each of four observation channels has absolute error <= eta. Given true vector V and rival unshifted vector W, the smallest shared-observation ambiguity radius, optimizing their relative offsets, is

\[
E(V,W)=\frac{\max_i(V_i-W_i)-\min_i(V_i-W_i)}4.
\]

This is the minimax radius for two models whose per-channel error budgets are BOTH eta: the best relative offset removes the midpoint of the residual range and the shared reading bisects the two resulting four-vectors. It is not the one-model error radius.

Fix true q=4, s=1, product 0<P<=1/4. Then V=(4,3,30P,8P), and the true weights are positive roots of u²-u+P.

## Main theorem (previously open interval)

For **every real** P in [23/100,1/4], against every distinct positive integer Port count q !=4, every strictly positive rival weight pair and arbitrary separate common offsets, the exact globally sharp ambiguity radius is

\[
\boxed{
\eta_{\rm crit}(P)=
2\sqrt{\frac{11P}{19}}-\frac34+\frac{21P}{38}.
}
\]

For eta<eta_crit, the four observations uniquely identify Port count 4; at eta=eta_crit there exists a strictly positive q=5 rival and a common measurement compatible with both.

Together with R54 and R55, this completes the full normalized interval 0<P<=1/4, with two prior transition points:

\[
\rho=\frac{7601-100\sqrt{5497}}{882},\qquad
\sigma=\frac{6821-95\sqrt{4873}}{882}.
\]

\[
\boxed{
\eta_{\rm crit}(P)=
\begin{cases}
(19+42P)/400,&0<P\le\rho,\\
\frac14\sqrt{(16P-3)/5},&\rho\le P\le\sigma,\\
2\sqrt{11P/19}-3/4+21P/38,&\sigma\le P\le1/4.
\end{cases}}
\]

This corollary uses the **exact hypotheses and prior proofs** of R54/R55; R56 adds a proof only for the previously uncovered [23/100,1/4] and checks the common endpoint.

## Proof I — positive q=5 witness

Set

\[
s_*=2\sqrt{11P/19},\quad t_*=11P/19=s_*^2/4.
\]

The two competing source weights are both s_*/2>0. The four unshifted residuals are

\[
r=(4-5s_*,\ 3-4s_*,\ 42P/19,\ 42P/19).
\]

On [23/100,1/4], r_2<=r_1<=r_3=r_4. Indeed r_1-r_2=1-s_*>0, while r_3-r_1=42P/19-4+5s_*>0 already at 23/100 and increases with P. The range is therefore 42P/19-3+4s_*. Dividing by four gives exactly the claimed eta_crit. Midpoint offsets and the midpoint observation give an admissible ambiguity witness.

This candidate is strictly increasing in P and is always less than 3/20. At P=1/4, this reduces to the exact inequality

\[
2\sqrt{11/76}<579/760
\]

whose squared positive-side difference is 841/577600>0. Thus write E_*(P)<3/20 throughout this interval.

## Proof II — q=5 global lower bound (positivity, not unconstrained products)

Let arbitrary rival q=5 have s>0 and 0<t<=s²/4, and define

\[
r=(4-5s,\ 3-4s,\ 30P-48t,\ 8P-10t),\quad E=(\max r-\min r)/4.
\]

It suffices to exclude E<E_*; then E<3/20 and every pairwise residual difference has magnitude <3/5.

From r_1-r_2=1-s, s>2/5. From r_3-r_4=22P-38t and r_4-r_2=8P-3+4s-10t, we get

\[
t<\frac{22P+3/5}{38},\qquad
s<\frac{18/5-8P+10(22P+3/5)/38}{4}
=\frac{357}{380}-\frac{21P}{38}
\le\frac{3087}{3800}<\frac{41}{50}.
\]

Define the two concave lower envelopes

\[
f_3(s)=4s-3+30P-12s^2,\qquad
f_4(s)=4s-3+8P-\frac52s^2.
\]

Since t<=s²/4, always 4E>=r_3-r_2>=f_3(s) and 4E>=r_4-r_2>=f_4(s).

If s<=s_*, then f_3 is strictly decreasing for s>2/5, and
4E>=f_3(s)>=f_3(s_*)=4E_*.

If s>=s_*, concavity of f_4 on [s_*,41/50] gives its minimum at an endpoint. We have f_4(s_*)=4E_* and also

\[
f_4(41/50)-4E_*=
(110/19)P+1599/1000-8\sqrt{11P/19}>0.
\]

For the last inequality, the expression decreases throughout [23/100,1/4], and its value at P=1/4 is positive: the difference of squares between its positive rational part and radical part is
6210161/361000000>0. Hence 4E>=4E_* in either case, contradicting E<E_*.

So q=5 attains precisely E_* and cannot improve it.

## Proof III — exclude all other positive integer q without a cutoff

The R50/R54 annihilating contrast, evaluated at the fixed true P, gives for q>=2, q!=4,

\[
E\ge B_q(P)=
\frac{|4-q|[(q^2-q-1)+2P(4q+1)]}
{4q^2(q-1)}.
\]

For q=2, B_2=(1+18P)/8>=257/400>3/20.
For q=3, B_3=(5+26P)/72>=61/400>3/20.

For q>=8, B_q(P) increases in q: the exact numerator of B_(q+1)-B_q, over positive denominator 2q²(q-1)(q+1)², is

\[
(2-4P)q^3+(1+22P)q^2+(38P-7)q+(4P-2)>0
\]

for P in [23/100,1/4] and q>=8. The first three terms are positive and the q³ term dominates the last negative constant. Consequently B_q(P)>=B_8(23/100)=3509/22400>3/20.

For q=1, the true D-H equals 22P, while the rival D-H equals -2t<0. The residual range is >22P, giving E>11P/2>3/20.

It remains to exclude q=6 and q=7, for which the contrast bound alone is insufficient near P=1/4. Both are excluded using positive-weight feasibility, with no numerical optimization.

**q=6.** If E<=3/20, residual differences give

\[
\frac{22P-3/5}{58}\le t\le\frac{22P+3/5}{58}.
\]

In particular t>=223/2900 and t<=61/580. From r_4-r_2<=3/5,

\[
s\le\frac{18/5-8P+12t}{5}\le\frac{2191}{3625}<61/100.
\]

Also |r_1-r_2|<=3/5 forces s>=2/5. Combining r_4-r_2<=3/5 with t<=s²/4 implies

\[
5s-3s^2\le18/5-8P\le44/25.
\]

On [2/5,61/100] the left side is increasing. At s=13/25 it equals 1118/625>44/25; therefore s<13/25 and t<=s²/4<169/2500<223/2900, contradiction.

**q=7.** Similarly E<=3/20 gives t<=61/820. From r_4-r_2<=3/5,

\[
s\le\frac{18/5-8P+14t}{6}\le5743/12300<1/2.
\]

Since |r_1-r_2|<=3/5, s>=2/5. Positivity and r_4-r_2<=3/5 require

\[
6s-\frac72s^2\le18/5-8P\le44/25.
\]

The left side increases on [2/5,1/2] and already equals 46/25>44/25 at 2/5. Contradiction.

Thus every rival q!=4,5 has E>3/20>E_*. With Proof II and the positive q=5 witness, the claimed **globally sharp radius** follows. QED.

## Verification, evidence scope, unresolved native question

The companion Python Fraction verifier enumerates the actual **R44 named whole-triad branch grammar** for four words over Port counts 1..12 (48 independent word/count checks), compares coefficient polynomials, tests five rational exact witnesses in [23/100,1/4], and validates exact rational bounds used above. The symbolic proof covers the continuum of real P and all rival positive integers; finite checks are supporting calculations, not that proof.

Input lineage: R44 named event grammar, R47 mass identities, R50/R51 corrected contrast norm, R54 first global segment, R55 post-rho segment. The fixed P000 V5 native six-axis Cell/Link/Port and triadic closure premises are unchanged. R/T remain **conditional candidate transitions**: a Cell/Link/Port/source-preserving native TRIADIC_CLOSURE_E admission map and independent review remain open. Neither formal Result nor native PROGRESS is asserted.

Next research: test admissible source-preserving native R/T embedding against frozen P000 joint occupancy and transition signatures. For metrology, extend the exact radius beyond normalized true p=4 or allow structured correlated rather than coordinate-wise errors.
