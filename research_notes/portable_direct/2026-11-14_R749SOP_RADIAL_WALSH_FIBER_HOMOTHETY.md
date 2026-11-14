# R749SOP — Exact radial source-fiber homothety over the full Walsh parameter triangle

**2026-11-14. Author-side exact proof; NOT_REVIEWED.** Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Builds on R749SOO (Draft PR #2388) and on the zero-gap boundary ray of R749SOI (Draft PR #2380). This is the auxiliary Walsh 16-atom source/observer model, with no implied promotion to native P000/X6/V29/V39 physics.

## Definitions and main theorem

On \(G=\mathbb F_2^4\), write \(A=\chi_3,\ B=\chi_{12},\ C=\chi_{15}=AB\), with \(\chi_m(k)=(-1)^{\operatorname{popcount}(m\mathbin{\&}k)}\). The source law is

\[
\mu_{t,s,h,u,v,w,z}(k)=\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

The fiber \(F_{t,s}\) comprises all nonnegative normalized laws of this form. Let \(\sigma=\mu_{1,1,1,0,0,0,0}\), supported with equal mass \(1/4\) on the four \(A=B=+1\) atoms. For **every real** \(0\le t,s\le1\) with \(t+s\ge1\), put \(\alpha=t+s-1\) and \(\lambda=2-t-s=1-\alpha\).

**Theorem R749SOP.** If \(\lambda>0\), let

\[
T=\frac{1-s}{\lambda},\qquad S=\frac{1-t}{\lambda};
\qquad T,S\in[0,1],\quad T+S=1.
\]

Then the **entire compatible-source fiber** is the exact homothetic copy

\[
\boxed{F_{t,s}=\alpha\{\sigma\}+\lambda F_{T,S}.}
\]

The coefficient \(\alpha=t+s-1\) is the **largest common \(\sigma\)-component** that can be subtracted coordinatewise from *every* source in \(F_{t,s}\).

Let \(\rho(t,s)=\min_{q\in\Delta_{16}}\max_{\mu\in F_{t,s}}\operatorname{TV}(q,\mu)\) be the free minimax radius, and \(\rho^{\mathrm{cal}}(t,s)=\min_{q\in F_{t,s}}\max_{\mu\in F_{t,s}}\operatorname{TV}(q,\mu)\) the moment-preserving calibrated radius. Their exact radial scaling law is

\[
\boxed{\rho(t,s)=\lambda\rho(T,S),\quad
\rho^{\mathrm{cal}}(t,s)=\lambda\rho^{\mathrm{cal}}(T,S),\quad
g(t,s)=\lambda g(T,S).}
\]

At the apex \((t,s)=(1,1)\) one has \(F_{1,1}=\{\sigma\}\) and \(\rho=\rho^{\mathrm{cal}}=g=0\).

Consequently, solving the **one-dimensional boundary fiber family \(T+S=1\)** determines all free and calibrated minimax radii on the **two-dimensional closed triangle** \(t+s\ge1,\ 0\le t,s\le1\). The R749SOO diagonal theorem is the special case \(T=S=1/2\).

## Full source-floor proof

A Walsh state \(k\) is represented by \((a,b,\xi,\eta)=(A(k),B(k),\chi_1(k),\chi_4(k))\in\{\pm1\}^4\), with \(\chi_2=a\xi\) and \(\chi_8=b\eta\). Write the sixteen atom numerators as

\[
16\mu(a,b,\xi,\eta)=1+ta+sb+hab+
\xi(u+av)+\eta(w+bz).
\]

Set \(X_\pm=|u\pm v|\), \(Y_\pm=|w\pm z|\). Nonnegativity of all four \((\xi,\eta)\) atoms within each \((a,b)\) group yields

\[
\begin{array}{ll}
X_++Y_+\le1+t+s+h,&X_++Y_-\le1+t-s-h,\\
X_-+Y_+\le1-t+s-h,&X_-+Y_-\le1-t-s+h.
\end{array}
\]

The last inequality forces \(h\ge t+s-1=\alpha\). The second and third imply

\[
X_+\le1+t-s-h,\quad Y_+\le1-t+s-h,
\quad X_++Y_+\le2-2h.
\]

Therefore **each** of the four \(a=b=+1\) atoms has the exact lower bound

\[
16\mu(+,+,\xi,\eta)\ge
1+t+s+h-X_+-Y_+
\ge\alpha+3h\ge4\alpha.
\]

Equivalently \(\mu(k)\ge\alpha\sigma(k)\) for all 16 atoms (trivial on atoms outside \(\sigma\)'s support). Thus when \(\lambda>0\), \(\nu=(\mu-\alpha\sigma)/\lambda\) is a bona fide probability law in the same seven-character Fourier subspace, with retained \(A,B\) expectations

\[
\frac{t-\alpha}{\lambda}=\frac{1-s}{\lambda}=T,\qquad
\frac{s-\alpha}{\lambda}=\frac{1-t}{\lambda}=S.
\]

This proves \(F_{t,s}\subseteq\alpha\{\sigma\}+\lambda F_{T,S}\). Conversely, every \(\nu\in F_{T,S}\) maps to a nonnegative normalized \(\mu=\alpha\sigma+\lambda\nu\in F_{t,s}\), proving equality. For \(\lambda=0\), \(t=s=1\) and the pointwise floor plus unit total mass force \(\mu=\sigma\).

**Sharpness.** On \(T+S=1\), the explicit compatible law

\[
\nu_*=\mu_{T,S,0,-T,-T,-S,-S}
\]

is nonnegative: its four group inequalities are saturated (at \((a,b)=(-,-)\), all values vanish; at the other groups the Walsh baseline equals the sum of character amplitudes). At \(k=0\), where \(A=B=+1\), it has \(\nu_*(0)=0\). Hence the mixed source \(\mu_*=\alpha\sigma+\lambda\nu_*\) satisfies \(\mu_*(0)=\alpha/4\). No larger uniform \(\sigma\)-coefficient is possible.

## Minimax scaling, including the simplex restriction

For the calibrated radius, the affine bijection \(F_{T,S}\to F_{t,s}\) scales all TV distances by exactly \(\lambda\) and maps admissible calibrated centers bijectively, so \(\rho^{\mathrm{cal}}(t,s)=\lambda\rho^{\mathrm{cal}}(T,S)\).

For the free radius one must account for the decoder constraint \(q\in\Delta_{16}\). First, in the affine hyperplane \(H=\{q\in\mathbb R^{16}:\sum_k q_k=1\}\), the minimum enclosing TV radius of *any subset of the simplex* equals its minimum over \(q\in\Delta_{16}\). Indeed, for any signed \(q\in H\), set all negative coordinates to zero (improving its L1 distance to every nonnegative probability vector by the total negative mass \(n\)) and subtract exactly \(n\) nonnegative mass from its positive coordinates, without making any coordinate negative. The second modification increases L1 distance to any probability vector by **at most** \(n\). The resulting \(q^\sharp\in\Delta_{16}\) satisfies \(\|q^\sharp-p\|_1\le\|q-p\|_1\) simultaneously for every \(p\in\Delta_{16}\). Thus allowing signed mass-one centers cannot improve the minimax objective.

The affine homothety \(q\mapsto\alpha\sigma+\lambda q\) acts bijectively on \(H\) and rescales TV by \(\lambda\); hence the unconstrained \(H\)-minimax radius rescales exactly. Apply the projection lemma at both ends to obtain \(\rho(t,s)=\lambda\rho(T,S)\). Subtraction gives the gap scaling.

## Exact consequences, replication and open questions

For \(t+s\ge1\) with \(3t-2s\ge1\), one has \(T\ge3/5\). The R749SOI boundary zero-gap formula \(\rho(T,1-T)=\rho^{\mathrm{cal}}(T,1-T)=(1+T)/4\) and the radial theorem give

\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{3-t-2s}{4},\quad g(t,s)=0.}
\]

This independently recovers the zero-gap triangle from R749SOI and the zero side of R749SON. Along the diagonal \(t=s=r\ge1/2\), \(T=S=1/2\), reproducing R749SOO exactly: \(\rho=4(1-r)/5\), \(\rho^{\mathrm{cal}}=9(1-r)/11\) and \(g=(1-r)/55\). In particular, the full triangle splits into rays of fixed boundary gap sign and linearly varying gap amplitude. The precise one-dimensional boundary gap for \(0<T<3/5\) is the remaining discriminating problem.

The standard-library Python \`R749SOP_RADIAL_WALSH_FIBER_EXACT_CHECK.py\` and corresponding \`R749SOP_RADIAL_WALSH_FIBER_RESULTS.json\` provide an exact rational witness census (36 parameter pairs; 105 inverse/mixing witness checks; 35 sharp shared-core checks), with \`Fraction\` and no floating point. The proof's universal real-parameter quantifiers are discharged by the algebraic inequalities and affine argument above; finite checks cover the declared rational grid.

**Status:** AUTHOR_EXACT_NOT_REVIEWED. The native six-dimensional X6 P000, native three-dimensional slice, triadic dynamics, residual-fidelity obligations, and source/port preserving X6/V29/V39 bridge are unchanged. Next: solve the exact boundary source-fiber minimax problem on \(T+S=1\), or obtain tight piecewise bounds separating positive gap from the zero-gap sector; preserve explicit source distinction in any future native transfer.
