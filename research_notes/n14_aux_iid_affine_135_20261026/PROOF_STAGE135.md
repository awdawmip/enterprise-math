# Stage135 | N14 exact real optimal interval — author finite-model theorem

Status: AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF. Two separate author-side local algorithms PASS; NO independent Research Driver review, native owner/CLAIM, Result freeze, Working Truth, or P000-X6/Heartbeat physical theorem.

## Scope and exact theorem

External auxiliary ternary iid model: P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=14. Randomized policies may use every literal ordered observation history, must stop by N and declare P or Q. eP=P(declare Q), eQ=Q(declare P), tP=E_P[tau], tQ=E_Q[tau]. Let V14(alpha) be the minimum of max(tP,tQ) under eP,eQ<=alpha.

Inherited Stage134 author endpoint:
alpha134=36703016772992738695/105616844785075617792,
V134=656399729826573779227/52808422392537808896.

Bellman dual parameters:
K135=119895901488/209680375,
L135=113419128664/209680375,
S135=K135+L135=233315030152/209680375.

THEOREM for EVERY REAL 0<=delta<=eta135=4586758203125/103141449985425408:

V14(alpha134+delta)=V134-(233315030152/209680375)*delta.

The sharp right support endpoint is:
alpha135=12235904537797579565/35205614928358539264,
V135=72642955720985708803/5867602488059756544.

The *same supporting line* cannot equal V14(alpha) for alpha>alpha135. This is not infeasibility of tests at higher alpha.

## Universal P-weighted Bellman lower bound

At count state s=(n,a,b), a and b count observed symbols 0 and 1. Every ordered history with this state has Q/P likelihood ratio r(s)=2^(a+b)/3^a. Its minimum dual conditional cost H(s) uses:
declare P: K135*r(s);
declare Q: L135;
continue, when n<14: 1+P0*H(n+1,a+1,b)+P1*H(n+1,a,b+1)+P2*H(n+1,a,b).
At n=14 continuing is forbidden.

Exact Fraction backward recurrence covers all 680 states. Among 1240 possible nonselected actions, 1238 have STRICTLY POSITIVE gap, none have negative gap, and exactly two zero gaps occur at:
B=(11,0,1): declare Q / continue;
A=(7,3,0): declare P / continue.
Least strictly positive gap = 8101984967/271745766000.
Root H(0)=1222494294337487125572330743/3063040058209052550758400.

Bellman backward induction applies to ALL LITERAL HISTORY-DEPENDENT randomized rules: iid suffix laws and Q/P ratio are count-sufficient for these four observables. For every feasible policy,
H(0) <= tP + L135*eP + K135*eQ <= max(tP,tQ)+S135*alpha.
Thus V14(alpha)>=H(0)-S135*alpha.

## Exact literal BRC provenance and four-observer family

Carry each literal first-hit word with positive rational P/Q branch weight and full stopping-depth provenance before the exact iid four-observer count quotient. Independently implemented integer-weight ordered DFS gives the actual first-hit prefixes:
A=(7,3,0): 35 literal words; P mass 21875/663552; Q mass 21875/2239488.
B=(11,0,1): 11 literal words; P mass 107421875/1451188224; Q mass 107421875/725594112.

Their descendant cones are disjoint: A has 3 observed zeros at depth7 while B has 0 at depth11, and zero-count never decreases; B cannot precede A due to depth. Consequently no mixed w*u term occurs.

Let w be the probability of declaring Q at B rather than continuing; u the probability of declaring P at A rather than continuing. Else use the unique strict Bellman action. For ALL REAL (w,u) in [0,1]^2 and M=(eP,eQ,tP,tQ):

M(w,u)=M00+w*dB+u*dA,

M00=(
2431517550617008769/7011906707722862592,
447002042121041/1283918464548864,
10923488398350461711/876488338465357824,
1276430797262933/106993205379072
);
dB=(
4619140625/2229025112064,
-751953125/417942208512,
-25673828125/278628139008,
-17939453125/104485552128
);
dA=(
-128337803125/760840571584512,
4604665625/20061226008576,
-1268240553125/31701690482688,
-7877209375/557256278016
).

Two separately implemented author-side programs obtain these coefficients: an exact bottom-up Fraction moment recurrence and a top-down independent literal integer-prefix DFS on branch numerators (3,1,20)/24 and (1,1,10)/12. They match all four deterministic corners and M11-M10-M01+M00=0. DFS counts 704938,691078,704806,690946 visited prefixes and 469959,460719,469871,460631 terminal histories at corners (00,01,10,11).

## Full continuous interval, attainment and right sharpness

The unique exact error compensation relation eP=eQ is

w(u)=29128806260109437/81438720000000000+(2617695451/25449600000)*u,
0<=u<=1.

All parameters are legal:
0<w(0)<w(u)<=w(1)=37505431703309437/81438720000000000<1.
Exact substitution gives for each REAL u:
eP=eQ=alpha134+eta135*u,
tP=V134-S135*eta135*u.
The endpoint values of tP-tQ are
88912023540183944807/158425267177613426688 > 0 at u=0, and
86109883987742344807/158425267177613426688 > 0 at u=1.
Affineness makes tP>tQ throughout the entire real interval. All used actions attain Bellman equality, so the universal bound is attained. This proves the theorem for all real delta, not just a rational grid.

For right-sharpness, finite behavioral strategy space is compact; a policy attaining the same support at alpha>alpha135 would force both error constraints to bind (K,L>0), and every positively visited action to be Bellman minimizing. The strictly positive gaps exclude all non-tie alternatives. Prefix-conditioned coins at the same tie can be mass-averaged because the Q/P likelihood ratio and iid conditional suffix laws coincide for that count, giving an effective (w,u) in [0,1]^2 with identical four aggregate observers. Disjoint path cones give the same affine family. Error balancing then forces the displayed w(u), and eP=eQ increases strictly with u, hence cannot exceed alpha135 since u<=1, contradiction. Therefore this dual supporting line is right-sharp.

## Actual verification, authority, and next stage

Executed locally (not on GitHub runners):
CHECKER_STAGE135.py -> PASS, all 680 Bellman states, 1238 strictly positive gaps, four corners and exact interval.
INDEPENDENT_ORDERED_STAGE135.py -> PASS, separate Bellman + 4 complete literal integer-weight ordered DFS, first-hit mass and all four observer vectors.
SCAN_STAGE136.py -> DUAL_CANDIDATE_ONLY, not a Stage136 primal proof. Preserve B Q/continue tie under dK=-1,dL=-112/129. First strict gap closure at t=6774079272730056/320084850611375, giving K136=840571992/1526537, L136=797676584/1526537, new P/continue tie D=(10,6,2), old B Q/continue tie. Exact 680-state check again yields 1238 positive gaps, min 3073199/82432998. Stage136 full-real primal interval is UNPROVED.

Inputs: GLOBAL_KNOWLEDGE_V1 frozen main@7b33f8066e9993e7c941959a9d738ed405248eb8, initial Enterprise Math ref@e27e64dfe4803804ff84c9ca75d83da4cc38459b, verified Stage134 Git blob a3617b8862c92ef97090babe549309642f748597. P000 is retained as an internal starting axiom; the auxiliary iid model supplies no P000 or physical bridge.

GitHub authenticated login awdawmip. Native task inventory returned CONTROL_QUOTA and native session creation was explicitly rejected STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No actual active native owner/CLAIM, Source-native Result, Driver review or mathematical admission is asserted. Next mathematical unit is Stage136's literal first-hit B/D weights, cone relation, four-observer affine compensation and exact full-real interval.
