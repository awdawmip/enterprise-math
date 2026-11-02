# EC49ER — Reproduce the verified finite certificates

All source and executed reports are losslessly packaged as UTF-8 base64 of a gzip-compressed tar archive. No credentials or private identifiers are included.

To extract, download `EC49ER_COMPLETE_EVIDENCE.tar.gz.b64` then run:

```sh
base64 -d EC49ER_COMPLETE_EVIDENCE.tar.gz.b64 | tar xz
sha256sum -c SHA256SUMS_EC49ER.txt
python VERIFY_EC49ER.py
python VERIFY_EC49ER_ALL_M3.py
```

The two independent cross-checks require SciPy / HiGHS:

```sh
python VERIFY_EC49ER_MILP.py
python VERIFY_EC49ER_M3_MILP.py
```

The reported `PASS` for 3 M=2 cases and 434 M=3 cases is based on previously actually executed source/results in the archive. Reruns overwrite their JSON result files in the current working directory. `EC49ER_M4_S4_UPPER.json` reports only an 80-edge **feasible upper bound**, not optimality. No full H=6 Pareto frontier is asserted.

Original tar SHA256: `bee8a4768604ef74a2d0261524b8ad901ef5b9362251b17ab462e7cc3cd7665a`.
