# R5 — Exact non-diagonal minimal 5/6 Blackwell supports and a two-parameter 6→5→3 stratification

Date: 2026-11-11 (Asia/Shanghai). Author-side exact theorem and executable rational witnesses; independent Source Result/review pending.

Scientific input **unchanged**: frozen global \`a01383f825ef9d43b4b754254303298c64041568\`; frozen EM \`86149263e38c22292c9def1e0f69092efa1be77e\`. R5 seven-likelihood-ratio P/Q–BRC **auxiliary Blackwell observer**; original 14 physical variables, five physical equalities, 26 capacity slacks, 21 coupling equations and all 30 allowed arcs. This is a theorem of the frozen observer, with no asserted native X6 dynamics transfer.

Predecessor scientific frontier: [#2011](https://github.com/awdawmip/enterprise-math/pull/2011) constructed *diagonal* exact 4/5/6 examples and classified the special E7 face. The present work exhibits **non-diagonal** exact 5/6 examples and a 2D lawful connection to the 3-edge diagonal family. The full physical mass/slack/clock formulae are in the attached \`VERIFY_NONDIA_56.py\`.

## Theorem (closed-form two-parameter support strata)

Use likelihood ratios

\[
(r_0,\ldots,r_6)=(1/10,1/2,3/4,1,5/4,3/2,19/10).
\]

Let \(s\in[1/2,1]\) and define

\[
c(s)=\frac{247s}{4076},\quad
u(s)=\frac{13s}{40}+\frac1{80},\quad
w(s)=\frac{3s}{40}+\frac{21}{80}.
\]

Write the source and target physical seven-tuples (in the original \((g,a,b,u,v,w,z)\) order) as

\[
x_s=(1,s,1,u(s),0,w(s),0),\qquad
y_s=(1,s,1,u(s)-c(s),2c(s),w(s)-c(s),s/10).
\]

The transport \(E_s\) has positive arcs and weights

\[
\begin{array}{c|c}
(i,j)&E_{ij}\\ \hline
(0,0)&m_0(x_s)\\
(1,3)&c(s)\\
(2,2)&(1-s)/2\quad\text{(present only for }s<1)\\
(3,3)&m_3(y_s)\\
(5,3)&c(s)\\
(6,6)&m_6(x_s)
\end{array}
\]

where \(m\) is the model's exact seven-point mass map. The indices follow the frozen operator: \(i\) denotes a **target** likelihood index, \(j\) a **source** index.

Put

\[
d=(1,1,1,27/80,1/10,27/80,1/10),\quad
p_3=(d,d),
\]
and let \(E_3\) be the three-edge diagonal coupling of \(m(d)\) with itself on \((0,0),(3,3),(6,6)\).

For \(0\leq t\leq1\) set

\[
P_{s,t}=(1-t)(x_s,y_s)+t(d,d),\qquad
F_{s,t}=(1-t)E_s+tE_3.
\]

Every \(P_{s,t}\) satisfies the **original five physical equalities and 26 capacity inequalities**; \(F_{s,t}\) is an exact nonnegative solution of the **original 21 Blackwell coupling equations** on the original 30 allowed arcs.

The **global** minimum positive coupling support satisfies the exact stratification

\[
\boxed{N_{\min}(P_{s,t})=
\begin{cases}
6,&1/2\leq s<1,\;0\leq t<1,\\
5,&s=1,\;0\leq t<1,\\
3,&1/2\leq s\leq1,\;t=1.
\end{cases}}
\]

Consequently, the frozen model has continuous *non-diagonal* families of globally minimal 5- and 6-edge transfers. In particular, there are explicit continuous 6→3 and 5→3 support jumps on physical paths.

## Proof

1. **Exact physical and mass identities.** The source satisfies \(g_x=b_x=1\); the target satisfies \(g_y=1,z_y=a_y/10\). Decreasing target \(u,w\) by \(c\) and raising target \(v\) by \(2c\) preserves **both** model clock readings exactly. The source has \(m_1=m_4=m_5=0\). Its target has \(m_4=0\), \(m_2(x_s)=m_2(y_s)=(1-s)/2\), and \(m_1(y_s)=m_5(y_s)=c(s)\). The two exact marginal differences for \(m_0,m_6\) coincide and equal
   \[
   m_0(y_s)-m_0(x_s)=m_6(y_s)-m_6(x_s)
    =\frac{1019}{4050}c(s)-\frac{247s}{16200}=0.
   \]
   Since all masses normalize to one, \(m_3(x_s)-m_3(y_s)=2c(s)\). The source-3 moment is balanced because
   \[
   c(s)(r_1-r_3)+c(s)(r_5-r_3)=c(s)(-1/2+1/2)=0.
   \]
   These identities establish all 21 exact coupling equations, including all marginal and martingale rows.
2. **Physical feasibility of the whole parameter interval.** Every original capacity slack and each physical mass is affine in \(s\). The attached rational verifier checks all 26 capacity slacks and all 21 coupling equations at the exact endpoints \(s=1/2,1\), as well as the exact interior point \(s=3/4\). Hence capacity feasibility and equation validity hold throughout \([1/2,1]\) by affinity/convexity; the endpoint lists show \(m_0(y_s),m_3(y_s),m_6(y_s),c(s)>0\) throughout. At \(s<1\), also \(m_2(y_s)=(1-s)/2>0\).
3. **Interpolation.** The original physical equalities, capacity slacks, mass map and coupling operator are affine/linear in the physical pair and \(E\). Thus the convex combination with the verified diagonal \(p_3,E_3\) preserves all constraints for every \(t\in[0,1]\). Target masses at indices 0,3,6 remain positive; indices 1 and 5 equal \((1-t)c(s)>0\) for \(t<1\); index 2 equals \((1-t)(1-s)/2\), positive exactly when \(s<1,t<1\). The target index 4 has zero mass throughout.
4. **Minimality over all 30 arcs.** Any nonnegative coupling must have at least one positive arc **per positive target-marginal row**; distinct target rows require distinct arcs. At each displayed \((s,t)\), the number of positive target masses is exactly 6, 5 or 3 as above, and the explicit \(F_{s,t}\) has exactly that many positive arcs. Therefore the claimed support counts are globally minimal among all 30 arcs, independently of any fixed-edge search.
5. **Additional 5-edge uniqueness.** For \(s=1,t<1\), the only positive source-marginal indices are \(0,3,6\); allowed arcs exiting sources 0 and 6 are only \((0,0),(6,6)\). All other target masses \(1,3,5\) must come from source 3, uniquely fixing \((1,3),(3,3),(5,3)\) and their weights. Thus this entire 5-edge stratum has a **unique** feasible coupling.

## Exact witnesses and checker evidence

At \(s=1\), the physical source and target are

\[
x_1=(1,1,1,27/80,0,27/80,0),\quad
y_1=(1,1,1,22573/81520,247/2038,22573/81520,1/10).
\]

The five strictly positive arc masses, ordered \((0,0),(1,3),(3,3),(5,3),(6,6)\), are

\[
(777/4000,\;247/4076,\;999237/2038000,\;247/4076,\;777/4000).
\]

At \(s=1/2\), the target is

\[
y_{1/2}=(1,1/2,1,2949/20380,247/4076,10993/40760,1/20),
\]

and the six masses ordered \((0,0),(1,3),(2,2),(3,3),(5,3),(6,6)\) are

\[
(3671/36000,\;247/8152,\;1/4,\;7630501/18342000,\;247/8152,\;2057/12000).
\]

The attached \`VERIFY_NONDIA_56.py\` is designed as a standalone exact \`fractions.Fraction\` verifier. Local execution of its same complete expressions checked \(s=1/2,3/4,1\), the diagonal endpoint, and \(t=0,1/4,1/2,3/4,1\) at each \(s\). \`EXACT_OUTPUT.txt\` retains the complete observed local stdout; finite samples are evidence and the full continuum follows from the explicit affine/convex identities in the proof.

## BRC interpretation and scope

The transport uses nonnegative *branch masses with labeled source/target ports*; the observer only retains the marginal and likelihood-ratio moment constraints. The non-diagonal source-3 branch splits into target ports 1 and 5 at equal weight, preserving its conditional moment exactly. The separate target-index occupancy count is sufficient to certify global minimum support for this family. Path/branch labels remain explicit; no native spatial/time or physical X6 theorem is asserted.

## Next mathematical unit

Find a lawful **non-diagonal 4-edge** instance, or give a global exact infeasibility certificate for the finite original 30-arc family (including supports with two independent branch pairs). Numerical exploration on 405 four-arc patterns consisting of one balanced offdiagonal pair plus two diagonal arcs found none, but this limited numerical search is **not** a global 4-edge no-go claim. Another useful question: characterize when the target-support lower bound is saturated for all admissible non-diagonal families.

Formal R5 task publication/CLAIM is not established by these author-side notes. Independent mathematical review and canonical Result admission remain pending.