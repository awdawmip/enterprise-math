# Exact 51st affine interval in an N=14 auxiliary iid sequential test

**Status:** author-level exact finite-model proof, not independently reviewed or formally checked. **Date:** 2026-10-23. **Scientific scope:** the explicitly defined auxiliary iid problem, not a theorem about native BRC/X6/Heartbeat dynamics.

## Model and inherited endpoint

At each observation one of symbols 0,1,2 is sampled independently. Under hypotheses P and Q its laws are respectively P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6). A policy is an arbitrary, possibly history-randomized, stopping/decision rule with maximum length 14. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P(sample count), tQ=E_Q(sample count), and

V14(alpha) = inf { max(tP,tQ): eP<=alpha, eQ<=alpha }.

Inherit the **author-checked, Driver-unreviewed** 50th right endpoint, fixed stop tree, and two parameters

alpha50 = 5171825736073354397 / 14900301753911083008,
V50 = 12376506639448300069 / 931268859619442688,
s50 = 8831125038893923 / 13926400000000000,

where s50 is the probability of deciding Q immediately at B=(12,0,1). Its source is `awdawmip/enterprise-math@a4c8fe0e5e86a686493fae83125f83e567ec532a`, `research_notes/2026-10-23_N14_auxiliary_iid_50th_exact_affine_AUTHOR_UNREVIEWED.md`. At A50=(9,5,0) the inherited right-endpoint action is now always immediate P, and at earlier historical switch states the corresponding right-endpoint deterministic stop actions are preserved. A new candidate state is A51=(10,4,4), previously continuation.

## Theorem

For every real `0 <= delta <= eta51`, where

eta51 = 8490125 / 310422953206480896,

we have the **global**, unrestricted-history optimization identity

V14(alpha50+delta) = V50 - (7153992/217) delta.

The sharp right endpoint is

alpha51 = 5171825736480880397 / 14900301753911083008,
V51 = 12376505799748489069 / 931268859619442688.

The stated Bellman supporting line is unattainable for any alpha>alpha51. This says neither that V14 terminates at alpha51 nor that there is a native physical interpretation.

## Global Bellman-dual certificate

For state x=(n,a,b), n observations with a zeros and b ones, the likelihood ratio Q(path)/P(path) is `r(x)=2^(a+b)/3^a`; the exact order matters to stopping histories but not to this likelihood ratio. Choose

K51=3779136/217, lambdaQ=K51, lambdaP=72+8*K51/9=3374856/217,
Gamma=lambdaP+lambdaQ=7153992/217.

For every one of the 680 states with n<=14, compute using exact rationals

D(x)=min{ lambdaQ*r(x) [decide P], lambdaP [decide Q],
          1+sum_i P_i*D(child_i) [continue if n<14] }.

Finite backward enumeration (680 states, 1240 comparisons with nonselected actions) has exactly two zero slacks and 1238 strictly positive slacks: continuation ties with immediate Q at **A51=(10,4,4)** and at **B=(12,0,1)**, with no other ties. The root is

D(0,0,0)=8786093731573779237937 / 766927296157188096
        = V50 + Gamma*alpha50.

The Bellman identity is a bound over **every ordered-history-dependent randomized policy**, not just count-state stationary policies: by iterated conditional minimization,

D(root)<= tP + lambdaP*eP + lambdaQ*eQ.

Since lambdaP,lambdaQ>0, the constraint eP,eQ<=alpha and max(tP,tQ)>=tP imply

V14(alpha)>=V50+Gamma*(alpha50-alpha).

## Exact first-stop reach and conditional suffixes

For A51=(10,4,4), 10 observations consist of four 0s, four 1s and two 2s; there are `10!/(4!4!2!)=3150` nominal ordered histories. Applying all inherited *first-stop* rules to every prefix leaves **1565 true survivors**, with 1585 histories already stopped. The surviving unconditional masses are

pA=39125/48922361856 (under P), qA=39125/15479341056 (under Q).

B has exactly 12 surviving first-hit histories, with

pB=48828125/725594112, qB=48828125/362797056.

Conditional continuation suffix tuples `(eP,eQ,tP,tQ)` are

cA=(4095/4096, 1/20736, 585/512, 1885/1728),
cB=(63/64, 1/144, 9/8, 13/12).

The endpoint actions at A51 and B may be mixed independently because their history cylinders are disjoint: A51 prefixes have four zeros while B prefixes have none. First reach is not recoverable from terminal multinomial weights alone; the 1565 survivors are explicitly counted.

## Constructive primal attainment and exact balance

Let u in [0,1] be the probability of immediate Q at A51, and let s be the probability of immediate Q at B. The changes in errors relative to the 50th endpoint are

eP-alpha50 = X*u + E*(s-s50),
eQ-alpha50 = -Y*u - H*(s-s50),

where exact positive fractions are

X=pA*(1-cA.eP)=39125/200385994162176,
Y=qA*cA.eQ=39125/320979616137216,
E=pB*(1-cB.eP)=48828125/46438023168,
H=qB*cB.eQ=48828125/52242776064.

Setting `s=s50-h51*u` with

h51=(X+Y)/(E+H)=3335641/20889600000000

forces eP=eQ=alpha50+eta51*u, where

eta51 = X-E*h51 = H*h51-Y = 8490125/310422953206480896 > 0.

The second equality is H*h51-Y (not Y-H*h51); both equal the common error increment. The probability remains admissible: 0<s50-h51<=s<=s50<1, and

s51=s50-h51 = 26493368445399769/41779200000000000.

Exact forward and absorbing-backward recursions (including all first-stop rules) give

tP(u)=V50-Gamma*eta51*u,

and a strictly positive worst-time margin at both ends. At u=1,

tP-tQ = 1748365495275977401 / 3725075438477770752 > 0.

By disjointness of A51 and B, both sample means are affine in u along this balance path; endpoint positivity therefore gives tP>=tQ everywhere. Thus the constructed policy attains the global dual lower bound for every u, equivalently every claimed delta.

## Sharpness of this supporting line

If the same supporting line were attained at alpha>alpha51, the strictly positive multipliers force both eP=eQ=alpha and the Bellman slack decomposition forces only the two tied actions to be randomized on reachable histories. Although a policy may mix differently across histories ending at the same count state, their identical conditional laws and likelihood ratios reduce these mixtures to weighted average probabilities u and s. The exact error identities above then force `s=s50-h51*u` and `alpha=alpha50+eta51*u`; since u<=1, alpha<=alpha51, a contradiction. The finite randomized policy space is compact, so no policy can attain this supporting line beyond the right endpoint.

## Reproducibility, provenance and the next unit

`verify_n14_fiftyfirst.py` checks the deterministic stop table, exact dual costs and slacks, true reach, conditional suffixes, five real-parameter samples represented rationally, and the next dual crossing. `verify_n14_fiftyfirst_crosscheck.py` independently minimizes the finite Bellman recursion, enumerates all `3^10=59049` length-ten words for first-stop reach and checks all four backward-randomization corners. Both are **author-side** checkers; independence of an external Research Driver has not been established. Finite model exhaustiveness relies on the explicit enumerated stop sets and all 680 reachable-or-unreachable count states, not a sample of trajectories.

At the new endpoint, fixing A51 to immediate Q yields the next **dual candidate only**

K52=280418092213968/16640988557, A52=(3,0,3), with continue/Q tie.

The 52nd error compensation and optimality are NOT proved. Next work: calculate the true first-stop reach of A52 under the 51st policy (in particular, its potential influence on descendants), build the two-error balance and derive its attainable right endpoint. Native CLAIM, independent Driver review, formal proof, and BRC/X6/Heartbeat transfer remain unverified/not performed.

Pinned global source: `awdawmip/chatgpt-global-knowledge@bf441dbd96e3aff7f1df531c6569d56fa048a10b`; Enterprise Math scientific startup source: `awdawmip/enterprise-math@d20e28116f8a9a1df78f5641d70f72e797a4856d`. P000 is an in-scope starting axiom; no P000, worldview, or native-model result is modified by this auxiliary lemma.