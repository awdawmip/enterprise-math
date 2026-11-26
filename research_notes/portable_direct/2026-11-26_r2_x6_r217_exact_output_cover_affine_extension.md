# X6 R217 — exact output-cover number, unrestricted Boolean depth and affine extension

2026-11-26. AUTHOR PROOF / EXACT BIGINT REPLAY / NOT_REVIEWED. Independent informed static six-pair BRC observer research, no native dynamics claim, no formal Task or CLAIM. P000 V5 and ACTIVE worldview retained. Same frozen Port 10, 1935 unoriented directions, weights (17t,B,22t,D), t,B,D>0. Leaf returns a legal optimizer term among the same 15 T and the complete strict 3/2 near mask. Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd, R122@1e4ab68c4f9c91bc60c07017acc57be20829832f, R168@ee8eb26824479ec56924b81871b0cd7b38bee8ce (checker af4ab6561827525b3c4d1b58f502522d3e39b4de), R176@c665f671a31d2bfeffb151e06bb308628110029e, R216@0b5f89c35844559a07c3cd49c25f882ae1c7472f. Reuse exact bank and face-coverage proof; not repinning scientific inputs.

## 1. Exact output-cover number 35

For each input p, let M(p) be the mask of legal optimizer terms and N(p) the full near mask. For a given N let A_N={M(p):N(p)=N}. Define the minimum output cover k_N=min{|S|: S intersects every M in A_N}. Every correct tree needs at least sum k_N distinct leaf outputs. Conversely in the model allowing an arbitrary Boolean-valued function of the original comparison sign vector as one query, choose one legal output from a minimum cover (e.g. the least legal index). Encode the finite chosen output set by distinct binary words of length ceil(log2(sum k_N)); query one bit at a time and decode. Each bit is a finite Boolean combination of the original oriented strict comparisons (sign zero resolved by both directions), not necessarily a single polynomial sign. Therefore the exact binary depth in this enlarged Boolean-oracle model is ceil(log2(sum k_N)). This is a count of composite oracle calls, not a cost bound for implementing a composite predicate.

Independent JS BigInt implementation of the R168 exact face construction and rational scoring found the same 197 lines, 7311 polygons, 27611 strictly positive face representatives, 16 near masks and 162 distinct joint labels. For every one of the 16 near masks, the set S_N of singleton optimizer labels hits every admissible mask in A_N. Every singleton forces its own output, so k_N=|S_N| exactly. Sum k_N=35. Hence 35 is the minimum number of distinct admissible leaf outputs and in the unrestricted composite Boolean-observation model D=6. The lower bound holds for ANY binary test model with fixed leaf outputs, even nonlinear. The upper bound is ONLY for the stated composite Boolean oracle; it does not show a depth-six tree whose individual queries are polynomial signs, nor a speedup in elementary comparisons. The actual elementary linear result from R216 remains 7 (author-level, independent review pending).

All 35 singleton witnesses were separately evaluated against the entire 1935-direction population (67,725 exact direction scores), including all six channels; each had the asserted singleton term and full near mask, with no outsider. Thus the six-binary-observation lower bound from these witnesses does not need the global bank coverage for the witness step. The global upper/output cover uses the inherited R168/R162–R165 coverage proof.

## 2. Affine extension (no new census)

The output contract is invariant under positive scaling of p=(t,B,D): the eta term identities and strict near set are unchanged. Restrict any correct finite affine-query tree on the positive cone to t+B+D=1. Each node tests a·p+b>0, which on this section equals (a+b(1,1,1))·p>0. Replace that node by the corresponding homogeneous linear test. Constant-zero and constant-sign nodes can be removed. By homogeneity the resulting tree works on the whole cone, with no larger depth, including ties. Thus the arbitrary real affine binary model has exactly the same optimum as the homogeneous linear model: D_affine=D_linear=7, conditional on the R216 closure. This does not depend on a limiting argument or a scale bound.

## 3. Polynomial degree budget

On the normalized open triangle, each polynomial query restricts to a polynomial in two independent auxiliary chart coordinates; identically zero restrictions are removable constant tests. For any R176 mandatory active support line, some nonzero restricted query polynomial must vanish identically along that line. Otherwise each has only finitely many zeros along its open active segment; choose a point avoiding all of them. All query signs then stay constant in a neighborhood, forcing one illegal leaf output by the R176 local activity argument. A polynomial vanishing on an open line interval has the corresponding affine linear factor (change affine coordinates and use the univariate identity theorem). Distinct supports give distinct nonassociate factors. Therefore sum of the degrees of all nonconstant restricted node polynomials is at least 47. With maximum degree k and binary depth d, k(2^d-1)>=47. Independently the 35 singleton witnesses force d>=6 for any binary model. These are necessary conditions, not a construction for polynomial queries. The next discriminating problem is depth six with individual quadratic or higher polynomial sign tests; the composite-Boolean construction cannot be relabeled polynomial sign without proof.

## 4. Actual evidence and reproduction

Exact output (zero-based T indices; near masks follow R168 V order):
```json
{
  "lines": 197,
  "cells": 7311,
  "points": 27611,
  "terms": [
    [
      0,
      1
    ],
    [
      0,
      2
    ],
    [
      0,
      3
    ],
    [
      1,
      3
    ],
    [
      1,
      6
    ],
    [
      2,
      3
    ],
    [
      2,
      6
    ],
    [
      2,
      7
    ],
    [
      2,
      11
    ],
    [
      2,
      12
    ],
    [
      3,
      2
    ],
    [
      3,
      3
    ],
    [
      4,
      6
    ],
    [
      4,
      12
    ],
    [
      5,
      7
    ]
  ],
  "nearGroups": 16,
  "jointLabels": 162,
  "singleton": 35,
  "minOutputs": 35,
  "directions": 1935,
  "fullChecks": 67725,
  "rows": [
    {
      "near": 49,
      "labels": 4,
      "mandatory": 1024,
      "cover": 1024,
      "size": 1,
      "trials": 8,
      "masks": [
        1024,
        1032,
        5120,
        5256
      ],
      "witnesses": [
        [
          1024,
          [
            "18",
            "26",
            "1241"
          ]
        ]
      ]
    },
    {
      "near": 64,
      "labels": 3,
      "mandatory": 8704,
      "cover": 8704,
      "size": 2,
      "trials": 1,
      "masks": [
        512,
        8192,
        8704
      ],
      "witnesses": [
        [
          512,
          [
            "3",
            "53",
            "1821"
          ]
        ],
        [
          8192,
          [
            "3",
            "1",
            "935"
          ]
        ]
      ]
    },
    {
      "near": 72,
      "labels": 19,
      "mandatory": 8961,
      "cover": 8961,
      "size": 4,
      "trials": 16,
      "masks": [
        1,
        256,
        258,
        260,
        512,
        513,
        1280,
        2304,
        8192,
        8193,
        8194,
        8448,
        8450,
        8704,
        8705,
        9216,
        9472,
        9728,
        10496
      ],
      "witnesses": [
        [
          1,
          [
            "7",
            "123",
            "2783"
          ]
        ],
        [
          256,
          [
            "2",
            "1049",
            "395"
          ]
        ],
        [
          512,
          [
            "8",
            "140",
            "3797"
          ]
        ],
        [
          8192,
          [
            "43",
            "1520",
            "8542"
          ]
        ]
      ]
    },
    {
      "near": 89,
      "labels": 2,
      "mandatory": 8192,
      "cover": 8192,
      "size": 1,
      "trials": 2,
      "masks": [
        8192,
        8200
      ],
      "witnesses": [
        [
          8192,
          [
            "4",
            "1",
            "620"
          ]
        ]
      ]
    },
    {
      "near": 121,
      "labels": 10,
      "mandatory": 9216,
      "cover": 9216,
      "size": 2,
      "trials": 8,
      "masks": [
        1024,
        1032,
        1280,
        1288,
        1536,
        1544,
        8192,
        8200,
        9216,
        9224
      ],
      "witnesses": [
        [
          1024,
          [
            "41",
            "51",
            "3776"
          ]
        ],
        [
          8192,
          [
            "9",
            "147",
            "1943"
          ]
        ]
      ]
    },
    {
      "near": 132,
      "labels": 18,
      "mandatory": 52,
      "cover": 52,
      "size": 3,
      "trials": 16,
      "masks": [
        4,
        16,
        20,
        32,
        36,
        48,
        52,
        68,
        80,
        84,
        4112,
        4128,
        4144,
        8208,
        8224,
        8240,
        16388,
        16404
      ],
      "witnesses": [
        [
          4,
          [
            "6",
            "1",
            "11"
          ]
        ],
        [
          16,
          [
            "3",
            "10",
            "9"
          ]
        ],
        [
          32,
          [
            "7",
            "2",
            "1"
          ]
        ]
      ]
    },
    {
      "near": 164,
      "labels": 3,
      "mandatory": 16,
      "cover": 16,
      "size": 1,
      "trials": 4,
      "masks": [
        16,
        4112,
        8208
      ],
      "witnesses": [
        [
          16,
          [
            "11",
            "193",
            "97"
          ]
        ]
      ]
    },
    {
      "near": 561,
      "labels": 40,
      "mandatory": 22730,
      "cover": 22730,
      "size": 7,
      "trials": 4,
      "masks": [
        2,
        8,
        10,
        12,
        64,
        68,
        72,
        76,
        128,
        130,
        136,
        138,
        140,
        2048,
        2056,
        2184,
        4096,
        4098,
        4100,
        4160,
        4164,
        4224,
        4226,
        6144,
        6216,
        6272,
        8200,
        8256,
        8264,
        8328,
        16384,
        16392,
        16396,
        18432,
        18440,
        20480,
        20484,
        20490,
        22528,
        24584
      ],
      "witnesses": [
        [
          2,
          [
            "4",
            "35",
            "275"
          ]
        ],
        [
          8,
          [
            "12",
            "1552",
            "775"
          ]
        ],
        [
          64,
          [
            "2",
            "44",
            "83"
          ]
        ],
        [
          128,
          [
            "74",
            "439",
            "4809"
          ]
        ],
        [
          2048,
          [
            "36",
            "610",
            "2195"
          ]
        ],
        [
          4096,
          [
            "2",
            "18",
            "99"
          ]
        ],
        [
          16384,
          [
            "44",
            "500",
            "2509"
          ]
        ]
      ]
    },
    {
      "near": 569,
      "labels": 3,
      "mandatory": 8,
      "cover": 8,
      "size": 1,
      "trials": 4,
      "masks": [
        8,
        12,
        8200
      ],
      "witnesses": [
        [
          8,
          [
            "2",
            "352",
            "159"
          ]
        ]
      ]
    },
    {
      "near": 633,
      "labels": 25,
      "mandatory": 8456,
      "cover": 8456,
      "size": 3,
      "trials": 16,
      "masks": [
        8,
        10,
        12,
        256,
        260,
        264,
        266,
        268,
        520,
        522,
        2056,
        2312,
        8192,
        8194,
        8196,
        8200,
        8202,
        8204,
        8448,
        8452,
        8456,
        8704,
        8706,
        10240,
        10760
      ],
      "witnesses": [
        [
          8,
          [
            "13",
            "2514",
            "1132"
          ]
        ],
        [
          256,
          [
            "2",
            "795",
            "265"
          ]
        ],
        [
          8192,
          [
            "9",
            "260",
            "1202"
          ]
        ]
      ]
    },
    {
      "near": 676,
      "labels": 3,
      "mandatory": 16,
      "cover": 16,
      "size": 1,
      "trials": 4,
      "masks": [
        16,
        4112,
        8208
      ],
      "witnesses": [
        [
          16,
          [
            "53",
            "745",
            "646"
          ]
        ]
      ]
    },
    {
      "near": 689,
      "labels": 1,
      "mandatory": 4096,
      "cover": 4096,
      "size": 1,
      "trials": 1,
      "masks": [
        4096
      ],
      "witnesses": [
        [
          4096,
          [
            "8",
            "20",
            "421"
          ]
        ]
      ]
    },
    {
      "near": 692,
      "labels": 3,
      "mandatory": 16,
      "cover": 16,
      "size": 1,
      "trials": 4,
      "masks": [
        16,
        4112,
        8208
      ],
      "witnesses": [
        [
          16,
          [
            "35",
            "488",
            "444"
          ]
        ]
      ]
    },
    {
      "near": 693,
      "labels": 23,
      "mandatory": 4180,
      "cover": 4180,
      "size": 4,
      "trials": 16,
      "masks": [
        4,
        16,
        20,
        64,
        80,
        144,
        148,
        4096,
        4100,
        4112,
        4116,
        4160,
        4176,
        4224,
        4228,
        4240,
        6144,
        8208,
        8256,
        8272,
        16400,
        20480,
        20496
      ],
      "witnesses": [
        [
          4,
          [
            "5",
            "8",
            "117"
          ]
        ],
        [
          16,
          [
            "11",
            "97",
            "191"
          ]
        ],
        [
          64,
          [
            "7",
            "123",
            "156"
          ]
        ],
        [
          4096,
          [
            "90",
            "204",
            "3319"
          ]
        ]
      ]
    },
    {
      "near": 695,
      "labels": 1,
      "mandatory": 4,
      "cover": 4,
      "size": 1,
      "trials": 1,
      "masks": [
        4
      ],
      "witnesses": [
        [
          4,
          [
            "104",
            "149",
            "2437"
          ]
        ]
      ]
    },
    {
      "near": 951,
      "labels": 4,
      "mandatory": 4100,
      "cover": 4100,
      "size": 2,
      "trials": 2,
      "masks": [
        4,
        132,
        4096,
        4100
      ],
      "witnesses": [
        [
          4,
          [
            "10",
            "1",
            "228"
          ]
        ],
        [
          4096,
          [
            "7",
            "2",
            "242"
          ]
        ]
      ]
    }
  ]
}
```

Standalone Node.js exact replay, using frozen R168 banks; computes all label masks, output covers, 35 singleton witnesses, and full population witness checks:
```javascript
function run(){
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],M=[30,51,10,21,58,51,20,3,23,30],W=[0,3,5,6,7,9],MASK=[30,51,42,21,58,51,20,7,23,30],E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]].map(a=>a.map(BigInt));
function gaps([x,y,z]){let h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z],g=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)g.push(Math.abs(h[i]-h[j]));return g}
const G=V.map(gaps),key=a=>a.join(),uniq=a=>[...new Map(a.map(x=>[key(x),x])).values()],gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a,norm=a=>{let g=a.reduce(gcd,0n);return g?a.map(x=>x/g):a},canon=a=>{a=norm(a);return a.find(x=>x)!==undefined&&a.find(x=>x)<0n?a.map(x=>-x):a},dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),add=(a,b)=>a.map((x,i)=>x+b[i]);
const bank=(inds,mask)=>uniq(inds.flatMap(i=>G[i].flatMap((g,j)=>g&&(mask[i]>>j&1)?[[j,g]]:[]))).sort((a,b)=>a[0]-b[0]||a[1]-b[1]);
const T=bank(W,MASK),H=bank(V.map((_,i)=>i),M);
function line([j,g],[h,f],k=1n,l=1n){return canon(E[h].map((x,i)=>k*BigInt(g)*x-l*BigInt(f)*E[j][i]))}
const L=uniq(T.flatMap((a,i)=>[...T.slice(i+1).map(b=>line(a,b)),...H.map(b=>line(a,b,3n,2n))])).filter(a=>a.some(x=>x>0n)&&a.some(x=>x<0n));
let polys=[[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]]];
for(const l of L){let next=[];for(const p of polys){let s=p.map(x=>dot(l,x));if(!s.some(x=>x>0n)||!s.some(x=>x<0n)){next.push(p);continue}let pos=[],neg=[];for(let i=0;i<p.length;i++){let j=(i+1)%p.length,a=s[i],b=s[j];if(a>=0n)pos.push(p[i]);if(a<=0n)neg.push(p[i]);if(a*b<0n){let r=norm(p[i].map((x,k)=>(b<0n?-b:b)*x+(a<0n?-a:a)*p[j][k]));pos.push(r);neg.push(r)}}next.push(pos,neg)}polys=next}
let pts=new Map();function put(p){p=norm(p);if(p.every(x=>x>0n))pts.set(key(p),p)}
for(const p of polys){put(p.reduce(add,[0n,0n,0n]));for(let i=0;i<p.length;i++){put(p[i]);put(add(p[i],p[(i+1)%p.length]))}}
const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1],max=a=>a.reduce((x,y)=>cmp(x,y)>=0n?x:y),min=a=>a.reduce((x,y)=>cmp(x,y)<=0n?x:y);
const groups=new Map(),witnesses=new Map();
for(const p of pts.values()){let s=E.map(e=>dot(e,p)),F=G.map(g=>max(g.map((v,j)=>[BigInt(v),s[j]]))),eta=min(W.map(i=>F[i]));let m=0,n=0;T.forEach(([j,g],i)=>{if(cmp([BigInt(g),s[j]],eta)===0n)m|=1<<i});F.forEach((f,i)=>{if(2n*f[0]*eta[1]<3n*eta[0]*f[1])n|=1<<i});if(!m)throw Error("missing optimizer");if(!groups.has(n))groups.set(n,new Set());groups.get(n).add(m);if(!witnesses.has([m,n].join()))witnesses.set([m,n].join(),p.map(String))}
const pop=x=>{let n=0;while(x){x&=x-1;n++}return n};
let rows=[],total=0;
for(const [n,set] of [...groups].sort((a,b)=>a[0]-b[0])){let masks=[...set].sort((a,b)=>a-b),mandatory=masks.filter(x=>pop(x)===1).reduce((a,b)=>a|b,0),choices=masks.reduce((a,b)=>a|b,0),free=choices&~mandatory,best=choices;let trials=0;for(let s=free;;s=(s-1)&free){let z=s|mandatory;trials++;if(pop(z)<pop(best)&&masks.every(x=>x&z))best=z;if(!s)break}if(!masks.every(x=>x&best)||best!==mandatory)throw Error("singleton cover mismatch");total+=pop(best);rows.push({near:n,labels:masks.length,mandatory,cover:best,size:pop(best),trials,masks,witnesses:masks.filter(x=>pop(x)===1).map(x=>[x,witnesses.get([x,n].join())])})}
const directions=[];for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){let v=[x,y,z];if((v.find(a=>a!==0)||0)>0&&Math.max(v.reduce((a,b)=>a+Math.max(b,0),0),v.reduce((a,b)=>a+Math.max(-b,0),0))<=10)directions.push([v,gaps(v)])}
const vi=new Map(V.map((v,i)=>[v.join(),i]));let fullChecks=0;
for(const row of rows)for(const [m,ps] of row.witnesses){let p=ps.map(BigInt),s=E.map(e=>dot(e,p)),F=directions.map(([v,g])=>max(g.map((a,j)=>[BigInt(a),s[j]]))),eta=min(F),actualMask=0,n=0;T.forEach(([j,g],i)=>{if(cmp([BigInt(g),s[j]],eta)===0n)actualMask|=1<<i});F.forEach((f,i)=>{if(2n*f[0]*eta[1]<3n*eta[0]*f[1]){let j=vi.get(directions[i][0].join());if(j===undefined)throw Error("outside near bank");n|=1<<j}});if(n!==row.near||m!==actualMask)throw Error("full population witness mismatch");fullChecks+=directions.length}
return {lines:L.length,cells:polys.length,points:pts.size,terms:T,nearGroups:groups.size,jointLabels:[...groups.values()].reduce((s,g)=>s+g.size,0),singleton:rows.reduce((s,r)=>s+pop(r.mandatory),0),minOutputs:total,directions:directions.length,fullChecks,rows}
}
console.log(JSON.stringify(run(),null,2));
```

## Control and next

Native read r2-20261126-r217-x6-read SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY, Source 88afc5b07355ac1919f38f8c54fe818606b952fe, observed 2026-11-26T01:09:12.511796Z; no native owner projection and no execution authorization. Site client identity checked but current lane Researcher-ID/Activity binding not established; no CLAIM or shared task mutation. This is a continuation of the already exposed static research, not a new clean discovery or independent reviewer. Next: distinguish the true polynomial-sign query model from unrestricted Boolean composition; either construct a depth-six polynomial tree or prove a structural obstruction. Also complete independent mathematical review of the R176/R213/R216 lower chain and R168 upper chain. Do not repeat the 4249-class closure just to count progress.
