# Independent valley-band benchmark

This directory is independently authored from the frozen targeted packet. It contains no source-prototype code.

Regenerate the frozen corpus:

```powershell
python experiments\valley_band_benchmark\corpus.py
```

Check the frozen corpus without rewriting it:

```powershell
python experiments\valley_band_benchmark\corpus.py --check
```

Run the frozen matrix non-interactively:

```powershell
python experiments\valley_band_benchmark\runner.py --matrix frozen
```

The default command has the predeclared 300-second local-checkpoint budget. It
does not discard the rest of the plan: every unstarted row is emitted as
`NOT_RUN_BUDGET`. The frozen 2026-08-23 result must not be silently extended or
merged with exploratory runs.

Canonical run outputs are
`research_output/VALLEY_BAND_BENCHMARK_RUNS_20260823.csv` and
`research_output/evidence/VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_20260823.jsonl`.

Aggregate the frozen run table while retaining null, timeout, error, and
not-run rows:

```powershell
python experiments\valley_band_benchmark\aggregate.py
```

Run fast correctness/equivalence validation:

```powershell
python experiments\valley_band_benchmark\verify.py
```

The corpus contains factors solely for corpus and post-run validation. The
collector, multiplier scorer, relation/dependency engine, and stopping rules
receive `N` and the frozen run specification, never the factor fields.
