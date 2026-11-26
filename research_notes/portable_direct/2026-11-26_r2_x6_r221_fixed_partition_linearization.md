# X6 R221 — fixed-partition exact linearization and cached factor-cost audit

2026-11-26; AUTHOR PROOF AND EXACT COMPUTATION / NOT_REVIEWED. Independent informed static six-pair BRC continuation. Frozen Port 10, 1935 unoriented integer directions, weights (17t,B,22t,D)>0, full strict 3/2 near mask and legal eta term. P000 V5, ACTIVE worldview and joint relation preservation retained. Auxiliary weight-coordinate chart only. Input: R220@fc01363a177cea3e107d701741022e72e7a29368:research_notes/portable_direct/2026-11-26_r2_x6_r220_quadratic_tree_raw_arrangement_audit.md; R219@180042eca43ea1f5bbc0c6e0f409db70b53ebd42; lower bounds R216@0b5f89c35844559a07c3cd49c25f882ae1c7472f and R217@c7d78ae72c2dcb4970f9b830397f6be65e359fb1. No repinning of science.

## Exact local partition replacement theorem

For a binary decision tree on a domain U, let S_v be the actual input subset reaching a node v, with old split Y_v and S_v\\Y_v. Let Q_1 and Q_2 be the allowed linear and quadratic sign predicates. If a predicate q has true set on S_v equal to Y_v or its complement in S_v, replacing the old predicate by q (and swapping children in the complement case) preserves the full leaf reached for every input. Induction from the root proves all descendant input subsets unchanged, up to path names. This is valid on boundaries: complement means logical negation of a strict positive test, not simply reversing the sign of the polynomial. Retain all zero signs.

Consequently for the fixed labeled tree and fixed node partitions, if some linear predicate is equivalent, a linear test can replace that node; if none is equivalent, that node must remain nonlinear in any rewrite restricted to the declared predicate library and exact partition. Choices are independent across nodes because reaching subsets remain unchanged. Replacing every linearizable node minimizes total nonlinear-node count and simultaneously the nonlinear count along every original leaf path in this fixed-partition class. This is not a lower bound for arbitrary new topologies, partitions, output selections, or arbitrary linear coefficients. The support library is not erased; the certificate covers this static output tree and its paths only.

The R220 raw 256-form arrangement includes every one of the 47 frozen support forms. The sign of each support form is constant on each relatively open face; positive representatives for vertices, edges and cells cover the positive cone projectively. Thus a partition equality across all 1925 complete ternary support-sign fibers is an exact equality on the declared continuum. Use full bit masks; do not identify zero with either sign. The candidates are all 94 signed linear tests, 47 nonzero square tests, and 2162 signed distinct-factor products (2303 total, including any partition duplicates). Match each candidate against the actual node's true and false masks. Pick minimum degree; within that choose fewest new factor evaluations relative to a path cache, then lexicographic order. The latter is a greedy secondary criterion, not an optimal caching proof. Cache stores exact ternary sign per primitive factor, not a guessed sign from a product.

## Results and resource semantics

The rewritten tree retains all 55 leaves, 35 outputs, maximum depth 6 and the original leaf identity on every complete support fiber (up to child swaps). The number of quadratic internal nodes changes from 53 to 23; 31 nodes have an equivalent signed support-linear predicate. The exact fixed-partition minimum is 23. All 43685 raw positive face representatives were compared with the original path output and replayed against exact scoring. R220's full direction check was rerun once per support-sign fiber, 3724875 original direction scores. The same inherited bank coverage qualification applies as R220. Metrics below count actual representative fibers, not a probability distribution on the real cone. 'distinct' is the number of distinct support forms whose ternary signs are evaluated along a path, assuming cached signs and no further inference; 'uncached' counts occurrences, with a square's repeated factor evaluated once. These are primitive form-evaluation counts, not binary comparison depth, CPU latency, bit complexity, or a claim of lower total arithmetic cost.

## Exact output, node certificate and rewritten tree

```json
{
  "rewrite": {
    "rawLines": 256,
    "cells": 11487,
    "positiveRepresentatives": 43685,
    "patterns": 1925,
    "queryCandidates": 2303,
    "nodes": 54,
    "originalQuadratic": 53,
    "newQuadratic": 23,
    "linearizableNodes": 31,
    "metrics": {
      "old": {
        "depth": {
          "5": 427,
          "6": 1498
        },
        "quadratic": {
          "4": 60,
          "5": 413,
          "6": 1452
        },
        "distinct": {
          "6": 60,
          "7": 146,
          "8": 263,
          "9": 540,
          "10": 284,
          "11": 455,
          "12": 177
        },
        "uncached": {
          "9": 60,
          "10": 367,
          "11": 46,
          "12": 1452
        }
      },
      "new": {
        "depth": {
          "5": 427,
          "6": 1498
        },
        "quadratic": {
          "2": 305,
          "3": 507,
          "4": 896,
          "5": 158,
          "6": 59
        },
        "distinct": {
          "6": 60,
          "7": 519,
          "8": 439,
          "9": 761,
          "10": 146
        },
        "uncached": {
          "8": 471,
          "9": 596,
          "10": 647,
          "11": 152,
          "12": 59
        }
      }
    },
    "info": [
      {
        "path": "",
        "patterns": 1925,
        "original": [
          1,
          29,
          1
        ],
        "chosen": [
          1,
          29,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "Y",
        "patterns": 638,
        "original": [
          0,
          26,
          -1
        ],
        "chosen": [
          0,
          26,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "YY",
        "patterns": 288,
        "original": [
          2,
          7,
          -1
        ],
        "chosen": [
          2,
          7,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "YYY",
        "patterns": 218,
        "original": [
          16,
          27,
          -1
        ],
        "chosen": [
          16,
          27,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "YYYY",
        "patterns": 124,
        "original": [
          2,
          25,
          1
        ],
        "chosen": [
          2,
          25,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 2
      },
      {
        "path": "YYYYY",
        "patterns": 40,
        "original": [
          2,
          41,
          1
        ],
        "chosen": [
          2,
          41,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 3
      },
      {
        "path": "YYYYN",
        "patterns": 84,
        "original": [
          0,
          2,
          1
        ],
        "chosen": [
          2,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 4,
        "quadraticOptions": 132
      },
      {
        "path": "YYYN",
        "patterns": 94,
        "original": [
          0,
          16,
          1
        ],
        "chosen": [
          16,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 6,
        "quadraticOptions": 192
      },
      {
        "path": "YYYNN",
        "patterns": 82,
        "original": [
          0,
          11,
          1
        ],
        "chosen": [
          11,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 37
      },
      {
        "path": "YYN",
        "patterns": 70,
        "original": [
          9,
          25,
          -1
        ],
        "chosen": [
          9,
          25,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "YYNY",
        "patterns": 25,
        "original": [
          2,
          8,
          -1
        ],
        "chosen": [
          2,
          8,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "YYNYN",
        "patterns": 19,
        "original": [
          2,
          10,
          -1
        ],
        "chosen": [
          2,
          10,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "YYNN",
        "patterns": 45,
        "original": [
          0,
          7,
          1
        ],
        "chosen": [
          7,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 4,
        "quadraticOptions": 40
      },
      {
        "path": "YYNNN",
        "patterns": 21,
        "original": [
          0,
          1,
          1
        ],
        "chosen": [
          1,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 52,
        "quadraticOptions": 858
      },
      {
        "path": "YN",
        "patterns": 350,
        "original": [
          0,
          24,
          -1
        ],
        "chosen": [
          0,
          24,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 26
      },
      {
        "path": "YNY",
        "patterns": 244,
        "original": [
          0,
          27,
          1
        ],
        "chosen": [
          27,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 29
      },
      {
        "path": "YNYY",
        "patterns": 100,
        "original": [
          0,
          2,
          1
        ],
        "chosen": [
          2,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 35
      },
      {
        "path": "YNYN",
        "patterns": 144,
        "original": [
          19,
          27,
          1
        ],
        "chosen": [
          19,
          27,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "YNYNY",
        "patterns": 76,
        "original": [
          0,
          23,
          -1
        ],
        "chosen": [
          23,
          -1,
          -1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 36
      },
      {
        "path": "YNYNN",
        "patterns": 68,
        "original": [
          27,
          28,
          1
        ],
        "chosen": [
          27,
          28,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "YNN",
        "patterns": 106,
        "original": [
          0,
          -1,
          1
        ],
        "chosen": [
          0,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 60,
        "quadraticOptions": 0
      },
      {
        "path": "YNNY",
        "patterns": 60,
        "original": [
          0,
          6,
          1
        ],
        "chosen": [
          6,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 32
      },
      {
        "path": "YNNN",
        "patterns": 46,
        "original": [
          1,
          16,
          1
        ],
        "chosen": [
          16,
          -1,
          -1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 39
      },
      {
        "path": "YNNNY",
        "patterns": 6,
        "original": [
          1,
          33,
          -1
        ],
        "chosen": [
          33,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 44
      },
      {
        "path": "YNNNN",
        "patterns": 40,
        "original": [
          0,
          45,
          -1
        ],
        "chosen": [
          45,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 40
      },
      {
        "path": "N",
        "patterns": 1287,
        "original": [
          11,
          20,
          1
        ],
        "chosen": [
          20,
          -1,
          -1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 11
      },
      {
        "path": "NY",
        "patterns": 660,
        "original": [
          31,
          35,
          1
        ],
        "chosen": [
          31,
          35,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NYY",
        "patterns": 230,
        "original": [
          15,
          46,
          -1
        ],
        "chosen": [
          15,
          46,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NYYY",
        "patterns": 163,
        "original": [
          17,
          22,
          -1
        ],
        "chosen": [
          17,
          22,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NYYYY",
        "patterns": 73,
        "original": [
          0,
          21,
          -1
        ],
        "chosen": [
          21,
          -1,
          -1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 35
      },
      {
        "path": "NYYYN",
        "patterns": 90,
        "original": [
          0,
          14,
          1
        ],
        "chosen": [
          17,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 4,
        "quadraticOptions": 128
      },
      {
        "path": "NYYN",
        "patterns": 67,
        "original": [
          31,
          37,
          -1
        ],
        "chosen": [
          31,
          37,
          -1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 2
      },
      {
        "path": "NYYNY",
        "patterns": 34,
        "original": [
          0,
          3,
          1
        ],
        "chosen": [
          15,
          -1,
          -1
        ],
        "swap": true,
        "linearOptions": 10,
        "quadraticOptions": 360
      },
      {
        "path": "NYYNN",
        "patterns": 33,
        "original": [
          0,
          3,
          1
        ],
        "chosen": [
          15,
          -1,
          -1
        ],
        "swap": true,
        "linearOptions": 21,
        "quadraticOptions": 630
      },
      {
        "path": "NYN",
        "patterns": 430,
        "original": [
          11,
          31,
          -1
        ],
        "chosen": [
          31,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 19
      },
      {
        "path": "NYNY",
        "patterns": 125,
        "original": [
          40,
          46,
          1
        ],
        "chosen": [
          40,
          46,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NYNYY",
        "patterns": 62,
        "original": [
          1,
          40,
          1
        ],
        "chosen": [
          40,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 4,
        "quadraticOptions": 144
      },
      {
        "path": "NYNYN",
        "patterns": 63,
        "original": [
          43,
          46,
          1
        ],
        "chosen": [
          43,
          46,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NYNN",
        "patterns": 305,
        "original": [
          0,
          14,
          -1
        ],
        "chosen": [
          14,
          -1,
          -1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 25
      },
      {
        "path": "NYNNY",
        "patterns": 163,
        "original": [
          0,
          32,
          1
        ],
        "chosen": [
          32,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 28
      },
      {
        "path": "NYNNN",
        "patterns": 142,
        "original": [
          0,
          21,
          -1
        ],
        "chosen": [
          21,
          -1,
          -1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 31
      },
      {
        "path": "NN",
        "patterns": 627,
        "original": [
          5,
          16,
          1
        ],
        "chosen": [
          5,
          16,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NNY",
        "patterns": 239,
        "original": [
          18,
          42,
          1
        ],
        "chosen": [
          18,
          42,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NNYY",
        "patterns": 114,
        "original": [
          0,
          12,
          1
        ],
        "chosen": [
          18,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 6,
        "quadraticOptions": 174
      },
      {
        "path": "NNYYY",
        "patterns": 108,
        "original": [
          0,
          44,
          1
        ],
        "chosen": [
          44,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 33
      },
      {
        "path": "NNYN",
        "patterns": 125,
        "original": [
          0,
          38,
          -1
        ],
        "chosen": [
          38,
          -1,
          -1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 32
      },
      {
        "path": "NNYNY",
        "patterns": 67,
        "original": [
          0,
          39,
          1
        ],
        "chosen": [
          39,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 38
      },
      {
        "path": "NNYNN",
        "patterns": 58,
        "original": [
          0,
          36,
          1
        ],
        "chosen": [
          36,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 37
      },
      {
        "path": "NNN",
        "patterns": 388,
        "original": [
          3,
          34,
          1
        ],
        "chosen": [
          3,
          34,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NNNY",
        "patterns": 63,
        "original": [
          4,
          30,
          1
        ],
        "chosen": [
          4,
          30,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NNNYY",
        "patterns": 14,
        "original": [
          0,
          13,
          1
        ],
        "chosen": [
          13,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 44
      },
      {
        "path": "NNNYN",
        "patterns": 49,
        "original": [
          0,
          4,
          -1
        ],
        "chosen": [
          4,
          -1,
          -1
        ],
        "swap": false,
        "linearOptions": 1,
        "quadraticOptions": 38
      },
      {
        "path": "NNNN",
        "patterns": 325,
        "original": [
          12,
          15,
          1
        ],
        "chosen": [
          12,
          15,
          1
        ],
        "swap": false,
        "linearOptions": 0,
        "quadraticOptions": 1
      },
      {
        "path": "NNNNN",
        "patterns": 106,
        "original": [
          0,
          3,
          1
        ],
        "chosen": [
          3,
          -1,
          1
        ],
        "swap": false,
        "linearOptions": 19,
        "quadraticOptions": 390
      }
    ],
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
                  2,
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
                    16
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
                "out": [
                  132,
                  16
                ]
              },
              "no": {
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
              27,
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
                16,
                -1,
                -1
              ],
              "yes": {
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
              },
              "no": {
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
                31,
                37,
                -1
              ],
              "yes": {
                "q": [
                  15,
                  -1,
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
                    121,
                    1024
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
                    72,
                    256
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
                  13,
                  -1,
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
                  4,
                  -1,
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
                  3,
                  -1,
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
    }
  },
  "rawLines": 256,
  "cells": 11487,
  "positiveRepresentatives": 43685,
  "treeReplay": "PASS",
  "depthCounts": {
    "5": 7871,
    "6": 35814
  },
  "uniqueOutputs": 35,
  "fullPopulation": 1935,
  "fullPatternRepresentatives": 1925,
  "fullDirectionChecks": 3724875,
  "stats": {
    "nodes": 54,
    "leaves": 55,
    "linear": 31,
    "quadratic": 23,
    "leafDepths": {
      "5": 9,
      "6": 46
    },
    "outputs": 35,
    "factors": 47
  }
}
```

## Standalone reproduction

The following JavaScript is the R220 immutable replay with the exact new partition-rewrite code inserted and executed before the unchanged raw-scoring audit. The final line returns the result in a function wrapper; for ordinary Node.js replace that final return by console.log(JSON.stringify(audit(tree),null,2)). No original tree search is executed.

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
const info=[];
function rewrite(t,S,path,cache){
 if(t.out)return {out:t.out};
 let Y=mask(t.q)&S,Z=S^Y;if(!Y||!Z)throw Error("empty original branch "+path);
 const matches=Q.filter(c=>{let a=c.b&S;return a===Y||a===Z}).map(c=>({q:c.q,swap:(c.b&S)===Z,new:factors(c.q).filter(i=>!cache.has(i)).length}));
 matches.sort((a,b)=>Number(a.q[1]>=0)-Number(b.q[1]>=0)||a.new-b.new||a.q[0]-b.q[0]||a.q[1]-b.q[1]||b.q[2]-a.q[2]);
 if(!matches.length)throw Error("no equivalent query");
 let c=matches[0],next=new Set([...cache,...factors(c.q)]);
 info.push({path,patterns:count(S),original:t.q,chosen:c.q,swap:c.swap,linearOptions:matches.filter(x=>x.q[1]<0).length,quadraticOptions:matches.filter(x=>x.q[1]>=0).length});
 let y=rewrite(t.yes,Y,path+"Y",next),z=rewrite(t.no,Z,path+"N",next);
 return {q:c.q,yes:c.swap?z:y,no:c.swap?y:z};
}
const old=tree,improved=rewrite(old,all,"",new Set());
function trace(t,s){let depth=0,quadratic=0,cache=new Set(),uncached=0;
 while(t.q){let [i,j,sg]=t.q;depth++;if(j>=0)quadratic++;let f=factors(t.q);uncached+=f.length;f.forEach(k=>cache.add(k));t=sg*s[i]*(j<0?1:s[j])>0?t.yes:t.no}
 return {out:t.out,depth,quadratic,distinct:cache.size,uncached};
}
const metrics={old:{},new:{}}, hist=(name,r)=>{for(let k of ["depth","quadratic","distinct","uncached"]){let h=metrics[name][k]??={};h[r[k]]=(h[r[k]]||0)+1}};
for(let s of A){let x=trace(old,s),y=trace(improved,s);if(x.out.join()!==y.out.join()||x.depth!==y.depth)throw Error("output or depth changed");hist("old",x);hist("new",y)}
for(let p of pts.values()){let s=sign(p),x=trace(old,s),y=trace(improved,s);if(x.out.join()!==y.out.join()||x.depth!==y.depth)throw Error("raw face mismatch")}
const rewriteResult={rawLines:L.length,cells:cells.length,positiveRepresentatives:pts.size,patterns:N,queryCandidates:Q.length,nodes:info.length,originalQuadratic:info.filter(a=>a.original[1]>=0).length,newQuadratic:info.filter(a=>a.chosen[1]>=0).length,linearizableNodes:info.filter(a=>a.linearOptions>0).length,metrics,info,tree:improved};
tree=improved;

function runTree(p){let node=tree,d=0;while(node.q){let [i,j,sg]=node.q;let x=dot(R[i],p)*BigInt(sg);if(j!==-1)x*=dot(R[j],p);node=x>0n?node.yes:node.no;d++}return [node.out,d]}
const vi=new Map(V.map((v,i)=>[v.join(),i])),covered=new Set();let exactFull=0,outs=new Set(),depthCounts={},fullMasks=0,fullChecks=0;
function max(a){return a.reduce((x,y)=>x>y?x:y)}
function min(a){return a.reduce((x,y)=>x<y?x:y)}
for(let p of pts.values()){
let c=E.map(e=>dot(e,p)),prod=c.reduce((s,x)=>s*x,1n),scale=c.map(x=>prod/x),scores=G.map(g=>max(g.map((a,i)=>a*scale[i]))),eta=min(W.map(i=>scores[i])),near=0;
for(let i=0;i<scores.length;i++)if(2n*scores[i]<3n*eta)near|=1<<i;
let [[n,m],depth]=runTree(p),i=Math.log2(m),[j,g]=T[i];if(n!==near||BigInt(g)*scale[j]!==eta)throw Error("tree mismatch");
outs.add([n,m].join());depthCounts[depth]=(depthCounts[depth]||0)+1;
let k=R.map(r=>{let x=dot(r,p);return x>0n?1:x<0n?-1:0}).join();if(!covered.has(k)){covered.add(k);let s=D.map(([v,g])=>max(g.map((a,i)=>a*scale[i]))),f=min(s),mask=0;if(f!==eta)throw Error("full optimum mismatch");for(let i=0;i<s.length;i++)if(2n*s[i]<3n*f){let j=vi.get(D[i][0].join());if(j===undefined)throw Error("full outsider");mask|=1<<j}if(mask!==n)throw Error("full near mismatch");fullChecks+=D.length;exactFull++;}}
let stats={nodes:0,leaves:0,linear:0,quadratic:0,leafDepths:{},outputs:new Set(),factors:new Set()};function walk(t,d){if(t.out){stats.leaves++;stats.leafDepths[d]=(stats.leafDepths[d]||0)+1;stats.outputs.add(t.out.join());return}stats.nodes++;let [i,k]=t.q;stats.factors.add(i);if(k<0)stats.linear++;else{stats.quadratic++;stats.factors.add(k)}walk(t.yes,d+1);walk(t.no,d+1)}walk(tree,0);
return {rewrite:rewriteResult,rawLines:L.length,cells:cells.length,positiveRepresentatives:pts.size,treeReplay:"PASS",depthCounts,uniqueOutputs:outs.size,fullPopulation:D.length,fullPatternRepresentatives:exactFull,fullDirectionChecks:fullChecks,stats:{...stats,outputs:stats.outputs.size,factors:stats.factors.size}};
}
const tree={"q":[1,29,1],"yes":{"q":[0,26,-1],"yes":{"q":[2,7,-1],"yes":{"q":[16,27,-1],"yes":{"q":[2,25,1],"yes":{"q":[2,41,1],"yes":{"out":[951,4096]},"no":{"out":[693,4096]}},"no":{"q":[0,2,1],"yes":{"out":[693,4096]},"no":{"out":[693,16]}}},"no":{"q":[0,16,1],"yes":{"out":[132,16]},"no":{"q":[0,11,1],"yes":{"out":[693,16]},"no":{"out":[693,64]}}}},"no":{"q":[9,25,-1],"yes":{"q":[2,8,-1],"yes":{"out":[951,4]},"no":{"q":[2,10,-1],"yes":{"out":[695,4]},"no":{"out":[693,4]}}},"no":{"q":[0,7,1],"yes":{"out":[132,4]},"no":{"q":[0,1,1],"yes":{"out":[693,4096]},"no":{"out":[72,1]}}}}},"no":{"q":[0,24,-1],"yes":{"q":[0,27,1],"yes":{"q":[0,2,1],"yes":{"out":[132,4]},"no":{"out":[132,16]}},"no":{"q":[19,27,1],"yes":{"q":[0,23,-1],"yes":{"out":[692,16]},"no":{"out":[676,16]}},"no":{"q":[27,28,1],"yes":{"out":[164,16]},"no":{"out":[132,16]}}}},"no":{"q":[0,-1,1],"yes":{"q":[0,6,1],"yes":{"out":[132,32]},"no":{"out":[132,4]}},"no":{"q":[1,16,1],"yes":{"q":[1,33,-1],"yes":{"out":[72,512]},"no":{"out":[64,512]}},"no":{"q":[0,45,-1],"yes":{"out":[72,8192]},"no":{"out":[64,8192]}}}}}},"no":{"q":[11,20,1],"yes":{"q":[31,35,1],"yes":{"q":[15,46,-1],"yes":{"q":[17,22,-1],"yes":{"q":[0,21,-1],"yes":{"out":[633,8]},"no":{"out":[569,8]}},"no":{"q":[0,14,1],"yes":{"out":[561,8]},"no":{"out":[633,8192]}}},"no":{"q":[31,37,-1],"yes":{"q":[0,3,1],"yes":{"out":[121,1024]},"no":{"out":[72,8192]}},"no":{"q":[0,3,1],"yes":{"out":[49,1024]},"no":{"out":[72,256]}}}},"no":{"q":[11,31,-1],"yes":{"q":[40,46,1],"yes":{"q":[1,40,1],"yes":{"out":[121,8192]},"no":{"out":[72,8192]}},"no":{"q":[43,46,1],"yes":{"out":[89,8192]},"no":{"out":[72,8192]}}},"no":{"q":[0,14,-1],"yes":{"q":[0,32,1],"yes":{"out":[633,256]},"no":{"out":[72,256]}},"no":{"q":[0,21,-1],"yes":{"out":[633,8]},"no":{"out":[569,8]}}}}},"no":{"q":[5,16,1],"yes":{"q":[18,42,1],"yes":{"q":[0,12,1],"yes":{"q":[0,44,1],"yes":{"out":[693,4096]},"no":{"out":[689,4096]}},"no":{"out":[561,8]}},"no":{"q":[0,38,-1],"yes":{"q":[0,39,1],"yes":{"out":[561,4096]},"no":{"out":[561,16384]}},"no":{"q":[0,36,1],"yes":{"out":[561,4096]},"no":{"out":[561,2048]}}}},"no":{"q":[3,34,1],"yes":{"q":[4,30,1],"yes":{"q":[0,13,1],"yes":{"out":[561,128]},"no":{"out":[561,8]}},"no":{"q":[0,4,-1],"yes":{"out":[561,4096]},"no":{"out":[561,2]}}},"no":{"q":[12,15,1],"yes":{"out":[561,8]},"no":{"q":[0,3,1],"yes":{"out":[49,1024]},"no":{"out":[561,64]}}}}}}};
return audit(tree);
```

## Control and continuation

X6 native read r2-20261126-r221-x6-task-read SUCCEEDED, NO_CANONICAL_PUBLICATION_DIRECTORY, source 2bfae8ca1fa4512d200d6e331f9a3d2b2279fb7b at 2026-11-26T03:07:29.136047Z. Native owner projection not evaluated; no CLAIM, shared state change, or identity reassignment. Current researcher identity and activity association remain unconfirmed. Next: search six-depth trees with a bounded count of genuine joint observations per path, or certify local infeasibility using the 35-output cover bound; fixed-partition result is a baseline, not an arbitrary-tree optimum. Independent review remains open.
