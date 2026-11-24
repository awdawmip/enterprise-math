# X6 R177 — Two-level mandatory-support capacity with endpoint closure and exact clipping

2026-11-24. AUTHOR PROOF / EXACT BIGINT REPLAY / NOT_REVIEWED. Independent informed static BRC observer research. Frozen scientific inputs R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd, R122@1e4ab68c4f9c91bc60c07017acc57be20829832f; R175@eadbd5e26a1a44f2bef376229785e7d2886f5938 and R176@c665f671a31d2bfeffb151e06bb308628110029e:research_notes/portable_direct/2026-11-24_r2_x6_r176_arbitrary_linear_boundary_supports.md. P000 V5 and ACTIVE worldview retained. This is an auxiliary parameter chart, not native spatial geometry/dynamics. Historical lane EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317; live native session binding unconfirmed, no CLAIM.

## Proposition and new results

Keep Port 10, w=(17t,B,22t,D), t,B,D>0, six capacities, 1935 unoriented integer directions, 15 legal optimizer terms and complete strict near set of R176. Tests are arbitrary fixed real linear homogeneous forms with a binary strict-sign answer (rational forms are a subset). Normalize t+B+D=1. R176 proved 47 mandatory support lines with 51 distinct extreme endpoint rays. We seek to rule out depth 6. The first two levels of any correct depth-six tree must satisfy the following necessary conditions.

1. For each of the 611 root ternary endpoint classes surviving the R176 31-support test, retain in either open root half the strict endpoint rays on that side. Enumerate all possible second tests by the 4249 antipodal ternary endpoint sign patterns. Each of the two open grandchildren of this half must contain at most 15 mandatory supports. Counting only supports with an endpoint strictly satisfying both signs is a safe relaxation; 553 root classes survive.
2. Strengthen by retaining zero-root-sign endpoints of every support that also has an extreme endpoint strictly inside that half. These zero endpoints are closure points of that support's active pieces in the half, even when active pieces are disconnected. Count a support for a second open half when any retained endpoint has the corresponding strict second sign. 537 root classes survive this stronger test. This excludes 74 of R176's survivors, uniformly over all actual coefficient vectors realizing each excluded root class.
3. For each of the 47 mandatory supports as an exact fixed first test, clip each actual active elementary segment to both open root halves. Recompute the two extreme closure rays per surviving support in each half, and exhaustively enumerate all second-test sign patterns on those clipped rays. 11 mandatory root supports pass level one; 4 pass level two. Remaining exact mandatory roots are (9,-1,0), (61,0,-1), (69,0,-1), (198,5,-4). These are necessary, not sufficient, conditions. Arbitrary nonmandatory root directions remain allowed; the 6 versus 7 full-domain question is open.

## Proof

Use the R176 local boundary theorem: if an active open segment has a point in an open node cell, a small neighborhood of that point is in the cell; the corresponding support must occur somewhere in that subtree. Indeed every other finite query support meets that segment in at most one point; at a generic point failure to query that support would send locally incompatible outputs to one leaf. With two ancestors tested, at most four further binary tests are available, hence at most 15 internal nodes in that subtree. Different support lines require different nodes.

Let a mandatory support have extreme closure rays u,v of its active portions (normalized in the auxiliary chart). A strict positive dot product at u or v implies an actual active point nearby with positive dot product. The same applies to two simultaneous strict signs by continuity. For the closure refinement, if r·u=0 and r·v>0, then r is positive on the relative interior of the entire u-v span. In particular the active portion approaching u from within the span has positive root sign. Thus u is a closure point of actual active portions inside the positive root half; a strict second sign at u is a valid obligation. The negative-half version follows by negation. If both root signs vanish, the support is not counted in either open root half. For opposite root signs the negative endpoint is discarded; the true cut intersection may add information, deliberately not used in this uniform relaxation. The counting rule is therefore a lower bound on mandatory supports, not a sufficient feasibility model. The root class fixes the retained endpoint sets per support; second tests are completely enumerated on these same finite rays using R176's dual great-circle vertex/tangent lexicographic enumeration. Antipodal identification is valid because both open grandchildren must satisfy the same capacity. Zero signs retained. For a set of at least two distinct projective rays the arrangement has intersections; in rank two all circles share the antipodal pair and the same tangent construction covers arcs and chambers. Empty/single-ray cases handled explicitly. Thus absence of a feasible second sign pattern is a proof for every actual root with the given ternary class. No representative-only exclusion is promoted to a whole class.

For a fixed root r, use homogeneous integer endpoint rays u,v of each actual elementary active interval. If both r·u,r·v<=0 there is no positive interior. If both are nonnegative with at least one positive, keep the interval closure. If a=r·u<0<b=r·v, replace u by primitive(bu-av); the other crossing is symmetric. Since the active interval is open, endpoint equality is used only as closure, never asserted to be a positive input. The union of clipped active intervals may be disconnected, so compute its extremes only AFTER clipping each actual elementary interval. For any second linear sign, an active point satisfying it exists iff an extreme has that strict sign; proof by linearity after normalization and continuity. Thus the fixed-root second-level open-support capacity condition is exact, not just an endpoint relaxation. The open-half condition ignores extra equality obligations and remains necessary for the binary strict comparison tree. No actual new depth-six tree is claimed.

## Exact results and replay

Reconstructed 21842 elementary open segments, 1574 active segments and the original 47 support records exactly byte-for-byte in JSON structure, with 2 gaps between adjacent active elementary segments along a support. This uses R176's bank/line/label reductions and BigInt integer arithmetic. It is not a new direct all-1935-directions check; R176's verified witnesses and preceding bank proofs are inherited. All root/second-layer counts are completed finite calculations. No time speedup or native physical claim.

```json
{
  "segments": 21842,
  "changes": 1574,
  "supports": 47,
  "activeRunGaps": 2,
  "endpointRays": 51,
  "rootClasses": 4249,
  "rootCapacitySurvivors": 611,
  "strictEndpointSecondSurvivors": 553,
  "closureEndpointSecondSurvivors": 537,
  "strictSideMasks": 357,
  "closureSideCarriers": 580,
  "fixedRootFirstPass": 11,
  "fixedRootSecondPass": 4,
  "fixed": [
    {
      "l": [
        "187",
        "12",
        "-1"
      ],
      "halves": [
        {
          "n": 44,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 4,
          "best": 2,
          "classes": 73
        }
      ]
    },
    {
      "l": [
        "204",
        "11",
        "-1"
      ],
      "halves": [
        {
          "n": 43,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 4,
          "best": 2,
          "classes": 49
        }
      ]
    },
    {
      "l": [
        "5",
        "-2",
        "0"
      ],
      "halves": [
        {
          "n": 15,
          "best": 7,
          "classes": 971
        },
        {
          "n": 40,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "9",
        "-1",
        "0"
      ],
      "halves": [
        {
          "n": 26,
          "best": 13,
          "classes": 2223
        },
        {
          "n": 29,
          "best": 15,
          "classes": 1391
        }
      ]
    },
    {
      "l": [
        "85",
        "7",
        "-2"
      ],
      "halves": [
        {
          "n": 33,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 21,
          "best": 11,
          "classes": 1399
        }
      ]
    },
    {
      "l": [
        "51",
        "2",
        "-1"
      ],
      "halves": [
        {
          "n": 29,
          "best": 16,
          "classes": 1635
        },
        {
          "n": 22,
          "best": 12,
          "classes": 1251
        }
      ]
    },
    {
      "l": [
        "0",
        "1",
        "-1"
      ],
      "halves": [
        {
          "n": 13,
          "best": 6,
          "classes": 189
        },
        {
          "n": 42,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "34",
        "1",
        "-1"
      ],
      "halves": [
        {
          "n": 21,
          "best": 13,
          "classes": 825
        },
        {
          "n": 33,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "187",
        "20",
        "-9"
      ],
      "halves": [
        {
          "n": 20,
          "best": 13,
          "classes": 697
        },
        {
          "n": 36,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "68",
        "1",
        "-3"
      ],
      "halves": [
        {
          "n": 17,
          "best": 10,
          "classes": 383
        },
        {
          "n": 38,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "176",
        "22",
        "-9"
      ],
      "halves": [
        {
          "n": 21,
          "best": 12,
          "classes": 699
        },
        {
          "n": 35,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "22",
        "0",
        "-1"
      ],
      "halves": [
        {
          "n": 8,
          "best": 5,
          "classes": 109
        },
        {
          "n": 40,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "61",
        "0",
        "-1"
      ],
      "halves": [
        {
          "n": 23,
          "best": 13,
          "classes": 1213
        },
        {
          "n": 27,
          "best": 15,
          "classes": 1423
        }
      ]
    },
    {
      "l": [
        "74",
        "0",
        "-1"
      ],
      "halves": [
        {
          "n": 29,
          "best": 16,
          "classes": 1603
        },
        {
          "n": 18,
          "best": 10,
          "classes": 731
        }
      ]
    },
    {
      "l": [
        "126",
        "0",
        "-1"
      ],
      "halves": [
        {
          "n": 35,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 13,
          "best": 7,
          "classes": 487
        }
      ]
    },
    {
      "l": [
        "4",
        "-1",
        "0"
      ],
      "halves": [
        {
          "n": 19,
          "best": 9,
          "classes": 1391
        },
        {
          "n": 35,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "17",
        "-1",
        "0"
      ],
      "halves": [
        {
          "n": 33,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 20,
          "best": 10,
          "classes": 483
        }
      ]
    },
    {
      "l": [
        "156",
        "-1",
        "-1"
      ],
      "halves": [
        {
          "n": 37,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 22,
          "best": 11,
          "classes": 935
        }
      ]
    },
    {
      "l": [
        "69",
        "0",
        "-1"
      ],
      "halves": [
        {
          "n": 27,
          "best": 15,
          "classes": 1697
        },
        {
          "n": 23,
          "best": 13,
          "classes": 1153
        }
      ]
    },
    {
      "l": [
        "9",
        "0",
        "-1"
      ],
      "halves": [
        {
          "n": 5,
          "best": 3,
          "classes": 55
        },
        {
          "n": 43,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "235",
        "0",
        "-3"
      ],
      "halves": [
        {
          "n": 31,
          "best": 16,
          "classes": 1721
        },
        {
          "n": 17,
          "best": 9,
          "classes": 731
        }
      ]
    },
    {
      "l": [
        "87",
        "0",
        "-1"
      ],
      "halves": [
        {
          "n": 33,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 16,
          "best": 9,
          "classes": 663
        }
      ]
    },
    {
      "l": [
        "104",
        "-1",
        "-1"
      ],
      "halves": [
        {
          "n": 32,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 24,
          "best": 12,
          "classes": 1171
        }
      ]
    },
    {
      "l": [
        "38",
        "0",
        "-3"
      ],
      "halves": [
        {
          "n": 6,
          "best": 3,
          "classes": 73
        },
        {
          "n": 42,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "5",
        "0",
        "-2"
      ],
      "halves": [
        {
          "n": 1,
          "best": 0,
          "classes": 5
        },
        {
          "n": 45,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "39",
        "-1",
        "-1"
      ],
      "halves": [
        {
          "n": 13,
          "best": 6,
          "classes": 679
        },
        {
          "n": 38,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "40",
        "0",
        "-3"
      ],
      "halves": [
        {
          "n": 7,
          "best": 4,
          "classes": 91
        },
        {
          "n": 41,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "26",
        "-1",
        "-1"
      ],
      "halves": [
        {
          "n": 6,
          "best": 3,
          "classes": 113
        },
        {
          "n": 44,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "25",
        "0",
        "-3"
      ],
      "halves": [
        {
          "n": 3,
          "best": 1,
          "classes": 25
        },
        {
          "n": 44,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "83",
        "0",
        "-2"
      ],
      "halves": [
        {
          "n": 16,
          "best": 9,
          "classes": 581
        },
        {
          "n": 31,
          "best": 17,
          "classes": 1815
        }
      ]
    },
    {
      "l": [
        "102",
        "-7",
        "-1"
      ],
      "halves": [
        {
          "n": 15,
          "best": 8,
          "classes": 885
        },
        {
          "n": 37,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "204",
        "-11",
        "1"
      ],
      "halves": [
        {
          "n": 43,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 12,
          "best": 6,
          "classes": 73
        }
      ]
    },
    {
      "l": [
        "395",
        "0",
        "-2"
      ],
      "halves": [
        {
          "n": 40,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 10,
          "best": 5,
          "classes": 305
        }
      ]
    },
    {
      "l": [
        "289",
        "18",
        "-1"
      ],
      "halves": [
        {
          "n": 45,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 2,
          "best": 1,
          "classes": 13
        }
      ]
    },
    {
      "l": [
        "66",
        "2",
        "-1"
      ],
      "halves": [
        {
          "n": 34,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 15,
          "best": 8,
          "classes": 675
        }
      ]
    },
    {
      "l": [
        "132",
        "5",
        "-1"
      ],
      "halves": [
        {
          "n": 40,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 9,
          "best": 4,
          "classes": 259
        }
      ]
    },
    {
      "l": [
        "44",
        "1",
        "-1"
      ],
      "halves": [
        {
          "n": 23,
          "best": 13,
          "classes": 1039
        },
        {
          "n": 29,
          "best": 16,
          "classes": 2211
        }
      ]
    },
    {
      "l": [
        "88",
        "3",
        "-1"
      ],
      "halves": [
        {
          "n": 38,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 12,
          "best": 6,
          "classes": 425
        }
      ]
    },
    {
      "l": [
        "88",
        "7",
        "-3"
      ],
      "halves": [
        {
          "n": 23,
          "best": 14,
          "classes": 1069
        },
        {
          "n": 31,
          "best": 16,
          "classes": 2709
        }
      ]
    },
    {
      "l": [
        "132",
        "-7",
        "-1"
      ],
      "halves": [
        {
          "n": 23,
          "best": 12,
          "classes": 2017
        },
        {
          "n": 33,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "153",
        "8",
        "-1"
      ],
      "halves": [
        {
          "n": 41,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 8,
          "best": 4,
          "classes": 193
        }
      ]
    },
    {
      "l": [
        "153",
        "5",
        "-4"
      ],
      "halves": [
        {
          "n": 22,
          "best": 13,
          "classes": 1001
        },
        {
          "n": 31,
          "best": 16,
          "classes": 2477
        }
      ]
    },
    {
      "l": [
        "117",
        "-2",
        "-2"
      ],
      "halves": [
        {
          "n": 18,
          "best": 10,
          "classes": 1233
        },
        {
          "n": 36,
          "best": null,
          "reason": "root capacity"
        }
      ]
    },
    {
      "l": [
        "198",
        "8",
        "-1"
      ],
      "halves": [
        {
          "n": 42,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 6,
          "best": 3,
          "classes": 91
        }
      ]
    },
    {
      "l": [
        "198",
        "5",
        "-4"
      ],
      "halves": [
        {
          "n": 28,
          "best": 15,
          "classes": 1525
        },
        {
          "n": 26,
          "best": 13,
          "classes": 1751
        }
      ]
    },
    {
      "l": [
        "306",
        "17",
        "-1"
      ],
      "halves": [
        {
          "n": 45,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 2,
          "best": 1,
          "classes": 13
        }
      ]
    },
    {
      "l": [
        "234",
        "-1",
        "-1"
      ],
      "halves": [
        {
          "n": 41,
          "best": null,
          "reason": "root capacity"
        },
        {
          "n": 18,
          "best": 9,
          "classes": 485
        }
      ]
    }
  ]
}
```

To replay, extract the following JS into a Node.js file and run. The embedded expected active records are the exact R176 pinned JSON array; the code regenerates the complete active intervals, checks the records, then enumerates the two-layer conditions.

```js
function research(data){
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0,gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a,norm=p=>{let d=p.reduce(gcd,0n);return d?p.map(x=>x/d):p},canon=p=>{p=norm(p);return (p.find(x=>x)??0n)<0n?p.map(x=>-x):p},uniq=a=>[...new Map(a.map(p=>[p.join(),p])).values()];
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],W=[0,3,5,6,7,9],M=[30,51,42,21,58,51,20,7,23,30],E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]].map(x=>x.map(BigInt));
const gaps=([x,y,z])=>{let h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z],g=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)g.push(BigInt(Math.abs(h[j]-h[i])));return g};const G=V.map(gaps),terms=(rows,mask)=>{let s=new Map();for(let i of rows)G[i].forEach((g,j)=>{if(g&&(!mask||(M[i]>>j&1)))s.set(`${j},${g}`,[j,g])});return [...s.values()].sort((a,b)=>a[0]-b[0]||Number(a[1]-b[1]))},T=terms(W,true),H=terms(V.map((_,i)=>i),false);
const line=(a,b,k,l)=>canon(E[b[0]].map((x,i)=>k*a[1]*x-l*b[1]*E[a[0]][i]));let L=[];for(let a of T){for(let b of T)L.push(line(a,b,1n,1n));for(let b of H)L.push(line(a,b,3n,2n))}L=uniq(L.filter(q=>q.some(x=>x<0n)&&q.some(x=>x>0n)));const axes=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]],all=L.concat(axes),abs=x=>x<0n?-x:x;let K=1n;for(let l of L)for(let m of all)if(abs(dot(l,m))>=K)K=abs(dot(l,m))+1n;
function label(p){let s=E.map(e=>dot(e,p));function score(row){let a=0n,b=1n;for(let j=0;j<6;j++)if(row[j]*b>a*s[j]){a=row[j];b=s[j]}return [a,b]}let fs=G.map(score),[a,b]=fs[W[0]];for(let i of W){let [c,d]=fs[i];if(c*b<a*d){a=c;b=d}}let m=0,n=0;for(let i=0;i<T.length;i++){let [j,g]=T[i];if(g*b===a*s[j])m|=1<<i}for(let i=0;i<fs.length;i++)if(2n*fs[i][0]*b<3n*a*fs[i][1])n|=1<<i;return [m,n]}
let active=[],segments=0,changes=0;const den=p=>p.reduce((s,x)=>s+x,0n),cmp=(a,b,i)=>sg(a[i]*den(b)-b[i]*den(a));for(let l of L){let ps=uniq(all.map(m=>canon(cross(l,m))).filter(p=>p.some(x=>x>0n)&&p.every(x=>x>=0n)));let ax=[0,1,2].find(i=>ps.some(p=>cmp(p,ps[0],i)));if(ax===undefined)continue;ps.sort((a,b)=>cmp(a,b,ax));let act=[];for(let i=0;i+1<ps.length;i++){let p=norm(ps[i].map((x,j)=>x+ps[i+1][j]));if(p.some(x=>x<=0n))continue;let pp=p.map((x,j)=>K*x+l[j]),pm=p.map((x,j)=>K*x-l[j]);if(pp.some(x=>x<=0n)||pm.some(x=>x<=0n))throw Error('perturbation');let a=label(pp),b=label(pm),c=label(p);segments++;if(a[1]!==b[1]||c[1]!==a[1]||!(a[0]&b[0]&c[0])){changes++;act.push([ps[i],ps[i+1]])}}if(act.length){let ends=[act[0][0],act.at(-1)[1]];active.push({l,ax,act,p:ends})}}
let reconstructed=active.map(x=>({normal:x.l.map(String),segments:x.act.length,endpoints:x.p.map(p=>p.map(String))}));if(JSON.stringify(reconstructed)!==JSON.stringify(data)||segments!==21842||changes!==1574)throw Error('pinned census mismatch');
let gapsBetween=active.reduce((s,e)=>s+e.act.slice(1).filter((uv,i)=>cmp(e.act[i][1],uv[0],e.ax)!==0).length,0);
function states(P){if(!P.length)return [[0n,0n]];if(P.length===1)return [[1n,0n],[0n,0n]];let S=new Map();function rec(r,t=null,p=null,s=1,u=1){let a=0n,b=0n;for(let i=0;i<P.length;i++){let x=sg(dot(r,P[i]));if(!x&&t)x=s*sg(dot(t,P[i]));if(!x&&p)x=u*sg(dot(p,P[i]));if(x>0)a|=1n<<BigInt(i);if(x<0)b|=1n<<BigInt(i)}let k=a<b?`${a},${b}`:`${b},${a}`;if(!S.has(k))S.set(k,[a,b]);}for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){let r=cross(P[i],P[j]);if(!r.some(Boolean))continue;rec(r);for(let k=0;k<P.length;k++)if(!dot(r,P[k])){let t=cross(r,P[k]);for(let s of [-1,1]){rec(r,t,null,s);for(let u of [-1,1])rec(r,t,P[k],s,u)}}}return [...S.values()]}
function carrier(edges){let P=uniq(edges.flatMap(e=>e.p)),ix=new Map(P.map((p,i)=>[p.join(),i]));let masks=edges.map(e=>e.p.reduce((v,p)=>v|(1n<<BigInt(ix.get(p.join()))),0n));return {P,masks,S:states(P)}}
const {P,masks,S}=carrier(active),cache=new Map();function count(m){if(!cache.has(m))cache.set(m,masks.filter(e=>!!(e&m)).length);return cache.get(m)}let roots=S.filter(([a,b])=>count(a)<=31&&count(b)<=31),memo=new Map();function feasible(m){if(memo.has(m))return memo.get(m);let ans=S.some(([a,b])=>count(m&a)<=15&&count(m&b)<=15);memo.set(m,ans);return ans}let strict=roots.filter(([a,b])=>feasible(a)&&feasible(b));
let closureMemo=new Map();function closureFeasible(a,b){let eligible=masks.filter(e=>!!(e&a)).map(e=>e&~b);let key=eligible.join(';');if(closureMemo.has(key))return closureMemo.get(key);let ans=S.some(([u,v])=>eligible.filter(e=>!!(e&u)).length<=15&&eligible.filter(e=>!!(e&v)).length<=15);closureMemo.set(key,ans);return ans}let closed=strict.filter(([a,b])=>closureFeasible(a,b)&&closureFeasible(b,a));
function clippedEdges(r,s){let out=[];for(let f of active){let parts=[];for(let [u0,v0] of f.act){let u=u0,v=v0,a=s*dot(r,u),b=s*dot(r,v);if(a<=0n&&b<=0n)continue;if(a<0n)u=norm(u.map((x,i)=>b*x-a*v[i]));else if(b<0n)v=norm(v.map((x,i)=>a*x-b*u[i]));parts.push([u,v]);}if(parts.length)out.push({l:f.l,p:[parts[0][0],parts.at(-1)[1]]})}return out}
let fixed=[];for(let e of active){let halves=[];for(let s of [1n,-1n]){let clipped=clippedEdges(e.l,s),n=clipped.length;if(n>31){halves.push({n,best:null,reason:"root capacity"});continue}let c=carrier(clipped),best=99;for(let [a,b] of c.S){let x=c.masks.filter(e=>!!(e&a)).length,y=c.masks.filter(e=>!!(e&b)).length;best=Math.min(best,Math.max(x,y));}halves.push({n,best,classes:c.S.length})}fixed.push({l:e.l.map(String),halves})}
return {segments,changes,supports:active.length,activeRunGaps:gapsBetween,endpointRays:P.length,rootClasses:S.length,rootCapacitySurvivors:roots.length,strictEndpointSecondSurvivors:strict.length,closureEndpointSecondSurvivors:closed.length,strictSideMasks:memo.size,closureSideCarriers:closureMemo.size,fixedRootFirstPass:fixed.filter(x=>x.halves.every(h=>h.n<=31)).length,fixedRootSecondPass:fixed.filter(x=>x.halves.every(h=>h.best!==null&&h.best<=15)).length,fixed}
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
console.log(JSON.stringify(research(data),null,2));
```

## Next

Use the conditional support carrier to search the remaining 537 root classes. To reason uniformly about the true cut intersection in a root class, retain its dependence on root coefficients rather than choosing a single representative. One useful subproblem is to combine the support capacity with independent finite-point incompatibility constraints, or build a depth-six tree. R175's 884-predicate sharp result is closed and is not repeated. Current exact Task lookup request r2-20261124-2310-x6-current-read-v1 SUCCEEDED/error=null at 2026-11-24T15:10:35.019921Z, source d4b2a7149f7c33ff4e9b0c0d2a762dc59de9b6e8, NO_CANONICAL_PUBLICATION_DIRECTORY, execution_authorized=false; no native owner projection. Source preservation only; Activity association pending real binding verification. Independent review pending.
