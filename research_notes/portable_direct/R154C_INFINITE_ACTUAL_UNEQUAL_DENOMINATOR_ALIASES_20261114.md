# R154C — Infinite genuine *unequal-denominator* Sturmian word-identity aliases

Date: 2026-11-14 (Asia/Shanghai). AUTHOR-SIDE COMPLETE PROOF + EXACT TESTS; independent mathematical review NOT_REVIEWED. Frozen science pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.

**Scope:** external tied-phase scalar finite Sturmian S23 observation; not an equivalence with native six-axis Heartbeat World, P000, or a physically typed BRC operation. This extends R154B's complete classification of the equal-denominator sector and answers its next question by constructive counterexample in the unequal-denominator sector.

## Theorem — An infinite actual Sturmian alias family

For every integer \(r\ge1\), define two **distinct** binary words of equal length \(m=2r+4\):

\[
\boxed{u_r=0\,1^r\,0\,1^{r+1}\,0,\qquad
v_r=0\,1^{r+1}\,0\,1^r\,0.} \tag{1}
\]

Their free-intercept slope support intervals coincide, with strictly interior endpoints

\[
\boxed{\alpha=\frac r{r+1},\quad \beta=\frac{r+1}{r+2}},
\]

whose **reduced denominators \(r+1\) and \(r+2\) differ and are coprime**. Both words have *identical exact absolute integer intercept cuts* in R146–R153 notation:

\[
\boxed{(a,b,c,d,U,V)=(r,r+1,r+1,r+2,1,0).} \tag{2}
\]

Consequently their integer-phase fiber counts are equal at **every** \(K=L+1\ge2\), with closed formula

\[
\boxed{
C_{u_r}(L+1)=C_{v_r}(L+1)
=\left\lceil\frac{L+1}{r+1}\right\rceil
-\left\lfloor\frac L{r+2}\right\rfloor-1.} \tag{3}
\]

Thus *preserving the whole support interval, both exact phase cuts, and the complete future integer-fiber count sequence still cannot recover the original word*. Equal-denominator resonance is not a necessary condition for **word-identity** aliasing, even though unequal denominators do ensure **cut-residue** injectivity (R153.1). These are different observation maps.

## Proof

For a binary factor \(f\) of length \(q\) with \(z\) zeros and \(t=q-z\) ones, the free-intercept slope support inequalities against candidate endpoints \(\alpha=r/(r+1)\) and \(\beta=(r+1)/(r+2)\) are exactly

\[
\frac{t-1}{q}\le\frac r{r+1}
\iff q\le(r+1)(z+1), \tag{4}
\]

and

\[
\frac{t+1}{q}\ge\frac{r+1}{r+2}
\iff q\ge(r+2)(z-1). \tag{5}
\]

**All factors obey both inequalities.** Both words have exactly 3 zeros, at their first, middle, and last positions, with internal runs of lengths \(r\) and \(r+1\) in opposite order.

To verify (4), classify a factor by \(z\):
- \(z=0\): a run of consecutive ones has length at most \(r+1\), so \(q\le r+1\).
- \(z=1\): at most the two internal runs and their separating zero, so \(q\le2r+2=2(r+1)\).
- \(z=2\): the factor omits at least one endpoint zero, so \(q\le2r+3\le3(r+1)\).
- \(z=3\): the factor is the entire word, \(q=2r+4\le4(r+1)\).

To verify (5), the assertion is vacuous for \(z\le1\). For \(z=2\), a factor containing two zeros must span two consecutive zeros of the original word, separated by at least \(r\) ones, so \(q\ge r+2\). For \(z=3\), the factor is the whole word, \(q=2r+4=2(r+2)\).

Therefore \(\alpha(w)\le r/(r+1)\) and \(\beta(w)\ge(r+1)/(r+2)\) for either word. A factor \(1^{r+1}\) has \(q=t=r+1\), attaining lower bound \((t-1)/q=r/(r+1)\); and a factor \(0\,1^r\,0\) has \(q=r+2,t=r\), attaining upper bound \((t+1)/q=(r+1)/(r+2)\). These factors occur in **both** words. Thus the support endpoints are exactly as claimed, with positive gap and therefore genuine finite Sturmian words.

Let \(p_j\) be the number of ones in the first \(j\) letters and let \(z_j=j-p_j\) be the number of zeros in the prefix. Using the R146/R152 definition of cuts,

\[
U=\min_{0\le j\le m}\{(r+1)(p_j+1)-rj\}
  =\min_j\{j+(r+1)(1-z_j)\}, \tag{6}
\]

\[
V=\max_{0\le j\le m}\{(r+2)p_j-(r+1)j\}
  =\max_j\{j-(r+2)z_j\}. \tag{7}
\]

The first zero is the first symbol, so \(j=1\) has \(z_j=1\), giving \(U\le1\). Across all prefixes:
- before the first zero (\(j=0\)) (6) equals \(r+1\);
- between the first and second zero \(z_j=1,j\ge1\), giving (6) at least 1;
- between the second and third zeros \(z_j=2,j\ge r+2\), giving (6) at least 1;
- after the third zero \(j=m=2r+4,z_j=3\), giving (6) equal 2.
Hence \(U=1\) in both words.

For (7), \(j=0\) gives value 0, and for all later prefixes:
- after the first zero but before the second, \(z_j=1\) and \(j\le r+2\), giving value at most 0;
- after the second but before the third, \(z_j=2\) and \(j\le2r+3\), giving value at most \(-1\);
- after the final zero, \((j,z_j)=(2r+4,3)\), giving a negative value.
Hence \(V=0\) for both. This proves (2).

R146's exact count formula (externally defined S23 fiber count) then gives

\[
C_w(L+1)=\left\lceil\frac{(r+1)L}{r+2}\right\rceil
-\left\lfloor\frac{rL-1}{r+1}\right\rfloor-1
=\left\lceil\frac{L+1}{r+1}\right\rceil
-\left\lfloor\frac L{r+2}\right\rfloor-1,
\]

since \(\lceil L-L/(r+2)\rceil=L-\lfloor L/(r+2)\rfloor\) and \(\lfloor L-(L+1)/(r+1)\rfloor=L-\lceil(L+1)/(r+1)\rceil\). This proves the all-coefficient identity (3). The two words differ at their first interior zero, so they are genuinely different for every \(r\). QED.

**Smallest example** \(r=1,m=6\):
\[
u_1=010110,\qquad v_1=011010,\quad
(\alpha,\beta)=(1/2,2/3),\quad (U,V)=(1,0).
\]
Both count sequences equal \(\lceil(L+1)/2\rceil-\lfloor L/3\rfloor-1\).

## Exact verification

The separate \`R154C_check.py\` reconstructs each word independently from its bits, enumerates **every factor length** and computes the exact endpoint fractions, then reconstructs \(U,V\) independently from all prefix sums. For \(r=1,\ldots,50\), all 50 distinct pairs match (2). It checks \(L=1,\ldots,2(r+1)(r+2)+1\) against (3), totaling **93,750 exact count checks**, all passing. Output in \`R154C_verification.json\`. Computation uses \`fractions.Fraction\` and integer arithmetic only, no floating approximation. Verification is finite corroboration; the theorem's infinite scope is the symbolic factor/count argument above.

## Research interpretation and remaining questions

R154B proved: *equal* interior reduced endpoint denominators occur among actual words **only** for even-length alternating pairs. R154C shows the unequal-denominator sector also has actual aliases; therefore a downstream observer wanting **word identity** needs an explicit provenance/word-structure residual beyond just \((\alpha,\beta,U,V,C(K))\). R153.1 remains valid: for unequal denominators, the full increment waveform does determine the **cut residue pair**; no contradiction, because (2) uses the same cuts for both distinct words.

Next scientific problem: characterize the equivalence classes of the map
\[
w\longmapsto(\alpha_w,\beta_w,U_w,V_w)
\]
on genuine finite Sturmian words at fixed length, and find a minimal explicit, future-safe repair coordinate that separates these classes. Study whether the classes have uniformly bounded size or grow, and whether any more general invisible factor rearrangements exist. Separately, R152B's all-length permanent-saturation threshold remains open.

**Status:** independently authored proof, not peer-reviewed (NOT_REVIEWED); no formal Task CLAIM, admitted Result, native X6 transfer, P000 alteration or computational complexity improvement implied.
