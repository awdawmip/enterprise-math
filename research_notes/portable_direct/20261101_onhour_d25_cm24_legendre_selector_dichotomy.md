# D25 SECOND-DIGIT-LIFT — exact CM(-24) Legendre selector dichotomy

2026-11-01 Asia/Hong_Kong. **AUTHOR-SIDE MATHEMATICAL PROOF USING CLASSICAL CM/DEURING + EXECUTED FINITE CHECK; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN.**

Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`. Publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. This Research lane \`chatgpt-research-onhour-enterprise-math-20260923\` retains its logical identity, without using the maintenance lane. The exact predecessor cutoff/Frobenius identity is \`research_notes/portable_direct/20261101_onhour_d25_quadratic_frobenius_carry_elimination.md\` (the predecessor contribution is consumed, not recredited).

## New all-prime theorem — CM Legendre selector, including the ordinary complementary class

For any prime p>3 with p=5 (mod 8), let s²=2 over \`F_(p²)\`, n=(p−1)/4, and t_−=1/2−s/3. Then

\[
\boxed{P_n(2s/3)=0\pmod p\quad\Longleftrightarrow\quad p\equiv13\pmod {24}.}
\]

Equivalently, the finite original \`U_p(t)=sum_(k=0)^(p−1) (1/4)_k(3/4)_k t^k/(k!)²\` obeys

\[
U_p(t_-)\equiv0\pmod p\quad (p=13\ \mathrm{mod}\ 24),
\qquad
U_p(t_-)\not\equiv0\pmod p\quad (p=5\ \mathrm{mod}\ 24).
\]

This closes the previously finite-only **Legendre CM selector** in the predecessor note for the entire stated prime class. It does not prove the original \`F_beta,p(1/9)=0 (mod p²)\` or original weighted216 target.

## Proof, with every algebraic connection explicit

**(1) Auxiliary elliptic carrier and its Hasse observable.** For t=t_− over Q(s), introduce the *external auxiliary* elliptic curve

\[
E_t:\quad Y^2=X^3-2X^2+(1-t)X
       =X\big((X-1)^2-t\big).
\]

Its discriminant and j-invariant are

\[
\Delta(E_t)=64t(1-t)^2,\qquad
j(E_t)=\frac{64(1+3t)^3}{t(1-t)^2}.
\]

The original t_± satisfy t_−t_+=1/36; hence t_± and 1−t_± are p-units for every p>3. Thus E_t has good reduction at every prime above such p. This E_t is a mathematical comparison carrier, not native X6/H0/B0.

**(2) Exact Hasse–Legendre coefficient identity.** For p=4n+1 put m=(p−1)/2=2n. The Hasse invariant of E_t in characteristic p is its original cubic polynomial coefficient

\[
\mathcal H_p(t)=[X^{p-1}]\left(X((X-1)^2-t)\right)^m.
\]

Binomial expansion gives, *as a polynomial in t*,

\[
\mathcal H_p(t)=\sum_{k=0}^n(-t)^k
 \binom{m}{k}\binom{p-1-2k}{m}.
\tag{H}
\]

For 0≤k≤n, use \(\binom{p-1-2k}{m}\equiv\binom{m+2k}{m}\pmod p\), since m is even. Let \(A_k=\binom m k\binom{m+2k}m\) and \(B_k=\binom nk\binom{n+k}k\). Both have A_0=B_0=1 and, for k<n,

\[
\frac{A_{k+1}}{A_k}
 \equiv-\frac{(4k+1)(4k+3)}{16(k+1)^2}
 \equiv\frac{B_{k+1}}{B_k}\pmod p.
\]

All displayed denominators are p-units for 0≤k<n. Thus A_k≡B_k, and the well-known finite hypergeometric expression for Legendre gives the *coefficientwise identity*

\[
\boxed{\mathcal H_p(t)\equiv
 \sum_{k=0}^n(-1)^k\binom nk\binom{n+k}k t^k
 =P_n(1-2t)\pmod p.}
\tag{HL}
\]

The original U_p reduces modulo p to this same polynomial since (1/4,3/4) reduce to (−n,n+1). At t_−, 1−2t_−=2s/3. Consequently its selector vanishes **if and only if** the good reduction of E_{t_-} is supersingular. This also establishes the exact bridge between the original finite Gauss coefficients, Hasse invariant, and the chosen quadratic branch.

**(3) Certifying the CM order, with fixed exact j data.** Direct substitution gives

\[
j(E_{t_-})=2417472-1707264s,\qquad
j(E_{t_+})=2417472+1707264s.
\]

Their sum is 4834944 and their product is 14670139392, exactly the two roots of the standard Hilbert class polynomial

\[
H_{-24}(J)=J^2-4834944J+14670139392.
\]

The externally verifiable CM discriminant is **−24**, with underlying quadratic CM field \(K=\mathbb Q(\sqrt{-6})\). A characteristic-zero elliptic curve having this j-invariant has CM by the order of discriminant −24. External identity sources:
- OEIS A305474: https://oeis.org/A305474 (row D=−24, exact integer polynomial).
- LMFDB CM elliptic curves over Q(sqrt2): https://www.lmfdb.org/EllipticCurve/?field=2.2.8.1&jinv=-1707264%2Aa+%2B+2417472 (CM discriminant −24).
- Direct special-j evaluation: https://www.kaynet.or.jp/~kay/misc/jtau6.html.

**(4) Apply the classical Deuring reduction theorem, not an assumed project axiom.** Deuring's theorem for an elliptic curve with CM by an imaginary quadratic order and good reduction states: an unramified prime inert in the CM field gives supersingular reduction, while a split prime gives ordinary reduction. Source: https://link.springer.com/article/10.1007/s10231-024-01528-x (Theorem 4.1). Here p>3 is unramified in K, and

\[
\left(\frac{-6}{p}\right)
 =\left(\frac{-1}{p}\right)
  \left(\frac 2p\right)\left(\frac 3p\right)
 =-\left(\frac 3p\right)\qquad(p=5\ \mathrm{mod}\ 8).
\]

For p=13 (mod 24), \((3/p)=1\), so p is inert and E_t is supersingular; for p=5 (mod 24), \((3/p)=-1\), so p splits and E_t is ordinary. Equation (HL) proves the stated **if-and-only-if**. This is an all-prime argument based on a standard published CM theorem plus explicit algebra, not inference from the finite sample. QED.

## Exact finite validation (independent arithmetic interface)

Companion executable: \`research_notes/portable_direct/d25_p13_cm24_legendre_selector_20261101.py\`. Run with Python standard-library integer arithmetic; checks 95 primes p≤1200 with p=1 (mod4) for **every coefficient** in (HL), and among the p=5 (mod8) primes checks 26 inert p=13 (mod24) zero selectors and 25 split p=5 (mod24) nonzero selectors in the full quadratic two-coordinate ring. Crosscheck values: p5 (0,4); p13 (0,0); p29 (0,24); p37 (0,0); p53 (0,18); p61 (0,0); p109 (0,0); p373 (0,0), coordinates in F_p[s]/(s²−2). This is coverage of those stated finite domains, not a native experiment or a replacement for proof.

## Consumed frontier, BRC observer fidelity, and immediate next unit

The predecessor \`20261101_onhour_d25_quadratic_frobenius_carry_elimination.md\` required two mod-p selectors (S) to eliminate its first Frobenius carry. **The separate Legendre selector is now proven** for every p=13 (mod24). Using the predecessor's *existing* original-beta mod-p CM selector as a separately sourced input, the predecessor's \(H_p(t_-)\equiv0\pmod p\) and carry elimination are now unconditional relative to that already established beta result. Retain the original source-labeled cutoff \(R_p(t)=t^pH_p(t)\), its quadratic branch and signed trace; no new native operator is inferred. The smallest mathematical obligation is the first digit of the remaining even trace:

\[
\frac12\operatorname{Tr}\!\left(\overline{t_-}
 \frac{H_p(t_-)}p\right)\equiv0\pmod p
\quad\text{for }p=13\pmod{24}.
\]

In BRC terms this is an actual composed carrier/observer bridge: original finite Gauss cutoff → elliptic Hasse coefficient (with an explicit invertible coordinate map) → CM inert/split Frobenius type → original Legendre selector. The CM classification lives only on the *auxiliary elliptic carrier*. The native six-dimensional spatial slice, H0/B0 divided-power, signed odd Green/Hesse, eta, kappa and future native operations remain separate, not silently projected to the elliptic model.

Mother scientific target remains \(A_p\equiv p\pmod{p^3}\) for p=13,19 (mod24), combining the original 216 Delta−R port. Fixed p373 original-class native benchmark remains issue https://github.com/awdawmip/enterprise-math/issues/1559 (OPEN/unassigned on 2026-11-01), requiring raw [X]U mod139129, rank, semilinear Frobenius, signed observers, kappa, and independent replication; **NATIVE_NOT_RUN / PENDING_OWNER**.

2026-11-01 fresh Gateway 0.6.11: research_authority_granted=false, executor_binding_configured=false, Source control code review required. Own checkpoint list ACCESS_DENIED; prior request \`research-onhour-20261031-0205-dispatch-r15\` currently returned CONTROL_REQUEST_NOT_FOUND for this authenticated client; its actual global outcome remains unverified. There is no new session/claim/run or Source checkpoint/Result/review. Keep old staging separate and no duplicate dispatch. Preserve P000, ACTIVE worldview, scientific pin and existing hourly scheduler state. This document and companion program are **author-side provenance artifacts**, not canonical Source task admission.
