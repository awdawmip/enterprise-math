# R27 exact execution and reproduction evidence

Date: 2026-11-10 Asia/Shanghai. Author-side evidence under frozen scientific pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Executed

Using the exact `VERIFY_R27.py` saved alongside this document (local Git blob `f56af00927831d30b6f86ece70bd8f30c97ee90e`), Python standard-library integer arithmetic and `fractions.Fraction`, with the prior R16 and R25 files as OPTIONAL references:

```sh
R16_FILE=/mnt/data/em_r16/AFFINE_RUNS_1T.tsv \
R25_FILE=/mnt/data/em_r25/EPOCHS_R25.tsv \
python /mnt/data/em_r27/VERIFY_R27.py 1000000000128
```

The program saves three exact TSV outputs to the directory containing the script by default; set `R27_OUT_DIR` for another destination. When R16 is absent, it checks selected locations against its included independently callable floor-sum oracle instead, and still runs the complete small-`n` direct phase-partition checks. The published `VERIFY_R27.py` contains the algorithm and expected assertions.

Observed console summary:

```
PASS_R27_FAREY_REGIME_SELECT_EXACT
N 1000000000128 regimes 78 positive_events 9697 crosschecks 1642 end (-4017401528447, 15321634290944) affine_runs 298 elapsed_s 8.467 max_regime_len 247444762089
RISK_1T (-4017401528447, 15321634290944)
```

The 78 regime start and end checks used the independent R26 risk oracle. All integer positions `128<=n<=500` were independently reconstructed by sorting the entire phase partition and checking its 128 historical-arc maxima. An additional 1,642 fixed probes were checked against the R16 table, including affine boundaries, neighboring positions, and deterministic pseudo-random positions. The complete generated 298-row TSV was compared row-for-row against the earlier R16 reference; all rows match.

## Exact generated artifacts

```
SHA256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6  AFFINE_RUNS_R27.tsv
SHA256 cb51b2cd873d8fb86e5d7edd916e9a2b614dc76e4d8fc1837898d932a808723b  EVENTS_R27.tsv
SHA256 d8e1dd426869b4f6c5d029bf170436ece3d5dfb361bc25908706386a247d5bae  REGIMES_R27.tsv
SHA256 e297057960761535ac714f892dceee480052397cc471c055a33930447a6c77c0  VERIFY_R27.py
```

Counts including headers: `AFFINE_RUNS_R27.tsv` has 299 lines; `EVENTS_R27.tsv` has 9,698 lines; `REGIMES_R27.tsv` has 79 lines.

The above table SHA is exactly the previously observed R16 `AFFINE_RUNS_1T.tsv` hash. Algorithm generation did not read any R16 epochs; R16 was only consumed by the final validation phase.

The final Farey regime (from `n=752555238040` to `N`) contains zero positive increments, despite a change of sign of `u-v` over the frozen parameter enclosure. The implementation correctly avoids selecting an irrelevant winner for that regime, while the risk oracle still certifies its actual historical-arc winners at the declared endpoints.

## Evidence scope and next check

The general last-survivor law is proved in `PROOF.md`. The finite S23 run uses the given 24-digit rational theta enclosure and integer horizon; each exact comparison is checked at both endpoints where the affine coefficient choice matters. The output files are generated deterministically by `VERIFY_R27.py`; the hashes above certify the actual locally produced files.

Independent mathematical review, shared-task CLAIM, and activity-to-checkpoint native binding remain separate operations. Next: group repeated Farey regimes, then directly output the 298 affine rows without expanding all 9,697 individual positive-event labels.
