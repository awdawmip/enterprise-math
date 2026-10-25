# D25 — Polynomial Clausen tail and exact forced cubic moment

2026-10-25; TASK_RESEARCH author-side evidence; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Immutable science Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3
Research lane: chatgpt-research-onhour-enterprise-math-20260923. Maintenance lane is separate.

This is original author-side evidence, not a native CLAIM, Source checkpoint, Result, review, freeze, or original benchmark.

## Definitions

Let p=6m+1 >=7 be prime. All rationals are localized at p. Write

r_n = (1/6)_n (1/3)_n / [2^n (n!)^2],
c_n = (1/2)_n (1/3)_n (2/3)_n / [2^n (n!)^3],
M(z) = sum_{n=0}^{p-1} r_n z^n,
d_n = [z^n] M(z)^2.

Classical Clausen (prior art) gives d_n=c_n for n<p. We do NOT extend equality above this cutoff. The frozen original scalar is W_p=sum_{n<p}(6n+1)c_n.

## A. NEW ALL-PRIME THEOREM: polynomial-resolved signed cutoff

Define b_j = 2^{-j} binom(m,j) binom(2m,j) mod p for 0<=j<=m.
Let v_h = r_{p-h}/p^2 mod p, 1<=h<=m, where the existing reflected recurrence is
v_1=1/10,
v_{h+1}=v_h * 36 h^2 / [(6h+5)(3h+2)] mod p.

Let B_p(z)=sum_{t=0}^{p-2} d_{p+t} z^t, a polynomial with coefficients divisible by p^2.

PROVED, for all p=6m+1 >=7:

 B_p(z)/p^2 = 2 sum_{j=1}^m b_j sum_{h=1}^j v_h z^{j-h}  (mod p).

In particular the reduced polynomial has degree at most m-1. If e_t=2 sum_{j=t+1}^m b_j v_{j-t} mod p for 0<=t<m, then d_{p+t}=p^2 e_t mod p^3, and d_{p+t}=0 mod p^3 for t>=m.

Proof: The exact p-valuation of r_n for n<p is 0 (n<=m), 1 (m<n<=2m), 2 (2m<n<p), from the two p-factors at source numerator indices m and 2m. For a convolution pair i+j>=p, low+low, low+middle, and middle+middle have insufficient combined rank (at most 2m,3m,4m), while middle+high and high+high have valuation >=3. Thus only low+high and symmetric high+low contribute mod p^3. Write low index j<=m, high index p+t-j=p-(j-t); 1<=j-t<=j yields 0<=t<m. Low r_j=b_j mod p and high r_{p-h}/p^2=v_h mod p, with a factor 2 for rank orientation. This proves every coefficient and its support.

COROLLARY (every p-integral polynomial observer Phi):
  p^{-2} sum_{n=p}^{2p-2} Phi(n)d_n
   = 2 sum_{j=1}^m b_j sum_{h=1}^j v_h Phi(j-h) (mod p).

The pre-existing signed tail scalar T_p=Q_p/p^2 mod p with Q_p=sum_{n>=p}(6n+1)d_n is exactly the projection Phi(n)=6n+1, not a lossless replacement for all polynomial rank observers.

## B. NEW EXACT FINITE PICARD–FUCHS BOUNDARY AND ORIGINAL-RANK CUBIC CERTIFICATE

Set theta=z*d/dz and K_j=(theta^j M)(1), in particular K_0=M(1), K_1=N=sum_{n<p}n r_n.

The original coefficient recurrence n^2 r_n = (n-5/6)(n-2/3)r_{n-1}/2 proves an EXACT rational polynomial equation:

 [theta^2 - (z/2)(theta+1/6)(theta+1/3)] M(z) = -p^2 r_p z^p.

After evaluation and one theta derivative at z=1:

 K_2=K_1/2+K_0/18-2p^2 r_p.
 K_3=47 K_1/36+5 K_0/36-(3p^2+2p^3)r_p.

Let J_j=(theta^j M^2)(1). Applying the product rule and substituting these identities proves exactly

 J_3 - (3/2)J_2 - (13/18)J_1 - J_0/9
 = -4p^3 r_p K_0 -12p^2 r_p K_1.

An independent Wilson-product argument establishes r_p=1/36 mod p:
 r_p = product_{i=0}^{p-1}(6i+1)(3i+1) / [36^p (p!)^2].
The two numerator factors p occur only at i=m and i=2m. Removing them, each remaining factor set is the complete F_p^× with product -1; the denominator after removing p^2 is 36 mod p. Thus r_p is a p-unit of residue 1/36.

Define the cubic rank observer

 Phi3(x) = x^3 - 3x^2/2 - 13x/18 -1/9
         = (18x^3 -27x^2 -13x -2)/18.

By combining exact finite Picard–Fuchs forcing with classical Clausen only below rank p and Theorem A only above rank p, we PROVE the following unconditional all-prime congruence on the ORIGINAL truncated hypergeometric coefficients:

 sum_{n=0}^{p-1} Phi3(n)c_n
 + 2p^2 sum_{j=1}^m b_j sum_{h=1}^j v_h Phi3(j-h)
 = -(p^2/3) sum_{n=0}^{p-1}n r_n    (mod p^3).

This is a genuine additional exact moment conservation/forcing relation for D25, NOT proof of W_p=p mod p^3.

## C. Strict observer-loss counterexample

For p=13, m=2:
 b=(1,4,8), v=(4,9), e_0=7, e_1=12 modulo 13.
 Signed T_13=e_0+7e_1=0 mod13, yet cubic tail moment
 e_0 Phi3(0)+e_1 Phi3(1)=2 mod13 is NONZERO.
 Thus the scalar T_p is adequate only for its declared signed observer, not for subsequent cubic Picard–Fuchs operations. This is NOT a counterexample to original LIFT.

Observer/BRC implementation: exact signed coefficient, discrete rank t, and separate low/high p-valuation branch provenance are retained. No inference about positive mass, physical axes, or native six-dimensional world dynamics is made.

## D. Exact execution evidence

Companion local script: d25_frobenius_tail_operator_check_20261025.py
Run output: d25_frobenius_tail_operator_check_output_20261025.txt
95 primes p=6m+1 <=1200 plus p=19963 (53 target residue-class primes) passed the cubic congruence. At all 14 primes <=127, every tail coefficient was checked against independently computed original truncated convolution; at other primes, six selected inner/boundary coefficients were checked. The exact Fraction Clausen + K2 + K3 + J moment identities passed p=7,13,19. No floats or inferential numerical proof claims.

Representative (p,signed_T,cubic_tail,N_mod_p):
(7,3,2,1), (13,0,2,7), (19,12,6,1), (211,119,197,42), (19963,13363,17697,6798).

## E. Native/source boundary and precise next unfinished question

Frozen source pin unchanged. Native D25/SECOND-DIGIT-LIFT remains OPEN: prove/deny W_p=p mod p^3 on p=13,19 mod24; target Legendre/CM zero and full signed joint obstruction remain; original Delta_p-R_p observer, native benchmark, independent review and Result have not been satisfied. New theorem is a bound on a genuine future-observer gap, not an additional acceptance shortcut.

Gateway 0.6.11 Site authority is read-only (no Researcher write path). Exact continuation request research-onhour-20261025-2129-continuation-v1 returned CONTROL_QUOTA; scoped older request onhour-20261025-1930-research-cont-v1 returned CONTROL_REQUEST_NOT_FOUND (not proof of absence of all native effects). No own authenticated session/claim/run was recovered. Existing support issue awdawmip/enterprise-math#1539; preserve original requests and do not impersonate maintenance identity or replay a rejected write. This neutral GitHub note does not create native session/activity/Result.

NEXT EXACT ACTION: use a finite-field adjoint pairing on the intact polynomial cutoff and existing three-band L0/L1/L2 jets, seeking a direct signed-observer cancellation certificate for original D25 without presupposing the individual auxiliary sums vanish. Preserve the completed units and native benchmark requirement; no new scheduler was introduced.
