# X6 R225 — budget-two focused resynthesis

2026-11-26; AUTHOR COMPUTATION / NOT_REVIEWED. Informed static X6 six-pair BRC, Port 10, 1935 directions, positive (17t,B,22t,D), same frozen candidate-bank assumptions and 35-label alphabet as R223 and R224. No new native spatial transfer. R223 pinned 91e99a63adfe2021ec59c8ee0e8553f40975be68:research_notes/portable_direct/2026-11-26_r2_x6_r223_exact_local_output_cover.md; R224 pinned 68345b0d06d09eb777e1345811856bb0015c7d28. Reuses exact raw-arrangement construction, all zero-sign fibers, R223 exact local output cover and mixed-budget recursion. No full raw-direction rerun; inherited R220/R221 evidence. The root experiment is bounded, and BUDGET is UNKNOWN, not infeasible. EXHAUSTED applies only to the fixed state, alphabet and support-product library. Successful replacement trees are checked over all fibers; the existing full-domain arrangement and bank proof are inherited. No formal Task or owner authority: control request r2-20261126-1306-x6-read, source ec9b04591b12b7a40eddf01c316a99a713f68931, NO_CANONICAL_PUBLICATION_DIRECTORY at 2026-11-26T05:06:30.773414Z. Activity association pending; no identity invented.

## Actual exact experiment

The local necessary leaf-cover budget is evaluated on each child; unordered identical partitions retain the least-cost query because linear queries are visited first. A failed child is sufficient to discard a candidate. State keys are (fiber mask, depth, remaining joint budget); a cut is not cached as failure. Every successful tree is validated using direct ternary factor arithmetic including zeros. The output includes unchanged baseline and actual replacement. 

```json
{
  "rawLines": 256,
  "cells": 11487,
  "positiveRepresentatives": 43685,
  "fibers": 1925,
  "labels": 35,
  "queries": 2303,
  "old": {
    "d": 6,
    "k": 3,
    "nodes": 59,
    "quadratic": 14,
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
    "maxFactors": 8,
    "outputs": 35
  },
  "new": {
    "d": 6,
    "k": 2,
    "nodes": 60,
    "quadratic": 8,
    "hist": {
      "0": 500,
      "1": 617,
      "2": 808
    },
    "depth": {
      "5": 113,
      "6": 1812
    },
    "maxFactors": 8,
    "outputs": 35
  },
  "logs": [
    {
      "path": "R223-yes",
      "d": 5,
      "k": 2,
      "status": "FOUND",
      "states": 3170,
      "scans": 426526,
      "boundCalls": 563032
    },
    {
      "path": "R223-no",
      "d": 5,
      "k": 2,
      "status": "FOUND",
      "states": 69,
      "scans": 17731,
      "boundCalls": 24641
    }
  ],
  "visited": 3239,
  "scans": 444257,
  "boundCalls": 587673,
  "tree": {
    "q": [
      12,
      -1,
      1
    ],
    "yes": {
      "q": [
        2,
        29,
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
            8,
            -1,
            -1
          ],
          "yes": {
            "q": [
              7,
              -1,
              1
            ],
            "yes": {
              "q": [
                9,
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
                "out": [
                  132,
                  4
                ]
              }
            },
            "no": {
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
            }
          },
          "no": {
            "q": [
              9,
              -1,
              -1
            ],
            "yes": {
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
            },
            "no": {
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
              16,
              -1,
              1
            ],
            "yes": {
              "q": [
                44,
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
                  689,
                  4096
                ]
              }
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
      },
      "no": {
        "q": [
          26,
          -1,
          -1
        ],
        "yes": {
          "q": [
            5,
            16,
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
                27,
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
                  132,
                  16
                ]
              }
            },
            "no": {
              "q": [
                44,
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
                  689,
                  4096
                ]
              }
            }
          },
          "no": {
            "q": [
              29,
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
                  693,
                  16
                ]
              },
              "no": {
                "out": [
                  693,
                  64
                ]
              }
            },
            "no": {
              "q": [
                2,
                -1,
                -1
              ],
              "yes": {
                "out": [
                  561,
                  64
                ]
              },
              "no": {
                "out": [
                  561,
                  4096
                ]
              }
            }
          }
        },
        "no": {
          "q": [
            19,
            -1,
            -1
          ],
          "yes": {
            "q": [
              27,
              -1,
              -1
            ],
            "yes": {
              "q": [
                23,
                -1,
                -1
              ],
              "yes": {
                "out": [
                  692,
                  16
                ]
              },
              "no": {
                "out": [
                  676,
                  16
                ]
              }
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
          46,
          -1,
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
                31,
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
                  633,
                  256
                ]
              }
            }
          },
          "no": {
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
              "q": [
                43,
                -1,
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
              31,
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
                "out": [
                  72,
                  8192
                ]
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

## Reproduction

Use the following function on the JSON tree in pinned R223's first JSON block; the support forms and candidate bank are explicit. 

```javascript
function experiment(old){
const R="187,12,-1;204,11,-1;5,-2,0;9,-1,0;85,7,-2;51,2,-1;0,1,-1;34,1,-1;187,20,-9;68,1,-3;176,22,-9;22,0,-1;61,0,-1;74,0,-1;126,0,-1;4,-1,0;17,-1,0;156,-1,-1;69,0,-1;9,0,-1;235,0,-3;87,0,-1;104,-1,-1;38,0,-3;5,0,-2;39,-1,-1;40,0,-3;26,-1,-1;25,0,-3;83,0,-2;102,-7,-1;204,-11,1;395,0,-2;289,18,-1;66,2,-1;132,5,-1;44,1,-1;88,3,-1;88,7,-3;132,-7,-1;153,8,-1;153,5,-4;117,-2,-2;198,8,-1;198,5,-4;306,17,-1;234,-1,-1".split(";").map(s=>s.split(",").map(BigInt));
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],T=[[0,1],[0,2],[0,3],[1,3],[1,6],[2,3],[2,6],[2,7],[2,11],[2,12],[3,2],[3,3],[4,6],[4,12],[5,7]],E=[[17n,1n,0n],[39n,0n,0n],[17n,0n,1n],[22n,1n,0n],[0n,1n,1n],[22n,0n,1n]],W=[0,3,5,6,7,9];
function gaps(v){let [x,y,z]=v,h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]].map(([i,j])=>BigInt(Math.abs(h[i]-h[j])))}
const G=V.map(gaps),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){let t=a%b;a=b;b=t}return a}
function norm(a,u=false){let d=gcd(gcd(a[0],a[1]),a[2]);if(!d)return a;a=a.map(x=>x/d);if(u&&a.find(x=>x!==0n)<0n)a=a.map(x=>-x);return a}
let raw=new Map();function add(a){a=norm(a,true);if(a.some(x=>x>0n)&&a.some(x=>x<0n))raw.set(a.join(),a)}
for(let i=0;i<T.length;i++){let [j,g]=T[i];for(let k=i+1;k<T.length;k++){let [h,f]=T[k];add(E[h].map((x,s)=>BigInt(g)*x-BigInt(f)*E[j][s]))}for(let gg of G)for(let h=0;h<6;h++)if(gg[h])add(E[h].map((x,s)=>3n*BigInt(g)*x-2n*gg[h]*E[j][s]))}
const L=[...raw.values()];for(let r of R)if(!raw.has(norm(r,true).join()))throw Error("support absent");
let cells=[[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]]];
for(let l of L){let next=[];for(let c of cells){let sig=c.map(x=>dot(l,x));if(!sig.some(x=>x>0n)||!sig.some(x=>x<0n)){next.push(c);continue}for(let side of [1n,-1n]){let out=[];for(let i=0;i<c.length;i++){let j=(i+1)%c.length,a=sig[i],b=sig[j];if(a*side>=0n)out.push(c[i]);if(a*b<0n){let r=cross(cross(c[i],c[j]),l);if(r.some(x=>x<0n))r=r.map(x=>-x);if(r.some(x=>x<0n)||!r.some(x=>x>0n)||dot(r,l)!==0n)throw Error("bad intersection");out.push(norm(r))}}next.push(out)}}cells=next}
const pts=new Map(),sum=a=>[0,1,2].map(i=>a.reduce((s,x)=>s+x[i],0n));function put(a){if(a.every(x=>x>0n)){a=norm(a);pts.set(a.join(),a)}}
for(let c of cells){put(sum(c));for(let i=0;i<c.length;i++){put(c[i]);put(sum([c[i],c[(i+1)%c.length]]))}}
const sign=p=>R.map(r=>{let x=dot(r,p);return x>0n?1:x<0n?-1:0}),F=new Map(),max=a=>a.reduce((x,y)=>x>y?x:y),min=a=>a.reduce((x,y)=>x<y?x:y);
for(let p of pts.values()){let s=sign(p),key=s.join(),c=E.map(e=>dot(e,p)),pr=c.reduce((a,b)=>a*b,1n),scale=c.map(x=>pr/x),scores=G.map(g=>max(g.map((a,i)=>a*scale[i]))),eta=min(W.map(i=>scores[i])),n=0,m=0;for(let i=0;i<scores.length;i++)if(2n*scores[i]<3n*eta)n|=1<<i;for(let i=0;i<T.length;i++){let [j,g]=T[i];if(BigInt(g)*scale[j]===eta)m|=1<<i}let f=F.get(key);if(f){if(f.n!==n)throw Error("near mismatch");f.m&=m;if(!f.m)throw Error("empty intersection")}else F.set(key,{s,n,m})}
const A=[...F.values()],N=A.length,all=(1n<<BigInt(N))-1n;
if(L.length!==256||cells.length!==11487||pts.size!==43685||N!==1925)throw Error("coverage mismatch");
let labelMap=new Map();function gather(t){if(t.out){labelMap.set(t.out.join(),t.out);return}gather(t.yes);gather(t.no)}gather(old);const lab=[...labelMap.values()],covers=lab.map(()=>0n),groups=new Map(),pos=R.map(()=>0n),neg=R.map(()=>0n);
A.forEach((f,i)=>{let bit=1n<<BigInt(i),hits=0;f.s.forEach((v,j)=>{if(v>0)pos[j]|=bit;if(v<0)neg[j]|=bit});lab.forEach(([n,m],j)=>{if(n===f.n&&(m&f.m)){covers[j]|=bit;hits++}});if(!hits)throw Error("uncovered");groups.set(f.n,(groups.get(f.n)||0n)|bit)});
const mask=([i,j,s])=>j<0?(s>0?pos[i]:neg[i]):s>0?(pos[i]&pos[j])|(neg[i]&neg[j]):(pos[i]&neg[j])|(neg[i]&pos[j]);
const Q=[];for(let i=0;i<R.length;i++)for(let s of [1,-1])Q.push({q:[i,-1,s],b:mask([i,-1,s]),cost:0});for(let i=0;i<R.length;i++)for(let j=i;j<R.length;j++)for(let s of [1,-1])if(i!==j||s===1)Q.push({q:[i,j,s],b:mask([i,j,s]),cost:1});
const gs=[...groups].map(([n,b])=>{let cs=lab.map((l,i)=>l[0]===n?covers[i]:0n).filter(Boolean),opts=[];for(let m=1;m<(1<<cs.length);m++){let v=0n,k=0;for(let j=0;j<cs.length;j++)if(m&(1<<j)){v|=cs[j];k++}opts.push({v,k})}opts.sort((a,b)=>a.k-b.k);return {b,opts}});
let boundCalls=0;function bound(S,lim){boundCalls++;let n=0;for(let g of gs){let x=S&g.b;if(!x)continue;n+=g.opts.find(o=>(x&o.v)===x).k;if(n>lim)return n}return n}
function leaf(S){for(let i=0;i<covers.length;i++)if((S&covers[i])===S)return {out:lab[i]};return null}
let visited=0,scans=0,cap=0,memo=new Map(),logs=[],stopped={};
function solve(S,d,k){let l=leaf(S);if(l)return l;if(!d||bound(S,1<<d)>1<<d)return null;k=Math.min(d,k);let key=S.toString(36)+"/"+d+"/"+k;if(memo.has(key))return memo.get(key);if(++visited>cap)throw stopped;let seen=new Set(),cand=[],lim=1<<(d-1);
for(let c of Q){if(c.cost>k)break;let y=S&c.b,z=S^y;if(!y||!z)continue;let key=y<z?y:z;if(seen.has(key))continue;seen.add(key);scans++;let a=bound(y,lim);if(a>lim)continue;let b=bound(z,lim);if(b>lim)continue;if(d===1){let yy=leaf(y),zz=leaf(z);if(yy&&zz){let t={q:c.q,yes:yy,no:zz};memo.set(key,t);return t}continue}cand.push({c,y,z,a,b,score:Math.max(a,b)*100+(a+b)*3+c.cost*4});}
cand.sort((a,b)=>a.score-b.score);
for(let {c,y,z,a,b} of cand){let yy,zz,k1=k-c.cost;if(a>=b){yy=solve(y,d-1,k1);if(!yy)continue;zz=solve(z,d-1,k1)}else{zz=solve(z,d-1,k1);if(!zz)continue;yy=solve(y,d-1,k1)}if(yy&&zz){let t={q:c.q,yes:yy,no:zz};memo.set(key,t);return t}}memo.set(key,null);return null}
function trial(S,d,k,path,budget){let v=visited,s=scans,b=boundCalls,t=null,status;cap=visited+budget;try{t=solve(S,d,k);status=t?"FOUND":"EXHAUSTED"}catch(e){if(e!==stopped)throw e;status="BUDGET"}logs.push({path,d,k,status,states:visited-v,scans:scans-s,boundCalls:boundCalls-b});return t}
function stats(t){if(t.out)return {d:0,k:0,nodes:0,quadratic:0};let a=stats(t.yes),b=stats(t.no),k=Number(t.q[1]>=0);return {d:1+Math.max(a.d,b.d),k:k+Math.max(a.k,b.k),nodes:1+a.nodes+b.nodes,quadratic:k+a.quadratic+b.quadratic}}
function verify(t){let hist={},depth={},distinct=new Set(),maxFactors=0;for(let f of A){let x=t,d=0,k=0,fs=new Set();while(x.q){let [i,j,s]=x.q;fs.add(i);if(j>=0){fs.add(j);k++}d++;x=s*f.s[i]*(j<0?1:f.s[j])>0?x.yes:x.no}if(x.out[0]!==f.n||!(x.out[1]&f.m)||d>6)throw Error("bad tree");hist[k]=(hist[k]||0)+1;depth[d]=(depth[d]||0)+1;maxFactors=Math.max(maxFactors,fs.size);distinct.add(x.out.join())}return {...stats(t),hist,depth,maxFactors,outputs:distinct.size}}
let t=old;let y=mask(t.q)&all,z=all^y;let k=2-Number(t.q[1]>=0);for(let [name,S] of [["yes",y],["no",z]])if(stats(t[name]).k>k){let u=trial(S,5,k,"R223-"+name,12000);if(u)t={...t,[name]:u}}
if(stats(t).k>2){let u=trial(all,6,2,"ROOT",12000);if(u)t=u}
return {rawLines:L.length,cells:cells.length,positiveRepresentatives:pts.size,fibers:N,labels:lab.length,queries:Q.length,old:verify(old),new:verify(t),logs,visited,scans,boundCalls,tree:t};
}
```

## Next

Try budget one, and compare global minimum under support-product vs unrestricted quadratic libraries.
