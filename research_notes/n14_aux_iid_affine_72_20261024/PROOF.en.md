# N=14 auxiliary iid sequential discrimination — exact 72nd affine interval

**24 October 2026. Evidence: author-level exact finite-model proof.** Two related author-side exact-rational programs were executed locally and passed; no independent Research Driver review, native CLAIM, native BRC/X6/Heartbeat transfer, or theorem admission is asserted.

## Model and theorem

For independent ordered observations in alphabet {0,1,2}, let
P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), with a maximum of N=14 observations. Arbitrary full-history randomized stopping and decision policies are permitted. Let eP=P(decide Q), eQ=Q(decide P), and tP,tQ be their respective expected sample counts. Put V14(alpha)=inf max(tP,tQ) over policies satisfying eP,eQ <= alpha.

Inherit the exact deterministic stop table from `research_notes/n14_aux_iid_affine_70_20261024/verify_n14_70.py` (70th immutable source), and additionally set 70th site (9,4,4) and 71st site (11,1,2) to deterministic immediate Q decisions. This source table and the likelihood-threshold terminal rule, not a guessed aggregate decision, define the author-level model.

The preceding author-checked endpoint and balancing Q coin are

    alpha71 = 2585958427839642247/7450150876955541504
    V71     = 24596496152727045149/1862537719238885376
    B       = (12,0,1)
    s71     = 11804104280776811/20889600000000000.

**The 72nd affine interval** is exactly

    eta72 = 2865625/1761205026816
    Gamma72 = 1162152/131

and, for *every real* 0 <= delta <= eta72,

    V14(alpha71+delta) = V71-Gamma72*delta.

In particular

    alpha72 = 2585970549846042247/7450150876955541504
    V72     = 24569611393219845149/1862537719238885376.

This same Bellman supporting line cannot attain the optimal value beyond alpha72 (sharp right endpoint).

## Exact global lower bound for full-history policies

Write a state (n,a,b) for word length and numbers of symbols 0 and 1. The P-normalized likelihood ratio is Q/P = 2^(a+b)/3^a. For the multipliers

    K72=lambdaQ=10374480/2227
    lambdaP=72+(8/9)K72=9382104/2227
    Gamma72=lambdaP+lambdaQ=1162152/131,

the Bellman options at any state are

    C_P=lambdaQ*2^(a+b)/3^a,
    C_Q=lambdaP,
    C_C=1+sum_i P_i D(child_i) [only if n<14].

Backward induction takes the minimum and provides a lower bound for every ordered-history policy, since the likelihood ratio and future suffix law depend only on state. An exact Fraction check covers all 680 states and 1240 comparisons to the inherited chosen action. There are precisely 1238 positive gaps, zero negative gaps, and exactly two tied actions: A72=(9,4,0), continue versus immediately decide P; and B=(12,0,1), continue versus immediately decide Q. The minimum positive gap is

    963802307/13299572736,

and the root is

    D000=754541330703681222073405/243992441220293984256
        = V71 + Gamma72*alpha71.

For all admissible policies:
D000 <= tP+lambdaP*eP+lambdaQ*eQ <= max(tP,tQ)+Gamma72*alpha,
so V14(alpha) >= D000-Gamma72*alpha.

## BRC provenance, surviving ordered histories, and suffix risks

The site A72 has C(9,4)=126 nominal ordered words. All 126 survive the earlier stopping rule, so the exact positive-rational BRC branch masses are

    pA=P(first reach A72)=21875/1769472,
    qA=Q(first reach A72)=21875/8957952.

B has 12 surviving ordered histories and first-hit weights

    pB=48828125/725594112,
    qB=48828125/362797056.

Conditional continuation suffix risks (eP,eQ,tP,tQ) are

    RA=(119/294912,27563/27648,124867/110592,973/768)
    RB=(63/64,1/144,9/8,13/12).

The older stop (10,4,0) has 210 live ordered prefixes, 126 of which passed A72. The stop (10,5,0) has 126 live prefixes, and all 126 passed A72. Immediate P at A72 removes those downstream first-stop paths; it cannot be added as an independent stop without truncating descendants. The calculation retains ordered-path provenance and exact positive branch weights. This is a finite iid auxiliary BRC carrier, not an identification with native spatial/phase paths.

## Continuous optimal constructive policy

Let u in [0,1] be the probability of early P at A72, and let s be the probability of early Q at B. B requires zero symbol-0 observations while A72 requires four; a path cannot visit both sites. Thus the four exact rational risk functions have zero mixed coefficient in u*s (confirmed by all four corner checks).

With the symbols

    X=pA*RA.eP                  =2603125/521838526464
    Y=qA*(1-RA.eQ)             =1859375/247669456896
    E=pB*(1-RB.eP)             =48828125/46438023168
    H=qB*RB.eQ                 =48828125/52242776064,

the error changes from the baseline (u,s)=(0,s71) are

    Delta eP = -X*u+E*(s-s71),
    Delta eQ =  Y*u-H*(s-s71).

Hence exact balancing requires

    s=s71+h72*u,
    h72=(X+Y)/(E+H)=805329/128000000,

and gives

    eP=eQ=alpha71+eta72*u,
    eta72=E*h72-X=Y-H*h72=2865625/1761205026816.

The coin ranges strictly within [0,1], since 0<s71<s72<1, with

    s72 =11935533973576811/20889600000000000.

Both endpoint sample gaps tP-tQ are positive:

    (tP-tQ)|u=0 =281489708847513187/465634429809721344
    (tP-tQ)|u=1 =276636241011513187/465634429809721344.

The sample risks are affine in u because the two randomization sites cannot meet on a trajectory. Hence tP is the worst side at every real u in [0,1], and the constructed Bellman-minimizing policy attains

    tP = V71-Gamma72*eta72*u,
    tP+lambdaP*eP+lambdaQ*eQ = D000.

For each real delta in [0,eta72], choose u=delta/eta72 to meet the global lower bound, proving the entire interval, not merely its rational test points.

## Sharpness and next frontier

The randomized full-history finite policy space is compact. Equality to this supporting line requires every reached action to minimize Bellman and both error constraints to be tight because both multipliers are positive. Exactly A72 and B offer nontrivial ties. Histories arriving at one count state have identical conditional risks, so history-conditioned randomization reduces to a single effective u and s for these four observables. Equal errors enforce s=s71+h72*u and therefore alpha=alpha71+eta72*u <= alpha72. This excludes support-line equality for alpha>alpha72.

Two distinct author-side exact Fraction verifiers rechecked the global Bellman recursion, nominal and surviving ordered histories, backward conditional risks, path-truncated descendants, corner cross terms and rational interior points. They use the same inherited author stop table, so they are **not independent research-driver validation**. No native BRC/X6/Heartbeat faithful embedding or empirical physics conclusion is claimed.

**Next unproved segment:** K73=2306549196/525227, A73=(8,6,1) with continue vs immediate P. The 72nd checker found this as the first dual crossing, and a separate fixed-table candidate check found only A73 and B as ties and no negative Bellman slacks at this K. Its first-hit mass, truncations, feasible balancing interval and sharp endpoint remain unproved.

Source pins: GLOBAL_KNOWLEDGE_V1 main e209497cea450b0ef02e3844215db1497479c53f; Enterprise Math starting main e769033889819c85d90b0944afde978c0ee52d80; inherited 70th source GitHub commit eb98673aa12c1f7db38928e73b8504b779391346. Publication/driver authority remain distinct.
