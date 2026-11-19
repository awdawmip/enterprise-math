# R284BI — Guarded leading-window compression of the R284BG star-Port scalar

Date: 2026-11-20 (Asia/Shanghai). Author-side proof and exact finite checks. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. Parent scientific pin: R284BG plus R284BH's distinction between raw scalar output and controller magnitude. Independent portable work; not an operational Task or Result.

## Observation interface

For n>=3 and C in {1,...,H}^{n by n}, use the precise R284BG construction: distinct nonnegative quadratic Sidon offsets a_i with a_0=0, A=max a_i, Q=4A+2, R=A+1,
\[
e_i=Q+a_i,\quad d_i=b^{e_i},\quad z_i=b^{R+2a_i}\;(i>=1),\quad S=\sum_i e_i.
\]
Let
\[
y=\det\bigl(\mathrm{diag}(d_i)-C-\sum_{i=1}^{n-1}z_iE_{0i}\bigr).
\]
As established in R284BG, integer y has one known leading digit at power b^S and enough distinct, bounded, balanced digits to recover every entry of C in polynomial bit time. Let L=n n!(1+H)^n and choose odd b>4L+8 ceil(delta)+9, for a prescribed finite absolute error delta>=0.

This note analyzes an **augmented observer interface** in which the measurement source can subtract the known monic term and transmit a rounded leading window, instead of transmitting the original raw determinant y.

## BI1: Exact target-preserving quotient

Define
\[
T=3Q-R+A=12A+5,\qquad K=S-T.
\]
For n>=3, K>=1. From a measurement u=y+epsilon with |epsilon|<=delta, let the **source side** emit the single signed integer
\[
q=\operatorname{round}\left(\frac{u-b^S}{b^K}\right)
\]
(round to nearest; the gap estimate makes tie conventions irrelevant).

Then q equals the integer sum of all nonleading coefficients at exponent k>=K, shifted down by K, and is independent of epsilon. In particular, the original R284BG decoder can read every required coefficient from balanced digits of q: a source digit originally at exponent k=S-h becomes digit at exponent T-h, for the following target deficits
\[
\begin{array}{ll}
h=Q+a_i&\text{baseline missing-one, coefficient }-C_{ii},\\
h=2Q+a_i+a_j&\text{baseline missing-two, coefficient }C_{ii}C_{jj}-C_{ij}C_{ji},\\
h=2Q-R-a_i\ (i>=1)&\text{star coefficient }-C_{i0},\\
h=3Q-R-a_i+a_j\ (i,j>=1,\ i\ne j)&\text{star one-extra-missing, coefficient }C_{i0}C_{jj}-C_{ij}C_{j0}.
\end{array}
\]
Every target h is in [Q,T] and retains its unique R284BG address. Recover C_ii and bidirectional products; recover C_i0>0 from the third family, then C_0i by division, and finally C_ij for nonroot i!=j by the fourth family. Exact divisions and polynomially many coefficient extractions suffice.

**Proof.** Write y=b^S+sum_{k=0}^{S-1} c_k b^k where all aggregated signed digit coefficients have |c_k|<=L. Splitting at K yields
\[
\frac{u-b^S}{b^K}
=\sum_{k=K}^{S-1}c_k b^{k-K}
 + \sum_{k<K}c_k b^{k-K}+\frac{\epsilon}{b^K}.
\]
The last two terms have combined absolute value at most L/(b-1)+delta/b^K<1/2, so rounding returns exactly the displayed upper sum. R284BG's address census proves the four target families lie inside deficits [Q,T] and no unwanted source lands at any target position. Its original reconstruction formulas now apply at shifted addresses. This preserves all matrix entries and the directed Port identity within this explicitly changed output interface. QED.

## BI2: Quadratic-bit transmitted scalar, with scope

Among nonleading terms the least possible deficit is Q, achieved uniquely by -C_00 at deficit Q, since a_0=0 and the first star deficit is greater than Q. Therefore the highest possible nonzero power in q is T-Q=8A+3. For strictly positive integer C, its leading coefficient is -C_00, so
\[
|q|=\Theta(b^{T-Q})
\quad\text{up to constants bounded by the same digit guard},\qquad
\operatorname{bitlen}|q|=\Theta(A\log_2 b)=\Theta(n^2\log b).
\]
The R284BG raw determinant itself requires Theta(n^3 log b) bits (see R284BH). Hence source-side guarded leading-window transmission reduces the communicated one-number bit length by an asymptotic factor Theta(n), while retaining deterministic polynomial-time decoding and the same bounded-noise guarantee.

**Scope and cost.** The ideal raw determinant y remains of cubic-exponent magnitude. This does not lower the native determinant oracle's internal dynamic range, arithmetic precision or the complexity of generating the quotient at the measurement source. The added source-side subtraction, scaling and rounding are part of this observer interface. A receiver that is given only unprocessed y still must receive its full raw length; source-side computation and physical feasibility must be costed separately. Thus BI1/BI2 are exact **communication/readout-interface** results, not a solution to raw-output minimization.

## Exact author-side evidence

Companion checker: research_notes/portable_direct/R284BI_guarded_top_window_checker.py. It uses exact Bareiss integer determinants, balanced coefficient extraction and rational/integer rounding, with delta=7000. It checked all 512 binary 3x3 matrices, plus 40 random binary 4x4, 20 random binary 5x5 and 8 random binary 6x6 matrices. Every one of 580 instances recovered all target coefficients from q and returned the same q under errors +/-7000. PASS.

Representative fixed-parameter bit lengths (n, raw y bits, transmitted q bits): (3,2880,1694-1695), (4,10191,4513-4514), (5,18129,6384-6385), (6,47446,14038-14039). Evidence JSON: research_notes/portable_direct/R284BI_guarded_top_window_verification.json.

P000 and Heartbeat X6 remain intact; the calculation is a typed finite positive-matrix Port observer. Source-side top-window projection has an explicit fiber-constancy proof for the declared future operation, namely recovery of the entire matrix C. No uncontrolled collapsing of signed Port/provenance directions occurs.

## Next

Investigate whether the necessary leading-window operation can be implemented with verified polynomial-time **near-quadratic precision internal arithmetic**, without constructing y in full or invoking a raw determinant oracle; quantify rounding/conditioning and source operation cost. In parallel retain the open unprocessed-raw-output O(n^2) question under the original scalar interface.