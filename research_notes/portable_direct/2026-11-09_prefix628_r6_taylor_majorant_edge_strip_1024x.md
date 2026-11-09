# PREFIX-628-R6 — 1024-fold wider BRC variance exclusion strip by exact Taylor majorants

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependencies: PREFIX-621 finite signed first-passage counts; PREFIX-624 central-unimodal survivor shape; PREFIX-626 exact edge witnesses; PREFIX-627 original strip. P000 V5 and the Heartbeat X6 observer/provenance scope are unchanged.

## Model and question

In the frozen two-direction signed-observer BRC model, each native action returns (i,+) with probability p_i/q, (i,-) with probability (1-p_i)/q (i=1,2), or neutral otherwise, q>=2 (actual slots q=12,24). Direction i stops when the PREFIX-621 anytime-confidence interval with beta=1/40 first attains diameter <=1/4. T_q counts all native actions until both directions complete; V_q(p1,p2)=Var(T_q). By sign symmetry use (p1,p2) in [0,1/2]^2.

**Theorem.** Let a=37/256, b=39/256, h=1/16384. For every q>=2 and every (p1,p2) in [0,h] x [a,b],

\[
\boxed{\partial_{p_1}V_q(p_1,p_2)<-119q^2.}
\]

Consequently, whenever 0<p1<=h, the strict bound

\[
V_q(p_1,p_2)<V_q(0,p_2)-119q^2p_1
\]

excludes that point from the global maximizers. This strip is 1024 times wider than PREFIX-627's width 2^-24. Native q=12 and q=24 gradient bounds are < -17136 and < -68544.

## Finite exact power-basis lemma

For n=0,...,188, let A[n,k] count signed words with k plus signs which have not yet satisfied the first-passage stopping rule after n informative observations. PREFIX-621 verifies the exact 189-layer finite recurrence. Thus

\[
s_n(p)=\sum_{k=0}^{n}A[n,k]p^k(1-p)^{n-k}
       =\sum_{j=0}^{n} c[n,j]p^j,
\]
\[
c[n,j]=\sum_{k=0}^{j}(-1)^{j-k}A[n,k]\binom{n-k}{j-k}.
\]

All c[n,j] are integers. For p in [0,h], the triangle inequality gives
\[
|s'_n(p)-s'_n(0)|\le R_n(h)
 :=\sum_{j=2}^{n} j|c[n,j]|h^{j-1}.
\]
Define R0(h)=sum_(n=0)^188 R_n(h), R1(h)=sum_(n=0)^188 (n+1)R_n(h).

The companion exact Python program reuses the verified PREFIX-621 recurrence, independently recomputes all power coefficients, checks 378 endpoint polynomial identities, and proves with one shared integer denominator 2^(14*187):
\[
\boxed{R0(2^{-14})<7/8,\qquad R1(2^{-14})<30}.
\]
For orientation only, R0=0.84428497215962069902496..., R1=29.70744386610769165437... . The strict comparisons use integers, not decimals.

## Moment derivation and uniform-gradient proof

By the PREFIX-622 independent Poisson-clock representation, write Y for the maximum of two informative completion times, mu=E[Y], H2=E[Y^2]/2, W=2H2-mu^2. The number of native trials satisfies
\[
V_q=q^2W-q\mu.
\]

Let w(n,m)=binom(n+m,n)/2^(n+m+1), z(n,m)=(n+m+1)w(n,m)/2. The finite moment formulas give:
\[
U(p_1,p_2):=\partial_{p_1}\mu
 =\sum_{n=0}^{188} \alpha_n(p_2)s'_n(p_1),
\]
\[
J(p_1,p_2):=\partial_{p_1}H2
 =\sum_{n=0}^{188} \beta_n(p_2)s'_n(p_1),
\]
where alpha_n=1-sum_(m=0)^188 w(n,m)s_m(p2) and beta_n=(n+1)-sum_(m=0)^188 z(n,m)s_m(p2). The complete negative-binomial sums give 0<=alpha_n<=1, 0<=beta_n<=n+1. The Taylor lemma therefore gives, uniformly in p2,
\[
|U(p_1,p_2)-U(0,p_2)|<7/8,\quad
|J(p_1,p_2)-J(0,p_2)|<30
\]
for 0<=p1<=h.

PREFIX-624 proves s'_n(p)>=0 and s_n(p) nondecreasing on [0,1/2]. Hence mu increases in both parameters; alpha_n and beta_n decrease with p2, so U and J decrease with p2. PREFIX-626 supplies exact rational endpoint witnesses:
\[
\mu(0,a)>87,\qquad U(0,b)>4,\qquad J(0,a)<182.
\]
Combining, throughout the rectangle,
\[
\mu>87,\quad U>4-7/8=25/8,\quad J<182+30=212.
\]
Therefore
\[
\partial_{p_1}W=2J-2\mu U
<424-2(87)(25/8)=-479/4<-119,
\]
and \(\partial_{p_1}V_q=q^2\partial_{p_1}W-qU<-119q^2\).
Integration in p1 proves the strict variance decrease. QED.

## Verification and use

Run Python 3 standard library script PREFIX628_R6_power_series_edge_strip_certificate.py in this directory alongside the existing SOURCE-published PREFIX621_R6_stochastic_tail_certificate.py. Observed: ALL_CHECKS_PASS, 189 rows, 378 coefficient endpoint identities, and strict exact-integer R0/R1 inequalities. Full computation evidence: PREFIX628_R6_RESULTS.json. The original 96-port native graph and upstream PREFIX-626 endpoint certificate were reused at their exact frozen statements, not re-executed. These are author-level model-internal results pending independent review and project admission.

Next research step: improve the power-coefficient triangle bound using signed Bernstein subdivision of U(p1,b), J(p1,a) on [0,1/256], or construct a rational interior sign-change witness for partial_1 V. This discriminates wider exclusion from a more complicated interior optimizer structure.

Canonical routes: docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, docs/PORTABLE_RESEARCH_PROTOCOL.md, research_priorities/research_method.json.
