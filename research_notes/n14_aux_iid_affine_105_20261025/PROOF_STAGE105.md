# Stage105 exact minimax affine interval — external iid N=14

Evidence: **AUTHOR exact rational finite-model proof**, two independent author-side implementations; no independent Research Driver admission, native CLAIM, Result freeze, or native P000/X6/Heartbeat transfer. Frozen predecessor: Stage104 author proof and certificate at enterprise-math main (research_notes/n14_aux_iid_affine_104_20261025). Account-level input snapshot: awdawmip/chatgpt-global-knowledge main@4292cf9480b01650cccdda42b811dd2de3057aec. P000 is untouched. This is an *external auxiliary* probability model; it is not a native lower-dimensional spatial ontology.

## Theorem

Let the observation alphabet be {0,1,2}, with iid probabilities
P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). A randomized test can depend on the entire **ordered** observation history, decides P or Q and stops by time N=14. Set eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau; V14(alpha) is the infimum of max(tP,tQ) over tests with both errors <=alpha.

At the proven Stage104 author endpoint,

    alpha104 = 646648471503178867/1862537719238885376
    V104 = 6009287153480025269/465634429809721344

the exact optimum for **every real** 0<=delta<=eta105 is

    V14(alpha104+delta) = V104 - gamma105 * delta
    eta105 = 348715675/4850358643851264
    gamma105 = 4323250440/1992661.

The endpoint and its value are

    alpha105 = 38038153259411651/109561042308169728
    V105 = 353483207227801957/27390260577042432.

The support line with slope -gamma105 is strictly unattainable beyond alpha105.

## 1. Bellman dual certificate for all ordered histories

For a count state z=(n,a,b), where a and b count occurrences of symbols 0 and 1, the exact likelihood ratio is Q(prefix)/P(prefix)=2^(a+b)/3^a. Set

    K=lambda_Q = 2212824096/1992661
    L=lambda_P = 2110426344/1992661 = 72+8*K/9.

Define D(n,a,b) backwards as the minimum of:

    decide P: K * 2^(a+b)/3^a
    decide Q: L
    continue: 1+P0*D(n+1,a+1,b)+P1*D(n+1,a,b+1)+P2*D(n+1,a,b),

with continuation absent at n=14. The finite recursion is a dual bound for *every full ordered-history strategy* by backward induction (even if the strategy itself depends on order). Exact rational enumeration gives:

    count states = 680
    non-selected action comparisons = 1240
    strict positive gaps = 1238
    negative gaps = 0
    exact ties = 2
    min strictly positive gap = 2872871/430414776
    D(0,0,0) = 41816487905082472657156687/54579504031709949591552.

The only ties are A=(8,5,1), choose P versus continue, and B=(12,0,1), choose Q versus continue.

For every strategy,

    D(root) <= tP + L*eP + K*eQ
            <= max(tP,tQ)+(L+K)*alpha

when both errors are <=alpha. Exact equality at the Stage104 endpoint is

    D(root)=V104+(L+K)*alpha104.

The selected policy follows the strict Bellman action elsewhere, continues at A and B as its base. The costs of this fixed policy and the nonselected-action gaps are affine in K along L=72+8K/9. They are nonnegative at both K104=4881384/4373 and K105=2212824096/1992661; hence this exact action policy remains dual optimal at every K between the endpoints. The former Stage104 tie at (11,8,3) selects P after Stage104.

## 2. True ordered first hits and continuation branches

Enumerate *genuinely reached* ordered words under the unique strict Bellman actions before either tied state; positive exact P/Q weights are accumulated, not inferred solely from multinomial counts.

    A=(8,5,1): 112 reached words; P=175/1769472; Q=175/6718464.
    B=(12,0,1): 12 reached words; P=48828125/725594112; Q=48828125/362797056.

Forced continuation at each tied state and then strict successor actions yields conditional tuples

    (P-error, Q-error, extra P-time, extra Q-time, terminal suffix words):

    R_A=(229681/47775744, 182623/186624, 86903/73728, 42763/31104, 105)
    R_B=(63/64, 1/144, 9/8, 13/12, 5).

Early stopping at A truncates 112*105=11760 complete terminal-history paths. The two tie cones are disjoint: a path reaching A already has five copies of symbol 0, whereas B has zero even later at n=12; B is deeper than A and cannot precede A. There are consequently no u*s interaction terms.

This is positive-rational, ordered-provenance BRC branch-mass reuse, not a theorem of native X6 dynamics or a replacement for original Heartbeat BRC arithmetic.

## 3. Exact primal family for every real cap

At the Stage104 endpoint, continue at A; decide Q at B with probability

    s104 = 4103853056103079/5222400000000000.

Let u in [0,1] be probability of deciding P early at A, and s the probability of deciding Q early at B. Exact error increments relative to Stage104:

    eP=alpha104+x*u+e*(s-s104)
    eQ=alpha104+y*u+f*(s-s104)

    x=-40194175/84537841287168
    y=700175/1253826625536
    e=48828125/46438023168
    f=-48828125/52242776064.

Solving eP=eQ gives

    s(u)=s104+c*u
    c=849554069/1632000000000
    s105=s(1)=241563037007287/307200000000000
    alpha(u)=alpha104+eta105*u
    eta105=348715675/4850358643851264.

Since eta105>0 and 0<s104<s105<1, this realizes *every* real alpha in the claimed interval via a legal randomized full-history test.

At u=0 the exact ordered-root tuple (eP,eQ,tP,tQ) is

    (alpha104, alpha104,
     6009287153480025269/465634429809721344,
     5709042008510518661/465634429809721344).

At u=1 the tuple is

    (alpha105, alpha105,
     353483207227801957/27390260577042432,
     111940980237083111/9130086859014144).

Exact rational inequalities give tP>tQ at both endpoints, and hence everywhere by affine dependence on u, justified by the disjoint cones. Each chosen local action is a Bellman minimizer. Therefore tP+L*eP+K*eQ=D(root), so max(tP,tQ)=tP=D(root)-(L+K)*alpha and the universal dual bound is attained, proving the theorem for all real delta, not merely sampled values.

## 4. Sharp right endpoint

Suppose the same support line were attained at alpha>alpha105. Equality in the global bound forces eP=eQ=alpha (since L,K>0), tP=max(tP,tQ), and a Bellman-minimizing decision at every reached ordered prefix. Only A and B have Bellman ties. All prefixes reaching either count state have the same likelihood ratio and identical conditional continuations; even an arbitrary order-dependent randomization has the same global moments as first-hit-mass-weighted means u,s in [0,1]. Because the two cones are disjoint, the error-balance equations above remain exact. They force alpha=alpha104+eta105*u<=alpha105. Contradiction. The finite randomized-strategy feasible set is compact and an optimum exists. Therefore this support line is strictly unattainable to its right.

## 5. Exact cross-check and research boundary

The author-side bottom-up Fraction program recalculated every Bellman gap, true first hits, forced continuation suffixes, endpoint/midpoint moments, positive dual pencil and the next candidate. Separately written top-down cached Bellman plus ordered-word DFS visited 1,013,272 nodes at u=0, 995,800 nodes at u=1 and 1,013,272 nodes at u=1/2, and exactly reproduced all four root observables. No floating point and no grid interpolation were used. Both are **author checks**, not clean independent Driver review. Full source programs, raw logs, JSON certificate and hash manifest are in the downloadable local reproducibility package.

After fixing A to stop P, the **next dual-only** candidate is K106=107892/101 at (11,5,4), with continue becoming tied to the preceding stop action. The Stage106 primal theorem is **not yet proved**. The proof is scoped strictly to the external iid finite model and does not imply native P000/X6/Heartbeat transfer. Native control read returned CONTROL_QUOTA and native session registration returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false), so no active Owner/CLAIM/native Result/Driver acceptance was established.