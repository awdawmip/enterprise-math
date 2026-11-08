# PREFIX-609-R6 — Simultaneous-critical BRC Fisher matrix is exactly diagonal

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Frozen original native BRC source: research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py; Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41.
Dependencies: PREFIX-601/602 weighted incidence nullspace, PREFIX-605 binary native slot observers, PREFIX-608 one-critical-pair Fisher law.
BRC reuse: REUSE_EXECUTED for frozen original graph and PREFIX-605 exact null basis; REUSE_APPLIED for PREFIX-608 symbolic Fisher identity.
Independent scientific work; no formal TASK CLAIM, Result or Review asserted.

## Exact experiment

The original native phase graph has 48 phase states, 12 incidences organized into 6 disjoint paired classes (e,f), and three native slots. At source phase p of incidence e(p), choose slots 0, 1, 2 with probabilities

    (1, t_e(p), t_e(p)) / (1+2*t_e(p)),

then follow the original NEXT table. All t_e are finite and positive. A pair is *critical* when 4*t_e*t_f=1. Choose any k of six critical pairs. Other pairs have arbitrary positive weights. Each selected critical pair contributes two primitive real left-null contrasts, one from each signed 24-phase block: h_l, l=1,...,2k. Every h_l has two +1 entries, two -1 entries, and zero elsewhere, and h_l P=0 for the untagged transition matrix P.

Let pi_0=(1/48,...,1/48), and pi_theta=pi_0+sum_l(theta_l*h_l). The open cube |theta_l|<1/48 is strictly inside the probability simplex because the phase supports of all h_l are disjoint. In each of N independent trials, sample one phase from pi_theta, execute *one* weighted native slot, and record both the terminal phase q and the Boolean tag [slot=j] for a fixed j in {0,1,2}. The estimand is the 2k-dimensional vector of otherwise invisible phase contrasts, not the general 48-parameter source law. The nine frozen native reward roots leave the phase/slot kernel unchanged.

## Theorem

For every k=0,...,6, every selection of critical pairs and arbitrary positive weights as specified, the per-trial Fisher information matrix at theta=0 is

    I_slot0(0) = 192 * Identity_(2k)
    I_slot1(0) =  96 * Identity_(2k)
    I_slot2(0) =  96 * Identity_(2k).

All cross-coordinate Fisher entries also vanish for every theta in the stated open cube. The diagonal entries at nonzero theta may depend on theta.

## Proof

Order the 48 phases as the original 24 positive and 24 negative phases. PREFIX-605 supplies twelve primitive source supports G_l, one per (paired incidence, signed block), each containing exactly four phase states and with the G_l disjoint and covering all 48 source states. The original NEXT table gives output supports

    Q_l = {NEXT[p][j]: p in G_l, j=0,1,2}.

Direct original-graph enumeration establishes |Q_l|=4, Q_l disjoint, union_l Q_l equals all 48 terminal phases; moreover *every* arrow originating in G_l ends inside Q_l. Thus every tagged-terminal observation atom involving a phase q in Q_l receives probability mass only from G_l. Its derivative with respect to theta_m vanishes for every m != l, even with six independent critical weights. Consequently the Fisher summand (partial_l p)(partial_m p)/p is zero at every outcome for l != m. This proves exact Fisher orthogonality over the entire admissible parameter cube.

For a selected critical pair write t_e=x>0 and t_f=1/(4x). Define C_j as the matrix of joint [slot=j, terminal=q] transition probabilities and P=sum_j C_j. Since h_l P=0, if

    a_q=(pi_0 C_j)_q, b_q=(pi_0(P-C_j))_q, d_q=(h_l C_j)_q,

the complementary-tag derivative is -d_q. Hence

    I^(j)_(l,l)(0) = sum_(q in Q_l, d_q != 0) d_q^2 (1/a_q + 1/b_q).

No incoming arrow to Q_l originates outside G_l. Thus the sum depends only on that one critical pair's x, regardless of the other five pairs' weights. The exact native-graph Laurent-rational simplification for all 6 pairs and both signed blocks gives 192 for slot0 and 96 for each of slot1 and slot2 for every x>0 (the existing PREFIX-608 identity; independently rechecked here with x0,...,x5 as independent positive symbolic parameters). This establishes all diagonal entries. The selected subset result follows because noncritical groups are disjoint from all selected active groups. QED.

## Exact attainable local estimation risk

For fixed tag j write c_0=192 and c_1=c_2=96. Denote the score of outcome Y with respect to theta_l at theta=0 by u_l(Y). Put

    theta_hat_l = (1/(N*c_j)) * sum_(a=1)^N u_l(Y_a).

Because the outcome law is affine in theta and all cross Fisher products vanish, E_theta[u_l(Y)]=c_j*theta_l for *all* theta in the cube. Each estimator is jointly unbiased. At theta=0,

    Cov_0(theta_hat)= (N*c_j)^(-1) Identity_(2k).

This attains the vector Cramer-Rao covariance lower bound at the uniform baseline, and the exact baseline total mean-squared error is

    E_0 ||theta_hat-theta||_2^2 = k/(96N)  [slot0],
    E_0 ||theta_hat-theta||_2^2 = k/(48N)  [slot1 or slot2].

In primitive contrast coordinates, simultaneously activating up to all six singular incidence pairs produces no Fisher cross-coupling penalty. The theorem concerns the specified regular local model and one-step tagged-terminal observer; full-distribution minimax recovery is a separate research question.

## Exact verification and evidence

Companion executable PREFIX609_R6_multi_fiber_fisher_certificate.py imports original frozen PREFIX565 and the PREFIX605 generator. It verifies the immutable native Git blob and science pin; partitions all 48 inputs/outputs into twelve size-four blocks; checks all native arrows within their corresponding block; verifies 576 exact symbolic left-null equations; constructs six algebraically independent positive critical parameters x0,...,x5 and checks 36 Fisher diagonal identities by SymPy rational simplification; verifies 66 off-diagonal support disjointness checks per tag. The recorded result is ALL_CHECKS_PASS using SymPy 1.14.0; exact-result JSON is stored alongside this paper.

## Next scientific units

(1) Derive all theta-dependent diagonal Fisher functions and finite-deviation bounds; (2) compare efficient unknown-baseline/full-48-phase estimation under the same data; (3) measure native tag/endpoint codec and sample cost, including precision/bit complexity. Branch-source identity and end-phase joint information must remain in the observer until a proven future-safe reduction is available.
