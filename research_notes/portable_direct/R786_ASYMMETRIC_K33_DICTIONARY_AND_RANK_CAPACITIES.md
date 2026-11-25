# R786 - Exact asymmetric K3,3 boundary dictionary and rank capacities

2026-11-25. AUTHOR_PROOF_WITH_EXHAUSTIVE_FINITE_CERTIFICATE / NOT_REVIEWED. Independent portable continuation of R785, EM-DIRECT-82A007 / TASK_RESEARCH, Activity RA-708BCC309CE076D8BB599B91. Own session metadata r3-20261125-1120-own-metadata-v1 confirms existing registered session, no own run, execution_authorized=false. Owner inventory request r3-20261125-1120-owner-read-v1 last observed RUNNING before publication. No shared Task, CLAIM, Result or review changed. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and mandatory joint-observer contract blob 3923890d77a02d84b772f789e6912dd14f220d14 read directly. Generated foundation startup package at this pin returned 404. Current ACTIVE worldview and current normative/portable rules read; account main entry snapshot cab5d3c0a17dc51dcd290fdd7815bf8dd172a703 verified. This is a fixed-prefix unsigned auxiliary Boolean boundary observer, not native weighted BRC execution or a native slice result.

Predecessors (immutable):
- 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md
- 236e6fea7374ac883a0fe12e2083cfcb31ada64b:research_notes/portable_direct/R783_MATCHING_REPRESENTATION_AND_SPARSE_BOUNDARY.md
- 44a473ee417d519a9c6e4d65b8bc168f577c7eef:research_notes/portable_direct/R785_ARBITRARY_ORDER_CAPACITY_RESIDUALS.md

## 1. Complete classification for the fixed labeled K3,3 pair graph

Let E be a normalized, fixed-prefix realizable relation, 0 in E, on six labeled terminal bits split as A={0,1,2}, B={3,4,5}. Its pair graph is exactly K3,3. No assumption of permutation symmetry of E. The R779 paired-exchange theorem says for every u,v in E there exists a perfect pairing of the support of u XOR v such that every toggle by a union of these disjoint pairs stays in E. Applying this at u=0 shows every member is balanced: every paired toggle from 0 must be an edge of K3,3, hence crosses A,B. Thus the only possible assignments are the 20 balanced masks Q below, including the ten compulsory masks of sizes zero and two. Exactly ten membership bits remain free: nine four-toggles and one six-toggle. This yields an exhaustive universe of 1024 candidate relations, valid for arbitrary size and cycle rank of the interior.

Theorem: exactly 51 of these 1024 candidates are realizable. Equivalently the paired-exchange property is both necessary and sufficient on this particular normalized pair-graph class. Under separate permutations of A and B there are exactly nine orbits. (No general sufficiency claim for other pair graphs.) The proof is the following finite exact certificate with an unbounded-interior necessity and explicit matching graphs for every surviving relation.

Necessity: enumerate all 1024 candidates; for each pair u,v present, enumerate all perfect pairings of u XOR v by selecting the least available label and pairing it with every possible partner recursively. For each pairing generate the entire cube by successively adjoining its translates. Reject the candidate if no pairing gives a cube contained in it. This enumerates all possible pairings without relying on a bound on the underlying Port graph. Precisely 51 survive; the code below checks the complete domain.

Sufficiency: generalize R785's matching-deletion construction to three slots with arbitrary incidence matrices a,b (each has 9 binary entries indexed by 3*j+k for terminal j, slot k). Each terminal is a leaf with private partner; each slot is a pair x_k,y_k with an internal edge. A partners join x slots according to a, B partners join y slots according to b. For a deletion of terminal sets U,V, unused terminal leaves force their partners. An occupied slot must match one freed partner on each side, so feasibility is equivalent to the existence of the SAME subset of slots onto which U and V can each be matched bijectively. Local possible slot-subsets are computed exactly by iterating labels and assigning a new unused slot. Enumerating 512^2 incidence pairs gives 19,537 with complete pair graph, and 45 distinct surviving relations. All witnesses use at most 18 graph vertices.

The remaining six surviving masks (750,757,862,883,925,939) have the full toggle and exactly six four-toggles. For each, the complements of its three excluded four-toggles form a perfect matching of K3,3. Use H=K3,3 minus that matching, i.e. a six-cycle, with the six graph vertices themselves as terminals (no private leaves). H-D has a perfect matching at D=0 and D=all. For a cross pair D the remaining induced 2-by-2 bipartite graph lacks at most a matching of two edges and has a perfect matching; for a four-toggle D it has two vertices and succeeds exactly when their complementary pair is an edge. Unbalanced deletions fail by unequal part sizes. This realizes exactly the six remaining masks. The R783 matching representation converse converts every such H to a trivalent auxiliary Port relation. The graph witnesses can have irrelevant internal components; the terminal pair graph is connected, but no extra claim about a specific connected Port gadget implementation is needed. The independent recursive perfect-matching oracle replays all 64 terminal masks for each of the 51 witnesses; zero discrepancies.

## 2. Dictionary size, orbit representatives, and genuine six-order residuals

Masks use bits in ascending order of opt=[27,29,30,43,45,46,51,53,54,63]. Each represents the optional membership flags; the compulsory masks fixed=[0,9,10,12,17,18,20,33,34,36] are implicit. Nine orbit representatives, with orbit size, number of four-toggles and full-toggle bit, are:
[[0,1,0,0],[27,9,4,0],[63,3,6,0],[219,3,6,0],[511,1,9,0],[750,6,6,1],[751,18,7,1],[767,9,8,1],[1023,1,9,1]]

There are 17 relations without the full toggle, 34 with it. The respective counts by number of four-toggles 0..9 are:
[[1,0,0,0,9,0,6,0,0,1],[0,0,0,0,0,0,6,18,9,1]]
In particular, only the four-toggle pattern containing all nine four-toggles occurs with both full-toggle values (511 and 1023): inspect the fullDistribution and the exact mask list, or compare all pairs differing in bit 9. This is precisely R785's capacity-2 versus capacity-3 relation. Hence the symmetric R785 pair is the ONLY labeled normalized K3,3 ambiguity remaining when all four-toggles are known. For every other four-toggle pattern the six-toggle is determined by the paired-exchange condition.

There are 51 distinct labeled relations, so an exact fixed-length dictionary index uses 6 bits rather than the raw 10 optional bits. Distinct relations are distinguishable by a singleton exterior fixing a differing even boundary assignment (R783 converse, e.g. matching graph with a private partner for each coordinate fixed to zero and pairing the coordinates fixed to one in the baseline construction). Thus this is the minimum fixed-length code for single relations under all complete Boolean graphic contexts on this fixed labeled pair graph. Nine orbit types are not a replacement for the labeled relation without the relabeling information. Encoding, decoding and table construction are finite; no general time bound or improvement for multi-prefix antichains is asserted.

## 3. General bipartite pair graph: exact mixed rank-capacity coordinates

This is an analytic result for arbitrary finite part sizes m,n (not just K3,3). Reuse R783 Theorem B and the normalized base 0. The skew-symmetric boundary matrix M over its rational-function field has zero entries within either side of the pair graph, hence, in A,B order, M=[0 C; -C^T 0]. For equal-size subsets U of A and V of B, det M[U union V]=det(C[U,V])^2; for unequal size it vanishes by the rectangular block rank bound. Construct the m-row matrix N=[I_m C], indexed by A union B, with A the identity basis. For D=U union V balanced, the m-column set S=(A minus U) union V has determinant equal, up to sign, to det C[U,V], by expansion along the identity columns. Therefore D is feasible iff S is a basis of the represented column matroid. This identifies the entire auxiliary support with basis exchange of a linear matroid, retaining the actual correlations of the entries of C.

For any W subset of A union B define the mixed capacity
r(W)=rank N[:,W]=|W intersect A|+rank C[A minus W, W intersect B],
where A minus W means remove W intersect A. The rank identity follows by quotienting out the included identity columns. Then for balanced D, S as above, feasibility is equivalent to every capacity inequality |S intersect W|<=r(W). Necessity follows from column independence. Sufficiency follows by taking W=S: |S|=m, so rank N[:,S]=m. Equivalently r(W)=max over feasible D of |((A minus U) union V) intersect W|, since any independent columns in W extend to a basis of N. This proves a precise general capacity-inequality representation using mixed terminal subsets, not just one symmetric slot count. It does not establish a small family of inequalities or a polynomial-size numeric encoding of C; rational-function representation length and computation cost are unresolved. The R785 symmetric capacity is a special case. Finding sparse sufficient inequalities via actual matching cuts, and deciding the full six-cut dictionary outside the K3,3 class, are next questions.

## 4. Exact replay evidence

Executed dependency-free JS integer arithmetic. All 1024 candidate relations, all 262144 three-slot incidence configurations, and all 3264 matching-deletion decisions across the final 51 explicit witnesses were checked. Separate relabeling orbit enumeration verified closure. No native signed/weighted BRC run. Preserve lift provenance, multiplicity, exact weights, signed phase, path/event order and native X6 common depth as distinct observations. The result is author-checked finite proof relative to R779/R783, not independent review.

Actual output:
```json
{
  "Q": [
    0,
    9,
    10,
    12,
    17,
    18,
    20,
    27,
    29,
    30,
    33,
    34,
    36,
    43,
    45,
    46,
    51,
    53,
    54,
    63
  ],
  "fixed": [
    0,
    9,
    10,
    12,
    17,
    18,
    20,
    33,
    34,
    36
  ],
  "opt": [
    27,
    29,
    30,
    43,
    45,
    46,
    51,
    53,
    54,
    63
  ],
  "candidates": 1024,
  "valid": 51,
  "slotConfigs": 262144,
  "completePairConfigs": 19537,
  "slotRelations": 45,
  "missing": [
    750,
    757,
    862,
    883,
    925,
    939
  ],
  "orbits": [
    [
      0,
      1,
      0,
      0
    ],
    [
      27,
      9,
      4,
      0
    ],
    [
      63,
      3,
      6,
      0
    ],
    [
      219,
      3,
      6,
      0
    ],
    [
      511,
      1,
      9,
      0
    ],
    [
      750,
      6,
      6,
      1
    ],
    [
      751,
      18,
      7,
      1
    ],
    [
      767,
      9,
      8,
      1
    ],
    [
      1023,
      1,
      9,
      1
    ]
  ],
  "replays": 3264,
  "validMasks": [
    0,
    27,
    45,
    54,
    63,
    195,
    216,
    219,
    325,
    360,
    365,
    390,
    432,
    438,
    455,
    504,
    511,
    750,
    751,
    757,
    759,
    765,
    766,
    767,
    862,
    863,
    883,
    887,
    891,
    894,
    895,
    925,
    927,
    939,
    943,
    955,
    957,
    959,
    989,
    990,
    991,
    1003,
    1006,
    1007,
    1011,
    1013,
    1015,
    1019,
    1021,
    1022,
    1023
  ],
  "slotWitnesses": [
    [
      0,
      [
        73,
        73
      ]
    ],
    [
      27,
      [
        75,
        75
      ]
    ],
    [
      45,
      [
        89,
        75
      ]
    ],
    [
      54,
      [
        201,
        75
      ]
    ],
    [
      63,
      [
        91,
        75
      ]
    ],
    [
      195,
      [
        75,
        89
      ]
    ],
    [
      216,
      [
        75,
        201
      ]
    ],
    [
      219,
      [
        74,
        219
      ]
    ],
    [
      325,
      [
        89,
        89
      ]
    ],
    [
      360,
      [
        89,
        201
      ]
    ],
    [
      365,
      [
        81,
        219
      ]
    ],
    [
      390,
      [
        201,
        89
      ]
    ],
    [
      432,
      [
        201,
        201
      ]
    ],
    [
      438,
      [
        82,
        219
      ]
    ],
    [
      455,
      [
        91,
        89
      ]
    ],
    [
      504,
      [
        91,
        201
      ]
    ],
    [
      511,
      [
        83,
        219
      ]
    ],
    [
      751,
      [
        93,
        107
      ]
    ],
    [
      759,
      [
        205,
        107
      ]
    ],
    [
      765,
      [
        93,
        331
      ]
    ],
    [
      766,
      [
        205,
        331
      ]
    ],
    [
      767,
      [
        92,
        367
      ]
    ],
    [
      863,
      [
        93,
        93
      ]
    ],
    [
      887,
      [
        233,
        107
      ]
    ],
    [
      891,
      [
        93,
        205
      ]
    ],
    [
      894,
      [
        233,
        331
      ]
    ],
    [
      895,
      [
        85,
        223
      ]
    ],
    [
      927,
      [
        205,
        93
      ]
    ],
    [
      943,
      [
        233,
        93
      ]
    ],
    [
      955,
      [
        205,
        205
      ]
    ],
    [
      957,
      [
        233,
        205
      ]
    ],
    [
      959,
      [
        86,
        223
      ]
    ],
    [
      989,
      [
        93,
        345
      ]
    ],
    [
      990,
      [
        205,
        345
      ]
    ],
    [
      991,
      [
        92,
        381
      ]
    ],
    [
      1003,
      [
        93,
        233
      ]
    ],
    [
      1006,
      [
        233,
        345
      ]
    ],
    [
      1007,
      [
        85,
        251
      ]
    ],
    [
      1011,
      [
        205,
        233
      ]
    ],
    [
      1013,
      [
        233,
        233
      ]
    ],
    [
      1015,
      [
        86,
        251
      ]
    ],
    [
      1019,
      [
        92,
        493
      ]
    ],
    [
      1021,
      [
        85,
        475
      ]
    ],
    [
      1022,
      [
        86,
        475
      ]
    ],
    [
      1023,
      [
        84,
        511
      ]
    ]
  ],
  "fullDistribution": [
    [
      1,
      0,
      0,
      0,
      9,
      0,
      6,
      0,
      0,
      1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      6,
      18,
      9,
      1
    ]
  ],
  "failures": 0
}
```

Reproduction (Node or any ordinary JS runtime):
```js
function verify(){
 const pop=x=>{let n=0;for(;x;x&=x-1)n++;return n};
 const Q=Array.from({length:64},(_,i)=>i).filter(x=>pop(x&7)===pop(x>>3)), fixed=Q.filter(x=>pop(x)<=2), opt=Q.filter(x=>pop(x)>=4);
 function parts(s){if(!s)return [[]];let a=s&-s,t=s^a,o=[];for(let z=t;z;z&=z-1){let b=z&-z;for(let p of parts(t^b))o.push([a|b,...p])}return o}
 const pairs=[];for(let i=0;i<Q.length;i++)for(let j=i+1;j<Q.length;j++){let u=Q[i],v=Q[j];let cubes=parts(u^v).map(p=>{let c=[u];for(let b of p)c=c.concat(c.map(x=>x^b));return c});pairs.push([u,v,cubes])}
 const valid=[];for(let m=0;m<1024;m++){let s=new Set([...fixed,...opt.filter((x,i)=>m>>i&1)]);if(pairs.every(([u,v,cubes])=>!s.has(u)||!s.has(v)||cubes.some(c=>c.every(x=>s.has(x)))))valid.push(m)}
 function local(g){let d=[];for(let i=0;i<8;i++){let a=1;for(let j=0;j<3;j++)if(i>>j&1){let b=0;for(let s=0;s<8;s++)if(a>>s&1)for(let k=0;k<3;k++)if(!(s>>k&1)&&(g>>(3*j+k)&1))b|=1<<(s|1<<k);a=b}d.push(a)}return d}
 let dict=Array.from({length:512},(_,i)=>local(i)), w=new Map(), n=0;
 for(let a=0;a<512;a++)for(let b=0;b<512;b++){if(!fixed.every(s=>dict[a][s&7]&dict[b][s>>3]))continue;n++;let m=0;opt.forEach((s,i)=>{if(dict[a][s&7]&dict[b][s>>3])m|=1<<i});if(!w.has(m))w.set(m,[a,b])}
 const missing=valid.filter(x=>!w.has(x));if([...w.keys()].some(x=>!valid.includes(x)))throw Error("necessity");
 const perm=a=>a.length?a.flatMap(x=>perm(a.filter(y=>x!==y)).map(p=>[x,...p])):[[]],ps=perm([0,1,2]);
 const transform=(m,p,q)=>{let n=0;for(let i=0;i<10;i++)if(m>>i&1){let x=opt[i],s=0;for(let j=0;j<3;j++){if(x>>j&1)s|=1<<p[j];if(x>>(3+j)&1)s|=1<<(3+q[j])}n|=1<<opt.indexOf(s)}return n};
 let seen=new Set(),orbits=[];for(let m of valid)if(!seen.has(m)){let o=new Set(ps.flatMap(p=>ps.map(q=>transform(m,p,q))));for(let x of o){if(!valid.includes(x))throw Error("orbit");seen.add(x)}orbits.push([m,o.size,pop(m&511),m>>9])}
 let replays=0;for(let m of valid){let adj=[],add=()=>{adj.push(0);return adj.length-1},edge=(u,v)=>{adj[u]|=1<<v;adj[v]|=1<<u};for(let i=0;i<6;i++)add();
 if(w.has(m)){let [a,b]=w.get(m);for(let i=0;i<6;i++)edge(i,add());for(let k=0;k<3;k++){let x=add(),y=add();edge(x,y);for(let j=0;j<3;j++){if(a>>(3*j+k)&1)edge(6+j,x);if(b>>(3*j+k)&1)edge(9+j,y)}}}
 else {let excluded=opt.slice(0,9).filter((s,i)=>!(m>>i&1)).map(s=>s^63);if(excluded.length!==3||new Set(excluded.map(s=>s&7)).size!==3||new Set(excluded.map(s=>s>>3)).size!==3||!(m>>9))throw Error("cycle form");for(let a=0;a<3;a++)for(let b=0;b<3;b++)if(!excluded.includes((1<<a)|(1<<(b+3))))edge(a,b+3)}
 const memo=new Map([[0,true]]);function pm(s){if(memo.has(s))return memo.get(s);let a=s&-s,i=31-Math.clz32(a),ok=false;for(let z=adj[i]&s;z;z&=z-1)if(pm(s^a^(z&-z))){ok=true;break}memo.set(s,ok);return ok}
 const E=new Set([...fixed,...opt.filter((s,i)=>m>>i&1)]);for(let s=0;s<64;s++){if(pm(((1<<adj.length)-1)^s)!==E.has(s))throw Error("witness "+m+" "+s);replays++}}
 return {Q,fixed,opt,candidates:1024,valid:valid.length,slotConfigs:262144,completePairConfigs:n,slotRelations:w.size,missing,orbits,replays,validMasks:valid,slotWitnesses:[...w.entries()].sort((a,b)=>a[0]-b[0]),fullDistribution:[0,1].map(f=>Array.from({length:10},(_,i)=>valid.filter(m=>(m>>9)===f&&pop(m&511)===i).length)),failures:0}
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Continuation

Determine which mixed rank-capacity coordinates suffice for small asymmetric boundary graphs, especially whether actual matching-path bottleneck cuts give a compact inequality family. Extend paired-exchange necessity plus explicit witnesses to other six-terminal pair graphs; do not assume sufficiency globally. Use the 51-entry K3,3 dictionary as an exact single-prefix subcatalog when studying actual external-context quotients or multi-prefix state reachability. No shared Task completion or mathematical acceptance is claimed.
