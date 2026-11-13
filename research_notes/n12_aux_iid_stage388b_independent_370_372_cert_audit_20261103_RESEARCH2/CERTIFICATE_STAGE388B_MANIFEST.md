# Stage388-B exact certificate manifest

Executed independently locally with Python fractions.Fraction:
- python REPRO_STAGE388B_PORTABLE.py --emit-dir . (certificates actually regenerated)
- python REPRO_STAGE388B_PORTABLE.py (no-write exact replay)
- Both program executions returned STAGE388B_INDEPENDENT_STAGE370_AND_STAGE372_PASS.

CSV | exact bytes | SHA256 | leaves
--- | ---: | --- | ---:
CERTIFICATE_STAGE370B_REGENERATED.csv | 257043 | b21fe204b5baa2485dfb08d529cd9a003f2491caf83d2e27012cb83b8dab58a0 | 1662+95 (plus 1191 exact R cover)
CERTIFICATE_STAGE372B_REGENERATED.csv | 782383 | 5608a0843c3105eafa75c65b7496050391e3781919c337acb4c861d2303c6323 | 4200+51

The certificates were regenerated locally and the complete CSV digests matched the original Stage370-B and Stage372-B source records. Their 1,039,426 bytes are *not* embedded in this Git commit; the runnable code generates the full exact certificate bytes with verified digests. Total closed leaves including Stage370 R support: **7199**, unresolved **0**. Full certificate CSVs are additionally saved as this run's artifacts.

Scientific pins: Global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
Status portable author check, not formally reviewed/admitted.
