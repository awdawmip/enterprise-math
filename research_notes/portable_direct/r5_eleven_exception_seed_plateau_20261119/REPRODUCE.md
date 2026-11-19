# R5 11-label exact verification / reproduction

Frozen scalar input: `EXACT_R5_ALL_101_BUDGETS.json`, SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`, frozen science `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`.

Complete local evidence archive: `EnterpriseMath_R5_Eleven_246_50Class_20261119.zip`, SHA256 `e9f3cd8d2d7f5ac043401bbecf43d4ee9725268d71ed2641adf658400381ce86`. The archive contains the full 246-row CSV, all 50 class logs, original frozen input, two C++ source files, independent Python verifier, SHA manifest and reproduction helper. This GitHub branch contains the theorem, outcome manifest and runnable source, but is not a formal Result.

Place the exact input JSON next to the scripts:

```bash
python3 MAKE_WINDOW_ADJ.py
g++ -O3 -std=c++17 EXACT_SOLVER.cpp -o exact11
./exact11 6 5000000 > full_f0_f6.csv
for class in $(seq 0 49); do
    ./exact11 8 5000000 "$class" > "class${class}.csv"
done
python3 VERIFY_ENDPOINT.py
```

Class-filtered output uses -2 for other classes: retain only rows whose class ID matches the selected class. All fifty classes must finish without UNFINISHED or STATE_CAP_REACHED. Every one of 246 original labels must have f0..f8 values (733,1681,2628,3575,4522,5469,6416,7363,8310). Rebuilt adjacency SHA256: `daad32bc5c4f1a11361f1389c0e95d2de349a4870f7c240179f44d02d2d282af`. Independent verification output: `PASS_ELEVEN_INDEPENDENT_F0 246 F1 12`.

The f2..f8 values have exact C++ author checks, not independent Python replication or human review. The 10-label precursor is in preserved local evidence; its own remote Source publication is unverified. The stronger old 256-label interval remains 8335..8343, and the result is scalar-only, not a native X6/Port/BRC semantic compression.

Next test simultaneous addition of two labels to the ten-label seed, and the true joint support union with the 17-label lower-bound witness.
