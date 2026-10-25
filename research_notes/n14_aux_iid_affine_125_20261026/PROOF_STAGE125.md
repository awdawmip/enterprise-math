# R1 / N14 Stage125 — exact full-real optimal affine segment and right-sharpness

Status: AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF, not Research Driver reviewed. External finite ternary iid auxiliary model only, not the P000 native X6 world.

## Theorem
Let N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6); allow any randomized stopping and decision policy depending on the *full literal ordered history*. Define eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min max(tP,tQ) with both errors at most alpha.

From author-proved Stage124,
alpha124 = 2573845372952647230925/7411551152237344456704,
V124 = 377878009388672358128945/29646204608949377826816.

Put
K125 = 3579845625/4855672, L125 = 416181048/606959,
S125 = K125+L125 = 6909294009/4855672,
eta125 = 43094089/1647011367163854323712.

**For every real 0<=delta<=eta125**,
\[
V_{14}(\alpha_{124}+\delta)=V_{124}-S_{125}\delta.
\]
At the new endpoint:
\[
\alpha_{125}=\frac{5147690745905682308651}{14823102304474688913408},\quad
V_{125}=\frac{1511512037550274393644029}{118584818435797511307264}.
\]
The same affine supporting line cannot remain equal to V14(alpha) for alpha>alpha125. This says nothing about the existence of feasible policies beyond that support.

## Universal Bellman lower bound
For count state s=(n,a,b) with a,b the counts of symbols 0,1, the prefix Q/P likelihood ratio is 2^(a+b)/3^a. All ordered prefixes in that fiber share this ratio and the iid suffix conditional law. Thus Bellman minimization applies to *all literal-history policies* (not a count-policy restriction):
\[
H(s)=\min\{K125\,2^{a+b}/3^a,\ L125,\
1+\tfrac18H(n+1,a+1,b)+\tfrac1{24}H(n+1,a,b+1)+\tfrac56H(n+1,a,b)\},
\]
omitting continuation when n=14. Exact rational evaluation of all 680 states yields exactly 1238 positive nonchosen action gaps, zero negative gaps, and precisely two ties:
A=(9,3,0) P/continue and U=(12,7,5) Q/continue.
The least positive gap is 578968738307/115991671209984.
The root is H(0)=16854019707653693377319545/33249530339162194968576 = V124+S125*alpha124.

For every randomized literal-history policy,
H(0)<=tP+L125*eP+K125*eQ<=max(tP,tQ)+S125*alpha.
Hence V14(alpha)>=H(0)-S125*alpha.

## Literal positive-mass first hits and exact four observers
Under unique minimizers outside the ties, literal first hits are:
A: 84 ordered words; P mass 109375/1990656; Q mass 109375/6718464.
U: 142 ordered words; P mass 71/8349416423424; Q mass 71/4458050224128.

A cannot precede U on the same path: moving from depth 9 counts (3,0) to depth 12 counts (7,5) would require 9 counted increments in only 3 observations. U cannot precede A by depth. The tie cones are disjoint; no mixed randomization term occurs.

Let y=P-stop probability at A, otherwise continue, and w=Q-stop probability at U, otherwise continue. Let M=(eP,eQ,tP,tQ). Then for all reals y,w in [0,1],
M(y,w)=M00+y*dA+w*dU, with
M00=(
608919703452600011/1752976676930715648,
55715889515225/160489808068608,
2798007941169380921/219122084616339456,
161747615623729/13374150672384),
dA=(
-1921609375/7925422620672,
259765625/835884417024,
-20758609375/330225942528,
-1476453125/69657034752),
dU=(
71/534362651099136,
-71/641959232274432,
-71/7421703487488,
-923/53496602689536).
The root four-corner identity M11=M00+dA+dU was verified by two different exact author implementations, one directly iterating literal ordered prefixes with independent integer weights.

The exact error-balance line eP=eQ is:
\[
y(w)=151548960415319/415627392000000+
(2560757/5818783488000000)w,\qquad 0\le w\le1.
\]
Both endpoint y values are strictly within (0,1); the right value is 707228482791741/1939594496000000. Along this line:
eP=eQ=alpha124+eta125*w,
tP=V124-S125*eta125*w.
The strictly positive time margins (tP-tQ) at w=0 and w=1 are respectively
19564523009155753489121/29646204608949377826816,
26086030678453378424287/39528272811932503769088.
These quantities are affine in w; hence tP>tQ for every real w in [0,1]. All actions attain their Bellman minima, giving equality in the universal support bound at every alpha in the stated interval.

## Right-sharpness
At finite horizon the randomized literal-history policy space is compact. Equality to the above support at a greater alpha would force (positive K125,L125) *both* eP=eQ=alpha, and Bellman-minimizing actions at every positively reached prefix. Away from A/U every nonminimizing alternative has strict positive gap. Within a tie count fiber, all literal prefixes have identical iid conditional suffix laws and identical Q/P likelihood ratio. For exactly the four observers (eP,eQ,tP,tQ), prefix-specific randomization therefore averages to a scalar y or w; the A and U path cones are disjoint. Every equality-attaining observer vector is consequently of the above M(y,w) form. Balance imposes unique y(w), and alpha=alpha124+eta125*w<=alpha125 since w<=1. Contradiction. Thus the supporting line is right-sharp.

## Verification and boundaries
Primary author exact Fraction bottom-up Bellman/four-observer recurrence PASS. Second author independent top-down Bellman plus literal integer-weight ordered-history DFS PASS, 815542 / 814690 / 810502 / 809650 prefix nodes at corners 00/01/10/11. Sources, machine certificate and execution evidence are in this directory. GitHub storage/readback is not remote execution or independent mathematical review. BRC REUSE_APPLIED: positive rational ordered branch mass, multiplicity, provenance and an expressly limited iid four-observer quotient. No mapping to P000 native six-axis Cell world and no physical interpretation have been established.

Research snapshot: GLOBAL_KNOWLEDGE_V1 main@3c15f1c6ac3c2903a001243f93bc7a3bea145e63; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; initial EM Source main@658e1f3e8d592d635dfae1751b42d0d6ccbca598. GitHub actor awdawmip; native inventory CONTROL_QUOTA; native session STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No verified active owner, CLAIM, Result admission or independent Driver acceptance.