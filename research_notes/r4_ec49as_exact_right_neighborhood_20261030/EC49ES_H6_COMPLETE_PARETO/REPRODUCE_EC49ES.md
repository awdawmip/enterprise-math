# EC49ES reproducibility — 2026-11-02

Checkout the Draft PR #1730 branch containing this directory and its sibling `EC49ER_H6_LOW_CACHE_EXACT`. The latter's immutable parent commit is `ed3ade49956f8a4deba33d0718097d5b30657539`; the exact parent evidence archive is named `EC49ER_COMPLETE_EVIDENCE.tar.gz.b64` and its decoded tar.gz SHA256 is `bee8a4768604ef74a2d0261524b8ad901ef5b9362251b17ab462e7cc3cd7665a`.

From this `EC49ES_H6_COMPLETE_PARETO` directory, run:

```sh
python LOAD_EC49ER_SOURCE.py
python M5_SCREEN_STRONG.py
python RUN_SCREENED_EC49ES.py
python CROSSCHECK_EC49ES.py
python VERIFY_EC49ES_MILP.py
node VERIFY_EC49ES_INDEPENDENT.js
```

The first command checks the parent archive SHA256 and extracts only the exact reused Python input/model/checker plus its prior executed result JSON; no network requests or credentials are used. All other commands run locally with native signed-X6 paths. The exact bounded integer DP and screening use only Python standard library; independent integer programming requires NumPy/SciPy/HiGHS; the separate witness checker uses Node.js. Executed `EC49ES_EXECUTED.json`, `EC49ES_MILP_EXECUTED.json`, `EC49ES_CROSSCHECK_EXECUTED.json`, `EC49ES_INDEPENDENT_EXECUTED.json` record this run's results. Reproduction on slower hosts may take longer; runtime speedup is not a mathematical claim. Do not reinterpret a solver's zero gap as verification of the complete enumeration: the all-case proof is the bounded integer DP with mathematically certified screening. All source evidence is non-sensitive.
