# PREFIX-627-R6 — Explicit certified BRC variance edge-exclusion strip

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_ARITHMETIC_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Researcher: EM-DIRECT-E79758 / TASK_RESEARCH. Activity: RA-451D03649AC0EC6C5611A48B.

## Objective and model

PREFIX-626 proves a strictly negative inward variance gradient along a BRC signed-label observation-model edge. We now give a **quantitative, uniform, nonzero-width two-parameter exclusion strip** for global variance-maximizer search, rather than only a qualitative continuity argument.

Preserve the frozen BRC signed-observer carrier. Each native action returns label $(i,+)$ with probability $p_i/q$, label $(i,-)$ with $(1-p_i)/q$ for $i=1,2$, and otherwise a neutral label, where $q\ge2$ (actual slots: $q=12,24$). Let $T_q$ count original actions until both direction-specific anytime-confidence intervals (beta $1/40$) first have diameter at most $1/4$. The admissible parameter closure is $(p_1,p_2)\in[0,1/2]^2$. Native BRC model provenance and P000 are those of PREFIX-610/621/626, with original 96-port graph frozen, not rerun.

Write $I=[37/256,39/256]$, $h=2^{-24}=1/16777216$, and $V_q(p_1,p_2)=\operatorname{Var}(T_q(p_1,p_2))$.

## Theorem (uniform inward exclusion of positive-width strip)

For every $q\ge2$, $p_2\in I$, and $0\le p_1\le h$,

$$
\boxed{\partial_{p_1}V_q(p_1,p_2)<-19q^2.}
$$

In particular, for $0<p_1\le h$,

$$
\boxed{V_q(p_1,p_2)<V_q(0,p_2)-19q^2p_1.}
$$

Thus no point in $(0,h]\times I$ is a global maximizer over the full parameter square: the point $(0,p_2)$ in the same horizontal section has strictly higher variance. The actual slot gradient bounds are $<-2736$ for $q=12$ and $<-10944$ for $q=24$, in native-action-count variance per unit $p_1$.

## Proof

The corrected PREFIX-621 signed first-passage survivor law has an exact finite horizon $M=189$: $s_n(p)=0$ for $n\ge M$. For $0\le n<M$, $s_n(p)$ is the probability of not yet satisfying the direction-specific stopping rule after $n$ informative observations. Each $n$-symbol signed word survives or does not, and so

$$
s_n(p)=\sum_{k=0}^n a_{nk}\binom nk p^k(1-p)^{n-k},
\quad 0\le a_{nk}\le1.
$$

Here $a_{nk}$ is the fraction of the $\binom nk$ words with $k$ plus signs that survive. The Bernstein forward-difference derivative formulas yield uniformly on $[0,1]$

$$
0\le s_n\le1,\quad |s_n'|\le n,\quad |s_n''|\le 2n(n-1).
$$

The last bound uses $|a_{n,k+2}-2a_{n,k+1}+a_{nk}|\le2$.

Set

$$
w(n,m)=\binom{n+m}{n}2^{-(n+m+1)},\qquad
z(n,m)=\tfrac12(n+m+1)w(n,m).
$$

The exact negative-binomial identities are $\sum_{m\ge0}w(n,m)=1$ and $\sum_{m\ge0}z(n,m)=n+1$. Each finite truncated sum with nonnegative $s_m$ is bounded above by the corresponding infinite sum.

Let $Y$ be the maximum of the two unit-rate independent informative-clock stopping times in the exact PREFIX-622 Poisson representation, $\mu=E[Y]$, $H=E[Y^2]/2$, and $W=2H-\mu^2$. Their finite formulas are

$$
\mu=\sum_{n<M}s_n(p_1)+\sum_{m<M}s_m(p_2)
-\sum_{n,m<M}w(n,m)s_n(p_1)s_m(p_2),
$$

$$
H=\sum_{n<M}(n+1)s_n(p_1)+\sum_{m<M}(m+1)s_m(p_2)
-\sum_{n,m<M}z(n,m)s_n(p_1)s_m(p_2).
$$

For fixed $p_2$, each coefficient of $s_n(p_1)$ in $\mu$ belongs to $[0,1]$, and its coefficient in $H$ belongs to $[0,n+1]$. Consequently, putting

$$
A=\sum_{n<M}n=17766,\qquad
B=\sum_{n<M}2n(n-1)=4429656,\qquad
D=\sum_{n<M}2n(n-1)(n+1)=631225980,
$$

we obtain, throughout the complete parameter square,

$$
|\partial_1\mu|\le A,\quad |\partial_1^2\mu|\le B,\quad
|\partial_1^2H|\le D,\quad0\le\mu\le2M=378.
$$

Differentiating $W=2H-\mu^2$ twice gives

$$
|\partial_1^2W|\le 2D+2A^2+4MB=5242533408.
$$

The exact time-change theorem of PREFIX-622 states $V_q=q^2W-q\mu$ for all $q\ge2$. Hence

$$
|\partial_1^2V_q|
\le q^2(5242533408+4429656/q)
\le q^2L,\quad L=5244748236.
$$

The **already certified** PREFIX-626 exact rational inward witness states

$$
\partial_1V_q(0,p_2)<-332q^2\quad(p_2\in I,\ q\ge2).
$$

The fundamental theorem of calculus therefore yields for $0\le p_1\le h$,

$$
\partial_1V_q(p_1,p_2)<q^2(-332+Lp_1)
\le q^2(-332+Lh).
$$

Exact integer arithmetic checks $L=5244748236<313\cdot16777216$; more precisely,

$$
332-L/16777216=81321869/4194304>19.
$$

The first asserted inequality follows. Integrating over $[0,p_1]$ proves the strict variance decrease for $p_1>0$. QED.

## Exact verification, scope, and next unit

The standard-library Python certificate PREFIX627_R6_uniform_inward_strip_certificate.py computes all sum identities, Hessian constants, and margins using integers/Fraction. Local output: ALL_CHECKS_PASS 16. Corresponding exact values are in PREFIX627_R6_RESULTS.json. The certificate checks the new universal bound and implication from PREFIX-626; this run did not rerun PREFIX-626's full 357260-step threshold certificate or PREFIX-565 original native 96-port graph. Evidence status is author proof and exact-bound arithmetic, pending independent mathematical review/admission.

The exact explicit positive-area strip enables safe subdivision pruning. Next: exploit the source first-passage word coefficients to replace the crude universal Bernstein $|s_n''|$ bound by a narrower parameter-specific envelope, enlarge the verified exclusion from $p_1\le2^{-24}$ toward $p_1\le1/256$, then compare remaining cells with the edge candidate. Test any rational interior challenger by exact formula before extending a global conjecture.

Provenance: immutable science pin above; current project P000, ACTIVE worldview, RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context and portable protocol; source-published PREFIX621_R6_stochastic_tail_certificate.py, PREFIX-622 moment identity and PREFIX626_R6_boundary_normal_variance_certificate.py. No P000, Working Truth, Foundation, CLAIM, Result or Review status is changed by this research note.
