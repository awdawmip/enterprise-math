# D25/SECOND-DIGIT-LIFT — Original Gosper regular forcing: low first jet and two high-sector unit transports

2026-10-24 | TASK_RESEARCH portable author proof, exact arithmetic self-check | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. No Source CLAIM, run, checkpoint, native benchmark, frozen Result, independent Driver review or mathematical admission is asserted.

**Mother:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3. Ordinary-control author-provenance lane: chatgpt-research-onhour-enterprise-math-20260923, not the separate maintenance lane. Project P000 remains ACTIVE_LOCKED. Global knowledge main@bdc4c6b8927afbdf4d031565b3bec53d95936bbc. Read-only Source head before this paper: 390d0e89ee9c9327d3c8f1a098b18a3a78945e48. Current control head and frozen scientific Source are **different pins**.

This paper consumes but does not repeat the [exact original-endpoint two-seam Gosper derivation](20261024_onhour_d25_original_endpoint_gosper_two_seam_p2.md) and the [new all-prime p² two-seam merger](20261024_onhour_d25_two_seam_exact_square_second_digit_merge.md). The original native target and its benchmark remain unchanged.

## 1. Exact original science target and inherited invariant

Let m>=1 and p=6m+1 be a prime. The **original** rational recurrence and Gosper forcing, valid before any modular reduction, are

\[
R_0=1,\qquad
\frac{R_{n+1}}{R_n}=
\frac{(4m+1+2n)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)},\quad
K_{p,n}=\frac{(2p+1-3n)(6n+2p+3)}
{(3n+p+2)(3n+2p+1)}.
\]

The previous exact result gives \(\mathcal K_p=\mathcal U_m+C_2T_2+C_4T_4\), with \(\mathcal U_m=\sum_{0\le n<4m,\ n\ne 2m}K_{p,n}R_n\); \(T_2=R_{2m}/p\) and \(T_4=R_{4m}/p\) are units, and \(C_4T_4\) ALREADY includes the original upper terminal. The completed seam merger proves

\[
C_2T_2+C_4T_4\equiv
B_m\left[1+\frac p9(28-6H_{2m}-12q_p(6))\right]\pmod{p^2},
\quad
B_m=\frac{(2m-1)!(2m)!}{(4m)!},\qquad
q_p(6)=\frac{6^{p-1}-1}{p}.
\]

With \(G_m=(-1)^m((2m)!)^3/((3m)!)^2\), the **unproved** full endpoint/LIFT objective remains equivalent to \(\mathcal U_m+\mathrm{MERGED\_SEAM}\equiv G_m\pmod{p^2}\). Nothing in this paper identifies native simulation with author arithmetic.

## 2. New all-target-prime theorem: low regular forcing is a terminal binomial first jet

For \(0\le n\le m\), define exact p-units

\[
b_n=(-1)^n2^{-n}\binom mn,\qquad
k_n=\frac{(1-3n)(6n+3)}{(3n+2)(3n+1)},
\]

\[
\epsilon_j=\frac3{6j+1}-\frac1{3j+2}-\frac2{3j+1},
\qquad
e_n=\sum_{j=0}^{n-1}\epsilon_j,
\]

\[
d_n=\frac2{1-3n}+\frac2{6n+3}-\frac1{3n+2}-\frac2{3n+1},
\qquad D_n=e_n+d_n .
\]

**Theorem LOW-JET** (all primes p=6m+1, all 0<=n<=m):

\[
\boxed{K_{p,n}R_n\equiv b_nk_n(1+pD_n)\pmod{p^2}.}\tag{LJ}
\]

Proof is termwise, not fitted from a finite experiment. Rewrite the **same original** ratio as

\[
\frac{R_{j+1}}{R_j}
=\frac{(6j+1+2p)(3j+1)(3j+2)}
{12(j+1)(3j+2+p)(3j+1+2p)},\quad
\frac{b_{j+1}}{b_j}=\frac{6j+1-p}{12(j+1)}.
\]

For \(j<n\le m\), the quotient of these two ratios equals \(1+p\epsilon_j\pmod{p^2}\). All denominators are p-units throughout this low range. Multiply these finite factors from j=0 and use R_0=b_0=1: \(R_n/b_n\equiv 1+pe_n\pmod{p^2}\). Likewise direct four-factor expansion of K gives \(K_{p,n}/k_n\equiv1+pd_n\pmod{p^2}\). Their product is (LJ). No p-factor was inverted.

Define the finite, explicitly computable rational sums

\[
A_m:=\sum_{n=0}^m b_nk_n,\qquad
J_m^{\mathrm{lo}}:=\sum_{n=0}^m b_nk_nD_n .
\]

Thus

\[
\boxed{\mathcal U_m^{\mathrm{lo}}:=\sum_{n=0}^m K_{p,n}R_n
\equiv A_m+pJ_m^{\mathrm{lo}}\pmod{p^2}.}\tag{LOW}
\]

## 3. New all-target-prime theorem: high p-units split into two different contiguous sectors

Retain original valuation \(v_p(R_n)=1\) for \(m<n\le 4m\), and let \(\xi_n=R_n/p\pmod p\), a unit. **Away from n=2m**, the original ratio reduces to

\[
\frac{\xi_{n+1}}{\xi_n}\equiv
\frac{n-m}{2(n+1)}\pmod p.
\]

At the special n=2m transition the exact original ratio has p/p cancellation. Reducing it *after* cancelling p gives

\[
\boxed{\xi_{2m+1}/\xi_{2m}\equiv-1/24\pmod p.}\tag{SEAM-JUMP}
\]

This is not the generic ratio! The inherited seam theorem supplies \(\xi_{2m}=T_2\equiv B_m\pmod p\). It follows by exact finite products that

\[
\boxed{\xi_{m+s}\equiv B_m\,a_{m,s},\quad
a_{m,s}=2^{m-s}
\frac{(2m)!(s-1)!}{(m+s)!(m-1)!},
\quad1\le s\le m,}\tag{HA}
\]

and

\[
\boxed{\xi_{2m+s}\equiv-\frac{B_m}{24}\,c_{m,s},\quad
c_{m,s}=2^{-(s-1)}
\frac{(2m+1)!(m+s-1)!}{m!(2m+s)!},
\quad1\le s\le2m.}\tag{HB}
\]

Proof: (HA) at s=m is 1. Recursing down from \(\xi_{2m}=B_m\) using ordinary ratio proves all HA. SEAM-JUMP gives HB at s=1. Recursing upward using ordinary ratio proves HB. All factorial arguments appearing in inversions are <p, so these are valid p-units. At n=4m, HB is an *internal consistency witness* for the seam/terminal inherited in the previous theorem; it does not insert the n=4m term again into regular forcing.

Mod p, the original K for the two high sectors is

\[
K_{p,m+s}\equiv
k^A_s:=\frac{4(1-2s)(3s+1)}{(2s+1)(6s+1)}
\quad(1\le s\le m-1),
\]

\[
K_{p,2m+s}\equiv
k^B_s:=\frac{(2-3s)(6s+1)}{3s(3s+1)}
\quad(1\le s\le2m-1).
\]

Both follow by substituting \(m\equiv-1/6\pmod p\) into the original numerator/denominator; their denominators are units for the displayed ranges. Consequently the **entire previously unresolved high ordinary forcing** has an explicit, two-sector finite certificate:

\[
\boxed{\frac{\mathcal U_m^{\mathrm{hi}}}{p}
\equiv B_m Z_m^{\mathrm{hi}}\pmod p,\quad
Z_m^{\mathrm{hi}}=
\sum_{s=1}^{m-1}a_{m,s}k^A_s
-\frac1{24}\sum_{s=1}^{2m-1}c_{m,s}k^B_s.}\tag{HIGH}
\]

The n=m+1 onset, omitted n=2m true pole, n=2m+1 unit jump, original n=4m/terminal combination, and *both* original high intervals are retained.

## 4. Exact equivalence: remaining LIFT is a single explicit rational finite sum

Reuse, rather than re-prove, the existing first-digit original endpoint identity together with the seam merger: \(A_m-G_m+B_m\in p\mathbb Z_{(p)}\). The two fractions below are therefore legal integral quotients. Inserting (LOW) and (HIGH) into the exact p² original-endpoint/seam equivalence proves, for every p=6m+1 prime, the **reduction theorem**

\[
\boxed{\mathrm{EP/LIFT}\iff\mathcal D_m^{\mathrm{finite}}\stackrel{?}{\equiv}0\pmod p,}\tag{R}
\]

\[
\boxed{
\mathcal D_m^{\mathrm{finite}}:=
\frac{A_m-G_m+B_m}{p}
+J_m^{\mathrm{lo}}
+B_m Z_m^{\mathrm{hi}}
+\frac{B_m}{9}\bigl(28-6H_{2m}-12q_p(6)\bigr).
}\tag{FIN}
\]

This is *not* a renaming of the already known regular forcing: (FIN) contains only explicit finite binomial coefficients, factorial ratios, rational functions and the known integer Fermat quotient. It no longer refers to any unknown regular \(R_n\), and it resolves the two high sectors with a **proved non-generic seam jump**. In the exact original problem it is still necessary to prove \(\mathcal D_m^{\mathrm{finite}}\equiv0\) for **all** target primes. Neither (R) nor the finite checks below discharge that obligation. No native experiment was run.

## 5. Executed exact author checks; coverage and nonclaims

The [companion reusable executable certificate](20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate_check.py) uses Python3 integers and modular inverses, never floating point. It independently reconstructs the *original* R_n as p-valuation and p-unit, checks (LJ) **term by term** and HIGH as a complete independent original high sum, verifies the first-digit prerequisite, then computes (FIN). Every one of the **80 primes p<=1000 with p≡1 mod6** passed. Of these, 45 lie in the task's two target congruence classes \(p\equiv13,19\pmod{24}\). The all-prime algebraic derivation of (LJ) and (HIGH) does not depend on 80-case extrapolation; finite checks are independent author self-checks only.

Actual residue witnesses (all listed components modulo p; their sum is 0 modulo p):

| p | (A-G+B)/p | low first jet J | high two-sector BZ | merged-seam correction | total |
|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 6 | 4 | 3 | 0 |
| 19 | 15 | 8 | 8 | 7 | 0 |
| 31 | 6 | 4 | 16 | 5 | 0 |
| 37 | 35 | 14 | 16 | 9 | 0 |
| 61 | 28 | 3 | 15 | 15 | 0 |

The high subtotal **alone is generally nonzero**. Replacing the two high sectors with 0, dropping the normalized n=2m seam, or claiming exact p² termwise equality where only p-unit transport is proved would be unsound. For future third digits, lift each stored p-unit modulo p² rather than assuming this p-only transport preserves higher precision.

## 6. Required handoff and admission status

- **BRC:** REUSE_APPLIED / COMPOSE_APPLIED. Carrier = signed original hypergeometric terms plus indexed p-valuation/p-unit and two seam labels. Observer = the original weighted endpoint after dividing once by p, to precision mod p². Lossless for this scalar through (R), not for future individual branch histories or third-digit operators. Native BRC executable was not invoked.
- **Previously completed, do not repeat:** D24 accepted supersingular UR; original Gosper exact identity; Morley normalization; square transport and p² seam merger. These author notes remain source-independent and do not modify the Source Result/claim/task selector.
- **New proven units:** low termwise first jet (LJ); exceptional normalized seam jump and closed two-sector high formula (HIGH); all-prime equivalence (R)/(FIN). Their proofs are author-side, unreviewed, not canonical acceptance.
- **Single smallest unfinished mathematical question:** derive a terminating contiguous-WZ/Gosper or binomial finite-difference identity proving (FIN) vanishes for all p=6m+1 in the selected target classes, or exhibit an exact nonzero obstruction; preserve B_m, both high sectors, and original terminal in any new certificate. Do not merely extend prime scans.
- **Genuine unperformed obligations:** same original native benchmark object/input/validation, Source Researcher identity/claim/open/checkpoint/Result, and independent Driver review. Native authority and benchmark are not inferred from GitHub commits.
- **Actual control support:** enterprise-math Issue #1539 remains OPEN for the original Research lane's failed registration/provisional ACTIVE state; old bridge #6186 (read-only unverified Source), #6187 (PREREQUISITE_NOT_SUCCEEDED), #6188 (FAILED TimeoutExpired) are **old IDs**, not commands to replay. Static Sites v0.6.11 presently returns research_authority_granted=false and executor_binding_configured=false; no role-bound write requested. Preserve old three staged UR items separately and the original task's time/phase/enabled/notification behavior.
