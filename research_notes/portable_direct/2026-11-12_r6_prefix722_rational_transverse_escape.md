# PREFIX-722-R6 — Enlarged rational transverse exclusion and constructive Gamma escape

Date: 2026-11-12 (Asia/Shanghai). Parent: PREFIX-675. Direct predecessor: PREFIX-721-R6. Frozen science reference: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Mathematical scope: auxiliary two-parameter BRC stopping-count / independent Gamma completion-clock observer on \(D=[0,1/2]^2\), not native X6 dynamics. Status: AUTHOR_DERIVED / EXACT_FRACTION_ARITHMETIC_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Input and reused verified frontier

Put \(Y(p,z)=\max(T_p,T_z)\), with the original frozen 189-level stopping-count law and independent conditional Gamma clocks. Let \(\mu=E[Y]\), \(M_2=E[Y^2]\), \(W=M_2-\mu^2\), \(f_t=W-t\mu\), and \(V_q=q^2f_{1/q}\). At \(x_0=11/96\), write
\[
J=\mu_p(M_2)_z-\mu_z(M_2)_p=(z-p)K.
\]
PREFIX-721 supplies the author-certified exact-integer facts
\[
J_z(x_0,x_0)>40{,}800{,}000,\quad
|K(p,z)-J_z(x_0,x_0)|\le B\max(|p-x_0|,|z-x_0|),
\quad B=542610983324712960,
\]
and, within its radius \(r_0=1/14{,}000{,}000{,}000\), \(K>2{,}000{,}000\). The polynomial/Bernstein derivative lemmas give, for every partial derivative of total positive order \(1\le k\le3\),
\[
|D^\alpha\mu|\le \frac N2\,376^k,\qquad
|D^\alpha M_2|\le \frac{N(N+1)}2\,376^k,\quad N=189.
\]
The frozen kernel yields \(\mu_p,\mu_z>0\) in \(\mathrm{int}(D)\). The present work uses these specific published bounds and does not reexecute the 189-row kernel.

## Theorem 1 — A strictly larger exact rational no-maximizer square

Define \(r_1=1/13{,}300{,}000{,}000\). On the full closed square \(S_{r_1}=\{|p-x_0|,|z-x_0|\le r_1\}\), exact rational arithmetic gives
\[
K(p,z)>40{,}800{,}000-\frac{542610983324712960}{13{,}300{,}000{,}000}
=\frac{170445696}{78125}>2000.
\]
The certified radius is larger by the exact factor \(140/133\) (approximately 5.26%); the square area is larger by \((140/133)^2\).

**Proof of exclusion.** For \(p\ne z\), \(\mu_p\mu_z>0\) and stationarity would imply \(J=0\), while \(J=(z-p)K\ne0\). At \(p=z=x\), a stationary point of \(f_t\) has transverse curvature
\[
\left.\frac{d^2}{ds^2}f_t(x+s,x-s)\right|_{s=0}
=2J_z(x,x)/\mu_p(x,x)=2K(x,x)/\mu_p(x,x)>0.
\]
As \(S_{r_1}\subset\mathrm{int}(D)\), no point of the square is a local maximizer of \(f_t\), for any real \(t\); hence it contains no global maximizer of \(V_q\) for any \(q>0\). This is an area improvement for a local continuously certified square; it is **not added** to the inherited 384-by-384 witness-cell tally.

A useful off-diagonal quantitative separation follows on \(S_{r_1}\). Set \(R_p=(M_2)_p/\mu_p\) and \(R_z=(M_2)_z/\mu_z\). Since \(J=\mu_p\mu_z(R_z-R_p)\), \(\mu_p,\mu_z\le35532\), and \(K>2000\),
\[
\max\left(\left|\frac{f_{t,p}}{\mu_p}\right|,
          \left|\frac{f_{t,z}}{\mu_z}\right|\right)
\ge \frac{|R_z-R_p|}{2}
>\frac{1000}{35532^2}|z-p|\quad(p\ne z).
\]
The comparison is independent of \(t\).

## Theorem 2 — A constructive uniform escape at every old-square diagonal stationary point

Let \(0\le t\le1/2\), and let \((x,x)\in S_{r_0}\) be stationary for \(f_t\). Put \(h=10^{-12}\) and \(\Phi(s)=f_t(x+s,x-s)\), defined for \(0\le s\le h\). Then
\[
\boxed{\Phi(h)-\Phi(0)>40h^2=\frac{1}{25{,}000{,}000{,}000{,}000{,}000{,}000{,}000}.}
\]
For \(q\ge2\), \(t=1/q\), the corresponding original objective satisfies
\[
\boxed{V_q(x+h,x-h)-V_q(x,x)>160h^2
=\frac{1}{6{,}250{,}000{,}000{,}000{,}000{,}000{,}000}.}
\]

**Proof.** Along the anti-diagonal, each derivative order \(k=1,2,3\) has the uniform bounds
\[
|\Phi_\mu^{(k)}|\le \tfrac N2(752)^k,\quad
|\Phi_{M_2}^{(k)}|\le\tfrac{N(N+1)}2(752)^k.
\]
The Gamma shape bound gives \(0\le\mu\le2N=378\). Differentiating \(M_2-\mu^2-t\mu\) three times, and using \(t\le1/2<1\), produces the valid uniform bound
\[
|\Phi'''(s)|\le C=N(4N+1)752^3=60{,}843{,}082{,}051{,}584.
\]
Symmetry gives \(\Phi'(0)=0\). The positive exact derivative bound \(\mu_p(x,x)\le N376/2=35532\) and PREFIX-721's \(J_z(x,x)>2{,}000{,}000\) give \(\Phi''(0)>4{,}000{,}000/35532\). Taylor's theorem therefore yields
\[
\Phi(h)-\Phi(0)>
\left[\frac{2{,}000{,}000}{35532}
-\frac{C}{6}\,h\right]h^2>40h^2.
\]
Since \((x,x)\in S_{r_0}\) and \(h<r_0\), the displaced point stays inside \(D\). Finally \(q^2\ge4\). The bound is constructive and uniform in the stationary diagonal location and all \(q\ge2\).

## Reproduction, scope and next discriminating unit

The adjacent \`PREFIX722_R6_EXPLICIT_ESCAPE.py\` performs exact rational assertions, and \`PREFIX722_R6_RESULTS.json\` stores all constants, strict margins and conditions. Local run: \`ALL_CHECKS_PASS PREFIX722-R6\`. It checks the new inequalities using the exact published PREFIX-721 bounds; it does not recompute those source-kernel coefficients. No new witness-grid cell was certified this round, so the previous author tally 139018/147456 is unchanged, and its independent review status is unchanged.

Next: certify tighter local Bernstein bounds for \(K\) in the surviving PREFIX-718 fine-grid cells, compare any resulting exclusions to the existing non-overlapping set, and then isolate potential boundary/global maximizers for PREFIX-675. A distinct Task CLAIM, formal Result, and independent review require their own actual Source authorizations.