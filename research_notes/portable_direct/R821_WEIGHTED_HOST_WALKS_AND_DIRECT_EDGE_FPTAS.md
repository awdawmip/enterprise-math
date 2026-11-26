# R821 — Logarithmic host-degree payment and direct residual-edge FPTAS

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED.
Continuation of own portable informed TASK_RESEARCH lane metadata EM-DIRECT-82A007, RA-708BCC309CE076D8BB599B91, session MCP-ec17f2f30fb8409f8e664eb29ae6c08c (Source record read; no authenticated execution capability asserted). No shared Task claim, owner change, Result or review. RUNNING inventory r3-20261126-r821-running-read was RUNNING during derivation. Science pin a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and joint observer contract read. Frozen heartbeat companion missing (404); current method companion read. ACTIVE worldview and global canonical entries read at e60162ef6748f90bc625615038d1a2e235bedcdf. R820 exact predecessor d84938639538e5d9db1a0c3aec0846a3c3c24b9d:research_notes/portable_direct/R820_STEINER_OVERLAP_HOST_SUPPORT_FPTAS.md (blob 7810b200b9af2c073209408595a2222431517e60); R819 proof read from main. Scope: nonnegative auxiliary fixed-charge observer, no new native Heartbeat/BRC evolution or residual attribution. Original signed BRC, complete road matrices, branch/time/provenance/common depth are retained.

## 1. Weighted walk enumeration (unbounded host degree)
Let H be an explicitly given finite loopless multigraph, d_v its labeled incidence degree. Isolated vertices are allowed. Define b_v=ceil(log2 d_v) for d_v>=1, and
 w_e=max(1,b_u+b_v), w(A)=sum_{e in A}w_e.
All these costs are integers computed by doubling, not floating point. Then the connected nonempty edge sets C with w(C)<=k can be enumerated in n 2^{O(k)} poly(N) time, even if maximum degree is unbounded (N explicit input length).

Proof. Double every edge of C in opposite directions; the directed graph is Eulerian. Starting from any chosen vertex of C, a closed tour uses each directed edge exactly once. At each step from v encode its incident labeled edge choice by b_v binary digits; degree one requires zero digits. A tour's total code length is sum_{e=uv in C}(b_u+b_v)<=w(C)<=k and step count <=2k. For each start and fixed step count the decoding is deterministic, including zero-digit steps. Thus at most n(2k+1)2^{k+1} words/tours suffice. Enumerate affordable walks with depth <=2k, charge b_v at each departure, retain their connected distinct edge sets with w<=k and deduplicate. Prefix count obeys the same bound at each fixed depth; inspecting the actual adjacency list costs at most polynomial in N. Every eligible C occurs via its Euler tour. The decoding works for parallel labeled edges, with no degree-bound constant. This is a logarithmic, rather than linear, degree payment.

## 2. Weighted R820 host theorem
Use R820's factor model Z/Z_base=P(1), with independent base groups at host vertices, factors 1+a_f I_f supported on connected nonempty labeled edge sets F_f. Assume |I_f|<=1 and depends only on groups of that footprint. For the Steiner case there is at most one factor per original labeled subtree, identifiable from its edge set. Set c_f=w(F_f), P(t)=E prod_f(1+a_f I_f t^{c_f}), q_f=2^{c_f}|a_f|.
Suppose beta_v=sum_{f:v in V(F_f)}q_f<=1/16 for every vertex. Then P has no zeros on |t|<=3/2, and its normalized analytic log is bounded by n/15 there. The tail after degree k is <=(2n/15)(2/3)^k.

Proof: apply the R820 section 2 dependency-polymer lemma, whose sole graph hypothesis is factorization of joint moments across disconnected support. A footprint has at most |F_f|+1<=c_f+1 vertices; local product bound implies prod_{g adjacent f}(1-q_g)^2 >= (15/16)^{2(c_f+1)} >=(15/16)^{4c_f}. Since 2(15/16)^4>3/2, the R820 sufficient inequality holds at radius 3/2. Sum q_f/(1-q_f)<=n/15; Cauchy bound yields the tail. All signs allowed for a_f if final real partition is positive.

For edge restriction A keep exactly the factors with F_f subset A. The R820 Möbius support proof works verbatim with weighted cost: every monomial of degree j uses a union C of cost w(C)<=j (overlaps and repeats only increase the sum of factor costs), and disconnected C cancels by independence. Thus [t^j] log P=sum_{C connected,w(C)<=j} sum_{A subset C} (-1)^{|C|-|A|}[t^j]log P_A. Section 1 enumerates these supports. For R820 glued trees, at most 2^k candidate subtrees inside A, at most 2^{k+1} full-tree corner calls per factor, at most 2k terminal ports involved, and all restricted polynomials can be computed by exact local unary/pinned oracle evaluation and truncated products. For a direct edge model below the computation is even simpler. Use the explicit oracles and bit complexity assumptions of R820; each low-order rational coefficient uses products of at most k factor weights, and polynomially many distinct queried rationals when k=O(log(n/eps)). Common denominators are bounded by products of their denominators to polynomial powers, so no exponential bit-length hidden in the exact computations. Recover Z by exact Z_base times certified exp of the truncated log. As in R820 this yields a deterministic FPTAS under the uniform local load condition, with no maximum host degree restriction. If Z_base=0, detect it before normalization.

## 3. Degree-adaptive Steiner load without Delta
For R819 choose r_e=1/(8 max(d_u,d_v)) using host degrees (which dominate original degrees after gluing). Then sum incident radii <=1/8 at original tree vertices. Let theta_e=D_e/r_e. By R819, for a Steiner support with s>=2 edges, |L_f| <= (1/3) prod_{e in F} (2 theta_e), because |S|-1<=s. If for every edge
  2^{w_e+1} theta_e <= alpha/(d_u d_v), alpha=1/4,
then the bound on |L_f| is <=1/2. Hence |a_f|=|exp(L_f)-1|<=2|L_f| and
  q_f <= (2/3) alpha^s prod_{e=uv in F}1/(d_u d_v).
For a fixed host vertex v and fixed s, the sum of prod 1/(d_u d_v) over all distinct connected labeled s-edge supports containing v is at most 1: select a canonical directed Euler tour of the doubled edge set starting at v, injectively; the simple incidence-uniform random walk of length 2s assigns that exact tour probability prod 1/(d_u d_v). This also handles a support whose image has cycles after terminal identification. Summing the distinct tour probabilities cannot exceed 1. Since each original Steiner footprint determines its terminal subset and edge labels are disjoint between trees, no multiplicity factor is needed. Therefore beta_v <=(2/3) sum_{s>=2} alpha^s=1/18<1/16. This proves a concrete unbounded-degree extension of R820. No truncation of original joint laws is required. The random walk is only a counting proof, not an algorithm requiring sampling.

## 4. Stronger direct edge theorem: avoid the high-order expansion altogether
Whenever the internal groups and original residual roads are still available, keep the R817 rank-one absorbed representation directly:
 Z=Z_base E prod_{e=uv}(1-D_e A_{ue} A_{ve}),
where all local group laws are independent across vertices, arbitrary within each vertex, binary indicators and nonnegative rational masses. Require exact polynomial-time, polynomial-bit group pinned/unary moment oracles (or explicit tables), and an exact polynomial-bit baseline. In particular all R820 glued-tree networks have this representation before eliminating their internal groups. No assumption of acyclic host, low treewidth, bounded degree, bounded number of ports, or independent indicators within groups.
Set c_e=w_e, a_e=-D_e. The simple direct-edge sufficient condition is
  sum_{e incident v} 2^{w_e}D_e <=1/16 for every v.
It implies section 2 exactly, with one factor per edge. A direct pointwise sufficient certificate is
  D_e <= 1/[16 max(d_u,d_v) 2^{w_e}].
For any restriction A, compute P_A through degree k by enumerating B subset A; the coefficient of t^{w(B)} is incremented by
  prod_{e in B}(-D_e) prod_v E_v[prod_{e in B incident v} A_{ve}].
No high-order Steiner tensor construction, complex numerical root finding, or conditioning on exponentially many port configurations. The local joint moments are exact, not products of individual marginals. The formal log recurrence P'=P(log P)' and weighted host Möbius recovery give the FPTAS. All group weights and original residuals are retained. For arbitrary fixed feasible charge the result applies if its actual representation has these independent nonnegative group laws and tractable pinned oracles. It does not assert that arbitrary Port graphs or charges admit that representation.

With R817 D_e<=4*125^{-l_e}, put d=max(d_u,d_v). Since 2^{w_e}<=4d^2, it suffices that
  125^{l_e} >= 256 d^3.
This is O(log d) separator length, independent of target accuracy. The sharper edge-specific criterion is 125^{l_e}>=64 d 2^{w_e}. In a star the leaf degree is 1, so w_e=ceil(log2 d) for d>=2, and a quadratic rather than cubic degree payment suffices: 125^{l_e}>=128 d^2. R820's bounded-degree and R817's linear-in-dependency-degree sufficient conditions can both be bypassed for networks with the direct independent-group representation. The latter assumption matters: a general strongly coupled exterior law cannot simply be replaced by independent groups.

## 5. Exact finite verification
Executed deterministic JS BigInt rational verification, five variable-degree multigraph shapes, three weight choices per shape, including parallel edges, cycles, a degree-eight star and exact hard within-group correlation (all ports at a vertex share a bit). Base probabilities include zero and one. Verify the weighted walk enumerator against exhaustive connected edge subsets, the zero-free sufficient inequalities at each edge, weighted support vanishing and coefficient recovery through order 8, exact partition values against direct binary group assignments, and integer Port length certificate for degrees 1..1024. This is auxiliary combinatorial evidence, not native BRC computation, not a complex-root numerical test, not a production-scale FPTAS benchmark. General theorem rests on the analytic proof.

```json
{
  "cases": 15,
  "load": 84,
  "zeroFreeHypothesis": 90,
  "weightedEnumeration": 5892,
  "supportZeros": 10710,
  "coefficientRecovery": 120,
  "directPartition": 15,
  "portLengthCertificate": 1024
}
```

```javascript
function verify(){
 const gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a<0n?-a:a};
 const F=(a,b=1n)=>{const g=gcd(a,b);return[a/g,b/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],le=(a,b)=>a[0]*b[1]<=b[0]*a[1],pow=(a,k)=>{let b=F(1n);while(k--)b=mul(a,b);return b};
 const zero=F(0n),one=F(1n),cl=d=>{let k=0,p=1;while(p<d){k++;p*=2}return k},stats={cases:0,load:0,zeroFreeHypothesis:0,weightedEnumeration:0,supportZeros:0,coefficientRecovery:0,directPartition:0,portLengthCertificate:0};
 const ck=(b,k)=>{if(!b)throw Error(k);stats[k]++};
 const shapes=[[[0,1],[1,2],[2,3],[3,4]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8]],[[0,1],[1,2],[2,0],[0,3],[1,3],[2,3]],[[0,1],[0,1],[1,2],[2,3],[3,0]],[[0,1],[0,2],[0,3],[1,4],[1,5],[2,5],[3,4]]];
 for(const edges of shapes)for(let rep=0;rep<3;rep++){
  const n=1+Math.max(...edges.flat()),m=edges.length,M=1<<m,adj=Array.from({length:n},()=>[]);
  edges.forEach(([u,v],i)=>{adj[u].push([v,i]);adj[v].push([u,i])});
  const d=adj.map(a=>a.length),w=edges.map(([u,v])=>Math.max(1,cl(d[u])+cl(d[v]))),D=edges.map(([u,v],i)=>F(1n,BigInt(16*Math.max(d[u],d[v])*(2**w[i])*(1+rep)))),q=D.map((x,i)=>mul(x,F(2n**BigInt(w[i])))),K=8;
  const probs=Array.from({length:n},(_,v)=>F(BigInt((v+rep)%5),4n));
  for(let v=0;v<n;v++)ck(le(adj[v].reduce((s,[u,i])=>add(s,q[i]),zero),F(1n,16n)),"load");
  for(let i=0;i<m;i++){let b=q[i];for(let j=0;j<m;j++)if(i!==j&&edges[i].some(v=>edges[j].includes(v)))b=mul(b,pow(sub(one,q[j]),2));ck(le(mul(D[i],pow(F(3n,2n),w[i])),b),"zeroFreeHypothesis")}
  const cost=Array(M).fill(0),vs=Array(M).fill(0),terms=Array(M).fill(one);
  for(let a=1;a<M;a++){let i=31-Math.clz32(a&-a),b=a^(1<<i);cost[a]=cost[b]+w[i];vs[a]=vs[b]|(1<<edges[i][0])|(1<<edges[i][1]);terms[a]=mul(terms[b],sub(zero,D[i]))}
  const moments=vs.map(mask=>probs.reduce((p,x,v)=>mask&(1<<v)?mul(p,x):p,one));
  function connected(a){if(!a)return false;let i=31-Math.clz32(a&-a),seen=1<<edges[i][0],old;do{old=seen;edges.forEach(([u,v],j)=>{if((a&(1<<j))&&(seen&((1<<u)|(1<<v))))seen|=(1<<u)|(1<<v)})}while(old!==seen);return seen===vs[a]}
  for(const budget of [2,4,6,8]){
   const found=new Set();
   function walk(v,steps,c,a){if(a&&cost[a]<=budget)found.add(a);if(steps===2*budget||c+cl(d[v])>budget)return;for(const [u,i] of adj[v]){const b=a|(1<<i);if(cost[b]<=budget)walk(u,steps+1,c+cl(d[v]),b)}}
   for(let v=0;v<n;v++)walk(v,0,0,0);
   for(let a=1;a<M;a++)ck(found.has(a)===(connected(a)&&cost[a]<=budget),"weightedEnumeration");
  }
  const p=Array.from({length:M},()=>Array(K+1).fill(zero));
  for(let a=0;a<M;a++)if(cost[a]<=K)p[a][cost[a]]=mul(terms[a],moments[a]);
  for(let i=0;i<m;i++)for(let a=0;a<M;a++)if(a&(1<<i))for(let k=0;k<=K;k++)p[a][k]=add(p[a][k],p[a^(1<<i)][k]);
  const L=p.map(P=>{let l=Array(K+1).fill(zero);for(let k=1;k<=K;k++){let s=zero;for(let i=1;i<k;i++)s=add(s,mul(F(BigInt(i)),mul(l[i],P[k-i])));l[k]=sub(P[k],div(s,F(BigInt(k))))}return l});
  const allL=L[M-1].slice();
  for(let i=0;i<m;i++)for(let a=0;a<M;a++)if(a&(1<<i))for(let k=1;k<=K;k++)L[a][k]=sub(L[a][k],L[a^(1<<i)][k]);
  for(let k=1;k<=K;k++){let sum=zero;for(let a=1;a<M;a++){if(cost[a]>k||!connected(a))ck(eq(L[a][k],zero),"supportZeros");else sum=add(sum,L[a][k])}ck(eq(sum,allL[k]),"coefficientRecovery")}
  let z=zero,ref=zero;
  for(let a=0;a<M;a++)z=add(z,mul(terms[a],moments[a]));
  for(let x=0;x<1<<n;x++){let y=probs.reduce((p,v,i)=>mul(p,x&(1<<i)?v:sub(one,v)),one);edges.forEach(([u,v],i)=>{if((x&(1<<u))&&(x&(1<<v)))y=mul(y,sub(one,D[i]))});ref=add(ref,y)}
  ck(eq(z,ref),"directPartition");stats.cases++;
 }
 for(let d=1;d<=1024;d++){let l=1;while(125n**BigInt(l)<256n*BigInt(d)**3n)l++;let w=Math.max(1,2*cl(d));ck(4n*16n*BigInt(d)*2n**BigInt(w)<=125n**BigInt(l),"portLengthCertificate")}
 return stats
}
console.log(JSON.stringify(verify(),null,2));
```

Next: remove the long-separator hypothesis for direct residual networks, by deriving a local load certificate tied to actual Port degree at each original block and by allowing degree-adaptive costs that need not charge both endpoint degrees on every edge. Determine which arbitrary Port networks can be represented as independent tractable joint groups with small two-end residual edges. General complete Port FPTAS and native residual attribution remain open.
