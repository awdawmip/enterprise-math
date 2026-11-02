# Stage380-B — Portable exact certificate manifest
Frozen input pins: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.

REPRO_STAGE380B.py is fully self-contained with Python standard-library Fraction, not a version-pinned adapter. It was executed locally in emit mode and verify mode; stdout matched byte-for-byte:
STAGE380B_PARETO_FACE_REDUCTION_PORTABLE_PASS.

CSV CERTIFICATE_STAGE380B_PORTABLE.csv: 3350 UTF-8 bytes; SHA256 65c35b8863113dd06903a1e89b855197d7fac7843149272618f01d423a9ac425.
It has 40 exact endpoints (32 audit comparisons and 8 residual channel bounds) and 16 rational witnesses for all open sign combinations in the Stage379 rectangular tube; witnesses do not claim joint-budget feasibility. Reproduce and independently verify:
python REPRO_STAGE380B.py --emit CERTIFICATE_STAGE380B_PORTABLE.csv
python REPRO_STAGE380B.py --verify CERTIFICATE_STAGE380B_PORTABLE.csv

Additional expanded local standalone verification: 5670-byte exact certificate SHA256 5c4eceb089d1b9d531cc0baca2d4ff5809a844afcb590e2d61b094b4e04a27a9, marker STAGE380B_EXACT_PARETO_QUADRATIC_COLLAPSE_PASS. The locally executed verifier/certificates are preserved in the conversation assets. GitHub stores a shorter fully executable exact version; authorship and review/admission remain separate.
