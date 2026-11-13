# R26 run evidence and provenance

Run date: 2026-11-10 Asia/Shanghai. Local Python standard-library `Fraction` / integer arithmetic, no approximate phase comparisons. Source program `VERIFY_R26.py` and independent `CROSSCHECK_R16.py`; exact frozen interval defined in program. Predecessor scientific result R25 @ `7f2aff7df2ff1a5360362d106e14f9a9b4074fc7`. Comparator is the prior locally mounted R16 `AFFINE_RUNS_1T.tsv`, 298 rows, SHA256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`. This comparator file must be supplied at `/mnt/data/em_r16/AFFINE_RUNS_1T.tsv` for the separate crosscheck; the main evaluator is standalone.

Actual stdout from `python /mnt/data/em_r26/VERIFY_R26.py` (selected full set of 30 frontier inputs plus the exhaustive 128..500 loop):

```
CASE 128 R= (0, 0) i,j= (103, 61) jumps= 6 gap_counts= [25, 67, 36] direct= True
CASE 129 R= (16, -61) i,j= (103, 61) jumps= 6 gap_counts= [26, 68, 35] direct= True
CASE 225 R= (-2047, 7808) i,j= (164, 61) jumps= 6 gap_counts= [61, 164, 0] direct= True
CASE 226 R= (-2090, 7972) i,j= (164, 225) jumps= 7 gap_counts= [62, 1, 163] direct= True
CASE 292 R= (-4928, 18796) i,j= (164, 225) jumps= 7 gap_counts= [128, 67, 97] direct= True
CASE 328 R= (-4928, 18796) i,j= (164, 225) jumps= 7 gap_counts= [164, 103, 61] direct= True
CASE 329 R= (-4971, 18960) i,j= (164, 225) jumps= 7 gap_counts= [165, 104, 60] direct= True
CASE 456 R= (-10432, 39788) i,j= (164, 389) jumps= 7 gap_counts= [292, 67, 97] direct= True
CASE 492 R= (-10432, 39788) i,j= (164, 389) jumps= 7 gap_counts= [328, 103, 61] direct= True
CASE 493 R= (-10475, 39952) i,j= (164, 389) jumps= 7 gap_counts= [329, 104, 60] direct= True
CASE 717 R= (5505, -20992) i,j= (164, 553) jumps= 7 gap_counts= [553, 164, 0] direct= True
CASE 1106 R= (5505, -20992) i,j= (717, 553) jumps= 8 gap_counts= [389, 553, 164] direct= True
CASE 1107 R= (5317, -20275) i,j= (717, 553) jumps= 8 gap_counts= [390, 554, 163] direct= True
CASE 1173 R= (-7091, 27047) i,j= (717, 553) jumps= 8 gap_counts= [456, 620, 97] direct= True
CASE 1174 R= (-7091, 27047) i,j= (717, 553) jumps= 8 gap_counts= [457, 621, 96] direct= True
CASE 15000 R= (109313, -416896) i,j= (14298, 11041) jumps= 12 gap_counts= [702, 3959, 10339] direct= True
CASE 25175 R= (109313, -416896) i,j= (14298, 11041) jumps= 12 gap_counts= [10877, 14134, 164] direct= False
CASE 25176 R= (105564, -402598) i,j= (14298, 11041) jumps= 12 gap_counts= [10878, 14135, 163] direct= True
CASE 25340 R= (-370559, 1413248) i,j= (14298, 25339) jumps= 13 gap_counts= [11042, 1, 14297] direct= False
CASE 39473 R= (-370559, 1413248) i,j= (14298, 25339) jumps= 13 gap_counts= [25175, 14134, 164] direct= False
CASE 39474 R= (-374308, 1427546) i,j= (14298, 25339) jumps= 13 gap_counts= [25176, 14135, 163] direct= False
CASE 168155 R= (-4689407, 17884544) i,j= (14298, 154021) jumps= 13 gap_counts= [153857, 14134, 164] direct= False
CASE 168156 R= (-4649022, 17730523) i,j= (14298, 154021) jumps= 13 gap_counts= [153858, 14135, 163] direct= False
CASE 168319 R= (479873, -1830144) i,j= (14298, 154021) jumps= 13 gap_counts= [154021, 14298, 0] direct= False
CASE 168320 R= (479873, -1830144) i,j= (168319, 154021) jumps= 14 gap_counts= [1, 14299, 154020] direct= False
CASE 200000 R= (479873, -1830144) i,j= (168319, 154021) jumps= 14 gap_counts= [31681, 45979, 122340] direct= False
CASE 322176 R= (479873, -1830144) i,j= (168319, 154021) jumps= 14 gap_counts= [153857, 168155, 164] direct= False
CASE 322177 R= (520258, -1984165) i,j= (168319, 154021) jumps= 14 gap_counts= [153858, 168156, 163] direct= False
CASE 322340 R= (5649153, -21544832) i,j= (168319, 154021) jumps= 14 gap_counts= [154021, 168319, 0] direct= False
CASE 323000 R= (5649153, -21544832) i,j= (322340, 154021) jumps= 14 gap_counts= [660, 168979, 153361] direct= False
LARGE 1000000 R= (-5169279, 19714688) denom= (476361, 630382) steps= 15 gap_counts= [523639, 369618, 106743]
LARGE 2000000 R= (-21156991, 80688896) denom= (1106743, 1737125) steps= 17 gap_counts= [893257, 262875, 843868]
LARGE 100000000 R= (-1638096639, 6247400832) denom= (42489701, 91297520) steps= 21 gap_counts= [57510299, 8702480, 33787221]
LARGE 1000000000 R= (1426046849, -5438681728) denom= (558684231, 516194530) steps= 22 gap_counts= [441315769, 483805470, 74878761]
PASS_R26_FAREY_FLOORSUM_EXACT_RISK_ALL_128_500_AND_30_FRONTIER_POINTS
```

Actual stdout from `python /mnt/data/em_r26/CROSSCHECK_R16.py`:

```
PASS_R26_CROSSCHECK_R16_AFFINE_1T
R16_TSV_ROWS 298 SHA256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
EXACT_CHECKED 1147 RANGE 128 1000000000128
DURATION_SEC 18.814
AT_ONE_TRILLION_FUTURE (-4017401528447, 15321634290944)
```

Independent additional exact endpoint evaluations (performed with `eval_risk`, separate short Python call):

```
start_n   end_n           zero_increments   R_start = R_end (A,B)
322340    476197           153857           (5649153,-21544832)
476361    630218           153857           (10818433,-41259520)
630382    1106579          476197           (-5169279,19714688)
752555238039 1000000000128 247444762089  (-4017401528447,15321634290944)
```

At each of the four start positions, `R_start-R_(start-1)>0` was checked strictly at both theta endpoints. Since risk is monotone in n, equal endpoint risk proves the full plateau for every intermediate integer n.

## Scope and reproducibility

`VERIFY_R26.py` writes a 30-row `CERTIFICATE_R26.tsv` to `/mnt/data/em_r26/`; this local output was computed in the present run, and its provenance is the exact program + printed stdout. The standalone verifier needs Python 3 standard library and a writable output directory. No credentials are embedded. `CROSSCHECK_R16.py` needs the separately preserved 298-row R16 table at its declared local path.

This is self-reviewed author-side mathematical evidence; an independent reviewer has not admitted the result to project Foundation.
