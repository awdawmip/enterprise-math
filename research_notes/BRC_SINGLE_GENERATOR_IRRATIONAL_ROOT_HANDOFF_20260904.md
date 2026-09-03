# BRC single-generator irrational-root handoff

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T51, main-backed PR #1186, main-backed PR #1188

## 1. Problem

WBRC-T52/T53 separate two exact Newton regimes:

- rational translated selected roots preserve rational coefficients over the rational-prime-valuation scale carrier;
- an irrational algebraic **base** selected root may be kept as one selected-root evaluation generator as long as later translated roots are rational.

The remaining boundary has often been summarized as "irrational translated root => multi-generator algebraic frontier".  That is too coarse.

There is a strictly easier case:

> if the coefficient algebra immediately before the first irrational translated root is still Q, then that new irrational root can simply become the new single selected-root generator.

No second algebraic generator is required.

This note proves that handoff and also isolates a second no-new-generator mechanism: a new algebraic root already certified as an element of the current single-root evaluation algebra.

Newton/Puiseux theory and algebraic root isolation are classical prior art.  No generic algebraic-number novelty is claimed.

## 2. Exact scale carrier is unchanged

Continue to use

S_rad = Q_{>0}^x tensor_Z Q,

stored by finite rational prime valuations.  The root handoff changes only the coefficient carrier; it does not change Newton scale arithmetic.

## 3. Rational-coefficient irrational-root handoff

Let a finite Newton jet be

J_s(y) = sum_sigma sigma^s P_sigma(y),   P_sigma in Q[y].

Assume the scale-one polynomial E(y)=P_1(y) has an exact selected real root beta, possibly irrational, of multiplicity r >= 1.  An exact selector consists of:

- a rational polynomial f(y) vanishing at beta;
- a rational interval I_beta isolating beta from the other real roots relevant to the selected branch.

Define the single-root evaluation algebra

A_beta = { [g]_beta := g(beta) : g in Q[y] },

with semantic equality/zero and sign decided by the same gcd/Sturm + interval-refinement method already used by WBRC-T53.

For the Newton translation

y = beta + theta^s x,

every Taylor coefficient is

P_sigma^(k)(beta)/k! = [P_sigma^(k)/k!]_beta.

Therefore after dividing by the selected Newton scale, the residual jet has:

- finite support in S_rad;
- polynomial-in-x coefficients in A_beta;
- exact semantic zero, equality, sign and contact tests.

Hence the first irrational translated root over a rational coefficient jet does **not** require a multi-generator carrier.

### Handoff theorem

RATIONAL_COEFFICIENT_JET + FIRST_IRRATIONAL_TRANSLATED_ROOT beta
    -> SINGLE_SELECTED_ROOT_EVALUATION_ALGEBRA A_beta.

If subsequent translated selected roots are rational, WBRC-T53-style recursion continues exactly with beta as the sole algebraic generator.

## 4. Generator absorption inside an existing single-root algebra

Suppose coefficients already lie in A_alpha and a later edge polynomial E(y) has a selected root beta for which an explicit candidate h in Q[x] is supplied with semantics

beta = [h]_alpha.

A sufficient exact certificate for "no new generator" is:

1. E([h]_alpha) = 0 by selected-root semantic zero testing;
2. the candidate value is isolated on the intended selected real branch (for example by exact sign bracketing against rational/algebraic interval endpoints when the application supplies such a bracket);
3. multiplicity/contact statements are verified in the existing A_alpha algebra.

Then every coefficient after translation by beta remains in A_alpha, because beta itself is already an A_alpha element.

This is a **certificate interface**, not a general search algorithm for h.

## 5. The genuinely multi-generator boundary

A new algebraic generator is required only after the two easier routes fail:

- the current coefficient carrier is already non-rational, so simple handoff would discard live algebraic data; and
- the new selected root is not certified as an element of the current single-root evaluation algebra.

Thus the boundary becomes

EXISTING ALGEBRAIC GENERATOR alpha
+ NEW IRRATIONAL TRANSLATED ROOT beta
+ NO ABSORPTION CERTIFICATE beta=[h]_alpha
    -> MULTI_GENERATOR FRONTIER.

This is strictly narrower than the previous shorthand "irrational translated root".

## 6. Systematic BRC realization of handoff

Take a non-negative irreducible integer 2x2 matrix B with irrational Perron root lambda.  Form the 4-state tied base

K = I_4,
L = diag(B,B).

Choose rational scales

0 < eta < 1,
eta^2 < tau < eta.

Consider the exact normalized moment family

A_s = I_4 + eta^s L + tau^s I_4.

This is an explicit positive-branch BRC family: every integer entry of L is realized as that many branches in the eta layer, and I_4 as one branch per diagonal cell in the tau layer.

At z=1 the first Newton edge is

E_1(y) = det(y I_2 + B)^2.

The Perron-selected root is

beta = -rho(B),

which is irrational for the chosen B and has multiplicity two because of the repeated block.

Handoff to A_beta.  Since eta^2 < tau, the next scale is

theta_2 = tau / eta,

and the second translated selected root is exactly

x_0 = -1,

again of multiplicity two.  Thus recursion resumes inside the single generator A_beta with a rational translated root.

This family directly realizes

Q  ->  A_beta  ->  A_beta

and refutes the idea that an irrational translated root by itself forces a multi-generator coefficient field.

## 7. Golden/Fibonacci witness

Let

B = [[1,1],[1,0]].

Its Perron root is phi=(1+sqrt(5))/2.  The first edge factor is

y^2+y-1,

so the selected negative root is

beta = -phi.

With eta=1/2 and tau=1/3,

eta^2=1/4 < 1/3 < 1/2=eta.

The second Newton scale is

theta_2 = (1/3)/(1/2) = 2/3,

and the next translated root is -1.  All beta-dependent coefficients are represented as rational polynomials evaluated at beta; no floating phi is used.

## 8. Exact validation plan

The dedicated checker must:

1. implement a research-level rational-polynomial real-root selector using Sturm sequences and a rational Cauchy bound, including negative roots;
2. enumerate non-negative irreducible B in {0,1,2}^{2x2} whose Perron root is irrational;
3. construct K=diag(B,B) in the first Newton edge and select beta=-rho(B) as the smallest real edge root;
4. verify beta is irrational and double in the repeated-block edge polynomial;
5. build the A_beta evaluation jet from Taylor coefficients;
6. verify the next rational root -1 and its multiplicity;
7. compare recursive handoff + rational second step against one-shot two-step substitution by semantic equality at beta;
8. test selected-root zero/sign operations without floating beta;
9. validate the Fibonacci/golden witness;
10. validate an absorption certificate beta=[h]_alpha in a controlled single-root example.

## 9. Hard boundaries

- SINGLE_GENERATOR_HANDOFF != MULTI_GENERATOR_ALGEBRAIC_FIELD.
- HANDOFF_FROM_Q does not apply if old algebraic coefficients must remain live.
- ABSORPTION_CERTIFICATE is a verifier, not a general solver for h.
- RESEARCH_REAL_ROOT_SELECTOR is not yet a production replacement for WBRC-T41.
- No general factorization, inversion field, primitive-element construction, complete Puiseux solver, signed/amplitude, infinite-state or arbitrary exact-weight extension is claimed.
