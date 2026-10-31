# PREFIX-404｜互补144候选定理与全部六项带噪观测的二维纤维归约

**Date:** 2026-11-01. **Status:** AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING.
This is an external auxiliary static three-complex-amplitude five-Port inverse model, **not** native P000 X6, a native three-axis slice, or typed BRC dynamics.

**Frozen sources:** GLOBAL_KNOWLEDGE_V1 main@75711f73714b2cebf8a177ec4ec53912e23acffc; Enterprise Math main@ac48238d40c28c9ad139faa5b0e11cb7defdd8f9. Read global bootstrap/manual, P000, ACTIVE worldview, joint-observer preservation, BRC and portable-research protocols. PREFIX-403 is an author-side, not independently admitted, predecessor.

## Exact model

The original complex matrix is
\[
A=\begin{pmatrix}4&4&0\\0&-4&4\\-5+3i&0&-3+i\\-2-2i&4+4i&2+2i\\-2&0&5+2i\end{pmatrix}.
\]
Its first three rows form an invertible matrix \(A_3\) with determinant \(-32+32i\). After quotienting a common phase under the exact normalization \(I_1=1\), write \(W=A_3Y=(1,u,v)\); the original complex source is recovered as \(Y=A_3^{-1}W\). The five original Ports and two coherent readouts are
\[
I_2=|u|^2,\quad I_3=|v|^2,\quad C_u=|1+u|^2,\quad C_v=|1+v|^2,
\]
\[
I_4=|a_4+b_4u+c_4v|^2,\qquad I_5=|a_5+b_5u+c_5v|^2,
\]
where
\[
(a_4,b_4,c_4)=(5/2+9i/2,3/2+7i/2,4i),\quad
(a_5,b_5,c_5)=(11/4+15i/8,11/4+15i/8,5/4+9i/4).
\]
Every noisy observation is a finite rational closed interval, possibly degenerate.

## Theorem A — exact I2 and Cu, arbitrary noise in I3,Cv,I4,I5

Suppose \(I_1=1\) and \(I_2=j,\ C_u=p\) are **exact rational** values, while \(I_3,C_v,I_4,I_5\) are arbitrary rational closed intervals. Realizability is equivalent to testing **at most 144 explicitly constructible real-algebraic candidate sources**, of coordinate degree at most four over \(\mathbb Q\). A successful candidate reconstructs the original \(Y\); exhaustive failed candidates certify NO.

**Proof.** The exact pair yields
\[
x=(p-1-j)/2,\qquad d=j-x^2,\qquad u=x\pm i\sqrt{d}.
\]
If \(j<0\) or \(d<0\), the answer is NO; otherwise there are at most two \(u\) values, counting a double root once. For fixed \(u\), the four noisy conditions become **four annuli in the complex \(v\) plane**:
\[
I_3=|v|^2,\quad C_v=|v+1|^2,\quad
I_4=16|v-g_4(u)|^2,\quad I_5=(53/8)|v-g_5(u)|^2,
\]
with \(g_4(u)=-(a_4+b_4u)/c_4\), \(g_5(u)=-(a_5+b_5u)/c_5\). Negative upper bounds force NO; nonpositive lower bounds produce no inner hole. Each annulus has at most two boundary circles, hence \(n\le8\) distinct circles after deduplication.

The finite \(I_3\) upper bound makes the feasible intersection compact. If nonempty, maximize \(\operatorname{Re}v\). The maximizer is either a zero-radius boundary center, an extreme left/right point of a single active boundary circle, or an intersection of two different active boundary circles. Otherwise a short arc of the sole active circle would increase the real part while preserving all other strict constraints. Tangencies, zero radii and coincident centers are covered by deduplicating equal circles and skipping distinct concentric circles. The maximum number of candidates per \(u\) is
\[
2n+2{n\choose2}=n(n+1)\le72,
\]
so at most 144 overall. All circle centers belong to \(\mathbb Q(\sqrt d)\), and each circle extreme/intersection adds at most one square root; coordinate degree is at most four. Every candidate is rechecked against the **original labeled observations**, not an unverified eliminant. QED.

This is complementary to PREFIX-403 (which fixes \(I_3,C_v\) and permits noise in \(I_2,C_u\)); **the two statements cannot be combined into a false 144-point global solver with all six noisy**.

## Theorem B — all six noisy: exact 72-candidate parameter-fiber reduction

Suppose \(I_1=1\) is exact and all six \((I_2,C_u,I_3,C_v,I_4,I_5)\) have arbitrary finite rational closed intervals. Define the continuous parameter domain
\[
U=\{u\in\mathbb C:\ |u|^2\in J_2,\ |1+u|^2\in J_u\}.
\]
The entire six-observation record is realizable **if and only if** there exists \(u\in U\) for which at least one of **at most 72 algebraic candidates \(v\in E(u)\)** satisfies the remaining four labeled measurements. These 72 points are *per fixed parameter \(u\)*, not a global finite source population.

**Proof.** The four \(v\)-conditions for a fixed \(u\) are the four annuli from Theorem A. Its compactness/maximal-real-part argument is an if-and-only-if finite test in each fiber. Quantify over all \(u\in U\). Concretely each boundary circle has center \(c_i(u)\) affine in \(u\), rational squared radius \(r_i^2\), and extrema \(c_i(u)\pm\sqrt{r_i^2}\). For two nonconcentric circles put \(d=c_j-c_i,\ D=|d|^2>0,\ t=(r_i^2-r_j^2+D)/(2D),\ h^2=r_i^2-t^2D\). If \(h^2\ge0\), their intersection candidates are
\[
c_i+td\ \pm\ i d\sqrt{h^2/D}.
\]
If \(D=0\), identical circles are deduplicated and nonidentical concentric circles do not intersect. Thus every candidate condition is a semialgebraic sign condition in the **two real parameters \(\Re u,\Im u\)** with at most one additional square-root branch. A complete real-closed-field decision algorithm may decide those two-dimensional parameter branches. This is a **proved two-real-parameter reduction and abstract decidability**, not an executed general planar CAD or an assertion of polynomial bit complexity. QED.

## Exact all-noisy YES/NO with nonzero-width bands

Consider
\[
J_2=J_3=[0,10^{-6}],\quad J_u=J_v=[99/100,101/100],\quad
J_4=[26,27],\quad J_5=[10,12].
\]
**YES with continuum of sources:** every pair \(|u|,|v|\le1/1000\) is feasible, hence a full four-real-dimensional source neighborhood is feasible. The elementary norm bounds
\(|a_4|<6,\ |b_4|<4,\ |c_4|=4\) give the strict \(I_4\) deviation estimate
\[
|\Delta I_4|<12(8/1000)+(8/1000)^2<1/2
\]
about \(I_4^0=53/2\). Similarly \(|a_5|<4, |b_5|<4, |c_5|<3\) give
\[
|\Delta I_5|<8(7/1000)+(7/1000)^2<7/10
\]
about \(I_5^0=709/64\). The other four bands follow from \(|u|,|v|\le1/1000\) and \((1\pm1/1000)^2\in[99/100,101/100]\).

**NO with all six bands still of nonzero width:** retain all five other bands but replace \(J_4\) by \([0,1]\). The first and third intensity upper bounds force \(|u|,|v|\le1/1000\), whereas \(|a_4|>5,\ |b_4|<4,\ |c_4|=4\) imply
\[
|a_4+b_4u+c_4v|>5-8/1000=624/125>1,
\]
contradicting \(I_4\le1\). This NO certificate covers the full continuous error box, not a finite numerical scan.

## Evidence, BRC preservation and next problem

Executed: the exact SymPy complementary-slice solver returns **PASS_PREFIX404_DUAL_144_CANDIDATES_EXACT_U_NOISY_V** for four YES/NO tests including two \(u\) branches and zero-radius circles; an independently implemented standard-library Fraction Gauss–Jordan checker verifies the original \(A(A_3)^{-1}\) identity on three complex basis vectors plus the all-noisy exact YES/NO bounds, returning **PASS_PREFIX404_INDEPENDENT_FRACTION_ALL_NOISY_YES_NO_AND_ORIGINAL_MATRIX**. The mathematics of Theorems A/B is supplied by the proofs, not extrapolated from four tests. The generic two-parameter CAD was **not** executed.

**BRC reuse:** REUSE_APPLIED for preserving complete source fibers, original Port labels, phase and future coherent observers. These witnesses are existence representatives, not a quotient that identifies physically distinct \((u,v,Y)\). No typed BRC computation was performed, and no P000-native bridge is claimed.

**PREFIX-405:** implement an exact two-real-parameter sign decomposition for all 72 parameterized algebraic branches including degeneracies (coincident circles, tangency, zero-radius and endpoint contacts), with explicit YES witness or replayable NO certificate. Analyze solver/certificate complexity separately from mathematical decidability.
