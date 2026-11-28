# R863 candidate - Exact suffix-local character bridges and minimum compatible rank
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Continuation: R862 at 692636058c1fd95e918c384e9324f91df8bf94ce:research_notes/portable_direct/R862_COMPACT_SINGLE_INSTANCE_CHARACTER_RANK.md, next problem in section 4. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION read, generated EM_FOUNDATION_STARTUP.json returned 404; no repin. Global canonical entry snapshot c27e45d48d73a3717a24dc43ebd842724b85b8da; P000 V4 and ACTIVE worldview read. Own activity RA-708BCC309CE076D8BB599B91, researcher EM-DIRECT-82A007: own session recovery read succeeded, execution_authorized=false. Original R862 owner query SUCCEEDED, empty RUNNING filter as of 2026-11-28T07:19:16.445305Z, not an atomic current-head assertion. New owner request r3-20261128-r863-running-read last observed RUNNING / NATIVE_RUNNER. No shared claim or Result/review mutation. Scope: auxiliary independent integer option model; no native BRC/Port execution or correspondence asserted.

## 1. Affine suffix space and exact transition
Let p be prime, r>=1, E_i nonempty finite indexed integer-vector option lists (i=0,...,n-1); duplicates are retained as different choices. Let S_i be the set of full integer suffix sums, t_i=sum_{k>=i} b_k for any chosen b_k in E_k, and V_i=span over F_p of all z-b_k with k>=i, z in E_k, reduced mod p. V_n=0 and t_n=0. Then V_i is exactly the span of differences of S_i mod p: one may change one option while holding all other choices at their chosen baselines. V_{i+1} is a subspace of V_i. Define centered feature chi_i(F)=A_i(F-t_i) mod p.

For consecutive stages, the following are equivalent: (a) A_i restricted to V_{i+1} factors through A_{i+1}; (b) ker(A_{i+1}|V_{i+1}) is contained in ker(A_i|V_{i+1}); (c) the restricted row space of A_i is contained in the restricted row space of A_{i+1}. Proof: a linear map on the image of A_{i+1} is well-defined precisely under kernel inclusion, and extends to the ambient feature space; transposition gives row inclusion. A matrix M_i can be obtained by finite-field elimination, so A_i x=M_i A_{i+1}x on V_{i+1}. Thus for every actual suffix F in S_{i+1} and every indexed option z in E_i:
chi_i(z+F)=A_i(z-b_i)+M_i chi_{i+1}(F) mod p.
This is an exact affine descent certificate, not a numerical approximation. If uncentered coordinates are used, add the constant (A_i-M_i A_{i+1})t_{i+1}. It is necessary and sufficient for linear decoding on the entire affine hull; on the actual finite set alone a nonlinear decoder can be possible even if it fails. Example p=3, S={(0,0),(1,1),(2,1)}, A_child=(1,0), A_parent=(0,1). Child labels identify all three points, but the two independent differences span F_3^2 and the parent is not linear in child. Hence no claim of necessity for arbitrary nonlinear encodings.

## 2. Minimal compatible adaptive schedule
At each suffix i, prescribe a demand space D_i contained in V_i^* (e.g. the row restrictions of features obtained from R861's residual refinement). For any linear schedule, its actual restricted row space U_i must contain D_i and satisfy res_{V_{i+1}} U_i subset U_{i+1} to enable the above backward table recursion. Define W_0=D_0, W_{i+1}=D_{i+1}+res_{V_{i+1}} W_i. Equivalently W_i=sum_{k<=i} res_{V_i} D_k. Every compatible U_i contains W_i by induction, and W itself is compatible. Therefore s_i=dim W_i is the pointwise minimum rank among schedules supporting the declared demands and linear bridges on each affine hull. Compute V backwards from local differences, then W forwards by basis restriction; choose ambient row representatives A_i, and solve for M_i. No enumeration of S_i is needed for construction. Rank minimization for discovering D_i itself is a different question.

For each fixed integer support direction a, let B_i(v,a)=max over F in S_i with chi_i(F)=v of a dot F; absent class has -infinity. Terminal B_n(0,a)=0. Compute by taking the maximum of a dot z+B_{i+1}(u,a) over z in E_i and reachable u for which A_i(z-b_i)+M_i u=v. Induction on suffix length proves exactness because each child class maps to one parent class for each local option and every word has precisely such a decomposition. Store a maximizing indexed option and child class per direction to recover an original word; no cross-direction witness recombination. For the original demanded feature (as distinct from W_i), push forward using the row inclusion D_i subset W_i and the exact affine offset. Taking maxima over its fibers reproduces exactly its original conditional support values; all previous sound R859-R860 budget cuts remain sound under that readout. With finite declared direction library N common across stages, support values and optional pointers require O(|N| sum_i p^{s_i}) entries. Candidate transitions are <= |N| sum_{i=0}^{n-1} |E_i| p^{s_{i+1}}; each includes finite-field matrix operations and exact integer additions/comparisons. The bridge construction uses polynomially many Gaussian elimination operations in r,n,total explicit options and demanded rows; modulo p arithmetic has bit cost polynomial in log p. Integer support bit lengths are bounded by input magnitude bit lengths plus log(nr). Dot products can be precomputed. These counts are for support preprocessing, not a bound for the entire budget optimization state table. Witness recovery takes n local choices, plus verification of the original sums.

## 3. Exponential separation for exact demanded readouts
For any prime p and d>=1 let n=r=d, E_i={a e_i: a=0,...,p-1}, D_i=span of the i-th coordinate functional restricted to V_i=span(e_i,...,e_{d-1}); D_d=0. Here indices start at zero. Restricting the preceding coordinate to the next suffix kills it; hence W_i=D_i has rank 1 for every nonterminal i. Each local table has exactly p reachable classes, terminal has one. All bridges between nonterminal stages are zero matrices. Across all d stages the table has dp+1 classes (per direction).

Conversely a single fixed matrix A that can recover each demanded i-th feature linearly on its corresponding affine suffix must have a row combination f_i whose i-th entry is 1 and whose entries j>i are 0. The d rows f_i form a lower triangular matrix with diagonal one, hence rank(A)>=d. At the first suffix S_0 mod p=F_p^d, so the fixed table contains exactly p^d reachable classes. This also holds if the fixed-map readout decoder is arbitrary: on each suffix the reachable centered set is the whole V_i, so fiber constancy enforces the same kernel inclusion. The separation is therefore between fixed exact multi-stage readouts and compatible adaptive exact readouts. It is not a hardness claim for budget feasibility or for arbitrary compressed support formulas. For fixed p, the construction has dp options (O(d^2p) dense scalar entries). Adaptive support preprocessing uses at most dp^2 transitions per direction, before the stated polynomial coordinate overhead; no claim of p^d actual enumeration in the large case.

## 4. Baseline-aware safe budget propagation before building features
For full word budget h, let G_i be current retained indexed options, m_{ij}=min_{z in G_i} z_j and L_j=sum_i m_{ij}. Delete option z in group i if z_j+L_j-m_{ij}>h_j for some j. Every full word containing z violates that coordinate under the current retained lists. Inductively every originally feasible word survives each deletion round. The minima can be taken at different words because only a lower bound is used; no false joint witness is constructed. Empty group or L_j>h_j proves infeasibility; otherwise iterate until no deletion. There are at most N=sum_i |E_i| deletion rounds plus a final check, with O(rN) operations per round (naive bound). Recompute suffix spaces on the filtered lists only for this declared fixed budget and preserved original order. This can eliminate previously necessary residue directions, and R862 collapses to infeasibility before constructing a character table. Keep original options and deletion certificate if future budgets, operations, or identities outside that horizon are requested. No claim of general feasibility completeness for this propagation.

## 5. Evidence and remaining question
Exact bounded author computation below compares adaptive support tables with complete suffix enumeration, checks every actual bridge on the small domains, tests baseline-aware propagation by matching feasible sum multisets (since filtering only removes words this preserves their multiplicities), and tests the rank-one chain with p=2,3,5. Arithmetic fits JS safe integer range. Coefficient recovery in this bounded test is an exhaustive reference search, whereas the analytic construction uses finite-field elimination. Analytic proofs above cover arbitrary finite parameters; no independent review, novelty search, native realization or formal admission. Next: replace affine-hull compatibility by exact reachable-fiber compatibility with certified low-cost non-linear bridge repair; quantify when the resulting rank savings offset the cost of building the bridge. Connect it to actual R859/R860 conditional support and cost-state pruning rather than only preprocessing counts.

## Executed reproducible verification
```javascript
function verify(){
 const out={instances:0,suffix_words:0,support_classes:0,bridge_checks:0,filter_word_checks:0,filter_instances:0,chain_instances:0,max_local_rank:0};
 const ck=x=>{if(!x)throw Error("assertion")};
 let seed=8632026;const rand=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n};
 const mod=(x,p)=>((x%p)+p)%p,dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),sub=(a,b)=>a.map((x,i)=>x-b[i]),add=(a,b)=>a.map((x,i)=>x+b[i]),key=a=>a.join(","),map=(A,x,p)=>A.map(a=>mod(dot(a,x),p));
 const digits=(k,p,n)=>Array.from({length:n},()=>{let a=k%p;k=Math.floor(k/p);return a});
 function basis(rows,p){
   const B=[],piv=[];
   for(const row of rows){const v=row.map(x=>mod(x,p));
     for(let j=0;j<B.length;j++){const c=v[piv[j]];for(let k=0;k<v.length;k++)v[k]=mod(v[k]-c*B[j][k],p)}
     const t=v.findIndex(x=>x!==0);if(t<0)continue;let inv=1;while(mod(inv*v[t],p)!==1)inv++;
     B.push(v.map(x=>mod(x*inv,p)));piv.push(t);
   }return B;
 }
 function choose(rows,V,p){
   const W=[],R=[];let k=0;
   for(const a of rows){const x=V.map(v=>mod(dot(a,v),p));const k1=basis([...R,x],p).length;if(k1>k){R.push(x);W.push(a);k=k1}}
   return W;
 }
 function coeff(target,rows,p){
   // Small-domain independent reference search, not the claimed general Gaussian solver.
   for(let j=0;j<p**rows.length;j++){const x=digits(j,p,rows.length);if(target.every((v,k)=>mod(rows.reduce((s,a,l)=>s+x[l]*a[k],0)-v,p)===0))return x}
   throw Error("missing affine bridge");
 }
 function words(E,r){let L=[Array(r).fill(0)];for(const G of E)L=L.flatMap(x=>G.map(z=>add(x,z)));return L}
 function run(E,D,p,N,r,chain=false){
   const n=E.length,V=Array(n+1),A=Array(n+1),base=Array(n+1);
   V[n]=[];base[n]=Array(r).fill(0);
   for(let i=n-1;i>=0;i--){V[i]=basis([...V[i+1],...E[i].map(z=>sub(z,E[i][0]))],p);base[i]=add(base[i+1],E[i][0])}
   for(let i=0;i<=n;i++)A[i]=choose([...(i?A[i-1]:[]),...(D[i]||[])],V[i],p);
   if(chain)ck(A.slice(0,n).every(a=>a.length===1));
   out.max_local_rank=Math.max(out.max_local_rank,...A.map(a=>a.length));
   let T=new Map([["",N.map(()=>0)]]);
   for(let i=n-1;i>=0;i--){
     const rows=A[i+1].map(a=>V[i+1].map(v=>mod(dot(a,v),p)));
     const M=A[i].map(a=>coeff(V[i+1].map(v=>mod(dot(a,v),p)),rows,p));
     const next=new Map();
     for(const [k,val] of T){const x=k===""?[]:k.split(",").map(Number);for(const z of E[i]){
       const b=map(A[i],sub(z,E[i][0]),p),y=map(M,x,p),v=key(add(b,y).map(t=>mod(t,p)));
       const s=N.map((a,j)=>dot(a,z)+val[j]);const prev=next.get(v);
       next.set(v,prev?prev.map((a,j)=>Math.max(a,s[j])):s);
     }}
     T=next;const direct=new Map();
     for(const f of words(E.slice(i),r)){
       const k=key(map(A[i],sub(f,base[i]),p)),s=N.map(a=>dot(a,f)),old=direct.get(k);
       direct.set(k,old?old.map((a,j)=>Math.max(a,s[j])):s);out.suffix_words++;
     }
     for(const f of words(E.slice(i+1),r)){
       ck(key(map(A[i],sub(f,base[i+1]),p))===key(map(M,map(A[i+1],sub(f,base[i+1]),p),p)));out.bridge_checks++;
     }
     ck(T.size===direct.size);for(const [k,v] of direct){ck(key(T.get(k))===key(v));out.support_classes++}
     if(chain)ck(T.size===p);
   }out.instances++;
 }
 function filtered(E,h,r){
   let G=E.map(g=>g.slice());
   for(;;){
     if(G.some(g=>!g.length))return null;
     const mins=G.map(g=>Array.from({length:r},(_,j)=>Math.min(...g.map(z=>z[j])))),total=mins.reduce(add,Array(r).fill(0));
     if(total.some((v,j)=>v>h[j]))return null;
     const next=G.map((g,i)=>g.filter(z=>z.every((v,j)=>v+total[j]-mins[i][j]<=h[j])));
     if(next.every((g,i)=>g.length===G[i].length))return next;
     G=next;
   }
 }
 function feasibleWords(E,h,r){return words(E,r).filter(f=>f.every((x,j)=>x<=h[j])).map(key).sort()}
 for(let t=0;t<240;t++){
   const p=[2,3,5][t%3],r=1+rand(4),n=1+rand(5);
   const E=Array.from({length:n},()=>Array.from({length:1+rand(3)},()=>Array.from({length:r},()=>rand(10))));
   const D=Array.from({length:n+1},(_,i)=>i===n?[]:Array.from({length:1+rand(2)},()=>Array.from({length:r},()=>rand(p))));
   const N=Array.from({length:3},()=>Array.from({length:r},()=>rand(7)-3));
   run(E,D,p,N,r);
   const h=Array.from({length:r},()=>rand(25)),G=filtered(E,h,r);
   ck(key(feasibleWords(E,h,r))===key(G?feasibleWords(G,h,r):[]));out.filter_word_checks+=words(E,r).length;out.filter_instances++;
 }
 for(const p of [2,3,5])for(let d=1;d<=(p===2?9:p===3?5:4);d++){
   const eye=j=>Array.from({length:d},(_,k)=>+(k===j));
   const E=Array.from({length:d},(_,i)=>Array.from({length:p},(_,a)=>eye(i).map(x=>x*a)));
   const D=Array.from({length:d},(_,i)=>[eye(i)]).concat([[]]);
   run(E,D,p,[Array(d).fill(1),Array.from({length:d},(_,j)=>j-2)],d,true);out.chain_instances++;
 }
 return out;
}
console.log(JSON.stringify(verify()));
```
Executed result:
```json
{
  "instances": 258,
  "suffix_words": 8250,
  "support_classes": 2055,
  "bridge_checks": 3707,
  "filter_word_checks": 2636,
  "filter_instances": 240,
  "chain_instances": 18,
  "max_local_rank": 4
}
```
All assertions passed.
