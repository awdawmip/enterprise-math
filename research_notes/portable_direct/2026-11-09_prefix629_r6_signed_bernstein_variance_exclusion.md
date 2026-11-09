# PREFIX-629-R6 — Signed Bernstein certification of a 1/14-width BRC variance exclusion strip

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Inputs: SOURCE-published PREFIX-621 first-passage coefficient recurrence, PREFIX-622 Poisson moment law, PREFIX-624 sign-monotone survivor shapes, PREFIX-626 endpoint witnesses. Original BRC 96-port graph frozen, not rerun. P000 V5/Heartbeat X6 observer scope unchanged.

## Exact theorem

In the two-direction signed-observer model, native trial labels (i,+), (i,-) have probabilities p_i/q,(1-p_i)/q for i=1,2, with remaining neutral probability; q>=2 (actual native slots q=12,24). A direction stops on first attaining the PREFIX-621 anytime-confidence diameter <=1/4 with beta=1/40; T_q is total native actions until both directions finish, V_q(p1,p2)=Var(T_q). Restrict by sign symmetry to [0,1/2]^2. Let a=37/256 and b=39/256.

**Theorem A:** For every q>=2, every 0<=p1<=1/14 and a<=p2<=b,

\[
\boxed{\partial_{p_1} V_q(p_1,p_2)<-36q^2.}
\]

In particular, for 0<p1<=1/14,

\[
V_q(p_1,p_2)<V_q(0,p_2)-36q^2p_1.
\]

The corresponding open-inward rectangle contains no global maximizer of V_q on the parameter square. Its width is 2^24/14 = 8,388,608/7 times the PREFIX-627 width 2^-24.

**Theorem B:** For 0<=p1<=1/16 and the same p2,q,

\[
\boxed{\partial_{p_1} V_q(p_1,p_2)<-376q^2.}
\]

## Proof: finite signed Bernstein upper envelopes

Let A[n,k] count signed words with k plus signs that have not met the first-passage stopping condition after n informative observations. The SOURCE-published exact PREFIX-621 recurrence certifies s_n(p)=0 for n>=189 and, for n<=188,

\[
s_n(p)=\sum_{k=0}^{n}A[n,k]p^k(1-p)^{n-k}
      =\sum_{j=0}^{n}c[n,j]p^j,
\]
\[
c[n,j]=\sum_{k=0}^{j}(-1)^{j-k}A[n,k]\binom{n-k}{j-k}.
\]

All c are integers. PREFIX-624 establishes s_n nondecreasing, s'_n>=0 on [0,1/2], with a strict s_25 term.

Let Y be the maximum of the two independent unit-rate informative Poisson-clock stopping times, mu=E[Y], H=E[Y^2]/2 and W=2H-mu^2. The PREFIX-622 time change yields V_q=q^2 W-q mu.

Define w(n,m)=binom(n+m,n)/2^(n+m+1), z(n,m)=(n+m+1)w(n,m)/2. For n<=188 put

\[
\alpha_n(p)=1-\sum_{m=0}^{188}w(n,m)s_m(p),
\qquad
\beta_n(p)=n+1-\sum_{m=0}^{188}z(n,m)s_m(p).
\]

The exact negative-binomial sums imply 0<=alpha_n<=1, 0<=beta_n<=n+1, and both are nonincreasing in p. Differentiating finite Poisson sums gives

\[
U(p_1,p_2)=\partial_1\mu=\sum_n\alpha_n(p_2)s'_n(p_1),\qquad
J(p_1,p_2)=\partial_1H=\sum_n\beta_n(p_2)s'_n(p_1).
\]

Therefore J(p1,p2)<=J(p1,a), U(p1,p2)>=U(p1,b)>0, and mu(p1,p2)>=mu(0,a)>87, the last strict rational witness being from PREFIX-626. So

\[
\partial_1 W=2(J-\mu U)<2F(p_1),
\quad
F(p):=J(p,a)-87U(p,b)=\sum_{j=0}^{187}f_jp^j,
\]
\[
f_j=(j+1)\sum_{n=j+1}^{188}(\beta_n(a)-87\alpha_n(b))c[n,j+1].
\]

For p=h x and 0<=x<=1, express F(hx) in the degree-187 Bernstein basis. Its control coefficients are

\[
B_k(h)=\sum_{j=0}^{k}f_jh^j
 \frac{\binom{k}{j}}{\binom{187}{j}},
\quad k=0,\ldots,187.
\]

Bernstein basis values are nonnegative and sum to one, so F(p)<=max_k B_k(h) over [0,h]. The accompanying certificate independently computes all exact Fraction coefficients from the published PREFIX-621 recurrence, checks all polynomial endpoint identities, and proves by 188 strict *rational* comparisons for EACH h:

\[
\max_{0\le k\le187}B_k(1/16)<-188,\qquad
\max_{0\le k\le187}B_k(1/14)<-18.
\]

The display approximations for those two maxima are -188.2152306390753 and -18.4645527468804 respectively; comparisons are exact. Thus d_1 W<-376 or <-36 respectively. Since U>0, d_1 V_q=q^2 d_1 W-qU is strictly below the respective q^2 bound. Integration from 0 to p1 establishes the asserted strict exclusions. QED.

## Verification and next research question

Execute "python PREFIX629_R6_bernstein_signed_interval_certificate.py" alongside SOURCE-published PREFIX621_R6_stochastic_tail_certificate.py (Python 3 standard library). Output: ALL_CHECKS_PASS; it produces PREFIX629_R6_RESULTS.json including exact coefficient counts and SHA256 hashes of the exact rational maximum-coefficient representations. A verified exact-rational model proof is not independent review or project admission. Native source observation and frozen graph are not modified.

Next mathematical unit: improve the mu lower envelope or use piecewise signed Bernstein subdivision beyond p1=1/14; test exact rational interior counterexamples against boundary candidate, with full parameter model and observer provenance retained.
