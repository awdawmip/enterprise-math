# Stage136 — exact affine optimal interval and sharp right endpoint (N14 ternary iid)

**Status:** AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF. Two separately coded author verifiers executed locally and passed. No independent Research Driver review, formal Result/CLAIM, P000-X6 theorem, or physical assertion.

## Model and theorem

Observations are independent over {0,1,2} under P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Tests may randomize based on *literal ordered histories*, stop by N=14 and decide P/Q. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P[tau], tQ=E_Q[tau], and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

From the Stage135 author endpoint, alpha135=12235904537797579565/35205614928358539264 and V135=72642955720985708803/5867602488059756544. Define eta136=2480622625/733450311007469568.

**THEOREM (every real delta in [0,eta136]):**

V14(alpha135+delta)=V135-(1638248576/1526537)*delta.

The sharp endpoint is alpha136=12235904656867465565/35205614928358539264 and V136=72642934423754220803/5867602488059756544. "Sharp" refers to the supporting affine line; tests at larger alpha remain feasible.

## Universal dual bound, including arbitrary ordered-prefix tests

Take K=840571992/1526537, L=797676584/1526537, S=K+L=1638248576/1526537. For counts s=(n,a,b), a,b counting symbols 0 and 1, the Q/P likelihood ratio is r(s)=2^(a+b)/3^a. The exact P-conditional Bellman cost is

H(s)=min{K*r(s) [decide P], L [decide Q], 1+(1/8)H(n+1,a+1,b)+(1/24)H(n+1,a,b+1)+(5/6)H(n+1,a,b) [continue, n<14]}.

At n=14 only the first two actions exist. Independent suffix laws and the likelihood ratio are count-sufficient for this *specific dual and four-observer objective*, although literal histories remain distinct. Exact rational backward induction covers 680 states. There are 1238 strictly positive nonchosen-action gaps, no negative gaps; minimum positive 3073199/82432998. Exactly two ties exist: B=(11,0,1), decide Q/continue; D=(10,6,2), decide P/continue. H(0,0,0)=42968477475733404697846433/111499323227990994714624.

Consequently, for **every history-dependent randomized policy** H0 <= tP+L*eP+K*eQ <= max(tP,tQ)+S*alpha if eP,eQ<=alpha. Hence V14(alpha)>=H0-S*alpha.

## Provenance-retaining BRC and four-observer test family

Each literal first-hit prefix is retained with ordered symbol history, stopping depth and both exact positive P/Q branch masses before taking a proved sufficient count quotient. Under optimal strict actions and continuation at the two ties:

* B=(11,0,1): 11 literal first-hit words; P mass 107421875/1451188224; Q mass 107421875/725594112.
* D=(10,6,2): 585 literal first-hit words; P mass 1625/603979776; Q mass 1625/1719926784.

No path visits both ties: D already has six observed zeros at depth 10, whereas B has zero zeros at depth 11, and zero-count is monotone; B cannot precede D because of depth.

Let w be the probability of *decide Q* at B (versus continue) and u the probability of *decide P* at D (versus continue). Else use the unique strict Bellman action. For the ordered vector M=(eP,eQ,tP,tQ), two independently coded exact algorithms prove for every real (w,u) in [0,1]^2:

M(w,u)=M00+w*dB+u*dD,

M00=(2430334789423408769/7011906707722862592, 447296740721041/1283918464548864, 10888424083537661711/876488338465357824, 1274918373062933/106993205379072),

dB=(4619140625/2229025112064, -751953125/417942208512, -25673828125/278628139008, -17939453125/104485552128),

dD=(-2253875/200385994162176, 573625/35664401793024, -24873875/8349416423424, -3420625/2972033482752).

The first algorithm uses bottom-up Fraction observer recurrence. The second walks *literal* ordered histories with independent top-down recursive Bellman actions and integer P/Q weights (3,1,20)/24 and (1,1,10)/12, keeping common denominators 24^14 and 12^14. All four deterministic corners match coordinatewise, with zero interaction M11-M10-M01+M00=0. DFS visited-prefix counts at (00,10,01,11) are respectively 691078, 690946, 680548, 680416.

## Attainment throughout a continuum

The unique exact error compensation equation eP=eQ is

w(u)=37505431703309437/81438720000000000 + (95823429/13573120000000)*u, 0<=u<=1.

Both w(0) and w(1)=3409636967625767/7403520000000000 are strictly between 0 and 1. Substitution into the four-observer affine family gives

eP=eQ=alpha135+eta136*u, and tP=V135-S*eta136*u.

The exact gaps tP-tQ at u=0 and u=1 are respectively 86109883987742344807/158425267177613426688 and 86109683330236204807/158425267177613426688. Both are >0, so affineness proves tP>tQ for *all real u* in [0,1]. Every selected action minimizes the Bellman dual; equality with the universal lower bound proves the entire real interval, not a sampled grid.

## Right sharpness of this supporting line

Suppose the same line attained V14(alpha) at alpha>alpha136. Finite-horizon behavioral strategy spaces are compact, so an attaining policy exists. Equality in the dual chain, with K,L>0, forces eP=eQ=alpha and forces every positively visited action to be Bellman optimal. Strict gaps rule out any other actions. History-dependent coins at either tie can be mass-averaged: all first-hit words with those counts share the same Q/P ratio and iid suffix distribution. The effective w,u preserve all four aggregate observers. Disjoint tie path cones make their joint effect precisely the displayed affine family. The equal-error equation then forces w=w(u); the common error increases strictly with u (eta136>0), and u<=1 imposes alpha<=alpha136. Contradiction. No extension of *this supporting line* exists to the right.

## Stage137 dual candidate only

At the Stage136 right edge D's stop-P becomes strict; preserving B's Q/continue tie along (dK,dL)=(-1,-112/129), exact one-sided gap scanning finds the first new equality at t=9892799730/612141337. New parameters K137=214326/401, L137=203912/401; new Q/continue tie G=(13,6,4), old B tie remains. Fresh Bellman check: 680 states, 1238 positive gaps, minimum positive 1/173232. **No Stage137 primal interval, feasibility family or sharpness claim yet.**

## Authority, limitations and next work

Input snapshots: GLOBAL_KNOWLEDGE_V1 main@56d2c838ada2338ab606ffdf76cad21738a8b258, Enterprise Math source main@35542fad3bdf95e3b06f7b13ddf2952f386b2286. Exact P000 startup projection matched original P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Active worldview and portable research protocol read. Method status: BRC positive-rational ordered branch carrier and exact four-observer quotient **REUSE_APPLIED**; no signed-amplitude interpretation.

Native task inventory returned CONTROL_QUOTA. Direct session start with this static read-only identity returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Current active Owner/CLAIM could not be verified; ordinary author evidence publication is not formal native research admission. No independent Driver review. This external finite iid test has no proved correspondence to native P000 X6 Cell dynamics, three-dimensional slice or any physical process.

**Next executable unit:** Stage137 B/G literal first-hit masses, potential path-cone interactions, exact four-observer corner vectors by two independent methods, equal-error compensation, time-gap feasibility and a full-real optimal interval or precise no-go, with an independently tested sharpness argument.
