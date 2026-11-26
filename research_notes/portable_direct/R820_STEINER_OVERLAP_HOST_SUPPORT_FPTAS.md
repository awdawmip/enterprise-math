# R820 — Overlapping Steiner factors: local load and host-support FPTAS

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH, own registered metadata EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 recovered; execution_authorized=false. No shared claim, Result, or owner change. RUNNING query r3-20261126-r820-running-read was pending at derivation; no inference of empty inventory. Frozen scientific input a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 and joint observer read. ACTIVE worldview read; current global entries verified at 0c5702144ed3018b81f1b1cc7c3653c8c6b49e3c. Predecessor e8e09b6c56e25b95f941cfd0b5a3157aab0570cb:research_notes/portable_direct/R819_STEINER_TREE_INTERACTION_AND_SPARSE_TENSOR.md (blob 154f8c381f5a9e687f84fa35d304f869dc576f47). Nonnegative auxiliary fixed-charge observer only; preserve native signed BRC, full original road matrices, branch/time/provenance and common depth. No claim of native residual attribution.

## 1. Model and result

Take finitely many R819 trees, disjoint as labeled edge sets, with distinct terminal leaves in each tree. Each terminal is attached to an exterior independent nonnegative rational joint group, possibly with multiple distinct ports in one group. Identify each terminal leaf with its exterior group vertex to form a host multigraph H; retain all internal tree vertices and edge labels. The host can have arbitrary cycles and treewidth. Assume maximum host degree Delta is fixed. Each local group, internal or exterior, is given by a rational table or an exact polynomial-bit, polynomial-time unary/pinned contraction oracle; its support can be arbitrary. Tree corner contractions are exact via R813/R819 messages. All baseline unary weights are absorbed into exterior groups, including any original nonnegative unary factors; zero total mass is detected separately. Each R819 tree has positive corner contractions on the considered support. Factor the constant and singleton interactions exactly. The remaining factors are indexed by selected terminal sets S, |S|>=2, with footprint F equal to the edge set of its minimal Steiner subtree in its original tree, cost c=|F|, and interaction R_S=exp(L_S), positive rational. Assume c>=2 (exclude isolated two-leaf one-edge trees, or handle their factors with the general local-load condition below). Each footprint determines its S before terminal identification. After gluing the footprint is connected and has at most c+1 host vertices. Its multiplier on a binary exterior configuration is 1+a_S I_S with a_S=R_S-1, I_S the product of its selected terminal bits. Let Z_base be the exactly computable unary baseline normalization. Under the normalized independent group measure,
 Z/Z_base = P(1), P(t)=E prod_S(1+a_S t^c I_S).
All factors including overlapping high-order ones are retained in this exact expression. The total possible S can be exponential; the algorithm need not enumerate them.

Theorem: if R819 radii satisfy the vertex sum condition, theta=max D_e/r_e, x=4 Delta^2 theta<1, and (2/3)x^2/(1-x)<=1/16, then there is a deterministic FPTAS for Z for this class, with an arbitrary number of trees and terminal ports. In particular Delta<=3 and every R817 contracted tree edge passes at least two actual soft shared factors (D_e<=4/125^2), using r_e=1/24, meets the certificate. This is a statement about the specified glued-tree auxiliary family, not arbitrary exterior weights or arbitrary Port graphs without such a representation.

## 2. General overlap zero-free proof (independent derivation of the R814/R815 type condition)

For any finite family of bounded factors with a dependency graph (here adjacency when host footprints meet a vertex), assume moments factor across disconnected induced supports and absolute joint moments <=1. Allow signed real a_f and complex t. For any subset U of factors, write P_U(t) for its polynomial. The expansion over connected supports C gives polymer weights w(C)=prod_{f in C}(a_f t^c_f) E prod I_f; hence |w(C)|<=prod u_f, u_f=|a_f| R^c_f for |t|<=R. Recurrence at v in U:
 P_U=P_{U-v}+sum_{connected C subset U, v in C} w(C) P_{U minus N[C]}.
Assume 0<q_f<1 and u_f<=q_f prod_{g adjacent f}(1-q_g)^2 (omit zero factors). Prove inductively P_U nonzero and |P_U/P_{U-v}-1|<=q_v. The ratio of smaller polynomials in the recurrence is bounded using successive deletions by prod_{g in N[C] minus {v}}(1-q_g)^(-1). Set b_f=u_f prod_{g in N[f]}(1-q_g)^(-1). This ratio times the polymer weight is at most (1-q_v) prod_{f in C} b_f. For each connected C choose a deterministic rooted spanning tree. Bound the sum of these products by the sum over rooted labeled trees of finite height, allowing repeated labels across distinct branches and using at most one child of each neighboring label at a node. This overcounts, since distinct C have distinct label sets, and all terms are nonnegative. Its height recursion is T_f^(0)=b_f, T_f^(h+1)=b_f prod_{g adjacent f}(1+T_g^(h)). For t_f=q_f/(1-q_f), the hypothesis gives b_f prod(1+t_g)<=t_f. By induction all T_f^(h)<=t_f. Thus the recurrence ratio difference <=(1-q_v)t_v=q_v. Strict positivity of 1-q_v proves nonvanishing. The same reasoning works for arbitrary bounded joint factors with the declared moment factorization; no assumption of mutual independence within a connected support.

For the footprints choose q_f=2^c |a_f|. Suppose at every host vertex v, sum_{f whose footprint touches v}q_f<=beta=1/16. Then each q_f<=beta, and for each footprint F of cost c,
 prod_{g adjacent f}(1-q_g)^2 >= (1-beta)^{2(c+1)} >= (1-beta)^{4c}.
This follows by multiplying the local products at all vertices of F (repeated factors can only decrease the product), and the elementary prod(1-q)>=1-sum q. With R=3/2, 2(15/16)^4=50625/32768>3/2, so u_f<=q_f prod(1-q_g)^2. A telescope of the analytic logarithms of successive deletion ratios gives |log P(t)|<=sum q_f/(1-q_f)<= (16/15) beta |V(H)|=|V(H)|/15 on |t|<=3/2. The analytic branch is zero at t=0. Cauchy's coefficient estimate gives log tail
 E_k<= (2 |V(H)|/15)(2/3)^k.
No dependence on total number of factors or maximum degree of the factor dependency graph.

## 3. Actual R819 residual budget

For a footprint with c edges, |S|<=c+1. R819 implies |L_S|<= (2 theta)^c/3. Under the stated x condition this is <=1/2. Since e^y-1<=2y for 0<=y<=1/2, |a_f|<= (2/3)(2 theta)^c. Thus q_f<= (2/3)(4 theta)^c. For any host vertex, at most Delta^(2c) connected c-edge footprints contain it: fix ordered incident edge labels, encode each by the length-2c depth-first traversal of the original subtree rooted at a preimage of the vertex. For merged terminal leaves, choose the smallest labeled preimage deterministically. A traversal on the host reconstructs its labeled edge set, so the encoding is injective even if its image has cycles. There is at most one factor per footprint. This proves beta <=(2/3) sum_{c>=2}(4 Delta^2 theta)^c. For Delta=3, r=1/24, theta<=96/15625, x=3456/15625=0.221184, beta<= (2/3)x^2/(1-x)<1/16. The dependence graph of the high-order factors can have unbounded degree even for fixed host degree; the proof pays by geometric footprint size instead.

## 4. Host-edge support algorithm (not factor enumeration)

For A subset E(H), P_A includes exactly factors whose entire footprint is in A. Set l_j(A)=[t^j]log P_A and d_j(C)=sum_{A subset C}(-1)^(|C|-|A|)l_j(A). As a formal series, log P has monomials in independent factor variables; on replacing factor variable by t^cost, a monomial of order j uses a union of footprints with at most j distinct edges. Restriction to A preserves exactly monomials whose union is in A. Therefore d_j(C)=0 for |C|>j. If C is disconnected in edge adjacency (sharing host vertices), then for every A subset C the polynomial factors by the components, since their exterior groups are disjoint. Log adds; alternating sum is zero. Hence
 [t^j] log P = sum_{C connected, 1<=|C|<=j} d_j(C).
This is exact, even when many factors overlap. Enumerate connected host edge sets C up to k with bounded-degree DFS walks of length <=2k (for a cyclic edge set traverse each edge twice using a deterministic Euler walk in the doubled graph). Number <= n sum_{c<=k} Delta^(2c). For each C enumerate its 2^|C| subsets A; identify every contained factor by testing subsets of A for a minimal subtree of an original labeled tree with terminal leaves. At most 2^k candidate footprints. For each retained footprint compute R_S from <=2^(k+1) exact full tree corner contractions; do not cut off off-footprint branches, as their influence is included in the corner values. Only terminal ports whose incident labeled edge lies in A can be involved, at most 2k such ports. Enumerate their binary assignments, get their joint marginal weight by multiplying exact exterior group pinned/unary oracle values divided by the normalization, then multiply the factors 1+a_f I_f t^cost to order k. Sum to obtain P_A(t) mod t^(k+1); compute its formal log via the recurrence from P'=P (log P)'. All computations through log coefficients are rational. Thus cost is n exp(O(k)) poly(input length) for fixed Delta. Common denominator bounds: each retained rational coefficient has polynomial bit length before products; after expanding, any coefficient of degree <=k uses at most k factors and sums over <=2^(2k) assignments, and denominators are bounded by products of the polynomially many oracle denominators and their powers <=k (and factorials through k for log). The number of all retained quantities is polynomial for k=O(log(n/epsilon)); rational arithmetic remains polynomial-bit. Final exponentiation can use certified rational interval Taylor or standard arbitrary-precision exp with polynomial bit cost, since the real truncated log has magnitude O(n) and absolute accuracy O(epsilon) suffices. For example choose E_k<=epsilon/8 and exp evaluation relative error <=epsilon/4 for 0<epsilon<=1; the combined multiplicative error is inside 1±epsilon. Z_base is exact. Arbitrary feasible nonzero charge already represented in the local group oracles is allowed; no claim that such a decomposition exists for every charge or every native network. Original data are not erased.

## 5. Exact finite checks

Deterministic BigInt rational replay below: two or three three-arm trees glued to common exterior groups, including repeated triple of exterior vertices and host cycles. Exterior ports within a group are all the same binary variable (hard correlation); independent across groups. Nonuniform rational weights and zero local states permitted. The check starts after absorption of unary factors, comparing exact normalized full tensor and residual factor products. Exact corner reconstruction, local load and zero-free sufficient inequalities, host-support cancellation and log coefficient reconstruction through degree 4 were checked. It does not benchmark the asymptotic algorithm or directly check complex zeros; the latter rests on the proof. The synthetic D values are <=1/4000. These are auxiliary observer fixtures, not native BRC experiments.

```json
{
  "cases": 12,
  "cornerIdentities": 256,
  "localCertificate": 77,
  "analyticCondition": 129,
  "supportZeros": 15284,
  "coefficientRecovery": 48,
  "exactContraction": 12
}
```
```javascript
function verify(){
 const gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a<0n?-a:a};
 const F=(a,b=1n)=>{if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],le=(a,b)=>a[0]*b[1]<=b[0]*a[1],abs=a=>a[0]<0n?neg(a):a,pow=(a,k)=>{let b=F(1n);while(k--)b=mul(a,b);return b};
 const zero=F(0n),one=F(1n),pc=x=>{let c=0;while(x){x&=x-1;c++}return c};
 const stats={cases:0,cornerIdentities:0,localCertificate:0,analyticCondition:0,supportZeros:0,coefficientRecovery:0,exactContraction:0};
 const ck=(b,k)=>{if(!b)throw Error(k);stats[k]++};
 let seed=820;const rnd=()=>((seed=(Math.imul(seed,1664525)+1013904223)>>>0)>>>16);
 const shapes=[[[0,1,2],[0,1,3]],[[0,1,2],[1,2,3],[0,2,3]],[[0,1,2],[0,1,2],[0,1,2]]];
 for(const stars of shapes)for(let rep=0;rep<4;rep++){
  const n=1+Math.max(...stars.flat()),m=3*stars.length,K=4,all=(1<<m)-1;
  const factors=[],tables=[],probs=Array.from({length:n},()=>F(BigInt(1+rnd()%7),8n));
  for(let j=0;j<stars.length;j++){
   const w=Array.from({length:8},()=>BigInt(rnd()%8)),D=Array.from({length:3},()=>F(1n,BigInt(4000+rnd()%2000)));if(w.every(x=>!x))w[0]=1n;
   const Z=Array.from({length:8},(_,x)=>{let s=zero;for(let a=0;a<8;a++){let v=F(w[a]);for(let i=0;i<3;i++)if((a&x)&(1<<i))v=mul(v,sub(one,D[i]));s=add(s,v)}return s});
   const R=Array.from({length:8},(_,s)=>{let r=one;for(let u=s;;u=(u-1)&s){r=(pc(s)-pc(u))%2?div(r,Z[u]):mul(r,Z[u]);if(!u)break}return r});
   for(let x=0;x<8;x++){let y=Z[0];for(let u=x;u;u=(u-1)&x)y=mul(y,R[u]);ck(eq(y,Z[x]),"cornerIdentities")}
   tables.push({Z,R});
   for(let s=1;s<8;s++)if(pc(s)>=2){let ext=0;for(let i=0;i<3;i++)if(s&(1<<i))ext|=1<<stars[j][i];factors.push({foot:s<<(3*j),ext,c:pc(s),a:sub(R[s],one),vs:[n+j,...stars[j].filter((v,i)=>s&(1<<i))]})}
  }
  const q=factors.map(f=>mul(abs(f.a),F(2n**BigInt(f.c))));
  for(let v=0;v<n+stars.length;v++){let s=zero;factors.forEach((f,i)=>{if(f.vs.includes(v))s=add(s,q[i])});ck(le(s,F(1n,16n)),"localCertificate")}
  for(let i=0;i<factors.length;i++){let f=factors[i],b=q[i];for(let j=0;j<factors.length;j++)if(i!==j&&f.vs.some(v=>factors[j].vs.includes(v)))b=mul(b,pow(sub(one,q[j]),2));ck(le(mul(abs(f.a),pow(F(3n,2n),f.c)),b),"analyticCondition")}
  const weights=Array.from({length:1<<n},(_,x)=>probs.reduce((p,v,i)=>mul(p,x&(1<<i)?v:sub(one,v)),one));
  const cache=new Map();
  function logpoly(A){
   let ids=0;factors.forEach((f,i)=>{if((f.foot&A)===f.foot)ids|=1<<i});if(cache.has(ids))return cache.get(ids);
   let P=Array(K+1).fill(zero);
   for(let x=0;x<1<<n;x++){let p=Array(K+1).fill(zero);p[0]=weights[x];for(let i=0;i<factors.length;i++){let f=factors[i];if(!(ids&(1<<i))||(x&f.ext)!==f.ext)continue;for(let k=K;k>=f.c;k--)p[k]=add(p[k],mul(f.a,p[k-f.c]))}P=P.map((v,k)=>add(v,p[k]))}
   let L=Array(K+1).fill(zero);for(let k=1;k<=K;k++){let s=zero;for(let i=1;i<k;i++)s=add(s,mul(F(BigInt(i)),mul(L[i],P[k-i])));L[k]=sub(P[k],div(s,F(BigInt(k))))}cache.set(ids,L);return L;
  }
  const edges=stars.flatMap((t,j)=>t.map(v=>[v,n+j]));
  function connected(A){if(!A)return false;let seen=new Set(edges[Math.clz32(A&-A)^31]);let old=-1;while(old!==seen.size){old=seen.size;edges.forEach(([u,v],i)=>{if((A&(1<<i))&&(seen.has(u)||seen.has(v))){seen.add(u);seen.add(v)}})}return edges.every(([u,v],i)=>!(A&(1<<i))||(seen.has(u)&&seen.has(v)))}
  const arr=Array.from({length:1<<m},(_,a)=>logpoly(a).slice());
  for(let i=0;i<m;i++)for(let a=0;a<=all;a++)if(a&(1<<i))arr[a]=arr[a].map((v,k)=>sub(v,arr[a^(1<<i)][k]));
  for(let k=1;k<=K;k++){let sum=zero;for(let a=1;a<=all;a++){if(pc(a)>k||!connected(a))ck(eq(arr[a][k],zero),"supportZeros");else sum=add(sum,arr[a][k])}ck(eq(sum,logpoly(all)[k]),"coefficientRecovery")}
  let direct=zero,prod=zero;
  for(let x=0;x<1<<n;x++){
   let d=weights[x],p=weights[x];for(let j=0;j<stars.length;j++){let a=stars[j].reduce((s,v,i)=>s|(((x>>v)&1)<<i),0),b=tables[j].Z[0];for(let i=0;i<3;i++)if(a&(1<<i))b=mul(b,tables[j].R[1<<i]);d=mul(d,div(tables[j].Z[a],b))}
   for(const f of factors)if((x&f.ext)===f.ext)p=mul(p,add(one,f.a));direct=add(direct,d);prod=add(prod,p)
  }ck(eq(direct,prod),"exactContraction");stats.cases++;
 }
 const x=F(3456n,15625n),beta=div(mul(F(2n,3n),pow(x,2)),sub(one,x));ck(le(beta,F(1n,16n)),"localCertificate");ck(le(F(3n,2n),mul(F(2n),pow(F(15n,16n),4))),"analyticCondition");
 return stats;
}
console.log(JSON.stringify(verify(),null,2));
```

Next: extend the host-support enumeration to variable host degree using a weighted connected-edge cost with per-vertex degree payment, and investigate exact decompositions of general Port networks into the glued-tree family or direct hypergraph residual coordinates. General Port FPTAS remains open. No formal acceptance or native attribution.
