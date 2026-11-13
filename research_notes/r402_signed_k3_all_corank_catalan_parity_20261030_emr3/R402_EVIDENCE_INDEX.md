# R402 exact evidence — full lossless record and readback guide

The full machine evidence EVIDENCE.json is stored **losslessly** as EVIDENCE.json.br.b64, base64 of Brotli quality-11 compressed original UTF-8 JSON. It is a full record of five theta values and ranks 1..8, including pointwise top-coefficient outputs and exact coefficient/turan degeneration orders, not an empty placeholder or only a checksum.

Actual local execution of the matching VERIFY.py source:
```text
R402_EXACT_FINITE_CROSSCHECK_PASS theta_cases= 5 ranks= 8 catalan_identities= 40 polynomial_differences= 40 degenerate_orders= 36 sha256= a2e4a304573b98f3cff141e0ab881f8f4f56bfc1eccfd43de0af255022309a26
theta -1/2 a 38 last_catalan 27031713965781697808553082880
theta 0 a 30 last_catalan 615568110300000000000000000
theta 1/2 a 22 last_catalan 4306246939764863154913280
theta 15/8 a 0 last_catalan 0
theta 187/100 a 2/25 last_catalan 18743296/4656612873077392578125
```

Evidence content bytes: 9922. Original JSON SHA256: a2e4a304573b98f3cff141e0ab881f8f4f56bfc1eccfd43de0af255022309a26. Brotli-compressed original bytes SHA256: 397c74cd18e8ccc79643273349d7d64e3ab3975bf0c572fe97f6102f6b412080. Base64 count before terminal newline: 2000 characters. Original stdout SHA256: ec1d5c25598fc306c9cba65897d7e018d6b80719feba1eb7b81f7e1173d57b9c. Executed verifier Git blob SHA1: d4bbffb08a1161275939f89dc64995790d591492.

Rebuild full machine JSON (requires Python brotli for *decompression only*; direct verifier itself is pure Python stdlib):

```bash
python - <<'PY'
import base64, hashlib, pathlib, brotli
p=pathlib.Path('EVIDENCE.json.br.b64')
raw=brotli.decompress(base64.b64decode(p.read_text().strip()))
assert hashlib.sha256(raw).hexdigest()=='a2e4a304573b98f3cff141e0ab881f8f4f56bfc1eccfd43de0af255022309a26'
pathlib.Path('EVIDENCE.json').write_bytes(raw)
print('R402_EVIDENCE_RECOVERY_PASS',len(raw))
PY
python VERIFY.py
```

This proof is for **all positive integer coranks via algebra**, not from these 40+40+36+28 finite checks. The tests cover theta=-1/2,0,1/2,15/8,187/100 and r=1..8; 36 exact degeneration coefficient orders and 28 Turan divisibility checks. An extra r<=10 exact jet calculation succeeded as author-side supplemental testing, but is not part of the frozen 9922-byte artifact. No signed branch was rewritten as positive mass; no physical/native X6 inference or formal admission.

Full author-side downloadable ZIP within the originating chat contains the longer Chinese proof, original executable VERIFY.py, actual evidence JSON, stdout, SHA256SUMS, HANDOFF and NEXT_TASK; this GitHub PR stores full verbatim verifier and losslessly recoverable JSON, alongside the readable mathematical argument.
