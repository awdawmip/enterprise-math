# OAI7 r329 — Dual Johnson-slice concentration and the exact fixed-offset asymptotic threshold

Date: 2026-11-18. Evidence level: new author-side mathematical derivation, based on pinned r328; not an independent Native Result review, Task completion, CLAIM, Source/Activity admission, native X6/Port/Link implementation, or a low-entropy improvement. Original OAI7 researcher and r307/r321/r325–r328 authors retain their actual mathematical contributions.

## Theorem (mean-driven phase separation for distinct shifts)

Fix b=17/64 and write J=1-b+b log b, c_*=(4J)^{-1}. Let p run through primes, u=ceil(sqrt(p)), L=log p, and d be any fixed real number. Set

$$n=n_p=\left\lceil c_*\sqrt p\,[L-2\log L+d]\right\rceil,\quad \mu=nu/p,\quad h=\lfloor b\mu\rfloor.$$

For a deterministic u-element test set K in F_p and a *pairwise-distinct* n-shift schedule W, define

$$V_W(K)=\#\{x\in\mathbb F_p: |(x+W)\cap K|\le h\}.$$

Let

$$P_p=\Pr\{\operatorname{Hypergeom}(p,n,u)\le h\},\quad
M_p=pP_p,\quad
\theta_p=\{b\mu\},\quad
A_b=\frac{1}{(1-b)\sqrt{2\pi b c_*}},\quad
\Lambda_p=A_b\,b^{\theta_p}e^{-d/4}.$$

All logs are natural. Then, uniformly over all deterministic distinct W, and separately uniformly over all deterministic u-sets K,

$$
\mathbb E_{K\ {\rm uniform}} V_W(K)=M_p
=\mathbb E_{W\ {\rm uniform\ distinct}}V_W(K),\qquad
\frac{M_p}{p^{3/4}}=\Lambda_p(1+o(1)).
\tag{R329.1}
$$

The two variance controls are, with constants depending only on b and fixed d,

$$
\sup_W \operatorname{Var}_{K}V_W(K)\le C u n^2 P_h,\qquad
\sup_K\operatorname{Var}_{W}V_W(K)\le C n u^2 P_h,
\quad
P_h=\Pr\{\operatorname{Hypergeom}(p,n,u)=h\}.
\tag{R329.2}
$$

Consequently both V_W(K)/M_p concentrate at 1 in their respective randomizations: the upper bounds on their relative variances are O(p^{-1/4}L^2) and O(p^{-1/4}L), respectively.

Define the worst deterministic-test-set failure probability of a random shift law \mathcal W, supported on distinct sequences, by

$$q_p(\mathcal W)=\max_{|K|=u}\Pr_{W\sim\mathcal W}\{V_W(K)>p^{3/4}\}.$$

The *fixed-offset phase criterion* is:

1. If liminf_{p\to\infty}\Lambda_p>1, then q_p(\mathcal W_p)\to1 for **every** sequence of arbitrary (including correlated/adaptive) distinct-shift laws \mathcal W_p.
2. If limsup_{p\to\infty}\Lambda_p<1, then for the **uniformly random ordered distinct-shift law**, q_p(\mathcal W_p)\to0, uniformly over all deterministic K.

In particular, since b\le b^{\theta_p}\le1,

$$
d<4\log(A_bb)=-4.24295535245\ldots
\ \Longrightarrow\ q_p(\mathcal W_p)\to1
\quad\text{for every distinct law,}
\tag{R329.3}
$$

whereas

$$
d>4\log A_b=1.05972360476\ldots
\ \Longrightarrow\ q_p(\mathcal W_p)\to0
\quad\text{for the uniform distinct law.}
\tag{R329.4}
$$

The exact necessary/sufficient criterion off the boundary is \Lambda_p, rather than either coarse numerical bound. The fractional part \theta_p retains the lattice oscillation at the third-order fixed-d scale; no universal unqualified single d-threshold is asserted. This theorem addresses arbitrary-entropy distinct-shift laws. The uniform ordered law has entropy H(W)=log (p)_n, of order n log p, and does **not** supply the O((log p)^2) information-cost upper bound of r327.

## Proof A: exact common hypergeometric mean and sharp lattice prefactor

For fixed distinct W and uniform u-subset K, |(x+W)\cap K| has the hypergeometric law Hypergeom(p,n,u), independent of W and x. Conversely, for fixed K and uniform n-subset W, the same law holds, independent of K and x. Summing indicators over x gives the first mean identity.

The exact falling-factorial comparison from r328 Proof 1, uniform for j=h+O(1), yields

$$
\Pr(X=j)=(1+O(L^3/\sqrt p))e^{-\mu}\mu^j/j!,
\quad X\sim\operatorname{Hypergeom}(p,n,u).
$$

With h=b\mu-\theta_p, Stirling expansion *retaining the fractional part* gives

$$
P_h=(1+o(1))\frac{b^{\theta_p}}{\sqrt{2\pi b\mu}}e^{-J\mu}.
$$

For fixed nonnegative integer r, the ratio \Pr(X=h-r)/P_h tends to b^r, uniformly with respect to \theta_p in [0,1). Exact hypergeometric successive ratios admit a uniform geometric upper bound with ratio <1 (choose any fixed number strictly between b and 1), hence summing the lower tail,

$$
P_p=(1+o(1))\frac{P_h}{1-b}.
\tag{R329.5}
$$

As \mu=c_*[L-2\log L+d]+o(1), the identity Jc_*=1/4 gives

$$
e^{-J\mu}=p^{-1/4}L^{1/2}e^{-d/4}(1+o(1)),
\quad \sqrt\mu=\sqrt{c_*L}(1+o(1)).
$$

Together these prove (R329.1), uniformly in the oscillating \theta_p. In particular P_h\asymp_{b,d}p^{-1/4} and M_p\asymp_{b,d}p^{3/4}.

## Proof B: two orientations of the Johnson-slice spectral gap

On the uniform a-element slice of the p-point set, the exact one-swap Poincare inequality established in r328 Proof 2 is

$$
\operatorname{Var}F\le\frac{a(p-a)}{2p}
 \mathbb E_{S,\alpha\in S,\delta\notin S}
 [F(S-\{\alpha\}+\{\delta\})-F(S)]^2.
\tag{R329.6}
$$

For the first orientation, fix distinct W, randomize K on the u-slice, and apply the r328 rare-boundary calculation. Each swap affects at most 2n starting residues; conditional on the removed/added elements, a boundary hit count follows a shifted Hypergeom(p-2,u-1,n-e) law with e in {0,1,2}, whose h±1 point probabilities are O_b(P_h). Thus the squared-difference expectation is at most C n^2 P_h and the u-slice spectral gap gives Var_K V <=C u n^2P_h.

For the **new dual orientation**, fix K, randomize W on the n-slice, and swap a in W with d_0 outside W. A starting residue x is affected only if x+a or x+d_0 belongs to K, so at most 2u starts are affected. Conditional on the selected a,d_0, the other n-1 shifts are a uniform subset of the p-2 remaining field elements. For each affected x the count is an indicator for the removed member plus a Hypergeom(p-2,n-1,u-e) random variable, where e in {0,1,2}. The relevant threshold-boundary masses at h±1 are O_b(P_h), uniformly over K,x,a,d_0, by the same r328 asymptotic point-mass comparison.

If B is the number of affected x whose threshold indicator can flip, then |Delta V|<=B<=2u and E B<=C u P_h. Hence E(Delta V)^2<=2u E B<=C u^2P_h. Apply (R329.6) with a=n to obtain Var_W V<=C n u^2P_h. Because u\asymp sqrt p, n\asymp sqrt p L, and P_h\asymp p^{-1/4}, the variance-to-mean-squared estimates in (R329.2) follow.

## Proof C: deterministic-set quantifiers and dual minimax construction

If liminf \Lambda_p>1, choose fixed epsilon>0 so M_p> (1+epsilon)p^{3/4} eventually. The first orientation and Chebyshev show

$$
\sup_{\text{distinct deterministic }W}
\Pr_{K\ {\rm uniform}}\{V_W(K)\le p^{3/4}\}=o(1).
$$

Average over **any** random distinct-shift law \mathcal W and exchange the finite expectations. The maximum over deterministic K of the failure probability is at least its K-average, so q_p(\mathcal W_p)>=1-o(1).

If limsup \Lambda_p<1, choose epsilon>0 so M_p<(1-epsilon)p^{3/4} eventually. The second orientation and Chebyshev imply

$$
\sup_{\text{deterministic }|K|=u}
\Pr_{W\ {\rm uniform\ distinct}}\{V_W(K)>p^{3/4}\}=o(1),
$$

which proves the uniform distinct-law construction. Uniformly permuting the n-set gives an ordered shift schedule with distinct entries, individually uniform marginals, and the same V. Its entropy is log binom(p,n)+log(n!)=log (p)_n. All max_K operations occur *outside* the schedule probability.

## Exact small finite crosscheck and numerical constants

At p=11, u=4, n=5, h=floor((17/64)(20/11))=0, for every distinct W and uniform K, and for every K and uniform distinct W,

$$M_p=11\binom{7}{5}/\binom{11}{5}
=11\binom{6}{4}/\binom{11}{4}=\tfrac12.$$

Enumerating the 330 possible K for W={0,1,2,3,4}, and all 462 distinct W-sets for K={0,1,2,3} and K={0,2,5,8}, independently reproduces mean 1/2; the two W-set populations both have variance 7/12. This is a finite combinatorial check of the two orientations, not asymptotic verification.

For b=17/64, c_*=0.6540325447238404..., A_b=1.3033409133617793..., giving the quoted bracket (R329.3)-(R329.4).

## Provenance and next open boundary

This result reuses r328's sharp point-mass comparison and exact Johnson spectral-gap proof, and supplies the **new n-slice dual variance bound**, fixed-d lattice prefactor, and the minimax converse/achievability separation. Prior sources: r328 GitHub main@961b63fca64881cfbd24894803bdaf24f5d5b570; r327 main@d9deb25a2561cbf7ccbbcca8dd75ee7528a6b356; r326 main@4d94923811a8b47a01f584f337fd5028bd23b40d; first-order necessity r321, source commit 3c411d17ca496dfcfcdb91082643597981f6b9d2.

The threshold **for low-entropy schedules** at fixed d, and the critical window \Lambda_p\to1, remain open. No authenticated Native Result, independent review or Source/Activity linkage is claimed here. The original OAI7 task's external Gaussian-prime and typed Heartbeat-X6 transfer are distinct scientific questions.
