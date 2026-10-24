# N=14 auxiliary iid sequential discrimination: the 75th exact affine interval

**2026-10-24. Evidence: author-level exact finite-model proof.** There is no native Enterprise Math CLAIM, independent Research Driver acceptance, Lean proof, or native BRC/X6/Heartbeat transfer.

## Model and exact theorem

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) be iid laws on {0,1,2}, with stopping horizon N=14. Policies may randomize based on the entire ordered observation history. Put e_P=P(decide Q), e_Q=Q(decide P), t_P=E_P[T], t_Q=E_Q[T], and
V_14(alpha)=inf{max(t_P,t_Q): e_P<=alpha,e_Q<=alpha}.

The inherited **author-verified** 74th endpoint is
alpha74=2585972551358493847/7450150876955541504,
V74=24565716022242816749/1862537719238885376,
and the probability of immediate Q at B=(12,0,1) is
s74=12002006216766011/20889600000000000.
The full inherited deterministic stop table is in the executable verifier; freeze its prior tie A74=(12,5,1) as immediate P.

**Theorem.** Define
eta75=9239954171/1655589083767898112 and
Gamma75=68010728968800/9239954171.
For **every real** 0<=delta<=eta75, including irrational deltas,

V_14(alpha74+delta) = V74 - Gamma75*delta.

The exact right endpoint and optimum are

alpha75=5171945185876575233/14900301753911083008,
V75=24565639510172726849/1862537719238885376.

The displayed Bellman supporting line is sharp at its right endpoint: beyond alpha75 it cannot still be attained. This statement concerns support-line attainment, not the existence of later affine intervals.

## Complete Bellman dual lower bound

At count state x=(n,a,b), n observations and a,b counts of symbols 0,1, the positive likelihood ratio Q(w)/P(w)=2^(a+b)/3^a is independent of order. Set
K75=lambda_Q=35653474730376/9239954171,
lambda_P=72+(8/9)K75=32357254238424/9239954171;
Gamma75=lambda_P+lambda_Q.
The P-normalized Bellman alternatives are

C_P=lambda_Q*2^(a+b)/3^a;
C_Q=lambda_P;
C_C=1+sum_i P_i D(child_i) for n<14,

with continuation prohibited at n=14. Exact Fraction backward induction covers all
sum_{n=0}^{14} (n+1)(n+2)/2 = **680** states and **1240** comparisons between nonchosen and chosen actions. It records **1238 strictly positive gaps, zero negative gaps, exactly two ties**: B=(12,0,1), continue/immediate-Q; and A75=(4,1,3), continue/immediate-Q. The smallest strictly positive gap is 2154656646001/71849883633696. The root certificate is

D(0,0,0)=2599732686354294991877622056087/1012339009854480345609535488
=V74+Gamma75*alpha74.

The iid suffix laws and the likelihood ratio agree for every full ordered history having the same count state, so Bellman minimization bounds even fully history-dependent randomized policies:

D(0,0,0) <= t_P+lambda_P*e_P+lambda_Q*e_Q
          <= max(t_P,t_Q)+Gamma75*alpha.

Therefore V_14(alpha)>=D(0,0,0)-Gamma75*alpha globally.

## Real ordered first-hit mass and truncation

The new tie A75=(4,1,3) has four nominal ordered prefixes, of which **three** survive all old stop decisions. Their exact positive first-hit masses are

p_A=1/36864, q_A=1/6912.

At B the 12 surviving histories have

p_B=48828125/725594112,
q_B=48828125/362797056.

The inherited continuation suffix risks, ordered as (e_P,e_Q,remaining t_P,remaining t_Q), are

R_A=(260465029237/260919263232,
13453613/61917364224,
52995478699/32614907904,
774946309/573308928),

R_B=(63/64, 1/144, 9/8, 13/12).

Enabling early Q at A truncates downstream stop paths. The exact ordered-prefix routing program enumerates **49 distinct downstream first-stop states** reached following A and **4035 completed ordered terminal histories** passing through A. These are numbers of distinct words of varying lengths, NOT likelihood-weighted mass. The separate forward and backward exact calculations retain P/Q rational branch weights. Three immediate child count states (5,1,3), (5,2,3), (5,1,4) have respectively 3,3,3 surviving ordered prefixes passing A. Aggregating nominal paths before accounting for early stopping would give a wrong answer. This work applies positive rational ordered-branch BRC provenance; it makes no claim about signed or phase-amplitude cancellation.

## Exact constructive primal family for all real u

Let 0<=u<=1 be the probability of immediate Q at A, otherwise continue. Let s be the probability of immediate Q at B. Every path reaching A has symbol 0 in its prefix; no path reaching B has symbol 0. Hence these states cannot occur on one trajectory, and the four risk observables have identically zero coefficient of the mixed monomial u*s. The second checker also verifies the four-corner identities using independent backward rational recursion.

Put
X=p_A*(1-R_A.e_P)=454233995/9618527719784448,
Y=q_A*R_A.e_Q=13453613/427972821516288,
E=p_B*(1-R_B.e_P)=48828125/46438023168,
H=q_B*R_B.e_Q=48828125/52242776064.

Relative to the former endpoint,

Delta e_P = X*u + E*(s-s74),
Delta e_Q = -Y*u - H*(s-s74).

Demanding e_P=e_Q fixes the **negative** balancing adjustment
s=s74-h75*u,
h75=(X+Y)/(E+H)=551560577747/13926400000000000.

Then, in exact rational arithmetic,

Delta e_P=Delta e_Q=eta75*u,
eta75=X-E*h75=-Y+H*h75>0,

and the coin remains feasible for every real u:

0<s75=24002357751798781/41779200000000000<s74<1.

At u=0 and u=1 the sample count gaps t_P-t_Q are respectively
276114249347617787/465634429809721344
and 2209467934106972251/3725075438477770752,
both positive. Since all risks are affine throughout this family, t_P remains the maximum for every real u. Each action used is Bellman-optimal at K75, so

t_P+lambda_P*e_P+lambda_Q*e_Q=D(0,0,0),

which gives t_P=V74-Gamma75*eta75*u. Choosing u=delta/eta75 achieves the universal lower bound for **all real** delta in the closed interval. Finite grid checks alone are not used as a proof of the continuous-parameter statement.

## Sharpness of the support line

Any policy attaining the same dual supporting line must use only zero-slack Bellman actions on every reached positive-mass ordered history. The 1238 strict comparisons fix all other actions. The positive dual multipliers further force both error budgets tight. The only relevant tied actions are at A and B. Even history-dependent randomized decisions there reduce, for the four declared observables and iid suffix law, to the corresponding first-hit-mass-weighted effective probabilities u and s. The disjoint support of A and B forces the affine error formulas above. If both errors equal alpha, their difference forces s=s74-h75*u and alpha=alpha74+eta75*u. Since 0<=u<=1, equality is impossible for alpha>alpha75. The support line is therefore right-sharp.

## Exact evidence and scope

Three finite rational tools were run locally with Python's fractions.Fraction: verify_n14_75.py exhausts the Bellman comparisons, exact forward risks, endpoints and seven rational u values; verify_n14_75_crosscheck.py separately minimizes the Bellman table, enumerates all nominal and surviving ordered prefixes, computes risks backward and checks mixed coefficients at four corners; descend75.py enumerates the 49 downstream terminal-stop states and 4035 completed truncated path histories. The main two verifiers share the inherited author's stopping table and thus do NOT amount to independent Research Driver examination. Certificate and run outputs record the full exact fractions and verify that the stated continuum argument rests on exact affineness, not merely finite interpolation.

After fixing the new tie A75 to immediate Q, the exploratory dual candidate for the next segment is K76=63090576/16703, state A76=(10,7,2), continue versus immediate P. **The 76th interval is not yet proved.**

Provenance: inherited n74 source from awdawmip/enterprise-math research_notes/n14_aux_iid_affine_74_20261024 at remote main faf1569f46918c781b3587dd8dec1b2b4ce09981. Global account rules fixed at awdawmip/chatgpt-global-knowledge main cfd9080253a6fcc9baa0cd15c7ff0f7472e209c3, GLOBAL_KNOWLEDGE_V1. Native em_control_tasks returned CONTROL_QUOTA and em_session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). This independent author contribution does not allocate a formal task owner, CLAIM, Result or Driver review. P000 and ACTIVE worldview remain unchanged.