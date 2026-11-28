# T6 q13 split(5,8) negative lengths 1–3 — exact modular interval join

Informed Driver continuation, EM-DVR-DEBB5E; frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Original alternate solver pinned at 0f5415ae2ef3e91852500912e71549b2e6285a51:research_notes/driver/2026-11-28_t6_q13_split4_9_len1to3_modular_interval_join.md (blob eb2e7cd92fd6ef9ab4ccd74e5639e5a276810c0c). Basis pinned 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json (blob bcab5ce85b368d2b65a74340ceadb4527da0f01e). Existing author-side coverage/fiber audit 5eacc4e8e68275f7c923f5e3c3ee9c901103bf11:research_checks/T6_P13_Q13_SPLIT5_8_LEN1_3_COVERAGE_FIBER_AUDIT_20261128.json explicitly does not replay lattice search. This alternate exact computation adds independent solver execution, not a clean independent review of Driver's own method. Common atoms retained; relaxed model, separate signed budget 2331, six mixed congruences. Exact interval uniqueness and saturated kernel proof previously established at cd13961f1ad5ca95a5e1431216f0017e57f00825. All 7 positive partitions of 5 crossed with 10 negative partitions of 8 of lengths <=3. All recovered vectors checked by original congruences and signed budgets. H0, observation-envelope sufficiency, lower-prime completion, mother T6=2332 open.

## Executed results
```json
{
  "rows": [
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        6
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1155484,
      "box_survivors": 41,
      "valid": 0,
      "rejects": [
        2932964,
        814297,
        233519,
        69151,
        23905,
        9412,
        3226,
        1184,
        444,
        225,
        55,
        25
      ],
      "minMaxBudgetExcess": 1725
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        1,
        1,
        6
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1208291,
      "box_survivors": 69,
      "valid": 0,
      "rejects": [
        2880157,
        836967,
        249968,
        76504,
        27838,
        10330,
        4025,
        1481,
        690,
        258,
        125,
        36
      ],
      "minMaxBudgetExcess": 1972
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        1,
        1,
        6
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 270673,
      "box_survivors": 37,
      "valid": 0,
      "rejects": [
        605423,
        183328,
        57912,
        17821,
        6915,
        2791,
        1080,
        493,
        162,
        95,
        27,
        12
      ],
      "minMaxBudgetExcess": 1991
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        1,
        1,
        6
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 270380,
      "box_survivors": 36,
      "valid": 0,
      "rejects": [
        605716,
        182999,
        57953,
        18254,
        6745,
        2665,
        987,
        410,
        197,
        93,
        23,
        18
      ],
      "minMaxBudgetExcess": 1673
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        1,
        1,
        6
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43454,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        91330,
        29028,
        9317,
        3002,
        1265,
        505,
        185,
        67,
        58,
        13,
        4,
        7
      ],
      "minMaxBudgetExcess": 3169
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        1,
        1,
        6
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43412,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        91372,
        28823,
        9547,
        3021,
        1163,
        521,
        189,
        86,
        32,
        19,
        8,
        2
      ],
      "minMaxBudgetExcess": 5445
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        1,
        1,
        6
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3754,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7478,
        2371,
        877,
        284,
        137,
        47,
        20,
        11,
        2,
        3,
        1,
        0
      ],
      "minMaxBudgetExcess": 4699
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        2,
        5
      ],
      "raw": 7547904,
      "search": 7547904,
      "index_pass": 2133740,
      "box_survivors": 86,
      "valid": 0,
      "rejects": [
        5414164,
        1504710,
        432995,
        127106,
        43248,
        15945,
        5864,
        2285,
        999,
        320,
        123,
        59
      ],
      "minMaxBudgetExcess": 1531
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        1,
        2,
        5
      ],
      "raw": 7547904,
      "search": 7547904,
      "index_pass": 2231678,
      "box_survivors": 141,
      "valid": 0,
      "rejects": [
        5316226,
        1548533,
        460015,
        140733,
        50624,
        19377,
        7371,
        2892,
        1230,
        477,
        182,
        103
      ],
      "minMaxBudgetExcess": 1224
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        1,
        2,
        5
      ],
      "raw": 1617408,
      "search": 1617408,
      "index_pass": 498810,
      "box_survivors": 44,
      "valid": 0,
      "rejects": [
        1118598,
        338810,
        105807,
        33285,
        12587,
        5039,
        1873,
        749,
        350,
        139,
        70,
        57
      ],
      "minMaxBudgetExcess": 2294
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        1,
        2,
        5
      ],
      "raw": 1617408,
      "search": 1617408,
      "index_pass": 500442,
      "box_survivors": 33,
      "valid": 0,
      "rejects": [
        1116966,
        341158,
        105402,
        33415,
        12300,
        4865,
        1933,
        759,
        367,
        130,
        59,
        21
      ],
      "minMaxBudgetExcess": 2075
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        1,
        2,
        5
      ],
      "raw": 248832,
      "search": 248832,
      "index_pass": 79825,
      "box_survivors": 8,
      "valid": 0,
      "rejects": [
        169007,
        53470,
        16987,
        5615,
        2158,
        929,
        371,
        164,
        90,
        20,
        9,
        4
      ],
      "minMaxBudgetExcess": 2196
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        1,
        2,
        5
      ],
      "raw": 248832,
      "search": 248832,
      "index_pass": 80516,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        168316,
        53775,
        17334,
        5563,
        2245,
        956,
        355,
        167,
        72,
        27,
        11,
        4
      ],
      "minMaxBudgetExcess": 3052
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        1,
        2,
        5
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6975,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        13761,
        4439,
        1591,
        567,
        183,
        96,
        58,
        24,
        9,
        4,
        1,
        1
      ],
      "minMaxBudgetExcess": 3017
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        3,
        4
      ],
      "raw": 7547904,
      "search": 7547904,
      "index_pass": 2131996,
      "box_survivors": 64,
      "valid": 0,
      "rejects": [
        5415908,
        1500761,
        433584,
        127389,
        44344,
        16395,
        5719,
        2289,
        900,
        353,
        133,
        65
      ],
      "minMaxBudgetExcess": 1782
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        1,
        3,
        4
      ],
      "raw": 7547904,
      "search": 7547904,
      "index_pass": 2234330,
      "box_survivors": 98,
      "valid": 0,
      "rejects": [
        5313574,
        1543502,
        466091,
        141167,
        51685,
        19603,
        7306,
        2854,
        1218,
        499,
        207,
        100
      ],
      "minMaxBudgetExcess": 1818
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        1,
        3,
        4
      ],
      "raw": 1617408,
      "search": 1617408,
      "index_pass": 499697,
      "box_survivors": 46,
      "valid": 0,
      "rejects": [
        1117711,
        337663,
        107347,
        33704,
        12703,
        4735,
        2123,
        790,
        339,
        132,
        93,
        22
      ],
      "minMaxBudgetExcess": 1495
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        1,
        3,
        4
      ],
      "raw": 1617408,
      "search": 1617408,
      "index_pass": 498624,
      "box_survivors": 66,
      "valid": 0,
      "rejects": [
        1118784,
        337491,
        106748,
        33699,
        12345,
        5023,
        1939,
        758,
        300,
        173,
        52,
        30
      ],
      "minMaxBudgetExcess": 2428
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        1,
        3,
        4
      ],
      "raw": 248832,
      "search": 248832,
      "index_pass": 80290,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        168542,
        53422,
        17344,
        5602,
        2296,
        991,
        365,
        150,
        72,
        26,
        12,
        6
      ],
      "minMaxBudgetExcess": 3615
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        1,
        3,
        4
      ],
      "raw": 248832,
      "search": 248832,
      "index_pass": 79824,
      "box_survivors": 15,
      "valid": 0,
      "rejects": [
        169008,
        52880,
        17486,
        5706,
        2170,
        860,
        402,
        167,
        89,
        28,
        15,
        6
      ],
      "minMaxBudgetExcess": 2360
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        1,
        3,
        4
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6948,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        13788,
        4514,
        1545,
        503,
        207,
        97,
        48,
        21,
        4,
        5,
        1,
        0
      ],
      "minMaxBudgetExcess": 5652
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        7
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 185880,
      "box_survivors": 6,
      "valid": 0,
      "rejects": [
        443112,
        128179,
        38841,
        11726,
        4471,
        1656,
        626,
        228,
        101,
        32,
        11,
        3
      ],
      "minMaxBudgetExcess": 3775
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        1,
        7
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 194266,
      "box_survivors": 40,
      "valid": 0,
      "rejects": [
        434726,
        132746,
        40556,
        12861,
        4911,
        1914,
        735,
        297,
        134,
        45,
        20,
        7
      ],
      "minMaxBudgetExcess": 1368
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        1,
        7
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43546,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        91238,
        29018,
        9419,
        2970,
        1214,
        543,
        197,
        84,
        42,
        39,
        11,
        2
      ],
      "minMaxBudgetExcess": 3380
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        1,
        7
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43400,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        91384,
        29153,
        9281,
        3004,
        1127,
        494,
        187,
        89,
        31,
        24,
        4,
        2
      ],
      "minMaxBudgetExcess": 4657
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        1,
        7
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 7036,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        13700,
        4616,
        1469,
        526,
        257,
        88,
        41,
        26,
        6,
        2,
        2,
        1
      ],
      "minMaxBudgetExcess": 6576
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        1,
        7
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6948,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        13788,
        4541,
        1506,
        530,
        209,
        98,
        36,
        13,
        10,
        2,
        2,
        1
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        1,
        7
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 590,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1138,
        361,
        134,
        53,
        26,
        10,
        5,
        0,
        1,
        0,
        0,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        2,
        2,
        4
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1155320,
      "box_survivors": 41,
      "valid": 0,
      "rejects": [
        2933128,
        814131,
        234767,
        68882,
        23805,
        8682,
        3129,
        1105,
        485,
        183,
        75,
        35
      ],
      "minMaxBudgetExcess": 2042
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        2,
        2,
        4
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1208001,
      "box_survivors": 36,
      "valid": 0,
      "rejects": [
        2880447,
        834097,
        251968,
        76778,
        27732,
        10693,
        4128,
        1521,
        650,
        261,
        80,
        57
      ],
      "minMaxBudgetExcess": 2114
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        2,
        2,
        4
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 270813,
      "box_survivors": 24,
      "valid": 0,
      "rejects": [
        605283,
        183175,
        58034,
        18254,
        6768,
        2732,
        1063,
        440,
        171,
        93,
        37,
        22
      ],
      "minMaxBudgetExcess": 1672
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        2,
        2,
        4
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 270395,
      "box_survivors": 31,
      "valid": 0,
      "rejects": [
        605701,
        182357,
        58269,
        18156,
        7038,
        2776,
        1091,
        341,
        178,
        102,
        31,
        25
      ],
      "minMaxBudgetExcess": 2572
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        2,
        2,
        4
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43596,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        91188,
        28831,
        9524,
        3086,
        1283,
        476,
        216,
        116,
        39,
        16,
        3,
        2
      ],
      "minMaxBudgetExcess": 3326
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        2,
        2,
        4
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43671,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        91113,
        28960,
        9467,
        3135,
        1206,
        557,
        204,
        68,
        30,
        35,
        6,
        2
      ],
      "minMaxBudgetExcess": 3372
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        2,
        2,
        4
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3769,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        7463,
        2441,
        873,
        266,
        110,
        44,
        21,
        5,
        5,
        2,
        0,
        0
      ],
      "minMaxBudgetExcess": 4185
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        2,
        3,
        3
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1155182,
      "box_survivors": 41,
      "valid": 0,
      "rejects": [
        2933266,
        813344,
        234818,
        69076,
        23827,
        8885,
        3229,
        1136,
        513,
        202,
        87,
        24
      ],
      "minMaxBudgetExcess": 1155
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        2,
        3,
        3
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1208239,
      "box_survivors": 62,
      "valid": 0,
      "rejects": [
        2880209,
        835062,
        251815,
        76528,
        27738,
        10350,
        4117,
        1574,
        577,
        262,
        94,
        60
      ],
      "minMaxBudgetExcess": 1760
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        2,
        3,
        3
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 270659,
      "box_survivors": 17,
      "valid": 0,
      "rejects": [
        605437,
        182950,
        57845,
        18493,
        6883,
        2800,
        977,
        390,
        167,
        88,
        30,
        19
      ],
      "minMaxBudgetExcess": 2235
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        2,
        3,
        3
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 271470,
      "box_survivors": 33,
      "valid": 0,
      "rejects": [
        604626,
        183747,
        58103,
        18482,
        6684,
        2718,
        989,
        431,
        167,
        59,
        42,
        15
      ],
      "minMaxBudgetExcess": 2444
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        2,
        3,
        3
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43388,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        91396,
        28835,
        9455,
        3026,
        1222,
        490,
        194,
        81,
        45,
        25,
        7,
        1
      ],
      "minMaxBudgetExcess": 1533
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        2,
        3,
        3
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43492,
      "box_survivors": 6,
      "valid": 0,
      "rejects": [
        91292,
        28887,
        9404,
        3124,
        1160,
        517,
        234,
        99,
        33,
        14,
        9,
        5
      ],
      "minMaxBudgetExcess": 7268
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        2,
        3,
        3
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3764,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        7468,
        2410,
        836,
        328,
        103,
        51,
        21,
        11,
        0,
        2,
        1,
        1
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        2,
        6
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 186093,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        442899,
        128870,
        38394,
        11881,
        4326,
        1624,
        589,
        231,
        111,
        37,
        17,
        10
      ],
      "minMaxBudgetExcess": 2927
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        2,
        6
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 194268,
      "box_survivors": 18,
      "valid": 0,
      "rejects": [
        434724,
        132572,
        40842,
        12614,
        4947,
        1973,
        784,
        306,
        125,
        53,
        23,
        11
      ],
      "minMaxBudgetExcess": 3040
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        2,
        6
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43484,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        91300,
        28929,
        9475,
        3040,
        1170,
        494,
        227,
        86,
        31,
        15,
        7,
        6
      ],
      "minMaxBudgetExcess": 2691
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        2,
        6
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 42935,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        91849,
        28790,
        9174,
        3029,
        1170,
        420,
        189,
        88,
        39,
        19,
        6,
        10
      ],
      "minMaxBudgetExcess": 10480
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        2,
        6
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 7019,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        13717,
        4575,
        1561,
        510,
        208,
        85,
        49,
        20,
        7,
        0,
        4,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        2,
        6
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6984,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        13752,
        4558,
        1573,
        479,
        232,
        81,
        35,
        13,
        9,
        3,
        0,
        1
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        2,
        6
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 597,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1131,
        381,
        128,
        49,
        27,
        5,
        3,
        3,
        1,
        0,
        0,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        3,
        5
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 186146,
      "box_survivors": 11,
      "valid": 0,
      "rejects": [
        442846,
        128660,
        38865,
        11680,
        4242,
        1659,
        612,
        256,
        104,
        31,
        18,
        8
      ],
      "minMaxBudgetExcess": 3016
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        3,
        5
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 194121,
      "box_survivors": 12,
      "valid": 0,
      "rejects": [
        434871,
        131435,
        41453,
        12909,
        4947,
        2046,
        800,
        310,
        126,
        54,
        17,
        12
      ],
      "minMaxBudgetExcess": 2464
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        3,
        5
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43410,
      "box_survivors": 6,
      "valid": 0,
      "rejects": [
        91374,
        28758,
        9478,
        3155,
        1137,
        504,
        210,
        94,
        40,
        16,
        4,
        8
      ],
      "minMaxBudgetExcess": 2685
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        3,
        5
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43453,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        91331,
        28907,
        9406,
        3045,
        1207,
        507,
        226,
        77,
        40,
        16,
        14,
        5
      ],
      "minMaxBudgetExcess": 3837
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        3,
        5
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6979,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        13757,
        4544,
        1530,
        509,
        233,
        87,
        39,
        17,
        11,
        4,
        3,
        2
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        3,
        5
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6993,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        13743,
        4543,
        1513,
        560,
        211,
        82,
        55,
        18,
        6,
        3,
        2,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        3,
        5
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 600,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1128,
        404,
        125,
        37,
        18,
        9,
        5,
        1,
        1,
        0,
        0,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        4,
        4
      ],
      "raw": 340704,
      "search": 340704,
      "index_pass": 100684,
      "box_survivors": 8,
      "valid": 0,
      "rejects": [
        240020,
        69450,
        20964,
        6532,
        2298,
        879,
        317,
        138,
        57,
        26,
        9,
        6
      ],
      "minMaxBudgetExcess": 3615
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        4,
        4
      ],
      "raw": 340704,
      "search": 340704,
      "index_pass": 105551,
      "box_survivors": 9,
      "valid": 0,
      "rejects": [
        235153,
        71473,
        22409,
        7157,
        2725,
        1075,
        430,
        159,
        67,
        31,
        10,
        6
      ],
      "minMaxBudgetExcess": 3398
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        4,
        4
      ],
      "raw": 73008,
      "search": 73008,
      "index_pass": 23527,
      "box_survivors": 6,
      "valid": 0,
      "rejects": [
        49481,
        15597,
        5087,
        1710,
        664,
        272,
        119,
        44,
        17,
        6,
        5,
        0
      ],
      "minMaxBudgetExcess": 3607
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        4,
        4
      ],
      "raw": 73008,
      "search": 73008,
      "index_pass": 23399,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        49609,
        15571,
        5085,
        1659,
        661,
        235,
        110,
        44,
        14,
        13,
        3,
        4
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        4,
        4
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3797,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7435,
        2387,
        865,
        304,
        157,
        46,
        26,
        7,
        3,
        0,
        1,
        0
      ],
      "minMaxBudgetExcess": 6921
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        4,
        4
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3737,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7495,
        2394,
        831,
        309,
        104,
        55,
        21,
        12,
        8,
        2,
        0,
        0
      ],
      "minMaxBudgetExcess": 4123
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        4,
        4
      ],
      "raw": 936,
      "search": 936,
      "index_pass": 322,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        614,
        212,
        61,
        28,
        12,
        5,
        2,
        0,
        2,
        0,
        0,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        8
      ],
      "raw": 52416,
      "search": 52416,
      "index_pass": 16256,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        36160,
        10994,
        3465,
        1102,
        397,
        166,
        84,
        21,
        16,
        6,
        2,
        1
      ],
      "minMaxBudgetExcess": 3655
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        2
      ],
      "neg_pattern": [
        8
      ],
      "raw": 52416,
      "search": 52416,
      "index_pass": 16861,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        35555,
        11297,
        3575,
        1204,
        460,
        189,
        75,
        35,
        15,
        6,
        1,
        2
      ],
      "minMaxBudgetExcess": 3489
    },
    {
      "pos_pattern": [
        1,
        1,
        3
      ],
      "neg_pattern": [
        8
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3742,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7490,
        2465,
        799,
        284,
        117,
        37,
        21,
        11,
        2,
        2,
        1,
        2
      ],
      "minMaxBudgetExcess": 5105
    },
    {
      "pos_pattern": [
        1,
        2,
        2
      ],
      "neg_pattern": [
        8
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3797,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        7435,
        2552,
        792,
        279,
        96,
        43,
        24,
        8,
        3,
        0,
        0,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        4
      ],
      "neg_pattern": [
        8
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 600,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1128,
        384,
        131,
        55,
        19,
        4,
        5,
        0,
        1,
        0,
        1,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        2,
        3
      ],
      "neg_pattern": [
        8
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 603,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1125,
        399,
        127,
        43,
        21,
        7,
        3,
        2,
        0,
        0,
        0,
        1
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        5
      ],
      "neg_pattern": [
        8
      ],
      "raw": 144,
      "search": 144,
      "index_pass": 54,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        90,
        28,
        17,
        5,
        3,
        1,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "minMaxBudgetExcess": null
    }
  ],
  "totals": {
    "raw": 74021688,
    "search": 74021688,
    "index_pass": 21798580,
    "box_survivors": 1257,
    "valid": 0
  },
  "minExcess": 1155,
  "minWitness": {
    "pp": [
      1,
      1,
      1,
      1,
      1
    ],
    "np": [
      2,
      3,
      3
    ],
    "pos": [
      4,
      7,
      10,
      10,
      10
    ],
    "neg": [
      9,
      2,
      10
    ],
    "u": [
      "-11",
      "-12",
      "-15",
      "-3",
      "17",
      "1",
      "1",
      "-1",
      "-3",
      "-2",
      "1",
      "0"
    ],
    "masses": [
      "2770",
      "3486"
    ],
    "excess": 1155
  },
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

## Reproduce
Load U from pinned basis and call audit(U,3). Only split constants adapted.
```js
function audit(U0, maxLen=3){
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
const coords=new Map(),targets=new Map();for(let q=1;q<=9;q++)for(let r=1;r<=12;r++){let t=Array.from({length:6},(_,k)=>inv(BigInt(13*q+r)**BigInt(k+1),P**BigInt(k+1)));targets.set(q*100+r,t);let x=lift(t);coords.set(q*100+r,Array.from({length:N},(_,i)=>Number(mod(x.reduce((a,v,j)=>a+v*D[j][i],0n),B))))}
const bounds=Array.from({length:N},(_,i)=>{let g=UI.map((r,j)=>div(r[i],f(W[j]))),lo=g.reduce((a,b)=>lt(a,b)?a:b,f(0n)),hi=g.reduce((a,b)=>lt(a,b)?b:a,f(0n));return {i,lo,hi,width:sub(hi,lo)}}).sort((a,b)=>lt(a.width,b.width)?-1:lt(b.width,a.width)?1:0);
const width=mul(bounds.at(-1).width,f(2453n));if(!lt(width,f(1n)))throw Error("width");
const cache=new Map(),i0=bounds[0].i;
function box(mp,mn){let key=mp*3000+mn;if(cache.has(key))return cache.get(key);let ap=f(BigInt(C-mp)),am=f(BigInt(C-mn)),arr=bounds.map(({i,lo,hi})=>{let l=mul(f(B),sub(mul(ap,lo),mul(am,hi))),h=mul(f(B),sub(mul(ap,hi),mul(am,lo)));let low=Number(ceil(l[0],l[1])),high=Number(floor(h[0],h[1]));if(low>0||high<0||high-low>=BN)throw Error("box");return {i,low,high}});cache.set(key,arr);return arr}
function* parts(n,lo=1){if(!n){yield [];return}for(let q=lo;q<=n;q++)for(let r of parts(n-q,q))yield [q,...r]}
function roster(pat){let out=[],v=Array(N).fill(0),rs=[];const tail=Array(pat.length+1).fill(0);for(let i=pat.length-1;i>=0;i--)tail[i]=tail[i+1]+169*pat[i]+12;function go(i,m){if(i===pat.length){out.push({m,rs:rs.slice(),v:v.slice()});return}let start=i&&pat[i]===pat[i-1]?rs[i-1]:1;for(let r=start;r<=12;r++){let cost=169*pat[i]+13*r-1;if(m+cost+tail[i+1]>C)break;let a=coords.get(pat[i]*100+r);rs.push(r);for(let k=0;k<N;k++)v[k]=(v[k]+a[k])%BN;go(i+1,m+cost);for(let k=0;k<N;k++)v[k]=(v[k]-a[k]+BN)%BN;rs.pop()}}go(0,0);return out}
function raw(pat){let counts={};for(let q of pat)counts[q]=(counts[q]??0)+1;let p=1;for(let k of Object.values(counts)){let c=1;for(let j=1;j<=k;j++)c=c*(12+j-1)/j;p*=c}if(!Number.isSafeInteger(p))throw Error("raw");return p}
function group(list){let m=new Map();for(let p of list){if(!m.has(p.m))m.set(p.m,[]);m.get(p.m).push(p)}for(let a of m.values())a.sort((p,q)=>p.v[i0]-q.v[i0]);return m}
function lb(a,x){let l=0,h=a.length;while(l<h){let k=(l+h)>>1;if(a[k].v[i0]<x)l=k+1;else h=k}return l}
function ranges(a,c,low,high){let l=(c-high+BN)%BN,h=(c-low+BN)%BN;return l<=h?[[lb(a,l),lb(a,h+1)]]:[[0,lb(a,h+1)],[lb(a,l),a.length]]}
let rows=[],minExcess=Infinity,minWitness=null;
const ppList=[...parts(5)].map(pp=>{let pos=roster(pp);return {pp,pos,groups:group(pos)}});
for(let np of [...parts(8)].filter(p=>p.length<=maxLen)){let neg=roster(np);for(let {pp,pos,groups} of ppList){let row={pos_pattern:pp,neg_pattern:np,raw:raw(pp)*raw(np),search:pos.length*neg.length,index_pass:0,box_survivors:0,valid:0,rejects:Array(N).fill(0),minMaxBudgetExcess:null};
for(let n of neg)for(let [mp0,list] of groups){let bs=box(mp0,n.m),rs=ranges(list,n.v[i0],bs[0].low,bs[0].high);let nPass=rs.reduce((s,[l,h])=>s+h-l,0);row.index_pass+=nPass;row.rejects[0]+=list.length-nPass;
for(let [l,h] of rs)for(let k0=l;k0<h;k0++){let p=list[k0],z=Array(N),ok=true;for(let j=0;j<N;j++){let {i,low,high}=bs[j],c=(n.v[i]-p.v[i]+BN)%BN;if(c<=high)z[i]=c;else if(c-BN>=low)z[i]=c-BN;else{if(j===0)throw Error("index false positive");row.rejects[j]++;ok=false;break}}if(!ok)continue;row.box_survivors++;
let u=Array.from({length:N},(_,j)=>{let x=z.reduce((s,v,k)=>s+BigInt(v)*U[k][j],0n);if(x%B)throw Error("integrality");return x/B});
let rhs=Array.from({length:6},(_,k)=>n.rs.reduce((s,r,j)=>s+targets.get(np[j]*100+r)[k],0n)-p.rs.reduce((s,r,j)=>s+targets.get(pp[j]*100+r)[k],0n));if(!check(u,rhs))throw Error("congruences");
let mp=BigInt(p.m)+u.reduce((s,v,j)=>s+(v>0n?v*W[j]:0n),0n),mn=BigInt(n.m)+u.reduce((s,v,j)=>s+(v<0n?-v*W[j]:0n),0n);let excess=Number((mp>mn?mp:mn)-BigInt(C));if(row.minMaxBudgetExcess===null||excess<row.minMaxBudgetExcess)row.minMaxBudgetExcess=excess;if(excess<minExcess){minExcess=excess;minWitness={pp,np,pos:p.rs,neg:n.rs,u:u.map(String),masses:[String(mp),String(mn)],excess}}if(excess<=0)row.valid++}}
if(row.rejects.reduce((a,b)=>a+b,0)+row.box_survivors!==row.search)throw Error("coverage");if(row.index_pass!==row.search-row.rejects[0])throw Error("index coverage");rows.push(row)}}
return {rows,totals:Object.fromEntries(["raw","search","index_pass","box_survivors","valid"].map(k=>[k,rows.reduce((s,r)=>s+r[k],0)])),minExcess,minWitness,width:width.join("/"),det:abs(det[0]).toString(),coordinate_order:bounds.map(b=>b.i)}
}
```
