# D25/LIFT — fixed-row dual hypergeometric identity; finite original-216 character falsifier

Date: 2026-10-28 21:12 Asia/Hong_Kong. Research logical lane: chatgpt-research-onhour-enterprise-math-20260923.
Status: AUTHOR-SIDE / ALGEBRAIC IDENTITY PROVED / 781 FINITE EXACT CONJECTURE TESTS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED.
Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Immutable scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
P000 remains ACTIVE_LOCKED; this scalar finite-field observer is an auxiliary representation, not a theorem in native Heartbeat X6 or native H0/B0.

## Exact mathematical starting objects

For any prime p=6m+1>3, let
\[
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},\qquad
h_r=2^r\frac{(-1/3)_r^3}{(7/6)_r(4/3)_r r!},\qquad
S_m=\frac9{32}\sum_{r=0}^{m-1}(66r^2-25r+3)h_r\pmod p.
\]
Consume, without recrediting, existing original-216 endpoint, high-tail pairing, one-seed transport, dual _3F2 and forced cutoff at immutable EM commits d8dee3c159b5c991272d50e29165b357ae8718cf, a4a706832aec5351ab7cfd36b76daef4b1ac7e28, 83233b9637e72b677998e2befa5f12b9770461a4, aab9bee8c8338a4d83f6ed20bc4098fd35da1a50.

## Theorem A: fixed-row binomial dualization (PROVED)

For every p=6m+1>3 prime and every 0<=r<m,
\[
\boxed{h_r\equiv(-2)^r\frac{\binom{4m+1}{r}^3}
{\binom{m-1}{r}\binom{2m-1}{r}}\pmod p.}\tag{A}
\]
All the denominator binomial coefficients are nonzero modulo p. Hence
\[
\boxed{S_m=\frac9{32}\sum_{r=0}^{m-1}(66r^2-25r+3)(-2)^r
\frac{\binom{4m+1}{r}^{3}}{\binom{m-1}{r}\binom{2m-1}{r}}\pmod p.}\tag{B}
\]

Proof: in F_p, -1/3=2m, 7/6=1-m and 4/3=1-2m. For r<m all the relevant rising-factorial factors are p-units. Using (2m)_r=r! C(2m+r-1,r), (1-m)_r=(-1)^r r! C(m-1,r), (1-2m)_r=(-1)^r r! C(2m-1,r) gives
h_r=2^r C(2m+r-1,r)^3/[C(m-1,r)C(2m-1,r)] modulo p. Since -2m=4m+1-p, C(2m+r-1,r)=(-1)^r C(-2m,r)=(-1)^r C(4m+1,r) mod p. Cubing contributes (-1)^r, proving (A); the signed quadratic sum proves (B). QED.

Actual BRC composition: retain the labeled, signed r-indexed kernel through r=m-1, its multiplicities and denominator-unit conditions. The observable is S_m modulo p and, using the already-established transport, original high-tail p² u_0^{-1}S_m modulo p³, with
u_0=-2(4m+2)! / [((2m+1)!)^5 216^(2m+1)] mod p.
The first excluded r=m is singular: C(m-1,m)=0, matching the previously proved v_p(h_m)=-1. Infinite-series completion would alter the p-adic source and is not authorized by the identity. No information about the true signed native H0/B0 Frobenius operator is inferred.

## Research observation B (UNPROVED ALL-PRIME CONJECTURE)

The exact full-cutoff original weighted W_p was tested for every prime 5<=p<6000 (781 primes). It satisfied
\[
\boxed{W_p\stackrel{?}{\equiv}\left(\frac{-3}{p}\right)p\pmod{p^3}.}\tag{C: CONJECTURE}
\]
This is a finite exhaustive computation over a declared range, NOT a proof for arbitrary primes. The character equals +1 when p=1 mod3 and -1 when p=2 mod3; the original frozen p=13,19 mod24 target contains 194 tested primes. The search candidate Guo–Zudilin, A q-microscope for supercongruences (Adv. Math. 346 (2019), arXiv:1803.01830), proves a congruence with p(-3/p) for a DIFFERENT 8n+1 / binom(4n,2n) kernel. No transfer of its proof is asserted; a kernel-preserving, boundary-correct quadratic/WZ bridge remains to be established or falsified. Prior-art completeness is NOT claimed.

## Actually executed exact checker

Program: research_notes/portable_direct/d25_onhour_fixed_binomial_character_guard_20261028.py. Standard-library integer modular arithmetic; no floating point. Exact stdout:
PASS_D25_FIXED_ROW_BINOMIAL_DUALIZATION 384 p=1(mod6) primes
PASS_D25_ORIGINAL_HIGH_TAIL_BRIDGE 37 p=1(mod6) primes <400
OBSERVED_UNPROVED_ALL_PRIME_CHARACTER_PATTERN 781 primes < 6000 ; frozen target residue-class count 194
P373_CERTIFICATE {'m': 62, 'u0': 320, 'S_m': 230, 'high_tail_mod_p3': 8208611, 'W_mod_p3': 373}

Methods: full n=0,...,p-1 original-weighted hypergeometric recurrence modulo p³ for 781 primes; independent original-integer binomial readout at 5,7,13,19,37,43,211,373; fixed-row binomial versus dual recurrence at 384 primes; original high-band a_n versus p²u_0^-1 S_m at 37 primes. The identity is proved algebraically; finite tests support the conjecture only over the stated range.

## Source and continuation

At 2026-10-28 21:05+08, the Site reported research_authority_granted=false, write_relay_enabled=false, code-review-required Source control and active native-request quota 5/5. Existing Research-lane bridge recovery request research-onhour-20261027-0501-recovery-r13 (#6575) contains an active LOCAL session pointer only, no own claims or runs and source_authority_verified=false; its neutrally preserved historical staging remains separate. Original dispatch request research-onhour-20261027-0507-dispatch-r13 (#6576) completed FAILED/TimeoutExpired and was not replayed. No new CLAIM, open, session, dispatch or Source Research-Activity was created in this run. A GitHub author-side artifact is not a canonical task checkpoint or Result.

Original same-class native p373 H0/B0 divided-power benchmark under enterprise-math Issue #1559 was OPEN, PENDING_OWNER, NATIVE_NOT_EXECUTED on read. Actual [X]U mod139129, native module rank, F-semilinear direction/eta, odd signed Green/Hesse, kappa and Delta_p-R_p remain required from the authentic executor with reproducible source. No portable scalar computation replaces this acceptance.

NEXT: pursue a p³-precision original-cutoff-preserving quadratic hypergeometric/WZ certificate between the actual 216 weighted kernel and a genuinely proved p(-3/p) model, or construct an exact counterexample to a proposed correspondence; use (B) to retain the high-tail when testing both p=13,19 mod24 classes. Route #1559 to an authorized native executor; do not alter Source pin or task owner. Formal Source registration/checkpoint, Result and independent review remain pending legitimate authority.
