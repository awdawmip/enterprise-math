# D25 / SECOND-DIGIT-LIFT — exact cubic-moment telescoper and fourth-digit endpoint

2026-10-30 (Asia/Hong_Kong). Author-side mathematical research for logical Research lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane chatgpt-hourly-enterprise-math-20260921 was not used.
Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Immutable scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.
Classification: **AUTHOR-SIDE / PROVED EXACT TELESCOPER / EXECUTED EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING**.

## Exact finite theorem, original 216 model

For every integer N>=0, work over rational coefficients and define

\[
 a_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
 =\frac{(2n)!(3n)!}{(n!)^5 216^n},
 \qquad S_j(N)=\sum_{n=0}^N n^j a_n \quad (j=0,1,2,3).
\]

Set Q(n)=(2n+1)(3n+1)(3n+2). Then, **exactly for every N**, with no prime hypothesis,

\[
 \boxed{18S_3(N)-27S_2(N)-13S_1(N)-2S_0(N)=-Q(N)a_N.}\tag{1}
\]

Proof: The original coefficient ratio is

\[
 \frac{a_n}{a_{n-1}}=\frac{(2n-1)(3n-1)(3n-2)}{36n^3},\quad n\ge1.
\]

Consequently Q(n-1)a_{n-1}=36n^3a_n, while
Q(n)=18n^3+27n^2+13n+2. Subtraction gives the exact telescoping difference

\[
 (18n^3-27n^2-13n-2)a_n=Q(n-1)a_{n-1}-Q(n)a_n.
\]

The n=0 term is -2=-Q(0)a_0, proving (1) by summation. This does not require a mod-p approximation.

The original weighted target is A_N=S_0(N)+6S_1(N). Hence (1) is equivalently the exact signed-source relation

\[
 \boxed{108S_3(N)-162S_2(N)+S_0(N)-13A_N=-6Q(N)a_N.}\tag{2}
\]

## Uniform nonzero fourth-digit endpoint

For every prime p>3, put N=p-1. Since 216 is a p-adic unit,

\[
 \boxed{v_p(a_{p-1})=3,\qquad a_{p-1}/p^3\equiv-1\pmod p.}\tag{3}
\]

Proof: factorial valuations are v_p((2p-2)!)=1, v_p((3p-3)!)=2 and v_p((p-1)!)=0. After removing exactly the integer factors p and p², Wilson's theorem gives

\[
 (2p-2)!/p\equiv(p-1)!(p-2)!\equiv-1\pmod p,
\]
\[
 (3p-3)!/p^2\equiv2((p-1)!)^2(p-3)!\equiv-1\pmod p.
\]

The denominator ((p-1)!)^5 is -1 mod p and 216^(p-1) is 1 mod p, proving (3).
Now Q(p-1)=(2p-1)(3p-2)(3p-1)\equiv-2\pmod p. From (1)-(3) we deduce:

\[
 \boxed{18S_3(p-1)-27S_2(p-1)-13S_1(p-1)-2S_0(p-1)\equiv-2p^3\pmod{p^4},}\tag{4}
\]
\[
 \boxed{108S_3(p-1)-162S_2(p-1)+S_0(p-1)-13A_p\equiv-12p^3\pmod{p^4}.}\tag{5}
\]

The p-adic valuation of each residual is exactly 3 for every p>3. Any proposed higher-digit homogeneous moment/Picard-Fuchs or WZ certificate must retain this nonzero terminal source. This theorem concerns the original A216 moment observer; it is not a proof of A_p≡p mod p³.

## Executed exact certificate

Script: research_notes/portable_direct/d25_a216_third_moment_boundary_20261030.py (Git blob 45bed28e487915187957c911656620784c52cd97). The published script itself was locally re-executed and its Git blob matched the remote blob. It checked: exact Fraction sums N=0,...,12; all 667 primes 5<=p<5000 with p^4 arithmetic (166 frozen p≡13,19 mod24); and independent original-binomial computations for p=5,7,11,13,19,37,373. All passed. Universal proof is the telescoper and Wilson/Fermat arithmetic above, not inference from finite samples.

At p=373 the script returns a_372/373³≡372 and moment defect (4) divided by 373³≡371 mod373, matching -1 and -2. This moment defect is a different typed observable from the already named 216/2304 bridge difference D_p; do not conflate them.

BRC: COMPOSE_APPLIED. Carrier = original ordered indices n, exact signed rational coefficients, ports S0,S1,S2,S3, terminal n=N, valuations. Observer = weighted A216 and cubic moment combination through p^4. Finite telescoping is an allowed future operation. Quotienting away the terminal source Q(N)a_N gives a provably incorrect mod-p^4 homogeneous equation. No native X6/H0/B0 physical or operator claim is made.

## Scientific continuation and authority

The exact outstanding LIFT remains A_p≡p (mod p³) for p≡13,19 (mod24), equivalently the already source-aligned joint Gauss value/derivative plus R cutoff criterion, not a separate vanishing of its source ports. The current fourth-digit endpoint is a guard for any attempted joint certificate. Consume the already completed 2026-10-26 Clausen/R alignment and CM/low-two-zone/regular middle work at their actual scope, not as fresh results.

The independent highest-priority native benchmark remains GitHub issue #1559: original fixed-p373 H0/B0 divided-power [X]U modulo 139129, genuine semilinear Frobenius, rank, signed odd Green/Hesse, kappa, independent review. No native benchmark was executed in this artifact. The 2026-10-30 06:02 UTC Sites configuration returned research_authority_granted=false and write_relay_enabled=false; own checkpoint list read returned ACCESS_DENIED. This lane did not acquire or borrow a Source session/claim/run, did not replay an unknown request identifier and did not publish a formal Result. A future authorized continuation first reconciles its own exact Source request and canonical continuation. GitHub author-side storage is not Source admission.
