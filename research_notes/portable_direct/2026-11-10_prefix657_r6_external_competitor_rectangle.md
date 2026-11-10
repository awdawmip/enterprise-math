# PREFIX-657-R6 — Exact exterior competitor rectangle for BRC sampling variance

Date: 2026-11-10 (Asia/Shanghai). Research role: TASK_RESEARCH (EM-DIRECT-836E3B), activity RA-21063825209E93F6ED82C60A.
Status: AUTHOR_DERIVED / EXACT_FRACTION_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Question and certified inherited frontier

Consider the frozen signed 189-layer two-informative-direction BRC survivor observer. Let mu=E[Y], H=E[Y²]/2, W=2H-mu² for the maximum Y of two independently Poissonized first-stop times. Its q-slot count variance is V_q(p,z)=q² W(p,z)-q mu(p,z). Actual slots are 12 and 24, with inherited analytic interpolation 12<=q<=24.

PREFIX-655/656 certify that on B=([3/20,1/6]×Z) ∪ (Z×[3/20,1/6]), where Z=[38911/262144,38913/262144], the only maximizers are (3/20,a) and (a,3/20), a=38911/262144. Their strict maximum value intervals are 47425.459<M_12<47425.460 and 192190.134<M_24<192190.135.

The question is whether an exterior admissible parameter point and then an entire nonzero-area rectangle give a larger q-slot variance than M_q.

## Theorem 657.1: certified point witness and uniform rectangle

Let P=(3/20,1/8), h=2^(-19)=1/524288, and C=[3/20-h,3/20+h] × [1/8,1/8+h]. Direct exact Fraction replay of the frozen 189-layer first-stop recurrence proves

- 98.334<mu(P)<98.335 and 366.012<W(P)<366.013.
- 51525.770<V_12(P)<51525.771.
- 208463.103<V_24(P)<208463.104.

Thus V_12(P)-M_12>4100.310, and V_24(P)-M_24>16272.968.

In fact, **for every real 12<=q<=24 and every (p,z) in C, V_q(p,z)>M_q**. At the two actual q values the uniform strict margins are

- V_12(p,z)-M_12 > 3338443629/1638400 > 2000;
- V_24(p,z)-M_24 > 32860522553/4096000 > 8000.

C is disjoint from B since 1/8+h<38911/262144. Hence the B-corners are not maximizers on B∪C. If the parent task's full parameter domain includes C, the B-corners are not global maximizers there either. That final inclusion condition must be checked from the frozen task publication before making an unconditional statement about the parent domain.

## Proof: finite exact witness

The frozen row recurrence starts from rows[0]={0:1}, duplicates child counts at each subsequent n and retains only dyadic-width-accepted states. Its integer predicate uses the strict condition 40(n+1) binom(n,k) (a/2^18)^k (1-a/2^18)^(n-k)>1, with integer bisection of the two crossings and strict width >1/4. The companion certificate checks intact survival through row 24, first rejection of two paths at row 25 and complete extinction at row 189. Survivors are finite polynomials s_n(u)=Σ_k rows[n,k]u^k(1-u)^(n-k).

For w(n,m)=binom(n+m,n)/2^(n+m+1), the exact existing kernel identities are

mu=Σ_n s_n(p)+Σ_m s_m(z)-Σ_{n,m} w(n,m)s_n(p)s_m(z);

H=Σ_n(n+1)s_n(p)+Σ_m(m+1)s_m(z)-Σ_{n,m}[(n+m+1)/2]w(n,m)s_n(p)s_m(z).

Evaluating them at P with arbitrary-precision rational arithmetic and computing q²(2H-mu²)-qmu yields the displayed strict thousandth enclosures. No finite floating-point test is a premise of these inequalities.

## Proof: two-coordinate error bounds

For each u∈[1/8,1/6], u(1-u)>=7/64. The PREFIX-643 binomial score lemma applies to every event survivor polynomial (with branch multiplicities retained):

|s_n'(u)|<=1/2 sqrt(n/[u(1-u)])<=sqrt(3008/7)<21, n<=188.

The nonnegative negative-binomial kernels give coefficient in [0,1] for each s_n in mu and coefficient in [0,n+1] for each s_n in H, hence for each coordinate i∈{p,z}:

|mu_i|<189·21=3969, |H_i|<21·189·190/2=377055.

Each stopped clock uses at most 189 unit-mean Poisson arrival intervals, so mu=E[max(Y_1,Y_2)]<=E[Y_1+Y_2]<=378. Thus

|W_i|=|2H_i-2mu mu_i|<2·377055+2·378·3969=3754674.

Therefore on [1/8,1/6]²,

|V_12,i|<144·3754674+12·3969=540720684,
|V_24,i|<576·3754674+24·3969=2162787480.

Every point of C can be reached from P by a coordinate path of ℓ1-length at most 2h. The resulting strict loss bounds are

V_12(P)-V_12(p,z)<(2h)540720684=135180171/65536,
V_24(P)-V_24(p,z)<(2h)2162787480=270348435/32768.

Subtract these from the strict witness advantages to obtain the stated margins.

Finally [V_q(p,z)-M_q]/q=q[W(p,z)-W(3/20,a)]-[mu(p,z)-mu(3/20,a)] is affine in q for each fixed (p,z)∈C. Endpoint positivity at q=12 and q=24 implies positivity for all real q in [12,24]. QED.

## Evidence, exact scope, next problem

BRC reuse: REUSE_APPLIED — signed survivor state, its preserved multiplicities and two-clock observer, moment kernel, score derivative and q-affine interpolation. p and z are statistical observer parameters, not native two-dimensional Enterprise space. The exact replay is of the frozen finite statistical model, not a new original 96-port native experiment.

The executable companion `PREFIX657_R6_COMPARATIVE_VARIANCE_WITNESS_CERTIFICATE.py` produced `ALL_CHECKS_PASS 4930` with Python standard-library integer and Fraction operations; the count includes inner bisection assertions. Complete exact comparison margins and moment intervals are in `PREFIX657_R6_RESULTS.json`.

Dependencies: PREFIX-643@ae7872ca18676397fcc0dd9424fb77e08928bee7 (score lemma); PREFIX-655@3dc372940c317cf540c96fc02b55284462549bac (local corner enclosures); PREFIX-656@5352d203d66148eb8262ff1c38d49d3f1700f510 (symmetric B maxima). Source data/recurrence follow PREFIX-654/655, science pin unchanged.

Next: resolve parent task's immutable *full* parameter domain; if it contains C, use C as the strict exclusion witness and certify further lower-z regions (including z=0 if allowed) with adaptive interval/Bernstein bounds. A preliminary floating mesh suggests higher edge candidates, but only this exact rectangle has been certified in this unit. Formal task CLAIM/Result/Review and independent admission have not been created.
