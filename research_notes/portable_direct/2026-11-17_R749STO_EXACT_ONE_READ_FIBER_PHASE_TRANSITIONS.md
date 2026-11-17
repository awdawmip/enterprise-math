# R749STO — Exact phase transitions of single-read ambiguity in two frozen five-source pairs

**Date:** 2026-11-17. **Status:** \`AUTHOR_EXACT_NOT_REVIEWED\`. **Frozen scientific input:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. **Direct prior:** [R749STN](https://github.com/awdawmip/enterprise-math/blob/5cc987c78f6c2be29f218f5df471758ffbb6392a/research_notes/portable_direct/2026-11-17_R749STN_SHORT_HORIZON_TWO_TIME_EXACT_SEPARATION.md). This result concerns the auxiliary scalar observer; no native X6 Port/Cell correspondence is asserted.

## Model, observer and quantifiers

The five **labelled** sources have weights \((1,1,2,3,6)\). For each positive integer \(n\), let \(C_n\) count nonnegative integer source tuples whose weighted sum is at most \(n-1\), and \(T_n\) sum their first weight-one coordinate. Set

\[
 S(n)=18n^4+54n^3-345n^2+2070n-16315,\qquad
 Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-\frac{S(n)}{108}.
\]

All nuisance parameters belong to \([-2,2]\); a candidate state retains its parameters over a sequence. At a **single fixed** index \(j\ge0\), write
\[
 F_j(e,d,E,D)=Y_{q+6j}(e,d)-Y_{p+6j}(E,D).
\]
A *single-read collision at index* \(j\) means there exists a legal nuisance quadruple with \(F_j=0\). Its witnesses may differ for different \(j\). Source labels remain distinct in the counting model; their scalar aggregate is explicitly a lossy observer, not the native source-complete carrier.

## New theorems

**Theorem A (perpetual pointwise ambiguity for 73/265).** For every integer \(j\ge0\), there exist \(e,d,E,D\in[-2,2]\) such that
\[
Y_{73+6j}(e,d)=Y_{265+6j}(E,D).
\]
In fact, the minimum of \(F_j\) over the nuisance box is strictly negative and its maximum strictly positive for every \(j\ge0\).

**Theorem B (sharp first-read transition for 77/7859).** For every integer \(0\le j\le22\) and every legal quadruple, \(F_j>0\). The sharp uniform gap over these 23 indices is
\[
 \boxed{\delta_{22}=\min_{0\le j\le22}\min_{[-2,2]^4}F_j
 =\frac{2781963755899710066647}{603273189896095648315920}>0},
\]
attained at \(j=22\) and the nuisance corner \((-2,2,2,-2)\). For **every** integer \(j\ge23\), there exists a legal quadruple for which \(F_j=0\). Thus the first single-read collision index for this pair is exactly 23. At indices 0 through 22, two independently corrupted scalar readouts with absolute errors \(\le\eta\) remain correctly separated whenever \(2\eta<\delta_{22}\).

**Two-read contrast.** R749STN already establishes a two-time separator at indices \(j,2j\) for \((73,265)\) when \(j\ge37\), and \((77,7859)\) when \(j\ge1\). Thus an individual late read can admit exact cross-state collisions while two time-separated reads distinguish all legal nuisance quadruples. This theorem does not assert simultaneous multi-index collisions.

## Exact proof

For all relevant \(n\), \(C_n>2\) and \(T_n>2\). Thus \(Y_n\) increases strictly with \(e\) and decreases strictly with \(d\) over the nuisance square. Consequently the exact extrema of \(F_j\) on \([-2,2]^4\) are at two opposite corners:
\[
 L_{q,p}(j)=Y_n(-2,2)-Y_m(2,-2),\qquad
 U_{q,p}(j)=Y_n(2,-2)-Y_m(-2,2),\quad n=q+6j,\ m=p+6j.
\]
The maps are continuous, so \(L<0<U\) implies a collision by the intermediate value theorem on a continuous path between corners. Strict \(L>0\) implies universal separation.

The rational generating functions, inherited from R749STN, are
\[
\sum_{n\ge1}C_nz^{n-1}=\frac1{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{n\ge1}T_nz^{n-1}=\frac{z}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
Thus, for each fixed residue class \(n\bmod6\), \(C_n\) and \(T_n\) are exact quasi-polynomials of degrees at most 5 and 6. Exact interpolation from 6 and 7 consecutive evaluations, respectively, determines the whole progression, not just a finite fit.

Clear the positive denominators:
\[
 A_{q,p}(j)=108(C_n+2)(C_m-2)L_{q,p}(j),\quad
 B_{q,p}(j)=108(C_n-2)(C_m+2)U_{q,p}(j).
\]
Exact expansion gives degree-9 polynomials in \(j\). The accompanying exact certificate outputs the **complete ascending rational coefficient arrays**:

* For \((73,265)\), all 10 coefficients of \(-A_{73,265}(j)\) and all 10 coefficients of \(B_{73,265}(j)\) are strictly positive, so \(L<0<U\) for every \(j\ge0\).
* For \((77,7859)\), the 23 exact rational evaluations \(A_{77,7859}(j)\), \(0\le j\le22\), are strictly positive. Dividing by positive denominators and comparing the 23 fractions gives the displayed sharp \(\delta_{22}\).
* Setting \(t=j-23\), all 10 coefficients of \(-A_{77,7859}(t+23)\) and all 10 coefficients of \(B_{77,7859}(t+23)\) are strictly positive. Hence \(L<0<U\) for all \(j\ge23\).

The finite evaluations cover precisely the integer indices where the transition occurs, while positive coefficients in \(t\ge0\) prove the infinite half-line.

## Reproduction and evidence

Run \`python R749STO_ONE_READ_FIBER_PHASE_CERT.py\` using Python 3 with SymPy. The program builds exact five-source integer counts, derives degree-certified residue-class polynomials, tests the cleared numerator at four indices for each pair, checks 40 positive polynomial coefficients and 23 exact finite values, and regenerates \`R749STO_ONE_READ_FIBER_PHASE_RESULTS.json\` with all rational coefficients. Author-side execution on 2026-11-17: **PASS**; regenerated JSON SHA256: \`7b6eacec7363af5918fe614e773143f73806e03407ebee06e6816ddb3f0fb4c2\`. Independent off-interpolation count checks are diagnostic; the quasi-polynomial degree is the universal interpolation justification. Evidence level: \`AUTHOR_EXACT_NOT_REVIEWED\`.

**Future questions:** Find the earliest uniformly separating two-read schedule for \((73,265)\) without fixing the R749STN linear statistic; classify first pointwise collision indices over congruent pairs; build a provenance-preserving typed BRC observer whose future-operation equivalence realizes the separation.
