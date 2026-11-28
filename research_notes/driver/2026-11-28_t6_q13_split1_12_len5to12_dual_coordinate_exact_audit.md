# T6 q13 split (1,12), negative lengths 5–12: exact dual-coordinate audit and complete split closure

Original informed Driver EM-DVR-DEBB5E, 2026-11-28. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Shared row basis: 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json, blob bcab5ce85b368d2b65a74340ceadb4527da0f01e. Compare length 5 author certificate 4a70a7b060fa09262f9aa491a765fcfa62380b75:research_checks/T6_P13_Q13_SPLIT1_12_LEN5_AUTHOR_EXACT_CERT_20261126.json blob b0e88cbdc3205dc6e757b72e9624c90529770967; length 6–12 certificate a4e13df8b7e32517673e6067bba9b2ad596d54bd:research_checks/T6_P13_Q13_SPLIT1_12_LEN6_12_CERT_20261126.json blob 8035785804d39bc11d71d9c79d4a840135341be6. The latter exact locator was recovered from author RA-A468735D7C934B25C4B9614F at d723b4a393ced2094141a4217a52114e851c6bd6. No blind claim; actual independent solver relative to author's GS implementation; shared scientific inputs and prior Driver p19 signed-coordinate method. No new general toolbox or novelty claim.

## Exact dual-coordinate lemma
Let u be the row vector of 12 signed low-atom coefficients, U a saturated row basis for the homogeneous mixed congruences, and alpha=u U^{-1}. In an affine coset alpha belongs to c/B+Z^12 with B=13^6. Use the same digit-lift proof of surjectivity as in the prior split0 audit; each stage is a Vandermonde system on distinct nonzero mod-13 units, so the full index is 13^21. Recheck U row congruences, determinant and every lifted high-atom representative. Let w_j=13j-1 for j=1..12, A,B_minus be remaining separate positive and negative mass budgets. For column i define g_{ji}=(U^{-1})_{ji}/w_j, l_i=min(0,min_j g_{ji}), h_i=max(0,max_j g_{ji}). Then EVERY feasible alpha_i lies in [A*l_i-B_minus*h_i,A*h_i-B_minus*l_i], since positive and negative weighted mass vectors are nonnegative with total at most A,B_minus. The width is (A+B_minus)(h_i-l_i). For any nonempty high roster of total q=13, high mass is 169*13+sum(13r-1) >= 2197+12. Thus A+B_minus <= 2*2331-2209=2453. Exact inverse-matrix arithmetic establishes max_i 2453*(h_i-l_i)=498515831/736645312<1. Consequently each coordinate interval admits at most one integer shift, and there is at most one possible u for every high roster. If any coordinate is empty reject; otherwise recover u exactly and test all mixed congruences and both separate budgets. This does not rely on a Euclidean enclosing sphere or nearest-vector heuristic. The lemma applies to every q13 split with this full fixed carrier and the same budgets. Scope remains six mixed congruences only, not observer implication, H0, lower-prime completion, or global T6.

## Coverage
For each negative partition of 12, enumerate all 12 positive labels and every unordered negative group roster satisfying high mass <=2331. For length ell, m_minus=169*12+13 sum r-ell, so pruning only when even the minimum remaining label sum would exceed floor((2331-169*12+ell)/13) is complete. Raw roster count product over q multiplicities a_q of binom(12+a_q-1,a_q); common-atom count subtracts the product with one chosen q=1 label removed (11 rather than 12) and multiplies by 12. Keep common atoms in actual searches. Exact integer residue and interval comparisons: all scaled coordinate values fit safely in JS integer range (B=4826809, residues reduced at every step, intervals width<B and contain zero); inverse, fraction bounds, recovered u and final masses use BigInt. Six author fields per pattern independently compared (raw, search, over, common_included, common_feasible, valid). Node/leaf counts deliberately not equated to a different algorithm. All surviving boxes are recovered and checked, even if budget-invalid.

Previously audited 34 length 1–4 patterns: 7ab22f8ee19772fab74f458818c716e4a78bfbb3 and 5fac59bcb449f6ea3b68c8b7f0ad3788c51b821d. This new audit completes remaining 43, hence all 77 split(1,12) patterns are independently excluded even without smoothness. Together with split(0,13) 101 patterns, independent exact solver coverage is 178/885. This is not formal Review, Result admission, Task completion or mother closure.

## Actual exact output
```json
{
  "rows": [
    {
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
        1,
        1
      ],
      "raw": 16224936,
      "common_included": 8465184,
      "search": 3252,
      "over": 16221684,
      "common_feasible": 887,
      "valid": 0,
      "box_survivors": 1,
      "coordinate_rejects": [
        2116,
        750,
        213,
        122,
        31,
        8,
        4,
        2,
        1,
        2,
        1,
        1
      ]
    },
    {
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
        2
      ],
      "raw": 50791104,
      "common_included": 24186240,
      "search": 14940,
      "over": 50776164,
      "common_feasible": 3902,
      "valid": 0,
      "box_survivors": 0,
      "coordinate_rejects": [
        10032,
        3229,
        1054,
        388,
        152,
        61,
        15,
        6,
        2,
        1,
        0,
        0
      ]
    },
    {
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
        3
      ],
      "raw": 24186240,
      "common_included": 10883808,
      "search": 20424,
      "over": 24165816,
      "common_feasible": 5501,
      "valid": 0,
      "box_survivors": 0,
      "coordinate_rejects": [
        13528,
        4454,
        1573,
        468,
        242,
        113,
        26,
        11,
        4,
        5,
        0,
        0
      ]
    },
    {
      "neg_pattern": [
        1,
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
      "raw": 70744752,
      "common_included": 29787264,
      "search": 38784,
      "over": 70705968,
      "common_feasible": 9804,
      "valid": 0,
      "box_survivors": 2,
      "coordinate_rejects": [
        25721,
        8494,
        3049,
        928,
        348,
        135,
        66,
        24,
        12,
        5,
        0,
        0
      ]
    },
    {
      "neg_pattern": [
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
      "raw": 10883808,
      "common_included": 4582656,
      "search": 26940,
      "over": 10856868,
      "common_feasible": 7441,
      "valid": 0,
      "box_survivors": 0,
      "coordinate_rejects": [
        18047,
        5809,
        1960,
        707,
        236,
        101,
        45,
        14,
        14,
        6,
        1,
        0
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "raw": 54991872,
      "common_included": 21385728,
      "search": 89292,
      "over": 54902580,
      "common_feasible": 22771,
      "valid": 0,
      "box_survivors": 7,
      "coordinate_rejects": [
        59556,
        19311,
        6685,
        2256,
        879,
        315,
        160,
        59,
        38,
        19,
        5,
        2
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        5
      ],
      "raw": 4582656,
      "common_included": 1782144,
      "search": 25500,
      "over": 4557156,
      "common_feasible": 6964,
      "valid": 0,
      "box_survivors": 1,
      "coordinate_rejects": [
        16878,
        5683,
        1880,
        698,
        209,
        83,
        41,
        19,
        4,
        3,
        1,
        0
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "raw": 54058368,
      "common_included": 19079424,
      "search": 73164,
      "over": 53985204,
      "common_feasible": 17757,
      "valid": 0,
      "box_survivors": 3,
      "coordinate_rejects": [
        49108,
        15434,
        5312,
        1916,
        825,
        302,
        139,
        66,
        33,
        18,
        3,
        5
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "raw": 21385728,
      "common_included": 7547904,
      "search": 83568,
      "over": 21302160,
      "common_feasible": 20903,
      "valid": 0,
      "box_survivors": 8,
      "coordinate_rejects": [
        55561,
        18163,
        6362,
        2084,
        824,
        326,
        140,
        50,
        28,
        12,
        9,
        1
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        3
      ],
      "raw": 11583936,
      "common_included": 4088448,
      "search": 48444,
      "over": 11535492,
      "common_feasible": 12247,
      "valid": 0,
      "box_survivors": 3,
      "coordinate_rejects": [
        32108,
        10548,
        3583,
        1175,
        597,
        255,
        90,
        36,
        18,
        23,
        3,
        5
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        6
      ],
      "raw": 1782144,
      "common_included": 628992,
      "search": 30420,
      "over": 1751724,
      "common_feasible": 8329,
      "valid": 0,
      "box_survivors": 2,
      "coordinate_rejects": [
        20255,
        6628,
        2308,
        685,
        321,
        108,
        69,
        29,
        12,
        2,
        1,
        0
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        3
      ],
      "raw": 49061376,
      "common_included": 15331680,
      "search": 146964,
      "over": 48914412,
      "common_feasible": 33788,
      "valid": 0,
      "box_survivors": 5,
      "coordinate_rejects": [
        97826,
        32114,
        10824,
        3747,
        1378,
        649,
        251,
        90,
        49,
        20,
        8,
        3
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        5
      ],
      "raw": 7547904,
      "common_included": 2358720,
      "search": 99948,
      "over": 7447956,
      "common_feasible": 24647,
      "valid": 0,
      "box_survivors": 3,
      "coordinate_rejects": [
        66981,
        21599,
        7131,
        2519,
        945,
        435,
        223,
        67,
        26,
        8,
        8,
        3
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        3,
        4
      ],
      "raw": 7547904,
      "common_included": 2358720,
      "search": 99948,
      "over": 7447956,
      "common_feasible": 24647,
      "valid": 0,
      "box_survivors": 3,
      "coordinate_rejects": [
        66351,
        21888,
        7598,
        2360,
        1025,
        409,
        166,
        73,
        40,
        20,
        13,
        2
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        7
      ],
      "raw": 628992,
      "common_included": 196560,
      "search": 32424,
      "over": 596568,
      "common_feasible": 8659,
      "valid": 0,
      "box_survivors": 3,
      "coordinate_rejects": [
        21609,
        7060,
        2320,
        854,
        355,
        145,
        50,
        16,
        5,
        6,
        0,
        1
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2
      ],
      "raw": 22358700,
      "common_included": 5962320,
      "search": 72672,
      "over": 22286028,
      "common_feasible": 15491,
      "valid": 0,
      "box_survivors": 4,
      "coordinate_rejects": [
        48565,
        15667,
        5311,
        1826,
        728,
        334,
        160,
        37,
        27,
        10,
        2,
        1
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "raw": 15331680,
      "common_included": 4088448,
      "search": 170868,
      "over": 15160812,
      "common_feasible": 37489,
      "valid": 0,
      "box_survivors": 9,
      "coordinate_rejects": [
        114000,
        37232,
        12432,
        4189,
        1705,
        765,
        342,
        96,
        62,
        23,
        11,
        2
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3,
        3
      ],
      "raw": 15331680,
      "common_included": 4088448,
      "search": 170868,
      "over": 15160812,
      "common_feasible": 37489,
      "valid": 0,
      "box_survivors": 4,
      "coordinate_rejects": [
        113738,
        37309,
        12643,
        4292,
        1630,
        731,
        284,
        137,
        57,
        30,
        11,
        2
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        6
      ],
      "raw": 2358720,
      "common_included": 628992,
      "search": 103908,
      "over": 2254812,
      "common_feasible": 24178,
      "valid": 0,
      "box_survivors": 5,
      "coordinate_rejects": [
        69505,
        22380,
        7764,
        2408,
        1026,
        471,
        192,
        90,
        33,
        25,
        5,
        4
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        5
      ],
      "raw": 2358720,
      "common_included": 628992,
      "search": 103908,
      "over": 2254812,
      "common_feasible": 24178,
      "valid": 0,
      "box_survivors": 8,
      "coordinate_rejects": [
        69212,
        22477,
        7724,
        2555,
        1095,
        473,
        220,
        86,
        32,
        20,
        6,
        0
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        4,
        4
      ],
      "raw": 1277640,
      "common_included": 340704,
      "search": 58668,
      "over": 1218972,
      "common_feasible": 13734,
      "valid": 0,
      "box_survivors": 3,
      "coordinate_rejects": [
        39033,
        12752,
        4354,
        1466,
        635,
        234,
        107,
        48,
        29,
        4,
        3,
        0
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        8
      ],
      "raw": 196560,
      "common_included": 52416,
      "search": 28944,
      "over": 167616,
      "common_feasible": 7180,
      "valid": 0,
      "box_survivors": 2,
      "coordinate_rejects": [
        19205,
        6360,
        2167,
        668,
        291,
        144,
        70,
        24,
        9,
        4,
        0,
        0
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "raw": 19079424,
      "common_included": 4088448,
      "search": 200028,
      "over": 18879396,
      "common_feasible": 37489,
      "valid": 0,
      "box_survivors": 8,
      "coordinate_rejects": [
        133452,
        43491,
        14838,
        4824,
        1963,
        793,
        343,
        188,
        64,
        37,
        17,
        10
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        5
      ],
      "raw": 4088448,
      "common_included": 876096,
      "search": 164808,
      "over": 3923640,
      "common_feasible": 32049,
      "valid": 0,
      "box_survivors": 6,
      "coordinate_rejects": [
        109783,
        35833,
        12222,
        4070,
        1667,
        729,
        293,
        112,
        62,
        21,
        8,
        2
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "raw": 7547904,
      "common_included": 1617408,
      "search": 290136,
      "over": 7257768,
      "common_feasible": 56164,
      "valid": 0,
      "box_survivors": 11,
      "coordinate_rejects": [
        192940,
        63537,
        21256,
        7495,
        2771,
        1213,
        509,
        225,
        112,
        41,
        12,
        14
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        7
      ],
      "raw": 628992,
      "common_included": 134784,
      "search": 86160,
      "over": 542832,
      "common_feasible": 17482,
      "valid": 0,
      "box_survivors": 4,
      "coordinate_rejects": [
        57191,
        18611,
        6348,
        2365,
        966,
        419,
        150,
        70,
        18,
        14,
        3,
        1
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        3,
        3,
        3
      ],
      "raw": 1589952,
      "common_included": 340704,
      "search": 70044,
      "over": 1519908,
      "common_feasible": 13734,
      "valid": 0,
      "box_survivors": 4,
      "coordinate_rejects": [
        46540,
        15253,
        5262,
        1700,
        751,
        310,
        132,
        34,
        27,
        15,
        12,
        4
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        3,
        6
      ],
      "raw": 628992,
      "common_included": 134784,
      "search": 86160,
      "over": 542832,
      "common_feasible": 17482,
      "valid": 0,
      "box_survivors": 2,
      "coordinate_rejects": [
        57434,
        18687,
        6320,
        2192,
        849,
        420,
        142,
        47,
        36,
        19,
        4,
        8
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        4,
        5
      ],
      "raw": 628992,
      "common_included": 134784,
      "search": 86160,
      "over": 542832,
      "common_feasible": 17482,
      "valid": 0,
      "box_survivors": 3,
      "coordinate_rejects": [
        57325,
        18853,
        6277,
        2254,
        835,
        349,
        135,
        61,
        43,
        13,
        11,
        1
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        2,
        2
      ],
      "raw": 4088448,
      "common_included": 628992,
      "search": 57264,
      "over": 4031184,
      "common_feasible": 8329,
      "valid": 0,
      "box_survivors": 1,
      "coordinate_rejects": [
        38142,
        12957,
        3874,
        1395,
        518,
        220,
        99,
        33,
        14,
        9,
        2,
        0
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        4
      ],
      "raw": 4088448,
      "common_included": 628992,
      "search": 164808,
      "over": 3923640,
      "common_feasible": 24178,
      "valid": 0,
      "box_survivors": 5,
      "coordinate_rejects": [
        109841,
        36418,
        11643,
        4083,
        1647,
        653,
        302,
        117,
        54,
        33,
        6,
        6
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "raw": 5694624,
      "common_included": 876096,
      "search": 218916,
      "over": 5475708,
      "common_feasible": 32049,
      "valid": 0,
      "box_survivors": 15,
      "coordinate_rejects": [
        145798,
        47723,
        15991,
        5516,
        2169,
        907,
        414,
        218,
        105,
        36,
        19,
        5
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "raw": 876096,
      "common_included": 134784,
      "search": 116832,
      "over": 759264,
      "common_feasible": 17482,
      "valid": 0,
      "box_survivors": 12,
      "coordinate_rejects": [
        77582,
        25452,
        8800,
        2924,
        1205,
        486,
        219,
        82,
        40,
        19,
        8,
        3
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "raw": 1617408,
      "common_included": 248832,
      "search": 209784,
      "over": 1407624,
      "common_feasible": 31339,
      "valid": 0,
      "box_survivors": 9,
      "coordinate_rejects": [
        139765,
        45075,
        15899,
        5226,
        2214,
        890,
        446,
        134,
        68,
        33,
        14,
        11
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        4,
        4
      ],
      "raw": 876096,
      "common_included": 134784,
      "search": 116832,
      "over": 759264,
      "common_feasible": 17482,
      "valid": 0,
      "box_survivors": 3,
      "coordinate_rejects": [
        77602,
        25587,
        8625,
        2981,
        1164,
        525,
        191,
        89,
        46,
        13,
        6,
        0
      ]
    },
    {
      "neg_pattern": [
        1,
        1,
        3,
        3,
        4
      ],
      "raw": 876096,
      "common_included": 134784,
      "search": 116832,
      "over": 759264,
      "common_feasible": 17482,
      "valid": 0,
      "box_survivors": 2,
      "coordinate_rejects": [
        77664,
        25350,
        8736,
        2970,
        1243,
        499,
        217,
        85,
        33,
        27,
        3,
        3
      ]
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "raw": 2358720,
      "common_included": 196560,
      "search": 103908,
      "over": 2254812,
      "common_feasible": 8659,
      "valid": 0,
      "box_survivors": 13,
      "coordinate_rejects": [
        69190,
        22848,
        7647,
        2527,
        993,
        390,
        162,
        58,
        32,
        30,
        15,
        3
      ]
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        5
      ],
      "raw": 628992,
      "common_included": 52416,
      "search": 86160,
      "over": 542832,
      "common_feasible": 7180,
      "valid": 0,
      "box_survivors": 5,
      "coordinate_rejects": [
        57393,
        18452,
        6642,
        2142,
        873,
        375,
        173,
        45,
        42,
        10,
        5,
        3
      ]
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "raw": 1617408,
      "common_included": 134784,
      "search": 209784,
      "over": 1407624,
      "common_feasible": 17482,
      "valid": 0,
      "box_survivors": 20,
      "coordinate_rejects": [
        139539,
        45863,
        15450,
        5195,
        2124,
        896,
        377,
        201,
        63,
        36,
        10,
        10
      ]
    },
    {
      "neg_pattern": [
        1,
        2,
        3,
        3,
        3
      ],
      "raw": 628992,
      "common_included": 52416,
      "search": 86160,
      "over": 542832,
      "common_feasible": 7180,
      "valid": 0,
      "box_survivors": 5,
      "coordinate_rejects": [
        57247,
        18894,
        6325,
        2190,
        845,
        389,
        140,
        57,
        36,
        17,
        8,
        7
      ]
    },
    {
      "neg_pattern": [
        2,
        2,
        2,
        2,
        2,
        2
      ],
      "raw": 148512,
      "common_included": 0,
      "search": 9024,
      "over": 139488,
      "common_feasible": 0,
      "valid": 0,
      "box_survivors": 0,
      "coordinate_rejects": [
        6044,
        2066,
        581,
        209,
        74,
        32,
        9,
        6,
        2,
        0,
        1,
        0
      ]
    },
    {
      "neg_pattern": [
        2,
        2,
        2,
        2,
        4
      ],
      "raw": 196560,
      "common_included": 0,
      "search": 28944,
      "over": 167616,
      "common_feasible": 0,
      "valid": 0,
      "box_survivors": 3,
      "coordinate_rejects": [
        19264,
        6385,
        2095,
        717,
        260,
        135,
        51,
        18,
        10,
        3,
        2,
        1
      ]
    },
    {
      "neg_pattern": [
        2,
        2,
        2,
        3,
        3
      ],
      "raw": 340704,
      "common_included": 0,
      "search": 47844,
      "over": 292860,
      "common_feasible": 0,
      "valid": 0,
      "box_survivors": 2,
      "coordinate_rejects": [
        31835,
        10474,
        3488,
        1169,
        488,
        224,
        93,
        36,
        27,
        5,
        2,
        1
      ]
    }
  ],
  "totals": {
    "raw": 503445228,
    "search": 4100436,
    "over": 499344792,
    "common_included": 179004240,
    "common_feasible": 748710,
    "valid": 0,
    "box_survivors": 209
  },
  "coordinate_rejects": [
    2730506,
    893150,
    302566,
    102455,
    41096,
    17451,
    7457,
    2996,
    1469,
    697,
    259,
    125
  ],
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
  ],
  "full": [
    {
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
        1,
        1
      ],
      "p": 4,
      "rs": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        3,
        3,
        3
      ],
      "u": [
        "-175",
        "-2",
        "16",
        "13",
        "16",
        "20",
        "-5",
        "-2",
        "-9",
        "-2",
        "3",
        "-5"
      ],
      "masses": [
        "4481",
        "7185"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
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
      "p": 12,
      "rs": [
        1,
        1,
        1,
        1,
        3,
        3,
        4,
        5,
        1,
        3
      ],
      "u": [
        "28",
        "25",
        "31",
        "22",
        "34",
        "9",
        "2",
        "6",
        "-19",
        "11",
        "-9",
        "1"
      ],
      "masses": [
        "8826",
        "5799"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
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
      "p": 11,
      "rs": [
        1,
        1,
        1,
        2,
        2,
        2,
        4,
        4,
        3,
        3
      ],
      "u": [
        "-108",
        "70",
        "63",
        "7",
        "-17",
        "12",
        "2",
        "-9",
        "-12",
        "5",
        "5",
        "-4"
      ],
      "masses": [
        "7271",
        "7640"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "p": 3,
      "rs": [
        1,
        1,
        1,
        1,
        2,
        4,
        4,
        6,
        1
      ],
      "u": [
        "-196",
        "108",
        "44",
        "-22",
        "-3",
        "-13",
        "-4",
        "-1",
        "-33",
        "-14",
        "2",
        "2"
      ],
      "masses": [
        "5173",
        "13056"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "p": 9,
      "rs": [
        1,
        1,
        1,
        1,
        3,
        3,
        5,
        4,
        2
      ],
      "u": [
        "76",
        "-19",
        "2",
        "17",
        "-8",
        "-1",
        "-21",
        "18",
        "-11",
        "6",
        "8",
        "8"
      ],
      "masses": [
        "7144",
        "6522"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "p": 10,
      "rs": [
        1,
        1,
        1,
        2,
        2,
        4,
        5,
        1,
        4
      ],
      "u": [
        "71",
        "15",
        "46",
        "58",
        "-9",
        "29",
        "-1",
        "0",
        "14",
        "10",
        "4",
        "-3"
      ],
      "masses": [
        "11946",
        "3423"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "p": 1,
      "rs": [
        1,
        1,
        2,
        2,
        3,
        3,
        3,
        2,
        1
      ],
      "u": [
        "-145",
        "28",
        "53",
        "22",
        "-31",
        "-5",
        "0",
        "-1",
        "-10",
        "-5",
        "10",
        "-3"
      ],
      "masses": [
        "5437",
        "8735"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "p": 2,
      "rs": [
        1,
        2,
        2,
        2,
        3,
        3,
        3,
        2,
        1
      ],
      "u": [
        "-145",
        "28",
        "53",
        "22",
        "-31",
        "-5",
        "0",
        "-1",
        "-10",
        "-5",
        "10",
        "-3"
      ],
      "masses": [
        "5450",
        "8748"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "p": 3,
      "rs": [
        1,
        2,
        2,
        3,
        3,
        3,
        3,
        2,
        1
      ],
      "u": [
        "-145",
        "28",
        "53",
        "22",
        "-31",
        "-5",
        "0",
        "-1",
        "-10",
        "-5",
        "10",
        "-3"
      ],
      "masses": [
        "5463",
        "8761"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "p": 4,
      "rs": [
        1,
        2,
        2,
        3,
        3,
        3,
        4,
        2,
        1
      ],
      "u": [
        "-145",
        "28",
        "53",
        "22",
        "-31",
        "-5",
        "0",
        "-1",
        "-10",
        "-5",
        "10",
        "-3"
      ],
      "masses": [
        "5476",
        "8774"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        5
      ],
      "p": 3,
      "rs": [
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        6
      ],
      "u": [
        "-65",
        "43",
        "23",
        "10",
        "17",
        "16",
        "-4",
        "-3",
        "-16",
        "9",
        "4",
        "5"
      ],
      "masses": [
        "7490",
        "5546"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "p": 8,
      "rs": [
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
      "u": [
        "6",
        "-19",
        "30",
        "40",
        "7",
        "18",
        "-11",
        "6",
        "-3",
        "16",
        "16",
        "3"
      ],
      "masses": [
        "10777",
        "3949"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "p": 4,
      "rs": [
        1,
        1,
        1,
        1,
        7,
        7,
        1,
        1,
        2
      ],
      "u": [
        "-7",
        "6",
        "32",
        "-4",
        "-15",
        "5",
        "-8",
        "-4",
        "-4",
        "1",
        "7",
        "1"
      ],
      "masses": [
        "3249",
        "5149"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "p": 4,
      "rs": [
        1,
        2,
        2,
        2,
        2,
        2,
        1,
        3,
        8
      ],
      "u": [
        "-25",
        "73",
        "24",
        "4",
        "2",
        "3",
        "2",
        "6",
        "-22",
        "-3",
        "7",
        "7"
      ],
      "masses": [
        "6397",
        "5557"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "p": 2,
      "rs": [
        1,
        1,
        1,
        1,
        1,
        3,
        1,
        8
      ],
      "u": [
        "-1",
        "9",
        "39",
        "12",
        "28",
        "11",
        "1",
        "4",
        "-14",
        "6",
        "-9",
        "-4"
      ],
      "masses": [
        "6428",
        "5775"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "p": 3,
      "rs": [
        1,
        1,
        1,
        2,
        2,
        8,
        5,
        3
      ],
      "u": [
        "119",
        "50",
        "20",
        "26",
        "25",
        "10",
        "-7",
        "-4",
        "-5",
        "-3",
        "2",
        "-4"
      ],
      "masses": [
        "7625",
        "4948"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "p": 12,
      "rs": [
        1,
        1,
        1,
        3,
        3,
        3,
        10,
        1
      ],
      "u": [
        "69",
        "59",
        "35",
        "28",
        "13",
        "11",
        "13",
        "2",
        "-3",
        "-4",
        "-2",
        "4"
      ],
      "masses": [
        "9060",
        "3467"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "p": 12,
      "rs": [
        1,
        1,
        1,
        4,
        4,
        4,
        1,
        2
      ],
      "u": [
        "-90",
        "8",
        "4",
        "22",
        "4",
        "21",
        "-11",
        "1",
        "-14",
        "11",
        "1",
        "5"
      ],
      "masses": [
        "6110",
        "5948"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "p": 2,
      "rs": [
        1,
        1,
        3,
        3,
        3,
        3,
        1,
        8
      ],
      "u": [
        "-168",
        "115",
        "33",
        "16",
        "-12",
        "1",
        "16",
        "-4",
        "-15",
        "6",
        "-2",
        "2"
      ],
      "masses": [
        "7740",
        "7539"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "p": 6,
      "rs": [
        1,
        2,
        2,
        2,
        3,
        3,
        3,
        6
      ],
      "u": [
        "120",
        "25",
        "-2",
        "6",
        "26",
        "9",
        "-15",
        "8",
        "-1",
        "5",
        "-4",
        "0"
      ],
      "masses": [
        "6443",
        "4416"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "p": 1,
      "rs": [
        1,
        2,
        2,
        3,
        4,
        4,
        4,
        3
      ],
      "u": [
        "-23",
        "17",
        "18",
        "9",
        "17",
        "18",
        "0",
        "-17",
        "-8",
        "3",
        "2",
        "2"
      ],
      "masses": [
        "5204",
        "5274"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        4
      ],
      "p": 8,
      "rs": [
        2,
        2,
        2,
        2,
        2,
        2,
        5,
        6
      ],
      "u": [
        "46",
        "39",
        "-1",
        "14",
        "50",
        "10",
        "18",
        "0",
        "-2",
        "7",
        "-9",
        "11"
      ],
      "masses": [
        "10711",
        "3867"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        3
      ],
      "p": 12,
      "rs": [
        1,
        1,
        1,
        1,
        3,
        5,
        5,
        5
      ],
      "u": [
        "-38",
        "-41",
        "-9",
        "28",
        "9",
        "8",
        "-20",
        "4",
        "-1",
        "-3",
        "2",
        "-1"
      ],
      "masses": [
        "3640",
        "6587"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        3
      ],
      "p": 11,
      "rs": [
        1,
        1,
        1,
        2,
        3,
        5,
        2,
        3
      ],
      "u": [
        "-33",
        "48",
        "24",
        "16",
        "20",
        "-18",
        "9",
        "8",
        "-22",
        "-3",
        "-3",
        "7"
      ],
      "masses": [
        "7238",
        "7401"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        3
      ],
      "p": 12,
      "rs": [
        1,
        1,
        2,
        2,
        2,
        8,
        2,
        5
      ],
      "u": [
        "111",
        "20",
        "36",
        "48",
        "-13",
        "12",
        "4",
        "3",
        "4",
        "6",
        "1",
        "-1"
      ],
      "masses": [
        "8945",
        "3306"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        6
      ],
      "p": 2,
      "rs": [
        1,
        1,
        1,
        1,
        3,
        5,
        2
      ],
      "u": [
        "29",
        "47",
        "22",
        "-6",
        "-7",
        "-1",
        "-7",
        "0",
        "3",
        "-6",
        "1",
        "-5"
      ],
      "masses": [
        "3043",
        "5213"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        1,
        6
      ],
      "p": 3,
      "rs": [
        1,
        1,
        2,
        2,
        4,
        11,
        1
      ],
      "u": [
        "91",
        "46",
        "41",
        "31",
        "0",
        "-9",
        "-1",
        "6",
        "-2",
        "2",
        "-3",
        "6"
      ],
      "masses": [
        "7394",
        "3748"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        3
      ],
      "p": 7,
      "rs": [
        1,
        1,
        1,
        2,
        2,
        1,
        2,
        2
      ],
      "u": [
        "47",
        "-33",
        "20",
        "4",
        "-20",
        "2",
        "-3",
        "-1",
        "8",
        "-11",
        "3",
        "-2"
      ],
      "masses": [
        "3295",
        "6383"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        3
      ],
      "p": 3,
      "rs": [
        1,
        1,
        2,
        4,
        10,
        1,
        2,
        1
      ],
      "u": [
        "142",
        "14",
        "14",
        "4",
        "-7",
        "6",
        "-19",
        "0",
        "15",
        "4",
        "0",
        "0"
      ],
      "masses": [
        "5715",
        "4464"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        3
      ],
      "p": 4,
      "rs": [
        1,
        1,
        3,
        3,
        9,
        2,
        2,
        2
      ],
      "u": [
        "-135",
        "2",
        "27",
        "18",
        "6",
        "14",
        "-18",
        "-4",
        "-27",
        "-5",
        "14",
        "-6"
      ],
      "masses": [
        "5664",
        "10678"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        3
      ],
      "p": 8,
      "rs": [
        1,
        1,
        3,
        4,
        7,
        1,
        4,
        2
      ],
      "u": [
        "-6",
        "29",
        "26",
        "25",
        "-9",
        "-6",
        "2",
        "1",
        "0",
        "-7",
        "-2",
        "-5"
      ],
      "masses": [
        "3543",
        "5391"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        3
      ],
      "p": 1,
      "rs": [
        1,
        2,
        3,
        3,
        7,
        3,
        3,
        1
      ],
      "u": [
        "-50",
        "46",
        "33",
        "-49",
        "-27",
        "-20",
        "2",
        "1",
        "-13",
        "-9",
        "-2",
        "0"
      ],
      "masses": [
        "2868",
        "11639"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        5
      ],
      "p": 9,
      "rs": [
        1,
        1,
        1,
        1,
        7,
        2,
        6
      ],
      "u": [
        "7",
        "-14",
        "6",
        "17",
        "23",
        "3",
        "-3",
        "6",
        "-11",
        "-5",
        "0",
        "1"
      ],
      "masses": [
        "3940",
        "4809"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        5
      ],
      "p": 8,
      "rs": [
        2,
        2,
        2,
        4,
        5,
        2,
        5
      ],
      "u": [
        "4",
        "16",
        "27",
        "7",
        "-2",
        "8",
        "-2",
        "-14",
        "-4",
        "-12",
        "0",
        "-7"
      ],
      "masses": [
        "2719",
        "7154"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        2,
        5
      ],
      "p": 1,
      "rs": [
        2,
        2,
        2,
        4,
        6,
        5,
        2
      ],
      "u": [
        "36",
        "-31",
        "6",
        "19",
        "-4",
        "3",
        "-23",
        "9",
        "-4",
        "-19",
        "6",
        "-6"
      ],
      "masses": [
        "3820",
        "9266"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        3,
        4
      ],
      "p": 6,
      "rs": [
        1,
        1,
        3,
        3,
        3,
        8,
        4
      ],
      "u": [
        "-121",
        "97",
        "23",
        "0",
        "28",
        "-2",
        "16",
        "-1",
        "-24",
        "-1",
        "-4",
        "3"
      ],
      "masses": [
        "7242",
        "7510"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        3,
        4
      ],
      "p": 6,
      "rs": [
        1,
        3,
        4,
        4,
        4,
        6,
        1
      ],
      "u": [
        "43",
        "37",
        "33",
        "18",
        "7",
        "6",
        "20",
        "7",
        "-8",
        "5",
        "2",
        "7"
      ],
      "masses": [
        "9304",
        "3248"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        3,
        4
      ],
      "p": 8,
      "rs": [
        2,
        2,
        2,
        2,
        4,
        2,
        2
      ],
      "u": [
        "-131",
        "17",
        "9",
        "-23",
        "18",
        "-16",
        "-8",
        "12",
        "-11",
        "1",
        "-6",
        "12"
      ],
      "masses": [
        "5416",
        "9054"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        7
      ],
      "p": 9,
      "rs": [
        1,
        1,
        3,
        5,
        5,
        1
      ],
      "u": [
        "-135",
        "39",
        "44",
        "4",
        "-17",
        "14",
        "-1",
        "-5",
        "-7",
        "-1",
        "8",
        "4"
      ],
      "masses": [
        "5970",
        "6484"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        7
      ],
      "p": 6,
      "rs": [
        1,
        1,
        4,
        5,
        5,
        1
      ],
      "u": [
        "-47",
        "-30",
        "53",
        "6",
        "2",
        "4",
        "-6",
        "7",
        "-14",
        "10",
        "-4",
        "7"
      ],
      "masses": [
        "6098",
        "6289"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        7
      ],
      "p": 12,
      "rs": [
        2,
        2,
        5,
        5,
        7,
        1
      ],
      "u": [
        "83",
        "9",
        "39",
        "22",
        "-9",
        "4",
        "3",
        "2",
        "-3",
        "-1",
        "5",
        "-1"
      ],
      "masses": [
        "5643",
        "3516"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2
      ],
      "p": 7,
      "rs": [
        1,
        1,
        2,
        2,
        2,
        2,
        6,
        6
      ],
      "u": [
        "-5",
        "29",
        "-22",
        "-31",
        "26",
        "14",
        "-10",
        "-1",
        "7",
        "-4",
        "-3",
        "3"
      ],
      "masses": [
        "5003",
        "6728"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2
      ],
      "p": 5,
      "rs": [
        1,
        3,
        3,
        7,
        1,
        2,
        3,
        3
      ],
      "u": [
        "-66",
        "15",
        "-9",
        "-12",
        "-4",
        "-6",
        "-13",
        "6",
        "-16",
        "-1",
        "18",
        "8"
      ],
      "masses": [
        "5022",
        "7938"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2
      ],
      "p": 6,
      "rs": [
        2,
        2,
        2,
        2,
        1,
        3,
        5,
        5
      ],
      "u": [
        "114",
        "46",
        "8",
        "8",
        "6",
        "-5",
        "5",
        "-2",
        "-5",
        "-5",
        "-6",
        "-1"
      ],
      "masses": [
        "4310",
        "5129"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2
      ],
      "p": 4,
      "rs": [
        2,
        2,
        3,
        7,
        2,
        2,
        2,
        3
      ],
      "u": [
        "-79",
        "-2",
        "33",
        "-13",
        "-25",
        "0",
        "-21",
        "4",
        "-7",
        "-11",
        "13",
        "2"
      ],
      "masses": [
        "4042",
        "9701"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "p": 7,
      "rs": [
        1,
        1,
        1,
        1,
        1,
        8,
        3
      ],
      "u": [
        "-172",
        "26",
        "40",
        "6",
        "-22",
        "13",
        "-13",
        "-11",
        "-19",
        "0",
        "9",
        "-3"
      ],
      "masses": [
        "5014",
        "10673"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "p": 8,
      "rs": [
        1,
        1,
        1,
        5,
        3,
        4,
        1
      ],
      "u": [
        "103",
        "17",
        "34",
        "34",
        "11",
        "23",
        "0",
        "-7",
        "6",
        "1",
        "3",
        "5"
      ],
      "masses": [
        "9460",
        "2950"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "p": 3,
      "rs": [
        1,
        1,
        1,
        7,
        3,
        4,
        3
      ],
      "u": [
        "72",
        "59",
        "7",
        "3",
        "30",
        "7",
        "21",
        "-2",
        "-3",
        "1",
        "5",
        "5"
      ],
      "masses": [
        "8928",
        "2835"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "p": 8,
      "rs": [
        1,
        1,
        2,
        5,
        1,
        4,
        9
      ],
      "u": [
        "31",
        "54",
        "28",
        "-25",
        "9",
        "-3",
        "-6",
        "2",
        "-10",
        "3",
        "-4",
        "3"
      ],
      "masses": [
        "4692",
        "6094"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "p": 7,
      "rs": [
        1,
        2,
        2,
        4,
        1,
        6,
        4
      ],
      "u": [
        "62",
        "-27",
        "-17",
        "25",
        "10",
        "-4",
        "-2",
        "24",
        "-8",
        "11",
        "3",
        "11"
      ],
      "masses": [
        "8940",
        "5018"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "p": 9,
      "rs": [
        1,
        2,
        3,
        4,
        1,
        6,
        3
      ],
      "u": [
        "-19",
        "26",
        "38",
        "29",
        "-7",
        "11",
        "4",
        "-6",
        "-16",
        "5",
        "12",
        "5"
      ],
      "masses": [
        "8189",
        "5431"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "p": 10,
      "rs": [
        1,
        2,
        4,
        7,
        1,
        2,
        3
      ],
      "u": [
        "-27",
        "-54",
        "-8",
        "-6",
        "-13",
        "4",
        "-29",
        "6",
        "5",
        "-1",
        "13",
        "3"
      ],
      "masses": [
        "4115",
        "8136"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "p": 5,
      "rs": [
        2,
        2,
        2,
        2,
        2,
        4,
        9
      ],
      "u": [
        "-163",
        "29",
        "1",
        "-19",
        "-28",
        "-13",
        "-11",
        "7",
        "-24",
        "-1",
        "9",
        "2"
      ],
      "masses": [
        "3305",
        "11941"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        2,
        4
      ],
      "p": 6,
      "rs": [
        4,
        4,
        4,
        5,
        1,
        3,
        2
      ],
      "u": [
        "29",
        "-1",
        "-9",
        "-16",
        "-13",
        "-9",
        "-8",
        "11",
        "-2",
        "-3",
        "8",
        "6"
      ],
      "masses": [
        "3793",
        "6367"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3,
        3
      ],
      "p": 2,
      "rs": [
        1,
        1,
        1,
        1,
        2,
        6,
        8
      ],
      "u": [
        "-140",
        "-14",
        "12",
        "0",
        "-12",
        "3",
        "-18",
        "14",
        "-2",
        "1",
        "5",
        "5"
      ],
      "masses": [
        "3937",
        "6931"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3,
        3
      ],
      "p": 6,
      "rs": [
        1,
        2,
        2,
        2,
        1,
        2,
        12
      ],
      "u": [
        "49",
        "28",
        "44",
        "42",
        "11",
        "21",
        "-6",
        "-9",
        "-2",
        "10",
        "-4",
        "2"
      ],
      "masses": [
        "9269",
        "4574"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3,
        3
      ],
      "p": 5,
      "rs": [
        1,
        2,
        3,
        7,
        1,
        2,
        2
      ],
      "u": [
        "-52",
        "-7",
        "-20",
        "-18",
        "2",
        "0",
        "-27",
        "13",
        "-2",
        "7",
        "2",
        "3"
      ],
      "masses": [
        "3352",
        "7394"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3,
        3
      ],
      "p": 12,
      "rs": [
        1,
        3,
        4,
        5,
        1,
        3,
        3
      ],
      "u": [
        "-126",
        "-26",
        "16",
        "-3",
        "-14",
        "-13",
        "-12",
        "3",
        "-11",
        "-5",
        "9",
        "2"
      ],
      "masses": [
        "2829",
        "9494"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        6
      ],
      "p": 1,
      "rs": [
        1,
        1,
        1,
        12,
        1,
        1
      ],
      "u": [
        "78",
        "114",
        "-20",
        "-26",
        "10",
        "-2",
        "12",
        "-2",
        "-3",
        "-3",
        "-7",
        "0"
      ],
      "masses": [
        "5687",
        "6418"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        6
      ],
      "p": 10,
      "rs": [
        1,
        1,
        2,
        3,
        1,
        5
      ],
      "u": [
        "-122",
        "34",
        "3",
        "5",
        "-10",
        "-6",
        "-7",
        "5",
        "-13",
        "12",
        "2",
        "4"
      ],
      "masses": [
        "4484",
        "6895"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        6
      ],
      "p": 9,
      "rs": [
        1,
        1,
        5,
        5,
        6,
        5
      ],
      "u": [
        "-66",
        "24",
        "-9",
        "11",
        "33",
        "6",
        "-6",
        "12",
        "-15",
        "18",
        "3",
        "13"
      ],
      "masses": [
        "10019",
        "5735"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        6
      ],
      "p": 8,
      "rs": [
        1,
        1,
        5,
        5,
        7,
        4
      ],
      "u": [
        "-18",
        "-19",
        "37",
        "0",
        "-7",
        "-12",
        "-13",
        "11",
        "-1",
        "2",
        "-2",
        "4"
      ],
      "masses": [
        "3689",
        "5954"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        6
      ],
      "p": 8,
      "rs": [
        2,
        2,
        4,
        4,
        5,
        6
      ],
      "u": [
        "-120",
        "74",
        "7",
        "-23",
        "8",
        "-4",
        "-2",
        "-5",
        "-6",
        "-14",
        "-6",
        "-1"
      ],
      "masses": [
        "2900",
        "9446"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        5
      ],
      "p": 11,
      "rs": [
        1,
        1,
        3,
        8,
        7,
        3
      ],
      "u": [
        "-126",
        "53",
        "33",
        "18",
        "-6",
        "5",
        "2",
        "1",
        "-9",
        "4",
        "-7",
        "1"
      ],
      "masses": [
        "5147",
        "6255"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        5
      ],
      "p": 8,
      "rs": [
        1,
        1,
        4,
        9,
        2,
        3
      ],
      "u": [
        "-132",
        "19",
        "13",
        "29",
        "12",
        "14",
        "-26",
        "3",
        "-14",
        "-6",
        "10",
        "4"
      ],
      "masses": [
        "6915",
        "8604"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        5
      ],
      "p": 4,
      "rs": [
        1,
        2,
        2,
        2,
        1,
        7
      ],
      "u": [
        "-139",
        "45",
        "-20",
        "-21",
        "17",
        "-14",
        "0",
        "-6",
        "-22",
        "-10",
        "2",
        "6"
      ],
      "masses": [
        "3647",
        "11254"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        5
      ],
      "p": 12,
      "rs": [
        1,
        4,
        4,
        4,
        5,
        2
      ],
      "u": [
        "-172",
        "29",
        "57",
        "-20",
        "-24",
        "-15",
        "-16",
        "-6",
        "-7",
        "-8",
        "-1",
        "1"
      ],
      "masses": [
        "3370",
        "12101"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        5
      ],
      "p": 4,
      "rs": [
        2,
        2,
        3,
        8,
        1,
        4
      ],
      "u": [
        "132",
        "-39",
        "24",
        "11",
        "-37",
        "5",
        "-12",
        "5",
        "12",
        "4",
        "6",
        "4"
      ],
      "masses": [
        "7557",
        "6705"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        5
      ],
      "p": 11,
      "rs": [
        2,
        3,
        3,
        4,
        2,
        7
      ],
      "u": [
        "-23",
        "25",
        "32",
        "-17",
        "0",
        "-5",
        "5",
        "-4",
        "-12",
        "-2",
        "5",
        "10"
      ],
      "masses": [
        "4862",
        "5885"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        5
      ],
      "p": 1,
      "rs": [
        3,
        3,
        5,
        10,
        1,
        1
      ],
      "u": [
        "37",
        "-31",
        "20",
        "65",
        "1",
        "26",
        "-16",
        "3",
        "3",
        "13",
        "7",
        "-2"
      ],
      "masses": [
        "10094",
        "4846"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        3,
        5
      ],
      "p": 9,
      "rs": [
        3,
        4,
        5,
        6,
        3,
        1
      ],
      "u": [
        "-123",
        "49",
        "10",
        "27",
        "33",
        "13",
        "9",
        "-2",
        "-22",
        "6",
        "-8",
        "2"
      ],
      "masses": [
        "8274",
        "7678"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        4,
        4
      ],
      "p": 5,
      "rs": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "u": [
        "-88",
        "45",
        "43",
        "-1",
        "25",
        "-1",
        "0",
        "6",
        "-23",
        "6",
        "-10",
        "5"
      ],
      "masses": [
        "6759",
        "7372"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        4,
        4
      ],
      "p": 10,
      "rs": [
        1,
        1,
        1,
        1,
        2,
        10
      ],
      "u": [
        "-69",
        "-26",
        "8",
        "-6",
        "-1",
        "-1",
        "-2",
        "12",
        "-21",
        "3",
        "7",
        "-1"
      ],
      "masses": [
        "3219",
        "6926"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        4,
        4
      ],
      "p": 3,
      "rs": [
        2,
        2,
        5,
        8,
        1,
        1
      ],
      "u": [
        "-119",
        "-14",
        "43",
        "26",
        "4",
        "10",
        "-26",
        "-2",
        "-9",
        "-3",
        "7",
        "-1"
      ],
      "masses": [
        "5187",
        "8179"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        8
      ],
      "p": 6,
      "rs": [
        2,
        2,
        5,
        10,
        2
      ],
      "u": [
        "-66",
        "14",
        "34",
        "-2",
        "-7",
        "5",
        "-9",
        "-3",
        "-13",
        "-10",
        "3",
        "-7"
      ],
      "masses": [
        "2699",
        "8640"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        1,
        8
      ],
      "p": 11,
      "rs": [
        3,
        4,
        4,
        8,
        4
      ],
      "u": [
        "-36",
        "32",
        "11",
        "14",
        "6",
        "-15",
        "-15",
        "5",
        "-25",
        "2",
        "4",
        "3"
      ],
      "masses": [
        "4433",
        "8159"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "p": 11,
      "rs": [
        1,
        1,
        6,
        1,
        5,
        7,
        1
      ],
      "u": [
        "-6",
        "51",
        "-2",
        "-18",
        "-14",
        "6",
        "1",
        "-5",
        "-1",
        "-5",
        "1",
        "-4"
      ],
      "masses": [
        "2280",
        "6165"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "p": 6,
      "rs": [
        1,
        2,
        3,
        2,
        3,
        7,
        5
      ],
      "u": [
        "-80",
        "41",
        "-4",
        "21",
        "4",
        "7",
        "-10",
        "9",
        "1",
        "8",
        "-2",
        "-1"
      ],
      "masses": [
        "5212",
        "4771"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "p": 12,
      "rs": [
        1,
        2,
        4,
        1,
        1,
        2,
        10
      ],
      "u": [
        "-32",
        "-17",
        "0",
        "14",
        "26",
        "22",
        "-9",
        "7",
        "-1",
        "4",
        "-8",
        "-1"
      ],
      "masses": [
        "5633",
        "5320"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "p": 1,
      "rs": [
        1,
        2,
        7,
        1,
        1,
        2,
        7
      ],
      "u": [
        "-11",
        "-17",
        "35",
        "27",
        "-1",
        "10",
        "0",
        "-7",
        "2",
        "-2",
        "6",
        "3"
      ],
      "masses": [
        "5207",
        "3894"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "p": 7,
      "rs": [
        1,
        3,
        3,
        1,
        2,
        7,
        4
      ],
      "u": [
        "12",
        "12",
        "29",
        "56",
        "23",
        "8",
        "-1",
        "3",
        "-18",
        "9",
        "2",
        "2"
      ],
      "masses": [
        "8813",
        "4472"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "p": 2,
      "rs": [
        2,
        2,
        7,
        1,
        1,
        2,
        7
      ],
      "u": [
        "-11",
        "-17",
        "35",
        "27",
        "-1",
        "10",
        "0",
        "-7",
        "2",
        "-2",
        "6",
        "3"
      ],
      "masses": [
        "5220",
        "3907"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "p": 3,
      "rs": [
        2,
        3,
        7,
        1,
        1,
        2,
        7
      ],
      "u": [
        "-11",
        "-17",
        "35",
        "27",
        "-1",
        "10",
        "0",
        "-7",
        "2",
        "-2",
        "6",
        "3"
      ],
      "masses": [
        "5233",
        "3920"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2,
        3
      ],
      "p": 4,
      "rs": [
        3,
        3,
        7,
        1,
        1,
        5,
        1
      ],
      "u": [
        "-63",
        "-26",
        "-15",
        "-13",
        "-5",
        "2",
        "-15",
        "3",
        "-3",
        "7",
        "-1",
        "-5"
      ],
      "masses": [
        "1586",
        "7868"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        5
      ],
      "p": 3,
      "rs": [
        1,
        1,
        7,
        1,
        1,
        3
      ],
      "u": [
        "55",
        "-50",
        "21",
        "42",
        "-1",
        "30",
        "0",
        "-7",
        "1",
        "4",
        "14",
        "-4"
      ],
      "masses": [
        "8737",
        "4859"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        5
      ],
      "p": 12,
      "rs": [
        1,
        1,
        7,
        1,
        4,
        2
      ],
      "u": [
        "143",
        "-29",
        "-2",
        "54",
        "-12",
        "6",
        "-6",
        "7",
        "6",
        "3",
        "11",
        "-5"
      ],
      "masses": [
        "8622",
        "5114"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        5
      ],
      "p": 5,
      "rs": [
        1,
        2,
        3,
        4,
        5,
        4
      ],
      "u": [
        "129",
        "60",
        "-18",
        "18",
        "38",
        "8",
        "12",
        "0",
        "9",
        "-5",
        "-11",
        "3"
      ],
      "masses": [
        "9836",
        "5160"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        5
      ],
      "p": 4,
      "rs": [
        2,
        2,
        2,
        1,
        7,
        8
      ],
      "u": [
        "-142",
        "43",
        "59",
        "-26",
        "-8",
        "-5",
        "1",
        "-7",
        "-13",
        "-6",
        "-2",
        "2"
      ],
      "masses": [
        "3937",
        "9522"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        5
      ],
      "p": 7,
      "rs": [
        2,
        2,
        2,
        2,
        4,
        4
      ],
      "u": [
        "50",
        "48",
        "10",
        "-5",
        "30",
        "3",
        "24",
        "-2",
        "-12",
        "2",
        "1",
        "6"
      ],
      "masses": [
        "8080",
        "4083"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        5
      ],
      "p": 9,
      "rs": [
        2,
        7,
        8,
        2,
        2,
        1
      ],
      "u": [
        "-150",
        "90",
        "28",
        "-39",
        "-6",
        "-25",
        "-1",
        "-3",
        "-23",
        "-18",
        "-5",
        "0"
      ],
      "masses": [
        "3599",
        "14505"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 2,
      "rs": [
        1,
        1,
        1,
        5,
        4,
        4
      ],
      "u": [
        "-56",
        "34",
        "34",
        "2",
        "-21",
        "-6",
        "8",
        "-6",
        "1",
        "-9",
        "-1",
        "2"
      ],
      "masses": [
        "3584",
        "6629"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 1,
      "rs": [
        1,
        1,
        4,
        2,
        1,
        12
      ],
      "u": [
        "124",
        "5",
        "45",
        "34",
        "11",
        "18",
        "18",
        "-2",
        "1",
        "3",
        "-3",
        "-1"
      ],
      "masses": [
        "9451",
        "3082"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 2,
      "rs": [
        1,
        1,
        7,
        2,
        6,
        3
      ],
      "u": [
        "-195",
        "12",
        "5",
        "10",
        "12",
        "27",
        "-15",
        "-2",
        "-5",
        "9",
        "-6",
        "-3"
      ],
      "masses": [
        "5202",
        "8075"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 7,
      "rs": [
        1,
        1,
        9,
        7,
        3,
        1
      ],
      "u": [
        "-23",
        "11",
        "7",
        "13",
        "15",
        "10",
        "-12",
        "2",
        "-13",
        "-11",
        "1",
        "-6"
      ],
      "masses": [
        "3541",
        "7521"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 9,
      "rs": [
        1,
        2,
        2,
        1,
        10,
        1
      ],
      "u": [
        "9",
        "40",
        "3",
        "12",
        "6",
        "-11",
        "10",
        "-2",
        "-3",
        "-9",
        "-1",
        "5"
      ],
      "masses": [
        "4178",
        "4947"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 2,
      "rs": [
        1,
        2,
        4,
        2,
        1,
        12
      ],
      "u": [
        "124",
        "5",
        "45",
        "34",
        "11",
        "18",
        "18",
        "-2",
        "1",
        "3",
        "-3",
        "-1"
      ],
      "masses": [
        "9464",
        "3095"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 1,
      "rs": [
        1,
        2,
        7,
        3,
        3,
        7
      ],
      "u": [
        "-101",
        "25",
        "15",
        "39",
        "-11",
        "24",
        "-23",
        "0",
        "-19",
        "6",
        "14",
        "-3"
      ],
      "masses": [
        "7975",
        "8976"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 3,
      "rs": [
        1,
        3,
        4,
        2,
        1,
        12
      ],
      "u": [
        "124",
        "5",
        "45",
        "34",
        "11",
        "18",
        "18",
        "-2",
        "1",
        "3",
        "-3",
        "-1"
      ],
      "masses": [
        "9477",
        "3108"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 6,
      "rs": [
        2,
        2,
        8,
        5,
        3,
        3
      ],
      "u": [
        "-19",
        "-53",
        "34",
        "14",
        "-18",
        "15",
        "-30",
        "0",
        "6",
        "1",
        "3",
        "-3"
      ],
      "masses": [
        "4658",
        "8191"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 6,
      "rs": [
        2,
        3,
        7,
        1,
        1,
        8
      ],
      "u": [
        "-104",
        "36",
        "27",
        "12",
        "-24",
        "-11",
        "8",
        "0",
        "-15",
        "-2",
        "2",
        "3"
      ],
      "masses": [
        "4253",
        "7937"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        3,
        4
      ],
      "p": 5,
      "rs": [
        2,
        6,
        6,
        1,
        1,
        5
      ],
      "u": [
        "-25",
        "61",
        "-2",
        "23",
        "13",
        "5",
        "-4",
        "-1",
        "-5",
        "13",
        "1",
        "5"
      ],
      "masses": [
        "6742",
        "3714"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        7
      ],
      "p": 9,
      "rs": [
        1,
        1,
        8,
        4,
        9
      ],
      "u": [
        "-210",
        "70",
        "35",
        "8",
        "-6",
        "9",
        "11",
        "-10",
        "-8",
        "2",
        "0",
        "2"
      ],
      "masses": [
        "6024",
        "7184"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        7
      ],
      "p": 3,
      "rs": [
        1,
        1,
        11,
        1,
        4
      ],
      "u": [
        "-20",
        "-27",
        "17",
        "-3",
        "20",
        "8",
        "3",
        "0",
        "1",
        "3",
        "-7",
        "1"
      ],
      "masses": [
        "3677",
        "4319"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        7
      ],
      "p": 4,
      "rs": [
        1,
        2,
        5,
        3,
        11
      ],
      "u": [
        "-11",
        "21",
        "42",
        "21",
        "-23",
        "-4",
        "8",
        "-9",
        "-15",
        "-11",
        "10",
        "1"
      ],
      "masses": [
        "5707",
        "8307"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        2,
        7
      ],
      "p": 11,
      "rs": [
        1,
        7,
        8,
        1,
        6
      ],
      "u": [
        "-73",
        "42",
        "32",
        "-20",
        "15",
        "-11",
        "-2",
        "-2",
        "-17",
        "-3",
        "2",
        "8"
      ],
      "masses": [
        "5061",
        "7810"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        3,
        3,
        3
      ],
      "p": 8,
      "rs": [
        1,
        3,
        3,
        3,
        3,
        8
      ],
      "u": [
        "-61",
        "108",
        "9",
        "-20",
        "-6",
        "-5",
        "5",
        "-9",
        "-14",
        "-15",
        "6",
        "-3"
      ],
      "masses": [
        "4616",
        "9767"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        3,
        3,
        3
      ],
      "p": 2,
      "rs": [
        1,
        3,
        4,
        1,
        3,
        3
      ],
      "u": [
        "3",
        "28",
        "-12",
        "3",
        "12",
        "13",
        "3",
        "-2",
        "4",
        "3",
        "-3",
        "5"
      ],
      "masses": [
        "4748",
        "3305"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        3,
        3,
        3
      ],
      "p": 8,
      "rs": [
        1,
        4,
        4,
        4,
        4,
        4
      ],
      "u": [
        "30",
        "21",
        "-10",
        "21",
        "2",
        "-2",
        "-10",
        "24",
        "-3",
        "9",
        "0",
        "8"
      ],
      "masses": [
        "7229",
        "4077"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        3,
        3,
        3
      ],
      "p": 10,
      "rs": [
        3,
        3,
        12,
        1,
        1,
        2
      ],
      "u": [
        "-36",
        "40",
        "-11",
        "22",
        "37",
        "11",
        "-7",
        "3",
        "-18",
        "-1",
        "0",
        "1"
      ],
      "masses": [
        "6099",
        "6005"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        3,
        6
      ],
      "p": 3,
      "rs": [
        2,
        2,
        5,
        5,
        7
      ],
      "u": [
        "167",
        "47",
        "15",
        "6",
        "30",
        "7",
        "15",
        "-2",
        "11",
        "-5",
        "-11",
        "3"
      ],
      "masses": [
        "9812",
        "4709"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        3,
        6
      ],
      "p": 7,
      "rs": [
        3,
        4,
        5,
        7,
        2
      ],
      "u": [
        "25",
        "24",
        "25",
        "25",
        "7",
        "4",
        "1",
        "-3",
        "9",
        "-9",
        "0",
        "-3"
      ],
      "masses": [
        "5274",
        "4231"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        4,
        5
      ],
      "p": 2,
      "rs": [
        1,
        3,
        5,
        2,
        5
      ],
      "u": [
        "-44",
        "42",
        "14",
        "10",
        "10",
        "8",
        "-12",
        "-1",
        "-12",
        "-7",
        "-2",
        "6"
      ],
      "masses": [
        "4472",
        "6521"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        4,
        5
      ],
      "p": 6,
      "rs": [
        1,
        4,
        8,
        3,
        2
      ],
      "u": [
        "95",
        "15",
        "3",
        "-18",
        "27",
        "-19",
        "6",
        "12",
        "1",
        "-7",
        "-4",
        "4"
      ],
      "masses": [
        "6115",
        "6109"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        1,
        4,
        5
      ],
      "p": 9,
      "rs": [
        2,
        2,
        2,
        6,
        10
      ],
      "u": [
        "115",
        "28",
        "30",
        "15",
        "4",
        "10",
        "1",
        "5",
        "-6",
        "10",
        "1",
        "11"
      ],
      "masses": [
        "9038",
        "3005"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        2,
        2
      ],
      "p": 12,
      "rs": [
        1,
        10,
        1,
        1,
        1,
        1,
        1
      ],
      "u": [
        "-102",
        "79",
        "41",
        "3",
        "7",
        "-2",
        "-8",
        "-8",
        "-22",
        "-4",
        "-1",
        "1"
      ],
      "masses": [
        "4613",
        "8361"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        4
      ],
      "p": 8,
      "rs": [
        1,
        2,
        1,
        2,
        2,
        6
      ],
      "u": [
        "61",
        "55",
        "5",
        "-2",
        "-10",
        "-2",
        "-11",
        "12",
        "-7",
        "5",
        "4",
        "11"
      ],
      "masses": [
        "6723",
        "4902"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        4
      ],
      "p": 3,
      "rs": [
        1,
        7,
        2,
        3,
        8,
        2
      ],
      "u": [
        "-47",
        "70",
        "30",
        "-11",
        "-18",
        "-10",
        "-11",
        "-9",
        "-9",
        "-4",
        "5",
        "0"
      ],
      "masses": [
        "3807",
        "8845"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        4
      ],
      "p": 6,
      "rs": [
        1,
        9,
        1,
        3,
        3,
        3
      ],
      "u": [
        "0",
        "101",
        "14",
        "23",
        "-2",
        "5",
        "16",
        "6",
        "-5",
        "3",
        "-3",
        "4"
      ],
      "masses": [
        "7926",
        "3416"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        4
      ],
      "p": 10,
      "rs": [
        2,
        2,
        2,
        5,
        10,
        1
      ],
      "u": [
        "-3",
        "4",
        "1",
        "17",
        "-11",
        "-8",
        "-7",
        "10",
        "-8",
        "6",
        "11",
        "9"
      ],
      "masses": [
        "6064",
        "5222"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        2,
        4
      ],
      "p": 10,
      "rs": [
        2,
        7,
        2,
        2,
        3,
        6
      ],
      "u": [
        "-84",
        "0",
        "27",
        "16",
        "-3",
        "10",
        "-18",
        "4",
        "-14",
        "6",
        "6",
        "4"
      ],
      "masses": [
        "5568",
        "6752"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 6,
      "rs": [
        1,
        1,
        1,
        2,
        4,
        10
      ],
      "u": [
        "57",
        "68",
        "-16",
        "-40",
        "18",
        "-11",
        "2",
        "-1",
        "-8",
        "-5",
        "-6",
        "9"
      ],
      "masses": [
        "5357",
        "8292"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 6,
      "rs": [
        1,
        1,
        1,
        5,
        3,
        4
      ],
      "u": [
        "-156",
        "38",
        "35",
        "18",
        "-16",
        "14",
        "-12",
        "2",
        "-18",
        "15",
        "8",
        "2"
      ],
      "masses": [
        "8109",
        "8281"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 9,
      "rs": [
        1,
        2,
        4,
        4,
        5,
        6
      ],
      "u": [
        "-11",
        "-19",
        "-21",
        "30",
        "-13",
        "22",
        "-23",
        "0",
        "-5",
        "3",
        "15",
        "-2"
      ],
      "masses": [
        "6026",
        "7505"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 7,
      "rs": [
        1,
        3,
        2,
        3,
        2,
        11
      ],
      "u": [
        "-74",
        "61",
        "27",
        "-8",
        "-24",
        "-24",
        "7",
        "7",
        "-23",
        "-16",
        "8",
        "0"
      ],
      "masses": [
        "5297",
        "11720"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 5,
      "rs": [
        1,
        7,
        2,
        9,
        1,
        1
      ],
      "u": [
        "79",
        "-26",
        "16",
        "14",
        "-12",
        "-2",
        "-7",
        "11",
        "1",
        "5",
        "1",
        "9"
      ],
      "masses": [
        "5934",
        "4497"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 2,
      "rs": [
        1,
        9,
        3,
        6,
        1,
        1
      ],
      "u": [
        "76",
        "12",
        "6",
        "18",
        "16",
        "16",
        "7",
        "5",
        "-16",
        "4",
        "3",
        "2"
      ],
      "masses": [
        "7205",
        "4151"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 2,
      "rs": [
        1,
        10,
        1,
        4,
        1,
        3
      ],
      "u": [
        "160",
        "8",
        "11",
        "-3",
        "13",
        "7",
        "7",
        "-5",
        "21",
        "3",
        "-11",
        "3"
      ],
      "masses": [
        "8021",
        "4512"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 8,
      "rs": [
        2,
        3,
        2,
        7,
        1,
        4
      ],
      "u": [
        "-13",
        "-3",
        "10",
        "25",
        "31",
        "16",
        "-5",
        "2",
        "-8",
        "6",
        "-8",
        "1"
      ],
      "masses": [
        "6278",
        "5014"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 10,
      "rs": [
        2,
        7,
        2,
        2,
        4,
        6
      ],
      "u": [
        "5",
        "12",
        "-20",
        "-24",
        "11",
        "-13",
        "6",
        "9",
        "-10",
        "1",
        "-1",
        "2"
      ],
      "masses": [
        "3268",
        "6608"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 1,
      "rs": [
        2,
        7,
        2,
        6,
        3,
        3
      ],
      "u": [
        "36",
        "34",
        "27",
        "33",
        "23",
        "24",
        "5",
        "-9",
        "-4",
        "6",
        "-6",
        "-4"
      ],
      "masses": [
        "8716",
        "5184"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 8,
      "rs": [
        3,
        6,
        1,
        2,
        5,
        5
      ],
      "u": [
        "-117",
        "22",
        "40",
        "24",
        "6",
        "17",
        "-1",
        "-4",
        "-2",
        "6",
        "0",
        "-3"
      ],
      "masses": [
        "6033",
        "4911"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 1,
      "rs": [
        3,
        7,
        2,
        4,
        2,
        3
      ],
      "u": [
        "-78",
        "-13",
        "-36",
        "9",
        "5",
        "10",
        "-15",
        "-5",
        "-1",
        "-12",
        "4",
        "-1"
      ],
      "masses": [
        "2298",
        "8608"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 9,
      "rs": [
        4,
        7,
        1,
        2,
        3,
        3
      ],
      "u": [
        "-7",
        "-9",
        "5",
        "14",
        "5",
        "9",
        "-7",
        "10",
        "-13",
        "-5",
        "8",
        "-3"
      ],
      "masses": [
        "4368",
        "5839"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 12,
      "rs": [
        4,
        8,
        2,
        7,
        1,
        1
      ],
      "u": [
        "-32",
        "5",
        "43",
        "6",
        "-9",
        "-1",
        "-6",
        "2",
        "-10",
        "-6",
        "6",
        "-5"
      ],
      "masses": [
        "3447",
        "6607"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3,
        3
      ],
      "p": 7,
      "rs": [
        4,
        10,
        2,
        3,
        1,
        1
      ],
      "u": [
        "-61",
        "-51",
        "0",
        "35",
        "-8",
        "23",
        "-25",
        "5",
        "-6",
        "13",
        "10",
        "4"
      ],
      "masses": [
        "8047",
        "7760"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 6,
      "rs": [
        1,
        2,
        3,
        4,
        6
      ],
      "u": [
        "-59",
        "59",
        "45",
        "12",
        "-16",
        "1",
        "-5",
        "7",
        "-13",
        "10",
        "4",
        "5"
      ],
      "masses": [
        "7474",
        "5921"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 10,
      "rs": [
        1,
        3,
        1,
        4,
        6
      ],
      "u": [
        "-2",
        "43",
        "13",
        "8",
        "4",
        "-6",
        "-6",
        "6",
        "-10",
        "3",
        "0",
        "5"
      ],
      "masses": [
        "4311",
        "4404"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 3,
      "rs": [
        1,
        5,
        2,
        4,
        9
      ],
      "u": [
        "61",
        "-6",
        "38",
        "29",
        "0",
        "13",
        "-10",
        "6",
        "10",
        "13",
        "0",
        "-5"
      ],
      "masses": [
        "8318",
        "4121"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 4,
      "rs": [
        1,
        5,
        2,
        5,
        4
      ],
      "u": [
        "7",
        "-18",
        "33",
        "12",
        "23",
        "12",
        "-18",
        "3",
        "-5",
        "1",
        "1",
        "5"
      ],
      "masses": [
        "5921",
        "4894"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 4,
      "rs": [
        1,
        7,
        1,
        1,
        1
      ],
      "u": [
        "-120",
        "93",
        "68",
        "1",
        "-18",
        "-9",
        "-7",
        "-3",
        "-14",
        "2",
        "-3",
        "1"
      ],
      "masses": [
        "5593",
        "8440"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 12,
      "rs": [
        1,
        7,
        1,
        5,
        6
      ],
      "u": [
        "40",
        "47",
        "8",
        "8",
        "20",
        "8",
        "-6",
        "6",
        "-3",
        "-8",
        "-1",
        "1"
      ],
      "masses": [
        "5360",
        "4345"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 1,
      "rs": [
        2,
        5,
        2,
        9,
        1
      ],
      "u": [
        "21",
        "-8",
        "50",
        "-1",
        "-9",
        "-9",
        "10",
        "4",
        "8",
        "8",
        "-16",
        "1"
      ],
      "masses": [
        "5760",
        "6062"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 9,
      "rs": [
        3,
        3,
        5,
        8,
        4
      ],
      "u": [
        "27",
        "-31",
        "27",
        "21",
        "8",
        "12",
        "-12",
        "15",
        "-3",
        "13",
        "-2",
        "9"
      ],
      "masses": [
        "8759",
        "4809"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 9,
      "rs": [
        3,
        8,
        2,
        6,
        4
      ],
      "u": [
        "-139",
        "19",
        "22",
        "-9",
        "-15",
        "8",
        "-17",
        "-8",
        "3",
        "-7",
        "-1",
        "-3"
      ],
      "masses": [
        "2560",
        "9273"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 10,
      "rs": [
        4,
        5,
        4,
        7,
        2
      ],
      "u": [
        "-40",
        "17",
        "32",
        "37",
        "24",
        "16",
        "-16",
        "-1",
        "0",
        "8",
        "0",
        "1"
      ],
      "masses": [
        "7781",
        "4332"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 6,
      "rs": [
        4,
        7,
        2,
        6,
        1
      ],
      "u": [
        "-84",
        "20",
        "42",
        "-16",
        "-28",
        "-8",
        "-3",
        "1",
        "-5",
        "-16",
        "6",
        "2"
      ],
      "masses": [
        "3607",
        "9429"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        2,
        6
      ],
      "p": 10,
      "rs": [
        5,
        8,
        1,
        6,
        1
      ],
      "u": [
        "62",
        "30",
        "45",
        "16",
        "2",
        "13",
        "-4",
        "-2",
        "-2",
        "17",
        "5",
        "8"
      ],
      "masses": [
        "9590",
        "3094"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "p": 6,
      "rs": [
        1,
        3,
        7,
        3,
        2
      ],
      "u": [
        "181",
        "-4",
        "7",
        "44",
        "25",
        "25",
        "-6",
        "10",
        "-8",
        "13",
        "0",
        "-3"
      ],
      "masses": [
        "11160",
        "4264"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "p": 2,
      "rs": [
        1,
        6,
        1,
        1,
        10
      ],
      "u": [
        "16",
        "50",
        "-2",
        "10",
        "-4",
        "4",
        "-11",
        "2",
        "8",
        "3",
        "1",
        "-2"
      ],
      "masses": [
        "4117",
        "3902"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "p": 5,
      "rs": [
        1,
        8,
        3,
        1,
        5
      ],
      "u": [
        "109",
        "1",
        "12",
        "-13",
        "4",
        "-3",
        "-16",
        "7",
        "10",
        "-7",
        "2",
        "3"
      ],
      "masses": [
        "4908",
        "5494"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "p": 5,
      "rs": [
        2,
        6,
        2,
        10,
        1
      ],
      "u": [
        "-13",
        "-27",
        "54",
        "39",
        "-10",
        "23",
        "-21",
        "5",
        "-12",
        "15",
        "6",
        "-3"
      ],
      "masses": [
        "9347",
        "7514"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "p": 12,
      "rs": [
        3,
        3,
        3,
        4,
        3
      ],
      "u": [
        "132",
        "33",
        "-2",
        "16",
        "-17",
        "2",
        "-8",
        "11",
        "12",
        "1",
        "3",
        "-1"
      ],
      "masses": [
        "6783",
        "4270"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "p": 1,
      "rs": [
        3,
        4,
        1,
        2,
        4
      ],
      "u": [
        "-106",
        "-6",
        "7",
        "-4",
        "2",
        "4",
        "-28",
        "-1",
        "-6",
        "-3",
        "6",
        "0"
      ],
      "masses": [
        "1735",
        "7537"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "p": 7,
      "rs": [
        3,
        4,
        1,
        3,
        1
      ],
      "u": [
        "163",
        "23",
        "8",
        "-24",
        "-6",
        "-7",
        "2",
        "0",
        "2",
        "-3",
        "-5",
        "-3"
      ],
      "masses": [
        "3506",
        "5888"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "p": 9,
      "rs": [
        3,
        7,
        2,
        6,
        1
      ],
      "u": [
        "39",
        "-7",
        "11",
        "14",
        "19",
        "2",
        "9",
        "10",
        "-3",
        "10",
        "-12",
        "0"
      ],
      "masses": [
        "6385",
        "4497"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        3,
        5
      ],
      "p": 3,
      "rs": [
        4,
        4,
        2,
        1,
        2
      ],
      "u": [
        "-10",
        "-1",
        "51",
        "-7",
        "-2",
        "10",
        "-12",
        "3",
        "-8",
        "-2",
        "6",
        "-7"
      ],
      "masses": [
        "4076",
        "6173"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        4,
        4
      ],
      "p": 7,
      "rs": [
        2,
        2,
        9,
        1,
        2
      ],
      "u": [
        "-64",
        "89",
        "-4",
        "43",
        "51",
        "29",
        "-6",
        "-4",
        "-8",
        "18",
        "-6",
        "-1"
      ],
      "masses": [
        "12496",
        "6038"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        4,
        4
      ],
      "p": 5,
      "rs": [
        2,
        3,
        8,
        3,
        4
      ],
      "u": [
        "-26",
        "-15",
        "47",
        "16",
        "-14",
        "10",
        "4",
        "-8",
        "8",
        "4",
        "-3",
        "5"
      ],
      "masses": [
        "6184",
        "5116"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        4,
        4
      ],
      "p": 1,
      "rs": [
        3,
        6,
        1,
        3,
        6
      ],
      "u": [
        "-8",
        "-71",
        "38",
        "15",
        "-31",
        "18",
        "-23",
        "5",
        "-1",
        "4",
        "13",
        "-7"
      ],
      "masses": [
        "6653",
        "9396"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        3,
        3,
        4
      ],
      "p": 9,
      "rs": [
        1,
        1,
        4,
        4,
        5
      ],
      "u": [
        "-65",
        "91",
        "-13",
        "-7",
        "5",
        "-5",
        "-13",
        "10",
        "-23",
        "3",
        "3",
        "3"
      ],
      "masses": [
        "5188",
        "8072"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        1,
        3,
        3,
        4
      ],
      "p": 5,
      "rs": [
        2,
        10,
        2,
        3,
        2
      ],
      "u": [
        "-167",
        "-19",
        "8",
        "26",
        "-15",
        "19",
        "-23",
        "-5",
        "-18",
        "-6",
        "18",
        "2"
      ],
      "masses": [
        "6192",
        "11156"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 1,
      "rs": [
        1,
        1,
        1,
        4,
        4,
        4
      ],
      "u": [
        "-81",
        "23",
        "45",
        "-3",
        "4",
        "-5",
        "-18",
        "4",
        "-22",
        "-2",
        "0",
        "-2"
      ],
      "masses": [
        "3134",
        "8467"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 5,
      "rs": [
        1,
        1,
        2,
        4,
        6,
        1
      ],
      "u": [
        "59",
        "86",
        "6",
        "-38",
        "12",
        "-9",
        "16",
        "0",
        "0",
        "-7",
        "-6",
        "4"
      ],
      "masses": [
        "6147",
        "6603"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 12,
      "rs": [
        2,
        1,
        1,
        1,
        10,
        6
      ],
      "u": [
        "-4",
        "-28",
        "19",
        "50",
        "4",
        "15",
        "-13",
        "3",
        "-10",
        "4",
        "12",
        "0"
      ],
      "masses": [
        "7536",
        "5373"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 2,
      "rs": [
        2,
        1,
        1,
        4,
        4,
        4
      ],
      "u": [
        "-81",
        "23",
        "45",
        "-3",
        "4",
        "-5",
        "-18",
        "4",
        "-22",
        "-2",
        "0",
        "-2"
      ],
      "masses": [
        "3147",
        "8480"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 3,
      "rs": [
        3,
        1,
        1,
        4,
        4,
        4
      ],
      "u": [
        "-81",
        "23",
        "45",
        "-3",
        "4",
        "-5",
        "-18",
        "4",
        "-22",
        "-2",
        "0",
        "-2"
      ],
      "masses": [
        "3160",
        "8493"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 4,
      "rs": [
        4,
        1,
        1,
        4,
        4,
        4
      ],
      "u": [
        "-81",
        "23",
        "45",
        "-3",
        "4",
        "-5",
        "-18",
        "4",
        "-22",
        "-2",
        "0",
        "-2"
      ],
      "masses": [
        "3173",
        "8506"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 5,
      "rs": [
        5,
        1,
        1,
        4,
        4,
        4
      ],
      "u": [
        "-81",
        "23",
        "45",
        "-3",
        "4",
        "-5",
        "-18",
        "4",
        "-22",
        "-2",
        "0",
        "-2"
      ],
      "masses": [
        "3186",
        "8519"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 6,
      "rs": [
        6,
        1,
        1,
        4,
        4,
        4
      ],
      "u": [
        "-81",
        "23",
        "45",
        "-3",
        "4",
        "-5",
        "-18",
        "4",
        "-22",
        "-2",
        "0",
        "-2"
      ],
      "masses": [
        "3199",
        "8532"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 10,
      "rs": [
        7,
        1,
        1,
        1,
        12,
        1
      ],
      "u": [
        "77",
        "-43",
        "8",
        "18",
        "-9",
        "-3",
        "-14",
        "8",
        "-8",
        "-9",
        "12",
        "-2"
      ],
      "masses": [
        "4972",
        "7862"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 7,
      "rs": [
        7,
        1,
        1,
        4,
        4,
        4
      ],
      "u": [
        "-81",
        "23",
        "45",
        "-3",
        "4",
        "-5",
        "-18",
        "4",
        "-22",
        "-2",
        "0",
        "-2"
      ],
      "masses": [
        "3212",
        "8545"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 6,
      "rs": [
        8,
        1,
        1,
        1,
        6,
        5
      ],
      "u": [
        "-47",
        "20",
        "14",
        "-2",
        "-14",
        "9",
        "7",
        "0",
        "-1",
        "-5",
        "4",
        "3"
      ],
      "masses": [
        "3634",
        "4631"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 8,
      "rs": [
        8,
        1,
        1,
        4,
        4,
        4
      ],
      "u": [
        "-81",
        "23",
        "45",
        "-3",
        "4",
        "-5",
        "-18",
        "4",
        "-22",
        "-2",
        "0",
        "-2"
      ],
      "masses": [
        "3225",
        "8558"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2,
        3
      ],
      "p": 9,
      "rs": [
        9,
        1,
        1,
        4,
        4,
        4
      ],
      "u": [
        "-81",
        "23",
        "45",
        "-3",
        "4",
        "-5",
        "-18",
        "4",
        "-22",
        "-2",
        "0",
        "-2"
      ],
      "masses": [
        "3238",
        "8571"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        5
      ],
      "p": 12,
      "rs": [
        2,
        1,
        3,
        3,
        2
      ],
      "u": [
        "67",
        "-17",
        "12",
        "-8",
        "-8",
        "7",
        "0",
        "-5",
        "19",
        "0",
        "-7",
        "-3"
      ],
      "masses": [
        "4327",
        "5485"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        5
      ],
      "p": 1,
      "rs": [
        3,
        1,
        2,
        2,
        3
      ],
      "u": [
        "-39",
        "-13",
        "32",
        "34",
        "-4",
        "18",
        "-24",
        "-8",
        "-10",
        "-10",
        "12",
        "0"
      ],
      "masses": [
        "6221",
        "8649"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        5
      ],
      "p": 1,
      "rs": [
        3,
        1,
        4,
        5,
        1
      ],
      "u": [
        "-59",
        "-70",
        "-4",
        "20",
        "-15",
        "1",
        "-21",
        "7",
        "-9",
        "-1",
        "15",
        "-2"
      ],
      "masses": [
        "4129",
        "9148"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        5
      ],
      "p": 2,
      "rs": [
        4,
        1,
        1,
        3,
        2
      ],
      "u": [
        "-193",
        "113",
        "44",
        "5",
        "6",
        "-3",
        "16",
        "-12",
        "-24",
        "0",
        "-7",
        "-1"
      ],
      "masses": [
        "6770",
        "9882"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        2,
        5
      ],
      "p": 7,
      "rs": [
        4,
        4,
        4,
        5,
        5
      ],
      "u": [
        "7",
        "51",
        "30",
        "-6",
        "-1",
        "-7",
        "15",
        "-11",
        "-1",
        "-3",
        "4",
        "0"
      ],
      "masses": [
        "4676",
        "4854"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 1,
      "rs": [
        1,
        1,
        1,
        1,
        4
      ],
      "u": [
        "-110",
        "51",
        "-24",
        "-18",
        "-20",
        "2",
        "-20",
        "0",
        "-3",
        "-9",
        "4",
        "-10"
      ],
      "masses": [
        "2178",
        "11416"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 9,
      "rs": [
        1,
        1,
        3,
        4,
        5
      ],
      "u": [
        "-84",
        "53",
        "-3",
        "14",
        "25",
        "1",
        "-9",
        "9",
        "-19",
        "-4",
        "3",
        "11"
      ],
      "masses": [
        "7059",
        "6857"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 12,
      "rs": [
        1,
        3,
        7,
        9,
        1
      ],
      "u": [
        "-27",
        "-31",
        "12",
        "8",
        "-2",
        "3",
        "-9",
        "14",
        "-9",
        "0",
        "10",
        "3"
      ],
      "masses": [
        "4746",
        "5377"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 1,
      "rs": [
        1,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4774",
        "9250"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 2,
      "rs": [
        2,
        1,
        1,
        1,
        4
      ],
      "u": [
        "-110",
        "51",
        "-24",
        "-18",
        "-20",
        "2",
        "-20",
        "0",
        "-3",
        "-9",
        "4",
        "-10"
      ],
      "masses": [
        "2191",
        "11429"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 4,
      "rs": [
        2,
        2,
        5,
        3,
        5
      ],
      "u": [
        "0",
        "37",
        "17",
        "31",
        "25",
        "6",
        "7",
        "-7",
        "-10",
        "6",
        "-3",
        "4"
      ],
      "masses": [
        "7458",
        "4551"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 2,
      "rs": [
        2,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4787",
        "9263"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 6,
      "rs": [
        3,
        1,
        2,
        1,
        2
      ],
      "u": [
        "-112",
        "18",
        "55",
        "-6",
        "-27",
        "12",
        "-18",
        "-8",
        "-6",
        "-9",
        "14",
        "-7"
      ],
      "masses": [
        "5698",
        "10904"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 3,
      "rs": [
        3,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4800",
        "9276"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 10,
      "rs": [
        4,
        1,
        3,
        4,
        11
      ],
      "u": [
        "-103",
        "87",
        "11",
        "-14",
        "-1",
        "5",
        "-2",
        "-12",
        "-11",
        "-7",
        "6",
        "1"
      ],
      "masses": [
        "4283",
        "7931"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 4,
      "rs": [
        4,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4813",
        "9289"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 5,
      "rs": [
        5,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4826",
        "9302"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 9,
      "rs": [
        6,
        3,
        10,
        1,
        2
      ],
      "u": [
        "-145",
        "-21",
        "44",
        "0",
        "-19",
        "11",
        "-4",
        "-11",
        "-2",
        "-7",
        "3",
        "4"
      ],
      "masses": [
        "3850",
        "8418"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 6,
      "rs": [
        6,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4839",
        "9315"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 7,
      "rs": [
        7,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4852",
        "9328"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 6,
      "rs": [
        8,
        1,
        4,
        2,
        1
      ],
      "u": [
        "97",
        "7",
        "-35",
        "-32",
        "21",
        "-11",
        "15",
        "0",
        "4",
        "-8",
        "-3",
        "5"
      ],
      "masses": [
        "5518",
        "7498"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 8,
      "rs": [
        8,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4865",
        "9341"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 9,
      "rs": [
        9,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4878",
        "9354"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 10,
      "rs": [
        10,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4891",
        "9367"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        3,
        4
      ],
      "p": 11,
      "rs": [
        11,
        5,
        5,
        1,
        1
      ],
      "u": [
        "-56",
        "79",
        "2",
        "-12",
        "13",
        "-9",
        "19",
        "-3",
        "-18",
        "-14",
        "-4",
        "-2"
      ],
      "masses": [
        "4904",
        "9380"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        3,
        3,
        3
      ],
      "p": 5,
      "rs": [
        1,
        2,
        2,
        3,
        4
      ],
      "u": [
        "123",
        "-13",
        "9",
        "21",
        "-13",
        "5",
        "-23",
        "11",
        "4",
        "-6",
        "16",
        "3"
      ],
      "masses": [
        "7841",
        "6180"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        3,
        3,
        3
      ],
      "p": 11,
      "rs": [
        2,
        7,
        3,
        4,
        4
      ],
      "u": [
        "11",
        "17",
        "44",
        "39",
        "-15",
        "-2",
        "2",
        "1",
        "-20",
        "5",
        "12",
        "3"
      ],
      "masses": [
        "7626",
        "5717"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        3,
        3,
        3
      ],
      "p": 2,
      "rs": [
        3,
        6,
        3,
        3,
        6
      ],
      "u": [
        "-149",
        "34",
        "-18",
        "14",
        "-18",
        "-3",
        "-7",
        "1",
        "-8",
        "-5",
        "11",
        "4"
      ],
      "masses": [
        "4043",
        "8354"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        3,
        3,
        3
      ],
      "p": 5,
      "rs": [
        4,
        1,
        1,
        2,
        8
      ],
      "u": [
        "-81",
        "91",
        "15",
        "13",
        "3",
        "18",
        "13",
        "-3",
        "-15",
        "2",
        "-1",
        "-6"
      ],
      "masses": [
        "6747",
        "6324"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        1,
        2,
        3,
        3,
        3
      ],
      "p": 4,
      "rs": [
        11,
        4,
        1,
        1,
        4
      ],
      "u": [
        "-101",
        "116",
        "41",
        "-5",
        "6",
        "0",
        "23",
        "-5",
        "-9",
        "-2",
        "-7",
        "3"
      ],
      "masses": [
        "7597",
        "6574"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        2,
        2,
        2,
        2,
        4
      ],
      "p": 10,
      "rs": [
        1,
        1,
        5,
        6,
        7
      ],
      "u": [
        "126",
        "-7",
        "23",
        "32",
        "3",
        "19",
        "-3",
        "5",
        "8",
        "11",
        "3",
        "0"
      ],
      "masses": [
        "9259",
        "2728"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        2,
        2,
        2,
        2,
        4
      ],
      "p": 3,
      "rs": [
        1,
        2,
        3,
        5,
        4
      ],
      "u": [
        "-3",
        "52",
        "51",
        "-9",
        "-37",
        "-25",
        "5",
        "4",
        "-8",
        "-12",
        "9",
        "2"
      ],
      "masses": [
        "5895",
        "9482"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        2,
        2,
        2,
        2,
        4
      ],
      "p": 4,
      "rs": [
        2,
        2,
        2,
        5,
        4
      ],
      "u": [
        "6",
        "-19",
        "39",
        "7",
        "-22",
        "-2",
        "-14",
        "0",
        "-2",
        "-5",
        "10",
        "8"
      ],
      "masses": [
        "4791",
        "6392"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        2,
        2,
        2,
        3,
        3
      ],
      "p": 5,
      "rs": [
        1,
        6,
        8,
        1,
        6
      ],
      "u": [
        "-178",
        "74",
        "17",
        "-48",
        "8",
        "-31",
        "17",
        "1",
        "-24",
        "-12",
        "-7",
        "8"
      ],
      "masses": [
        "6114",
        "14606"
      ],
      "valid": false
    },
    {
      "neg_pattern": [
        2,
        2,
        2,
        3,
        3
      ],
      "p": 7,
      "rs": [
        2,
        3,
        3,
        1,
        10
      ],
      "u": [
        "-20",
        "27",
        "51",
        "-33",
        "-5",
        "-20",
        "9",
        "-2",
        "-14",
        "-11",
        "-7",
        "7"
      ],
      "masses": [
        "4767",
        "10296"
      ],
      "valid": false
    }
  ],
  "bounds": [
    {
      "i": 0,
      "lo": "-1342/9282325",
      "hi": "1418/28589561",
      "width": "138784/714739025"
    },
    {
      "i": 1,
      "lo": "-1592/11510083",
      "hi": "3269/23762752",
      "width": "203227/736645312"
    },
    {
      "i": 2,
      "lo": "-26719/308915776",
      "hi": "68350/497161327",
      "width": "548189/2447563456"
    },
    {
      "i": 3,
      "lo": "-72721/748155395",
      "hi": "67170/497161327",
      "width": "17901613/77060005685"
    },
    {
      "i": 4,
      "lo": "-20272/246167259",
      "hi": "6276/53094899",
      "width": "543068/2707839849"
    },
    {
      "i": 5,
      "lo": "-12102/207552787",
      "hi": "56443/497161327",
      "width": "3673555/21377937061"
    },
    {
      "i": 6,
      "lo": "-20431/559909844",
      "hi": "61225/371664293",
      "width": "8675287/43113057988"
    },
    {
      "i": 7,
      "lo": "-2973/33787663",
      "hi": "642/4826809",
      "width": "7467/33787663"
    },
    {
      "i": 8,
      "lo": "-83899/748155395",
      "hi": "58984/622658361",
      "width": "118139/571077195"
    },
    {
      "i": 9,
      "lo": "-37185/497161327",
      "hi": "143148/748155395",
      "width": "20507919/77060005685"
    },
    {
      "i": 10,
      "lo": "-11767/207552787",
      "hi": "8786/82055753",
      "width": "44449/271415183"
    },
    {
      "i": 11,
      "lo": "-16454/207552787",
      "hi": "53457/685406878",
      "width": "4635119/29472495754"
    }
  ],
  "universal_width_bound": "498515831/736645312",
  "det": "247064529073450392704413",
  "field_checks": 258
}
```

## Reproduction
Load U0 and certs from the three exact files above. Run:
```js
function audit(U0,certs){
const P=13n,B=P**6n,N=12,C=2331,BN=Number(B);
const abs=a=>a<0n?-a:a,mod=(a,m)=>(a%m+m)%m,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a};
const f=(a,b=1n)=>{if(!b)throw Error("division");if(b<0n){a=-a;b=-b}let d=gcd(a,b);return [a/d,b/d]},add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),sum=a=>a.reduce(add,f(0n)),lt=(a,b)=>a[0]*b[1]<b[0]*a[1],floor=(a,b)=>a/b-(a<0n&&a%b?1n:0n),ceil=(a,b)=>-floor(-a,b);
const inv=(a,m)=>{let b=m,x=1n,y=0n;a=mod(a,m);while(b){let q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y]}if(a!==1n)throw Error("unit");return mod(x,m)};
const H=Array.from({length:6},(_,k)=>Array.from({length:N},(_,i)=>inv(BigInt(i+1)**BigInt(k+1),P**BigInt(k+1))));
const U=U0.map(r=>r.map(BigInt)),W=Array.from({length:N},(_,i)=>P*BigInt(i+1)-1n);
const check=(v,t)=>H.every((h,k)=>mod(h.reduce((s,a,i)=>s+a*v[i],0n)-t[k],P**BigInt(k+1))===0n);
for(let u of U)if(!check(u,Array(6).fill(0n)))throw Error("kernel");
let A=U.map((r,i)=>[...r.map(x=>f(x)),...Array.from({length:N},(_,j)=>f(BigInt(i===j)))]),det=f(1n);
for(let i=0;i<N;i++){let j=A.findIndex((r,k)=>k>=i&&r[i][0]);if(j<0)throw Error("singular");if(i!==j){[A[i],A[j]]=[A[j],A[i]];det=mul(det,f(-1n))}let p=A[i][i];det=mul(det,p);A[i]=A[i].map(x=>div(x,p));for(let j=0;j<N;j++)if(j!==i){let c=A[j][i];A[j]=A[j].map((x,k)=>sub(x,mul(c,A[i][k])))}}
if(det[1]!==1n||abs(det[0])!==P**21n)throw Error("det");
const UI=A.map(r=>r.slice(N));
function lift(t){let x=Array(N).fill(0n);for(let j=0;j<6;j++){let q=P**BigInt(j),m=6-j;let a=H.slice(j).map((h,k)=>{let d=t[j+k]-h.reduce((s,v,i)=>s+v*x[i],0n);if(d%q)throw Error("lift residue");return [...h.slice(0,m).map(v=>mod(v,P)),mod(d/q,P)]});for(let k=0;k<m;k++){let l=a.findIndex((r,i)=>i>=k&&r[k]);if(l<0)throw Error("rank");[a[k],a[l]]=[a[l],a[k]];let s=inv(a[k][k],P);a[k]=a[k].map(v=>mod(v*s,P));for(let i=0;i<m;i++)if(i!==k){let c=a[i][k];a[i]=a[i].map((v,h)=>mod(v-c*a[k][h],P))}}for(let i=0;i<m;i++)x[i]+=q*a[i][m]}if(!check(x,t))throw Error("lift check");return x}
const coords=new Map();for(let q=1;q<=12;q++)for(let r=1;r<=12;r++){let t=Array.from({length:6},(_,k)=>inv(BigInt(13*q+r)**BigInt(k+1),P**BigInt(k+1)));let x=lift(t);let v=Array.from({length:N},(_,i)=>sum(x.map((a,j)=>mul(f(a),UI[j][i]))));coords.set(q*100+r,v.map(a=>{let b=mul(a,f(B));if(b[1]!==1n)throw Error("denominator");return Number(mod(b[0],B))}))}
const bounds=Array.from({length:N},(_,i)=>{let g=UI.map((r,j)=>div(r[i],f(W[j]))),lo=g.reduce((a,b)=>lt(a,b)?a:b,f(0n)),hi=g.reduce((a,b)=>lt(a,b)?b:a,f(0n));return {i,lo,hi,width:sub(hi,lo)}});
const max=bounds.reduce((a,b)=>lt(a.width,b.width)?b:a);let universal=mul(max.width,f(2453n));if(!lt(universal,f(1n)))throw Error("width");
const order=bounds.slice().sort((a,b)=>lt(a.width,b.width)?-1:lt(b.width,a.width)?1:0);
const interval=new Map();
function box(p,mn){const key=p*3000+mn;if(interval.has(key))return interval.get(key);let ap=BigInt(C-(169+13*p-1)),am=BigInt(C-mn);if(ap<0n||am<0n)throw Error("budget");let arr=order.map(({i,lo,hi})=>{let l=mul(f(B),sub(mul(f(ap),lo),mul(f(am),hi))),h=mul(f(B),sub(mul(f(ap),hi),mul(f(am),lo)));let low=Number(ceil(l[0],l[1])),high=Number(floor(h[0],h[1]));if(low>0||high<0||high-low>=BN||!Number.isSafeInteger(low)||!Number.isSafeInteger(high))throw Error("box");return {i,low,high}});interval.set(key,arr);return arr}
function* parts(n,lo=1){if(!n){yield [];return}for(let q=lo;q<=n;q++)for(let r of parts(n-q,q))yield [q,...r]}
function choose(n,k){let v=1;for(let j=1;j<=k;j++)v=v*(n-j+1)/j;if(!Number.isSafeInteger(v))throw Error("choose");return v}
const fields=["raw","search","over","common_included","common_feasible","valid"];
const rows=[],full=[];
for(let pat of [...parts(12)].filter(p=>p.length>=5)){
const groups=new Map();for(let q of pat)groups.set(q,(groups.get(q)??0)+1);
let negRaw=1,negAvoid=1;for(let [q,k] of groups){negRaw*=choose(12+k-1,k);negAvoid*=choose((q===1?11:12)+k-1,k)}
const row={neg_pattern:pat,raw:12*negRaw,common_included:12*(negRaw-negAvoid),search:0,over:0,common_feasible:0,valid:0,box_survivors:0,coordinate_rejects:Array(N).fill(0)};
if(!Number.isSafeInteger(row.raw))throw Error("raw");
const maxSum=Math.floor((C-169*12+pat.length)/13);
const rs=[],neg=Array(N).fill(0),used1=Array(13).fill(0);
function visit(i,sr){
if(i<pat.length){let lower=i&&pat[i]===pat[i-1]?rs[i-1]:1;for(let r=lower;r<=12;r++){if(sr+r+pat.length-i-1>maxSum)break;rs.push(r);let v=coords.get(pat[i]*100+r);for(let k=0;k<N;k++)neg[k]=(neg[k]+v[k])%BN;if(pat[i]===1)used1[r]++;visit(i+1,sr+r);if(pat[i]===1)used1[r]--;for(let k=0;k<N;k++)neg[k]=(neg[k]-v[k]+BN)%BN;rs.pop()}return}
let mn=169*12+13*sr-pat.length;
if(mn>C)throw Error("pruning");
for(let p=1;p<=12;p++){row.search++;if(used1[p])row.common_feasible++;let pos=coords.get(100+p),z=Array(N);let ok=true,boxi=box(p,mn);for(let j=0;j<N;j++){let {i,low,high}=boxi[j],c=(neg[i]-pos[i]+BN)%BN;let a=c<=high,bb=c-BN>=low;if(a&&bb)throw Error("nonunique");if(a)z[i]=c;else if(bb)z[i]=c-BN;else{row.coordinate_rejects[j]++;ok=false;break}}
if(!ok)continue;row.box_survivors++;
let u=Array.from({length:N},(_,j)=>{let a=z.reduce((s,v,k)=>s+BigInt(v)*U[k][j],0n);if(a%B)throw Error("integrality");return a/B});
let rhs=Array.from({length:6},(_,k)=>rs.reduce((s,r,j)=>s+inv(BigInt(13*pat[j]+r)**BigInt(k+1),P**BigInt(k+1)),-inv(BigInt(13+p)**BigInt(k+1),P**BigInt(k+1))));
if(!check(u,rhs))throw Error("congruences");
let mp=BigInt(169+13*p-1)+u.reduce((s,v,j)=>s+(v>0n?v*W[j]:0n),0n),mm=BigInt(mn)+u.reduce((s,v,j)=>s+(v<0n?-v*W[j]:0n),0n);
if(mp<=BigInt(C)&&mm<=BigInt(C))row.valid++;
full.push({neg_pattern:pat,p,rs:rs.slice(),u:u.map(String),masses:[String(mp),String(mm)],valid:mp<=BigInt(C)&&mm<=BigInt(C)});
}}
visit(0,0);row.over=row.raw-row.search;
if(row.coordinate_rejects.reduce((a,b)=>a+b,0)+row.box_survivors!==row.search)throw Error("coverage");
let orig=certs.flatMap(c=>c.rows).find(r=>r.neg_pattern.join()===pat.join());if(!orig)throw Error("missing author row");for(let k of fields)if(row[k]!==orig[k])throw Error("mismatch "+JSON.stringify({pat,k,ours:row[k],orig:orig[k]}));rows.push(row)
}
if(rows.length!==certs.reduce((s,c)=>s+c.rows.length,0))throw Error("coverage");
return {rows,totals:Object.fromEntries([...fields,"box_survivors"].map(k=>[k,rows.reduce((s,r)=>s+r[k],0)])),coordinate_rejects:Array.from({length:N},(_,i)=>rows.reduce((s,r)=>s+r.coordinate_rejects[i],0)),coordinate_order:order.map(o=>o.i),full,bounds:bounds.map(({i,lo,hi,width})=>({i,lo:lo.join("/"),hi:hi.join("/"),width:width.join("/")})),universal_width_bound:universal.join("/"),det:abs(det[0]).toString(),field_checks:fields.length*rows.length}
}
console.log(JSON.stringify(audit(U0,certs),null,2));
```
