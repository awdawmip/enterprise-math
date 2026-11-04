# R5 — lawful two-gate BRC with repeated likelihood-ratio mergers: exact Jensen separation interval

Date: 2026-11-05 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED_AT_LAMBDA_1_20 / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scientific source and scope

Continue the verified author-side frontier research_notes/brc_r5_roc_profile_classification_20261104_t2349/RESEARCH.md at immutable commit 9b22d476e4a362653b25244d0b26753136648aae. Frozen inputs remain Global a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Current normative rules are a separate read. P000/ACTIVE X6 worldview and joint-relation preservation are unchanged. This is an explicitly typed finite positive-weight BRC probability/path observer, making no native spatial/physical computation claim.

## Exact legal two-measure stopped experiment

At time 1 an unobserved source h in {A,B} is sampled with P(h)=Q(h)=1/2, so the two histories collide at LR=1. At each nonterminal node FULL may STOP_P, STOP_Q, or CONTINUE. Seedless LR uses a single behavioral policy at each (time, likelihood-ratio) key, with independent fresh randomization.

If time-1 CONTINUE is selected, time-2 signal s in {0,1} is sampled conditional on either source using Q(s|h)=(1/2,1/2), P(s|h)=(1/4,3/4). Therefore r_2(s)=P/Q is 1/2 or 3/2: both keys again merge the A/B histories. At time 2 all three actions remain legal. On CONTINUE to time 3, the terminal signal u has strictly positive source-dependent laws

A: Q_A=(1/2,1/2), P_A=(3/8,5/8); terminal multipliers u=(3/4,5/4).
B: Q_B=(1/2,1/2), P_B=(1/4,3/4); terminal multipliers u=(1/2,3/2).

The absolute time-3 LR is r_3=r_2(s)*u. At time 3 the decision is free P/Q declaration (no forced label). The seven terminal LR keys are {1/4,3/8,5/8,3/4,9/8,15/8,9/4}. In particular r_3=3/4 is reached from both B,s=0,u=3/2 and B,s=1,u=1/2: a later distinct-path LR collision. All listed stochastic transition probabilities are strictly positive.

The four-dimensional observation is O4=(eP,eQ,TP,TQ), where eP=P(declare Q), eQ=Q(declare P), TP=E_P(stopping time), TQ=E_Q(stopping time).

## New scoped theorem (a full real penalty interval)

For every real lambda in [1/24,1/12] set n_lambda=(-1,-1,-lambda,0). In this exact two-gate tree,

 h_FULL(n_lambda) - h_seedlessLR(n_lambda)
   = 1/32 - 3 lambda / 8.

The gap is strictly positive for lambda in [1/24,1/12), and vanishes at the upper endpoint for this specified direction. Consequently throughout the strict interval the complete O4 convex hulls are unequal. This supplies a continuum of exact separation certificates even after adding the second controlled stop/continue gate and repeated LR collisions.

### Proof

Maximizing n_lambda·O4 is equivalent to minimizing eP+eQ+lambda TP. Terminal Bayes declaration at any LR r chooses Q for r<1, P for r>1, with arbitrary tie at r=1. It is LR-compatible even across the terminal collision r=3/4.

At time-2 key r=1/2, all source-specific terminal LRs are below 1, so continued observation never improves Bayes error while it incurs the nonnegative TP penalty. Both policy classes stop and declare Q.

At time-2 key r=3/2, both A terminal LRs are greater than 1; the A Bayes risk gain from continuation per unit Q mass is G_A=0. The B terminal LRs are 3/4 and 9/4, yielding per-unit-Q Bayes gain G_B=1-( (3/4+1)/2 )=1/8. Continuing one step costs r*lambda=3lambda/2 in P-weighted stopping time per unit Q mass. FULL therefore continues for B, r=3/2 whenever lambda<1/12, and stops on A. For seedless LR, the conditional Q-mixture of A and B at r=3/2 is uniform (both sources have identical time-2 Q kernels). Its gain is (G_A+G_B)/2=1/16, so LR stops whenever lambda>=1/24. All these decisions are legal, including boundary indifference.

For the specified interval the time-1 optimal action is CONTINUE for both sources/classes: observing the time-2 signal reduces error from 1 to 3/4 per unit initial mass, while the incremental time penalty is lambda<=1/12<1/4. FULL's optional further B-high continuation can only improve its value. Thus both classes reach time 2 with probability one.

The only behavioral difference is FULL continuing at the B,s=1 cell, which has Q mass 1/4, P mass 3/8. The gain in Bayes errors is (1/4)*(1/8)=1/32, while the extra TP penalty is (3/8)*lambda. Hence the exact support gap is 1/32-3lambda/8. At the endpoint lambda=1/12, FULL may stop instead at equal cost, giving gap zero. No behavioral randomization increases a linear support optimum: the finite-policy Bellman minima are attained deterministically. QED.

## Exact rational witness and distance certificate

Choose lambda=1/20. A FULL deterministic policy continues at time 1; at time 2 it stops and declares Q for s=0 regardless of source, stops and declares P for A,s=1, and continues for B,s=1; at time 3 it declares Q when r_3=3/4 and P when r_3=9/4. Other unreachable time-3 declarations may be arbitrary.

Its exact observation W=(11/32,3/8,19/8,9/4). The best LR policy at this direction continues at time 1 and stops at time 2, declaring Q at r=1/2 and P at r=3/2. The resulting observation is (1/4,1/2,2,2).

For n=(-1,-1,-1/20,0),

 h_FULL(n)=-67/80, h_LR(n)=-17/20, Delta=1/80>0.

Since ||n||_1=41/20, the separating FULL witness satisfies

 dist_infty(W,conv O4(LR)) >= (1/80)/(41/20) = 1/164.

This is a strict rational four-coordinate certificate. The finite check enumerates all 3*3^2*2^7=3456 seedless-LR deterministic policies; FULL is optimized by exact dynamic programming, independently evaluated at the stated FULL witness. The computed sample phase values are algebraic checks of the interval formula, not a numerical proof of its universal scope.

## Interpretation and remaining R5 objective

The first likelihood-ratio merger (time 1), second source merger (two keys at time 2), and third path collision (r_3=3/4 at time 3) coexist with legitimate free declarations. The B-specific future Bayes gain at the second gate remains a future-relevant history residual. A later LR collision of terminal labels alone does not cancel its signed support excess. This is a scoped mathematical obstruction for this topology, not a universal impossibility claim for multi-gate BRC.

The full R5 mother objective remains open: exhibit a lawful positive-P/Q BRC process for which conv O4(FULL)=conv O4(seedless LR) but O4(FULL) differs from the actual real-behavior LR image. The next unit should test a compensating interaction branch that changes the FULL and LR four-dimensional hulls, with an exact rational vertex/dual certificate before algebraic nonmembership.

Literature context: Ryan A. Anderson and Guido Montufar, "The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes", ICML 2026, PMLR 306:2677–2715, https://proceedings.mlr.press/v306/anderson26a.html . Their result concerns infinite-horizon memoryless-POMDP value sets, not this stopped BRC model. No new originality or independent review claim is made.
