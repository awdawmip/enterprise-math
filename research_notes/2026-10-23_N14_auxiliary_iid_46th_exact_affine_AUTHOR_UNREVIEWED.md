# N=14 auxiliary iid sequential test — 46th exact affine interval (AUTHOR-LEVEL, UNREVIEWED)

Date: 2026-10-23. This is a **finite auxiliary iid model** proof, not a formal Enterprise Math Task Result/CLAIM, independent Research Driver review, Working Truth, P000 proof, or native BRC/X6/Heartbeat correspondence. Author context: EM-R5-02F1D7, TASK_RESEARCH; owner/CLAIM not verified (native control tasks returned `CONTROL_QUOTA`).

## Model and immutable inherited frontier

For independent observations, P=(3,1,20)/24 and Q=(2,2,20)/24, horizon N=14. Allow arbitrary history-dependent randomized stopping and decisions P or Q. Write E_P=P(decide Q), E_Q=Q(decide P), T_P=E_P[stopping time], T_Q=E_Q[stopping time], and V_14(alpha)=inf_{E_P,E_Q<=alpha}max(T_P,T_Q). Count state (n,a,b) records length, number of zeros, and number of ones; likelihood ratio Q/P=2^(a+b)/3^a.

Inherit the *author-level*, not independently admitted, 45th frontier at Enterprise Math Source commit `666fe2a4db4d675820f268c0368a862d05988321`: `research_notes/2026-10-23_N14_auxiliary_iid_45th_exact_affine_portable.py` (Git blob `66bb88e0432f845706493a0d3809b43b32d032e7`) and the accompanying 45th unreviewed research note. Fix exactly the stop sets in that script and **add stop-P at (11,6,1)** (the 45th endpoint); leave all other inherited decisions unchanged. At balance state B=(12,0,1), the inherited early-Q probability is s45=26392513263428113/41779200000000000. Also inherit
alpha45=5171815392886725797/14900301753911083008,
V45=193780295680165309/14551075931553792.

Fixed account snapshot: `GLOBAL_KNOWLEDGE_V1 main@c0063368858bfea93f5bda62c8f43039d03a1f0e`, P000 projection equals original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. The auxiliary model is not promoted to the native worldview.

## Exact theorem

Let K46=15422430942/577175, lambda_P=13750384104/577175=72+8*K46/9, lambda_Q=K46 and Gamma46=lambda_P+lambda_Q=29172815046/577175. Let eta46=577175/206948635470987264. **For every real 0<=delta<=eta46**,

    V_14(alpha45+delta) = V45 - Gamma46*delta.

The 46th endpoint is

    alpha46 = 5171815392928282397/14900301753911083008,
    V_14(alpha46) = 12401938792252912069/931268859619442688
                  ~ 13.317248466056181.

The supporting affine line is not attained beyond alpha46.

## Finite global dual certificate

Reference measure P. Bellman at state (n,a,b), with actions decide P, decide Q and (when n<14) continue, is the minimum of

    lambda_Q*2^(a+b)/3^a,
    lambda_P,
    1+sum_{symbol i} P_i*D(n+1,a+[i=0],b+[i=1]).

Exact rational evaluation of 680 count states and 1240 alternative-action differences finds 1238 strictly positive slacks and exactly two zero slacks: A=(8,7,1), continue=decide P; B=(12,0,1), continue=decide Q. Root exact value:

    D_root = 4440910098067979291250392543/252943578376871451033600
           = V45 + Gamma46*alpha45.

For **all**, including ordered-history-dependent randomized strategies, max(T_P,T_Q)>=T_P>=D_root-lambda_P*E_P-lambda_Q*E_Q>=V45+Gamma46*alpha45-Gamma46*alpha, since both multipliers are positive.

## Branch-faithful reachability and conditional continuations

A=(8,7,1) has eight nominal permutations (7 zeros and 1 one); explicit earliest-stop enumeration eliminates two prefixes through inherited stop-P state (6,6,0). **Six** are live, not eight. Independently propagated P and Q masses:

    p_A=1/8388608; q_A=1/71663616.

Conditional continuation vector (P error, Q error, additional P samples, additional Q samples), computed by exact 6-step suffix recursion and separately verified by explicit terminal-pruned enumeration:

    c_A=(21299/47775744, 743687/746496, 2286725/1990656, 13717/10368).

B retains 12 live ordered prefixes, masses

    p_B=48828125/725594112; q_B=48828125/362797056,

and suffix vector c_B=(63/64,1/144,9/8,13/12). Ordered branch provenance and separate exact positive P/Q weights are necessary: nominal counts alone are an unsafe BRC observer quotient. There is no signed/phase cancellation or native-dynamics identification here.

## Primal, balanced errors, and exact attainability

At A randomize early P with probability u in [0,1]; at B randomize early Q with probability s=s45+h46*u, retaining all other stopping decisions. Put

    D=p_A*cP_A=21299/400771988324352,
    W=q_A*(1-cQ_A)=2809/53496602689536,
    E=p_B*(1-cP_B)=48828125/46438023168,
    H=q_B*cQ_B=48828125/52242776064.

Changing u creates error delta (-D*u,+W*u); increasing s creates (+E*(s-s45),-H*(s-s45)). The unique balancing coefficient

    h46=(D+W)/(E+H)=92603569/1740800000000000

obeys 0<s45<=s45+h46<1. Therefore E_P=E_Q=alpha45+eta46*u, with eta46=-D+h46*E=W-h46*H>0. Exact forward probability propagation verifies

    T_P(u)=V45-Gamma46*eta46*u,
    T_P(1)-T_Q(1)=1805488412918399401/3725075438477770752>0.

T_P(0)>=T_Q(0), so affine interpolation proves T_P>=T_Q for all u. Thus these feasible policies attain the global dual lower bound on the entire claimed interval.

**Sharpness:** positive dual multipliers force both errors tight at a supporting-line equality; positive slack at every other reachable action forces only the two Bellman ties A/B to remain variable. A and B are prefix-incomparable (A has seven zeros, B zero), and equal count-state likelihood ratios make history-specific mixing equivalent to aggregate u,s. Equality of errors forces s=s45+h46*u, hence alpha=alpha45+eta46*u<=alpha46. Therefore the old support line is unattainable for alpha>alpha46; this does not rule out later new affine intervals.

## Exact replay, status and next problem

Main author checker: exact fractions; 680 Bellman states/1240 comparisons; 8 nominal A paths with 6 live; suffix recursion; five u values {0,1/4,1/2,3/4,1}; root dual/primal equality and full T_P/T_Q dominance. Second author-side checker: independent backward absorption over the four extreme (u,s) corners and zero mixed-interaction interpolation; five different u values; same exact endpoint. Both executed successfully locally. Neither is an independent Driver review; external mathematical novelty/prior-art analysis and native transfer remain open.

**Next dual-only candidate** K47=419904/17 at A47=(10,2,3), continue=decide Q (B remains continue=decide Q). The exact 47th interval is **not proved**. Compute live ordered prefix masses under the complete 46th endpoint stop tree, conditional risk/sample tuple, balanced B compensation, next endpoint, global dual and beyond-endpoint sharpness.

Global-Knowledge-Sync: main@c0063368 / GLOBAL_KNOWLEDGE_V1
