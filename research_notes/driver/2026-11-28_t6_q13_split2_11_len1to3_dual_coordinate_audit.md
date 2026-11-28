# T6 q13 split(2,11), negative lengths 1–3 — exact dual-coordinate continuation

Original informed Driver lane EM-DVR-DEBB5E; 2026-11-28. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Shared basis verified from 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json blob bcab5ce85b368d2b65a74340ceadb4527da0f01e. Reuses Driver dual-coordinate lemma at cd13961f1ad5ca95a5e1431216f0017e57f00825; not a new novelty claim, not an independent review of own lemma. Independent exact search relative to author GS method; no author field comparison claimed in this unit.

For each positive partition of 2 and negative partition of 11 of lengths 1–3, enumerate labels 1..12 in nondecreasing order inside each equal-q group. High mass is sum(169q+13r-1). Prune a partial roster only if its mass plus minimum remaining mass exceeds 2331. The positive and negative rosters are crossed exhaustively, including common atoms. Low carrier weights 13j-1, six congruences sum u_j/j^k = sum negative (13q+r)^(-k) minus sum positive (13q+r)^(-k) mod 13^k, k=1..6. The prior digit-lift surjectivity proof and det 13^21 establish saturation of U. With alpha=u U^-1, remaining budgets A,Bminus, each coordinate is inside [A*l_i-Bminus*h_i,A*h_i-Bminus*l_i]. Width <1 for all q13, as verified below. Lift atom residues to scaled coordinates mod 13^6; each interval contains at most one compatible coordinate. Reject empty intervals, otherwise restore u and check six congruences and original separate budgets. All operations exact; modular residues and interval endpoints fit in safe JS integers, matrix arithmetic uses BigInt rational. No smoothness needed, no common-atom pruning. Per-pattern counts and recovered vectors preserved below. Not observer implication, H0, lower-prime completion, global T6 or a formal Review/Result/Task completion. No author certificates for these rows independently compared in this turn.

## Executed result
```json
{
  "rows": [
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        9
      ],
      "raw": 73008,
      "search": 73008,
      "common": 19944,
      "box_survivors": 13,
      "valid": 0,
      "rejects": [
        49470,
        15722,
        5156,
        1603,
        620,
        253,
        97,
        42,
        8,
        12,
        10,
        2
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        9
      ],
      "raw": 11232,
      "search": 11232,
      "common": 0,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7481,
        2498,
        788,
        288,
        106,
        33,
        19,
        11,
        4,
        2,
        1,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        2,
        8
      ],
      "raw": 134784,
      "search": 134784,
      "common": 20736,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        91214,
        28967,
        9479,
        3033,
        1215,
        489,
        236,
        76,
        48,
        12,
        4,
        4
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        2,
        8
      ],
      "raw": 20736,
      "search": 20736,
      "common": 1728,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        13842,
        4597,
        1432,
        496,
        230,
        71,
        35,
        20,
        9,
        1,
        0,
        1
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        3,
        7
      ],
      "raw": 134784,
      "search": 134784,
      "common": 20736,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        91103,
        29073,
        9497,
        2970,
        1257,
        523,
        215,
        74,
        41,
        18,
        6,
        4
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        3,
        7
      ],
      "raw": 20736,
      "search": 20736,
      "common": 0,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        13916,
        4420,
        1510,
        530,
        211,
        75,
        41,
        13,
        8,
        4,
        5,
        1
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        4,
        6
      ],
      "raw": 134784,
      "search": 134784,
      "common": 20736,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        91423,
        28924,
        9450,
        2982,
        1186,
        478,
        201,
        83,
        30,
        7,
        10,
        3
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        4,
        6
      ],
      "raw": 20736,
      "search": 20736,
      "common": 0,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        13760,
        4606,
        1484,
        519,
        210,
        90,
        40,
        15,
        6,
        1,
        2,
        1
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        5,
        5
      ],
      "raw": 73008,
      "search": 73008,
      "common": 11232,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        49307,
        15509,
        5232,
        1747,
        694,
        295,
        108,
        73,
        27,
        10,
        0,
        5
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        5,
        5
      ],
      "raw": 11232,
      "search": 11232,
      "common": 0,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        7452,
        2456,
        827,
        295,
        112,
        53,
        19,
        6,
        6,
        2,
        1,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        10
      ],
      "raw": 11232,
      "search": 11232,
      "common": 1728,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        7413,
        2261,
        949,
        406,
        116,
        35,
        13,
        35,
        3,
        1,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        10
      ],
      "raw": 1728,
      "search": 1728,
      "common": 0,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1132,
        344,
        158,
        53,
        23,
        9,
        5,
        2,
        2,
        0,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        2,
        2,
        7
      ],
      "raw": 73008,
      "search": 73008,
      "common": 0,
      "box_survivors": 6,
      "valid": 0,
      "rejects": [
        49698,
        15262,
        5204,
        1715,
        642,
        275,
        120,
        44,
        22,
        14,
        4,
        2
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        2,
        2,
        7
      ],
      "raw": 11232,
      "search": 11232,
      "common": 1728,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        7463,
        2451,
        852,
        269,
        119,
        37,
        25,
        10,
        6,
        0,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        2,
        3,
        6
      ],
      "raw": 134784,
      "search": 134784,
      "common": 0,
      "box_survivors": 8,
      "valid": 0,
      "rejects": [
        91437,
        28764,
        9417,
        3071,
        1213,
        522,
        204,
        78,
        39,
        22,
        7,
        2
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        2,
        3,
        6
      ],
      "raw": 20736,
      "search": 20736,
      "common": 1728,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        13762,
        4546,
        1530,
        478,
        246,
        84,
        45,
        28,
        11,
        4,
        1,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        2,
        4,
        5
      ],
      "raw": 134784,
      "search": 134784,
      "common": 0,
      "box_survivors": 5,
      "valid": 0,
      "rejects": [
        91377,
        28731,
        9479,
        3114,
        1207,
        518,
        206,
        80,
        40,
        17,
        7,
        3
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        2,
        4,
        5
      ],
      "raw": 20736,
      "search": 20736,
      "common": 1728,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        13765,
        4541,
        1520,
        531,
        208,
        98,
        35,
        19,
        9,
        4,
        5,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        2,
        9
      ],
      "raw": 11232,
      "search": 11232,
      "common": 0,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        7437,
        2551,
        797,
        249,
        110,
        54,
        20,
        10,
        4,
        0,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        2,
        9
      ],
      "raw": 1728,
      "search": 1728,
      "common": 144,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1127,
        420,
        111,
        43,
        14,
        10,
        1,
        1,
        0,
        1,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        3,
        3,
        5
      ],
      "raw": 73008,
      "search": 73008,
      "common": 0,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        49544,
        15545,
        5095,
        1725,
        653,
        266,
        107,
        44,
        17,
        5,
        3,
        2
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        3,
        3,
        5
      ],
      "raw": 11232,
      "search": 11232,
      "common": 0,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        7465,
        2451,
        833,
        278,
        119,
        46,
        19,
        11,
        8,
        1,
        1,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        3,
        4,
        4
      ],
      "raw": 73008,
      "search": 73008,
      "common": 0,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        49583,
        15599,
        5062,
        1629,
        656,
        269,
        111,
        47,
        25,
        12,
        11,
        3
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        3,
        4,
        4
      ],
      "raw": 11232,
      "search": 11232,
      "common": 0,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        7486,
        2466,
        798,
        284,
        112,
        46,
        17,
        10,
        10,
        1,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        3,
        8
      ],
      "raw": 11232,
      "search": 11232,
      "common": 0,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7456,
        2443,
        870,
        273,
        115,
        43,
        18,
        8,
        3,
        2,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        3,
        8
      ],
      "raw": 1728,
      "search": 1728,
      "common": 0,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        1123,
        391,
        128,
        54,
        17,
        11,
        1,
        2,
        0,
        0,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        4,
        7
      ],
      "raw": 11232,
      "search": 11232,
      "common": 0,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7383,
        2498,
        838,
        297,
        124,
        54,
        17,
        10,
        5,
        4,
        1,
        0
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        4,
        7
      ],
      "raw": 1728,
      "search": 1728,
      "common": 0,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        1133,
        382,
        138,
        44,
        14,
        11,
        3,
        1,
        0,
        1,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        5,
        6
      ],
      "raw": 11232,
      "search": 11232,
      "common": 0,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        7451,
        2396,
        882,
        281,
        137,
        36,
        25,
        11,
        4,
        3,
        2,
        0
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        5,
        6
      ],
      "raw": 1728,
      "search": 1728,
      "common": 0,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1125,
        376,
        133,
        60,
        17,
        12,
        4,
        1,
        0,
        0,
        0,
        0
      ]
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        11
      ],
      "raw": 936,
      "search": 936,
      "common": 0,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        609,
        206,
        82,
        19,
        13,
        1,
        1,
        2,
        1,
        1,
        0,
        1
      ]
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        11
      ],
      "raw": 144,
      "search": 144,
      "common": 0,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        90,
        35,
        9,
        7,
        1,
        0,
        1,
        0,
        1,
        0,
        0,
        0
      ]
    }
  ],
  "totals": {
    "raw": 1264680,
    "search": 1264680,
    "common": 102168,
    "box_survivors": 75,
    "valid": 0
  },
  "survivors": [
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        1
      ],
      "neg": [
        1,
        2,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5503",
        "4101"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        3,
        12
      ],
      "neg": [
        1,
        2,
        3
      ],
      "u": [
        "201",
        "-1",
        "3",
        "24",
        "-4",
        "-5",
        "-4",
        "21",
        "16",
        "8",
        "1",
        "2"
      ],
      "masses": [
        "9784",
        "2960"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        8
      ],
      "neg": [
        1,
        12,
        8
      ],
      "u": [
        "94",
        "46",
        "5",
        "31",
        "7",
        "25",
        "1",
        "-8",
        "17",
        "3",
        "-2",
        "-2"
      ],
      "masses": [
        "9324",
        "3547"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        2
      ],
      "neg": [
        2,
        2,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5516",
        "4114"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        3
      ],
      "neg": [
        2,
        3,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5529",
        "4127"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        4
      ],
      "neg": [
        2,
        4,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5542",
        "4140"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        5
      ],
      "neg": [
        2,
        5,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5555",
        "4153"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        6
      ],
      "neg": [
        2,
        6,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5568",
        "4166"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        7
      ],
      "neg": [
        2,
        7,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5581",
        "4179"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        8
      ],
      "neg": [
        2,
        8,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5594",
        "4192"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        9
      ],
      "neg": [
        2,
        9,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5607",
        "4205"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        1,
        10
      ],
      "neg": [
        2,
        10,
        3
      ],
      "u": [
        "108",
        "59",
        "22",
        "-19",
        "-2",
        "5",
        "0",
        "-2",
        "-3",
        "-4",
        "7",
        "1"
      ],
      "masses": [
        "5620",
        "4218"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        2,
        2
      ],
      "neg": [
        3,
        5,
        2
      ],
      "u": [
        "96",
        "12",
        "-5",
        "-4",
        "-11",
        "6",
        "-1",
        "0",
        "9",
        "10",
        "4",
        "-4"
      ],
      "masses": [
        "5204",
        "3794"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        1,
        9
      ],
      "pos": [
        6
      ],
      "neg": [
        4,
        10,
        1
      ],
      "u": [
        "36",
        "-35",
        "14",
        "5",
        "-4",
        "7",
        "0",
        "-5",
        "13",
        "-1",
        "5",
        "9"
      ],
      "masses": [
        "5786",
        "3826"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        2,
        8
      ],
      "pos": [
        3,
        8
      ],
      "neg": [
        2,
        3,
        6
      ],
      "u": [
        "81",
        "-30",
        "3",
        "25",
        "-10",
        "7",
        "-17",
        "14",
        "-6",
        "-2",
        "9",
        "1"
      ],
      "masses": [
        "6254",
        "5873"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        2,
        8
      ],
      "pos": [
        1,
        9
      ],
      "neg": [
        2,
        8,
        11
      ],
      "u": [
        "28",
        "-47",
        "5",
        "6",
        "-7",
        "3",
        "-22",
        "-10",
        "1",
        "-12",
        "7",
        "-5"
      ],
      "masses": [
        "2639",
        "9085"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        2,
        8
      ],
      "pos": [
        2,
        2
      ],
      "neg": [
        6,
        5,
        4
      ],
      "u": [
        "-5",
        "4",
        "8",
        "12",
        "14",
        "-2",
        "17",
        "11",
        "-5",
        "-1",
        "-5",
        "5"
      ],
      "masses": [
        "5738",
        "3684"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        2,
        8
      ],
      "pos": [
        5,
        8
      ],
      "neg": [
        6,
        5,
        6
      ],
      "u": [
        "-151",
        "47",
        "13",
        "-7",
        "-2",
        "-2",
        "-6",
        "3",
        "-18",
        "-11",
        "-1",
        "4"
      ],
      "masses": [
        "3103",
        "8717"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        2,
        8
      ],
      "pos": [
        1,
        12
      ],
      "neg": [
        6,
        9,
        5
      ],
      "u": [
        "-74",
        "69",
        "0",
        "-31",
        "-11",
        "-1",
        "-1",
        "-8",
        "6",
        "-11",
        "-3",
        "-4"
      ],
      "masses": [
        "2926",
        "8745"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        2,
        8
      ],
      "pos": [
        1,
        1
      ],
      "neg": [
        8,
        11,
        2
      ],
      "u": [
        "1",
        "23",
        "11",
        "21",
        "21",
        "8",
        "8",
        "9",
        "-1",
        "13",
        "-7",
        "12"
      ],
      "masses": [
        "9582",
        "3239"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        2,
        8
      ],
      "pos": [
        4,
        4
      ],
      "neg": [
        12,
        6,
        1
      ],
      "u": [
        "52",
        "-4",
        "-26",
        "-5",
        "2",
        "-2",
        "3",
        "0",
        "-3",
        "-5",
        "14",
        "-1"
      ],
      "masses": [
        "3450",
        "4748"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        2,
        8
      ],
      "pos": [
        6
      ],
      "neg": [
        3,
        9,
        7
      ],
      "u": [
        "110",
        "14",
        "28",
        "22",
        "7",
        "9",
        "-7",
        "13",
        "-13",
        "11",
        "9",
        "6"
      ],
      "masses": [
        "10378",
        "4241"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        2,
        8
      ],
      "pos": [
        1
      ],
      "neg": [
        11,
        5,
        3
      ],
      "u": [
        "-239",
        "76",
        "18",
        "-32",
        "-21",
        "-18",
        "5",
        "-9",
        "-20",
        "-15",
        "5",
        "-1"
      ],
      "masses": [
        "4094",
        "14670"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        3,
        7
      ],
      "pos": [
        2,
        11
      ],
      "neg": [
        3,
        9,
        6
      ],
      "u": [
        "-36",
        "-24",
        "-40",
        "-8",
        "8",
        "-7",
        "-8",
        "13",
        "-24",
        "-3",
        "14",
        "6"
      ],
      "masses": [
        "5274",
        "9480"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        3,
        7
      ],
      "pos": [
        2,
        10
      ],
      "neg": [
        6,
        4,
        5
      ],
      "u": [
        "-16",
        "-15",
        "-12",
        "1",
        "-2",
        "0",
        "-16",
        "14",
        "-16",
        "16",
        "10",
        "4"
      ],
      "masses": [
        "6089",
        "6498"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        3,
        7
      ],
      "pos": [
        6,
        7
      ],
      "neg": [
        10,
        8,
        4
      ],
      "u": [
        "-89",
        "51",
        "13",
        "33",
        "2",
        "5",
        "-10",
        "6",
        "-16",
        "6",
        "4",
        "-3"
      ],
      "masses": [
        "6430",
        "6431"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        3,
        7
      ],
      "pos": [
        12
      ],
      "neg": [
        7,
        4,
        8
      ],
      "u": [
        "-45",
        "-13",
        "39",
        "6",
        "-38",
        "-5",
        "-12",
        "-3",
        "5",
        "-7",
        "1",
        "-5"
      ],
      "masses": [
        "3003",
        "8852"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        3,
        7
      ],
      "pos": [
        8
      ],
      "neg": [
        7,
        5,
        4
      ],
      "u": [
        "-147",
        "31",
        "11",
        "-24",
        "-12",
        "-14",
        "-8",
        "3",
        "-9",
        "-7",
        "-6",
        "1"
      ],
      "masses": [
        "2098",
        "10417"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        4,
        6
      ],
      "pos": [
        9,
        12
      ],
      "neg": [
        2,
        1,
        10
      ],
      "u": [
        "-22",
        "-11",
        "40",
        "-1",
        "-16",
        "0",
        "-7",
        "1",
        "-3",
        "-1",
        "1",
        "-7"
      ],
      "masses": [
        "2374",
        "5831"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        4,
        6
      ],
      "pos": [
        9,
        10
      ],
      "neg": [
        5,
        3,
        1
      ],
      "u": [
        "-105",
        "10",
        "4",
        "-11",
        "0",
        "11",
        "4",
        "0",
        "-1",
        "-6",
        "1",
        "1"
      ],
      "masses": [
        "2489",
        "4684"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        4,
        6
      ],
      "pos": [
        3,
        9
      ],
      "neg": [
        7,
        8,
        6
      ],
      "u": [
        "-151",
        "83",
        "35",
        "-18",
        "-17",
        "12",
        "-5",
        "-18",
        "-10",
        "-11",
        "9",
        "-7"
      ],
      "masses": [
        "6099",
        "11915"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        4,
        6
      ],
      "pos": [
        3,
        5
      ],
      "neg": [
        7,
        11,
        8
      ],
      "u": [
        "77",
        "1",
        "30",
        "-1",
        "11",
        "-9",
        "1",
        "9",
        "-2",
        "2",
        "-8",
        "0"
      ],
      "masses": [
        "4508",
        "4306"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        4,
        6
      ],
      "pos": [
        4,
        11
      ],
      "neg": [
        9,
        2,
        4
      ],
      "u": [
        "202",
        "-6",
        "42",
        "48",
        "-9",
        "7",
        "8",
        "5",
        "9",
        "8",
        "-1",
        "8"
      ],
      "masses": [
        "12089",
        "2919"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        4,
        6
      ],
      "pos": [
        3,
        5
      ],
      "neg": [
        9,
        7,
        2
      ],
      "u": [
        "-229",
        "32",
        "15",
        "14",
        "-14",
        "8",
        "-6",
        "1",
        "-9",
        "4",
        "1",
        "5"
      ],
      "masses": [
        "4676",
        "7318"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        4,
        6
      ],
      "pos": [
        7,
        7
      ],
      "neg": [
        10,
        7,
        11
      ],
      "u": [
        "-43",
        "50",
        "69",
        "9",
        "3",
        "-1",
        "9",
        "3",
        "-15",
        "11",
        "-4",
        "4"
      ],
      "masses": [
        "8199",
        "5121"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        4,
        6
      ],
      "pos": [
        3
      ],
      "neg": [
        2,
        3,
        11
      ],
      "u": [
        "97",
        "32",
        "31",
        "4",
        "-10",
        "0",
        "-11",
        "9",
        "-15",
        "6",
        "7",
        "6"
      ],
      "masses": [
        "7347",
        "5434"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        4,
        6
      ],
      "pos": [
        12
      ],
      "neg": [
        11,
        6,
        7
      ],
      "u": [
        "89",
        "-32",
        "14",
        "27",
        "-26",
        "6",
        "-13",
        "-2",
        "7",
        "-10",
        "14",
        "-2"
      ],
      "masses": [
        "6732",
        "7608"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        5,
        5
      ],
      "pos": [
        2,
        2
      ],
      "neg": [
        9,
        6,
        8
      ],
      "u": [
        "118",
        "-61",
        "26",
        "13",
        "9",
        "13",
        "2",
        "-4",
        "19",
        "0",
        "-3",
        "2"
      ],
      "masses": [
        "7726",
        "4518"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        5,
        5
      ],
      "pos": [
        1
      ],
      "neg": [
        2,
        8,
        8
      ],
      "u": [
        "-77",
        "46",
        "30",
        "25",
        "15",
        "-1",
        "-7",
        "-2",
        "-4",
        "2",
        "-1",
        "5"
      ],
      "masses": [
        "5908",
        "4533"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        5,
        5
      ],
      "pos": [
        8
      ],
      "neg": [
        7,
        8,
        8
      ],
      "u": [
        "-12",
        "2",
        "-3",
        "0",
        "28",
        "9",
        "5",
        "-3",
        "-10",
        "15",
        "-4",
        "6"
      ],
      "masses": [
        "6291",
        "4450"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        5,
        5
      ],
      "pos": [
        3
      ],
      "neg": [
        9,
        6,
        11
      ],
      "u": [
        "-8",
        "102",
        "-10",
        "-1",
        "17",
        "-7",
        "2",
        "4",
        "-15",
        "4",
        "-7",
        "9"
      ],
      "masses": [
        "6517",
        "5994"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        2,
        7
      ],
      "pos": [
        4,
        11
      ],
      "neg": [
        1,
        3,
        6
      ],
      "u": [
        "-46",
        "-4",
        "33",
        "-17",
        "-16",
        "-2",
        "-4",
        "-5",
        "6",
        "-3",
        "-6",
        "4"
      ],
      "masses": [
        "3101",
        "6797"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        2,
        7
      ],
      "pos": [
        7,
        12
      ],
      "neg": [
        3,
        12,
        7
      ],
      "u": [
        "-40",
        "-17",
        "-11",
        "0",
        "5",
        "-6",
        "5",
        "6",
        "-10",
        "-4",
        "4",
        "-2"
      ],
      "masses": [
        "2539",
        "5913"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        2,
        7
      ],
      "pos": [
        3,
        6
      ],
      "neg": [
        4,
        8,
        2
      ],
      "u": [
        "-197",
        "61",
        "16",
        "10",
        "-7",
        "7",
        "-13",
        "-1",
        "-20",
        "4",
        "2",
        "1"
      ],
      "masses": [
        "4590",
        "8443"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        2,
        7
      ],
      "pos": [
        4,
        12
      ],
      "neg": [
        4,
        8,
        4
      ],
      "u": [
        "-175",
        "8",
        "6",
        "-6",
        "-3",
        "-14",
        "0",
        "3",
        "-8",
        "-9",
        "-2",
        "1"
      ],
      "masses": [
        "1436",
        "8113"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        2,
        7
      ],
      "pos": [
        1,
        8
      ],
      "neg": [
        6,
        9,
        2
      ],
      "u": [
        "-3",
        "95",
        "25",
        "26",
        "22",
        "7",
        "10",
        "0",
        "-25",
        "3",
        "0",
        "3"
      ],
      "masses": [
        "8803",
        "5013"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        2,
        7
      ],
      "pos": [
        2,
        6
      ],
      "neg": [
        9,
        11,
        2
      ],
      "u": [
        "-18",
        "55",
        "56",
        "29",
        "3",
        "6",
        "-3",
        "-6",
        "2",
        "8",
        "-3",
        "2"
      ],
      "masses": [
        "7650",
        "3672"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        3,
        6
      ],
      "pos": [
        1,
        6
      ],
      "neg": [
        4,
        6,
        5
      ],
      "u": [
        "1",
        "7",
        "50",
        "6",
        "-30",
        "-9",
        "-3",
        "3",
        "-1",
        "5",
        "8",
        "5"
      ],
      "masses": [
        "5685",
        "5050"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        3,
        6
      ],
      "pos": [
        1,
        6
      ],
      "neg": [
        5,
        1,
        12
      ],
      "u": [
        "-72",
        "64",
        "3",
        "28",
        "17",
        "1",
        "7",
        "3",
        "-12",
        "3",
        "-4",
        "-4"
      ],
      "masses": [
        "6060",
        "5534"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        3,
        6
      ],
      "pos": [
        2,
        9
      ],
      "neg": [
        5,
        1,
        12
      ],
      "u": [
        "-43",
        "21",
        "11",
        "-6",
        "1",
        "6",
        "-2",
        "-2",
        "-9",
        "1",
        "9",
        "2"
      ],
      "masses": [
        "3665",
        "4342"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        3,
        6
      ],
      "pos": [
        2,
        2
      ],
      "neg": [
        6,
        3,
        7
      ],
      "u": [
        "11",
        "-7",
        "36",
        "-8",
        "5",
        "-4",
        "-1",
        "3",
        "-4",
        "7",
        "-12",
        "8"
      ],
      "masses": [
        "4660",
        "5213"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        3,
        6
      ],
      "pos": [
        5,
        12
      ],
      "neg": [
        7,
        4,
        8
      ],
      "u": [
        "-116",
        "-1",
        "-2",
        "8",
        "6",
        "6",
        "9",
        "1",
        "1",
        "-1",
        "0",
        "0"
      ],
      "masses": [
        "2840",
        "3725"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        3,
        6
      ],
      "pos": [
        9,
        9
      ],
      "neg": [
        7,
        4,
        8
      ],
      "u": [
        "16",
        "-18",
        "-2",
        "2",
        "12",
        "13",
        "2",
        "4",
        "-10",
        "-3",
        "7",
        "1"
      ],
      "masses": [
        "4374",
        "4176"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        3,
        6
      ],
      "pos": [
        11,
        12
      ],
      "neg": [
        11,
        7,
        12
      ],
      "u": [
        "-77",
        "72",
        "-1",
        "9",
        "9",
        "8",
        "-3",
        "2",
        "-4",
        "-1",
        "-5",
        "0"
      ],
      "masses": [
        "4292",
        "4781"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        3,
        6
      ],
      "pos": [
        6,
        9
      ],
      "neg": [
        12,
        1,
        1
      ],
      "u": [
        "65",
        "20",
        "18",
        "-2",
        "0",
        "-14",
        "1",
        "6",
        "-15",
        "-1",
        "-6",
        "-3"
      ],
      "masses": [
        "3203",
        "6404"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        2,
        3,
        6
      ],
      "pos": [
        4
      ],
      "neg": [
        3,
        1,
        1
      ],
      "u": [
        "-253",
        "82",
        "27",
        "-8",
        "-4",
        "9",
        "-9",
        "-7",
        "-31",
        "-4",
        "9",
        "0"
      ],
      "masses": [
        "5436",
        "11264"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        4,
        5
      ],
      "pos": [
        8,
        9
      ],
      "neg": [
        10,
        1,
        4
      ],
      "u": [
        "27",
        "-19",
        "12",
        "37",
        "11",
        "23",
        "-9",
        "4",
        "-6",
        "18",
        "12",
        "2"
      ],
      "masses": [
        "10447",
        "4032"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        4,
        5
      ],
      "pos": [
        1,
        6
      ],
      "neg": [
        10,
        7,
        8
      ],
      "u": [
        "29",
        "-4",
        "29",
        "-8",
        "10",
        "5",
        "-20",
        "6",
        "-1",
        "-4",
        "0",
        "3"
      ],
      "masses": [
        "3985",
        "5121"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        4,
        5
      ],
      "pos": [
        2,
        6
      ],
      "neg": [
        11,
        3,
        5
      ],
      "u": [
        "-90",
        "14",
        "26",
        "8",
        "33",
        "9",
        "3",
        "-5",
        "1",
        "3",
        "-2",
        "1"
      ],
      "masses": [
        "5919",
        "3982"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        4,
        5
      ],
      "pos": [
        1,
        7
      ],
      "neg": [
        12,
        3,
        8
      ],
      "u": [
        "20",
        "-7",
        "30",
        "27",
        "-5",
        "14",
        "-14",
        "13",
        "-1",
        "4",
        "-3",
        "-3"
      ],
      "masses": [
        "6130",
        "4917"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        2,
        4,
        5
      ],
      "pos": [
        4,
        7
      ],
      "neg": [
        12,
        6,
        1
      ],
      "u": [
        "-29",
        "-17",
        "35",
        "10",
        "34",
        "6",
        "-4",
        "5",
        "-16",
        "11",
        "-4",
        "10"
      ],
      "masses": [
        "8441",
        "5660"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        2,
        4,
        5
      ],
      "pos": [
        12
      ],
      "neg": [
        11,
        6,
        2
      ],
      "u": [
        "79",
        "13",
        "-3",
        "12",
        "0",
        "-9",
        "2",
        "11",
        "4",
        "-1",
        "3",
        "3"
      ],
      "masses": [
        "5046",
        "3039"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        3,
        3,
        5
      ],
      "pos": [
        6,
        9
      ],
      "neg": [
        2,
        3,
        1
      ],
      "u": [
        "-3",
        "-4",
        "9",
        "2",
        "-7",
        "14",
        "-9",
        "-19",
        "9",
        "-11",
        "0",
        "-4"
      ],
      "masses": [
        "3097",
        "7324"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        3,
        3,
        5
      ],
      "pos": [
        7,
        7
      ],
      "neg": [
        3,
        11,
        6
      ],
      "u": [
        "-7",
        "18",
        "-15",
        "11",
        "2",
        "19",
        "-14",
        "-11",
        "-7",
        "-2",
        "9",
        "-8"
      ],
      "masses": [
        "4398",
        "7473"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        3,
        4,
        4
      ],
      "pos": [
        2,
        11
      ],
      "neg": [
        2,
        4,
        6
      ],
      "u": [
        "44",
        "16",
        "33",
        "-11",
        "-10",
        "7",
        "-12",
        "-9",
        "13",
        "1",
        "-7",
        "-3"
      ],
      "masses": [
        "4863",
        "6679"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        3,
        4,
        4
      ],
      "pos": [
        5
      ],
      "neg": [
        6,
        4,
        5
      ],
      "u": [
        "-196",
        "23",
        "-16",
        "13",
        "-5",
        "7",
        "-19",
        "6",
        "-17",
        "-10",
        "9",
        "0"
      ],
      "masses": [
        "4075",
        "10303"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        3,
        4,
        4
      ],
      "pos": [
        8
      ],
      "neg": [
        11,
        1,
        6
      ],
      "u": [
        "1",
        "40",
        "46",
        "-11",
        "-7",
        "7",
        "-5",
        "-10",
        "2",
        "-1",
        "5",
        "-7"
      ],
      "masses": [
        "4682",
        "5793"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        3,
        8
      ],
      "pos": [
        3,
        4
      ],
      "neg": [
        1,
        1
      ],
      "u": [
        "-153",
        "-8",
        "23",
        "-12",
        "-18",
        "-4",
        "-3",
        "-10",
        "-3",
        "-8",
        "-4",
        "2"
      ],
      "masses": [
        "1611",
        "9239"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        3,
        8
      ],
      "pos": [
        2
      ],
      "neg": [
        7,
        10
      ],
      "u": [
        "-121",
        "84",
        "39",
        "25",
        "-1",
        "2",
        "8",
        "-4",
        "-10",
        "-1",
        "2",
        "4"
      ],
      "masses": [
        "6998",
        "5295"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        4,
        7
      ],
      "pos": [
        2,
        10
      ],
      "neg": [
        6,
        4
      ],
      "u": [
        "-50",
        "26",
        "35",
        "16",
        "0",
        "-3",
        "-8",
        "-9",
        "-13",
        "-3",
        "10",
        "5"
      ],
      "masses": [
        "5483",
        "6360"
      ],
      "valid": false
    },
    {
      "pp": [
        2
      ],
      "np": [
        4,
        7
      ],
      "pos": [
        10
      ],
      "neg": [
        5,
        6
      ],
      "u": [
        "-123",
        "3",
        "5",
        "25",
        "-16",
        "15",
        "-29",
        "1",
        "8",
        "0",
        "0",
        "-9"
      ],
      "masses": [
        "4193",
        "8505"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        5,
        6
      ],
      "pos": [
        4,
        5
      ],
      "neg": [
        4,
        3
      ],
      "u": [
        "55",
        "-21",
        "-1",
        "32",
        "-3",
        "13",
        "-8",
        "-3",
        "9",
        "-8",
        "12",
        "-4"
      ],
      "masses": [
        "6494",
        "5384"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        5,
        6
      ],
      "pos": [
        2,
        2
      ],
      "neg": [
        4,
        9
      ],
      "u": [
        "-54",
        "45",
        "13",
        "13",
        "21",
        "7",
        "-8",
        "1",
        "-12",
        "-5",
        "0",
        "-2"
      ],
      "masses": [
        "4656",
        "5741"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        5,
        6
      ],
      "pos": [
        5,
        5
      ],
      "neg": [
        10,
        3
      ],
      "u": [
        "66",
        "12",
        "43",
        "-2",
        "-6",
        "4",
        "0",
        "0",
        "-17",
        "-7",
        "8",
        "4"
      ],
      "masses": [
        "5256",
        "5387"
      ],
      "valid": false
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        5,
        6
      ],
      "pos": [
        2,
        3
      ],
      "neg": [
        12,
        4
      ],
      "u": [
        "52",
        "16",
        "28",
        "-11",
        "-16",
        "-14",
        "28",
        "4",
        "-8",
        "-5",
        "1",
        "4"
      ],
      "masses": [
        "6183",
        "6301"
      ],
      "valid": false
    }
  ],
  "width": "498515831/736645312",
  "det": "247064529073450392704413",
  "coordinate_order": [
    11,
    10,
    5,
    0,
    4,
    6,
    8,
    7,
    2,
    3,
    9,
    1
  ]
}
```

## Reproduction
Load U from pinned basis file above; run audit(U).
```js
function audit(U0){
const P=13n,B=P**6n,N=12,C=2331,BN=Number(B);
const abs=a=>a<0n?-a:a,mod=(a,m)=>(a%m+m)%m,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a};
const f=(a,b=1n)=>{if(!b)throw Error("division");if(b<0n){a=-a;b=-b}let d=gcd(a,b);return [a/d,b/d]},add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),lt=(a,b)=>a[0]*b[1]<b[0]*a[1],floor=(a,b)=>a/b-(a<0n&&a%b?1n:0n),ceil=(a,b)=>-floor(-a,b);
const inv=(a,m)=>{let b=m,x=1n,y=0n;a=mod(a,m);while(b){let q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y]}if(a!==1n)throw Error("unit");return mod(x,m)};
const H=Array.from({length:6},(_,k)=>Array.from({length:N},(_,i)=>inv(BigInt(i+1)**BigInt(k+1),P**BigInt(k+1))));
const U=U0.map(r=>r.map(BigInt)),W=Array.from({length:N},(_,i)=>P*BigInt(i+1)-1n);
const check=(v,t)=>H.every((h,k)=>mod(h.reduce((s,a,i)=>s+a*v[i],0n)-t[k],P**BigInt(k+1))===0n);
for(let u of U)if(!check(u,Array(6).fill(0n)))throw Error("kernel");
let A=U.map((r,i)=>[...r.map(x=>f(x)),...Array.from({length:N},(_,j)=>f(BigInt(i===j)))]),det=f(1n);
for(let i=0;i<N;i++){let j=A.findIndex((r,k)=>k>=i&&r[i][0]);if(j<0)throw Error("singular");if(i!==j){[A[i],A[j]]=[A[j],A[i]];det=mul(det,f(-1n))}let p=A[i][i];det=mul(det,p);A[i]=A[i].map(x=>div(x,p));for(let j=0;j<N;j++)if(j!==i){let c=A[j][i];A[j]=A[j].map((x,k)=>sub(x,mul(c,A[i][k])))}}
if(det[1]!==1n||abs(det[0])!==P**21n)throw Error("det");
const UI=A.map(r=>r.slice(N)),D=UI.map(r=>r.map(x=>{let z=mul(x,f(B));if(z[1]!==1n)throw Error("denom");return z[0]}));
function lift(t){let x=Array(N).fill(0n);for(let j=0;j<6;j++){let q=P**BigInt(j),m=6-j;let a=H.slice(j).map((h,k)=>{let d=t[j+k]-h.reduce((s,v,i)=>s+v*x[i],0n);if(d%q)throw Error("lift residue");return [...h.slice(0,m).map(v=>mod(v,P)),mod(d/q,P)]});for(let k=0;k<m;k++){let l=a.findIndex((r,i)=>i>=k&&r[k]);if(l<0)throw Error("rank");[a[k],a[l]]=[a[l],a[k]];let s=inv(a[k][k],P);a[k]=a[k].map(v=>mod(v*s,P));for(let i=0;i<m;i++)if(i!==k){let c=a[i][k];a[i]=a[i].map((v,h)=>mod(v-c*a[k][h],P))}}for(let i=0;i<m;i++)x[i]+=q*a[i][m]}if(!check(x,t))throw Error("lift check");return x}
const coords=new Map(),targets=new Map();for(let q=1;q<=11;q++)for(let r=1;r<=12;r++){let t=Array.from({length:6},(_,k)=>inv(BigInt(13*q+r)**BigInt(k+1),P**BigInt(k+1)));targets.set(q*100+r,t);let x=lift(t);coords.set(q*100+r,Array.from({length:N},(_,i)=>Number(mod(x.reduce((a,v,j)=>a+v*D[j][i],0n),B))))}
const bounds=Array.from({length:N},(_,i)=>{let g=UI.map((r,j)=>div(r[i],f(W[j]))),lo=g.reduce((a,b)=>lt(a,b)?a:b,f(0n)),hi=g.reduce((a,b)=>lt(a,b)?b:a,f(0n));return {i,lo,hi,width:sub(hi,lo)}}).sort((a,b)=>lt(a.width,b.width)?-1:lt(b.width,a.width)?1:0);
const width=mul(bounds.at(-1).width,f(2453n));if(!lt(width,f(1n)))throw Error("width");
const cache=new Map();
function box(mp,mn){let key=mp*3000+mn;if(cache.has(key))return cache.get(key);let ap=f(BigInt(C-mp)),am=f(BigInt(C-mn)),arr=bounds.map(({i,lo,hi})=>{let l=mul(f(B),sub(mul(ap,lo),mul(am,hi))),h=mul(f(B),sub(mul(ap,hi),mul(am,lo)));let low=Number(ceil(l[0],l[1])),high=Number(floor(h[0],h[1]));if(low>0||high<0||high-low>=BN)throw Error("box");return {i,low,high}});cache.set(key,arr);return arr}
function* parts(n,lo=1){if(!n){yield [];return}for(let q=lo;q<=n;q++)for(let r of parts(n-q,q))yield [q,...r]}
function roster(pat){let out=[],v=Array(N).fill(0),rs=[];function go(i,m){if(i===pat.length){out.push({m,rs:rs.slice(),v:v.slice()});return}let start=i&&pat[i]===pat[i-1]?rs[i-1]:1;for(let r=start;r<=12;r++){let cost=169*pat[i]+13*r-1;if(m+cost+pat.slice(i+1).reduce((s,q)=>s+169*q+12,0)>C)break;let a=coords.get(pat[i]*100+r);rs.push(r);for(let k=0;k<N;k++)v[k]=(v[k]+a[k])%BN;go(i+1,m+cost);for(let k=0;k<N;k++)v[k]=(v[k]-a[k]+BN)%BN;rs.pop()}}go(0,0);return out}
function raw(pat){let counts={};for(let q of pat)counts[q]=(counts[q]??0)+1;let p=1;for(let k of Object.values(counts)){let c=1;for(let j=1;j<=k;j++)c=c*(12+j-1)/j;p*=c}if(!Number.isSafeInteger(p))throw Error("raw");return p}
let rows=[],survivors=[];
for(let np of [...parts(11)].filter(p=>p.length<=3)){let neg=roster(np);for(let pp of parts(2)){let pos=roster(pp),row={pos_pattern:pp,neg_pattern:np,raw:raw(pp)*raw(np),search:pos.length*neg.length,common:0,box_survivors:0,valid:0,rejects:Array(N).fill(0)};
for(let n of neg)for(let p of pos){if(pp.some((q,i)=>np.some((q2,j)=>q===q2&&p.rs[i]===n.rs[j])))row.common++;let z=Array(N),ok=true,bs=box(p.m,n.m);for(let j=0;j<N;j++){let {i,low,high}=bs[j],c=(n.v[i]-p.v[i]+BN)%BN;if(c<=high)z[i]=c;else if(c-BN>=low)z[i]=c-BN;else{row.rejects[j]++;ok=false;break}}if(!ok)continue;row.box_survivors++;
let u=Array.from({length:N},(_,j)=>{let x=z.reduce((s,v,k)=>s+BigInt(v)*U[k][j],0n);if(x%B)throw Error("integrality");return x/B});
let rhs=Array.from({length:6},(_,k)=>n.rs.reduce((s,r,j)=>s+targets.get(np[j]*100+r)[k],0n)-p.rs.reduce((s,r,j)=>s+targets.get(pp[j]*100+r)[k],0n));if(!check(u,rhs))throw Error("congruences");
let mp=BigInt(p.m)+u.reduce((s,v,j)=>s+(v>0n?v*W[j]:0n),0n),mn=BigInt(n.m)+u.reduce((s,v,j)=>s+(v<0n?-v*W[j]:0n),0n);let valid=mp<=BigInt(C)&&mn<=BigInt(C);if(valid)row.valid++;survivors.push({pp,np,pos:p.rs,neg:n.rs,u:u.map(String),masses:[String(mp),String(mn)],valid})}
if(row.rejects.reduce((a,b)=>a+b,0)+row.box_survivors!==row.search)throw Error("coverage");rows.push(row)}}
return {rows,totals:Object.fromEntries(["raw","search","common","box_survivors","valid"].map(k=>[k,rows.reduce((s,r)=>s+r[k],0)])),survivors,width:width.join("/"),det:abs(det[0]).toString(),coordinate_order:bounds.map(b=>b.i)}
}
```
