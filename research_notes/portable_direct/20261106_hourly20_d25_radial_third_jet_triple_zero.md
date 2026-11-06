# D25: cubic radial source jet, one-carry decomposition and p=5113 triple zero

2026-11-06, Asia/Hong_Kong. Author-side portable TASK_RESEARCH; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.

## Theorem (exact rational identity)

Let m>=1, a=2m, b=3m, c=4m, and
P_m(z)=sum_{j=0}^b (6j+1)(-1/2)^j binom(b,j) binom(a+z,j) binom(c+z,j)
over Q[z]. Set H_n^(r)=sum_{h=1}^n 1/h^r and H_0^(r)=0.

For j<=a, define U_j=(-1/2)^j binom(a,j)binom(b,j)binom(c,j),
L_j=H_a-H_(a-j)+H_c-H_(c-j),
R_j=H_a^(2)-H_(a-j)^(2)+H_c^(2)-H_(c-j)^(2),
S_j=H_a^(3)-H_(a-j)^(3)+H_c^(3)-H_(c-j)^(3).
For a<j<=b, define
E_(a,j)=(-1)^(j-a-1) a!(j-a-1)!/j!,
M_j=H_a-H_(j-a-1)+H_c-H_(c-j),
N_j=H_a^(2)+H_(j-a-1)^(2)+H_c^(2)-H_(c-j)^(2).

Then, for every m>=1, the third coefficient is exactly
[z^3]P_m(z) = HEAD_3 + CARRY_3,
HEAD_3=sum_{j=0}^a (6j+1)U_j (L_j^3-3L_j R_j+2S_j)/6,
CARRY_3=sum_{j=a+1}^b (6j+1)(-1/2)^j binom(b,j)binom(c,j)E_(a,j)(M_j^2-N_j)/2.
When p=6m+1 is prime (p>=7), all denominators are p-units, so reduction mod p is valid.

Proof: for j<=a, both outer binomial factors have nonzero constant terms; their nonzero linear factor reciprocals have power sums L,R,S. Newton's identities give elementary symmetric e3=(L^3-3LR+2S)/6. For a<j<=b, the a-source contains exactly one zero factor z, with product of other factors equal to E_(a,j) in its binomial coefficient. Their reciprocal sums together with the c-source are M,N; e2=(M^2-N)/2 is the third coefficient after multiplication by z. For j>b the unperturbed b-source binomial is identically zero. Indices are <p and all remaining factorial and reciprocal denominators are units mod p. QED.

This extends the earlier second-jet head/carry theorem (research_notes/portable_direct/20261106_hourly20_d25_radial_curvature_head_carry_2143.md) while preserving normal indices j<=2m and first-carry indices 2m<j<=3m as separate BRC sources.

## Verified p=5113 triple zero

At m=852, independent truncated-polynomial and reciprocal-factor calculations give
[z^0..z^3]P_852(z)=(0,0,0,3783) mod 5113.
HEAD_3=4774, CARRY_3=4122, and (4774+4122) mod 5113=3783 != 0.
Thus z=0 has exactly multiplicity three in P_852(z) over F_5113.
The zero second jet (HEAD_2=3519, CARRY_2=1594) was previously published and is not recounted as new.

A genuinely separate direct-modulus test evaluated E(t)=P_852(5113t) mod 5113^4 at t=0,1,2,3:
E=(610854945333422,135964409472485,269664176976589,628728155215035).
The third forward difference is 300218278356662=2246*5113^3 mod 5113^4.
Since every coefficient of P_852 is 5113-integral and the third finite difference eliminates powers t^0,t^1,t^2, this tests 6*[z^3]P_852 = 2246 mod 5113. It passes.

The two direct coefficient algorithms agree for ten test primes: 7,13,19,109,211,229,373,1093,3511,5113. Exact integer-only reproducibility: d25_radial_third_jet_20261106.py and d25_radial_third_difference_p5113_20261106.py. These prove the rational formula algebraically and certify the stated finite instance; no original native H0/B0 experiment or universal supercongruence is claimed.

## Continuation and control

Mother goal: Delta_p-R_p=0 mod p for p mod24 in {13,19}. Next discriminating science unit: characterize primes with simultaneous vanishing of the quadratic and cubic radial jets, or find a head/carry telescoping identity for the open universal T1+T3=0. Preserve original Frobenius, H0/B0, eta/kappa and independent review obligations.

Configured research-lane label chatgpt-research-hourly-enterprise-math-20260923 is not proof of actual service identity; maintenance lane chatgpt-hourly-enterprise-math-20260921 was not used for writes. Original request IDs em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 returned QUEUED after bounded same-ID reconciliation, with prior EVENT_COLLECTION_IO fault retained. Current old session/protected staging/claim/run unverified; no new native CLAIM, OPEN, publish_checkpoint, Result or role transition. Support path: Enterprise Math issue #1558.
