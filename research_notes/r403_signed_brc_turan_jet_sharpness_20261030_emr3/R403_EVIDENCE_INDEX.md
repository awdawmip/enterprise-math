# R403 evidence and exact recovery

This is a signed BRC auxiliary-model mathematical draft, not a native claim/result/review. Human-readable theorem and proof: R403_PROOF.zh-CN.md.

Exact executed Python source was losslessly gzip-compressed and base64-encoded in r403_exact_verify.py.gz.b64. Actual generated 7009-byte evidence JSON is in R403_EVIDENCE.json.gz.b64. Neither payload contains credentials. Uncompressed source SHA256 = a32f9e17689bbd2f271f9241e6ae24c59e518a4ffbf1ae65dacf3df846b06093; uncompressed evidence SHA256 = 0ada5e717aa2aa99a561317c589fa436cc146df130a6fccd807f57ab6a55e40f.

Recover locally (inside this directory): python -c "import pathlib,base64,gzip; p=pathlib.Path('r403_exact_verify.py.gz.b64');pathlib.Path('r403_exact_verify.py').write_bytes(gzip.decompress(base64.b64decode(p.read_text().strip())));p=pathlib.Path('R403_EVIDENCE.json.gz.b64');pathlib.Path('R403_EVIDENCE.json').write_bytes(gzip.decompress(base64.b64decode(p.read_text().strip())))"

Execute: python r403_exact_verify.py 240. Expected R403_EXACT_PASS, exact pairs 28680, positive 28558, negative 122, zero 0, independent delta checks 560. Regenerated JSON should have the same SHA256. All coefficients use integer arithmetic. The all-r s=1/s=2 proof is separate; finite scanning for s>=3 is not a universal proof.

Frozen knowledge main@96380d0434ed98c5425defd71c8bd31c86639859; project control main@4e72c173d9a6e82db691a8ececa673890d2e0429; R402 prior PR commit 61f791f347056222fe253b641911d4f87d90eb29. Next problem: show D_(r,s)>0 for all s>=3 or isolate exact counterexample.
