# S23 conditional AV: exact asymptotic minimax overlap constant through observable fibers

Date: 2026-11-07. AUTHOR_ANALYTIC_PROOF / FINITE_EXACT_REGRESSION_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Prior frontier: Draft PR #1777, research_notes/brc_s23_av_fisher_arcsine_constant_20261106_r1/PROOF.md at b5867e6448585deb06619f30a365df14ad287910.

## Model and new theorem

Take a,c in [1/2,7/8], t=1-a, z=tc, q=t-z, r=q/(1-z). A full three-tag observation (stop1,stop3,stop4) has law P=(1-z-q,z,q); its compressed two-tag observation (other,stop3) has law B=(1-z,z). The same unknown a,c are shared among n conditionally independent repetitions. Write

delta_n = inf_(parameter-independent stochastic K) sup_(legal a,c) TV(P_(a,c)^tensor-n,B_z^tensor-n K).

For finite distributions, overlap Omega(P,Q)=sum_x min(P(x),Q(x))=1-TV(P,Q), so 1-delta_n=sup_K inf_(a,c) Omega(P_(a,c)^n,B_z^n K).

**Theorem:**

lim_(n->infinity) sqrt(n/log n) (1-delta_n)
= C_* := 2/[sqrt(3)(arcsin sqrt(1/3)-arcsin sqrt(1/21))]
= 2.9196578513965343623379765654579...

The limit is for all lawful real parameters and *all* parameter-independent Markov kernels, not just a chosen beta-mixture family. The proof below independently constructs a lower bound and a matching adversarial upper bound.

## Exact feasible fibers

Let z be fixed. The restrictions t=1-a in [1/8,1/2] and c=z/t in [1/2,7/8] imply

z in [1/16,7/16], t_-(z)=max(1/8,8z/7), t_+(z)=min(1/2,2z).

As r=(t-z)/(1-z) increases with t, its *entire* feasible interval is [L(z),U(z)], with

L(z)=(t_-(z)-z)/(1-z), U(z)=(t_+(z)-z)/(1-z).

Explicitly:
- for 1/16 <=z<=7/64: L=(1/8-z)/(1-z), U=z/(1-z);
- for 7/64 <=z<=1/4: L=z/[7(1-z)], U=z/(1-z);
- for 1/4 <=z<=7/16: L=z/[7(1-z)], U=(1/2-z)/(1-z).

Conversely every legal (z,r) corresponds to t=z+(1-z)r, a=1-t, c=z/t, a lawful parameter pair. The total feasible r range is [1/57,1/3]. At z_*=1/4 the fiber is exactly [1/21,1/3].

Define the Bernoulli Fisher coordinate theta(r)=2 arcsin sqrt(r), with theta'(r)=1/sqrt(r(1-r)), Fisher length I(z)=theta(U(z))-theta(L(z)) and F(z)=sqrt(1-z) I(z).

**Fiber-maximum lemma:** max_z F(z)=F(1/4)=sqrt(3)(arcsin sqrt(1/3)-arcsin sqrt(1/21)).

Proof. On z in [1/16,7/64] put x=z/(1-z), A(x)=(1-7x)/8, g(x)=arcsin sqrt(x)-arcsin sqrt(A(x)). Then F=2g/sqrt(1+x). Writing f(s)=1/[2sqrt(s(1-s))]>=1, g'=f(x)+(7/8)f(A)>=1. Also 0<=g<=pi/2; the derivative sign is that of g'-g/[2(1+x)]>=1-pi/4>0. On [7/64,1/4], L=x/7,U=x and

F=sqrt(x/(1+x)) integral_(1/7)^1 du/[sqrt(u)*sqrt(1-xu)],

whose positive factors strictly increase with x. On [1/4,7/16], L increases and U decreases while sqrt(1-z) decreases, so F decreases. Hence the unique maximum occurs at z=1/4. QED.

## Uniform tagged-branch local-overlap lemma

Conditional on a compressed word with m positions labeled "other", its true stop4 count is Bin(m,r). If one draws a single R from density w and fills the m positions independently conditional on R, the reconstructed count law is

Q_m^w(k)=C(m,k) integral_0^1 u^k(1-u)^(m-k)w(u)du, k=0,...,m.

Both the true and reconstructed laws are uniform across the C(m,k) tagged subsets given count k, hence full conditional-word overlap is exactly

h_m(r;w)=sum_(k=0)^m min(C(m,k)r^k(1-r)^(m-k),Q_m^w(k)).

**Lemma.** If r ranges over a fixed compact subinterval of (0,1), the density family w is uniformly bounded, and around each r it has a uniform positive neighborhood on which w and w' are uniformly bounded and w(r) stays uniformly positive, then uniformly in r and w,

h_m(r;w)=[2w(r)sqrt(r(1-r))+o(1)] sqrt(log m/m).

Proof. For k=mr+O(sqrt(m log m)), the exact beta-posterior identity gives
Q_m^w(k)=(m+1)^(-1) E[w(T)] with T~Beta(k+1,m-k+1).
Uniform posterior concentration and local regularity show Q_m^w(k)=(w(r)+o(1))/m. The uniform Stirling/moderate deviation expansion gives
log p_m(k)=-0.5 log(2pi m r(1-r))-(k-mr)^2/[2m r(1-r)]+o(1).
For every fixed eta in (0,1), on |k-mr|<=(1-eta)sqrt(mr(1-r)log m), p_m(k)/Q_m^w(k)->infinity uniformly, and the sum of Q in this interval has coefficient 2(1-eta)w(r)sqrt(r(1-r)). On the enlarged interval with 1+eta, use Q for an upper bound; outside it, Chernoff's binomial KL bound and D(r+d||r)=d²/[2r(1-r)](1+O(d)) give tail <=2m^(-(1+eta)^2/2+o(1))=o(sqrt(log m/m)). Let eta↓0, obtaining the uniform equality. QED.

## Constructive minimax lower bound: observable-z-adaptive Fisher mixture

Fix rho in (0,1/57), and set l_rho(x)=L(x)-rho, u_rho(x)=U(x)+rho,
J_rho(x)=integral_(l_rho(x))^(u_rho(x)) dt/sqrt(t(1-t)).
The endpoints are strictly inside (0,1) for all legal x. Define

w_(rho,x)(s)=1_[l_rho(x),u_rho(x)](s)/[J_rho(x)sqrt(s(1-s))].

Given the *observed* compressed word y, compute zhat=#(stop3)/n and x=clip(zhat,[1/16,7/16]); draw ONE R from w_(rho,x), preserve every observed stop3 position, and label every other position stop4 with probability R and stop1 otherwise, conditionally independently. This K_(rho,n) is parameter-independent and reads only y.

For any legal (z,r), Hoeffding gives P(|zhat-z|>n^(-1/3))<=2exp(-2n^(1/3)). The maps L and U are Lipschitz on the legal compact interval. On this uniformly high probability event the true r lies at least rho/2 inside [l_rho(x),u_rho(x)] for all sufficiently large n. Therefore the shared density family satisfies the uniform local lemma and J_rho(x)=J_rho(z)+o(1), uniformly in legal (z,r). The number M=n(1-zhat) of other positions satisfies M/n=1-z+o(1) and is uniformly of order n.

Because y's marginal law is identical for P^n and B_z^n K_(rho,n) and the kernel preserves the compressed y, conditioning on y and summing tagged branch overlap gives

Omega(P^n,B_z^n K_(rho,n))=E_y[h_M(r;w_(rho,x))].

Thus
liminf_n sqrt(n/log n) inf_(z,r legal) Omega(P^n,B_z^n K_(rho,n))
>= 2 / max_z [sqrt(1-z) J_rho(z)].

Take the supremum over all kernels, then let rho↓0 *after* the n-limit. Since J_rho(z)->I(z) uniformly on the legal compact z interval, the fiber-maximum lemma yields
liminf_n sqrt(n/log n)(1-delta_n) >= 2/F(1/4)=C_*.

## Matching upper bound against every reconstruction kernel

Fix the single legal fiber z_*=1/4, beta=1-z_*=3/4, r in [1/21,1/3], length I_*=I(1/4). For any K, the law Q=B_(1/4)^n K is *identical* for all hypotheses on this fiber, regardless of whether K preserves y.

For fixed eta>0, choose N_n=floor(I_*/d_n)+1 distinct hypotheses equally spaced in theta-coordinate at step
d_n=2(1+eta)sqrt(log n/(n beta));
their coordinates are theta_j=theta(1/21)+j d_n, j=0,...,floor(I_*/d_n).
All r_j=sin²(theta_j/2) are feasible with z_*.

Partition full tagged words into disjoint events A_j by nearest Fisher-coordinate grid point to
thetahat=2 arcsin sqrt(S/M), where M=#(non-stop3), S=#(stop4), with a fixed tie/default rule for M=0.

Under true hypothesis j, M~Bin(n,beta), S|M~Bin(M,r_j). Choose gamma>0 small enough that (1-gamma)(1+eta)^2>1. Chernoff gives P(M<(1-gamma)n beta)<=e^(-c_gamma n). On the complementary event, A_j^c implies |thetahat-theta_j|>=d_n/2. Uniformly over r_j∈[1/21,1/3], binomial KL and D(s||r)=0.5(theta(s)-theta(r))²(1+o(1)) for close s,r give

sup_j P_j(A_j^c)
<= e^(-c_gamma n)+2n^(-(1-gamma)(1+eta)^2/2+o(1))
= o(sqrt(log n/n)).

For arbitrary Q, Omega(P_j,Q)<=Q(A_j)+P_j(A_j^c). Since the A_j partition the output space,
inf_j Omega(P_j,Q) <= (1/N_n) sum_j Omega(P_j,Q)
<= 1/N_n+o(sqrt(log n/n)).

As N_n~I_*sqrt(n beta)/[2(1+eta)sqrt(log n)], taking supremum over K then eta↓0 gives

limsup_n sqrt(n/log n)(1-delta_n) <= 2/(I_*sqrt(beta))=2/F(1/4)=C_*.

The constructive lower bound matches this, completing the proof.

## Computation and scope

A standalone Python verifier checks the exact piecewise fiber inequalities and inverse legal pair map using Fraction arithmetic, plus finite three-tag multinomial normalization (7,013 assertions passed). Its mpmath 70-digit diagnostic evaluates the Fisher constant and verifies monotonicity on a finite grid; global monotonicity and all asymptotics are proved analytically above. Independent mathematical review remains pending. The six-source/ten-label S23 mother target R_beh(k,10) (k=4,6) requires a separately legal source-selection, encoder/decoder and observation bridge; this theorem is for the precisely declared conditional AV auxiliary experiment.

BRC applicability: REUSE_APPLIED for a positive rational tagged branch histogram retaining positional identity, multiplicities and one shared latent parameter. Standard probability/Fisher analysis is a typed auxiliary calculation, not a native spatial or BRC–Shor dynamics claim.

Next units: independent analytic audit (uniform local lemma near padded boundaries and uniform KL exponent); constructive finite-n certified convergence; lawful ten-label S23 mother-bridge search.