# X6 R250 — unique internal quadratic location restriction and complete real-product exclusion

2026-11-27. Author proof + exact BigInt computation; NOT_REVIEWED. Independent informed TASK_RESEARCH; native original read r2-20261127-0410-x6-read SUCCEEDED at 2026-11-26T20:10:07.315651Z, Source 49d7b85b2fb05cade5cf9b7ad0b8312545279f2d, NO_CANONICAL_PUBLICATION_DIRECTORY (directory observation only, no active owner projection or own research identity established). No CLAIM, Result, Review or shared task-state mutation. P000 V5 and ACTIVE worldview unchanged.

## Inputs and scope

Reuse the frozen Port 10, 1935 integer directions, six-pair BRC, positive weights (17t,B,22t,D), strict 3/2 output problem, 47 necessary labelled supports, 49 connected components, 51 endpoint rays, 98 directed interval germs and 2225 pure-linear observation masks. This is auxiliary weight-coefficient arithmetic, not native spatial geometry or dynamics. All conclusions inherit the necessary-wall and complete linear-germ suffix capacity premises. Exact executable input and pure-linear capacity implementation:
- 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md (blob fdbef2ee6e6c32573f3a1ccd171cb5337de520fa).
- 92b9c31df5b741322107e6fa70319d20d320ddfb:research_notes/portable_direct/2026-11-26_r2_x6_r242_reducible_quadratic_root_closure.md (complete real-product root exclusion; author-verified only).
- 2cade14d4c14cc047f63e0475475138a04ed7e37:research_notes/portable_direct/2026-11-27_r2_x6_r249_pole_event_interval_closure.md (blob 7b215074c71cc60352c89dab73350b52cdef4d15). R249's narrow single-anchor root interval is retained; this round attacks the independent unresolved internal placement instead of scanning more pole slices.

## 1. One-quadratic position capacity lemma

Let S be a subset of the frozen directed germs reaching a node; c(S) is the number of distinct necessary support labels represented. Let G(S,d) denote the inherited pure-linear capacity relaxation, downward closed in S, with G(S,d) false if c(S)>2^d-1. A sign query partitions S into strict sign masks S+ and S-; zero germs can be discharged in the relaxation. A zero germ of a nonzero homogeneous polynomial implies divisibility by that germ's support linear form (R238); isolated point zeros do not discharge a germ.

Consider a subtree with at most d remaining internal query levels and exactly one designated nonzero quadratic. Suppose the quadratic contains at most k distinct necessary support factors (k=0,1,2). Every linear node can discharge at most one distinct label, and the quadratic can discharge at most k. Hence
  c(S) <= 2^d - 2 + k.
This follows by assigning every represented label to at least one discharging node; a label represented in both branches may consume multiple nodes, which can only tighten the inequality. Equivalently use induction on the two branch capacities and the root's discharge bound. The zero polynomial supplies no actual split and can be deleted; an unused node may be removed without increasing depth. If the quadratic lies j linear nodes below the subtree root along its unique path, a necessary relaxed predicate F_k(S,d,j) is defined by:
  F_k(S,d,0) = [c(S) <= 2^d-2+k].
  F_k(S,d,j) = false if c(S)>2^d-2+k or d<=1 for j>0.
  Otherwise F_k(S,d,j) is the existential over the complete linear mask bank and the two possible branch orientations (U,V), of G(U,d-1) AND F_k(V,d-1,j-1).
For j=0 we permit even arbitrary partitions at the quadratic, ignoring geometry and its pure-linear descendants. This is a necessary test, not an existence proof. The induction is immediate from the unique nonlinear node having only one path, with its sibling purely linear. Every subsequent computation retains the actual directed-germ masks, not only label totals.

At a linear root of a six-level tree, at least one of its two strict branches must pass G(.,5). If both pass the entire pure-linear capacity relaxation passes, which the complete bank calculation below rules out. If neither passes, a single quadratic cannot help both branches. Thus the branch T containing the unique quadratic is forced. This assertion is only about the relaxation; zero-germ paths are deliberately ignored conservatively.

## 2. Exact prefix location experiment

All 2225 linear root masks checked: 0 both branches feasible, 490 neither, 1735 exactly one. The latter require the quadratic in the failed branch. Applying the bound and F yields the following numbers of root masks (counts not distinct quadratic forms), at absolute quadratic depth j+1 with the root at depth 0:

| maximum distinct necessary support factors k | depth 1 | depth 2 | depth 3 | depth 4 | depth 5 |
|---|---:|---:|---:|---:|---:|
| 0 | 34 | 0 | 0 | 0 | 0 |
| 1 | 87 | 1 | 0 | 0 | 0 |
| 2 | 122 | 14 | 0 | 0 | 0 |

For k=0 the 34 forced branches have label counts 27:2, 28:4, 29:14, 30:14. For k=1 add 53 with count31; for k=2 add 35 with count32. The depth2 possible prefixes for k=1 consist of one root, one prefix, one target state; for k=2 they consist of 14 roots, 15 prefixes, two distinct target states. Their target masks in hex are 5c3030003f31230000fc0 and c000003ffc0c2003ffc030 (only the first for k=1). Prefix classification used 3,374,652 exact inherited can() observation checks, inclusive of 3,275,335 checks in the common initial root classification. No cutoffs.

Consequently any factor-free quadratic strictly below a linear root must occur at depth 1, and any quadratic whatsoever with a necessary support factor can occur at most at depth 2.

## 3. Complete internal product closure

For any real product Q=LM, let (a,b) and (c,e) be the two factors' strict sign masks on the current target S. Its strict signs are exactly
  X=(a & c) | (b & e), Y=(a & e) | (b & c).
Zero germs are precisely the union of the factor zero germs; do not replace these by a symmetric difference. Branch-swap canonicalization of each factor is safe because it can only exchange X,Y. Deduplicate factor partitions only after restricting to the *same* target S, an exact congruence for these set operations and the subsequent pure-linear capacity recursion.

There are 47 necessary support factor masks and 2178 masks without a zero germ in the complete 2225 mask bank. A nonzero linear factor has a zero germ iff it is proportional to a necessary support. Thus every product is covered by (i) two no-zero factors, (ii) one support factor and one no-zero factor, or (iii) two support factors, including repeated factors. Use k=0,1,2 respectively (k=2 is a harmless overbound for repeated factors). At the possible Q node at remaining depth d, exhaust the corresponding product masks on S, requiring c(X),c(Y)<=2^(d-1)-1 and G(X,d-1) AND G(Y,d-1). This is again a necessary condition; relaxed survivors would not be actual trees. In the no-zero case XOR of canonical restricted negative masks and its complement suffices exactly (the two factors partition S).

Actual exact results:

| product type | depth1 targets | depth2 distinct targets | factor-pair visits | feasible relaxed targets |
|---|---:|---:|---:|---:|
| no support factors | 34 | 0 | 7,115,144 | 0 |
| one support + no-zero factor | 87 | 1 | 2,078,621 | 0 |
| two support factors (incl. repeat) | 122 | 2 | 156,165 | 0 |

For no-support products the restricted factor bank sizes range from 459 to 888; only 230 distinct product masks (counted per target, after per-target dedup) passed direct capacity, all then excluded. Exact inherited can() checks: 3,331,998 for that run inclusive of common root classification; 3,722,043 for the combined support-product run inclusive of common classification. Counts are per executed run, not unique across the three runs. All searches exhausted (no early witness), no cutoff. Every possible internal product placement is excluded, not just products at the root. Unlike the earlier root proof R242, these internal cases require no midpoint refinement.

**Theorem.** Under the frozen necessary-wall/linear capacity completeness premises, no correct depth-six decision tree using arbitrary linear queries and only one quadratic query can use a real-decomposable quadratic Q=LM at *any* node. Proof: R242 covers root placement. Sections 1–3 cover every other depth and factor class, including repeated factors, with finite exact exhaustion. QED.

A nonzero semidefinite quadratic of rank >=2 has no zero germ (otherwise it has a real support factor), so all its directed germs have a single strict sign. Such a query cannot repair a failure of G: replacing it by the one pure-linear branch yields a pure-linear capacity witness with no more depth, contradicting the root classification (or, if the quadratic itself is root, the depth-five capacity). Rank-one semidefinite quadratics are already products. A singular indefinite real ternary quadratic factors over R. Therefore **any successful unique quadratic in a depth-six tree must be full-rank indefinite and must be either the root, or its immediate child in one of the 34 forced root masks.** No general full-rank indefinite mask has been proved feasible. K6 remains 1–2, general root and 34 internal candidates open.

## 4. Exact reproduction of actual computations

Read the first JavaScript code block of the pinned R247 note as src. The three executed variants below independently replace its final return and the outer experiment call; all of the original input, linear arrangement, S (support masks), ordered (complete bank), c=count and G=can remain unchanged. BigInt masks and label counts exact. In the original helper, a CUT throws on ceiling, so an uncaught cutoff cannot be reported as an exclusion. Each variant sets ceiling=100000000. The output summaries stated above are from actual executed variants, not predictions. All full product loops returned no witness.

```javascript
// Common root prefix, present in all three variants.
const common = `ceiling=100000000;let roots=[];
for(let [a,b] of ordered){
 let ca=can(a,5),cb=can(b,5);
 if(ca&&cb)throw Error("linear six");
 if(ca===cb)continue;
 let t=ca?b:a,u=ca?a:b;
 roots.push([t,u,count(t),count(u)]);
}
let initialChecks=checks;`;
const placement = `
function mixed(t,d,k,j,memo){
 if(count(t)>2**d-2+k)return false;
 if(j===0)return true;
 if(d<=1)return false;
 let key=[t,d,k,j].join();
 if(memo.has(key))return memo.get(key);
 for(let [a,b] of ordered){
  let x=a&t,y=b&t;
  for(let [u,v] of [[x,y],[y,x]]){
   if(count(u)>2**(d-1)-1||count(v)>2**(d-1)-2+k)continue;
   if(can(u,d-1)&&mixed(v,d-1,k,j-1,memo)){memo.set(key,true);return true}
  }
 }
 memo.set(key,false);return false
}
let out={};for(let k of [0,1,2]){
 let memo=new Map(),levels=[];
 for(let j=0;j<5;j++){
  let r=roots.filter(([t])=>mixed(t,5,k,j,memo));
  levels.push({n:r.length,counts:r.reduce((h,[t,u,c])=>(h[c]=(h[c]||0)+1,h),{}),masks:r.map(([t,u])=>[t.toString(16),u.toString(16)])})
 }
 out[k]=levels
}
return {bank:ordered.length,roots:roots.length,initialChecks,checks,out};`;
const supports = `
let result={};for(let k of [1,2]){
 let prefix=[],states=new Set(),r0=roots.filter(([t])=>count(t)<=30+k);
 for(let [t,u] of r0)for(let [a,b] of ordered){
  let x=a&t,y=b&t;
  for(let [w,v] of [[x,y],[y,x]]){
   if(count(w)>15||count(v)>14+k)continue;
   if(can(w,4)){prefix.push([t,u,w,v]);states.add(v)}
  }
 }
 let suffix=k===1?ordered.filter(([a,b])=>(a|b)===ALL):S;
 let memo=new Map(),pairVisits=0;
 function prodCan(t,d){
  let key=t+","+d;if(memo.has(key))return memo.get(key);
  let left=new Map(),right=new Map();
  for(let [a,b] of S){let [x,y]=canon(a&t,b&t);left.set(x+","+y,[x,y])}
  for(let [a,b] of suffix){let [x,y]=canon(a&t,b&t);right.set(x+","+y,[x,y])}
  for(let [a,b] of left.values())for(let [c,e] of right.values()){
   pairVisits++;
   let x=(a&c)|(b&e),y=(a&e)|(b&c),cap=2**(d-1)-1;
   if(count(x)>cap||count(y)>cap)continue;
   if(can(x,d-1)&&can(y,d-1)){let res=[a,b,c,e,x,y].map(z=>z.toString(16));memo.set(key,res);return res}
  }
  memo.set(key,null);return null
 }
 let p0=r0.map(([t,u])=>[t,u,prodCan(t,5)]);
 let p1=[...states].map(t=>[t,prodCan(t,4)]);
 let keep0=p0.filter(z=>z[2]),keep1=p1.filter(z=>z[1]);
 let validP=prefix.filter(z=>memo.get(z[3]+",4"));
 result[k]={r0:r0.length,states:states.size,prefix:prefix.length,prefixRoots:new Set(prefix.map(z=>z[0]+","+z[1])).size,keep0:keep0.length,keep1:keep1.length,validPrefix:validP.length,validRoots:new Set(validP.map(z=>z[0]+","+z[1])).size,pairVisits,stateMasks:[...states].map(t=>t.toString(16))};
}
return {bank:ordered.length,roots:roots.length,initialChecks,checks,result};`;
const factorFree = `
roots=roots.filter(([t])=>count(t)<=30);
let bank=ordered.filter(([a,b])=>(a|b)===ALL),visits=0,afterCount=0,results=[];
for(let [t,u,c,d] of roots){
 let M=new Set();
 for(let [a,b] of bank){let [x,y]=canon(a&t,b&t);if((x|y)!==t)throw Error("not partition");M.add(x)}
 let A=[...M],tested=new Set(),witness=null;
 for(let i=0;i<A.length&&!witness;i++)for(let j=i;j<A.length;j++){
  visits++;let x=A[i]^A[j],y=t^x;[x,y]=canon(x,y);
  if(tested.has(x))continue;tested.add(x);
  if(count(x)>15||count(y)>15)continue;afterCount++;
  if(can(x,4)&&can(y,4)){witness=[A[i],A[j],x,y].map(x=>x.toString(16));break}
 }
 results.push({t:t.toString(16),u:u.toString(16),c,d,restricted:A.length,visited:tested.size,witness})
}
return {bank:bank.length,initialChecks,checks,visits,afterCount,results};`;
function run(src,patch){
 const old='return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};';
 if(!src.includes(old))throw Error("pin mismatch");
 let v=src.replace(old,common+patch).replace(/experiment\(data\)\s*$/,"return experiment(data)");
 return Function(v)()
}
// run(src,placement), run(src,supports), run(src,factorFree)
// Consolidated reproduction: actual variants were executed separately with the same common logic;
// factorFree filtered during initial root loop rather than after, which is equivalent.
```

## 5. Next

Do not repeat R242 product root or R250 internal product coverage. The remaining unique-query problem has only two placements: full-rank indefinite root, or full-rank indefinite depth1 in the 34 root masks generated by factorFree. For the latter, restrict the R233 six-coefficient lift to the actual target germs T and require pure-linear depth4 children; use monotone capacity-conflict certificates / oriented sign feasibility, rather than enumerating all poles. A candidate must still pass the true decision-tree output and clipped-interval checks beyond the relaxation. General root problem and prior R249 narrow interval remain unchanged. Independent review and Activity binding pending.
