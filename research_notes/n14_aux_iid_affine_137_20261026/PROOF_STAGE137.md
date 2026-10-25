# Stage137 | N14 full-real exact optimal affine interval and right-sharpness — author theorem

Status: **AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF**. Two independently implemented local author checkers passed; formal independent Research Driver review, native Researcher session/CLAIM/Result and P000-X6 transfer are NOT established.

## Model, parameters, and exact theorem

The *external auxiliary* finite ternary iid sequential test takes independent symbols under P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), with at most N=14 observations. Strategies may depend on every literal ordered observed prefix, randomize stopping/decision, and must declare P or Q by N. Let eP=P(declare Q), eQ=Q(declare P), tP=E_P[tau], tQ=E_Q[tau], and V14(alpha)=min max(tP,tQ) over eP,eQ<=alpha.

Stage136 author theorem supplied alpha136=12235904656867465565/35205614928358539264 and V136=72642934423754220803/5867602488059756544.

Use exact dual coefficients K137=214326/401 and L137=203912/401, sum S137=418238/401. Put eta137=121452875/412565799941701632.

**Theorem. For every real delta with 0<=delta<=eta137,**

V14(alpha136+delta) = V136 - (418238/401)*delta.

The new right endpoint equals

alpha137 = 36707714001694332695/105616844785075617792,

V137 = 653786393599537203227/52808422392537808896.

**Right sharpness:** The *same supporting affine line* ceases to equal V14(alpha) for any alpha>alpha137. This does not assert nonexistence of feasible tests for larger alpha.

## Universal Bellman lower bound

At state s=(n,a,b), where a and b are counts of symbols 0 and 1, likelihood ratio Q/P equals r(s)=2^(a+b)/3^a. The exact P-weighted conditional Bellman cost is

H(s) = min { K137*r(s) [declare P], L137 [declare Q], 1+ (1/8)H(n+1,a+1,b) + (1/24)H(n+1,a,b+1) + (5/6)H(n+1,a,b) [continue, only n<14] }.

At depth N continuing is excluded. Exact rational backward recurrence covers all 680 count states. Of 1240 nonselected-action comparisons, exactly 1238 gaps are strictly positive, zero negative, and precisely two equalities remain:

- B=(11,0,1): declare Q / continue.
- G=(13,6,4): declare Q / continue.

Minimum strictly positive gap = 1/173232. Root H0=2744968460634070393271/7322329660929343488.

Because the conditional suffix laws under each hypothesis and their likelihood ratio are count-sufficient for these four specified observables, Bellman induction yields a lower bound for **all literal history-dependent randomized policies**, not just count strategies:

H0 <= tP + L137*eP + K137*eQ <= max(tP,tQ)+(K137+L137)*alpha.

Thus V14(alpha)>=H0-S137*alpha for every feasible alpha.

## Literal-history BRC carrier and exact four-observer family

Each literal first-hit prefix is kept with ordered word identity, stopping depth and separate positive exact P and Q branch mass prior to the count quotient. The two author implementations use (i) bottom-up Fraction observer recurrence and (ii) an independent top-down integer-weight DFS using P weights (3,1,20)/24 and Q weights (1,1,10)/12.

Tie first-hit data (actual ordered-prefix counts):

B=(11,0,1): 11 words; P mass 107421875/1451188224; Q mass 107421875/725594112.

G=(13,6,4): 9692 words; P mass 302875/4696546738176; Q mass 302875/3343537668096.

Their continuation cones are disjoint: B has zero symbol-0 observations at depth11, but G has six symbol-0 observations at depth13, so B cannot precede G on a word; and G (depth13) cannot precede B (depth11). Thus two tie controls have no mixed interaction.

Define w=probability of immediately declaring Q at B (versus continuing); z=probability of **continuing** at G (versus declaring Q), with each in [0,1]. All other decisions use the unique Bellman-minimizing action. For M=(eP,eQ,tP,tQ),

M(w,z) = M00 + w*dB + z*dG,

where the *exact rational* coefficients are

M00=(
2430334710555814769/7011906707722862592,
447296761371541/1283918464548864,
10888421472377759711/876488338465357824,
1274918249920433/106993205379072
);

dB=(
4619140625/2229025112064,
-751953125/417942208512,
-25673828125/278628139008,
-17939453125/104485552128
);

dG=(
-302875/37572373905408,
302875/40122452017152,
302875/4696546738176,
302875/3343537668096
).

Both author algorithms agree at all four deterministic corners M00,M10,M01,M11. In particular M11-M10-M01+M00=0 exactly. Independent DFS visited-prefix counts at corners (w,z)=(0,0),(1,0),(0,1),(1,1) respectively: 680548, 680416, 709624, 709492, with 453699,453611,473083,472995 terminals.

BRC resolution: **REUSE_APPLIED** — positive-rational labeled ordered branches, observer-sufficient iid quotient only for (eP,eQ,tP,tQ) and finite horizon, no signed cancellation or native-X6 transfer.

## Attainment throughout all real delta and endpoint

Solving eP=eQ for w yields the exact unique compensation law

w(z) = 3409636967625767/7403520000000000 + (186571/46272000000)*z, 0<=z<=1.

Both w(0) and w(1)=1136555606328589/2467840000000000 belong strictly to (0,1). Exact substitution gives, for every real z in [0,1]:

eP=eQ=alpha136 + eta137*z,

tP=V136 - (418238/401)*eta137*z.

The exact endpoint gaps tP-tQ are 86109683330236204807/158425267177613426688 at z=0 and 28703243336799108269/52808422392537808896 at z=1. Both are strictly positive, so tP>tQ for the whole real segment by affineness. The Bellman equality actions attain H0=tP+L137*eP+K137*eQ at all z. Combining primal attainment and universal dual bound proves V14(alpha) exactly over the stated entire real interval, not merely rational sample points.

At z=1 the new G tie is fully continued; the old B stopping randomization w remains internal.

## Sharpness of this particular supporting line

Suppose this supporting line stayed equal to V14(alpha) at some alpha>alpha137. The finite-horizon behavioral strategy space is compact and the minimum is attained. Equality in

H0 <= tP+L137*eP+K137*eQ <= max(tP,tQ)+S137*alpha

with K137,L137>0 forces both errors to equal alpha, and any positively visited action must Bellman-minimize. Every other action has strictly positive gap, hence only B/G ties may randomize. At a fixed tie count, all positive-probability first-hit prefixes share identical Q/P ratio and both conditional suffix laws; mass-average their history-dependent decisions, preserving all four observables. The disjoint tie cones force the exact M(w,z) family. Equal errors force w=w(z), while alpha=alpha136+eta137*z and 0<=z<=1. Therefore alpha<=alpha137, contradiction. Thus the old supporting line is right-sharp.

## Next exact Stage138 dual candidate only

From the Stage137 sharp edge, preserve B's Q/continue tie along direction dK=-1,dL=-112/129. The G Q/continue tie breaks toward continuation. The first positive gap reaches zero at t=6966/2783341, giving

K138=3709800/6941, L138=3529544/6941.

New H=(11,4,1) declare P/continue tie and old B Q/continue tie; fresh 680-state check gives 1238 strictly positive gaps, min gap 4/187407 and root 190052304168624227306189/506975463107337388032. **Stage138 is DUAL_CANDIDATE_ONLY**: no primal interval, endpoint or sharpness has been proved.

## Provenance, verification and authority

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@56d2c838ada2338ab606ffdf76cad21738a8b258, Enterprise Math source main@35542fad3bdf95e3b06f7b13ddf2952f386b2286 and Stage136 proof/blob from research_notes/n14_aux_iid_affine_136_20261026 at project commit 9e6c9c530195161a5282bdcbdf67eef0f5800d43. P000 startup projection matched original canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE residual-faithful worldview and current portable research protocol applied.

Actually executed: Stage137 bottom-up Fraction main program PASS; independent literal integer-prefix DFS PASS; Stage138 exact directional scan PASS (candidate only). Author calculations, not independent Research Driver mathematical review. GitHub readback of published code/certificates does not imply remote code execution.

Current native control inventory attempt: CONTROL_QUOTA. Native session start denied STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Real native Owner/CLAIM could not be verified, no formal Researcher session/Source Result, no independent review or accepted theorem. These author artifacts do not claim project acceptance or physical reality. The external iid model has no established embedding/readout/relation preserving bridge to P000 native six-dimensional Cell space and 3D slice. Worldview/P000 remain unchanged.

Next runnable unit: Stage138 B/H ordered first-hit masses, cone structure, four-corner observer family, real alpha interval or no-go, support sharpness; retain author/source evidence and await genuinely independent review.
