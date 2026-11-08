# PREFIX-608-R6 — Exact Fisher information for native BRC binary slot observers at all six singular incidence pairs

Date: 2026-11-08 Asia/Shanghai.
Frozen scientific pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Original native BRC kernel: \`research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py\`, immutable Git blob \`7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41\`.
Dependencies: PREFIX-601/602 weighted twelve-incidence model and nullspace, PREFIX-605 three binary native slot partitions, PREFIX-606 exact total-variation retention, PREFIX-607 finite-sample internal-slot estimator risk.
Status: AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Question and exact experiment

Fix one of the six original paired incidence classes (e,f), and a positive real parameter x. Give the three native action slots from source phase p probabilities

    Pr(slot=0 | p) = 1/(1+2t_e(p)),
    Pr(slot=1 | p) = Pr(slot=2 | p) = t_e(p)/(1+2t_e(p)).

Set t_e=x, t_f=1/(4x), and all ten other incidence weights equal to 1. Thus exactly the chosen pair is critical. Let P be the 48×48 untagged terminal-phase stochastic matrix, and C_j the 48×48 joint matrix recording (slot=j, terminal phase) for j=0,1,2, each from the unmodified original native NEXT graph. The nine frozen reward roots do not change these phase/slot kernels.

For either of the two signed 24-phase blocks in PREFIX-605, select its normalized critical left-null generator h in R^48. It has two +1 entries, two -1 entries, all others 0, and satisfies h P=0 and sum h=0. Define pi_0=(1/48,...,1/48) and pi_theta=pi_0+theta h, |theta|<1/48, so this is a differentiable family of **legal phase probability distributions**.

In each trial independently sample one starting phase from pi_theta, run exactly one weighted native action, and observe its terminal phase and the Boolean event (slot=j). Repeat independently N times. The parameter theta and selected signed contrast are the inferential target; this is not estimation of all 48 unknown source probabilities nor a single length-N trajectory.

## Theorem — universal critical-fiber information constants

For every x>0, every one of the six incidence pairs, either signed block and all three binary tags, the **per-trial Fisher information at theta=0** is exactly

    I_0(0) = 192,
    I_1(0) = I_2(0) = 96.                            (1)

The values are independent of x, despite x changing both slot frequencies and the native one-step transition law.

Proof. At theta=0 let a_{j,q}=(pi_0 C_j)_q and b_{j,q}=(pi_0(P-C_j))_q. The derivative in the slot=j outcome is d_{j,q}=(h C_j)_q; because hP=0, the derivative for the complementary outcome is -d_{j,q}. The exact Fisher information is therefore

    I_j(0) = sum_q d_{j,q}^2 (1/a_{j,q} + 1/b_{j,q}),  (2)

with zero-derivative summands omitted. All denominators for nonzero d are strictly positive for finite x>0. This formula retains both tag outcomes and the full destination-phase identity.

The native incidence matrix and the PREFIX-605 symbolic critical-pair generator give a finite exact Laurent-rational expression in x for (2). The companion certificate uses the frozen source action table, computes the relevant rows of P and C_j without reconstructing a new graph, verifies hP=0 as 48 exact symbolic identities for each of 12 (pair, signed block) selections, and simplifies (2) in Q(x). All 36 resulting expressions are identically 192, 96, 96 as claimed. The complete finite selection of six pairs times two blocks and three tags covers precisely the theorem's original-graph choices; cancellation in Q(x) proves the identities for every x>0 because the denominators are positive. QED.

## Exact attainable local variance at the uniform baseline

Let Y denote one complete (binary tag, terminal phase) outcome and define its baseline score

    u_j(Y) = [partial_theta p_theta(Y) at theta=0]/p_0(Y).

For N independent trials, define theta_hat_j = [sum_{a=1}^N u_j(Y_a)]/[N I_j(0)].

Since p_theta(Y)=p_0(Y)+theta p'_0(Y) exactly and sum_Y p'_0(Y)=0,

    E_theta u_j(Y) = theta I_j(0).

Therefore theta_hat_j is unbiased for every |theta|<1/48, and at the uniform baseline,

    Var_0(theta_hat_0) = 1/(192 N),
    Var_0(theta_hat_1) = Var_0(theta_hat_2) = 1/(96 N).      (3)

In this regular one-dimensional model these equal the exact Cramer–Rao variance bounds at theta=0; the estimators attain them there. In particular slot0 carries twice the Fisher information of either other singleton-slot tag for the specified critical null contrast.

## Relation to PREFIX-607 and the next objective

PREFIX-607 established that the simple unprojected estimator of the *whole* 48-phase probability vector based only on slot0 hits has mean-squared-error coefficient 1/(2x) on one heavy-incidence point mass. Equation (1) shows a different, complementary fact: at the uniform baseline and when the target is a known single critical null contrast, the **full tagged endpoint distribution** has constant attainable local information in x. An apparent sampling obstruction depends on the estimand, baseline and use of both tag outcomes.

BRC reuse: REUSE_EXECUTED for the pinned PREFIX-565 native graph and PREFIX-605 exact critical left-null generator; REUSE_APPLIED for the PREFIX-606 TV comparison and PREFIX-607 exact risk; the branch identity and terminal-phase observer are retained. The native original model t_e=1 lies off the singular surfaces; this particular Fisher result concerns the declared singular weighted extension.

Actual validation: Python 3 standard library plus SymPy 1.14.0, using exact symbolic rational simplification and pinned native graph imports. The script checks 576 symbolic left-null equations and 36 exact Fisher identities, prints ALL_CHECKS_PASS, and writes PREFIX608_R6_RESULTS.json. Formal proof/admission/independent review remain open.

Next: characterize Fisher eigenvalues on the full active 2k-dimensional nullspace under multiple simultaneous critical incidence pairs, especially with asymmetric positive weights; compare efficient estimators with a full 48-coordinate target and the minimax risk when the baseline is unknown. Distinguish local Fisher, global total variation and finite-sample risk.
