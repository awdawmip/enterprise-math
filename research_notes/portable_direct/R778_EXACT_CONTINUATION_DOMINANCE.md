# R778 — Exact continuation dominance and sharp three-cut distinguishing contexts

2026-11-25. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, no shared Task claim. Predecessor R777, 9b61a7108eb3e9c847743688079429aadb2590ad:research_notes/portable_direct/R777_SEPARATOR_BOUNDARY_ANTICHAIN_RESERVE.md. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 retained; P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint relation observer contract blob 3923890d77a02d84b772f789e6912dd14f220d14 read at pin. Generated foundation package at that pin returned 404; current ACTIVE worldview and applicable continuation, portable, account mathematical, BRC and residual policies read. Scope is the Boolean auxiliary Port observer, not the native signed BRC, provenance, time or common-depth observer. Own session metadata read r3-20261125-0320-own-metadata-v1 confirmed registered MCP-ec17f2f30fb8409f8e664eb29ae6c08c, no runs, execution_authorized=false. Owner inventory original r3-20261125-0320-owner-read-v1 last read RUNNING at time of proof publication; no claim mutation.

## 1. Exact dominance theorem

Use the R777 model: finite loop-free subcubic multigraph, each vertex completed to three ports by private ports, local even binary triples V_v, cycle kernel K with equal edge bits and zero private bits. S(0)={0}, S(1)=V_v minus {0}, S(2)=V_v. For a fixed reserve t_X and target representative w_X, actual prefix x_X ranges independently in product S(p_v). Its extendible boundary assignments L_X(x_X,t_X) form a subset of the even boundary universe Q=B_X. The state is the nonempty inclusion-minimal family A=Min{L_X(x_X,t_X)}. Any family containing the empty set is infeasible and discarded.

For two feasible antichains A,B on the same labeled Q, write A >= B if every a in A contains some b in B. Define the exterior test T_A(E) as 1 iff every a in A intersects E, for E subset Q. Then

    A >= B iff T_B(E) <= T_A(E) for every E subset Q.

Proof: if each a contains a b, any E hitting all b hits all a. Conversely, if some a contains no b, take E=Q minus a. Every b intersects E, but a is disjoint. This is a constructive separating test. For antichains mutual dominance implies equality: from a in A select b subset a and a' subset b; minimality in A implies a'=a=b. Symmetry gives equality. Thus distinct antichains have different continuation predicates in the universe of arbitrary exterior test sets, and the predicate or its minimal hitting sets is an alternative lossless representation of the same observer. The result concerns labeled states, not unlabeled cardinalities.

## 2. Dominance survives arbitrary future separator composition

For R777's join/projection J, if a contains b then J(a,c) contains J(b,c) for any c; this follows directly from matching the same shared edge assignments. If A >= B then each J(a,c) contains J(b,c). Removing supersets on either side does not change dominance: each element contains an inclusion-minimal member. Hence

    Min{J(a,c): a in A,c in C} >= Min{J(b,c): b in B,c in C}.

The property holds through every sequence or binary tree of future joins, including impossible families with the natural bottom element. At the root (singleton boundary universe), feasibility is preserved in the improving direction. With disjoint independent prefix populations and additive nonnegative local costs, a partial reserve with state A and cost c_A <= c_B can replace any reserve B dominated by A. The exterior reserve can be reused unchanged, and a witness for every actual prefix is recovered using the retained reserve's R777 traceback. The replacement is an optimization dominance, not a claim that the original reserve's actual prefix-to-lift mapping is identical. The minimum global cost is unchanged by deleting dominated entries after each merge. Equal families retain their cheapest representative first; strict distinct-state dominance has no cycles. At a given price, more flexible states dominate less flexible ones. At different prices a cheaper weak state and more expensive strong state can both be necessary.

## 3. Actual graphic separating tests on a connected three-edge cut

For a region with one connected component touching exactly three cut edges, Q consists of 000,011,101,110, indexed in that order. Every nonempty subset E of Q is realizable by a fixed-reserve, zero-prefix exterior in the same graph model. All exterior w are even triples, private z bits remain zero, and edges retain their labels.

* Size 4: one exterior vertex meeting the three cut edges, p=0,t=2.
* Size 3: same vertex p=0,t=1, set w to the excluded even triple; the remaining three are accepted.
* Size 1: same vertex p=0,t=0, set w to the selected triple.
* Size 2: any pair of distinct even triples agrees on exactly one bit e. Subdivide that exterior port by a degree-two vertex u, with its third port private. At the center use p=0,t=2. At u use p=0,t=0, and set w to (b,b,0) in the two incident edge ports and private port, where b is the shared bit value. Equality forces both those edges to b. The center parity then permits exactly the desired pair. Every one of the six pairs is obtained.

If dominance fails, E=Q minus a is nonempty (all b are nonempty and none is contained in a), and is one of the 15 above; the exterior has one actual prefix. Thus the dominance test is necessary as well as sufficient for universal fixed-reserve substitution across all actual graphic continuations attached to a connected three-edge interface. In particular, any two distinct attainable antichains on this cut are distinguished by an actual graphic continuation in at least one direction. This does not assert that every one of the 166 abstract feasible antichains is attainable by an interior graph. The analogous claim for a connected two-edge cut follows from its universe {00,11}: a degree-two vertex with private port and t=0 fixes either point; t=2 permits both. A one-edge cut has a singleton even universe. For larger or disconnected cuts the general dominance rule is sufficient and exact for arbitrary set-valued exterior tests; realizability of all separating tests by actual graphs is not established.

## 4. Implementation and evidence

A feasible family is a nonempty antichain of nonempty subsets. On a four-label universe there are 166 such families. Enumerate all 2^15-1 nonempty families of nonempty subsets, filter by inclusion, compare every ordered pair with the analytic rule and all 16 test sets. For q=4 a 16-bit hit truth table is an optional representation: A>=B exactly when all true bits of B are true for A. It is not an unconditional memory improvement over the direct antichain. The 166 abstract states imply an 8-bit index suffices if a complete state table is precomputed, not that 8 bits are necessary for actual graphic interiors.

The second experiment implements the R777 exact sequential separator recurrence both with and without the new pruning. Eight graphs (theta, K4, K33, ladders of length 8,16,32,64,128) each receive 34 deterministic cases: all-saturated zero target, all-single zero target, and 32 sampled p in {0,1,2}, w in the four even triples, alpha in {0,1,2,3,4}. No independent exhaustive graph optimum is claimed here: the reference is the unpruned proven R777 recurrence. Exact BigInt masks; costs are small exact integers. Counts are candidate transition attempts, not measured wall-clock speed. Naive pairwise dominance pruning adds O(D^2 s^2) subset checks per merge for at most D families of size s; raw cut preprocessing and join costs remain as R777. Thus fewer transitions alone do not prove faster runtime. Store retained representatives and backpointers for output recovery; test code compares costs only. All assertions passed.

```json
{
  "families": 166,
  "pairs": 7246,
  "strict": 7080,
  "incomp": 13230,
  "queries": 440896,
  "gadgets": 15,
  "rows": [
    {
      "name": "theta",
      "n": 2,
      "checks": 34,
      "peakBefore": 3,
      "peakAfter": 3,
      "attemptBefore": 408,
      "attemptAfter": 360,
      "removed": 16
    },
    {
      "name": "K4",
      "n": 4,
      "checks": 34,
      "peakBefore": 15,
      "peakAfter": 9,
      "attemptBefore": 2223,
      "attemptAfter": 1422,
      "removed": 169
    },
    {
      "name": "K33",
      "n": 6,
      "checks": 34,
      "peakBefore": 58,
      "peakAfter": 55,
      "attemptBefore": 11196,
      "attemptAfter": 6162,
      "removed": 644
    },
    {
      "name": "ladder8",
      "n": 16,
      "checks": 34,
      "peakBefore": 9,
      "peakAfter": 9,
      "attemptBefore": 7167,
      "attemptAfter": 5001,
      "removed": 352
    },
    {
      "name": "ladder16",
      "n": 32,
      "checks": 34,
      "peakBefore": 9,
      "peakAfter": 9,
      "attemptBefore": 15345,
      "attemptAfter": 10467,
      "removed": 811
    },
    {
      "name": "ladder32",
      "n": 64,
      "checks": 34,
      "peakBefore": 9,
      "peakAfter": 9,
      "attemptBefore": 32352,
      "attemptAfter": 21429,
      "removed": 1740
    },
    {
      "name": "ladder64",
      "n": 128,
      "checks": 34,
      "peakBefore": 9,
      "peakAfter": 9,
      "attemptBefore": 66195,
      "attemptAfter": 43635,
      "removed": 3539
    },
    {
      "name": "ladder128",
      "n": 256,
      "checks": 34,
      "peakBefore": 9,
      "peakAfter": 9,
      "attemptBefore": 133158,
      "attemptAfter": 87822,
      "removed": 7100
    }
  ]
}
```

Node.js reproduction (no dependencies):
```javascript
function verify(){
 const subsets=(a,b)=>(a&b)===a, minfam=xs=>{let a=[...new Set(xs)];return a.filter(x=>!a.some(y=>y!==x&&subsets(y,x))).sort((x,y)=>x<y?-1:x>y?1:0)};
 const better=(a,b)=>a.every(x=>b.some(y=>subsets(y,x)));
 const hit=(a,e)=>a.every(x=>(x&e)!==0n);
 const F=[];for(let k=1;k<32768;k++){let a=[];for(let j=1;j<16;j++)if(k&(1<<(j-1)))a.push(BigInt(j));if(minfam(a).length===a.length)F.push(a)}
 let pairs=0,strict=0,incomp=0,queries=0;for(const a of F)for(const b of F){const d=better(a,b);let semantic=true;for(let m=0;m<16;m++){queries++;if(hit(b,BigInt(m))&&!hit(a,BigInt(m)))semantic=false}if(d!==semantic)throw Error("dominance");if(d){pairs++;if(a!==b)strict++}else if(!better(b,a))incomp++}
 const even=[0,3,5,6],S=[[0],[1,2,3],[0,1,2,3]],bit=i=>1n<<BigInt(i);
 const realized=new Set();
 for(let t=0;t<=2;t++)for(let w=0;w<4;w++){let m=0;for(let j=0;j<4;j++)if(S[t].includes(j^w))m|=1<<j;realized.add(m)}
 for(let e=0;e<3;e++)for(let b=0;b<2;b++){let m=0;for(let j=0;j<4;j++)if(((even[j]>>e)&1)===b)m|=1<<j;realized.add(m)}
 if(realized.size!==15||realized.has(0))throw Error("gadget");
 function graph(n,E){return {n,E,inc:Array.from({length:n},(_,v)=>E.flatMap((e,j)=>e.includes(v)?[j]:[]))}}
 function prep(G){let cut=[],steps=[];for(let v=0;v<G.n;v++){const I=G.inc[v],u=[...new Set([...cut,...I])],next=u.filter(e=>!(cut.includes(e)&&I.includes(e)));const pick=(x,A)=>A.reduce((s,e,j)=>s|(((x>>u.indexOf(e))&1)<<j),0);const triples=Array.from({length:2**u.length},(_,x)=>[bit(pick(x,cut)),bit(pick(x,I)),bit(pick(x,next))]);const local=Array.from({length:3},(_,p)=>Array.from({length:4},(_,w)=>Array.from({length:3},(_,t)=>minfam(S[p].map(x=>{let m=0n;for(let b=0;b<2**I.length;b++){let j=even.indexOf(b);if(j>=0&&S[t].includes(x^w^j))m|=bit(b)}return m})))));steps.push({v,triples,local});cut=next}return steps}
 function solve(P,p,w,alpha,prune){let dp=[{a:[1n],c:0}],peak=1,attempts=0,retained=0,removed=0;for(const {v,triples,local} of P){let next=new Map(),cache=new Map();function join(a,b){let key=a+","+b;if(cache.has(key))return cache.get(key);let m=0n;for(const [x,y,z] of triples)if((a&x)&&(b&y))m|=z;cache.set(key,m);return m}for(const {a,c} of dp)for(let t=0;t<3;t++){attempts++;let f=local[p[v]][w[v]][t];if(f[0]===0n)continue;let h=minfam(a.flatMap(x=>f.map(y=>join(x,y))));if(h[0]===0n)continue;let key=h.join(","),nc=c+alpha[v]*t;if(!next.has(key)||next.get(key).c>nc)next.set(key,{a:h,c:nc})}let arr=[...next.values()];dp=prune?arr.filter(x=>!arr.some(y=>x!==y&&y.c<=x.c&&better(y.a,x.a))):arr;removed+=arr.length-dp.length;retained+=dp.length;peak=Math.max(peak,dp.length)}if(dp.length!==1||dp[0].a.join(",")!=="1")throw Error("root");return {cost:dp[0].c,peak,attempts,retained,removed}}
 const ladder=L=>graph(2*L,[...Array.from({length:L},(_,i)=>[2*i,2*i+1]),...Array.from({length:L-1},(_,i)=>[2*i,2*i+2]),...Array.from({length:L-1},(_,i)=>[2*i+1,2*i+3])]);
 let seed=778;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return Math.floor(seed/4294967296*n)};
 const cases=[["theta",graph(2,[[0,1],[0,1],[0,1]])],["K4",graph(4,[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]])],["K33",graph(6,[0,1,2].flatMap(i=>[3,4,5].map(j=>[i,j])))],... [8,16,32,64,128].map(L=>["ladder"+L,ladder(L)])];
 let rows=[];for(let [name,G] of cases){let n=G.n,P=prep(G),row={name,n,checks:0,peakBefore:0,peakAfter:0,attemptBefore:0,attemptAfter:0,removed:0};for(let k=0;k<34;k++){let p=k===0?Array(n).fill(2):k===1?Array(n).fill(1):Array.from({length:n},()=>rnd(3)),w=k<2?Array(n).fill(0):Array.from({length:n},()=>rnd(4)),alpha=k<2?Array(n).fill(1):Array.from({length:n},()=>rnd(5));let a=solve(P,p,w,alpha,false),b=solve(P,p,w,alpha,true);if(a.cost!==b.cost)throw Error("cost");row.checks++;row.peakBefore=Math.max(row.peakBefore,a.peak);row.peakAfter=Math.max(row.peakAfter,b.peak);row.attemptBefore+=a.attempts;row.attemptAfter+=b.attempts;row.removed+=b.removed}rows.push(row)}
 return {families:F.length,pairs,strict,incomp,queries,gadgets:realized.size,rows};
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next

Investigate which antichains really occur at a connected three-edge cut and the minimal exact state catalog under graphic realizability. For larger cuts, characterize attainable exterior tests rather than assuming arbitrary relations can be realized. Compare dominance implementation cost against saved transitions; use bounded cut widths, not global cycle rank, as the computational parameter. Keep signed amplitude, branch provenance, event order and common depth in their distinct observers. No mathematical admission or formal task closure claimed.
