# X6 R166 — Sharp adaptive threshold decision tree at the original ratio

2026-11-24. AUTHOR ANALYTIC REDUCTION / EXACT FINITE CERTIFICATE / NOT_REVIEWED. Informed independent static observer, Port 10, C/A=22/17. Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd, R122@1e4ab68c4f9c91bc60c07017acc57be20829832f; R162@3682ce83f1a1638e29f600769ffa6cd6207b4841, R163@c8a9d155c12ba72410a3f9f3b2a793e1e4657adb, R164@8c94c3e4d6e7a751441b11f2042638515c22ff15, R165@6713e10fe0ddbb5f7602409ba59b0f71981de515. P000 V5, Heartbeat World, raw joint relations and provenance preserved. No native dynamic transfer.

## Question and sharp result

Using the unchanged q, h, six labeled gaps, capacities and F from R165, suppose the exact optimum eta is already known. The allowed runtime tests are original single-channel strict threshold predicates 2g_j(v)<3eta*s_j. We count binary adaptive tests; outputs are the complete strict-near direction set. Precomputed fixed lookup and tree traversal are permitted; no other arithmetic comparisons, optimizer intermediate observations or arbitrary thresholds are supplied in this decision model. Zero gaps always pass. At the original ratio the near bank has ten rows. R165 has 20 distinct retained predicates and proves an upper bound 14 for separate rank searches.

The actual feasible rank-vector universe for the 20 predicates has 83 states and exactly 16 distinct near sets. The exact worst depth of that particular separate binary search algorithm is 13, sharpened from the 14 upper bound. A joint adaptive decision tree computes the complete near set in at most 6 tests; 6 is necessary in this predicate model.

Enlarging the allowed tests to ALL 30 distinct nonzero-gap predicates of the ten original rows (including channels R165 did not need) gives 113 feasible rank states and 16 outputs; its optimal worst depth is 6. Therefore the smaller-bank tree attains the optimum in the enlarged model if these depths agree. This is a sharp comparison complexity statement for the declared threshold-only model, not a claim about arbitrary arithmetic programs or the full joint optimization cost.

Runtime tree uses test index q into the listed table: evaluate 2*d*g<3*n*s_j for rational eta=n/d; take yes on strict success and no on equality or failure. A leaf out is a bitset of the ten directions in the order V in the code. The reduced tree begins with channel AB, gap 3. It avoids computing the complete scores and even the complete rank vector. No raw data are deleted.

## Proof of exact states

As R165 proved, normalize u=3eta*w=(17t,b,22t,d), t,b,d>0, and require min_W F(u)=1/3. That is a union over six possible optimizer lower vectors s_j>=3g_j(a) and maximal upper boxes (each optimizer candidate has at least one s_j<=3g_j). The 29 maximal boxes are exact by coordinatewise containment and componentwise minimum induction. The 50 nonempty optimizer/box conjunctions cover all normalized weights. For ordered positive gap list L_j, a rank k means s_j>2L_j[k-1] if k>0 and s_j<=2L_j[k] if k<length, with endpoints exactly as specified. Enumerate the six ranks recursively and prune only infeasible systems via strict Fourier–Motzkin elimination of three variables, as in R165. At each branch exact feasibility is necessary and sufficient; a finite side may be unbounded, strictness is propagated by logical OR, and zero rows reject only false constants. Thus every retained rank state is genuinely attainable, and every positive weight is represented. Weak upper bounds include all equality cases. The enlarged model cross-checks that all six original tests and the R165 mask give identical output for every rank state.

## Proof of sharp adaptive depth

For a nonempty set S of feasible states still compatible with previous predicate outcomes, let D(S)=0 when all have the same output. Otherwise let S_yes(q), S_no(q) be the two parts given by allowed predicate q; skip a constant split, which cannot help. Then
D(S)=1+min_q max(D(S_yes(q)),D(S_no(q))).
Every tree has some root q, so induction on |S| proves this recurrence is a lower bound for all deterministic adaptive trees, and choosing a minimizing q gives an actual tree attaining it. All proper splits strictly reduce |S|. Memoization by exact BigInt subset bitset changes no result. Pruning a candidate when one child alone cannot beat the incumbent depth preserves the minimum. The computation enumerates the exact reachable state subsets, not sampled weights; all constructed leaves are independently replayed on every feasible rank vector. The full raw model yields the sharper lower bound among all raw candidate predicates, while the reduced model gives a simpler tree. Neither model counts obtaining eta, forming capacities, multiplication bit costs, preprocessing or output retrieval.

## Actual results

14130 exact affine feasibility calls, 3736 reduced and 7490 raw memoized decision states. 924 additional exact weight replays over the full 1935-direction population (1787940 direction/weight cases, 126 equality cases); both trees match all full-domain near sets and the optimizer agrees. Observed worst depths 6 and 6; full state certificate, not these samples, proves the sharp values. PASS.

```json
{
  "boxes": 29,
  "nonemptyBases": 50,
  "queries": 14130,
  "maxProduct": 3790072,
  "reduced": {
    "queries": 4825,
    "rankVectors": 83,
    "outputCount": 16,
    "outputMasks": [
      49,
      64,
      72,
      89,
      121,
      132,
      164,
      561,
      569,
      633,
      676,
      689,
      692,
      693,
      695,
      951
    ],
    "maxRank": 13,
    "optimalWorst": 6,
    "worst": 6,
    "meanDepth": 5.385542168674699,
    "states": 3736,
    "first": {
      "j": 0,
      "i": 2,
      "g": 3
    },
    "tests": [
      {
        "j": 0,
        "i": 0,
        "g": 1
      },
      {
        "j": 0,
        "i": 1,
        "g": 2
      },
      {
        "j": 0,
        "i": 2,
        "g": 3
      },
      {
        "j": 0,
        "i": 3,
        "g": 4
      },
      {
        "j": 1,
        "i": 0,
        "g": 3
      },
      {
        "j": 1,
        "i": 1,
        "g": 6
      },
      {
        "j": 1,
        "i": 2,
        "g": 9
      },
      {
        "j": 2,
        "i": 0,
        "g": 6
      },
      {
        "j": 2,
        "i": 1,
        "g": 7
      },
      {
        "j": 2,
        "i": 2,
        "g": 10
      },
      {
        "j": 2,
        "i": 3,
        "g": 11
      },
      {
        "j": 2,
        "i": 4,
        "g": 12
      },
      {
        "j": 3,
        "i": 0,
        "g": 2
      },
      {
        "j": 3,
        "i": 1,
        "g": 3
      },
      {
        "j": 3,
        "i": 2,
        "g": 4
      },
      {
        "j": 4,
        "i": 0,
        "g": 6
      },
      {
        "j": 4,
        "i": 1,
        "g": 12
      },
      {
        "j": 5,
        "i": 0,
        "g": 7
      },
      {
        "j": 5,
        "i": 1,
        "g": 8
      },
      {
        "j": 5,
        "i": 2,
        "g": 11
      }
    ],
    "L": [
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
    "tree": {
      "q": 2,
      "yes": {
        "q": 9,
        "yes": {
          "q": 3,
          "yes": {
            "q": 16,
            "yes": {
              "q": 11,
              "yes": {
                "q": 4,
                "yes": {
                  "out": 633
                },
                "no": {
                  "out": 72
                }
              },
              "no": {
                "q": 10,
                "yes": {
                  "out": 569
                },
                "no": {
                  "out": 561
                }
              }
            },
            "no": {
              "q": 6,
              "yes": {
                "q": 15,
                "yes": {
                  "out": 951
                },
                "no": {
                  "out": 132
                }
              },
              "no": {
                "q": 5,
                "yes": {
                  "out": 693
                },
                "no": {
                  "out": 561
                }
              }
            }
          },
          "no": {
            "q": 16,
            "yes": {
              "q": 4,
              "yes": {
                "q": 11,
                "yes": {
                  "out": 633
                },
                "no": {
                  "out": 569
                }
              },
              "no": {
                "out": 72
              }
            },
            "no": {
              "q": 5,
              "yes": {
                "q": 14,
                "yes": {
                  "out": 693
                },
                "no": {
                  "out": 689
                }
              },
              "no": {
                "out": 561
              }
            }
          }
        },
        "no": {
          "q": 8,
          "yes": {
            "q": 6,
            "yes": {
              "q": 15,
              "yes": {
                "q": 19,
                "yes": {
                  "out": 695
                },
                "no": {
                  "out": 693
                }
              },
              "no": {
                "out": 132
              }
            },
            "no": {
              "q": 5,
              "yes": {
                "q": 15,
                "yes": {
                  "out": 693
                },
                "no": {
                  "out": 132
                }
              },
              "no": {
                "out": 561
              }
            }
          },
          "no": {
            "q": 7,
            "yes": {
              "q": 15,
              "yes": {
                "q": 18,
                "yes": {
                  "out": 692
                },
                "no": {
                  "out": 676
                }
              },
              "no": {
                "out": 132
              }
            },
            "no": {
              "q": 15,
              "yes": {
                "q": 17,
                "yes": {
                  "out": 164
                },
                "no": {
                  "out": 132
                }
              },
              "no": {
                "out": 132
              }
            }
          }
        }
      },
      "no": {
        "q": 1,
        "yes": {
          "q": 4,
          "yes": {
            "q": 13,
            "yes": {
              "q": 16,
              "yes": {
                "out": 633
              },
              "no": {
                "out": 561
              }
            },
            "no": {
              "q": 16,
              "yes": {
                "out": 121
              },
              "no": {
                "out": 49
              }
            }
          },
          "no": {
            "out": 72
          }
        },
        "no": {
          "q": 4,
          "yes": {
            "q": 12,
            "yes": {
              "out": 89
            },
            "no": {
              "out": 72
            }
          },
          "no": {
            "q": 0,
            "yes": {
              "out": 72
            },
            "no": {
              "out": 64
            }
          }
        }
      }
    }
  },
  "raw": {
    "queries": 9131,
    "rankVectors": 113,
    "outputCount": 16,
    "outputMasks": [
      49,
      64,
      72,
      89,
      121,
      132,
      164,
      561,
      569,
      633,
      676,
      689,
      692,
      693,
      695,
      951
    ],
    "maxRank": 16,
    "optimalWorst": 6,
    "worst": 6,
    "meanDepth": 5.469026548672566,
    "states": 7490,
    "first": {
      "j": 0,
      "i": 2,
      "g": 3
    },
    "tests": [
      {
        "j": 0,
        "i": 0,
        "g": 1
      },
      {
        "j": 0,
        "i": 1,
        "g": 2
      },
      {
        "j": 0,
        "i": 2,
        "g": 3
      },
      {
        "j": 0,
        "i": 3,
        "g": 4
      },
      {
        "j": 1,
        "i": 0,
        "g": 3
      },
      {
        "j": 1,
        "i": 1,
        "g": 6
      },
      {
        "j": 1,
        "i": 2,
        "g": 9
      },
      {
        "j": 2,
        "i": 0,
        "g": 2
      },
      {
        "j": 2,
        "i": 1,
        "g": 3
      },
      {
        "j": 2,
        "i": 2,
        "g": 4
      },
      {
        "j": 2,
        "i": 3,
        "g": 5
      },
      {
        "j": 2,
        "i": 4,
        "g": 6
      },
      {
        "j": 2,
        "i": 5,
        "g": 7
      },
      {
        "j": 2,
        "i": 6,
        "g": 10
      },
      {
        "j": 2,
        "i": 7,
        "g": 11
      },
      {
        "j": 2,
        "i": 8,
        "g": 12
      },
      {
        "j": 3,
        "i": 0,
        "g": 1
      },
      {
        "j": 3,
        "i": 1,
        "g": 2
      },
      {
        "j": 3,
        "i": 2,
        "g": 3
      },
      {
        "j": 3,
        "i": 3,
        "g": 4
      },
      {
        "j": 3,
        "i": 4,
        "g": 5
      },
      {
        "j": 4,
        "i": 0,
        "g": 6
      },
      {
        "j": 4,
        "i": 1,
        "g": 12
      },
      {
        "j": 5,
        "i": 0,
        "g": 1
      },
      {
        "j": 5,
        "i": 1,
        "g": 3
      },
      {
        "j": 5,
        "i": 2,
        "g": 4
      },
      {
        "j": 5,
        "i": 3,
        "g": 7
      },
      {
        "j": 5,
        "i": 4,
        "g": 8
      },
      {
        "j": 5,
        "i": 5,
        "g": 11
      },
      {
        "j": 5,
        "i": 6,
        "g": 12
      }
    ],
    "L": [
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
        2,
        3,
        4,
        5,
        6,
        7,
        10,
        11,
        12
      ],
      [
        1,
        2,
        3,
        4,
        5
      ],
      [
        6,
        12
      ],
      [
        1,
        3,
        4,
        7,
        8,
        11,
        12
      ]
    ],
    "tree": {
      "q": 2,
      "yes": {
        "q": 13,
        "yes": {
          "q": 3,
          "yes": {
            "q": 22,
            "yes": {
              "q": 15,
              "yes": {
                "q": 4,
                "yes": {
                  "out": 633
                },
                "no": {
                  "out": 72
                }
              },
              "no": {
                "q": 14,
                "yes": {
                  "out": 569
                },
                "no": {
                  "out": 561
                }
              }
            },
            "no": {
              "q": 6,
              "yes": {
                "q": 21,
                "yes": {
                  "out": 951
                },
                "no": {
                  "out": 132
                }
              },
              "no": {
                "q": 5,
                "yes": {
                  "out": 693
                },
                "no": {
                  "out": 561
                }
              }
            }
          },
          "no": {
            "q": 22,
            "yes": {
              "q": 4,
              "yes": {
                "q": 15,
                "yes": {
                  "out": 633
                },
                "no": {
                  "out": 569
                }
              },
              "no": {
                "out": 72
              }
            },
            "no": {
              "q": 5,
              "yes": {
                "q": 19,
                "yes": {
                  "out": 693
                },
                "no": {
                  "out": 689
                }
              },
              "no": {
                "out": 561
              }
            }
          }
        },
        "no": {
          "q": 12,
          "yes": {
            "q": 6,
            "yes": {
              "q": 21,
              "yes": {
                "q": 28,
                "yes": {
                  "out": 695
                },
                "no": {
                  "out": 693
                }
              },
              "no": {
                "out": 132
              }
            },
            "no": {
              "q": 5,
              "yes": {
                "q": 21,
                "yes": {
                  "out": 693
                },
                "no": {
                  "out": 132
                }
              },
              "no": {
                "out": 561
              }
            }
          },
          "no": {
            "q": 11,
            "yes": {
              "q": 21,
              "yes": {
                "q": 27,
                "yes": {
                  "out": 692
                },
                "no": {
                  "out": 676
                }
              },
              "no": {
                "out": 132
              }
            },
            "no": {
              "q": 21,
              "yes": {
                "q": 26,
                "yes": {
                  "out": 164
                },
                "no": {
                  "out": 132
                }
              },
              "no": {
                "out": 132
              }
            }
          }
        }
      },
      "no": {
        "q": 1,
        "yes": {
          "q": 4,
          "yes": {
            "q": 18,
            "yes": {
              "q": 22,
              "yes": {
                "out": 633
              },
              "no": {
                "out": 561
              }
            },
            "no": {
              "q": 22,
              "yes": {
                "out": 121
              },
              "no": {
                "out": 49
              }
            }
          },
          "no": {
            "out": 72
          }
        },
        "no": {
          "q": 4,
          "yes": {
            "q": 17,
            "yes": {
              "out": 89
            },
            "no": {
              "out": 72
            }
          },
          "no": {
            "q": 0,
            "yes": {
              "out": 72
            },
            "no": {
              "out": 64
            }
          }
        }
      }
    }
  },
  "weights": 924,
  "fullRowChecks": 1787940,
  "equalities": 126,
  "observedWorstReduced": 6,
  "observedWorstRaw": 6
}
```

## Reproduction

```javascript
function exactTree(){
 const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]];
 const M=[30,51,10,21,58,51,20,3,23,30],W=[V[0],V[3],V[5],V[6],V[7],V[9]];
 const E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]],J=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
 const gap=([x,y,z])=>{const h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return J.map(([i,j])=>Math.abs(h[i]-h[j]))};
 const G=W.map(gap),R=V.map(gap),INF=1000000;
 const weakUpper=(j,n)=>[...E[j],n,0],lower=(j,n,strict=0)=>[...E[j].map(x=>-x),-n,strict],positive=[[-1,0,0,0,1],[0,-1,0,0,1],[0,0,-1,0,1]];
 const dominated=(a,b)=>a.every((x,j)=>x<=b[j]);
 let boxes=[Array(6).fill(INF)];
 for(const a of G){const next=[];for(const b of boxes)for(let j=0;j<6;j++)if(a[j]>0){const x=b.slice();x[j]=Math.min(x[j],3*a[j]);next.push(x)}
 const S=[...new Map(next.map(b=>[String(b),b])).values()].sort((a,b)=>b.reduce((s,x)=>s+x,0)-a.reduce((s,x)=>s+x,0)),out=[];for(const x of S)if(!out.some(y=>dominated(x,y)))out.push(x);boxes=out}
 function gcd(a,b){a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b]}return a}
 let checks=0,maxProduct=0;
 function clean(rows){const m=new Map;for(const a of rows){if(!a.slice(0,-2).some(Boolean)){if(a.at(-2)<0||(a.at(-2)===0&&a.at(-1)))return null;continue}const d=a.slice(0,-1).reduce(gcd,0)||1,z=a.slice(0,-1).map(x=>x/d),k=String(z);if(!z.every(Number.isSafeInteger))throw Error("integer");m.set(k,[...z,Math.max(a.at(-1),m.get(k)?.at(-1)||0)])}return [...m.values()]}
 function feasible(rows){checks++;rows=clean(rows);for(let k=0;k<3;k++){if(rows===null)return false;const p=rows.filter(a=>a[0]>0),n=rows.filter(a=>a[0]<0),out=rows.filter(a=>a[0]===0).map(a=>a.slice(1));for(const a of p)for(const b of n){const z=a.slice(1,-1).map((x,i)=>{const p=a[0]*b[i+1],q=b[0]*x;maxProduct=Math.max(maxProduct,Math.abs(p),Math.abs(q));if(!Number.isSafeInteger(p)||!Number.isSafeInteger(q)||!Number.isSafeInteger(p-q))throw Error("overflow");return p-q});out.push([...z,Math.max(a.at(-1),b.at(-1))])}rows=clean(out)}return rows!==null}
 const bases=[];for(const u of G)for(const b of boxes){const base=positive.concat(u.map((g,j)=>lower(j,3*g)),b.flatMap((g,j)=>g===INF?[]:[weakUpper(j,g)]));if(feasible(base))bases.push(base)}
 function solveModel(raw){
 const before=checks,L=J.map((_,j)=>[...new Set(R.filter((a,i)=>a[j]>0&&(raw||M[i]&(1<<j))).map(a=>a[j]))].sort((a,b)=>a-b)),tests=L.flatMap((a,j)=>a.map((g,i)=>({j,i,g})));
 const cells=new Map,order=[1,4,0,3,2,5];
 function recurse(base,r,k){if(k===6){cells.set(String(r),r.slice());return}
 const j=order[k],a=L[j];for(let n=0;n<=a.length;n++){const b=base.concat(n>0?[lower(j,2*a[n-1],1)]:[],n<a.length?[weakUpper(j,2*a[n])]:[]);if(feasible(b)){r[j]=n;recurse(b,r,k+1)}}}
 for(const base of bases)recurse(base,Array(6).fill(0),0);
 const ranks=[...cells.values()].sort((a,b)=>String(a).localeCompare(String(b)));
 const out=ranks.map(r=>R.reduce((s,a,i)=>s|(J.every((_,j)=>!(M[i]&(1<<j))||r[j]>L[j].indexOf(a[j]))?1<<i:0),0));
 if(raw)for(let i=0;i<ranks.length;i++){const r=ranks[i],full=R.reduce((s,a,k)=>s|(J.every((_,j)=>a[j]===0||r[j]>L[j].indexOf(a[j]))?1<<k:0),0);if(full!==out[i])throw Error("mask scope")}
 const N=ranks.length,all=(1n<<BigInt(N))-1n,tmask=tests.map(t=>ranks.reduce((s,r,i)=>r[t.j]>t.i?s|(1n<<BigInt(i)):s,0n)),outputs=[...new Set(out)],omask=outputs.map(o=>out.reduce((s,x,i)=>x===o?s|(1n<<BigInt(i)):s,0n));
 function rankCost(a,r){let l=0,h=a.length,c=0;while(l<h){let m=(l+h)>>1;c++;if(m<r)l=m+1;else h=m}return c}
 const maxRank=Math.max(...ranks.map(r=>r.reduce((s,n,j)=>s+rankCost(L[j],n),0)));
 const memo=new Map;
 function solve(s){if(memo.has(s))return memo.get(s);if(omask.some(m=>(s&m)===s)){const ans={d:0,q:-1};memo.set(s,ans);return ans}
 let best={d:Infinity,q:-1};for(let j=0;j<tests.length;j++){const y=s&tmask[j],n=s^y;if(y===0n||n===0n)continue;const a=solve(y);if(a.d+1>=best.d)continue;const b=solve(n),d=1+Math.max(a.d,b.d);if(d<best.d)best={d,q:j}}
 if(!Number.isFinite(best.d))throw Error("no decision");memo.set(s,best);return best}
 const root=solve(all);
 const treeNodes=(s)=>{const a=solve(s);if(a.q<0)return {out:outputs[omask.findIndex(m=>(s&m)===s)]};const y=s&tmask[a.q],n=s^y;return {q:a.q,yes:treeNodes(y),no:treeNodes(n)}};
 const tree=treeNodes(all);
 let worst=0,total=0;for(let i=0;i<N;i++){let t=tree,d=0;while(t.q!==undefined){d++;t=(tmask[t.q]&(1n<<BigInt(i)))!==0n?t.yes:t.no}if(t.out!==out[i])throw Error("tree replay");worst=Math.max(worst,d);total+=d}
 if(worst!==root.d)throw Error("depth");
 return {queries:checks-before,rankVectors:N,outputCount:outputs.length,outputMasks:outputs.sort((a,b)=>a-b),maxRank,optimalWorst:root.d,worst,meanDepth:total/N,states:memo.size,first:tests[root.q],tests,L,tree};
 }
 const reduced=solveModel(false),raw=solveModel(true);
 const pop=[];for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){const v=[x,y,z];if(!(v.find(t=>t!==0)>0)||Math.max(v.reduce((a,t)=>a+Math.max(t,0),0),v.reduce((a,t)=>a+Math.max(-t,0),0))>10)continue;pop.push({v,a:gap(v)})}
 if(pop.length!==1935)throw Error("population");
 function score(a,s){let j=0;for(let k=1;k<6;k++)if(a[k]*s[j]>a[j]*s[k])j=k;return [a[j],s[j]]}
 function opt(rows,s){let u=score(rows[0],s);for(const a of rows.slice(1)){const v=score(a,s);if(v[0]*u[1]<u[0]*v[1])u=v}return u}
 const values=[1,2,3,5,8,13,21,34,55,89,144,233,377,610,987],weights=[];for(const t of [1,2,5,8])for(const B of values)for(const D of values)weights.push([17*t,B,22*t,D]);
 weights.push(...[20,8,4].flatMap(B=>[188,292,421,448,528,568,1584+8*B,2448+17*B].map(D=>[136,B,176,D])));
 const index=new Map(V.map((v,i)=>[String(v),i])),fullRows=pop.map(r=>r.a);let observedWorstReduced=0,observedWorstRaw=0,equalities=0;
 for(const w of weights){const s=J.map(([i,j])=>w[i]+w[j]),[n,d]=opt(G,s),[N,D]=opt(fullRows,s);if(n*D!==N*d)throw Error("opt");
 let actual=0;for(const a of pop){const [p,q]=score(a.a,s);if(2*p*d===3*n*q)equalities++;if(2*p*d<3*n*q){const i=index.get(String(a.v));if(i===undefined)throw Error("bank");actual|=1<<i}}
 for(const model of [reduced,raw]){let t=model.tree,k=0;while(t.q!==undefined){const {j,g}=model.tests[t.q];t=2*d*g<3*n*s[j]?t.yes:t.no;k++}if(t.out!==actual)throw Error("full replay "+w);if(model===reduced)observedWorstReduced=Math.max(observedWorstReduced,k);else observedWorstRaw=Math.max(observedWorstRaw,k)}
 }
 return {boxes:boxes.length,nonemptyBases:bases.length,queries:checks,maxProduct,reduced,raw,weights:weights.length,fullRowChecks:weights.length*pop.length,equalities,observedWorstReduced,observedWorstRaw};
}
console.log(JSON.stringify(exactTree(),null,2));
```

## Continuation

Same own informed Researcher/Activity as R165. Prior original X6 continuation has NO_CURRENT_FORMAL_TASK, no formal CLAIM/Result or owner mutation. Next: incorporate optimizer active-channel decisions into the adaptive model, or project the exact optimal decision complexity to other weight ratios / Ports. This theorem and R165 await independent review; no P000 or native claim.
