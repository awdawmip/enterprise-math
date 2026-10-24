# N=14 auxiliary iid sequential discrimination: exact 68th affine interval

**2026-10-24 — author-level exact finite-model proof.** This is an external iid statistical model, not a native BRC/X6/Heartbeat dynamics theorem, a frozen Task Result, or an independent Driver acceptance. All claims inherit the earlier author's deterministic stop tree.

## Statement and inherited facts

Observations are iid with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=14. All randomized full ordered-history sequential decisions are allowed. Let e_P=P(decide Q), e_Q=Q(decide P), t_P=E_P[tau], t_Q=E_Q[tau], and V14(alpha)=min_{e_P,e_Q<=alpha} max(t_P,t_Q).

Source predecessor: commit d0b60bcd906cddf60ce7a2f513afaed4b93354bf, 67th author-level proof and full inherited stopping sets, with A67=(5,1,3) now stopping immediately at Q. At the inherited endpoint, B=(12,0,1) announces Q with s67=26147520029410919/41779200000000000, and

alpha67=5171859472066685747/14900301753911083008,
V67=6168006010039251047/465634429809721344.

Put K68=30451140/5149, lambda_Q=K68, lambda_P=72+(8/9)K68=27438408/5149, Gamma68=57889548/5149, and eta68=563171875/303147415240704.

**Theorem (author level).** For every real 0<=delta<=eta68, including irrational delta,

V14(alpha67+delta)=V67-Gamma68*delta.

The exact endpoint and its value are

alpha68=5171887153090685747/14900301753911083008,
V14(alpha68)=6158280565975251047/465634429809721344.

This supporting line is *right-sharp*: it cannot be attained for alpha>alpha68.

## Bellman bound over the entire ordered-history policy class

At count state z=(n,a,b), the likelihood ratio is L=Q(prefix)/P(prefix)=2^(a+b)/3^a. In the P-normalized Lagrangian t_P+lambda_P e_P+lambda_Q e_Q, action costs are C_P=lambda_Q L, C_Q=lambda_P and, for n<14, C_C=1+sum_i P_i D(child_i). Define D(z) as their minimum, with no C at n=14. Full-history policies have the same suffix law at each count state; therefore the Bellman recursion gives a global lower bound even for arbitrary path-dependent randomization. Ordered histories are retained separately for first-hit counting.

An exact Fraction sweep of 680 states compares 1,240 nonchosen actions: 1,238 strict positive margins, zero negative margins and exactly two zero ties (A68=(8,0,2), C vs Q; B=(12,0,1), C vs Q). Minimum strict margin is 131483062037/7871913787392. The exact root dual value is

D(0,0,0)=4417836723113547221593889/1128259613689531858944
         =V67+Gamma68*alpha67.

For any feasible policy D(root)<=t_P+lambda_P e_P+lambda_Q e_Q<=max(t_P,t_Q)+Gamma68*alpha, so V14(alpha)>=D(root)-Gamma68*alpha.

## Real first-hit enumeration and stop truncation

The new tied A68 has 28 nominal ordered words, **all 28 true first arrivals**. Incoming masses are p_A=109375/6718464 and q_A=109375/1679616. At B, all 12 nominal words survive and p_B=48828125/725594112, q_B=48828125/362797056.

Of the 36 true arrivals at the inherited Q-stop (9,0,2), 28 passed through A68. The inherited Q-stop (10,0,2) has nine first arrivals, none passing through A68, since those paths would already stop at (9,0,2). These facts independently follow from explicit ordered-word enumeration. They preclude treating descendant nominal masses as independent after adding the earlier A68 stop.

With inherited continuation at A68 and B, the exact conditional suffix quadruples (e_P,e_Q,t_P,t_Q) are

R_A=(2354987/2359296, 1051/2985984, 414721/294912, 310613/248832),
R_B=(63/64, 1/144, 9/8, 13/12).

Let u be the conditional probability of announcing Q early at A68, and s the probability of announcing Q early at B. No history can reach both: A68 already has b=2, while the later B has b=1. All four risk functions therefore have zero mixed u*s coefficient, independently checked by backward-risk four-corner differences.

The exact error sensitivities are

X=p_A(1-R_A.e_P)=471296875/15850845241344,
Y=q_A R_A.e_Q=114953125/5015306502144,
E=p_B(1-R_B.e_P)=48828125/46438023168,
H=q_B R_B.e_Q=48828125/52242776064.

Relative to u=0 and s=s67,

Delta e_P=Xu+E(s-s67),  Delta e_Q=-Yu-H(s-s67).

Hence balancing both errors forces

s=s67-h68*u,
h68=(X+Y)/(E+H)=865319/32640000.

The final endpoint s68=25039911709410919/41779200000000000 lies strictly between 0 and 1, so s remains admissible for every u in [0,1]. Then Delta e_P=Delta e_Q=(X-Eh68)u=eta68*u, where eta68=563171875/303147415240704>0.

## Achievability for every real parameter

At the endpoints u=0 and u=1, exact forward risk evaluation yields respectively

t_P-t_Q=640722304971736273/1241691812825923584>0,
t_P-t_Q=2132764916067208819/3725075438477770752>0.

Because the mixed four-corner coefficients vanish, the four risk functions are affine in u under s=s67-h68*u. Therefore t_P>=t_Q throughout the full real segment, and the exact endpoint Bellman equalities extend by affine interpolation:

t_P(u)=V67-Gamma68*eta68*u,
t_P(u)+lambda_P e_P(u)+lambda_Q e_Q(u)=D(root).

Both constraints equal alpha67+eta68*u, so this constructive policy attains the global lower bound for all real u in [0,1]. Let u=delta/eta68 to prove the theorem, without finite-grid extrapolation.

## Sharpness

The finite ordered-history randomized policy polytope is compact. Equality with the same Bellman lower line for any alpha>alpha68 would force both positive-multiplier error constraints to be tight and every positively used action to minimize its state Bellman cost. The exhaustive strict/zero slack certificate permits nontrivial randomization only at the two tied count states A68 and B. Identical likelihood ratios and conditional iid future distributions reduce history-dependent randomization at each tied state to an effective u and s; the states are mutually unreachable on one path. Equal errors enforce s=s67-h68*u and alpha=alpha67+eta68*u<=alpha68 because 0<=u<=1: contradiction. The line is right-sharp, without asserting anything stronger about the next interval.

## Computation scope, BRC and next question

The two exact-Fraction author verifiers are the main 680-state Bellman/first-hit/forward risk script and an independent ordered-word enumeration, Bellman minimization and backward risk script with seven exact rational interpolation samples. Both ran locally and passed. They share the inherited 67th author stop rules: this is not independent Research Driver validation. The BRC positive-weight branch law W=sum over surviving ordered histories of products of branch probabilities is REUSE_APPLIED from definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json (existing source pin d748a6e8c39f40acb5ad5f213d25177a55e54198). Ordered provenance is retained until the stopping filter; no native BRC engine was executed, no P000/X6 physical-law bridge or Lean formalization was completed.

**Unproved 69th candidate only:** K69=103267977646032/19155062389, A69=(5,5,0), CONTINUE versus immediate P. Derive its true first hits, suffix effects, balanced risk and sharp endpoint anew.

Status: N14_68_AUTHOR_PROVED / TWO_AUTHOR_EXACT_RATIONAL_CHECKS / PREDECESSOR_DEPENDENT / DRIVER_UNREVIEWED / NO_NATIVE_BRIDGE / NATIVE_CLAIM_UNVERIFIED.
