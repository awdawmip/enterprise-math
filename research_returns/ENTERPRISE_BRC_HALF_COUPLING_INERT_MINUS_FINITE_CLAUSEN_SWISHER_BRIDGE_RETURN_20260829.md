# Enterprise BRC Inert-Minus Finite Clausen-Swisher Bridge — Research Return

Status: `FINAL_FROZEN / PROOF_NOT_CLOSED / STRICT_EXACT_SINGULAR_BOUNDARY_REDUCTION`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-FINITE-CLAUSEN-SWISHER-BRIDGE`  
Publication: `TP2-4F101DF8AD14340C933C`  
Claim: `chatgpt-ebp6m-20260829-0005`  
Researcher-ID: `EM-EBP6M-0FFBAD`  
Execution: `ER-3E2515F5765D859565E7`

## Verdict

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_STRICT_EXACT_SINGULAR_BOUNDARY_REDUCTION`.

No exact all-prime proof of
\[
C_p=2\widetilde W_p-E_p\equiv0\pmod{p^3}
\]
was obtained, and no target-class counterexample was found. A bounded literature check did not locate a verified prior theorem matching the exact weighted \(216^{-k}\) statement; Sun A14(ii) remains identification only in this execution.

The new result is an exact reduction of the finite bridge to a unique \(p\)-singular step in the first-order recurrence of Sun's A14(i) companion quotient. The unknown hypergeometric core is shortened from the original endpoint
\[
M=\frac{2p-1}{3}
\]
to
\[
s-1=\frac{p-5}{2},
\]
while the whole upper part is replaced by explicit first-order back-propagation through binomial/Fuss-Catalan source terms.

## 1. Frozen parent interface

For target primes \(p\equiv17,23\pmod{24}\), freeze the accepted predecessor facts:
\[
W_p:=\sum_{k=0}^{p-1}(6k+1)
\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k},
\qquad
W_p\equiv \widetilde W_p\pmod{p^3},
\]
and Swisher's proved theorem
\[
E_p\equiv-2p\pmod{p^3}
\qquad (p\equiv2\pmod3).
\]
Hence
\[
C_p\equiv0\pmod{p^3}
\iff
W_p\equiv-p\pmod{p^3}.
\tag{1}
\]

Nothing below reopens the predecessor's Clausen collapse, high-tail valuation, unit-tail cancellation, or two-scalar bookkeeping.

## 2. Companion quotient and an exact first-order recurrence

For \(n\ge1\), define the finite companion quotient
\[
a_n:=
\frac{
\displaystyle\sum_{k=0}^{n-1}(6k+1)
\binom{2k}{k}^2\binom{3k}{k}\,216^{\,n-1-k}
}{
n(2n+1)\binom{2n}{n}
}.
\tag{2}
\]
This is the sequence appearing in Sun A14(i), but only its exact finite definition is used here.

Let
\[
R_n:=(6n+1)\binom{2n-1}{n}
\frac{1}{2n+1}\binom{3n}{n}.
\tag{3}
\]
The factor \(\frac1{2n+1}\binom{3n}{n}\) is the order-2 Fuss-Catalan integer.

If \(S_n\) denotes the numerator in (2), then directly
\[
S_{n+1}=216S_n+(6n+1)\binom{2n}{n}^2\binom{3n}{n}.
\]
Writing
\[
D_n=n(2n+1)\binom{2n}{n}
\]
gives
\[
\frac{D_{n+1}}{D_n}=\frac{2(2n+3)}{n}.
\]
Therefore, with no conjectural input,
\[
\boxed{(2n+3)a_{n+1}=108n\,a_n+R_n.}
\tag{4}
\]

The definition also gives the exact identity
\[
\boxed{
W_p=
p(2p+1)\binom{2p}{p}\,216^{1-p}a_p.
}
\tag{5}
\]

Thus (1) is exactly equivalent to
\[
a_p\equiv
-216^{p-1}
\left((2p+1)\binom{2p}{p}\right)^{-1}
\pmod{p^2}.
\tag{6}
\]
The inverse exists because the displayed factor is a \(p\)-adic unit.

## 3. The unique singular recurrence step

Set
\[
s:=\frac{p-3}{2}.
\tag{7}
\]
Among all integers \(1\le n<p\),
\[
p\mid(2n+3)
\]
holds at exactly one place:
\[
n=s,\qquad 2s+3=p.
\tag{8}
\]

For every \(n=s+1,\ldots,p-1\), both \(108n\) and \(2n+3\) are \(p\)-adic units. Therefore the target (6) can be propagated backward uniquely modulo \(p^2\).

Define
\[
T_p:=
-216^{p-1}
\left((2p+1)\binom{2p}{p}\right)^{-1}
\pmod{p^2},
\tag{9}
\]
and recursively, for \(n=p-1,p-2,\ldots,s+1\),
\[
\boxed{
T_n\equiv
\big((2n+3)T_{n+1}-R_n\big)(108n)^{-1}
\pmod{p^2}.
}
\tag{10}
\]

By (4),
\[
a_p\equiv T_p\pmod{p^2}
\iff
a_{s+1}\equiv T_{s+1}\pmod{p^2}.
\tag{11}
\]

At the unique singular step \(n=s\), (4) becomes the exact identity
\[
p\,a_{s+1}=108s\,a_s+R_s.
\tag{12}
\]
Multiplying (11) by \(p\) and using (12) yields the new certificate
\[
\boxed{
B_p:=108s\,a_s+R_s-pT_{s+1}\equiv0\pmod{p^3}.
}
\tag{13}
\]

Combining (1), (6), (11), and (12):
\[
\boxed{
C_p\equiv0\pmod{p^3}
\iff
B_p\equiv0\pmod{p^3}
}
\tag{14}
\]
for every target prime \(p\equiv17,23\pmod{24}\), using only the frozen Swisher/high-tail interface.

This is not a restatement at the same endpoint. In (13), the only non-explicit companion quotient is \(a_s\), whose defining sum stops at
\[
k=s-1=\frac{p-5}{2},
\]
whereas the original finite bridge runs through
\[
k=M=\frac{2p-1}{3}.
\]
The unknown hypergeometric support is therefore shortened by
\[
(M+1)-s=\frac{p+13}{6}>0.
\]

## 4. Exact source-valuation zoning

The recurrence source has a rigid target-class valuation pattern. For
\[
M=\frac{2p-1}{3},\qquad s=\frac{p-3}{2},
\]
Legendre/Kummer valuation of the two binomial factors in (3) gives:

\[
v_p(R_s)=1,
\tag{15}
\]
\[
v_p(R_{s+1})=0,
\tag{16}
\]
\[
v_p(R_n)=1
\qquad (s+2\le n\le M),
\tag{17}
\]
and
\[
v_p(R_n)\ge2
\qquad (M+1\le n\le p-1).
\tag{18}
\]

The possible extra valuation in the last zone can come from \(6n+1\); only the lower bound is needed.

Thus the upper recurrence is homogeneous modulo \(p^2\) once \(n>M\). Immediately below it lies a \(p\)-linear strip, then exactly one \(p\)-unit source \(R_{s+1}\), and then the singular coefficient \(2s+3=p\). This four-zone pattern is the structural reason (13) is a useful continuation object rather than a cosmetic change of notation.

## 5. Literature and duplication check

The exact weighted statement
\[
W_p\equiv p\left(\frac p3\right)\pmod{p^3}
\]
is the \(a=1\) specialization of Zhi-Wei Sun's A14(ii) in *Open Conjectures on Congruences* (arXiv:0911.5665). It is used here only as identification. The source itself places A14 in its open-conjecture part.

Swisher's 2015 result proving
\[
\sum_{k=0}^{(2p-1)/3}(-1)^k(6k+1)\frac{(1/3)_k^3}{(k!)^3}
\equiv-2p\pmod{p^3}
\]
for \(p\equiv2\pmod3\) remains the proved theorem furnishing the \(E_p\) side.

A bounded targeted search also checked recent adjacent supercongruence/q-supercongruence literature. No verified theorem with identical \(216^{-k}\), weight \(6k+1\), range, residue classes, and modulus \(p^3\) was located. Therefore this execution does not return `DUPLICATED`.

## 6. Regression and checker

Checker:
`scripts/check_enterprise_brc_half_coupling_inert_minus_finite_clausen_swisher_bridge.py`.

Artifact:
`research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_FINITE_CLAUSEN_SWISHER_BRIDGE/singular_boundary_certificate_20260829.json`.

The checker verifies:

- exact identity (5);
- exact recurrence (4) for a fixed symbolic-free integer range;
- uniqueness of the singular coefficient (8);
- valuation zones (15)-(18);
- frozen high-tail congruence on bounded samples;
- bounded \(C_p\) regression modulo \(p^3\);
- bounded \(B_p\) regression modulo \(p^3\).

Regression target primes:
\[
17,23,41,47,71,89.
\]
All pass in the independent exact-rational checker.

These finite checks are falsification/regression evidence only and are not used as proof of (14) or of the open all-prime congruence.

## Final boundary

Closed in this execution:

- exact A14 companion identity (5);
- independent derivation of the exact first-order recurrence (4);
- unique \(p\)-singular step \(n=(p-3)/2\);
- exact source-valuation zoning (15)-(18);
- exact equivalence of the original finite bridge with the smaller singular-boundary certificate (13).

Open:

- prove or refute
  \[
  B_p\equiv0\pmod{p^3}
  \]
  uniformly for \(p\equiv17,23\pmod{24}\);
- consequently, the original \(C_p\) bridge and the inert-minus all-prime target remain unproved.

Recommended continuation: attack the unique singular step directly. The upper zone \(n>M\) is already homogeneous modulo \(p^2\), so a next proof attempt should seek a closed product/creative-telescoping evaluation of the backward target \(T_{s+1}\) together with the shortened core \(a_s\), rather than reopening the full \(C_p\), enlarging the prime census, or treating Sun A14(ii) as a theorem.

`HARD_TARGET = NOT_ACHIEVED_AT_FULL_PROOF_STRENGTH`.  
`HARD_TARGET_DISPOSITION = ACHIEVED_AT_STRICT_EXACT_REDUCTION_STRENGTH`.  
`SMALLEST_EXACT_REMAINING_IDENTITY = UNIQUE_P_SINGULAR_A14_BOUNDARY_CERTIFICATE_B_P`.  
`FOUNDATION_MUTATION = NONE`.  
`WORKING_TRUTH = NOT_GRANTED`.  
`NOVELTY_OR_PRIORITY_CLAIM = NONE`.
