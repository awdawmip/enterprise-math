# Nondecisive mathematical review: held-state Euler clock bridge

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: the held-state transform, joint parity transport and same-mean
counterexample are valid under the stated independent positive-integer
waiting mechanism. No unresolved mathematical defect was found.

Reviewed file: `native/EULER_CLOCK_BRIDGE.md`.
SHA256: `25712f05260a722b9bc0b96ee529752d562e3c10fbae6cff211e5399d6990af1`.
The original edge-index C,R_0,R_1 formulas are explicitly reused inputs;
this review concerns the added clock composition, not re-admission of the
old K4 comparison grammar.

For T_n<=t<T_(n+1), summing u^t gives u^(T_n)*(1-u^(W_(n+1)))/(1-u).
Independence of consecutive waits and the entire original process permits
factorization as F(u)^n(1-F(u))/(1-u). Bounded observables ensure absolute
convergence for |u|<1; positive waits also make every formal coefficient
depend on finitely many n. The stated exact-time completion convention
matches the strict upper endpoint of the holding interval.

Conditioning on each original complete return path gives F(u)^L and leaves
its mark L mod 2 unchanged. Thus the two joint kernels are R_h(F(u)); no
independence between length and parity is assumed. Positive summation and
finite mean mu give E[tau|h]=mu*E[L|h] and E tau=4mu. Independence from the
entire joint process, not merely a current marginal, is necessary and
explicitly required.

For deterministic W=2, N(t)=floor(t/2). For geometric waits of parameter
1/2, the memoryless Bernoulli realization gives N(t)~Binomial(t,1/2).
The prefactor is 2/(2-u). Direct substitution of c_0=1,c_1=c_2=-1/2 gives
responses (1,1,-1/2) and (1,1/4,-1/8), respectively. Both mean waits are 2
and mean return durations 8, so the claimed mean-summary insufficiency is
an exact counterexample. In the deterministic clock all elapsed return
durations are even while the odd edge-transport mark still has mass 2/5;
the mark is correctly not retyped as elapsed-time parity.

The clocked decay bound is the expectation of the old bound at N(t).
No unproved substitution of t for n or exponential clock-rate conclusion
is made. Native clock selection, state-dependent waiting and calibration
remain genuinely open interfaces.

Validation grade: independent paper check and exact hand calculation of
the discriminating coefficients. The author's finite 32-order checker was
not rerun or counted as my independent computation. No historical Euler
suite or BRC world experiment was rerun and no proof kernel was used.

Reuse resolution: COMPOSE_APPLIED, standard renewal holding transform and
old joint positive path kernels. The new value is the source-specific
typed interface and counterexample, not a new general theorem/tool family.
It is distinct from the cited adversarial hold/skip detector horizon and
the old joint-duration marginal counterexample.

Shared control/source context is disclosed; reviewer did not construct
this result and is not clean-blind. The clock is an external ordered label,
not a native spatial axis or physical time law. This report grants no
Driver disposition, formal Task closure or parent completion.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
