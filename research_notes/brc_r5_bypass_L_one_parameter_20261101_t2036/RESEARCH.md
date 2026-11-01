# R5 — Bypass-fed fourth shared LR key: old support gap vanishes but a second obstruction persists

2026-11-01 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Frozen sources and model scope

GLOBAL_KNOWLEDGE_V1 canonical main a01383f825ef9d43b4b754254303298c64041568 (00_BOOTSTRAP, OPERATING_MANUAL, EM task researcher router, P000 startup, ACTIVE worldview and math/BRC/activity rules). P000 startup canonical blob SHA 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc equals the original P000 blob at this same global snapshot. Enterprise Math main 86149263e38c22292c9def1e0f69092efa1be77e (AGENTS, original p000_reality_foundation, joint observer preservation, native X6/time, current control, AUTONOMOUS_RESEARCH_OPERATIONS and PORTABLE_RESEARCH_PROTOCOL). Predecessor research: commit b4db5ed625347d380689a79c2a09dc4fedd29baf, brc_r5_downstream_shared_behavior_20261101_t1935. Its >=1/4 support-gap theorem is limited to K-only descendants, without an external bypass.

This paper treats an auxiliary finite classical P/Q stopping model. BRC interface REUSE_APPLIED: retain nonnegative two-law, source-labelled branch masses until four-observer projection. Signed coefficients apply only to the observer, NOT to branch probabilities. No native six-axis X6/three-dimensional-slice transfer or external physics claim is made.

## Definition and genuinely bypass-fed fourth shared key

The observer is O=(eP,eQ,TP,TQ) with eP=P(final answer P), eQ=Q(final answer Q), and TP,TQ the expected terminal times. At every shared behavioral key LR chooses the same real stopping probability under P and Q; FULL may condition it on source history. Initial source P/Q masses: A1=A2=(1/8,1/8), B=(1/4,1/8), C=(1/2,5/8). They separately sum to 1 under each law. C has behavior r: stop Q at t=1, otherwise answer P at t=3.

For each A source: at I=(1,1), p_i stops P at t=1; after continuation the natural low (P,Q)=(1/2,3/4) answers Q at t=2, high=(1/2,1/4) reaches J=(2,2). At J, q_i stops P at t=2; continuation natural low (3/5,1/2) answers Q at t=3, high (2/5,1/2) reaches K=(3,8/5). K first nature-thins with shared epsilon=1/2 to stop P at t=3; the retained portion stops P with behavioral k_i or continues, nature low (1/4,1/2) answering Q at t=4, high (3/4,1/2) entering L=(4,12/5). At L, l_i stops P at t=4, otherwise Q at t=5.

NEW: B reaches J directly with ratio 2. It stops P at t=2 with q_B, otherwise nature splits at t=4: high has conditional (P,Q)=(6η/5,η), and low the complements (1−6η/5,1−η). Assume the OPEN strict-probability domain 0<η<5/6. Low answers P at t=4; high enters the SAME L=(4,12/5), since 2(6η/5)/η=12/5. Here l_B stops P at t=4, otherwise Q at t=5. The A high arrival at L has positive masses (3/320,1/256) before its behavioral decisions, likewise ratio 12/5. Nature probabilities on every edge are strictly positive throughout this interval; terminal behavior may be deterministic.

FULL has independent variables (p1,p2,q1,q2,qB,r,k1,k2,l1,l2,lB) in [0,1]^11. LR ties p1=p2=p, q1=q2=qB=q, k1=k2=k, l1=l2=lB=l, with r free, thus [0,1]^5. No path revisits a behavioral key, so each observation coordinate is separately affine in each variable. Therefore for ANY signed linear cost, minima/maxima on the entire real policy cubes occur at deterministic vertices (2048 FULL, 32 LR); equality of actual behavioral images is NOT assumed.

## Theorem 1: complete all-real phase diagram of the old H gap

Put H(O)=5eP+5TP−8TQ and α(l)=−3/8+l/4. Direct positive-flow expansion yields

~~~text
H_FULL = −33/8 + SUM_i [13p_i/16 −p_i*q_i/8 +q_i/8
                   + α(l_i)(1−p_i)(1−q_i)(1−k_i)/8]
         −qB/4 +(1−qB)(1/4−η+η*lB) +(5/2)r.
~~~

Each A bracket is >=−3/64 on the entire real unit cube, with equality at p=q=k=l=0. FULL chooses r=0 and the cheaper B decision between qB=1 (cost −1/4) and qB=lB=0 (cost 1/4−η). Thus

min_FULL H = −143/32 + min(0,1/2−η).

For LR, the monotonic terms permit p=k=l=r=0, leaving only affine q. Its two values are −33/8 at q=1 and −127/32−η at q=0. Thus

min_LR H = min(−33/8,−127/32−η).

The EXACT signed support gap G_H=min_LR H−min_FULL H is 11/32 for 0<η<=5/32; 1/2−η for 5/32<=η<=1/2; and ZERO for 1/2<=η<5/6. At η=1/2, B high nature probabilities are (3/5,1/2) and every nature branch remains strictly positive: the old H gap is genuinely repaired. This is outside the predecessor K-only theorem's assumptions, so does not contradict it.

## Theorem 2: persistent second exact support gap for ALL strictly positive η

Use cost C(O)=3eP+TP and signed support direction J=−C=(-3,0,-1,0). A source contributes

~~~text
A(p,q,k,l)=p/2+(1−p)[1/8+5q/16
           +(1−q)(3/16+3k/40+(1−k)(19/320+3l/160))].
~~~

Its all-real minimum is 119/320 at p=q=k=l=0; if q=1 and p=0, its cost is 7/16. B contributes

B(qB,lB;η)=(5/4)qB+(1−qB)[7/4−(3η/5)(1−lB)].

For 0<η<5/6, the B minimum is 5/4 (qB=1); the competing qB=0 value is strictly >5/4. C contributes r/2+3(1−r), min=1/2 at r=1. Independent FULL minimization gives

min_FULL C = 2(119/320)+5/4+1/2 = 399/160.

In LR, p=k=l=0 and r=1 minimize C for every shared q. Its remaining expression is exactly

C_LR(q;η)=(479/160−3η/5)(1−q)+(21/8)q.

Thus min_LR C=min(21/8,479/160−3η/5). In the signed direction J,

~~~text
G_J(η)=max_FULL J−max_LR J=min_LR C−min_FULL C
      =21/160                   for 0<η<=59/96,
       1/2−3η/5               for 59/96<=η<5/6.
~~~

G_J(η) is STRICTLY POSITIVE throughout the allowed open interval. Hence even for every η>=1/2 where G_H(η)=0, conv(FULL) != conv(LR). This is an all-real, complete one-parameter no-go, NOT a finite sampling claim.

At η=1/2, FULL policy bits (p1,p2,q1,q2,qB,r,k1,k2,l1,l2,lB)=(0,0,0,0,1,1,0,0,0,0,1) give W=(11/40,55/64,267/160,187/128), C(W)=399/160. LR has min C=21/8. Thus J(W)=−399/160 versus max_LR J=−21/8, a strict gap 21/160. By ||J||_1=4, dist_infinity(W,conv LR)>=21/640.

The LR four-observer affine rank is exactly four for every η. Set k=l=1. Four difference rows are
B=(1/5,-7/32,-3/8,-5/16),
C=(3/40,-1/32,-5/8,-5/16),
D=(-3/40,1/32,1/8,1/16),
E=(-1/2,5/8,-1,-5/4).
Their determinant is 59/10240>0, independent of η because B always answers P at t=4 in this slice.

## Validation, restrictions and next question

VERIFY.py uses standard-library Fraction only. For eta=1/8,1/3,1/2,2/3,4/5, it exactly reconstructs normalized P and Q terminal flows, checks both H and C formulas over every deterministic strategy, compares all minima against the analytical phase formulas, checks the explicit separating witness and the rank-four determinant: 5*(2048+32)=10400 exact observations. EXACT_OUTPUT.txt contains captured actual execution stdout. The universal real-parameter claims follow from displayed multiaffine identities and inequalities, NOT from these five tests. No Lean formalization, independent review, canonical task CLAIM/Result or native X6 transfer is asserted.

As eta approaches 5/6, G_J tends to 0, but the B low P nature probability tends to 0; the endpoint is EXCLUDED. One vanishing support gap does not imply all-signed hull equality.

Native status v0.6.11: research_authority_granted=false, executor_binding_configured=false. A read-only owner inventory returned CONTROL_QUOTA; no active owner or permission-bound claim was certified. Portable source publication is not native mathematical admission.

Smallest next unit: vary a second bypass mechanism (B low terminal answer/time, or add an appropriately calibrated C bypass at L); seek simultaneously G_H=G_J=0 with strictly positive P/Q natural kernels. If both vanish, test full all-signed four-observer convex inclusion with exact rational convex combinations or Farkas separators, then and ONLY then actual real-behavior image nonmembership. The original four-observer mother question remains OPEN.
