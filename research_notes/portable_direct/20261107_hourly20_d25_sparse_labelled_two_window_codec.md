# D25: Sparse two-window recovery of every j-labelled source weight

2026-11-07 Asia/Hong_Kong. AUTHOR-SIDE PROVED ALGEBRA / EXACT FINITE TESTS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science input c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane is chatgpt-research-hourly-enterprise-math-20260923. This is an auxiliary BRC-labelled hypergeometric observer, not an X6, H0/B0 or native Frobenius experiment.

## Exact model and theorem

Let p=6m+1>=7 be prime; set a=2m, b=3m, c=4m, A_s=Z/p^sZ for arbitrary s>=1, and G_j(t)=binom(t-a,j)binom(t,j) for 0<=j<=b. Generalized binomials mean polynomials; all j! are invertible in A_s. Allow arbitrary unknown labelled coefficients u_0,...,u_b in A_s and define F_u(t)=sum_{j=0}^b u_j G_j(t).

Observe only the following TWO WINDOWS of scalar values:
 S={0,1,...,a-1} union {c,c+1,...,c+m}.
There are exactly a+m+1=b+1=(p+1)/2 observations. Order both windows increasingly, and match row j to t_j=j for 0<=j<a, then row j=a+r to t_j=c+r for 0<=r<=m.

THEOREM: the (b+1)x(b+1) matrix M_{j,k}=G_k(t_j) is lower triangular with p-adic unit diagonal, hence an isomorphism over A_s for every s and over Z_(p). It recovers every individual labelled weight u_j, with NO loss of p-adic precision. In particular every original source port u_j G_j(t), normal/carry aggregation, full polynomial, and any polynomial derivative can subsequently be computed from these observations without further original scalar queries.

Proof. If j<a then t_j=j; for k>j the factor binom(t_j,k)=0. At k=j, the diagonal equals binom(j-a,j)=(-1)^j binom(a-1,j), a p-unit. For j=a+r (0<=r<=m), t_j=c+r and t_j-a=a+r=j; for k>j the factor binom(t_j-a,k)=0. Its diagonal equals binom(c+r,a+r)=binom(c+r,a), a p-unit since 0<=a<=c+r<=5m<p. Consequently
 det(M)=product_{j=0}^{a-1}[(-1)^j binom(a-1,j)] * product_{r=0}^{m} binom(c+r,a+r),
an element of Z_(p)^times. Forward substitution successively computes u_j from F_u(t_j), dividing only by the p-units M_{j,j}. The inverse matrix has coefficients in Z_(p), so recovery preserves all s digits. QED.

OPTIMALITY within the DECLARED unrestricted labelled-weight class: it has b+1 free field coordinates. Fewer than b+1 scalar linear observations over F_p have a nonzero kernel; thus the count is minimal for recovering all u_j. Explicitly, the last port G_b(t) vanishes on every point of S except t=c+m, where G_b(c+m)=binom(5m,3m) is a p-unit. So omitting the last query leaves u_b invisible. This is a different observer class from the previous full degree <=p-1 normal/carry polynomial pair class, whose unrestricted dimension is p.

COROLLARY for the concrete D25 source coefficients u_j=(6j+1)(-1/2)^j binom(3m,j): u_0=1 is known. The sample t=0 can be omitted. The remaining b=(p-1)/2 scalar samples uniquely reconstruct all unknown u_1,...,u_b modulo p^s. Thus the original labelled-source family uses exactly HALF of the p-entry scalar table, with the fixed zeroth source supplied.

## Connection to the open tangent

The source polynomial in previous D25 results is F_m(t)=P_m(t-4m)=sum_j u_j G_j(t). The recovered weights determine the exact derivative at t=c:
 for 0<=j<=a:
 G_j'(c)=binom(a,j)binom(c,j)[H_a-H_{a-j}+H_c-H_{c-j}];
 for a<j<=b:
 G_j'(c)=(-1)^(j-a-1) a!(j-a-1)!/j! * binom(c,j).
These are identities in Z_(p), with all needed denominators p-units. Hence the two-window observer determines separately
 N'(c)=sum_{j<=a}u_j G_j'(c), R'(c)=sum_{j>a}u_j G_j'(c)
at every p-adic precision, and thereby the second digit lambda_p=F_m'(c)/p mod p when the first digit vanishes. This is an exact sourced reconstruction, not a proof that F_m'(c)=0 mod p in general.

## Executed exact checks

The companion standard-library Python code verifies all 80 primes p=6m+1 <=1000, at s=1,2, both original D25 weights and synthetic arbitrary weights: 320/320 PASS. At p=13,109,373 it additionally verifies s=3 with both weight sets: 6/6 PASS; TOTAL 326/326. All cases recover all j labels, check unsampled gap values, verify source-separated derivative, and confirm the last-port witness. For each original-weight case it also skips t=0 using known u_0=1.

Concrete p=373: m=62,a=124,b=186,c=248. The unconstrained two-window codec uses 187 samples (t=0..123 and t=248..310); D25 with known u_0 uses 186. The recovered sourced tangent agrees modulo 373^2 with N'(248)=62372, R'(248)=4768, F'(248)=67140=373*180.

## BRC and next mathematical unit

Carrier: indexed integer source j with exact coefficient u_j and normal/carry label. Observer: selected F_u(t) scalar values modulo p^s. Future operations: reconstruction of each port, arbitrary polynomial evaluation and jets, and sourced second-digit analysis. Resolution: COMPOSE_APPLIED, extending the existing D25 Newton source representation with an exactly invertible triangular port basis; not an unrelated tool family. Lossless for this source-family input; creating observations from the raw finite sum has separate cost O(b^2) with naive evaluation. Forward inversion also costs O(b^2) arithmetic and O(b) storage. No generic runtime speedup is asserted.

Next unit: derive a direct sparse-sample linear functional for F_m'(4m)/p modulo p (where the first digit is zero), seek smaller specialized observation sets for tangent-only recovery, and test the second-digit carry correction against Wieferich p=1093,3511. The frozen mother Delta_p-R_p=0 mod p, p=13,19 mod24, remains OPEN and retains independent native H0/B0/Frobenius obligations.

## Native control and contribution boundary

The 2026-11-07 05:22 Asia/Hong_Kong em_status attempt returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Site is CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Existing target request IDs em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 are preserved; old session, pending staging, claim and run remain unverified. Support path awdawmip/enterprise-math#1558. This is portable author evidence, not a native checkpoint, formal claim, Result, independent review or admitted mathematics.