# D25/LIFT — Exact seam-to-target normalization and regular-forcing-only mod-p² target

2026-10-24 | TASK_RESEARCH / portable author result / **AUTHOR-PROVED TWO EXACT FACTORIAL-PRODUCT RELATIONS AND p² CONSEQUENCES / UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.
This is a separate mathematical unit continuing [the exact two-seam transfer](20261024_hourly_d25_two_seam_collapse_mod_p2.md), not a canonical CLAIM, authorized run, native benchmark, freeze, Result, or Driver review.

Mother task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3**, preserved. Stable logical Research conversation **chatgpt-research-hourly-enterprise-math-20260923** (not maintenance and not the other onhour lane). Prior genuine Researcher registration is evidenced in enterprise-math#1558; no fresh claim/open or native checkpoint is claimed in this turn. Global authority read main@11f9d30dffa56c0be5bfc4f7f362c9b4558a2f62, P000 ACTIVE_LOCKED. Previous mathematical files checked against enterprise-math main@ec00581176d3454493d637ad200e509e2b9544ac.

## Precise new question

The preceding two-seam transfer proves, with p=6m+1 prime and R_n as in the original endpoint,
\[
T_2=R_{2m}/p,\quad T_4=R_{4m}/p,\quad
G_m=(-1)^m\frac{((2m)!)^3}{((3m)!)^2},
\]
\[
\mathcal K_p
\equiv
\sum_{\substack{0\le n<4m\\n\ne2m}}K_{p,n}R_n
+
T_2[1+pL_m]\pmod{p^2},
\quad
L_m=\frac19-\frac23H_{2m}-\frac13q_p(6),
\]
where \(q_p(6)=(6^{p-1}-1)/p\), and the **still-unproved original** LIFT is equivalent to \(\mathcal K_p\equiv G_m\pmod{p^2}\). The previous unit retained both seams via an exact product. Here the next independent objective is to normalize its remaining unit \(T_2\) against the actual target \(G_m\), without guessing an unproved arithmetic equality.

## Theorem A: exact normalization of the first seam by the target factorial ratio

For every integer m>=1, write p=6m+1, whether or not p is prime. In rational numbers,
\[
\boxed{
\frac{T_2}{G_m}
=\frac{1}{2m\,6^{p-1}}\,
\frac{
\displaystyle\prod_{j=1}^{2m-1}(1+p/j)
\displaystyle\prod_{k=1}^{2m}(1-p/k)
}{
\displaystyle\prod_{k=2m+1}^{3m}(1-p/k)
}.
}\tag{NORM-exact}
\]
The factors in the denominator are nonzero in Q for m>=1. When p is prime, their denominators and factors are p-adic units.

**Direct proof.** The previous exact factorial formula gives
\[
T_2=\frac{(8m)!}{p\,6^{p-1}((4m)!)^2}.
\]
Put \(A=(6m)!=(p-1)!\),
\[
P=\prod_{j=1}^{2m-1}(1+p/j),\quad
E=\prod_{k=1}^{2m}(1-p/k),\quad
F=\prod_{k=1}^{3m}(1-p/k).
\]
Splitting at the *actual* factorial boundary \(p\), with no modular replacement,
\[
\frac{(8m)!}{p}=A(2m-1)!\,P,
\]
\[
A=(4m)!(2m)!\,E,\qquad
A=(-1)^{3m}((3m)!)^2F.
\]
Substitute the three equations into \(T_2/G_m\), using the exact sign
\((-1)^m(-1)^{3m}=+1\), to obtain
\[
\frac{T_2}{G_m}
=\frac{1}{2m\,6^{p-1}}\,\frac{PE^2}{F}.
\]
Cancelling exactly one common \(E\) factor against
\(F=E\prod_{k=2m+1}^{3m}(1-p/k)\)
proves NORM-exact. In particular this is an **all-m exact product certificate**, not an empirical p-adic pattern or a use of Wilson's theorem.

## Theorem B: all-target-prime p² normalization and a regular-sum-only obligation

For prime p=6m+1>=7, all harmonic denominators below are p-units. Expand NORM-exact using finite products and Fermat's little theorem:
\[
P\equiv1+pH_{2m-1},\ \
E\equiv1-pH_{2m},\ \
\Bigl(\prod_{k=2m+1}^{3m}(1-p/k)\Bigr)^{-1}
\equiv1+p(H_{3m}-H_{2m}),
\]
and \(6^{-(p-1)}\equiv1-pq_p(6)\pmod{p^2}\).
Since \(1/(2m)=3/(p-1)\equiv-3(1+p)\pmod{p^2}\), it follows that
\[
\boxed{
T_2\equiv -3G_m
\left[1+p\left(4+H_{3m}-H_{2m}-q_p(6)\right)\right]
\pmod{p^2}.}\tag{NORM-p2}
\]
At the first digit, \(T_2\equiv-3G_m\pmod p\); this statement is now **proved** for every target prime rather than extrapolated from examples.

Combining NORM-p2 with the already proved *combined two-seam* formula SEAM-ONE gives
\[
\boxed{
\text{both original seams together}
\equiv -3G_m[1+pE_m]\pmod{p^2},
}\tag{BOTH-SEAMS}
\]
where the explicit prime-local coefficient is
\[
\boxed{
E_m=\frac{37}{9}+H_{3m}-\frac53H_{2m}-\frac43q_p(6).
}\tag{E}
\]
Do not misread this as either original seam being zero, or as an individual replacement that preserves their full branch information.

Define the **unchanged regular forcing sum** from the original endpoint:
\[
\mathcal R_m=\sum_{\substack{0\le n<4m\\n\ne2m}}
\frac{(2p+1-3n)(6n+2p+3)}
{(3n+p+2)(3n+2p+1)}R_n.
\]
The original second-digit LIFT/EP is now **equivalent**, with no seam coordinates left to solve independently at this observer, to the single specific **open** congruence
\[
\boxed{
\mathcal R_m\stackrel{?}{\equiv}
G_m\left[
4+p\left(\frac{37}{3}+3H_{3m}-5H_{2m}-4q_p(6)\right)
\right]\pmod{p^2}.
}\tag{REGULAR-P2}
\]
This is a true reduction: the right side has only a fixed factorial ratio, two harmonic numbers and the Fermat quotient. It is not a proof of REGULAR-P2. Any all-prime proof must still evaluate the full regular sum \(\mathcal R_m\), maintaining the exact upper terminal and original n provenance. The original Source-provided native benchmark also remains unexecuted.

## Bounded exact checks and observer discipline

Author verification used Python Fraction/integer factorial arithmetic, independent of native Source. NORM-exact was checked as an equality of Q for m=1,...,7. NORM-p2, BOTH-SEAMS, and the *equivalence computation* were checked modulo p² for all 15 target primes with 1<=m<=24:
7,13,19,31,37,43,61,67,73,79,97,103,109,127,139.
In these same 15 finite cases, the still-open REGULAR-P2 itself also happened to match the original exact rational regular sum; that is **finite author evidence only**. Illustrative values p : (regular forcing mod p², explicit candidate mod p²) are
7:(31,31), 13:(45,45), 19:(355,355), 31:(464,464), 37:(441,441), 61:(1033,1033). Nothing is promoted from these finite matches.

BRC = REUSE_APPLIED / COMPOSE_APPLIED. Original signed term weights R_n, index/branch n, p-valuation+unit T_2,T_4, two historical seam labels, and whole scalar observer \(\bmod p^2\) are preserved. NORM-exact and ST-exact prove which information can be projected away **only for this target scalar modulo p²**; their original rational products supply a lossless reconstruction route at a finer observer. No new axiom, native six-axis theorem, source pin change, formal task owner claim, or review is asserted.

**Next genuinely unresolved scientific unit:** find and prove the finite contiguous/WZ-Gosper or parameter identity for the explicitly displayed regular forcing sum \(\mathcal R_m\) with original terminal n=4m-1, excluding n=2m, and its required p² coefficient; alternatively find an exact all-prime obstruction. This result must not be confused with the already proved failure of a *global exact one-term rational primitive* for the full weighted summand. Current backend identity/read path is blocked upstream (BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false), tracked in enterprise-math#1558. This manuscript is neutral durable evidence, **not** a native Source checkpoint or official research acceptance.