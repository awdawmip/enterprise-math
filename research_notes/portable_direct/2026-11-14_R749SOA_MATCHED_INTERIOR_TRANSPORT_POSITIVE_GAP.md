# R749SOA — Matched-interior transport and an enlarged positive Walsh calibration-gap diamond

Date: 2026-11-14. Status: AUTHOR_ANALYTIC_PROOF / NOT_REVIEWED.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Dependencies: R749SNG, PR #2309 @74abff6fff03fb6defec95c6c505c69ea5b0832c; R749SNZ, positive-gap diamond in PR #2357. Auxiliary 16-state Walsh source/observer model; P000 unchanged.

## 1. Full exact statement

Let \(G=\mathbb F_2^4\), with characters \(\chi_m(x)=(-1)^{\mathrm{popcount}(m\mathbin{\&}x)}\).
The source fiber \(F_{t,s}\) consists of all probability laws

\[
\mu(x)=[1+t\chi_3(x)+s\chi_{12}(x)+h\chi_{15}(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)]/16
\]

with free real \(h,u,v,w,z\) making all sixteen masses nonnegative. The remaining retained masks \(5,6,7,9,10,11,13,14\) have zero coefficient. Write \(\rho(t,s)\) for the minimal worst-case total-variation radius when the prediction center is any probability law on \(G\), and \(\rho^{\mathrm{cal}}(t,s)\) when it must lie in \(F_{t,s}\). Put \(g=\rho^{\mathrm{cal}}-\rho\).

**Theorem R749SOA (two strictly positive-gap diamonds).** Every real point with
\(d=|t-\tfrac12|+|s-\tfrac12|\le1/827\) has a nonempty source fiber and satisfies

\[
\boxed{g(t,s)\ge\frac1{110}-3\left(\frac{d}{\frac12-d}+\frac d2\right)\ge\frac1{227425}>0.}
\]

On the nested closed diamond \(d\le1/1652\), the stronger uniform estimate
\(g(t,s)\ge4131/908600>1/220\) holds.

The outer diamond has exact area \(2/683929\). Relative to R749SNZ's certified radius \(1/4455\), its certified area increases by the rational factor \(19847025/683929>29\). The result bounds a strictly positive difference between the two minimax radii; it does not assert exact off-diagonal risk formulas.

## 2. Optimal interior source reference law

For \(0\le t,s<1\), abbreviate \(A=\chi_3\), \(B=\chi_{12}\), so \(AB=\chi_{15}\), and define

\[
r^*_{t,s}(x)=\frac{1+tA(x)+sB(x)+\min(t,s)A(x)B(x)}{16}.
\]

This is a compatible source law. Its four distinct numerators, for \(t\ge s\), are
\(1+t+2s,\ 1+t-2s,\ 1-t,\ 1-t\); thus
\[
\boxed{\min_x r^*_{t,s}(x)=\frac{1-\max(t,s)}{16}.}
\]
The case \(s\ge t\) follows by swapping the two parity blocks. This minimum is optimal among *all* members of \(F_{t,s}\): the entire \(A=-1\) block has total probability \((1-t)/2\), shared by eight atoms, so one of these has mass at most \((1-t)/16\); likewise the \(B=-1\) block has total probability \((1-s)/2\). The best possible smallest atom is therefore at most \((1-\max(t,s))/16\), which \(r^*\) attains.

This maximally interior compatible reference law replaces the product reference \((1+tA)(1+sB)/16\) used in R749SNZ. It is a new extremal-support observation for the same frozen fiber, rather than a new model.

## 3. Matched-interior transport lemma

Let \(p=(t,s)\) and \(p'=(t',s')\) have coordinates in \([0,1)\). Write
\(d=|t'-t|+|s'-s|\) and \(M=\max(t,s,t',s')<1\). If \(d\le1-M\), set \(\epsilon=d/(1-M)\).

Every \(\mu\in F_p\) has the transported law
\[
T_{p\to p'}\mu(x)=(1-\epsilon)\mu(x)+\epsilon r^*_{p}(x)
+\frac{(t'-t)A(x)+(s'-s)B(x)}{16}.
\]
It is normalized because all nonconstant Walsh characters sum to zero; its two known Walsh moments are exactly \(t',s'\), and it creates no forbidden coefficients. Each of its atoms is nonnegative: the first term is nonnegative, the second is at least \(\epsilon(1-M)/16=d/16\), and the third is no less than \(-d/16\). Thus \(T_{p\to p'}\mu\in F_{p'}\), for every \(\mu\), with no assumption about the free five coefficients.

The signed Walsh correction has exact total variation
\[
\frac12\sum_x\left|\frac{\Delta t\,A(x)+\Delta s\,B(x)}{16}\right|
=\frac{\max(|\Delta t|,|\Delta s|)}2.
\]
Indeed \(A,B\) take all four sign combinations, each four times. Since \(\operatorname{TV}(\mu,r^*_{p})\le1\), the triangle inequality yields
\[
\operatorname{TV}(\mu,T\mu)
\le\frac{d}{1-M}+\frac{\max(|\Delta t|,|\Delta s|)}2
\le\frac{d}{1-M}+\frac d2.
\]
The symmetric construction from \(p'\) back to \(p\) has the same bound. Therefore the TV Hausdorff distance of the two compact source fibers is at most \(H=d/(1-M)+d/2\).

## 4. Stability and exact choice of radii

For any nonempty compact probability-source sets \(F,F'\) at TV Hausdorff distance \(H\), let \(R_F(q)=\sup_{\mu\in F}\operatorname{TV}(q,\mu)\). Triangle inequality gives \(|R_F(q)-R_{F'}(q)|\le H\) for every common probability prediction center \(q\), and hence
\[
|\rho(F)-\rho(F')|\le H.
\]
For calibrated predictions, transport an optimal center \(q\in F\) into a center \(q'\in F'\) at TV distance at most \(H\), and match each adversarial \(\mu'\in F'\) to a \(\mu\in F\) within \(H\). Then \(R_{F'}(q')\le R_F(q)+2H\). Interchanging sets proves
\[
|\rho^{\mathrm{cal}}(F)-\rho^{\mathrm{cal}}(F')|\le2H,
\quad |g(F)-g(F')|\le3H.
\]

The exact base theorem R749SNG gives at \(p_0=(1/2,1/2)\)
\[
\rho(p_0)=2/5,\quad \rho^{\mathrm{cal}}(p_0)=9/22,\quad g(p_0)=1/110.
\]
For real \(p\) at \(d=\|p-p_0\|_1\le1/827\), all coordinates are positive and
\(M\le1/2+d\); moreover \(d\le1-M\). The preceding lemma gives
\(H\le d/(1/2-d)+d/2\). The function \(f(d)=d/(1/2-d)+d/2\) is increasing for \(0\le d<1/2\), so the lower bound at the outer boundary is exactly
\[
1/110-3f(1/827)=1/227425>0.
\]
At the inner boundary it is
\[
1/110-3f(1/1652)=4131/908600>1/220.
\]
The Euclidean area of an \(\ell_1\) diamond of radius \(R\) is \(2R^2\); the claimed ratio is therefore exactly \((4455/827)^2=19847025/683929\).

This establishes the theorem on *all real points* in each closed diamond. The rational check is a check of the closed-form constants, not a substitute for the analytic universal proof.

## 5. Reproduction and scope

Run R749SOA_MATCHED_POSITIVE_INTERIOR_EXACT_CHECK.py using Python 3 standard library. Its deterministic stdout is R749SOA_MATCHED_POSITIVE_INTERIOR_RESULTS.json. It uses Fraction throughout, verifies the exact corner-source atom minima and threshold arithmetic, and records that the next larger proposed radius \(1/826\) fails this particular conservative bound. The failure at \(1/826\) does *not* rule out a larger true positive-gap region.

Dependency status: R749SNG is an earlier author-side exact proof with independent review pending; R749SNZ is a previously published author-side continuity argument. R749SOA supplies a strict quantitative improvement without re-enumerating the sixteen-state fiber or changing the frozen science. It creates no shared Task CLAIM and establishes no native X6/V29/V39 event identification.

**Next unresolved problem:** obtain sharper, possibly direction-dependent transport constants using actual feasible fiber diameter rather than TV \(\le1\); then identify the exact two-dimensional zero/positive calibration-penalty transition boundary. Any native X6 interpretation additionally requires a typed observer/future-operation preserving map.