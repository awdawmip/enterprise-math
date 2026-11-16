# R5 — Exact two-switch support structure for all signed-error directions in [-1/10,1/10]

Date: 2026-11-07 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance, fixed scientific domain

R5 frozen inputs: Global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate immutable predecessor: `586b0a6fdcb7db11ff825d6231fcb09bcf69e4f4`, `research_notes/brc_r5_signed_lambda_dual_20261107_t1336/RESEARCH.md`. The applicable current behavioral protocols are outside the scientific freeze. The object is the frozen four-stage P/Q-BRC likelihood-ratio observer, NOT a full native-X6 dynamics model. This work retains the seven stopped likelihood-ratio Q masses and their historical mixture provenance until the final four-observer map.

Mother question: Does the complete four-observer image O4(FULL_HIST) equal or differ from O4(seedless LR) when W=(eP,eQ,TP,TQ)? The present unit determines the exact entire one-parameter support function at TP=TQ=31/10 for lambda in [-1/10,1/10].

## Model and definitions

Take real flow (g,a,b,u,v,w,z) subject to 0<=a,b<=g<=1 and
C0=13a/40+b/80, C1=a/10+9b/40, C2=3a/40+21b/80;
0<=u<=C0, 0<=v<=C1, 0<=w<=C2, 0<=z<=a/10, 0<=v-z<=9b/40.
Times:
TP=1+g+(3a+5b)/8+u/2+v+3w/2,
TQ=1+g+(a+b)/2+u+v+w.
The seven increasing LR keys are r=(1/10,1/2,3/4,1,5/4,3/2,19/10).
Stopped Q masses are:

~~~
M0 = 509u/900 + 47z/180 + 67(v-z)/162 + w/100
M1 = C0-u
M2 = (g-a)/2
M3 = 1-g+C1-v+191(u+w)/450+43z/90+14(v-z)/81
M4 = (g-b)/2
M5 = C2-w
M6 = u/100+47z/180+67(v-z)/162+509w/900
~~~

Independent declared Q masses 0<=Ej<=Mj give eQ=sum Ej and 1-eP=sum rj Ej.
Seedless LR adds 9*b*z=4*a*(v-z), using literal degenerate cases where a*b=0.

Define U_lam=eQ-(1+lam)(1-eP). For each fixed flow, declarations maximizing U_lam are Ej=Mj for positive coefficient 1-(1+lam)rj, zero for negative; a zero-coefficient key is free. On the claimed lambda interval the resulting support functional S_lam is affine in lambda separately on [-1/10,0] and [0,1/10]. On the negative half, keys {0,1,2,3} have nonnegative coefficients; on the positive half, keys {0,1,2} do; at zero key 3 has coefficient zero.

## THEOREM — complete exact support function, with two nonzero switch points

Set l_minus=-351/17291, l_plus=351/16589 and let A, B be the seedless LR timing policies

~~~
A: (g,a,b,u,v,w,z)=(28/31,28/31,28/31,0,91/310,0,14/155)
B: (g,a,b,u,v,w,z)=(1,44/53,44/53,0,143/530,0,22/265).
~~~

For EVERY real lambda in [-1/10,1/10], optimizing over all real admissible FULL_HIST timing flows and all legal terminal random declarations while fixing TP=TQ=31/10,

~~~
max_FULL_HIST U_lam = max_seedless_LR U_lam =
  966/3875 - (3932/11625)*lambda,        -1/10 <= lambda <= l_minus
  13269/53000 - (45413/159000)*lambda,  l_minus <= lambda <= 0
  13269/53000 - (641/3000)*lambda,      0 <= lambda <= l_plus
  966/3875 - (1897/11625)*lambda,        l_plus <= lambda <= 1/10.
~~~

This is a real, not grid-restricted, theorem. At both l_minus and l_plus the timing optimizer is exactly the continuous seedless line:
~~~
a=b=s, g=21/10-(53/40)*s, u=w=0, v=13s/40, z=s/10,
44/53 <= s <= 28/31.
~~~
Off the two switches the maximizing timing flow is uniquely A on the outer two intervals and B on the inner two intervals. At lambda=0, the declaration at r=1 is free, and B remains the unique optimal timing flow. Optimal declarations at zero-coefficient likelihood-ratio keys can vary without changing U.

## Proof by five exact nonnegative affine certificates

Write dP=TP-31/10, dQ=TQ-31/10 and four legal slacks L=(u,C1-v,w,9b/40-v+z); the remaining nonnegative slacks used below are G=g-b and J=1-g.

For each anchor lambda in {-1/10,l_minus,0,l_plus,1/10}, the following EXACT AFFINE IDENTITY holds for all seven real flow variables, with coefficients specified in the same order:

~~~
  B + alpha*dP + beta*dQ - S_lambda
       = mu0*u + mu1*(C1-v) + mu2*w + mu3*(9b/40-v+z)
         + eta*(g-b) + xi*(1-g).
~~~

Anchor    B             alpha           beta           (mu0,mu1,mu2,mu3)                                                 eta          xi
-1/10     16456/58125   21007/348750    9403/348750   (46481/930000,54791/558000,183499/2790000,17537/162000)         13781/558000 0
l_minus   22146/86455    6694/86455     3016/86455   (22473/345820,7789/69164,46129/345820,81757/622476)            0            0
0         13269/53000     391/6625       364/6625   (3999/53000,1283/10600,7127/53000,247/1800)                 0            117/10600
l_plus    20391/82945    3184/82945     6526/82945   (26373/331780,7789/66356,42229/331780,81757/597204)            0            0
+1/10     27083/116250 -43037/348750   81727/348750  (332837/2790000,67769/558000,112541/2790000,21983/162000)     13079/558000 0
~~~

Every slack coefficient is nonnegative. At dP=dQ=0, each anchor implies S_lambda<=B. All five inequalities are sharp: A achieves the outer anchors and both switch anchors; B achieves the inner anchor and both switch anchors. The -1/10 and +1/10 certificates reuse the predecessor's exact support identities; the two switch identities and lambda=0 identity give the new exact certificates.

For lambda between adjacent anchors on the same side of zero, write lambda=(1-theta)*lambda_left+theta*lambda_right with theta in [0,1]. Because the set of positively declaring LR nodes is unchanged over each open half, for any fixed flow S_lambda=(1-theta)S_left+theta*S_right. Interpolating the two nonnegative certificate identities yields a nonnegative certificate for this real lambda. The affine interpolation of their B values equals the appropriate A or B objective displayed in the theorem. Thus the certificates bound ALL FULL_HIST flows. Since the relevant A and B timing policies satisfy the seedless relation and their optimal declarations are legal, each bound is attained in seedless LR. This proves the four pieces for all real lambda.

Rigidity: at the two switch anchors the four strictly positive mu coefficients force u=w=0, v=C1, v-z=9b/40, hence z=a/10. With TP=TQ, (b-a)/8=0, hence a=b. The fixed time requires g+(53/40)a=21/10. Combining a<=g<=1 yields exactly the segment 44/53<=a<=28/31. For lambda between anchors, positive interpolation of the eta or xi coefficients additionally forces g=b (outer cases) or g=1 (inner cases), leaving A or B uniquely. At zero the xi coefficient remains positive, so B is unique. The seedless relation holds identically on the entire segment: 9*b*z=9a*b/10=4*a*(v-z). End proof.

## Validation, interpretation and next work

Run: `python3 VERIFY.py`. The standard-library Fraction checker runs the 5 anchor affine identities at the origin and 7 independent coordinate vectors (40 exact coefficient evaluations), verifies both seedless endpoints, their moments, times, and switch equations, and checks 201 rational diagnostic lambda values. These coefficient-level exact checks validate the algebraic identities in the analytical proof; the real-parameter conclusion follows from affine interpolation and explicitly verified policy legality. Actual execution output is in EXACT_OUTPUT.txt.

The calculation exhibits TWO policy switches at nonzero lambda within [-1/10,1/10]. Despite the switches, every exposed optimizer on this symmetric-time slice is seedless LR. This closes the specified one-parameter support subproblem without deciding equality of the full four-dimensional observer images.

Next discriminating unit: fix rational asymmetric times near (31/10,31/10), compute signed-direction FULL_HIST exact LP witnesses and compare them against the nonlinear seedless LR relation allowing *all* early flows. Aim at an exact global four-observer separation certificate, or a provable local equivalence band. See NEXT_UNIT.md.

Control boundary observed 2026-11-07: Site gateway research_authority_granted=false; native task query BACKEND_IDENTITY_OR_VERSION_MISMATCH (operation_sent=false). No authenticated CLAIM, Source Result or independent reviewer status is asserted. This is an author-side mathematical proof and durable artifact.
