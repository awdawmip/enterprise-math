# R835 — Neighbor-prefix regrading and a high-girth obstruction to every incidence-anchor grading

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_GRAPH_CODE_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH; EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Own metadata recovered by r3-20261127-r835-own-read; no run, execution_authorized=false. Owner query r3-20261127-r835-running-read RUNNING during derivation; no shared claim, Result or ownership mutation.
Frozen scientific source a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint-observer blob 3923890d77a02d84b772f789e6912dd14f220d14 verified. Frozen Heartbeat companion path returned 404; current terminology companion read at 93224276f755299b75d5b5e1a3e2553fb41668c9 without repinning. Global entry snapshot 476f1fa8fbcf0ed8619e50802fde5c5cf3bac737; ACTIVE worldview, P000 projection/original blob, mathematical evidence and relevant method rules read. This is auxiliary independent-group joint-moment theory, preserving original signed factors, road and branch data, time and common depth. No native BRC dynamics or native residual attribution.
Direct dependencies: R834 at 6fd1421bb2e12caf06677625b23706d5d04444bf:research_notes/portable_direct/R834_DEPENDENCY_COVER_QUOTIENT_AND_COST_REGRADING.md; R825 at 6ee4743d62741ab9898036d556175202ab6c76d8:research_notes/portable_direct/R825_ADAPTIVE_PREFIX_ENTROPY_PAYMENT.md. R834 analytic certificate reused with its hypotheses; new enumeration proof is independent of the choice of analytic anchors.

## 1. Neighbor-prefix enumeration theorem

Let G=(V,E) be the explicit original LABEL dependency graph, or a supergraph covering every actual dependence edge, so moments on vertex sets with no cross-edge factor exactly (as in R834 independent physical groups). Choose nonnegative integer lengths L_v satisfying the open-neighborhood Kraft constraints
    sum_{w in N(v)} 2^(-L_w) <= 1   for every v.
The empty neighborhood has sum zero. Set new interpolation degrees
    c_v = L_v + 2.
For any connected nonempty support S, let c(S)=sum_{v in S} c_v. All supports with c(S)<=k can be enumerated without duplication in |V| 2^{O(k)} poly(N,k) time, N the full explicit input size, even when physical degree is large. A uniform alternative is L_v=ceil(log2(max(1,Delta))) for max degree Delta. This is not the R834 incidence-anchor cost a_v+L_v: degree/anchor count is no longer charged linearly.

Proof. At each v build a canonical binary prefix code for the labels in N(v), with their prescribed lengths L_w. For a support S take the least label as root and its deterministic BFS spanning tree (neighbors ordered by label). Encode the rooted ordered tree recursively: at each vertex v, for each child w emit 1, then the codeword of w in v's codebook, then the encoding of the subtree at w; after all children emit 0. The root label is supplied separately. Zero-length prefix code is allowed only for a singleton neighborhood. There are |S|-1 child flags and |S| stop bits, hence bit length exactly
    2|S|-1 + sum_{w in S minus root} L_w <= c(S)-1.
Decoding is deterministic, even with empty codewords because each child has a preceding 1. The decoded labels reconstruct S. A repeated label, incomplete parse, invalid prefix, noncanonical root/tree or cost exceeding k is rejected. Enumerate roots and binary strings of length <=k-1 and accept canonical encodings; this proves the complexity and complete coverage. Ineligible labels with c_v>k may be removed solely from the enumeration codebooks, retaining their original contribution to the full polynomial. Restricted Kraft remains valid; construct codes of lengths <=k in polynomial time. No loss of original joint observations.

## 2. Exact log coefficients and FPTAS transfer

Write P_U(t)=E prod_{v in U}(1+alpha_v I_v t^{c_v}), with exact joint moment oracle and envelope |E prod_{v in S}I_v|<=prod lambda_v; same scope as R834. At t=1 the regraded polynomial equals the old target for EVERY U; general-t identity is not asserted. For any support S the subset Mobius difference of log P_U over U subset S vanishes if S is disconnected, since each induced set factors across the components of S. As formal multivariate log, the difference retains only monomials using every label of S, so its lowest possible univariate degree is at least c(S). Exact truncated logs can be computed from subset joint moments, using formal rational power series through k. Enumerating all connected S with c(S)<=k and summing those differences obtains the true degree-k truncation of log P. Cost is |V| 2^{O(k)} poly(N,k) with the polynomial-bit/time oracle (each selected support has <=k/2 labels). Canonical prefix code, Mobius extraction and moment evaluation retain actual labels and signs; the graph is a computational certificate, not a quotient of physical state.

Independently choose any R834 analytic bundle cover and payments d_AH. With u_v=|alpha_v| lambda_v R^{c_v} and the R834 w_H,Q_A,T_A|H, its sufficient inequalities imply nonvanishing and error
    E_k <= R^(-k)/(R-1) sum_A (Q_A-1)/(2-Q_A).
Fixed R>1 and Q_A<=2-eta for fixed eta>0, explicit polynomial-size cover and valid witness give k=O(log((N+1)/epsilon)). Real coefficients and P(0)=1 imply P(1)>0; certified exponential of the approximate log gives a deterministic FPTAS (positive baseline as in R825; zero baseline handled exactly). This decouples the graph-neighbor enumeration coordinate from the analytic anchor coordinate. No novel native arithmetic is claimed.

## 3. A family with high degree and no incidence-grading certificate, even with artificial anchors

For j>=7 let Delta=2^j, C=4j+13. Take any finite simple Delta-regular graph G of girth >2^C. Such graphs exist constructively: take the finite radius-g ball of the infinite tree of reduced words in Delta involutive generators, g=2^C. For each generator i, swap the endpoints of all color-i edges inside the ball and fix unmatched boundary vertices. These are permutations of the ball. No nonempty reduced word of length <=g acts as identity, since its action on the root follows the reduced tree path inside the ball (reversal of word order does not alter reducedness). The finite generated group has a connected simple Delta-regular Cayley graph of girth >g. This is an existence construction, not an executed huge graph generation. The family has unbounded treewidth (treewidth >= min degree).

One original label per vertex. One independent Bernoulli group per graph edge, p=1-1/(100 Delta). I_v is the product of its incident group bits; joint moment on S is p to the number of distinct incident edges. Exact moment oracle in polynomial time and bit length in explicit input. The true physical dependency graph is precisely G for 0<p<1 (neighbor indicators have strictly positive covariance). Choose arbitrary signs of rational alpha_v with magnitude
    |alpha_v|=1/[12 Delta (4/3)^(j+2)].
Use lambda_v=1, uniform L_v=j, c_v=j+2, R=4/3. Then u_v=1/(12 Delta). For analytic certificate use singleton bundles and edge anchors with constant d=1/(4 Delta). Every Q_A=(1+d)^2<2. Every incidence inequality is
    u_v ((1+d)/(1-d))^(Delta-1) <= d.
Indeed ratio=1+x, x=2/(4 Delta-1), Delta x<=2/3. Binomial coefficients <=Delta^r, so (1+x)^(Delta-1) < 1/(1-Delta x)<=3. All inequalities pass with strict margin. For Delta>=2 Q is uniformly bounded away from 2. Even sum_A (Q_A-1)/(2-Q_A)<=9|V|/14: d<=1/4 implies Q-1<=9d/4 and 2-Q>=7/16, |E|=|V|Delta/2. Therefore k=O(log((|V|+1)/epsilon)) for this family. We have the deterministic FPTAS in section 2 without any degree bound.

Now consider ANY R834 incidence-based original-label interpolation grading: an arbitrary explicit family of nonempty anchors covering every vertex and every dependency edge, including arbitrary artificially added edges, each with Kraft lengths L_v>=0 and costs c_v=a_v+L_v where a_v is its anchor count. The analytic cover may be entirely separate, with any bundles and valid envelopes. Suppose an R834 certificate at any R>=4/3 existed. Each original envelope obeys lambda_v>=E I_v=p^Delta>=99/100. For its analytic bundle H, u_v<=w_H<=d_AH<1 (T/(2-T)>=1 and Q_A<2). Thus
    (4/3)^(c_v-(j+2)) < 1200 Delta/99.
But (4/3)^3>2 and 16 Delta>1200 Delta/99; hence c_v<j+2+3(j+4)=4j+14, i.e. c_v<=C. In particular every anchor contains at most 2^C labels by Kraft (each term >=2^(-C)). By the girth assumption its induced TRUE dependency subgraph is a forest; an anchor A covers at most |A|-1 true edges, regardless of artificial ones. Since every true edge must be covered,
    |V| Delta/2 = |E| <= sum_A |E(G[A])| <= sum_A |A| = sum_v a_v <= |V| C.
This contradicts Delta/2>C for j>=7 (base j=7 and doubling). Therefore no such old incidence-anchor grading and analytic witness can certify any R>=4/3, even with optimized arbitrary artificial covers, bundle partitions and lawful envelope choices. This is a separation of the R834 grading/certificate class, not a hardness result, nor an impossibility for R834 at smaller radii. The new method uses exactly the same complete physical moments and same target P(1). High girth is necessary only for this strong all-cover separation, not the new enumeration theorem or its zero-free witness.

## 4. Evidence and limitations

Executed JavaScript exhaustive enumeration of every labeled simple graph on 1..5 vertices under two length allocations (uniform; heterogeneous increasing lengths by label modulo 3), all nonempty connected supports. Verified code length, exact inverse decoding, uniqueness. Exact BigInt integer checks for Delta=2..128 of analytic edge witness inequalities; j=7..64 of the numerical obstruction. Results (counts are not independent theorem reviews):
{"graphs":2198,"connected_supports":39576,"code_length":39576,"decode":39576,"injective":39576,"degree_certificates":254,"cover_obstructions":116}
All assertions passed. General theorems have the written analytic proofs above. No huge high-girth graph was materialized, no native BRC execution, and no production timing test. General full Port realization, original moment oracle availability there, and native transfer remain open. Next: optimize neighbor Kraft lengths jointly with R834 analytic payments, using the neighborhood rather than anchor incidence constraints; investigate rationally verified graph-based resource optimizer and actual native Port realizability. Do not repeat this enumeration/obstruction proof.

## Replay (JavaScript)

```javascript
function replay(){
 let checks={graphs:0,connected_supports:0,code_length:0,decode:0,injective:0,degree_certificates:0,cover_obstructions:0};
 const ok=(x)=>{if(!x)throw Error("check failed")};
 for(let n=1;n<=5;n++){
  let edges=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)edges.push([i,j]);
  for(let mask=0;mask<2**edges.length;mask++){
   let adj=Array.from({length:n},()=>[]);for(let i=0;i<edges.length;i++)if(mask&(1<<i)){let [a,b]=edges[i];adj[a].push(b);adj[b].push(a)}
   adj.forEach(x=>x.sort((a,b)=>a-b));
   for(let variant=0;variant<2;variant++){
    checks.graphs++;
    let base=Math.ceil(Math.log2(Math.max(1,...adj.map(x=>x.length))));
    let L=adj.map((_,i)=>base+(variant?i%3:0)),codes=adj.map(ns=>{let k=0,prev=0,table={};for(let v of [...ns].sort((a,b)=>L[a]-L[b]||a-b)){k*=2**(L[v]-prev);ok(k<2**L[v]);table[v]=L[v]?k.toString(2).padStart(L[v],"0"):"";k++;prev=L[v]}return table});
    let seen=new Set();
    for(let S=1;S<2**n;S++){
     let vs=Array.from({length:n},(_,i)=>i).filter(i=>S&(1<<i)),root=vs[0],visited=new Set([root]),child=adj.map(()=>[]);
     let queue=[root];for(let i=0;i<queue.length;i++){let v=queue[i];for(let w of adj[v])if((S&(1<<w))&&!visited.has(w)){visited.add(w);queue.push(w);child[v].push(w)}}
     if(visited.size!==vs.length)continue;
     checks.connected_supports++;
     const encode=v=>child[v].map(w=>"1"+codes[v][w]+encode(w)).join("")+"0";
     let word=encode(root),cost=vs.reduce((a,v)=>a+L[v]+2,0);
     ok(word.length<=cost-1);checks.code_length++;
     let pos=0,decoded=new Set([root]);
     function decode(v){while(true){let b=word[pos++];if(b==="0")return;ok(b==="1");let opts=Object.entries(codes[v]);let code="",hit=opts.find(([w,c])=>c===code);while(!hit){ok(pos<word.length);code+=word[pos++];hit=opts.find(([w,c])=>c===code)}let w=+hit[0];ok(!decoded.has(w));decoded.add(w);decode(w)}}
     decode(root);ok(pos===word.length&&decoded.size===vs.length&&vs.every(v=>decoded.has(v)));checks.decode++;
     let key=root+":"+word;ok(!seen.has(key));seen.add(key);checks.injective++;
    }
   }
  }
 }
 for(let d=2n;d<=128n;d++){
  let a=4n*d+1n,b=4n*d-1n;ok(a*a<2n*(4n*d)**2n);ok(a**(d-1n)<3n*b**(d-1n));checks.degree_certificates+=2;
 }
 for(let j=7n;j<=64n;j++){let d=2n**j,C=4n*j+13n;ok(C<d/2n);ok(99n*4n**(3n*(j+4n))>=1200n*d*3n**(3n*(j+4n)));checks.cover_obstructions+=2}
 return checks;
}
console.log(replay());
```
