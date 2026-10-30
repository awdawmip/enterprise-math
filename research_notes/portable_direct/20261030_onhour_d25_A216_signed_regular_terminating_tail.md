# D25 / SECOND-DIGIT-LIFT — original A216 middle port as a regular, signed terminating kernel

Date: 2026-10-30 Asia/Hong_Kong. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Research logical conversation chatgpt-research-onhour-enterprise-math-20260923 is distinct from maintenance. The frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.

Status: AUTHOR-SIDE / PROVED ORIGINAL-PORT ALGEBRAIC LEMMA / EXECUTED EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

## All-prime theorem (PROVED)

Let p=6m+1>=7 be prime. Define a_n=binom(2n,n)^2 binom(3n,n)/216^n and w_n=(6n+1)a_n. Define the original signed sources A_low=sum_(0<=n<=3m) w_n and A_mid=sum_(3m+1<=n<=4m) w_n. All divisions below are made over Z_(p) before reduction.

Define the uniform finite-field recurrence
r_0=1,
r_(s+1)=r_s*(6s+7)*(6s+5)*(s+1)/[9*(2s+3)^3] mod p,
and H_reg(p)=sum_(s=0..m-1)(6s+4)r_s mod p.

THEOREM: A_mid/p^2 = ( (-2/p)/9 ) H_reg(p) (mod p), with (-2/p) the Legendre symbol. No denominator vanishes for 0<=s<=m-1. At the first omitted step s=m-1 the factor 6s+7=p makes r_m=0 mod p: a regular *zero* boundary, in contrast to the 6s+7=p denominator pole in the earlier reflected H_m kernel.

In the frozen classes p=13 mod24 the prefactor is -1/9; for p=19 mod24 it is +1/9. The class sign is necessary BRC observer data.

## Complete exact proof

Put (x1,x2,x3)=(-3m,-2m,-4m) and (lambda1,lambda2,lambda3)=(1/2,1/3,2/3), and define one finite polynomial

F_m(T)=sum_(n=0..4m) (6n+1)*[product_(i=1..3)(x_i+lambda_i*T)_n] / [2^n*(n!)^3].

Exactly at T=p, its three parameters are 1/2,1/3,2/3, so F_m(p)=A_low+A_mid. All original coefficients from n=4m+1..p-1 have at least THREE p-factors, so A_p=F_m(p) mod p^3.

At T=0 distinguish THREE genuine zero-factor zones: n<=2m has no zero factor; 2m<n<=3m has one zero factor at (-2m+T/3), j=2m; and 3m<n<=4m has TWO zero factors, (-3m+T/2) at j=3m and (-2m+T/3) at j=2m. The latter multiply to T^2/6. Thus the coefficient of T^2 in zone three, without a reflection or singular parameter division, is exactly A_mid/p^2 mod p.

Write n=3m+1+s, 0<=s<m, and let d_s be the *unweighted* coefficient of T^2 in its hypergeometric term. Removing the two zero factors gives

d_s = [product_(j<n,j!=3m)(-3m+j) * product_(j<n,j!=2m)(-2m+j) * product_(j<n)(-4m+j)] / [6*2^n*(n!)^3].

Using product_(j<n,j!=k)(-k+j)=(-1)^k*k!*(n-k-1)! for n>k yields

d_0=D_m= -m*(3m)!*(2m)!*(4m)!/[6*2^(3m+1)*((3m+1)!)^3]
and
d_(s+1)/d_s=(s+1-m)*(s+1)*(m+s+1) / [2*(3m+s+2)^3].

This is an EXACT terminating rational sequence: the upper factor 1-m kills s=m. The zone-three T^2 coefficient equals sum_(s=0..m-1)(18m+7+6s)d_s.

Now reduce the exact ratio modulo p=6m+1. Use 1-m=7/6, m+1=5/6, 3m+2=3/2, 18m+7=4 (mod p) to obtain

(d_(s+1)/d_s) = (6s+7)(6s+5)(s+1)/[9(2s+3)^3] (mod p).

Thus A_mid/p^2=D_m*H_reg mod p. The m-dependent terminating hypergeometric representation is the differential (18m+7+6 theta) applied at z=1/2 to the terminating 4F3(1-m,1,1,m+1;3m+2,3m+2,3m+2;z), times D_m.

Wilson and binom(p-1,k)=(-1)^k show (2m)!(4m)!=-1 mod p and 1/((3m)!)^2=(-1)^(m+1) mod p. Also m=-1/6 and 3m+1=1/2 mod p. Consequently D_m=(-1)^m/[9*2^(3m)] mod p. Euler's criterion, 3m=(p-1)/2 and parity(m)=parity(3m), gives D_m=((-2/p))/9 mod p. This completes an all-prime proof without conjectural input or a p-divisible denominator.

## Strict equivalent live LIFT obligation

Consume the accepted D24 first digit and the earlier *original* finite Clausen interface Delta_p-R_p=(A_p-p)/p^2 mod p. In BOTH frozen classes,

LIFT iff (A_low-p)/p^2 + ((-2/p))/9*H_reg(p) = 0 mod p.

This removes the old singular reflection-kernel port and its factorial prefactor. The unchanged original signed middle source is now one p-independent regular recurrence with a **zero** at the next term, and the full A216 observer is a *single* finite polynomial F_m(T) with exactly three zero-factor zones. Existing two-zone A_low jet is reused; the all-prime LOWER-to-MIDDLE cancellation is still OPEN. The older negative Gosper result concerned the different singular kernel and cannot exclude a paired m-dependent WZ/contiguous certificate on this regular polynomial.

BRC COMPOSE_APPLIED: original model A216, integer n, weight 6n+1, source valuation band 0/1/2/3, exact zero-factor locations and their slopes, prime class sign, precise p-local T^2 observer and future signed addition all retained. Here the external arithmetic finite-field observer is NOT a proof of native Heartbeat X6/H0/B0 equivalence.

## Executed exact evidence

The accompanying standard-library Python checker d25_regular_signed_tail_guard_20261030.py ran for every one of the 115 primes 7<=p<1500, p=1 mod6, including all 60 primes p=13/19 mod24. It checks the genuine original weighted A216 stream modulo p^3, original middle port, factorial D_m, new regular recurrence, divided low-port residual and the unproved LIFT for those finite cases; independent raw original integer-binomial checks for p=7,13,19,31,37,43,373. All passed. The executed identical standalone script had SHA-256 07342780c9cbc31147f5f2b542fbfa3a2549ba171904f528596587c4c6d3be51.

p | chi(-2) | D_m | H_reg | A_mid/p^2 | (A_low-p)/p^2
13 | -1 | 10 | 1 | 10 | 3
19 | +1 | 17 | 5 | 9 | 10
373 | -1 | 290 | 217 | 266 | 107

At p=373, 290*217=266 mod373 and 107+266=0 mod373. This is finite regression, not a universal LIFT proof.

Related literature with distinct proof status: Zhi-Hong Sun (AIMS Mathematics 7(2), 2022), Conjecture 5.30, uses the original 216/2304 coefficient families with *reciprocal weights* modulo p^2; it is a conjecture, not an input theorem or the original weighted p^3 LIFT. Guo-Zudilin (Adv. Math. 346, 2019), the *proved* B2304 dual cutoff is separately consumed, not re-proved.

## Authentic Source and next actions

2026-10-30 current Site gateway advertised research_authority_granted=false, write_relay_enabled=false and no executor binding. The actual Source session/CLAIM/run/request/recovery is UNKNOWN here, no formal operation and no Source checkpoint/Result/review is claimed. This author-side project Git note does not establish legal task ownership or independent admission.

High-priority authentic support issue #1559 was GitHub-read OPEN/unassigned on 2026-10-30; same-original-class p373 native H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius/eta, signed odd Green/Hesse, kappa, original Delta-R, exact code and independent replication remain PENDING_OWNER / NOT_EXECUTED. An authorized owner must execute the unchanged original benchmark. Next smallest mathematical action is construct finite WZ/parameter-contiguous pairing on the ONE polynomial F_m(T), preserving its three zero-factor zones and the class-signed regular kernel, to prove or refute the last cancellation for both target classes. Accepted D24 UR, prior B2304 dual cutoff and original Clausen interface are fixed dependencies and not re-done. Original scientific pin/P000/worldview and other Claims/schedulers/notifications are unchanged.
