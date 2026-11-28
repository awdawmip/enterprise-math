# R870 — Bounded-separation defect polymers: exact counting and cost optimization
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED. Independent informed portable auxiliary integer work; no native BRC attribution or shared CLAIM. Predecessor R869 at c67a66e95828f8586e3242ebe6d88730cdaef508:research_notes/portable_direct/R869_REFERENCE_LIFT_CUT_QUOTIENT.md. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 and joint observer read, generated foundation startup and separate residual companion unavailable (404), no repin. Global canonical e9802bdfc9d93e42d58cba3287a936c8c3b81cb6 entries and active worldview read. Existing own RA-708BCC309CE076D8BB599B91 session recovery verified, no execution authority. Previous R869 RUNNING read succeeded, empty as of 2026-11-28T14:36:17.631762Z; current r3-20261128-r870-running-read RUNNING / NATIVE_RUNNER at last observation.

## 1. A structural parameter beyond feedback edges or treewidth
Same R869 loopless indexed multigraph, explicit finite distinct integer domains and additive integer costs. In this unit G is connected bipartite; take a feasible reference X with slack k0<=K, B=K+k0<=2K, obtainable by R868 FPT decision/witness. Choose a sign on each side and set y_v=s_v(x_v-X_v). Orient each edge from positive to negative side. Then eps_e(x)=eps_e(X)+y_u-y_v. Gauge domains contain 0 and costs transform bijectively. Every feasible x has TV(y)=sum_e |y_u-y_v|<=B; every individual difference along a path is bounded by B. Actual budget remains sum_e |eps_e(X)+y_u-y_v|<=K.

Assume the (q,B)-unbreakability promise: every edge cut of size <=B has a side with at most q vertices. q>=0 integer; capacity counts indexed parallel edges. This is a promised structural class, not a claim that arbitrary graph can be recognized or decomposed into it in FPT time here. Goal exact slack histogram, arbitrary unary cost minimum and one inverse witness, in f(K,q)*poly(input) time. For q bounded by a function of K this is K-only FPT on this class. No bounded degree or treewidth assumption.

If n<=(B+1)q, enumerate any root value from its explicit domain, then all other values within B of the root (<=2B+1 choices each); verify original budget and costs. Complexity Dmax*(2B+1)^((B+1)q) times polynomial. Otherwise remove all edges where y differs: at most B edges, hence <=B+1 connected components. A component of size>q exists. Its edge boundary <=B, so its complement has <=q vertices. For B>=1, n>2q, so its value r is unique majority. For B=0 all labels are constant by connectedness. Thus every feasible assignment has a uniquely determined background r (in union of gauge domains) and a defect set of size <=q; each connected defect component is a proper connected set A, |A|<=q, |delta(A)|<=B. Conversely we may count assignments with unique background and TV<=B and exact budget, regardless of number of defects: their background is unique when the nonbackground set has <=q. To ensure uniqueness even for enumerated candidates before feasibility filtering, note that any reconstructed assignment with TV<=B and feasible budget has a majority component; if chosen background r is not the majority, then there is a defect component containing that majority component, of size>q, contradiction. This holds also B=0. Hence no additional global cardinality filter needed.

## 2. Bounded-degree defect interaction graph even for unbounded-degree G
For each background r, enumerate every connected proper A with size<=q and boundary<=B. For each root in A, branch on one deterministic frontier neighbor: include it permanently (charges one of q vertices) or exclude it permanently (charges at least one edge between included and excluded; excluded vertices distinct, total at most B). Reject oversized states; at a terminal all neighbors decided, retain A, dedup sorted vertex IDs. Every target A containing the root has exactly one branch path, at most q+B decisions before pruning. At most 2^(q+B+1) leaves per root, and polynomial scanning cost per node. For each A enumerate all domain labels other than r within [r-B,r+B], at most (2B)^q assignments; keep original IDs. A labelled component P has variation v(P)>0 (nonempty proper set, connected G), exact slack increment d(P)=sum_{incident e}(|eps0_e+y_u-y_v|-|eps0_e|) where outside label=r, and arbitrary unary cost increment c(P). Keep v<=B, |d|<=v. Let H={u:r not in domain_u}. If |H|>q reject background; otherwise set default cost 0 on H and use h(P)=|A intersect H|. Distinct P,Q conflict iff sets intersect or are adjacent in G. Nonconflicting components have disjoint incident edge sets (no cross edge); all three increments add, including negative d. All H covered iff sum h=|H|, since sets disjoint. Thus original feasible assignments correspond bijectively to independent sets I of candidates with sum v<=B, 0<=k0+sum d<=K and sum h=|H|. Proof of uniqueness across backgrounds above. Inverse stores original labels and graph edges, hence signed residuals, cost, count and identity recover exactly for fixed K, domains and targets. Not a new native observer equivalence.

Each graph vertex occurs in at most A0=2^(q+B+1)*max(1,2B)^q distinct candidates. A candidate has <=q+B vertices in its closed neighborhood (external neighbor count <= boundary). Its conflict degree <= (q+B)A0; despite original unbounded degree, N<=n*A0 and conflict graph construction polynomial times parameter function. Every independent set of interest uses <=B candidates.

## 3. Exact counting via connected-support logarithm
Let Z(t,x,u)=sum_{independent I} t^(sum v) x^(sum d) u^(sum h) modulo t^(B+1). Laurent x permits negative slack changes. Coefficients at x^(k-k0)u^|H|, summed t degrees, count exact slack k. Work over rational formal truncated series. For subset S of candidate vertices define L_S=sum_{T subset S} (-1)^(|S|-|T|) log Z_{G[T]}. By Mobius inversion log Z_G=sum_S L_S. Expand log(1+W)=sum_{j=1}^B (-1)^(j+1)W^j/j. Every monomial term in this expansion has a support of used candidate IDs, and its inclusion-exclusion contribution to L_S vanishes unless support=S. Hence L_S has no t-degree <=B when |S|>B. If S disconnected, log factors add across its connected components; the unused-component alternating sums cancel, so L_S=0. Enumerate only connected subsets |S|<=B, growing along candidate graph adjacency and deduplicating; at most N*(B*max(1,Delta))^(B-1) times a factor B (safe bound; B=0 use Z=1), Delta bounded above. For each subset, enumerate all T and all their independent sets (2^B), compute truncated log, sum. Recover Z by exp or t-derivative recurrence. The coefficient space uses t degree <=B, signed x exponent in [-B,B], u exponent <=Bq (including intermediate products); f(B,q) coefficients. Exact rational computations can use B! scaling of logs; exp recurrence divides by B!*v and yields exact integers. Bit lengths polynomial in input and parameter (coefficients involve at most B labels from N and bounded factorial). No enumeration of global independent sets. This connected-support logarithm is a standard formal combinatorial technique; contribution is the bounded-degree defect reduction and joint residual bookkeeping in this relation model.

## 4. Cost optimization by a bounded candidate kernel
For each type (v,d,h), retain L0=(B-1)(Delta+1)+1 cheapest candidates (at least 1 for B=0), with a deterministic tie order; if fewer retain all. Any optimum independent set using an omitted candidate has at most B-1 other candidates, which collectively forbid at most (B-1)(Delta+1) candidates (including themselves). One retained candidate of same type is available, not more expensive, and preserves all three sums. Replacing one omitted candidate strictly reduces number omitted, preserving feasibility and not increasing cost. Therefore an optimum lies in the bounded kernel; enumerate its independent subsets of size <=B and exact budget/coverage. Number types bounded by B*(2B+1)*(q+1), kernel size depends only on B,q. Count still uses ALL candidates, never the cost kernel. Return optimum and decode witness. Complexity of whole algorithm f(K,q)*poly(explicit input), including reference witness via R868, domain translation, enumeration of backgrounds, exact bit arithmetic and reconstruction. General nonbipartite graphs and arbitrary unbreakable decomposition not established here. The theorem is conditional on the supplied structural promise; testing it for arbitrary inputs is not included.

## 5. Evidence and limits
Implemented in JavaScript, exact BigInt coefficients and safe integer small labels/costs. Test verifies small-case unbreakability by exhaustive cuts and compares full original gauge assignments and optimum; large star checked against analytic formula 2 binom(100,k), min -4 (all ones cost -1 then flip 3 odd leaves to zero). Large star is a stress case for unbounded degree and combinatorial count, not evidence of improvement over R869 forest solver on trees. First test run exposed mutable label-array aliasing in candidate witness; copied values before final full rerun. The analytic large optimum was also corrected before rerun. Final output:
```json
{
  "instances": 104,
  "brute_assignments": 26588,
  "polymer_runs": 77,
  "small_runs": 28,
  "candidates": 765,
  "connected_supports": 836,
  "kernel_candidates": 222,
  "large": {
    "vertices": 101,
    "K": 3,
    "hist": [
      "2",
      "200",
      "9900",
      "323400"
    ],
    "best": -4
  },
  "failures": 0
}
```
```javascript
function verify870(){
 const ck=(a,m)=>{if(!a)throw Error(m)}, abs=Math.abs;
 const out={instances:0,brute_assignments:0,polymer_runs:0,small_runs:0,candidates:0,connected_supports:0,kernel_candidates:0,large:null,failures:0};
 function solve(D,C,E,K,q){
  const n=D.length,k0=E.reduce((a,e)=>a+abs(e[2]),0),B=K+k0;
  ck(k0<=K&&D.every(d=>d.includes(0)),"reference");
  const adj=Array.from({length:n},()=>new Set());for(const [u,v] of E){adj[u].add(v);adj[v].add(u)}
  const hist=Array(K+1).fill(0n);let best=Infinity,witness=null;
  function record(y){let k=E.reduce((a,[u,v,c])=>a+abs(c+y[u]-y[v]),0);if(k>K)return;hist[k]++;let v=y.reduce((a,x,i)=>a+C[i].get(x),0);if(v<best){best=v;witness=y.slice()}}
  function product(dom,cb,cur=[]){if(cur.length===dom.length){cb(cur);return}for(const x of dom[cur.length]){cur.push(x);product(dom,cb,cur);cur.pop()}}
  if(n<=(B+1)*q){out.small_runs++;for(const r of D[0])product(D.map((d,i)=>i?d.filter(x=>abs(x-r)<=B):[r]),record);return {hist,best,witness}}
  out.polymer_runs++;
  const sets=new Map();
  for(let root=0;root<n;root++){
   function go(A,F){let bd=0;for(const [u,v] of E)if(A.has(u)&&F.has(v)||A.has(v)&&F.has(u))bd++;if(bd>B||A.size>q)return;
    let x=-1;for(const u of A){for(const v of adj[u])if(!A.has(v)&&!F.has(v)){x=v;break}if(x>=0)break}
    if(x<0){let a=[...A].sort((x,y)=>x-y);sets.set(a.join(","),a);return}
    if(A.size<q){A.add(x);go(A,F);A.delete(x)}F.add(x);go(A,F);F.delete(x);
   }if(q>0)go(new Set([root]),new Set());
  }
  for(const r of [...new Set(D.flat())]){
   const bad=D.map(d=>!d.includes(r)),nb=bad.filter(Boolean).length;if(nb>q)continue;
   const base=C.reduce((a,c)=>a+(c.get(r)??0),0),P=[];
   for(const A of sets.values()){let S=new Set(A),near=new Set(A);for(const u of A)for(const v of adj[u])near.add(v);
    product(A.map(u=>D[u].filter(x=>x!==r&&abs(x-r)<=B)),vals=>{
     let y=new Map(A.map((u,i)=>[u,vals[i]])),v=0,d=0;
     for(const [u,w,c] of E)if(S.has(u)||S.has(w)){let t=(y.get(u)??r)-(y.get(w)??r);v+=abs(t);d+=abs(c+t)-abs(c)}
     if(v===0||v>B)return;let cover=A.filter(u=>bad[u]).length,dc=A.reduce((a,u,i)=>a+C[u].get(vals[i])-(C[u].get(r)??0),0);
     P.push({A,S,near,vals:vals.slice(),v,d,cover,dc})
    })
   }
   out.candidates+=P.length;
   const N=P.length,G=Array.from({length:N},()=>new Set()),by=Array.from({length:n},()=>[]);
   P.forEach((p,i)=>p.A.forEach(v=>by[v].push(i)));
   P.forEach((p,i)=>{for(const v of p.near)for(const j of by[v])if(j!==i)G[i].add(j)});
   const key=(v,d,c)=>`${v},${d},${c}`,un=k=>k.split(",").map(Number),zero=key(0,0,0);
   const add=(m,k,a)=>{let b=(m.get(k)??0n)+a;if(b)m.set(k,b);else m.delete(k)};
   const mul=(a,b)=>{let m=new Map();for(const [ka,x] of a)for(const [kb,y] of b){let [v,d,c]=un(ka),[w,e,f]=un(kb);if(v+w<=B)add(m,key(v+w,d+e,c+f),x*y)}return m};
   const one=new Map([[zero,1n]]);let F=1n;for(let j=1;j<=B;j++)F*=BigInt(j);
   function localZ(S){let z=new Map(one);function rec(i,picked,v,d,c){for(let j=i;j<S.length;j++){let a=S[j],p=P[a];if(v+p.v>B||picked.some(b=>G[a].has(b)))continue;add(z,key(v+p.v,d+p.d,c+p.cover),1n);rec(j+1,[...picked,a],v+p.v,d+p.d,c+p.cover)}}rec(0,[],0,0,0);return z}
   function logScaled(S){let z=localZ(S);z.delete(zero);let l=new Map(),pow=new Map(one);for(let j=1;j<=B;j++){pow=mul(pow,z);if(!pow.size)break;let t=(j%2?1n:-1n)*F/BigInt(j);for(const [k,a] of pow)add(l,k,t*a)}return l}
   let seen=new Set(),L=new Map();
   function conn(S){let k=[...S].sort((a,b)=>a-b).join(",");if(seen.has(k))return;seen.add(k);out.connected_supports++;
    let a=[...S];function sub(i,T){if(i===a.length){if(!T.length)return;let sign=(a.length-T.length)%2?-1n:1n;for(const [k,x] of logScaled(T))add(L,k,sign*x);return}sub(i+1,T);sub(i+1,[...T,a[i]])}sub(0,[]);
    if(S.size<B){let nb=new Set();for(const u of S)for(const v of G[u])if(!S.has(v))nb.add(v);for(const v of nb)conn(new Set([...S,v]))}
   }
   if(B>0)for(let i=0;i<N;i++)conn(new Set([i]));
   let Z=new Map(one);for(let v=1;v<=B;v++){let row=new Map();for(const [k,a] of L){let [j,d,c]=un(k);if(j>v)continue;for(const [h,b] of Z){let [w,e,f]=un(h);if(j+w===v)add(row,key(v,d+e,c+f),BigInt(j)*a*b)}}for(const [k,a] of row){ck(a%(F*BigInt(v))===0n,"integer exp");let b=a/(F*BigInt(v));ck(b>=0n,"negative count");if(b)Z.set(k,b)}}
   for(const [k,c] of Z){let [v,d,h]=un(k);if(h===nb&&k0+d>=0&&k0+d<=K)hist[k0+d]+=c}
   let deg=G.reduce((a,s)=>Math.max(a,s.size),0),L0=Math.max(1,(B-1)*(deg+1)+1),types=new Map();
   P.forEach((p,i)=>{let t=key(p.v,p.d,p.cover);if(!types.has(t))types.set(t,[]);types.get(t).push(i)});
   let U=[...types.values()].flatMap(a=>a.sort((i,j)=>P[i].dc-P[j].dc||i-j).slice(0,L0)).sort((a,b)=>a-b);out.kernel_candidates+=U.length;
   function opt(i,S,v,d,c,cost){if(c===nb&&k0+d>=0&&k0+d<=K&&base+cost<best){best=base+cost;witness=Array(n).fill(r);for(const a of S)P[a].A.forEach((u,j)=>witness[u]=P[a].vals[j])}
    for(let j=i;j<U.length;j++){let a=U[j],p=P[a];if(v+p.v>B||c+p.cover>nb||S.some(b=>G[a].has(b)))continue;opt(j+1,[...S,a],v+p.v,d+p.d,c+p.cover,cost+p.dc)}
   }opt(0,[],0,0,0,0)
  }
  if(witness){ck(witness.every((x,i)=>D[i].includes(x)),"witness domain");ck(E.reduce((a,[u,v,c])=>a+abs(c+witness[u]-witness[v]),0)<=K,"witness slack");ck(witness.reduce((a,x,i)=>a+C[i].get(x),0)===best,"witness cost")}
  return {hist,best,witness}
 }
 let seed=8702026;function rand(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n}
 function test(D,C,E,K,q){let n=D.length,B=K+E.reduce((a,e)=>a+abs(e[2]),0);
  for(let mask=1;mask<(1<<n)-1;mask++){let s=0;for(let i=0;i<n;i++)s+=(mask>>i)&1;if(Math.min(s,n-s)<=q)continue;ck(E.filter(([u,v])=>((mask>>u)^(mask>>v))&1).length>B,"promise")}
  let expected=Array(K+1).fill(0n),best=Infinity;
  function brute(y){if(y.length===n){out.brute_assignments++;let k=E.reduce((a,[u,v,c])=>a+abs(c+y[u]-y[v]),0);if(k<=K){expected[k]++;best=Math.min(best,y.reduce((a,x,i)=>a+C[i].get(x),0))}return}for(const x of D[y.length])brute([...y,x])}brute([]);
  let z=solve(D,C,E,K,q);ck(z.best===best&&z.hist.every((a,i)=>a===expected[i]),"brute mismatch");out.instances++;
 }
 for(let i=0;i<80;i++){let n=5+rand(4),K=1+rand(2),E=Array.from({length:n-1},(_,j)=>[0,j+1,0]);if(i%4===0)E[0][2]=1;let B=K+E.reduce((a,e)=>a+abs(e[2]),0),D=Array.from({length:n},()=>[...new Set([0,rand(3)-1,rand(3)-1])]),C=D.map(d=>new Map(d.map(x=>[x,rand(13)-6])));test(D,C,E,K,B)}
 for(let i=0;i<24;i++){let n=8,K=1+rand(2),E=[];for(let u=0;u<4;u++)for(let v=4;v<8;v++)E.push([u,v,0]);let D=Array.from({length:n},()=>[0,1]),C=D.map(d=>new Map(d.map(x=>[x,rand(7)-3])));test(D,C,E,K,0)}
 let n=101,K=3,D=Array.from({length:n},()=>[0,1]),C=D.map((d,i)=>new Map([[0,0],[1,i%2?1:-1]])),E=Array.from({length:n-1},(_,j)=>[0,j+1,0]);let z=solve(D,C,E,K,3),bin=(n,k)=>{let r=1n;for(let i=1;i<=k;i++)r=r*BigInt(n-i+1)/BigInt(i);return r};ck(z.hist.every((a,i)=>a===2n*bin(n-1,i)),"star hist");ck(z.best===-4,"star optimum");out.large={vertices:n,K,hist:z.hist.map(String),best:z.best};return out
}
console.log(verify870());
```

## 6. Next
Find a decomposition that isolates (q(K),B)-unbreakable regions with boundary signatures of size f(K), preserving the exact defect histogram and arbitrary unary costs, or produce a counterexample to such a uniform interface. Consider unbreakable bags with boundary conditioning rather than forest-only quotient. Literature lead (not a dependency or claimed transfer): Berge et al., On the Parameterized Complexity of Counting Small-Sized Minimum (S,T)-Cuts, DOI 10.1137/21M1398203, treats minimum terminal cuts, not this full residual model. Native BRC/Port correspondence remains open.
