# T6 q13 split(2,11), negative lengths 4–11 — exact dual-coordinate closure

Informed Driver lane EM-DVR-DEBB5E, frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Basis input 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json blob bcab5ce85b368d2b65a74340ceadb4527da0f01e. Reuses exact dual-coordinate lemma and previous implementation from cd13961f1ad5ca95a5e1431216f0017e57f00825 and 35b35ea07ebfb12e57110564d6a79efd92a05e8b. This is independent execution relative to author GS solver, not independent review of own method. Only new negative lengths 4–11, both positive partitions. No author certificate field comparison asserted. All relaxed rosters retained, including common atoms. Enumerate labels in nondecreasing order within each equal-q group; prune only when remaining minimum mass exceeds 2331. Saturation by digit-lift surjectivity and determinant 13^21; each coordinate interval has width <= 498515831/736645312 < 1, and compatible scaled coordinates modulo 13^6 are unique. For every survivor reconstruct u, verify six congruences exactly, evaluate both signed masses; row-level exclusion counts sum to actual search cardinality. Record minimum max-side budget excess and its successive attaining vectors; no claim all survivors individually persisted. Raw counts use binomial multiset product. Scope excludes H0, lower-prime completion, observer implication, entire T6; no formal Review or acceptance. This run completes split(2,11) only in conjunction with previously verified 32 rows.

## Executed data
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
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "raw": 55023696,
      "search": 641238,
      "box_survivors": 10,
      "valid": 0,
      "rejects": [
        450983,
        132084,
        38614,
        11562,
        4830,
        1868,
        702,
        327,
        200,
        29,
        27,
        2
      ],
      "minMaxBudgetExcess": 2098
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "raw": 8465184,
      "search": 98652,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        67776,
        20919,
        6609,
        2024,
        809,
        319,
        124,
        28,
        23,
        11,
        5,
        2
      ],
      "minMaxBudgetExcess": 4488
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2
      ],
      "raw": 157210560,
      "search": 3261960,
      "box_survivors": 26,
      "valid": 0,
      "rejects": [
        2303486,
        665094,
        197779,
        60917,
        21363,
        8332,
        3126,
        1045,
        499,
        174,
        86,
        33
      ],
      "minMaxBudgetExcess": 1897
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2
      ],
      "raw": 24186240,
      "search": 501840,
      "box_survivors": 9,
      "valid": 0,
      "rejects": [
        347250,
        105490,
        32316,
        10148,
        3974,
        1586,
        585,
        269,
        136,
        45,
        20,
        12
      ],
      "minMaxBudgetExcess": 3584
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        3
      ],
      "raw": 70744752,
      "search": 3393078,
      "box_survivors": 49,
      "valid": 0,
      "rejects": [
        2390114,
        693788,
        209132,
        62934,
        23240,
        8427,
        3287,
        1301,
        481,
        190,
        94,
        41
      ],
      "minMaxBudgetExcess": 2215
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        3
      ],
      "raw": 10883808,
      "search": 522012,
      "box_survivors": 15,
      "valid": 0,
      "rejects": [
        360037,
        109763,
        34582,
        10780,
        4167,
        1599,
        648,
        239,
        112,
        39,
        26,
        5
      ],
      "minMaxBudgetExcess": 2329
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2
      ],
      "raw": 193617216,
      "search": 8116056,
      "box_survivors": 121,
      "valid": 0,
      "rejects": [
        5716698,
        1657385,
        502180,
        151962,
        55112,
        19884,
        7902,
        2852,
        1203,
        480,
        202,
        75
      ],
      "minMaxBudgetExcess": 1481
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2
      ],
      "raw": 29787264,
      "search": 1248624,
      "box_survivors": 34,
      "valid": 0,
      "rejects": [
        864283,
        261077,
        81730,
        25638,
        9578,
        3838,
        1466,
        556,
        256,
        107,
        48,
        13
      ],
      "minMaxBudgetExcess": 2418
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4
      ],
      "raw": 29787264,
      "search": 2750592,
      "box_survivors": 48,
      "valid": 0,
      "rejects": [
        1929148,
        565292,
        172594,
        52263,
        19348,
        7069,
        2905,
        1162,
        488,
        142,
        100,
        33
      ],
      "minMaxBudgetExcess": 2096
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4
      ],
      "raw": 4582656,
      "search": 423168,
      "box_survivors": 10,
      "valid": 0,
      "rejects": [
        291437,
        88811,
        28329,
        8825,
        3493,
        1381,
        506,
        219,
        99,
        37,
        11,
        10
      ],
      "minMaxBudgetExcess": 3372
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "raw": 139007232,
      "search": 11495406,
      "box_survivors": 133,
      "valid": 0,
      "rejects": [
        8072178,
        2358259,
        715597,
        218343,
        80497,
        30912,
        11738,
        4463,
        1929,
        804,
        399,
        154
      ],
      "minMaxBudgetExcess": 2027
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "raw": 21385728,
      "search": 1768524,
      "box_survivors": 41,
      "valid": 0,
      "rejects": [
        1219437,
        370570,
        117846,
        37143,
        14222,
        5619,
        2087,
        924,
        384,
        145,
        78,
        28
      ],
      "minMaxBudgetExcess": 1614
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        5
      ],
      "raw": 11583936,
      "search": 2330328,
      "box_survivors": 53,
      "valid": 0,
      "rejects": [
        1631981,
        480166,
        146438,
        44534,
        16750,
        6322,
        2461,
        959,
        375,
        172,
        99,
        18
      ],
      "minMaxBudgetExcess": 1800
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        5
      ],
      "raw": 1782144,
      "search": 358512,
      "box_survivors": 11,
      "valid": 0,
      "rejects": [
        246288,
        75347,
        24332,
        7732,
        2844,
        1163,
        480,
        185,
        73,
        33,
        18,
        6
      ],
      "minMaxBudgetExcess": 2395
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "raw": 124016256,
      "search": 9836502,
      "box_survivors": 103,
      "valid": 0,
      "rejects": [
        6909608,
        2011780,
        615358,
        188842,
        68625,
        25970,
        9749,
        3840,
        1600,
        636,
        269,
        122
      ],
      "minMaxBudgetExcess": 1936
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "raw": 19079424,
      "search": 1513308,
      "box_survivors": 34,
      "valid": 0,
      "rejects": [
        1043173,
        315901,
        101875,
        32065,
        12352,
        4740,
        1983,
        687,
        295,
        125,
        48,
        30
      ],
      "minMaxBudgetExcess": 1197
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "raw": 49061376,
      "search": 9349782,
      "box_survivors": 149,
      "valid": 0,
      "rejects": [
        6554616,
        1920145,
        588309,
        179303,
        66528,
        25224,
        9491,
        3718,
        1344,
        608,
        223,
        124
      ],
      "minMaxBudgetExcess": 1747
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "raw": 7547904,
      "search": 1438428,
      "box_survivors": 27,
      "valid": 0,
      "rejects": [
        988580,
        301935,
        97303,
        31215,
        11625,
        4605,
        1870,
        727,
        337,
        124,
        57,
        23
      ],
      "minMaxBudgetExcess": 2002
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        3,
        3
      ],
      "raw": 26574912,
      "search": 5120934,
      "box_survivors": 93,
      "valid": 0,
      "rejects": [
        3587445,
        1056238,
        321426,
        99820,
        34382,
        13327,
        5052,
        1903,
        718,
        357,
        98,
        75
      ],
      "minMaxBudgetExcess": 1713
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        3,
        3
      ],
      "raw": 4088448,
      "search": 787836,
      "box_survivors": 15,
      "valid": 0,
      "rejects": [
        542276,
        165480,
        52653,
        16807,
        6282,
        2516,
        1075,
        406,
        186,
        85,
        35,
        20
      ],
      "minMaxBudgetExcess": 2833
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        6
      ],
      "raw": 4088448,
      "search": 1630668,
      "box_survivors": 31,
      "valid": 0,
      "rejects": [
        1140122,
        336580,
        103575,
        31784,
        11436,
        4303,
        1578,
        667,
        418,
        102,
        52,
        20
      ],
      "minMaxBudgetExcess": 1875
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        6
      ],
      "raw": 628992,
      "search": 250872,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        171877,
        53031,
        16991,
        5437,
        2053,
        884,
        350,
        147,
        56,
        29,
        6,
        4
      ],
      "minMaxBudgetExcess": 1573
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        3
      ],
      "raw": 99655920,
      "search": 18297786,
      "box_survivors": 247,
      "valid": 0,
      "rejects": [
        12841091,
        3754078,
        1145467,
        349143,
        127164,
        49435,
        18814,
        7495,
        2883,
        1223,
        510,
        236
      ],
      "minMaxBudgetExcess": 1934
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        3
      ],
      "raw": 15331680,
      "search": 2815044,
      "box_survivors": 68,
      "valid": 0,
      "rejects": [
        1937477,
        590516,
        188616,
        60103,
        22817,
        9082,
        3697,
        1493,
        674,
        294,
        143,
        64
      ],
      "minMaxBudgetExcess": 1273
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        5
      ],
      "raw": 15331680,
      "search": 6046716,
      "box_survivors": 110,
      "valid": 0,
      "rejects": [
        4227241,
        1251484,
        380097,
        117255,
        43088,
        16642,
        6593,
        2621,
        995,
        396,
        135,
        59
      ],
      "minMaxBudgetExcess": 2223
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        5
      ],
      "raw": 2358720,
      "search": 930264,
      "box_survivors": 18,
      "valid": 0,
      "rejects": [
        638561,
        197156,
        62059,
        19899,
        7555,
        2959,
        1208,
        467,
        235,
        86,
        40,
        21
      ],
      "minMaxBudgetExcess": 1505
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        4
      ],
      "raw": 15331680,
      "search": 6046716,
      "box_survivors": 178,
      "valid": 0,
      "rejects": [
        4225760,
        1249167,
        381540,
        118982,
        43426,
        17319,
        6208,
        2431,
        1074,
        358,
        200,
        73
      ],
      "minMaxBudgetExcess": 1748
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        4
      ],
      "raw": 2358720,
      "search": 930264,
      "box_survivors": 25,
      "valid": 0,
      "rejects": [
        637722,
        196321,
        63073,
        20492,
        7605,
        2959,
        1191,
        479,
        235,
        108,
        31,
        23
      ],
      "minMaxBudgetExcess": 2814
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        7
      ],
      "raw": 1277640,
      "search": 865878,
      "box_survivors": 10,
      "valid": 0,
      "rejects": [
        601967,
        180368,
        55466,
        17254,
        6592,
        2533,
        1031,
        383,
        158,
        75,
        13,
        28
      ],
      "minMaxBudgetExcess": 2252
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        7
      ],
      "raw": 196560,
      "search": 133212,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        90773,
        28607,
        9017,
        2895,
        1134,
        478,
        173,
        77,
        33,
        14,
        8,
        1
      ],
      "minMaxBudgetExcess": 3349
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        2
      ],
      "raw": 38755080,
      "search": 7292220,
      "box_survivors": 116,
      "valid": 0,
      "rejects": [
        5112590,
        1497544,
        458809,
        140016,
        51191,
        20019,
        7318,
        2699,
        1202,
        486,
        151,
        79
      ],
      "minMaxBudgetExcess": 1944
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        2
      ],
      "raw": 5962320,
      "search": 1121880,
      "box_survivors": 20,
      "valid": 0,
      "rejects": [
        772127,
        233537,
        76364,
        24176,
        9331,
        3768,
        1419,
        670,
        309,
        81,
        48,
        30
      ],
      "minMaxBudgetExcess": 1145
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "raw": 26574912,
      "search": 10414638,
      "box_survivors": 227,
      "valid": 0,
      "rejects": [
        7284027,
        2148125,
        657698,
        203743,
        74087,
        28596,
        11068,
        4114,
        1801,
        753,
        276,
        123
      ],
      "minMaxBudgetExcess": 1834
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "raw": 4088448,
      "search": 1602252,
      "box_survivors": 44,
      "valid": 0,
      "rejects": [
        1099502,
        336501,
        108949,
        35029,
        13349,
        5251,
        2203,
        842,
        323,
        164,
        63,
        32
      ],
      "minMaxBudgetExcess": 2182
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        3
      ],
      "raw": 26574912,
      "search": 10414638,
      "box_survivors": 190,
      "valid": 0,
      "rejects": [
        7286165,
        2148330,
        655985,
        202440,
        75051,
        28070,
        11277,
        4211,
        1811,
        724,
        263,
        121
      ],
      "minMaxBudgetExcess": 1363
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        3
      ],
      "raw": 4088448,
      "search": 1602252,
      "box_survivors": 40,
      "valid": 0,
      "rejects": [
        1099175,
        338067,
        108444,
        34812,
        13034,
        5203,
        2091,
        804,
        321,
        178,
        55,
        28
      ],
      "minMaxBudgetExcess": 2130
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        6
      ],
      "raw": 4088448,
      "search": 2799888,
      "box_survivors": 55,
      "valid": 0,
      "rejects": [
        1949390,
        582298,
        179035,
        54835,
        20924,
        8220,
        2987,
        1208,
        522,
        256,
        100,
        58
      ],
      "minMaxBudgetExcess": 1961
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        6
      ],
      "raw": 628992,
      "search": 430752,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        294083,
        91977,
        29242,
        9390,
        3643,
        1493,
        510,
        195,
        133,
        50,
        18,
        11
      ],
      "minMaxBudgetExcess": 1338
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        3,
        5
      ],
      "raw": 4088448,
      "search": 2799888,
      "box_survivors": 56,
      "valid": 0,
      "rejects": [
        1948726,
        581334,
        179434,
        56312,
        20735,
        8223,
        3047,
        1169,
        520,
        215,
        77,
        40
      ],
      "minMaxBudgetExcess": 2165
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        3,
        5
      ],
      "raw": 628992,
      "search": 430752,
      "box_survivors": 14,
      "valid": 0,
      "rejects": [
        294037,
        91420,
        29450,
        9658,
        3656,
        1465,
        593,
        264,
        104,
        43,
        40,
        8
      ],
      "minMaxBudgetExcess": 4324
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        4,
        4
      ],
      "raw": 2214576,
      "search": 1511328,
      "box_survivors": 47,
      "valid": 0,
      "rejects": [
        1051779,
        313269,
        97851,
        30121,
        11022,
        4377,
        1762,
        652,
        236,
        132,
        60,
        20
      ],
      "minMaxBudgetExcess": 1849
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        4,
        4
      ],
      "raw": 340704,
      "search": 232512,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        158546,
        49304,
        16007,
        5269,
        2022,
        801,
        327,
        134,
        50,
        28,
        14,
        3
      ],
      "minMaxBudgetExcess": 4237
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        8
      ],
      "raw": 340704,
      "search": 314262,
      "box_survivors": 5,
      "valid": 0,
      "rejects": [
        216459,
        66445,
        20566,
        6630,
        2605,
        962,
        395,
        106,
        50,
        25,
        11,
        3
      ],
      "minMaxBudgetExcess": 2582
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        8
      ],
      "raw": 52416,
      "search": 48348,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        32753,
        10498,
        3284,
        1091,
        416,
        175,
        77,
        32,
        14,
        1,
        2,
        4
      ],
      "minMaxBudgetExcess": 3306
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "raw": 26574912,
      "search": 10414638,
      "box_survivors": 148,
      "valid": 0,
      "rejects": [
        7283951,
        2150531,
        656036,
        203533,
        74591,
        27819,
        10921,
        4252,
        1597,
        757,
        346,
        156
      ],
      "minMaxBudgetExcess": 1966
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "raw": 4088448,
      "search": 1602252,
      "box_survivors": 42,
      "valid": 0,
      "rejects": [
        1100057,
        337322,
        108232,
        34478,
        13114,
        5321,
        2225,
        837,
        384,
        170,
        51,
        19
      ],
      "minMaxBudgetExcess": 2658
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        2,
        2,
        5
      ],
      "raw": 5694624,
      "search": 3914664,
      "box_survivors": 81,
      "valid": 0,
      "rejects": [
        2723695,
        815951,
        250182,
        77768,
        28722,
        11136,
        4300,
        1654,
        706,
        259,
        151,
        59
      ],
      "minMaxBudgetExcess": 1635
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        2,
        2,
        5
      ],
      "raw": 876096,
      "search": 602256,
      "box_survivors": 23,
      "valid": 0,
      "rejects": [
        411154,
        129460,
        40257,
        13015,
        4892,
        2016,
        855,
        344,
        134,
        69,
        31,
        6
      ],
      "minMaxBudgetExcess": 1981
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        2,
        3,
        4
      ],
      "raw": 10513152,
      "search": 7254624,
      "box_survivors": 166,
      "valid": 0,
      "rejects": [
        5048303,
        1506228,
        466646,
        144404,
        54548,
        20982,
        8095,
        3022,
        1322,
        572,
        211,
        125
      ],
      "minMaxBudgetExcess": 948
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        2,
        3,
        4
      ],
      "raw": 1617408,
      "search": 1116096,
      "box_survivors": 46,
      "valid": 0,
      "rejects": [
        762403,
        236116,
        76393,
        24860,
        9636,
        4087,
        1489,
        588,
        283,
        115,
        58,
        22
      ],
      "minMaxBudgetExcess": 2045
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        2,
        7
      ],
      "raw": 876096,
      "search": 814944,
      "box_survivors": 30,
      "valid": 0,
      "rejects": [
        560722,
        171661,
        54229,
        17256,
        6549,
        2729,
        995,
        419,
        193,
        118,
        35,
        8
      ],
      "minMaxBudgetExcess": 1692
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        2,
        7
      ],
      "raw": 134784,
      "search": 125376,
      "box_survivors": 6,
      "valid": 0,
      "rejects": [
        85383,
        26817,
        8425,
        2787,
        1160,
        444,
        214,
        81,
        36,
        15,
        7,
        1
      ],
      "minMaxBudgetExcess": 2664
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        3,
        3,
        3
      ],
      "raw": 2214576,
      "search": 1511328,
      "box_survivors": 15,
      "valid": 0,
      "rejects": [
        1050304,
        314729,
        97443,
        30170,
        11359,
        4518,
        1671,
        675,
        249,
        147,
        29,
        19
      ],
      "minMaxBudgetExcess": 3362
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        3,
        3,
        3
      ],
      "raw": 340704,
      "search": 232512,
      "box_survivors": 6,
      "valid": 0,
      "rejects": [
        158814,
        49237,
        15896,
        5161,
        1978,
        863,
        339,
        126,
        55,
        19,
        15,
        3
      ],
      "minMaxBudgetExcess": 3539
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        3,
        6
      ],
      "raw": 876096,
      "search": 814944,
      "box_survivors": 30,
      "valid": 0,
      "rejects": [
        561688,
        170963,
        54107,
        16921,
        6819,
        2565,
        1044,
        508,
        168,
        95,
        22,
        14
      ],
      "minMaxBudgetExcess": 2070
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        3,
        6
      ],
      "raw": 134784,
      "search": 125376,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        84738,
        27087,
        8705,
        2944,
        1114,
        461,
        195,
        78,
        26,
        12,
        7,
        6
      ],
      "minMaxBudgetExcess": 4512
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        4,
        5
      ],
      "raw": 876096,
      "search": 814944,
      "box_survivors": 15,
      "valid": 0,
      "rejects": [
        561596,
        171645,
        53997,
        16681,
        6532,
        2746,
        1099,
        386,
        158,
        52,
        20,
        17
      ],
      "minMaxBudgetExcess": 2854
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        1,
        4,
        5
      ],
      "raw": 134784,
      "search": 125376,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        84902,
        26994,
        8695,
        2855,
        1147,
        451,
        199,
        77,
        25,
        17,
        4,
        3
      ],
      "minMaxBudgetExcess": 4445
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        2
      ],
      "raw": 4088448,
      "search": 1630668,
      "box_survivors": 41,
      "valid": 0,
      "rejects": [
        1139228,
        337474,
        102992,
        31817,
        11672,
        4514,
        1758,
        681,
        299,
        104,
        43,
        45
      ],
      "minMaxBudgetExcess": 2206
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        2
      ],
      "raw": 628992,
      "search": 250872,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        171278,
        53293,
        17214,
        5459,
        2148,
        909,
        354,
        122,
        61,
        18,
        8,
        4
      ],
      "minMaxBudgetExcess": 2768
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        2,
        2,
        2,
        4
      ],
      "raw": 4088448,
      "search": 2799888,
      "box_survivors": 49,
      "valid": 0,
      "rejects": [
        1947668,
        582718,
        179681,
        55615,
        20755,
        8186,
        3169,
        1157,
        519,
        230,
        89,
        52
      ],
      "minMaxBudgetExcess": 1999
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        2,
        2,
        2,
        4
      ],
      "raw": 628992,
      "search": 430752,
      "box_survivors": 11,
      "valid": 0,
      "rejects": [
        294329,
        90992,
        29743,
        9414,
        3742,
        1546,
        621,
        192,
        91,
        44,
        20,
        7
      ],
      "minMaxBudgetExcess": 5104
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        2,
        2,
        3,
        3
      ],
      "raw": 5694624,
      "search": 3914664,
      "box_survivors": 88,
      "valid": 0,
      "rejects": [
        2723928,
        812896,
        251872,
        78402,
        28753,
        11504,
        4311,
        1705,
        755,
        302,
        92,
        56
      ],
      "minMaxBudgetExcess": 1868
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        2,
        2,
        3,
        3
      ],
      "raw": 876096,
      "search": 602256,
      "box_survivors": 12,
      "valid": 0,
      "rejects": [
        411628,
        127653,
        41150,
        13324,
        5071,
        1887,
        941,
        318,
        167,
        70,
        24,
        11
      ],
      "minMaxBudgetExcess": 1817
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        2,
        2,
        6
      ],
      "raw": 876096,
      "search": 814944,
      "box_survivors": 12,
      "valid": 0,
      "rejects": [
        561325,
        171662,
        53934,
        17292,
        6398,
        2607,
        993,
        417,
        161,
        105,
        23,
        15
      ],
      "minMaxBudgetExcess": 2044
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        2,
        2,
        6
      ],
      "raw": 134784,
      "search": 125376,
      "box_survivors": 6,
      "valid": 0,
      "rejects": [
        84942,
        27036,
        8675,
        2800,
        1044,
        500,
        181,
        104,
        41,
        29,
        10,
        8
      ],
      "minMaxBudgetExcess": 4095
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        2,
        3,
        5
      ],
      "raw": 1617408,
      "search": 1510938,
      "box_survivors": 50,
      "valid": 0,
      "rejects": [
        1041457,
        318023,
        99807,
        31496,
        11861,
        4936,
        1961,
        815,
        321,
        136,
        48,
        27
      ],
      "minMaxBudgetExcess": 3380
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        2,
        3,
        5
      ],
      "raw": 248832,
      "search": 232452,
      "box_survivors": 12,
      "valid": 0,
      "rejects": [
        157003,
        50063,
        16355,
        5393,
        2148,
        868,
        358,
        142,
        67,
        30,
        10,
        3
      ],
      "minMaxBudgetExcess": 2756
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        2,
        4,
        4
      ],
      "raw": 876096,
      "search": 814944,
      "box_survivors": 21,
      "valid": 0,
      "rejects": [
        561311,
        171598,
        53819,
        17213,
        6551,
        2773,
        1008,
        364,
        169,
        86,
        17,
        14
      ],
      "minMaxBudgetExcess": 2784
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        2,
        4,
        4
      ],
      "raw": 134784,
      "search": 125376,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        84947,
        26759,
        8889,
        2887,
        1156,
        434,
        194,
        67,
        27,
        9,
        3,
        0
      ],
      "minMaxBudgetExcess": 5042
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        1,
        3,
        3,
        4
      ],
      "raw": 876096,
      "search": 814944,
      "box_survivors": 19,
      "valid": 0,
      "rejects": [
        561395,
        171203,
        54224,
        17264,
        6526,
        2609,
        982,
        409,
        176,
        76,
        36,
        25
      ],
      "minMaxBudgetExcess": 2023
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        1,
        3,
        3,
        4
      ],
      "raw": 134784,
      "search": 125376,
      "box_survivors": 8,
      "valid": 0,
      "rejects": [
        84877,
        26766,
        8864,
        2941,
        1160,
        473,
        177,
        68,
        28,
        9,
        3,
        2
      ],
      "minMaxBudgetExcess": 2581
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        2,
        2,
        2,
        2,
        3
      ],
      "raw": 1277640,
      "search": 865878,
      "box_survivors": 21,
      "valid": 0,
      "rejects": [
        602260,
        179828,
        55484,
        17524,
        6581,
        2507,
        973,
        421,
        157,
        80,
        36,
        6
      ],
      "minMaxBudgetExcess": 1237
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        2,
        2,
        2,
        2,
        3
      ],
      "raw": 196560,
      "search": 133212,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        90513,
        28582,
        9156,
        3057,
        1133,
        458,
        204,
        68,
        23,
        10,
        7,
        0
      ],
      "minMaxBudgetExcess": 4295
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        2,
        2,
        2,
        5
      ],
      "raw": 340704,
      "search": 314262,
      "box_survivors": 17,
      "valid": 0,
      "rejects": [
        216654,
        66183,
        20684,
        6580,
        2507,
        974,
        401,
        142,
        65,
        33,
        14,
        8
      ],
      "minMaxBudgetExcess": 3091
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        2,
        2,
        2,
        5
      ],
      "raw": 52416,
      "search": 48348,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        32736,
        10579,
        3198,
        1139,
        412,
        173,
        69,
        28,
        7,
        4,
        1,
        2
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        2,
        2,
        3,
        4
      ],
      "raw": 876096,
      "search": 814944,
      "box_survivors": 20,
      "valid": 0,
      "rejects": [
        561396,
        170980,
        54245,
        17397,
        6543,
        2606,
        1037,
        407,
        199,
        76,
        24,
        14
      ],
      "minMaxBudgetExcess": 1933
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        2,
        2,
        3,
        4
      ],
      "raw": 134784,
      "search": 125376,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        84943,
        26620,
        8862,
        2889,
        1205,
        529,
        199,
        83,
        31,
        10,
        0,
        2
      ],
      "minMaxBudgetExcess": 6207
    },
    {
      "pos_pattern": [
        1,
        1
      ],
      "neg_pattern": [
        2,
        3,
        3,
        3
      ],
      "raw": 340704,
      "search": 314262,
      "box_survivors": 11,
      "valid": 0,
      "rejects": [
        216286,
        66179,
        20961,
        6576,
        2549,
        1007,
        403,
        165,
        66,
        41,
        15,
        3
      ],
      "minMaxBudgetExcess": 3583
    },
    {
      "pos_pattern": [
        2
      ],
      "neg_pattern": [
        2,
        3,
        3,
        3
      ],
      "raw": 52416,
      "search": 48348,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        32662,
        10420,
        3341,
        1089,
        482,
        189,
        101,
        30,
        21,
        8,
        4,
        1
      ],
      "minMaxBudgetExcess": null
    }
  ],
  "totals": {
    "raw": 1342531800,
    "search": 190247220,
    "box_survivors": 3537,
    "valid": 0
  },
  "minExcess": 948,
  "witnesses": [
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "pos": [
        2,
        6
      ],
      "neg": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4
      ],
      "u": [
        "-122",
        "49",
        "-13",
        "5",
        "4",
        "-3",
        "-8",
        "9",
        "-26",
        "-12",
        "7",
        "5"
      ],
      "masses": [
        "4872",
        "9503"
      ],
      "excess": 7172
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "pos": [
        1,
        1
      ],
      "neg": [
        1,
        1,
        1,
        1,
        3,
        3,
        3,
        4,
        5,
        6,
        9
      ],
      "u": [
        "-40",
        "79",
        "25",
        "30",
        "13",
        "22",
        "1",
        "-11",
        "-9",
        "5",
        "1",
        "-5"
      ],
      "masses": [
        "8220",
        "5761"
      ],
      "excess": 5889
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "pos": [
        9,
        12
      ],
      "neg": [
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3
      ],
      "u": [
        "61",
        "61",
        "15",
        "1",
        "2",
        "-17",
        "11",
        "7",
        "-8",
        "3",
        "-4",
        "2"
      ],
      "masses": [
        "6023",
        "4952"
      ],
      "excess": 3692
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "pos": [
        1,
        10
      ],
      "neg": [
        1,
        1,
        1,
        2,
        3,
        3,
        3,
        3,
        4,
        4,
        9
      ],
      "u": [
        "66",
        "19",
        "4",
        "23",
        "5",
        "-1",
        "-8",
        "9",
        "0",
        "-8",
        "0",
        "-2"
      ],
      "masses": [
        "4318",
        "4429"
      ],
      "excess": 2098
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2
      ],
      "pos": [
        6,
        7
      ],
      "neg": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        8,
        8
      ],
      "u": [
        "6",
        "-12",
        "30",
        "5",
        "-14",
        "-1",
        "-5",
        "2",
        "14",
        "1",
        "1",
        "1"
      ],
      "masses": [
        "4228",
        "3923"
      ],
      "excess": 1897
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2
      ],
      "pos": [
        8,
        10
      ],
      "neg": [
        1,
        2,
        3,
        3,
        3,
        6,
        6,
        2,
        8
      ],
      "u": [
        "-27",
        "-14",
        "-8",
        "8",
        "0",
        "1",
        "5",
        "5",
        "2",
        "-3",
        "1",
        "-1"
      ],
      "masses": [
        "2394",
        "3812"
      ],
      "excess": 1481
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "pos": [
        1
      ],
      "neg": [
        1,
        1,
        2,
        5,
        10,
        2,
        6,
        6
      ],
      "u": [
        "47",
        "4",
        "-19",
        "2",
        "0",
        "-2",
        "-1",
        "9",
        "-1",
        "1",
        "3",
        "6"
      ],
      "masses": [
        "3528",
        "3362"
      ],
      "excess": 1197
    },
    {
      "pp": [
        2
      ],
      "np": [
        1,
        1,
        1,
        2,
        2,
        2,
        2
      ],
      "pos": [
        10
      ],
      "neg": [
        1,
        1,
        1,
        6,
        7,
        9,
        9
      ],
      "u": [
        "7",
        "-10",
        "1",
        "21",
        "4",
        "-1",
        "-4",
        "4",
        "3",
        "4",
        "2",
        "0"
      ],
      "masses": [
        "3476",
        "2981"
      ],
      "excess": 1145
    },
    {
      "pp": [
        1,
        1
      ],
      "np": [
        1,
        1,
        2,
        3,
        4
      ],
      "pos": [
        1,
        6
      ],
      "neg": [
        1,
        9,
        6,
        4,
        10
      ],
      "u": [
        "100",
        "-6",
        "17",
        "-7",
        "4",
        "-2",
        "-1",
        "0",
        "0",
        "0",
        "-2",
        "3"
      ],
      "masses": [
        "2994",
        "3279"
      ],
      "excess": 948
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
Load U from pinned JSON input; call audit(U). Exact BigInt for algebra, safe integers for residues, bounded masses and count.
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
function roster(pat){let out=[],v=Array(N).fill(0),rs=[];const tail=Array(pat.length+1).fill(0);for(let i=pat.length-1;i>=0;i--)tail[i]=tail[i+1]+169*pat[i]+12;function go(i,m){if(i===pat.length){out.push({m,rs:rs.slice(),v:v.slice()});return}let start=i&&pat[i]===pat[i-1]?rs[i-1]:1;for(let r=start;r<=12;r++){let cost=169*pat[i]+13*r-1;if(m+cost+tail[i+1]>C)break;let a=coords.get(pat[i]*100+r);rs.push(r);for(let k=0;k<N;k++)v[k]=(v[k]+a[k])%BN;go(i+1,m+cost);for(let k=0;k<N;k++)v[k]=(v[k]-a[k]+BN)%BN;rs.pop()}}go(0,0);return out}
function raw(pat){let counts={};for(let q of pat)counts[q]=(counts[q]??0)+1;let p=1;for(let k of Object.values(counts)){let c=1;for(let j=1;j<=k;j++)c=c*(12+j-1)/j;p*=c}if(!Number.isSafeInteger(p))throw Error("raw");return p}
let rows=[],witnesses=[],minExcess=Infinity;
const ppList=[...parts(2)].map(pp=>({pp,pos:roster(pp)}));
for(let np of [...parts(11)].filter(p=>p.length>=4)){let neg=roster(np);for(let {pp,pos} of ppList){let row={pos_pattern:pp,neg_pattern:np,raw:raw(pp)*raw(np),search:pos.length*neg.length,box_survivors:0,valid:0,rejects:Array(N).fill(0),minMaxBudgetExcess:null};
for(let n of neg)for(let p of pos){let bs=box(p.m,n.m),z=Array(N),ok=true;for(let j=0;j<N;j++){let {i,low,high}=bs[j],c=(n.v[i]-p.v[i]+BN)%BN;if(c<=high)z[i]=c;else if(c-BN>=low)z[i]=c-BN;else{row.rejects[j]++;ok=false;break}}if(!ok)continue;row.box_survivors++;
let u=Array.from({length:N},(_,j)=>{let x=z.reduce((s,v,k)=>s+BigInt(v)*U[k][j],0n);if(x%B)throw Error("integrality");return x/B});
let rhs=Array.from({length:6},(_,k)=>n.rs.reduce((s,r,j)=>s+targets.get(np[j]*100+r)[k],0n)-p.rs.reduce((s,r,j)=>s+targets.get(pp[j]*100+r)[k],0n));if(!check(u,rhs))throw Error("congruences");
let mp=BigInt(p.m)+u.reduce((s,v,j)=>s+(v>0n?v*W[j]:0n),0n),mn=BigInt(n.m)+u.reduce((s,v,j)=>s+(v<0n?-v*W[j]:0n),0n);let excess=Number((mp>mn?mp:mn)-BigInt(C));if(row.minMaxBudgetExcess===null||excess<row.minMaxBudgetExcess)row.minMaxBudgetExcess=excess;if(excess<minExcess){minExcess=excess;witnesses.push({pp,np,pos:p.rs,neg:n.rs,u:u.map(String),masses:[String(mp),String(mn)],excess})}if(excess<=0)row.valid++}
if(row.rejects.reduce((a,b)=>a+b,0)+row.box_survivors!==row.search)throw Error("coverage");rows.push(row)}}
return {rows,totals:Object.fromEntries(["raw","search","box_survivors","valid"].map(k=>[k,rows.reduce((s,r)=>s+r[k],0)])),minExcess,witnesses,width:width.join("/"),det:abs(det[0]).toString(),coordinate_order:bounds.map(b=>b.i)}
}
```
