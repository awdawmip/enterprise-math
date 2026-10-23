# D25/LIFT — Exact two-seam transfer and one-seam mod-p² certificate

2026-10-24 | TASK_RESEARCH, independent portable mathematical author evidence.
**Status: AUTHOR-PROVED EXACT IDENTITY; MOD-p² DERIVATION; FINITE EXACT CHECK; UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT.**
This file is not a native benchmark, Researcher CLAIM, authorized run, Source checkpoint, Result/freeze, or independent Driver review.

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7. Original task source pin: **c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged)**.
Logical lane: chatgpt-research-hourly-enterprise-math-20260923, separate from chatgpt-hourly-enterprise-math-20260921 (maintenance) and other Research lanes. The last independently evidenced successor Researcher registration was EM-DIRECT-211CEB / MCP-cf39e84761fa4092a3600450d8aad3ab (support #1558); **no fresh winning claim/run was obtained in this turn**. On this turn the native em_status request was not sent upstream: BACKEND_IDENTITY_CHECK_UNAVAILABLE / operation_sent=false. Mathematical derivation below is neutral portable evidence only.
Global rules: GLOBAL_KNOWLEDGE_V1 main@11f9d30dffa56c0be5bfc4f7f362c9b4558a2f62; P000 ACTIVE_LOCKED. Current research-repository evidence compared against main@070a56781c04c99167d20e6494350ace701bb013, without changing the frozen task source pin.

## Question, exact carrier and predecessor

The prior original-endpoint work [original two-seam paper](20261024_onhour_d25_original_endpoint_gosper_two_seam_p2.md) established, for p=6m+1 prime and m>=1,

\[
\mathcal K_p
=\sum_{\substack{0\le n<4m\\n\ne2m}} K_{p,n}R_n
+\frac{(p+2)(4p+1)}{3(2p+1)}T_2
+\frac{-8p^2+14p-3}{4p-1}T_4,
\quad
T_2=\frac{R_{2m}}p,\ T_4=\frac{R_{4m}}p
\]
and that the still-open original LIFT/EP target is equivalent to
\[
\mathcal K_p\equiv G_m \pmod{p^2},\qquad
G_m=(-1)^m\frac{((2m)!)^3}{((3m)!)^2}.
\]
Here R_0=1 and
\[
\frac{R_{n+1}}{R_n}=
\frac{(4m+2n+1)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)}.
\]
Previous work separately proved T_2,T_4 are p-adic units, and both seam contributions are nonzero modulo p. **Neither seam is dropped.** The new unit derives an exact dependence between their p-adic coordinates.

## Theorem 1: all-m exact seam-transfer product

For **every integer m>=1**, with p=6m+1 (even when p is composite), there is an exact identity in rational numbers:
\[
\boxed{
\frac{R_{4m}}{R_{2m}}
=\frac{1}{9\,6^{p-1}}
\left[\prod_{j=2m}^{6m-1}\left(1+\frac pj\right)\right]^2.
}\tag{ST-exact}
\]
The identity is not merely a congruence.

**Proof.** The recurrence above has the finite factorial solution
\[
R_n=\frac{(4m+2n)!\,((2m)!)^2\,(3n)!}
{216^n\,((2m+n)!)^2\,(n!)^2\,(4m+n)!}.
\]
Indeed the successive ratio of this expression is the displayed recurrence, and at n=0 its value is one. In particular
\[
R_{2m}=\frac{(8m)!}{216^{2m}((4m)!)^2},
\quad
\frac{R_{4m}}{R_{2m}}
=\frac1{216^{2m}}
\left[\frac{(12m)!(2m)!}{(6m)!(8m)!}\right]^2.
\]
Since p=6m+1, split the factorials **exactly**, not by replacing p+j with j:
\[
\begin{aligned}
\frac{(12m)!(2m)!}{(6m)!(8m)!}
&=\frac{(2m)!}{(6m)!}\prod_{j=2m}^{6m-1}(p+j)\\
&=\frac13\prod_{j=2m}^{6m-1}\left(1+\frac pj\right).
\end{aligned}
\]
Finally 216^{2m}=6^{6m}=6^{p-1}, which proves ST-exact. No modular division was used.

## Theorem 2: second-digit transfer and *combined* seam coefficient

Suppose p=6m+1 is prime. Put the integer Fermat quotient
\[
q_p(6)=\frac{6^{p-1}-1}{p}
\]
and the finite p-integral harmonic segment
\[
D_m=\sum_{j=2m}^{6m-1}\frac1j
=H_{6m-1}-H_{2m-1}.
\]
All j in this sum are less than p. Expanding ST-exact in \(\mathbb Z_{(p)}/p^2\) gives
\[
\boxed{T_4\equiv\frac{T_2}{9}
\left[1+p(2D_m-q_p(6))\right]\pmod{p^2}.}\tag{ST-p2}
\]
The unit property of T_2 and T_4 is inherited from the prior exact valuation theorem, not deduced from numerical samples.

In particular, because H_{p-1}=0 mod p by reciprocal pairing, H_{p-2}=1 mod p; also (2m)^{-1}=-3 mod p. Thus
\[
D_m\equiv 1-(H_{2m}+3)=-2-H_{2m}\pmod p,
\]
and ST-p2 can equivalently use \(2D_m-q_p(6)\equiv-4-2H_{2m}-q_p(6)\pmod p\).

Expand the **existing** lower and upper seam coefficients without omitting either:
\[
\frac{(p+2)(4p+1)}{3(2p+1)}
\equiv\frac23+\frac53p,\qquad
\frac{-8p^2+14p-3}{4p-1}\equiv 3-2p\pmod{p^2}.
\]
Inserting ST-p2 and collecting exactly one scalar coefficient yields
\[
\boxed{
\frac{(p+2)(4p+1)}{3(2p+1)}T_2
+\frac{-8p^2+14p-3}{4p-1}T_4
\equiv T_2\left[
1+p\left(\frac19-\frac23H_{2m}-\frac13q_p(6)\right)
\right]\pmod{p^2}.}\tag{SEAM-ONE}
\]
At the first digit this says precisely \((2/3)T_2+3T_4\equiv T_2\pmod p\); no seam vanishes independently.

Consequently the **same still-open original second-digit problem** has the strictly smaller exact-observer congruence target:
\[
\boxed{
\sum_{\substack{0\le n<4m\\n\ne2m}} K_{p,n}R_n
+T_2\left[
1+p\left(\frac19-\frac23H_{2m}-\frac13q_p(6)\right)
\right]
\stackrel{?}{\equiv}
(-1)^m\frac{((2m)!)^3}{((3m)!)^2}
\pmod{p^2}.}\tag{ONE-SEAM-P2}
\]
This is equivalent to the old TWO-SEAM-P2, *not* a proof that it holds. The regular forcing sum and p² cancellation remain open. Exact ST-exact should be retained if a p³ or higher observer is later requested.

## Independent exact-arithmetic author validation and boundaries

Using Fraction/integer arithmetic for the **original** R_n recurrence, ST-exact was tested exactly at m=1,...,7. With factorial Fraction arithmetic, ST-p2 and SEAM-ONE were tested at every prime p=6m+1 for 1<=m<=24, namely
p=7,13,19,31,37,43,61,67,73,79,97,103,109,127,139.
All 15 passed; this is author finite self-check, not a native test or independent acceptance.

Distinct nontrivial modular witnesses (p; T_2 mod p²; T_4 mod p²; combined seam mod p²; correction coefficient mod p):
(7;38;40;45;5), (13;28;123;106;3), (19;280;86;147;9), (31;86;819;706;6).
The **proof** of ST-exact and SEAM-ONE is the displayed rational-product algebra and prime-local expansion; the finite checks are additional error detection only.

Typed BRC reuse: signed original hypergeometric branches with n, exact weight R_n, p-valuation+unit, observer \(\bmod p^2\), operation of summing through 4m, and both labeled seams were retained. At this particular scalar observer, the upper seam coordinate is reconstructible from the lower seam by ST-p2; the seam labels remain recoverable via ST-exact. This is **REUSE_APPLIED / COMPOSE_APPLIED**, not a positive-mass theorem or a native-X6 transfer.

**Next precise mathematics:** Evaluate the uncollapsed regular forcing sum in ONE-SEAM-P2 by a source-matched terminating finite-difference / contiguous-WZ identity with correct endpoints, and prove or disprove its cancellation against G_m for all p=6m+1. Do not search again for the now disproved universal exact rational one-term Gosper primitive. No current Source CLAIM, run, publication checkpoint or mathematical admission is asserted. Submit through original lawful continuation once control transport is restored; support: enterprise-math#1558.