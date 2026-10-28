# D25/LIFT GH-65/GH-66 — Integral F/G ports and global G-only operator

2026-10-29 Asia/Hong_Kong. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Research logical lane chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance lane. No native Researcher CLAIM, OPEN, Source checkpoint, Result, or review is implied.

For prime p=8m+3 >=11 and k=F_p, retain separate original ports:
\[
F_m(z)=\sum_{r=0}^m\frac{(-m)_r^2}{(2m+2)_r r!}z^r,\quad
G_m(z)=(16z\partial_z+5)F_m(z),\quad
D_m=\binom{3m+1}{m}.
\]
Inherited GH-56 Gauss operator: \(z(1-z)F''+(5-7z)F'/4-9F/64=0\) in k[z]. The open class-p=11(mod24) G_m(9)=0 hypothesis is NOT assumed.

## GH-65: exact integral source transport

**Theorem over integers for all m>=1:**
\[
D_mF_m(z)=\sum_{r=0}^m\binom mr\binom{3m+1}{m-r}z^r
=[x^m](1+x)^{3m+1}(1+zx)^m. \tag{65.1}
\]
\[
D_mG_m(z)=\sum_{r=0}^m(16r+5)\binom mr\binom{3m+1}{m-r}z^r
=[x^m](1+x)^{3m+1}(1+zx)^{m-1}(5+(16m+5)zx). \tag{65.2}
\]
**Proof:** The exact coefficient calculation is
\[
D_m\frac{(-m)_r^2}{(2m+2)_r r!}
=\frac{(3m+1)!\,m!}{r!(m-r)!^2(2m+1+r)!}
=\binom mr\binom{3m+1}{m-r}.
\]
Binomial expansion gives (65.1), then applying 16z∂_z+5 to each indexed source gives (65.2). Every rank and source weight is preserved. QED.

Since 3m+1<p, D_m is a unit modulo every p^a. Since 16m+5=2p−1≡−1 mod p,
\[
D_mG_m(9)=[x^m](1+x)^{3m+1}(1+9x)^{m-1}(5-9x)\pmod p. \tag{65.3}
\]
More generally, the new **finite-field coefficient/power-sum dual** is
\[
D_mG_m(z)=
-\sum_{x\in\mathbf F_p^\times}x^{-m}(1+x)^{3m+1}(1+zx)^{m-1}(5-zx),\ z\in k. \tag{65.4}
\]
**Proof:** The polynomial under the coefficient extractor has degree 4m+1 in x. In the power sum, the exponents p−1−m+j, 0<=j<=4m+1, lie strictly between 0 and 2(p−1); exactly j=m is divisible by p−1. Summation over nonzero field elements isolates minus this coefficient. QED. Formula (65.4) is a new exact arithmetic observer but is NOT yet an independently evaluated CM/Jacobi special-value certificate.

## GH-66: global scalar equation and all possible repeated roots

**Theorem in k[z]:**
\[
16z(1-z)G_m'=(1+7z)G_m+(z-5)F_m. \tag{66.1}
\]
\[
64z(z-1)(z-5)G_m''+
16(7z^2-56z+25)G_m'+9(z-21)G_m=0. \tag{66.2}
\]
**Proof:** Differentiate G=16zF'+5F, use the Gauss equation to substitute F'', obtaining \(G'=(1+7z)F'/(1-z)+9F/[4(1-z)]\). Replacing F' by (G−5F)/(16z) yields (66.1) after clearing denominators. Differentiating (66.1), eliminating F' and (z−5)F with the same identities, and clearing denominators gives (66.2). Polynomial identities hold also at z=0,1,5; the point 5 arises from scalar elimination, not a claimed new singularity of the original Gauss system. QED.

With \(G_m(z)=\sum_{n=0}^m b_nz^n\), and b_{−1}=b_{m+1}=b_{m+2}=0, coefficient comparison gives
\[
80(n+1)(4n+5)b_{n+1}
-(384n^2+512n+189)b_n+(8n-5)^2b_{n-1}=0
\quad(0\le n\le m+1). \tag{66.3}
\]
For 0<=n<m the forward multiplier is a p-unit, so b_0=5 uniquely generates the complete G port in O(m) finite-field operations without first computing F. The n=m+1 boundary is (8m+3)^2 b_m=p^2 b_m=0 in k.

**Repeated-root theorem:** F and G are coprime. G(0)=5≠0; G(1)=F(1)/2≠0 since \(F(1)=(3m+2)_m/(2m+2)_m\) is a p-unit. All G roots over the algebraic closure are simple except possibly 5. If G(5)=0, then
\[
G_m'(5)=0,\quad G_m''(5)=-F_m(5)/320\ne0, \tag{66.4}
\]
so 5 is exactly a double root. **Proof:** Ordinary-point uniqueness of the inherited Gauss equation and deg F=m<p force F-roots outside 0,1 to be simple; hence F and G cannot share a root. At any G root a not 0,1,5, (66.1) gives \(16a(1-a)G'(a)=(a-5)F(a)\ne0\). At a=5, (66.1) gives G'(5)=0; differentiating it gives \(-320G''(5)=F(5)\ne0\). QED. This global result does not recredit GH-56's earlier conditional local derivative at z=9.

## Evidence, limits and next action

A locally executed standard-library Python checker verified (65.1)-(65.2) for m=1..12 with five z values; (66.3) coefficientwise with independent recurrence recovery for ALL 310 primes p<10000, p=3 mod8; 108 power-sum/chart cases; and small-prime GCD classifications. Separately compiled native C++ modular code evaluated all 4494 primes p<=200000 with p=3 mod8 (none had G(5)=0) and 2250 primes p=11 mod24 (none had G(9)≠0). These are FINITE exact observations, not uniform proofs; no native p=373 H0/B0 experiment was run or replaced. Full proof, reproducible scripts, test log and SHA256 hashes were delivered in a portable same-turn ZIP; actual source-level GitHub admission still requires Source authorization and review.

BRC COMPOSE_APPLIED: immutable original rank r and integer source weights, the distinct F/G ports, coefficient and power-sum observers, differentiation and root multiplicity are retained. This auxiliary finite-field chart is not an X6 native position, full three-dimensional slice, original W/S, Hasse-6, R23/R36 or GH-20/21 second-digit record. ACTIVE P000/worldview unchanged.

**Next minimal science:** independently evaluate (65.4) at z=9 by a real CM/cubic/Jacobi-sum route, or establish its failure with a proven counterexample. Independently classify G(5), not by finite sampling alone. Preserve GH-3, second-digit, W/S, Hasse ports, R23/R36 and native experiments as separate OPEN obligations. Earlier GH-55..GH-64 are do-not-repeat.

At the observed Sites backend 0.6.11 status: research_authority_granted=false, executor_binding_configured=false, source_sync.control.state=CODE_REVIEW_REQUIRED, active_jobs=5/5; a standalone recovery_status operation was not available. Old service session, request and staging untouched. No session, CLAIM, OPEN, Source checkpoint, Result, HANDOFF or independent Driver review. Control issue enterprise-math#1558 remains responsible.