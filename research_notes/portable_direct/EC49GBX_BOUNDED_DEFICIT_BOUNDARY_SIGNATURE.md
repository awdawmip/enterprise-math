# EC49GBX — Bounded-prefix-deficit boundary signatures and an exponential separation

Status: AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_BRUTE_REPLAY / NOT_REVIEWED.
Predecessor: 4afb6f54fd07750c78d4236f02000d1a28737317:research_notes/portable_direct/EC49GBW_PREFIX_FACE_EXACT_FRONTIER.md (full content read this turn; blob a6e55535ac0173c3b9464921a29374ff5d664adc).
Inherited scientific pin BRC16943 unchanged; raw archive not reread. This is the auxiliary labeled strict-Hall combinatorial model, not a native physical simulation or new P000 assumption.

## 1. Exact bounded-deficit interface theorem
Let C be a finite set of ports with positive integer capacities c_i. Each label x has a nonempty neighborhood E_x subset C. For label set S write f_S(V)=number of labels with E_x subset V. Strict independence means f_S(V)<=c(V)-1 for every nonempty V subset C. Let A be the prefix label set, S subset A independent, r=r_M(A), d=r-|S|. Let B subset C be the boundary containing the neighborhoods of every allowed future suffix label. For nonempty U subset B define
  q_S(U)=min_{V subset C, V superset U} [c(V)-1-f_S(V)].
This is a nonnegative integer and is monotone nondecreasing in U. If B is empty, there are no coordinates and no nonempty future neighborhoods.

For every finite disjoint future set T of labeled targets supported on B,
  S union T is strictly independent iff f_T(U)<=q_S(U) for every nonempty U subset B.
Necessity: f_T(U)<=f_T(V)<=c(V)-1-f_S(V) for every V superset U. Sufficiency: for each nonempty V put U=V intersect B. If U is empty, f_T(V)=0 and S is independent. Otherwise f_T(V)=f_T(U)<=q_S(U)<=c(V)-1-f_S(V). This proves full suffix feasibility preservation, hence all suffix-subset ranks in the contraction and all weighted suffix optima. Insertions and deletions of suffix labels are evaluated against the same fixed prefix signature; deleting prefix labels itself is outside the interface scope.

For a basis J of A, q_J(U) is independent of the choice of J. Indeed q_J(U) is exactly the maximum number of extra distinct labels with neighborhood U that can be added to J, by strict Hall. Put enough such fresh probe labels in one enlarged finite strict-Hall matroid (total port capacity suffices). All bases of A span A in this matroid, so each gives the same independence verdict for every probe subset, by r(J union T)=r(A union T). The matroid property is the GBP/GBR strict-Hall greedy property: intersecting tight sets of an independent set have tight union, so maximal tight sets are disjoint; each label rejected by adding it lies inside a tight set. For any maximal independent J in a finite ground H, the disjoint maximal tight sets cover every rejected label, and any other independent set can keep at most c(V)-1 labels inside each such tight set and at most all labels outside them; thus no independent set is larger. Heredity and this property on every restriction imply matroid augmentation.

Fix a reference basis J0 of A and denote q_A=q_J0. Extend S to a basis J of A by d labels Z. For every nonempty V, slack for S equals slack for J plus f_Z(V), with 0<=f_Z(V)<=d. Taking minima over supersets and using basis invariance gives
  0 <= q_S(U)-q_A(U) <= d.
Thus delta_S=(q_S-q_A) is an exact bounded residual interface, with at most (d+1)^(2^b-1) possible signatures for d<=given d and b=|B|, at most (2^b-1)*ceil(log2(d+1)) bits in a fixed-width residual encoding. The reference, boundary, label weights/costs and prefix accounting must be retained separately; this is not a storage bound on the entire problem. The scalar d alone is not a sufficient observation. At d=0 every signature is zero, recovering GBW's suffix-independence factorization.

## 2. Exact incremental signature update
If a new label x has nonempty neighborhood E subset B, then it can be added to S iff q_S(E)>=1. For every nonempty U subset B,
  q_(S+x)(U)=min(q_S(U),q_S(U union E)-1).
Proof: in min_{V superset U} [slack_S(V)-1_{E subset V}], split according to E subset V. Equivalently the minimum of the unmodified slack minimum and the minimum over V containing U union E reduced by one. This works whether or not the attempted addition is feasible, although the retained-prefix algorithm accepts only feasible additions. More generally for a future multiset T,
  q_(S+T)(U)=min_{K subset B, K superset U} (q_S(K)-f_T(K)).
For one inequality choose a minimizer V for q_S(K), observing f_T(V)>=f_T(K); for the reverse choose a minimizer V for q_(S+T)(U), with K=V intersect B. All minima are finite. This is an exact update in O(2^b) coordinate operations per insertion using the single-label formula, plus mask representation cost. Dropping boundary ports restricts the signature to the remaining nonempty subsets, provided all future labels are supported there. Arbitrary suffix deletions can be handled by re-evaluating the fixed-prefix formula with the current T, not by inverting the single-insertion minimum.

## 3. Application to GBW bounded positive deficits
At each ordered cut j compute reference q_(A_j) once from a fixed basis and let B_j be the union of neighborhoods of remaining labels, so B_(j+1) subset B_j. Keep prefix count (or deficiency), accumulated integer release cost, and best reward at each interface. In processing the next label: include iff q(E)>=1 and update q by the formula, or exclude; then restrict to B_(j+1) and subtract its reference. Included actual labels earn their value, excluded dummy labels charge their release cost; other transitions charge zero. Budget-exceeding states can be discarded for nonnegative costs. Merge equal (signature, count, cost) states by keeping maximum prefix reward and witness, since suffix feasibility and future increments coincide. GBW's g_j d_j <= Delta bounds can discard states exceeding the certified per-cut deficits; at least one optimal solution remains (incumbent kept separately for strict improvement). This yields an exact finite DP with a per-cut signature count bounded by (D_j+1)^(2^|B_j|-1) for allowed deficiency D_j, plus count and budget factors. No claim of polynomial complexity in input bit length, no general small-boundary guarantee. Computing reference signatures and all DP costs must be included in performance tests. Full budget DP not executed in this round.

## 4. Sharp obstruction to a deficit-only finite-state bound
Take n>=2 ports of unit capacity. Prefix A consists of all pair neighborhoods (complete graph), suffix contains a fresh distinct copy of every pair. Strict Hall independence for pair labels is exactly graphic forest independence: a cycle violates the edge count on its vertices, a forest has at most |V|-1 edges in every nonempty induced set. For any unordered bipartition of ports into two nonempty parts choose a tree in each part. Their union S has n-2 labels, rank(A)=n-1, so d=1. A suffix edge can be added iff its endpoints are in distinct parts. Distinct unordered bipartitions give distinct single-edge feasibility patterns: the same-part equivalence relation can be reconstructed from the forbidden pairs. Hence at least 2^(n-1)-1 observer-distinct states occur at a single cut with d=1, even for one-step suffix queries. More generally all partitions into d+1 nonempty blocks occur, with exactly Stirling number S(n,d+1) distinct forest contraction partitions on this complete-graph prefix family. Thus no bound on the number of exact interface states depending only on deficit, regardless of implementation, can preserve all these labeled observations. This is an information lower bound, not a computational hardness theorem or a denial of other polynomial-size encodings.

## 5. Executed finite replay
Actual deterministic JavaScript execution in available JS runtime; seed 20261128. Models: 240 synthetic positive-capacity strict-Hall systems, 1..5 ports, 1..8 prefix labels, 1..6 suffix labels, randomly selected nonempty boundary. Exhaust all prefix subsets and all suffix subsets for each independent prefix. Direct Hall oracle tests each nonempty port subset. Compare two greedy reference bases (forward/reverse), coordinate bounds, direct suffix feasibility against signature, and sequential updates against direct recomputation for every feasible suffix subset. Additionally enumerate all unordered bipartitions with vertex 0 on the first side for n=2..8, compare single-edge query signatures and verify the exact state count. No frozen archive replay and no physical root calculation.
Result:
```json
{"seed":20261128,"models":240,"prefixSubsets":13056,"independentPrefixes":6498,"referenceBasisCoordinates":772,"residualCoordinates":23612,"suffixSubsets":107704,"acceptedSuffixSubsets":36886,"updateCoordinates":164258,"graphPartitions":247,"disagreements":0,"graphCounts":[[2,1],[3,3],[4,7],[5,15],[6,31],[7,63],[8,127]]}
```
Executed source (standalone Node-compatible; no Node timing claimed):
```javascript
function replay(){
  let z=20261128; const rnd=n=>{z=(Math.imul(z,1664525)+1013904223)>>>0;return z%n};
  const count={seed:20261128,models:0,prefixSubsets:0,independentPrefixes:0,referenceBasisCoordinates:0,residualCoordinates:0,suffixSubsets:0,acceptedSuffixSubsets:0,updateCoordinates:0,graphPartitions:0,disagreements:0};
  function ok(c,L){for(let v=1;v<c.length;v++){let f=0;for(const e of L)if((e&v)===e)f++;if(f>=c[v])return false}return true}
  function q(c,L,B){let r=Array(c.length).fill(null);for(let u=1;u<c.length;u++)if((u&B)===u){let h=Infinity;for(let v=u;v<c.length;v++)if((u&v)===u){let f=0;for(const e of L)if((e&v)===e)f++;h=Math.min(h,c[v]-1-f)}r[u]=h}return r}
  function greedy(c,A){let S=[];for(const e of A)if(ok(c,[...S,e]))S.push(e);return S}
  function sub(L,k){return L.filter((_,i)=>k&(1<<i))}
  function assert(x,msg){if(!x){count.disagreements++;throw Error(msg)}}
  for(let t=0;t<240;t++){
    const n=1+rnd(5),N=1<<n,caps=Array.from({length:n},()=>1+rnd(3)),c=Array.from({length:N},(_,v)=>caps.reduce((a,x,i)=>a+((v>>i)&1)*x,0));
    const m=1+rnd(8),s=1+rnd(6),A=Array.from({length:m},()=>1+rnd(N-1)),B=1+rnd(N-1),bm=Array.from({length:N-1},(_,i)=>i+1).filter(u=>(u&B)===u),T=Array.from({length:s},()=>bm[rnd(bm.length)]);
    const base=greedy(c,A),rev=greedy(c,[...A].reverse()),q0=q(c,base,B),q1=q(c,rev,B);
    count.models++;assert(base.length===rev.length,"basis ranks");for(const u of bm){count.referenceBasisCoordinates++;assert(q0[u]===q1[u],"reference basis signature")}
    for(let k=0;k<(1<<m);k++){
      count.prefixSubsets++;const S=sub(A,k);if(!ok(c,S))continue;
      count.independentPrefixes++;const d=base.length-S.length,qs=q(c,S,B);
      for(const u of bm){count.residualCoordinates++;assert(qs[u]>=q0[u]&&qs[u]<=q0[u]+d,"deficit bound")}
      for(let j=0;j<(1<<s);j++){
        const U=sub(T,j),orig=ok(c,[...S,...U]);let predicted=true;for(const u of bm){let f=0;for(const e of U)if((u&e)===e)f++;if(f>qs[u]){predicted=false;break}}
        count.suffixSubsets++;assert(orig===predicted,"observer");if(!orig)continue;
        count.acceptedSuffixSubsets++;let r=qs.slice();for(const e of U){assert(r[e]>=1,"single edge");let a=r.slice();for(const u of bm)a[u]=Math.min(r[u],r[u|e]-1);r=a}
        const actual=q(c,[...S,...U],B);for(const u of bm){count.updateCoordinates++;assert(actual[u]===r[u],"update")}
      }
    }
  }
  const graphCounts=[];
  for(let n=2;n<=8;n++){
    const N=1<<n,c=Array.from({length:N},(_,v)=>{let p=0;while(v){v&=v-1;p++}return p}), seen=new Set(), edges=[];
    for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)edges.push((1<<i)|(1<<j));
    for(let a=1;a<N-1;a+=2){const b=(N-1)^a,S=[];for(const side of [a,b]){let root=side&-side;for(let k=side^root;k;k&=k-1)S.push(root|(k&-k))}
      assert(S.length===n-2&&ok(c,S),"partition forest");const code=edges.map(e=>ok(c,[...S,e])?1:0).join("");assert(!seen.has(code),"partition distinguishability");seen.add(code);count.graphPartitions++}
    assert(seen.size===2**(n-1)-1,"partition count");graphCounts.push([n,seen.size])
  }
  return {...count,graphCounts};
}
console.log(JSON.stringify(replay()));
```

## 6. Source and continuation
Global main 4b0b44a8caa10502c30f1910980b3765e3e195f6; both entry blobs verified at same immutable commit (25ae05640c7920104820dba91a1df5e9fafca25e, 108cd58e0458070b5f1a8171d2f66c8c3d0aa613). Current EM control 3d3c3da71c7e20c173de7c55b66c82bcf7aff19e; current continuation, portable, research method, P000 V4/V5, ACTIVE worldview and joint/residual/Heartbeat contracts read. Native original receipt r4-20261128-0026-ec49as-read SUCCEEDED at 2026-11-27T16:27:02.673999Z: NO_CANONICAL_PUBLICATION_DIRECTORY for RS-EC49AS, no native owner projection. Historical provenance EM-DIRECT-23537B; current private identity not confirmed. Independent portable material only; no new identity, shared CLAIM, task or acceptance. Activity association pending.
Next: implement and brute-replay the actual budget DP with GBW cutoff, compare reference/signature construction, reachable states and end-to-end runtime; seek smaller envelope for small deficit and sparse boundary. Recover actual frozen BRC16943 bytes before any claimed frozen replay. Inherited GBT physical frontier (not reverified): 1991 YES, 68 NO, 334 other; next 2046; 25<=M14<=27.
