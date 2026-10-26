# Stage163 — entire real interval and strict right-hand sharpness (author exact)

Status: AUTHOR_EXACT_COMPUTATION_ASSISTED / NO_NATIVE_CLAIM / NOT_ADMITTED.

**Scope and provenance.** External finite-N ternary IID sequential decision model, not the P000 six-axis native Cell space. Frozen upstream: R2 Stage162 author commit `21ddd4fc14d9ee9cc38e9b54e4bfaa6f6dac70e9`. This work keeps distinct ordered histories and both positive P/Q branch masses until a suffix-state equivalence is justified.

Under P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), decisions P/Q/continue may randomize on the *full ordered history* before or at horizon 14. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau; define V14(alpha)=min(max(tP,tQ): eP,eQ<=alpha).

## Exact theorem

Let

K = 163900037061/554150611,
L = 476600779976/1662451833,
m = K+L = 138328698737/237493119.

Let the inherited Stage162 endpoint be

A=440625031179621048365/1265046575011281764352,
B=2138966145833987829541/180720939287325966336,

and eta=69268826375/26145969225596928. Then for **every real** 0<=delta<=eta:

**V14(A+delta)=B-m*delta.**

The exact endpoint is

alpha163 = 440628382682516376365/1265046575011281764352,
V163 = 2138687275177334037541/180720939287325966336.

Furthermore the particular lower-support line H-m*alpha cannot attain equality for ANY alpha>alpha163. This statement does not assert that V14 itself stops beyond the endpoint.

## Universal Bellman lower support

Count state s=(n,a,b) has n draws, a type-0 and b type-1; the type-2 count is n-a-b. Because all letters have positive P/Q probabilities, the likelihood ratio on *any ordered history* at s equals ell(s)=2^(a+b)/3^a. Let H_s be the backward recursion:

H_s = min{ K*ell(s), L, 1+sum_i P_i*H_(s+e_i) }

with continuation omitted at n=14. Stop-P, stop-Q and continue are the three actions. For arbitrary full-history policies, exact backward induction gives tP+K*eQ+L*eP >= H_root; therefore V14(alpha) >= H_root-(K+L)*alpha.

Exact Fraction arithmetic over sum_(n=0)^14 (n+1)(n+2)/2 = **680** states gives

H_root=9776752862063305564417447471/45534988902651828797177856.

Exactly two count states have ties:

* R=(10,0,1), decide Q / continue;
* Y=(8,4,1), decide P / continue.

The other nonoptimal action gaps number **1238**; every gap is strictly positive, with minimum 1577397669610597/79424873185738752. No floating point or sampling is used. The executable verifier accompanying this note reruns the recurrence, not a hardcoded outcome lookup.

## Preserve the ordered branch histories

Let r be the probability of deciding Q at R and y the probability of deciding P at Y; otherwise choose the unique Bellman-minimal action. Define the four-component observer M(r,y)=(eP,eQ,tP,tQ).

A literal ordered-prefix integer-weight DFS and an independent count-state Fraction suffix recursion agree exactly on all four deterministic corners (r,y)=(0,0),(0,1),(1,0),(1,1). Their DFS node counts are respectively 473080,445864,472840,445624, total **1837408**. The integer P branch weights are (3,1,20)/24 and Q branch weights are (1,1,10)/12, and each terminal mass sums to 1 under both measures.

First-hit prefixes at R: 10 distinct ordered histories; P mass 9765625/120932352, Q mass 9765625/60466176.

First-hit prefixes at Y: 168 distinct ordered histories; P mass 875/884736, Q mass 875/2239488.

These prefix cones cannot overlap: Y has depth 8 with four type-0 letters whereas R has depth 10 with zero type-0 letters. Thus

M(r,y)=M00+r*dR+y*dY, with exact mixed difference M11-M10-M01+M00=(0,0,0,0).

The complete observer vectors are:

M00=(608980572829895015/1752976676930715648, 28011719403025/80244904034304, 2600662244346814961/219122084616339456, 17058155693101/1486016741376).

dR=(4521484375/1486016741376,-3232421875/1253826625536,-61181640625/557256278016,-20751953125/104485552128).

dY=(-615115375/84537841287168,36976625/3343537668096,-4173890875/3522410053632,-5606125/10319560704).

These assertions are explicitly recorded in the local `certificate163.json` and checked by its generator.

## Construct an optimal policy for EVERY real alpha in the interval

The linear equality eP=eQ forces

r(y)=1766864861392271/5911808000000000
     +(430465623/131960000000)*y.

For every **real** y∈[0,1], 0<r(0)<r(y)<=r(1)<1 (endpoint inequalities understood appropriately); both coins are legal. At y=0, r(0) matches the inherited Stage162 R coin and M=(A,A,B,tQ). Along the balance line, the common error grows strictly as

alpha(y)=A+eta*y.

At y=1 the exact result is alpha163 and tP=V163. The inequalities tP>tQ hold at both ends, with exact positive time gaps

left: 526240831439401052735/1265046575011281764352,
right: 525795582839779772735/1265046575011281764352.

Both time gaps and the dual equality tP+K*eQ+L*eP=H_root interpolate affinely in y. Thus each point meets both error constraints, has max(tP,tQ)=tP, and saturates the universal Bellman lower bound. This proves the theorem on the **entire real interval**, not on a grid.

## Sharpness of this Bellman support (not value-function termination)

For any alpha>alpha163, if equality with the *same* H_root-(K+L)*alpha held, positivity K,L would force both errors equal alpha and zero use of positive-gap actions; all reached choices must be Bellman-minimal. The finite policy space is compact, so equality must be attainable by some randomized full-history behavioral policy if optimal.

At either tie, all ordered first-hit prefixes share the same conditional IID suffix law and the same P/Q likelihood ratio; replacing prefix-dependent tie coins by their P-mass-weighted average leaves all four observers unchanged. The two first-hit cones are disjoint, so any potential equality-attaining full-history policy is observer-equivalent to some M(r,y), with r,y in [0,1].

Balancing the errors forces r=r(y) and the balanced common error grows strictly with y; its maximum on y∈[0,1] is alpha163. Contradiction for any larger alpha. Hence the *same* support line is strictly unattainable past alpha163.

## Verification, evidence and next question

Author validation: exact 680 Bellman states, 1238 positive gaps, four full-history deterministic corners checked by two structurally distinct algorithms, 1837408 literal ordered prefixes, exact positive P/Q mass normalization, zero mixed effect, valid continuous probabilities, dual equality, and endpoint strictness. No independent Driver validation, formal Source Result, CLAIM, native-P000 transfer or Stage164 primal theorem is claimed.

The Stage164 *dual-only* next candidate, with R kept tied and Y made strict, is K=211248/725, L=615448/2175; ties R=(10,0,1) (Q/C) and Z=(13,5,2) (P/C), 1238 other positive gaps. The next unit is to compute the exact two-tie first-hit observer, solve error balance, and prove or refute a full-real primal segment. This is separate from Stage163 acceptance.

The full replay capsule, including the **executed** `VERIFY_STAGE163.py`, all exact JSON/console records, `SCAN_STAGE164.py`, proof and Stage164 task packet, is available in the same research directory after final publication. The local handoff also contains the original complete documents and manifest.