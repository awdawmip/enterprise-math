# N=14 auxiliary iid sequential discrimination — exact 71st affine interval

**24 October 2026.** Author-level exact rational finite-model result; two related author-side Fraction verifiers passed locally. Not an independent Research Driver acceptance, and not a native BRC/X6/Heartbeat result.

## Model and theorem

Ordered independent samples of symbols 0,1,2 have distributions
P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Maximum observation horizon N=14. A randomized stopping/decision rule may depend on the *entire ordered history*. Let eP=P(decide Q), eQ=Q(decide P); tP,tQ are the two expected sample counts. Define V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

The author-checked 70th endpoint is alpha70=2585943605439642247/7450150876955541504, V70=24633048191127045149/1862537719238885376, and the early-Q coin at B=(12,0,1) has probability s70=4173506760258937/6963200000000000. The inherited stopping rules are exactly those encoded in the 70th verified checker at source commit eb98673aa12c1f7db38928e73b8504b779391346, with the 70th tie state (9,4,4) now deterministically deciding Q.

Set K71=5184, lambdaP=4680, lambdaQ=5184, Gamma71=9864, and eta71=75390625/37893426905088.

**Claim proved at author level. For every real delta in [0, eta71], including irrational interior points:**

    V14(alpha70+delta)=V70-9864*delta.

Consequently,

    alpha71=2585958427839642247/7450150876955541504
    V14(alpha71)=24596496152727045149/1862537719238885376.

The *same* Bellman supporting affine function is not attained for any alpha>alpha71: this right endpoint is sharp.

## Global lower bound (all full-history policies)

For a prefix with n observations, a symbols 0 and b symbols 1, its likelihood ratio Q/P is 2^(a+b)/3^a. In units normalized by P mass, the Lagrangian tP+lambdaP*eP+lambdaQ*eQ has state costs:

    C_P=lambdaQ*2^(a+b)/3^a
    C_Q=lambdaP
    C_C=1+sum_i P_i D(n+1,a+[i=0],b+[i=1])
    D=min of available actions; C_C unavailable at n=14.

Although the policy is allowed to inspect the entire ordered word, the suffix law and likelihood ratio depend only on (n,a,b); the recursion therefore gives a valid lower bound for *every* ordered-history policy.

Exact Fraction backward induction checked 680 count states, 1240 comparisons with the chosen action, 1238 strict positive gaps, zero negative gaps, and precisely two zero ties: A71=(11,1,2), C versus Q; and B=(12,0,1), C versus Q. Minimum strictly positive gap: 6491/248832. The root is

    D(0,0,0)=376562939953252048603/109561042308169728
            =V70+9864*alpha70.

For any feasible policy, D(root)<=tP+4680 eP+5184 eQ<=max(tP,tQ)+9864 alpha. Hence V14(alpha)>=D(root)-9864 alpha, globally.

## Branch provenance, true first hits and suffix risks

A71 has 495 nominal ordered histories of length 11 but only 386 are live, since prior stops truncate 109 (84 at (8,0,2), 16 at (9,0,2), 9 at (10,0,2)). First-hit P and Q mass, obtained by weighted *surviving ordered word* accumulation:

    pA=75390625/3869835264
    qA=75390625/1451188224.

At B, all 12 nominal histories are live:

    pB=48828125/725594112
    qB=48828125/362797056.

Conditional suffix risks for continuing at the two states, written (eP,eQ,tP,tQ), are

    RA=(511/512,1/1728,73/64,157/144),
    RB=(63/64,1/144,9/8,13/12).

As a provenance witness, old first-stop (12,1,2) has 496 live arriving words, including 386 that first visit A71; old first-stop (12,1,3) has 386, all passing A71. Early Q at A71 truncates these downstream branches. The BRC method actually reused here is the positive rational labeled-branch law W=sum over surviving words of the product of step weights; replacing this first-hit carrier with raw count-state nominal multiplicities is invalid. This is not signed amplitude or native spatial path semantics.

## Constructive optimal policy for the full real interval

Let u∈[0,1] be the probability of immediate Q at A71, and s the probability of immediate Q at B. The sites cannot lie on one trajectory, since A71 has observed a=1 and B has a=0, and a can only increase. Four Fraction corner evaluations confirm the coefficient of u*s is zero in each of the four risk functions.

Define positive sensitivities:

    X=pA*(1-RA.eP)=75390625/1981355655168
    Y=qA*RA.eQ=75390625/2507653251072
    E=pB*(1-RB.eP)=48828125/46438023168
    H=qB*RB.eQ=48828125/52242776064.

Relative to (u,s)=(0,s70), the changes are

    ΔeP=X*u+E*(s-s70),
    ΔeQ=-Y*u-H*(s-s70).

Equal errors require

    s=s70-h71*u, h71=(X+Y)/(E+H)=5597/163200.

At u=1, s71=11804104280776811/20889600000000000. Exactly 0<s71<s70<1, so this is a feasible family for every real u in [0,1]. Exact substitution yields

    eP=eQ=alpha70+eta71*u,
    eta71=X-E*h71=H*h71-Y=75390625/37893426905088.

The worst-sample-side tP dominates throughout: endpoint tP-tQ gaps are respectively

    266582080047513187/465634429809721344
    281489708847513187/465634429809721344,

both positive, and sample risks are affine in u. The retained actions are Bellman-minimizing for these dual multipliers. Therefore tP+4680 eP+5184 eQ=D(root), giving tP=V70-9864*eta71*u. For any real delta∈[0,eta71], choose u=delta/eta71. That policy achieves the global lower bound, proving the whole real interval rather than only rational grid points.

## Sharpness, validation and limits

The finite randomized full-history policy polytope is compact. Equality with the same affine support beyond alpha71 would force both error constraints tight (dual multipliers are positive) and only Bellman-minimizing actions at all reached histories. The only two nontrivial tie states are A71 and B; each collection of histories at one count state has the same conditional suffix risks and likelihood ratio. History-dependent coins therefore collapse to one effective u and s for these observables. Equality eP=eQ enforces s=s70-h71*u, and hence alpha=alpha70+eta71*u<=alpha71, contradiction.

Actual local computation: an inherited-rule exact Fraction checker and another author crosschecker performing a fresh Bellman minimization, explicit length-11 ordered-word history enumeration, backward risk calculation, four corner mixed-term tests, and seven rational interpolation checks both passed. They *share* the inherited author stopping table; there is no independent Driver review, native task freeze, accepted physical interpretation or native BRC/X6/Heartbeat faithful bridge. The live Owner and native CLAIM could not be established: control dispatch returned CONTROL_QUOTA. This mathematical note is an author-level source artifact, not a formal result admission.

**Next unproved candidate:** K72=10374480/2227, state A72=(9,4,0), continue versus P. Recompute genuine first-hit histories, truncated descendants, dual slacks, balance-state compensation and a positive real interval before claiming the 72nd theorem.

Control pins: GLOBAL_KNOWLEDGE_V1 immutable main 5b5304151d63b63c0c3e9133f05fd7a0fbe33ffd; Enterprise Math control main d1d7d3453258acd50becb821d92386d3e18f9f24; inherited source commit eb98673aa12c1f7db38928e73b8504b779391346.
