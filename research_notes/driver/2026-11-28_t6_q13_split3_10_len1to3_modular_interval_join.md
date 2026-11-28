# T6 q13 split(3,10), negative lengths 1–3 — exact sorted modular interval join

Informed Driver EM-DVR-DEBB5E, frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Basis 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json blob bcab5ce85b368d2b65a74340ceadb4527da0f01e. Reuse previously verified dual coordinate theorem at cd13961f1ad5ca95a5e1431216f0017e57f00825 and exact implementation in b6ba599e1f387b2bbe43e653b8e076885c8c08cc. All budget-feasible high-rosters in relaxed model including common atoms. New split 3,10 only, negative lengths 1–3. No author certificate field comparison or novelty assertion beyond actual method change. Not independent review of own theorem; distinct from author GS solver.

## Exact index lemma
Fix positive high-mass group m and a negative roster n, and the first dual coordinate i with scaled residue c of n. Let positive residues p be sorted in [0,B-1], B=13^6. Its necessary difference residue must have a representative d in [low,high], an inclusive integer interval of length strictly less than B, with low<=0<=high. Equivalently p lies on the circular inclusive interval [c-high,c-low] modulo B. Translate the two endpoints into [0,B-1]; for a nonwrapping interval binary-search lower_bound(l), lower_bound(h+1), otherwise use [0,h] and [l,B-1]. This includes duplicate coordinates and both endpoint residues; when the interval contains all B residues the two ranges partition the full list. Every feasible original pair must belong to exactly one such returned range. Grouping by exact positive mass and fixing the negative mass preserves the original signed separate budget bounds; no cross-group approximation. Count every excluded index outside those ranges, then check all 12 coordinates, restore surviving u and verify all six congruences and both original budgets. Exact mass groups and circular interval search replace only the first-coordinate Cartesian filtering, not its predicate. Sorting cost and index queries are additional; no asymptotic runtime claim for all models. Entire raw domain counted separately by binomial multiset product; only high-budget-feasible rows enter search. Bound 498515831/736645312 < 1 and determinant 13^21 reverified. Independent digit-lift surjectivity and prior saturated-kernel proof retained. H0, lower-prime completion, observer implication and global T6 remain open.

## Executed data
```json
{
  "rows": [
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        8
      ],
      "raw": 340704,
      "search": 340704,
      "index_pass": 105467,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        235237,
        71556,
        22444,
        6885,
        2702,
        1047,
        580,
        150,
        60,
        29,
        9,
        2
      ],
      "minMaxBudgetExcess": 3099
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        1,
        1,
        8
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43209,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        91575,
        28531,
        9532,
        3057,
        1278,
        502,
        167,
        62,
        50,
        14,
        9,
        3
      ],
      "minMaxBudgetExcess": 2706
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        1,
        1,
        8
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3754,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7478,
        2453,
        832,
        269,
        121,
        45,
        20,
        5,
        5,
        0,
        0,
        3
      ],
      "minMaxBudgetExcess": 7481
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        2,
        7
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 194909,
      "box_survivors": 24,
      "valid": 0,
      "rejects": [
        434083,
        133088,
        40856,
        13091,
        4595,
        1983,
        795,
        283,
        115,
        42,
        26,
        11
      ],
      "minMaxBudgetExcess": 1839
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        1,
        2,
        7
      ],
      "raw": 248832,
      "search": 248832,
      "index_pass": 79339,
      "box_survivors": 8,
      "valid": 0,
      "rejects": [
        169493,
        52945,
        17170,
        5572,
        2127,
        890,
        355,
        166,
        71,
        23,
        9,
        3
      ],
      "minMaxBudgetExcess": 2450
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        1,
        2,
        7
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6763,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        13973,
        4399,
        1480,
        495,
        208,
        103,
        44,
        24,
        6,
        2,
        0,
        0
      ],
      "minMaxBudgetExcess": 2781
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        3,
        6
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 194046,
      "box_survivors": 20,
      "valid": 0,
      "rejects": [
        434946,
        131288,
        41532,
        13090,
        4893,
        1902,
        838,
        267,
        116,
        76,
        12,
        12
      ],
      "minMaxBudgetExcess": 3067
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        1,
        3,
        6
      ],
      "raw": 248832,
      "search": 248832,
      "index_pass": 80346,
      "box_survivors": 13,
      "valid": 0,
      "rejects": [
        168486,
        53092,
        17609,
        5656,
        2290,
        1063,
        377,
        125,
        74,
        27,
        8,
        12
      ],
      "minMaxBudgetExcess": 2306
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        1,
        3,
        6
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6928,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        13808,
        4489,
        1543,
        511,
        223,
        89,
        40,
        14,
        9,
        6,
        2,
        0
      ],
      "minMaxBudgetExcess": 4814
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        4,
        5
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 194321,
      "box_survivors": 22,
      "valid": 0,
      "rejects": [
        434671,
        131705,
        41460,
        13135,
        4831,
        1839,
        747,
        354,
        132,
        70,
        13,
        13
      ],
      "minMaxBudgetExcess": 2427
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        1,
        4,
        5
      ],
      "raw": 248832,
      "search": 248832,
      "index_pass": 79978,
      "box_survivors": 11,
      "valid": 0,
      "rejects": [
        168854,
        52682,
        17766,
        5646,
        2239,
        924,
        434,
        151,
        82,
        24,
        10,
        9
      ],
      "minMaxBudgetExcess": 2289
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        1,
        4,
        5
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6934,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        13802,
        4482,
        1590,
        499,
        205,
        85,
        37,
        17,
        12,
        4,
        1,
        1
      ],
      "minMaxBudgetExcess": 5627
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        9
      ],
      "raw": 52416,
      "search": 52416,
      "index_pass": 16884,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        35532,
        11213,
        3605,
        1220,
        493,
        245,
        64,
        22,
        10,
        5,
        4,
        1
      ],
      "minMaxBudgetExcess": 4999
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        1,
        9
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6923,
      "box_survivors": 2,
      "valid": 0,
      "rejects": [
        13813,
        4343,
        1648,
        552,
        210,
        96,
        36,
        17,
        12,
        3,
        2,
        2
      ],
      "minMaxBudgetExcess": 6057
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        1,
        9
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 598,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        1130,
        399,
        123,
        44,
        17,
        5,
        4,
        2,
        1,
        0,
        2,
        0
      ],
      "minMaxBudgetExcess": 4562
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        2,
        2,
        6
      ],
      "raw": 340704,
      "search": 340704,
      "index_pass": 105459,
      "box_survivors": 11,
      "valid": 0,
      "rejects": [
        235245,
        71717,
        22293,
        7010,
        2678,
        1054,
        416,
        173,
        58,
        34,
        11,
        4
      ],
      "minMaxBudgetExcess": 2038
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        2,
        2,
        6
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43524,
      "box_survivors": 5,
      "valid": 0,
      "rejects": [
        91260,
        28658,
        9555,
        3165,
        1203,
        542,
        229,
        75,
        58,
        11,
        18,
        5
      ],
      "minMaxBudgetExcess": 2362
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        2,
        2,
        6
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3730,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7502,
        2411,
        822,
        312,
        95,
        60,
        11,
        6,
        7,
        3,
        1,
        1
      ],
      "minMaxBudgetExcess": 6408
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        2,
        3,
        5
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 194268,
      "box_survivors": 19,
      "valid": 0,
      "rejects": [
        434724,
        131662,
        41340,
        13111,
        4913,
        1960,
        738,
        302,
        122,
        63,
        27,
        11
      ],
      "minMaxBudgetExcess": 1414
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        2,
        3,
        5
      ],
      "raw": 248832,
      "search": 248832,
      "index_pass": 80165,
      "box_survivors": 5,
      "valid": 0,
      "rejects": [
        168667,
        53259,
        17425,
        5667,
        2235,
        963,
        328,
        159,
        68,
        37,
        13,
        6
      ],
      "minMaxBudgetExcess": 3029
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        2,
        3,
        5
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6964,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        13772,
        4554,
        1535,
        474,
        250,
        91,
        28,
        19,
        7,
        4,
        1,
        0
      ],
      "minMaxBudgetExcess": 5134
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        2,
        4,
        4
      ],
      "raw": 340704,
      "search": 340704,
      "index_pass": 105276,
      "box_survivors": 9,
      "valid": 0,
      "rejects": [
        235428,
        71160,
        22634,
        7083,
        2681,
        1036,
        414,
        138,
        76,
        31,
        9,
        5
      ],
      "minMaxBudgetExcess": 3058
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        2,
        4,
        4
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43150,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        91634,
        28672,
        9276,
        3170,
        1179,
        488,
        193,
        103,
        38,
        19,
        4,
        5
      ],
      "minMaxBudgetExcess": 2322
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        2,
        4,
        4
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3775,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7457,
        2493,
        803,
        280,
        118,
        49,
        14,
        10,
        5,
        2,
        0,
        0
      ],
      "minMaxBudgetExcess": 2731
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        2,
        8
      ],
      "raw": 52416,
      "search": 52416,
      "index_pass": 16945,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        35471,
        11426,
        3545,
        1201,
        455,
        177,
        79,
        32,
        16,
        6,
        3,
        1
      ],
      "minMaxBudgetExcess": 2691
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        2,
        8
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6955,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        13781,
        4559,
        1539,
        514,
        187,
        75,
        54,
        16,
        6,
        2,
        2,
        1
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        2,
        8
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 589,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1139,
        372,
        142,
        41,
        15,
        10,
        7,
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
        1
      ],
      "neg_pattern": [
        3,
        3,
        4
      ],
      "raw": 340704,
      "search": 340704,
      "index_pass": 105326,
      "box_survivors": 8,
      "valid": 0,
      "rejects": [
        235378,
        71297,
        22351,
        7185,
        2688,
        1109,
        403,
        170,
        74,
        25,
        9,
        7
      ],
      "minMaxBudgetExcess": 2316
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        3,
        3,
        4
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43331,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        91453,
        28848,
        9319,
        3075,
        1237,
        496,
        201,
        72,
        47,
        18,
        9,
        5
      ],
      "minMaxBudgetExcess": 3372
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        3,
        3,
        4
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3744,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        7488,
        2413,
        800,
        286,
        141,
        48,
        22,
        13,
        17,
        2,
        1,
        0
      ],
      "minMaxBudgetExcess": 6900
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        3,
        7
      ],
      "raw": 52416,
      "search": 52416,
      "index_pass": 17004,
      "box_survivors": 3,
      "valid": 0,
      "rejects": [
        35412,
        11321,
        3679,
        1187,
        475,
        202,
        83,
        38,
        7,
        4,
        5,
        0
      ],
      "minMaxBudgetExcess": 3182
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        3,
        7
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6839,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        13897,
        4437,
        1517,
        510,
        198,
        96,
        44,
        18,
        8,
        6,
        3,
        1
      ],
      "minMaxBudgetExcess": 4031
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        3,
        7
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 586,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1142,
        386,
        122,
        44,
        21,
        9,
        2,
        0,
        0,
        1,
        1,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        4,
        6
      ],
      "raw": 52416,
      "search": 52416,
      "index_pass": 16807,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        35609,
        11190,
        3630,
        1193,
        450,
        196,
        82,
        42,
        11,
        7,
        4,
        2
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        4,
        6
      ],
      "raw": 20736,
      "search": 20736,
      "index_pass": 6958,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        13778,
        4526,
        1553,
        528,
        203,
        77,
        35,
        17,
        9,
        7,
        2,
        1
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        4,
        6
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 613,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1115,
        400,
        134,
        46,
        21,
        7,
        4,
        0,
        0,
        1,
        0,
        0
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        1,
        1,
        1
      ],
      "neg_pattern": [
        5,
        5
      ],
      "raw": 28392,
      "search": 28392,
      "index_pass": 9165,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        19227,
        6201,
        1920,
        618,
        239,
        105,
        47,
        21,
        6,
        5,
        2,
        0
      ],
      "minMaxBudgetExcess": 5358
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        5,
        5
      ],
      "raw": 11232,
      "search": 11232,
      "index_pass": 3784,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        7448,
        2541,
        791,
        271,
        100,
        51,
        19,
        8,
        1,
        0,
        1,
        1
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        5,
        5
      ],
      "raw": 936,
      "search": 936,
      "index_pass": 328,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        608,
        214,
        65,
        27,
        13,
        7,
        1,
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
        1
      ],
      "neg_pattern": [
        10
      ],
      "raw": 4368,
      "search": 4368,
      "index_pass": 1498,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        2870,
        1031,
        292,
        97,
        45,
        17,
        6,
        5,
        3,
        1,
        0,
        0
      ],
      "minMaxBudgetExcess": 2888
    },
    {
      "pos_pattern": [
        1,
        2
      ],
      "neg_pattern": [
        10
      ],
      "raw": 1728,
      "search": 1728,
      "index_pass": 592,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        1136,
        409,
        105,
        49,
        18,
        7,
        1,
        1,
        1,
        0,
        0,
        1
      ],
      "minMaxBudgetExcess": null
    },
    {
      "pos_pattern": [
        3
      ],
      "neg_pattern": [
        10
      ],
      "raw": 144,
      "search": 144,
      "index_pass": 51,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        93,
        31,
        14,
        5,
        1,
        0,
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
    "raw": 5887440,
    "search": 5887440,
    "index_pass": 1847825,
    "box_survivors": 194,
    "valid": 0
  },
  "minExcess": 1414,
  "minWitness": {
    "pp": [
      1,
      1,
      1
    ],
    "np": [
      2,
      3,
      5
    ],
    "pos": [
      3,
      7,
      7
    ],
    "neg": [
      9,
      12,
      6
    ],
    "u": [
      "33",
      "-2",
      "4",
      "3",
      "-5",
      "-7",
      "-6",
      "11",
      "1",
      "-2",
      "0",
      "6"
    ],
    "masses": [
      "3605",
      "3745"
    ],
    "excess": 1414
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

## Reproduction
Load U from pinned JSON; call audit(U).
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
const coords=new Map(),targets=new Map();for(let q=1;q<=10;q++)for(let r=1;r<=12;r++){let t=Array.from({length:6},(_,k)=>inv(BigInt(13*q+r)**BigInt(k+1),P**BigInt(k+1)));targets.set(q*100+r,t);let x=lift(t);coords.set(q*100+r,Array.from({length:N},(_,i)=>Number(mod(x.reduce((a,v,j)=>a+v*D[j][i],0n),B))))}
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
const ppList=[...parts(3)].map(pp=>{let pos=roster(pp);return {pp,pos,groups:group(pos)}});
for(let np of [...parts(10)].filter(p=>p.length<=3)){let neg=roster(np);for(let {pp,pos,groups} of ppList){let row={pos_pattern:pp,neg_pattern:np,raw:raw(pp)*raw(np),search:pos.length*neg.length,index_pass:0,box_survivors:0,valid:0,rejects:Array(N).fill(0),minMaxBudgetExcess:null};
for(let n of neg)for(let [mp0,list] of groups){let bs=box(mp0,n.m),rs=ranges(list,n.v[i0],bs[0].low,bs[0].high);let nPass=rs.reduce((s,[l,h])=>s+h-l,0);row.index_pass+=nPass;row.rejects[0]+=list.length-nPass;
for(let [l,h] of rs)for(let k0=l;k0<h;k0++){let p=list[k0],z=Array(N),ok=true;for(let j=0;j<N;j++){let {i,low,high}=bs[j],c=(n.v[i]-p.v[i]+BN)%BN;if(c<=high)z[i]=c;else if(c-BN>=low)z[i]=c-BN;else{if(j===0)throw Error("index false positive");row.rejects[j]++;ok=false;break}}if(!ok)continue;row.box_survivors++;
let u=Array.from({length:N},(_,j)=>{let x=z.reduce((s,v,k)=>s+BigInt(v)*U[k][j],0n);if(x%B)throw Error("integrality");return x/B});
let rhs=Array.from({length:6},(_,k)=>n.rs.reduce((s,r,j)=>s+targets.get(np[j]*100+r)[k],0n)-p.rs.reduce((s,r,j)=>s+targets.get(pp[j]*100+r)[k],0n));if(!check(u,rhs))throw Error("congruences");
let mp=BigInt(p.m)+u.reduce((s,v,j)=>s+(v>0n?v*W[j]:0n),0n),mn=BigInt(n.m)+u.reduce((s,v,j)=>s+(v<0n?-v*W[j]:0n),0n);let excess=Number((mp>mn?mp:mn)-BigInt(C));if(row.minMaxBudgetExcess===null||excess<row.minMaxBudgetExcess)row.minMaxBudgetExcess=excess;if(excess<minExcess){minExcess=excess;minWitness={pp,np,pos:p.rs,neg:n.rs,u:u.map(String),masses:[String(mp),String(mn)],excess}}if(excess<=0)row.valid++}}
if(row.rejects.reduce((a,b)=>a+b,0)+row.box_survivors!==row.search)throw Error("coverage");if(row.index_pass!==row.search-row.rejects[0])throw Error("index coverage");rows.push(row)}}
return {rows,totals:Object.fromEntries(["raw","search","index_pass","box_survivors","valid"].map(k=>[k,rows.reduce((s,r)=>s+r[k],0)])),minExcess,minWitness,width:width.join("/"),det:abs(det[0]).toString(),coordinate_order:bounds.map(b=>b.i)}
}
```
