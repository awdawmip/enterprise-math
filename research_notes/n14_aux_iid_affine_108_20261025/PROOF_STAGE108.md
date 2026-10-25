# Stage108 — first two-multiplier Bellman face after B saturation (external iid, N=14)

**Scientific status: AUTHOR exact finite-model theorem, computationally verified by two separately implemented exact rational checks; not a native CLAIM/Result, Research Driver acceptance, P000 theorem, X6 or Heartbeat bridge.** Source snapshot: GLOBAL_KNOWLEDGE_V1 main@0fa426dd718b6912246848bdbbbe8977f757b8d1 (P000 projected canonical blob checked: 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc); predecessor Enterprise Math main@9713f10774d8c0a64c64fb2bd9888bec5679f40d, Stage107 proof and certificate.

## Theorem: entire real interval and sharp right support

Let full ordered histories of ternary iid observations have P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), and stopping time tau<=14. Arbitrary history-dependent randomized stop-and-decision policies are permitted. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha. At the Stage107 author-proved endpoint,

    alpha107=91588670614917102449/263775056922062880768
    V107=13541383133505475882195/1055100227688251523072

For **every real** 0<=delta<=eta108,

    V14(alpha107+delta)=V107-(409248885/206588)*delta,
    eta108=1457736575/2442361638167248896,
    alpha108=13084095824621807507/37682150988866125824,
    V108=1934483126570299962385/150728603955464503296.

The displayed Bellman support line is strictly unattainable for alpha>alpha108 (its right endpoint is sharp).

## Dual: genuinely two adjustable multipliers, not the previous pencil

Stage107 has K107=778896/767, L107=747576/767 and tied states A=(10,3,0) P/continue and B=(12,0,1) Q/continue. The Stage107 primal B Q-stop mixing probability has reached 1, while A P-stop mixing remains u0=1115808042440821/1479206400000000<1. Extending the old dual pencil L=72+8K/9 cannot extend a balanced primal family.

Choose the common Bellman policy that continues at A, stops Q at B, and chooses the unique other optimal action elsewhere. Its fixed-action costs are affine in (K,L). Enforcing the A P/continue tie while varying both multipliers gives the exact face

    L=-185064/635+(21376/17145)*K.

Decrease K from K107 along this face. The first additional Bellman gap to vanish occurs at

    K108=208946709/206588,
    L108=50075544/51647,
    Gamma108=K108+L108=409248885/206588,
    C=(11,5,4) with Q/continue tie.

B now strictly prefers immediate Q. Exhaustive rational enumeration finds 680 count states, 1240 nonselected-action comparisons, 1238 strictly positive gaps, no negative gaps, exactly the two action ties A P/C and C Q/C, and minimum strict positive gap 37821/1652704. A single fixed policy is dual feasible at the Stage107 and Stage108 vertices. Its action gaps are affine on the displayed face, hence nonnegative all along the connecting segment. The Stage108 endpoint dual root is

    D(root)=V107+Gamma108*alpha107.

For every ordered prefix with counts (n,a,b), the exact P-likelihood-normalized Bellman recurrence is

    R(n,a,b)=2^(a+b)/3^a = Q(prefix)/P(prefix),
    D(n,a,b)=min{ K*R(n,a,b), L, 1+sum_j P_j D(child_j) },

with continuation omitted for n=14. Backward induction remains valid for **all full ordered-history policies** even though the conditional optimal value depends only on the counts. It gives the universal bound

    D(root) <= tP + L*eP + K*eQ
            <= max(tP,tQ)+(K+L)*alpha.

## Ordered first-hit probabilities and conditional suffixes

Follow the strict Bellman decisions until first encountering A or C, maintaining every ordered prefix and its P/Q mass. The true first-hit totals are:

    A=(10,3,0): 120 ordered prefixes;
      P mass=390625/5971968, Q mass=390625/20155392.
    C=(11,5,4): 2258 ordered prefixes;
      P mass=28225/195689447424, Q mass=28225/92876046336.

Forced continuation at each tie and strict downstream decisions gives conditional tuples (P-error, Q-error, extra P-time, extra Q-time, terminal ordered suffix count):

    A: (635/165888,10201/10368,7711/6912,1069/864,21)
    C: (1493/1536,7/576,239/192,167/144,9)

Their ordered-history cones are disjoint: A at depth 10 has a=3,b=0, but C at depth 11 has a=5,b=4 and thus cannot be reached in one child step. C cannot precede A. Therefore there is no product mixing term; the four root moments are affine in the mixing variables.

Let u be the probability of deciding P rather than continuing at A. Let w be the probability of deciding Q rather than continuing at C. B deterministically decides Q. At (u,w)=(u0,0) the Stage107 endpoint is recovered. Exact branch-mass differences yield

    eP=alpha107+x*(u-u0)+zP*w,
    eQ=alpha107+y*(u-u0)+zQ*w,
    x=-248046875/990677827584,
    y=65234375/208971104256,
    zP=1213675/300578991243264,
    zQ=-197575/53496602689536.

Solving eP=eQ gives

    u(w)=u0+(67761451/4930688000000)*w,
    alpha(w)=alpha107+(1457736575/2442361638167248896)*w,
    0<=w<=1.

At w=1, u=159404052982303/211315200000000<1: C's Q-stop mixing saturates before A's P-stop mixing. All real w in [0,1] give valid randomized policies with eP=eQ=alpha(w). Their exact root moments at the two endpoints are:

    w=0:
    tP=13541383133505475882195/1055100227688251523072
    tQ=805267616960628807535/65943764230515720192

    w=1:
    tP=1934483126570299962385/150728603955464503296
    tQ=38346074856588751535/3140179249072177152

Both endpoints satisfy tP>tQ. By affinity this holds throughout the real interval. Every chosen action minimizes the Stage108 Bellman dual, so tP+L*eP+K*eQ=D(root). Consequently tP=D(root)-Gamma108*alpha(w) attains the universal lower bound everywhere in the entire real interval.

## Right-support sharpness, including arbitrary ordered-history randomization

Suppose the same support line could be attained at alpha>alpha108. Strict positivity of K,L forces eP=eQ=alpha and action optimality at every reached positive-mass history. Since the Bellman table has ties only A,C, arbitrary history-specific random decisions average to two numbers u,w∈[0,1] weighted by their P-first-hit mass: all histories at each count share likelihood ratio and forced suffix moments, and the two cones are disjoint. Therefore the same exact affine error identities hold. Balance enforces u(w) above and hence alpha=alpha107+eta108*w≤alpha108. Contradiction. The finite policy polytope is compact, so the optimum exists; this proves sharpness.

## Executed verification and limits

Author checker 1, bottom-up exact Python Fraction Bellman recurrence, verified both dual vertices, A-tie face, full 680 states and 1240 comparisons, true first-hit masses, forced suffixes, endpoint and midpoint four-moment equality, and next candidate. Author checker 2 used a separately written memoized top-down Bellman with literal full ordered-word DFS; it visited 1,022,824 / 1,022,824 / 995,728 nodes at w=0,1/2,1 and independently matched exact four moments in all three cases. Both local programs passed. Neither is an independent Research Driver review. Auxiliary iid evidence cannot be identified with native P000/X6/Heartbeat dynamics without an explicit verified bridge.

## Next mathematical question and authority

The next **dual-only** candidate is K109=491857029/506348 at D=(10,3,3), competing immediate Q, after C is fixed Q and A stays P/C on the A-tie line. Stage109 primal matching interval is NOT proved. Compute first-hit probabilities, disjointness/interaction, balanced mixing and next sharp endpoint.

GitHub actor awdawmip had repository push rights. Native em_control_tasks failed CONTROL_QUOTA; native em_session_start returned STATIC_READONLY_SCOPE_DENIED and operation_sent=false. No current native Owner, CLAIM, Result or independent Driver acceptance was verified. GitHub author publication does not imply those statuses; do not use Drive to bypass an authorization refusal.
