# R749STN — Short-horizon exact two-time separators via positive Bernstein–power coefficients

**Date:** 2026-11-17. **Status:** `AUTHOR_EXACT_NOT_REVIEWED`. **Frozen scientific pin:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Predecessor:** R749STM, [PR #2640](https://github.com/awdawmip/enterprise-math/pull/2640), commit `9589aaabda9ec8d1e604f67c0d0748caeaba4564`. This is an auxiliary scalar observer theorem, not an asserted native X6 Port/Cell mapping.

## Model and separator

Five individually labelled nonnegative coordinates have weights (1,1,2,3,6). Let \(C_n\) count tuples with weighted sum at most \(n-1\), \(T_n\) sum the first weight-one coordinate over them, and

\[
S(n)=18n^4+54n^3-345n^2+2070n-16315,\qquad
Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-S(n)/108.
\]

Each candidate holds its fixed real nuisance pair in \([-2,2]^2\) throughout its tail. Compare \(q\) against \(p=q+6h\); define
\(F_j=Y_{q+6j}(e,d)-Y_{p+6j}(E,D)\). For \(j\ge1\), put \(x=1/(6j)\), \(a=2-(q+27)x\), \(b=-4+4(q+27)x\), and
\[
H_j=aF_j+bF_{2j},\qquad
\widehat J_2=\frac{H_j}{4320x^2}.
\]
This is the same finite sheared two-jet statistic as in R749STM; its coefficients retain their exact signs even for small \(j\).

## Theorem

For **every** \(e,d,E,D\in[-2,2]\):

* If \((q,p)=(73,265)\), then \(H_j>0\) for **every integer \(j\ge37\)**.
* If \((q,p)=(77,7859)\), then \(H_j>0\) for **every integer \(j\ge1\)**.

Thus in these ranges the two candidates can never have both matched observations at \(j\) and \(2j\) equal. The earlier sufficient thresholds \(3,899,747\) and \(44,927,677,740\) in R749STM improve to **37** and **1**.

For the first pair and every \(1\le j\le36\), \(H_j<0\) at \((-2,2,2,-2)\) and \(H_j>0\) at \((2,-2,-2,2)\), so the statistic also vanishes somewhere on a legal connecting segment. Hence \(37\) is the **sharp uniform positive-sign threshold of this specified separator**. Early zero values of this linear statistic do not assert equality of both individual observations.

## Exact polynomial proof

The counting generating functions are

\[
\sum_{n\ge1}C_n z^{n-1}=
\frac{1}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},
\quad
\sum_{n\ge1}T_n z^{n-1}=
\frac{z}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

They give exact degree-5 and degree-6 quasi-polynomials in each residue class modulo 6. Let
\(Q_1=C_{q+6j}+d\), \(Q_2=C_{q+12j}+d\),
\(P_1=C_{p+6j}+D\), \(P_2=C_{p+12j}+D\), and \(\mathrm{Den}=Q_1Q_2P_1P_2>0\). Define
\[
\mathscr P(j,e,d,E,D)=108(6j)\,\mathrm{Den}\,H_j. \tag{1}
\]
Direct exact substitution makes (1) a **polynomial of degree 19 in \(j\)** and multidegree \((1,2,1,2)\) in the four nuisance variables. For \(J_0\in\mathbb N\), substitute \(j=J_0+t\) with \(t\ge0\), and normalize each nuisance variable to \(v=-2+4u\), \(u\in[0,1]\). Then
\[
\mathscr P(J_0+t,-2+4u)
=\sum_{m=0}^{19}t^m
\sum_{\alpha\le(1,2,1,2)}
\beta_{m,\alpha}\prod_{\ell=1}^{4}
B^{n_\ell}_{\alpha_\ell}(u_\ell),
\quad
B^n_k(u)={n\choose k}u^k(1-u)^{n-k}. \tag{2}
\]
Each Bernstein basis function is nonnegative and the tensor basis sums to 1.

The reproducible exact-rational program verifies all \(\beta_{m,\alpha}>0\) for \(J_0=37\) and \((73,265)\): **720 of 720** coefficients, and similarly for \(J_0=8\) and \((77,7859)\): **720 of 720**. The remaining \(j=1,\ldots,7\) of the second pair have **252 of 252** positive Bernstein coefficients computed at those fixed \(j\). Since \(t\ge0\), (2) is strictly positive throughout the full nuisance cube and infinite index half-line. Positivity of \(\mathrm{Den}\) and \(j\) proves the theorem.

The program independently checks 228 integer dynamic-count values against the quasi-polynomials, the cleared numerator against the original \(Y\) formulas at exact rational nuisance points, and the opposite corner signs for **all 36** earlier indices of the first pair. These checks total **1,692 strict-positive Bernstein coefficients**. All comparisons are rational, not floating point and not a sample of the four-dimensional real parameter box.

## Noise at the first certified indices

Let \(m\) be the smallest of the 36 fixed-\(j=J_0\) Bernstein coefficients for \(108\,\mathrm{Den}\,H_j\), and \(\mathrm{Den}_{\max}\) the product of the four \(C_n+2\) bounds. Then
\[
\widehat J_2\ge
\frac{mJ_0^2}{12960\,\mathrm{Den}_{\max}}. \tag{3}
\]
The exact certificate establishes \(\widehat J_2>83/100\) at \(j=37\) for \((73,265)\), and \(\widehat J_2>34/100\) at \(j=8\) for \((77,7859)\).

If all four raw scalar readouts individually incur absolute error at most \(\eta\), the estimator error is at most
\[
|\Delta\widehat J_2|
\le\frac{2\eta(|a|+|b|)}{4320x^2}. \tag{4}
\]
The sign is therefore retained at the respective starting indices when \(\eta\le1/120\) and \(\eta\le1/20\). The exact all-\(j\) theorem is noiseless; apply (3)–(4) for a time-specific bound at subsequent \(j\).

## Reproduction, use and open question

Run `python R749STN_ALL_TIME_TWO_READ_BERNSTEIN_CERT.py` with Python 3 and SymPy; it writes `R749STN_TWO_READ_BERNSTEIN_RESULTS.json` including exact rational bounds, checks, and SHA256 digests of the complete ordered coefficient lists. Digests identify the reproducible outputs; positive-rational checks are the proof.

This supplies a source-fidelity-motivated auxiliary observer repair: a particular linear combination of two time-separated readouts exposes a residual that a single scalar reading can hide. It does not claim an X6 native Cell/Link/Port descent.

**Next:** Determine the earliest two-read index for the pair (73,265) using more general separators or exact semialgebraic feasibility; \(37\) is sharp only for the displayed \(H_j\). Generalize the Bernstein positivity method to arbitrary congruent shifts \(k,h\) with nonzero sheared residual, and separately establish any genuinely source-labelled native BRC mapping.