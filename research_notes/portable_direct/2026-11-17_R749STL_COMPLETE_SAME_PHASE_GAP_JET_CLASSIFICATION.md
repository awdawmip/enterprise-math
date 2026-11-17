# R749STL — Complete sharp asymptotic jet-depth classification for all same-phase six-step cutoff gaps

Date: 2026-11-17. Evidence: **AUTHOR_EXACT_NOT_REVIEWED**. Frozen auxiliary five-labeled-source scalar model: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Mathematical dependencies: R749STH, R749STI, R749STJ, and R749STK at immutable GitHub commit \`f160b86c98f035ef712778bb495bcd6764d28693\`. This result concerns asymptotic scalar readouts, not physical/native X6 admission.

## Model and exact classification question

For five *distinctly labeled* positive sources \(w=(1,1,2,3,6)\), let
\[
\Omega_n=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le n-1\},\quad
C_n=|\Omega_n|,\quad T_n=\sum_{k\in\Omega_n}k_1.
\]
Define \(S(n)=18n^4+54n^3-345n^2+2070n-16315\) and
\[
Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-\frac{S(n)}{108},\qquad(e,d)\in[-2,2]^2.
\]
The nuisance parameters are fixed throughout each candidate's full observation tail.

For residues \(r=0,\ldots,5\), let \(b=(78,73,74,75,76,77)\). For any two integers \(k\ge0,h\ge1\), set \(q=b_r+6k\), \(p=q+6h\). Compare the same-index tails \(Y_{q+6j}(e,d)\) and \(Y_{p+6j}(E,D)\), expanded at \(x=(6j)^{-1}\to0^+\). Call the largest \(m\) for which the coefficient differences \(a_0,\ldots,a_m\) vanish the **maximal legal coincident asymptotic jet depth**, maximizing over all \((e,d,E,D)\in[-2,2]^4\).

## Main theorem — complete classification (all six residues, all positive gaps)

| Residue \(r\) | Gap \(h=1\) | Gap \(h\ge2\): depth 2 holds | Gap \(h\ge2\): depth 1 holds |
|---:|---:|---|---|
| 0 | 3 | all \(h\ge2\) | none |
| 1 | 3 | \(2\le h\le31\) | \(h\ge32\) |
| 2 | 3 | all \(h\ge2\) | none |
| 3 | 3 | all \(h\ge2\) | none |
| 4 | 3 | all \(h\ge2\) | none |
| 5 | 3 | \(2\le h\le1296\) | \(h\ge1297\) |

Thus every pair of cutoffs in the **same residue class**, separated by a positive multiple of six, has a completely determined maximal asymptotic coincidence depth. The exact transition thresholds are **31 and 1296**. This classification holds simultaneously for every base shift \(k\ge0\) and any fixed legal real nuisance parameters; the witnesses below use exact rational values.

## Uniform symbolic derivation

For each phase set \(q=b_r\), \(p=q+6h\). Use the exact quasi-polynomial generating functions previously proved in R749STH/STI/STK:
\[
\sum_{n\ge1} C_nz^{n-1}=\frac1{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{n\ge1}T_nz^{n-1}=\frac{z}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
Their finite-block coefficient extraction gives rational polynomials for each residue, valid for \(n\ge29\). Expanding exactly in \(x=(6j)^{-1}\) gives \(a_0=0\) and
\[
a_1=720(D-d).
\]
After requiring \(a_1=0\), i.e. \(d=D\), the second coefficient reduces to
\[
\boxed{a_2=4320\left[e-E-h\left(D-\frac{A_r}{34992}\right)\right].}
\]
The six rational coefficients controlling these equations are:

| \(r\) | \(A_r\) | \(B_r\) | \(8A_r+2B_r\) |
|---:|---:|---:|---:|
| 0 | 54027 | 118312 | 668840 |
| 1 | 74412 | 119707 | 834710 |
| 2 | 69363 | 105532 | 765968 |
| 3 | 60588 | 110455 | 705614 |
| 4 | 62019 | 127564 | 751280 |
| 5 | 70092 | 132667 | 826070 |

Solving \(a_1=a_2=a_3=0\) by exact rational linear algebra yields the **complete three-jet algebraic family**, parameterized by the one remaining nuisance coordinate \(D\):
\[
\boxed{\quad d=D,\qquad
e=\frac{(34992h-139968)D-A_rh-B_r}{69984},\qquad
E=\frac{-(34992h+139968)D+A_rh-B_r}{69984}.\quad} \tag{1}
\]
Direct substitution into all three exact coefficients is an identity for every integer \(h\ge1\).

### 1. The unique small-gap enhancement \(h=1\)

R749STK proves, separately in all six phases, that the parameters in (1) admit strictly interior rational solutions when \(h=1\), but the four-jet equations force \(E>2\). Hence \(h=1\) has **exact depth 3** for every residue. This argument reuses that exact dependency and does not need new numerical sampling.

### 2. No gap \(h\ge2\) admits a three-jet match

At \(h=2\), (1) becomes
\[
 e=-D-\frac{2A_r+B_r}{69984},\qquad
 E=-3D+\frac{2A_r-B_r}{69984}.
\]
The necessary legal bounds \(e\ge-2\) and \(E\le2\) force the interval constraints
\[
\frac{2A_r-B_r-139968}{209952}\le D
\le 2-\frac{2A_r+B_r}{69984}.
\]
They can both hold only if
\[
\boxed{8A_r+2B_r\le559872.} \tag{2}
\]
The table shows **all six** values are strictly greater than 559872. Hence \(h=2\) admits no legal three-jet coincidence.

Now let \(h\ge2\). Formula (1) satisfies
\[
e_h+E_h=-4D-\frac{B_r}{34992},\qquad
e_h-E_h=h\left(D-\frac{A_r}{34992}\right).
\]
For fixed \(D\), going from \(h\) to \(2\) leaves the sum unchanged and multiplies the difference by \(2/h\in(0,1]\). Therefore \((e_2,E_2)\) is the convex contraction of \((e_h,E_h)\) around their midpoint. If \((e_h,E_h)\in[-2,2]^2\), then \((e_2,E_2)\in[-2,2]^2\) as well, contradicting the proven \(h=2\) obstruction. This eliminates three-jet coincidence for **every** \(h\ge2\).

### 3. Exact existence and sharp threshold for two-jet matching

The necessary and sufficient two-jet equations are
\[
d=D,\qquad e-E=h\left(D-\frac{A_r}{34992}\right). \tag{3}
\]
Since \(e,E\in[-2,2]\), their difference ranges over the entire interval \([-4,4]\). Equation (3) is solvable with \(D\in[-2,2]\) if and only if
\[
\boxed{h\,\operatorname{dist}\!\left(\frac{A_r}{34992},[-2,2]\right)\le4.} \tag{4}
\]

For \(r=0,2,3,4\), \(A_r/34992\in[-2,2]\), so simply take \(d=D=A_r/34992\), \(e=E=0\), valid for **all** \(h\ge2\). These are rational witnesses.

For \(r=1,5\), \(A_r>69984\), so (4) is equivalent to
\[
h(A_r-69984)\le139968.
\]
At phase \(r=1\), \(A_1-69984=4428\) and \(\lfloor139968/4428\rfloor=31\). At phase \(r=5\), \(A_5-69984=108\) and \(139968/108=1296\). Whenever the inequality holds, choose
\[
d=D=2,\quad e=-\frac{h(A_r-69984)}{69984},\quad E=\frac{h(A_r-69984)}{69984};
\]
the stated inequality is precisely their legality condition. For larger \(h\), no legal two-jet solution exists.

Finally \(a_1=0\) is always possible by selecting \(d=D=0\), so the depth is exactly one where the second coefficient cannot vanish.

### 4. Shift to arbitrary base cutoff \(k\ge0\)

Replacing \(q,p\) by \(q+6k,p+6k\) replaces \(j\) by \(j+k\). In \(x=(6j)^{-1}\) this is the formal substitution \(x\mapsto x/(1+6kx)\), triangular with unit diagonal. Vanishing coefficients through each order, and the leading nonzero coefficient, are invariant. The classification therefore holds for every \(k\ge0\), completing the proof.

## Exact reproducibility, evidence, and continuation

The standalone SymPy checker \`R749STL_ALL_SAME_PHASE_GAP_JET_CLASSIFICATION_CERT.py\` reconstructs all phase quasi-polynomials from the labeled weight generating functions, checks independent dynamic-programming count values for \(29\le n\le240\), derives and verifies formulas (1), (3), the strict inequalities (2), both thresholds and the rational boundary witnesses. Author-side exact execution: **PASS (6/6 phases)**. Its companion JSON preserves the six symbolic branches and conditions. R749STK independently supplies the sharp \(h=1\) four-jet obstruction and witnesses.

This result uses fixed nuisance parameters and exact **asymptotic** scalar observations. The earlier finite-exact-read global bound \(5\le m_*\le11\) is unchanged. An observer-faithful native X6/BRC Port/Cell realization remains an independent research target requiring source labels, path/branch and future-operation permission preservation.

Next question: determine exact late-time lower bounds for the first unavoidable nonzero jet in the \(h\ge2\) families, including the finite absolute precision needed to separate candidates; test whether a minimal source-aware BRC repair coordinate can preserve those distinct future residual orders.
