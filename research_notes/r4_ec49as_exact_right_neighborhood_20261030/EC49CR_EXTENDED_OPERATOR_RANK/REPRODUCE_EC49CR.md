# EC49CR — Independent reproduction from PR #1730 files

The canonical readable theorem and its precise typed domain are in `README_EC49CR.md`. Everything needed to independently recompute the **n=12 literal 132-column determinant lower bound** and the formal/true-path rational ranks is present in this directory of the GitHub PR.

## Inputs and provenance

- Actually executed source: `VERIFY_EC49CR.py`, `VERIFY_EC49CR_RATIONAL.py`, `RECHECK_EC49CR_INDEPENDENT.py`, `VERIFY_EC49CR_NATIVE.py`. These exact text Git blobs matched local executed source.
- The unchanged prior `VERIFY_EC49CJ.py` helper and original `native_signed_brc.py` have been preserved losslessly as `EC49CR_REPRO_DEPENDENCIES.tar.xz.b64`, whose decompressed archive SHA256 is `db375df470a3327029aecc0a1d0b46f3497d2544f696c6a0a7c5b6ec2e71f1e6`. They are real source dependencies, not newly simulated native methods.
- Full literal 132-path n=12 certificate is `CERT_EC49CR_REAL_12_SLE2.json.xz.b64`: after decoding and xz expansion the JSON SHA256 must equal `2987b49e2bcc1505e742edf934d909de8ad2480bf19b2d23bef68ee46eaa8a5e`. It contains all nine per-fiber row selections, authentic 12-letter primitive signed paths and expected modular determinants, so rechecking does not require the generator.
- `EXACT_SUMMARY_EC49CR.json` records theorem rank table, literal integer minors, frozen source pins, verification and outstanding authority status.

## Reproduce (Python3 with SymPy)

Download the plaintext program files, the two *.b64 files, and the summary from this folder. In one directory:

```sh
base64 -d EC49CR_REPRO_DEPENDENCIES.tar.xz.b64 | tar -xJf -
base64 -d CERT_EC49CR_REAL_12_SLE2.json.xz.b64 | xz -d > CERT_EC49CR_REAL_12_SLE2.json
sha256sum CERT_EC49CR_REAL_12_SLE2.json
python RECHECK_EC49CR_INDEPENDENT.py CERT_EC49CR_REAL_12_SLE2.json
python VERIFY_EC49CR.py --no-path
python VERIFY_EC49CR_RATIONAL.py
python VERIFY_EC49CR_NATIVE.py
```

These are recomputation instructions. The author already executed the underlying programs, exact native-X6 comparison and independent certificate checks; no external reviewer execution or independent Driver acceptance is claimed. The full original 17,628-byte execution bundle including additional n=4,6,8,10 literal certificates, 4 source reports and captured original log remains a **conversation attachment only**, with SHA256 `2e15022c9ec3e9bf891490e4c25976c22c3df8f21fafc4753463f6da6bd474e0`; it is **not** an additional uploaded GitHub file.

In this mathematical setting, exact rational elimination is a proof of the stated finite row ranks and explicit nonzero modular determinants are independent Q-rank lower bounds. The n>=12 continuation follows the stated analytic neutral prefix insertion lemma. The source-native research gateway reported `BACKEND_IDENTITY_CHECK_UNAVAILABLE`, `operation_sent=false` for this actual client; not a task CLAIM, Result or review.
