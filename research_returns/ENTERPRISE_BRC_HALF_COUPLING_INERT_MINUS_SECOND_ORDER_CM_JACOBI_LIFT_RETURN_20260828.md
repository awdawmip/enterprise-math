# Enterprise BRC Inert-Minus Second-Order CM/Jacobi Lift — Research Return

Status: `FINAL_FROZEN / PROOF_NOT_CLOSED / STRICT_EXACT_CLAUSEN_REDUCTION`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-SECOND-ORDER-CM-JACOBI-LIFT`
Publication: `TP2-05DB03EAF4E1DDCDBDF2`
Claim: `chatgpt-ebp5m2-20260828-1411-d74849`
Researcher-ID: `EM-EBP5M2-D74849`
Execution: `ER-69F4296978826B9EBFA6`

## Verdict

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_STRICT_EXACT_REDUCTION`.

For every prime \(p\equiv17,23\pmod{24}\), the frozen predecessor's two congruences `(R0-)` and `(R1-)` are exactly equivalent to the single weighted Ramanujan-type congruence
\[
\boxed{
W_p:=\sum_{n=0}^{p-1}(6n+1)
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
\equiv-p\pmod{p^3}.
}
\tag{W-}
\]
The all-prime proof of `(W-)` was not closed in this execution.

## 1. Exact finite Clausen collapse

The frozen predecessor uses
\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}2^{-k},\qquad
G_p=\sum_{k=0}^{p-1}B_k,\qquad
H_p=\sum_{k=0}^{p-1}(12k+1)B_k,
\]
and
\[
T_p=\sum_{\substack{0\le i,j<p\\i+j\ge p}}
(1+6(i+j))B_iB_j,\qquad S_p=G_pH_p-T_p.
\]
Averaging the product \(G_pH_p\) under \(i\leftrightarrow j\) gives the exact identity
\[
G_pH_p=\sum_{0\le i,j<p}(1+6(i+j))B_iB_j.
\]
Hence
\[
S_p=\sum_{\substack{0\le i,j<p\\i+j<p}}(1+6(i+j))B_iB_j.
\]
Now
\[
F(x):=\sum_{k\ge0}B_kx^k
={}_2F_1\!\left(\frac16,\frac13;1;\frac{x}{2}\right),
\]
and Clausen's formula gives
\[
F(x)^2
={}_3F_2\!\left(\frac12,\frac13,\frac23;1,1;\frac{x}{2}\right).
\]
Therefore for every \(n\ge0\),
\[
\sum_{i=0}^n B_iB_{n-i}
=
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3 2^n}
=
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}.
\]
Grouping the triangle by \(n=i+j\) yields the exact finite identity
\[
\boxed{S_p=W_p.}
\tag{FC}
\]
No infinite-series truncation is used in `(FC)`.

## 2. Exact valuation endpoint

For \(0\le n<p\),
\[
v_p\!\left(\binom{2n}{n}^2\binom{3n}{n}\right)
=
\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{3n}{p}\right\rfloor.
\tag{V}
\]
For \(p=6m+5\), set \(M=(2p-1)/3=4m+3\). If \(n>M\), the valuation in `(V)` is at least \(3\). Thus
\[
W_p\equiv
\sum_{n=0}^{M}(6n+1)
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
\pmod{p^3}.
\tag{T}
\]

## 3. Equivalence with the predecessor R0-/R1- interface

The predecessor proves
\[
\frac{S_p}{p}\equiv A+pB\pmod{p^2},
\]
where
\[
A=g_0J_0-\tau_0,\qquad
B=g_0J_1+g_1J_0-\tau_1.
\]
Therefore \(S_p\equiv-p\pmod{p^3}\) is equivalent to
\[
A+pB\equiv-1\pmod{p^2},
\]
whose zeroth and first base-\(p\) digits are exactly `(R0-)` and `(R1-)`. Combining this with `(FC)` proves
\[
\boxed{(R0-)\ \&\ (R1-)\iff(W-).}
\tag{EQ}
\]

## 4. Classical identification

Zhi-Wei Sun's *Open Conjectures on Congruences* (arXiv:0911.5665v41), Conjecture A14(ii), states in particular
\[
\frac1{p^a}\sum_{k=0}^{p^a-1}
\frac{6k+1}{6^{3k}}
\binom{2k}{k}^2\binom{3k}{k}
\equiv
\left(\frac{p^a}{3}\right)
\pmod{p^2}.
\]
At \(a=1\), this is
\[
W_p\equiv p\left(\frac p3\right)\pmod{p^3}.
\]
For the target classes \(p\equiv17,23\pmod{24}\), \((p/3)=-1\), so the conjecture specializes exactly to `(W-)`.

A targeted literature check located the exact conjecture and adjacent proved supercongruences, but did not locate a verifiable all-prime proof of this exact weighted \(216^{-n}\) statement. This return therefore treats Sun A14(ii) as a conjectural identification, not as an imported theorem.

## 5. Smallest finite bridge to a proved theorem

For \(p\equiv2\pmod3\), let \(M=(2p-1)/3\) and
\[
E_p=\sum_{k=0}^{M}(-1)^k(6k+1)\frac{(1/3)_k^3}{(k!)^3}.
\]
Swisher proved
\[
E_p\equiv-2p\pmod{p^3}.
\tag{Sw}
\]
By `(T)` and `(Sw)`, `(W-)` is equivalent to the single finite transformation congruence
\[
\boxed{
C_p:=
2\sum_{k=0}^{M}(6k+1)
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3 2^k}
-
\sum_{k=0}^{M}(-1)^k(6k+1)\frac{(1/3)_k^3}{(k!)^3}
\equiv0\pmod{p^3}.
}
\tag{Bridge-}
\]
This is the smallest exact unresolved certificate frozen by this execution.

The ordinary infinite analytic transformation cannot simply be truncated: the corresponding infinite Ramanujan values satisfy \(W_\infty=2E_\infty\), whereas the finite bridge required here is \(E_p\equiv2W_p\pmod{p^3}\). Any proof must explicitly control the terminating boundary/tail.

## 6. Independent Domb route

Let
\[
D_n=\sum_{k=0}^{n}
\binom nk^2\binom{2k}{k}\binom{2n-2k}{n-k}.
\]
The Rogers/Domb pullback
\[
\phi(x)=\frac{108x^2}{(1-4x)^3}
\]
satisfies \(\phi(-1/8)=1/2\), the Clausen argument behind \(W_p\). This gives a structurally independent modular/Domb route. The bounded diagnostic
\[
\sum_{n=0}^{p-1}(2n+1)D_n(-8)^{-n}\equiv-p\pmod{p^3}
\]
passed the tested \(p\equiv2\pmod3\) primes, but the finite Rogers boundary remains unproved. It is evidence and route information only.

## 7. Regression and artifacts

Checker:
`scripts/check_enterprise_brc_half_coupling_inert_minus_second_order_cm_jacobi_lift.py`.

Certificate:
`research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT/reduction_certificate_20260828.json`.

Frozen bounded regression:
- exact Clausen coefficients \(n=0,\ldots,10\): PASS as rational identities;
- valuation formula `(V)`: PASS for every \(0\le n<p\) on primes \(5\le p\le1000\);
- broad pattern \(W_p\equiv p(p/3)\pmod{p^3}\): 166 primes \(5\le p\le1000\), zero failures;
- target classes \(p\equiv17,23\pmod{24}\): 45 primes \(\le1000\), zero failures;
- finite Swisher bridge `(Bridge-)`: 86 primes \(p\equiv2\pmod3\), \(p\le1000\), zero failures;
- Domb diagnostic: 12 primes \(p\equiv2\pmod3\), \(p\le100\), zero failures.

All finite scans are falsification/regression evidence only.

## Final boundary

Closed:
- exact finite collapse \(S_p=W_p\);
- exact equivalence `(R0-) + (R1-)` with `(W-)`;
- exact high-tail valuation cutoff modulo \(p^3\);
- exact identification with the target subfamily of Sun A14(ii);
- exact reduction to the single finite bridge `(Bridge-)`;
- two structurally distinct continuation routes: finite hypergeometric/Swisher and Domb/modular.

Open:
- an all-prime proof of `(W-)`, equivalently `(Bridge-)`;
- therefore the full inert-minus second-order target is not claimed proved.

`HARD_TARGET = NOT_ACHIEVED_AT_FULL_PROOF_STRENGTH`.
`HARD_TARGET_DISPOSITION = ACHIEVED_AT_STRICT_EXACT_REDUCTION_STRENGTH`.
`SMALLEST_EXACT_REMAINING_IDENTITY = FINITE_CLAUSEN_TO_SWISHER_BRIDGE`.
`FOUNDATION_MUTATION = NONE`.
`WORKING_TRUTH = NOT_GRANTED`.
`NOVELTY_OR_PRIORITY_CLAIM = NONE`.

Recommended Driver action: accept the exact collapse. If continuation remains high value, publish one narrow successor for a terminating cubic/WZ/creative-microscoping proof of `(Bridge-)`; do not reopen the proved mod-\(p\) cancellation layer, do not treat Sun A14(ii) as proved without a verified source, and do not substitute a larger prime scan for proof.
