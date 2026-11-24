# X6 R176 — Mandatory boundary supports and finite dual root census for arbitrary rational linear observations

2026-11-24. AUTHOR ANALYTIC REDUCTION / EXACT BIGINT COMPUTATION / NOT_REVIEWED. Independent informed static BRC observer research. Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f; R175@eadbd5e26a1a44f2bef376229785e7d2886f5938; exact bank and forms from R171@15032218f2f7c4c1474c123c2e2cefd46d7e0030. P000 V5 and ACTIVE worldview retained; auxiliary weight parameter chart, not native X6 spatial geometry or dynamics.

## Model and theorem

Port 10, w=(17t,B,22t,D), all three parameters strictly positive. Keep the original four heights, six capacities, all 1935 sign-reduced feasible integer directions, eta=min F_v, strict near set N={v:2F_v<3eta}. As in R175, a leaf selects any legal optimizer term from T (15 terms) and the exact near set. New model: each test is sign(a*t+b*B+c*D)>0 with arbitrary rational coefficients, fixed per node; one binary observation is counted, coefficient synthesis, input representation and bit/arithmetic costs are not included. R168 upper bound 7 carries over. R175 closed raw family is not reopened.

**Theorem.** At least 47 distinct linear boundary supports must occur as internal-node tests of every finite correct tree, even allowing arbitrary real coefficients. Hence at least 48 leaves and depth at least 6. The 47 supports give a necessary root condition for depth 6: each open root half must contain active subsegments of at most 31 distinct supports. This is strictly stronger in leaf-count terms than R174's 44. No claim yet of depth 7 for arbitrary linear observations.

## Proof

Normalize t+B+D=1 in the auxiliary chart. The R171 bank (V,W,M,T,H) is reused, with the R162–R164 reductions as inherited in R175. The optimizer is a min of maxima of retained T terms, so its ordering and ties are fixed by the signs of T-vs-T comparisons. Given an optimizer term, the near membership is the conjunction of its strict 3/2 inequalities against every raw channel of each candidate, so the signs of T-vs-H threshold comparisons fix N. Nonconstant cross-multiplied supports form 256 primitive lines. All are rational. Partition each such line by its exact intersections with all other supports and the three coordinate boundaries. On each open segment the sign vector, including equalities, is constant. In the positive cone use primitive integer ray p=u+v reduced by gcd for adjacent endpoints. K=1+max |l·m| over supports and coordinate axes gives positive rays Kp±l, with other signs unchanged since nonzero integer dot products have magnitude at least one. These represent both adjacent open cells; the boundary itself is p. The two adjacent open cells have unique optimizer terms (after identity of coincident expressions), as verified for this bank by the strict comparison signs; the code uses the actual intersection of all three masks, allowing ties. A segment is active if no single leaf output is legal simultaneously in both adjacent cells and the boundary. Label constancy extends this certificate to the whole open segment and arbitrary small neighborhoods of it.

Take an active segment on support l. If a finite correct tree never queries that support, its finitely many other supports intersect the segment in only finitely many points. At a remaining interior point a neighborhood lies in a single tree leaf, contradicting activity. The same argument inside either open root half forces a query in the corresponding subtree for each active support entering that half. Each depth-five child has at most 31 internal nodes. Distinct supports require distinct nodes. A tree with at least 47 internal nodes has at least 48 leaves. This proof is independent of the raw predicate family; it does not rely on leaf labels being disjoint when ties are legal.

The enumeration gives 47 active supports. For each support, keep the two extreme endpoints of the union of active segments in projective order. For a proposed root r, an active open subsegment lies in r·p>0 iff at least one extreme has strictly positive dot product; the same holds with negative. This remains true for disconnected active segments, by linearity on the normalized line and continuity near extreme endpoints. Thus all root capacities depend on ternary signs at just 51 distinct endpoint rays.

## Exhaustive finite reduction for root filtering

For every nonzero root coefficient vector r, use its ray on the coefficient sphere, up to antipodal symmetry (open-half capacity is symmetric). The 51 endpoint rays define great circles r·p_i=0. Their arrangement is essential since endpoints include the three coordinate axes. Every vertex is ±cross(p_i,p_j) for independent endpoints. Every open arc has a vertex at its closure, and every open chamber has a vertex in its closure (the arrangement spans 3-space). At each vertex r enumerate the exact vertex, and for each incident endpoint p_i the tangent directions ±cross(r,p_i) along its circle. This enumerates all incident open arcs using the lexicographic sign of (r·p,s cross(r,p_i)·p). For the adjacent open chambers append the term ±p_i·p; lexicographic sign equals sign of r+εs cross(r,p_i)+ε²u p_i for sufficiently small positive rational ε. No other distinct circle vanishes along that tangent except the one being crossed, since incident circle normals are distinct projective rays. This covers every face, including concurrent intersections. Deduplicate ordered positive/negative endpoint masks up to exchange. Zero signs are retained. This gives exactly 4249 antipodal ternary root classes for the endpoint carrier; 3638 fail the 31-support capacity test and 611 survive. The minimum possible max child support count is 27. This is not a measure or probability on roots. The root boundary's equality convention can add obligations, so using open halves is a safe necessary condition, not sufficiency.

A direct cross-through test found no pair of active supports simultaneously active immediately on both sides of their intersection; the simple crossing-matching route to duplicate-support lower bounds gives zero here. Next: condition the active segments on actual root geometry and study second-layer support capacity, or construct an unrestricted depth-six tree. A finite sample obstruction may use all linear dichotomies, not only the original 884 raw queries. Do not infer impossibility from the present 611 survivors.

## Actual verification

Exact BigInt replay below, independently scores all 1935 directions at the first and last active segments of each support (first segment is also checked during scanning). These 423 representative evaluations = 818505 direction scores, with possible repeated points. This cross-check verifies local witness outputs, while completeness of the active-segment census inherits the bank reductions. All 256 lines, 21842 open segments, 1574 active elementary segments, 47 distinct supports, 51 endpoint rays, and all dual face sign patterns enumerated. No timing or native physical observation claim.

```json
{
  "lines": 256,
  "K": "479958",
  "directions": 1935,
  "segments": 21842,
  "changes": 1574,
  "tieOnly": 0,
  "active": 47,
  "crossingEdges": 0,
  "fullDirectionChecks": 818505,
  "endpointRays": 51,
  "dualStates": 4249,
  "oneSideEndpointStates": 7,
  "rootSurvivors": 611,
  "rootExcluded": 3638,
  "minMaxSupport": 27,
  "activeLines": [
    {
      "normal": [
        "187",
        "12",
        "-1"
      ],
      "segments": 9,
      "endpoints": [
        [
          "0",
          "1",
          "12"
        ],
        [
          "1",
          "17",
          "391"
        ]
      ]
    },
    {
      "normal": [
        "204",
        "11",
        "-1"
      ],
      "segments": 9,
      "endpoints": [
        [
          "0",
          "1",
          "11"
        ],
        [
          "1",
          "17",
          "391"
        ]
      ]
    },
    {
      "normal": [
        "5",
        "-2",
        "0"
      ],
      "segments": 51,
      "endpoints": [
        [
          "2",
          "5",
          "73"
        ],
        [
          "2",
          "5",
          "5"
        ]
      ]
    },
    {
      "normal": [
        "9",
        "-1",
        "0"
      ],
      "segments": 4,
      "endpoints": [
        [
          "1",
          "9",
          "74"
        ],
        [
          "1",
          "9",
          "69"
        ]
      ]
    },
    {
      "normal": [
        "85",
        "7",
        "-2"
      ],
      "segments": 10,
      "endpoints": [
        [
          "1",
          "9",
          "74"
        ],
        [
          "3",
          "17",
          "187"
        ]
      ]
    },
    {
      "normal": [
        "51",
        "2",
        "-1"
      ],
      "segments": 9,
      "endpoints": [
        [
          "1",
          "9",
          "69"
        ],
        [
          "1",
          "0",
          "51"
        ]
      ]
    },
    {
      "normal": [
        "0",
        "1",
        "-1"
      ],
      "segments": 2,
      "endpoints": [
        [
          "2",
          "5",
          "5"
        ],
        [
          "1",
          "0",
          "0"
        ]
      ]
    },
    {
      "normal": [
        "34",
        "1",
        "-1"
      ],
      "segments": 7,
      "endpoints": [
        [
          "2",
          "5",
          "73"
        ],
        [
          "1",
          "0",
          "34"
        ]
      ]
    },
    {
      "normal": [
        "187",
        "20",
        "-9"
      ],
      "segments": 5,
      "endpoints": [
        [
          "6",
          "15",
          "158"
        ],
        [
          "1",
          "1",
          "23"
        ]
      ]
    },
    {
      "normal": [
        "68",
        "1",
        "-3"
      ],
      "segments": 8,
      "endpoints": [
        [
          "2",
          "5",
          "47"
        ],
        [
          "3",
          "0",
          "68"
        ]
      ]
    },
    {
      "normal": [
        "176",
        "22",
        "-9"
      ],
      "segments": 4,
      "endpoints": [
        [
          "6",
          "15",
          "154"
        ],
        [
          "19",
          "28",
          "440"
        ]
      ]
    },
    {
      "normal": [
        "22",
        "0",
        "-1"
      ],
      "segments": 47,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "1",
          "17",
          "22"
        ]
      ]
    },
    {
      "normal": [
        "61",
        "0",
        "-1"
      ],
      "segments": 78,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "1",
          "17",
          "61"
        ]
      ]
    },
    {
      "normal": [
        "74",
        "0",
        "-1"
      ],
      "segments": 14,
      "endpoints": [
        [
          "1",
          "9",
          "74"
        ],
        [
          "1",
          "4",
          "74"
        ]
      ]
    },
    {
      "normal": [
        "126",
        "0",
        "-1"
      ],
      "segments": 103,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "1",
          "30",
          "126"
        ]
      ]
    },
    {
      "normal": [
        "4",
        "-1",
        "0"
      ],
      "segments": 35,
      "endpoints": [
        [
          "1",
          "4",
          "152"
        ],
        [
          "1",
          "4",
          "74"
        ]
      ]
    },
    {
      "normal": [
        "17",
        "-1",
        "0"
      ],
      "segments": 44,
      "endpoints": [
        [
          "0",
          "0",
          "1"
        ],
        [
          "1",
          "17",
          "22"
        ]
      ]
    },
    {
      "normal": [
        "156",
        "-1",
        "-1"
      ],
      "segments": 46,
      "endpoints": [
        [
          "1",
          "4",
          "152"
        ],
        [
          "1",
          "30",
          "126"
        ]
      ]
    },
    {
      "normal": [
        "69",
        "0",
        "-1"
      ],
      "segments": 16,
      "endpoints": [
        [
          "1",
          "17",
          "69"
        ],
        [
          "1",
          "9",
          "69"
        ]
      ]
    },
    {
      "normal": [
        "9",
        "0",
        "-1"
      ],
      "segments": 47,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "1",
          "17",
          "9"
        ]
      ]
    },
    {
      "normal": [
        "235",
        "0",
        "-3"
      ],
      "segments": 84,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "3",
          "77",
          "235"
        ]
      ]
    },
    {
      "normal": [
        "87",
        "0",
        "-1"
      ],
      "segments": 107,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "1",
          "17",
          "87"
        ]
      ]
    },
    {
      "normal": [
        "104",
        "-1",
        "-1"
      ],
      "segments": 60,
      "endpoints": [
        [
          "1",
          "4",
          "100"
        ],
        [
          "3",
          "77",
          "235"
        ]
      ]
    },
    {
      "normal": [
        "38",
        "0",
        "-3"
      ],
      "segments": 57,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "3",
          "40",
          "38"
        ]
      ]
    },
    {
      "normal": [
        "5",
        "0",
        "-2"
      ],
      "segments": 72,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "2",
          "5",
          "5"
        ]
      ]
    },
    {
      "normal": [
        "39",
        "-1",
        "-1"
      ],
      "segments": 50,
      "endpoints": [
        [
          "3",
          "1",
          "116"
        ],
        [
          "1",
          "17",
          "22"
        ]
      ]
    },
    {
      "normal": [
        "40",
        "0",
        "-3"
      ],
      "segments": 63,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "3",
          "38",
          "40"
        ]
      ]
    },
    {
      "normal": [
        "26",
        "-1",
        "-1"
      ],
      "segments": 39,
      "endpoints": [
        [
          "2",
          "5",
          "47"
        ],
        [
          "3",
          "53",
          "25"
        ]
      ]
    },
    {
      "normal": [
        "25",
        "0",
        "-3"
      ],
      "segments": 52,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "3",
          "53",
          "25"
        ]
      ]
    },
    {
      "normal": [
        "83",
        "0",
        "-2"
      ],
      "segments": 69,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "2",
          "34",
          "83"
        ]
      ]
    },
    {
      "normal": [
        "102",
        "-7",
        "-1"
      ],
      "segments": 14,
      "endpoints": [
        [
          "1",
          "4",
          "74"
        ],
        [
          "3",
          "17",
          "187"
        ]
      ]
    },
    {
      "normal": [
        "204",
        "-11",
        "1"
      ],
      "segments": 51,
      "endpoints": [
        [
          "0",
          "1",
          "11"
        ],
        [
          "1",
          "30",
          "126"
        ]
      ]
    },
    {
      "normal": [
        "395",
        "0",
        "-2"
      ],
      "segments": 119,
      "endpoints": [
        [
          "0",
          "1",
          "0"
        ],
        [
          "2",
          "73",
          "395"
        ]
      ]
    },
    {
      "normal": [
        "289",
        "18",
        "-1"
      ],
      "segments": 10,
      "endpoints": [
        [
          "0",
          "1",
          "18"
        ],
        [
          "1",
          "17",
          "595"
        ]
      ]
    },
    {
      "normal": [
        "66",
        "2",
        "-1"
      ],
      "segments": 11,
      "endpoints": [
        [
          "1",
          "4",
          "74"
        ],
        [
          "1",
          "0",
          "66"
        ]
      ]
    },
    {
      "normal": [
        "132",
        "5",
        "-1"
      ],
      "segments": 16,
      "endpoints": [
        [
          "1",
          "17",
          "217"
        ],
        [
          "1",
          "0",
          "132"
        ]
      ]
    },
    {
      "normal": [
        "44",
        "1",
        "-1"
      ],
      "segments": 9,
      "endpoints": [
        [
          "1",
          "17",
          "61"
        ],
        [
          "1",
          "11",
          "55"
        ]
      ]
    },
    {
      "normal": [
        "88",
        "3",
        "-1"
      ],
      "segments": 7,
      "endpoints": [
        [
          "1",
          "4",
          "100"
        ],
        [
          "1",
          "0",
          "88"
        ]
      ]
    },
    {
      "normal": [
        "88",
        "7",
        "-3"
      ],
      "segments": 5,
      "endpoints": [
        [
          "1",
          "17",
          "69"
        ],
        [
          "1",
          "11",
          "55"
        ]
      ]
    },
    {
      "normal": [
        "132",
        "-7",
        "-1"
      ],
      "segments": 14,
      "endpoints": [
        [
          "1",
          "9",
          "69"
        ],
        [
          "1",
          "11",
          "55"
        ]
      ]
    },
    {
      "normal": [
        "153",
        "8",
        "-1"
      ],
      "segments": 7,
      "endpoints": [
        [
          "1",
          "9",
          "225"
        ],
        [
          "1",
          "0",
          "153"
        ]
      ]
    },
    {
      "normal": [
        "153",
        "5",
        "-4"
      ],
      "segments": 1,
      "endpoints": [
        [
          "3",
          "1",
          "116"
        ],
        [
          "4",
          "0",
          "153"
        ]
      ]
    },
    {
      "normal": [
        "117",
        "-2",
        "-2"
      ],
      "segments": 42,
      "endpoints": [
        [
          "2",
          "5",
          "112"
        ],
        [
          "2",
          "34",
          "83"
        ]
      ]
    },
    {
      "normal": [
        "198",
        "8",
        "-1"
      ],
      "segments": 5,
      "endpoints": [
        [
          "1",
          "4",
          "230"
        ],
        [
          "1",
          "0",
          "198"
        ]
      ]
    },
    {
      "normal": [
        "198",
        "5",
        "-4"
      ],
      "segments": 11,
      "endpoints": [
        [
          "2",
          "8",
          "109"
        ],
        [
          "2",
          "0",
          "99"
        ]
      ]
    },
    {
      "normal": [
        "306",
        "17",
        "-1"
      ],
      "segments": 8,
      "endpoints": [
        [
          "1",
          "17",
          "595"
        ],
        [
          "1",
          "0",
          "306"
        ]
      ]
    },
    {
      "normal": [
        "234",
        "-1",
        "-1"
      ],
      "segments": 43,
      "endpoints": [
        [
          "1",
          "4",
          "230"
        ],
        [
          "2",
          "73",
          "395"
        ]
      ]
    }
  ]
}
```

## Reproduction

Extract the following JavaScript and run with Node.js. Integer sign and score operations use BigInt; small direction indices and masks are bounded integers.

```js
function research(){
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],W=[0,3,5,6,7,9],M=[30,51,42,21,58,51,20,7,23,30],E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]].map(x=>x.map(BigInt));
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a,norm=p=>{let d=p.reduce(gcd,0n);return d?p.map(x=>x/d):p},canon=p=>{p=norm(p);return (p.find(x=>x)??0n)<0n?p.map(x=>-x):p},uniq=a=>[...new Map(a.map(p=>[p.join(),p])).values()];
const gaps=([x,y,z])=>{let h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z],g=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)g.push(BigInt(Math.abs(h[j]-h[i])));return g};
const G=V.map(gaps),terms=(rows,mask)=>{let s=new Map();for(let i of rows)G[i].forEach((g,j)=>{if(g&&(!mask||(M[i]>>j&1)))s.set(`${j},${g}`,[j,g])});return [...s.values()].sort((a,b)=>a[0]-b[0]||Number(a[1]-b[1]))},T=terms(W,true),H=terms(V.map((_,i)=>i),false);
const line=(a,b,k,l)=>canon(E[b[0]].map((x,i)=>k*a[1]*x-l*b[1]*E[a[0]][i]));
let L=[];for(let a of T){for(let b of T)L.push(line(a,b,1n,1n));for(let b of H)L.push(line(a,b,3n,2n))}
L=uniq(L.filter(q=>q.some(x=>x<0n)&&q.some(x=>x>0n)));const axes=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]],all=L.concat(axes);const abs=x=>x<0n?-x:x;let K=1n;for(let l of L)for(let m of all)if(abs(dot(l,m))>=K)K=abs(dot(l,m))+1n;
let full=[];for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){let v=[x,y,z];if((v.find(x=>x)??0)>0&&Math.max(v.reduce((a,x)=>a+Math.max(x,0),0),v.reduce((a,x)=>a+Math.max(-x,0),0))<=10)full.push(v)}
const GG=full.map(gaps),vi=new Map(V.map((v,i)=>[v.join(),i]));
let checks=0;
function label(p,verify=false){let s=E.map(e=>dot(e,p));function score(row){let a=0n,b=1n;for(let j=0;j<6;j++)if(row[j]*b>a*s[j]){a=row[j];b=s[j]}return [a,b]}let fs=G.map(score),[a,b]=fs[W[0]];for(let i of W){let [c,d]=fs[i];if(c*b<a*d){a=c;b=d}}let m=0,n=0;for(let i=0;i<T.length;i++){let [j,g]=T[i];if(g*b===a*s[j])m|=1<<i}for(let i=0;i<fs.length;i++)if(2n*fs[i][0]*b<3n*a*fs[i][1])n|=1<<i;if(!m)throw Error('missing optimizer');if(verify){let f=GG.map(score),[aa,bb]=f[0];for(let [c,d] of f)if(c*bb<aa*d){aa=c;bb=d}if(aa*b!==a*bb)throw Error('eta');let nn=0;for(let i=0;i<f.length;i++)if(2n*f[i][0]*bb<3n*aa*f[i][1]){let k=vi.get(full[i].join());if(k===undefined)throw Error('near outside bank');nn|=1<<k}if(nn!==n)throw Error('near');checks+=f.length}return [m,n]}
let active=[],segments=0,changes=0,tieOnly=0;const den=p=>p.reduce((s,x)=>s+x,0n),cmp=(a,b,i)=>{let x=a[i]*den(b)-b[i]*den(a);return x<0n?-1:x>0n?1:0};for(let l of L){let ps=uniq(all.map(m=>canon(cross(l,m))).filter(p=>p.some(x=>x>0n)&&p.every(x=>x>=0n)));let ax=[0,1,2].find(i=>ps.some(p=>cmp(p,ps[0],i)));if(ax===undefined)continue;ps.sort((a,b)=>cmp(a,b,ax));let act=[];for(let i=0;i+1<ps.length;i++){let p=norm(ps[i].map((x,j)=>x+ps[i+1][j]));if(p.some(x=>x<=0n))continue;let pp=p.map((x,j)=>K*x+l[j]),pm=p.map((x,j)=>K*x-l[j]);if(pp.some(x=>x<=0n)||pm.some(x=>x<=0n))throw Error('perturbation');let a=label(pp),b=label(pm),c=label(p);segments++;if(a[1]!==b[1]||c[1]!==a[1]||!(a[0]&b[0]&c[0])){changes++;if(a[1]===b[1]&&(a[0]&b[0]))tieOnly++;act.push([ps[i],ps[i+1]]);if(act.length===1){label(pp,true);label(pm,true);label(p,true);}}}if(act.length){let ends=[act[0][0],act.at(-1)[1]];for(let [u,v] of [act[0],act.at(-1)]){let p=norm(u.map((x,j)=>x+v[j]));label(p,true);label(p.map((x,j)=>K*x+l[j]),true);label(p.map((x,j)=>K*x-l[j]),true)}active.push({l,ax,act,ends})}}
let graph=[];for(let i=0;i<active.length;i++)for(let j=i+1;j<active.length;j++){let a=active[i],b=active[j],p=canon(cross(a.l,b.l));if(p.some(x=>x<=0n))continue;let both=z=>z.act.some(([u,v])=>cmp(u,p,z.ax)<0&&cmp(v,p,z.ax)>=0)&&z.act.some(([u,v])=>cmp(u,p,z.ax)<=0&&cmp(v,p,z.ax)>0);if(both(a)&&both(b))graph.push([i,j])}
const P=uniq(active.flatMap(x=>x.ends)),I=new Map(P.map((p,i)=>[p.join(),i])),edges=active.map(x=>x.ends.map(p=>1n<<BigInt(I.get(p.join())))),sg=x=>x>0n?1:x<0n?-1:0;
let states=new Map();function record(r,t=null,p=null,s=1,u=1){let a=0n,b=0n;for(let i=0;i<P.length;i++){let x=sg(dot(r,P[i]));if(!x&&t)x=s*sg(dot(t,P[i]));if(!x&&p)x=u*sg(dot(p,P[i]));if(x>0)a|=1n<<BigInt(i);if(x<0)b|=1n<<BigInt(i)}let key=a<b?`${a},${b}`:`${b},${a}`;if(!states.has(key))states.set(key,[a,b]);}
for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){let r=cross(P[i],P[j]);if(!r.some(Boolean))continue;record(r);for(let k=0;k<P.length;k++)if(!dot(r,P[k])){let t=cross(r,P[k]);for(let s of [-1,1]){record(r,t,null,s);for(let u of [-1,1])record(r,t,P[k],s,u)}}}
let good=0,constant=0,mins=99;for(let [a,b] of states.values()){let x=edges.filter(e=>e.some(v=>a&v)).length,y=edges.filter(e=>e.some(v=>b&v)).length;if(!a||!b)constant++;if(x<=31&&y<=31)good++;mins=Math.min(mins,Math.max(x,y))}
return {lines:L.length,K:String(K),directions:full.length,segments,changes,tieOnly,active:active.length,crossingEdges:graph.length,fullDirectionChecks:checks,endpointRays:P.length,dualStates:states.size,oneSideEndpointStates:constant,rootSurvivors:good,rootExcluded:states.size-good,minMaxSupport:mins,activeLines:active.map(x=>({normal:x.l.map(String),segments:x.act.length,endpoints:x.ends.map(p=>p.map(String))}))}
}
console.log(JSON.stringify(research(),null,2));
```

## Control provenance

Current read-only request r2-20261124-2210-x6-current-read-v1 returned SUCCEEDED/error=null, observed 2026-11-24T14:10:32.600602Z, Source 0bccba3f0e29647572d02da3b2af7c991fb16e3e, NO_CANONICAL_PUBLICATION_DIRECTORY. Native operational owner projection not evaluated; execution_authorized=false. Gateway identity-only check succeeded, but current own Researcher SID/private binding unconfirmed; historical lane provenance EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317 is not current execution authority. No new CLAIM or task mutation. Source note preservation only; Activity association pending own binding verification.
