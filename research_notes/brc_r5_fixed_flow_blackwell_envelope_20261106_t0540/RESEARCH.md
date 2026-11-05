# R5: an exact fixed-flow Blackwell envelope and a rational global repair

Date: 2026-11-06 (Asia/Shanghai). Research status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / PORTABLE_ONLY.

## Mother target and inherited source

R5 asks for a strictly positive rational finite P/Q stopping tree with equal four-observer FULL_HIST and seedless LR convex hulls but different actual real-behavior images. Frozen scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e. This is the auxiliary likelihood-ratio/BRC observer, *not* a claim about native Heartbeat X6 dynamics.

Inherit the exact delta=1/4 tree and its affine stopped-ratio lift from research_notes/brc_r5_scalar_nonlumpability_gate_20261106_t0343/RESEARCH.md (commit 57f7d654e5dd002567e0b0d333937e6e38f3b4cb). Inherit the rational-stationarity method from research_notes/brc_r5_rational_stationary_20261106_t0440/RESEARCH.md (commit 5552ea78713cfcbaada5f6601fccc31e7aedbe65). The earlier author-side equal-hull proof is cited at EM fed51a882c12831a889cd5437da5d1dc564fd673, not re-executed here.

Let g be root continuation, 0<=u_0,u_1<=g<=1, and X_j time-3 continued Q masses at the three ratio keys j=0,1,2, bounded 0<=X_j<=V_j. The central history masses are A=u_0/10, B=9u_1/40, V_1=A+B, and alpha=47/180, beta=67/162, d=beta-alpha=247/1620. FULL uses independent historical continuations and central terminal coefficient J, with

    J_lo=max(alpha X_1, beta X_1-d A),
    J_hi=min(beta X_1, alpha X_1+d B).

seedless LR uses J_LR=X_1(alpha A+beta B)/(A+B) for A+B>0 and J_LR=0 otherwise. Both stopping-time coordinates are independent of J. All other stopped-ratio masses are J-independent, while

    (M_{1/10}, M_1, M_{19/10}) = (m_-,m_0,m_+) + J(1,-2,1).

The seven distinct stopped-ratios are R={1/10,1/2,3/4,1,5/4,3/2,19/10}. Every row of the inherited probability kernel is strictly positive and has the required LR mean.

## Theorem 1: nested terminal declaration zonotopes

Fix *any* feasible (g,u_0,u_1,X_0,X_1,X_2) and vary J over [J_lo,J_hi]. Let Z(J) denote all attainable (e_P,e_Q) with unrestricted P/Q declarations at the seven stopped-ratio keys, and write s_rho=e_P+rho e_Q. Then for every rho in R,

    L_rho(J) <= s_rho <= U_rho(J),
    L_rho(J)=1+sum_{r>rho}(rho-r)M_r(J),
    U_rho(J)=1+sum_{r<rho}(rho-r)M_r(J),

and these fourteen halfspaces characterize Z(J) exactly. Their J-slopes are

    dL_rho/dJ=-c_rho,   dU_rho/dJ=c_rho,
    c_rho=min(rho-1/10,19/10-rho)>=0.

Consequently, whenever J_1<=J_2 in the feasible interval,

    Z(J_1) subset Z(J_2),

including all mass-zero and action-probability boundary cases. Indeed s_rho=1+sum_r(rho-r)ell_r, 0<=ell_r<=M_r; the lower/upper bounds follow by choosing ell_r at 0 or M_r according to the sign of rho-r. The edge directions of this planar zonotope are (-r,1), so exactly the fourteen listed supporting lines describe it. The varying mass triplet (1,-2,1) yields the stated slopes by direct calculation, proving the inclusion.

In experiment-comparison language, increasing J adds a mean-preserving spread at likelihood-ratios 1/10,1,19/10, enlarging the achievable binary declaration-error region for this *fixed continuation flow*. No additional probabilistic limit is used.

## Theorem 2: eliminate J from FULL membership by six-variable linear inequalities

At a fixed six-variable flow the FULL union over every legal historical J is exactly

    union_{J_lo<=J<=J_hi} Z(J)=Z(J_hi).

Put p=beta X_1 and q=alpha X_1+dB. Since J_hi=min(p,q) and each L_rho decreases and each U_rho increases in J,

    L_rho(J_hi)=max(L_rho(p), L_rho(q)),
    U_rho(J_hi)=min(U_rho(p), U_rho(q)).

The notation L_rho(p), etc. is an affine algebraic *evaluation* and is not required to be a standalone probability experiment. Therefore a target W=(e_P,e_Q,T_P,T_Q) lies in O4(FULL_HIST) **if and only if** there exist six real variables (g,u_0,u_1,X_0,X_1,X_2) satisfying:
(1) 0<=g<=1, 0<=u_i<=g, 0<=X_j<=V_j;
(2) the two inherited affine time equalities T_P,T_Q; and
(3) for every rho in R, the **four linear inequalities**

    L_rho(p)<=e_P+rho e_Q,    L_rho(q)<=e_P+rho e_Q,
    e_P+rho e_Q<=U_rho(p),    e_P+rho e_Q<=U_rho(q).

These are 28 rational linear inequalities, so FULL membership has an exact six-variable rational linear-programming certificate. Proof of sufficiency: pick J=J_hi and use the fourteen valid zonotope inequalities to reconstruct ell_r and legal declarations. The central split bounds are always consistent because 0<=X_1<=A+B implies J_lo<=J_hi. Necessity follows from the preceding inclusion. This removes a full-history search coordinate without approximating real behavior.

## Theorem 3: exact fixed-flow information premium

For A+B>0, the shared LR coefficient lies between J_lo and J_hi, and

    J_hi-J_LR = d*min(A X_1, B(A+B-X_1))/(A+B).

At A+B=0 this premium is zero. Proof: split at X_1=B. If X_1<=B, J_hi=beta X_1, so the difference equals d A X_1/(A+B). If X_1>=B, J_hi=alpha X_1+dB, giving d B(A+B-X_1)/(A+B). These meet at X_1=B. Therefore, for every rho in R, the exact expansion of both support bounds from the LR fixed-flow declaration region to the FULL fixed-flow envelope is

    L_rho(J_LR)-L_rho(J_hi) =
    U_rho(J_hi)-U_rho(J_LR) = c_rho*(J_hi-J_LR).

When A,B>0 and 0<X_1<A+B, the local premium is strictly positive for 1/10<rho<19/10. Its maximum over 0<=X_1<=A+B is attained at X_1=B with value d AB/(A+B).

## Exact witness and a global repair: the flow distinction matters

Fix g=u_0=u_1=1, (X_0,X_1,X_2)=(0,9/40,0). Then J_LR=33/400, J_hi=67/720, premium J_hi-J_LR=19/1800. At J_hi choose time-3 central history continuations z_{0,1}=0,z_{1,1}=1, with both outside-central continuations zero. Declare P at ratios 1/10 and 1/2, and Q elsewhere. The exact four-observer FULL point is

    W=(e_P,e_Q,T_P,T_Q)
     =(2959/3600,31/72,129/40,129/40).

At this *same flow* the FULL rho=1 statistic is e_P+e_Q=501/400, whereas every seedless LR declaration at this flow satisfies e_P+e_Q<=1243/1000. The local difference is exactly 19/2000.

However **the same W is globally seedless-LR reachable by changing the flow**. Take g=u_0=u_1=49/50, (X_0,X_1,X_2)=(0,53/200,0), so the common central time-3 continuation is z_1=530/637 and J=J_LR=583/6000. Use P-declaration probabilities at stopped ratios

    t_{1/10}=1,    t_{1/2}=6602/6615,    t_1=296/12975,

with t_r=0 at the other stopped ratios. All probabilities lie in [0,1], and direct exact mass sums give precisely W. This simultaneously verifies a nonzero *fixed-flow* information defect and an exact *global* flow repair at the identical four-observer target.

## Verification, scope and next unit

VERIFY.py executes 720 seeded rational six-flow profiles and 5,040 exact ratio halfplane checks, checking the feasible J interval, mass normalization and LR mean, the nested support slopes, the p/q endpoint elimination, and the premium identity. It also checks both complete policies and their exact shared W using Python's Fraction arithmetic. Output is recorded in EXACT_OUTPUT.txt. The universal fixed-model identities are justified analytically above; the finite checks are regression evidence. This run supplies an exact membership witness at one informative W, not a global image-equality theorem or an R5 mother counterexample.

Next: exploit the six-variable FULL linear lift to choose candidate rational W; then solve the true **global** LR fiber over all six flows, using the earlier seven-variable K(W) plus exact stationary-face extrema or an explicit rational/quadratic-algebraic LR reconstruction. Fixed-flow support gaps alone must not be classified as global image gaps. Independent mathematical review and formal Source claim remain pending.
