# D25 supersingular ASD visibility no-go and minimal lifted comparison carrier — 2026-09-24

Status: `ROUTE_SPECIFIC_NO_GO / EXACT_INFORMATION_BOUNDARY / NOT_A_RESULT / UNREVIEWED`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`

Current canonical run input pin consumed before this unit:
`research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-70a0fec6896849ac81484f0e00b3f0dd/1d58f6ee8351b2b94f51/_checkpoint.json@98dac6678146d2c3872604cb5d4073e106cbb255`.

This note does not reopen D24 UR/JT0, the accepted finite Clausen tail, or the exhausted first-order adjoint branch.

## 1. Question isolated

The canonical D25 continuation permits a source-level Frobenius route only if the Frobenius coordinate is proved equal to the actual source carrier. The unresolved digit remains

\[
\frac{a_{\rm parent}\Psi-1}{p}\pmod p
\]

together with the already typed endpoint correction needed to reach \(R_p\).

A natural idea is to push the supersingular Atkin–Swinnerton-Dyer/Katz recurrence already used in Chisholm–Deines–Long–Nebe–Swisher one order farther. This note proves that **the characteristic-polynomial recurrence by itself cannot see the required lifted \(p-1\) coefficient digit**. The missing datum is exactly a lifted coefficient-comparison scalar; it cannot be reconstructed from the supersingular recurrence (5.1) plus the first-order comparison used in Proposition 16.

This is a route-specific no-go, not a no-go for Frobenius methods in general.

## 2. External theorem boundary actually used

Chisholm–Deines–Long–Nebe–Swisher, *p-Adic Analogues of Ramanujan Type Formulas for \(1/\pi\)*, Mathematics 1 (2013), Proposition 16 and equation (5.1), supplies the following structure in the supersingular case.

For a coefficient sequence \(c(n)\) coming from a normalized de Rham differential,

\[
c(np^r-1)-b_1 c(np^{r-1}-1)^\sigma
+b_2 c(np^{r-2}-1)^{\sigma^2}\equiv0\pmod{p^r},
\tag{ASD}
\]

where supersingularity gives \(b_1=0\) and \(v_p(b_2)=1\).

For the degree-\(p\) square-root Frobenius matrix in a normalized basis,

\[
M=\begin{pmatrix}u&v\\ w&-u\end{pmatrix},
\qquad
-u^2-vw=b_2.
\tag{M}
\]

In the target quartic-normalized supersingular specialization used by the project, the first coefficient comparisons have the form

\[
1\equiv \frac{v\,\widetilde b_{p-1}}{p}\pmod p,
\qquad
1\equiv \frac{w\,\widetilde a_{p-1}}{p}\pmod p.
\tag{C1}
\]

The published theorem proves the de Rham product only modulo \(p^2\). No \(p^3\) coefficient comparison is imported from that paper.

## 3. Exact visibility lemma

Assume only

\[
b_1=0,\qquad v_p(b_2)=1,\qquad v_p(c(p-1))\ge1.
\]

Consider the perturbation

\[
c(p-1)\longmapsto c(p-1)+p^2 t
\qquad (t\in A).
\tag{G}
\]

Then **every occurrence of \(c(p-1)\) in (ASD), for every integral \(n\ge1\) and every admissible \(r\), is unchanged modulo the modulus asserted by (ASD)**.

Proof. There are only three positions in (ASD).

1. First position:
   \(np^r-1=p-1\) implies \(np^r=p\). The only nontrivial integral case is \(r=1,n=1\), whose modulus is \(p\). The perturbation \(p^2t\) is invisible modulo \(p\).

2. Middle position:
   \(np^{r-1}-1=p-1\) can occur, but the entire term is multiplied by \(b_1=0\).

3. Third position:
   \(np^{r-2}-1=p-1\) means \(np^{r-2}=p\).
   For \(r=2\), this gives \(n=p\); the perturbation contributes
   \(b_2p^2t\), of valuation at least \(3\), hence is invisible modulo \(p^2\).
   For \(r=3\), this gives \(n=1\); the same contribution has valuation at least \(3\), hence is invisible modulo \(p^3\).
   For \(r>3\), no positive integer \(n\) solves \(np^{r-2}=p\).

Thus (G) is an exact one-digit gauge symmetry of the full recurrence family (ASD). QED.

Consequently, the recurrence can determine at most the first normalized digit \(c(p-1)/p\bmod p\). It cannot determine the next digit \(c(p-1)/p\bmod p^2\).

## 4. Lifted comparison carrier

Write, in the target quartic-normalized supersingular chart,

\[
u=pU,\qquad v=pV,\qquad w=W,
\qquad
\widetilde a_{p-1}=pA,\qquad
\widetilde b_{p-1}=B,
\]

where \(V,W,A,B\) are units modulo \(p\). For the target normalization \(b_2=p\), (M) gives

\[
VW=-1-pU^2.
\tag{D}
\]

The first-order comparisons (C1) allow and require two lifted defects

\[
e_a:=\frac{WA-1}{p}\pmod p,
\qquad
e_b:=\frac{VB-1}{p}\pmod p.
\tag{E}
\]

These are not extra axioms: they are simply names for the first omitted digits of the actual coefficient comparisons.

Then, modulo \(p^3\),

\[
\begin{aligned}
\widetilde a_{p-1}\widetilde b_{p-1}
&=pAB\\
&=p(VW)^{-1}(1+p(e_a+e_b))\\
&\equiv -p+p^2\bigl(U^2-e_a-e_b\bigr).
\end{aligned}
\tag{P2}
\]

Hence the complete second digit of the quartic-normalized supersingular de Rham product is

\[
\boxed{\mathcal F_p=U^2-e_a-e_b\pmod p.}
\tag{FROB2}
\]

This algebra independently reproduces the safe combined Frobenius carrier previously present only in the unreviewed historical height-2 continuation; no separate twist/Clausen split is used.

## 5. Minimality at the declared observer

The gauge symmetry from Section 3 acts on the lifted comparison by

\[
A\mapsto A+pW^{-1}t
\quad\Longleftrightarrow\quad
e_a\mapsto e_a+t.
\]

It preserves:

- all congruences (ASD);
- the Frobenius characteristic polynomial and determinant relation;
- the first-order comparison \(WA\equiv1\pmod p\);
- every already-proved modulo-\(p^2\) product statement.

But by (FROB2) it changes

\[
\mathcal F_p\mapsto \mathcal F_p-t.
\]

Therefore the known supersingular characteristic-polynomial data plus Proposition-16 first-order comparisons **do not determine the second product digit**.

At the observer
\[
\text{“determine the quartic-normalized de Rham product modulo }p^3\text{”},
\]
at least one new \(\mathbf F_p\)-scalar is information-theoretically necessary. A convenient lossless choice is the combined comparison defect

\[
\boxed{E_p:=e_a+e_b\pmod p,}
\]

because \(U^2\) is already a Frobenius-matrix jet and
\(\mathcal F_p=U^2-E_p\).

This proves a sharper route boundary than “Frobenius remains open”:

> Any D25 Frobenius proof that uses only the supersingular ASD/Katz characteristic-polynomial recurrence and the modulo-\(p\) coefficient comparisons from Proposition 16 is insufficient. A successful source-level Frobenius bridge must additionally compute one lifted comparison scalar equivalent to \(E_p\), or an exactly source-equivalent scalar that kills the same gauge.

## 6. Consequence for the current D25 route

This no-go does not determine the project carrier
\([a_{\rm parent}\Psi-1]/p\) by itself. It does, however, remove an otherwise plausible redundant route.

The next Frobenius-side unit is now strictly smaller and testable:

1. derive a modulo-\(p^2\) coefficient comparison for the target \(d=3,\lambda=1/2\) quartic-normalized differential pair, sufficient to compute \(E_p=e_a+e_b\); or
2. prove an exact source bridge from a different Frobenius/deformation scalar to that same \(E_p\).

A mere higher-\(r\) reuse of (ASD) cannot satisfy this requirement.

Any eventual bridge must still be connected, by proof rather than analogy, to the current finite-Gauss source carrier and endpoint correction. The current LIFT/JT2 theorem remains open.

## 7. BRC information audit

Population: target primes \(p\equiv13,19\pmod{24}\), in the quartic-normalized supersingular \(d=3,\lambda=1/2\) lane.

Branch: D25 Frobenius/source-level alternative to the exhausted first-order adjoint route.

Observer: determine the one additional \(p\)-adic digit needed for LIFT/JT2.

Future operations retained: coefficient comparison, Frobenius determinant, source normalization, and exact bridge to the finite-Gauss carrier.

Safe quotient: replace the two separate lifted defects \((e_a,e_b)\) by their sum \(E_p=e_a+e_b\) **only for the product-second-digit observer**.

Unsafe quotient: discard \(E_p\) and retain only the characteristic polynomial/ASD recurrence.

`BRC_REUSE_RESOLUTION = REUSE_APPLIED + COMPOSE_APPLIED`.

## 8. Disposition

`SUPERSINGULAR_ASD_RECURRENCE_ONLY = EXACT_ROUTE_NO_GO_FOR_D25_SECOND_DIGIT`.

`MINIMUM_NEW_FROBENIUS_INFORMATION = AT_LEAST_ONE_Fp_SCALAR`.

`SAFE_COMBINED_CARRIER = E_p=e_a+e_b` at the product-second-digit observer.

`FROB2 = U^2-E_p`.

`LIFT/JT2 = OPEN`.

`NEXT_ACTION = derive the target quartic-normalized coefficient comparison one order deeper, or an exactly source-equivalent bridge to E_p; do not spend another cycle increasing r in the same ASD recurrence.`

External source:
Sarah Chisholm, Alyson Deines, Ling Long, Gabriele Nebe, Holly Swisher,
*p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1 (2013), DOI 10.3390/math1010009, especially equation (5.1) and Proposition 16.
