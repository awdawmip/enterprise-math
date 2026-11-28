# R284KF — Negative double fibers and whole-composite congruence sieve

2026-11-28. Author proof and executed exact computation; NOT_REVIEWED. Auxiliary arithmetic of R284, no native spatial attribution. Own recovered EM-DIRECT-0C386E / TASK_RESEARCH, RA-B82240E8488EF5A1DA5186C4; original registration r1-20261124-0256-r284gd-session-v1 open, no formal runs (r1-20261128-1000-own-recovery). Current owner inventory r1-20261128-1000-owner-inventory-v1 SUCCEEDED, no LEASED tasks in snapshot 2026-11-28T02:00:12.213067Z, source cc96d5d8a5e25dd712222f8971ebdd3655d2b93f, head advanced during read. No shared task acquisition or ownership mutation. Global entries at immutable main 9601583883c291941e7d9ab18122f351411c6c63; P000 V4/V5, ACTIVE worldview, joint observer/residual contracts, portable protocol and current research method consulted.

Frozen inputs: JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md (original rational observer and integer carrier); KE c0709a6e3bbbc1112f61f4e41285e97a25bd6142:research_notes/portable_direct/R284KE_AFFINE_ZERO_FIBER_AND_SIGNED_JET_SIEVE_20261128.md (simple formal affine root for d=2 mod 3); KD 544d7a97fa075fe62848ae1cf27acdb9bdc7df19:research_notes/portable_direct/R284KD_FINITE_BRIDGE_AND_MODULAR_FALLBACK_20261128.md as carried by KE (unique real root in 4d^2/5<=q<=4d^2/3 for d>=81, all legal integers excluded through d=3000). JP/JQ previously studied q=0, not this family of negative double fibers. No repeat of finite bridge.

## 1. Unbounded family of simultaneous vanishing fibers

Retain JR definitions: u=q+d, n=2q+d, R_v(k)=prod_{i=0}^{k-1}(v-i)/(v+i+3), l=d-k; a=(k+1)(l+1)R_u(k)R_n(l), b=(k+1)l R_u(k)R_n(l-1) for l>=1 and 0 otherwise, v_k=(u-k)(u+k+2)/(2u(2u+1)). V=sum a, Q=sum b, A=sum v_k(a+b), E=R_u(d)(u-d)(2d+3)(n+2)/(2(2u+1)(4n+2)), W=A+E, Z=qA+Q+V, C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2. The target equality implies C=0.

Define J_d={j integer: (d+1)/3<j<=d/2}, with d>=3. At q=-j the branch values U=d-j>=1 and N=d-2j>=0 are nonnegative integers and U+N=2d-3j<=d-2. All denominators are nonzero. R_U(k)=0 for k>U and R_N(l)=0 for l>N. In V, a nonzero term would require k+l=d<=U+N, impossible. In Q a nonzero term would require k+(l-1)=d-1<=U+N, also impossible. Thus V=Q=A=0. Since U<d, E=0 as well, including N=0. Therefore W=Z=0. Each rational observation is regular and divisible by q+j locally, so C is divisible by (q+j)^2. This proof applies to all three d residue classes (for d=3,5 the set is empty).

Writing prime as q derivative, define T_{d,j}=3(-j)(3d+1-4j)^2 W'(-j)Q'(-j)-32(d+1-3j) Z'(-j)^2. Then C(-j+h,d)=h^2 T_{d,j}+O(h^3), with Z'=(-j)A'+Q'+V', W'=A'+E'. This is the exact quadratic coefficient, not an assumption that the root has order exactly two. The coefficient is computed by the complete joint derivative recurrence; E' is retained. For d=2 mod 3 the previous KE simple root at j=(d+1)/3 lies immediately before, and is distinct.

## 2. Integer carrier compression and composite divisibility (no prime-factor restriction)

Use JR's D=2u(2u+1)(4n+2) D_u D_n, D_v=prod_{i=0}^{d-1}(v+i+3). P_d=D^2 C is an integer polynomial of degree 4d+9. For each j in J_d, D(-j) is nonzero, P_d(-j)=P_d'(-j)=0. The monic integer factor (q+j)^2 divides P_d in Z[q] by monic division; distinct linear factors are coprime over Q, so their product G_d=prod_{j in J_d}(q+j)^2 divides P_d in Z[q]. Define S_d=P_d/G_d. On legal q>=64, G_d>0 and D>0, so C=0 iff S_d=0. Its degree is exactly 4d+9-2|J_d| (|J_d|=floor(d/2)-floor((d+1)/3)); KE optionally supplies one additional simple factor for d=2 mod 3, not used here. No observation is dropped: the quotient is sign/zero preserving on the legal domain and the removed factor and denominator are retained.

At q=-j, Taylor expansion gives the exact identity
M_{d,j}=S_d(-j)=D(-j)^2 T_{d,j}/prod_{k in J_d,k!=j}(k-j)^2 in Z.
This integer can be computed directly without expanding the degree-O(d) polynomial. If a legal integer q is a root, q+j divides S_d(q)-S_d(-j)=-M_{d,j}, hence
    for every j in J_d: q+j | M_{d,j}.
If M_{d,j}=0 this constraint is vacuous; if nonzero it bounds q+j by |M_{d,j}| and restricts it to positive divisors. Unlike a large-prime-only test, this is an exact congruence of the entire composite q+j, including powers and small factors. Different j constraints must hold for the same q. This is an independent whole-composite sieve; no independence assumption, factorization requirement, or heuristic discarding of the composite road. Intersect with KD's bracket when applicable.

## 3. Prime-fiber valuation and third jet

For prime p>2d+2 and j in J_d, all original denominator factors at q=-j are p-units: the R denominators are positive <=U+d+2<=2d+2, 2U,2U+1 and 4N+2 are <=2d+2 (N<d/3). Products and inverse expansions consequently have coefficients in Z_p. C(-j+h)=h^2(T+U_3 h+...) with integral coefficients. For p|q+j, if T is a unit, v_p(C)=2v_p(q+j). Thus integer equality implies p|num(T) for each eligible large prime, regardless of valuation. No assertion that such primes must exist.

When T is divisible by p, put B=T/p mod p and A_3=U_3 mod p. For q=-j+pt:
 C/p^3 = t^2(B+t A_3) mod p.
A_3 can be computed as C(-j+p)/p^3-B mod p from C mod p^4. In the KD bracket, 0<q+j<=4d^2/3+d/2 < (2d+2)^2 < p^2, so 1<=t<p. A_3!=0 gives at most one actual q candidate in the entire bracket; A_3=0,B!=0 gives none. If both vanish, higher jets or another coordinate are needed. The actual formal root q=-j remains in Z_p, so no claim that the entire residue ball is root-free. The exact polynomial quotient and the prime jets are different observers of the same primal C.

## 4. Executed exact calculations

Python Fraction for jets and integer modular inverses for original C; trial-division primality; no floating point. Complete test domain d=4..120, all j in J_d, all primes 2d+3<=p<=8d+8. Checked simultaneous vanishing, and independent C(-j+p), C(-j+2p) mod p^3; for every exception also C(-j+2p), C(-j+3p) mod p^4. Output:
 {'fibers': 1180, 'positive': 39, 'prime_pairs': 93739, 'unit': 93482, 'exception': 257, 'linear_unit': 257, 'negative': 1141}
Every tested T nonzero; every exceptional prime pair has nonzero third-jet slope. The bracket test for all d in this finite run produced 12 candidates (2 at d<81, where it is only a test interval, not a KD theorem application). Every candidate was verified to have C=0 mod p^4 and C!=0 mod p^5. Rows (d,j,p,q,C/p^4 mod p):
 [(56,23,131,4038,130),(63,22,139,3453,84),(81,40,193,5750,23),(83,34,193,6335,189),(86,43,307,6711,135),(88,31,179,7845,5),(88,41,379,9055,106),(96,33,197,8438,48),(102,36,223,11560,80),(103,39,241,12493,147),(109,46,269,13673,234),(119,54,241,15852,1)].
For d>=81 in the tested d,p range, all eligible large-prime fibers q+j=0 mod p are closed on KD's bracket. No uniform nonzero T or third-jet theorem yet.

Independent composite sieve test d=81..120, start with all integer q in KD bracket. Compute M_{d,j} by exact Fraction and assert denominator=1; test modulo q+j sequentially until candidate list empty. All 40 d closed after 284 evaluations of M (average 7.1 per d). Output:
 {'initial': 218330, 'after_first': 67897, 'after_second': 17191, 'closed': 40, 'fibers_used': 284}
 max_after_first 2413; survivors [].
This is an alternative certificate of all-budget integer exclusion for those d by the KD bracket, including smooth q+j. It does not extend KD's already certified d<=3000. The finite calculation is not evidence of a uniform closure theorem.

Exact replay files (same folder when running both):
- cb1d25a1d9b8c0e5f538f78b22b6cc6d64f35644:research_notes/portable_direct/R284KF/kf_final.py, Git blob 6a9d4249f2e9b1a40366649b169700c543518fc3, SHA256 c32180c1ad8aea3223c05d0dc4eb8c0378a163285367068ec6be7e853118c85c.
- b906828c959c3b65df3d07f2438115e3ae519ab0:research_notes/portable_direct/R284KF/kf_composite.py, Git blob 64af093581b43f1b3c2e153d57b89b264ad27fef, SHA256 7ee1117d24dc4412d868782b246aa0a76d9528cd1bf5dd9de7c6d9c7b6662321.
Both remote blobs read back and matched executed local file blobs; first upload had a transcription typo in the primal C formula, corrected by CAS before claiming verification.

## 5. Frontier

Study joint arithmetic of M_{d,j} as j varies rather than independently factoring each number. In particular, divide S_d by its integer content to strengthen every composite congruence; find a uniform tractable content divisor and exact factorial/recurrence structure in T_{d,j}. Investigate whether the consecutive q+j constraints cannot all hold in KD's bracket for d>3000, or produce a verified survivor of that necessary sieve. The observed sign pattern (positive only for the first j of d=1 mod 3, negative for the others in this tested domain) is a conjectural clue, not a theorem. Combining KE's simple factor and existing JP/JQ/JO constraints remains useful. JY/JZ sparsity and KD coverage keep their original scopes. No formal Result, independent Review or theorem admission.
