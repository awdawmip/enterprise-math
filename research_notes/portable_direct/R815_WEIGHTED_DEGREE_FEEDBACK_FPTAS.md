# R815 — Degree-paid weighted feedback supports without a bounded dependency degree

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, no shared CLAIM/RUN/Result. Researcher EM-DIRECT-82A007 / TASK_RESEARCH, own session metadata recovered, no run and execution_authorized=false. Original RUNNING inventory request r3-20261126-r815-running-read remains RUNNING at derivation; no empty-inventory inference. Predecessor b3fb17526b9c6f0b4aaa0a90de0aae3688a3fb50:research_notes/portable_direct/R814_DEPENDENCY_CONNECTED_FEEDBACK_FPTAS.md (read immutable bytes). Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read. Global entries and applicable rules at 880c2029c26496efa31afc9f828d149970dee1ef. The work concerns only the R813–R814 positive auxiliary combinatorial observer for a fixed feasible charge. Native signed BRC, road matrices, time order, common depth and branch provenance remain retained; no native phase claim.

## 1. Weighted feedback generating coordinates

Use R813 H,D,Z0, pinned forest moment m(A)=Z_A/Z0, and R814's exact dependency graph G_D. Z0=0 gives exact zero, so suppose Z0>0. Write n=|D|, h_v=deg_G_D(v), delta_v in [0,1), and positive integer costs c_v. Define weighted degree c(A)=sum_{v in A}c_v and
 P_S(t)=E0 prod_{v in S}(1-delta_v t^{c_v} I_v).
At t=1 this recovers the exact R813 observer Z=Z0 P_D(1) for any fixed feasible boundary charge. No change in activation weights, joint moments or endpoint relations. The polynomial is an analytic auxiliary coordinate, not a physical time trajectory.

The R814 induction applies with R delta_v replaced throughout by R^{c_v} delta_v. Specifically, if R>1 and 0<q_v<1 satisfy
 delta_v R^{c_v} <= q_v prod_{u~v}(1-q_u)^2,                 (1)
then every P_S is nonzero on |t|<=R, and
 |P_S(t)/P_{S-v}(t)-1| <= q_v.                              (2)
For completeness: connected polymer C has activity (-1)^|C| delta(C) m(C) t^{c(C)}. Deleting a vertex v yields the exact recurrence P_S=P_{S-v}+sum_{C connected,v in C subset S} w(C) P_{S\N[C]}. Inductively divide by P_{S-v}, delete neighbors using 1-q_u lower ratio bounds, and majorize the sum by (1-q_v) times rooted connected-set weight with b_x=R^{c_x}delta_x prod_{u in N[x]}(1-q_u)^(-1). Encode each connected set by a rooted labeled spanning tree; allow repeated labels across different nodes, but distinct children. The nonnegative height recursion T_x=b_x prod_{u~x}(1+T_u) is bounded by L_x=q_x/(1-q_x) because (1) gives b_x prod(1+L_u)<=L_x. Thus the ratio is bounded by (1-q_v)L_v=q_v<1. Zero deltas are allowed by the same argument.

## 2. A tail bound independent of polynomial degree

Order the vertices arbitrarily and telescope P_D into ratios P_{S_i}/P_{S_{i-1}}. Each ratio lies in the closed complex disk |z-1|<=q_i<1. Its analytic log normalized to zero at t=0 has modulus <=-log(1-q_i)<=q_i/(1-q_i) on |t|<=R, by the absolutely convergent log(1+z) series. Sum to obtain |log P_D(t)|<=M=sum q_i/(1-q_i) on the disk. By Cauchy's coefficient estimate, for ell_j=[t^j]log P_D(t),
 |ell_j|<=M R^{-j},
 |log P_D(1)-sum_{j=1}^k ell_j|<=M R^{-k}/(R-1).             (3)
This avoids dependence on sum c_v in the tail (the old root-degree bound remains an alternative). On [0,1] P_D is positive, hence the analytic log at 1 is its real log. For q_v=1/9 and R=5/4, the bound is (n/2)(4/5)^k.

## 3. Weighted connected enumeration and coefficient recovery

Introduce one formal variable per vertex in E0 prod(1-delta_v z_v I_v). The full-support Mobius transform of its log vanishes on disconnected C by moment factorization, and substituting z_v=t^{c_v} shows it has no term of weighted order below c(C). Thus if ell_j(S)=[t^j]log P_S,
 ell_j(D)=sum_{C connected, c(C)<=j} sum_{A subset C}(-1)^{|C|-|A|}ell_j(A).   (4)
Use exact forest oracle calls for m(A), weighted powers c(A), and the recurrence j ell_j=j p_j-sum_{i=1}^{j-1} i ell_i p_{j-i}. There is no factor exponential in the total number of feedback vertices.

Assume h_v<=K c_v for a fixed K. For each root, enumerate connected sets of minimum label root by a deterministic queue of included vertices and their ordered adjacency lists. Each newly encountered neighbor is decided once (include/exclude), all lower labels excluded initially, and inclusion stops if the cumulative cost would exceed k. This generates each connected set exactly once: for any target connected set, every discovered neighbor has a forced decision by membership, and connectivity ensures discovery of every member. Each search path inspects at most sum_{v included} h_v<=K k adjacency entries (including ignored or already decided entries). Hence binary branching nodes are bounded by 2^{Kk+1}, per root, up to polynomial housekeeping. No max-degree assumption. Each set uses <=2^k moment queries and O(3^k poly(k)) rational coefficient operations, by summing over A and sub-A. With a polynomial exact forest oracle, fixed R separated from 1, q_v<=q_*<1 and K fixed, k=O(log((n+1)/epsilon)) yields a deterministic FPTAS, with poly(input,1/epsilon) bit complexity. For rational physical inputs, every forest moment has polynomial bit length; even without a common denominator, only polynomially many rationals are combined through polynomially bounded order, and recurrence and Mobius denominators have polynomial bit length (e.g. formal log via sum_{l<=k}(-1)^{l+1}(P-1)^l/l). Exponentiate the exact truncated rational log with a certified relative epsilon/4 error using positive Taylor series with geometric tail for its absolute argument and reciprocal if negative. The argument is O(n+1) by (3) and the log bound. Choose (3)<=epsilon/4, 0<epsilon<=1. Then relative error <=epsilon. Multiply by Z0 and the original K0 as appropriate. The empty feedback set is exact. Cost bound is theoretical, not a practical optimized runtime exponent.

## 4. Explicit unbounded-degree Port family

Let d_v>=2 be ORIGINAL road degree of each shared factor, delta_v<=2^{-(2d_v+1)}. Suppose h_v<=2d_v. Choose
 c_v=max(1,ceil(h_v/4)), K=4, R=5/4, q_v=1/9.
Then c_v<=ceil(d_v/2) and
 delta_v R^{c_v} <= (5/4)^{ceil(d_v/2)}2^{-(2d_v+1)}
 <= (1/9)(8/9)^{4d_v}
 <= (1/9)(8/9)^{2h_v}.                                   (5)
For d=2 the middle inequality is 5/128 <= 8^8/9^9, equivalent to 5*9^9<=128*8^8. Incrementing d multiplies the left by at most 5/16 and the right by (8/9)^4>5/16, proving all d>=2. Shared factors have d>=2 because they meet at least two disjoint edge groups. No bound on maximum h_v, original degree, number of feedback vertices, or total interface count.

A simple sufficient structural test: each connected component of H-D touches at most three distinct feedback factors. Each such component contributes at most two neighbors to any incident v, and the number of incident components is at most the number of distinct groups touching v, at most d_v since edge groups partition the roads. Thus h_v<=2d_v. Components themselves can be arbitrarily large forests with arbitrary internal correlations, and interface width can grow; R813's exact oracle still supplies the moments. This is strictly an extension of the bounded dependency-degree algorithmic certificate, not a claim that all physical networks meet the new condition. In particular the R813 choice D and forest oracle assumptions are retained. A supplied D satisfying the test is verifiable in polynomial time; existence or finding an optimal D is not claimed.

## 5. Limits and explicit large hub example

For an abstract star dependency graph with h leaves, independent pair tables with integer weights [2,5,3,7] indexed by root bit then leaf bit (root is low bit), the root event is the product of its h bits, leaf event its one bit. Set leaf delta=1/32, root delta=2^{-(2max(2,h)+1)}. Direct independence gives exactly
 P(1)=(534/544)^h-delta_root (377/544)^h.
Deleting just the root changes P by relative-to-deleted loss delta_root*(377/534)^h <= delta_root. With weighted budget k<ceil(h/4) the connected support list consists only of the h singleton leaves. This example demonstrates the weighted enumeration mechanism; it is an abstract rational interface case, not asserted to be the precise physical Port matrix family. The general criterion (5) applies to actual Port whenever its stated assumptions hold.

The large-component clique obstruction cannot be ignored for arbitrary base oracles: take all I_v equal to one Bernoulli bit with probabilities 1/2 and common delta=1/32. Then P(t)=[1+(1-delta*t)^n]/2. A zero has t=(1-exp(i*pi/n))/delta, modulus <=pi/(n delta), <1 at n=256. Thus a uniform local bound on delta alone cannot give an R>1 zero-free theorem for arbitrary joint oracle tables, even when a common bit has a compact equality-chain representation. This is an auxiliary abstract counterexample, not a physical Port counterexample; actual weak local coupling may prevent such long-range correlation. Next problem: exploit R813 forest's exact conditional separator transfer and original Port soft factors to replace the large-component clique by finer weighted connected supports, or prove a physical obstruction. General complete Port FPTAS remains open.

## 6. Actual exact verification

The following deterministic JavaScript BigInt rational program was executed in the current turn. It verifies the certificate on six dependency-group patterns, moment factorization, weighted-degree and disconnected support cancellation, connected enumeration against all subsets, coefficient reconstruction, and real endpoint ratios at t=+/-5/4. Large star checks use exact formula and compare small cases with direct subset enumeration; large cases verify the deletion bound and support counts. Analytic proof, not these endpoint checks, establishes complex nonvanishing. No independent review or native BRC computation; no large production FPTAS benchmark.

```json
{
  "stats": {
    "cases": 30,
    "certificate": 185,
    "momentFactor": 2400,
    "weightedSupportCancellation": 12265,
    "enumeration": 280,
    "coefficientReconstruction": 1525,
    "realRatio": 15520,
    "starFormula": 3,
    "starBound": 7,
    "starEnumeration": 7
  },
  "star": [
    {
      "h": 2,
      "k": 2,
      "rootCost": 1,
      "connectedSupports": 5,
      "numeratorBits": 24,
      "denominatorBits": 24,
      "rootOmissionBoundExponent": 5
    },
    {
      "h": 4,
      "k": 2,
      "rootCost": 1,
      "connectedSupports": 9,
      "numeratorBits": 46,
      "denominatorBits": 46,
      "rootOmissionBoundExponent": 9
    },
    {
      "h": 8,
      "k": 3,
      "rootCost": 2,
      "connectedSupports": 17,
      "numeratorBits": 90,
      "denominatorBits": 90,
      "rootOmissionBoundExponent": 17
    },
    {
      "h": 16,
      "k": 5,
      "rootCost": 4,
      "connectedSupports": 33,
      "numeratorBits": 178,
      "denominatorBits": 179,
      "rootOmissionBoundExponent": 33
    },
    {
      "h": 32,
      "k": 9,
      "rootCost": 8,
      "connectedSupports": 65,
      "numeratorBits": 355,
      "denominatorBits": 356,
      "rootOmissionBoundExponent": 65
    },
    {
      "h": 128,
      "k": 10,
      "rootCost": 32,
      "connectedSupports": 128,
      "numeratorBits": 1417,
      "denominatorBits": 1421,
      "rootOmissionBoundExponent": 257
    },
    {
      "h": 512,
      "k": 10,
      "rootCost": 128,
      "connectedSupports": 512,
      "numeratorBits": 5665,
      "denominatorBits": 5678,
      "rootOmissionBoundExponent": 1025
    }
  ],
  "checks": 32192
}
```

```javascript
function verify(){
 const f=(a,b=1n)=>{if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}let x=a<0n?-a:a,y=b;while(y){let r=x%y;x=y;y=r;}return[a/x,b/x];};
 const zero=()=>f(0n),one=()=>f(1n), add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>f(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],abs=a=>[a[0]<0n?-a[0]:a[0],a[1]];
 const sum=a=>a.reduce((s,x)=>s+x,0n), pop=m=>{let k=0;for(;m;m&=m-1)k++;return k;};
 function subsets(m){let a=[];for(let s=m;;s=(s-1)&m){a.push(s);if(!s)return a;}}
 function logcoef(p,k){let l=Array.from({length:k+1},zero);for(let j=1;j<=k;j++){let z=mul(f(BigInt(j)),p[j]??zero());for(let i=1;i<j;i++)z=sub(z,mul(mul(f(BigInt(i)),l[i]),p[j-i]??zero()));l[j]=div(z,f(BigInt(j)));}return l;}
 function val(p,t){return p.reduceRight((s,x)=>add(x,mul(s,t)),zero());}
 function weightedSets(adj,c,k){let out=[];for(let root=0;root<adj.length;root++){if(c[root]>k)continue;const seen=new Set(Array.from({length:root+1},(_,i)=>i));
  function walk(q,h,i,seen,cost){if(h===q.length){out.push(q.slice().sort((a,b)=>a-b));return;}if(i===adj[q[h]].length){walk(q,h+1,0,seen,cost);return;}const v=adj[q[h]][i];if(seen.has(v)){walk(q,h,i+1,seen,cost);return;}let ns=new Set(seen);ns.add(v);walk(q,h,i+1,ns,cost);if(cost+c[v]<=k)walk(q.concat(v),h,i+1,ns,cost+c[v]);}
  walk([root],0,0,seen,c[root]);}return out;}
 let stats={cases:0,certificate:0,momentFactor:0,weightedSupportCancellation:0,enumeration:0,coefficientReconstruction:0,realRatio:0,starFormula:0,starBound:0,starEnumeration:0};function check(ok,key){if(!ok)throw Error(key);stats[key]++;}
 let seed=815;const rand=()=>seed=(Math.imul(seed,1664525)+1013904223)>>>0;
 const patterns=[[[0,1,2],[2,3,4],[4,5],[5,0]],Array.from({length:6},(_,i)=>[0,i+1]),Array.from({length:6},(_,i)=>Array.from({length:6-i-1},(_,j)=>[i,i+j+1])).flat(),[[0,1,2],[1,3,4],[2,4,5],[0,5,6]],[[0],[1],[2,3],[3,4]],[[0,1],[1,2],[2,3],[3,4],[4,5],[5,0]]];
 for(const groups of patterns)for(let rep=0;rep<5;rep++){
  const n=1+Math.max(...groups.flat()),full=(1<<n)-1, adj=Array.from({length:n},()=>new Set()),d=Array(n).fill(0);
  const data=groups.map(v=>({v,w:Array.from({length:1<<v.length},()=>BigInt(rand()%11))}));for(const g of data)if(sum(g.w)===0n)g.w[0]=1n;
  for(const g of groups)for(const v of g){d[v]++;for(const u of g)if(v!==u)adj[v].add(u);}
  const graph=adj.map(s=>[...s].sort((a,b)=>a-b)),deg=graph.map(a=>a.length),c=deg.map(x=>Math.max(1,Math.ceil(x/4))),delta=d.map(x=>f(1n,2n**BigInt(2*Math.max(2,x)+1)));
  for(let v=0;v<n;v++){check(le(mul(delta[v],f(5n**BigInt(c[v]),4n**BigInt(c[v]))),f(8n**BigInt(2*deg[v]),9n**BigInt(2*deg[v]+1))),"certificate");}
  const wc=Array.from({length:full+1},(_,m)=>c.reduce((s,x,v)=>s+((m>>v&1)?x:0),0)),K=wc[full]+2;
  const comps=m=>{let out=[];while(m){let x=m&-m;for(;;){let y=x;for(let v=0;v<n;v++)if(x>>v&1)for(const u of graph[v])if(m>>u&1)y|=1<<u;if(y===x)break;x=y;}out.push(x);m^=x;}return out;};
  const M=Array.from({length:full+1},(_,m)=>data.reduce((p,g)=>mul(p,f(sum(g.w.filter((_,i)=>g.v.every((v,j)=>!(m>>v&1)||(i>>j&1)))),sum(g.w))),one()));
  for(let m=0;m<=full;m++)check(eq(M[m],comps(m).reduce((p,s)=>mul(p,M[s]),one())),"momentFactor");
  const signed=Array.from({length:full+1},(_,m)=>delta.reduce((p,x,v)=>m>>v&1?mul(p,x):p,f(pop(m)%2?-1n:1n)));
  const P=Array.from({length:full+1},(_,m)=>{let p=Array.from({length:K+1},zero);for(const a of subsets(m))p[wc[a]]=add(p[wc[a]],mul(signed[a],M[a]));return p;});
  const L=P.map(p=>logcoef(p,K)), mob=Array.from({length:full+1},()=>Array.from({length:K+1},zero));
  for(let m=1;m<=full;m++)for(let j=1;j<=K;j++){let z=zero();for(const a of subsets(m))z=pop(m^a)%2?sub(z,L[a][j]):add(z,L[a][j]);mob[m][j]=z;if(comps(m).length>1||wc[m]>j)check(eq(z,zero()),"weightedSupportCancellation");}
  for(let k=1;k<=K;k++){let got=weightedSets(graph,c,k).map(a=>a.reduce((m,v)=>m|(1<<v),0)).sort((a,b)=>a-b),want=Array.from({length:full},(_,i)=>i+1).filter(m=>wc[m]<=k&&comps(m).length===1);check(got.join(",")===want.join(","),"enumeration");for(let j=1;j<=k;j++)check(eq(got.reduce((z,m)=>add(z,mob[m][j]),zero()),L[full][j]),"coefficientReconstruction");}
  for(const t of [f(5n,4n),f(-5n,4n)])for(let m=1;m<=full;m++)for(let v=0;v<n;v++)if(m>>v&1)check(le(abs(sub(div(val(P[m],t),val(P[m^(1<<v)],t)),one())),f(1n,9n)),"realRatio");
  stats.cases++;
 }
 const star=[];
 for(const h of [2,4,8,16,32,128,512]){
  let d0=Math.max(2,h),D=2n**BigInt(2*d0+1),a=534n**BigInt(h),b=377n**BigInt(h),den=544n**BigInt(h);
  let P=f(D*a-b,D*den),P0=f(a,den),loss=sub(one(),div(P,P0));
  check(le(zero(),loss)&&le(loss,f(1n,D)),"starBound");
  if(h<=8){let direct=zero();for(let m=0;m<(1<<(h+1));m++){let root=m&1,p=f(pop(m)%2?-1n:1n,root?D:1n);for(let i=0;i<h;i++){let leaf=m>>(i+1)&1;p=mul(p,root?(leaf?f(7n,544n):f(12n,17n)):(leaf?f(10n,544n):one()));}direct=add(direct,p);}check(eq(P,direct),"starFormula");}
  const adj=[Array.from({length:h},(_,i)=>i+1),...Array.from({length:h},()=>[0])],c=[Math.max(1,Math.ceil(h/4)),...Array(h).fill(1)],k=Math.min(c[0]+1,10);
  const count=weightedSets(adj,c,k).length;
  const choose=(n,j)=>{let z=1;for(let i=1;i<=j;i++)z=z*(n-i+1)/i;return z;};
  let expected=h;for(let j=0;j<=Math.min(h,k-c[0]);j++)expected+=choose(h,j);check(count===expected,"starEnumeration");
  star.push({h,k,rootCost:c[0],connectedSupports:count,numeratorBits:P[0].toString(2).length,denominatorBits:P[1].toString(2).length,rootOmissionBoundExponent:2*d0+1});
 }
 return {stats,star,checks:Object.entries(stats).filter(([k])=>k!=="cases").reduce((s,[,v])=>s+v,0)};
}
console.log(JSON.stringify(verify(),null,2));
```
