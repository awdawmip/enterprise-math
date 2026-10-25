# R1 / N14 Stage126 — exact full-real affine optimum and right-sharpness

**Claim grade:** AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF. Two different author algorithms pass; not independently Research Driver reviewed or admitted as native Result. This theorem concerns a *finite ternary iid auxiliary model*, not P000 native X6 Cell-space dynamics.

## 1. Model, inherited endpoint and new theorem

Let N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Policies may inspect every literal **ordered observation history**, stop at or before 14, and randomize stopping and terminal decision. Define eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau). Set
V14(alpha)=minimum of max(tP,tQ) subject to eP,eQ<=alpha.

The author-proved Stage125 endpoint is
alpha125=5147690745905682308651/14823102304474688913408,
V125=1511512037550274393644029/118584818435797511307264.

Put K126=387210888/527153, L126=359623016/527153,
S126=K126+L126=746833904/527153,
eta126=649645440960773356627/19052627495351466816700416.

**Theorem.** For **every real** 0<=delta<=eta126,
\[
\boxed{V_{14}(\alpha_{125}+\delta)=V_{125}-S_{126}\delta.}
\]
Exact new endpoint:
\[
\boxed{\alpha_{126}=\frac{18340838011402083499}{52808422392537808896}},\qquad
\boxed{V_{126}=\frac{335279238082246223695}{26404211196268904448}}.
\]
The *same supporting affine line* cannot extend right beyond alpha126. This is **support right-sharpness**, not global infeasibility.

## 2. Universal dual Bellman support over full ordered strategies

At count state (n,a,b), a and b are the numbers of observed symbols 0 and 1. The literal prefix Q/P ratio is r=2^(a+b)/3^a. The conditional iid suffix distribution and four stopping/decision observables depend on the count state; this justifies Bellman minimization *even for full-history policies*.

For each state define the minimum H(n,a,b) among: declare P with cost K126*r; declare Q with cost L126; if n<14 continue with 1+sum_j P_j H(child_j). A complete exact Fraction backward computation yields all 680 states, **1238 strictly positive nonchosen action gaps** and **no negative gaps**. The smallest strictly positive gap is 8171681291077/1813329127931904. Exactly two ties occur:
A=(9,3,0), actions P/continue, and
B=(11,0,1), actions Q/continue.

Root dual:
\[
H(0)=\frac{9717182964780466957407421}{19251810711959532208128}
=V_{125}+S_{126}\alpha_{125}.
\]
For every ordered-history randomized policy, Bellman gives
H(0)<=tP+L126*eP+K126*eQ
<=max(tP,tQ)+S126*alpha,
hence V14(alpha)>=H(0)-S126*alpha.

## 3. BRC typed ordered-first-hit masses and exact moments

We retain literal ordered prefix identities, positive rational P/Q masses, their multiplicity, and transition provenance before performing the **specific four-observer iid-preserving** state quotient.

At the unique minimizer policy away from ties, ordered first-hits are:

| Tie state | Literal first-hit words | P positive mass | Q positive mass |
|---|---:|---:|---:|
| A=(9,3,0) | 84 | 109375/1990656 | 109375/6718464 |
| B=(11,0,1) | 11 | 107421875/1451188224 | 107421875/725594112 |

The A/B ordered prefix cones are disjoint: if A at depth9 preceded B at depth11, symbol-0 count would have to **decrease** from 3 to 0; B cannot precede A by observation depth. Consequently, randomization produces **no mixed coefficient**.

Let y=P-stop probability at A (otherwise continue), w=Q-stop probability at B (otherwise continue), and M=(eP,eQ,tP,tQ). Then **for every real y,w in [0,1]**:
\[
M(y,w)=M_{00}+y\,d_A+w\,d_B
\]
with all exact vectors:
M00=(
1217839406905665853/3505953353861431296,
74287852686943/213986410758144,
5596015882334569363/438244169232678912,
646990462493993/53496602689536);
dA=(
-1921609375/7925422620672,
259765625/835884417024,
-20758609375/330225942528,
-1476453125/69657034752);
dB=(
4619140625/2229025112064,
-751953125/417942208512,
-25673828125/278628139008,
-17939453125/104485552128).

Two *author*-independent algorithms check all four corners and M11=M00+dA+dB: a bottom-up Fraction Bellman/moment recurrence and a separate top-down Bellman with literal ordered-prefix integer weight DFS, respectively.

## 4. Full real primal interval and new saturation boundary

The unique error balance eP=eQ gives
\[
\boxed{
y(w)=\frac{707228482791741}{1939594496000000}
+\frac{53020000}{7576541}\,w.
}
\]
The coefficient is positive. Unlike Stage125, the B-randomization cannot reach w=1 while balancing errors legally: **A saturates first**. Exact bound:
\[
w_*=\frac{1-y(0)}{53020000/7576541}
=\frac{1232366013208259}{13573120000000000},\quad 0<w_*<1,\quad y(w_*)=1.
\]
For **every real** 0<=w<=w*, y(w) lies in [0,1]. Substitution gives exact identities:
eP=eQ=alpha125+eta126*(w/w*),
tP=V125-S126*eta126*(w/w*).
The endpoint time margins tP-tQ are:
left 26086030678453378424287/39528272811932503769088 > 0;
right 16916724390710645177/26404211196268904448 > 0.
By affineness, tP>tQ on the *whole real interval*. Every used action is Bellman-minimizing; the primal family attains the universal lower bound for each alpha.

## 5. Exact right-sharpness

The full literal-history randomized policy space is compact at finite horizon. If equality with this affine support held at alpha>alpha126, positivity of K126,L126 forces both error bounds to be saturated and all positively reached actions to minimize the Bellman dual. All other action alternatives have strictly positive gaps, leaving only A and B variable. Within one iid count state, the Q/P prefix ratio and conditional suffix laws for the four declared observables are constant, so literal prefix-specific tie randomizations can be averaged to a single effective y or w. Their cones are disjoint. Therefore any such equality policy has observer vector exactly M(y,w) for some legal [0,1]^2 pair, which by equality eP=eQ must obey the displayed balance law. The alpha reached increases with w; y<=1 forces w<=w*. Thus alpha<=alpha126, contradiction.

## 6. Verification, scope and handoff

VERIFY_STAGE126.py: exact rational bottom-up Bellman and four-corner observer checker, PASS. INDEPENDENT_ORDERED_STAGE126.py: independently written top-down Bellman plus literal full-prefix DFS with P integer numerators (3,1,20)/24 and Q numerators (1,1,10)/12, PASS. DFS node counts for corners 00,01,10,11: **814690, 814558, 809650, 809518**. Literal first-hit counts/masses and all four observer vectors agree exactly. Independently executed SCAN_STAGE127.py produces a **dual candidate only** at K127=8246448/11561, L127=7673768/11561, new tie (11,6,2).

BRC reuse: REUSE_APPLIED to typed positive rational literal branch weights, multiplicity, provenance and limited iid four-observer quotient. Not a P000 native X6 proof; physical or native correspondence remains unproved. Research activity and Source persistence are not native research-role registration, CLAIM, Result freeze or Driver acceptance.

Frozen start sources: GLOBAL_KNOWLEDGE_V1 main@3c15f1c6ac3c2903a001243f93bc7a3bea145e63; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Enterprise Math main@658e1f3e8d592d635dfae1751b42d0d6ccbca598. Authenticated GitHub login awdawmip. Native inventory returned CONTROL_QUOTA, native session registration STATIC_READONLY_SCOPE_DENIED with operation_sent=false; no verified active owner or formal CLAIΜ. Remote GitHub source readback validates stored bytes, not GitHub-side execution.
