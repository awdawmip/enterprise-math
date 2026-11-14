# R749SOG — Positive-gap two-dimensional collar approaching the exact transverse transition

**Date:** 2026-11-14. **Status:** author-side analytic proof, exact-rational computational checks; **NOT_REVIEWED**.

**Frozen scientific input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
**Dependencies:** R749SOF at PR #2370, scientific commit 9dc5a0242c1b5dcb42fb7101eaea66ba91e727fd (exact transverse minimax phases), and R749SOA (the maximal-minimum-atom interior source). This note reuses their exact defined 16-state auxiliary Walsh source observer.

## Model and result

Let \(G=\mathbf F_2^4\), \(\chi_m(k)=(-1)^{\mathrm{popcount}(m\mathbin{\&}k)}\), \(A=\chi_3\), \(B=\chi_{12}\), and \(C=\chi_{15}=AB\). Define the full source fiber

\[
F_{t,s}=\left\{\mu_{t,s,h,u,v,w,z}(k)=
\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}\ge0,\quad k=0,\ldots,15\right\}.
\]

For total variation, write the free circumradius \(\rho(t,s)=\inf_{q\in\Delta_{16}}\sup_{\mu\in F_{t,s}}\mathrm{TV}(q,\mu)\), the calibrated circumradius \(\rho^{cal}(t,s)=\inf_{q\in F_{t,s}}\sup_{\mu\in F_{t,s}}\mathrm{TV}(q,\mu)\), and \(g=\rho^{cal}-\rho\).

From R749SOF, for all real \(1/2\le t<2/3\),

\[
G(t):=g(t,1/2)=
\begin{cases}
7/220-t/22,&1/2\le t\le9/16,\\
(2t-1)/20,&9/16\le t\le3/5,\\
(2-3t)/20,&3/5\le t<2/3.
\end{cases}
\]

**Theorem.** For every real parameter pair satisfying

\[
\boxed{\frac12\le t<\frac23,\qquad |s-\tfrac12|\le \frac{1-t}{4}G(t),}
\]

the entire two-dimensional collar has a strictly positive calibrated-minus-free minimax gap:

\[
\boxed{g(t,s)\ge \frac{129}{2128}G(t)>0.}
\]

Its exact planar area is \(\boxed{18199/76032000}\). At \(t=3/5\), the result includes \(499/1000\le s\le501/1000\) with \(g(t,s)\ge129/212800\). The certified positive region has nonempty interior and accumulates at the exact transverse zero-gap transition \((2/3,1/2)\).

## Analytic proof

**1. Exact source-fiber transport.** Define

\[
r_{t,s}(k)=\frac{1+tA(k)+sB(k)+\min(t,s)C(k)}{16}.
\]

For \(0\le t,s\le1\), the four equipopulated \((A,B)\) sign classes give \(\min_k r_{t,s}(k)=(1-\max(t,s))/16\).

For two such pairs, put \(d=|t'-t|+|s'-s|\) and suppose \(d\le1-\max(t,s)\). For arbitrary \(\mu\in F_{t,s}\), let \(\alpha=d/(1-\max(t,s))\) and

\[
\Phi(\mu)(k)=(1-\alpha)\mu(k)+\alpha r_{t,s}(k)
 +\frac{(t'-t)A(k)+(s'-s)B(k)}{16}.
\]

Here \(0\le\alpha\le1\). Each atom of \(\alpha r\) is at least \(d/16\), which cancels the possible negative correction; thus \(\Phi(\mu)\ge0\). The total mass remains one; the \(A,B\) Walsh moments become \(t',s'\), and all retained zero moments stay zero. Hence \(\Phi(\mu)\in F_{t',s'}\).

Because the four \(A,B\) sign pairs occur four times each,

\[
\begin{aligned}
\mathrm{TV}(\mu,\Phi(\mu))
&\le\alpha\mathrm{TV}(\mu,r_{t,s})+
\frac1{32}\sum_{k=0}^{15}|(t'-t)A(k)+(s'-s)B(k)|\\
&\le\alpha+\frac12\max(|t'-t|,|s'-s|).
\end{aligned}
\]

If the reverse transport is also admissible, the Hausdorff distance of the two fibers obeys

\[
H\le\max\left(\frac d{1-\max(t,s)},\frac d{1-\max(t',s')}\right)
+\frac12\max(|t'-t|,|s'-s|). \tag{1}
\]

**2. Radius stability.** For two compact nonempty fibers at total-variation Hausdorff distance \(H\), the free minimax radius changes by at most \(H\). For calibrated minimax, moving an admissible center incurs one additional \(H\), hence its radius changes by at most \(2H\). These follow directly from the TV triangle inequality and applying the argument in both directions. Therefore

\[
g(F')\ge g(F)-3H. \tag{2}
\]

**3. Certified collar.** Fix \(t\in[1/2,2/3)\), put \(a=1-t\), \(d=|s-1/2|\), and use \(0<G(t)\le1/100\) from R749SOF. Within the claimed collar,

\[
0\le d\le aG(t)/4\le a/400<a/2.
\]

Both source-to-target and target-to-source constructions apply, because \(\max(t,s)\le t+d\). Thus (1) gives \(H\le d/(a-d)+d/2\). Combine with (2) to obtain the sharper pointwise inequality

\[
\boxed{g(t,s)\ge G(t)-3\left(\frac d{1-t-d}+\frac d2\right).} \tag{3}
\]

From \(d\le aG/4\), \(a\le1/2\), and \(G\le1/100\),

\[
\frac d{a-d}\le\frac{G}{4-G}\le\frac{100}{399}G,\qquad
\frac d2\le\frac1{16}G.
\]

Hence

\[
g(t,s)\ge\left(1-\frac{300}{399}-\frac3{16}\right)G(t)
=\frac{129}{2128}G(t)>0.
\]

All inequalities hold for **every real** parameter in the stated set. The area follows by exact integration of vertical width \((1-t)G(t)/2\) over the breakpoints \(1/2,9/16,3/5,2/3\), yielding \(18199/76032000\).

Near \(t=2/3\), writing \(\varepsilon=2/3-t>0\), the certified half-width is \(\varepsilon/80+3\varepsilon^2/80\); this is an explicit positive inner tangent cone, not a determination of the optimal phase boundary.

## Evidence and next question

Attached source code R749SOG_TRANSVERSE_POSITIVE_COLLAR_EXACT_CHECK.py and JSON results validate the exact fraction identities, area and representative two-way fiber maps. The checker enumerates all \(16\choose5\) active-atom subsets to obtain every vertex of each selected fixed-parameter five-dimensional source fiber; it tests four rational transverse anchors and both collar endpoints. The continuous theorem is established by the analytic argument above using the R749SOF exact transverse theorem, which retains its author-side NOT_REVIEWED status.

**Next discriminating unit:** compute directional derivatives or exact neighboring polyhedral chambers at \((2/3,1/2)\) to locate the genuine \(\{g>0\}\) tangent boundary, comparing it against this certified inner collar. Native X6/V29/V39 event correspondence remains a separate open question.
