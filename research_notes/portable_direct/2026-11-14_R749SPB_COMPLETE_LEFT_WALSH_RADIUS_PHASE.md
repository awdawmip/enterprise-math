# R749SPB — The exact first radius-phase kink on the \(s=3/5\) Walsh slice

Date: 2026-11-14. Classification: AUTHOR_EXACT_NOT_REVIEWED. Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Direct continuation of R749SPA, saved in the same GitHub Draft PR, and R749SOZ at PR #2413. The model is the auxiliary complete compatible 16-atom Walsh family, not an assertion of a native X6/V29/V39 dynamics correspondence.

## Theorem (complete zero-gap interval from the coordinate axis)

Use the same \(K=\mathbb F_2^4\), \(\chi_m(k)=(-1)^{\operatorname{popcount}(k\mathbin{\&}m)}\) and

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3+s\chi_{12}+h\chi_{15}+u\chi_1+v\chi_2+w\chi_4+z\chi_8}{16}
\]

as in the R749SPA manuscript. The source fiber contains *all* nonnegative normalized members of this family. Define the free TV minimax radius \(\rho\) over any 16-atom probability center, the calibrated radius \(\rho^{\rm cal}\) with center constrained to the source fiber, and \(g=\rho^{\rm cal}-\rho\).

**For every real \(t\in[0,2/5]\), at \(s=3/5\),**

\[
\boxed{\rho(t,3/5)=\rho^{\rm cal}(t,3/5)=
\begin{cases}
(1-t)/2,&0\le t\le2/15,\\
(18/5-t)/8,&2/15\le t\le2/5,
\end{cases}
\qquad g(t,3/5)=0.}
\]

One explicit compatible optimal center is \(q_t=p_{t,3/5,H(t),0,0,0,0}\), where

\[
\boxed{H(t)=
\begin{cases}
0,&0\le t\le2/15,\\
1/5-3t/2,&2/15\le t\le1/5,\\
(t-2/5)/2,&1/5\le t\le2/5.
\end{cases}}
\]

Thus the exact minimax radius has a genuine **slope change at \(t=2/15\)**, from \(-1/2\) to \(-1/8\), while the calibration gap remains zero on both sides. The value at the junction is \(13/30\); all three center formulas meet continuously. The present new part is \(0\le t\le2/15\); R749SPA proves the adjacent two pieces at the identical frozen input.

## Exact source-pair lower certificate on the new left interval

Take the two explicit compatible laws used in R749SPA,

\[
P_+(t)=p_{t,3/5,0,t,t,1-t,3/5},\quad
P_-(t)=p_{t,3/5,0,-t,-t,t-1,-3/5}.
\]

Their sixteen atom masses are affine in \(t\) and nonnegative at both endpoints \(t=0\) and \(t=2/15\). Therefore they are nonnegative for every intermediate real \(t\). Their atomwise difference signs are consistent at both endpoints, including any zero differences. The exact total variation endpoint values are \(1\) and \(13/15\), respectively. Accordingly, on the whole left interval,

\[
\boxed{\operatorname{TV}(P_+(t),P_-(t))=1-t.}
\]

Every probability center must incur worst-case TV at least half this pairwise distance, giving \(\rho(t,3/5)\ge(1-t)/2\).

## Exact calibrated upper certificate

Take the calibrated center \(q_t=p_{t,3/5,0,0,0,0,0}\). It is a probability law because \(t+3/5\le11/15<1\) on the entire left interval. Let \(J\) be the bounded six-dimensional polytope of all \((t,h,u,v,w,z)\) with \(0\le t\le2/15\) satisfying the sixteen full source nonnegativity inequalities.

The risk gap \(\Phi(x)=\operatorname{TV}(p_x,q_t)-(1-t)/2\) is convex in the six-dimensional joint variables: atomwise differences are affine, absolute values are convex and the proposed radius is affine. Thus verifying \(\Phi\le0\) at every vertex suffices for every real source and parameter in \(J\).

The accompanying Python 3 pure-standard-library checker imports the exact Bareiss/Fraction vertex enumerator already published as R749SPA. It changes only the proposed exact radius to \((1-t)/2\), and checks all \({18\choose6}=18,564\) choices of six active constraints (sixteen atom inequalities and two interval endpoints):

| Exact computation | Result |
|---|---:|
| Nonsingular six-facet bases | 9,536 |
| Feasible bases including repetitions | 560 |
| Distinct exact vertices | 76 |
| Vertices with equality | 26 |
| Maximum TV excess above \((1-t)/2\) | **0** |
| Complete standard-library result | **PASS** |

The 76 vertices split into 32 at \(t=0\) and 44 at \(t=2/15\). All source and center laws in the enumeration satisfy exact probability normalization and nonnegativity. This finite calculation together with the compact-polytope convexity argument gives the universal **real-parameter** upper bound, matching the source-pair lower bound. R749SPA supplies the exact proofs for the two right intervals, completing the theorem.

## Interpretation and next frontier

At \(t=2/15\), the active lower-bound source-pair sign pattern changes. The exact radius branches \((1-t)/2\) and \((18/5-t)/8\) meet but have unequal slopes. This is a *radius phase boundary*, not a calibration-gap phase boundary. It demonstrates that a change of active extremal faces can occur without loss of calibrated optimality, a useful BRC signed-branch/provenance distinction.

Run `python R749SPB_LEFT_PHASE_EXACT_CERT.py` in the same directory as `R749SPA_WALSH_REPAIRED_SEGMENT_EXACT_CERT.py` and compare stdout byte-for-byte with `R749SPB_LEFT_PHASE_RESULTS.json`. All source laws retain the original Walsh coefficient family and no information-reducing projection is assumed. Independent mathematical review and native X6/V29/V39 observer-preserving transfer remain open.

**Next problem:** identify exact new optimal centers and matching dual bounds immediately beyond \(t=2/5\), and whether a positive-area zero-gap polygon extends the complete segment. Distinguish loss of the particular center, change of radius formula and the sign of the true calibration gap.
