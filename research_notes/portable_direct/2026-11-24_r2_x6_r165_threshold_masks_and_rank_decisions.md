# X6 R165 — Exact threshold-only minimal channel masks and shared rank decisions

2026-11-24. AUTHOR ANALYTIC REDUCTION / EXACT FINITE CERTIFICATE / NOT_REVIEWED. Independent informed research, conditional static six-pair BRC observer, Port 10, fixed C/A=22/17. Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f; R162@3682ce83f1a1638e29f600769ffa6cd6207b4841, R163@c8a9d155c12ba72410a3f9f3b2a793e1e4657adb, R164@8c94c3e4d6e7a751441b11f2042638515c22ff15. P000 V5, Heartbeat World, raw labeled six-gap and provenance preservation unchanged. No native time-dynamics inference.

## Result

For a physical integer direction v=(x,y,z), retain q=max(sum positive,sum negative)<=10, unoriented representative with first nonzero coordinate positive, heights h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z), gap g in order AB,AC,AD,BC,BD,CD, positive capacities s and score F=max_j g_j/s_j. eta is the full 1935-row minimum. R162 and R163 give the ten-row near bank T and six-row optimizer W at the ratio 22/17. We work with their frozen results. Given exact eta, a threshold-only mask M_v is a fixed subset of the original six tests such that for every A,B,D>0, C=22A/17, v is strictly near iff every j in M_v has 2g_j<3eta*s_j.

The unique smallest mask for each row is (channel order as above, bit 0=AB, bit 5=CD):
- 1,0,0 : AC AD BC BD; exact feasible nonempty failure masks 2, 4, 8, 10, 11, 16, 20
- 1,3,-1 : AB AC BD CD; exact feasible nonempty failure masks 1, 2, 3, 10, 11, 16, 32, 34, 42, 43, 48, 50
- 4,-4,1 : AC BC; exact feasible nonempty failure masks 2, 8, 10, 11
- 4,-1,0 : AB AD BD; exact feasible nonempty failure masks 1, 4, 9, 16, 20, 36, 52
- 5,-4,1 : AC BC BD CD; exact feasible nonempty failure masks 2, 8, 10, 11, 16, 32, 36, 48, 52
- 5,-1,0 : AB AC BD CD; exact feasible nonempty failure masks 1, 2, 3, 11, 16, 32, 48
- 6,-4,1 : AD BD; exact feasible nonempty failure masks 4, 16, 20, 36, 52
- 6,-1,0 : AB AC; exact feasible nonempty failure masks 1, 2, 3, 11
- 7,-1,0 : AB AC AD BD; exact feasible nonempty failure masks 1, 2, 3, 4, 6, 10, 11, 14, 15, 16, 20, 22
- 9,-5,1 : AC AD BC BD; exact feasible nonempty failure masks 2, 4, 8, 10, 16, 20
Here a failure mask includes equality (2g_j>=3eta*s_j). The masks have 33 row tests in total, versus R164's 35 for full scores. In particular (4,-4,1) needs only AC and BC, and (6,-1,0) only AB and AC. Their dropped channels remain necessary for some exact row scores per R164: this is a strictly weaker declared observer, not full-score equivalence.

There are only 20 distinct (channel,gap) threshold predicates. Ordered gap lists by channel:
- AB: 1, 2, 3, 4
- AC: 3, 6, 9
- AD: 6, 7, 10, 11, 12
- BC: 2, 3, 4
- BD: 6, 12
- CD: 7, 8, 11
At runtime find, for each channel j, the rank of 3eta*s_j/2 relative to the sorted list using strict comparisons. A balanced binary search on k sorted positive integers takes at most ceil(log2(k+1)) comparisons to determine the number strictly below the threshold; it also handles equality exactly. Total worst-case comparisons for this separable rank implementation are 3+2+3+2+2+2=14 after eta is available. Every row is recovered by intersecting its retained rank predicates. No extra direction scores or division needed for membership; for rational eta=n/d, test 2*d*g<3*n*s. Counts exclude computing eta, forming six sums, arithmetic bit costs and mask/list lookup/output. The optimizer itself may use the previous R164 15 distinct fractions or cross-products. No end-to-end runtime improvement or globally minimum decision tree is asserted.

## Complete exact feasibility proof

Normalize weights u=3eta(w)*w. All capacities scale by the same factor. Then min_W F(u)=1/3. Conversely any positive u with min_W F(u)=1/3 is itself a valid normalized weight. At fixed ratio write u=(17t,b,22t,d), t,b,d>0. The six capacities are (17t+b,39t,17t+d,22t+b,b+d,22t+d). The equality min_W F=1/3 is exactly the conjunction of: (i) some optimizer candidate a in W satisfies s_j>=3g_j(a) for every j, and (ii) for each a in W at least one channel j satisfies s_j<=3g_j(a). The second part is a finite union of weak upper boxes, one choice per row; zero gaps cannot be blocking because capacities are positive. As in R162, discard any upper vector coordinatewise contained in another, since componentwise minima under subsequent constraints preserve containment. This gives 29 maximal boxes; the sentinel in code only represents absent upper bounds and exceeds every finite upper bound.

For each of ten rows and each nonempty six-bit failure pattern m, impose s_j<=2g_j(v) for j in m and s_j>2g_j(v) for the others. Check feasibility with each possible optimizer lower vector from (i) and each maximal box from (ii), plus positivity. This is a finite union of systems of weak and strict integer affine inequalities in t,b,d. Fourier–Motzkin elimination of the three real variables is exact: pair each upper and lower bound, propagate strictness if either is strict, retain coefficient-zero rows, and reject only false constant rows. An unbounded side permits an appropriate finite value. Integer gcd normalization divides by a positive factor and equal left-and-right rows retain the stricter copy. Therefore the returned feasible pattern lists are complete over all positive real weights at this ratio, not weight sampling. Finite floating representation is only used for exactly represented integer operations: the replay checks each multiplication and subtraction for safe-integer range, normalizes by exact gcd, and reports the observed magnitude.

A test subset M preserves membership iff it intersects every feasible nonempty failure pattern. Every singleton feasible failure pattern forces its channel in every sufficient mask. In this certificate the set of singleton channels intersects every nonempty feasible pattern in each row, so it is the unique minimum mask, even when all six original channels are available. No scores of omitted channels need evaluation for this threshold output; their underlying gaps remain retained for other observers or future operations. This proves the threshold-only theorem for the original ratio.

The rank implementation is a second exact factorization: for each fixed channel, all its predicates are monotone in its gap, so a single strict rank recovers every listed predicate. This proves the 14-comparison upper bound. A further reduction using cross-channel dependence, or a joint optimizer/membership decision tree, remains open. The general failure-pattern algorithm applies to any finite candidate bank at any fixed rational ratio; no all-ratio table has been proved in this turn.

## Actual computation

The exact certificate below was executed, with 68984 feasibility queries, 924 weight-vector crosschecks and 1787940 full-domain direction checks. The latter is an additional replay of the full optimum and exact near set, including 126 row/weight equality cases. Result: PASS; all assertions passed.

```json
{
  "boxes": 29,
  "queries": 68984,
  "maxInt": 18716,
  "maxProduct": 3790072,
  "results": [
    {
      "v": [
        1,
        0,
        0
      ],
      "a": [
        1,
        3,
        7,
        2,
        6,
        4
      ],
      "patterns": [
        2,
        4,
        8,
        10,
        11,
        16,
        20
      ],
      "minimal": [
        30
      ],
      "k": 4
    },
    {
      "v": [
        1,
        3,
        -1
      ],
      "a": [
        4,
        9,
        2,
        5,
        6,
        11
      ],
      "patterns": [
        1,
        2,
        3,
        10,
        11,
        16,
        32,
        34,
        42,
        43,
        48,
        50
      ],
      "minimal": [
        51
      ],
      "k": 4
    },
    {
      "v": [
        4,
        -4,
        1
      ],
      "a": [
        2,
        6,
        2,
        4,
        0,
        4
      ],
      "patterns": [
        2,
        8,
        10,
        11
      ],
      "minimal": [
        10
      ],
      "k": 2
    },
    {
      "v": [
        4,
        -1,
        0
      ],
      "a": [
        1,
        0,
        11,
        1,
        12,
        11
      ],
      "patterns": [
        1,
        4,
        9,
        16,
        20,
        36,
        52
      ],
      "minimal": [
        21
      ],
      "k": 3
    },
    {
      "v": [
        5,
        -4,
        1
      ],
      "a": [
        1,
        3,
        5,
        2,
        6,
        8
      ],
      "patterns": [
        2,
        8,
        10,
        11,
        16,
        32,
        36,
        48,
        52
      ],
      "minimal": [
        58
      ],
      "k": 4
    },
    {
      "v": [
        5,
        -1,
        0
      ],
      "a": [
        2,
        3,
        4,
        1,
        6,
        7
      ],
      "patterns": [
        1,
        2,
        3,
        11,
        16,
        32,
        48
      ],
      "minimal": [
        51
      ],
      "k": 4
    },
    {
      "v": [
        6,
        -4,
        1
      ],
      "a": [
        0,
        0,
        12,
        0,
        12,
        12
      ],
      "patterns": [
        4,
        16,
        20,
        36,
        52
      ],
      "minimal": [
        20
      ],
      "k": 2
    },
    {
      "v": [
        6,
        -1,
        0
      ],
      "a": [
        3,
        6,
        3,
        3,
        0,
        3
      ],
      "patterns": [
        1,
        2,
        3,
        11
      ],
      "minimal": [
        3
      ],
      "k": 2
    },
    {
      "v": [
        7,
        -1,
        0
      ],
      "a": [
        4,
        9,
        10,
        5,
        6,
        1
      ],
      "patterns": [
        1,
        2,
        3,
        4,
        6,
        10,
        11,
        14,
        15,
        16,
        20,
        22
      ],
      "minimal": [
        23
      ],
      "k": 4
    },
    {
      "v": [
        9,
        -5,
        1
      ],
      "a": [
        0,
        3,
        6,
        3,
        6,
        3
      ],
      "patterns": [
        2,
        4,
        8,
        10,
        16,
        20
      ],
      "minimal": [
        30
      ],
      "k": 4
    }
  ],
  "lists": [
    [
      1,
      2,
      3,
      4
    ],
    [
      3,
      6,
      9
    ],
    [
      6,
      7,
      10,
      11,
      12
    ],
    [
      2,
      3,
      4
    ],
    [
      6,
      12
    ],
    [
      7,
      8,
      11
    ]
  ],
  "total": 33,
  "distinct": 20,
  "rankBound": 14,
  "weights": 924,
  "fullRowChecks": 1787940,
  "equalities": 126,
  "maxRank": 13,
  "rankTotal": 11310
}
```

## Reproduction

Execute the following standalone JavaScript (Node compatible). It enumerates the physical Port-10 population independently for crosschecks and uses all six raw gap values. The exact elimination is the load-bearing certificate.

```javascript
function certificate(){
 const T=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]];
 const W=[T[0],T[3],T[5],T[6],T[7],T[9]];
 const E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]], J=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
 function g([x,y,z]){const h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return J.map(([i,j])=>Math.abs(h[i]-h[j]))}
 const G=W.map(g),INF=1000000;
 if(G.flat().some(x=>3*x>=INF))throw Error("sentinel");
 const dominated=(a,b)=>a.every((x,j)=>x<=b[j]);
 function maximal(B){const S=[...new Map(B.map(b=>[String(b),b])).values()].sort((a,b)=>b.reduce((s,x)=>s+x,0)-a.reduce((s,x)=>s+x,0)),out=[];for(const x of S)if(!out.some(y=>dominated(x,y)))out.push(x);return out}
 let boxes=[Array(6).fill(INF)];for(const a of G){const next=[];for(const b of boxes)for(let j=0;j<6;j++)if(a[j]>0){const x=b.slice();x[j]=Math.min(x[j],3*a[j]);next.push(x)}boxes=maximal(next)}
 function gcd(a,b){a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b]}return a}
 let maxInt=0,maxProduct=0,queries=0;
 function clean(rows){const m=new Map;for(const a of rows){if(!a.slice(0,-2).some(Boolean)){if(a.at(-2)<0||(a.at(-2)===0&&a.at(-1)))return null;continue}
 const d=a.slice(0,-1).reduce(gcd,0)||1;const z=a.slice(0,-1).map(x=>x/d);maxInt=Math.max(maxInt,...z.map(Math.abs));if(!z.every(Number.isSafeInteger))throw Error("integer");const k=String(z);m.set(k,[...z,Math.max(a.at(-1),m.get(k)?.at(-1)||0)])}return [...m.values()]}
 function feasible(rows){queries++;rows=clean(rows);for(let k=0;k<3;k++){if(rows===null)return false;const p=rows.filter(a=>a[0]>0),n=rows.filter(a=>a[0]<0),out=rows.filter(a=>a[0]===0).map(a=>a.slice(1));for(const a of p)for(const b of n){const z=a.slice(1,-1).map((x,i)=>{const p=a[0]*b[i+1],q=b[0]*x;maxProduct=Math.max(maxProduct,Math.abs(p),Math.abs(q));if(!Number.isSafeInteger(p)||!Number.isSafeInteger(q)||!Number.isSafeInteger(p-q))throw Error("overflow");return p-q});out.push([...z,Math.max(a.at(-1),b.at(-1))])}rows=clean(out)}return rows!==null}
 const pos=[[-1,0,0,0,1],[0,-1,0,0,1],[0,0,-1,0,1]];
 const lower=(j,n,strict=0)=>[...E[j].map(x=>-x),-n,strict],upper=(j,n)=>[...E[j],n,0];
 const bits=x=>Array.from({length:6},(_,j)=>j).filter(j=>x&(1<<j));
 const results=[];
 for(const v of T){const a=g(v),patterns=[];for(let m=1;m<64;m++){if(bits(m).some(j=>a[j]===0))continue;
 const base=[...pos,...E.map((_,j)=>m&(1<<j)?upper(j,2*a[j]):lower(j,2*a[j],1))];
 let found=false;for(const u of G){if(found)break;const low=base.concat(u.map((x,j)=>lower(j,3*x)));for(const b of boxes){if(feasible(low.concat(b.flatMap((x,j)=>x===INF?[]:[upper(j,x)])))){found=true;break}}}if(found)patterns.push(m)}
 const valid=Array.from({length:64},(_,m)=>m).filter(m=>patterns.every(p=>(p&m)!==0));const k=Math.min(...valid.map(m=>bits(m).length));const minimal=valid.filter(m=>bits(m).length===k);
 if(minimal.length!==1||bits(minimal[0]).some(j=>!patterns.includes(1<<j)))throw Error("unique forced mask");
 results.push({v,a,patterns,minimal,k});
 }
 const lists=J.map((_,j)=>[...new Set(results.filter(r=>r.minimal[0]&(1<<j)).map(r=>r.a[j]))].sort((a,b)=>a-b));
 const total=results.reduce((s,r)=>s+r.k,0),distinct=lists.reduce((s,a)=>s+a.length,0),rankBound=lists.reduce((s,a)=>s+Math.ceil(Math.log2(a.length+1)),0);
 const pop=[];for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){const v=[x,y,z];if(!(v.find(t=>t!==0)>0)||Math.max(v.reduce((a,t)=>a+Math.max(t,0),0),v.reduce((a,t)=>a+Math.max(-t,0),0))>10)continue;pop.push({v,a:g(v)})}
 if(pop.length!==1935)throw Error("population");
 function score(a,s){let j=0;for(let k=1;k<6;k++)if(a[k]*s[j]>a[j]*s[k])j=k;return [a[j],s[j]]}
 function opt(rows,s){let u=score(rows[0],s);for(const a of rows.slice(1)){const v=score(a,s);if(v[0]*u[1]<u[0]*v[1])u=v}return u}
 const values=[1,2,3,5,8,13,21,34,55,89,144,233,377,610,987],weights=[];for(const t of [1,2,5,8])for(const B of values)for(const D of values)weights.push([17*t,B,22*t,D]);
 weights.push(...[20,8,4].flatMap(B=>[188,292,421,448,528,568,1584+8*B,2448+17*B].map(D=>[136,B,176,D])));
 let maxRank=0,equalities=0,rankTotal=0;
 const checkSet=(x,y)=>JSON.stringify(x.map(String).sort())===JSON.stringify(y.map(String).sort());
 const fullRows=pop.map(r=>r.a);
 for(const w of weights){const s=J.map(([i,j])=>w[i]+w[j]),[n,d]=opt(G,s),[N,D]=opt(fullRows,s);if(n*D!==N*d)throw Error("opt");
 let rankChecks=0;const pass=lists.map((a,j)=>{let lo=0,hi=a.length;while(lo<hi){let mid=(lo+hi)>>1;rankChecks++;if(2*d*a[mid]<3*n*s[j])lo=mid+1;else hi=mid}return new Set(a.slice(0,lo))});
 maxRank=Math.max(maxRank,rankChecks);rankTotal+=rankChecks;
 const actual=pop.filter(r=>{const [p,q]=score(r.a,s);if(2*p*d===3*n*q)equalities++;return 2*p*d<3*n*q}).map(r=>r.v);
 const predicted=results.filter(r=>bits(r.minimal[0]).every(j=>pass[j].has(r.a[j]))).map(r=>r.v);
 if(!checkSet(actual,predicted))throw Error(JSON.stringify({w,actual,predicted}));
 }
 if(total!==33||distinct!==20||rankBound!==14||maxRank>rankBound)throw Error("totals");
 return {boxes:boxes.length,queries,maxInt,maxProduct,results,lists,total,distinct,rankBound,weights:weights.length,fullRowChecks:weights.length*pop.length,equalities,maxRank,rankTotal};
}
console.log(JSON.stringify(certificate(),null,2));
```

## Continuation and control

Original own Researcher registration r2-20261124-0310-r155-own-session-v1 returned SUCCEEDED, EM-DIRECT-AE5AD5, RA-B60559848FD879270DCA6317; recovery metadata confirmed own session remains open, no run, execution_authorized=false. Original r2-20261124-1110-x6-cont-read-v1 returned FAILED / CANONICAL_REJECTED: unknown current immutable task publication, projection NO_CURRENT_FORMAL_TASK. Do not repeat or infer another task ID. Current active owner not established for a formal X6 Task; independent source preservation only, no CLAIM/Result/Review. Next: exact joint optimizer-plus-near decision tree, starting with reuse of optimizer comparisons or adaptive cross-channel rank tests; alternatively project the threshold-only masks across the ratio intervals from R162/R163. Independent mathematical review pending.
