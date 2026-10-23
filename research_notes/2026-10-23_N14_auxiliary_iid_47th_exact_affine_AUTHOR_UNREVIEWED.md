# N=14 auxiliary iid sequential test — 47th exact affine interval (AUTHOR-LEVEL, UNREVIEWED)

Date: 2026-10-23. **Exact scope:** three-symbol iid finite-horizon sequential binary decision problem only, N=14. This is an author-side theorem/certificate, NOT a formally CLAIMed Enterprise Math Task Result, independently reviewed proof, Working Truth/Foundation result, or native BRC/X6/Heartbeat correspondence.

## Model and inherited author frontier

At each independent draw, P=(3,1,20)/24 and Q=(2,2,20)/24. Any history-dependent randomized policy stops by N=14 and declares P or Q. Define E_P=P(declare Q), E_Q=Q(declare P), T_P=E_P[stopping time], T_Q=E_Q[stopping time], and V_14(alpha)=inf_{E_P,E_Q<=alpha} max(T_P,T_Q). At a count state (n,a,b), n=length and a,b count symbols 0 and 1, so Q/P=2^(a+b)/3^a. Retain **ordered first-stop provenance**, not the raw multinomial count alone.

The preceding author-only N14-46 source is at immutable commit `9aab52edc7625781088c0bac031d8c9a23ed4c6b`, file `research_notes/2026-10-23_N14_auxiliary_iid_46th_exact_affine_AUTHOR_UNREVIEWED.md`. Reuse its complete endpoint stop tree; newly fix immediate P at (8,7,1), retain the previous stop-P and stop-Q sets and baseline probability of early Q at B=(12,0,1). Inherited exact constants:
- alpha46 = 5171815392928282397/14900301753911083008;
- V46 = 12401938792252912069/931268859619442688;
- s46 = 26392515485913769/41779200000000000.

## Main author theorem (fully specified)

Set K47=419904/17, lambda_P=72+(8/9)K47=374472/17, lambda_Q=K47, and Gamma47=lambda_P+lambda_Q=46728. Set eta47=1315625/71328803586048. Then for **every real** 0<=delta<=eta47,

    V_14(alpha46+delta) = V46 - 46728*delta.

The **47th exact endpoint** is

    alpha47 = 5171815667757082397/14900301753911083008
    V_14(alpha47) = 12401136154742512069/931268859619442688.

This *particular* supporting line cannot be attained beyond alpha47; the existence of later affine intervals is not excluded.

## Global Bellman dual certificate

Under reference measure P, minimizing T_P+lambda_P E_P+lambda_Q E_Q, use

    D(n,a,b)=min{ lambda_Q*2^(a+b)/3^a,
                  lambda_P,
                  1+sum_i P_i D(child_i(n,a,b)) },

where the final continuation action is permitted only for n<14. The first term is deciding P (Q-side error), the second deciding Q (P-side error). A complete exact Fraction evaluation of the 680 possible count states verifies all 1240 nonchosen-action differences: 1238 strictly positive and **exactly two ties**:
- A=(10,2,3): continue = declare Q;
- B=(12,0,1): continue = declare Q.

Every other alternative has positive slack. The root is

    D(0,0,0)=30233377587678603305015/1862537719238885376
            =V46+Gamma47*alpha46.

Thus for every randomized stopping policy, including arbitrary dependence on the ordered history,

    max(T_P,T_Q)>=T_P>=Droot-lambda_P E_P-lambda_Q E_Q
                     >=V46+Gamma47*alpha46-Gamma47*alpha.

This is a global feasible-set lower bound, not merely a comparison of two fixed policies.

## Ordered-history reach and conditional suffixes

A=(10,2,3) has 10!/(2!3!5!)=2520 nominal ten-symbol histories. Checking first stopping ancestors under the complete inherited policy eliminates **836**; exactly **1684** survive. First-stop pruned counts:
- (4,0,3):60; (5,0,3):60; (6,0,3):60; (7,0,3):45;
- (8,0,3):21; (8,1,3):422; (9,1,3):168.

The hypothesis-specific surviving weights are

    p_A=1315625/1719926784, q_A=1315625/483729408.

Starting at A and **continuing**, the exact conditional tuple (P-error,Q-error,additional P-samples,additional Q-samples) is

    c_A=(4095/4096, 1/20736, 585/512, 1885/1728).

B has 12 live ordered prefixes and

    p_B=48828125/725594112, q_B=48828125/362797056,
    c_B=(63/64,1/144,9/8,13/12).

Branch labels, earliest-stop status and both positive-rational hypothesis masses are mathematically required here. Naively counting all 2520 target strings as live erases an actual provenance residual. No signed-mass/phase cancellation or native residual-dynamics transfer is asserted.

## Constructive primal and equality with the dual

At A, declare Q early with probability u in [0,1]; at B, declare Q early with probability s. All other inherited decisions remain unchanged. Write

    D=p_A*(1-cP_A)=1315625/7044820107264,
    W=q_A*cQ_A    =1315625/10030613004288,
    E=p_B*(1-cP_B)=48828125/46438023168,
    H=q_B*cQ_B    =48828125/52242776064.

Changing u alone changes (E_P,E_Q) by (+D*u,-W*u), while changing s by Delta_s changes them by (+E*Delta_s,-H*Delta_s). Both errors remain equal with

    s=s46-h47*u,   h47=(D+W)/(E+H)=30733/192000000.

In particular, 0<s46-h47<=s<=s46<1, so all these policies are admissible, and

    E_P=E_Q=alpha46+eta47*u,
    eta47=D-h47*E=-W+h47*H=1315625/71328803586048>0.

A and B are prefix-incomparable (A already has two zeros, B zero), so the four risk/length observables vary affinely with u,s, with zero mixed interaction. Exact forward propagation and a separately written backward-absorption four-corner checker verify this at u=0,1/4,1/2,3/4,1 and independent rational points. Moreover,

    T_P(u)=V46-Gamma47*eta47*u,
    T_P(1)-T_Q(1)=1813242707510399401/3725075438477770752>0,

and T_P(0)>=T_Q(0) at the inherited endpoint. Affinity gives T_P>=T_Q on the full real interval. The strategy therefore attains the global Bellman lower bound, proving the theorem.

## Sharp endpoint and next research unit

Positive multipliers force both errors tight for equality on this supporting line, and strict Bellman slack forbids all other local alternatives at positive-probability reached states. The only free actions are at A and B; varying mixtures by ordered prefix does not change the four observables beyond their count-state averages because their likelihood ratios agree at each fixed state. Equal errors force s=s46-h47*u, hence alpha=alpha46+eta47*u<=alpha47 because 0<=u<=1. Thus this line cannot still be optimal and attained for alpha>alpha47.

A separate **post-endpoint affine Bellman slack scan**, with immediate Q fixed at A and with B still tied, finds the next dual-only candidate:

    K48=146772/7,  A48=(11,4,0), continue=declare P.

This is NOT a proof of the 48th interval. Next: compute exact live histories and conditional tail tuple at A48 under the fully stopped 47th endpoint tree, balancing at B, the next primal endpoint, global dual equality and sharpness.

## Evidence, limitations and fixed control provenance

The primary author script uses exact `fractions.Fraction`, all 680 Bellman states/1240 comparisons, pruning-aware forward propagation, explicit 2520 nominal A histories, exact suffix recursion and five randomized test points. A second author-only checker uses independent backward absorption, four corners, no mixed term and a symbolic affine next-K scan. Both passed; shared author context makes these **not** a Research Driver's independent review. There is no native BRC/X6/Heartbeat transfer, prior-art priority claim or approved Source Result.

Global-Knowledge-Sync snapshot fixed for this unit: `awdawmip/chatgpt-global-knowledge main@c0063368858bfea93f5bda62c8f43039d03a1f0e` (`GLOBAL_KNOWLEDGE_V1`); original P000 file blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matched the startup projection. Starting Enterprise Math source `main@2a3d794778d8bfbc205bf0b971a247754dc86869`. Connected identity: `awdawmip`. Native `em_control_tasks` returned `CONTROL_QUOTA` this run; owner/CLAIM were not verified. This is a standalone **author research note only**, not an attempt to claim a task or bypass native result admission.
