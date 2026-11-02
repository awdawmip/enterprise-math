# Stage387-B exact audit / deterministic evidence manifest

Date: 2026-11-03 Asia/Shanghai. Research2 branch of Draft PR #1736.

The independently reconstructed Stage373 complete certificate is available as `CERTIFICATE_STAGE373B_REGENERATED.csv` in the research run's exported attachments. Its exact UTF-8 data is regenerable using:

```sh
python REPRO_STAGE387B_INDEPENDENT.py --emit CERTIFICATE_STAGE373B_REGENERATED.csv
python REPRO_STAGE387B_INDEPENDENT.py
```

Both commands were run. The first command wrote the CSV; the second was independent program replay without generating it. Their stdout files were compared byte-for-byte, and `cmp` reported equality.

| Artifact | UTF-8 bytes | SHA256 |
|---|---:|---|
| `CERTIFICATE_STAGE373B_REGENERATED.csv` | 1581616 | `fd8a761683245556cef44f15bd44fd1fadb539d6c3fa868f1dec6ff75b0bd5ae` |
| `REPRO_STAGE387B_INDEPENDENT.py` |  | `0803b0b54a32e6cda9b8263f261c78740d93cb9729a8ac9f856c019a2497450c` |
| `REPRO_STAGE387B_EXECUTED_STDOUT.txt` |  | `205d81e2145ce95338be1ea437581847e301ac0e1fa855c5e1db3ca8ce7ad40d` |
| `REPRO_STAGE387B_REPLAY_STDOUT.txt` |  | `205d81e2145ce95338be1ea437581847e301ac0e1fa855c5e1db3ca8ce7ad40d` |

Exact 8,544 closed leaves: 4200 left, 4258 low-right and 86 high-right; all-real dyadic rectangles (boundaries included), no unresolved leaves. Maximum depths 20, 23, 14. Strict cost differences versus the independently reverified feasible comparator `>1/10^6` and `>3/10^6` for the two excluded right-y regions. The CSV digest and length reproduce the original Stage373 author's exact certificate bytes; it is sufficient to run the attached program to produce every rational leaf and check the strict inequalities and area cover.

Scope: external frozen Bernoulli/BRC auxiliary model, conditioned on upstream Stage370/372 ordered optimizer core and earlier global localization. No project-native Result/Review, P000/X6 observational transport or mathematical promotion is asserted. Scientific pins are preserved in the proof and program. Published text and code are the deterministic source of the full CSV; the 1.58MB CSV is retained as a run attachment rather than duplicated as a repository blob.
