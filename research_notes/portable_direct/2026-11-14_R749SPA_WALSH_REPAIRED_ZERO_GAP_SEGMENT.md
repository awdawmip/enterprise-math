# R749SPA — Exact repaired zero-calibration-gap segment through the former center obstruction

Date: 2026-11-14. Status: `AUTHOR_EXACT_NOT_REVIEWED`.
Scientific input frozen at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Continuation: R749SOZ in [PR #2413](https://github.com/awdawmip/enterprise-math/pull/2413), immutable source `a5757b24e97e2c7464a852b10a8c24dff1af4f2d`, with prior R749SOX–SOY in [PR #2409](https://github.com/awdawmip/enterprise-math/pull/2409). Auxiliary probabilistic Walsh observer only; native X6 observer fidelity remains a separate question. This artifact is independent portable research and does not assert a shared Task CLAIM, Result, Review, or Foundation promotion.

## 1. Exact model and proposition

Let `K=F_2^4`, `chi_m(k)=(-1)^popcount(k&m)`. Put `A=chi_3`, `B=chi_12`, and `C=chi_15=AB`. The *complete* compatible 16-atom family is

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16},\quad p(k)\geq0\ \forall k.
\]

Let `F_{t,s}` be this family of probability laws. Total variation is `TV(p,q)=sum_k |p(k)-q(k)|/2`. Define `rho(t,s)=inf_{q in Delta_16}sup_{p in F_{t,s}}TV(p,q)`, `rho_cal(t,s)=inf_{q in F_{t,s}}sup_{p in F_{t,s}}TV(p,q)`, and `g=rho_cal-rho`.

**Theorem R749SPA (all real parameters in a complete line segment).** For **every real**

\[
\frac{2}{15}\le t\le\frac25,\quad s=\frac35,
\]

we have

\[
\boxed{\rho(t,3/5)=\rho_{\rm cal}(t,3/5)=\frac{18/5-t}{8}=\frac9{20}-\frac t8,\qquad g(t,3/5)=0.}
\]

The following is an explicit compatible minimax center:

\[
q_t=p_{t,3/5,H(t),0,0,0,0},\qquad
H(t)=\begin{cases}
\frac15-\frac32t,&\frac{2}{15}\le t\le\frac15,\\[2pt]
\frac{t-2/5}{2},&\frac15\le t\le\frac25.
\end{cases}
\]

The two coefficients agree at `t=1/5`: both give `H=-1/10`. This extends the previously established `s=3/5` intersection of R749SOZ's triangle, `6/25<=t<=2/5`, leftwards to `2/15` without changing the exact radius formula. The proven segment length is `4/15` rather than `4/25` (factor `5/3`).

## 2. Two feasible source laws give the exact lower bound

Take

\[
P_+(t)=p_{t,3/5,0,t,t,1-t,3/5},\qquad
P_-(t)=p_{t,3/5,0,-t,-t,t-1,-3/5}.
\]

Every atom of each law is affine in `t`. The attached exact checker establishes all 16 nonnegative probabilities at the endpoints `t=2/15,1/5,2/5`; hence both laws are feasible for every intermediate real `t`. At these three points, it also establishes the signs of the 16 atomwise differences `P_+(t)-P_-(t)` are consistent (zero signs allowed). Therefore every absolute difference is affine on the full segment. Exact endpoint values are

| `t` | `TV(P_+,P_-)` |
|---:|---:|
| `2/15` | `13/15` |
| `1/5` | `17/20` |
| `2/5` | `4/5` |

and so for all real `t` in this segment

\[
\operatorname{TV}(P_+(t),P_-(t))=\frac{18/5-t}{4}.
\]

For any probability center `q`, the triangle inequality yields `max{TV(q,P_+),TV(q,P_-)}>=TV(P_+,P_-)/2`. Thus both unconstrained and calibrated minimax radii are at least `(18/5-t)/8`.

## 3. Exact upper certificates on two joint polytopes

For each of the two intervals `I=[a,b]`, consider all six-tuples `x=(t,h,u,v,w,z)` constrained by `a<=t<=b` and the full **16 source nonnegativity inequalities** with `s=3/5`. The resulting joint source polytope `J_I` is bounded: the 16 probabilities sum to one, and each Walsh coefficient of a probability law lies in `[-1,1]`. It has six-dimensional interior, e.g. choose an interior `t` with `t+3/5<1` and sufficiently small additional coefficients; the second interval also admits such a point `t<2/5`.

For each piece set `q_t` as in the theorem and define

\[
\Phi_I(t,h,u,v,w,z)=\operatorname{TV}(p_{t,3/5,h,u,v,w,z},q_t)-\frac{18/5-t}{8}.
\]

Every atomwise difference is affine in `x`, so `Phi_I` is convex (sum of absolute values minus an affine function). Every point in the compact polytope is a convex combination of its vertices. Consequently it suffices to verify `Phi_I<=0` at **all** vertices of each `J_I`. The two centers are probability laws throughout the segments: their atom masses are affine in `t`, and nonnegativity/normalization is checked exactly at the endpoint coordinates (also checked at every joint vertex).

The attached self-contained Python 3 standard-library script enumerates all `C(18,6)=18,564` active six-facet combinations for *each* interval, solves each nonsingular integer matrix by exact Bareiss elimination and `Fraction` back substitution, checks all 18 inequalities, deduplicates exact rational vertices, and verifies source/center laws and `Phi_I<=0`. The recorded exact outputs are:

| Joint interval | Nonsingular bases | Feasible bases (with multiplicity) | Unique vertices | Tight vertices | Max `Phi_I` |
|---|---:|---:|---:|---:|---:|
| `[2/15,1/5]` | 9,536 | 580 | 78 | 32 | `0` |
| `[1/5,2/5]` | 9,536 | 948 | 54 | 18 | `0` |

Every vertex occurs at the endpoint `t` of the corresponding interval (as the exact result JSON shows), a consequence of the particular fixed-`s` joint-polytope structure. All listed counts are algorithmic evidence that can be checked by rerunning the executable certificate; the proof's finite-to-continuum step is the bounded-polytope convexity argument above. Therefore the explicit *calibrated* centers achieve `(18/5-t)/8` for all real `t`, matching the source-pair lower bound. This completes the theorem.

## 4. Resolving R749SOZ's explicit center obstruction

R749SOZ found that the *old* center `q_0=p_{1/5,3/5,0,0,0,0,0}` fails its triangle radius formula at `(t,s)=(1/5,3/5)`. Its feasible witness

\[
p_*=p_{1/5,3/5,-1/5,0,0,4/5,4/5}
\]

satisfies `TV(p_*,q_0)=9/20>17/40`. The new center `q_1=p_{1/5,3/5,-1/10,0,0,0,0}` instead has **worst-case risk exactly** `17/40` over the complete compatible fiber, with an exact lower matching source-pair diameter `17/20`. Thus the previous witness detects failure of the *particular old center* while the optimal radius and zero-calibration gap persist at this parameter.

This is a concrete BRC-style preservation distinction: the source fiber still carries all four branch masses `M_ab=1+t a+s b+h ab` and internal signed splittings `U_a=u+a v`, `V_b=w+b z`; only the prediction center is changed. No source information is quotient-collapsed in either certificate.

## 5. Reproduction, evidence and continuation

Files: this entire paper, `R749SPA_WALSH_REPAIRED_SEGMENT_EXACT_CERT.py`, and `R749SPA_WALSH_REPAIRED_SEGMENT_RESULTS.json`. Run `python R749SPA_WALSH_REPAIRED_SEGMENT_EXACT_CERT.py` with Python 3 standard library and compare its entire JSON stdout with the saved result. No sampling or floating-point arithmetic enters the certificate. The proof is author-side exact, awaiting independent mathematical review. It is confined to the frozen auxiliary Walsh observer model and makes no native X6/V29/V39 preservation claim.

**Next questions.** Determine whether `t=2/15` is a genuine change point for this radius formula along `s=3/5`, by finding matching optimal lower/upper certificates immediately to its left. Then seek a nonzero-area polygon joining this repaired line segment with the previously proved R749SOZ triangle, using piecewise affine calibrated centers and joint-polytope certificates. Separately study what additional provenance/residual carrier would be needed for faithful transfer to native X6 operations.
