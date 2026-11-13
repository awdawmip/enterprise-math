# PREFIX-756-R6 — Centered killing preserves symmetric Bernstein unimodality under the Pascal bridge

Date: 2026-11-13 (Asia/Shanghai). Parent: PREFIX-675. Predecessors: PREFIX-754 and PREFIX-755.
Frozen scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Scope: finite frozen BRC stopped-survivor count and an abstract symmetric, centered killed-Bernoulli family. This is an external auxiliary probability model, not native X6 geometry or an asserted native BRC dynamics transfer.
Evidence: AUTHOR_EXACT_INTEGER_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.

## Main result: a structural theorem beyond the specific 189-row count

**Theorem 756.1 (centered killed-Pascal preservation, all finite orders).**
Let w_n(k) in {0,1}, 0<=k<=n, be any symmetric centered mask: for every n, either its accepted set is empty or it is an integer interval
    {k:w_n(k)=1}={L_n,L_n+1,...,n-L_n}
for some 0<=L_n<=n/2. Define a[0,0]=1 and the killed Pascal recurrence
    a[n,k]=w_n(k)*(a[n-1,k]+a[n-1,k-1])
with out-of-range counts zero, for arbitrary finite n>=1. Define normalized Bernstein coefficients
    b[n,k]=a[n,k]/binom(n,k).
Then, for every n, b[n,k]=b[n,n-k]>=0, and
    b[n,k+1]>=b[n,k] for 0<=k<floor(n/2).
Consequently, the polynomial survival function
    S_n(p)=sum_k a[n,k] p^k (1-p)^(n-k)
is nondecreasing on the entire real interval p in [0,1/2], without any grid approximation.

**Proof.**
The Pascal/binomial identities give a normalized bridge before the mask:
    \widetilde b[n,k] = ((n-k)/n)*b[n-1,k] + (k/n)*b[n-1,k-1].
It is nonnegative and symmetric if b[n-1] is. For 0<=k<floor(n/2), its adjacent difference is
    n*(\widetilde b[n,k+1]-\widetilde b[n,k])
      =(n-k-1)*(b[n-1,k+1]-b[n-1,k])
       +k*(b[n-1,k]-b[n-1,k-1]).
Each coefficient is nonnegative. The two differences are nonnegative by the previous level's symmetry and central unimodality. For the even-n final comparison, k=n/2-1, the first difference vanishes because n-1 is odd and the two center coefficients are symmetric equals. Hence \widetilde b is symmetric and centrally nondecreasing.

Multiplication by w_n retains symmetry and nonnegativity. It also retains central nondecrease: before the left acceptance edge both masked values are zero; crossing that edge changes 0 to a nonnegative number; within the accepted center, the inequality is inherited. Induction from b[0,0]=1 proves the coefficient assertions.

For the last assertion expand b[n,k] by its central differences delta_j=b[n,j]-b[n,j-1]>=0, j=1,...,floor(n/2):
    b[n,k]=b[n,0]+sum_j delta_j*1{j<=k<=n-j}.
For K~Bin(n,p), E[b[n,K]]=S_n(p). Each central-binomial probability H_nj(p)=Pr(j<=K<=n-j) has derivative
    H'_nj(p)=n*binom(n-1,j-1)
       *[p^(j-1)(1-p)^(n-j)-p^(n-j)(1-p)^(j-1)] >= 0
for every p in [0,1/2], as n-j>=j and 1-p>=p. Thus S_n is nondecreasing. QED.

This theorem is exact for **every** finite n and for **any** sequence of symmetric centered masks, with no assumption on their interval widths varying monotonically with n.

## The frozen width predicate satisfies the hypothesis

Use the exact frozen width test:
    W=2^18,
    inside(n,k,x)=[40(n+1)binom(n,k)x^k(W-x)^(n-k)>W^n],
    wide(n,k) obtained from the published integer bisection and strict W/4 width decisions.
The existing published PREFIX-754 independent checker fixes these operations and the killed recurrence. In the exhaustive independent author run, the accepted k at every n=1,...,188 form one full symmetric centered integer interval, and at n=189 the mask is empty.

The accompanying checker reuses *the same published PREFIX-755 implementation* and verifies all 18,144 possible mask memberships k=0,...,n for n=1,...,189. For each nonempty row it checks exact interval equality, including no holes, symmetry and the two endpoints. It also verifies:
    188 nonempty mask rows (n=1,...,188),
    one empty row (n=189),
    left edge L_25=1 and L_188=89.
All checks use exact integer arithmetic. It returns ALL_CHECKS_PASS PREFIX756-R6.

**Corollary 756.2 (Gamma(max) endpoint monotonicity follows structurally).**
For this frozen model, the centered-mask theorem establishes S_n(p) nondecreasing for all p in [0,1/2] and all n<=188. Under the independent conditional Gamma(k,1) clock model of PREFIX-712, the single-clock survival H_p(t)=exp(-t)*sum_n S_n(p)t^n/n! and the independent maximum survival H_p+H_z-H_pH_z are coordinatewise nondecreasing. Consequently the mean and the second raw moment of Y(p,z) are nondecreasing. This recovers the analytic order premise used in the continuous Gamma endpoint certificates without even needing to enumerate the 8,836 normalized adjacent-coefficient inequalities from PREFIX-755.

## Reproducibility and next mathematical question

The self-contained PREFIX-755 exact recursion is already published in this directory. Run:
    python PREFIX756_R6_CENTERED_KILLED_PASCAL_CHECK.py
in the same directory as PREFIX755_R6_BERNSTEIN_MONOTONE_GAMMA_CHECK.py. The first script invokes the predecessor checker and exhaustively tests the mask. The local author process returned ALL_CHECKS_PASS. See PREFIX756_R6_CENTERED_KILLED_PASCAL_RESULTS.json for finite-domain check counts.

This establishes an abstract all-orders killed-Pascal theorem plus an exact 189-row frozen-model hypothesis verification. It does not introduce additional excluded geometric cells or change the current author-only historical support 140662/147456. The remaining scientific direction is to check an actual uncovered fine grid cell using a new comparator after normalizing historical cell coordinates, and independently examine the numerical IEEE/BLAS bound premises of PREFIX-754. Shared research CLAIMs were not mutated.
