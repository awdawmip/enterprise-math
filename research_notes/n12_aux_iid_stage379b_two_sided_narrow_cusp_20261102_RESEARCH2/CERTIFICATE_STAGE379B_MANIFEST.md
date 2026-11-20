# Stage379-B complete certificate manifest

Normalized CSV CERTIFICATE_STAGE379B_TWO_SIDED.csv, independently generated and replayed locally; 182434 UTF-8 bytes; SHA256 aa48034a214df51a493d387862e12d05eed5b18681299574f41264656262d828.
Columns: region,path,xlo,xhi,ylo,yhi,lower; exact dyadic full binary tree cover, region/path/box equality and strict rational lower bound verified.
Counts: P=1344, Q_LO=37, Q_HI=72, total=1453, unresolved=0.
Local standalone exact checker output: STAGE379B_EXACT_NARROWER_CUSP_QY_PASS.
Repository REPRO_STAGE379B.py is a short deterministic adapter to pinned Stage377 core Git Blob 9b54a83059ff965e4807577448c3828cc64e8f04. It regenerates and verifies the same CSV hash via:
python research_notes/n12_aux_iid_stage379b_two_sided_narrow_cusp_20261102_RESEARCH2/REPRO_STAGE379B.py --emit /tmp/stage379b.csv
python research_notes/n12_aux_iid_stage379b_two_sided_narrow_cusp_20261102_RESEARCH2/REPRO_STAGE379B.py --verify /tmp/stage379b.csv

The entire executed CSV and standalone checker were retained as session artifacts; the repository stores the reproducible generator, proof, digest, and actual standalone stdout. Hashes identify bytes, not mathematical admission.
