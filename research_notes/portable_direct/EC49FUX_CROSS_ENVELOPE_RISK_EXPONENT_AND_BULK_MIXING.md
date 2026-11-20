# EC49FUX — Cross-endpoint error exponent and eventual bulk least-favorable mixing

Date: 2026-11-20 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FRACTION_FINITE_CROSSCHECK / PARENT_DEPENDENT_FOR_ENDPOINT_PRIOR / NOT_REVIEWED.

## Frozen science and model
Frozen BRC16943 input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Scientific predecessor: EC49FUW at c31293eaa1fb72f6b721df228f7abdfb2862cbbb. FUO/FUQ/FUR are author-proved, not independently reviewed, and establish threshold completeness, endpoint least-favorability, and the dual formula. The risk inequality and exponent below are independent of these parent reductions; only the final endpoint-prior interpretation depends on FUQ.

Let E=31597745/1653649, beta=3/637, u_theta=21829245984/(45529434409-456083905 theta),
T_theta(x)=(1-x)(1-beta x+beta theta x), p_theta=1-T_theta, q_theta=1-u_theta T_theta.
At a common unknown theta in [0,E], H0 is n conditionally iid Bernoulli(p_theta) observations and H1 is n conditionally iid Bernoulli(q_theta) observations, with equal hypothesis priors. For any randomized test phi on the full n-bit vector, R_theta(phi)=[P_{p_theta}(phi=1)+P_{q_theta}(phi=0)]/2 and V_n(x)=inf_phi sup_theta R_theta(phi).

For 0<x<1, write p0=p_0(x), pE=p_E(x), q0=q_0(x), qE=q_E(x). Then

    0 < pE < p0 < qE < q0 < 1.                              (O)

Indeed T_theta and u_theta both strictly increase with theta and q_theta strictly decreases. The middle gap is

    qE-p0=(1-x)[(1-uE)-(beta+uE beta(E-1))x],

with the exact positive certificate
(1-uE)-beta-uE beta(E-1)=1822277955590/5180265550733 > 0.

For 0<p<q<1, let B_n(p,q) be the Bayes error for two equal-prior iid Bernoulli hypotheses:

    B_n(p,q) = (1/2) sum_{k=0}^n min{Bin(n,p)[k], Bin(n,q)[k]}.

This binary clipped-price observer is a deliberately lossy projection, not the native BRC/X6 state; native signed relations, path, ports and provenance remain outside its observation.

## Theorem 1. Uniform finite-n cross-endpoint risk sandwich

For every n>=1 and every x in (0,1),

    (1/2) B_n(p0,qE) <= V_n(x) <= B_n(p0,qE).                (1)

Proof. Since p0<qE, the simple pair (p0,qE) has a monotone likelihood-ratio test phi_c, increasing in the total hit count K. Since p_theta<=p0 and q_theta>=qE for each theta, stochastic dominance gives R_theta(phi_c)<=B_n(p0,qE); this proves the upper bound.

For any arbitrary randomized phi, max(R_0,R_E)>=(R_0+R_E)/2. Expand:

    (R_0+R_E)/2
    =[FP_{p0}+FP_{pE}+FN_{q0}+FN_{qE}]/4
    >=[FP_{p0}+FN_{qE}]/4.

Infimizing over all phi in the final expression gives B_n(p0,qE)/2. Neither minimax interchange nor the FUO/FUQ reductions are used. QED.

## Theorem 2. Exact composite minimax error exponent, uniform on interior compact widths

Define for each fixed 0<x<1 the cross-endpoint probabilities a=p0(x), b=qE(x), and

    t(x)=log((1-a)/(1-b))/log(b(1-a)/(a(1-b))),
    D(t||r)=t log(t/r)+(1-t) log((1-t)/(1-r)),
    C_cross(x)=D(t(x)||a)=D(t(x)||b)>0.

Then a<t<b and

    lim_{n->infinity} -(1/n) log V_n(x)=C_cross(x).          (2)

For every eps in (0,1/2) this convergence is uniform for x in [eps,1-eps].

Proof. The equality of relative entropies is the zero log-likelihood-ratio identity. The simple-pair test that accepts H1 when K>=ceil(nt) has each error tail bounded by exp(-n C_cross), by binomial Chernoff inequalities. Consequently B_n(a,b)<=exp(-n C_cross).

For a lower bound let k_n be an integer nearest nt, and h_n=k_n/n. The standard exact-type inequality

    binom(n,k)>=exp(n H(k/n))/(n+1)

yields

    B_n(a,b)>=exp[-n max{D(h_n||a),D(h_n||b)}]/[2(n+1)].

Here h_n=t+O(1/n), and both divergences at t equal C_cross. Their derivatives are bounded locally because 0<a<t<b<1. This proves -log B_n/n -> C_cross. For x in [eps,1-eps], all the parameters and t stay in a compact subset of (0,1); all error constants are therefore uniform. Inequality (1) changes -log risk/n by at most log(2)/n. QED.

## Theorem 3. Compulsory two-endpoint mixing throughout compact interior width ranges at large n

Let C_E(x)=C(pE,qE) and C_0(x)=C(p0,q0), with C the equal-prior Bernoulli Chernoff exponent. For every 0<x<1,

    C_cross(x)<min{C_E(x),C_0(x)}.                           (3)

For every x there exists N(x) such that n>=N(x) implies

    V_n(x)>max{B_n(pE,qE),B_n(p0,q0)}.                      (4)

For each eps in (0,1/2), a single N(eps) makes (4) hold simultaneously over the entire real interval x in [eps,1-eps].

Combined with FUQ's existence of an endpoint-supported least-favorable prior, every optimal endpoint-supported prior must assign strictly positive mass to both theta=0 and theta=E throughout the specified interval for n>=N(eps).

Proof. When 0<p<q<1, the Chernoff coefficient A_s(p,q)=p^s q^(1-s)+(1-p)^s(1-q)^(1-s), at each 0<s<1, strictly increases with p and strictly decreases with q. Its minimizing exponent s is interior; hence C(p,q) strictly increases when p decreases at fixed q or q increases at fixed p. Apply (O) to obtain (3).

Theorem 2 gives B_n(p0,qE)>=c_x(n+1)^(-1)exp(-n C_cross), for some c_x>0; and B_n(pE,qE)<=exp(-n C_E), B_n(p0,q0)<=exp(-n C_0). The positive gaps in (3) imply eventually B_n(p0,qE)/2 exceeds both pure-endpoint Bayes errors. On each compact interior interval these gaps have a strictly positive minimum and c_x has a common positive lower bound; therefore the same assertion holds for all x there with one N(eps). Apply (1) to get (4).

If the least-favorable endpoint prior were a single delta_0 or delta_E, finite minimax duality would force V_n to equal its respective simple endpoint Bayes error, contradicting (4). QED.

## Significance and verification scope

This identifies the actual asymptotic risk-controlling pair: the largest null success probability p0 and smallest alternative success probability qE. The two probabilities need not occur at the same nuisance value. They provide a tight factor-two error bound for the *common-theta* game, not a replacement of that game by a mismatched-theta experiment.

This is consistent with FUW's fixed-j mixing windows at exponentially small widths b_(n,j)->0: such widths eventually leave every fixed interior compact. The observed n=30 high-width pure-E regime of FUU is therefore a finite-n phenomenon at any fixed width x<1. The theorem does not assert a count of connected components.

Companion exact Fraction code: EC49FUX_CROSS_ENVELOPE_VERIFY.py. Executed locally on 2026-11-20. It constructs full binomial count masses and exhausts every dual affine kink to obtain the exact finite-n two-endpoint minimax value under the FUQ reduction. It tests (1) and both simple endpoint lower bounds for n=2,5,15,30 and x=1/100,3/20,7/20,3/5,19/20: **PASS, 20 exact rational cases**. Sample n=30,x=7/20: B_cross approximately 0.0789886251, V approximately 0.0646901442, E prior weight approximately 0.958482767. Those numbers certify only the finite samples; general results follow from the analytic proofs.

Next: a quantitative effective N(eps), asymptotic optimal threshold and mixing weights, and boundary-layer scales x->0 and x->1. Preserve source-labelled BRC/X6 fibers and the explicit loss of binary observation information.

Historical attribution: Researcher EM-DIRECT-8454C6 / SID MCP-44cfc4e6f2094f96861854ebefc77e84 / Activity RA-ED136F89271FD89288F3E58D. These are prior provenance, not new execution credentials. Current work is independent portable science; no CLAIM, formal Result, Review, Activity CAS update or P000 change is asserted.