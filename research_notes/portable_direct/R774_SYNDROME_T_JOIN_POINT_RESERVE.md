# R774 — Exact syndrome coordinates and weighted point-terminal reserve via T-joins

2026-11-24. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R773, 8c9c1a69883a9d97653bf131414ab20423a0f57f:research_notes/portable_direct/R773_ALL_RANK_HALL_DEFICIT_RESERVE.md (read statement/proof). Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged; P000 V5 and joint-relation observer contract read at pin (blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447, 3923890d77a02d84b772f789e6912dd14f220d14). ACTIVE worldview, current portable and continuation protocols, account math/output/BRC/residual rules and public method record consulted. Frozen Heartbeat companion path returned 404; no repin. R773's Boolean auxiliary observer only, no native signed/weighted BRC or physical attribution. Existing own registration metadata verified SUCCEEDED, no runs, execution_authorized=false; owner inventory r3-20261124-2320-owner-read-v1 last observed RUNNING before publication. No shared claim or formal task transition.

## 1. Exact quotient coordinate theorem

G is a finite loop-free subcubic multigraph, with private ports completing each vertex to three ports. V_i is the even binary triple space, V=product V_i. K is the space of graph cycles (even edge subsets), represented by equal bits at the two ends of each chosen edge and zero private bits. q:V -> V/K. As R773, S(0)={0}, S(1)=V_i minus {0}, S(2)=V_i, P(p)=product S(p_i); k_p(w) is the least sum t_i with q(P(p))+w subset q(P(t)), where w is a quotient target.

For y in V define sigma_e(y)=y_(u,e) xor y_(v,e) for each graph edge, and sigma_b(y)=y_b for each private port. All these bits are retained. Kernel sigma=K: zero syndrome means edge bits match, private bits vanish, and even local parity is precisely the cycle condition. Thus sigma is a faithful linear coordinate for the quotient; it does not discard any future addition or Boolean inclusion information in this observer. Image is exactly the syndrome vectors having even total parity on each connected component. Necessity follows by summing local parities; sufficiency by dimension: if n,m,c count vertices, edges and components, there are 3n-m syndrome bits and c independent nonempty component constraints. Their dimension 3n-m-c=2n-r, r=m-n+c, equals dim V/K. Hence one bit per component can be reconstructed from others. Isolated vertices and parallel edges allowed. Empty graph trivial. This is not a native spatial coordinate replacement.

## 2. Exact point-terminal theorem (p=0), with nonnegative vertex costs

Let w be any legal syndrome, and alpha_v>=0 any assigned vertex cost for a single active auxiliary event. Let d_alpha(w)=min_{sigma(y)=w} sum_{v:y_v!=0} alpha_v. This is the minimum weighted reserve for empty prefix; unit alpha gives k_0(w).

Build an auxiliary undirected graph H_w:
- every syndrome-zero original edge uv stays as an edge of weight alpha_u+alpha_v;
- every syndrome-one edge uv is subdivided by a new terminal b_e, replacing it by u-b_e and v-b_e of weights alpha_u and alpha_v respectively;
- every syndrome-one private port gets a terminal leaf adjacent to its vertex v, weight alpha_v; syndrome-zero private ports are omitted.
All new terminals comprise T; all original vertices are nonterminals. A T-join means an edge subset whose odd-degree vertex set is exactly T.

Then
    2 d_alpha(w) = min_{F a T-join of H_w} sum_{e in F} weight(e).
Proof: map each syndrome-zero edge to the shared chosen half-port bit, each syndrome-one edge to exactly one of its two half-edges according to the chosen active endpoint, and each active private port to its mandatory leaf edge. The degree at an original vertex is the number of its active port bits, 0 or 2, since the local triple has even parity. Each terminal has degree one (degree at most two, odd). Conversely these parity conditions reconstruct exactly a y with syndrome w. Weight sum is sum_v alpha_v deg_F(v), exactly twice active-vertex cost. This is a bijection, not just a cost inequality; witness recovery is direct. There is always a feasible join for legal w, by section 1. Nonnegative weights are sufficient, including zeros. This auxiliary vertex weighting is not a BRC signed-amplitude or mass identity.

Equivalently the minimum is the shortest-path metric perfect matching on T (pairs must lie in same connected component). Any join decomposes into trails pairing odd vertices and closed trails; remove the closed trails and bound each open trail below by the metric distance. Conversely take shortest paths for any matching and xor their edge sets, producing a join at no greater cost since weights are nonnegative. Empty T has value zero. This proves equality and gives a standard polynomial-size matching reduction, rather than enumerating 2^r lifts. Graph construction uses O(n+m) vertices/edges. Standard shortest-path and minimum-weight perfect matching algorithms suffice; no runtime benchmark or particular production implementation claimed. The checker below uses exponential subset matching only to verify small exact instances.

For unit weights let M be the number of syndrome-one edges and private ports. Every join has exactly M selected terminal edges of weight one, and all other selected edges have weight two. Therefore
    k_0(w) = M/2 + min_F |F intersect {syndrome-zero original edges}|.
M is even per connected component. This splits local boundary discrepancy from the residual cost of transporting it through the retained joint graph. Two targets with the same M need not have the same cost: on a path with n>=2 vertices, take precisely two active private ports at distinct vertices i,j, all edge syndromes zero. The selected path is forced (tree), so cost |i-j|+1. In particular equal M=2 permits cost 2 or n.

## 3. Consequences for nonempty prefix (bounds, not a full spectrum formula)

Use d(w)=k_0(w) with unit costs. It is a translation-invariant metric on the quotient: positivity follows from the zero support, symmetry from exponent two, and subadditivity from adding representatives (support of a sum lies in union). For every prefix p,
    max(k_p(0), max_{x in q(P(p))} d(x+w)) <= k_p(w) <= k_p(0)+d(w)
where the first k_p(0) inequality uses R773, conditional on its R770 dependency. The pointwise bound holds because a reserve t realizing any single point has cost >= its minimum point cost. The upper bound uses an optimal zero reserve and a minimum-support lift of w; add one event at each active vertex of the lift, truncating at two; S(a)+S(b)=S(min(a+b,2)). More generally |k_p(w)-k_p(w')|<=d(w+w') by the same argument. These bounds preserve exact terminal information instead of treating all nonzero targets as interchangeable.

The pointwise lower bound alone is not sufficient for the fixed universal reserve problem. On one isolated vertex take p=1, w!=0. The translated three-point prefix contains zero and two nonzero points. Every point costs at most one, but S(1) excludes zero and S(0) has only one point, so k_p(w)=2. This is an explicit separation between adaptive point correction and one fixed inventory that must accommodate all possible prefix states.

If r=0, q is injective and the full target spectrum is local: at p_i=0 cost 1_{w_i!=0}; at p_i=1 cost 1+1_{w_i!=0}; at p_i=2 cost 2. Sum over vertices. More generally delete all bridges and regard their endpoint ports as private (keep the original target lift at both ends). The cycle kernel factors over the remaining connected blocks since no even edge subset contains a bridge. Both q and P factor, so the feasible reserve and the minimum cost factor as a sum of block costs for ANY p,w. This uses the two separate bridge half-port bits, not just their xor, in the block coordinates; they are recovered from the quotient or chosen lift and are invariant under K.

## 4. Exact verification

Enumerated every local even-triple configuration for each of 12 specified graphs, grouped by the syndrome and independently minimized the active-vertex cost. Compared with shortest-path subset perfect matching on the auxiliary graph for unit and deterministic nonuniform positive integer weights (1+i mod 3). All exact integer comparisons passed; Infinity merely represents disconnected pairs. The exact proof covers all graphs, the run below covers these instances only. Results:
```json
[
  {
    "n": 1,
    "edges": 0,
    "states": 4,
    "syndromes": 4,
    "weightedChecks": 8
  },
  {
    "n": 2,
    "edges": 1,
    "states": 16,
    "syndromes": 16,
    "weightedChecks": 32
  },
  {
    "n": 2,
    "edges": 2,
    "states": 16,
    "syndromes": 8,
    "weightedChecks": 16
  },
  {
    "n": 2,
    "edges": 3,
    "states": 16,
    "syndromes": 4,
    "weightedChecks": 8
  },
  {
    "n": 3,
    "edges": 3,
    "states": 64,
    "syndromes": 32,
    "weightedChecks": 64
  },
  {
    "n": 4,
    "edges": 3,
    "states": 256,
    "syndromes": 256,
    "weightedChecks": 512
  },
  {
    "n": 4,
    "edges": 4,
    "states": 256,
    "syndromes": 128,
    "weightedChecks": 256
  },
  {
    "n": 4,
    "edges": 6,
    "states": 256,
    "syndromes": 32,
    "weightedChecks": 64
  },
  {
    "n": 5,
    "edges": 7,
    "states": 1024,
    "syndromes": 128,
    "weightedChecks": 256
  },
  {
    "n": 6,
    "edges": 9,
    "states": 4096,
    "syndromes": 256,
    "weightedChecks": 512
  },
  {
    "n": 6,
    "edges": 9,
    "states": 4096,
    "syndromes": 256,
    "weightedChecks": 512
  },
  {
    "n": 4,
    "edges": 2,
    "states": 256,
    "syndromes": 256,
    "weightedChecks": 512
  }
]
```
Executable JavaScript (node or equivalent):
```javascript
function verify(){
 const graphs=[[1,[]],[2,[[0,1]]],[2,[[0,1],[0,1]]],[2,[[0,1],[0,1],[0,1]]],[3,[[0,1],[1,2],[2,0]]],[4,[[0,1],[1,2],[2,3]]],[4,[[0,1],[1,2],[2,0],[2,3]]],[4,[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]],[5,[[0,4],[4,1],[0,2],[0,3],[1,2],[1,3],[2,3]]],[6,Array.from({length:9},(_,i)=>[Math.floor(i/3),3+i%3])],[6,[[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[0,3],[1,4],[2,5]]],[4,[[0,1],[2,3]]]];
 let out=[];
 for(const [n,E] of graphs){
  const inc=Array.from({length:n},()=>[]),ports=[];
  E.forEach(([u,v],e)=>{ports.push([u,inc[u].length,v,inc[v].length]);inc[u].push(e);inc[v].push(e)});
  const privatePorts=[];for(let i=0;i<n;i++)for(let j=inc[i].length;j<3;j++)privatePorts.push([i,j]);
  const tri=[0,5,6,3],bit=(s,i,j)=>(tri[(s>>(2*i))&3]>>j)&1;
  const q=s=>{let a=0;ports.forEach(([u,j,v,k],e)=>a|=(bit(s,u,j)^bit(s,v,k))<<e);privatePorts.forEach(([v,j],k)=>a|=bit(s,v,j)<<(E.length+k));return a};
  let row={n,edges:E.length,states:4**n,syndromes:0,weightedChecks:0};
  for(const weights of [Array(n).fill(1),Array.from({length:n},(_,i)=>1+i%3)]){
   const truth=new Map();for(let s=0;s<4**n;s++){let c=0;for(let i=0;i<n;i++)if((s>>(2*i))&3)c+=weights[i];let a=q(s);truth.set(a,Math.min(truth.get(a)??Infinity,c))}
   row.syndromes=truth.size;
   for(const [a,c] of truth){
    let N=n,edges=[],T=[];
    ports.forEach(([u,j,v,k],e)=>{if((a>>e)&1){let b=N++;T.push(b);edges.push([u,b,weights[u]],[v,b,weights[v]])}else edges.push([u,v,weights[u]+weights[v]])});
    privatePorts.forEach(([v,j],k)=>{if((a>>(E.length+k))&1){let b=N++;T.push(b);edges.push([v,b,weights[v]])}});
    const d=Array.from({length:N},(_,i)=>Array.from({length:N},(_,j)=>i===j?0:Infinity));
    for(const [u,v,w] of edges)d[u][v]=d[v][u]=Math.min(d[u][v],w);
    for(let k=0;k<N;k++)for(let i=0;i<N;i++)for(let j=0;j<N;j++)d[i][j]=Math.min(d[i][j],d[i][k]+d[k][j]);
    let memo=new Map([[0,0]]);
    function match(m){if(memo.has(m))return memo.get(m);let l=m&-m,i=31-Math.clz32(l),r=m^l,best=Infinity;for(let u=r;u;u&=u-1){let k=u&-u,j=31-Math.clz32(k);best=Math.min(best,d[T[i]][T[j]]+match(r^k))}memo.set(m,best);return best}
    let got=match((1<<T.length)-1);if(got!==2*c)throw Error(JSON.stringify({n,E,a,weights,c,got}));row.weightedChecks++;
   }
  }
  out.push(row)
 }
 return out;
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next question

Find an exact fixed-universal-reserve formula for mixed prefix inventories and nonzero targets, beyond the metric bounds. In particular separate the cost of satisfying pointwise syndrome transport from the extra cost of one fixed reserve across the prefix fiber; investigate whether the R773 Hall deficit admits a target-specific extension. Keep native signed/ordered/provenance/common-depth observations separate. No new formal Result or theorem admission asserted.
