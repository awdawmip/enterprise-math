# D25 — wall-graded finite Green certificate and a single-boundary reduction

Date: 2026-11-04, Asia/Hong_Kong. AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF IN DECLARED SCOPE / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical conversation chatgpt-research-hourly-enterprise-math-20260923; maintenance chatgpt-hourly-enterprise-math-20260921 is distinct. No verified native Research claim/run is asserted.

This note uses the earlier dual Picard–Fuchs forcing and the independently authored exact Green adjoint (research_notes/portable_direct/20261104_onhour_d25_exact_green_adjoint_signed_transport.md); they are prerequisites, not re-claimed novelty. New increments: the six-channel p-adic wall filtration, finite boundary telescope reducing the two-wall channel to one lower-boundary mismatch, and the special-root separation of the one-wall source.

## 1. Original carriers and exact Green identity

Let p=6r+1>=7 be prime, N=p-1. Work over Z_(p) and reduce modulo p^3 where stated. Define original indexed, source-labelled coefficients

\[
a_j=\frac{(2j)!(3j)!}{(j!)^5 216^j},\qquad
b_j=\frac{(4j)!}{(j!)^4 2304^j},
\quad
\rho_j=\frac{(4j+1)(4j+2)(4j+3)}{576(j+1)^3},
\quad
\gamma_j=\frac{(2j+1)(56j(j+1)+13)}{288(j+1)^3},
\quad f_j=a_j\gamma_j.
\]

The exact original coefficient recurrences give a_(j+1)=(rho_j+gamma_j)a_j, b_(j+1)=rho_j b_j. With w_n=6n+1, K_j=sum_(n=j+1)^N w_n prod_(i=j+1)^(n-1)rho_i, the existing finite Green theorem states

\[
W_{216}(N)-V_{2304}(N)=
\sum_{j=0}^{N-1} f_jK_j-2\sum_{n=0}^{N}n b_n. \tag{1}
\]

The quartic original observer has weight 8n+1. The exact p-cutoff forcing from the previous dual PF identity is retained as its own source; (1) is the endpoint-terminated finite solution, not an infinite approximation.

## 2. New theorem: exactly three quartic walls yield six surviving channels

Set beta_1=floor(p/4)+1, beta_2=(p+1)/2=3r+1, beta_3=floor(3p/4)+1. For 1<=n<p,

\[
v_p(\rho_{n-1})=1 \ \text{iff}\ n\in\{\beta_1,\beta_2,\beta_3\};
\quad v_p(\rho_{n-1})=0\ \text{otherwise}.
\]

Proof: v_p(b_n)=floor(4n/p), since n! and 2304 are p-units and 4n<p^2, and the successive jumps occur at those three indices.

Also v_p(a_j)=floor(2j/p)+floor(3j/p) for j<p. All denominators of gamma_j are p-units for j<=p-2, so the exact source valuation is

\[
e_j=v_p(f_j)=\lfloor2j/p\rfloor+\lfloor3j/p\rfloor+
v_p((2j+1)(56j(j+1)+13)). \tag{2}
\]

Define K_j^[m] by restricting K_j to summands with exactly m quartic walls between j+1 and n, i.e., floor(4n/p)-floor(4(j+1)/p)=m. Every such product has valuation m, hence K_j^[m] is divisible by p^m.

The wall-filtered kernels have a three-state, O(p)-operation backward recurrence. At j=N-1, K_j^[0]=w_N and K_j^[1]=K_j^[2]=0; for j<N-1 put z_j=v_p(rho_(j+1)), then

\[
K_j^{[m]}=\mathbf1_{m=0}w_{j+1}
+\mathbf1_{m\ge z_j}\rho_{j+1}K_{j+1}^{[m-z_j]},\qquad m=0,1,2.\tag{3}
\]

For e+m<=2 let C_(e,m)=sum_(0<=j<=p-2,e_j=e) f_j K_j^[m] (mod p^3).
Also let Q_d=2 sum_(1<=n<p,floor(4n/p)=d) n b_n, d=0,1,2.
By exact valuation filtration of (1),

\[
\boxed{
W_{216}(p-1)-V_{2304}(p-1)\equiv
C_{0,0}+C_{0,1}+C_{0,2}+C_{1,0}+C_{1,1}+C_{2,0}
-Q_0-Q_1-Q_2\pmod{p^3}.}\tag{4}
\]

The six cells form the triangular p-adic carrier e+m<=2; discarded terms have an exact valuation reason. Each source index and signed observable remains recoverable up to the chosen precision. This is a for-all-primes reduction, not a proof of eventual scalar zero.

## 3. New theorem: the two-wall channel is one boundary mismatch times one tail

Write P_j(B)=prod_(i=j+1)^(B-1)rho_i for j<B-1. Define quartic unit tails

\[
T_0=\sum_{n=\beta_1}^{\beta_2-1}w_n\prod_{i=\beta_1}^{n-1}\rho_i,\quad
T_1=\sum_{n=\beta_2}^{\beta_3-1}w_n\prod_{i=\beta_2}^{n-1}\rho_i,\quad
T_2=\sum_{n=\beta_3}^{p-1}w_n\prod_{i=\beta_3}^{n-1}\rho_i.
\]

Two-wall paths with e_j=0 have only two possibilities:
j<=beta_1-2 ending beta_2<=n<beta_3, or beta_1-1<=j<=2r ending beta_3<=n<p.

The elementary source telescope is exact over Q for J<=K<B-1:
\[
\sum_{j=J}^{K}f_jP_j(B)=a_{K+1}P_K(B)-a_J\rho_JP_J(B). \tag{5}
\]

Proof: f_j=a_(j+1)-rho_j a_j, and rho_j P_j(B)=P_(j-1)(B). The sum cancels adjacent terms.

For the later family set J=beta_1-1, K=2r, B=beta_3. Its first endpoint has v_p(a_(2r+1))=1 and two crossed quartic walls; the second endpoint has three crossed walls. Therefore the whole later part is 0 modulo p^3. Restoring sources with e_j>0 to this family's sum does not change it mod p^3 (their paths already have two walls).

For the early family set J=0, K=beta_1-2, B=beta_2. Equation (5) and a_0=b_0=1 give
\[
\sum_{j=0}^{\beta_1-2} f_jP_j(\beta_2)
=a_{\beta_1-1}P_{\beta_1-2}(\beta_2)-b_{\beta_2}
=b_{\beta_2}\left(\frac{a_{\beta_1-1}}{b_{\beta_1-1}}-1\right).
\]
Here b_(beta_1-1) is a unit, so this ratio is legitimate in Z_(p). Omitting e_j>0 sources changes the early two-wall channel only by p^3 multiples.

Consequently the new closed boundary certificate is

\[
\boxed{C_{0,2}\equiv
b_{\beta_2}\left(\frac{a_{\beta_1-1}}{b_{\beta_1-1}}-1\right)T_1
\pmod{p^3}.}\tag{6}
\]

This replaces a double-index two-wall response by one early coefficient mismatch and one shared quartic tail, while preserving their separate sources.

## 4. New theorem: one-wall exceptional early roots must stay distinct

Define X_(1,0)=sum_(j<=beta_1-2,e_j=1) f_jP_j(beta_1), and
X_(1,1)=sum_(beta_1-1<=j<=beta_2-2,e_j=1) f_jP_j(beta_2).
Both belong to p^2 Z_(p). Exact wall separation yields

\[
\boxed{C_{1,1}=X_{1,0}T_0+X_{1,1}T_1\pmod{p^3}.}\tag{7}
\]

The early X_(1,0) records zeros of the numerator quadratic 56j(j+1)+13 in the first quartic interval. For p=13, X_(1,0)/p^2=7 mod 13; omitting this independent source gives a false channel equality.

## 5. Executed exact tests and discriminating example

The companion Python standard-library checker reconstructs both original coefficient families, source-graded Green recurrence, all three walls, the six source channels, the quartic 3-band correction, boundary telescope (5), and formulas (6)–(7). All 148 primes p=6r+1 with 7<=p<=2000 passed. For p=13,19,97,373 every original coefficient was also independently reconstructed from factorial/binomial representations.

| p | C_(0,2) mod p^3 | C_(1,1) mod p^3 | T0,T1,T2 mod p | W216-V2304 mod p^3 |
|---|---:|---:|---|---:|
| 13 | 169 | 507 | 5,11,11 | 0 |
| 19 | 5054 | 6137 | 3,12,8 | 0 |
| 97 | 0 | 0 | 3,0,70 | 0 |
| 373 | 11825965 | 16278093 | 355,194,290 | 0 |

At p=97 the shared T1 is zero mod 97; the early exceptional X_(1,0) source is absent, so both C_(0,2) and C_(1,1) vanish mod p^3. T2 remains nonzero (70 mod 97), confirming that the later two-wall disappearance is supplied by the exact telescope rather than an assumed third-tail zero. This is a finite instance diagnosing the mechanism, not a general zero theorem.

BRC reuse: COMPOSE_APPLIED. Exact signed source and provenance (family, index, valuation), future operation (Green), filtration by quartic crossing count and precision horizon p^3 are retained. No positive-mass collapse, unproved native X6 transfer, or fixed-373 native experiment is claimed.

## 6. Next unresolved step and Source boundaries

Seek a uniform finite WZ/hypergeometric pairing of C_(0,0), C_(0,1), C_(1,0), C_(2,0), exceptional X_(1,0)T0, and the three Q_d, using (6) directly. Test the distinct mechanisms at p=13,19,97,373 before claiming a universal cancellation. The signed scalar congruence for p mod24 in {13,19} and the frozen D24 Delta_p-R_p second-digit bridge remain independent open obligations.

Live Gateway em_status observed 2026-11-04: 0.6.11, UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5. No new native Research session, claim, run, checkpoint, Result, or review is claimed. Original protected requests and staging remain untouched. Control recovery stays with existing maintenance support #1558; the native fixed-373 benchmark remains with #1559. The research note and test are author-side pending native intake.