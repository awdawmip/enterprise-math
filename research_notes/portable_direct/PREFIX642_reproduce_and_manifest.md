# PREFIX-642 reproducibility and independent review

Science inputs: immutable task freeze `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; exact original native BRC action implementation reuse `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.

GitHub artifacts: proof `2026-11-10_prefix642_single_base_periodic_eventual_brc.md`, runnable `PREFIX642_single_base_periodic.py`, losslessly encoded **actual executed full JSON** `PREFIX642_raw_results.json.gz.b64`. Decompress:
```sh
base64 -d PREFIX642_raw_results.json.gz.b64 | gzip -d > PREFIX642_results.json
sha256sum PREFIX642_results.json
```
Expected raw JSON SHA256: `091bd0810e8dff4c215960051d31f615e6d5157fe18cc037a3706a12e7ceb8d3`. Actual executed local program SHA256 `b63b9b763b674f78891f0db2972deb10fa4f264e6ad2bde392bbddff382d993d`. The GitHub source is a readable reproduction transcription of the executed program, with the same operators, test cases, and assertions; its report output filename is `PREFIX642_check_results.json`, whereas the executed local script wrote `PREFIX642_results.json`. Timings will differ by environment.

To reproduce using the original frozen 96-port/576-label actions, run from one folder containing:
- `PREFIX642_single_base_periodic.py`
- `PREFIX640_fraction_free_rolling_jet.py` from PREFIX-640 complete archive, PR #1937.
- `PREFIX638/PREFIX638_native_jet_support.py` from PREFIX-638 complete archive, PR #1925.

`python PREFIX642_single_base_periodic.py`: exact operator equality, independent native-action oracle, and transient-prefix tests. Expected summary counts `ALL_ASSERTIONS_PASS 80 31 160`.

Local research handoff archive contains uncompressed proof, original executed program, raw JSON, run log, dependency source and checksums: `ENTERPRISE_MATH_PREFIX642_SINGLE_BASE_COMPLETE.tar.gz` (15,000 bytes; SHA256 `9705efa323580fa8dc76a387fc50d9e343bfcdc2c01aebeb9a82ef9af93c14dc`), provided in the generating conversation. GitHub branch + full remote raw JSON independently preserve the critical research evidence. No research credentials, passwords, private keys or sensitive data are included.

Research-Activity-ID `RA-2615A64775908B086D4AB997`; Researcher-ID `EM-X6-EC43D8`. Independent mathematical review not yet performed; no native task CLAIM, Result, or Foundation/Working Truth promotion.
