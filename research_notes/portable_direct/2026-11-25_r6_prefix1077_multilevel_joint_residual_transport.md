# PREFIX-1077 — Joint residual transport without accumulation of relative error

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Existing informed line EM-DIRECT-780BBE, TASK_RESEARCH; own session metadata recovered in r6-20261125-1150-recover-own, no formal run or CLAIM. Prior owner read r6-20261125-1050-owner-read SUCCEEDED with empty LEASED filter at 2026-11-25T02:52:22.897205Z; current r6-20261125-1150-owner-read admitted QUEUED. No shared task mutation.

Frozen input inherited unchanged from PREFIX-1076: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full X6 Cell pairing, port, sign, phase, multiplicity retained in original constant-term observer. This is an analytical theorem about the derived signed observer, no change to native state or physical time.

Parent read at immutable b47b157958692d0a62f438a3d546baa044168341:research_notes/portable_direct/2026-11-25_r6_prefix1076_uniform_beta_tail_transport.md (entire text). Use its conditional theorem (1) and exact telescoping, with positive constant A0 and uniform C_eta,K_eta for 0<eta<1/2. No re-enumeration or new classical reference computation. The parent assumptions and proof status are retained. Mother B_fix,odd(32) remains open.

## 1. Finite-horizon exact joint law

Write D_m(k)=D(m+8,k), a=m+4, b=k+1. Enlarge the parent threshold C>=1 so that every pair k>=C(m+1) lies in the strictly positive tail and the relative error is <=1/4. Parent gives
 D_m(k)=A0 B(a,b)(1+e_m(k)), |e_m(k)|<=K_eta [a/(a+b)]^eta,
 D_m(k)=sum_(l>=0) D_(m+1)(k+l).
Choose any integer r>=1 and k>=C(m+r+1); r may grow. Put s_i=l_1+...+l_i, s_0=0. At each of r levels use the genuine conditional probability
 P(l_i | l_1,...,l_(i-1))=D_(m+i)(k+s_i)/D_(m+i-1)(k+s_(i-1)).
All numerators and denominators positive because k+s_i>=k>=C(m+r+1). Each conditional sum is 1 by exact telescoping. Multiplication cancels all intermediate denominators:
 P_r(l_1,...,l_r)=D_(m+r)(k+s_r)/D_m(k).                   (J)
This is exact, not a product of separately approximated transition laws. Thus the finite vector is exchangeable, and conditional on S_r=s is exactly uniform over the binomial(s+r-1,r-1) weak compositions of s into r entries. The total law is
 P(S_r=s)=binomial(s+r-1,r-1)D_(m+r)(k+s)/D_m(k).
For h<=r the first h marginal is precisely the h-level law, by normalization of each later kernel; this is finite-horizon consistency, not an assertion that a fixed starting point admits all infinite horizons in the positive region. No original native branch data are deleted: the equality is certified only for this residual-transport observation.

Stronger exact joint survival identity: for arbitrary nonnegative integers t_1,...,t_r, translate l_i=t_i+u_i in (J); sum over u_i>=0 and apply the r-step telescoping at starting k+T, T=sum t_i. All terms positive, so iterated summation is justified. Then
 P_r(l_i>=t_i for every i)=D_m(k+T)/D_m(k).                 (S)
In particular every coordinate has the same one-step marginal. Exact rectangle probabilities follow by inclusion-exclusion on upper boundaries. The full joint survival is obtained from one ratio, rather than separate transition approximations. This identity preserves the correlations in the declared joint observer; using independent marginals in its place is in general incorrect.

## 2. Joint reference law and nonaccumulation of relative errors

Let nu=(a+r)/(a+b+r). The reference joint mass is
 P_r^0(l)=B(a+r,b+s_r)/B(a,b).
It is normalized by mixing r independent geometric failure counts (mass x(1-x)^l) conditionally on a single X~Beta(a,b). Thus the total reference law is beta-negative-binomial:
 P^0(S_r=s)=binomial(s+r-1,r-1) B(a+r,b+s)/B(a,b).
The conditional composition law agrees exactly with (J).

Apply the parent bound only to the endpoints of (J). At the numerator mu'=(a+r)/(a+b+r+s)<=nu; at the denominator mu=a/(a+b)<=nu. Therefore
 sup_(l in N^r) |P_r(l)/P_r^0(l)-1| <= (8K_eta/3) nu^eta.    (E)
Indeed |(1+e_num)/(1+e_den)-1| <= (|e_num|+|e_den|)/(3/4). No factor r multiplies the error. Any event and any nonnegative statistic with finite nonzero reference expectation have the same relative bound; total variation <= (4K_eta/3) nu^eta. Infinite reference expectations transfer when the bound is <1, or directly using each endpoint's error <=1/4. The same pointwise relative estimate applies to S_r. Consequently even when r tends to infinity, provided k/(m+r+1)->infinity, the whole r-dimensional law is approximated in relative error tending to zero. This is stronger than separately approximating every step and adding errors. It uses joint endpoint identity, not independent-residual assumptions.

By (S), joint survival is also uniformly [1+O_eta(mu^eta)] B(a,b+T)/B(a,b), with the *initial* mu, even for arbitrarily large T and every admitted r. For integer a its reference ratio equals prod_(j=0)^(a-1) (b+j)/(b+T+j). This gives a horizon-independent relative estimate for simultaneous lower-tail thresholds; it does not automatically give relative estimates for small inclusion-exclusion differences, for which (E) supplies direct event-wise control.

## 3. Exact reference joint factorial moments, dependence and total budget

For nonnegative integers d_i, R=sum d_i<a, conditional geometric factorial moments and the beta integral yield
 E_0[prod_i (l_i)_(falling d_i)] =
   (prod_i d_i!) B(a-R,b+R)/B(a,b).
For R>=a and at least one d_i>0 this integral diverges. Transfer by (E) gives the same moment existence threshold and the displayed leading formula with relative error O_eta(nu^eta). For total S_r, its conditional generating function is [x/(1-(1-x)z)]^r. Taking d derivatives at z=1 and integrating yields, for d<a,
 E_0[(S_r)_(falling d)] = (r)_(rising d) (b)_(rising d)/((a-1)_(falling d)),
with infinite factorial moments for d>=a. In particular E[S_r]=rb/(a-1)[1+O_eta(nu^eta)]. These moment statements apply to the complete joint transport observer and not to physical time.

For two distinct coordinates, the reference covariance is exactly
 Cov_0(l_i,l_j)=Var((1-X)/X)=b(a+b-1)/[(a-1)^2(a-2)]>0.
The identity follows from E_0 odds=b/(a-1) and E_0 odds^2=b(b+1)/[(a-1)(a-2)]. No relative accuracy for the small covariance difference is asserted when a grows; the raw mixed nonnegative moments are controlled separately. In the fixed-a, b->infinity regime (r>=2), the actual covariance divided by b^2 tends to 1/[(a-1)^2(a-2)] from the first and mixed second moment estimates (one may use the exact two-level marginal with its own threshold). Thus the common latent parameter cannot be replaced by independently drawn beta variables without losing the joint residual law.

## 4. Many-level scaling: two distinct regimes

Assume r->infinity and k/(m+r+1)->infinity, so (E) tends to zero. The following convergence statements therefore transfer from the reference joint law to the actual observer by total variation.

Conditionally on X, the reference total has mean r(1-X)/X and variance r(1-X)/X^2. The conditional variance divided by the square of the conditional mean is 1/[r(1-X)]. Since E[X]=a/(a+b)->0, Markov implies P(X>1/2)->0. On X<=1/2 conditional Chebyshev therefore gives S_r/(r(1-X)/X)->1 in probability. This conditional argument uses no assumption of unconditional independence.

(i) Fixed m (fixed a), b->infinity. The density of bX on 0<y<b is y^(a-1)(1-y/b)^(b-1)/(b^a B(a,b)). The denominator tends to Gamma(a) by the exact integer-a product B(a,b)=(a-1)!/prod_(j=0)^(a-1)(b+j). For b>=2 the numerator is dominated by y^(a-1)e^(-y/2); dominated convergence yields bX converges to G~Gamma(a,1). Thus
 S_r/(rb) converges in distribution to 1/G,
 or a S_r/(rb) converges to a/G.
Even arbitrarily many transport levels do not remove the common-scale fluctuations when the initial path length is fixed. Averaging the levels is not enough to turn this law into a deterministic constant.

(ii) m->infinity (a->infinity). Beta mean and variance give E[bX/a]=b/(a+b)->1 and Var(bX/a)=b^3/[a(a+b)^2(a+b+1)]<=1/a. Therefore bX/a->1 in probability, X->0, and the conditional concentration above gives
 a S_r/(rb)->1 in probability.
The random common scale becomes deterministic only in this simultaneous large-initial-length regime. The preceding two limits are statements under the specified joint asymptotic scaling, not finite-n tail certificates.

## 5. Evidence, next question and scope

New science: exact r-level endpoint and joint survival identities; exact uniform conditional composition; a beta-negative-binomial joint approximation with error not accumulating linearly in r; exact moment threshold and common-scale dependence; many-level inverse-gamma versus concentration dichotomy. All statements follow by algebraic telescoping, nonnegative summation, beta normalization and elementary probability estimates from the existing full signed BRC observer. No new native kernel execution, classical trigonometric or pi numerical computation, new external model inputs, or independent review. Probability and integration coordinates are restricted mathematical readouts of the proven positive tail, not new X6 coordinates or heartbeat timing. No formal Result, Task completion, or shared-tool acceptance is claimed.

Next: quantitative delta and observer norms for PREFIX-1076 to turn the relative bounds into finite parameter certificates; explore adaptive finite horizon truncation from (S) and (E), preserving correlation. Regular spectral boundary locations remain open. Do not redo the original native enumeration or endpoint cancellation.