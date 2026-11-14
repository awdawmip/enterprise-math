# R749SOH — A two-dimensional exact Walsh fiber-diameter witness

**Date:** 2026-11-14. **Scientific status:** author-side analytic lemma; NOT_REVIEWED. 
**Scientific input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
**Model:** the 16-state Walsh source fiber in R749SOF and R749SOG, with \(A=\chi_3\), \(B=\chi_{12}\), \(C=\chi_{15}=AB\), and free total-variation minimax radius \(\rho(t,s)\).

## Exact lemma

For **all real** \(t,s\) satisfying

\[
0\le s\le t\le1,\qquad t+s\ge1,
\]

there are two explicitly constructed compatible laws whose total variation distance is exactly

\[
\boxed{\operatorname{TV}(\mu_+,\mu_-)=\frac{3-t-2s}{2}.}
\]

Consequently, the free and calibrated radii satisfy

\[
\boxed{\rho^{cal}(t,s)\ \ge\ \rho(t,s)\ \ge\ \frac{3-t-2s}{4}.}
\]

By exchanging the two Walsh blocks, the symmetric bound applies when \(t\le s\), yielding the unified formula

\[
\boxed{\rho(t,s)\ge\frac{3-\max(t,s)-2\min(t,s)}{4}}
\quad (0\le t,s\le1,\quad t+s\ge1).
\]

This is a **lower bound**, not a claim that the free radius equals the expression throughout the triangle.

## Proof

Use the usual Walsh-law coefficients \(h,u,v,w,z\), and take

\[
h=t+s-1,\qquad
(u,v,w,z)=\pm(1-s,1-s,1-t,1-t).
\]

Let \(x=\chi_1(k)\), \(y=\chi_4(k)\) in a fixed sign block \(A=a\in\{\pm1\},B=b\in\{\pm1\}\).
Then \(\chi_2=ax,\ \chi_8=by\), and there is exactly one atom for each of the four \((x,y)\) choices in each \((a,b)\) block. The atom's numerator is

\[
P_{ab}\pm(1-s)(1+a)x\pm(1-t)(1+b)y,\quad
P_{ab}=1+ta+sb+(t+s-1)ab.
\]

The four \(P\)'s are

\[
P_{++}=2(t+s),\quad P_{+-}=2(1-s),\quad
P_{-+}=2(1-t),\quad P_{--}=0.
\]

For \(++\), the minimum atom numerator is \(2(t+s)-2(1-s)-2(1-t)=4(t+s-1)\ge0\).
For \(+-\) and \(-+\), the minimum is zero; for \(--\), all atoms are zero.
Thus both source laws are nonnegative and have total mass \(1\) (all nonconstant Walsh characters sum to zero). They retain precisely the specified \(t,s\) and zero first-order moments \(\chi_1,\chi_2,\chi_4,\chi_8\) in the *source family* sense: these four are free **fiber** coordinates, not retained observations. [Correction to wording: the free coordinates are allowed to be nonzero; their selected values are as above.] Both belong to the exact source fiber \(F_{t,s}\).

Put \(a_0=1-s\), \(b_0=1-t\). Since \(a_0\ge b_0\ge0\), the absolute source-difference sums over the four blocks are

\[
\begin{array}{c|cccc}
(A,B)&(+,+)&(+,-)&(-,+)&(-,-)\\
\hline
\sum_{\text{four atoms}}|\mu_+-\mu_-|&a_0&a_0&b_0&0.
\end{array}
\]

Indeed the \(++\) sum is
\(\frac14\sum_{x,y=\pm1}|a_0x+b_0y|=\max(a_0,b_0)=a_0\);
the other contributions follow immediately.
Therefore
\[
\operatorname{TV}(\mu_+,\mu_-)
=\tfrac12(2a_0+b_0)=1-s+\tfrac{1-t}{2}
=\tfrac{3-t-2s}{2}.
\]
Every candidate center \(q\) satisfies
\(\operatorname{TV}(\mu_+,\mu_-)\le\operatorname{TV}(\mu_+,q)+\operatorname{TV}(q,\mu_-)\).
Its worst-case radius is at least half this diameter. Taking infima over all free and calibrated centers proves the displayed bounds.

The symmetric statement follows by swapping the two independent Walsh bit pairs (and therefore \(t\) and \(s\)).

## Rational evidence and relationship to prior results

The identity was checked in exact Python \`fractions.Fraction\` at six points: \((1/2,1/2)\), \((13/20,49/100)\), \((7/10,51/100)\), \((1,0)\), \((4/5,1/5)\), and \((3/5,2/5)\). All have valid nonnegative 16-state laws and exact matching distance; the **universal real-parameter conclusion follows from the proof**, not sampling.

This extends the R749SOF diameter witness on \(s=1/2\) and R749SNN on \(t+s=1\) to a single two-dimensional parameter triangle, giving a reusable exact lower certificate for exploring the neighboring zero/positive-gap phase boundary. Independent review and native X6/V29/V39 correspondence remain open.
