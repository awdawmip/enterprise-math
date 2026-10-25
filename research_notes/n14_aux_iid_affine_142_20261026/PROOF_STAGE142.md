# Stage142 — full-real affine optimum and sharp endpoint (author proof)

**Status**: author computation-assisted proof for an **external finite ternary iid sequential-test model**. No native P000/X6 transfer, Research Driver review, formal Task CLAIM or Result is asserted.

## Exact model and theorem

Let N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Any randomized policy may depend on its **complete ordered ternary prefix**, but must stop by time 14. Put eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau, and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

Stage141's inherited author endpoint and this stage's exact constants are

~~~
alpha141 = 12238132337992249925/35205614928358539264
V141     = 72273275560058390723/5867602488059756544
eta142   = 4379128349365/366725155503734784
alpha142 = 12238552734313788965/35205614928358539264
V142     = 24070360310471940161/1955867496019918848
K142     = 395290882339224/875825669873
L142     = 54591710813272/125117952839
K142+L142= 777432858032128/875825669873
~~~

**Theorem:** For **every real** delta with 0<=delta<=eta142,

V14(alpha141+delta)=V141-(777432858032128/875825669873)*delta.

The displayed supporting line is **strictly lower** than V14(alpha) for every alpha>alpha142; right sharpness does not imply infeasibility beyond alpha142.

## Dual Bellman lower bound

At count state s=(n,a,b), where a,b count observations of symbols 0,1, the likelihood ratio is r(s)=Q(s)/P(s)=2^(a+b)/3^a. The admissible Bellman actions are P-decision with cost K*r(s), Q-decision with cost L, and (if n<14) continuation with cost 1+sum_j P_j*H(child_j). At K=K142,L=L142 an exact Fraction bottom-up enumeration checks **all 680 count states**, obtains

~~~
Hroot=20527217718648439652667729706057/63970915514357897417453469696
~~~

and the **only** ties B=(11,0,1): Q/continue and J=(4,3,0): P/continue. Exactly **1,238** other action gaps are strictly positive, no negative gaps, minimum strict gap

145705394717149261/3309864318741169728.

Conditional backward induction yields for *every* ordered-history randomized policy

Hroot <= tP + L142*eP + K142*eQ
      <= max(tP,tQ)+(K142+L142)*alpha.

The sufficiency of counts is proved by iid suffix law and likelihood ratio, and is used only to compute the dual: it does not restrict the competing policy class to count-Markov.

## Literal first hits; observer identity and zero interaction

J has depth 4 with three symbol-0 observations; B has depth 11 with zero symbol-0 observations. Counts do not decrease, so J cannot precede B, and B cannot precede J by depth. Their literal ordered prefix cones are disjoint.

A separate forward integer-weight DFS (P numerator factors 3,1,20 over 24^n; Q factors 1,1,10 over 12^n) finds:

| tied state | first-hit literal words | P mass | Q mass |
|:--|--:|:--|:--|
| B | 11 | 107421875/1451188224 | 107421875/725594112 |
| J | 4 | 5/768 | 5/2592 |

The carrier retains each ordered prefix, branch identity, multiplicity and positive rational mass (BRC-like usage); the count quotient is valid here for precisely the declared iid four-observer map M=(eP,eQ,tP,tQ). This is *not* a native Heartbeat/BRC–Shor operation.

Let w be the immediate Q-stop probability at B, and h the immediate P-stop probability at J; all other states use their strict Bellman action (in particular old Y is **fixed** P-stop). Four-corner exact evaluation yields

~~~
M(w,h)=M00+w*dB+h*dJ
M00=(
 2428854327866793209/7011906707722862592,
 447683882606041/1283918464548864,
 10843896971689477751/876488338465357824,
 1272910772511773/106993205379072)
dB=(
 4619140625/2229025112064,
 -751953125/417942208512,
 -25673828125/278628139008,
 -17939453125/104485552128)
dJ=(
 -880699823005/24346898290704384,
 239462825/4458050224128,
 -8582550517565/1014454095446016,
 -10561381045/3343537668096).
~~~

The mixed-corner defect M(1,1)-M(1,0)-M(0,1)+M(0,0)=(0,0,0,0) **exactly**. Bottom-up Fraction and an independent literal forward integer-weight DFS agree on each deterministic corner; the DFS visited respectively **643270,643138,621718,621586** prefix nodes for (w,h)=(0,0),(1,0),(0,1),(1,1).

## Primal construction for all real alpha

Solving eP=eQ gives exactly

~~~
w(h)=48289749016996117/81438720000000000
    +(3939275036289/169664000000000)*h.
~~~

w(0)=48289749016996117/81438720000000000 and w(1)=50180601034414837/81438720000000000 are strictly between 0 and 1, so the policy is valid for **every real h in [0,1]**. Its errors satisfy

eP=eQ=alpha141+eta142*h.

At h=0, (alpha,tP)=(alpha141,V141); at h=1, (alpha,tP)=(alpha142,V142). The two endpoint values of tP-tQ are strictly positive:

~~~
h=0: 82703143791980924407/158425267177613426688
h=1: 82155858325532762167/158425267177613426688.
~~~

Since tP-tQ is affine, tP remains the maximum throughout. Direct exact verification at both endpoints gives tP+L142*eP+K142*eQ=Hroot, hence this equality holds throughout. The policy therefore **attains** the universal dual lower bound for all real h, proving the theorem.

## Strict right sharpness

The finite-horizon randomized strategy space is a product of finite simplexes, hence compact, and expected errors and times are continuous. Assume alpha>alpha142 attained the same support line. Positive K,L and equality in both dual inequalities force eP=eQ=alpha and action choices restricted to the two tied states on every positive-mass reachable prefix, since all other action gaps are strictly positive. Each tied state's ordered histories have the same likelihood ratio and iid continuation; disjoint cones imply that any prefix-specific randomization has the same four observations as an effective pair (w,h) in [0,1]^2. Error equality forces the displayed w(h), and then alpha=alpha141+eta142*h<=alpha142, contradiction. Hence the right endpoint is sharp.

## Evidence and next frontier

Actually executed locally: exact Fraction Bellman and four observer corners; separate integer-weight literal-prefix DFS for all four corners; exact next-dual ray scan. The source-stored portable verifier and author certificate carry the inputs and assertions, but **GitHub storage is not remote execution**. Stage143 is presently a **dual-only candidate**, not a proved primal theorem.

Source snapshot pinned GLOBAL_KNOWLEDGE_V1 main@596508231dcc5d8cf66c6b991a311dd5d89c2ba0, Enterprise Math input main@c5902704247dcbecf47b24981935c623db607653. GitHub account awdawmip has ordinary source write access. Native control list failed CONTROL_QUOTA; native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Active owner, native Researcher session, CLAIM, Result and independent Driver review **remain unverified**. The P000 six-axis Cell world and its three-dimensional slice are unchanged; no native transfer map is asserted.

Next exact open unit: NEXT_TASK_PACKET_143.md.
