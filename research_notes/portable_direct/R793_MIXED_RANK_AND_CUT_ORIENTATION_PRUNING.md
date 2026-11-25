# R793 - Mixed rank envelope, canonical cuts and sharp prefix pruning

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R792_R791 / EXACT_JS_CHECKED / NOT_REVIEWED.
Independent portable continuation of own research Activity RA-708BCC309CE076D8BB599B91, EM-DIRECT-82A007 / TASK_RESEARCH. Own session recovery r3-20261125-1820-own-metadata-v1 verified existing registration and no runs, execution_authorized=false. Owner inventory r3-20261125-1820-owner-read-v1 last observed RUNNING; no shared claim or Task state changed. Frozen pin a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer contract read at that pin. Generated foundation package unavailable (404); relevant canonical inputs read directly. ACTIVE worldview and current applicable portable/continuation rules read. Global entries checked at main@3853d9c7c71e84c3ea3cb9e6f4f103b42dd86fad.

## 1. Population and scope

Reuse the exact same one-source network of R792:
6dcc39ca328ee24ca8493100a27cc1bf209b7446:research_notes/portable_direct/R792_SHARED_PORT_PREFIX_VERTEX_COVER.md.
For a simple graph G=(V,E), n=|V|, m=|E|>=1, let A={a_e:e in E} be its private labels and T=V disjoint union A. The m slots have actual independent ternary prefix choices: at the fixed cardinality m level in S=A xor D each slot admits private a_e and either endpoint u, endpoint v, or both. R792 proves these are actual local p=t=1 Port prefixes with fixed auxiliary target and reserve, and that the level is precisely a rank-m transversal matroid basis family M_x. The full network can have extra levels m+2j. Here the exterior has only the level-m states in this same twist, or the observer explicitly restricts to that level. No deletion of the other states from the full relation is asserted. R791 (96ddac0387d0c0dfd6c99aedc14612d143927f47:research_notes/portable_direct/R791_MINIMUM_RANK_ENVELOPE_AND_PREFIX_LOWER_BOUND.md) supplies the rank-envelope compatibility and distinguishability theorem for these typed relations. We reuse the classical matroid intersection theorem through R791, not claiming it as new.

## 2. Exact mixed envelope theorem

For U subset V and P subset E write A(P)={a_e:e in P}, W=U union A(P), and let G[U]-P mean the induced graph on U with edges belonging to P deleted. Then
    rho(W) = min_x r_x(W) = |P| + tau(G[U]-P).
This extends R792's P=empty formula to every mixed label direction, including those involving the private coordinates.

Proof. For any fixed prefix x, rank on W is maximum matching cardinality between slots and W. There is a maximum matching that assigns each slot e in P to a_e: if the slot was matched to another label, replace that edge with its private edge, without affecting other slots, and if it was unmatched add its private edge (contradicting maximal size). Since a_e has no other slot neighbor, these replacements do not interfere. Thus r_x(W)=|P| plus the maximum matching between slots outside P and allowed endpoint labels in U. Every edge of G[U]-P has at least one allowed endpoint. Select one such endpoint for each edge; distinct selected endpoints form a vertex cover, and each distinct endpoint can be matched to a distinct choosing slot. This gives the lower bound tau(G[U]-P). For a minimum cover C choose, on every un-paid internal edge, its endpoint in C; on every un-paid edge meeting the complement of U choose outside U. These singleton choices are actual prefixes, and no other public labels in U are available to those slots, giving equality. Paid edges are arbitrary.

A query reduces to minimum vertex cover on a graph with at most n vertices and m edges. On a bipartite source graph all such queries are polynomial by the classical Konig matching equality, including private-label queries. On unrestricted graphs the existing R792 hardness remains. A minimizing prefix is recovered by the above choices. This does not claim efficient simultaneous optimization over all W.

## 3. Canonical cuts for arbitrary typed exteriors

Let N be any rank-m exterior matroid on T with a real level-m witness and the same twist. Write s for its rank and s* for the dual rank. For a public subset I define E[I]=edges with both endpoints in I, and Q_I=I union A(E[I]). Then the worst common-independent cardinality is exactly
    L = min_{I subset V} ( |E[I]| + s(T minus Q_I) ).
Equivalently, the worst deficit is
    m-L = max_{I subset V} ( |I| - s*(Q_I) ).
By R791 the robust Boolean gluing predicate is L=m. For a finite nonempty exterior family replace s by its pointwise minimum envelope; the first formula still holds and yields worst pair deficit. The second is valid with max over the corresponding exterior dual rank expressions, equivalently min of their dual ranks at Q_I.

Proof. The rank cut expression from R791 is min over U,P of |P|+tau(G[U]-P)+s(T minus (U union A(P))). Choose a minimum cover C and set I=U minus C; E[I] subset P. Removing C and A(P minus E[I]) from W increases the complementary exterior rank by at most |C|+|P minus E[I]|, by the unit Lipschitz property of matroid rank. Therefore the Q_I cut has objective at most that of W. Conversely every Q_I is a legitimate cut, with rho(Q_I)=|E[I]|. This proves equality. Dual rank identity s*(Q)=|Q|-m+s(T minus Q) gives the second formula. The min of same-rank ranks is also unit Lipschitz and monotone, so the first proof is valid for families. All minima are finite. A failing I recovers a genuine worst prefix via endpoint choices away from I for every crossing edge and a rank-cut witness for its exterior. In the family case choose an exterior attaining its envelope at the complementary cut. A compatible pair need not have a single common lift for all prefixes.

This replaces 2^(n+m) mixed cut directions by at most 2^n canonical public directions, after forming the slot model. Straight enumeration costs O(2^n (n+m+cost of an exterior rank query)), no exponential pre-expansion of interior prefixes. A fixed exterior rank oracle may be implemented via R789/R790 on its matching witness. Preprocessing and witness construction costs are additional. This is a bound on this algorithm, not a lower bound or a claim of universal polynomial optimization.

## 4. Sharp exact pruning of the actual prefix population

For each edge choose just one endpoint (the private label remains allowed); call this a singleton orientation, directing the edge toward the selected endpoint. Every such orientation is an actual prefix. A cut I is covered by an orientation when every edge crossing I is directed away from I. For any prefix (including both-endpoint choices), attaining rho(Q_I)=|E[I]| is equivalent to having no allowed public endpoint in I on an un-paid slot, hence precisely the same away-from-I condition on all crossing edges, now for every allowed endpoint. A two-endpoint choice can be refined to either singleton without increasing rank on any W; it retains every formerly attained minimum.

Claim: a subfamily of actual prefixes preserves the complete level-m envelope iff it covers every cut I. Necessity follows by observing Q_I. For sufficiency, for any W=U union A(P), take a minimum cover C of G[U]-P and I=U minus C. A prefix covering I must have no allowed endpoint in I on any edge outside P: an edge with both endpoints in I belongs to P, and any other incident edge crosses I. Thus the remaining slots can match to at most |C| public labels in U, and it attains rho(W). This proves exact typed observational preservation (R791); no preservation of counts, weights, other levels or prefix provenance under pruning.

Define a conflict graph J(G) whose vertices are all 2^n subsets I of V. Two cuts I,J conflict iff some edge of G joins I minus J to J minus I. This is exactly the condition for contradictory away-orientation requirements on the same edge. A collection of cuts is jointly coverable iff it is pairwise nonconflicting: for each source edge assign the unique required direction if any, otherwise arbitrary. Therefore the minimum number of actual prefixes required to retain the complete typed envelope equals chi(J(G)). In one direction a covering family yields a coloring by assigning each cut to one covering prefix; in the other each color class yields an orientation and hence a real prefix. This equality concerns the minimum size of a subfamily of actual prefixes, not the bit length of arbitrary implicit encodings.

Bounds:
    2^nu(G) <= chi(J(G)) <= min(2^m, binom(n,floor(n/2))),
where nu(G) is maximum matching cardinality. For the lower bound choose exactly one endpoint on each edge of a fixed maximum matching, no other vertices; the 2^nu cuts pairwise conflict. All 2^m singleton orientations cover all cuts, giving the first upper bound. For the second, partition the Boolean subset lattice into symmetric inclusion chains. Any chain has no conflicts (nested cuts), and can be covered by one orientation. For completeness, the symmetric chain partition exists by induction from the empty set: given a chain C_k,...,C_{n-k} on n labels and a new label z, create chain C_k,...,C_{n-k},C_{n-k} union {z}, and if nonempty the chain C_k union {z},...,C_{n-k-1} union {z}. The two chains partition its doubled copies and are symmetric on n+1 labels. Every symmetric chain meets the middle rank once. Hence their count is the stated binomial coefficient.

Sharpness: for a matching of m disjoint edges (isolated vertices allowed), both 2^m bounds agree. This yields an exponential lower bound on explicit exact prefix pruning even for a linear-size R792 network and bipartite source graph with polynomial-time mixed envelope queries. For K_n every two distinct middle-rank subsets conflict, so the binomial bound is attained. This is distinct from R791's information lower bound for arbitrary independent families and R792's computational hardness: an implicit encoding can remain compact even when exponentially many actual representatives are necessary. For a star with at least one edge, two orientations (all toward the center, all away) cover all cuts, sharp by the matching lower bound. These illustrate actual structural variability; no general lower bound on implicit representation complexity is inferred.

## 5. Exact finite verification

JS bitmask computation on all 71 nonempty labeled simple graphs with n=2,3,4. Enumerate all 3^m actual level-m prefix choices and independently enumerate one-slot assignments to obtain their basis sets; build rank tables from downward closure and subset maxima. Compare the minimum table at every mixed W against exhaustive vertex-cover search. For each graph independently solve exact set cover over all 2^m singleton orientations on 2^n cuts, and check the symmetric-chain subfamily preserves every mixed rank. For 12 deterministic transversal exterior slot configurations per graph (uniform, private singleton, 10 reproducible pseudorandom slot systems), compare direct worst-prefix max over exterior bases of interior rank to the full rank-cut formula and reduced canonical cut formula. All these have full rank in this run. No native amplitude, time or BRC numerical experiment was performed. General results are supported by the analytic proofs, finite check only within this scope.

Executed result:
```json
{
  "graphs": 71,
  "prefixes": 4161,
  "rankChecks": 1885128,
  "mixedChecks": 11864,
  "exteriorChecks": 852,
  "coverChecks": 71,
  "chainChecks": 11864,
  "complete": [
    [
      2,
      2
    ],
    [
      3,
      3
    ],
    [
      4,
      6
    ]
  ],
  "matching": [
    [
      2,
      1,
      2
    ],
    [
      3,
      1,
      2
    ],
    [
      3,
      1,
      2
    ],
    [
      3,
      1,
      2
    ],
    [
      4,
      1,
      2
    ],
    [
      4,
      1,
      2
    ],
    [
      4,
      1,
      2
    ],
    [
      4,
      1,
      2
    ],
    [
      4,
      2,
      4
    ],
    [
      4,
      1,
      2
    ],
    [
      4,
      2,
      4
    ],
    [
      4,
      1,
      2
    ],
    [
      4,
      2,
      4
    ]
  ],
  "minHistogram": {
    "2": 29,
    "3": 5,
    "4": 36,
    "6": 1
  }
}
```

Executed dependency-free replay:
```javascript
function replay(){
 const pop=x=>{let z=0;while(x){x&=x-1;z++}return z};
 let graphs=0,prefixes=0,mixedChecks=0,rankChecks=0,exteriorChecks=0,coverChecks=0,chainChecks=0;
 const complete=[],matching=[],minHistogram={};
 function chains(n){if(!n)return [[0]];let bit=1<<(n-1),out=[];for(let c of chains(n-1)){out.push([...c,c[c.length-1]|bit]);if(c.length>1)out.push(c.slice(0,-1).map(x=>x|bit))}return out}
 for(let n=2;n<=4;n++){
  let all=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)all.push([u,v]);
  for(let g=1;g<(1<<all.length);g++){
   let es=all.filter((_,i)=>g>>i&1),m=es.length,b=n+m,V=(1<<n)-1,T=(1<<b)-1;graphs++;
   let rows=Array.from({length:m},(_,e)=>[1<<(n+e),1<<es[e][0],1<<es[e][1]]);
   const ranks=slots=>{let bas=new Set();function f(j,s){if(j===m){bas.add(s);return}for(let x of slots[j])if(!(s&x))f(j+1,s|x)}f(0,0);if(!bas.size)return null;let a=new Uint8Array(T+1);for(let s of bas){for(let d=s;;d=(d-1)&s){a[d]=pop(d);if(!d)break}}for(let w=1;w<=T;w++){let d=w;while(d){let l=d&-d;a[w]=Math.max(a[w],a[w^l]);d^=l}}return {a,bas}};
   let rr=[],rho=new Uint8Array(T+1).fill(m);
   for(let p=0;p<3**m;p++){let z=p,slots=rows.map(r=>{let d=z%3;z=Math.floor(z/3);return d===0?[r[0],r[1]]:d===1?[r[0],r[2]]:r});let {a,bas}=ranks(slots);rr.push({a,bas});prefixes++;for(let w=0;w<=T;w++){rho[w]=Math.min(rho[w],a[w]);rankChecks++}}
   const inside=I=>es.reduce((z,[u,v],e)=>z+(((I>>u&1)&&(I>>v&1))?(1<<e):0),0);
   for(let w=0;w<=T;w++){let U=w&V,P=w>>n,k=n;for(let C=U;;C=(C-1)&U){if(!(inside(U^C)&~P))k=Math.min(k,pop(C));if(!C)break}if(rho[w]!==pop(P)+k)throw Error("mixed");mixedChecks++}
   let covers=[],orientRanks=[];
   for(let p=0;p<(1<<m);p++){let z=0,idx=0,power=1;for(let e=0;e<m;e++){idx+=(p>>e&1)*power;power*=3}for(let I=0;I<=V;I++){let ok=es.every(([u,v],e)=>{let a=p>>e&1?v:u,c=p>>e&1?u:v;return !(I>>a&1)||Boolean(I>>c&1)});if(ok)z|=1<<I}covers.push(z);orientRanks.push(rr[idx].a)}
   let target=(1<<(V+1))-1, by=Array.from({length:V+1},(_,I)=>covers.filter(z=>z>>I&1)),memo=new Map([[0,0]]);
   function opt(w){if(memo.has(w))return memo.get(w);let l=w&-w,i=31-Math.clz32(l),v=99;for(let z of by[i])v=Math.min(v,1+opt(w&~z));memo.set(w,v);return v}
   let count=opt(target);minHistogram[count]=(minHistogram[count]||0)+1;coverChecks++;
   if(g===(1<<all.length)-1)complete.push([n,count]);if(es.every(([u,v],i)=>es.every(([a,c],j)=>i===j||![a,c].includes(u)&&![a,c].includes(v))))matching.push([n,m,count]);
   let chosen=chains(n).map(c=>covers.findIndex(z=>c.every(I=>z>>I&1)));if(chosen.some(p=>p<0))throw Error("chain");
   for(let w=0;w<=T;w++){if(Math.min(...chosen.map(p=>orientRanks[p][w]))!==rho[w])throw Error("prune");chainChecks++}
   let seed=(g+1)*12345+n;
   for(let t=0;t<12;t++){let sl=Array.from({length:m},(_,j)=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;let mask=t===0?T:t===1?1<<(n+j):(seed&T)||1;return Array.from({length:b},(_,i)=>1<<i).filter(x=>x&mask)});let ex=ranks(sl);if(!ex)continue;
    let direct=m;for(let {a} of rr){let v=0;for(let s of ex.bas)v=Math.max(v,a[s]);direct=Math.min(direct,v)}
    let cut=m;for(let w=0;w<=T;w++)cut=Math.min(cut,rho[w]+ex.a[T^w]);
    let canon=m;for(let I=0;I<=V;I++){let P=inside(I);canon=Math.min(canon,pop(P)+ex.a[T^(I|(P<<n))])}
    if(direct!==cut||cut!==canon)throw Error("exterior");exteriorChecks++;
   }
  }
 }
 return {graphs,prefixes,rankChecks,mixedChecks,exteriorChecks,coverChecks,chainChecks,complete,matching,minHistogram}
}
console.log(JSON.stringify(replay(),null,2));
```

## 6. Continuation

Investigate whether the complete (not just level-m) R792 Port population can be forced into one rank by an actual fixed local-gadget construction that retains independent prefixes; alternatively characterize its full typed multilevel envelope without erasing triple states. For the present level, seek more efficient implicit canonical-cut optimization for structured exterior duals, and exact graph invariant algorithms for chi(J(G)) beyond matching, stars and complete graphs. Source graph and slot architecture remain the exact R792 input. Keep all original signed/weighted BRC, multiplicity, source, temporal order and native X6 common-depth data outside this auxiliary Boolean quotient. No Task closure, Result freeze, independent review or Foundation promotion.
