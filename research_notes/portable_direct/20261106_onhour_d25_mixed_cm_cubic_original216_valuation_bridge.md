# D25 — Mixed-CM cubic coefficient / original-216 valuation bridge

Date: 2026-11-06. TASK_RESEARCH on-hour logical lane: chatgpt-research-onhour-enterprise-math-20260923 (maintenance lane excluded). Publication TP2-B6F4FC938FF94941C1B7, frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3. Scope: exact author-side finite identities and prime valuations; independent finite arithmetic check; separately attributed external preprint. Status: AUTHOR-PROVED / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED. No native H0/B0 execution.

## 1. Exact normalized original-216 convolution

Reuse the previously proved exact Clausen identity for G(z) = 2F1(1/6,1/3;1;z):
G(z)^2 = sum_{k>=0} (2^k a_k) z^k,
where a_k = (2k)!(3k)!/[216^k (k!)^5].

Put gamma_k = 216^k a_k = binom(2k,k)^2 binom(3k,k), b_n = 108^n (1/6)_n(1/3)_n/(n!)^2, B(z)=G(108z)=sum b_n z^n, A_n=[z^n]B(z)^3. Substitution yields B(z)^2=sum gamma_k z^k.

**Theorem (all integers n>=0, exact in Q):**

A_n = sum_{k=0}^n gamma_k b_{n-k},
sum_{k=0}^n (6k+1) gamma_k b_{n-k} = (4n+1)A_n.                    (E1)

Proof: first identity extracts [z^n]B^2 B. With theta=z d/dz, theta(B^2) B=(2/3)theta(B^3). Hence (1+6theta)(B^2) * B = (1+4theta)(B^3). Extract coefficients. No primality or interpolation is used.

## 2. External mathematical theorem used with attribution, not substituted for W

Alex Shvets, "Split-prime supercongruence at the mixed CM point (1/6, 1/3; 1)," arXiv:2605.19773 (submitted 2026-05-19), https://arxiv.org/abs/2605.19773 , states/proves that A_{mp} == A_m (mod p^4) for p>=7, p==1 (mod 3), m>=1, with the A_n just defined. A_1=18. Consuming that external claim yields for all p==1 (mod 6):
sum_{k=0}^p gamma_k b_{p-k} == 18 (mod p^4),
sum_{k=0}^p (6k+1) gamma_k b_{p-k} == 18(4p+1) (mod p^4). (E2)
Attribution and proof/admission status of this preprint are separate from the exact elementary identities here. E2 is **not** the original W_p congruence.

## 3. Exact p-adic valuations and source-preserving omission

**Theorem (all primes p=6m+1>3):** for 1<=k<=p-1,
v_p(gamma_k b_{p-k}) equals:
* 2 for 1<=k<=2m;
* 3 for 2m+1<=k<=3m;
* 4 for 3m+1<=k<=5m;
* 3 for 5m+1<=k<=6m.                              (E3)

The endpoints gamma_p, b_p are p-adic units.

Proof: for 0<=k<p, v_p(gamma_k)=floor(2k/p)+floor(3k/p). For 0<=n<p, the recurrence b_0=1, b_n/b_{n-1}=6(6n-5)(3n-2)/n^2 proves v_p(b_n)=0 at n<=m, 1 at m+1<=n<=2m, 2 at 2m+1<=n<p. At n=p its numerator has exactly two p-factors, canceled by n^2, hence v_p(b_p)=0; Legendre's factorial formula gives v_p(gamma_p)=0. Substitute n=p-k. All ranges in E3 follow, including endpoints.

Let L=sum_{k=1}^{2m} gamma_k b_{p-k}, M=sum_{k=2m+1}^{3m} gamma_k b_{p-k}, U=sum_{k=5m+1}^{6m} gamma_k b_{p-k}. Then, independently of E2,
A_p == b_p + gamma_p + L + M + U (mod p^4).       (E4)
Here L is p^2-divisible, M and U p^3-divisible; the intervening k=3m+1..5m band is p^4-divisible. This is a BRC typed observer with distinct original-index/sign/valuation carriers; neither live p^3 band can silently disappear. Multiplication by (6k+1) cannot lower the listed valuations.

**Exact two-index failed transfer:** There is no p-adic unit C satisfying b_{p-k}==C*216^(-k) (mod p) simultaneously at k=0 and k=1. k=0 forces C unit because b_p is unit; at k=1 b_{p-1} has valuation 2, whereas C/216 is unit. This rules out one naive pointwise scalar-kernel identification, not general signed multiport adjoint transfers. The frozen original evaluation W_p=sum_{k=0}^{p-1}(6k+1)gamma_k 216^(-k) has a different kernel and cutoff from E2.

## 4. Executed arithmetic and next discriminating action

Paired stdlib Python integer-only script was executed on **all 80 primes 7<=p<=997, p==1 mod6**, of which **45** lie in frozen p==13,19 mod24. For every p: checks E1 weighted and unweighted, E3 valuations at every interior k, E4, and the m=1 external E2 specialization, all modulo p^4. Independent direct triple Cauchy coefficient checks for p=13,19,373. Zero failures. Examples of *new* independent signed edge carriers, NOT the original J: at p19 (M/p^3,U/p^3)=(6,11) mod19; p373 (252,21) mod373. No floating-point steps.

Consume, do not re-credit, previous signed original Green observer J_p=sum h_t P_t (commit 8b4c34383377166ba1cba395bad631b2ad6abbd3), the existing full-216 p-unit residual and Clausen source. Next unit: seek a **proved** source/scale preserving finite adjoint kernel mapping original weighted *evaluation* W_p to a mixed-CM *coefficient* observer. The k=0,1 failed unit-scalar transfer is the minimum diagnostic; preserve low p^2 branch, both p^3 bands and original signed J_19=6, J_373=98. Actual mother goal is still Delta_p-R_p==0 (mod p), equivalently W_p==p (mod p^3), for p==13,19 mod24. Nothing here claims that final uniform proof.

## 5. Native Source and original benchmark separation

Original fixed p373 same-class divided-power H0/B0 [X]U mod 139129, rank, semilinear Frobenius direction/eta, original odd Hesse/Green, kappa and independent replica remain NOT_EXECUTED / PENDING_OWNER at https://github.com/awdawmip/enterprise-math/issues/1559 . No portable scalar or cubic coefficient check replaces that experiment. The original Source request onhour11-20261106-1400-exact-research-lane-continuation was WAITING_RESOURCE / EVENT_COLLECTION_IO on this run. New *read-only* continuation request onhour11-20261106-1600-read-exact-research was QUEUED/REVALIDATING at last receipt. Neither is to be reissued. Own Researcher session/CLAIM/run/Source Result absent; three old staging items separate. Previously confirmed Site checkpoint revision 22; later r23 was rejected BEFORE operation submission with BACKEND_IDENTITY_OR_VERSION_MISMATCH. This immutable GitHub report/checker/continuation is author-side preservation, not admission or a substitute native claim.
