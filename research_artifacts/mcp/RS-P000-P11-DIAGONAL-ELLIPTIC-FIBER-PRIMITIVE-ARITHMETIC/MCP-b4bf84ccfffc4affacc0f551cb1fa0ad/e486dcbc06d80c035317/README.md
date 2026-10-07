# Reproduce the P11 exact interface evidence

Keep all package files in one directory, using their original filenames. Python 3.10+ standard library is sufficient; no project checkout, network, Sage or external elliptic package is needed.

```sh
python -I check_p11_family.py --output REPRODUCED.json
```

REPRODUCED.json must be byte-identical to RUN.json. The program verifies the SHA-256 and Git blob of both reused sources before loading them. It checks the two frozen witnesses, first three multiples, all 25 affine coordinate pairs over F5, and targeted invalid interfaces. It does not invoke the old census.

RETURN.md is the main theorem argument. FAMILY.md supplies the all-n construction. REFERENCES.md gives exact external theorem hypotheses and source hashes. VALIDATION.md distinguishes exact finite certificates, isolated reproduction, and the shared-context proof audit. PROVENANCE.json and MANIFEST.json bind this execution and all delivered files. These records do not grant independent Driver acceptance.
