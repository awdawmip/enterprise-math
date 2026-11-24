# R776 — Exact robust terminal spectrum by joint-lift antichain descent

2026-11-25. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED.
Continuation of R775 at fba02cd0763bb30ef7a94ba02b053d1aadcac6a9:research_notes/portable_direct/R775_RANK1_COMPLETE_TARGET_SPECTRUM.md and R774 at b96e1401092ff2081dd239ba1583253e4b7191b2:research_notes/portable_direct/R774_SYNDROME_T_JOIN_POINT_RESERVE.md. Scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged. Frozen P000 V5 (dc84bdae6595b5e237a2ad50d8b21916adb2e447) and joint-relation contract (3923890d77a02d84b772f789e6912dd14f220d14) read; ACTIVE worldview, portable and continuation protocols and account policies consulted. Generated foundation startup at pin returned 404. Own recovery metadata r3-20261125-0120-own-metadata-v1 shows prior registration SUCCEEDED, no runs, execution_authorized=false. Owner inventory r3-20261125-0120-owner-read-v1 last observed RUNNING before derivation; independent portable unit only, no shared claim or Result.

## 1. Exact arbitrary-rank theorem

Retain R775's auxiliary Boolean model: V_i=F2^2, S(0)={0}, S(1)=V_i minus {0}, S(2)=V_i, P(p)=product S(p_i), K a linear subspace of product V_i, q the quotient map. The graphic case uses the cycle kernel of a finite loop-free subcubic multigraph. For target representative w and nonnegative vertex prices alpha_i, k_p^alpha(w) is the least sum alpha_i t_i over t in {0,1,2}^n satisfying q(P(p))+q(w) subset q(P(t)). This is fixed reserve with forall-prefix exists-lift quantifiers, not pointwise adaptive optimization.

Let B be the labelled set K of N=2^r lift states; K basis and local projections pi_i are retained. For each local reserve t define
    L_i(x,t)={z in B: x+w_i+pi_i(z) in S(t)}, x in S(p_i).
For any finite nonempty family F of subsets of B let min(F) delete duplicates and strict supersets. Define
    A_i(t)=min({L_i(x,t): x in S(p_i)}).
For two nonempty antichains define
    A * C = min({a intersect c: a in A, c in C}).
The absorbing infeasible state is {empty}. The identity is {B}. A reserve is universally feasible iff its product A_1(t_1)*...*A_n(t_n) does not contain empty.

Proof: For fixed prefix x, compatible lifts are exactly the intersection of the local sets; a prefix is impossible iff this intersection is empty. If a subset a is deleted in favour of a' contained in a, then a' intersect c is contained in a intersect c for every future constraint c; the deleted set cannot add a new inclusion-minimal intersection. More formally every member of a finite nonempty family contains a minimal member, so min(F intersect-pair G)=min(min(F) intersect-pair min(G)). Iterating proves the exact product representation of the minimal compatible-lift families for all prefix choices. Thus * is associative and commutative, with stated identity and absorbing failure. Failure iff empty belongs to the minimal family, and a failure cannot become feasible after adding more sites. This proves descent for every future appended site in this observer, with all lift labels retained. The antichain is a sufficient statistic for future fixed-reserve feasibility, not for signed, ordered, multiplicity, native amplitude, provenance or common-depth data. Preserve original projections/local inputs and traceback for recovery.

## 2. Exact cost recurrence and complexity

Initialize cost({B})=0, all other states infinity. For each site i, for each feasible state A and reserve t=0,1,2, compute H=A*A_i(t); if H is feasible, relax newcost(H) with cost(A)+alpha_i t. Minimum over final states is k_p^alpha(w). Induction: each state stores the cheapest partial reserve with exactly that minimal family; future feasibility is identical for equal states by section 1, so cheaper partial reserve dominates more expensive ones. Every possible reserve is covered, and no infeasible reserve is accepted. Backpointers recover a minimizing reserve, then for any actual prefix choose any lift in the intersection and obtain its compensation. Representative change by a kernel vector permutes all lift labels consistently, preserving the result.

For fixed rank r this is linear in n arithmetic/comparison steps with a rank-dependent finite constant; computing a cycle basis/local projection labels and a legal w lift is separate preprocessing (R774 supplies linear-time lift recovery given syndrome, a spanning forest gives a fundamental cycle basis in O(n+m+nr) explicit projection work). A generic upper bound is the Dedekind number M(N)-2 feasible nonempty antichains (exclude the empty family and {empty}); each has at most binomial(N,floor(N/2)) masks. A direct transition computes at most four times that many intersections, each with N bits, then checks pairwise subset relations. This is a fixed-parameter exact algorithm in rank, not a polynomial-in-r claim. Memory for cost values is two state layers; traceback O(n times number of states). Arithmetic cost depends on weight representation, exact integer weights used in the experiment. On bridge-separated blocks K is a direct sum on disjoint vertex sets in a subcubic graph (a bridge has zero cycle coordinate; degree <=3 prevents a vertex belonging to two disjoint cyclic blocks). Use independent minima and rank per block; retain bridge half-port values when factoring the local target. No numerical runtime speed benchmark claimed.

## 3. Rank two: exact 67-state table

For r=2, label the four lifts (0,0),(1,0),(0,1),(1,1). A local linear map has form [0,a,b,a xor b], a,b in {0,1,2,3}. Thus all possible local types are exhausted by 16 maps times three prefix stocks times four targets times three reserves. For each type compute the inclusion-minimal family of four-bit allowed masks; discard {0}. There are exactly 28 distinct feasible local types. Starting from {15}, close under * with these types, discarding failure. The reproducible finite closure below gives exactly 67 feasible reachable states, distributed by antichain cardinality 1:15, 2:33, 3:16, 4:2, 6:1. This is exact for arbitrary abstract rank-two local-map sequences, an upper bound for a constrained graphic topology. It replaces the generic 166-state bound. Closure is a finite exhaustive certificate: all local inputs are listed by loops; new states are visited until the growing list is exhausted; each transition is exact bitwise intersection and subset minimization. Every state visited has a sequence witness by construction, and closure contains every feasible finite sequence by induction. Store the transition table once (67 by 28), and optimize by at most 201 table lookups per site, plus local type lookup and exact weight arithmetic. Arbitrary-length theta graphs now have an exact full target spectrum algorithm with this bound, including weights and zero prices. Rank one R775 has a faster specialized closed formula and need not be replaced.

## 4. Small obstruction certificate, all ranks

A fixed reserve fails iff there exists a set of at most N distinct sites and one local prefix choice at each of them whose allowed-lift intersection is empty. Necessity: from any failing full prefix, for each lift z choose one site rejecting z; retain the union of chosen sites and their actual prefix values (consistent even when a site is selected repeatedly). Sufficiency: extend these choices to an arbitrary complete prefix, possible since S(p_i) nonempty. No lift can survive. This generalizes R775's two-label conflict; it is a bound on the number of sites in an obstruction, not a replacement for the jointly labelled masks or an assertion that every set of N sites fails. It offers a separate certificate and potential separation algorithm for higher rank.

## 5. Exact independent check

Seven theta path-interior count profiles [0,0,0], [1,0,0], [2,0,0], [1,1,0], [3,0,0], [2,1,0], [1,1,1], representing two degree-three endpoints (rank-two maps [1,2]) joined by three paths, with intermediate projections [1,0], [0,1], [1,1] respectively. Local invertible labels may be chosen independently since S(p) is invariant. All 3^n inventories and all 4^(n-1) quotient targets: representatives have first endpoint coordinate zero, unique because the first projection is bijective. Direct checker builds saturated lifted masks P(t)+K independently and checks translated inclusion for every candidate reserve in ascending cost order. Compare to the finite-state cost recurrence for uniform and deterministic nonuniform prices, also zero prices for n<=4. Exact integer arithmetic and BigInt bitsets; no numerical tolerance. Results:

```json
{
  "localTypes": 28,
  "states": 67,
  "bySize": {
    "1": 15,
    "2": 33,
    "3": 16,
    "4": 2,
    "6": 1
  },
  "total": 405756,
  "rows": [
    {
      "counts": [
        0,
        0,
        0
      ],
      "n": 2,
      "alpha": [
        1,
        1
      ],
      "checks": 36,
      "peak": 6
    },
    {
      "counts": [
        0,
        0,
        0
      ],
      "n": 2,
      "alpha": [
        1,
        2
      ],
      "checks": 36,
      "peak": 6
    },
    {
      "counts": [
        0,
        0,
        0
      ],
      "n": 2,
      "alpha": [
        0,
        1
      ],
      "checks": 36,
      "peak": 6
    },
    {
      "counts": [
        1,
        0,
        0
      ],
      "n": 3,
      "alpha": [
        1,
        1,
        1
      ],
      "checks": 432,
      "peak": 12
    },
    {
      "counts": [
        1,
        0,
        0
      ],
      "n": 3,
      "alpha": [
        1,
        2,
        3
      ],
      "checks": 432,
      "peak": 12
    },
    {
      "counts": [
        1,
        0,
        0
      ],
      "n": 3,
      "alpha": [
        0,
        1,
        2
      ],
      "checks": 432,
      "peak": 12
    },
    {
      "counts": [
        2,
        0,
        0
      ],
      "n": 4,
      "alpha": [
        1,
        1,
        1,
        1
      ],
      "checks": 5184,
      "peak": 15
    },
    {
      "counts": [
        2,
        0,
        0
      ],
      "n": 4,
      "alpha": [
        1,
        2,
        3,
        1
      ],
      "checks": 5184,
      "peak": 15
    },
    {
      "counts": [
        2,
        0,
        0
      ],
      "n": 4,
      "alpha": [
        0,
        1,
        2,
        0
      ],
      "checks": 5184,
      "peak": 15
    },
    {
      "counts": [
        1,
        1,
        0
      ],
      "n": 4,
      "alpha": [
        1,
        1,
        1,
        1
      ],
      "checks": 5184,
      "peak": 18
    },
    {
      "counts": [
        1,
        1,
        0
      ],
      "n": 4,
      "alpha": [
        1,
        2,
        3,
        1
      ],
      "checks": 5184,
      "peak": 18
    },
    {
      "counts": [
        1,
        1,
        0
      ],
      "n": 4,
      "alpha": [
        0,
        1,
        2,
        0
      ],
      "checks": 5184,
      "peak": 18
    },
    {
      "counts": [
        3,
        0,
        0
      ],
      "n": 5,
      "alpha": [
        1,
        1,
        1,
        1,
        1
      ],
      "checks": 62208,
      "peak": 15
    },
    {
      "counts": [
        3,
        0,
        0
      ],
      "n": 5,
      "alpha": [
        1,
        2,
        3,
        1,
        2
      ],
      "checks": 62208,
      "peak": 15
    },
    {
      "counts": [
        2,
        1,
        0
      ],
      "n": 5,
      "alpha": [
        1,
        1,
        1,
        1,
        1
      ],
      "checks": 62208,
      "peak": 21
    },
    {
      "counts": [
        2,
        1,
        0
      ],
      "n": 5,
      "alpha": [
        1,
        2,
        3,
        1,
        2
      ],
      "checks": 62208,
      "peak": 21
    },
    {
      "counts": [
        1,
        1,
        1
      ],
      "n": 5,
      "alpha": [
        1,
        1,
        1,
        1,
        1
      ],
      "checks": 62208,
      "peak": 22
    },
    {
      "counts": [
        1,
        1,
        1
      ],
      "n": 5,
      "alpha": [
        1,
        2,
        3,
        1,
        2
      ],
      "checks": 62208,
      "peak": 22
    }
  ]
}
```

Reproduce with Node.js:
```javascript
function verify(){
 const S=[[0],[1,2,3],[0,1,2,3]];
 function mf(a){a=[...new Set(a)].sort((a,b)=>a-b);return a.filter(x=>!a.some(y=>y!==x&&(x&y)===y))}
 function local(a,b,p,w,t){const v=[0,a,b,a^b];return mf(S[p].map(x=>v.reduce((m,z,j)=>m|(S[t].includes(x^w^z)?1<<j:0),0)))}
 const types=new Map();
 for(let a=0;a<4;a++)for(let b=0;b<4;b++)for(let p=0;p<3;p++)for(let w=0;w<4;w++)for(let t=0;t<3;t++){let f=local(a,b,p,w,t);if(!f.includes(0))types.set(f.join(","),f)}
 const states=[[15]],idx=new Map([["15",0]]), ts=[...types.values()], ti=new Map(ts.map((f,i)=>[f.join(","),i])),trans=[];
 for(let i=0;i<states.length;i++){let f=states[i];trans[i]=ts.map(g=>{let h=mf(f.flatMap(x=>g.map(y=>x&y)));if(h.includes(0))return -1;let k=h.join(",");if(!idx.has(k)){idx.set(k,states.length);states.push(h)}return idx.get(k)})}
 const ltab=Array.from({length:4},(_,a)=>Array.from({length:4},(_,b)=>Array.from({length:3},(_,p)=>Array.from({length:4},(_,w)=>Array.from({length:3},(_,t)=>ti.get(local(a,b,p,w,t).join(","))??-1)))));
 const cases=[[0,0,0],[1,0,0],[2,0,0],[1,1,0],[3,0,0],[2,1,0],[1,1,1]],rows=[];
 for(const counts of cases){
  const maps=[[1,2],[1,2]];[[1,0],[0,1],[1,1]].forEach((m,j)=>{for(let i=0;i<counts[j];i++)maps.push(m)});
  const n=maps.length,N=4**n,Z=[0,0,0,0];for(let i=0;i<n;i++){let [a,b]=maps[i];[0,a,b,a^b].forEach((v,j)=>Z[j]|=v<<(2*i))}
  const bit=Array.from({length:N},(_,i)=>1n<<BigInt(i));
  const masks=Array.from({length:2*n},(_,b)=>{let m=0n;for(let x=0;x<N;x++)if(!(x&(1<<b)))m|=bit[x];return m});
  function shift(m,w){for(let b=0;b<2*n;b++)if(w&(1<<b)){let a=masks[b],d=BigInt(1<<b);m=((m&a)<<d)|((m&~a)>>d)}return m}
  const inv=Array.from({length:3**n},(_,j)=>{let p=[],xs=[0];for(let i=0;i<n;i++){let a=j%3;j=(j-a)/3;p.push(a);xs=xs.flatMap(x=>S[a].map(v=>x|(v<<(2*i))))}let m=0n;for(const x of xs)for(const z of Z)m|=bit[x^z];return {p,m}});
  const weights=[Array(n).fill(1),Array.from({length:n},(_,i)=>1+i%3)];if(n<=4)weights.push(Array.from({length:n},(_,i)=>i%3));
  for(const alpha of weights){
   const ordered=inv.map(t=>({...t,c:t.p.reduce((a,b,i)=>a+b*alpha[i],0)})).sort((a,b)=>a.c-b.c);
   let checks=0,peak=0;
   for(const {p,m} of inv)for(let w=0;w<N;w+=4){
    const target=shift(m,w),actual=ordered.find(u=>(target&u.m)===target).c;
    let dp=new Map([[0,0]]);
    for(let i=0;i<n;i++){let next=new Map(),[a,b]=maps[i],ls=ltab[a][b][p[i]][(w>>(2*i))&3];for(let [s,c] of dp)for(let t=0;t<3;t++){if(ls[t]<0)continue;let j=trans[s][ls[t]];if(j<0)continue;let nc=c+alpha[i]*t;if(nc<(next.get(j)??Infinity))next.set(j,nc)}dp=next;peak=Math.max(peak,dp.size)}
    let predicted=Math.min(...dp.values());if(actual!==predicted)throw Error(JSON.stringify({counts,p,w,alpha,actual,predicted}));checks++;
   }
   rows.push({counts,n,alpha,checks,peak});
  }
 }
 return {localTypes:ts.length,states:states.length,bySize:states.reduce((r,a)=>(r[a.length]=(r[a.length]??0)+1,r),{}),total:rows.reduce((a,b)=>a+b.checks,0),rows};
}
console.log(JSON.stringify(verify(),null,2));
```

## 6. Next question

Seek exact state reduction using graph separators / low-rank interfaces rather than total cycle rank. In particular, separate interior lift variables that no future vertex can observe, respecting the order forall local prefix, exists global lift. Investigate how the obstruction bound sharpens under graphic constraints and how optimal nonzero-terminal overhead compares to R773 and R774. This is an auxiliary unsigned boundary observer result; native signed BRC, path/event order, source provenance and three-dimensional slice common depth remain separate and are not inferred from it. No formal Result or independent review asserted.
