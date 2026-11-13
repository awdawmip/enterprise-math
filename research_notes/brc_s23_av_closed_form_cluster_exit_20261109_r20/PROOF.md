# Closed-form positive-gap exit for rational-cluster circle observers

2026-11-09 | Enterprise Math / S23 auxiliary AV observable | author-side mathematical result; independent review pending.

Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged). Predecessor: Draft PR #1875, commit 5c2e92fd493e5f22bb47b563031bf3232f7cdb51, research_notes/brc_s23_av_three_level_cluster_o1_20261109_r19/PROOF.md. The theorem below concerns the scalar circle observer, not native Heartbeat X6/BRC dynamics.

## Theorem: exact first departure from original cluster cyclic order

Let q>=2, gcd(p,q)=1, 0<theta<1, theta=p/q+epsilon, epsilon!=0. For positive perturbation put k=p; for negative perturbation reflect the circle and put k=q-p. Let eta=abs(epsilon), let h be the inverse of k modulo q in {1,...,q-1}, and set z=q-h.

The existing ordered-cluster theorem certifies its original cyclic order for n>=q precisely when all its nominal inter-cluster gaps are strictly positive. Define the exact quantities

    T=(h+1/(q*eta))/q,
    t_max=ceil(T)-1,
    n_star=q*t_max+z.

For **every integer n>=q**, all nominal cluster-boundary gaps are strictly positive if and only if **n<=n_star**. If n_star>=q, the first failure is

    n_fail=n_star+1=q*t_max+z+1,
    n_fail is congruent to z+1 modulo q.

The congruence is modulo q: if h=1, z+1=q and the first failure is at residue 0, not residue q. If n_star<q, there is no positive-gap state in the domain n>=q and the first failing admissible n is q.

The ceiling convention handles exact equality: if T is an integer, t_max=T-1 because the original gap inequality is strict. After obtaining the modular inverse by Euclid in O(log q) arithmetic steps, the endpoint is evaluated with O(1) rational operations and comparisons. Full bit complexity includes the precision and encoding cost of eta.

When q=1, the single nominal cyclic wrap gap at n>=1 is

    G(n)=1-(n-1)*eta.

Its last positive-gap endpoint is n_star=ceil(1/eta), with first failing n=n_star+1.

## Proof

In the predecessor's source-residue-labelled cluster geometry, write n=a*q+b, 0<=b<q. Its exact boundary gap from source residue r to the next rational-base cluster is

    G_r(n)=1/q + [h-q*(a-1)-q*(1_{r>=z}+1_{r<b})]*eta.

For q>=2, {r>=z} is nonempty. The two indicator sets {r>=z} and {r<b} intersect exactly when b>z. Consequently the shortest of the q nominal boundary gaps is

    G_min(n)=1/q+[h-q*a-q*1_{b>z}]*eta.

Introduce t(n)=ceil((n-z)/q). If b<=z then t(n)=a, while if b>z then t(n)=a+1. Therefore

    G_min(n)=1/q+[h-q*t(n)]*eta,
    G_min(n)>0 iff t(n)<(h+1/(q*eta))/q=T.

Because t(n) is integral, t(n)<T iff t(n)<=ceil(T)-1=t_max. As

    ceil((n-z)/q)<=t_max iff n<=q*t_max+z,

the exact endpoint and first-failure congruence follow. For q=1 there is one cluster and the gap is the stated wrap gap. QED.

## Corollary for frozen S23 auxiliary observer

The predecessor's strictly certified interval is

    262204504569236716045286/10^24 < theta
    theta < 262204504569236716045287/10^24.

With p/q=16/61 and epsilon<0, the reflected numerator is k=45, inverse h=19, z=42. Evaluating T against *both rational endpoints* shows 3<T<4, so t_max=3 and

    n_star=61*3+42=225,
    n_fail=226, n_fail mod 61=43.

The exact shortest gaps satisfy

    G_min(225)=164*theta-43>0,
    G_min(226)=225*theta-59<0.

The initial crossing magnitude is x=59-225*theta>0. With within-cluster gap delta=16-61*theta, the same certified interval proves 0<delta-x<x<delta. By the predecessor's independently proved local first-swap theorem, the risk increment at n=226 is delta-x=164*theta-43.

The original *ordering* changes at n=226. This should not be confused with a change of the scalar risk slope: the pre-existing independently generated affine table has that same slope through n=292. The explicit endpoint formula eliminates the doubling/binary search requested in the preceding NEXT_TASK.

## Exact finite checks and scientific scope

The accompanying VERIFY_CLOSED_ORDER_EXIT.py tests the formula against a separately enumerated q-residue minimum gap on 2,120 rational parameters and 94,690 parameter/index pairs, including both signs and q=1. It checks 2,120 strict first-failure witnesses and the two enclosing S23 parameter endpoints using Fraction, without floating-point decisions. An optional cross-check with the pre-existing AFFINE_RUNS_2M.tsv tests the scalar slope at n=225,226,292, but remains a *regression comparison*, not a new proof of that legacy table. RUN_EVIDENCE.txt contains the actual local execution output.

General claim: symbolic consequence of the predecessor's exact nominal-gap identity, for the stated rational-cluster circle observer. Scientific-input pin is unchanged. Formal Source CLAIM, independent review, Result/Review acceptance and an X6/BRC physical bridge are separate future work.
