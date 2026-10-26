# Stage161 — all-real exact Bellman optimum, external N14 ternary iid model

**Status:** AUTHOR exact-rational computation-assisted proof; neither an independent Driver review nor a native Source Result, CLAIM, P000/X6 theorem or physics claim. Scientific input: prior Stage160 author proof at EM main@27b1841affa8abfc3c6c1dd279bb8498c074ed2c. This author's fixed starting references: GLOBAL_KNOWLEDGE_V1 main@134b0caf1925b2afd23722eb5766773a91fc5b01 and EM initial main@a498621ae6f31397d695d690d4ff19dc0ea96ebe. The complete P000 projection matches original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. The ACTIVE worldview and current portable-research protocol were consulted. GitHub-connected identity: awdawmip, admin. Native owner query: CONTROL_QUOTA; native session start: STATIC_READONLY_SCOPE_DENIED, operation_sent=false. This source record does not invent a live Researcher session or owner/claim.

## Problem and theorem

N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) iid over three distinct ordered symbols. A policy may use every ordered history and randomization, stopping by depth 14. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and
V14(alpha)=min{max(tP,tQ): eP<=alpha,eQ<=alpha}.

Inherit Stage160's author-certified endpoint:
alpha160=381586508350717329445/1096459521159585595392
V160=13167218152253362815857/1096459521159585595392.

For **every real** 0<=delta<=eta161 where

eta161 = 4901851558287759506275/16880359814758873436258304,

the exact value is

V14(alpha160+delta)=V160-(330721685/554801)*delta.

The sharp new endpoint is

alpha161=440625016346358918245/1265046575011281764352,
V161=2138967403739208846181/180720939287325966336.

The same dual support is strictly below the true V14(alpha) for **every** alpha>alpha161. A new support ray may replace it; no blanket affine claim beyond this interval is made.

## Universal dual certificate

State=(n,a,b), a counts symbol 0 and b symbol 1. The P-based likelihood ratio is Q/P=2^(a+b)/3^a. Set K=168193485/554801, L=162528200/554801, and use the exact backward recursion

H(n,a,b)=min {K*2^(a+b)/3^a [decide P],
              L [decide Q],
              1+P0*H(n+1,a+1,b)+P1*H(n+1,a,b+1)+P2*H(n+1,a,b) [continue, n<14]}.

At depth 14 only terminal actions exist. Exact Fraction enumeration of all 680 states gives two and only two ties:
J=(10,2,0): P versus continue;
R=(10,0,1): Q versus continue.
There are 1238 strictly positive nonminimal action gaps, smallest 1055356088281/238554274922496, no negative gaps. The exact root is
H(root)=555836388520164056590937/2532690659733953052672.

For any full-ordered-history policy, change of measure and Bellman induction yield
H(root)<=tP+K*eQ+L*eP<=max(tP,tQ)+(K+L)*alpha.
Here K,L>0 and K+L=330721685/554801. The inequalities are valid for randomized behavioral policies, not only count-state policies.

## Ordered BRC observer law and four-corner evidence

BRC carrier: distinct ordered prefixes carrying P and Q positive rational weights, stopping/decision label and provenance. The full-history law is retained before compressing to iid counts. For the declared observer (eP,eQ,tP,tQ) and declared future conditional iid suffix operations, all equal-count prefixes have identical likelihood ratio and suffix law. This is a four-observer quotient only, not a general native P000 quotient.

Under the strict Bellman actions outside the two ties, literal unmerged ordered integer-weight DFS gives:
J: 45 true first hits; P mass 1953125/11943936; Q mass 1953125/26873856.
R: 10 true first hits; P mass 9765625/120932352; Q mass 9765625/60466176.

At the same depth 10 the states J and R have distinct counts, hence the ordered prefix cones are disjoint; neither can descend from the other. Therefore their coin effects have no mixed interaction. Let j be the probability of immediate P at J and r the probability of immediate Q at R. For M=(eP,eQ,tP,tQ),

M(j,r)=M00+j*dJ+r*dR,

M00=(610396466270800655/1752976676930715648,
     6975157942835/20061226008576,
     2640775790463380201/219122084616339456,
     154719000766399/13374150672384);

dJ=(-3201171875/3962711310336,
     771484375/557256278016,
     -30224609375/165112971264,
     -4150390625/46438023168);

dR=(4521484375/1486016741376,
     -3232421875/1253826625536,
     -61181640625/557256278016,
     -20751953125/104485552128).

The complete four deterministic corners were calculated twice: (1) exact count-state conditional-suffix Fraction recurrence and (2) literal unmerged integer-weight ordered-history DFS using P=(3,1,20)/24 and Q=(1,1,10)/12. All coordinates agreed; the ordered DFS visited 484744, 484504, 483664, 483424 nodes respectively at corners 00,01,10,11; separate P and Q terminal mass sums equal exactly 1. The mixed vector M11-M10-M01+M00 equals (0,0,0,0). No signed/phase cancellation is inferred from positive branch masses.

## Every-real primal attainment and sharpness

Exact error balancing eP=eQ yields

j(r)=107743801834549/461157120000000+(923720/360279)*r.

The admissible segment is

0<=r<=rmax=353413318165451/1182361600000000,

where j(0) is strictly between 0 and 1 and j(rmax)=1. All intervening coin probabilities are legal. The common error is strictly increasing in r, from alpha160 at r=0 to alpha161 at rmax. Both observed expected stopping-time gaps tP-tQ remain strictly positive, since their exact affine endpoint values are

left: 505710367439141258645/1096459521159585595392,
right: 526231060559760430495/1265046575011281764352.

At both endpoints, exact calculation verifies tP+K*eQ+L*eP=H(root); by affine dependence it holds everywhere on the real segment. Thus max(tP,tQ)=tP and these feasible policies reach the universal dual lower bound at every real alpha in the stated interval, proving the theorem.

To show sharp right endpoint, note that the finite-horizon full-history behavioral policy space is compact (finite product of simplices), with continuous observers, so an optimum exists. Equality with this same dual support at alpha>alpha161 would force both errors to equal alpha (K,L>0), the tP-dominant equality and Bellman-optimal decisions at all positive-mass reached prefixes. The strict-gap certificate leaves only J/R ties. Since equal-count prefixes have constant P/Q likelihood ratio and suffix law, any history-dependent tie coins can be replaced by P-weighted average coins preserving exactly these four observer outputs. Their disjoint cones force the displayed affine M law. Equal errors then imply j=j(r), and j<=1 restricts r<=rmax; the maximum common error is alpha161, contradiction. Hence the same support is strictly unattainable to its right.

## Validation and next unit

Two structurally different author algorithms were executed locally with exact rational arithmetic; see VERIFY_STAGE161.py and certificate161.json, including the 680-state census, all ordered first hits, four corners, mixed-zero check, entire interval endpoints and equal dualities. This is AUTHOR computation-assisted evidence, not independent Driver validation. No source-native RESULT or independent acceptance is claimed. Native owner and CLAIM remain unverified due to the observed read/control restrictions.

Further author exact dual scanning from this endpoint gives a Stage162 DUAL-ONLY candidate, along the R-preserving ray dK=-1,dL=-10592/12501. First strictly positive affine gap closure at t=4397668819866927/3265678040893931 gives K162=1776538556208/5886215131, L162=5152927839848/17658645393, with R=(10,0,1) Q/continue and new X=(7,3,3) Q/continue tied. The 680-state exact scan reports 1238 positive gaps, minimum 1055356088281/183084835434624. Stage162's primal real interval is OPEN. See SCAN_STAGE162.py and NEXT_TASK_PACKET_162.md.

Research scope remains the external finite iid model, not a theorem for native P000/X6 Cell geometry, its 3D slices, or physical time.