# D25/LIFT — explicit Green inverse for the Hesse reflection defect and a second-digit parity exception

2026-10-24 · TASK_RESEARCH portable **author proof and exact finite certificate** · **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (**unchanged**). Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923, separate from control-plane maintenance. This note is **not** a claim to a current winning native CLAIM/open/run, an authenticated H0/B0 divided-power section, a Source checkpoint, a Result or review.

## Exact inherited input (not claimed as new)

Let p=6m+1 >=13 be prime, n=2m=(p-1)/3, and let

\[
c_k=\frac{(3k)!}{27^k(k!)^3},\qquad
A_p(X)=\sum_{k=0}^{2m}c_kX^k,\qquad
\mathscr D_p(X)=\frac{A_p(X)-A_p(1-X)}p.
\]

The [previous source-reflection proof](https://github.com/awdawmip/enterprise-math/blob/238626c2bb75a51b843c3cb3e1af56c60a30e530/research_notes/portable_direct/20261024_hourly_d25_hesse_polynomial_reflection_defect_first_digit_bridge.md) established coefficientwise p-integrality of \(\mathscr D_p\); the [previous exact half-rank proof](https://github.com/awdawmip/enterprise-math/blob/b1e773f528ecec65959c46881e698c27331190ab/research_notes/portable_direct/20261024_hourly_d25_hesse_reflection_defect_half_rank_observer_safe_quotient.md) established unique \(\Phi_p\in\mathbf Z_{(p)}[Y]\), degree <=m-1, such that

\[
\mathscr D_p(X)=(1-2X)\Phi_p(X(1-X)),
\quad
\mathcal M\Phi_p=C_p F_{2m-1}(Y),
\tag{1}
\]
where
\[
\mathcal M=Y(1-4Y)\partial_Y^2+(1-10Y)\partial_Y-\frac{20}{9},
\quad C_p=\frac{p+1}{9}c_{2m},
\]
\[
F_0=F_1=1,\qquad F_r=F_{r-1}-YF_{r-2}.
\]
Its *ordinary polynomial* second-digit even-derivative scalar is
\[
E_p=-\Phi_p(1/8)+\frac14\Phi_p'(1/8)\pmod p.
\tag{2}
\]
Neither \(\Phi_p\) nor \(E_p\) is the unprovided Source-native CM/divided-power \([X]U\), Frobenius or \(\kappa\) observer.

## Theorem — explicit terminal-only Green kernel and a zero test

Put
\[
f_j=(-1)^j\binom{2m-1-j}{j},\qquad
\lambda_j=\frac{(6j+4)(6j+5)}9
\qquad(0\le j<m).
\]
Define the *rational*, hence also p-integral, backward sequence
\[
\boxed{\beta_m=0,\qquad
\beta_j=\frac{(j+1)^2\beta_{j+1}-f_j}{\lambda_j}
\quad(j=m-1,m-2,\ldots,0).}
\tag{3}
\]
Then the following is an **exact identity over \(\mathbf Q[Y]\)**, not a guessed finite-prime congruence:
\[
\boxed{\Phi_p(Y)=C_p\sum_{j=0}^{m-1}\beta_jY^j.}
\tag{4}
\]
Equivalently, with empty products equal to 1, the coefficients are an explicit triangular Green inverse
\[
\boxed{
\beta_j=-\sum_{\ell=j}^{m-1}f_\ell
\frac{\prod_{r=j}^{\ell-1}(r+1)^2}
     {\prod_{r=j}^{\ell}\lambda_r}.}
\tag{5}
\]

**Consequently the previously unknown parity-lift zero condition can be tested entirely in the ground field, without harmonic sums or p-adic division:**
\[
\boxed{
E_p\equiv C_p Q_p\pmod p,\qquad
Q_p:=\sum_{j=0}^{m-1}(2j-1)\beta_j8^{-j}\pmod p.
}
\tag{6}
\]
Moreover, Wilson's theorem gives
\[
\boxed{C_p\equiv
-\left(9\,27^{2m}((2m)!)^3\right)^{-1}\pmod p\ \in\mathbf F_p^\times.}
\tag{7}
\]
Therefore, for **every** prime p=6m+1 >=13,
\[
\boxed{E_p=0\text{ in }\mathbf F_p\quad\Longleftrightarrow\quad Q_p=0\text{ in }\mathbf F_p.}
\tag{8}
\]
Equation (8) is a proved, explicit source-polynomial exception criterion. It is **not** a decision rule for the native LIFT residue \(\Delta_p-R_p\).

**Proof.** The recurrence of \(F_r\) shows by induction that its coefficient at degree \(j\) is \((-1)^j\binom{r-j}{j}\); hence \(F_{2m-1}=\sum_{j=0}^{m-1}f_jY^j\). Direct differentiation gives
\[
\mathcal M(Y^j)=j^2Y^{j-1}-\lambda_jY^j.
\]
In the basis \(1,Y,\ldots,Y^{m-1}\), the operator is upper triangular with diagonal \(-\lambda_j\). Since \(1\le6j+4\le p-3\) and \(1\le6j+5\le p-2\), every \(\lambda_j\) is a p-unit. Thus \(\mathcal M\) is invertible both over \(\mathbf Q\) and on this bounded polynomial space modulo p; no resonant coefficient or unspecified homogeneous polynomial is lost. Comparing coefficients in (1), then solving backward with the degree boundary \(a_m=0\), gives (3)–(4). Expanding the recurrence gives (5).

Next, for \(\Phi(Y)=C_p\sum\beta_jY^j\), (2) becomes
\[
E_p=C_p\sum_{j=0}^{m-1}
\left(-8^{-j}+\frac j4 8^{-(j-1)}\right)\beta_j
=C_p\sum_{j=0}^{m-1}(2j-1)\beta_j8^{-j}\pmod p,
\]
giving (6). Finally \(3(2m)=p-1\), so
\(c_{2m}=(p-1)!/[27^{2m}((2m)!)^3]\).
Wilson's theorem and \(p+1\equiv1\bmod p\) give (7), including its nonvanishing. Division by \(C_p\) then proves (8). No CM Frobenius/GM action or native experiment is invoked. QED.

## New exact witness: a target-class p-adic parity restoration at p=373

The target prime \(p=373\equiv13\pmod{24}\) has \(m=62,n=124\). Applying (3)–(7) in \(\mathbf F_{373}\) gives the fully reproducible unit/zero pair
\[
\boxed{C_{373}=40,\qquad Q_{373}=0,\qquad E_{373}=0\pmod{373}.}
\tag{9}
\]
Independently rebuild the ORIGINAL factorial coefficients of \(A_{373}\), use the quadratic coefficient ring
\[
R_2=(\mathbf Z/373^2\mathbf Z)[T]/(T^2-2),\quad
u=(2-T)/4,\quad \sigma(T)=-T,
\]
and evaluate \(A'_{373}(u)\) with pair multiplication \((a,b)(c,d)=(ac+2bd,ad+bc)\). The exact integer residue certificate is
\[
\boxed{
A'_{373}(u)\equiv0+130607T\pmod{139129}.
}
\tag{10}
\]
Because \(130607\bmod373=57\neq0\),
\[
\boxed{h_{373}\equiv3\cdot57=171\neq0\pmod{373},}
\tag{11}
\]
while the even scalar part vanishes **through p²**:
\[
A'_{373}(u)+\sigma(A'_{373}(u))
\equiv0\pmod{373^2}.
\]
Thus the inherited first-digit ordinary Hesse unit remains nonzero, but the **same fixed source-polynomial's** second-digit even/parity defect vanishes. This is a concrete counterexample to an unqualified all-target assertion that the ordinary \(E_p\) is everywhere nonzero. It is NOT a counterexample to D25 LIFT/JT2.

Selected independent values from the two routes:

| p | \(C_p\bmod p\) | \(Q_p\bmod p\) | \(E_p\bmod p\) |
|--:|--:|--:|--:|
| 13 | 2 | 5 | 10 |
| 19 | 14 | 12 | 16 |
| 37 | 30 | 28 | 26 |
| 43 | 20 | 28 | 1 |
| 373 | 40 | **0** | **0** |

## Exact checker and bounded coverage

Companion script: [d25_hesse_terminal_green_kernel_check.py](https://github.com/awdawmip/enterprise-math/blob/958760768a30dd0b71a66207edbf40ad072c4968/research_notes/portable_direct/20261024_hourly_d25_hesse_terminal_green_kernel_check.py).

The author executed the script using exact Python integers. Route A uses the **terminal-only backward Green recurrence** (3),(6), with Wilson normalization. Route B independently uses the previously derived **finite harmonic/trace sum** from the full coefficient polynomial (not the Green recursion). Every one of the **312 target primes p<10000** gave the same E-value; no mismatches. A bounded exhaustive enumeration of this domain gave **exactly one E=0 prime: 373**. The third, separate test reconstructs \(A'_{373}(u)\) modulo \(p^2\) from its factorial coefficients in the quadratic pair ring and confirms (10)–(11). The finite exception list claims nothing about p>=10000 or other prime classes. Author-run code is not independent review; Lean/proof-kernel check NOT_RUN; Source-native CM/divided-power benchmark NOT_RUN.

## BRC information audit and exact next action

Typed carrier: \((p,m,c_{2m},F_{2m-1},\mathcal M;\beta_j,Q_p,C_p;\Phi_p,\mathscr D_p;T,\sigma,u;A'_p(u),E_p,h_p)\). Declared operations are polynomial inversion **only in the bounded degree space**, reflection with its signed \(1-2X\) branch factor, differentiation, source evaluation, mod-p/p² reduction and scalar decomposition. (8) is observer-safe for the *zero/nonzero status of the ordinary \(E_p\)* because \(C_p\) is proved to be a unit. It is **not** an admissible quotient of \(B_p\), the H0/B0 differential, native \(\kappa\), or the second-digit LIFT residue. The exceptional witness at 373 proves that collapsing to the earlier first-digit nonzero \(h_p\) cannot determine the even second-digit port; equally, a nonzero first digit must not be used to assume that \(E_p\) is invertible.

**Durable portable increment:** equations (3)–(8), the exact p=373 zero/unit separation (9)–(11), and the bounded 312-prime dual-regression and direct-p² certificate. **Do not repeat:** previous reflection identity, differential equation, half-rank factorization, harmonic trace, norm-2 parameter Hensel proof, WZ/LOW/HIGH expansions, or larger unrelated scans.

**Next discriminating scientific unit:** obtain the **actual Source-authorized same-class** divided-power \(H_0/B_0\) representative on the specified inert Hesse \(E_\lambda\), determine semilinear map direction, source-normalized \([X]U\bmod p^2\), product \(c_p\), and prove or refute the typed transport from \((B_p,E_p)\) to native \(\kappa_p\) and \(\Delta_p-R_p\). In particular, any proposed transport that divides by \(E_p\) for *every* target prime must explicitly handle p=373 or fail by (9)–(11). The native Source checkpoint (19 previously recorded completed units), contribution history and frozen science pin remain untouched. Control continuation/CLAIM/open, formal Result, Driver independent review and full LIFT remain OPEN.
