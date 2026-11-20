# X6 R55 — Sharp positive-BRC Port ambiguity radius beyond the R54 discriminant transition

Date: 2026-11-20 (Asia/Shanghai). Original research line: RS-X6-NATIVE-TIME-DYNAMICS; recorded author lineage EM-X6-214D9C; Activity RA-545183ADD4EF71C3E4698AEE.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_RATIONAL_NAMED_BRC_CHECK / NOT_INDEPENDENTLY_REVIEWED.

## Frozen model and observable

Retain precisely the R44–R54 **conditional** named, once-only whole-triad A_i/B_i branch grammar, proposed release R and reoccupation T, and root observation F which erases the source and Port labels. Positive source weights are alpha,beta; S=alpha+beta, P=alpha*beta, with 0<P<=S²/4. Four short-word positive BRC path masses are

\[
A_q(S,P)=(qS,(q-1)S,2(q^2-1)P,2qP)
\]

in order F, FT, FF, FRF. A common real offset b and independent per-channel error bounded by eta are allowed for *both* candidate models. Two candidate mass vectors are compatible with some common reading exactly when their offset-adjusted L-infinity distance is at most 2 eta. Equivalently, for fixed true V and rival raw mass vector W, the minimum such eta over their relative common offsets is one quarter of the range of the four components of V-W.

Fix the true p=4, S=1, 0<P<=1/4, V=(4,3,30P,8P). The actual source weights are the positive roots of z²-z+P, so the theorem is valid throughout the stated P interval.

## Theorem: exact global radius on a new post-transition interval

Define the previously established R54 endpoint and the new second transition

\[
\rho=\frac{7601-100\sqrt{5497}}{882}\approx0.211819034439918,\quad
\sigma=\frac{6821-95\sqrt{4873}}{882}\approx0.214678840192349.
\]

For **every real** \(\rho\le P\le23/100\), against **every integer** \(q\ge1\), \(q\ne4\), arbitrary strictly positive competing source weights, and arbitrary relative common offset, the **exact** ambiguity radius is

\[
\boxed{\eta_{\rm crit}(P)=
\begin{cases}
\frac14\sqrt{\frac{16P-3}{5}},&\rho\le P\le\sigma,\\[3pt]
2\sqrt{\frac{11P}{19}}-\frac34+\frac{21P}{38},&\sigma\le P\le\frac{23}{100}.
\end{cases}}
\]

At eta<eta_crit, the Port count 4 is uniquely identified. At eta=eta_crit, a positive-weight q=5 model and a shared measurement exist. The two formulas agree at sigma, and at rho this theorem agrees exactly with R54's (19+42P)/400. The previously open near-critical region rho<P<=23/100 is therefore resolved, including a *second* change of the active residual constraints.

## Proof A: construct exact admissible q=5 witnesses

Put rival sum s>0 and product t>0. The positive-root condition is 0<t<=s²/4. The four residuals without the rival bias are

\[
r=(4-5s,\ 3-4s,\ 30P-48t,\ 8P-10t),\qquad
\eta=\frac{\max r_i-\min r_i}{4}.
\]

**Regime I, rho<=P<=sigma.** Let
\[
z=\sqrt{(16P-3)/5},\quad s=1-z,\quad t=s^2/4.
\]
Then r1=r4 is maximal, r2 is minimal and r2<=r3<=r1; hence eta=(1-s)/4=z/4. The two ordering inequalities reduce to
\[
r_3-r_2=-(21z^2-160z+43)/8\ge0,\quad
r_1-r_3=(21z^2-152z+43)/8\ge0.
\]
The smaller roots of these two quadratics are precisely z(rho) and z(sigma), respectively, proving the interval assertions. Both rival weights equal s/2>0.

**Regime II, sigma<=P<=23/100.** Let
\[
s=2\sqrt{11P/19},\qquad t=11P/19=s^2/4.
\]
Now r3=r4 is maximal and r2 is minimal; r2<=r1<=r3. Thus eta=(r3-r2)/4=s-3/4+21P/38. The middle inequality is equality at sigma and is monotone thereafter; s<1 on this interval. Again both source weights equal s/2>0.

In either regime choose the rival relative offset \(b=(\max r+\min r)/2\); then \(\lVert V-(A_5(s,t)+b\mathbf1)\rVert_\infty=2\eta\). The midpoint between the two adjusted mass vectors is a single reading within eta of both. This proves the upper bound and equality attainability.

## Proof B: global optimality among all positive q=5 rivals

For arbitrary rival (s,t), write \(E=(\max r-\min r)/4\). If E<=the proposed eta_crit, then E<107/1000 throughout the theorem interval. Pairwise differences imply \(|1-s|=|r_1-r_2|\le4E\), so \(s>1-428/1000>1/6\). Combining \(r_1-r_4\ge-4E\) and \(r_3-r_4\ge-4E\) gives

\[
s\le (76-42P+96E)/95
< (76-42(21/100)+96(107/1000))/95
<41/50.
\]

Define concave functions
\[
f_4(s)=4s-3+8P-\tfrac52s^2,\qquad
f_3(s)=4s-3+30P-12s^2.
\]
Since t<=s²/4,
\[
4E\ge r_4-r_2\ge f_4(s),\qquad 4E\ge r_3-r_2\ge f_3(s).
\]

Regime I: if s<=s_* from Proof A, then \(4E\ge r_1-r_2=1-s\ge1-s_*=4\eta_*\). If s>=s_*, concavity on [s_*,41/50], together with \(f_4(s_*)=1-s_*\) and \(f_4(41/50)\ge1-s_*\), gives \(4E\ge f_4(s)\ge4\eta_*\).

Regime II: if s<=s_*, \(f_3'(s)=4-24s<0\) for s>1/6, so \(4E\ge f_3(s)\ge f_3(s_*)=4\eta_*\). If s>=s_*, use concavity of f4 and \(f_4(s_*)=4\eta_*\), \(f_4(41/50)\ge4\eta_*\), to obtain the same conclusion.

For completeness, the two endpoint inequalities used above are elementary:
\[
f_4(41/50)=8P-1401/1000.
\]
In Regime I, \(8P-1401/1000-\sqrt{(16P-3)/5}>0\) already at \(P=21/100\), and increases thereafter (its derivative is \(8-8/(5\sqrt{(16P-3)/5})>0\)). In Regime II the difference is
\[
(110/19)P+1599/1000-8\sqrt{11P/19}.
\]
It decreases on the stated interval (its stationary point is \(76/275>23/100\)) and at \(P=23/100\) is strictly positive: its two positive terms satisfy
\[
(55681/19000)^2-64(253/1900)=23893761/361000000>0.
\]
Thus no q=5 model improves on the constructed radius.

## Proof C: all other Port counts excluded, without an integer cutoff

For q>=2, q!=4, the exact q-model annihilator from R50/R54 yields the valid lower bound
\[
E\ge B_q(P)=
\frac{|4-q|[(q^2-q-1)+2P(4q+1)]}{4q^2(q-1)}.
\]
For q=2, \(B_2=(1+18P)/8>107/1000\); for q=3, \(B_3=(5+26P)/72>107/1000\) since P>=rho>21/100. For q>=6, the q-increment numerator of B is
\[
(2-4P)q^3+(1+22P)q^2+(38P-7)q+(4P-2)
\]
over the positive denominator \(2q^2(q-1)(q+1)^2\). It is strictly positive for q>=6 and P in [rho,23/100]. Thus \(B_q\ge B_6=(29+50P)/360\ge79/720>107/1000\).

For q=1, the competing D-H difference is -2t<0 but the true D-H difference is 22P>0, hence E>(11/2)P>107/1000. All other q are therefore strictly worse than the q=5 witness throughout the theorem interval. QED.

## Exact evidence, status and continuation

Verifier: \`research_notes/portable_direct/x6_r55_post_rho_global_radius_verify.js\`.
Results: \`research_notes/portable_direct/x6_r55_post_rho_global_radius_results.json\`.

It enumerates the named R44 once-only BRC transitions for q=1..8 and the four words, compares their exact positive-path weight monomials with the four coefficient formulas, checks exact rational witness families in both regimes, rational root sign brackets and competing-Port linear exclusions on declared samples. General real-P coverage and all q are established by the algebraic proof above, not inferred from finite tests.

The theorem concerns *only* the conditional R/T grammar and positive BRC observer. Native P000 V5, ACTIVE six-axis Heartbeat World, Cell/Link/Port joint-relation preservation and task-frozen scientific inputs remain unchanged. No actual native TRIADIC_CLOSURE_E admission, independent review or formal Result is asserted. This is portable scientific material, not a canonical task PROGRESS event.

Next: determine \(\eta_{\rm crit}(P)\) on \(23/100<P\le1/4\), in particular whether the q=5 positivity-boundary candidate remains globally minimal after other q rivals are tested; separately construct a source-preserving native R/T admission map.