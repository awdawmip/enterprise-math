# R284GM — Global low-omission sharp capacity and exact minimizing histogram classification

2026-11-24. Informed portable continuation of the auxiliary four-phase fixed binary tag model. Author analytic proof and exact finite regression, NOT_REVIEWED. P000 and ACTIVE worldview unchanged. No shared CLAIM or native physical/BRC attribution. Original session registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED, Researcher EM-DIRECT-0C386E, Activity RA-B82240E8488EF5A1DA5186C4; current owner read r1-20261124-1000-owner was queued when initiated. No formal authority inferred. Frozen sources:
- R284GL @5f74ba8a545788cc3fdb080f9953bbe5a0926531:research_notes/portable_direct/R284GL_ASYMMETRIC_THREE_PATTERN_SHARP_CAPACITY_20261124.md (exact asymmetric prefix distances).
- R284GK @9c56aa402a9f36352c11ea721fe5b1bba580fdf1:research_notes/portable_direct/R284GK_LOW_OMISSION_THREE_PATTERN_CONSTRUCTION_20261124.md (symmetric upper construction).
- R284GE @a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md (GE1, source-group stable cuts and full-cycle criterion).

## Results

1. For all integers u>=1, 0<=q<=u, the complete seven-mode model has sharp capacity n_min(q,u)=5q+5u+2. This is global, without support restrictions, and supplies the first entire branch of GK's global conjecture. q=0 was already proved in GL.
2. For 1<=q<u all minimizing nonconstant histograms have no singleton/triple columns (types 1,2,4,7). Their ordered (A,B,C)=(x3,x5,x6) are exactly (H,J,H), (H-1,J+1,H), (H,J+1,H-1), where H=2q+u+1, J=q+3u. For q=u>=1 only (H,J,H) is safe at the minimum width.
3. The necessary relaxation using the four GE1 conditions and two opposite stable distances has exact all-parameter minimum min(5q+5u+2,4q+6u+2) for q>=0,u>=1. This improves GL's elementary general lower bound; the relaxation alone cannot prove the medium/high branches.

## Exact incidence and lower bound

Write A=x3, B=x5, C=x6, S=x1+x2+x4+x7. Normalize each bit at phase 0 to zero. The changing-source groups on edges 0,1,2,3 respectively are
  (1),(3),(5,7);
  (2),(6),(1,5);
  (3),(4),(2,5);
  (7),(6),(4,5).
For an edge with group sizes N_e, GE1 says sum_e (N_e-q)_+ >= q+4u+1, equivalently nominal changing distance D >= q+4u+1 + sum_e min(q,N_e). In particular D>=2q+4u+1 since the overflow is positive and sum_e min(q,N_e)>=q.

For opposite stable pairs (0,2) and (1,3), the demand incidence on two source and two comparison vertices of capacity q is the 2x2 matrix of mode counts
  [x2 A; C x7] and [x1 A; C x4].
These entries follow from last nominal changes (GE): phase 0/2 pairs (2,1),(2,0),(3,1),(3,0) for types 2,3,6,7, and phase 1/3 pairs (0,1),(0,2),(3,1),(3,2) for types 1,3,6,4. Each opposite distance is the maximum of 0, each cell minus 2q, each row/column sum minus 3q, and the whole matrix sum minus 4q. Indeed these are all nonempty contained-demand cuts on the four endpoints, after discarding cuts containing no extra demands. GE's integral matching dual gives equality. Separation requires at least one cut >=2u+1 for each opposite pair.

If either pair has a qualifying single-cell cut, its mode has count >=2q+2u+1 and some adjacent edge does not change that mode. Thus n>=4q+6u+2. If either pair has a qualifying row/column cut, its two modes have total >=3q+2u+1. Every such pair has a common nonchanging edge (directly from the group table). Thus n>=5q+6u+2. Both bounds suffice for q<=u. In the remaining case both whole-matrix cuts qualify, so
  2(A+C)+S >= 8q+4u+2.                         (1)

If A<q, the GE overflow on each edge 0 and 2 comes entirely from the other two groups. By (r-q)_+ +(s-q)_+ <= (r+s-q)_+ for nonnegative r,s, each of these two edges has B plus its singleton counts >=2q+4u+1. Sum gives 2B+S>=4q+8u+2. Add (1): n>=6q+6u+2. Same for C<q by rotation.

If A,C>=q but B<q, each GE edge overflow is bounded above by its balanced nonalternating count minus q plus its two singleton counts (because (B+s-q)_+<=s and (s-q)_+<=s). Adding the two edges for A yields 2A+S>=4q+8u+2, and similarly 2C+S>=4q+8u+2. Hence n>=4q+8u+2+B.

Finally A,B,C>=q. Every edge has two groups of size at least q. Each singleton appears as a standalone group on exactly one edge, so the sum of all four GE source penalties is exactly 8q+sum_{p=1,2,4,7}min(q,x_p). The sum of the six nominal distances is 4n-S: balanced columns contribute 4, singleton/triple columns 3. Sum the four adjacent GE inequalities and the two full opposite cuts:
  4n-S >= 20q+20u+6 + sum_{p=1,2,4,7} min(q,x_p).
Thus
  n >= 5q+5u+ceil((6+S+sum min(q,x_p))/4).     (2)

In every case n>=min(5q+5u+2,4q+6u+2). For q<=u, GK's symmetric construction attains 5q+5u+2 safely, proving the global theorem. For q>=u the relaxation minimum 4q+6u+2 is attained by (A,B,C)=(2q+2u+1,2q+4u+1,0) and no singletons: GE is satisfied, and each opposite distance is A-2q=2u+1. This witness is only for the relaxation, not a safe protocol.

## Rigidity at minimum width, 1<=q<=u

Suppose n=5q+5u+2. Row/column cuts cannot qualify because their lower bound exceeds n. For q<u, single-cell cuts also cannot qualify. In the full-cut case the small-count cases above are strictly too expensive (q>=1,u>=q); hence (2) applies. It gives S+sum min(q,x_p)<=2, which for positive integer q implies S<=1. If S=1, all six summed inequalities used in (2) must be tight. The unique singleton changes on two edges, on one as a standalone group and on the other sharing the B group. On its shared-group edge it increases D by 1 but does not increase the GE penalty; the opposite edge has the same A or C and B and no singleton. These two adjacent GE inequalities cannot both be tight. Therefore S=0.

At q=u, a single-cell cut might qualify at equality. The cell mode has exactly 4q+1, and each of its two nonchanging edges must contain all other 6q+1 coordinates. The only possible other modes are in the intersection of these two changing sets:
- For a balanced nonalternating cell A or C, the intersection is B and the other balanced nonalternating type. They occupy distinct source groups. GE equality at D=6q+1 forces one group zero, since q>=1 and the total exceeds q. If B=0, an edge updating the cell cannot meet D>=6q+1. Hence the only remaining single-cut candidates are (4q+1,6q+1,0) or its A/C exchange.
- For a singleton cell, the intersection is B and the complementary singleton (as shown by the group table). These occupy distinct groups on at least one of the two edges. The same equality forces one zero. If B=0, a changing edge of the original cell has only 4q+1 changes; if the complementary singleton is zero, one opposite pair has no differing columns (B differs on neither opposite pair). Both violate necessary conditions.
For the balanced single-cell candidate, test the edge updating A=4q+1 and B=6q+1 with C=0 (rotate if needed). GL's exact D2 at a=2q+1 is (b-2q)_+, so at the step from a=2q to 2q+1 safety requires b>=4q+1. At the preceding prefix GL's D3=max(0,B-b-q)<=q<2q+1. Thus no safe single-cut candidate. If both full cuts qualify we already proved S=0. This also excludes mixed histograms from the relaxation optimum at q=u.

With S=0 and A,B,C>=q, GE and full opposite cuts yield
 A+B>=3q+4u+1, C+B>=3q+4u+1, A+C>=4q+2u+1.
At n=5q+5u+2 this means A,C<=H=2q+u+1 and A+C>=2H-1. Integer possibilities are exactly (H,J,H),(H-1,J+1,H),(H,J+1,H-1), J=q+3u. The symmetric one is safe by GK.

For either asymmetric one when q<u, use the following explicit path for each edge. A denotes its changing nonalternating type (interchange A,C on rotated edges), C its unchanged nonalternating type; e=A-2q, d=C-2q so e+d=2u+1 and e,d in {u,u+1}. B=J+1. GL reduces D2 to (e-a)_+ +(b-q)_+ + d and D3 to max(0,d,(a-q)_+-q,B-b+(a-q)_+-q+d). First raise b to q; for a=1,...,e raise b by one to q+a and then raise a by one. D2 remains >=2u+1. D3 at each such preceding a-1 is >=2u+1 provided B>=2q+a+e-(a-1-q)_+. Its maximum required B is 2q+e+min(e,q+1)<=3q+e+1<=q+3u+1, since q<=u-1 and e<=u+1. This condition also covers initial b<=q. Now keep b=q+e and finish a to A; D2 stays safe, D3 is nondecreasing in a. Finally finish b to B; D2 increases and D3 decreases to a value at least e+d=2u+1. All adjacent GE and stable conditions hold by the displayed inequalities (opposite source pairs disjoint in this support); GE's full-cycle criterion proves safety. At q=u, test instead the edge updating larger A=H with C=H-1, e=u+1,d=u,B=4u+1. The step a=e-1=u to e forces b>=2u+1 by D2, while preceding D3<=2u. Thus either asymmetric candidate fails. This proves the exact minimizer classification.

## Executed finite regression

The following exact integer JS checker enumerated all seven-mode histograms of widths N-1 and N for 1<=q<=u<=3 (8,651,225 histograms total); it checked all GE and opposite cut conditions, then for surviving pure histograms tested exact monotone path existence on both edge types by GL formulas. Actual results: no candidate at N-1, no mixed candidate at N, 3 safe candidates when q<u, 1 when q=u; for q=u there were 5 pure relaxation candidates (the two asymmetric and two zero-mode ones fail). This is a cross-check, not the proof of unbounded parameters. Earlier exploratory floating MILP was used only to identify the relaxation conjecture, not as proof.

```javascript
const pos=z=>Math.max(0,z),G=[[[1],[3],[5,7]],[[2],[6],[1,5]],[[3],[4],[2,5]],[[7],[6],[4,5]]],O=[[2,3,6,7],[1,3,6,4]];
const sum=(x,ids)=>ids.reduce((s,i)=>s+x[i],0);
function stable(x,q,u){return O.every(([a,b,c,d])=>Math.max(0,x[a]-2*q,x[b]-2*q,x[c]-2*q,x[d]-2*q,x[a]+x[b]-3*q,x[c]+x[d]-3*q,x[a]+x[c]-3*q,x[b]+x[d]-3*q,x[a]+x[b]+x[c]+x[d]-4*q)>=2*u+1)}
function path(A,B,C,q,u){let dp=Array(B+1).fill(false);for(let a=0;a<=A;a++)for(let b=0;b<=B;b++){let d2=pos(A-a-2*q)+pos(pos(b-q)+pos(C-q)-q),s=pos(a-q),d3=Math.max(0,C-2*q,s-q,B-b+s-2*q+pos(C-q));dp[b]=d2>=2*u+1&&d3>=2*u+1&&((a===0&&b===0)||(a>0&&dp[b])||(b>0&&dp[b-1]))}return dp[B]}
let results=[];
for(let u=1;u<=3;u++)for(let q=1;q<=u;q++){
let N=5*q+5*u+2,x=Array(8).fill(0),rows=[],mixed=[],checked=0,below=0;
function rec(p,r,n){if(p===7){x[7]=r;checked++;if(!G.every(g=>g.reduce((s,ids)=>s+pos(sum(x,ids)-q),0)>=q+4*u+1)||!stable(x,q,u))return;if(n<N){below++;return;}if(x[1]+x[2]+x[4]+x[7])mixed.push(x.slice(1));else rows.push({x:[x[3],x[5],x[6]],safe:path(x[3],x[5],x[6],q,u)&&path(x[6],x[5],x[3],q,u)});return;}for(let v=0;v<=r;v++){x[p]=v;rec(p+1,r-v,n)}} 
rec(1,N-1,N-1);rec(1,N,N);results.push({q,u,N,checked,below,mixed,rows});}
console.log(JSON.stringify(results));
```

Actual counts by (q,u): (1,1) 30940; (1,2) 175560; (2,2) 672750; (1,3) 672750; (2,3) 2013760; (3,3) 5085465. All classifications matched.

## Next

Focus on u<q<2u and q>=2u below the existing high-q theorem. Single-cell-cut relaxation witnesses show that merely adding GE and opposite stable cuts cannot settle those branches: prefix competition is load-bearing. Use the 2x2 opposite cut incidence and source-penalty identity (2) to charge the remaining mixed modes, then bring in a third-phase prefix barrier. Do not repeat q<=u or the asymmetric carrier proof. No independent Review or theorem promotion claimed.
