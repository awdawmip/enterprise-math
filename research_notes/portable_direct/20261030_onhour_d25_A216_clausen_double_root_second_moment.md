# D25 / SECOND-DIGIT-LIFT — finite Clausen square and nonzero second-moment jet (2026-10-30)

**Status:** AUTHOR-SIDE / ALL-PRIME ALGEBRAIC DERIVATION / EXECUTED FINITE-FIELD REGRESSION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
**Lane:** \`chatgpt-research-onhour-enterprise-math-20260923\` (TASK_RESEARCH), distinct from maintenance. **Task:** \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`. **Publication:** \`TP2-B6F4FC938FF94941C1B7\`. **Mother:** \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\`. Immutable scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`; P000/ACTIVE worldview unchanged.

## Exact original observer and all-prime polynomial identity

For every prime \(p=6m+1\ge7\), work in the finite field \(\mathbb F_p\), and define
\[
a_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\qquad
F_p(z)=\sum_{n=0}^{p-1}\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}z^n,
\qquad P_m(z)=\sum_{k=0}^{m}\binom mk\binom{2m}{k}z^k.
\]
All divisions are by \(p\)-units, and **the original source coefficient is exactly** \(a_n=[z^n]F_p(z)\,2^{-n}\) for \(0\le n<p\).

**Theorem (proved using the classical Clausen identity, not a newly asserted Clausen theorem):**
\[
\boxed{F_p(z)=P_m(z)^2\quad\text{in }\mathbb F_p[z].}\tag{1}
\]
Proof. In the classical exact Clausen identity
\[
{}_2F_1(a,b;a+b+1/2;z)^2
={}_3F_2(2a,a+b,2b;\;2a+2b,a+b+1/2;\;z),
\]
take \(a=-m,b=-2m\). The left Gauss function is a terminating polynomial of degree \(m\), and its denominator parameter \(1/2-3m=1-p/2\) reduces to \(1\pmod p\); its coefficients therefore reduce to \(\binom mk\binom{2m}k\). The right side terminates by its numerator \(-2m\), at \(n=2m\); its denominator parameters \(-6m=1-p\) and \(1/2-3m=1-p/2\) are \(p\)-units through \(n=2m<p\). Modulo \(p\), its numerator parameters \((-2m,-3m,-4m)\) become \((1/3,1/2,2/3)\), and both denominators become \((1,1)\). Thus its coefficients are those of \(F_p\) for \(0\le n\le2m\); all later coefficients of \(F_p\) vanish because \((1/3)_n\) contains the factor \(p/3\) for \(n\ge2m+1\). This establishes the entire polynomial identity, not only the evaluation at \(1/2\).

## Full moment observer and an exact nonzero second jet

Preserve the original \(n\)-labeled sources and signed operation \(6n+1\) by defining \(S_{j,p}=\sum_{n=0}^{p-1}n^j a_n\) for \(j=0,1,2\), with \(\theta=z\,d/dz\). Equation (1) yields
\[
S_{0,p}\equiv P_m(1/2)^2,\qquad
S_{1,p}\equiv P_m(1/2)P'_m(1/2)\pmod p.
\]
The terminating Gauss polynomial \(P_m={}_2F_1(-m,-2m;1;z)\) solves
\[
z(1-z)P_m''+[1+(3m-1)z]P_m'-2m^2 P_m=0.\tag{2}
\]
Every root \(z_0\in\mathbb F_p\setminus\{0,1\}\) is **simple**: if its multiplicity \(r\ge2\), then \(r\le m<p\), and the lowest-order coefficient of the left side of (2) is
\(z_0(1-z_0)r(r-1)c(z-z_0)^{r-2}\ne0\), contradiction.

Consequently, **if** \(P_m(1/2)=0\), the first two source moments vanish modulo \(p\), while the next observer does not:
\[
\boxed{S_{0,p}\equiv S_{1,p}\equiv0,\qquad
S_{2,p}\equiv \frac12[P'_m(1/2)]^2\ne0\pmod p.}\tag{3}
\]
Indeed, at this root \(\theta^2(P_m^2)=2z^2(P'_m)^2\), and \(z=1/2\). The result is an **exact double zero of the full original \(F_p\)**, not a blanket disappearance of all moment information. The hypothesis \(P_m(1/2)=0\) is explicit; no universal zero in the target classes is inferred solely from finite tests.

The already used Sun (2015) transfer \((S_{0,p}=0\bmod p)\Rightarrow(S_{0,p}=0\bmod p^2)\) is conditional on this mod-\(p\) antecedent. The accepted D24 \(A_p=S_0+6S_1\equiv p\bmod p^2\) then gives \(S_{1,p}\equiv p/6\bmod p^2\). On the frozen \(p\equiv13,19\bmod24\) classes, the still-open LIFT is exactly the **joint**, source-preserving \(U_p+6V_p=0\bmod p\), where \(U_p=S_{0,p}/p^2\) and \(V_p=(S_{1,p}-p/6)/p^2\) when these quotients are integral. Equation (3) neither proves the antecedent for all primes in those classes nor proves the \(p^3\) cancellation.

## Source-strength check on the CM/Hasse antecedent

Zhi-Hong Sun, *Congruences involving* \(\binom{2k}{k}^2\binom{3k}{k}\), *J. Number Theory* **133** (2013), §4, Theorem 4.5, establishes a \(216\)-denominator \(p^2\)-vanishing theorem for the residue classes \(p\equiv17,23\bmod24\) under the stated quadratic-character conditions. His Remark 4.3 states the wider \(\{13,17,19,23\}\bmod24\) vanishing assertion as a **conjecture**. In particular the 2013 Theorem 4.5 cannot be cited as proving our \(p\equiv13,19\bmod24\) antecedent. This is a precise historical source-strength boundary, not a claim that later literature could not have resolved it. The 2015 p² transfer is an implication, not an unconditional replacement for its antecedent.

Sources: 2013 paper https://maths.hytc.edu.cn/__local/D/38/C6/C84E91B123BC83FDB760DC8E718_C164339E_34F8B.pdf (Theorem 4.5 and Remark 4.3); Zhi-Hong Sun, *Note on super congruences modulo p²*, 2015, https://arxiv.org/abs/1503.03418.

## Executed finite regression and source bounds

The attached exact-standard-library program \`d25_a216_clausen_double_root_guard_20261030.py\` was executed on **all 115 primes** \(7\le p<1500,\ p\equiv1\bmod6\), including **60 frozen-class primes**. It compares every coefficient of the finite Clausen square against the independently generated original hypergeometric recurrence, and independently accumulates original A216 weighted \(n^0,n^1,n^2\) moments modulo \(p\). All 115 polynomial and moment identities passed; all 60 frozen-class samples have \(P_m(1/2)=0\) and \(P_m'(1/2)\ne0\). Fixed original-source witnesses:

| \(p\) | \(m\) | \(P_m(1/2)\) | \(P_m'(1/2)\) | \(S_0\) | \(S_1\) | \(S_2\) |
|---:|---:|---:|---:|---:|---:|---:|
|13|2|0|1|0|0|7|
|19|3|0|2|0|0|2|
|373|62|0|215|0|0|173|

The numerical check certifies this exact finite range, while (1) and (3) are all-prime algebraic theorems in their stated conditional domains. Program SHA256 \`9bbfb9b1b8e41bf814006da29715e412cce8bb1a05346404810a3f4fec5e8926\` (actual executed local file).

**BRC applied:** the retained carrier consists of exact original \(n\)-labeled coefficients over \(\mathbb Z_{(p)}\), valuation/moment jets \((S_0,S_1,S_2)\), signed \(6n+1\) observer, prime residue class and the future operation \(\theta^2\). Projection onto \(S_0\) or even \((S_0,S_1)\bmod p\) erases the provably nonzero \(S_2\) at each zero root; (3) is a concrete information-loss witness. This scalar arithmetic is an external finite-field calculation, **not** the native H0/B0, six-axis X6 or Heartbeat experiment.

## Recovery frontier and next exact action

**Preserve:** frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`, accepted D24 UR, source-verified earlier A216 regular terminating tail and two-moment decomposition; do not re-prove their completed subunits. This note is author-side, not Source Result/Review/claim/checkpoint.

**Unfinished math:** (a) locate or prove uniform \(P_m(1/2)=0\) for all frozen \(p\equiv13,19\bmod24\), with a current nonconjectural CM/Hasse certificate; (b) prove or refute the joint second digit \(U_p+6V_p\equiv0\bmod p\), using source-faithful mixed moment jets and regular middle tail. The polynomial square establishes a promising analytic route but is not the missing \(p^3\) proof.

**Native benchmark:** GitHub issue #1559 was observed OPEN and unassigned on 2026-10-30. The exact original-class \(p=373\) H0/B0 divided-power \([X]U\bmod139129\), actual rank and semilinear Frobenius/eta, odd signed Green/Hesse, \(\kappa\), original \(\Delta-R\), and independent replication remain pending authorized native execution and review. No scalar substitute is permitted.

**Control:** current Site readback on 2026-10-30 displayed \`research_authority_granted=false\`, \`write_relay_enabled=false\`; own checkpoint list returned \`ACCESS_DENIED\`. Actual Source session/CLAIM/run/request/recovery pointers are unknown and no own native permission is established. Preserve the stable Research lane ID; do not request maintenance claims, replay denied native writes, or create a competing selector dispatch. The author-side GitHub note and exact checker are durable research evidence only. \`REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / UNREVIEWED / NOT_ADMITTED\`.