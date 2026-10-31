# D25/LIFT — all-prime second-digit reciprocal Clausen tail and two boundary source digits

2026-10-31 | TASK_RESEARCH portable author-side mathematics | logical conversation chatgpt-research-hourly-enterprise-math-20260923 (NOT the maintenance identity). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged. P000 ACTIVE_LOCKED premise maintained. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. All results below concern **external p-adic arithmetic**, not native X6 geometry.

## Specific increment and provenance

Consumed without recrediting: earlier all-prime mod-p reciprocal tail and differential walls in research_notes/portable_direct/20261031_hourly_d25_all_prime_reciprocal_p3_tail.md, and the p≡1(mod6) second-digit prime-index mirrors in research_notes/portable_direct/20261031_hourly_d25_lifted_prime_index_mirrors.md.

New here: the second-digit tail for the **complementary family p≡5(mod6)** including p=5, an all-prime polynomial transport at modulus p², and exact rational two-wall operator together with its two independent mod-p² source coefficients. The p≡1 weighted-tail values 373 and 1327 are *prior* results reused solely as regression anchors.

## Theorem — uniform modulo-p² mirrored tail

For a prime p≥5, put

\[
a_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3},\quad
h=\lfloor(p-1)/3\rfloor,\quad N=p-h.
\]

The existing exact valuation theorem gives v_p(a_{p-k})=3 and v_p(a_k)=0 for 1≤k≤h. All p³ divisions in this report are therefore p-integral. Set

\[
M_k=-18k^3a_k(a_{p-k}/p^3),\quad
q_p=(M_1-1)/p\pmod p,
\quad
H_k=\sum_{j=2}^{k}\left(
\frac2{2j-1}+\frac3{3j-1}+\frac3{3j-2}-\frac3{j-1}
\right).
\]

The all-prime Wilson endpoint gives M_1≡1(mod p). The coefficient recurrence

\[
a_{n+1}/a_n =
\frac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3}
\]

yields the **exact rational identity** (2≤k≤h)

\[
\boxed{\frac{M_k}{M_{k-1}}=
\frac{(1-p/(k-1))^3}
{(1-2p/(2k-1))(1-3p/(3k-1))(1-3p/(3k-2))}.}
\]

All reduced denominators are p-local units because k≤h≤(p-1)/3. Multiply the finite ratios and expand their factors to first order in p to obtain the **uniform transported coefficients**

\[
\boxed{M_k\equiv1+p(q_p+H_k)\pmod{p^2},\qquad
a_{p-k}/p^3\equiv-\frac{1+p(q_p+H_k)}{18k^3a_k}\pmod{p^2}.}
\tag{1}
\]

Consequently, as a **coefficientwise polynomial** identity in the p-local ring,

\[
\boxed{\frac1{p^3}\sum_{n=N}^{p-1}a_nX^n\equiv
-\sum_{k=1}^h\frac{1+p(q_p+H_k)}{18k^3a_k}\,X^{p-k}
\pmod{p^2}.}\tag{2}
\]

This is not an inference from a finite scan. It follows from the original coefficient recurrence, endpoint and p-local divisibility.

## Signed weighted tail, one higher digit

Retain the literal reflected weight 6(p-k)+1=1-6k+6p. Define

\[
Q_p^{[2]}=\sum_{n=N}^{p-1}(6n+1)a_n/p^3\pmod{p^2},
\quad B_p=\sum_{k=1}^h\frac{6k-1}{18k^3a_k}\pmod{p^2},
\]
\[
D_p=\sum_{k=1}^h\frac{(6k-1)H_k-6}{18k^3a_k}\pmod p.
\]

Then exact substitution in (1) gives

\[
\boxed{Q_p^{[2]}\equiv B_p+
p\big[q_p(B_p\bmod p)+D_p\big]\pmod{p^2}.}
\tag{3}
\]

The -6 inside D_p arises from the original 6p portion of the signed weight and is necessary at this precision. Multiplication by p³ supplies the original weighted high-tail remainder modulo p⁵.

For p=5, h=1 and 6(p-1)+1=25; although the **unweighted** p³-normalized coefficient is a unit, the weighted original tail is divisible by p⁵. Indeed q_5=2, B_5=5, D_5=4, and Q_5^[2]=0(mod25).

## Exact differential two-wall identity and second digits

Let \(\theta=X\,d/dX\),
\[
\mathscr L=\theta^3-\frac X2(\theta+\tfrac12)
(\theta+\tfrac13)(\theta+\tfrac23),\qquad
T_p(X)=\frac1{p^3}\sum_{n=N}^{p-1}a_nX^n.
\]

The same exact recurrence cancels **every interior coefficient over Q**, leaving only the two missing boundary neighbors:

\[
\boxed{\mathscr LT_p(X)=E_NX^N+E_pX^p,}
\]
\[
E_N=N^3(a_N/p^3),\qquad
E_p=-\frac{(2p-1)(3p-2)(3p-1)}{36}(a_{p-1}/p^3).
\tag{4}
\]

Use N=p-h, the k=h case of (1), and
\((2p-1)(3p-2)(3p-1)/36\equiv-1/18+13p/36\)
to obtain the two independent lifted boundary coefficients:

\[
\boxed{E_N\equiv
\frac{1}{18a_h}\left[1+p(q_p+H_h-\frac3h)\right]\pmod{p^2},}
\]
\[
\boxed{E_p\equiv-\frac1{18}
+p\left(\frac{13}{36}-\frac{q_p}{18}\right)\pmod{p^2}.}
\tag{5}
\]

The mod-p parts were known; the p² values are new for the complementary family and, as boundary calculations, also provide second-digit information for all p≥5. They should not be collapsed merely because the interior operator is the same.

## Executed exact evidence

Actual standard-library verifier: research_notes/portable_direct/d25_all_prime_second_digit_tail_check_20261031.py, Git blob 6bc3e6e7b10266a03bfb8f010bdb1c27f8a0d228; local SHA256 fbe74d189924ee608bb17b150c676ddb239c1b90bf880e661a024f06907ba554. Exact test logfile SHA256 cfd7ba2383d981fb4c164806dfb8b599d77cb313401e9415318147705e2b55e3.

Executed for 428 primes 5≤p≤3000: 221 p≡5(mod6), 207 p≡1(mod6); 197723 mirrored original coefficient comparisons, 428 weighted modulo-p² tails, 856 p² boundary checks; 8 additional exact Q-rational operator checks and 9 direct integer-binomial anchors. All passed: PASS_D25_ALL_PRIME_P2_LIFTED_CLAUSEN_TAIL_TWO_BOUNDARIES_EXACT. No float arithmetic.

Anchors (p,h,q_p,B_p,D_p,Q_p^[2],E_N,E_p) where D is mod p and other output residues mod p²:
(5,1,2,5,4,0,21,13);
(11,3,8,94,5,72,120,36);
(17,5,14,18,7,86,254,33);
(23,7,8,460,17,322,222,336);
(373,124,170,6992,13,109567,10399,108688);
(1327,442,993,1557898,67,1646807,1371754,563164).

Proof is the exact recurrence; finite tests are implementation/certificate evidence only. No native divided-power/Frobenius experiment, Lean checker, mathematical review or formal result admission has been performed.

## BRC interface / frozen objective / next action

BRC COMPOSE_APPLIED, observer scope = polynomial coefficients mod p², original signed scalar at X=1, and third-order differential boundary sources. The exact carrier retains p, original index n, reverse index k, p-valuations, original rational coefficient, original weight, q_p, H_k, first and terminal walls. This specific transport uses both endpoint and path information; no universal minimality or X6-native transfer is claimed.

The D25 hard target remains to prove the original signed residual C+L-J+I≡0(mod p) for **every** p mod24 in {13,19}, hence A_p≡p(mod p³), with frozen source and original 216 parameter X=1. Next discriminating unit: identify a finite WZ/CM relation that couples the low/middle valuation-wall contributions to the signed residual and test whether the two new p² wall coefficients admit a closed relation to the existing Clausen/CM jets. Do not recredit the prior p≡1 mirror lift.

The 2026-10-31T03:19Z Gateway 0.6.11 status snapshot 4429e0065fe66a78ea6b1fb3bc1a6a50b5781842a6b8570affc85222b7814da7 reported research_authority_granted=false; executor_binding_configured=false; active native jobs=5/5; new_job_allowed_by_quota=false; source control CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Historical own recovery/continuation #6424/#6425 from 2026-10-25 were read and showed no authorized run; they are not fresh ownership. Existing control owner issue awdawmip/enterprise-math#1558 covers session transition/claim recovery; native 373 experiment #1559. No maintenance-conversation writes, new session, CLAIM, OPEN, source checkpoint, Result, review or staging mutation occurred here.
