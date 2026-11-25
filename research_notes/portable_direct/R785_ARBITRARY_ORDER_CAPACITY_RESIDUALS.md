# R785 - Arbitrarily high-order joint residuals from shared capacity

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R779_R783 / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R784. Own session metadata request r3-20261125-1020-own-metadata-v1 confirms existing registration, no runs and execution_authorized=false; own Activity RA-708BCC309CE076D8BB599B91, EM-DIRECT-82A007 / TASK_RESEARCH. Owner inventory r3-20261125-1020-owner-read-v1 last observed RUNNING before publication. No shared Task or CLAIM changed. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-relation contract blob 3923890d77a02d84b772f789e6912dd14f220d14 verified directly. Current ACTIVE worldview, portable and continuation protocols and BRC preference read; attempted frozen weighted companion path unavailable, no native weighted execution claimed. Exact predecessors:
- 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md
- 236e6fea7374ac883a0fe12e2083cfcb31ada64b:research_notes/portable_direct/R783_MATCHING_REPRESENTATION_AND_SPARSE_BOUNDARY.md
- 5e37acd866dc1860c5534da22d57e8e03de461c8:research_notes/portable_direct/R784_LONG_EVEN_CYCLE_AND_CACTUS_BOUNDARY.md

## 1. Exact capacity relation and realization

Use the R779 fixed-prefix Boolean auxiliary Port observer, normalized at a feasible zero assignment. Let A,B be disjoint labeled terminal sets of sizes m,n>=1. For 0<=r<=min(m,n), define E_r={D subset A union B: |D intersect A|=|D intersect B|<=r}. Every such E_r is exactly realizable by a matching-deletion graph, hence by the original unsigned trivalent Port observer by R783 Theorem A converse (zero prefix and fixed reserves). This is a constructive statement for arbitrary finite sizes, not a classification inferred from sampling.

Construction: retain all m+n terminal leaves and introduce their private partners a_i',b_j'. Introduce r disjoint slot pairs x_l,y_l, each joined by an edge. Each a_i' joins every x_l; each b_j' joins every y_l. There are 2(m+n+r) vertices, and m+n+r+r(m+n) edges. In any perfect matching of H-D each undeleted terminal forces its partner to match it. Every freed A partner must match an x slot and every freed B partner a y slot. Each slot pair either matches internally or both endpoints match freed partners (one on each side). Therefore the counts must agree and be at most r. Conversely, assign the freed partners on each side bijectively to the same chosen slots and match all remaining slot pairs internally. Thus the stated relation is exact. For r>=1 the pair graph is K_{m,n}; for r=0 the only feasible assignment is empty. The graph H is connected for r>=1. The Port conversion uses R783's count-tree gadgets and may have private pins; no separate native geometric identification is asserted.

Counting: |E_r|=sum_{k=0}^r binom(m,k)binom(n,k). For m=n and r=m, the count is binom(2m,m) by choosing m from two m-element sets. At r=m-1, exactly the full set is absent. In particular m=3 gives 19 versus 20 feasible boundary assignments out of 32 even labels; all proper-subset membership tests agree, including all pair and four-toggle tests. The pair graph is K_{3,3} in both. This is the first possible width where pair+four membership is insufficient, since at width <=5 every even assignment has size 0,2,4. This is not the claim that every K_{3,3} relation belongs to this family.

## 2. Exact symmetric classification and unbounded-order obstruction

Suppose a normalized realizable relation is invariant under every separate permutation of A and B and its pair graph is K_{m,n}. R779 paired exchange applied from empty to any feasible D partitions D into feasible pairs (toggle one at a time); every such pair crosses the bipartition. Hence D is balanced. Let r be the largest feasible balanced size on either side. The same paired exchange yields feasible balanced sets at every smaller size by toggling subsets of the pairs. Separate permutation invariance then makes every balanced set of each such size feasible. Thus the relation is exactly E_r, and conversely all these relations with 1<=r<=min(m,n) are realized. This class requires exactly min(m,n) possibilities for a fixed complete bipartite pair graph under the stated symmetry; the minimal fixed-length code is ceil(log2(min(m,n))) bits. A capacity integer is sufficient here. With empty pair graph r=0 is the extra symmetric case.

For any fixed proposed membership cutoff d, take m=n>=2 with 2m>d. E_m and E_{m-1} agree on ALL assignments of Hamming weight at most d but disagree on the full toggle. In fact they agree on every proper subset, and every strict coordinate restriction obtained by pinning the omitted labels to zero. For ordinary existential projections, the only additional tuple in E_m is all-ones; its projected value can be extended within E_{m-1} by omitting an A/B pair if omitted labels include both parts. If omitted labels lie in only one part, the projected all-ones value distinguishes them. Thus the proved obstruction is for bounded-support membership and zero-pinned restrictions, NOT arbitrary projections or all possible local observations. A real singleton exterior pinning every boundary bit to 1 distinguishes the two in R780's Boolean context observer. Such a singleton is realizable by R783 (or the parity pin gadgets of R779). No uniform bound on the order of toggle-membership directions can reconstruct all fixed-prefix boundary relations. This does not preclude compact alternative coordinates such as the capacity integer.

## 3. Many independent high-order bits with a connected pair graph

Fix m>=2 and q>=1. Make q disjoint labeled groups, each with an A_j,B_j of size m, and assign each group its capacity r_j=m-1 or m independently. Add a bridge pair between a chosen label of group j and one of group j+1 for each consecutive j. For a global terminal v use a new terminal leaf and center c_v. Join c_v to the local terminal of v in every incident block (capacity block or bridge block). A nondeleted global leaf forces its center to match it. A deleted leaf forces its center to match exactly one local terminal, which removes that terminal from its block's internal matching problem. A bridge block is just two terminals joined by an edge; either both or neither are deleted. Therefore the global relation consists exactly of disjoint unions of feasible block-local deletions, with no label assigned to two blocks. This is the selector construction of R784, used here for capacity blocks.

The pair graph is fixed and connected: q copies of K_{m,m} joined by the chosen bridge edges; a two-label deletion must occupy a single block because no block admits a singleton. For any global deletion D of size <2m, no local block can use its full set of 2m labels, so feasibility is independent of all q capacity bits. For D equal to the entire label set of group j, no bridge can be used because each bridge leads to a label outside D. Thus D is feasible precisely if r_j=m. Consequently the 2^q configurations yield 2^q different real relations on one fixed connected pair graph, all identical on every membership direction of size <2m. Any exact code supplementing these lower-order membership bits needs at least q bits in the worst case; on this constructed family q bits suffice. This is a quantitative obstruction to bounded-order state reconstruction, not an exponential lower bound in all possible representations. The singleton tests distinguish the relations even in the true contextual quotient of R780. The construction also gives an exact solver on this family by choosing disjoint bridge pairs and applying local capacity checks; no performance claim is made for arbitrary pair graphs.

## 4. Exact independent finite replay

The analytic arguments cover arbitrary finite m,n,r,q as stated. The executable certificate independently builds matching-deletion graphs and recursively checks perfect matchability via BigInt adjacency, versus the capacity formulas. It checks all m,n from 1 through 5 and all allowed r, every boundary mask including odd masks. It also checks two capacity blocks joined by a bridge, m=2,3, all four bit choices and every global mask. No random sampling, floating-point arithmetic or native weighted BRC run.

Actual output:
```json
{
  "configs": 80,
  "queries": 17752,
  "chainConfigs": 8,
  "chainQueries": 17408,
  "examples": [
    {
      "m": 1,
      "r": 0,
      "count": 1
    },
    {
      "m": 1,
      "r": 1,
      "count": 2
    },
    {
      "m": 2,
      "r": 1,
      "count": 5
    },
    {
      "m": 2,
      "r": 2,
      "count": 6
    },
    {
      "m": 3,
      "r": 2,
      "count": 19
    },
    {
      "m": 3,
      "r": 3,
      "count": 20
    },
    {
      "m": 4,
      "r": 3,
      "count": 69
    },
    {
      "m": 4,
      "r": 4,
      "count": 70
    },
    {
      "m": 5,
      "r": 4,
      "count": 251
    },
    {
      "m": 5,
      "r": 5,
      "count": 252
    }
  ],
  "failures": 0
}
```

Dependency-free JS:
```js
function verify(){
 const pop=x=>{let n=0;for(;x;x&=x-1)n++;return n};
 function builder(n){
  let N=n,edges=[];const add=()=>N++,edge=(a,b)=>edges.push([a,b]);
  function block(A,B,r){let a=A.map(v=>{let p=add();edge(v,p);return p}),b=B.map(v=>{let p=add();edge(v,p);return p});for(let i=0;i<r;i++){let x=add(),y=add();edge(x,y);a.forEach(p=>edge(p,x));b.forEach(p=>edge(p,y))}}
  function oracle(){let adj=Array(N).fill(0n),bit=i=>1n<<BigInt(i);for(let [u,v] of edges){adj[u]|=bit(v);adj[v]|=bit(u)}let memo=new Map([[0n,true]]);function pm(s){if(memo.has(s))return memo.get(s);let best=0n,v=0n,d=Infinity;for(let a=s;a;){let x=a&-a;a^=x;let nb=adj[x.toString(2).length-1]&s,k=0;for(let z=nb;z;z&=z-1n)k++;if(k<d){d=k;v=x;best=nb;if(k<=1)break}}let ok=false;for(let a=best;a;){let x=a&-a;a^=x;if(pm(s^v^x)){ok=true;break}}memo.set(s,ok);return ok}return s=>pm(((1n<<BigInt(N))-1n)^BigInt(s))}
  return {add,edge,block,oracle}
 }
 let configs=0,queries=0,chainConfigs=0,chainQueries=0,examples=[];
 for(let m=1;m<=5;m++)for(let n=1;n<=5;n++)for(let r=0;r<=Math.min(m,n);r++){
  let h=builder(m+n);h.block(Array.from({length:m},(_,i)=>i),Array.from({length:n},(_,i)=>m+i),r);let can=h.oracle(),count=0;
  for(let s=0;s<1<<(m+n);s++){let a=pop(s&((1<<m)-1)),b=pop(s>>m),p=a===b&&a<=r,q=can(s);if(p!==q)throw Error(JSON.stringify({m,n,r,s,p,q}));queries++;count+=Number(q)}
  configs++;if(m===n&&r>=m-1)examples.push({m,r,count});
 }
 for(let m of [2,3])for(let bits=0;bits<4;bits++){
  let n=4*m,h=builder(n),ports=Array.from({length:n},()=>[]),rs=[m-1+(bits&1),m-1+((bits>>1)&1)];
  for(let j=0;j<2;j++){let t=Array.from({length:2*m},(_,i)=>{let v=h.add();ports[j*2*m+i].push(v);return v});h.block(t.slice(0,m),t.slice(m),rs[j])}
  const u=m,v=2*m,bridge=(1<<u)|(1<<v),a=h.add(),b=h.add();h.edge(a,b);ports[u].push(a);ports[v].push(b);
  for(let i=0;i<n;i++){let c=h.add();h.edge(i,c);ports[i].forEach(t=>h.edge(c,t))}
  let can=h.oracle(),mask=(1<<m)-1,local=s=>[0,1].every(j=>{let x=pop((s>>(2*m*j))&mask),y=pop((s>>(2*m*j+m))&mask);return x===y&&x<=rs[j]});
  for(let s=0;s<1<<n;s++){let p=local(s)||((s&bridge)===bridge&&local(s^bridge)),q=can(s);if(p!==q)throw Error(JSON.stringify({m,bits,s,p,q}));chainQueries++}
  chainConfigs++;
 }
 return {configs,queries,chainConfigs,chainQueries,examples,failures:0}
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Continuation

The capacity-slot mechanism provides explicit higher joint residuals at every even order, while the symmetric family compresses them into a rank-like integer. Next: characterize nonsymmetric K_{3,3} relations and more generally bipartite pair graphs by matching-path bottlenecks; investigate whether an exact small family of capacity inequalities characterizes the matching-realizable relations or find a counterexample. The full six-cut dictionary and universal multiprefix optimization remain open. Preserve signed BRC, exact weights, path identities, event order, provenance and native X6/three-dimensional slice common depth as distinct observers. These graph computations concern only fixed-prefix Boolean boundary support.
