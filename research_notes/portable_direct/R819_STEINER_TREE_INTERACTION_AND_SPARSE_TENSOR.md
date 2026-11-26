# R819 — Steiner-tree interaction payment and sparse joint tensor approximation

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable TASK_RESEARCH continuation of R818, own session metadata recovered (EM-DIRECT-82A007, no execution authority); no shared CLAIM/RUN/Result or ownership change. RUNNING inventory r3-20261126-r819-running-read was RUNNING at derivation. Frozen scientific input a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 and joint observer read; frozen Heartbeat companion returned 404. Current global entries verified at 30365f921deefcd362ac206af7fd3d3451182730. Predecessor 6ec7954b78b6cd4cb1b350c946da2b3c1a5a2c25:research_notes/portable_direct/R818_BRANCHING_SEPARATOR_CENTERED_RESIDUAL.md, blob a39c1087296b2db6c233ff01f53a629169509160. Fixed-charge nonnegative auxiliary observer only; native signed BRC, original road matrices, paths, time, provenance and common depth remain retained.

## 1. Model
Let a finite tree of independent nonnegative joint groups have arbitrary local laws on the binary indicators for its incident edges. Terminal observations are separate leaf vertices with fixed binary indicator x_i. Each edge e is an R817 residual factor 1-D_e A_{ve} A_{we}, 0<=D_e<1, after absorbing its rank-one unary factors into groups and external unary weights. The latter can be factored exactly; restrict to their positive support if necessary. Z(x) is the remaining positive contraction; no assumption of independence of different indicators within a group. A group with no positive mass gives an exact zero separately. R813 unary/pinned oracle or explicit local table provides exact group contractions. Define interaction L_S=sum_{U subset S} (-1)^(|S|-|U|) log Z(1_U) for nonempty S; all unselected terminal values are zero. Constant and unary terms are retained exactly. For |S|>=2 let T_S be the minimal tree connecting these leaves. Integrate all branches off T_S at their actual real parameters and fixed terminals; each such branch is an exact nonnegative unary factor on its incident group. Renormalize each group (positive normalizing constants cancel from L_S). Thus only T_S remains and its internal laws may still be arbitrary.

## 2. Polydisc and Steiner theorem
Choose positive radii r_e on T_S with sum_{e incident v} r_e<=1/8 at every vertex, and D_e<=r_e for its edges. Then
 |L_S| <= (2^(|S|-1)/3) prod_{e in T_S} (D_e/r_e).       (1)
Proof: replace D_e by complex z_e with |z_e|<=r_e. Root the tree at any vertex. A child group sends its normalization times 1-z_e A_parent p_child, where p_child is its normalized complex indicator mean given descendant messages. Inductively |p_child|<=2, including deterministic leaves. The local product of incoming factors H satisfies |H-1|<=prod(1+2r_e)-1<=1/(1-2 sum r_e)-1<=1/3. The product bound follows by comparing elementary symmetric terms with powers of the sum. Thus |E H|>=2/3, |E(A H)|<=4/3, and the next mean has modulus <=2. Normalizations are nonzero, so the partition function and all its conditioned versions are nonzero on the closed polydisc, and their normalized analytic logarithms exist (sum of logs of the local normalizations, with branches defined by the disks around 1). This also gives a neighborhood by compactness. The same bounds apply with any fixed selected leaf assignments.

Root at a chosen selected leaf i. The ratio between its two assignments is exactly 1-z_e p_child, with other selected assignments held fixed, and |z_e p_child|<=1/4. Its analytic log has modulus <=(1/4)/(1-1/4)=1/3. Terminal unary log ratios, if retained, cancel in mixed differences. Taking the other |S|-1 differences bounds the holomorphic mixed difference L_S(z) by 2^(|S|-1)/3 uniformly on the polydisc. For every e in T_S, setting z_e=0 separates selected terminals into two nonempty sets; Z factors, hence its normalized log splits and the full mixed difference vanishes identically on that coordinate hyperplane. Its analytic series therefore contains every edge variable as a factor. Divide by prod z_e (removable singularities), then apply maximum modulus successively in every coordinate to bound its value by [2^(|S|-1)/3]/prod r_e. At the physical z_e=D_e this proves (1), including zero edges by continuity. This proof pays every Steiner edge once, not merely distances from one arbitrarily chosen root. It also handles arbitrary hard local correlations. No claim about complex/native BRC phases is made.

## 3. Polynomial sparse joint tensor for a bounded-degree class
Let the original contracted tree have n vertices, max degree Delta>=2 fixed, and choose r_e=1/(8 max(deg(v),deg(w))) using original degrees, so every vertex passes the sum condition and all pruned subtrees do too. Write theta=max_e D_e/r_e and q=2 Delta^2 theta. If q<1 and is separated from 1 by a fixed constant, keep all unary and constant interactions and all |S|>=2 with m=|E(T_S)|<=L. A tree with m edges has at most m+1 leaves. At most n Delta^(2m) connected m-edge subtrees can be encoded by rooted ordered DFS walks of length 2m; a minimal connecting subtree identifies its selected terminal subset by its leaves because terminals are original leaves. By (1), each term is at most 2^m theta^m/3. Thus the uniform log tail, for every assignment, is bounded by
 E_L <= (n/3) q^(L+1)/(1-q).                         (2)
Exact retained factors are R_S=exp(L_S)=prod_{U subset S} Z(1_U)^[(-1)^(|S|-|U|)], rational. Form Zhat(x)=Z(0) prod_{i:x_i=1} R_i prod_{S retained subset supp(x)} R_S. No exponentiation or logarithm is needed for this representation. Then exp(-E_L) Zhat<=Z<=exp(E_L) Zhat uniformly. For rational E_L<1, A=(1-E_L) Zhat gives A<=Z<=(1-E_L)^(-2) A, including after any nonnegative exterior contraction or external nonnegative event. The original full tensor/repair data remain accessible. Choose L=O(log(n/epsilon)) to achieve a uniform relative epsilon certificate on this fixed class. Enumerate DFS walks up to 2L, deduplicate subtrees, and use <=2^(L+1) pinned contractions per retained interaction; total polynomial in explicit input size and 1/epsilon for fixed Delta,q gap. Exact tree contraction uses leaf-to-root unary messages; explicit rational group tables have polynomial bit length overall by common denominators over input weights and sums of products. For implicit groups require a polynomial exact unary oracle with polynomial bit length for the composed tree (as in R813 exact tractable blocks). Factor products involve polynomially many rational values. The result is an efficiently evaluable sparse joint tensor for an arbitrary nonnegative exterior, not a claim that an arbitrary exterior can itself be contracted in polynomial time.

For actual R817 arms D_e<=4*125^(-l_e), if Delta=3 and each l_e>=2, theta<=96/15625, q<=1728/15625=0.110592. This is a uniform certificate independent of interface count. The total number of terminal leaves may grow linearly. By contrast R818's all-subsets expansion with a global sum of residuals can fail its sufficient condition as n grows.

## 4. Exact product-order obstruction
For an arbitrary tree with k>=2 terminal leaves and all internal degrees >=2, consider independent internal groups uniformly distributed on incident spin configurations whose product is +1. Each leaf fixes its spin sigma_i=(-1)^x_i. Put on each edge the strictly positive factor 1+t_e sigma_ve sigma_we (0<t_e<1). Expanding over edge subsets, every internal group contributes zero unless the selected incident edges are empty or its complete incident set. Connectivity and the fact that leaves have degree one force a nonempty surviving edge set to be the entire tree. Hence Z(x)=1+P prod_i sigma_i, P=prod_e t_e, up to common normalization. The full terminal interaction is exactly (-1)^k 2^(k-1) log[(1+P)/(1-P)], since the sign of each summand in the alternating difference matches parity. Its absolute value is asymptotic to 2^k P as all t_e go to zero. Each edge can be placed in the R817 one-entry residual form by endpoint relabeling and positive rank-one gauge: D_e=1-((1-t_e)/(1+t_e))^2=4t_e/(1+t_e)^2. Absorb unary gauges into the arbitrary local laws and terminal unaries, and the mixed log coordinate is invariant. Thus the product order over all Steiner edges cannot be uniformly improved to an additional power of any one edge for arbitrary local groups. This is an abstract auxiliary family, not a demonstrated actual Port realization.

## 5. Exact replay
The deterministic JS BigInt program below was executed. Five tree shapes, 12 configurations each, positive integer group weights, heterogeneous small rational edge residuals; compare direct all half-edge assignments against tree contraction for every terminal corner. Check rational consequences 1-B<=exp(L_S)<=1/(1-B) for B<=1/2 from (1), exact vanishing when any Steiner edge is removed, rational tail consequences from (2), and exact parity product identity using integer symmetric edge factors with even-parity local groups. These are finite real-arithmetic checks, not numerical tests of complex nonvanishing. The latter rests on the proof.
```json
{
  "cases": 60,
  "brute": 720,
  "steiner": 456,
  "cutCancellation": 1464,
  "truncation": 1632,
  "parity": 720
}
```
```javascript
function verify(){
 const gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a<0n?-a:a};
 const f=(a,b=1n)=>{if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]};
 const mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],eq=(a,b)=>le(a,b)&&le(b,a),one=f(1n);
 let seed=819, rnd=()=>((seed=(Math.imul(seed,1664525)+1013904223)>>>0)>>>16), stats={cases:0,brute:0,steiner:0,cutCancellation:0,truncation:0,parity:0};
 const ck=(ok,k)=>{if(!ok)throw Error(k);stats[k]++},pop=x=>{let n=0;for(;x;x&=x-1)n++;return n};
 const shapes=[[[0,1],[1,2]],[[0,1],[0,2],[0,3]],[[0,1],[0,2],[0,3],[3,4],[3,5]],[[0,1],[0,2],[0,3],[3,4],[4,5],[4,6]],[[0,1],[0,2],[0,3],[0,4]]];
 for(const edges of shapes)for(let rep=0;rep<12;rep++){
  const n=edges.length+1,adj=Array.from({length:n},()=>[]);
  edges.forEach(([u,v],e)=>{adj[u].push([v,e]);adj[v].push([u,e])});
  const leaves=adj.map((a,i)=>a.length===1?i:-1).filter(i=>i>=0),k=leaves.length,N=1<<k,deg=Math.max(...adj.map(a=>a.length));
  const ds=edges.map(()=>BigInt(rep%2?4096:[128,512,2048][rnd()%3]));
  const w=adj.map(a=>Array.from({length:1<<a.length},()=>BigInt(1+rnd()%7)));
  function calc(mask,cut=-1,spin=false){
   function dfs(v,p){
    const j=adj[v].findIndex(([u])=>u===p),ch=adj[v].map(([u,e],i)=>({u,e,i})).filter(a=>a.u!==p).map(a=>({...a,m:dfs(a.u,v)}));
    let result=[0n,0n];
    for(let x=0;x<w[v].length;x++){
     const leaf=leaves.indexOf(v);
     if(leaf>=0&&x!==((mask>>leaf)&1))continue;
     let a=spin?(leaf>=0?1n:BigInt(pop(x)%2===0)):w[v][x];
     for(const {e,i,m} of ch){let bit=(x>>i)&1; a*=spin?(m[0]*(ds[e]+(bit?-1n:1n))+m[1]*(ds[e]+(bit?1n:-1n))):(m[0]*ds[e]+m[1]*(ds[e]-BigInt(e!==cut&&bit===1)))}
     result[j<0?0:(x>>j)&1]+=a;
    }return result;
   }return dfs(0,-1)[0];
  }
  function brute(mask){
   let z=0n;
   for(let x=0;x<1<<(2*edges.length);x++){
    let a=1n;
    for(let v=0;v<n;v++){
     let s=0;adj[v].forEach(([u,e],i)=>{s|=((x>>(2*e+(edges[e][1]===v?1:0)))&1)<<i});
     let l=leaves.indexOf(v);if(l>=0&&s!==((mask>>l)&1)){a=0n;break}a*=w[v][s];
    }
    if(a){for(let e=0;e<edges.length;e++)a*=ds[e]-BigInt(((x>>(2*e))&3)===3);z+=a}
   }return z;
  }
  function minimal(S){return edges.map((_,e)=>{let seen=new Set();function visit(v){if(seen.has(v))return;seen.add(v);for(const [u,j] of adj[v])if(j!==e)visit(u)}visit(edges[e][0]);let a=0,b=0;leaves.forEach((v,i)=>{if(S&(1<<i)){if(seen.has(v))a++;else b++}});return a&&b?e:-1}).filter(e=>e>=0)}
  function interaction(Z,S){let R=one;for(let U=S;;U=(U-1)&S){R=(pop(S)-pop(U))%2?div(R,f(Z[U])):mul(R,f(Z[U]));if(!U)break}return R}
  const Z=Array.from({length:N},(_,x)=>calc(x));
  for(let x=0;x<N;x++)ck(Z[x]===brute(x),"brute");
  const interactions=[];
  for(let S=1;S<N;S++)if(pop(S)>=2){
   const T=minimal(S),R=interaction(Z,S);let B=f(2n**BigInt(pop(S)-1),3n);
   for(const e of T)B=mul(B,f(BigInt(8*Math.max(...edges[e].map(v=>adj[v].length))),ds[e]));
   if(le(B,f(1n,2n)))ck(le(sub(one,B),R)&&le(R,div(one,sub(one,B))),"steiner");
   for(const e of T){let C=Array.from({length:N},(_,x)=>calc(x,e));ck(eq(interaction(C,S),one),"cutCancellation")}
   interactions.push({S,R,m:T.length});
  }
  if(rep%2){
   const theta=f(BigInt(8*deg),4096n),q=mul(f(BigInt(2*deg*deg)),theta);
   for(let L=1;L<=edges.length;L++){
    let B=f(BigInt(n),3n);for(let i=0;i<=L;i++)B=mul(B,q);B=div(B,sub(one,q));
    if(!le(B,f(1n,2n)))continue;
    for(let x=0;x<N;x++){
     let ratio=one;for(const a of interactions)if(a.m>L&&(a.S&x)===a.S)ratio=mul(ratio,a.R);
     ck(le(sub(one,B),ratio)&&le(ratio,div(one,sub(one,B))),"truncation");
    }
   }
  }
  const base=adj.reduce((a,b)=>a*(b.length===1?1n:2n**BigInt(b.length-1)),1n),P=ds.reduce((a,b)=>a*b,1n);
  for(let x=0;x<N;x++)ck(calc(x,-1,true)===base*(P+((pop(x)%2)?-1n:1n)),"parity");
  stats.cases++;
 }
 return stats;
}
console.log(JSON.stringify(verify(),null,2));
```

Next: combine sparse Steiner interaction factors with R815 weighted dependency expansion in an exterior network; investigate a zero-free condition for the resulting overlapping higher-order factors without assuming the total number of interfaces is bounded. Also examine physical realizability of the parity group and degree-dependent sharper radii. General full Port FPTAS remains open.
