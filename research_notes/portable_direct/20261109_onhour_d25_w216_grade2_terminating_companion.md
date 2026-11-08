# D25: Original W216 third-digit grade-2 tail — terminating hypergeometric companion

2026-11-09, Asia/Hong_Kong. TASK_RESEARCH author-side exact theorem, independent arithmetic regression; **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. Original task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, immutable science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Continues earlier source crosswalk and W/V proof-target reduction; accepted D24 and older scans remain consumed.

## Exact theorem, every prime p=6m+1>3

Keep the unchanged full 216 series:
$$
C_n=\binom{2n}{n}^{2}\binom{3n}{n}=\frac{(2n)!(3n)!}{(n!)^5},
\qquad
W_p=\sum_{n=0}^{p-1}(6n+1)C_n216^{-n}.
$$
For the **binomial coefficient** (not the additionally weighted term), the exact p-adic grades on \(0\le n<p\) are
$$
v_p(C_n)=
\begin{cases}
0&0\le n\le2m,\\
1&2m+1\le n\le3m,\\
2&3m+1\le n\le4m,\\
3&4m+1\le n\le6m.
\end{cases}
$$
In particular the full original grade-2 contribution is
$$
\mathcal T_{2,p}=\sum_{n=3m+1}^{4m}(6n+1)C_n\,216^{-n}.
$$
In \(\mathbf F_p\), define the unit and a terminating hypergeometric sequence
$$
K_p=\frac{(3m+2)!}{((3m+1)!)^5}216^{-(3m+1)},
\qquad
U_j=\frac{(1)_j(5/6)_j(7/6)_j}{(3/2)_j^3\,2^j}\quad(0\le j<m).
$$
All denominators are p-units. Since \(7/6\equiv1-m\pmod p\), the numerator naturally terminates at \(j=m\) in characteristic p. The resulting **uniform exact identity** is
$$
\boxed{\frac{\mathcal T_{2,p}}{p^2}
\equiv K_p\sum_{j=0}^{m-1}(6j+4)
\frac{(1)_j(5/6)_j(7/6)_j}{(3/2)_j^3\,2^j}
\pmod p.}
$$
This directly expresses the missing third-digit layer of the original D25 216 sum; it is not a change of the frozen cutoff.

## Proof

For \(n=3m+1+j,\ 0\le j<m\), write
\(2n=p+(2j+1)\) and \(3n=p+(3m+2+3j)\).
Wilson's theorem gives \((p+r)!/p\equiv-r!\pmod p\) for \(0\le r<p\). Hence
$$
\frac{C_n}{p^2}
\equiv
\frac{(2j+1)!\,(3m+2+3j)!}{((3m+1+j)!)^5}\pmod p,
\quad6n+1=3p+6j+4.
$$
The \(j=0\) factorial term times \(216^{-(3m+1)}\) is precisely \(K_p\).
Successive normalized factorial terms have ratio
$$
\frac{(2j+2)(2j+3)
(3m+3+3j)(3m+4+3j)(3m+5+3j)}
{216(3m+2+j)^5}
\equiv
\frac{(j+1)(j+5/6)(j+7/6)}{2(j+3/2)^3}\pmod p.
$$
This is \(U_{j+1}/U_j\) and proves the identity term-by-term.
The grade-3 tail \(n\ge4m+1\) vanishes modulo \(p^3\).

## Exact original p=373 certificate and cross-grade obstruction

For \(p=373,\ m=62,\ p^3=51895117\), exact integer computations yield
$$
K_{373}=290,\quad\sum_{j=0}^{61}(6j+4)U_j=217,\quad
K_{373}\cdot217\equiv266\pmod{373}.
$$
Thus
$$
\boxed{\mathcal T_{2,373}\equiv266\cdot373^2
=37008314\not\equiv0\pmod{373^3}.}
$$
For comparison, the separately source-labelled original coefficients of
\(V_p=\sum_{n=0}^{p-1}(8n+1)\binom{4n}{2n}\binom{2n}{n}^2/2304^n\)
give the following exact valuation-grade residues modulo \(51895117\):

| original series | grade 0 | grade 1 | grade 2 | grade >=3 |
| --- | ---: | ---: | ---: | ---: |
| W216 | 28094360 | 38687933 | 37008314 | 0 |
| V2304 | 45069217 | 6826273 | 0 | 0 |

Both totals are 373 modulo \(373^3\), but grade 2 differs by \(37008314\). This is a **strict counterexample to an attempted grade-by-grade W-to-V third-digit matching**. A full W/V transformation has to transfer contributions across grades. Earlier Guo–Zudilin full/half \(V\bmod p^3\) is consumed, not re-proved here.

## Checks and continuation

The separately executed original-binomial checker agrees with the companion formula for 18 primes:
\(7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373\).
An exhaustive sieve of all 611 primes \(p\equiv1\pmod6\), \(p\le10000\), finds zero vanishing companion values. This is a finite observation only.

Proof reproducer: `research_notes/portable_direct/d25_w216_grade2_companion_20261109.py`.
Raw output: `research_notes/portable_direct/d25_w216_grade2_companion_results_20261109.json`.

**Next exact research unit:** test finite-field hypergeometric transformations of the terminating \(U_j\) sum against the lower two valuation grades and the already proved 2304 full sum. A verified cross-grade cancellation identity would address the unresolved \(W_p-V_p\bmod p^3\) and original \(\Delta_p-R_p\) target; the 611 nonvanishing cases independently refute any blanket policy of discarding W grade 2.

**Distinct native benchmark:** #1559 still requires the source-pinned original p=373 H0/B0 divided-power \([X]U\bmod139129\), real module rank, semilinear orientation/eta, signed Green/Hesse \(\kappa\), original \(\Delta-R\) and independent reproducer. In this run the native gateway rejected status/capabilities/recovery with `BACKEND_IDENTITY_CHECK_UNAVAILABLE; operation_sent=false`. Historical source-issued Researcher `EM-ENTERPRISE-4DEB43`, session `MCP-ecbfd1c046864bb3bff1a2e04c87d207`, activity `RA-9553E027FD14223807511263` are provenance; there is no verified current winning claim, native checkpoint or Result.

The BRC/source valuation decomposition is an auxiliary external arithmetic representation that retains exact coefficients, signed weights, cutoffs and observer provenance; it does not assert a new native X6 isomorphism.
