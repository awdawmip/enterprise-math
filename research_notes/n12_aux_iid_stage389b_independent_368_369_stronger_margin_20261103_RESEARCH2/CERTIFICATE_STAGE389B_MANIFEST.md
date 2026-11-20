# Stage389-B exact certificate manifest

Frozen research pins: Global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`.

Execute `python REPRO_STAGE389B_INDEPENDENT.py --emit-dir DIR`, then `python REPRO_STAGE389B_INDEPENDENT.py`. Both executions were performed locally with identical stdout, and generated nonempty CSVs are attached to this run. The remote source and stdout suffice to recreate/verify them deterministically, with exact Fraction semantics.

* `CERTIFICATE_STAGE368B_REGENERATED.csv`: 43,413 bytes; SHA256 `adcca00c9a5cf502ab03fcecf324b321683487dab432b28ac59ee0b549c16040`; 604 real-cover leaves (338 outside and 266 inside), closed area=1.
* `CERTIFICATE_STAGE369B_REGENERATED.csv`: 189,212 bytes; SHA256 `c60855319b26ba0e842906aa9126489568b001eef5945fd24247e64369f884d9`; 1304 R/S leaves; exact areas 13/5000 and 767/500000.
* `REPRO_STAGE389B_EXECUTED_STDOUT.txt`: original executed diagnostics; no-emit replay identical.
* exact strengthened cost comparison: > `9379440296847963487/160000000000000000000000` for all feasible source-left pairs.

Scope: exact continuous real boxes, all 16 provenance-labelled Bernoulli port comparisons, four independent signed residuals, this frozen auxiliary model. Source stored in Research2 Draft PR; native Source Result and independent Driver admission remain open.
