# D25/LIFT GH11–GH13: original S reflection, next digit, and a surviving 19-class defect

2026-10-28 Asia/Hong_Kong. TASK_RESEARCH logical conversation: chatgpt-research-hourly-enterprise-math-20260923. Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / D25-LIFT-JT2. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Evidence: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. These are external hypergeometric/rank-observer results, not native Heartbeat World X6 theorems, and not native Source progress.

## Sources and exact carriers

Consume GH3's auxiliary coefficient and GH9/10's 3-mod-4 reflection without recrediting them:

$$
 C_r=9^r\frac{(1/4)_r^3}{(1/2)_r(3/4)_r\,r!},\qquad
 h_r=9^{-r}\frac{(1/4)_r(1/2)_r(3/4)_r}{(r!)^3}
 =\frac{(4r)!}{(r!)^4 2304^r},\quad s_r=(8r+1)h_r.
$$

For a prime p>3 put d=floor((p-1)/4) and T_p=sum_{r=0}^d (8r+1)C_r. Guo–Zudilin, A q-microscope for supercongruences, Adv. Math. 346 (2019), 329–358, https://arxiv.org/abs/1803.01830, proves for exactly this original S summand:

$$
 \sum_{r=0}^{p-1}s_r\equiv p\chi_p\pmod{p^3},
 \qquad\chi_p=\left(\frac{-3}{p}\right).
 \tag{GZ-S}
$$

For every d+1<=r<p, v_p(h_r)>=1: (4r)! contains p and the original denominator remains a p-unit. Hence S_short=sum_{r=0}^d s_r is 0 mod p for both p mod4 classes. Preserve the omitted original-S tail at higher precision.

## GH11 — prove the entire complementary p=1 (mod 4) scalar vanishing branch

**Theorem.** For EVERY prime p=4d+1>=5, EVERY 0<=r<=d:

$$
\frac{C_{d-r}}{C_d}
=9^{-r}\prod_{i=1}^{r}
\frac{(p+1-4i)(p+2-4i)(p+3-4i)}{(p-4i)^3}
\equiv h_r\pmod p. \tag{11}
$$

In particular $\boxed{T_p\equiv0\pmod p}$ for all such primes.

**Proof.** The exact recurrence is

$$
C_{k+1}/C_k=\frac{9(4k+1)^3}{(4k+2)(4k+3)(4k+4)}.
$$

Invert for k=d-i and telescope to (11). Denominators p-4i for i=1..d are units. The reduction is the exact Pochhammer product for h_r, because the three negative factors and the negative denominator cube cancel. All C_0,...,C_d are p-units. Reindex the ORIGINAL bounded auxiliary sum and retain the exact linear weight:

$$
\frac{T_p}{C_d}=\sum_{r=0}^d [2p-(8r+1)]\frac{C_{d-r}}{C_d}
\equiv-\sum_{r=0}^d(8r+1)h_r\equiv0\pmod p.
$$

This new conclusion settles the wider auxiliary T_p question for p=1 mod4, including frozen p=13 mod24. GH3's distinct MM/LH source-port equivalences apply only to the p=19 mod24 branch: do NOT extend those equivalences here. The source congruence GZ-S is a cited external theorem, not a theorem proved here.

## GH12 — next digit, true original S source and actual discarded tail

For p=4d+1 define:

$$
\Lambda_r^+=\sum_{i=1}^r\left(\frac1{4i-1}+\frac1{4i-2}+\frac1{4i-3}-\frac3{4i}\right),\quad\Lambda_0^+=0,
$$

$$
S_d=\sum_{r=0}^d(8r+1)h_r,\quad H_d=\sum_{r=0}^d h_r,\quad
K_d=\sum_{r=0}^d(8r+1)h_r\Lambda_r^+,\quad
E_d=\sum_{r=d+1}^{p-1}(8r+1)h_r\in p\mathbb Z_p.
$$

**Theorem.** For every such prime and all stated ranks:

$$
\boxed{\frac{C_{d-r}}{C_d}\equiv h_r(1-p\Lambda_r^+)\pmod{p^2}}, \tag{12a}
$$

$$
\boxed{\frac{T_p}{C_d}\equiv-S_d+p(2H_d+K_d)\pmod{p^2}}, \tag{12b}
$$

$$
\boxed{\frac{T_p}{pC_d}\equiv-\chi_p+\frac{E_d}{p}+2H_d+K_d\pmod p}. \tag{12c}
$$

**Proof.** Factor each quotient term in exact (11) relative to its p=0 value:

$$
\frac{(1-p/(4i-1))(1-p/(4i-2))(1-p/(4i-3))}
     {(1-p/(4i))^3}
\equiv1-p\left[\frac1{4i-1}+\frac1{4i-2}+\frac1{4i-3}-\frac3{4i}\right]\pmod{p^2}.
$$

Each denominator is a p-unit for 1<=i<=d. Multiply to obtain (12a), insert actual rank weight 2p-(8r+1) to obtain (12b), and use GZ-S with S_d+E_d congruent to p chi_p modulo p² to obtain (12c). GH11 ensures its left side is p-integral. The boundary term E_d/p is indispensable to the actual provenance-preserving second-digit observer.

**Finite observation (NOT a universal proof).** All 609 primes p<10000 with p=1 mod4 gave T_p/(pC_d)=chi_p modulo p, equivalently E_d/p+2H_d+K_d=2chi_p modulo p. The cancellation of the three separate contributions is an OPEN conjecture.

## GH13 — exact gauge-defect criterion in p=3 (mod 4), including frozen 19 mod24

For every prime p=4d+3>3, take GH9's finite reflected auxiliary coefficient

$$
B_r=9^{-r}\frac{(3/4)_r(1)_r(5/4)_r}{(3/2)_r^3}.
$$

Define the exact rank gauge

$$
\boxed{U_r=\frac{B_r}{h_r}=
\frac{4r+1}{(2r+1)^3}
\left(\frac{4^r}{\binom{2r}{r}}\right)^4}. \tag{13a}
$$

For 0<=r<=d all denominators are p-units, so U_r is also a p-unit. GH9's exact previously proved reflected sum, together with the exact original S-short congruence, gives the **proved reduction**

$$
\boxed{\frac{T_p}{C_d}\equiv
-\sum_{r=0}^{d}h_r[(8r+5)U_r-(8r+1)]\pmod p.} \tag{13b}
$$

**Proof.** Divide the B_r and h_r Pochhammer expressions. Use
(5/4)_r/(1/4)_r=4r+1, (3/2)_r/(1/2)_r=2r+1, and (1/2)_r/r!=binom(2r,r)/4^r. Then GH9 says T_p/C_d=-sum(8r+5)B_r modulo p; add the genuine original-S short sum, which is zero. This preserves two differently sourced summands, all ranks and the actual cutoff.

There is NO rank-constant source gauge: U_0=1, U_1=80/27, U_1-U_0=53/27, nonzero for every frozen p=19 mod24 (p>=19, p≠53). Equation (13b) isolates the nonlocal/global cancellation needed to prove GH3's still-open T_p=0 in the frozen 19-class; the cancellation itself remains unproved. The source-labelled GH3 port equations G_MM=-beta_b² T_p and G_LH=+beta_b² T_p retain their original conditional domain.

## Actually executed author exact checks

The companion local Python-stdlib checker executes exact Fraction-rational recurrence and integer modular arithmetic, and independent factorial-defined original S summands: 6 selected primes for rational (11); all 609 p=1 mod4 primes p<10000 for GH11 vanishing plus experimental strengthened next digit; all 147 p=1 mod4 primes p<2000 for every-rank GH12 modulo p², GZ-S p² consequence, original full S tail, three moments; all 154 p=3 mod4 primes p<2000 for GH13 rank gauge, proven defect equality and *experimental* zero. All actually run checks PASS. Neither the conjecture in GH12 nor the GH13 zero was proved by the finite runs.

Selected actual next-digit witnesses (p,d,T_p/p modp,C_d modp,chi_p,T_p/(pC_d),E_d/p,H_d,K_d):

- (5,1,4,1,-1,4,3,2,1)
- (13,3,4,4,1,1,2,0,0)
- (17,4,13,4,-1,16,6,0,9)
- (29,7,9,20,-1,28,9,21,5)
- (181,45,100,100,1,1,161,0,22)
- (373,93,59,59,1,1,24,0,351)

These p=181/373 are auxiliary checks, NOT the separately required native p=373 experiment.

## Typed research continuation

Mother D25-LIFT-JT2 remains OPEN. Next exact science: prove or refute the GH13 original-S sourced defect sum (13b) vanishes for EVERY frozen p=19 mod24 using actual finite-field/parameter WZ or character-sum proof, preserving original GH3 MM/LH labels; independently investigate GH12's three-component next-digit cancellation. Retain original W/S, BRC provenance and valuation/residual coordinates, R23/R36, original six Hasse J/E channels, finite endpoints, positive-direction infinity, H0/B0, [X]U mod p² and Frobenius eta/kappa. No native X6 embedding/readout has been established.

Current ordinary gateway 0.6.11 snapshot on 2026-10-28 showed research_authority_granted=false, executor_binding_configured=false, CONTROL_QUOTA at 5/5 and CODE_REVIEW_REQUIRED; recovery_status was advertised in status but no callable tool exposed to this connection. No new native winning CLAIM, authorized open/run, Source checkpoint or formal Research-Activity registration established. Historical session/staging/claim provenance and predecessor conflict tracked by enterprise-math#1558 remain preserved. This artifact represents portable author derivation, NOT Source accepted predecessor progress.