# R773 — All-rank exact reserve, Hall deficit and completion duality

2026-11-24. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R770 / EXACT_JS_CHECKED / NOT_REVIEWED.
Continuation of R772, 300d380d8d59a88eed022428af8d99da6fdf5035:research_notes/portable_direct/R772_INDUCED_SUPPORT_RESERVE_THEOREM.md (full content read, blob 04358162650eca64f26a47c59678c6c1fa2420a5), and R770, 7603a5655b287391d5a91c90508dd93ab7dabbec:research_notes/portable_direct/R770_ALL_RANK_GRAPHIC_SHARP_SAVING.md (proof sections 1–4 read). Scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged; P000 V5 and joint-relation at pin verified, blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14. Weighted BRC substrate exact blob f375a059fa4af8c6eefaddb4d4a8689a0c063674 read, pin association inherited. Generated foundation package at frozen pin returned 404; no repin. Current account entries at b0c85139b9bb0692651aacf1e7c4ee7f955dd184, ACTIVE worldview, P000 projection matching canonical V4, math/output/BRC/residual rules, current continuation, portable and method contracts consulted. Own read-only metadata recovery r3-20261124-2220-own-metadata-v1 returned original registration SUCCEEDED, no runs and execution_authorized=false, matching existing Activity RA-708BCC309CE076D8BB599B91, EM-DIRECT-82A007 / TASK_RESEARCH. Owner inventory r3-20261124-2220-owner-read-v1 last observed RUNNING at derivation. No shared CLAIM, PROGRESS or Result. Independent portable continuation.

## 1. Statement

Exactly the R772 Boolean auxiliary observer: finite loop-free subcubic multigraph G (parallel edges and isolated vertices allowed), local V_i=F2^2 (four even Port triples, private ports for absent incidences), cycle kernel K, quotient q:V=product V_i -> V/K. S(0)={0}, S(1)=V_i minus {0}, S(2)=V_i. Let P(p)=product S(p_i), p_i,t_i in {0,1,2}. Feasible reserve t for target q(w) means q(P(p))+q(w) subset q(P(t)); k_p(q(w)) is min sum t_i. The full quotient reserve cost is F=2n-r by R770 (author theorem, not independently admitted).

Let U={i:p_i>0}, J={i:p_i=1}, B=sum p_i=2|U|-|J|, H=q(V_U), K_U=K intersect V_U, r_U=r(G[U]), h=2|U|-r_U. For A subset J define d(A)=rank of the simultaneous projection of K_U on coordinates A. Since its kernel is exactly K_(U minus A),
d(A)=r_U-r(G[U minus A]).
Define the Hall deficit
D=max_{A subset J} (|A|-d(A)) >=0 (empty set included).
Then for every finite G and all p:
    k_p(0)=h-D <= k_p(q(w)) for EVERY target q(w).
    C(p)=F-h+D, where C(p)=min sum a_i with q(P(p))+q(P(a))=V/K.
In particular min_w k_p(q(w))+C(p)=F. The completion lower bound of R772 is always attained at zero, and all-rank zero-terminal optimality is settled within this observer. Equivalent exact saving:
    B-k_p(0)=max_{A subset J} [r(G[U minus A])-|J minus A|].
The maximizing A can be nonunique. No saturation, fixed cycle rank, or bounded subdivision assumption is needed.

## 2. Independent local observation directions (Hall lemma)

Let W_i be subspaces of a finite-dimensional vector space L over F2 indexed by a finite set I. There exist independent representatives f_i in W_i for all i iff dim(sum_{i in A} W_i)>=|A| for every A subset I. Necessity follows by taking the independent representatives on A. Sufficiency by induction on |I|. Empty set trivial; one index follows from the dimension condition. If there is a proper nonempty tight A, apply induction on A to get independent representatives spanning T=sum_{i in A} W_i. For each B subset I minus A, the images of W_i in L/T span dimension dim(sum_{i in A union B} W_i)-dim T>=|B|. Induct in the quotient and lift the representatives; their union with the first set is independent. Otherwise all proper nonempty A have dimension at least |A|+1. Choose a nonzero representative for one index and quotient by its span. Every nonempty subset of the remaining indices is proper in I and loses at most one dimension, so induction again applies.

For arbitrary W_i define D=max_A(|A|-dim sum_{i in A}W_i). Extend L by a common auxiliary space E of dimension D, and replace each W_i by W_i direct sum E. For every nonempty A the rank increases by exactly D, so the Hall inequalities hold; choose |I| independent extended representatives. Projection back to L loses at most D independent directions. Select an independent subset of the projected representatives of size at least |I|-D. Conversely a subset with independent representatives misses at least |A|-dim(sum_A W_i) indices from every A, hence misses at least D. Thus the maximum number of independent representatives is exactly |I|-D. The common E is only a proof device in the dual space, not a native axis or a physical state.

Apply with L=K_U^* and W_i=im(projection_i^*) for i in J. The span dimension over A equals d(A), by duality of the simultaneous projection. Thus there is a subset I of J with |I|=|J|-D and independent f_i in W_i, each pulled back from a nonzero local linear functional ell_i on V_i.

## 3. Completion upper bound

Upgrade the D singleton vertices J minus I from S(1) to S(2) by adding one event at each. For any x in V_U, solve the equations
    f_i(z)=1+ell_i(x_i), i in I, z in K_U.
Independence makes the joint map onto F2^I, hence they have a simultaneous solution. This ensures ell_i(x_i+z_i)=1, so every singleton constraint x_i+z_i !=0 is satisfied. All other U coordinates are saturated and impose no condition. Therefore the augmented prefix covers the whole H. This proves directly that only D upgrades suffice to fill H, with no enumeration of the 4^|U| local states.

For exterior A0=V(G) minus U, the quotient Q/H is V_A0 / projection_A0 K, dimension F-h. By the ordered rank-release construction of R770 (valid for any linear kernel for the upper bound), an inventory on A0 of cost F-h covers this quotient. Adding it to a prefix already covering H covers Q. The two augmentation supports are disjoint. Local sums S(a)+S(b)=S(min(a+b,2)) justify ordinary inventory addition including S(1)+S(1)=V_i. Thus C(p)<=F-h+D.

## 4. Fixed zero reserve and matching lower bound

Pick A subset J attaining D. For each i in A reserve one event, outside U reserve zero. On G[U minus A] choose the universal full-cover reserve from R770 of cost 2(|U|-|A|)-r(G[U minus A]). Extend corrections by zero on A and outside U: any cycle on this induced graph is a cycle in G. Hence every original x is corrected into this fixed reserve: x_i remains unchanged and nonzero on A, unchanged zero outside U, and on U minus A the full-cover construction handles arbitrary local x_i. Total cost is
    |A|+2(|U|-|A|)-r(G[U minus A])
    = h-(|A|-d(A)) = h-D.
This supplies k_p(0)<=h-D.

For any feasible t and any augmentation a that completes the full quotient, q(P(t))+q(P(a)) is full (by inclusion and translation). Its truncated inventory costs at most sum t_i+sum a_i, which by R770 is at least F. Thus k_p(q(w))>=F-C(p)>=h-D for every w. Combined with the fixed zero reserve, this proves every asserted equality, including C(p)=F-h+D. All empty and disconnected cases are covered.

## 5. Structural consequences and interpretation

R772's joint saturation criterion on all positive-stock singleton vertices is sharpened to the exact condition D=0. Necessity follows because C(p) inside G[U] is D (set U to whole vertex set there); sufficiency follows from the independent direction construction. For a set with no zero-rank singleton, joint saturation can fail even though each projection individually has rank one or two: D measures the worst shared rank shortage, not a sum of independent local ranks. In R772's prior case J0 independent zero-rank indices and saturated J1, D=|J0|. For no singletons D=0. For a simple cycle, m singleton vertices on the full occupied cycle give D=max(m-1,0). The formula is valid for all ranks, including rank 4 and above with arbitrary subdivisions. This resolves the open question in R772 and general graphic zero-terminal optimality left open by R770. The abstract R764 non-graphic counterexample is unaffected: the lower bound relies on R770's graphic sharp full-cover theorem and graphic induced restrictions.

For algorithmic use, computing D via the maximum independent partial transversal of the local dual subspaces (each has at most three nonzero vectors) is a linear matroid/partition constraint problem. An explicit polynomial implementation and cost accounting are not claimed in this note; the displayed subset formula and rank-release construction already give exact finite procedures. For a chosen maximizing A, the reserve is constructive and correction can be recovered without inspecting arbitrary terminal distributions. This preserves only the Boolean reserve-cost observation and feasibility at the stated target; the full weighted/signed, ordered, provenance-sensitive, native common-depth carrier remains separate.

## 6. Actual exact cross-check

Executed JavaScript BigInt quotient masks, using even edge-mask enumeration for K, Gaussian elimination for quotient coordinates, all truncated prefix/suffix inventories for each graph, independent graph-component computation of r(G[U]) and subset formula for D. For each prefix computed C separately as the minimum incremental cost among all full-cover inventories; checked all cheaper t have no feasible terminal, and at predicted cost found a zero-terminal witness. Counts below are per specified graph, not enumeration of all graphs; the analytic proof is unbounded.

[
  {
    "n": 1,
    "r": 0,
    "prefixes": 3,
    "terminals": 12,
    "positiveDeficit": 1,
    "maxDef": 1,
    "completionSum": 3
  },
  {
    "n": 2,
    "r": 0,
    "prefixes": 9,
    "terminals": 144,
    "positiveDeficit": 5,
    "maxDef": 2,
    "completionSum": 18
  },
  {
    "n": 2,
    "r": 1,
    "prefixes": 9,
    "terminals": 72,
    "positiveDeficit": 3,
    "maxDef": 1,
    "completionSum": 10
  },
  {
    "n": 2,
    "r": 2,
    "prefixes": 9,
    "terminals": 36,
    "positiveDeficit": 2,
    "maxDef": 1,
    "completionSum": 4
  },
  {
    "n": 3,
    "r": 1,
    "prefixes": 27,
    "terminals": 864,
    "positiveDeficit": 16,
    "maxDef": 2,
    "completionSum": 55
  },
  {
    "n": 4,
    "r": 1,
    "prefixes": 81,
    "terminals": 10368,
    "positiveDeficit": 59,
    "maxDef": 3,
    "completionSum": 246
  },
  {
    "n": 4,
    "r": 3,
    "prefixes": 81,
    "terminals": 2592,
    "positiveDeficit": 39,
    "maxDef": 2,
    "completionSum": 102
  },
  {
    "n": 5,
    "r": 3,
    "prefixes": 243,
    "terminals": 31104,
    "positiveDeficit": 156,
    "maxDef": 3,
    "completionSum": 523
  },
  {
    "n": 6,
    "r": 4,
    "prefixes": 729,
    "terminals": 186624,
    "positiveDeficit": 483,
    "maxDef": 4,
    "completionSum": 1581
  },
  {
    "n": 6,
    "r": 4,
    "prefixes": 729,
    "terminals": 186624,
    "positiveDeficit": 489,
    "maxDef": 4,
    "completionSum": 1595
  }
]

Executable code used (run verify() and print result):
```javascript
function verify(){
const S=[[0],[1,2,3],[0,1,2,3]];
const graphs=[[1,[]],[2,[[0,1]]],[2,[[0,1],[0,1]]],[2,[[0,1],[0,1],[0,1]]],[3,[[0,1],[1,2],[2,0]]],[4,[[0,1],[1,2],[2,0],[2,3]]],[4,[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]],[5,[[0,4],[4,1],[0,2],[0,3],[1,2],[1,3],[2,3]]],[6,Array.from({length:9},(_,i)=>[Math.floor(i/3),3+i%3])],[6,[[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[0,3],[1,4],[2,5]]]];
let rows=[];
for(const [n,E] of graphs){
const inc=Array.from({length:n},()=>[]);E.forEach(([u,v],i)=>{inc[u].push(i);inc[v].push(i)});
const pop=x=>{let c=0;while(x){x&=x-1;c++}return c};
const K=[];
for(let m=0;m<(1<<E.length);m++){let z=0,ok=true;for(let i=0;i<n;i++){let a=0;inc[i].forEach((e,j)=>a|=((m>>e)&1)<<j);if(pop(a)%2){ok=false;break}z|=(a&3)<<(2*i)}if(ok)K.push(z)}
const piv=Array(2*n).fill(0);
for(let z of K)for(let b=2*n-1;b>=0;b--)if(z>>b&1){if(piv[b])z^=piv[b];else{piv[b]=z;break}}
const free=piv.map((x,i)=>x?-1:i).filter(i=>i>=0),r=2*n-free.length,Q=1<<free.length,full=(1n<<BigInt(Q))-1n;
function q(z){for(let b=2*n-1;b>=0;b--)if((z>>b&1)&&piv[b])z^=piv[b];return free.reduce((a,b,i)=>a|(((z>>b)&1)<<i),0)}
const masks=free.map((_,b)=>{let m=0n;for(let x=0;x<Q;x++)if(!(x>>b&1))m|=1n<<BigInt(x);return m});
function shift(s,x){while(x){let k=x&-x,m=masks[Math.log2(k)],b=BigInt(k);s=((s&m)<<b)|((s&~m)>>b);x^=k}return s}
const types=Array.from({length:3**n},(_,j)=>{let p=Array.from({length:n},()=>{let a=j%3;j=Math.floor(j/3);return a});let m=1n;p.forEach((a,i)=>{let v=0n;for(let x of S[a])v|=shift(m,q(x<<(2*i)));m=v});return {p,m,c:p.reduce((a,b)=>a+b,0)}});
const costs=[...types].sort((a,b)=>a.c-b.c),fulltypes=types.filter(t=>t.m===full);
function rank(U){let k=0,vs=0,edges=0,par=Array.from({length:n},(_,i)=>i);const root=i=>{while(par[i]!==i)i=par[i];return i};for(let i=0;i<n;i++)if(U>>i&1){vs++;k++}for(let [u,v] of E)if((U>>u&1)&&(U>>v&1)){edges++;let a=root(u),b=root(v);if(a!==b){par[a]=b;k--}}return edges-vs+k}
let comparisons=0,defects=0,completionSum=0,maxDef=0;
for(const {p,m} of types){
 let U=0,J=0;for(let i=0;i<n;i++){if(p[i])U|=1<<i;if(p[i]===1)J|=1<<i}
 let rU=rank(U),h=2*pop(U)-rU,D=0;
 for(let A=J;;A=(A-1)&J){D=Math.max(D,pop(A)-rU+rank(U^A));if(!A)break}
 let want=h-D,wantC=2*n-r-want;
 let C=Math.min(...fulltypes.map(t=>t.p.reduce((s,b,i)=>s+Math.max(0,b-p[i]),0)));
 if(C!==wantC)throw Error(JSON.stringify({n,E,p,C,wantC}));
 let xs=[];for(let x=0;x<Q;x++)if((m>>BigInt(x))&1n)xs.push(x);
 let zero=false;
 for(const t of costs){if(t.c>want)break;let a=full;for(const x of xs){a&=shift(t.m,x);if(!a)break}if(t.c<want&&a)throw Error("lower "+JSON.stringify({n,E,p,want,t:t.p}));if(t.c===want&&(a&1n)){zero=true;break}}
 if(!zero)throw Error("upper "+JSON.stringify({n,E,p,want}));
 comparisons+=Q;defects+=D>0?1:0;completionSum+=C;maxDef=Math.max(maxDef,D);
}
rows.push({n,r,prefixes:types.length,terminals:comparisons,positiveDeficit:defects,maxDef,completionSum});
}
return rows;
}
console.log(JSON.stringify(verify(),null,2));
```

## 7. Next scientific question

The all-rank minimum over terminal and completion duality are solved. Next determine the full target-dependent reserve spectrum k_p(q(w)), especially whether the same deficiency framework gives a polynomial constructive formula for nonzero target lifts, and isolate which native signed/weighted/ordered observations can or cannot inherit this Boolean certificate. No new theorem admission or shared task completion asserted.
