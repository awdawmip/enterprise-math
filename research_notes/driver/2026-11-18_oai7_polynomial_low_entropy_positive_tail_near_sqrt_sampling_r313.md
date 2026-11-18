# OAI7 r313 — Low-entropy polynomial shared schedules: positive-tail sampling arbitrarily close to the square-root exponent

Date: 2026-11-18. Mathematical author of this increment: EM-DVR-DEBB5E (source-exposed Driver derivation). Preserve the earlier OAI7 scientific authorship of EM-EMF6D046-5A2844 and the separate Driver r307–r312 increments. This is an external finite cyclic/group-theoretic construction, not a Native Result or a typed Gaussian-prime/X6 path realization.

## Problem and exact provenance

The existing r310/r311 construction gives a **deterministic, every-K, q=0** list certificate with n=O(p^(3/4) log p), one p-valued random seed, and s=4097 signed base indices. The distinct-offset lower bound r312 concerns this almost-sure zero-tail class. Here we allow the **positive worst-set tail budget already authorized in r307**, and trade a fixed number of additional p-valued seed coefficients and signed base indices for shorter sampling. No change is made to r307 or r311.

Pinned mathematical inputs:
- r307 integrated-tail transfer, Git baaaabaacaf8543f62a45a00cdfcf03e95389075, research_notes/driver/2026-11-18_oai7_integrated_list_tail_transfer_r307.md.
- r310 single-seed starting-deficit construction, Git 0e14b422d86160a4525f0dad734d96a6aabf3441.
- r311 distinct-offset zero-tail construction, Git 8720c3abc815c45295a922a7dc9e10273cfed1ef.
- r312 exact distinct-offset positive-threshold obstruction, Git 34ac9052d5acd8cadb0ea75bf30d4fe07e346e70.

Set tau=1/4, delta=1/64, beta=beta'=1/2, eta=1/2, b=tau+delta=17/64, T=p and u=ceil(sqrt(p)). The r307 xi=0 integrated-tail budget is
\[
 Q=\eta(\delta/(\tau+\delta)-\delta/2)
  =\frac12\left(\frac1{17}-\frac1{128}\right)
  =\frac{111}{4352}\approx0.0255055147.
\]

## General theorem (even-wise independent shared offsets)

Fix an integer m>=2. Let
\[
 C_m=\sum_{j=1}^{m}\frac{j^{2m}}{j!},\qquad
 A_m=\max\left\{1,\left(\frac{2C_m}{(1-b)^{2m}Q}\right)^{1/m}\right\}.
\]
For every sufficiently large prime p (with the threshold depending only on m), set
\[
 n=\left\lceil A_m p^{1/2+1/(4m)}\right\rceil,\quad
 k=s=8192m+1,\quad G=\mathbb F_p,\quad \Lambda=\mathbb Z^k.
\]
Choose 2m independent uniform coefficients U_0,...,U_(2m-1) in G, and put
\[
 P(z)=\sum_{a=0}^{2m-1}U_a z^a,\qquad
 h_\ell=([P(\ell)]_p,\ldots,[P(\ell)]_p)\in\mathbb Z^k
 \quad(0\le\ell<n),
\]
where [.]_p is the standard integer representative. Let H=(h_0,...,h_(n-1)).
Fix any B subset G of size u; independently sample Y_j uniformly on G\B and use integer representatives, with Y=(Y_1,...,Y_k), A=Y, and Z=Y+h_0.

For all sufficiently large p the following assertions hold:

1. n<p and n>=2m. Every Y+h_\ell has the **same full integer-lattice distribution** as Z; each terminal signed residue is uniform, whereas each initial signed residue has u missing atoms and fails (tau,1/2)-coverage.
2. H is fully determined by 2m p-valued coefficients, and the first 2m offsets recover them by Vandermonde inversion. Hence its exact Shannon entropy is H(H)=2m log p.
3. For every signed coordinate c and every **deterministic** u-set K subset G, the worst-set small-list tail q_c from r307 is at most Q/2. In particular R_0<=Q/2<Q, so r307's integrated-tail criterion is satisfied with xi=0. All of r307's shared-entropy and logarithmic prerequisites are satisfied.
4. Consequently the sampling length is O_m(p^(1/2+1/(4m))) using only O_m(log p) shared random entropy. For every fixed epsilon>0, choosing an integer m>=max(2,ceil(1/(4epsilon))) gives a family with n=O_epsilon(p^(1/2+epsilon)) and an index budget k=s finite independently of p.

The offsets are jointly correlated and are not claimed pairwise distinct in every realization. The theorem concerns the positive-tail route, whereas r311 is a deterministic q=0 route with distinct offsets.

## Proof: bounded central moments from polynomial evaluation

Fix K and a residue x. Let rho=u/p and
\[
 I_\ell=1_{\{x+P(\ell)\in K\}},\quad X=\sum_{\ell=0}^{n-1}I_\ell,\quad \mu=n\rho.
\]
Any <=2m evaluations P(\ell) at distinct indices are jointly independent uniform G-valued random variables: the associated truncated Vandermonde evaluation map has full row rank over F_p because n<p. Therefore the indicators I_\ell are 2m-wise independent Bernoulli(rho), even though the entire n-vector has only 2m log p entropy.

Set V_\ell=I_\ell-rho, so E V_\ell=0, |V_\ell|<=1, and E|V_\ell|^a<=E V_\ell^2<=rho for every integer a>=2. Expanding the 2m-th central moment, every product involving an index occurring exactly once has zero expectation by 2m-wise independence. A surviving term has j<=m distinct indices, each repeated at least twice. Bounding the number of index choices by binom(n,j), assignments by j^(2m), and the absolute product moment by rho^j gives, whenever mu>=1,
\[
 E(X-\mu)^{2m}
 \le\sum_{j=1}^{m}\binom nj j^{2m}\rho^j
 \le\sum_{j=1}^{m}\frac{j^{2m}}{j!}\mu^j
 \le C_m\mu^m.
\]
Markov applied to |X-mu|^(2m) now yields
\[
 \Pr(X\le b\mu)\le
 \frac{C_m}{(1-b)^{2m}\mu^m}.
\]
For each fixed K and x this estimate is uniform. Summing over x gives
\[
 E_H|L_{c,K}(H)|
 \le \frac{p C_m}{(1-b)^{2m}\mu^m}.
\]
The signed minus-coordinate uses -P(\ell), still 2m-wise independent and uniform. Therefore Markov applied to |L| and the r307 threshold p^(3/4) gives
\[
 q_c\le \frac{C_m p^{1/4}}{(1-b)^{2m}\mu^m}.
\]
As u>=sqrt(p) and n>=A_m p^(1/2+1/(4m)), we have mu>=A_m p^(1/(4m)), and hence
\[
 \boxed{q_c\le C_m/((1-b)^{2m}A_m^m)\le Q/2.}
\]
This is a bound on the probability of a large list for each K fixed *before the coefficients are sampled*. It does not interchange the maximum over K with expectation over H.

Every P(\ell) is uniform in G because U_0 is uniform independent of the other coefficients. Thus each h_\ell is a uniform integer diagonal shift independently of Y and all Y+h_\ell have exactly equal full-lattice laws. As in r310, the u missing residues of every signed initial Y_j show failure of the specified initial coverage, while independent addition of P(0) makes each terminal signed residue uniform.

Entropy of a signed-index subset S with s distinct base indices is s log(p-u), giving epsilon=-log(1-u/p)/log p>0. The shift entropy is exactly 2m log p and kappa=2m/s. As
\[
 1/4096-\kappa
  =1/4096-\frac{2m}{8192m+1}
  =\frac{1}{4096(8192m+1)}>0,
\]
and epsilon tends to zero, epsilon+kappa<1/4096 for all sufficiently large p. The r307 logarithmic condition also holds eventually. Since 1/2+1/(4m)<1 for m>=2, n<p eventually. This completes the theorem.

## Explicit four-wise construction with numerical constants

Take m=2, p any prime >=2^70, s=k=16385, and n=ceil(32 p^(5/8)). Use the cubic P(z)=U_0+U_1z+U_2z^2+U_3z^3. Then H(H)=4log p, and mu=nu/p >=32 p^(1/8).

For 4-wise independent Bernoulli indicators, the exact fourth centered moment equals that of Bin(n,rho):
\[
 E(X-\mu)^4=3v^2+v(1-6\rho(1-\rho))
 \le3\mu^2+\mu,\quad v=\mu(1-\rho).
\]
Consequently
\[
 q_c\le \frac{p^{1/4}}{(1-b)^4}
           \left(\frac3{\mu^2}+\frac1{\mu^3}\right)
 \le\frac{3+1/(32p^{1/8})}{(47/64)^4\,32^2}
 <0.010074<Q.
\]
For p>=2^70, epsilon<=4/(sqrt(p)log p)<=2.4e-12, while the available entropy slack 1/4096-4/16385 is greater than 1.49e-8. Also n<p. Thus all r307 hypotheses hold for this explicit parameter choice, yielding a **p^(5/8)**-scale low-information fully correlated witness with a *positive but certified* worst-set tail.

For general m, the large-p qualifier is essential: A_m grows with m and the finite-field distinct-evaluation and entropy-slack conditions must actually hold.

## What this settles and what remains

This proves that positive-tail r307 coverage transfer admits sample exponents arbitrarily close to 1/2 with finitely many p-valued random coefficients and a larger, fixed-in-p signed-index budget. The r312 square-root-times-logarithm obstruction is specific to *zero-tail distinct-offset* certificates, so the two results coexist.

Open questions: achieve n=O(sqrt(p) polylog p) at a bounded information cost and suitable index budget; preserve pairwise distinctness for every polynomial realization while retaining the requisite moments; and identify a typed native Gaussian-prime/X6 path carrier with the original signed/ordered provenance. No formal Native Result, Task closure or P000/Foundation admission is claimed. Authorship is source-exposed Driver derivation, not an independent review of the original researcher.


## Independent finite arithmetic sanity check of the fourth-moment identity

At p=7, n=6, K={0,1}, x=0, enumerate **all 7^4=2401** cubic coefficient tuples (U_0,U_1,U_2,U_3) and count hits among P(0),...,P(5). The exact hit-count frequencies for X=0,1,2,3,4,5,6 are
\[
 (313,792,720,440,120,12,4).
\]
Their sum is 2401; the computed fourth central moment is exactly 10140/2401, matching the binomial fourth-moment expression with rho=2/7 and mu=12/7. This checks the limited-independence moment computation on one fully enumerated finite example. It does not attempt the p>=2^70 quantitative transfer conditions; those are established analytically above.
