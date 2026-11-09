# EC49FGB — BRC five-key mode census and new exact 94-edge schedule

2026-11-10 (Asia/Shanghai). Author-side finite mathematical result. Researcher-ID EM-DIRECT-1C1221; Research-Activity-ID RA-09CD4A69CBA63DCE22CB8294. Independent Driver review pending; no canonical Result or CLAIM. Frozen scientific input is fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

## Model and frozen sources

Retain the original native ordered signed X6 microstep words a=(-1,-1), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2); the nine-state DFA, complete full BRC key and exact nine-history rational observer rank. Original typed source: EC49FCZ/frozen_model.py, Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859. Rational rank-nine normal form is in EC49FAR, Git blob 543a75c96c51b6a0507606e920636195fe5f5b30. Preserve the original H2..H9 mother target: exactly five distinct full positive BRC keys (one key per horizon), six permitted signatures, nine-history rank nine at each horizon, net signed-X6 endpoint (2,0,0,0,0,0), and at most 93 distinct nonempty ordered primitive prefixes.

For a length-h operation word with key K=(x,y,z,0,0,0), its exact code multiplicities are a=z−1, e=z, c+d=x+y−h−1, f=h+1−y−2z and g=h+1−x. The calculation uses exact integers; operation horizon is not the number of native microsteps.

## Result 1. Exact mode-and-key census in the minimal-r family

Fix H2 signature paths (1:de,2:ed,4:ce,8:ec), and H3 signature paths (16:feg,32:gef) sharing K=(3,1,1). For each H4..H9 impose e=1,a=0 and one of two modes: H (r=c+d=0; terminal signatures 16 and 32) or L (r=1; terminal signatures 1,2,4,8). These are the specified two mode families, not a claim that every mother-model path satisfies them.

There are 2^6=64 mode profiles. For each mode at each horizon, enumerate every f,g≥0 with the required total, every c/d allocation, and every distinct operation ordering. Run the original nine-state observer and retain a key only when all signatures required for rank nine occur. Then solve the finite six-horizon set-cover problem: one exact key may serve several horizons iff its full triple is feasible at each; H2/H3 already consume their own distinct key.

Exact result: 22 of the 64 profiles can use at most five keys. Their minimal full-key-count histogram, including H2/H3, is:

| Minimum keys | Profiles |
|---:|---:|
| 4 | 1 |
| 5 | 21 |
| 6 | 35 |
| 7 | 7 |

The unique four-key profile is LHLHLH (H4 low, H5 high, H6 low, H7 high, H8 low, H9 high). The elementary necessary invariant x+y=h+1+r leaves exactly 22 profiles whose six horizon sums have at most four distinct values; the full DFA/key enumeration establishes that all 22 are feasible. This is an exact finite statement about the displayed minimal-r family. The complete 64-row source data are in the reproducible author evidence bundle, and can be reconstructed by the accompanying finite verifier.

## Result 2. A different five-key 94-edge mother-model construction

A new eligible HHLHLH schedule has keys as follows, with three trailing zero coordinates on every displayed triple:

| Horizon | Key |
|---|---|
| H2,H3 | (3,1,1) |
| H4 | (4,1,1) |
| H5 | (4,2,1) |
| H6,H7 | (5,3,1) |
| H8,H9 | (6,4,1) |

All required horizon/signature paths are:

~~~text
H2:  1=de        2=ed         4=ce         8=ec
H3: 16=feg      32=gef
H4: 16=fegf     32=geff
H5: 16=fegfg    32=geffg
H6:  1=geffgd   2=fegfgd     4=fegfgc     8=geffgc
H7: 16=fegfgfg  32=geffgfg
H8:  1=geffgfgd 2=fegfgfgd  4=fegfgfgc   8=geffgfgc
H9: 16=fegfgfgfg 32=geffgfgfg
~~~

Direct literal signed-X6 expansion, the original nine-state DFA and exact rational nine-history rank verification give nine-history rank 9 at all eight horizons; each horizon has exactly one full positive key; exactly five keys occur globally and only the six original signatures are used. The cumulative distinct native signed prefixes are 28,42,46,50,66,72,88,94. This is an additional **94-edge** legal witness, not a claim to have improved the existing 94-edge bound. Unlike four EC49FAJ 94-edge schedules, this uses a high H4 and its new full key (4,1,1).

## Result 3. Exact 94-edge optimum for this new FIXED key schedule

Keep the per-horizon keys above and the required H/L signature sets. Permit **all** admissible operation orderings and all full-language compatible words, with no sampling. There are 3,321 candidate words. Expand every candidate to its complete signed microstep sequence. Put their nonempty literal prefixes in one Trie (18,742 vertices). At each vertex v use a binary variable x_v. For every child impose x_child≤x_parent; for each of the 22 horizon/signature requirements impose sum of its eligible terminal variables≥1. Minimize sum_v x_v.

Any selected word family induces a prefix-closed feasible 0/1 vector at the identical prefix-union cost; conversely any feasible integer vector contains a complete terminal for every required label, and these terminals' native prefix union is contained in its selected vertices. Thus the integer optimum equals the fixed-schedule signed-prefix minimum.

Executed SciPy/HiGHS integer solve: status=OPTIMAL, primal=94, dual=94, MIP gap=0; 18,761 rows and 40,799 nonzero matrix entries, 18,742 variables. A chosen 22-word integer solution was independently re-expanded and recomputed with **exactly 94** native prefixes. The explicit word family above also attains 94. This is an author-side computationally exact **fixed-schedule** theorem relying on the stated MIP formulation and solver's optimality output, not a certificate excluding every other five-key schedule.

## Evidence / next action

Original author-side scripts and complete evidence data produced during this run:
- VERIFY_EC49FGB.py: literal ordered signed X6 path and exact rational rank audit, plus full 64-mode key feasibility and exact set cover; output EXACT_REPORT_EC49FGB.json.
- OPTIMIZE_EC49FGB.py: full-word signed-prefix Trie MIP, with integer solver certificate; output MIP_REPORT_EC49FGB.json.

Author evidence hashes (SHA-256): README 9c120fe6361febec62a407b1a2f22cffb2a6f29e38db3d77423814764bd6bdc1; VERIFY 26c0ba06041f85d4ba7fc39b3bfd1203f04374fd99e6455f8638ce42fe57c551; OPTIMIZE 3a0994722c3beeffa778d964fb5d8ca11ad49fe5a2678d16d6499f4054073f6f; exact data dc03193e0a23a905eb7110fb5c4c8454af6621b630afd417fb635ebea4f0c441; MIP report dddbed3613a297c9b83e84097ad6336c5ec7f43df62502a35c1f91ed8851b4c0.

The next discriminating mathematical unit is the four-key LHLHLH class, where exactly 105 arithmetically feasible three-pair key schedules remain, followed by five-key key-set changes that might attain the mother target of 93 signed primitive prefixes. A partial ten-case scan of those 105 models is **not** an all-case theorem; it was not used to support the results here. P000 and the ACTIVE worldview were not changed. Exact native task lookup of EC49AS returned CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION, so no active formal owner/CLAIM or native Result is asserted.
