# R787 - Cyclic-flat capacity compression and exact matching rank oracle

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R783_R786 / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, EM-DIRECT-82A007 / TASK_RESEARCH, Activity RA-708BCC309CE076D8BB599B91. Own recovery r3-20261125-1220-own-metadata-v1 confirms registered researcher, no own run, execution_authorized=false. Owner inventory r3-20261125-1220-owner-read-v1 observed RUNNING. No shared Task, CLAIM, Result or review mutated. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer 3923890d77a02d84b772f789e6912dd14f220d14 read; generated startup and Heartbeat companion returned 404 at frozen pin. ACTIVE worldview, portable and current normative rules read. Account entries at main@7ff308e53336b349703f0e0e26e45140b38c9a61. Scope: single fixed-prefix normalized unsigned Boolean auxiliary Port boundary; native signed BRC, weight, multiplicity, provenance, event order, X6 common depth remain separate.

Exact dependencies:
- 236e6fea7374ac883a0fe12e2083cfcb31ada64b:research_notes/portable_direct/R783_MATCHING_REPRESENTATION_AND_SPARSE_BOUNDARY.md
- c7b233960d24c33525572bd3c4d9b9663f2b830f:research_notes/portable_direct/R786_ASYMMETRIC_K33_DICTIONARY_AND_RANK_CAPACITIES.md

## 1. Cyclic-flat capacity reduction at arbitrary width

In R786, for a normalized feasible baseline zero and bipartite pair graph A,B, write N=[I_m C] over the rational-function field and S=(A minus U) union V, where |U|=|V|. Let T=A union B and r(W)=rank N[:,W]. A balanced exchange is feasible iff S is a basis. For a subset F of T call F a flat iff r(F+e)>r(F) for each e outside F; call it cyclic iff r(F-e)=r(F) for every e in F. The standard matroid cyclic-flat construction gives the following exact capacity compression in this Port observer:

    S feasible iff |S intersect F| <= r(F) for every cyclic flat F.

Proof: necessity follows from independence. If |S|=m and S is dependent, choose a minimal dependent subset K of S (a circuit). Its rank is |K|-1. Let F be its linear closure in T. It is a flat, with rank |K|-1. Deleting any e in F outside K leaves K and hence leaves rank unchanged; deleting e in K leaves K-e, an independent set of size |K|-1, so also leaves rank unchanged. Therefore F is cyclic and violates the inequality because K is contained in S intersect F. This argument also covers a zero-column loop. Empty F and full T inequalities are tautological on m-element S, so can be omitted. Alternatively any violating rank inequality on a set W contains a circuit in S intersect W and hence a violating cyclic-flat inequality. No unproven independence of effective coefficients is used. This is a standard matroid fact applied to the R786 exact support representation, not a claim that the matroid fact is new.

The complete single-prefix feasible set can be reconstructed exactly using these inequalities and balance. Consequently all Boolean operations that depend only on this relation (including exact R777 gluing and R780 contextual tests) retain their output; this does not identify weights or different prefix families. There is no general small bound on the number of cyclic flats asserted here.

## 2. Exact graph-based rank oracle without symbolic elimination

Let H be the even-order matching graph of R783 for the normalized relation; H has a perfect matching. For W subset T put O=(A minus W) union (B intersect W), with A and B viewed as labeled terminal vertices of H. Then

    r(W)=|W intersect A| + (1/2) max{|D|: D subset O, H-D has a perfect matching}.

Proof: the rank of C[A minus W,B intersect W] equals the largest size of a nonzero square minor (rank-minor characterization over a field). R786 and R783 identify that minor with the existence of a perfect matching after deleting the corresponding balanced terminal subset D. Conversely every feasible deletion in O is balanced by the bipartite pair graph representation, so its cardinality is twice the size of its minor. Empty deletion is feasible; the maximum exists and is even.

A single maximum-weight perfect matching query calculates this maximum: adjoin a private dummy d_t for every t in O, connect t to d_t with weight 1, and connect all dummy vertices to one another by weight-0 edges. If |O| is odd, add one further dummy joined to every other dummy (weight 0), without a terminal edge. Retain H with weight 0. Thus the number of dummy vertices is even and a perfect matching always exists (match H and pair all dummies). In any perfect matching of the augmented graph, let D be the terminals using their private dummy edge. The restriction to H-D is a perfect matching, and the weight is |D|. Conversely any feasible D subset O has even size, so pair the even number of remaining dummies arbitrarily in their clique; together with H-D and the private edges this yields weight |D|. Hence the maximum weight equals the desired deletion maximum. This is an exact reduction to a standard polynomial-time maximum-weight perfect matching problem in general graphs, with |V(H)|+|O|+(|O| mod 2) vertices and O(|O|^2) new edges; no numerical evaluation of rational functions needed. A matching witness gives the maximizing deletion. This is a per-query algorithm, not a polynomial-size enumeration of all cyclic flats or a solution to the multiprefix reserve problem. No implementation of weighted blossom is benchmarked here.

## 3. Sharp K3,3 capacity-constraint dictionary

Reuse the exact 51 labeled relations from R786, including its exhaustive necessity and explicit matching witnesses. Each relation corresponds to a rank-3 matroid on six labels by S=D XOR 7. There are 20 three-element sets. The exact ranks for all 64 W are computed by r(W)=max over bases S of popcount(S AND W). The latter follows by extending any independent subset of W to a basis. Enumerate every proper nonempty cyclic flat by its defining rank tests. For each valid relation, also compute the globally minimum number of original rank inequalities (from ALL 64 W) necessary to exclude every nonbasis, even allowing non-cyclic flats. This is an exact finite set cover: the universe is the list of nonbases; W covers precisely those candidates violating |S intersect W|<=r(W). Dynamic programming over covered masks considers every W, using an OR transition and unit cost; the OR is idempotent, so an in-place transition cannot improve a cost by reusing W. The final full-mask entry is optimal by induction on the processed sets. This is a finite proof relative to the R786 complete dictionary, not a sampled result.

Result: number of relations requiring respectively 0,1,2,3 constraints is 1,17,27,6. The proper nonempty cyclic-flat count equals this minimum for every one of the 51 relations. Thus at most three nontrivial inequalities suffice for EVERY normalized K3,3 relation, and three are necessary for six labeled relations. This is minimal within the class of individual R786 rank-capacity inequalities with balance and size already known, not an arbitrary bit-encoding lower bound. R786's 6-bit index remains the minimum fixed-length code among its 51 labeled relations.

Example: optional mask 750 has full-toggle feasible and exactly three excluded four-toggles. Its indispensable constraints are (W,r)=(28,2),(42,2),(49,2), each excluding one distinct 3-set. For optional masks 511 and 1023 (R785's symmetric capacity 2 and 3), respectively use just (56,2) or no extra constraint. Here 56 is all three B labels. The low-order ambiguity thus has a direct capacity witness. The cyclic-flat data supplies semantic constraints (not simply an opaque dictionary index).

Verification: all 51 x 20 = 1020 candidate basis decisions checked; all 51 x 64 = 3264 rank values compared against maximum feasible balanced deletion on O using the previously certified relation table. All 51 minimal-cover optima checked using all rank sets versus cyclic flats. Zero assertion failures. This verifies the rank identity on the actual finite dictionary, not execution of a general weighted-matching solver; the reduction in section 2 is analytic.

Actual replay result (row = [R786 optional mask, proper nonempty cyclic-flat count, minimum count, [[flat mask,rank],...]]):
```json
{
  "hist": {
    "0": 1,
    "1": 17,
    "2": 27,
    "3": 6
  },
  "cycHist": {
    "0": 1,
    "1": 17,
    "2": 27,
    "3": 6
  },
  "checks": 1020,
  "rankChecks": 3264,
  "rows": [
    [
      0,
      1,
      1,
      [
        [
          56,
          1
        ]
      ]
    ],
    [
      27,
      2,
      2,
      [
        [
          48,
          1
        ],
        [
          57,
          2
        ]
      ]
    ],
    [
      45,
      2,
      2,
      [
        [
          48,
          1
        ],
        [
          58,
          2
        ]
      ]
    ],
    [
      54,
      2,
      2,
      [
        [
          48,
          1
        ],
        [
          60,
          2
        ]
      ]
    ],
    [
      63,
      1,
      1,
      [
        [
          48,
          1
        ]
      ]
    ],
    [
      195,
      2,
      2,
      [
        [
          40,
          1
        ],
        [
          57,
          2
        ]
      ]
    ],
    [
      216,
      2,
      2,
      [
        [
          24,
          1
        ],
        [
          57,
          2
        ]
      ]
    ],
    [
      219,
      1,
      1,
      [
        [
          57,
          2
        ]
      ]
    ],
    [
      325,
      2,
      2,
      [
        [
          40,
          1
        ],
        [
          58,
          2
        ]
      ]
    ],
    [
      360,
      2,
      2,
      [
        [
          24,
          1
        ],
        [
          58,
          2
        ]
      ]
    ],
    [
      365,
      1,
      1,
      [
        [
          58,
          2
        ]
      ]
    ],
    [
      390,
      2,
      2,
      [
        [
          40,
          1
        ],
        [
          60,
          2
        ]
      ]
    ],
    [
      432,
      2,
      2,
      [
        [
          24,
          1
        ],
        [
          60,
          2
        ]
      ]
    ],
    [
      438,
      1,
      1,
      [
        [
          60,
          2
        ]
      ]
    ],
    [
      455,
      1,
      1,
      [
        [
          40,
          1
        ]
      ]
    ],
    [
      504,
      1,
      1,
      [
        [
          24,
          1
        ]
      ]
    ],
    [
      511,
      1,
      1,
      [
        [
          56,
          2
        ]
      ]
    ],
    [
      750,
      3,
      3,
      [
        [
          28,
          2
        ],
        [
          42,
          2
        ],
        [
          49,
          2
        ]
      ]
    ],
    [
      751,
      2,
      2,
      [
        [
          42,
          2
        ],
        [
          49,
          2
        ]
      ]
    ],
    [
      757,
      3,
      3,
      [
        [
          26,
          2
        ],
        [
          44,
          2
        ],
        [
          49,
          2
        ]
      ]
    ],
    [
      759,
      2,
      2,
      [
        [
          44,
          2
        ],
        [
          49,
          2
        ]
      ]
    ],
    [
      765,
      2,
      2,
      [
        [
          26,
          2
        ],
        [
          49,
          2
        ]
      ]
    ],
    [
      766,
      2,
      2,
      [
        [
          28,
          2
        ],
        [
          49,
          2
        ]
      ]
    ],
    [
      767,
      1,
      1,
      [
        [
          49,
          2
        ]
      ]
    ],
    [
      862,
      3,
      3,
      [
        [
          28,
          2
        ],
        [
          41,
          2
        ],
        [
          50,
          2
        ]
      ]
    ],
    [
      863,
      2,
      2,
      [
        [
          41,
          2
        ],
        [
          50,
          2
        ]
      ]
    ],
    [
      883,
      3,
      3,
      [
        [
          25,
          2
        ],
        [
          44,
          2
        ],
        [
          50,
          2
        ]
      ]
    ],
    [
      887,
      2,
      2,
      [
        [
          44,
          2
        ],
        [
          50,
          2
        ]
      ]
    ],
    [
      891,
      2,
      2,
      [
        [
          25,
          2
        ],
        [
          50,
          2
        ]
      ]
    ],
    [
      894,
      2,
      2,
      [
        [
          28,
          2
        ],
        [
          50,
          2
        ]
      ]
    ],
    [
      895,
      1,
      1,
      [
        [
          50,
          2
        ]
      ]
    ],
    [
      925,
      3,
      3,
      [
        [
          26,
          2
        ],
        [
          41,
          2
        ],
        [
          52,
          2
        ]
      ]
    ],
    [
      927,
      2,
      2,
      [
        [
          41,
          2
        ],
        [
          52,
          2
        ]
      ]
    ],
    [
      939,
      3,
      3,
      [
        [
          25,
          2
        ],
        [
          42,
          2
        ],
        [
          52,
          2
        ]
      ]
    ],
    [
      943,
      2,
      2,
      [
        [
          42,
          2
        ],
        [
          52,
          2
        ]
      ]
    ],
    [
      955,
      2,
      2,
      [
        [
          25,
          2
        ],
        [
          52,
          2
        ]
      ]
    ],
    [
      957,
      2,
      2,
      [
        [
          26,
          2
        ],
        [
          52,
          2
        ]
      ]
    ],
    [
      959,
      1,
      1,
      [
        [
          52,
          2
        ]
      ]
    ],
    [
      989,
      2,
      2,
      [
        [
          26,
          2
        ],
        [
          41,
          2
        ]
      ]
    ],
    [
      990,
      2,
      2,
      [
        [
          28,
          2
        ],
        [
          41,
          2
        ]
      ]
    ],
    [
      991,
      1,
      1,
      [
        [
          41,
          2
        ]
      ]
    ],
    [
      1003,
      2,
      2,
      [
        [
          25,
          2
        ],
        [
          42,
          2
        ]
      ]
    ],
    [
      1006,
      2,
      2,
      [
        [
          28,
          2
        ],
        [
          42,
          2
        ]
      ]
    ],
    [
      1007,
      1,
      1,
      [
        [
          42,
          2
        ]
      ]
    ],
    [
      1011,
      2,
      2,
      [
        [
          25,
          2
        ],
        [
          44,
          2
        ]
      ]
    ],
    [
      1013,
      2,
      2,
      [
        [
          26,
          2
        ],
        [
          44,
          2
        ]
      ]
    ],
    [
      1015,
      1,
      1,
      [
        [
          44,
          2
        ]
      ]
    ],
    [
      1019,
      1,
      1,
      [
        [
          25,
          2
        ]
      ]
    ],
    [
      1021,
      1,
      1,
      [
        [
          26,
          2
        ]
      ]
    ],
    [
      1022,
      1,
      1,
      [
        [
          28,
          2
        ]
      ]
    ],
    [
      1023,
      0,
      0,
      []
    ]
  ]
}
```

Dependency-free JS reproduction:
```js
function verify(){
 const pop=x=>{let n=0;for(;x;x&=x-1)n++;return n};
 const S=Array.from({length:64},(_,x)=>x).filter(x=>pop(x)===3);
 const fixed=[0,9,10,12,17,18,20,33,34,36],opt=[27,29,30,43,45,46,51,53,54,63];
 const masks=[0,27,45,54,63,195,216,219,325,360,365,390,432,438,455,504,511,750,751,757,759,765,766,767,862,863,883,887,891,894,895,925,927,939,943,955,957,959,989,990,991,1003,1006,1007,1011,1013,1015,1019,1021,1022,1023];
 const rows=[],hist={},cycHist={};let checks=0,rankChecks=0;
 for(const m of masks){
  const bases=[...fixed,...opt.filter((_,i)=>m>>i&1)].map(x=>x^7);
  const bad=S.filter(x=>!bases.includes(x));
  const r=Array.from({length:64},(_,w)=>Math.max(...bases.map(b=>pop(b&w))));
  // Independently calculate rank via maximum feasible exchange on the allowed rectangle.
  const d=bases.map(b=>b^7);
  for(let w=0;w<64;w++){
   let o=(7&~w)|(56&w);
   let q=pop(w&7)+Math.max(...d.filter(x=>(x&~o)===0).map(x=>pop(x)/2));
   if(q!==r[w])throw Error("rank oracle");rankChecks++;
  }
  const cap=Array.from({length:64},(_,w)=>bad.reduce((z,b,i)=>z|(pop(b&w)>r[w]?1<<i:0),0));
  const cyc=Array.from({length:64},(_,w)=>w).filter(w=>w>0&&w<63&&Array.from({length:6},(_,i)=>1<<i).every(bit=>(w&bit)?r[w^bit]===r[w]:r[w|bit]>r[w]));
  function solve(ws){let n=1<<bad.length,dp=Array(n).fill(null);dp[0]=[];for(let w of ws){if(!cap[w])continue;for(let x=0;x<n;x++)if(dp[x]){let y=x|cap[w];if(dp[y]===null||dp[y].length>dp[x].length+1)dp[y]=[...dp[x],w]}}return dp[n-1]}
  const all=solve(Array.from({length:64},(_,w)=>w)),z=solve(cyc);
  if(!all||!z)throw Error("coverage");
  for(const b of S){if(z.every(w=>pop(b&w)<=r[w])!==bases.includes(b))throw Error("basis");checks++}
  if(all.length!==z.length||z.length!==cyc.length)throw Error("minimum");
  hist[z.length]=(hist[z.length]??0)+1;cycHist[cyc.length]=(cycHist[cyc.length]??0)+1;
  rows.push([m,cyc.length,z.length,z.map(w=>[w,r[w]])])
 }
 return {hist,cycHist,checks,rankChecks,rows};
}
console.log(JSON.stringify(verify(),null,2));
```

## 4. Next problem

Extract cyclic-flat candidates directly from matching cuts, ideally without enumerating all 2^|T| subsets; study when the number of necessary capacities is polynomial in interface width, and construct a family with many independent capacity constraints if it is not. General graph H can be nonbipartite even when its terminal pair graph is bipartite, so a simple directed max-flow reduction is not assumed. Next also distinguish genuine cyclic-flat count from rank-inequality cover minimum beyond K3,3. No native mathematical acceptance or formal Result is asserted.
