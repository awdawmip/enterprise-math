# Stage378-B certificate manifest

Full CSV: CERTIFICATE_STAGE378B_TWO_SIDED.csv; 94157 bytes; SHA256 1c7552cc6ae40cb133faee01b59b47329e4357691bb58e7198cabda2b5a826bc; 794 leaves P=637, Q_LO=57, Q_HI=100.

The original standalone standard-library REPRO_STAGE378B.py and its 94157-byte CSV are available as local attachments in the run. The in-repository REPRO_STAGE378B.py reuses the exact Stage377-B source by Git blob 9b54a83059ff965e4807577448c3828cc64e8f04 and regenerates/verifies the normalized CSV hash. Execute from checkout:

python research_notes/n12_aux_iid_stage378b_two_sided_nearcusp_20261102_RESEARCH2/REPRO_STAGE378B.py --emit CERTIFICATE_STAGE378B_TWO_SIDED.csv
python research_notes/n12_aux_iid_stage378b_two_sided_nearcusp_20261102_RESEARCH2/REPRO_STAGE378B.py --verify CERTIFICATE_STAGE378B_TWO_SIDED.csv

These are continuous-domain exact rational certificates: no sampled grid or floating-point rounding.
