# S23/AV: exact minimax asymptotic coefficient from an observer-adaptive arcsine decoder

Date 2026-11-07. Author-side mathematical proof; independent review pending. Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor: 1232b4ecc1a309dae00231e6e9e4aaa94e0c22ab. This is an auxiliary statistical experiment, not a six-source/ten-label mother-model transfer.

## Model and theorem

For real a,c in [1/2,7/8], let z=(1-a)c, b=(1-a)(1-c). Full ordered trial output has law P=(a,z,b) on labels (1,3,4); binary compressed observation B=(z,1-z) on (Y,N), where Y denotes full label 3. Across n trials the *same* unknown (a,c) is shared, and trials are conditionally iid. A stochastic decoder L from {Y,N}^n to the entire ordered {1,3,4}^n is independent of parameters. Define delta_n=inf_L sup_(a,c) TV(P_(a,c)^⊗n,B_z^⊗n L).

**Theorem.**

lim_(n→infinity) sqrt(n/log n) (1-delta_n)
= C_* = 2/[sqrt(3) (asin sqrt(20/21) - asin sqrt(2/3))]
= 2.9196578513965...

The inverse sine is real, in radians, and log is natural. This *completes the leading asymptotic minimax constant* of this auxiliary full-ordered-output experiment. It is not a formula for every finite n.

## Lawful hidden parameter fibers

Write u=1-a, s=1-z, p=a/s. The lawful z interval is [1/16,7/16]. At fixed z, exactly

u_min(z)=max(1/8,8z/7), u_max(z)=min(1/2,2z),
p_-(z)=(1-u_max(z))/(1-z), p_+(z)=(1-u_min(z))/(1-z).

Every p in this interval arises from a lawful pair (a,c), by setting a=s p and c=z/(1-a). The endpoints p_± are globally 2-Lipschitz in z; all lawful p lie in [2/3,56/57]. Set v(p)=p(1-p), v_min=56/3249, h(z)=p_+-p_-,

g(p)=1/sqrt(v(p)),
I(z)=integral_[p_-]^[p_+] g(t) dt
    =2[asin sqrt(p_+) - asin sqrt(p_-)],
C(z)=2/[sqrt(1-z) I(z)] (interior z).

The exact observer fiber is the retained Y-law z together with the unrecovered range p; retaining the observed ordered Y-mask preserves the relevant future observations, and the hidden-fiber variation is not silently treated as independent per trial.

## Constructive adaptive arcsine-count decoder

Let R be the observed number of Ys, m=n-R, and zhat=clamp(R/n,[1/16,7/16]). If m=0, output all label 3. Otherwise set

W_n=ceil(4 sqrt(n log(n+2)))+1,
A=max(0,floor(m p_-(zhat))-W_n),
D=min(m,ceil(m p_+(zhat))+W_n).

Define g_cl(x)=1/sqrt(xbar(1-xbar)), xbar=clamp(x,[1/2,99/100]). This bounded, Lipschitz positive extension equals g on all lawful p. Choose K∈[A,D] with probability q_(n,R)(K)=g_cl(K/m)/H_(n,R), where H_(n,R)=sum_(j=A)^D g_cl(j/m). Preserve each input Y position as output 3. Of the m N positions choose K uniformly as label 1, and label the remainder 4. This is one normalized parameter-independent decoder of complete ordered words. Conditional on the Y-mask the full source hidden count is Bin(m,p), and arrangements given K are uniform for both source and decoder. Therefore its *full ordered total-variation overlap* is EXACTLY

O_n(a,c)=1-TV(P^⊗n,B_z^⊗n L_n)
=sum_(r=0)^n Bin(n,r;z) sum_(k=0)^(n-r) min{Bin(n-r,k;p),q_(n,r)(k)}.    (1)

No iid assumption is made for the decoder-generated hidden positions.

Take t_n=sqrt[(3/2) log(n+2)/n]. On E_n={|R/n-z|≤t_n}, Hoeffding gives P(E_n^c)≤2(n+2)^(-3). All lawful z have 1-z≥9/16, so m≥n/2 on E_n for large n. Since p_± are 2-Lipschitz and |zhat-z|≤t_n, the true mp is at least

W_n-2m t_n-O(1) ≥(4-sqrt(6)+o(1))sqrt(n log n)

from either un-clipped strip endpoint. Thus every central integer with

|k-mp|≤(1-eps) sqrt[m v(p) log m]                              (2)

is supported, uniformly in lawful parameters for any fixed eps∈(0,1), since v≤1/4. The clipped weights approximate their integral and the padding contributes O(W_n), yielding uniformly on E_n

H_(n,R)=m I(z)+O(sqrt(n log n)).                                 (3)

To handle all real parameter pairs, split at h0=1/1000.

If h(z)≥h0, equation (3) has o(1) relative error; for central k from (2), q(k)=(1+o(1))g(p)/(m I(z))=O(1/m), uniformly. Uniform Stirling's formula for compact p∈[2/3,56/57] gives

Bin(m,k;p)≥m^[-1+eps-eps^2/2+o(1)] >> 1/m.

So the central terms in (1) equal q(k). Counting them gives

sum_k min{Bin(m,k;p),q(k)}
≥[2(1-eps)/I(z)+o(1)]sqrt(log m/m),

hence coefficient at least (1-eps) C(z) against sqrt(log n/n), uniformly on E_n.

If h(z)<h0, use g_min=2, g_max<11 and (3) to obtain for sufficiently large n

H_(n,R)≤g_max*m*h0+O(sqrt(n log n))≤2g_max*m*h0,

so every supported q(k)≥g_min/(2g_max m h0). Put alpha=sqrt(v_min)/2. The central interval |k-mp|≤alpha sqrt(m log m) lies in the strip, and a uniform Stirling lower estimate gives Bin(m,k;p)≥m^[-5/8+o(1)], eventually larger than g_min/(2g_max m h0). Counting its integers gives

sum_k min{Bin(m,k;p),q(k)}
≥ [alpha*g_min/(g_max*h0)+o(1)]sqrt(log m/m).

Since m/n≤s_max+o(1), s_max=15/16, the resulting coefficient against sqrt(log n/n) is at least

alpha*g_min/[g_max*h0*sqrt(s_max)] > 12 > C_*.

This estimate is uniform even for fibers with h(z)→0. Combining both cases and P(E_n^c)=O(n^-3), then eps→0, proves

liminf sqrt(n/log n)*inf_(a,c) O_n(a,c) ≥ inf_(interior z) C(z). (4)

## Exact maximizer of the arcsine fiber measure

Let J(z)=sqrt(1-z)I(z). Substituting u=zt gives

J(z)=sqrt[z(1-z)] integral_[u_min(z)/z]^[u_max(z)/z]
      dt / sqrt[(1-zt)(t-1)].                                   (5)

For z in (1/16,7/64] the t-domain is [1/(8z),2], which expands as z increases. For z in [7/64,1/4] it is [8/7,2], constant. Through both ranges, sqrt[z(1-z)] increases (z<1/2), and the integrand increases pointwise. Thus J strictly increases up to 1/4.

For z∈[1/4,7/16), p_-=1/[2(1-z)] increases and p_+=(1-8z/7)/(1-z) decreases; the p-domain of the positive integral I(z) strictly contracts, and sqrt(1-z) decreases. Hence J strictly decreases. The maximum is uniquely at z=1/4, where p_-=2/3, p_+=20/21. Therefore inf_z C(z)=C_*. Equation (4) proves the constructive bound liminf sqrt(n/log n)(1-delta_n)≥C_*.

## Matching universal-decoder upper bound via a fixed fiber

Fix z0=1/4. Vary p over [2/3,20/21]; all points are lawful and produce the SAME compressed input distribution B_z0^⊗n. Hence every parameter-independent decoder output Q_n is p-independent on this fiber, even if it moves Y positions, discards their order or uses a stochastic non-coordinatewise rule.

Choose the arcsine prior dnu(p)=g(p)dp/I(z0). Coarsen target/output ordered words to histogram (r,k), counting 3 and 1. Since coarsening cannot decrease overlap, the full overlap is no larger than histogram overlap. Target histogram probabilities are pi_r beta_(m,p)(k), with pi_r=Bin(n,r;z0), m=n-r, beta_(m,p)=Bin(m,p). Let q_(r,k) be the arbitrary decoder's histogram distribution, independent of p and summing to 1.

Fix eps>0. For m≥2 set d_m=sqrt(log m/m), and

M_(m,k)={p in [p_-,p_+]: |k-mp|≤(1+eps)sqrt[m v(p) log m]}.

In arcsine coordinate theta(p)=integral_(p_-)^p g(t)dt, the diameter of M_(m,k) is at most [2(1+eps)+o(1)]d_m uniformly in k. To see this, all p in the window are within O(d_m) of k/m; v_min>0 and the mean-value theorem make g(p)/g(p')=1+O(d_m) across the window. Therefore

nu(M_(m,k)) ≤ [2(1+eps)/I(z0)+o(1)]d_m.                    (6)

Uniform Bernstein/Chernoff concentration for compact p gives

sup_p sum_(k:p notin M_(m,k)) beta_(m,p)(k)
≤2 exp(-[(1+eps)^2/2+o(1)] log m)=o(d_m).                  (7)

In the prior integral of min{pi_r beta_(m,p)(k),q_(r,k)}, use q_(r,k) inside M and pi_r beta outside. Restrict first to typical r with |r/n-z0|≤n^(-1/3); then m/n→3/4 uniformly. Sum the central term using (6) and sum_(r,k)q_(r,k)≤1. Sum the outside term using (7) and sum_r pi_r≤1. Atypical r contribute at most sum_atyp pi_r≤2 exp(-2n^(1/3)) by Hoeffding, independent of Q_n. Thus

integral [1-TV(P_(z0,p)^⊗n,Q_n)]dnu(p)
≤[2(1+eps)/(sqrt(3/4) I(z0))+o(1)]sqrt(log n/n).

The infimum over lawful p is ≤ this prior average for *every* decoder Q_n. Let eps↓0 to obtain

limsup sqrt(n/log n)(1-delta_n)≤2/[sqrt(3/4)I(z0)]=C_*.    (8)

The constructive (4) and universal upper (8) prove the theorem.

## Evidence and boundaries

VERIFY.py executes Python 3 standard-library Fraction checks of exact ordered-word vs histogram overlap at n=2,3,4 for three lawful rational pairs and rational comparison kernels, rational z=1/4 endpoints, a dense coefficient grid, and numerical checks of the actual arcsine decoder at n=40,400,20000. RUN_EVIDENCE.txt is actual executed stdout. The all-real n→infinity theorem is analytic, not an inference from those finite tests. The proof uses uniform Stirling/entropy local estimates, binomial Hoeffding/Bernstein bounds and total variation data processing.

BRC result: REUSE_APPLIED to exact retained Y-mask and hidden-p observer fiber; the new arcsine density is a variance-equalized repair coordinate for compression, not a theorem about native spatial X6. The six-source ten-label S23 mother bridge and finite-n exact minimax error remain separate questions. The connected GitHub actor is awdawmip with project push access; native em_status returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Formal CLAIM, active Owner, Research-Activity-ID, Result admission and independent mathematical review are unconfirmed.

NEXT: develop finite-n upper/lower envelopes and second-order asymptotics; separately build a lawful source/time-typed mother-observer bridge and test its exact encoder/decoder quantifiers.
