# D25/LIFT GH-58–GH-59 — First Frobenius boundary gate for labeled Gauss F/G ports

Date: 2026-10-28 Asia/Hong_Kong. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** Not a native CLAIM, RUN, checkpoint or mathematically admitted Result.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION (OPEN).
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923 (not the maintenance conversation). Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged. ACTIVE P000/worldview unchanged.

## Input, notation and exact question

For any prime p=8m+3 >=11, let k=F_p, retain GH-55–GH-57's **labeled** original ports
\[
F_m(z)=\sum_{r=0}^{m}\frac{(-m)_r^2}{(2m+2)_r r!}z^r,\qquad
G_m(z)=(16z\partial_z+5)F_m(z).
\]
The Gauss equation already proved in GH-56 is
\[
{\mathscr D}Y=z(1-z)Y''+(5/4-7z/4)Y'-9Y/64=0. \tag{58.0}
\]
This research asks whether local jets at z=9 alone force the open G-port vanishing for all p=11 mod24, and what the *first missing global compatibility* condition actually is. We separate GH-58 (a local no-go) from GH-59 (an operator-derived characteristic-p global boundary). Neither proves the all-prime G-port identity or original GH-3 truncated sum.

## GH-58 — exact ordinary-point recurrence and insufficiency theorem (PROVED)

Write w=z-9 and Y(9+w)=sum_{n>=0} a_n w^n. The entire coefficient recurrence of (58.0), interpreted as a formal-series identity, is
\[
\boxed{
72(n+1)(n+2)a_{n+2}
+\frac{(n+1)(34n+29)}2a_{n+1}
+\left(n+\frac38\right)^2a_n=0.}
\tag{58.1}
\]
**Proof.** In the new chart, z(1-z)=-72-17w-w² and 5/4-7z/4=-29/2-7w/4. Extract the coefficient of w^n and multiply by -1. Its final coefficient is n(n-1)+7n/4+9/64=(n+3/8)². This proves (58.1).

Since 72(n+1)(n+2) is a p-unit at *every* n=0,...,p-3, the recurrence through degree p-3 determines coefficients a_2,...,a_{p-1} uniquely from **any** initial labeled observation
\[
u=Y(9),\qquad v=(16zY'+5Y)_{z=9},\qquad
a_0=u,\quad a_1=(v-5u)/144.
\tag{58.2}
\]
Thus these p-2 ordinary-point equations alone cannot impose an algebraic relation between u and v. This precise limitation does not exclude the resonant equation n=p-1, a CM or Frobenius identity, a prime-dependent WZ certificate, or an independent arithmetic statement.

**Witness:** p=11, (u,v)=(1,1) produces a consistent low-order local jet through w^10 but does not satisfy the next compatibility gate: its obstruction is 7 (mod 11). It is a jet, **not** a full polynomial or formal-power-series solution.

## GH-59 — terminal Frobenius obstruction selects exactly the rank-m global polynomial (PROVED)

Let a_{p-1}(u,v) denote the terminal coefficient uniquely supplied by GH-58's recurrence. Define
\[
A_p=a_{p-1}(1,0),\quad
B_p=a_{p-1}(0,1),\quad
\boxed{\mathfrak O_p(u,v)=A_pu+B_pv.}
\tag{59.1}
\]
**Theorem.** A true solution Y in k[[z-9]] of \mathscr D Y=0 must satisfy \mathfrak O_p(u,v)=0. Conversely, that condition is sufficient for the jet to yield an exact polynomial solution of degree <=m. That polynomial must be a scalar multiple of the already proved F_m. Consequently
\[
\boxed{
\ker\mathfrak O_p=k\cdot(F_m(9),G_m(9)),
\qquad (A_p,B_p)\ne(0,0).}
\tag{59.2}
\]

**Proof of necessity.** At the first resonant coefficient n=p-1 of (58.1), terms involving a_{p+1} and a_p have a factor p and disappear. The surviving factor on a_{p-1} is (-1+3/8)²=25/64, a p-unit for all admissible primes. Therefore a_{p-1}=0.

**Proof of sufficiency.** Assume a_{p-1}=0. At n=p-2 the a_p coefficient also vanishes and the a_{p-1} term is zero; hence (-2+3/8)² a_{p-2}=169 a_{p-2}/64=0. Since the admissible primes are 3 mod 8 and hence exclude 13, a_{p-2}=0. Descending from n=p-3 through n=m+1, if a_{n+1}=a_{n+2}=0, (58.1) reduces to (n+3/8)²a_n=0. In that interval 8n+3 is nonzero modulo p: the only nonnegative root below p is n=m=(p-3)/8. Therefore a_{m+1},...,a_{p-1}=0. The remaining polynomial \sum_{n=0}^m a_nw^n satisfies every coefficient of \mathscr DY=0, since at n=m the last factor vanishes and all further coefficients are zero.

**Uniqueness and nonzero selector.** For a polynomial Y(z)=\sum_{r=0}^m b_rz^r, equation (58.0) gives at z=0
\[
(r+1)(r+5/4)b_{r+1}=(r+3/8)^2b_r\quad(0<=r<m).
\tag{59.3}
\]
All leading coefficients are p-units. Thus b_0 determines the polynomial; the nonzero original GH-22 F_m is such a solution, so the polynomial solution space has dimension one. If A_p=B_p=0, two independent initial pairs would produce two independent polynomial solutions by sufficiency, contradiction. The port expression follows from (58.2). QED.

### Source-separated O(p) algorithm and exact experimental certificates

Calculate A_p,B_p using only the ordinary-point operator recurrence (58.1) for the two port basis vectors. It uses O(p) exact field operations and **does not consume** original GH-22 hypergeometric coefficients; those provide an independent rank-labeled verification of A_pF_m(9)+B_pG_m(9)=0. The source-typed observer retains the difference between F and G and distinguishes a local jet from a globally compatible solution.

The companion Python standard-library checker, executed with exact integers and modular inverses, passed **all 310 primes** 11<=p<10000, p=3 mod8. It independently generated A_p,B_p and F_m,G_m, checked the nonzero selector and its kernel, and found the following **finite observations** (not all-prime theorems):
- 155/155 primes p=11 mod24: A_p=0, B_p≠0, F_m(9)≠0, G_m(9)=0.
- 155/155 primes p=19 mod24: A_p≠0, B_p=0, F_m(9)=0, G_m(9)≠0.

| p | A_p | B_p | F_m(9) | G_m(9) |
|---:|---:|---:|---:|---:|
| 11 | 0 | 7 | 6 | 0 |
| 19 | 9 | 0 | 0 | 5 |
| 43 | 41 | 0 | 0 | 6 |
| 59 | 0 | 14 | 21 | 0 |
| 67 | 19 | 0 | 0 | 33 |
| 83 | 0 | 1 | 32 | 0 |

The class p=19 mod24 has an existing **independent prior author derivation** GH-32 of F_m(9)=0; this paper does not re-prove it. The class p=11 mod24 remains OPEN: proving the exact operator-derived scalar A_p=0 for *all* such primes, e.g. through independently normalized Frobenius/finite character sum/CM evaluation, would imply G_m(9)=0 by (59.2), but currently its evidence is finite.

**Negative extension witness.** The superficially analogous composite-modulus statement is false: choose m=37 and N=299=13·23≡11 mod24, so 2 and 9 are units. The exact rational even-Legendre observer
\[
[tP'_{74}(t)-P_{74}(t)]_{t^2=8/9}\equiv250\pmod{299}\ne0.
\]
This is computed by the exact binomial expansion for P_{74}, with no floating-point arithmetic, and is **not** a counterexample to the prime conjecture.

**BRC COMPOSE_APPLIED:** population is the original finite-field rank/port-labeled signed coefficients; the observable state is (u,v), and the operation-sensitive *repair coordinate* is the additional Frobenius compatibility scalar \mathfrak O_p. Retain observer z=9, formal-jet order, distinct F/G labels, coefficient provenance, and future differentiation/global polynomial comparison. Total-only compression that omits the selector is not safe for those future operations. This finite-field auxiliary chart is *not* native X6, not a three-dimensional native slice, not a native W/S or six-Hasse transfer, and not an assertion that signed cancellations are positive BRC masses.

## Next minimum and control/readback boundary

Next exact mathematical obligation: independently prove or refute A_p=0 uniformly for p=11 mod24 using a properly normalized Frobenius/CM/character sum object. Do not recast the original defining G-port sum or more differentiated low-order equations as independent proof. Separately retain GH-3 original truncation, GH-20/21 second-digit matrix/jet matching, W/S, six native Hasse, R23/R36 Green, eta/kappa and native p=373.

Native status during author work: backend 0.6.11, Research authorization false, executor binding false, Source control CODE_REVIEW_REQUIRED, Site write relay false. No accessible recovery_status in this connector; previous exact continuation attempt returned INVALID_ARGUMENT / CONTROL_QUOTA and was not blindly replayed. Historical Source checkpoint/session/staging/requests/claims and contribution history preserved. Existing control-owner support: awdawmip/enterprise-math#1558. No new native session, CLAIM, OPEN, execution checkpoint, Result, freeze or review was performed; this is **portable GitHub author evidence only**.

Program file: research_notes/portable_direct/20261028_hourly_d25_gh58_gh59_frobenius_boundary_check.py. Program Git blob SHA-1 (matches actual executed file): 5d747ea1beada838a886a6743a346bdf825ee062.
