# Stage113 — exact real-affine optimum in the external ternary iid N=14 model

**Evidence level:** AUTHOR_EXACT_FINITE_PROOF; two author-side exact arithmetic implementations (one literal ordered-history DFS). Not an approved Research Driver review, native CLAIM/Result, P000 or X6 theorem.

**Fixed before research:** GLOBAL_KNOWLEDGE_V1 main@28a36bed4c273c46df19f5e267650a7429b06cb1; Enterprise Math main@3815d50ef89ab52b99f046252d90afe21ca926b3; P000 canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Consume Stage112 author proof in research_notes/n14_aux_iid_affine_112_20261025/PROOF_STAGE112.md, not an independent native Result.

## Model and theorem

At most 14 iid symbols from P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6); policies may depend on the complete ordered history, with randomized stopping and decisions. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), V14(alpha)=inf max(tP,tQ) subject to eP,eQ<=alpha.

Reuse alpha112=13084629132464364707/37682150988866125824 and V112=1930486644885404154985/150728603955464503296, with u112=66372737348901/70438400000000 the P-stop probability at A=(10,3,0). The Stage112 right policy **continues** at C=(5,2,3).

Define K113=814106972531223/875100809116, L113=189992854025880/218775202279, S113=K113+L113=1574078388634743/875100809116, and eta113=218775202279/19538893105337991168.

**Theorem.** For *every real* 0<=delta<=eta113,

    V14(alpha112+delta)=V112-S113*delta.

The exact right endpoint is

    alpha113=183184813761431567431/527550113844125761536,
    V113=27026770528279165031729/2110200455376503046144.

This supporting line cannot attain equality for alpha>alpha113; the value function itself is not claimed to terminate.

## Universal Bellman certificate

At count s=(n,a,b), R(s)=Q/P=2^(a+b)/3^a. With conditional P-weighted continuation,

    H(s)=min{K113*R(s), L113, 1+(1/8)H(n+1,a+1,b)
                        +(1/24)H(n+1,a,b+1)+(5/6)H(n+1,a,b)}

(the continue action is absent at n=14). Exact rational enumeration of all 680 count states and 1240 nonselected-action comparisons finds 1238 strict positive gaps, two zeros, no negative gaps; minimum positive gap 3797211181/1312651213674. The *only* tie states are A=(10,3,0): P-stop/continue; C=(5,2,3): Q-stop/continue. Root H=954868914544086623189532573343/1498077449554244331091525632=V112+S113*alpha112.

At each literal ordered prefix, the likelihood and next-symbol probabilities depend only on counts. Bellman induction on the full prefix tree, with no count-only restriction on competing strategies, therefore proves

    H(root)<=tP+L113*eP+K113*eQ
           <=max(tP,tQ)+S113*alpha.

## Exact BRC-style ordered rational path carrier

The two tie cones are disjoint: C has depth 5 and three symbol-1 observations, while A has depth 10 and zero symbol-1 observations. C cannot precede A because this count cannot decrease; A cannot precede C because it is deeper. Literal ordered DFS gives first-hit counts A=120, C=6; exact P masses A=390625/5971968, C=1/147456; exact Q masses A=390625/20155392, C=1/41472. Preserve each literal word and its positive rational mass before the justified count observer is applied.

Let u=P-stop probability at A (otherwise continue), w=Q-stop probability at C (otherwise continue); all other states take their unique minimizing action. No mixed u*w term occurs in any root moment. The exact derivatives are:

|moment|d/du|d/dw|
|---|---|---|
|eP|-248046875/990677827584|102549331/2404631929946112|
|eQ|65234375/208971104256|-1498645/53496602689536|
|tP|-3012109375/41278242816|-3298748975/300578991243264|
|tQ|-417578125/17414258688|-16132121/495338913792|

eP=eQ requires exactly

    u(w)=u112+(123866061659/986137600000000)*w.

For every 0<=w<=1 this is a legal probability; u(1)=929342188946273/986137600000000<1. Substitution gives

    eP=eQ=alpha112+eta113*w,
    tP=V112-S113*eta113*w.

At w=0, tP-tQ=32262304609783850035/50242867985154834432>0. At w=1, tQ=1604482572142993109465/131887528461031440384 and tP-tQ=451683124663758426763/703400151792167682048>0. The moment difference is affine, hence tP>tQ everywhere between the endpoints. The constructed policy therefore reaches the full-history Bellman lower bound for all real w in [0,1], proving the theorem.

## Sharpness, including arbitrary history-dependent choices

The feasible full prefix-tree realization measure space is compact. Attaining the *same* dual support line at alpha>alpha113 would force eP=eQ=alpha because K113,L113>0 and all used positive-mass actions Bellman-minimizing. Only the two ties A/C can randomize. Constant Q/P ratio over the literal histories entering a fixed count state implies that every history-dependent randomization has an equivalent P-first-hit-weighted aggregate parameter for both P/Q effects. The tie cones are disjoint, so these aggregates are u,w in [0,1] and the above moment equations are exact. Their balance forces alpha=alpha112+eta113*w<=alpha113, contradiction. Right-sharpness is proved for this support face, not for V14 beyond it.

## Actual validation, provenance and next unit

Two separately implemented author-side exact procedures passed: a Fraction Bellman + forward rational-mass checker and an independent integer-weight **literal ordered DFS** at the four deterministic corners (u,w)=(0,0),(1,0),(0,1),(1,1). The latter visits 889909, 886309, 884347, 880747 ordered nodes; finds A 120, C 6; independently obtains all derivatives and exactly zero interactions. No floating-point evidence is used. This is not independent Driver review or formal Lean verification.

**Stage114 is dual-only:** along L(K)=-185064/635+(21376/17145)K, the next decreasing K is 1903247523/2052316, L=443700120/513079; the new candidate D=(9,1,2) ties continue and Q-stop. The fixed-policy rational sweep finds 357 candidate downward gap zeros and picks the largest; exact Bellman at the candidate again yields only A/D ties and 1238 positive gaps. Reachability, mixed paths, primal interval and right sharpness remain unproved. See NEXT_TASK_PACKET_114.md.

Native em_control_tasks returned CONTROL_QUOTA. Native session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false), so active owner, native session, CLAIM, Result and independent admission were not obtained. This is a separately scoped GitHub **author research note**, not a formal Source-state-machine publication.
