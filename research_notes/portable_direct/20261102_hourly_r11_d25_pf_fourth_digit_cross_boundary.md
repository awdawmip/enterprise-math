# D25: universal fourth-digit Picard–Fuchs boundary and exact 16/3 inter-stream ratio

Date 2026-11-02 (Asia/Hong_Kong). Classification: AUTHOR-DERIVED / EXACT PROOF / 428 PRIME CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Frozen Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. P000 and ACTIVE worldview unchanged. This is the second substantive research unit following 20261102_hourly_r11_d25_pf_threeport_model_closure.md.

## Theorem: exact normalized boundary, for every prime p>=5

For alpha-sets A=(1/2,1/3,2/3), B=(1/4,1/2,3/4), write
 F_{a,p}(z)=sum_{k=0}^{p-1} c_k z^k, c_k=prod_{alpha in a}(alpha)_k/(k!)^3,
 theta=z d/dz, s1=sum alpha, s2=sum_{i<j}alpha_i alpha_j, s3=prod alpha,
 L_a=(1-z)theta^3-z(s1 theta^2+s2 theta+s3).
The preceding unit proved the exact finite endpoint identity
 L_a F_{a,p}(z)=-c_{p-1}prod_{alpha in a}(p-1+alpha)z^p.       (1)

NEW GENERAL COEFFICIENT LEMMA, BOTH FAMILIES:
                  c_{p-1}/p^3 = -1 (mod p).                   (2)

Proof. For any parameter 0<a<b<=4, with gcd(a,b)=1, let j0 in [0,p-2] be the unique index where a+b j0=t p, t in {1,...,b-1}; equivalently t p=a (mod b).
In the length p-1 Pochhammer numerator prod_{j=0}^{p-2}(a+bj), one term equals tp. The other p-2 residues cover the nonzero residue classes modulo p except a-b, which would be attained at the omitted j=p-1. By Wilson and Fermat,
 [(a/b)_{p-1}/p] mod p
 = b^{-(p-1)}t[-1/(a-b)] = t/(b-a) mod p.                  (3)
Here 1/2 has unit 1. For the (1/3,2/3) pair, the units are (1/2,2) when p=1 mod3, (1,1) when p=2 mod3; their product is 1. For (1/4,3/4), the units are (1/3,3) for p=1 mod4, (1,1) for p=3 mod4; again product 1. Dividing by ((p-1)!)^3 = (-1)^3 mod p establishes (2). Each factor is exactly p-divisible once, so c_{p-1} has exact valuation three.

The endpoint product reduces to -1/9 for A and -3/32 for B. Therefore the *first nonzero finite truncation source*, at p^3, is
 [L_A F_A(z)/p^3] = -z^p/9 (mod p),
 [L_B F_B(z)/p^3] = -3z^p/32 (mod p).                   (4)
At the original observation points z_A=1/2 and z_B=1/9, Fermat gives
 E_A=[L_A F_A(1/2)/p^3]=-1/18 (mod p),
 E_B=[L_B F_B(1/9)/p^3]=-1/96 (mod p).
Thus
                  3 E_A - 16 E_B = 0 (mod p)                 (5)
for all primes p>=5, with prime-independent cross-family ratio E_A/E_B=16/3.

The invariant (5) couples the two *source-labeled Picard–Fuchs boundary defects*. It does not assert a scalar match of the first CM jets, original weighted sums or the mother supercongruence. It is exact source data at the fourth p-adic digit which the mod-p^3 homogeneous equation forgets.

## Independent exact integer verification

The companion standard-library modular checker rebuilds each original truncated coefficient stream modulo p^4, checks (2), directly sums Euler jets f0..f3 at original z and evaluates L_a F modulo p^4, verifies the exact endpoint (1) and (4), then checks (5). All 428 primes 5<=p<=3000 pass, including all 107 D25 target primes in that window.

Selected certificates (p,E_A,E_B,3E_A-16E_B modp):
 (13,5,5,0), (19,1,18,0), (37,2,5,0),
 (373,145,237,0), (1171,65,1110,0).

## BRC and continuation

BRC: COMPOSE_APPLIED / SOURCE_BOUNDARY_UNIT_RETAINED. Carrier is original index and hypergeometric coefficient provenance, exact p-valuation, weighted differential operator, rational observation point, family label and normalized fourth-digit defect; future readout is source-aware cross-family boundary comparison. This builds on this run's preceding model-specific three-base-jet closure and two-port gauge formula: modulo p^3 homogeneous PF closure is a sufficient observer for that earlier next-digit gauge operation, while (4) gives its precise p^4 boundary repair.

Next: use the boundary normalization (5) as one exact input in a candidate non-scalar CM/character-sum/WZ transfer between source-tagged pairs (f1_A/p,f2_A) and (f1_B/p,f2_B). Preserve q, weighted resonance and Clausen signed tail; test separately against p373 228:114,138,365,316,91. Frozen mother Delta_p-R_p=0 modp on p mod24=13,19 remains open.

Status: author-side algebra plus finite exact checks; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING; native H0/B0 not executed. Current native Gateway 0.6.11 as of 2026-11-02T00:18:28Z shows CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, jobs 5/5. Historical own read-only recovery #6637 succeeded; continuation #6638 definitively failed and was not replayed; #1558 control and #1559 H0/B0 still own their separate duties. No Source CLAIM/OPEN/checkpoint/Result/review or scheduler/notification change.
