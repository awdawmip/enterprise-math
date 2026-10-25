# Stage110 exact Bellman affine interval — external ternary iid N=14

**Evidence status:** author-level rational finite-model proof; not native CLAIМ/Result, independent Driver review, or P000/X6/Heartbeat theorem.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main f54ad6814f1be98ffb6f7bc35a6ce332f6b61127 (P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc); Enterprise Math main read 5897ddc49f22fe2480961cd0fb5c5fdd47ff54de. Prior proof: research_notes/n14_aux_iid_affine_109_20261025/PROOF_STAGE109.md. Both repository pins are independent.

## Exact theorem

On the full ordered ternary iid history tree with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), stopping by depth 14, allow any randomized history-dependent stopping and decisions. Put eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau); define V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

Previous certified author endpoint:

alpha109 = 13084102500820187507/37682150988866125824
V109 = 1934432626777903782385/150728603955464503296.

**Theorem.** For every REAL 0<=delta<=18097625/9691911262568448,

    V14(alpha109+delta) = V109 - (1805151/962)*delta.

The right endpoint and its optimal value are

    alpha110 = 13084102571183753507/37682150988866125824,
    V110 = 1934432098641265410385/150728603955464503296.

The supporting affine line cannot be attained for any alpha>alpha110. Nothing beyond this support interval is asserted.

## Complete dual verification

For counts z=(n,a,b), where a,b record the first two outcome-symbol counts, the exact prefix P/Q likelihood ratio is R(z)=2^(a+b)/3^a. For any K,L>0, backward induction on all 680 states is

    H(z) = min( K*R(z), L, 1 + sum_j P[j]*H(child_j) ),

where continuation is forbidden at n=14. Against any policy on *ordered* histories,

    H(root) <= tP + L*eP + K*eQ <= max(tP,tQ) + (K+L)*alpha.

On the old A=(10,3,0) equality face, L=-185064/635+(21376/17145)*K. At

    K110 = 6497577/6734,
    L110 = 3069240/3367,
    Gamma110 = K110+L110 = 1805151/962,

the exact root dual is 8753048068398382030933/13174715337557409792, equal to V109+Gamma110*alpha109.

Of 1240 alternate-action comparisons on the 680-state tree, 1238 have a strictly positive gap, zero are negative, and exactly TWO are ties:

    A=(10,3,0), P-stop vs continue;
    E=(13,6,4), Q-stop vs continue.

The smallest positive gap is 71796655/11490066432. Choose the policy continuing at A,E and otherwise taking the unique minimizing action (D=(10,3,3) and C=(11,5,4) stop Q). For this *fixed* policy all gaps are nonnegative at BOTH prior K109=491857029/506348 and K110. Each gap is affine on the displayed K,L face, since fixed-policy values are affine in K and L; hence this selection stays minimizing at all intervening dual parameters. The count quotient is legitimate only for these Bellman conditional values; actual first-hit paths are separately retained below.

## First-hit history cone and exact moments

With A,E forced to continue for first-hit accounting and all other actions strict, E has 16254 *literal ordered* first-hit prefixes, exact P- and Q-masses

    P(E) = 37625/347892350976,
    Q(E) = 37625/247669456896.

Conditional on forced continuation at E, the suffix tuple (P-error, Q-error, additional P-time, additional Q-time, number of terminal ordered suffixes) is

    (7/8, 1/12, 1, 1, 3).

Thus immediate Q-stop at E replaces 16254*3=48762 complete ordered terminal histories. The old A first-hit data are

    P(A)=390625/5971968, Q(A)=390625/20155392;
    forced continuation suffix=(635/165888,10201/10368,7711/6912,1069/864,21).

A cannot lead to E because it would need 7 non-null symbol increments in only 3 sampling steps. D also cannot lead to E, needing 4 such increments in 3 steps. The possible count-ancestor C of E is already deterministically stopped Q. Therefore actual A- and E-first-hit cones are disjoint and randomization has no hidden product term.

At A, let u be the immediate-P-stop probability; at E, let w be the immediate-Q-stop probability, 0<=u,w<=1. The Stage109 right endpoint has u0=159859205042303/211315200000000 and w=0. Relative error changes are exactly

    eP-alpha109 = x*(u-u0) + zP*w,
    eQ-alpha109 = y*(u-u0) + zQ*w,

where

    x=-248046875/990677827584, y=65234375/208971104256,
    zP=37625/2783138807808, zQ=-37625/2972033482752.

Balancing BOTH errors imposes

    u(w)=u0+(327789/7043840000)*w,
    alpha(w)=alpha109+(18097625/9691911262568448)*w.

For every real 0<=w<=1, the probabilities are admissible: u(1)=159869038712303/211315200000000<1. The four moments are affine in w because the two randomization cones are disjoint. Direct rational root recurrences at endpoints and midpoint verify eP=eQ=alpha(w), tP=V109-Gamma110*(alpha(w)-alpha109) and tP>tQ. At w=1, tQ=115034069193316692605/9420537747216531456. Endpoint exact equalities plus the proved affine structure establish the theorem for *every* real w, not by numerical interpolation. Every used action minimizes the K110,L110 Bellman cost, attaining the global dual bound for the full history-dependent class.

## Sharpness against arbitrary ordered-history randomization

If this same support line were attained for alpha>alpha110, existence of a minimizing policy follows from compactness of the finite ordered-history randomized policy polytope. Strict positivity of K110,L110 forces eP=eQ=alpha and forces Bellman-minimizing actions at all positive-mass histories. Only A and E permit randomization. All histories reaching a given count state have one and the same P/Q likelihood ratio; averaging order-dependent tie-stop decisions with their first-hit weights therefore gives a common effective u at A and w at E under BOTH measures. Since those cones do not intersect, the displayed exact affine error equations are necessary; balance forces u-u0=(327789/7043840000)w, so alpha=alpha109+eta*w<=alpha110 as w<=1. Contradiction. Hence the right end is sharp.

## Reproducibility and limits

The included portable Fraction checker exhaustively verifies 680 Bellman states, the dual face, 1240 action inequalities at both endpoints, exact first hits, suffixes, affine compensation and endpoint/midpoint four moments. The included independent author-written top-down Bellman plus *literal history* DFS matched 16254 E-first hits, and scanned 952657/903895/952657 nodes at w=0/1/1/2 with identical moment fractions. Both actually ran; independent Driver review remains unperformed. Full expanded proof, raw console logs and SHA256 manifest are also present in the same-run downloadable research ZIP with SHA256 b29199a360515248ba3499e1b7feafb77da05d041a7cdfaf5d4ad7c9508a891a.

BRC reuse: explicit positive rational weighted branches and ordered provenance per definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json (source at the frozen EM read); count coarsening is demonstrated sufficient for iid Bellman only. This is REUSE_APPLIED plus adapted REUSE_EXECUTED, not a claim of native BRC-Shor computation or a typed P000 transfer.

**Next dual-only candidate** after stopping Q at E:

    K111=328788597439629/341261245318,
    L111=155234629311000/170630622659,
    Gamma111=91322550865947/48751606474,
    F=(4,0,2): competing Q-stop versus continue.

This is only a fixed-policy dual root; Stage111 primal interval, cones and sharpness remain open. Native current owner/claim/result unverified: em_control_tasks returned CONTROL_QUOTA; em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. GitHub author-side storage does not imply a Source claim or Driver acceptance.
