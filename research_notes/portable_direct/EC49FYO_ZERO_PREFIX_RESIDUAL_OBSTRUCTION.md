# EC49FYO — joint all-zero prefix residual obstruction for three and four holes

2026-11-24. Research-4 continuation, historical Researcher EM-DIRECT-23537B / RA-2D7B4AD1AA5CD3F5D9EF1C76 (original registration SUCCEEDED; current private write binding not verified). Parent EC49FYN, immutable 0e4e800d1a3f3efa4f58950309aa5fcfb33e4733:research_notes/portable_direct/EC49FYN_TWO_HOLE_UNIFORM_OBSTRUCTION.md. Frozen scientific input BRC16943, the 50 masks copied exactly from that parent's verifier below. Auxiliary observation model, no new native X6 dynamics attribution or P000 change.

## Result

For every integer m>h, in the fixed support family F, unit-cost noiseless Boolean observations W(U,Z)(t,j)=1[t in U]1[j not in Z], |Z|<=h, we prove Q_3(m)>=m+5 and Q_4(m)>=m+6. This improves FYN's uniform lower bounds and yields c_3 in {5,6}, c_4 in {6,7,8} using FYM's parent-dependent upper c_h<=2h. No large-m search or numerical extrapolation is used. The key is to retain the joint row/column negative residual across successive observations, not just the first-touch miss count.

## Prefix residual inequality (arbitrary finite support family of distinct nonempty masks)

A correct deterministic tree never needs to repeat the same physical probe on a path; erase repeats and contract deterministic nodes. Consider an all-zero prefix with k touched columns and nonempty row masks M_j for the distinct probes in each. For a support U, let H be any subset of touched columns, |H|<=h-1, containing every j with M_j & U nonzero. Choose the actual target (U,H), with all other columns live. It is compatible with every answer of the prefix. This choice is valid for m>h and k<=m, no need to pad the holes.

Each live column must ultimately exhibit a positive probe, to distinguish the legal competitor with that column also removed. Each hole must be queried in a row of U, to distinguish the competitor with that hole filled. These obligations cost at least m distinct probes. Let N be the union of M_j over live columns; by compatibility N is disjoint from U. Define tau_U(N) as the minimum cardinality of a row mask T hitting every strict-superset difference V\U not already hit by N. The live negative probes must collectively hit all such differences, since (V,H) is legal. Thus the additional probes beyond m are bounded below by

E(U,H;M) = sum_j |M_j| - sum_{j in H} 1[M_j intersects U] + tau_U(N).

Indeed, all prefix live negatives count as additional probes; each prefix hole query except at most one mandatory query at a row of U counts as additional, and at least tau_U(N) further live negatives are required. These three charges are disjoint. The inequality applies even when some prefix probes in different live columns share a row, since their costs are counted separately while N records their shared elimination effect.

Let B(M)=max E over the above compatible targets, and -1 when none exists. Any decision tree of depth <=m+c must have B(M)<=c at every such prefix. A prefix with B(M)>=0 cannot terminate correctly: its target has <=h-1 holes, and turning any live column into a hole preserves the entire all-zero prefix and gives a distinct legal state (m>h). If B(M)>c, that target already forces depth >m+c regardless of later answers.

Columns are exchangeable: sorted multisets of nonempty row masks suffice for this lower-bound test. Enumerate from empty M, extending by adding any unqueried row to one existing column or probing any row in a fresh column, sorting after the operation. Allowing arbitrarily many new columns enlarges the search space, so a contradiction also holds for every finite m. Keep a successor iff 0<=B<=c. Separately count every successor with B=-1; such successors could escape the low-hole adversary and must NOT be silently pruned as impossible. If no such escape occurs and the surviving layer becomes empty, no correct tree of depth m+c exists: induction follows its all-zero path, which must continue at each surviving node. All possible next distinct physical probes are covered by the extensions, and any actual prefix is among the enumerated ones up to permutation. Therefore the finite certificate proves a uniform impossibility for all m>h, even where the enumerated superproblem allows too many fresh columns.

## Exact verification

The JavaScript verifier below was actually executed using integer bit masks (<=1023 for rows, <=511 for column subsets in these runs). It independently agrees with a Python enumeration using explicit subsets of optional holes and cached transversal checks. For h=3,c=4, the successive surviving-state counts are 10,24,37,30,9,2,0; for h=4,c=5 they are 10,100,388,322,406,168,19,10,0. No empty-target escape in either search. Unique candidate successor masks tested (memo entries): 2976 and 33136 respectively. Hence both impossibility certificates close. A separate Python exploratory run for h=5,c=6 reached depth 6 with 3529 survivors before its execution timeout; no h=5 closure is asserted. The finite enumeration verifies all choices in the stated enlarged prefix problem, not a finite sample of m.

```js
const F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005];
const pc=Array.from({length:1024},(_,x)=>x.toString(2).replace(/0/g,"").length);
const rows=Array.from({length:1024},(_,x)=>x).sort((a,b)=>pc[a]-pc[b]);
const ts=F.map(u=>{const ds=F.filter(v=>v!==u&&(v&u)===u).map(v=>v^u);return Array.from({length:1024},(_,z)=>pc[rows.find(t=>ds.every(d=>d&(t|z)))])});
for(const [h,c,L] of [[3,4,7],[4,5,9]]){
 let s=new Map([["",[]]]),counts=[];const memo=new Map();
 const bound=a=>{const key=a.join();if(memo.has(key))return memo.get(key);let w=-1;const k=a.length;
 for(let i=0;i<F.length;i++){const u=F[i];let must=0;for(let j=0;j<k;j++)if(a[j]&u)must|=1<<j;if(pc[must]>=h)continue;
 for(let z=0;z<(1<<k);z++){if((z&must)!==must||pc[z]>=h)continue;let n=0,b=0;for(let j=0;j<k;j++){b+=pc[a[j]];if(z>>j&1){if(a[j]&u)b--}else n|=a[j]}w=Math.max(w,b+ts[i][n]);if(w>c){memo.set(key,w);return w}}
 }memo.set(key,w);return w};
 for(let d=1;d<=L;d++){let next=new Map(),empty=0;for(const a of s.values())for(let j=0;j<=a.length;j++)for(let t=0;t<10;t++){let b=1<<t;if(j<a.length&&(a[j]&b))continue;let q=a.slice();if(j===a.length)q.push(b);else q[j]|=b;q.sort((x,y)=>x-y);let w=bound(q);if(w<0)empty++;else if(w<=c)next.set(q.join(),q)}counts.push([d,next.size,empty]);s=next}
 console.log(JSON.stringify({h,c,counts,memo:memo.size,final:s.size}));
}
```

Actual output (entries are depth, surviving canonical prefixes, empty-target successor transitions):
```json
{"h":3,"c":4,"counts":[[1,10,0],[2,24,0],[3,37,0],[4,30,0],[5,9,0],[6,2,0],[7,0,0]],"memo":2976,"final":0}
{"h":4,"c":5,"counts":[[1,10,0],[2,100,0],[3,388,0],[4,322,0],[5,406,0],[6,168,0],[7,19,0],[8,10,0],[9,0,0]],"memo":33136,"final":0}
```

Note the verifier early-exits B as soon as B>c, because the exact larger value is unnecessary; it checks all legal low-hole target subsets otherwise. For the displayed cases the largest column-mask domain fits the precomputed popcount table.

## Next

Construct a finite m0 three-hole depth m0+5 tree (which by FYL's one-column extension would imply c3=5), or exclude m+5 uniformly. Improve prefix lower-bound search by optimizing enumeration of optional holes and replacing the strict-superset-only residual with additional pairwise separation obligations. The h=5,c=6 search remains incomplete. No formal task claim, Result or Review: current exact task lookup r4-20261124-0930-ec49as-task-read-v1 SUCCEEDED, Source ba34624744fdc7695ffeb0c27960df7cb4297c3e, NO_CANONICAL_PUBLICATION_DIRECTORY (limited absence observation, not owner projection). Existing source activity association is separate from this scientific save.

Status AUTHOR_PROVED / EXACT_FINITE_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.
