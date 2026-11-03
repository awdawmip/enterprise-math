# D25 — Four-moment normal form for the Hensel-lifted Green observer

2026-11-03 +08. **TASK_RESEARCH author-side mathematical result, algebraically proved / exact checked / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Research lane: chatgpt-research-hourly-enterprise-math-20260923; maintenance conversation not used. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Portable evidence only; no new claim, run or native Source checkpoint.

## Reuse / exact question

The immediately preceding author result (commit c8ae847fac9d38fcc1ae7e8fdb7e76086987d9f5, 20261103_hourly20_d25_original_high_hensel_adjoint_boundary_jet.md) proves the original, source-faithful high-strip p² Green identity
\[
\sum_{s=0}^{r-1}\mathcal L_p P(s)Y_s
\equiv(2r+1)^3P(r)Y_r-P(0)Y_0\pmod{p^2}
\]
for every polynomial P. Here p=6r+1>=7 is prime, n=3r, Y_s=b_(n+1+s)/p², Y_r=b_(4r+1)/p², with the original factorial b_k=(2k)!(3k)!/[(k!)^5 216^k]. At p² the forward coefficient of L_p has one rational denominator 2s+3. This note asks for the exact algebraic normal form after clearing that denominator, and the corresponding finite observer and endpoint semantics.

## Theorem: unique rank-four polynomial normal form over the p-adic second digit

For p=6r+1>=7 and R=Z/p²Z, define the R-linear polynomial operator
\[
\mathscr T_pP(s):=(2s+3)\mathcal L_pP(s)
=\underbrace{\frac{(2s+3)(s+1)(6s+5)(6s+7)}9 P(s+1)
 -(2s+3)(2s+1)^3P(s)}_{\text{unlifted part}}
 +\frac p{18}[108(s+1)^2+4(s+1)-1]P(s+1).
\tag{1}
\]
All denominators 9,18 are units in R. For any P∈R[s] with nonzero leading coefficient a of degree m, the leading coefficient of \(\mathscr T_pP\) at degree m+4 is **-8a**, which is nonzero because 8 is an R-unit. The p-dependent summand has degree at most m+2. Hence
\[
\boxed{R[s]=\mathscr T_p(R[s])\;\oplus\;
\operatorname{span}_R\{1,s,s^2,s^3\}.}\tag{2}
\]
Explicitly: every W∈R[s] has a unique P∈R[s] and unique (d0,d1,d2,d3)∈R⁴ such that
\[
\boxed{W(s)=\mathscr T_pP(s)+d_0+d_1s+d_2s^2+d_3s^3.}\tag{3}
\]
**Proof.** Eliminate the current highest degree d>=4 of W by subtracting \(-w_d/8\cdot \mathscr T_p(s^{d-4})\). Its leading term cancels and degree drops. Repeat to remainder <4. If two expressions exist, their difference would have degree >=4 unless P difference is zero. Injectivity and uniqueness then follow. These operations are valid in R because -8 is invertible. Thus this is a literal free rank-four polynomial quotient, rather than a heuristic finite-sample fit.

## Exact finite observer including both ports

For 0<=j<=3 define the *rescaled source moments*
\[
N_j:=\sum_{s=0}^{r-1}\frac{s^jY_s}{2s+3}\pmod{p^2}.
\]
The denominator is an R-unit for every 0<=s<r since 3<=2s+3<=2r+1<p. For W, P, d_i as in (3), the preceding original-source Green identity yields
\[
\boxed{\sum_{s=0}^{r-1}\frac{W(s)Y_s}{2s+3}
\equiv d_0N_0+d_1N_1+d_2N_2+d_3N_3
 +(2r+1)^3P(r)Y_r-P(0)Y_0\pmod{p^2}.}\tag{4}
\]
Both endpoint fluxes are retained. The outgoing source Y_r is divisible by p but is not automatically zero modulo p². Equation (4) is exact for the declared polynomial/rational observer; it does not claim rank four is minimal for a specific r-point finite readout (particularly r<4) or for unrelated later operators.

For a concrete degree-four certificate,
\[
\mathscr T_p(1)=
-8s^4-12s^3+
(\tfrac{106}{9}+6p)s^2+
(\tfrac{211}{9}+\tfrac{110p}{9})s+
(\tfrac{26}{3}+\tfrac{37p}{6}).
\]
Therefore the original factorial rescaled fourth moment satisfies
\[
\boxed{
\begin{aligned}
N_4\equiv\;&\tfrac18Y_0-\tfrac18(2r+1)^3Y_r-\tfrac32N_3\\
 &+(\tfrac{53}{36}+\tfrac{3p}{4})N_2
 +(\tfrac{211}{72}+\tfrac{55p}{36})N_1
 +(\tfrac{13}{12}+\tfrac{37p}{48})N_0
 \pmod{p^2}.
\end{aligned}}\tag{5}
\]
Here N_4 denotes the same rescaled fourth moment, not a new independent carrier.

## Executed exact integer checks / BRC interpretation

The companion standard-library program constructs p-free units of the **original** factorial b_k, evaluates Y_s mod p² and Y_r, then over R performs polynomial Euclidean cancellation for W=s^d (d=4,..,10). For every such degree it checks the polynomial identity (3) coefficientwise and the original finite observer (4). It also checks the explicit independent algebraic (5). Actual run: **PASS on all 148 primes p≡1 mod6 with 7<=p<=2000; 22,952 oriented high-band source positions; 7 polynomial degrees 4..10 each.** Witness N4 residues: p=13 ->106 mod 169; p=19 ->61 mod361; p=373 ->65591 mod 139129.

BRC compression scope: retain original factorial source/valuations, chi, Hensel jet, directed s↔k index, both endpoints, and polynomial test P. The four formal moments plus the two explicitly typed boundary functionals reconstruct every declared W-polynomial rescaled observation mod p². This is a quotient in **polynomial operator space**, not a claim that the native Heartbeat X6 state has four spatial axes. P000, ACTIVE world, science freeze and review authority remain unchanged.

## Next

Use the high-strip fourth-moment/endpoint normalizer and the already proved onhour primal-dual Laurent pairing in a genuinely p-dependent signed low/middle/high WZ construction, retaining 2r/3r/4r cutoffs and the first/middle p² source carry. Start with exact original residues at p=13,19,373, and separate a candidate finite certificate from any universal proof. The frozen mother target W_(p-1)=p (mod p³) for p mod24∈{13,19} is open.

Native status carried from this run: Gateway 0.6.11 UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, quota 5/5; previous recovery/continuation bridge #6637/#6638 are preserved and not replayed; current native CLAIM, authorized OPEN, checkpoint, Result and mathematical admission not established.