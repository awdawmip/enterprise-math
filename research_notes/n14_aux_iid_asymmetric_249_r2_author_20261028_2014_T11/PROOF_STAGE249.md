# Stage249 — exact N=9 asymmetric minimax theorem

**2026-10-28 | PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.** External IID auxiliary problem only. Parent scientific evidence: Stage247–248, Draft PR #1571 at 654c72ec6719f88c8ba39d1589d790579fb73895.

## Statement

Let independent symbols 0,1,2 have laws P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Let any possibly randomized complete-ordered-history policy stop at 0<=tau<=9 and decide P or Q. Define eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(tau), tQ=E_Q(tau). The exact optimum is

**V_9(3/10,19/40) = 65983208881/10195269120**, where V is the minimum of max(tP,tQ) subject to eP<=3/10 and eQ<=19/40.

This closes Stage248's unresolved exact 9-observation value, not merely a numerical or finite-policy-class bound.

## Universal rational Bellman dual

For count state s=(i,j,k), likelihood L(s)=Q(h)/P(h)=(2/3)^i 2^j for every history h with those counts. Fix lambda=43416/607 and let J(s) be defined backward, for |s|<=9, by

J(s) = min{lambda*L(s) [decide P], lambda [decide Q], 1 + sum_{r=0,1,2} P_r J(s+e_r) [continue]}.

At |s|=9 omit continuation. This recursion evaluates the conditional P-normalized cost of tP+lambda*(eP+eQ), because deciding P incurs Q-error weight lambda*L(s), deciding Q incurs P-error weight lambda, and continuing incurs one P-time unit and independent IID suffix cost. Backwards induction applies pointwise to **every full ordered history**, including arbitrary history-dependent coins; hence any policy satisfies

tP+lambda*(eP+eQ) >= J(0,0,0).

Fraction arithmetic over the 220 count states gives J(0,0,0)=126226064573/2039053824, exactly two Bellman ties (1,0,5) [P/continue] and (0,0,9) [P/Q], and 383 strictly positive alternative-action gaps. With the two caps,

max(tP,tQ) >= tP >= J(0)-lambda*(3/10+19/40) = **65983208881/10195269120**.

This is a two-time/two-error minimax supporting certificate with time weights (thetaP,thetaQ)=(1,0) and error multipliers (lambdaP,lambdaQ)=(43416/607,43416/607).

## Exact policy attaining equality

Use the unique Bellman-minimizing action at every other state. At A=(1,0,5), continue with c=24543634/28453125 and otherwise decide P. At B=(0,0,9), decide P with d=3388291539/4742187500, otherwise decide Q. Both c and d lie strictly between 0 and 1; A cannot reach B since A has seen one 0 while B has seen none, so mixed coin coefficients are zero.

Separate exact P/Q conditional suffix recurrences and an independent unmerged ordered-history DFS give the same four observables:

(eP,eQ,tP,tQ)=(3/10,19/40,65983208881/10195269120,61538202869/10195269120).

Therefore tP-tQ=1111251503/2548817280>0, max(tP,tQ)=tP, and equality holds in the dual (every chosen action minimizes Bellman cost). This proves the optimum for the unrestricted full-history randomized policy class and all alternative real-valued randomization parameters.

## Observer-safe BRC reduction

Original carrier: ordered positive-rational P/Q source-labeled reach, stop and decision branch masses. Declared observers: four quantities eP,eQ,tP,tQ; future operations: IID symbol extension, stopping and classification through horizon 9. For each count s, all histories in the fiber share exactly the same likelihood ratio L(s). Aggregate P reach/action mass over that fiber; Q reach/action mass is L(s) times the corresponding P mass. Averaging the original conditional action probabilities by P reach masses gives a count-state randomized policy preserving *both* P and Q action masses. IID extension propagates that identity to each child count state, thereby preserving all four declared observers and their finite-horizon future updates. This is a scope-specific exact Markovization/descent theorem, not a claim for path-sensitive readouts, non-IID laws, native X6 dynamics or arbitrary future operations.

BRC reuse: **REUSE_APPLIED** finite positive-rational weighted source-labeled branch carrier; no native BRC module execution is claimed.

## Exact execution evidence and boundary

Actual local execution of the adjacent pure-stdlib STAGE249_EXACT_REPRO.py gave STAGE249_EXACT_AUTHOR_PASS; verified 220 Bellman states, 2 ties, 383 strict gaps; conditional four-observer suffix result equals unmerged ordered DFS result from 637 history nodes / 432 terminal action branches with P and Q terminal total masses both 1. See RUN_STAGE249.txt. Author evidence and GitHub storage are not independent Driver review.

Fixed source reads this run: GLOBAL_KNOWLEDGE_V1 main@9e4f20918edc20e0c038133379525bd2470c37a4, Enterprise Math control main@aab9bee8c8338a4d83f6ed20bc4098fd35da1a50; original P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Native em_status research_authority_granted=false; em_control_tasks returned CONTROL_QUOTA. No official active Owner, CLAIM, Source Result, independent mathematical admission or X6 bridge is claimed.

**Next research unit:** Stage250 — exact V10(3/10,19/40) with two-time/two-error dual and rational witness, preserving the four observers and checking whether the time-support weight remains one-sided.
