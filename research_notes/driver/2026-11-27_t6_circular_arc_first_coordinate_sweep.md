# T6: output-sensitive circular-arc join for exact first-coordinate screening

2026-11-27; EM-DVR-DEBB5E. Shared nonblind research context; original frozen T6 p19 author EM-T6SM-B134BD and earlier contributor EM-T6-BFF294 retained. This is a new alternative join implementation and proof, not new original p19 authorship, new general-tool novelty, or repetition of the completed full six-split affine audit. Source input 6cdc7b061d6579d6993f2fbc30d396d9a5c29047:research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/input.json (blob e2f33462b95e1f0fc4ccc5a38f3bb922a4ade388). Earlier first-coordinate residue predicate and ledger at 186057cdc4fd939b886e2d2fdf5a6622f43d7336 and af81386070eb9079f70af7e52183936a68e5f920, respectively.

## Lemma and exact enumeration

Let D>0 be the final triangular pivot, g its integer projector, l=min(0,min g), h=max(0,max g). Each roster state s has residual side mass A_s>=0 and scalar projected particular value t_s. Put H_s=(t_s-A_s h) mod D, L_s=(t_s-A_s l) mod D, W_s=A_s(h-l). Suppose W_u+W_v<D for each opposite pair. Define I_s={H_s+j mod D: j integer, 0<=j<=W_s}. Then the existing first-coordinate predicate (L_u-H_v) mod D<=W_u+W_v is equivalent to I_u intersect I_v nonempty. Indeed a common residue is equivalent to H_v-H_u=a-b mod D for 0<=a<=W_u, 0<=b<=W_v. The differences fill exactly the integer interval [-W_v,W_u], so subtracting from W_u gives precisely the stated residue predicate, with no wrap ambiguity as the total width is <D.

Split each circular arc into at most two closed integer intervals inside [0,D-1]. Sweep all starts and ends, processing starts before ends at equal coordinates (including zero-width arcs), keeping active pieces by side. A newly starting piece intersects every opposite active piece; every intersecting piece pair is emitted exactly once at the later start, with deterministic ordering of ties. For each eligible orientation (for equal nonzero orders use u.id<v.id), compute the least integer intersection point of the full arcs by checking at most four piece pairs. Emit only when the event point equals this least point; since the pieces of one arc are disjoint, exactly one piece pair covers that point, preventing wrap duplicates. Finally test supports disjoint. This enumerates exactly the canonical first-coordinate survivors, without enumerating all cross-roster pairs. All later triangular coordinates, actual signed budgets, H0 and full observer conditions remain unchanged.

For m,n roster sizes and K intersecting piece pairs (before disjointness/orientation), sorting and sweeping take O((m+n)log(m+n)+K) exact integer comparisons/constant-size operations, O(m+n) storage apart from emitted output, measured in integer operations, not bit complexity. Degenerate worst case can still be quadratic. This is a scoped adaptation of an interval sweep; no novelty claim about generic sweep algorithms.

## Actual exact test against saved independent full audit

D=64705048744071327105980441283267960. Roster counts 1482,8124,8506,262 for orders 3,4,5,6. The uniform exact bound (4662-361*(a+b)-36)*(h-l)<D checked for all six splits. All emitted unique pairs rechecked against the direct residue predicate. Expected counts taken from prior full independent audit's first-coordinate rejection histograms, not from newly repeating the full pair loop.

| split | sweep events | segment overlaps incl duplicate/orientation | unique disjoint first-pass pairs | prior total minus first rejection |
|---|---:|---:|---:|---:|
|3,6|4086|87697|73680|73680|
|4,5|35202|8687528|5535791|5535791|
|4,6|18150|213520|165368|165368|
|5,5|35156|5231859|1538260|1538260|
|5,6|18104|107450|71226|71226|
|6,6|1052|1913|489|489|
|total| |14329967|7384814|7384814|

All six counts match. The old normalized disjoint domain has 70,285,694 pairs; the new sweep enumerates 14,329,967 segment overlaps even before orientation and support filters. These are operation-count proxies, not wall-clock speedups. 7,384,814 actual first-coordinate survivors are not feasible full solutions. The existing completed six-split affine audit excludes them all. No fresh full affine search, global threshold, Native review, Result or Task closure follows from this experiment.

## Executed reproduction (JavaScript BigInt)

Use exact raw input JSON; preserve large integer tokens before parsing.

```javascript
function sweepAudit(raw){
 const x=JSON.parse(raw.replace(/(?<!["\w])(-?\d{15,})(?!["\w])/g,'"$1"')), D=BigInt(x.projector_denominators[17]),g=x.projector_numerators[17].map(BigInt), lo=g.reduce((a,b)=>a<b?a:b,0n),hi=g.reduce((a,b)=>a>b?a:b,0n),B=2331,mod=t=>(t%D+D)%D;
 const assert=(c,m)=>{if(!c)throw Error(m)}, A=x.atoms, v=x.atom_representatives.map(row=>row.reduce((s,a,j)=>s+BigInt(a)*BigInt(19*(j+1)-1)*g[j],0n));
 const S={};for(const q of [3,4,5,6]){let out=[];function rec(i,Q,c,mask,t){if(!Q){const b=BigInt(B-c),H=mod(t-b*hi),L=mod(t-b*lo),W=b*(hi-lo);assert(W<D&&mod(L-H)===W,"arc");out.push({id:out.length,mask,H,L,W,pieces:H<=L?[[H,L]]:[[0n,L],[H,D-1n]]});return}for(let j=i;j<A.length;j++){let [a,,w]=A[j];if(a<=Q&&c+w<=B)rec(j,Q-a,c+w,mask|(1n<<BigInt(j)),t+v[j])}}rec(0,q,0,0n,0n);S[q]=out}
 const results=[];
 for(const [a,b,pairs,reject] of [[3,6,335374,261694],[4,5,45287075,39751284],[4,6,1724674,1559306],[5,5,21405127,19866867],[5,6,1513179,1441953],[6,6,20265,19776]]){
  const maxW=(BigInt(4662-361*(a+b)-36))*(hi-lo);assert(maxW<D,"width");
  const ev=[];for(const [side,list] of [[0,S[a]],[1,S[b]]])for(const s of list)for(const [l,h] of s.pieces){const p={side,s,l,h};ev.push({at:l,kind:0,p},{at:h,kind:1,p})}
  ev.sort((u,v)=>u.at<v.at?-1:u.at>v.at?1:u.kind-v.kind||u.p.side-v.p.side||u.p.s.id-v.p.s.id);
  const active=[new Set(),new Set()];let overlap=0,ordered=0,duplicates=0,disjoint=0;
  for(const e of ev){const p=e.p;if(e.kind){active[p.side].delete(p);continue}
   for(const q of active[1-p.side]){overlap++;const u=p.side===0?p.s:q.s,v=p.side===0?q.s:p.s;if(a===b&&u.id>=v.id)continue;ordered++;
    let first=null;for(const [l,h] of u.pieces)for(const [j,k] of v.pieces){let L=l>j?l:j,H=h<k?h:k;if(L<=H&&(first===null||L<first))first=L}
    assert(first!==null,"overlap");if(first!==e.at){duplicates++;continue}
    assert(mod(u.L-v.H)<=u.W+v.W,"predicate");if(u.mask&v.mask)continue;disjoint++;
   }active[p.side].add(p)}
   assert(disjoint===pairs-reject,"survivor mismatch "+a+","+b+" "+disjoint);
   results.push({split:[a,b],events:ev.length,segmentOverlaps:overlap,orientationEligible:ordered,duplicateOverlaps:duplicates,disjointFirstPass:disjoint,expected:pairs-reject,oldPairs:pairs})
 }
 return {D:String(D),rosters:Object.fromEntries(Object.entries(S).map(([q,l])=>[q,l.length])),results};
}
```
