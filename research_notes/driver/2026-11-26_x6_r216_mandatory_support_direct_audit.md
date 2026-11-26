# Driver audit: X6 Port 10 mandatory support geometry, direct all-direction verification

2026-11-26. Informed nonauthor audit, shared project context disclosed. Historical author EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317 per R178; preserve source authorship and current binding unknown. Not a Native Review/Result or completion of the R216 full sharpness audit.

Frozen sources:
- awdawmip/enterprise-math@c665f671a31d2bfeffb151e06bb308628110029e:research_notes/portable_direct/2026-11-24_r2_x6_r176_arbitrary_linear_boundary_supports.md (exact input JSON and declared model).
- @4765928190367b00d1e8a19e4a27d952897e4f98:research_notes/portable_direct/2026-11-25_r2_x6_r178_recursive_endpoint_capacity.md.
- @e39b9de2671fc0ba71a2ca03f89b74670f19d0e5:research_notes/portable_direct/2026-11-26_r2_x6_r213_rank_three_projected_union_capacity.md.
- @fc069513b1b5b6f758cb6e92e661cd9a91920c71:research_notes/portable_direct/2026-11-26_r2_x6_r216_unified_closure_audit.md.

## Mathematical scope and actual checks

Port 10, w=(17t,B,22t,D), t,B,D>0. Six capacities E, four heights and 1935 sign-reduced integer directions as R176. Output a legal optimizer term among its fifteen terms and exact strict near set 2F_v<3eta. Auxiliary homogeneous comparison tree, no assertion about native geometry, time or arithmetic cost.

Independently reimplemented direct scoring against ALL 1935 directions at three representatives for every elementary segment of the 47 *reported* supports (not just the endpoints and not a search for additional supports). Reconstructed the 256-line partition using declared bank data, 4638 elementary intervals on these supports, 26923590 exact direction scores. All 1574 active intervals, outer endpoints, 47 support labels and 49 components match author. The two disconnected supports and their gaps match R216's hardcoded clipping data. This rechecks the 47 reported supports without assuming that the reduced V/W bank yields correct scores at the sampled points. The lower bound requires these mandatory portions, not proof that no additional support exists.

For each active interval independently tried a stronger continuum certificate: choose a legal eta term at each representative, prove every direction has a fixed term >= eta on the entire open segment and one direction has all terms <= eta; certify near membership by all six strict inequalities, nonmembership by a fixed opposing term, and the exact optimizer mask by sign tests. Compare a term g/E_j with eta=a/E_k via linear form gE_k-aE_j, or 2gE_k-3aE_j for the strict near threshold. For open positive combinations of the two endpoint rays, the form is uniformly positive if the endpoint values are weakly positive and one strict, similarly negative. If both are zero the infinitesimal side perturbation along the support normal determines the sign (zero on the boundary). A finite number of comparisons gives a sufficiently small perturbation separately at each interior point; no uniform epsilon over an open interval is asserted. The certificate directly proves the three local labels and hence mandatory activity on an open interval, without using completeness of the reduced bank. It is sufficient but not necessary: mixed endpoint signs or lack of a single uniform witnessing term can leave a case unresolved. Actual uniformly certified intervals: 1574/1574; unresolved: 0. Successful per-side full direction verifications: 9137070 direction instances. For unresolved intervals only representative agreement is claimed. Exact arithmetic uses JS safe integer operations, max observed raw score cross-product bound 41303016077400<2^53; endpoint sign products are also checked for safe integer scale. In the fixed small input the integer geometric construction and coordinate dot/cross products are smaller than this bound.

## Review of necessary-relaxation arguments

R176 mandatory-support argument is valid: a finite tree omitting a required supporting line has only finitely many intersections with an open active segment; away from those intersections all tests are locally constant, contradicting incompatibility of the three local legal-output sets. The same argument in any open ancestor cell forces a distinct internal node per active support. R178 endpoint update remains one-sided even for disconnected components: if both retained endpoints bracket active pieces, a zero endpoint is retained in the positive child only when the other retained endpoint is strictly positive. On the segment between them the linear form is positive except at the zero endpoint, preserving its actual closure sequence. Dropping isolated zero/crossing obligations weakens the test. R213/R216 moving-point orientation follows (r cross q) dot (u cross v)=(r dot u)(q dot v)-(r dot v)(q dot u), with sign multiplied by sign(r dot u) and by the orientation of u cross v relative to the support normal. The static forced sign rule is safe because the cut is a positive combination of the bracketing original rays. For fixed root and query arrangement faces, each relative-interior vector is a positive combination of all extreme generators of its face closure; if all bilinear extreme-pair signs are weakly positive and at least one strict, all such interior pairs are strictly positive, so excluding zero in that case is sound. Opposite-sign pairs admit the enlarged ternary envelope; it need not be realizable. The union of projected support-normal sign tuples compatible with these envelopes contains every true fixed-root query pattern. Recursing in a superset can only make the necessary capacity condition easier. Neither passing the relaxed search nor its early permissive shortcuts construct an actual tree. The root/child equality convention is safely ignored only for lower bounds using open halves.

R216 full arbitrary-linear depth seven remains an author result under independent review. This audit does not independently replay the 4249-root arrangement, all 393 residual exclusions, or the R168 full-cone upper witness; those and any unresolved continuum intervals are the remaining review scope. Do not claim a Native Review or Result or formal acceptance. No new Task/CLAIM or source author change.

## Exact outputs

```json
{
  "lines": 256,
  "K": 479958,
  "T": 15,
  "H": 30,
  "directions": 1935,
  "maxGap": 1260,
  "maxProduct": 41303016077400,
  "segments": 4638,
  "checks": 26923590,
  "active": 1574,
  "supports": 47,
  "components": 49,
  "certified": 1574,
  "sideChecks": 9137070,
  "unresolved": [],
  "all": [
    {
      "normal": [
        187,
        12,
        -1
      ],
      "active": 9,
      "certified": 9,
      "components": [
        [
          [
            0,
            1,
            12
          ],
          [
            1,
            17,
            391
          ]
        ]
      ]
    },
    {
      "normal": [
        204,
        11,
        -1
      ],
      "active": 9,
      "certified": 9,
      "components": [
        [
          [
            0,
            1,
            11
          ],
          [
            1,
            17,
            391
          ]
        ]
      ]
    },
    {
      "normal": [
        5,
        -2,
        0
      ],
      "active": 51,
      "certified": 51,
      "components": [
        [
          [
            2,
            5,
            73
          ],
          [
            2,
            5,
            5
          ]
        ]
      ]
    },
    {
      "normal": [
        9,
        -1,
        0
      ],
      "active": 4,
      "certified": 4,
      "components": [
        [
          [
            1,
            9,
            74
          ],
          [
            1,
            9,
            69
          ]
        ]
      ]
    },
    {
      "normal": [
        85,
        7,
        -2
      ],
      "active": 10,
      "certified": 10,
      "components": [
        [
          [
            1,
            9,
            74
          ],
          [
            3,
            17,
            187
          ]
        ]
      ]
    },
    {
      "normal": [
        51,
        2,
        -1
      ],
      "active": 9,
      "certified": 9,
      "components": [
        [
          [
            1,
            9,
            69
          ],
          [
            3,
            17,
            187
          ]
        ],
        [
          [
            2,
            5,
            112
          ],
          [
            1,
            0,
            51
          ]
        ]
      ]
    },
    {
      "normal": [
        0,
        1,
        -1
      ],
      "active": 2,
      "certified": 2,
      "components": [
        [
          [
            2,
            5,
            5
          ],
          [
            1,
            0,
            0
          ]
        ]
      ]
    },
    {
      "normal": [
        34,
        1,
        -1
      ],
      "active": 7,
      "certified": 7,
      "components": [
        [
          [
            2,
            5,
            73
          ],
          [
            1,
            0,
            34
          ]
        ]
      ]
    },
    {
      "normal": [
        187,
        20,
        -9
      ],
      "active": 5,
      "certified": 5,
      "components": [
        [
          [
            6,
            15,
            158
          ],
          [
            1,
            1,
            23
          ]
        ]
      ]
    },
    {
      "normal": [
        68,
        1,
        -3
      ],
      "active": 8,
      "certified": 8,
      "components": [
        [
          [
            2,
            5,
            47
          ],
          [
            3,
            0,
            68
          ]
        ]
      ]
    },
    {
      "normal": [
        176,
        22,
        -9
      ],
      "active": 4,
      "certified": 4,
      "components": [
        [
          [
            6,
            15,
            154
          ],
          [
            19,
            28,
            440
          ]
        ]
      ]
    },
    {
      "normal": [
        22,
        0,
        -1
      ],
      "active": 47,
      "certified": 47,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            1,
            17,
            22
          ]
        ]
      ]
    },
    {
      "normal": [
        61,
        0,
        -1
      ],
      "active": 78,
      "certified": 78,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            1,
            17,
            61
          ]
        ]
      ]
    },
    {
      "normal": [
        74,
        0,
        -1
      ],
      "active": 14,
      "certified": 14,
      "components": [
        [
          [
            1,
            9,
            74
          ],
          [
            1,
            4,
            74
          ]
        ]
      ]
    },
    {
      "normal": [
        126,
        0,
        -1
      ],
      "active": 103,
      "certified": 103,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            1,
            30,
            126
          ]
        ]
      ]
    },
    {
      "normal": [
        4,
        -1,
        0
      ],
      "active": 35,
      "certified": 35,
      "components": [
        [
          [
            1,
            4,
            152
          ],
          [
            1,
            4,
            74
          ]
        ]
      ]
    },
    {
      "normal": [
        17,
        -1,
        0
      ],
      "active": 44,
      "certified": 44,
      "components": [
        [
          [
            0,
            0,
            1
          ],
          [
            1,
            17,
            391
          ]
        ],
        [
          [
            1,
            17,
            69
          ],
          [
            1,
            17,
            22
          ]
        ]
      ]
    },
    {
      "normal": [
        156,
        -1,
        -1
      ],
      "active": 46,
      "certified": 46,
      "components": [
        [
          [
            1,
            4,
            152
          ],
          [
            1,
            30,
            126
          ]
        ]
      ]
    },
    {
      "normal": [
        69,
        0,
        -1
      ],
      "active": 16,
      "certified": 16,
      "components": [
        [
          [
            1,
            17,
            69
          ],
          [
            1,
            9,
            69
          ]
        ]
      ]
    },
    {
      "normal": [
        9,
        0,
        -1
      ],
      "active": 47,
      "certified": 47,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            1,
            17,
            9
          ]
        ]
      ]
    },
    {
      "normal": [
        235,
        0,
        -3
      ],
      "active": 84,
      "certified": 84,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            3,
            77,
            235
          ]
        ]
      ]
    },
    {
      "normal": [
        87,
        0,
        -1
      ],
      "active": 107,
      "certified": 107,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            1,
            17,
            87
          ]
        ]
      ]
    },
    {
      "normal": [
        104,
        -1,
        -1
      ],
      "active": 60,
      "certified": 60,
      "components": [
        [
          [
            1,
            4,
            100
          ],
          [
            3,
            77,
            235
          ]
        ]
      ]
    },
    {
      "normal": [
        38,
        0,
        -3
      ],
      "active": 57,
      "certified": 57,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            3,
            40,
            38
          ]
        ]
      ]
    },
    {
      "normal": [
        5,
        0,
        -2
      ],
      "active": 72,
      "certified": 72,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            2,
            5,
            5
          ]
        ]
      ]
    },
    {
      "normal": [
        39,
        -1,
        -1
      ],
      "active": 50,
      "certified": 50,
      "components": [
        [
          [
            3,
            1,
            116
          ],
          [
            1,
            17,
            22
          ]
        ]
      ]
    },
    {
      "normal": [
        40,
        0,
        -3
      ],
      "active": 63,
      "certified": 63,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            3,
            38,
            40
          ]
        ]
      ]
    },
    {
      "normal": [
        26,
        -1,
        -1
      ],
      "active": 39,
      "certified": 39,
      "components": [
        [
          [
            2,
            5,
            47
          ],
          [
            3,
            53,
            25
          ]
        ]
      ]
    },
    {
      "normal": [
        25,
        0,
        -3
      ],
      "active": 52,
      "certified": 52,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            3,
            53,
            25
          ]
        ]
      ]
    },
    {
      "normal": [
        83,
        0,
        -2
      ],
      "active": 69,
      "certified": 69,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            2,
            34,
            83
          ]
        ]
      ]
    },
    {
      "normal": [
        102,
        -7,
        -1
      ],
      "active": 14,
      "certified": 14,
      "components": [
        [
          [
            1,
            4,
            74
          ],
          [
            3,
            17,
            187
          ]
        ]
      ]
    },
    {
      "normal": [
        204,
        -11,
        1
      ],
      "active": 51,
      "certified": 51,
      "components": [
        [
          [
            0,
            1,
            11
          ],
          [
            1,
            30,
            126
          ]
        ]
      ]
    },
    {
      "normal": [
        395,
        0,
        -2
      ],
      "active": 119,
      "certified": 119,
      "components": [
        [
          [
            0,
            1,
            0
          ],
          [
            2,
            73,
            395
          ]
        ]
      ]
    },
    {
      "normal": [
        289,
        18,
        -1
      ],
      "active": 10,
      "certified": 10,
      "components": [
        [
          [
            0,
            1,
            18
          ],
          [
            1,
            17,
            595
          ]
        ]
      ]
    },
    {
      "normal": [
        66,
        2,
        -1
      ],
      "active": 11,
      "certified": 11,
      "components": [
        [
          [
            1,
            4,
            74
          ],
          [
            1,
            0,
            66
          ]
        ]
      ]
    },
    {
      "normal": [
        132,
        5,
        -1
      ],
      "active": 16,
      "certified": 16,
      "components": [
        [
          [
            1,
            17,
            217
          ],
          [
            1,
            0,
            132
          ]
        ]
      ]
    },
    {
      "normal": [
        44,
        1,
        -1
      ],
      "active": 9,
      "certified": 9,
      "components": [
        [
          [
            1,
            17,
            61
          ],
          [
            1,
            11,
            55
          ]
        ]
      ]
    },
    {
      "normal": [
        88,
        3,
        -1
      ],
      "active": 7,
      "certified": 7,
      "components": [
        [
          [
            1,
            4,
            100
          ],
          [
            1,
            0,
            88
          ]
        ]
      ]
    },
    {
      "normal": [
        88,
        7,
        -3
      ],
      "active": 5,
      "certified": 5,
      "components": [
        [
          [
            1,
            17,
            69
          ],
          [
            1,
            11,
            55
          ]
        ]
      ]
    },
    {
      "normal": [
        132,
        -7,
        -1
      ],
      "active": 14,
      "certified": 14,
      "components": [
        [
          [
            1,
            9,
            69
          ],
          [
            1,
            11,
            55
          ]
        ]
      ]
    },
    {
      "normal": [
        153,
        8,
        -1
      ],
      "active": 7,
      "certified": 7,
      "components": [
        [
          [
            1,
            9,
            225
          ],
          [
            1,
            0,
            153
          ]
        ]
      ]
    },
    {
      "normal": [
        153,
        5,
        -4
      ],
      "active": 1,
      "certified": 1,
      "components": [
        [
          [
            3,
            1,
            116
          ],
          [
            4,
            0,
            153
          ]
        ]
      ]
    },
    {
      "normal": [
        117,
        -2,
        -2
      ],
      "active": 42,
      "certified": 42,
      "components": [
        [
          [
            2,
            5,
            112
          ],
          [
            2,
            34,
            83
          ]
        ]
      ]
    },
    {
      "normal": [
        198,
        8,
        -1
      ],
      "active": 5,
      "certified": 5,
      "components": [
        [
          [
            1,
            4,
            230
          ],
          [
            1,
            0,
            198
          ]
        ]
      ]
    },
    {
      "normal": [
        198,
        5,
        -4
      ],
      "active": 11,
      "certified": 11,
      "components": [
        [
          [
            2,
            8,
            109
          ],
          [
            2,
            0,
            99
          ]
        ]
      ]
    },
    {
      "normal": [
        306,
        17,
        -1
      ],
      "active": 8,
      "certified": 8,
      "components": [
        [
          [
            1,
            17,
            595
          ],
          [
            1,
            0,
            306
          ]
        ]
      ]
    },
    {
      "normal": [
        234,
        -1,
        -1
      ],
      "active": 43,
      "certified": 43,
      "components": [
        [
          [
            1,
            4,
            230
          ],
          [
            2,
            73,
            395
          ]
        ]
      ]
    }
  ]
}
```

## Reproduction

Extract the first JSON block from the pinned R176 report to r176.json. Execute this standalone JS with Node (no dependency).

```js
function audit(src){
 const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],W=[0,3,5,6,7,9],M=[30,51,42,21,58,51,20,7,23,30],E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]];
 function gaps([x,y,z]){const h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return [h[1],h[2],h[3],h[2]-h[1],h[3]-h[1],h[3]-h[2]].map(Math.abs)}
 const gcd=(a,b)=>{a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b]}return a},prim=v=>{const g=v.reduce(gcd,0);return g?v.map(x=>x/g):v},canon=v=>{let u=prim(v);return (u.find(Boolean)??0)<0?u.map(x=>-x):u},dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sum=a=>a[0]+a[1]+a[2];
 const T=[],H=[];for(let i=0;i<V.length;i++)for(let j=0;j<6;j++){let a=gaps(V[i])[j];if(!a)continue;if(!H.some(t=>t[0]===j&&t[1]===a))H.push([j,a]);if(W.includes(i)&&(M[i]&(1<<j))&&!T.some(t=>t[0]===j&&t[1]===a))T.push([j,a])}
 T.sort((a,b)=>a[0]-b[0]||a[1]-b[1]);const lines=new Map();for(const [i,a] of T){for(const [j,b] of T){let v=canon(E[j].map((x,k)=>a*x-b*E[i][k]));if(v.some(x=>x>0)&&v.some(x=>x<0))lines.set(v.join(),v)}for(const [j,b] of H){let v=canon(E[j].map((x,k)=>3*a*x-2*b*E[i][k]));if(v.some(x=>x>0)&&v.some(x=>x<0))lines.set(v.join(),v)}}
 const all=[...lines.values(),[1,0,0],[0,1,0],[0,0,1]],K=1+Math.max(...[...lines.values()].flatMap(l=>all.map(m=>Math.abs(dot(l,m)))));const dirs=[];for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){let a=[x,y,z];if((a.find(Boolean)??0)>0&&a.reduce((s,v)=>s+Math.max(0,v),0)<=10&&a.reduce((s,v)=>s+Math.max(0,-v),0)<=10)dirs.push(a)}
 const G=dirs.map(gaps),maxGap=Math.max(...G.flat());let maxProduct=0,checks=0,active=0,segments=0,certified=0,sideChecks=0;const results=[],unresolved=[];
 function label(p){const s=E.map(e=>dot(e,p));if(s.some(x=>x<=0||!Number.isSafeInteger(x)))throw Error("bad capacity");const bound=3*maxGap*Math.max(...s);if(!Number.isSafeInteger(bound))throw Error("integer bound");maxProduct=Math.max(maxProduct,bound);let fs=[],a=0,b=1;
 for(let i=0;i<G.length;i++){let aa=0,bb=1;for(let j=0;j<6;j++)if(G[i][j]*bb>aa*s[j]){aa=G[i][j];bb=s[j]}fs.push([aa,bb]);if(i===0||aa*b<a*bb){a=aa;b=bb}}
 let mask=0;for(let i=0;i<T.length;i++){let [j,g]=T[i];if(g*b===a*s[j])mask|=1<<i}if(!mask)throw Error("optimizer outside T");
 let near=[];for(let i=0;i<fs.length;i++)if(2*fs[i][0]*b<3*a*fs[i][1])near.push(i);checks+=G.length;return {mask,near:near.join(","),nearSet:new Set(near)}}
 // For any normalized ray in the open segment, endpoint signs determine a linear inequality.
 // If the form vanishes identically on the segment, its infinitesimal sign is determined by side*l.
 // The following returns +1/-1 if a strictly uniform sign, 0 for identically zero,
 // and 2 when a uniform sign cannot be certified by the endpoints.
 function uniformSign(x,y,d){if(x>=0&&y>=0&&(x||y))return 1;if(x<=0&&y<=0&&(x||y))return -1;if(!x&&!y)return Math.sign(d);return 2}
 function certify(u,v,l,side,L){
 const U=E.map(e=>dot(e,u)),Vv=E.map(e=>dot(e,v)),D=E.map(e=>side*dot(e,l));let idx=T.findIndex((_,i)=>L.mask&(1<<i)),[k,a]=T[idx];
 if(![...U,...Vv,...D].every(x=>Number.isSafeInteger(3*maxGap*x)))throw Error("unsafe sign products");
 const sign=(j,g,num,den)=>uniformSign(num*g*U[k]-den*a*U[j],num*g*Vv[k]-den*a*Vv[j],num*g*D[k]-den*a*D[j]);
 let attaining=false;
 for(let i=0;i<G.length;i++){
 let upper=true,lower=false,near=true,nonnear=false;
 for(let j=0;j<6;j++){let s=sign(j,G[i][j],1,1),t=sign(j,G[i][j],2,3);
 if(s!==-1&&s!==0)upper=false;if(s===1||s===0)lower=true;if(t!==-1)near=false;if(t===1||t===0)nonnear=true}
 if(!lower)return {reason:"lower",i};
 if(upper)attaining=true;
 if(L.nearSet.has(i)?!near:!nonnear)return {reason:"near",i};
 }
 if(!attaining)return {reason:"upper"};
 // Exact optimizer term mask: every equality with eta must be identically zero in the side limit,
 // or be uniformly nonzero there. This proves common-leaf legality across all three local pieces.
 for(let i=0;i<T.length;i++){let [j,g]=T[i],s=sign(j,g,1,1);if(s===2||((s===0)!==Boolean(L.mask&(1<<i))))return {reason:"optimizer-mask",i}}
 sideChecks+=G.length;return null
 }
 for(const rec of src.activeLines){const l=rec.normal.map(Number),points=[...new Map(all.map(m=>canon(cross(l,m))).filter(p=>p.some(Boolean)&&p.every(x=>x>=0)).map(p=>[p.join(),p])).values()];let ax=[0,1,2].find(i=>points.some(p=>p[i]*sum(points[0])!==points[0][i]*sum(p)));points.sort((a,b)=>a[ax]*sum(b)-b[ax]*sum(a));let intervals=[],components=[],certCount=0;
 for(let i=0;i<points.length-1;i++){let u=points[i],v=points[i+1],p=prim(u.map((x,j)=>x+v[j]));if(p.some(x=>x<=0))continue;const A=label(p.map((x,j)=>K*x+l[j])),B=label(p.map((x,j)=>K*x-l[j])),C=label(p);segments++;if(A.near!==B.near||A.near!==C.near||!(A.mask&B.mask&C.mask)){active++;intervals.push([u,v]);let last=components.at(-1);if(last&&last[1].join()===u.join())last[1]=v;else components.push([u,v]);let errs=[];for(const [s,L] of [[1,A],[-1,B],[0,C]]){let e=certify(u,v,l,s,L);if(e)errs.push({side:s,...e})}if(!errs.length){certified++;certCount++}else unresolved.push({normal:l,u,v,errs})}}
 if(intervals.length!==rec.segments||intervals[0][0].join()!==rec.endpoints[0].join()||intervals.at(-1)[1].join()!==rec.endpoints[1].join())throw Error("mismatch "+l);
 results.push({normal:l,active:intervals.length,certified:certCount,components});
 }
 return {lines:lines.size,K,T:T.length,H:H.length,directions:dirs.length,maxGap,maxProduct,segments,checks,active,supports:results.length,components:results.reduce((s,x)=>s+x.components.length,0),certified,sideChecks,unresolved,all:results}
}
const src=JSON.parse(require('fs').readFileSync('r176.json','utf8'));console.log(JSON.stringify(audit(src),null,2));
```
