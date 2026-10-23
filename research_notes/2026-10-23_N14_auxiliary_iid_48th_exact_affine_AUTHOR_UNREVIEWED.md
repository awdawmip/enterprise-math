# N=14 auxiliary iid sequential test: 48th exact affine interval (AUTHOR-LEVEL, UNREVIEWED)

**2026-10-23.** A complete author-side exact finite-model argument, not a native Enterprise Math CLAIM/Result, independent Research Driver review, Lean formalization, or correspondence to native BRC/X6/Heartbeat. Source inputs: global knowledge snapshot `awdawmip/chatgpt-global-knowledge@7a56e3a5a31c6af97f47a09befb54ae4443c9b41`; inherited immutable N14-47 author proof at `awdawmip/enterprise-math@af1ac6a8dc1f960a84449366b5ae9cafbae6b7d8:research_notes/2026-10-23_N14_auxiliary_iid_47th_exact_affine_AUTHOR_UNREVIEWED.md`.

## Exact question and theorem

Given independent samples with distributions P=(3,1,20)/24 and Q=(2,2,20)/24 over three symbols, any randomized history-dependent stopping-and-decision policy must stop by N=14 and choose P or Q. Let E_P=P(decide Q), E_Q=Q(decide P), T_P=E_P[stopping time], T_Q=E_Q[stopping time]. Define V14(alpha) as the infimum of max(T_P,T_Q) over policies with E_P,E_Q <= alpha. An exact count state is (n,a,b), where n samples have been drawn and a,b count outcomes 0 and 1; Q/P likelihood ratio equals 2^(a+b)/3^a. Preserve the ordered earliest-stopping history, not merely the nominal multinomial multiplicity.

Inherited: alpha47=5171815667757082397/14900301753911083008; V47=12401136154742512069/931268859619442688; balancing probability s47=8795275995037923/13926400000000000 at B=(12,0,1).

**Theorem.** With eta48=30078125/50524569206784 and Gamma48=277740/7, **for every real** 0<=delta<=eta48,

    V14(alpha47+delta) = V47 - Gamma48*delta.

Thus alpha48=5171824538157082397/14900301753911083008, and V14(alpha48)=12379139146742512069/931268859619442688. This *specific* global supporting line is sharp: it cannot remain attained at any alpha>alpha48; possible subsequent segments are not excluded.

## Global Bellman lower bound

Put K48=146772/7, lambda_Q=K48, lambda_P=72+(8/9)K48=130968/7, Gamma=lambda_P+lambda_Q=277740/7. Under reference probability P, let

    D(n,a,b)=min{lambda_Q*2^(a+b)/3^a, lambda_P,
                 1+sum_i P_i D(child_i(n,a,b))},

omitting continuation at n=14. The terms respectively correspond to immediate decide P, immediate decide Q, continue. The exact rational dynamic-programming minimization covers **all 680 count states and 1240 nonchosen actions**: 1238 nonchosen differences are strictly positive, precisely two are zero: A=(11,4,0) at `continue=decide P` and B=(12,0,1) at `continue=decide Q`. It yields

    D(0,0,0)=21144250159002694504331/1533854592314376192
            =V47+Gamma48*alpha47.

For every randomized history-dependent policy, max(T_P,T_Q) >= T_P >= Droot-lambda_P*E_P-lambda_Q*E_Q >= V47+Gamma48*(alpha47-alpha). This is a globally valid lower bound, not merely a local comparison between two candidate policies. Count-state Bellman sufficiency is justified by this auxiliary iid conditional law; native structural residuals are not asserted to vanish.

## Exact ordered branch reach and conditional continuation

Start from the complete inherited 47th endpoint stop tree, retain every inherited immediately-decide-P or immediately-decide-Q state, and newly fix the old 47th switching state (10,2,3) to immediate Q. The unique current new switching state is A=(11,4,0), where immediate P ties continuation; B remains a continuation/immediate-Q tie. Enumerating every ordered length-11 history with counts a=4,b=0, checking every earlier first-stop ancestor, proves **all 330/330 nominal A histories remain live**. Exact alive weights:

    p_A=4296875/191102976,  q_A=4296875/967458816.
    p_B=48828125/725594112, q_B=48828125/362797056.

There are 12 live B prefixes. Conditional continuation tuples (P-error,Q-error,additional P-samples,additional Q-samples) are

    c_A=(1/13824,1727/1728,601/576,157/144);
    c_B=(63/64,1/144,9/8,13/12).

These are exact rational recursions over the full stopped suffix tree; histories that have already stopped are never double-counted.

## Attaining primal and affine validity

Declare P early at A with probability u in [0,1], and Q early at B with probability s, keeping all remaining stop and continuation decisions fixed. Since A has four zeros and B zero, the branches are prefix-incomparable; both randomizations have no mixed effect on (E_P,E_Q,T_P,T_Q).

Define D=p_A*c_A[P-error]=4296875/2641807540224, W=q_A*(1-c_A[Q-error])=4296875/1671768834048, E=p_B*(1-c_B[P-error])=48828125/46438023168, H=q_B*c_B[Q-error]=48828125/52242776064. Relative to the previous endpoint, increasing u changes (E_P,E_Q) by (-D*u,+W*u), and changing s by Delta_s gives (+E*Delta_s,-H*Delta_s). Equalizing both errors forces

    s=s47+h48*u, h48=(D+W)/(E+H)=2299/1088000.
    E_P=E_Q=alpha47+eta48*u,
    eta48=-D+h48*E=W-h48*H=30078125/50524569206784 >0.

In particular 0<s47<=s<=s47+h48=8824703195037923/13926400000000000<1. Exact forward recursion verifies five rational mixtures u=0,1/4,1/2,3/4,1; a second author implementation independently computes backward absorbing tuples at the four (u,s) corners, confirms the vanishing mixed difference, and hence establishes affinity for every real mixture, not just the sampled rationals.

The P-expected sample size satisfies T_P(u)=V47-Gamma48*eta48*u. Its difference from Q-expected samples is affine and nonnegative at both u=0 (inherited) and u=1, where the exact margin is

    T_P(1)-T_Q(1)=1744440505910399401/3725075438477770752 > 0.

Therefore T_P=max(T_P,T_Q) and meets the Bellman lower bound on the entire interval. This completes the **global optimum** proof.

## Sharp right endpoint

Both dual multipliers are strictly positive: equality on this line requires E_P=E_Q=alpha. Every non-tied Bellman action has positive slack; only A and B permit mixing while retaining equality. For any fixed count state, likelihood ratio and suffix continuation tuples are invariant under which surviving ordered prefix reached it. Thus history-by-history mixing reduces, at the four-observable level, to state-average parameters u,s. The two error equalities impose s=s47+h48*u, so alpha=alpha47+eta48*u <= alpha48 since 0<=u<=1. The finite randomized-policy set is compact, so a strict unattainability means the supporting line cannot continue as an attained optimum beyond alpha48.

## Next frontier, evidence and limitations

With A fixed to immediate P and B left tied, a symbolic exact Bellman post-endpoint candidate is

    K49=56719116/2807, A49=(7,1,3), continue=decide Q.

This is **dual-only**; the 49th affine interval remains UNPROVED. Next: enumerate first-stop-surviving A49 prefixes against the full 48th endpoint tree, compute exact branch weights and conditional suffix tuple, balance at B, and verify dual equality, primal domination, endpoint and sharpness.

Evidence is exact Python fractions.Fraction computations with 680 states/1240 comparisons, full branch-history enumeration, forward mixture checks, backward four-corner absorption and a separate symbolic K scan. These are two author implementations sharing predecessor context, **not** independent Driver evidence or a Lean check. Reproduction companion is the self-contained portable checker and exact-rational JSON certificate committed alongside this note; a larger bilingual local author research archive is also available in this conversation. Applied BRC interface: positive rational branch weights with ordered first-stop provenance; raw multinomial counts must not erase earlier-stopping information. No signed/phase cancellation, native P000 change, or physical dynamics attribution is claimed.
