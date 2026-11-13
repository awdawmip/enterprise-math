# R749SMO — Sharp one-Walsh-coordinate minimax loss and horizon amplification

Date: 2026-11-13, Asia/Shanghai.
Continuation: R749SML–R749SMN, especially R749SMN at awdawmip/enterprise-math@5925c109867f0005c704b18e076fb034040e12c9.
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (unchanged).
Status: author-side exact mathematics plus finite rational checks; independent review pending. This is an abstract named signed-history observer, not a native V29/V39 event. Source bits are NOT additional native X6 spatial axes.

## 1. Arbitrary finite public observer: one deleted source relation

Let G=F_2^d, d>=1. For q in G, define chi_q(x)=(-1)^(q dot x). Let K(l|x) be any stochastic observer with finite output alphabet L and full source population G. Write its normalized Walsh coefficients

    k(l,q) = 2^(-d) sum_(x in G) K(l|x) chi_q(x).

For a source prior mu, write m_q(mu)=sum_x mu(x) chi_q(x). Walsh inversion gives the exact full-output prediction

    P_mu(l) = sum_(q in G) k(l,q) m_q(mu),   m_0=1.

Fix one nonzero named mask q. The lossy carrier retains EVERY m_r with r different from 0 and q; it deletes only the one coordinate m_q. This is a specified public observer and horizon, not a declaration that a joint historical relation is universally redundant.

**Theorem A (sharp diameter, optimal minimax decoder).** Define

    S_q(K) = sum_(l in L) |k(l,q)|.

(i) Over all pairs mu,nu of genuine source priors with identical retained moments, the largest total-variation distance TV(K mu,K nu) is exactly S_q(K), and 0<=S_q(K)<=1.

(ii) Over all decoders from the retained moments into valid public output probability laws, the minimum worst-prior TV reconstruction error is exactly S_q(K)/2.

(iii) This deletion is exactly lossless for all priors if and only if S_q(K)=0.

**Proof.** Finite Walsh inversion is a linear isomorphism. If mu and nu agree on all retained moments then their sole possible differing Fourier coordinate is q. Put Delta=m_q(mu)-m_q(nu), |Delta|<=2. Thus (K mu-K nu)(l)=Delta k(l,q), and TV=|Delta| S_q(K)/2 <=S_q(K).

This is sharp: mu_+(x)=2^(-d)(1+chi_q(x)) and mu_-(x)=2^(-d)(1-chi_q(x)) are nonnegative normalized priors, share all retained moments, and have m_q=+1 and -1. Their output TV equals S_q(K). Stochasticity of K implies this value is at most one.

For arbitrary feasible retained moments, define the known partial inverse transform

    g(x)=1 + sum_(r not in {0,q}) m_r chi_r(x).

All compatible priors have the form mu_t(x)=2^(-d)(g(x)+t chi_q(x)). Nonnegativity is EXACTLY the interval of allowed missing moments t in [L,U], with

    L = - min_(x:chi_q(x)=+1) g(x),
    U =   min_(x:chi_q(x)=-1) g(x).

This interval is nonempty for a feasible carrier and has width at most 2. Every output law varies along a line: P_t=P_0+t k(.,q). Choosing the midpoint t=(L+U)/2 supplies a valid output law induced by a genuine midpoint prior. Its worst error on this fiber is (U-L)S_q(K)/4 <=S_q(K)/2. The indistinguishable pair mu_+,mu_- above has output separation S_q(K), so the triangle inequality forces every decoder to incur worst-case error at least S_q(K)/2. Therefore the bound is attained globally and (i)–(iii) follow. QED.

The theorem gives an exact quantitative decision rule for deleting ONE Walsh source relation when every other moment is available. Deleting a set of moments requires a different feasible-prior optimization.

## 2. Exact amplification by repeated publicly observable signed-Port blocks

Choose linearly independent source masks a,b. A two-step observer first queries a with bias alpha in [-1,1], publicly emits sign s, and then on EITHER public branch queries the SAME named source Port b with the SAME bias beta in [-1,1], publicly emitting t. Its complete two-sign output likelihood is

    K((s,t)|x) = [(1+s alpha chi_a(x))(1+t beta chi_b(x))]/4.

Now repeat this entire block n>=1 times with independent fresh channel randomness, leaving the source x fixed and reinitializing the controller. Retain the entire public output of 2n signs. Denote this observer K^(n). Focus on the joint historical source mask q=a XOR b.

For a signed Bernoulli channel of bias lambda, let P_(lambda,u)^(n) be the n-fold sign distribution when the hidden Walsh sign is u=+1 or -1, respectively. Define

    D_n(lambda) = TV(P_(lambda,+)^(n), P_(lambda,-)^(n)).

**Theorem B (exact sharp multi-block prediction loss).** For all n>=1 and all alpha,beta in [-1,1],

    S_(a XOR b)(K^(n)) = D_n(alpha) D_n(beta),

    optimal minimax TV error when deleting ONLY m_(a XOR b)
        = (1/2) D_n(alpha) D_n(beta).

For p=(1+|lambda|)/2 and r=(1-|lambda|)/2, the fully explicit finite formula is

    D_n(lambda) = (1/2) sum_(k=0)^n binom(n,k)
                         |p^k r^(n-k)-r^k p^(n-k)|.

It gives D_1=D_2=|lambda| and D_3=D_4=(3|lambda|-|lambda|^3)/2.

**Proof.** Because the second Port is b and its bias beta is the same for both first-sign branches, the full block's A and B signs are conditionally independent given source parities u=chi_a(x), v=chi_b(x). Across n repeated blocks, the conditional law factors as P_(alpha,u)^(n) tensor P_(beta,v)^(n). The two genuine source priors mu_+,mu_- uniform on the joint cosets uv=+1 and uv=-1 give

    P_+ = (P_a+ tensor P_b+ + P_a- tensor P_b-)/2,
    P_- = (P_a+ tensor P_b- + P_a- tensor P_b+)/2.

Hence P_+-P_- = (P_a+-P_a-) tensor (P_b+-P_b-)/2. The L1 norm of a signed tensor product is multiplicative, so TV(P_+,P_-)=D_n(alpha)D_n(beta). By Theorem A, this output TV is exactly the q-direction sensitivity S_q, and half of it is the minimax deletion error. Grouping n signed outputs by the number of positive signs yields the displayed binomial formula. QED.

**Horizon corollary.** For lambda different from zero, majority-vote identification of the hidden signed source from n conditionally independent observations has error at most exp(-n lambda^2/2) by Hoeffding; thus D_n(lambda) approaches one. Accordingly, when alpha beta is nonzero, S_(a XOR b)(K^(n)) approaches one and optimal deletion error approaches 1/2. If either bias is zero, the joint sensitivity is zero for every n. S_q(K^(n)) is nondecreasing: the shorter experiment is a deterministic public marginal of the longer experiment, and TV contracts under marginalization.

This separates a declared finite-horizon approximation certificate from the distinct infinite-repeat observer. The same named Ports can be queried repeatedly without adding primitive spatial axes, while their mixed relation becomes progressively more important for prediction.

## 3. Exact family and sharp priors

For a=1, b=2, alpha=beta=1/2, one two-step block has rank 4 in the four-source experiment (as in R749SMN). Dropping only the mixed coordinate has one-block sensitivity 1/4 and minimax TV loss 1/8. Exact values are:

| Repeated blocks n | D_n(1/2) | S_(a XOR b) | Optimal TV deletion error |
|---:|---:|---:|---:|
| 1 | 1/2 | 1/4 | 1/8 |
| 2 | 1/2 | 1/4 | 1/8 |
| 3 | 11/16 | 121/256 | 121/512 |
| 4 | 11/16 | 121/256 | 121/512 |
| 5 | 203/256 | 41209/65536 | 41209/131072 |
| 6 | 203/256 | 41209/65536 | 41209/131072 |

The sharp diameter witnesses are the true coset priors mu_+(x)=2^(-d)(1+chi_(a XOR b)(x)) and mu_-(x)=2^(-d)(1-chi_(a XOR b)(x)). All other Walsh moments coincide. If strictly positive priors are required, uniformly mix both witnesses with the full uniform prior; their distance approaches the sharp supremum as the mixing weight tends to zero.

## 4. Executed exact verification

Companion code R749SMO_SINGLE_WALSH_MINIMAX_EXACT_CHECK.py uses the Python standard library fractions.Fraction without floating-point approximations. Actual execution returned PASS:

- 848 exact Walsh moment/TV witness assertions for 176 deterministic, erased and repeated-mask depth-three binary trees with source counts d=2 and d=3.
- 36 repeated-block factorization checks, six boundary/interior signed-bias pairs times n=1,...,6, comparing DIRECT full path likelihood products with the independent binomial formula.
- Probability normalization, 0<=S_q<=1, coset-witness identity and all displayed exact fraction entries.

See R749SMO_SINGLE_WALSH_MINIMAX_RESULTS.json. Finite check coverage is evidence for the code; Theorems A and B hold over their explicitly stated full parameter domains by the preceding algebra.

## 5. Next research

Find exact minimax loss when several specified Walsh relations are jointly removed, using finite feasible-prior polytopes; isolate when the sensitivity sum is sharp. Extend repeated-block analysis to distinct child biases and feedback that changes the next queried Port. Identify actual licensed V29/V39 observer kernels and the true BRC provenance source maps before applying these abstract theorems to native events.

Independent scientific review, true native event correspondence and any formal Task CLAIM/Result remain separate work.
