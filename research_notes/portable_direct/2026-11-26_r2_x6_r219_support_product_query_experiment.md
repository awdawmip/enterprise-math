# X6 R219 — exact product-of-support query experiment

2026-11-26. AUTHOR COMPUTATION / NOT_REVIEWED. Independent informed static six-pair BRC continuation. Same Port 10, weights (17t,B,22t,D)>0, 1935 directions; exact legal optimizer term and full strict 3/2 near mask. Sources R217@c7d78ae72c2dcb4970f9b830397f6be65e359fb1, R176@c665f671a31d2bfeffb151e06bb308628110029e, R168@ee8eb26824479ec56924b81871b0cd7b38bee8ce, R216@0b5f89c35844559a07c3cd49c25f882ae1c7472f. P000 V5/ACTIVE/JOINT retained. Auxiliary parameter chart only.

## Finite model and proof

Use all 47 mandatory support forms from R176, plus the 197 R217 forms, to subdivide the positive projective parameter triangle. Every original label and every support-product predicate is constant on each relatively open face. Exact vertex/edge/cell representatives cover the positive domain by the R168 clipping argument. Group representatives by complete 47-component ternary sign vector; on each fiber a leaf may choose only the intersection of optimizer masks, with identical near mask. A conflict proves no tree using only these support signs (even arbitrary Boolean compositions) can distinguish that fiber; absence of conflicts proves the quotient is sufficient for the declared static output, not for other observers. Products are evaluated as strict sign of ± L_i L_j, including i=j for nonzero tests; linear forms ±L_i also allowed. Complementary binary partitions are interchangeable by child swapping, including zeros. The search uses forced singleton/near-group lower bounds and additional one-leaf requirement if an admissible mask misses all forced terms. This bound is valid since different near masks cannot share leaves and every forced singleton needs its own output. Search at depth >=3 keeps only the ten best-ranked split candidates, hence a failure is heuristic, not an exhaustive impossibility proof. A returned tree is independently replayed on every full arrangement representative, which proves a six-depth global upper bound within inherited bank coverage; R217 supplies lower bound six. No floating-point arithmetic used for scientific signs (ranking heuristic uses numbers).

## Actual output

```json
{
  "lines": 197,
  "cells": 7311,
  "points": 27611,
  "patterns": 1925,
  "conflicts": 0,
  "labels": 120,
  "queries": 2303,
  "states": 117,
  "attempts": 84,
  "cutoff": false,
  "tree": {
    "q": [
      1,
      29,
      1
    ],
    "yes": {
      "q": [
        0,
        26,
        -1
      ],
      "yes": {
        "q": [
          2,
          7,
          -1
        ],
        "yes": {
          "q": [
            16,
            27,
            -1
          ],
          "yes": {
            "q": [
              2,
              25,
              1
            ],
            "yes": {
              "q": [
                2,
                41,
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
                0,
                2,
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
                  16
                ]
              }
            }
          },
          "no": {
            "q": [
              0,
              16,
              1
            ],
            "yes": {
              "out": [
                132,
                16
              ]
            },
            "no": {
              "q": [
                0,
                11,
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
              2,
              8,
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
                2,
                10,
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
              0,
              7,
              1
            ],
            "yes": {
              "out": [
                132,
                4
              ]
            },
            "no": {
              "q": [
                0,
                1,
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
                  72,
                  1
                ]
              }
            }
          }
        }
      },
      "no": {
        "q": [
          0,
          24,
          -1
        ],
        "yes": {
          "q": [
            0,
            27,
            1
          ],
          "yes": {
            "q": [
              0,
              2,
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
                132,
                16
              ]
            }
          },
          "no": {
            "q": [
              19,
              27,
              1
            ],
            "yes": {
              "q": [
                0,
                23,
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
            0,
            -1,
            1
          ],
          "yes": {
            "q": [
              0,
              6,
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
              1,
              16,
              1
            ],
            "yes": {
              "q": [
                1,
                33,
                -1
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
            },
            "no": {
              "q": [
                0,
                45,
                -1
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
            }
          }
        }
      }
    },
    "no": {
      "q": [
        11,
        20,
        1
      ],
      "yes": {
        "q": [
          31,
          35,
          1
        ],
        "yes": {
          "q": [
            15,
            46,
            -1
          ],
          "yes": {
            "q": [
              17,
              22,
              -1
            ],
            "yes": {
              "q": [
                0,
                21,
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
                  569,
                  8
                ]
              }
            },
            "no": {
              "q": [
                0,
                14,
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
                  8192
                ]
              }
            }
          },
          "no": {
            "q": [
              31,
              37,
              -1
            ],
            "yes": {
              "q": [
                0,
                3,
                1
              ],
              "yes": {
                "out": [
                  121,
                  1024
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
                0,
                3,
                1
              ],
              "yes": {
                "out": [
                  49,
                  1024
                ]
              },
              "no": {
                "out": [
                  72,
                  256
                ]
              }
            }
          }
        },
        "no": {
          "q": [
            11,
            31,
            -1
          ],
          "yes": {
            "q": [
              40,
              46,
              1
            ],
            "yes": {
              "q": [
                1,
                40,
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
          },
          "no": {
            "q": [
              0,
              14,
              -1
            ],
            "yes": {
              "q": [
                0,
                32,
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
              "q": [
                0,
                21,
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
                  569,
                  8
                ]
              }
            }
          }
        }
      },
      "no": {
        "q": [
          5,
          16,
          1
        ],
        "yes": {
          "q": [
            18,
            42,
            1
          ],
          "yes": {
            "q": [
              0,
              12,
              1
            ],
            "yes": {
              "q": [
                0,
                44,
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
                8
              ]
            }
          },
          "no": {
            "q": [
              0,
              38,
              -1
            ],
            "yes": {
              "q": [
                0,
                39,
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
            },
            "no": {
              "q": [
                0,
                36,
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
            }
          }
        },
        "no": {
          "q": [
            3,
            34,
            1
          ],
          "yes": {
            "q": [
              4,
              30,
              1
            ],
            "yes": {
              "q": [
                0,
                13,
                1
              ],
              "yes": {
                "out": [
                  561,
                  128
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
                0,
                4,
                -1
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
                  2
                ]
              }
            }
          },
          "no": {
            "q": [
              12,
              15,
              1
            ],
            "yes": {
              "out": [
                561,
                8
              ]
            },
            "no": {
              "q": [
                0,
                3,
                1
              ],
              "yes": {
                "out": [
                  49,
                  1024
                ]
              },
              "no": {
                "out": [
                  561,
                  64
                ]
              }
            }
          }
        }
      }
    }
  },
  "checks": 27611,
  "depth": 6
}
```

## Exact standalone replay

```javascript
function experiment(){
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],M=[30,51,10,21,58,51,20,3,23,30],W=[0,3,5,6,7,9],MASK=[30,51,42,21,58,51,20,7,23,30],E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]].map(a=>a.map(BigInt));
const R="187,12,-1;204,11,-1;5,-2,0;9,-1,0;85,7,-2;51,2,-1;0,1,-1;34,1,-1;187,20,-9;68,1,-3;176,22,-9;22,0,-1;61,0,-1;74,0,-1;126,0,-1;4,-1,0;17,-1,0;156,-1,-1;69,0,-1;9,0,-1;235,0,-3;87,0,-1;104,-1,-1;38,0,-3;5,0,-2;39,-1,-1;40,0,-3;26,-1,-1;25,0,-3;83,0,-2;102,-7,-1;204,-11,1;395,0,-2;289,18,-1;66,2,-1;132,5,-1;44,1,-1;88,3,-1;88,7,-3;132,-7,-1;153,8,-1;153,5,-4;117,-2,-2;198,8,-1;198,5,-4;306,17,-1;234,-1,-1".split(";").map(s=>s.split(",").map(BigInt));
function gaps([x,y,z]){let h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z],g=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)g.push(Math.abs(h[i]-h[j]));return g}
const G=V.map(gaps),key=a=>a.join(),uniq=a=>[...new Map(a.map(x=>[key(x),x])).values()],gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a,norm=a=>{let g=a.reduce(gcd,0n);return g?a.map(x=>x/g):a},canon=a=>{a=norm(a);return a.find(x=>x)!==undefined&&a.find(x=>x)<0n?a.map(x=>-x):a},dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),add=(a,b)=>a.map((x,i)=>x+b[i]);
const bank=(inds,mask)=>uniq(inds.flatMap(i=>G[i].flatMap((g,j)=>g&&(mask[i]>>j&1)?[[j,g]]:[]))).sort((a,b)=>a[0]-b[0]||a[1]-b[1]);
const T=bank(W,MASK),H=bank(V.map((_,i)=>i),M);
function line([j,g],[h,f],k=1n,l=1n){return canon(E[h].map((x,i)=>k*BigInt(g)*x-l*BigInt(f)*E[j][i]))}
const L=uniq([...R,...T.flatMap((a,i)=>[...T.slice(i+1).map(b=>line(a,b)),...H.map(b=>line(a,b,3n,2n))])]).filter(a=>a.some(x=>x>0n)&&a.some(x=>x<0n));
let polys=[[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]]];
for(const l of L){let next=[];for(const p of polys){let s=p.map(x=>dot(l,x));if(!s.some(x=>x>0n)||!s.some(x=>x<0n)){next.push(p);continue}let pos=[],neg=[];for(let i=0;i<p.length;i++){let j=(i+1)%p.length,a=s[i],b=s[j];if(a>=0n)pos.push(p[i]);if(a<=0n)neg.push(p[i]);if(a*b<0n){let r=norm(p[i].map((x,k)=>(b<0n?-b:b)*x+(a<0n?-a:a)*p[j][k]));pos.push(r);neg.push(r)}}next.push(pos,neg)}polys=next}
let pts=new Map();function put(p){p=norm(p);if(p.every(x=>x>0n))pts.set(key(p),p)}
for(const p of polys){put(p.reduce(add,[0n,0n,0n]));for(let i=0;i<p.length;i++){put(p[i]);put(add(p[i],p[(i+1)%p.length]))}}
const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1],max=a=>a.reduce((x,y)=>cmp(x,y)>=0n?x:y),min=a=>a.reduce((x,y)=>cmp(x,y)<=0n?x:y);
let patterns=new Map(),records=[],conflicts=[];
for(const p of pts.values()){let s=E.map(e=>dot(e,p)),F=G.map(g=>max(g.map((v,j)=>[BigInt(v),s[j]]))),eta=min(W.map(i=>F[i]));let m=0,n=0;T.forEach(([j,g],i)=>{if(cmp([BigInt(g),s[j]],eta)===0n)m|=1<<i});F.forEach((f,i)=>{if(2n*f[0]*eta[1]<3n*eta[0]*f[1])n|=1<<i});let sign=R.map(r=>{let x=dot(r,p);return x>0n?1:x<0n?-1:0}),k=sign.join();let old=patterns.get(k);records.push({p,m,n,sign});if(old){old.m&=m;if(old.n!==n||!old.m)conflicts.push({first:old.p.map(String),second:p.map(String),n,oldn:old.n,m,oldm:old.m});}else patterns.set(k,{p,m,n,sign})}
let A=[...patterns.values()],N=A.length;
const base={lines:L.length,cells:polys.length,points:pts.size,patterns:N,conflicts:conflicts.length,example:conflicts[0]};
if(conflicts.length)return base;
let all=(1n<<BigInt(N))-1n,pos=R.map(()=>0n),neg=R.map(()=>0n),labels=new Map(),groups=new Map();
A.forEach((a,i)=>{let b=1n<<BigInt(i);a.sign.forEach((x,j)=>{if(x===1)pos[j]|=b;if(x===-1)neg[j]|=b});let k=a.n+","+a.m;if(!labels.has(k))labels.set(k,{n:a.n,m:a.m,b:0n});labels.get(k).b|=b;});
for(let l of labels.values()){if(!groups.has(l.n))groups.set(l.n,{b:0n,single:[],other:[]});let g=groups.get(l.n);g.b|=l.b;if((l.m&(l.m-1))===0)g.single.push(l);else g.other.push(l)}
let gs=[...groups.values()],ls=[...labels.values()],queries=[],seen=new Set();
function push(b,q){if(!b||b===all)return;let c=all^b,k=(b<c?b:c).toString(16);if(seen.has(k))return;seen.add(k);queries.push({b,q})}
for(let i=0;i<R.length;i++){push(pos[i],[i,-1,1]);push(neg[i],[i,-1,-1]);push(pos[i]|neg[i],[i,i,1]);for(let j=i+1;j<R.length;j++){push((pos[i]&pos[j])|(neg[i]&neg[j]),[i,j,1]);push((pos[i]&neg[j])|(neg[i]&pos[j]),[i,j,-1])}}
function lower(s){let n=0;for(let g of gs)if(g.b&s){let c=0,forced=0;for(let l of g.single)if(l.b&s){c++;forced|=l.m}if(!c)c=1;else if(g.other.some(l=>(l.b&s)&&!(l.m&forced)))c++;n+=c}return n}
function leaf(s){let n=-1,m=32767;for(let l of ls)if(l.b&s){if(n!==-1&&n!==l.n)return null;n=l.n;m&=l.m;if(!m)return null}return [n,m&-m]}
let states=0,attempts=0,cutoff=false,fail=new Set(),limit=3000;
function dfs(s,d){let z=leaf(s);if(z)return {out:z};if(d===0||lower(s)>2**d)return null;if(++states>limit){cutoff=true;return null}let k=d+":"+s.toString(16);if(fail.has(k))return null;
let candidates=[],local=new Set();for(let j=0;j<queries.length;j++){let a=queries[j].b&s,b=s^a;if(!a||!b)continue;let kk=(a<b?a:b).toString(16);if(local.has(kk))continue;local.add(kk);let x=lower(a),y=lower(b);if(Math.max(x,y)>2**(d-1))continue;if(d===1){let l=leaf(a),r=leaf(b);if(l&&r)return {q:queries[j].q,yes:{out:l},no:{out:r}};continue}
let la=0,lb=0;for(let l of ls){if(l.b&a)la++;if(l.b&b)lb++}candidates.push({j,a,b,x,y,score:Math.max(x,y)*4+x+y+(la+lb)*0.3+Math.max(la,lb)*0.2})}
candidates.sort((a,b)=>a.score-b.score||a.j-b.j);
for(let c of candidates.slice(0,d>=3?10:100000)){attempts++;let first=c.x>=c.y?c.a:c.b,second=first===c.a?c.b:c.a;let t=dfs(first,d-1);if(cutoff)return null;if(!t)continue;let u=dfs(second,d-1);if(cutoff)return null;if(u)return {q:queries[c.j].q,yes:first===c.a?t:u,no:first===c.a?u:t}}
fail.add(k);return null}
let tree=dfs(all,6);
let checks=0,depth=0;
if(tree)for(let a of records){let t=tree,d=0;while(t.q){let [i,j,sg]=t.q;let val=a.sign[i]*(j===-1?1:a.sign[j])*sg;t=val>0?t.yes:t.no;d++}if(t.out[0]!==a.n||!(t.out[1]&a.m))throw Error("bad tree");depth=Math.max(d,depth);checks++}
return {...base,labels:labels.size,queries:queries.length,states,attempts,cutoff,tree,checks,depth};
}
console.log(JSON.stringify(experiment(),null,2));
```

## Control and continuation

X6 read r2-20261126-1015-x6-read SUCCEEDED, NO_CANONICAL_PUBLICATION_DIRECTORY, Source 38ec2dc06dbbed82b730aa54c454886099506595, 2026-11-26T02:15:09.612658Z. Native owner view not evaluated. No CLAIM or shared state change. Current lane identity/Activity not established. Next: independent mathematical audit of the six-query tree and inherited bank coverage.
