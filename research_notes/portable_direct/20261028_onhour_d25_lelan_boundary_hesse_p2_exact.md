# D25/LIFT — exact universal Cauchy-cutoff boundary K ≡ 3p/2 (mod p²)

Date: 2026-10-28 Asia/Hong_Kong. Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923, not CONTROL_PLANE_MAINTENANCE. Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Exact Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific frozen Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3, **unchanged**.

**Classification: AUTHOR-SIDE / EXACT ALL-PRIME PROOF / 148 EXECUTED PRIME CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_H0B0_NOT_EXECUTED.** This is a genuine continuation of the prior finite Cauchy bridge (commit fb5040cf85bc10a53fe5ae65d9536f5b7048f805), not a Source-native CLAIM, run, checkpoint, Result or review.

## 1. Unchanged finite object

For each prime \(p=6m+1>3\), \(N=p-1=6m\), preserve the original coefficients, signed weights, convolution fibers and cutoff:

\[
t_k=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},\quad
b_j=\frac{\binom{2j}{j}}{8^j},\quad
B_j=\sum_{i=0}^{j}b_i.
\]

The **already proved rational finite identity**, consumed without taking new credit for it, is

\[
S_N=H_N-K_N,\quad
S_N=\sum_{n=0}^N(3n-1)\sum_{j=0}^n b_jt_{n-j},
\]
\[
H_N=\frac12\sum_{k=0}^N(6k+1)t_k B_{N-k},\quad
K_N=\frac32\sum_{k=0}^N(2(N-k)+1)t_k b_{N-k}.
\]

All rational denominators are p-units for p>3. The original D25 object is the **different** weighted sum \(W_N=\sum_{k=0}^N(6k+1)t_k\); no equality S=W is presupposed.

## 2. New full-prime theorem and proof

**Theorem.** For every prime \(p\equiv1\pmod6\),

\[
\boxed{K_{p-1}\equiv\frac{3p}{2}\pmod{p^2}.}\tag{B2}
\]

Consequently, at the same **exact finite cutoff**,

\[
\boxed{S_{p-1}\equiv H_{p-1}-\frac{3p}{2}\pmod{p^2}.}\tag{F2}
\]

All divisions and congruences are taken in the p-local rationals; in particular 1/2 is the unique unit inverse mod p².

**Step 1: valuation support.** For \(0\le k\le6m\), Legendre's factorial formula applied to the unaltered integer binomials yields:

\[
v_p(t_k)=
\begin{cases}
0 & 0\le k\le 2m,\\
1 & 2m<k\le3m,\\
2 & 3m<k\le4m,\\
3 & 4m<k\le6m.
\end{cases}
\]

For \(0\le j\le6m\), \(v_p(b_j)=0\) when \(j\le3m\), and \(v_p(b_j)=1\) otherwise. Write \(j=6m-k\). Terms with \(2m<k<3m\) have valuation at least two because both factors have positive valuation. For \(k>3m\) the original \(t_k\) alone has valuation at least two. At \(k=3m\), the exceptional term is also divisible by p² since its **signed weight** is \(2j+1=6m+1=p\). Only \(0\le k\le2m\) survives modulo p², and in that range \(j\ge4m\), so each term is divisible by p.

**Step 2: exact reflection with its sign.** For \(0\le k\le2m\), \(j=p-1-k\), Wilson's theorem and factorial rearrangement give the finite congruence

\[
\frac1p\binom{2j}{j}\equiv
-\frac{(k!)^2}{(2k+1)!}\pmod p.
\]

Since \(8^{-j}\equiv8^k\pmod p\) and \(2j+1\equiv-(2k+1)\pmod p\), the two *minus* signs cancel in the **original weighted summand**:

\[
\frac{(2j+1)b_j}{p}\equiv
\frac{8^k}{\binom{2k}{k}}\pmod p.
\]

The original \(216^k\) normalizer therefore survives exactly as

\[
\frac{K_N}{p}
\equiv\frac32\sum_{k=0}^{2m}
\frac{\binom{2k}{k}\binom{3k}{k}}{27^k}
=\frac32 A_p(1)\pmod p,
\]
\[
A_p(x)=\sum_{k=0}^{2m}\frac{(3k)!}{27^k(k!)^3}x^k.
\]

This A is the familiar finite Hesse-Hasse arithmetic polynomial **as an external observer**. Its appearance is a genuine coefficient identity, not a measured native H0/B0 Frobenius.

**Step 3: finite exact evaluation, no conjectures.** As \(p=6m+1\),

\[
\frac{(3k)!}{27^k(k!)^3}
=\frac{(1/3)_k(2/3)_k}{(k!)^2}
\equiv\frac{(-2m)_k(2m+1)_k}{(k!)^2}\pmod p
\]

for \(0\le k\le2m\). With \(n=2m\), the terminating sum gives

\[
A_p(1)\equiv
\sum_{k=0}^{n}(-1)^k\binom nk\binom{n+k}{k}
=(-1)^n=1\pmod p.
\]

For self-contained verification of the finite binomial identity, take coefficient \([x^n]\) on both sides of

\[
(1+x)^n\sum_{k=0}^n(-1)^k\binom nk(1+x)^k
=(1+x)^n(-x)^n.
\]

Thus \(K_N/p\equiv3/2\pmod p\), proving (B2), and (F2) follows from the prior *exact* finite S=H−K identity. **QED.**

The theorem holds in particular for both requested frozen classes \(p\equiv13,19\pmod{24}\), but says nothing about the unresolved full-prime \(W_{p-1}\equiv p\pmod{p^3}\) claim.

## 3. Executed certificates, precision boundary, non-target falsifier

Companion: research_notes/portable_direct/d25_lelan_boundary_hesse_p2_guard_20261028.py. Python standard-library integers; no floats in the arithmetic. It actually executed and passed at all 148 primes p<2000 with p≡1 mod6, using recurrence-mod-p² plus the terminating Hesse sum. For primes through p=373, a **separate exact integer-binomial implementation** also agreed. The finite regression checks the implementation but is not the universal proof.

At the priority p=373, independent p³ recomputation yields exactly the prior record

\[
(W_{372},S_{372},H_{372},K_{372})
=(373,8487242,29983232,21495990)\pmod{51895117}.
\]

Modulo p²=139129, \(K_{372}=70124=188p=(3/2)p\), \(H_{372}=70497=189p\), and \(S_{372}=p\). The *precise limit* of the new reduction is demonstrated by the nonzero higher digit

\[
\boxed{K_{372}-(3/2)p\equiv341p^2\not\equiv0\pmod{p^3}.}
\]

Thus (B2) is not valid as a mod-p³ compression. For p=11 (outside the theorem's class), the checker yields \(K_{10}\equiv44\pmod{121}\ne(3/2)p\); the prime-class scope matters.

## 4. BRC/Enterprise typing and lawful continuation

BRC resolution: COMPOSE_APPLIED. Population keeps p≡13 and p≡19 mod24 as **separate target labels**. Original carriers: (p, k, j=p−1−k, signed 2j+1, v_p(t_k), v_p(b_j), H, K, S), with precision and permissible future operations stated. For the observer S modulo p², replacing K by 3p/2 is **proved safe**; for modulo p³ the exact p=373 witness forces retention of the extra residual digit. Neither the unsigned sum nor the infinite analytic Cauchy product may replace the finite signed cutoff. The quadratic/p-adic and formal indices are externally typed arithmetic observers, not an asserted native two-dimensional Enterprise plane, complete X6 state, or derived heartbeat dynamics. P000 Heartbeat native six-dimensional discrete Cell space, separately typed time, and three-dimensional slice remain unchanged.

For D25 target classes, Le Lan's proposed Cauchy congruence S≡p (mod p²) is now **equivalent**, by (F2), to the single outstanding H-congruence \(H_{p-1}\equiv5p/2\pmod{p^2}\). This is a real reduction, **not a proof of the H-congruence, Le Lan's conjecture, or D25 LIFT**. Do not recredit the frozen CM0/UR, initial Clausen identity, or earlier finite regressions.

**Highest scientific obligation remains native, unchanged:** issue #1559 needs a lawful owner and an *actual same-original-class* p=373 H0/B0 divided-power execution: [X]U mod139129, native rank, full semilinear Frobenius direction/eta normalization, signed odd Green/Hesse, original κ and Δ−R, and source/code/version/reproducible output. It is not satisfied by this auxiliary exact theorem. The issue remained OPEN / PENDING_OWNER / NATIVE_NOT_EXECUTED when read.

**Source/recovery gate (verified this run):** old onhour logical request in awdawmip/kimi-query-bridge#6575 has an ACTIVE local session pointer but no verified winning CLAIM/open and source_authority_verified=false. Own dispatch #6576 finally failed with TimeoutExpired (not NO_DISPATCH). Gateway v0.6.11 Site client remained source/control read-only with research_authority_granted=false and active native job quota 5/5. No new registration, prepare, claim, open, run, formal checkpoint, Result, review, native experiment or maintenance-lane operation is asserted. Publication of this author-side proof is **not** Source admission. The next protected action is a genuinely authorized native evaluator/identity, then current exact Source continuation and matching own owner/claim recovery before the original run. Frozen pin and scheduled notification behavior were not modified.
