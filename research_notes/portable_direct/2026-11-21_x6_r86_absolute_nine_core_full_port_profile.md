# X6 R86 — 四阶正权 BRC 的全整数格九元最小核心及全 Port 最小候选数定理

Date: 2026-11-21 (Asia/Shanghai).
Status: EXACT_FINITE_AUTHOR_CERTIFICATE + SYMBOLIC_PROOF / NOT_INDEPENDENTLY_REVIEWED.
Mode: independent portable mathematical study; no shared Task CLAIM, canonical Result, review, native dynamics transfer or P000 change.
Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.
Immediate sources: R71 conformal cone lemma, R72 28-vector atlas, R79 nine-term analytic reduction, R84–R85 finite-Port profiles. New independent source: R86 full-domain C++ enumeration, integer bound and Python ray/dominance crosscheck.

## 1. Statement and exact observer domain

This is the **conditional normalized positive-count BRC star histogram** of maximum degree 4, with one unknown additive offset shared by the four readings and arbitrary strictly positive channel precision weights \(w=(A,B,C,D)\). It recovers only the high-degree count histogram \((c_2,c_3,c_4)\), not named native Cell/Link/Port or whole-triad event histories.

For an unoriented nonzero integer difference \(a=(x,y,z)\in\mathbb Z^3\setminus\{0\}/\{\pm 1\}\), define

\[
q(a)=\max\bigl(x^++y^++z^+,(-x)^++(-y)^++(-z)^+\bigr);
\quad Z(a)=(0,2x+6y+12z,6x+24y+60z,14x+78y+252z).
\]
\[
g_{ij}(a)=|Z_i-Z_j|/2,\qquad
F(a;w)=\max_{1\le i<j\le4}\frac{g_{ij}(a)}{w_i+w_j},\qquad
\eta^*_{p,4}(w)=\min_{a\ne0,\ q(a)\le p}F(a;w).
\]

The objective treats \(a\) and \(-a\) as the same direction. The nine candidate vectors are

| Short name | Port requirement \(q\) | Difference \(a=(x,y,z)\) |
|---|---:|---|
| s7 | 7 | (6,-4,1) |
| s10 | 10 | (9,-5,1) |
| s11 | 11 | (10,-5,1) |
| s16 | 16 | (15,-6,1) |
| s27 | 27 | (24,-14,3) |
| s39 | 39 | (36,-16,3) |
| s43 | 43 | (39,-20,4) |
| s49 | 49 | (45,-21,4) |
| s125 | 125 | (114,-56,11) |

**Theorem R86 (absolute nine-core minimality).** For every positive real \(w\), every integer \(p\ge125\), and the full set of all feasible integer difference directions (not merely the historical R72 atlas),

\[
\boxed{\eta^*_{p,4}(w)=\min_{s\in S_9}F(s;w),\qquad
N(p)=9\quad(p\ge125).}
\]

Here \(N(p)\) means the least cardinality of one **fixed** family of feasible unoriented integer differences that attains the true \(\eta^*_{p,4}(w)\) simultaneously for **every** \(w\in(0,\infty)^4\). The new lower bound is absolute: allowing arbitrary vectors outside the R72 28-element atlas cannot reduce nine.

Combining this result with R84, R80–R83 and R85 at their stated scopes gives the complete minimum-cardinality profile for all integers \(p\ge4\):

| Port range | \(N(p)\) |
|---|---:|
| 4 | 5 |
| 5 | 7 |
| 6 | 9 |
| 7–8 | 10 |
| 9 | 11 |
| 10 | 12 |
| 11–15 | 5 |
| 16–42 | 6 |
| 43–48 | 7 |
| 49–124 | 8 |
| 125 and above | **9** |

The profile is for the stated conditional BRC observer. The 4–124 portion inherits the exact predecessor author-side certificates, rather than being newly enumerated here.

## 2. Absolute lower bound: nine exact strict winners against the entire lattice

For each \(s\in S_9\), give a strictly positive integer four-weight \(w_s\) at which \(s\) is the unique global minimizing difference, modulo sign:

| q | \(s\) | \(w_s=(A,B,C,D)\) | Exact \(F(s;w_s)\) | Bound on any equal/better competitor's q |
|---:|---|---|---:|---:|
| 7 | (6,-4,1) | (8,8,26,187) | 4/65 | 40 |
| 10 | (9,-5,1) | (3,3,20,34) | 6/37 | 45 |
| 11 | (10,-5,1) | (2,2,2,2) | 1/4 | 22 |
| 16 | (15,-6,1) | (7,1,1,15) | 3/8 | 73 |
| 27 | (24,-14,3) | (163,165,1809,388) | 3/986 | 57 |
| 39 | (36,-16,3) | (199,41,18,18) | 6/217 | 146 |
| 43 | (39,-20,4) | (7,15,1,1) | 3/8 | 147 |
| 49 | (45,-21,4) | (1,15,7,1) | 3/8 | 111 |
| 125 | (114,-56,11) | (2,47,3,2) | 12/49 | 190 |

**Finite exact check.** The accompanying C++17 verifier enumerates every nonzero unoriented \(a\) with \(q(a)\le234\), using \(x\ge0\), a first-nonzero-positive orientation convention and exact q-dependent ranges for y,z. Exactly **21,492,159** directions are checked. For each of the nine weight profiles, integer cross-multiplication compares the six-ratio maximum to the indicated winner. Each profile has exactly **one** equal-cost direction, namely its listed \(s\), and **zero** directions strictly better. No floating-point comparison is used.

**Removal of the finite-domain limitation.** Write \(u=Z_2(a)/2\), \(v=Z_3(a)/2\), \(h=Z_4(a)/2\). The integer moment map is invertible over \(\mathbb Q\), with the exact inverse

\[
\begin{pmatrix}x\\y\\z\end{pmatrix}
=
\begin{pmatrix}
19/2&-4&1/2\\
-14/3&7/3&-1/3\\
11/12&-1/2&1/12
\end{pmatrix}
\begin{pmatrix}u\\v\\h\end{pmatrix}.
\]

If \(F(a;w)\le r\), then its three pairs against the first channel give
\(|u|\le r(A+B)\), \(|v|\le r(A+C)\), and \(|h|\le r(A+D)\). Therefore

\[
\begin{aligned}
q(a)&\le |x|+|y|+|z|\\
&\le r\left[\frac{181}{12}(A+B)+\frac{41}{6}(A+C)+\frac{11}{12}(A+D)\right].
\end{aligned}
\tag{R86-1}
\]

Taking \(r=F(s;w_s)\), the exact rational upper bounds, in table order, are

\[
7829/195,\quad3379/74,\quad137/6,\quad1173/16,\quad
227133/3944,\quad63621/434,\quad2363/16,\quad1787/16,\quad9323/49.
\]

Their floors are \(40,45,22,73,57,146,147,111,190\), all strictly less than 234. Thus every possible tie or improvement in the **infinite integer lattice** is already included in the exhaustive exact enumeration. Hence all nine witness weights force globally unique, independent directions. Any fixed universally sufficient family must contain each of the nine, so \(N(p)\ge9\) for every \(p\ge125\).

This resolves the R79 caveat that minimality had only been established within the R72 28-element atlas. We also corrected three old strict-winner candidates that tied with non-atlas vectors: s16, s43 and s49 now use the weights above.

## 3. Universal upper bound: exact cone covering and 28-to-nine reduction

The independent Python checker reconstructs the nine integer linear forms \(T=[I_3;Z_j-Z_i\ (i<j)]\). Its exact cross-products give 28 primitive unoriented extreme-ray lines, 56 oriented rays, 212 pairwise-conformal unoriented ray triples and maximum values

\[
\max_{\text{ray}}q=125,\qquad
\max_{\text{conformal triple}}\sum q=235.
\]

For any integer difference \(a\ne0\), its sign cone is a pointed rational cone. By conic Carathéodory it admits a combination of at most three conformal primitive extreme rays \(a=\sum\lambda_i r_i\). If some \(\lambda_i\ge1\), take \(h=r_i\), so \(q(h)\le125\), \(q(h)\le q(a)\), and every signed moment gap has no greater magnitude. Otherwise all \(\lambda_i<1\) imply \(q(a)<235\), hence \(q(a)\le234\). This proves the all-weight full-lattice-to-\(q\le234\) reduction of R71.

The C++17 R86 checker independently validates, with q eligibility, all **21,492,159** unoriented directions with \(q\le234\) against the fixed 28-element R72 candidate atlas. Every single direction is covered by at least one 28-atlas member with \(q(s)\le q(a)\) and six half-gaps coordinatewise no larger. Zero uncovered directions.

The Python checker independently verifies that 17 of the 19 noncore atlas members are coordinatewise dominated by a member of \(S_9\). The other two have q=47 and 71 and half-gap vectors (0,12,12,12,12,0) and (12,12,0,0,12,12). For arbitrary positive \(A,B,C,D\), exact algebra gives

\[
\begin{aligned}
F_{47}&=\frac{12}{\min(A,B)+\min(C,D)},&
F_{71}&=\frac{12}{\min(A,D)+\min(B,C)},\\
F_{27}&=\frac6{C+\min(A,B,D)},&
F_{39}&=\frac6{A+\min(B,C,D)}.
\end{aligned}
\]

Consequently

\[
\min(F_{27},F_{39})
\le \frac6{\max(A,C)}
\le\frac{12}{A+C}
\le F_{47},F_{71}.
\]

Both 27- and 39-Port candidates are in \(S_9\), so this removes both exceptions without additional hypotheses. Therefore the original full lattice's objective equals the nine-term minimum at every \(p\ge125\). This gives \(N(p)\le9\). Together with §2, \(N(p)=9\) and the complete profile are proved within the exact declared model.

## 4. Reproduction and evidence scope

- Source: research_notes/portable_direct/x6_r86_global_nine_verify.cpp
- Run: g++ -O3 -std=c++17 x6_r86_global_nine_verify.cpp -o r86_verify && ./r86_verify
- Output: research_notes/portable_direct/x6_r86_global_nine_results.json
- Independent combinatorial crosscheck: python3 research_notes/portable_direct/x6_r86_cone_crosscheck.py

Local execution on 2026-11-21: exhaustive atlas coverage PASS; tested_unoriented=covered=21,492,159; failures=0; all nine unique-optimum test records have below=0 and ties=1. Separate exact Python ray results PASS (28 lines, 56 orientations, 212 triples, max q 125/235); 17 atlas elements dominated and exactly two exceptional algebraic cases. The C++ and Python tools are different implementations by the same current author; they are **not an independent mathematical peer review**, native P000 dynamic experiment, formal proof assistant check, or accepted Source Result.

Source attribution: historical R71–R85 notes and original researcher EM-X6-214D9C are antecedent provenance. The current paper and code are new portable work; control/Activity/source ownership must use the actual newly registered session, never a borrowed historical SID.

## 5. Native X6 boundary and next executable question

The observer does not collapse native P000 X6 six-dimensional Cell/Link/Port source states. The 3-force whole event, signed branch/phase, joint-relation road, event time and future-operation-sensitive histories remain in their original typed carrier. The BRC quantity derived here is only an exact positive star-histogram readout invariant under the declared frozen conditional reset model; no native-to-BRC physical attribution follows. The original R063 six-file native benchmark is still pending and should not be replaced by the present abstract checker.

Further useful questions: characterize the weight tie walls of the nine-term formula (strict open chambers and boundary multiplicities); and, on the **native** track, identify an exact source-defined P000 triadic transition/observer for which histogram fibers fail or preserve future readouts, recording named Ports and time order. These are distinct scientific questions. Keep all historical proofs, original IDs and admission status untouched.
