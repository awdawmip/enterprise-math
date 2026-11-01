# D25: A CM(-24) Hasse proof of the full-prime Legendre selector

2026-11-01 Asia/Hong_Kong. **AUTHOR-DERIVED / CLASSICAL-CM-THEOREM-DEPENDENT / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN.** Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923. Frozen Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

This note consumes (but does not re-credit) the prior original 1/4–3/4 Legendre-period and quadratic cutoff/carry result at project commit f3473b69221a29e7021ee1503b92765fe9936a7c. That result explicitly left the all-prime Legendre CM selector as finite evidence. We prove it here using the classical Deuring and CM-class-polynomial theorems, with a new exact Hasse-coefficient identification. Neither the separate 1/8–3/8 Gauss CM selector nor the original216 mother goal is asserted as proved.

## Theorem: full CM residue-class dichotomy

Let p>3 be prime, p≡1(mod4), n=(p−1)/4, and let s²=2. Work in the finite étale algebra R_p=F_p[s]/(s²−2), which is F_(p²) if (2/p)=−1 or F_p×F_p otherwise. Set

\[
t_-=(3-2s)/6,\quad t_+=(3+2s)/6=1-t_-,\quad
U_p(z)=\sum_{k=0}^{p-1}\frac{(1/4)_k(3/4)_k}{(k!)^2}z^k.
\]

**Proved:** The following conditions are equivalent:

\[
\boxed{U_p(t_-)=0\ {\rm in}\ R_p
\iff P_{(p-1)/4}(2s/3)=0\ {\rm in}\ R_p
\iff \left(\frac{-6}{p}\right)=-1.}
\]

For p≡1(mod4), the zero classes are exactly p≡13,17(mod24); classes 1,5(mod24) are nonzero in each residue factor. In particular **all** p≡13(mod24) satisfy the previously unproved source-specific condition U_p(t_-)=0 mod p.

### 1. The exact auxiliary elliptic curve has CM(-24)

Over K=Q(s) define E_z:y²=x(x²+2x+1-z). Exact Weierstrass calculation gives

\[
\Delta(E_z)=64z(1-z)^2,\qquad j(E_z)=\frac{64(1+3z)^3}{z(1-z)^2}.
\]

At z=t_-:

\[
j(E_{t_-})=2417472-1707264s,\qquad
j^2-4834944j+14670139392=0.
\]

The polynomial H_{-24}(X)=X²−4834944X+14670139392 is the **standard Hilbert class polynomial** of the maximal order of Q(√−6), fundamental discriminant −24 (class number 2). By the defining CM characterization of H_{-24}, E_{t_-} has CM by that order over the algebraic closure. This uses a cited classical fact, not a new axiom. Both t_- and 1-t_- have norm 1/36, so

\[
N_{K/\mathbb Q}(\Delta(E_{t_-}))=64^2/36^3=64/729.
\]

Therefore E_{t_-} has good reduction at **every** prime p>3, with no omitted exceptional prime in the theorem.

### 2. Exact Hasse coefficient equals the *original* period polynomial

Put m=(p−1)/2=2n. The Hasse invariant of y²=f_z(x) is the coefficient of x^{p−1} in f_z(x)^m. Thus for E_z its entire Hasse polynomial is

\[
A_p(z)=[x^{p-1}](x((x+1)^2-z))^m
 =\sum_{k=0}^{n}(-1)^k\binom{2n}{k}\binom{4n-2k}{2n}z^k.
\]

Let a_k be its coefficients. a_0=C(p−1,(p−1)/2)≡1(mod p), and for 0≤k<n, with p-unit denominators,

\[
\frac{a_{k+1}}{a_k}=
-\frac{(2n-2k)(2n-2k-1)}{2(k+1)(4n-2k-1)}
\equiv\frac{(4k+1)(4k+3)}{16(k+1)^2}\pmod p.
\]

This is precisely the coefficient recurrence of the 1/4–3/4 finite hypergeometric series. At k=n+1 the rising (1/4)_k gains a p factor since 4n+1=p, and coefficients through k=p−1 have p-unit factorial denominators. Consequently **coefficientwise in F_p[z]**:

\[
\boxed{A_p(z)\equiv U_p(z)\equiv
{}_2F_1(-n,n+1;1;z)=P_n(1-2z)\pmod p.}
\]

At z=t_-, 1−2t_-=2s/3. Hence the actual *source* Legendre selector is exactly the Hasse invariant of E_{t_-}, not just numerically similar to one.

### 3. Supersingularity completes the infinite-prime proof

Classical Deuring reduction states: at good p unramified in its CM field, a CM elliptic curve is supersingular iff p is inert in that imaginary quadratic field. Here p>3 is unramified in Q(√−6). The Hasse invariant vanishes precisely for supersingular reduction, hence

\[
A_p(t_-)=0\iff \left(\frac{-6}{p}\right)=-1.
\]

Quadratic reciprocity yields symbol +1,+1,−1,−1 for p mod24=1,5,13,17. Conjugation s↦−s proves the same criterion for t_+. This establishes both zero and nonzero directions (including split √2 residue components). QED.

**External classical inputs:** standard H_{-24} coefficients: https://numberdb.org/Hilbert_class_polynomials and https://oeis.org/A305474 ; CM definition: https://magma.maths.usyd.edu.au/magma/handbook/text/1660 ; Deuring: https://mathoverflow.net/questions/18591/reduction-of-cm-elliptic-curves (quoting Lang, *Elliptic Functions*, p.182) and Blake, *Bull. LMS* 46 (2014), doi:10.1112/blms/bdu079. The standard genus-one Hasse–Witt coefficient test is used as stated. These references do not independently review this derived linkage.

## Consequence: delete one *assumption*, not the quadratic tail

The on-hour predecessor established the **exact finite** identity

\[
F_p(4t(1-t))-U_p(t)=t^pH_p(t),
\quad 4t_-(1-t_-)=1/9,
\]

the p² Legendre anti-trace U_p(t_-)+U_p(t_+)≡0, and a two-port Frobenius carry identity. Its p13 specialization assumed **both** F_p(1/9)=0(mod p) (the separate beta selector) and U_p(t_-)=0(mod p) (formerly supported only by finite tests).

The new CM theorem proves that second premise for **every** p13. Thus for all p≡13(mod24), since t_- is a unit,

\[
\boxed{F_p(1/9)=0\pmod p\iff H_p(t_-)=0\pmod p.}
\]

If the remaining *original beta* selector holds, write K_p(t_-)=H_p(t_-)/p via componentwise p-local division **before mod-p reduction**. The earlier exact anti-trace and carry formula then gives, with no independent Legendre assumption,

\[
\boxed{\frac{F_p(1/9)}p\equiv\frac12\operatorname{Tr}(t_+K_p(t_-))\pmod p.}
\]

If K_p(t_-)=u_p+v_ps, the scalar is u_p/2+2v_p/3. Its all-prime vanishing remains open. No second-digit Gauss theorem, native H0/B0 run, weighted216 conclusion, Result, review or Source checkpoint is claimed.

## Executed exact checks and typed BRC scope

Standalone standard-library Python program d25_cm_hasse_legendre_selector_20261101.py uses (i) an independently computed Hasse coefficient polynomial, (ii) original hypergeometric coefficient recurrence, (iii) independent Legendre recurrence, (iv) exact arithmetic in F_p[s]/(s²−2), and (v) the Legendre symbol. It also checks the two *integer* coordinates of the class polynomial relation and the exact discriminant norm.

All 211 primes p≡1(mod4), 5≤p≤3000: coefficientwise Hasse=hypergeometric and evaluated Legendre=Hasse, with class counts p mod24: 1:46 primes/0 zeros; 5:57/0; 13:53/53; 17:55/55. No floating-point calculation. These finite checks corroborate, but do **not** prove, the infinite statement; the latter uses the displayed derivation plus classical CM/Deuring.

**BRC COMPOSE_APPLIED:** the external number-theoretic carrier retains both s-conjugate branches, the original signed j≥p cutoff, the p-valuation and the p² future Frobenius/trace operations. Hasse scalar collapse is used *only* for the mod-p selector; it cannot erase the future-relevant divided tail K. This quadratic auxiliary ring is not a native X6 lower-dimensional spatial plane; P000 and ACTIVE world framing are unchanged.

**Current durable/remaining frontier:** This proves the separate Legendre CM selector beyond prior p≤10000 finite samples. Do not rerun that search or re-credit the predecessor quadratic tail. Next exact mathematical step: prove (or refute with an exact prime) the distinct beta 1/8–3/8 mod-p CM selector; then prove or falsify the full p13 trace of t_+K_p modulo p, preserving signed high-degree sources. The original216 mod p³ target and native p373 H0/B0, semilinear Frobenius and independent experiment still require their own evidence (#1559). Native control recovery remains with #1558. No new native CLAIM/OPEN/run/Source checkpoint, activity registration or mathematical admission is asserted by this portable proof.