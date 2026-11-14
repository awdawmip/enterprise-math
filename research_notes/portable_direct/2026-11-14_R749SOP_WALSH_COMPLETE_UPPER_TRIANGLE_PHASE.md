# R749SOP — Complete two-dimensional Walsh minimax phase on the upper parameter triangle

2026-11-14. Author-side exact mathematical result; status **NOT_REVIEWED**. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. The result concerns the auxiliary 16-atom Walsh source/observer model. The native X6/V29/V39 correspondence is a separate, unresolved problem. The locked P000 worldview and provenance obligations are preserved.

Scientific dependencies: the exact entire-line R749SOF theorem, PR #2370 at 9dc5a0242c1b5dcb42fb7101eaea66ba91e727fd, and the seven-coordinate Walsh source family. Related prior area-limited two-dimensional phase PR #2386 (R749SON), and diagonal homothety PR #2388 (R749SOO).

## 1. Model and exact theorem

Let G=F_2^4; chi_j(k)=(-1)^popcount(j&k), A=chi_3, B=chi_12 and C=chi_15=AB. Consider the complete nonnegative normalized family

\[
\mu_{t,s,h,u,v,w,z}(k)=
\frac{1+t A(k)+s B(k)+h C(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}, \quad k=0,\ldots,15.
\]

The fiber F_{t,s} consists of all laws with given retained moments (t,s). Define TV(p,q)=sum_k |p_k-q_k|/2 and

\[
\rho(t,s)=\min_{q\in\Delta_{16}}\max_{\mu\in F_{t,s}}TV(q,\mu),\qquad
\rho^{cal}(t,s)=\min_{q\in F_{t,s}}\max_{\mu\in F_{t,s}}TV(q,\mu),\qquad g=\rho^{cal}-\rho.
\]

**Theorem.** For **all real** 0<=t,s<=1 with t+s>=1, put r=max(t,s) and m=min(t,s). Then

\[
\boxed{\rho(t,s)=
\begin{cases}
(8-5r-3m)/10,&5r-4m\le1,\\
(3-r-2m)/4,&5r-4m\ge1;
\end{cases}}
\]

\[
\boxed{\rho^{cal}(t,s)=
\begin{cases}
(9-6r-3m)/11,&8r-7m\le1,\\
(4-2r-2m)/5,&8r-7m\ge1,\ 3r-2m\le1,\\
(3-r-2m)/4,&3r-2m\ge1.
\end{cases}}
\]

The exact calibration cost is

\[
\boxed{g(t,s)=
\begin{cases}
(2-5r+3m)/110,&8r-7m\le1,\\
(r-m)/10,&8r-7m\ge1,\ 5r-4m\le1,\\
(1-3r+2m)/20,&5r-4m\ge1,\ 3r-2m\le1,\\
0,&3r-2m\ge1.
\end{cases}}
\]

Boundary branches match. Thus g>0 iff 3r-2m<1, and g=0 iff 3r-2m>=1 in this triangle. Full area is 1/2; the two zero-cost triangles together have area 2/5 and the positive-cost region has area 1/10. The global maximum is 1/90, exactly at (t,s)=(5/9,4/9) and its swap.

## 2. Universal affine source-fiber decomposition

Let sigma=mu_{1,1,1,0,0,0,0}; sigma has probability 1/4 at atoms k=0,3,12,15 (the A=B=+1 atoms), and zero elsewhere. For t+s>=1 set alpha=t+s-1 and beta=2-t-s. When beta>0, let a=(1-s)/beta, b=(1-t)/beta. Then a,b>=0, a+b=1. The entire source fiber satisfies

\[
\boxed{F_{t,s}=\alpha\{\sigma\}+\beta F_{a,b}.}\tag{1}
\]

**Proof of the nonnegative common floor.** Index each atom by (A,B)=(epsilon,delta), (chi_1,chi_4)=(xi,eta), each sign independently in {+1,-1}. Its probability numerator is

\[
D_{\epsilon\delta}(\xi,\eta)=
1+\epsilon t+\delta s+\epsilon\delta h+
\xi(u+\epsilon v)+\eta(w+\delta z).
\]

For *every* choice of xi,eta the exact linear identity is

\[
\begin{aligned}
D_{++}(\xi,\eta)-4\alpha
={}&\frac12\sum_{\eta'=\pm1}D_{+-}(\xi,\eta')
+\frac12\sum_{\xi'=\pm1}D_{-+}(\xi',\eta)\\
&+\frac34\sum_{\xi',\eta'=\pm1}D_{--}(\xi',\eta')\ge0.
\end{aligned}\tag{2}
\]

All terms on the right are nonnegative by source legality. Thus each ++ atom has mass at least alpha/4, and the other atoms at least zero. Therefore mu>=alpha sigma coordinatewise. The residual nu=(mu-alpha sigma)/beta is a nonnegative probability law in the same seven-Walsh-coefficient span, with A,B moments ((t-alpha)/beta,(s-alpha)/beta)=(a,b). Conversely each nu in F_{a,b} gives a valid element alpha sigma+beta nu of F_{t,s}. For beta=0 the parameter is (1,1), and the fiber is exactly {sigma}.

The common floor is sharp. On the anti-diagonal a+b=1 take nu=mu_{a,b,0,a,a,b,b}; grouping atoms shows D_{--}=0, D_{+-}=2a(1+xi), D_{-+}=2b(1+eta), D_{++}=2+2a xi+2b eta. In particular one ++ atom has zero mass; translations by 3 and 12 permute the ++ atoms without changing retained moments, showing their exact coordinatewise lower envelope. Other classes also admit zero atoms. Hence the greatest common coordinatewise subprobability law is exactly alpha sigma.

## 3. Common-subprobability minimax scaling lemma

**Lemma.** Let K be a nonempty subset of a finite probability simplex and let w be a coordinatewise nonnegative vector with |w|_1=alpha<1, such that p>=w for all p in K. Write beta=1-alpha and K'={(p-w)/beta:p in K}. Both the unrestricted-probability-decoder and calibrated total-variation Chebyshev radii satisfy

\[
R_{\Delta}(K)=\beta R_{\Delta}(K'),\qquad R_K(K)=\beta R_{K'}(K').\tag{3}
\]

**Proof.** In the calibrated case the bijection p=w+beta p' preserves ratios of all TV distances exactly. In the unrestricted case, start from any decoder q in Delta. Increase every deficient coordinate q_i<w_i to w_i, adding total mass D. Since sum_i(q_i-w_i)=beta>0, the original positive surplus on coordinates q_i>w_i is at least D. Remove total D from these surplus coordinates without going below w. The resulting qtilde lies in Delta, qtilde>=w and for every p in K its L1 distance is no larger: raising deficiencies reduces distance by exactly D, and lowering surplus increases it by at most D. Hence minimax search may be restricted to q>=w, precisely the decoders w+beta q', q' in Delta. Pairwise TV distances scale identically. For nonclosed K replace min/max by inf/sup.

Apply (3) to (1) to obtain for all t+s>=1

\[
\boxed{(\rho,\rho^{cal},g)(t,s)
=\beta\,(\rho,\rho^{cal},g)(a,b),\quad a+b=1.}\tag{4}
\]

## 4. Reduce the whole two-dimensional region to R749SOF

Permuting the two bit pairs exchanges A and B and preserves the model; it is enough to take r=t>=s=m. Put

\[
z=\frac{1+r-2m}{2(1-m)}\in[1/2,1],\qquad\gamma=2(1-m).
\]

For m<1 the same fiber decomposition applied to (z,1/2) gives

\[
(\rho,\rho^{cal},g)(r,m)=\gamma(\rho,\rho^{cal},g)(z,1/2).\tag{5}
\]

Indeed F_{z,1/2}=(z-1/2){sigma}+(3/2-z)F_{a,1-a}, where (3/2-z)=beta/gamma. The scaling factors multiply to gamma. The exact R749SOF line theorem states for all real z in [1/2,1]:

\[
\rho(z,1/2)=
\begin{cases}
13/20-z/2,&z\le3/5,\\(2-z)/4,&z\ge3/5,
\end{cases}
\]

\[
\rho^{cal}(z,1/2)=
\begin{cases}
9/22-(6/11)(z-1/2),&z\le9/16,\\
3/5-2z/5,&9/16\le z\le2/3,\\
(2-z)/4,&z\ge2/3.
\end{cases}
\]

Its source, event-based dual lower bounds and exact seven-Walsh-fiber vertex certificates are in R749SOF (commit and file above). Exact substitution gives z=9/16 iff 8r-7m=1, z=3/5 iff 5r-4m=1, and z=2/3 iff 3r-2m=1. Multiply the two line radii by gamma and simplify: this proves all radii and the gap formula in Section 1 for the full stated **continuum of real parameters**, without sampling.

## 5. Explicit optimal free and calibrated predictors

When r=t>=s=m, predictors are q_{A,B,C}(k)=[1+A chi_3(k)+B chi_12(k)+C chi_15(k)]/16. An optimal free decoder is

\[
A_f=1,\qquad B_f=C_f=
\begin{cases}
(8m-3)/5,&5r-4m\le1,\\
(4m-1-r)/2,&5r-4m\ge1.
\end{cases}
\]

An optimal calibrated decoder has A_c=r, B_c=m and

\[
C_c=
\begin{cases}
(r+17m-7)/11,&8r-7m\le1,\\
(9m-r-3)/5,&8r-7m\ge1,\ 3r-2m\le1,\\
r+m-1,&3r-2m\ge1.
\end{cases}
\]

All are true nonnegative probability laws, obtained by the exact map q(r,m)=(2m-1)sigma+2(1-m)q_SOF(z,1/2). If s>t interchange the A,B coefficients, retaining C. The calibrated centers belong to the original fiber; at (1,1) both are sigma.

## 6. Phase areas and sharp penalty maximum

On the half t>=s, the zero-cost region is the triangle with vertices (3/5,2/5), (1,0), (1,1), area 1/5. Its swapped counterpart is another triangle of area 1/5 meeting it only at (1,1). The full upper parameter triangle has area 1/2, so the zero-cost area is 2/5 and the positive-cost area 1/10.

On the anti-diagonal a in [1/2,1], formula (4) and SOF give

\[
g(a,1-a)=
\begin{cases}
(5-8a)/110,&1/2\le a\le8/15,\\
(2a-1)/10,&8/15\le a\le5/9,\\
(3-5a)/20,&5/9\le a\le3/5,\\
0,&3/5\le a\le1.
\end{cases}
\]

Its maximum is 1/90 uniquely at a=5/9; it may first decrease and then increase, so a monotonicity assumption is unnecessary. Since g(t,s)=beta g(a,b) with beta<=1, the global maximum is 1/90, attained precisely at (5/9,4/9) and (4/9,5/9).

## 7. Verification, evidence and next question

Reproduce the accompanying standard-library Python Fraction/Bareiss program R749SOP_UPPER_TRIANGLE_EXACT_CHECK.py; its actual output is R749SOP_UPPER_TRIANGLE_RESULTS.json. The program checks (2) coefficientwise for every ++ sign pair, tests the sharp common floor, enumerates all 4368 five-facet subsets for each of six nondegenerate representative rational fibers, tests all 16 nonnegative constraints, and reports the exact maximal TV losses of the displayed centers. The tests confirm 17/20/20/20/20/2 fiber vertices for six cases, the single-source endpoint, and all listed exact radii. The universal result follows from the analytic common-floor reduction plus the R749SOF exact real-line theorem; the finite parameter checks serve as reproducible verification of representative instances, not a substitute for that universal argument.

**Contribution.** Prior R749SON proves a subquadrilateral of area 11/50; prior R749SOO proves diagonal affine homothety. The new nonnegative conic relation (2) proves full upper-triangle fiber homothety and reduces an entire two-parameter minimax problem to R749SOF. Author-side exact proof status NOT_REVIEWED. Native X6/V29/V39 causal, branch-provenance and signed-port faithful mapping remain unresolved.

**Next research problem.** Study the complementary triangle t+s<1: find its possible nonzero shared probability floor, optimal center/dual polyhedral fan, and the precise first failure of an SOF-derived predictor. Separately, seek a typed native-event observer that preserves previously unretained Walsh source distinctions and future composition.