# X6 R222 — bounded joint-budget subtree resynthesis

2026-11-26; AUTHOR PROOF AND EXACT COMPUTATION / NOT_REVIEWED. Independent informed static six-pair BRC continuation. Frozen Port 10, 1935 unoriented integer directions, positive weights (17t,B,22t,D), full strict 3/2 near mask and legal eta term, P000 retained. Auxiliary weight-coordinate chart. Source R221@7800603f36a2d99096ca4de7866e782cc51a2d07:research_notes/portable_direct/2026-11-26_r2_x6_r221_fixed_partition_linearization.md; R220@fc01363a177cea3e107d701741022e72e7a29368; R219@180042eca43ea1f5bbc0c6e0f409db70b53ebd42; lower bounds R216@0b5f89c35844559a07c3cd49c25f882ae1c7472f, R217@c7d78ae72c2dcb4970f9b830397f6be65e359fb1. The earlier source bank-coverage qualification is inherited, not replaced by sample checks. No repinning of science.

## Exact finite-state reduction and budget recurrence

Keep the complete 47-form ternary sign fibers, including zeros. Every query in the declared library is a signed support-linear test or signed product test; its Boolean answer is constant on a fiber. For each fiber intersect all legal eta-term sets from the full relatively open face representatives of the R220 raw arrangement; the near mask must agree. The 256 raw forms include all candidate term-comparison and near-threshold walls. Hence these intersections hold throughout each fiber under the inherited bank theorem. Restrict outputs to the 35 labels occurring in R221. For a label a let C_a be the fibers on which it is legal, and U_a be the fibers where it is the sole legal label *in this restricted output alphabet*. For each near mask n let G_n be its fibers. For any nonempty state S, the number of leaves needed is at least B(S)=sum over n with S∩G_n nonempty of max(1, number of labels a of near mask n with S∩U_a nonempty). Distinct near masks need distinct leaves and each singleton witness forces its label. Thus if B(S)>2^d the state is infeasible at remaining depth d. This bound is for the declared 35-label search; do not automatically apply local exhaustive failures to a larger output alphabet.

Let F(S,d,k) be feasibility with remaining depth d and per-path quadratic budget k. F is true immediately if S is contained in some C_a. Otherwise F is the disjunction over nontrivial splits q of F(S∩q,d−1,k−cost(q)) AND F(S\\q,d−1,k−cost(q)), where cost(q)=0 for linear and 1 for quadratic. Reject d=0, insufficient k or B(S)>2^d. This recurrence is exact by root decomposition. Complementary local partitions are equivalent after exchanging child subtrees; of queries inducing the same unordered partition retain one with minimum cost (linear candidates first). This preserves feasibility because remaining k is monotone. No inference from a signed product about individual factors is needed; retain strict positivity tests and all zeros. Memoization stores completed states only. A budget cut is UNKNOWN, not infeasibility. Every FOUND certificate is verified independently of the search decisions over all fibers and their exact intersected legal masks. EXHAUSTED is scoped to this finite query library, fixed state, depth and restricted alphabet. The global arbitrary-coefficient model lower bound remains 1 from R216 and the new constructive upper bound is 4.

## Actual computation

Raw arrangement regenerated exactly using BigInt, with 256 forms, 11487 full-dimensional cells, 43685 positive face representatives and 1925 support fibers. New tree uses 60 internal nodes, of which 9 are quadratic, 61 leaves, 35 labels, depth at most six and per-path joint budget 4. R221 baseline budget 6, 23 quadratic nodes. The tree is a new partition synthesis, not just local replacement. No whole-population direction rerun in this round: R220/R221 exact full-direction checks are inherited with their original scope. Fiber legality was independently recalculated from all raw arrangement faces for the candidate bank. The count of distinct factors is a cache-model form count, not arithmetic latency. Search work counts are actual unique local split scans after deduplication, not raw query loop iterations. Further optimization with expanded predicate/label libraries and independent review remain open.

## Exact result and fixed certificate

```json
{
  "rawLines": 256,
  "cells": 11487,
  "positiveRepresentatives": 43685,
  "patterns": 1925,
  "labels": 35,
  "globalCoverLower": 35,
  "old": {
    "hist": {
      "2": 305,
      "3": 507,
      "4": 896,
      "5": 158,
      "6": 59
    },
    "depth": {
      "5": 427,
      "6": 1498
    },
    "n": 1925,
    "maxq": 6,
    "nodes": [
      54,
      23,
      55
    ],
    "outputs": 35,
    "maxDistinct": 10,
    "joint": 6859
  },
  "stage3": {
    "hist": {
      "2": 305,
      "3": 1324,
      "4": 296
    },
    "depth": {
      "5": 206,
      "6": 1719
    },
    "n": 1925,
    "maxq": 4,
    "nodes": [
      56,
      13,
      57
    ],
    "outputs": 35,
    "maxDistinct": 10,
    "joint": 5766
  },
  "stage5": {
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
  "logs": [
    {
      "path": "YYYYY",
      "d": 1,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 1,
      "scans": 19
    },
    {
      "path": "YYYY",
      "d": 2,
      "target": 1,
      "status": "EXHAUSTED",
      "states": 7,
      "scans": 271
    },
    {
      "path": "YYY",
      "d": 3,
      "target": 2,
      "status": "FOUND",
      "states": 7,
      "scans": 839
    },
    {
      "path": "YYY",
      "d": 3,
      "target": 1,
      "status": "FOUND",
      "states": 23,
      "scans": 3736
    },
    {
      "path": "YYNYN",
      "d": 1,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 1,
      "scans": 9
    },
    {
      "path": "YYNY",
      "d": 2,
      "target": 1,
      "status": "FOUND",
      "states": 2,
      "scans": 41
    },
    {
      "path": "YYNY",
      "d": 2,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 3,
      "scans": 17
    },
    {
      "path": "YYN",
      "d": 3,
      "target": 1,
      "status": "FOUND",
      "states": 10,
      "scans": 252
    },
    {
      "path": "YYN",
      "d": 3,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 9,
      "scans": 129
    },
    {
      "path": "YNYNN",
      "d": 1,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 1,
      "scans": 25
    },
    {
      "path": "YNYN",
      "d": 2,
      "target": 1,
      "status": "EXHAUSTED",
      "states": 2,
      "scans": 234
    },
    {
      "path": "YNY",
      "d": 3,
      "target": 1,
      "status": "FOUND",
      "states": 11,
      "scans": 2506
    },
    {
      "path": "NYYY",
      "d": 2,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 1,
      "scans": 30
    },
    {
      "path": "NYYN",
      "d": 2,
      "target": 0,
      "status": "FOUND",
      "states": 3,
      "scans": 36
    },
    {
      "path": "NYY",
      "d": 3,
      "target": 1,
      "status": "EXHAUSTED",
      "states": 1,
      "scans": 526
    },
    {
      "path": "NYNYN",
      "d": 1,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 1,
      "scans": 22
    },
    {
      "path": "NYNY",
      "d": 2,
      "target": 1,
      "status": "EXHAUSTED",
      "states": 7,
      "scans": 377
    },
    {
      "path": "NYN",
      "d": 3,
      "target": 1,
      "status": "EXHAUSTED",
      "states": 27,
      "scans": 3267
    },
    {
      "path": "NNY",
      "d": 3,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 3,
      "scans": 99
    },
    {
      "path": "NNNY",
      "d": 2,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 1,
      "scans": 20
    },
    {
      "path": "NNNN",
      "d": 2,
      "target": 0,
      "status": "FOUND",
      "states": 2,
      "scans": 73
    },
    {
      "path": "NNN",
      "d": 3,
      "target": 1,
      "status": "FOUND",
      "states": 19,
      "scans": 1558
    },
    {
      "path": "NNN",
      "d": 3,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 3,
      "scans": 98
    },
    {
      "path": "YYN",
      "d": 3,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 0,
      "scans": 0
    },
    {
      "path": "YY",
      "d": 4,
      "target": 1,
      "status": "FOUND",
      "states": 83,
      "scans": 2316
    },
    {
      "path": "YY",
      "d": 4,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 34,
      "scans": 969
    },
    {
      "path": "YN",
      "d": 4,
      "target": 0,
      "status": "FOUND",
      "states": 22,
      "scans": 489
    },
    {
      "path": "Y",
      "d": 5,
      "target": 1,
      "status": "FOUND",
      "states": 407,
      "scans": 31766
    },
    {
      "path": "Y",
      "d": 5,
      "target": 0,
      "status": "FOUND",
      "states": 126,
      "scans": 3440
    },
    {
      "path": "NYYY",
      "d": 2,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 0,
      "scans": 0
    },
    {
      "path": "NYY",
      "d": 3,
      "target": 1,
      "status": "EXHAUSTED",
      "states": 0,
      "scans": 0
    },
    {
      "path": "NYNYN",
      "d": 1,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 0,
      "scans": 0
    },
    {
      "path": "NYNY",
      "d": 2,
      "target": 1,
      "status": "EXHAUSTED",
      "states": 0,
      "scans": 0
    },
    {
      "path": "NYN",
      "d": 3,
      "target": 1,
      "status": "EXHAUSTED",
      "states": 0,
      "scans": 0
    },
    {
      "path": "NY",
      "d": 4,
      "target": 2,
      "status": "EXHAUSTED",
      "states": 115,
      "scans": 43497
    },
    {
      "path": "NNY",
      "d": 3,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 0,
      "scans": 0
    },
    {
      "path": "NNN",
      "d": 3,
      "target": 0,
      "status": "EXHAUSTED",
      "states": 0,
      "scans": 0
    },
    {
      "path": "NN",
      "d": 4,
      "target": 1,
      "status": "EXHAUSTED",
      "states": 298,
      "scans": 22769
    },
    {
      "path": "N",
      "d": 5,
      "target": 2,
      "status": "BUDGET",
      "states": 1501,
      "scans": 400231
    },
    {
      "path": "ROOT",
      "d": 6,
      "target": 3,
      "status": "BUDGET",
      "states": 5001,
      "scans": 1493432
    }
  ],
  "visited": 7732,
  "scans": 2013093,
  "cut": 2,
  "tree": {
    "q": [
      1,
      29,
      1
    ],
    "yes": {
      "q": [
        9,
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
            2,
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
              16,
              -1,
              1
            ],
            "yes": {
              "q": [
                25,
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
                  4096
                ]
              }
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
            0,
            -1,
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
                1,
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
                  72,
                  1
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
      },
      "no": {
        "q": [
          23,
          -1,
          -1
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
                2,
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
                  132,
                  16
                ]
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
          }
        },
        "no": {
          "q": [
            27,
            -1,
            -1
          ],
          "yes": {
            "q": [
              28,
              -1,
              -1
            ],
            "yes": {
              "q": [
                19,
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
                  164,
                  16
                ]
              }
            },
            "no": {
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
            }
          },
          "no": {
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
            }
          }
        }
      }
    },
    "no": {
      "q": [
        20,
        -1,
        -1
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
                21,
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
                  569,
                  8
                ]
              }
            },
            "no": {
              "q": [
                17,
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
                  8192
                ]
              }
            }
          },
          "no": {
            "q": [
              3,
              -1,
              1
            ],
            "yes": {
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
            },
            "no": {
              "q": [
                31,
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
                  256
                ]
              }
            }
          }
        },
        "no": {
          "q": [
            31,
            -1,
            1
          ],
          "yes": {
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
          },
          "no": {
            "q": [
              14,
              -1,
              -1
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
              "q": [
                21,
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
              18,
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
                8
              ]
            }
          },
          "no": {
            "q": [
              38,
              -1,
              -1
            ],
            "yes": {
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
            },
            "no": {
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
            }
          }
        },
        "no": {
          "q": [
            3,
            30,
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
                34,
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
                  49,
                  1024
                ]
              }
            },
            "no": {
              "q": [
                12,
                -1,
                1
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
                  8
                ]
              }
            }
          },
          "no": {
            "q": [
              13,
              -1,
              1
            ],
            "yes": {
              "q": [
                4,
                -1,
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
                  128
                ]
              }
            },
            "no": {
              "q": [
                15,
                -1,
                -1
              ],
              "yes": {
                "out": [
                  561,
                  8
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
function bound(S,lim=1e9){let n=0;for(let g of groupList)if(g.b&S){let z=0;for(let b of g.s)if(b&S)z++;n+=Math.max(1,z);if(n>lim)return n}return n}
function leaf(S){for(let i=0;i<covers.length;i++)if((S&covers[i])===S)return {out:lab[i]};return null}
Q.sort((a,b)=>Number(a.q[1]>=0)-Number(b.q[1]>=0));
let visited=0, scans=0, cut=0, cap=1000, memo=new Map();
const stop={};
function solve(S,d,k){
 let l=leaf(S);if(l)return l;if(!d||bound(S,1<<d)>(1<<d))return null;
 const key=S.toString(36)+"/"+d+"/"+k;if(memo.has(key))return memo.get(key);
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
 let start=visited,sc0=scans;cap=visited+(d===6?5000:d>=4?1500:500);let ans=null,status;
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
const stage3=improve(tree,all,6,"",3);
const stage5=improve(stage3,all,6,"",5);
let t=stage5,b=maxq(t);
while(b>0){let ans=trial(all,6,b-1,"ROOT");if(!ans)break;t=ans;b=maxq(t)}
return {rawLines:L.length,cells:cells.length,positiveRepresentatives:pts.size,patterns:N,labels:lab.length,globalCoverLower:bound(all),old:verify(tree),stage3:verify(stage3),stage5:verify(stage5),optimized:verify(t),logs,visited,scans,cut,tree:t};
}

return audit({"q":[1,29,1],"yes":{"q":[0,26,-1],"yes":{"q":[2,7,-1],"yes":{"q":[16,27,-1],"yes":{"q":[2,25,1],"yes":{"q":[2,41,1],"yes":{"out":[951,4096]},"no":{"out":[693,4096]}},"no":{"q":[2,-1,1],"yes":{"out":[693,4096]},"no":{"out":[693,16]}}},"no":{"q":[16,-1,1],"yes":{"out":[132,16]},"no":{"q":[11,-1,1],"yes":{"out":[693,16]},"no":{"out":[693,64]}}}},"no":{"q":[9,25,-1],"yes":{"q":[2,8,-1],"yes":{"out":[951,4]},"no":{"q":[2,10,-1],"yes":{"out":[695,4]},"no":{"out":[693,4]}}},"no":{"q":[7,-1,1],"yes":{"out":[132,4]},"no":{"q":[1,-1,1],"yes":{"out":[693,4096]},"no":{"out":[72,1]}}}}},"no":{"q":[0,24,-1],"yes":{"q":[27,-1,1],"yes":{"q":[2,-1,1],"yes":{"out":[132,4]},"no":{"out":[132,16]}},"no":{"q":[19,27,1],"yes":{"q":[23,-1,-1],"yes":{"out":[692,16]},"no":{"out":[676,16]}},"no":{"q":[27,28,1],"yes":{"out":[164,16]},"no":{"out":[132,16]}}}},"no":{"q":[0,-1,1],"yes":{"q":[6,-1,1],"yes":{"out":[132,32]},"no":{"out":[132,4]}},"no":{"q":[16,-1,-1],"yes":{"q":[33,-1,1],"yes":{"out":[72,512]},"no":{"out":[64,512]}},"no":{"q":[45,-1,1],"yes":{"out":[72,8192]},"no":{"out":[64,8192]}}}}}},"no":{"q":[20,-1,-1],"yes":{"q":[31,35,1],"yes":{"q":[15,46,-1],"yes":{"q":[17,22,-1],"yes":{"q":[21,-1,-1],"yes":{"out":[633,8]},"no":{"out":[569,8]}},"no":{"q":[17,-1,1],"yes":{"out":[561,8]},"no":{"out":[633,8192]}}},"no":{"q":[31,37,-1],"yes":{"q":[15,-1,-1],"yes":{"out":[72,8192]},"no":{"out":[121,1024]}},"no":{"q":[15,-1,-1],"yes":{"out":[72,256]},"no":{"out":[49,1024]}}}},"no":{"q":[31,-1,1],"yes":{"q":[40,46,1],"yes":{"q":[40,-1,1],"yes":{"out":[121,8192]},"no":{"out":[72,8192]}},"no":{"q":[43,46,1],"yes":{"out":[89,8192]},"no":{"out":[72,8192]}}},"no":{"q":[14,-1,-1],"yes":{"q":[32,-1,1],"yes":{"out":[633,256]},"no":{"out":[72,256]}},"no":{"q":[21,-1,-1],"yes":{"out":[633,8]},"no":{"out":[569,8]}}}}},"no":{"q":[5,16,1],"yes":{"q":[18,42,1],"yes":{"q":[18,-1,1],"yes":{"q":[44,-1,1],"yes":{"out":[693,4096]},"no":{"out":[689,4096]}},"no":{"out":[561,8]}},"no":{"q":[38,-1,-1],"yes":{"q":[39,-1,1],"yes":{"out":[561,4096]},"no":{"out":[561,16384]}},"no":{"q":[36,-1,1],"yes":{"out":[561,4096]},"no":{"out":[561,2048]}}}},"no":{"q":[3,34,1],"yes":{"q":[4,30,1],"yes":{"q":[13,-1,1],"yes":{"out":[561,128]},"no":{"out":[561,8]}},"no":{"q":[4,-1,-1],"yes":{"out":[561,4096]},"no":{"out":[561,2]}}},"no":{"q":[12,15,1],"yes":{"out":[561,8]},"no":{"q":[3,-1,1],"yes":{"out":[49,1024]},"no":{"out":[561,64]}}}}}}});
```

## Current control and next

Original exact-topic native query r2-20261126T1213-x6-current-task-read returned SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY, source d34b74fbdb766a797634faec5c2300bc1958d6f7, observed 2026-11-26T04:13:57.778669Z. It is a directory-absence observation only, not owner projection or research authorization. No CLAIM, identity reassignment or protected state mutation. Current activity identity unconfirmed. Next: use the saved certificate and exact bounded-state recurrence to tighten K6; if root budget search exhausts, distinguish restricted-library/label lower bound from arbitrary-coefficient lower bound. Continue by improving pruning, expanding library or proving structural obstructions. Independent review remains open.
