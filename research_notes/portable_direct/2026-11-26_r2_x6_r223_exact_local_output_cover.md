# X6 R223 — exact local output-cover budget and focused continuation

2026-11-26; AUTHOR PROOF AND EXACT COMPUTATION / NOT_REVIEWED. Informed static six-pair BRC continuation, frozen scientific scope and bank qualification of R222, Port 10, positive (17t,B,22t,D), 1935 directions. Source R222@38b019d661cef0fa0a46ee3a81b40aa6fb9801ea:research_notes/portable_direct/2026-11-26_r2_x6_r222_joint_budget_resynthesis.md. No repinning or change of output semantics.

## Exact local output-cover resource

For each near mask n and each of the fixed 35 labels a of that mask, let C_a be the exact support-sign fibers on which a is legal (intersection over raw arrangement faces). For any subset of fibers S, define h_n(S)=min{|J|: S intersect G_n is contained in union_{a in J} C_a}, and h_n=0 if empty. The exact minimum number of output labels that can cover S is H(S)=sum_n h_n(S), because near-mask groups are disjoint and each label covers only its own group. Any depth-d binary tree on S needs at least H(S) leaves. This replaces R222's singleton lower bound with the exact set-cover bound within the fixed output alphabet. Enumerate the finite subsets within each near group and precompute their union masks, ordered by cardinality. All zero-sign fibers retained. The bound is exact for unconstrained label coverage, not necessarily realizable by the permitted queries at a given depth. The recurrence and minimum-cost partition deduplication from R222 remain exact; search-budget exits are UNKNOWN. A constructed tree is verified directly over all fibers, not inferred from a search failure. Arbitrary-coefficient K6 lower bound remains 1, upper bound 3.

## Computation

Regenerated exact 256-form arrangement and 1925 support fibers; root distinct unordered partitions counted after minimum-cost dedup. The focused budget-two child queries and budget-three global search have actual statuses in the output below. Coverage bounds, search states, split scans and budgets are separate counters. Full direction scores inherited from R220/R221, not rerun. All results below are restricted to the R222 35-label alphabet and 2303-query library for any negative search conclusions. No independent review.

```json
{
  "rootStats": {
    "linear": 94,
    "quadratic": 2209,
    "weakEligible": 1803,
    "exactEligible": 1803,
    "strictGain": 14,
    "maxGain": 2
  },
  "rawLines": 256,
  "cells": 11487,
  "positiveRepresentatives": 43685,
  "patterns": 1925,
  "labels": 35,
  "old": {
    "hist": {
      "1": 638,
      "2": 305,
      "3": 756,
      "4": 226
    },
    "depth": {
      "5": 23,
      "6": 1902
    },
    "n": 1925,
    "maxq": 4,
    "nodes": [
      60,
      9,
      61
    ],
    "outputs": 35,
    "maxDistinct": 10,
    "joint": 4420
  },
  "optimized": {
    "hist": {
      "0": 82,
      "1": 752,
      "2": 840,
      "3": 251
    },
    "depth": {
      "5": 15,
      "6": 1910
    },
    "n": 1925,
    "maxq": 3,
    "nodes": [
      59,
      14,
      60
    ],
    "outputs": 35,
    "maxDistinct": 8,
    "joint": 3185
  },
  "logs": [
    {
      "path": "R222-root-Y",
      "d": 5,
      "target": 2,
      "status": "FOUND",
      "states": 104,
      "scans": 5072
    },
    {
      "path": "R222-root-N",
      "d": 5,
      "target": 2,
      "status": "EXHAUSTED",
      "states": 5592,
      "scans": 1612759
    },
    {
      "path": "ROOT",
      "d": 6,
      "target": 3,
      "status": "FOUND",
      "states": 7396,
      "scans": 2314119
    }
  ],
  "visited": 13092,
  "scans": 3931950,
  "cut": 0,
  "boundCalls": 7887914,
  "tree": {
    "q": [
      12,
      -1,
      1
    ],
    "yes": {
      "q": [
        19,
        29,
        -1
      ],
      "yes": {
        "q": [
          2,
          -1,
          1
        ],
        "yes": {
          "q": [
            7,
            9,
            -1
          ],
          "yes": {
            "q": [
              8,
              -1,
              -1
            ],
            "yes": {
              "out": [
                951,
                4
              ]
            },
            "no": {
              "q": [
                10,
                -1,
                -1
              ],
              "yes": {
                "out": [
                  695,
                  4
                ]
              },
              "no": {
                "out": [
                  693,
                  4
                ]
              }
            }
          },
          "no": {
            "q": [
              9,
              25,
              -1
            ],
            "yes": {
              "q": [
                41,
                -1,
                1
              ],
              "yes": {
                "out": [
                  951,
                  4096
                ]
              },
              "no": {
                "out": [
                  693,
                  4096
                ]
              }
            },
            "no": {
              "q": [
                7,
                -1,
                1
              ],
              "yes": {
                "out": [
                  132,
                  4
                ]
              },
              "no": {
                "out": [
                  693,
                  4096
                ]
              }
            }
          }
        },
        "no": {
          "q": [
            11,
            27,
            1
          ],
          "yes": {
            "q": [
              25,
              -1,
              1
            ],
            "yes": {
              "q": [
                11,
                -1,
                1
              ],
              "yes": {
                "out": [
                  132,
                  16
                ]
              },
              "no": {
                "out": [
                  693,
                  16
                ]
              }
            },
            "no": {
              "q": [
                16,
                -1,
                1
              ],
              "yes": {
                "out": [
                  693,
                  4096
                ]
              },
              "no": {
                "out": [
                  693,
                  64
                ]
              }
            }
          },
          "no": {
            "q": [
              23,
              27,
              1
            ],
            "yes": {
              "q": [
                26,
                -1,
                -1
              ],
              "yes": {
                "out": [
                  693,
                  16
                ]
              },
              "no": {
                "out": [
                  692,
                  16
                ]
              }
            },
            "no": {
              "q": [
                27,
                -1,
                -1
              ],
              "yes": {
                "out": [
                  676,
                  16
                ]
              },
              "no": {
                "out": [
                  132,
                  16
                ]
              }
            }
          }
        }
      },
      "no": {
        "q": [
          11,
          -1,
          1
        ],
        "yes": {
          "q": [
            2,
            -1,
            1
          ],
          "yes": {
            "q": [
              6,
              -1,
              1
            ],
            "yes": {
              "out": [
                132,
                32
              ]
            },
            "no": {
              "out": [
                132,
                4
              ]
            }
          },
          "no": {
            "q": [
              28,
              -1,
              1
            ],
            "yes": {
              "q": [
                24,
                -1,
                1
              ],
              "yes": {
                "out": [
                  132,
                  32
                ]
              },
              "no": {
                "out": [
                  132,
                  16
                ]
              }
            },
            "no": {
              "q": [
                27,
                28,
                1
              ],
              "yes": {
                "out": [
                  164,
                  16
                ]
              },
              "no": {
                "out": [
                  132,
                  16
                ]
              }
            }
          }
        },
        "no": {
          "q": [
            16,
            42,
            1
          ],
          "yes": {
            "q": [
              44,
              -1,
              1
            ],
            "yes": {
              "q": [
                16,
                -1,
                1
              ],
              "yes": {
                "out": [
                  693,
                  4096
                ]
              },
              "no": {
                "out": [
                  561,
                  64
                ]
              }
            },
            "no": {
              "q": [
                5,
                -1,
                1
              ],
              "yes": {
                "out": [
                  689,
                  4096
                ]
              },
              "no": {
                "out": [
                  561,
                  4096
                ]
              }
            }
          },
          "no": {
            "q": [
              38,
              -1,
              1
            ],
            "yes": {
              "q": [
                36,
                -1,
                1
              ],
              "yes": {
                "out": [
                  561,
                  4096
                ]
              },
              "no": {
                "out": [
                  561,
                  2048
                ]
              }
            },
            "no": {
              "q": [
                39,
                -1,
                1
              ],
              "yes": {
                "out": [
                  561,
                  4096
                ]
              },
              "no": {
                "out": [
                  561,
                  16384
                ]
              }
            }
          }
        }
      }
    },
    "no": {
      "q": [
        14,
        -1,
        1
      ],
      "yes": {
        "q": [
          3,
          -1,
          1
        ],
        "yes": {
          "q": [
            4,
            15,
            1
          ],
          "yes": {
            "q": [
              13,
              -1,
              1
            ],
            "yes": {
              "q": [
                30,
                -1,
                1
              ],
              "yes": {
                "out": [
                  561,
                  4096
                ]
              },
              "no": {
                "out": [
                  561,
                  128
                ]
              }
            },
            "no": {
              "q": [
                22,
                -1,
                -1
              ],
              "yes": {
                "out": [
                  633,
                  8
                ]
              },
              "no": {
                "out": [
                  561,
                  8
                ]
              }
            }
          },
          "no": {
            "q": [
              34,
              -1,
              1
            ],
            "yes": {
              "q": [
                5,
                15,
                1
              ],
              "yes": {
                "out": [
                  561,
                  2
                ]
              },
              "no": {
                "out": [
                  561,
                  4096
                ]
              }
            },
            "no": {
              "q": [
                37,
                -1,
                -1
              ],
              "yes": {
                "out": [
                  121,
                  1024
                ]
              },
              "no": {
                "out": [
                  49,
                  1024
                ]
              }
            }
          }
        },
        "no": {
          "q": [
            18,
            -1,
            1
          ],
          "yes": {
            "q": [
              38,
              -1,
              1
            ],
            "yes": {
              "q": [
                16,
                -1,
                1
              ],
              "yes": {
                "out": [
                  561,
                  2048
                ]
              },
              "no": {
                "out": [
                  561,
                  8
                ]
              }
            },
            "no": {
              "q": [
                39,
                -1,
                1
              ],
              "yes": {
                "out": [
                  561,
                  4096
                ]
              },
              "no": {
                "out": [
                  561,
                  16384
                ]
              }
            }
          },
          "no": {
            "q": [
              21,
              22,
              1
            ],
            "yes": {
              "q": [
                21,
                -1,
                1
              ],
              "yes": {
                "out": [
                  561,
                  8
                ]
              },
              "no": {
                "out": [
                  633,
                  8
                ]
              }
            },
            "no": {
              "q": [
                20,
                22,
                1
              ],
              "yes": {
                "out": [
                  569,
                  8
                ]
              },
              "no": {
                "out": [
                  561,
                  8
                ]
              }
            }
          }
        }
      },
      "no": {
        "q": [
          1,
          31,
          1
        ],
        "yes": {
          "q": [
            35,
            -1,
            1
          ],
          "yes": {
            "q": [
              17,
              -1,
              1
            ],
            "yes": {
              "q": [
                15,
                -1,
                -1
              ],
              "yes": {
                "out": [
                  633,
                  8
                ]
              },
              "no": {
                "out": [
                  121,
                  1024
                ]
              }
            },
            "no": {
              "q": [
                46,
                -1,
                1
              ],
              "yes": {
                "out": [
                  633,
                  8192
                ]
              },
              "no": {
                "out": [
                  72,
                  8192
                ]
              }
            }
          },
          "no": {
            "q": [
              40,
              46,
              1
            ],
            "yes": {
              "q": [
                40,
                -1,
                1
              ],
              "yes": {
                "out": [
                  121,
                  8192
                ]
              },
              "no": {
                "out": [
                  72,
                  8192
                ]
              }
            },
            "no": {
              "q": [
                43,
                46,
                1
              ],
              "yes": {
                "out": [
                  89,
                  8192
                ]
              },
              "no": {
                "out": [
                  72,
                  8192
                ]
              }
            }
          }
        },
        "no": {
          "q": [
            0,
            -1,
            1
          ],
          "yes": {
            "q": [
              1,
              -1,
              1
            ],
            "yes": {
              "q": [
                32,
                -1,
                1
              ],
              "yes": {
                "out": [
                  633,
                  256
                ]
              },
              "no": {
                "out": [
                  72,
                  256
                ]
              }
            },
            "no": {
              "out": [
                72,
                1
              ]
            }
          },
          "no": {
            "q": [
              16,
              -1,
              1
            ],
            "yes": {
              "q": [
                45,
                -1,
                1
              ],
              "yes": {
                "out": [
                  72,
                  8192
                ]
              },
              "no": {
                "out": [
                  64,
                  8192
                ]
              }
            },
            "no": {
              "q": [
                33,
                -1,
                1
              ],
              "yes": {
                "out": [
                  72,
                  512
                ]
              },
              "no": {
                "out": [
                  64,
                  512
                ]
              }
            }
          }
        }
      }
    }
  }
}
```

## Reproduction (JavaScript function body)

```javascript
function audit(tree){
const R="187,12,-1;204,11,-1;5,-2,0;9,-1,0;85,7,-2;51,2,-1;0,1,-1;34,1,-1;187,20,-9;68,1,-3;176,22,-9;22,0,-1;61,0,-1;74,0,-1;126,0,-1;4,-1,0;17,-1,0;156,-1,-1;69,0,-1;9,0,-1;235,0,-3;87,0,-1;104,-1,-1;38,0,-3;5,0,-2;39,-1,-1;40,0,-3;26,-1,-1;25,0,-3;83,0,-2;102,-7,-1;204,-11,1;395,0,-2;289,18,-1;66,2,-1;132,5,-1;44,1,-1;88,3,-1;88,7,-3;132,-7,-1;153,8,-1;153,5,-4;117,-2,-2;198,8,-1;198,5,-4;306,17,-1;234,-1,-1".split(";").map(s=>s.split(",").map(BigInt));
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],T=[[0,1],[0,2],[0,3],[1,3],[1,6],[2,3],[2,6],[2,7],[2,11],[2,12],[3,2],[3,3],[4,6],[4,12],[5,7]],E=[[17n,1n,0n],[39n,0n,0n],[17n,0n,1n],[22n,1n,0n],[0n,1n,1n],[22n,0n,1n]];
function gaps(v){let [x,y,z]=v,h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]].map(([i,j])=>BigInt(Math.abs(h[i]-h[j])))}
const G=V.map(gaps),W=[0,3,5,6,7,9],D=[];
for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){let v=[x,y,z];if((v.find(a=>a!==0)||0)>0&&v.reduce((s,a)=>s+Math.max(a,0),0)<=10&&v.reduce((s,a)=>s+Math.max(-a,0),0)<=10)D.push([v,gaps(v)])}
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){let t=a%b;a=b;b=t}return a}
function norm(a,unoriented=false){let d=gcd(gcd(a[0],a[1]),a[2]);if(!d)return a;a=a.map(x=>x/d);if(unoriented&&a.find(x=>x!==0n)<0n)a=a.map(x=>-x);return a}
let raw=new Map();function addLine(a){a=norm(a,true);if(a.some(x=>x>0n)&&a.some(x=>x<0n))raw.set(a.join(),a)}
for(let i=0;i<T.length;i++){let [j,g]=T[i];for(let k=i+1;k<T.length;k++){let [h,f]=T[k];addLine(E[h].map((x,s)=>BigInt(g)*x-BigInt(f)*E[j][s]))}for(let gg of G)for(let h=0;h<6;h++)if(gg[h])addLine(E[h].map((x,s)=>3n*BigInt(g)*x-2n*gg[h]*E[j][s]))}
let L=[...raw.values()];for(let r of R)if(!raw.has(norm(r,true).join()))throw Error("support absent");
let cells=[[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]]];
for(let l of L){let next=[];for(let cell of cells){let sig=cell.map(x=>dot(l,x));if(!sig.some(x=>x>0n)||!sig.some(x=>x<0n)){next.push(cell);continue}for(let side of [1n,-1n]){let out=[];for(let i=0;i<cell.length;i++){let j=(i+1)%cell.length,a=sig[i],b=sig[j];if(a*side>=0n)out.push(cell[i]);if(a*b<0n){let r=cross(cross(cell[i],cell[j]),l);if(r.some(x=>x<0n))r=r.map(x=>-x);if(r.some(x=>x<0n)||!r.some(x=>x>0n)||dot(r,l)!==0n)throw Error("bad intersection");out.push(norm(r))}}next.push(out)}}cells=next}
const pts=new Map();function put(a){if(a.every(x=>x>0n)){a=norm(a);pts.set(a.join(),a)}}function sum(a){return [0,1,2].map(i=>a.reduce((s,x)=>s+x[i],0n))}
for(let c of cells){put(sum(c));for(let i=0;i<c.length;i++){put(c[i]);put(sum([c[i],c[(i+1)%c.length]]))}}

const patterns=new Map(), sign=p=>R.map(r=>{let x=dot(r,p);return x>0n?1:x<0n?-1:0});
for(const p of pts.values()){let s=sign(p),k=s.join();if(!patterns.has(k))patterns.set(k,s)}
const A=[...patterns.values()],N=A.length,all=(1n<<BigInt(N))-1n;
let pos=R.map(()=>0n),neg=R.map(()=>0n);
A.forEach((s,i)=>s.forEach((x,j)=>{if(x>0)pos[j]|=1n<<BigInt(i);if(x<0)neg[j]|=1n<<BigInt(i)}));
const mask=([i,j,sg])=>j<0?(sg>0?pos[i]:neg[i]):sg>0?((pos[i]&pos[j])|(neg[i]&neg[j])):((pos[i]&neg[j])|(neg[i]&pos[j]));
const qs=[];for(let i=0;i<R.length;i++){for(let s of [1,-1])qs.push([i,-1,s]);for(let j=i;j<R.length;j++)for(let s of [1,-1])if(i!==j||s===1)qs.push([i,j,s])}
const Q=qs.map(q=>({q,b:mask(q)}));
const count=b=>{let n=0;while(b){b&=b-1n;n++}return n};
const factors=q=>q[1]<0||q[0]===q[1]?[q[0]]:[q[0],q[1]];

const ix=new Map(A.map((s,i)=>[s.join(),i]));
const labels=new Map(), fibers=Array(N).fill(null);
const max=a=>a.reduce((x,y)=>x>y?x:y),min=a=>a.reduce((x,y)=>x<y?x:y);
for(const p of pts.values()){
 const c=E.map(e=>dot(e,p)),pr=c.reduce((a,b)=>a*b,1n),scale=c.map(x=>pr/x),scores=G.map(g=>max(g.map((a,i)=>a*scale[i]))),eta=min(W.map(i=>scores[i]));
 let n=0,m=0;for(let i=0;i<scores.length;i++)if(2n*scores[i]<3n*eta)n|=1<<i;
 for(let i=0;i<T.length;i++){let [j,g]=T[i];if(BigInt(g)*scale[j]===eta)m|=1<<i}
 const i=ix.get(sign(p).join()),f=fibers[i];if(!f)fibers[i]=[n,m];else{if(f[0]!==n)throw Error("near fiber mismatch");f[1]&=m;if(!f[1])throw Error("empty intersection")}
}
function gather(t){if(t.out){labels.set(t.out.join(),t.out);return}gather(t.yes);gather(t.no)}gather(tree);
const lab=[...labels.values()],covers=lab.map(()=>0n),groups=new Map(),single=lab.map(()=>0n);
for(let i=0;i<N;i++){let [n,m]=fibers[i],b=1n<<BigInt(i),hits=[];for(let j=0;j<lab.length;j++)if(lab[j][0]===n&&(lab[j][1]&m)){covers[j]|=b;hits.push(j)}if(!hits.length)throw Error("uncovered");if(hits.length===1)single[hits[0]]|=b;groups.set(n,(groups.get(n)||0n)|b)}
const groupList=[...groups].map(([n,b])=>({b,s:lab.map((l,j)=>l[0]===n?single[j]:0n).filter(Boolean)}));
function weakBound(S,lim=1e9){let n=0;for(let g of groupList)if(g.b&S){let z=0;for(let b of g.s)if(b&S)z++;n+=Math.max(1,z);if(n>lim)return n}return n}

const exactGroups=[...groups].map(([n,b])=>{
 const cs=lab.map((l,i)=>l[0]===n?covers[i]:0n).filter(Boolean),opts=[];
 for(let m=1;m<(1<<cs.length);m++){let v=0n,k=0;for(let j=0;j<cs.length;j++)if(m&(1<<j)){v|=cs[j];k++}opts.push({v,k})}
 opts.sort((a,b)=>a.k-b.k);return {b,opts}
});
let boundCalls=0,strictGains=0,maximumGain=0;
function bound(S,lim=1e9){boundCalls++;let n=0;for(let g of exactGroups){let x=S&g.b;if(!x)continue;let z=g.opts.find(o=>(x&o.v)===x);if(!z)throw Error("coverage missing");n+=z.k;if(n>lim)return n}return n}
function leaf(S){for(let i=0;i<covers.length;i++)if((S&covers[i])===S)return {out:lab[i]};return null}
Q.sort((a,b)=>Number(a.q[1]>=0)-Number(b.q[1]>=0));
let visited=0, scans=0, cut=0, cap=1000, memo=new Map();
const stop={};
function solve(S,d,k){
 let l=leaf(S);if(l)return l;if(!d||bound(S,1<<d)>(1<<d))return null;
 k=Math.min(k,d);const key=S.toString(36)+"/"+d+"/"+k;if(memo.has(key))return memo.get(key);
 if(++visited>cap)throw stop;
 let seen=new Set(),candidates=[],lim=1<<(d-1);
 for(let c of Q){if(c.q[1]>=0&&!k)continue;let y=c.b&S,z=S^y;if(!y||!z)continue;let part=y<z?y:z;if(seen.has(part))continue;seen.add(part);scans++;
 let a=bound(y,lim),b=bound(z,lim);if(a>lim||b>lim)continue;
 if(d===1){let yy=leaf(y),zz=leaf(z);if(yy&&zz){let t={q:c.q,yes:yy,no:zz};memo.set(key,t);return t}continue}
 candidates.push({q:c.q,y,z,a,b,score:Math.max(a,b)*100+(a+b)*3+Number(c.q[1]>=0)*2});
 }
 candidates.sort((a,b)=>a.score-b.score);
 for(let c of candidates){let k1=k-Number(c.q[1]>=0);let yy,zz;if(c.a>=c.b){yy=solve(c.y,d-1,k1);if(!yy)continue;zz=solve(c.z,d-1,k1)}else{zz=solve(c.z,d-1,k1);if(!zz)continue;yy=solve(c.y,d-1,k1)}if(yy&&zz){let t={q:c.q,yes:yy,no:zz};memo.set(key,t);return t}}
 memo.set(key,null);return null
}
function maxq(t){return t.out?0:Number(t.q[1]>=0)+Math.max(maxq(t.yes),maxq(t.no))}
function nodes(t){if(t.out)return [0,0,1];let a=nodes(t.yes),b=nodes(t.no);return [1+a[0]+b[0],Number(t.q[1]>=0)+a[1]+b[1],a[2]+b[2]]}
const logs=[];
function trial(S,d,k,path){
 let start=visited,sc0=scans;cap=visited+(d===6?18000:d>=4?10000:500);let ans=null,status;
 try{ans=solve(S,d,k);status=ans?"FOUND":"EXHAUSTED"}catch(e){if(e!==stop)throw e;status="BUDGET";cut++}
 logs.push({path,d,target:k,status,states:visited-start,scans:scans-sc0});return ans
}
function improve(t,S,d,path,ceiling){
 if(t.out)return t;
 let y=mask(t.q)&S,z=S^y;
 t={q:t.q,yes:improve(t.yes,y,d-1,path+"Y",ceiling),no:improve(t.no,z,d-1,path+"N",ceiling)};
 if(d>ceiling||d<1)return t;
 let b=maxq(t);
 while(b>0){let ans=trial(S,d,b-1,path);if(!ans)break;t=ans;b=maxq(t)}
 return t;
}
function verify(t){let h={},depth={},joint=0,outputs=new Set(),maxDistinct=0;for(let i=0;i<N;i++){let x=t,d=0,k=0,f=new Set();while(x.q){let [a,b,s]=x.q;d++;k+=Number(b>=0);f.add(a);if(b>=0)f.add(b);x=s*A[i][a]*(b<0?1:A[i][b])>0?x.yes:x.no}let [nm,mm]=fibers[i];if(x.out[0]!==nm||!(x.out[1]&mm))throw Error("bad output");if(d>6)throw Error("depth");outputs.add(x.out.join());maxDistinct=Math.max(maxDistinct,f.size);h[k]=(h[k]||0)+1;depth[d]=(depth[d]||0)+1;joint+=k}return {hist:h,depth,n:N,maxq:maxq(t),nodes:nodes(t),outputs:outputs.size,maxDistinct,joint}}

let t=tree;
let rootStats={linear:0,quadratic:0,weakEligible:0,exactEligible:0,strictGain:0,maxGain:0};
let seenRoot=new Set();
for(let q of Q){let y=q.b&all,z=all^y;if(!y||!z)continue;let p=y<z?y:z;if(seenRoot.has(p))continue;seenRoot.add(p);if(q.q[1]<0)rootStats.linear++;else rootStats.quadratic++;
let w1=weakBound(y),w2=weakBound(z),x1=bound(y),x2=bound(z);if(Math.max(w1,w2)<=32)rootStats.weakEligible++;if(Math.max(x1,x2)<=32)rootStats.exactEligible++;if(x1>w1||x2>w2){rootStats.strictGain++;rootStats.maxGain=Math.max(rootStats.maxGain,x1-w1,x2-w2)}
}
let y=mask(t.q)&all,z=all^y;
let ny=trial(y,5,2,"R222-root-Y"),nz=trial(z,5,2,"R222-root-N");
if(ny&&nz)t={q:t.q,yes:ny,no:nz};
else {if(ny)t={...t,yes:ny};if(nz)t={...t,no:nz};}
let best=maxq(t);
if(best>3){let ans=trial(all,6,3,"ROOT");if(ans)t=ans}
return {rootStats,rawLines:L.length,cells:cells.length,positiveRepresentatives:pts.size,patterns:N,labels:lab.length,old:verify(tree),optimized:verify(t),logs,visited,scans,cut,boundCalls,tree:t};
}
return audit({"q":[1,29,1],"yes":{"q":[9,-1,-1],"yes":{"q":[7,-1,1],"yes":{"q":[2,-1,1],"yes":{"q":[8,-1,-1],"yes":{"out":[951,4]},"no":{"q":[10,-1,-1],"yes":{"out":[695,4]},"no":{"out":[693,4]}}},"no":{"q":[16,-1,1],"yes":{"q":[25,-1,1],"yes":{"out":[693,16]},"no":{"out":[693,4096]}},"no":{"out":[693,64]}}},"no":{"q":[0,-1,1],"yes":{"q":[25,-1,1],"yes":{"q":[41,-1,1],"yes":{"out":[951,4096]},"no":{"out":[693,4096]}},"no":{"q":[1,-1,1],"yes":{"out":[693,4096]},"no":{"out":[72,1]}}},"no":{"q":[16,-1,1],"yes":{"q":[45,-1,1],"yes":{"out":[72,8192]},"no":{"out":[64,8192]}},"no":{"q":[33,-1,1],"yes":{"out":[72,512]},"no":{"out":[64,512]}}}}},"no":{"q":[23,-1,-1],"yes":{"q":[25,-1,1],"yes":{"q":[27,-1,-1],"yes":{"q":[26,-1,-1],"yes":{"out":[693,16]},"no":{"out":[692,16]}},"no":{"q":[2,-1,1],"yes":{"out":[132,4]},"no":{"out":[132,16]}}},"no":{"q":[11,-1,1],"yes":{"q":[26,-1,-1],"yes":{"out":[693,16]},"no":{"out":[692,16]}},"no":{"q":[16,-1,1],"yes":{"out":[693,4096]},"no":{"out":[693,64]}}}},"no":{"q":[27,-1,-1],"yes":{"q":[28,-1,-1],"yes":{"q":[19,-1,-1],"yes":{"out":[676,16]},"no":{"out":[164,16]}},"no":{"q":[24,-1,1],"yes":{"out":[132,32]},"no":{"out":[132,16]}}},"no":{"q":[2,-1,1],"yes":{"q":[6,-1,1],"yes":{"out":[132,32]},"no":{"out":[132,4]}},"no":{"q":[24,-1,1],"yes":{"out":[132,32]},"no":{"out":[132,16]}}}}}},"no":{"q":[20,-1,-1],"yes":{"q":[31,35,1],"yes":{"q":[15,46,-1],"yes":{"q":[17,22,-1],"yes":{"q":[21,-1,-1],"yes":{"out":[633,8]},"no":{"out":[569,8]}},"no":{"q":[17,-1,1],"yes":{"out":[561,8]},"no":{"out":[633,8192]}}},"no":{"q":[3,-1,1],"yes":{"q":[37,-1,-1],"yes":{"out":[121,1024]},"no":{"out":[49,1024]}},"no":{"q":[31,-1,1],"yes":{"out":[72,8192]},"no":{"out":[72,256]}}}},"no":{"q":[31,-1,1],"yes":{"q":[40,46,1],"yes":{"q":[40,-1,1],"yes":{"out":[121,8192]},"no":{"out":[72,8192]}},"no":{"q":[43,46,1],"yes":{"out":[89,8192]},"no":{"out":[72,8192]}}},"no":{"q":[14,-1,-1],"yes":{"q":[32,-1,1],"yes":{"out":[633,256]},"no":{"out":[72,256]}},"no":{"q":[21,-1,-1],"yes":{"out":[633,8]},"no":{"out":[569,8]}}}}},"no":{"q":[5,16,1],"yes":{"q":[18,42,1],"yes":{"q":[18,-1,1],"yes":{"q":[44,-1,1],"yes":{"out":[693,4096]},"no":{"out":[689,4096]}},"no":{"out":[561,8]}},"no":{"q":[38,-1,-1],"yes":{"q":[39,-1,1],"yes":{"out":[561,4096]},"no":{"out":[561,16384]}},"no":{"q":[36,-1,1],"yes":{"out":[561,4096]},"no":{"out":[561,2048]}}}},"no":{"q":[3,30,1],"yes":{"q":[3,-1,1],"yes":{"q":[34,-1,1],"yes":{"out":[561,4096]},"no":{"out":[49,1024]}},"no":{"q":[12,-1,1],"yes":{"out":[561,64]},"no":{"out":[561,8]}}},"no":{"q":[13,-1,1],"yes":{"q":[4,-1,1],"yes":{"out":[561,2]},"no":{"out":[561,128]}},"no":{"q":[15,-1,-1],"yes":{"out":[561,8]},"no":{"out":[49,1024]}}}}}}});

```

## Next

Reuse the best saved certificate; inspect the local states with the strongest exact cover obstruction. If budget three is still unresolved, stronger incompatible-pair/factor certificates or search order and expanded library are natural continuations. Control remains the R222 directory-absence observation; no owner or formal claim inferred. Activity association pending.
