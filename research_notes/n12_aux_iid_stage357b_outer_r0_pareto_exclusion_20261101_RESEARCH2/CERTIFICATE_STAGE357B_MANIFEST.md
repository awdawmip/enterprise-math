# Stage357-B — Exact certificate manifest

The *complete*, regenerable 71-cell table is produced by the same committed `REPRO_STAGE357B.py` and was generated in the actual author-side execution. Run `python3 REPRO_STAGE357B.py` in a writable copy of this directory. It writes `CERTIFICATE_STAGE357B_OUTER_R0.csv` with exact rational coordinates, leaf types, witnesses, lower bounds and recursion depths. No external dependency or external API is used.

- Actual generated CSV size: **14044 bytes** (71 data rows plus header).
- Actual generated CSV SHA-256: **eab8c77d8f2ac0c1d7ff98ef4aeff2b6af8fca47649a5c621296117aa4597671**.
- Verified executed stdout SHA-256: **064e43912f84d9962f41ab2a39a7987c27e8aac3075b23e7ecc0d75c3c06b26f**.
- Exact leaf counts: left 4 no-zero / 1 budget-excluded / 15 strict dominated; right 2 no-zero / 18 budget-excluded / 31 strict dominated. Total 71, max depth 13, total covered interval length 996/1000.
- All 46 dominance witnesses satisfy the two exact strict inequalities; all 19 exclusion cells satisfy the exact budget inequality.
- Computation and scientific inference scope: continuous real domain for the stated external Bernoulli/BRC labeled observer. No Native P000/X6 or BRC-Shor transfer and no formal review/admission.

The full 14,044-byte *generated CSV file itself* is retained in the current conversation artifact workspace; **the GitHub artifact is the source checker plus this size/hash manifest, not a claim that the generated CSV bytes were separately uploaded to GitHub**. To independently verify this manifest, execute the committed script and SHA-256 hash its produced CSV; the program itself validates the partition and strict inequalities rather than trusting a stored table.
