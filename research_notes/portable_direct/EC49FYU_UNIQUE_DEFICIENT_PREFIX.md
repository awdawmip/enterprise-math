# EC49FYU — unique deficient support at the last unsaturated prefix

2026-11-24. Frozen auxiliary Boolean observer BRC16943, 50 distinct nonempty masks, exact labeled state (U,H) with m>h>=1, |H|<=h and W(t,j)=1[t in U]1[j not in H]. Unit noiseless adaptive bit probes. Parent pins actually read: 438163ba045e2d3ea8d27bbb81004694f5069ae0:research_notes/portable_direct/EC49FYT_EVENTUAL_PERIODIC_EXCESS.md (block transport, one-bit upper bound, eventual phase threshold); c537688c0ee8151c4a2d3d7bf133a86d22a60414:research_notes/portable_direct/EC49FYS_EXACT_ASYMPTOTIC_HOLE_EXCESS.md (multicover cost K(h)=ceil(26h/11), integer dual weights). Auxiliary observer theorem; no new native X6 attribution.

## General lemma: uniqueness at exhausted residual budget

Take a correct decision tree of worst depth at most m+c. At an all-zero prefix of length d=c+h-1, let B(U) be the set of physical columns having a queried row in U, and b(U)=|B(U)|. If b(U)<h then the target (U,B(U)) is compatible, with every other column live. For this target, every live column requires a future positive query: otherwise changing only that column to a hole produces a legal competitor with exactly the same transcript. Thus d+m-b(U)<=m+c, hence b(U)>=h-1. Consequently every deficient U (b(U)<h) has b(U)=h-1, and its remaining budget is exactly m-h+1, all of which must be positive probes, one on each live column. All such targets follow the identical all-positive suffix of the same deterministic decision tree. Two distinct deficient U therefore cannot coexist at this prefix. This argument retains joint labels; counting live columns alone without the common suffix would miss uniqueness. Repeated probes and variable-depth leaves do not change the argument.

## Uniform dual-weight obstruction

Let K=K_F(h) be the integer row multicover cost at strength h. As in FYS, Q_h(m)>=m+K-h. Suppose equality holds, c=K-h. A zero prefix of length d=K-1 must exist in the tree: for each earlier prefix of length <K, the row counts cannot cover every U h times, hence some U has b(U)<h; the target (U,B(U)) and an extra-hole competitor exist (m>h), so the zero history is feasible and cannot be terminal. At d=K-1 there is again a deficient U, and the lemma shows it is unique, say U*, with b(U*)=h-1. Every other U has b(U)>=h.

For nonnegative support weights w_U with total T, per-row incidence <=A, and maximum support weight M, write x_t for the row multiplicities at d. Since b(U)<=sum_{t in U}x_t, we obtain
T h - w_(U*) <= sum_U w_U b(U) <= sum_t x_t sum_{U containing t}w_U <= A(K-1).
Thus a necessary condition for equality Q_h(m)=m+K-h is A K-T h >= A-M. This is independent of m and requires no decision-tree enumeration. It also identifies U*: w_(U*)>= A-(A K-T h). A nonweighted deficient U has weight zero and cannot satisfy this bound whenever the slack is <A.

## Frozen BRC16943 specialization

FYS certificate weights: (86,3),(101,4),(281,2),(394,5),(460,1),(602,3),(673,5),(788,3). T=26, A=11, M=5. Per-row incidence [11,11,11,11,11,9,11,11,11,11]. Define s_h=1+((15h-1) mod 11), with zero residue represented by 11. Slack 11K-26h=11-s_h. Thus equality requires s_h<=5. Equivalently for every m>h>=1,
Q_h(m) >= m+ceil((15h+6)/11).
Indeed if s_h>5 the integer lower bound increases by one, and otherwise it agrees with FYS. When s_h=5 any tight strategy must have its unique deficient support equal to 394 or 673 (weight 5). At that prefix all dual inequalities are equalities: row 5 is never probed, all positive-weight supports other than U* have exactly h forced holes, U* has h-1, and no counted incidence for a positive-weight support repeats an already-hit physical column. These are necessary, not sufficient, conditions.

Combine with FYT for h>=3:
ceil((15h+6)/11)<=c_h<=5+ceil(15(h-3)/11).
The interval is singleton for s_h=1 or 6..11. Equivalently seven residue classes mod 11 are now exact: h mod 11 in {0,2,3,5,7,8,10}; only {1,4,6,9} remain open (h>=3). For the six newly resolved classes c_h=ceil(15h/11)+1. The upper bound is attained for finite m>=10+ceil(26(h-3)/11) via the FYT/FYR construction; a threshold using FYQ alone is 11+ceil(26(h-3)/11). Therefore the same exact values hold for Q_h(m)-m above those thresholds. In particular c5=8, c7=11, c8=12, c10=15, c11=16. The three proposed bare-lower targets c5=7, c8=11, c11=15 are impossible. The eventual FYT offset delta is in {6,7,8,9,10}, since phases >5 always have epsilon=1. Next high-leverage constructive target is c4=6 (phase 5); if attained, delta=6 and all h>=4 are then exact via FYT propagation and this lower bound. If c4 fails, that alone does not exclude future exact indices with phase 5.

## Exact certificate and arithmetic crosscheck (executed JavaScript)

```js
const F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005];
const W=[[86,3],[101,4],[281,2],[394,5],[460,1],[602,3],[673,5],[788,3]];
const hits=Array.from({length:10},(_,t)=>W.reduce((a,[u,w])=>a+((u>>t&1)*w),0));
if(F.length!==50||new Set(F).size!==50||W.some(([u])=>!F.includes(u))||W.reduce((s,[u,w])=>s+w,0)!==26||Math.max(...hits)!==11||Math.max(...W.map(x=>x[1]))!==5)throw Error("certificate");
for(let h=3;h<=10000;h++){
 let s=(15*h-1)%11+1,lo=Math.ceil((15*h+6)/11),hi=5+Math.ceil(15*(h-3)/11);
 if(hi-lo!==(s>=2&&s<=5?1:0))throw Error("phase "+h);
}
console.log(hits,"h=3..10000 exact integer arithmetic PASS");
```

Observed incidence [11,11,11,11,11,9,11,11,11,11]; all 9998 arithmetic cases passed. The general proof is analytic, not based on the finite range. No new decision-tree witness was generated. Scientific status AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.

## Provenance and control

Original researcher registration EM-DIRECT-23537B / RA-2D7B4AD1AA5CD3F5D9EF1C76, original receipt r4-20261124-0240-ec49fyh-own-session-v1 reread SUCCEEDED. Current topic read r4-20261124-1530-ec49as-read-v1 SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at Source a88e3e001275269cae93c40d77e6984b1ef2970f observed 2026-11-24T07:30:35.440741Z; limited directory absence, not native owner projection. Current own private writer binding not established; independent portable research only, no CLAIM/Result/Review or Activity mutation. Preserve previous contributions and source pins.
