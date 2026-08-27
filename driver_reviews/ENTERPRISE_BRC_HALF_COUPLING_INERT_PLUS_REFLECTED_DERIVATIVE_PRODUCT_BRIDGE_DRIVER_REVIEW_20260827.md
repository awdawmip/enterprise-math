# Driver Review — Enterprise BRC Inert-Plus Reflected Derivative Product Bridge

Status: `DRIVER_FINAL / ACCEPTED / NEGATIVE_BOUNDARY / EXACT_SECOND_ORDER_REDUCTION / FOLLOWUP_TASK / NO_PROMOTION`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-REFLECTED-DERIVATIVE-PRODUCT-BRIDGE`

Publication: `TP2-17FC09F805797C961013`

Execution: `ER-1A1992ADA63C4AACE014`

Researcher-ID: `EM-EBP4P-6D8A31`

Result: `RR-810D5213FA9BCF4698C8`

Source result PR: `#739`

## 1. Final disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`HARD_TARGET = ACHIEVED_AT_EXACT_REDUCTION_STRENGTH`.

`FULL_INERT_PLUS_PRODUCT_TARGET = UNPROVED_AND_UNREFUTED`.

`RESULT_CLASS = EXACT_SECOND_ORDER_PARAMETER_DEFORMATION / NEGATIVE_BOUNDARY`.

`DESTINATION = FOLLOWUP_TASK`.

`FOLLOWUP_TASK = RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-FINITE-JACOBI-HARMONIC-IDENTITIES`.

`FOLLOWUP_PUBLICATION = TP2-AFF3DA9E8BBF2F6C886B`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_MUTATION = NONE`.

The Driver accepts the exact Taylor-block reconstruction and the equivalence of the parent product congruence to the two finite identities R0 and R1. The result does not prove the inert-plus supercongruence. It closes the present task at the strongest terminal state expressly allowed by its hard target: a strictly smaller exact identity remains.

## 2. Exact deformation audit

For \(p\equiv13,19\pmod{24}\), write \(p=6m+1\) and define

\[
b_{m,k}(\varepsilon)=
\frac{(-m+\varepsilon/6)_k(-2m+\varepsilon/3)_k}
{(k!)^2\,2^k}.
\]

The identities

\[
\frac16=-m+\frac p6,\qquad
\frac13=-2m+\frac p3
\]

give \(B_k=b_{m,k}(p)\) exactly.

The three parent valuation blocks are therefore the exact Taylor vanishing-order blocks:

\[
\begin{array}{c|c}
0\le k\le m&0\\
m<k\le2m&1\\
2m<k\le6m=p-1&2.
\end{array}
\]

This is structural, not a finite-prime observation.

## 3. Coefficient audit through second order

For the low block, direct logarithmic differentiation gives

\[
b_{m,k}(\varepsilon)
=w_k(1+L_k\varepsilon+Q_k\varepsilon^2)+O(\varepsilon^3),
\]

with

\[
w_k=\binom mk\binom{2m}k2^{-k},
\]

\[
L_k=-\frac16(H_m-H_{m-k})
-\frac13(H_{2m}-H_{2m-k}),
\]

and

\[
Q_k=\frac12\left(
L_k^2-\frac1{36}\Delta H_m^{(2)}
-\frac19\Delta H_{2m}^{(2)}\right).
\]

For \(m<k\le2m\), extracting the simple zero at \(-m\) gives

\[
b_{m,k}(\varepsilon)
=d_k\varepsilon+d_kM_k\varepsilon^2+O(\varepsilon^3),
\]

where

\[
d_k=
\frac{(-1)^{m+k}m!(k-m-1)!(2m)!}
{6(2m-k)!(k!)^2\,2^k}
\]

and

\[
M_k=\frac16(H_{k-m-1}-H_m)
-\frac13(H_{2m}-H_{2m-k}).
\]

For \(2m<k\le6m\), extracting both vanishing factors gives

\[
b_{m,k}(\varepsilon)=v_k\varepsilon^2+O(\varepsilon^3),
\]

\[
v_k=
\frac{(-1)^m m!(2m)!(k-m-1)!(k-2m-1)!}
{18(k!)^2\,2^k}.
\]

The Driver independently expanded these polynomials symbolically across representative \(m\) and every block index; the orders and coefficients agree exactly with the frozen formulas.

Summing the coefficients yields

\[
G_p\equiv F_0+pF_1+p^2F_2\pmod{p^3},
\]

\[
H_p\equiv J_0+pJ_1\pmod{p^2}.
\]

No \(J_2\) term is needed after the leading divisibility is established.

## 4. Leading divisibility dependency

The return imports the published unweighted congruence

\[
U_p=
\sum_{n=0}^{p-1}
\frac{(2n)!(3n)!}{(n!)^5\,216^n}
\equiv0\pmod{p^2}
\]

for the inert residue classes. Bibliographic identity and publication metadata were verified for Zhi-Hong Sun, *Congruences involving* \(\binom{2k}k^2\binom{3k}k\), Journal of Number Theory 133 (2013), 1572–1595, DOI `10.1016/j.jnt.2012.10.001`.

This theorem is treated as an explicit imported dependency, not as a theorem reproved by this execution. The task-local checker independently verifies the displayed congruence on its finite regression set only.

The exact finite unweighted Clausen identity has

\[
G_p^2=U_p+T_p^{(0)}.
\]

For \(p=6m+1\), low+low and middle+middle cannot enter degree at least \(p\), while every surviving low+high or high+low term has valuation at least two. Thus

\[
T_p^{(0)}\equiv0\pmod{p^2},
\]

and hence

\[
G_p^2\equiv0\pmod{p^2}.
\]

Because \(G_p\in\mathbb Z_p\), this implies

\[
\boxed{p\mid G_p}.
\]

The imported theorem is used only for this leading divisibility. It does not supply the derivative-weighted target.

## 5. Exact terminal equivalence

Define

\[
A_m=\frac{F_0}p+F_1.
\]

The quantity is \(p\)-adically integral because \(G_p\equiv F_0\pmod p\) and \(p\mid G_p\). Then

\[
\frac{G_p}p\equiv A_m+pF_2\pmod{p^2}.
\]

Together with the parent reflected tail

\[
T_p\equiv p^2R_p\pmod{p^3},
\]

the target

\[
G_pH_p\equiv p+p^2R_p\pmod{p^3}
\]

is exactly equivalent to

\[
(A_m+pF_2)(J_0+pJ_1)
\equiv1+pR_p\pmod{p^2}.
\]

Its two \(p\)-adic digits are precisely

\[
\boxed{A_mJ_0\equiv1\pmod p}
\tag{R0}
\]

and

\[
\boxed{
\frac{A_mJ_0-1}p+A_mJ_1+F_2J_0
\equiv R_p\pmod p}.
\tag{R1}
\]

The equivalence is reversible. No unknown tail or additional coefficient is hidden in R0/R1.

## 6. Residue classes, second route, and regression

The same algebra covers both requested classes:

\[
p\equiv13\pmod{24}\Longleftrightarrow m\equiv2\pmod4,
\]

\[
p\equiv19\pmod{24}\Longleftrightarrow m\equiv3\pmod4.
\]

The positive sign is not inserted into the deformation; it appears only in the target whose equivalence is being analyzed.

A distinct \(p\)-adic Gamma/Dwork transformation route was audited. The available unweighted modulo-\(p^2\) technology does not supply the derivative-weighted modulo-\(p^3\) correction, so it does not close R0/R1.

The checker reconstructs \(B_k,U_p,R_p,F_i,J_i\) with exact rational arithmetic and no import of a target implementation. Frozen regression covers all `77` plus-class primes below `2000`, split `40/37` between the two classes, with zero failures. This remains finite falsification evidence only.

## 7. Result-record normalization

The source result stored

`terminal_verdict = PROOF_NOT_CLOSED_WITH_SMALLER_IDENTITY`.

That phrase is a valid task-level research conclusion under the taskbook, but it is not one of the immutable result-contract terminal enums. Before review pinning, the current-main replay normalizes only this field to

`terminal_verdict = NEGATIVE_BOUNDARY`.

The detailed hard-target disposition, Result-ID, execution identity, return blob, output digests, owner head, mathematical content, and unresolved residue are unchanged.

The corrected result-record SHA-256 is

`sha256:00c2615538b4233759847df5906f085c1ac62826b65a8d3e88714200c872d272`.

## 8. Successor gate

The parent task has reached its permitted exact-reduction terminal state. The remaining unit is no longer the original length-\(p\) product or the finite Clausen tail; it is exactly R0/R1.

Closure, return to a broad route, another owner, and the already-audited Gamma/Dwork and Gosper routes were considered. A narrowly bounded continuation has higher leverage and a genuinely different proof interface.

The Driver therefore publishes:

- Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-FINITE-JACOBI-HARMONIC-IDENTITIES`;
- Publication: `TP2-AFF3DA9E8BBF2F6C886B`;
- Hard target: `INERT_PLUS_FINITE_JACOBI_HARMONIC_R0_R1_PROVED_REFUTED_OR_EXACTLY_OBSTRUCTED`.

The continuation forbids reopening the finite tail or replacing proof with a larger scan.

## 9. Integration boundary

PR `#739` contains only the return, reduction certificate, task-local checker, execution record, and result record. Its exact payload is replayed onto current `main` together with:

- the normalized result record;
- this immutable Driver review;
- its immutable review record;
- the registered R0/R1 continuation taskbook and publication record.

No shared Foundation or theorem-source module is rewritten. No CI-success claim is made.

## 10. Final freeze

`RR-810D5213FA9BCF4698C8 = ACCEPTED / NEGATIVE_BOUNDARY`.

`TP2-17FC09F805797C961013 = TERMINAL_AT_TASK_SCOPE`.

`INERT_PLUS_PRODUCT_TARGET = UNPROVED_UNREFUTED`.

`FINITE_CLAUSEN_TAIL = CLOSED_AND_NOT_REOPENED`.

`SMALLEST_OPEN_UNIT = R0_AND_R1`.

`FOLLOWUP_TASK = RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-FINITE-JACOBI-HARMONIC-IDENTITIES`.

`FOLLOWUP_PUBLICATION = TP2-AFF3DA9E8BBF2F6C886B`.

`FOUNDATION_AND_WORKING_TRUTH_STATUS = UNCHANGED`.
