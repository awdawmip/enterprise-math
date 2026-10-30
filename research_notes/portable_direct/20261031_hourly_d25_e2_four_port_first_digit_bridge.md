# D25/LIFT — an exact four-port first-digit 216/E.2 bridge and signed E.2 harmonic reflection

2026-10-31 Asia/Hong_Kong. TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. D25 Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. P000 ACTIVE_LOCKED unchanged, external p-adic math only.

## Consumed frontier / exact original sources

The distinct onhour author proved the original 216/E.2 decomposition, with
A_p=sum_{n=0}^{p-1}(6n+1)a_n,
a_n=(1/2)_n(1/3)_n(2/3)_n/(2^n(n!)^3),
B_p=sum_{n=0}^m(6n+1)b_n,
b_n=(-1)^n(1/3)_n^3/(n!)^3,
p=6l+1, m=2l, h=3l, q=4l,
D0=sum_{n<=m}(6n+1)(a_n-b_n),
D1=sum_{m<n<=h}(6n+1)a_n.

The all-prime bridge to B_p modulo p^3 still requires two UNPROVED conditions:
D0+D1=0 (mod p^2), and, only after it, (D0+D1)/p^2+I_p=0 (mod p).
The previous source-bound signed I_p 4F3 evaluation was consumed, not recredited. The frozen original LIFT class is p mod24 in {13,19}.

## New exact four-port theorem

For 0<=n<=m define in Z_(p):
t_n=(-1)^n 2^{-n} binom(h,n)binom(m,n)binom(q,n),
v_n=binom(m,n)^3,
delta_N(n)=H_N-H_{N-n}=sum_{r=N-n+1}^N 1/r,
kappa_n=(1/2)delta_h(n)+(1/3)delta_m(n)+(2/3)delta_q(n).
For m<n<=h define the once-crossed original 216 coefficient
u_n=m!(n-m-1)! binom(h,n)binom(q,n)/(3 n! 2^n) (mod p).

Keep four distinct source/provenance ports:
C_p=(1/p)sum_{n<=m}(6n+1)(t_n-v_n) (mod p),
H_A=-sum_{n<=m}(6n+1)t_n kappa_n (mod p),
H_B= sum_{n<=m}(6n+1)v_n delta_m(n) (mod p),
U_p= sum_{m<n<=h}(6n+1)u_n (mod p).

**First prove C_p exists.** The finite-field Clausen identity gives
sum_{n<=m}a_n X^n=G_l(X/2)^2 (mod p),
G_l(z)=sum_{r=0}^l binom(l,r)binom(2l,r)z^r.
At the previously established frozen-class CM root G_l(1/2)=0,
sum_{n<=m}(6n+1)a_n = G_l(1/2)^2+6G_l(1/2)G_l'(1/2)=0 (mod p).
On the distinct E.2 side, b_n=binom(m,n)^3 (mod p), and pairing n with m-n preserves the binomial cube but makes the two original signed weights sum to 6m+2=2p. Thus sum_{n<=m}(6n+1)b_n=0 (mod p) **for all** p=6l+1, without CM. Original middle a_n are divisible by p, hence D0+D1=0 (mod p) in the frozen CM classes. Since t_n=a_n (mod p) and v_n=b_n (mod p), C_p has a p-divisible numerator and legitimate first-digit quotient.

**Theorem (under the precisely stated previous CM zero):**
(D0+D1)/p = C_p+H_A+H_B+U_p (mod p)
for all frozen p mod24 in {13,19}.

Full algebraic proof: the exact rising-factorial crossing identity for n<=N<p,
(-N+p alpha)_n/n! = (-1)^n binom(N,n) product_{r=N-n+1}^{N}(1-p alpha/r)
applied separately to original a_n factors 1/2=-h+p/2, 1/3=-m+p/3, 2/3=-q+2p/3 gives a_n=t_n(1-p kappa_n) (mod p²) for n<=m. For the distinct alternating E.2 source, three factors 1/3=-m+p/3 give b_n=v_n(1-p delta_m(n)) (mod p²), with the (-1)^n sign canceling the triple residue sign. For m<n<=h, the 1/3 factor crosses p once, yielding a_n=p u_n (mod p²), with all factorial denominators units. Substituting in the ORIGINAL D0+D1 proves
D0+D1=sum_{n<=m}(6n+1)(t_n-v_n)
 +p(H_A+H_B+U_p) (mod p²).
The first sum is divisible by p by the preceding CM/pair argument, so division by p proves the claimed four-port identity. This is a reconstruction formula, **NOT** a proof that its four-port sum vanishes in all primes.

**New antisymmetric reflection reduction of E.2 harmonic port**:
H_B=(1/2)sum_{n<=m}(6n+1)binom(m,n)^3(H_n-H_{m-n}) (mod p).
Proof: reflect n -> m-n, use symmetric v_n and
(6(m-n)+1)=2p-(6n+1); average the two exact expressions mod p. This preserves signed source provenance and DOES NOT imply H_B=0 separately.

## Executed exact verification

Accompanying standard-library Python checker d25_e2_four_port_20261031.py uses only integer modular residues, factorial unit inversion and independent original a_n,b_n recurrence modulo p², separate from four-port construction. All **166** frozen-class primes p<=5000 passed; exact formula and divisibility verified independently. The stronger first-digit bridge D0+D1=0 (mod p²) was observed at those 166 finite primes but is NOT universally proved.

p : C_p,H_A,H_B,U_p, sum (mod p)
13 : 0,0,7,6,0
19 : 1,9,2,7,0
37 : 20,36,2,16,0
157: 2,91,74,147,0
373: 26,138,182,27,0

For p373 the four NONZERO source-dependent ports sum to 373. Actual program marker:
PASS_D25_E2_FOUR_PORT_DIGIT_FORMULA_EXACT.
This is author-side scalar arithmetic, NOT original native p373 divided-power / H0-B0 / semilinear Frobenius.

## BRC and next exact task

BRC COMPOSE_APPLIED: typed carrier (p,l,n,original 216 or distinct E.2 source, p-valuation, signed weight, factorial unit, carry, harmonic defect, modulus). Future operations include source reflection, p-adic expansion, first-digit quotient after divisibility, signed aggregation. This is a sufficient carrier for this exact scalar first-digit observer but not the full original second digit, hidden source observers or Enterprise X6 native transfer.

**OPEN mathematical problem:** prove C_p+H_A+H_B+U_p=0 (mod p) for ALL frozen-class primes by an honest joint finite WZ/CM relation (or produce a counterexample). Then still prove the separately open second bridge (D0+D1)/p²+I_p=0 (mod p). Preserve the previous 11 Euler-Clausen ports and CM resonant H/J degree guard; do not repeat one-term Gosper or alter original fixed parameter.

Gateway 0.6.11: research_authority_granted=false, executor_binding_configured=false, native jobs 5/5, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. No new lawful session/CLAIM/OPEN/Source checkpoint/Result/review; service historical staging/session untouched. Formal Research-Activity REGISTER_PENDING/SYNC_DEBT. Existing support EM #1558 for native recovery, #1559 for original p373 evaluator. Author-side Git publication is not native Source completed_units or independent mathematical acceptance.

Inputs: onhour E.2 work at EM 79a574c7bc6ce2ec8b2de65e99689e2d3d3254fc; same-lane D25 gauge/Clausen theorem at EM 691c111bd013c8c72867721c10b8cd6cb3416e5d.