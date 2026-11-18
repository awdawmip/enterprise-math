# EC49FKQ reproduction commands and checker scope

Work from this directory inside a checkout of the PR branch. Install Python >=3.10, NumPy and SciPy >=1.15 (executed version SciPy 1.17.0).

The 9-state native BRC generator and its frozen A/B witness JSON are in the sibling directory `../EC49FJD_RELEASE_B11_COMPLETE_20261111/`. Use that folder in `PYTHONPATH`, since the solver imports `EC49FGW_RADIUS5_SCREEN`.

```sh
for i in 0 1 2 3 4 5 6 7 8; do
  PYTHONPATH=../EC49FJD_RELEASE_B11_COMPLETE_20261111 \
    OPENBLAS_NUM_THREADS=1 python VERIFY_EC49FKQ_MILP.py "$i" 180
done
```

Expected every row: `status 0`; integer primal = dual = 98 for indices 0–3 and 112 for indices 4–8; `gap 0.0`. The solver writes `MIP_WITNESS_{i}.json` for independently verifying the selected actual 24 words.

To check the **published immutable** witness file, even without rerunning the solver:

```sh
python - <<'PY'
import gzip, base64, pathlib, json, hashlib
p = pathlib.Path('EXACT_WITNESSES_EC49FKQ.json.gz.b64')
data = gzip.decompress(base64.b64decode(p.read_text().strip()))
assert hashlib.sha256(data).hexdigest() == '45326f659546b3ec1776221eb5e5050362740aad4b4c4e4741610464da220265'
for i, witness in enumerate(json.loads(data)):
    pathlib.Path(f'MIP_WITNESS_{i}.json').write_text(json.dumps(witness,indent=2))
PY
python VERIFY_EC49FKQ_WITNESSES.py
```

The checker re-evaluates every selected macro-word's nine-state transitions, exact ordered signed six-axis microsteps and six-axis displacement, exact complete raw key, observer label, and total distinct nonempty literal signed prefix count. All nine author-side executions passed.

**Evidence classes:** explicit valid witnesses provide independently checkable *upper* bounds. The 0–1 trie-to-word equivalence is an analytic theorem. Corresponding *lower* bounds are currently HiGHS completed integer-solver results; no machine-checkable branch-and-bound proof log is included. The project Driver reviews them separately before admission.
