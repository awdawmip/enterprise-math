# BRC N=4 / S23: strict asymptotic full-source cost advantage at the Fisher-equality price

Date: 2026-11-03. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor: PR #1765@b572e09189dc4c1fab282162b1a130bc8d3177b0, research_notes/brc_n4_s23_cost_frontier_20261103_research1/PROOF.md and NEXT_TASK.md.

## Model and exact question

Keep lawful S23 scheme (3,31), source-row 0 deletion, full retained E-row-1 trial T, and Bernoulli E-row-0 event-2 repair trial B, together with the predecessor's lawful two-state pair. Every trial retains its source and stopping-branch tags. Fix h=1/42, s=(1-beta_E)^2=1/4, p=11/21, q=10/21, beta_N=0.

Under +/- respectively:
- T law on (+, erasure, -) is (11/84,3/4,10/84) vs (10/84,3/4,11/84);
- B law is Bernoulli with success probability x=11/84 vs y=10/84 (failure probabilities 73/84 vs 74/84).

T costs c_T=7/4; B costs c_B=1 stipulated abstract units. Trials are independent conditional on the state, hypotheses have equal prior, designs (f,r) are deterministic/nonadaptive, and a real budget L permits (7/4)f+r<=L. Let e(f,r) be the exact optimal testing error of the preceding finite likelihood-overlap theorem. Define E(L)=min e(f,r) over feasible nonnegative integers.

## Theorem: strict cost-normalized Chernoff advantage and optimal-design asymptotic purity

For an experiment X let Z_X(t)=sum_v P_+(v)^t P_-(v)^(1-t), 0<=t<=1; let C_X=-ln(min_t Z_X(t)). The ternary coefficient
Z_T(t)=3/4+(11/84)^t(10/84)^(1-t)+(10/84)^t(11/84)^(1-t)
has unique minimizer 1/2 and C_T=-ln(3/4+sqrt(110)/42).
The Bernoulli coefficient is
Z_B(t)=(11/84)^t(10/84)^(1-t)+(73/84)^t(74/84)^(1-t).

**The exact strict inequality is C_T/(7/4) > C_B.** Consequently, along all real L->infinity,
lim [-ln E(L)]/L=C_T/(7/4).
For *every* sequence of finite-budget exact optimizers (f_L,r_L),
r_L/L -> 0 and (7/4)f_L/L -> 1.
The scalar sample count can nevertheless be sublinear and finite budgets can have strict pure-B or mixed optima.

## Rigorous rational enclosure

Define z0=Z_B(1/2)=(sqrt(110)+sqrt(5402))/84;
d=Z_B'(1/2)=(sqrt(110)/84)ln(11/10)-(sqrt(5402)/84)ln(74/73).
For every 0<=t<=1,
Z_B''(t)>=(10/84)ln(11/10)^2+(73/84)ln(74/73)^2=:m.
Indeed each of the two t-dependent exponential terms is at least its smaller endpoint base. Integrating this second-derivative estimate about 1/2 and completing a square gives
min_t Z_B(t) >= z0-d^2/(2m).

VERIFY.py establishes by rational/integer arithmetic only:
z0 > 999837949/10^9; |d|<45/10^7; m>124/100000;
Z_T(1/2) < U=999716393/10^9.
Therefore min Z_B > 999837949/10^9-(45/10^7)^2/[2(124/100000)] > A=999837940/10^9.
The **exact integer comparison A^7>U^4** yields
min Z_B>A>U^(4/7)>[Z_T(1/2)]^(4/7).
Thus C_B<(4/7)C_T, strictly.

The executable bounds use integer isqrt to enclose sqrt(110),sqrt(5402) at denominator 10^14, and 5 terms of
ln[(1+u)/(1-u)]=2 sum_{j>=0}u^(2j+1)/(2j+1)
with positive remainder at most 2u^11/[11(1-u^2)], for u=1/21 and 1/147. Each sign test is an exact rational assertion, so floating-point calculations are unnecessary.

## Analytic asymptotics over all fixed allocations

For (f,r) set Z_{f,r}(t)=Z_T(t)^f Z_B(t)^r and C(f,r)=-ln(min_t Z_{f,r}(t)).
By min(a,b)<=a^t b^(1-t), the equal-prior Bayes error obeys
e(f,r)<=(1/2) exp[-C(f,r)].

The reverse inequality up to sublinear exponent has a direct proof. Choose an interior minimizing t* (both full-support component pairs differ). Tilt the product law to
Q_{t*}(v)=P_+(v)^t* P_-(v)^(1-t*)/Z_{f,r}(t*).
The log-likelihood ratio R=ln(P_+/P_-) has mean zero under Q_{t*} by the first-order condition. Its variance is <=K(f+r) because elementary T/B log-likelihood increments are bounded. For any feasible budget L, f+r<=L. Thus Chebyshev gives
Q_{t*}(|R|<=L^(2/3)) >= 1-K L^(-1/3).
On this event, min(P_+(v),P_-(v))>=exp[-C(f,r)-L^(2/3)]Q_{t*}(v).
So, uniformly across all feasible nonzero allocations for sufficiently large L,
e(f,r)>=(1/4)exp[-C(f,r)-L^(2/3)].
The zero-sample case has error 1/2, consistent with the lower bound.

For every t,
-ln Z_T(t)<=C_T and -ln Z_B(t)<=C_B; hence
C(f,r)<= f C_T+r C_B <= L M,
where M=max{C_T/(7/4), C_B}=C_T/(7/4).
This gives limsup[-ln E(L)]/L<=M. Conversely the all-T feasible design f=floor(4L/7),r=0 satisfies e(f,0)<=(1/2)exp(-f C_T), so the matching liminf is >=M.

Put delta=M-C_B>0. Every design obeys C(f,r)<=LM-delta*r. Were exact optimizers to have r_L>=epsilon L infinitely often, their lower error bound would exceed the all-T upper error bound by an exponentially diverging factor, contradiction. Hence r_L/L->0. The established optimal exponent also forces unused budget to be o(L), whence (7/4)f_L/L->1.

## Scientific status / scope

This is a global-in-budget asymptotic theorem for the specified paired S23 sampling experiment, extending the previous [0,14] exact budget grid without extrapolation. The finite-budget pure-B optimum at budget 11 and the asymptotic full-T cost share are compatible. All prices are stipulated; no empirical cost measurement or native X6/time lift is asserted. The source, branch and observer identities are retained. The original ten-label decoder minimax interval [1/2,2/3] is a separate open problem; no native CLAIM/Result, independent review or admission is claimed.

Reproduce the exact certificate by running Python 3 standard library VERIFY.py; observed stdout is RUN_EVIDENCE.txt. Next: quantitative finite crossover or boundedness of optimal r_L, variable h,s cost threshold, and z2<-0 intervention with operator pricing across nine parameters.
