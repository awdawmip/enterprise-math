# Reproducible exact author evidence

Files: PROOF.md (complete derivation), CERTIFICATE.json (exact rational outputs), VERIFY_EXECUTED.py.gz (the actual author-executed Python 3 checker, compressed with gzip), NEXT_TASK.md (narrow unresolved question).

Decompress: python -m gzip is not a CLI module on all installations; use Python: import gzip; open("verify.py","wb").write(gzip.open("VERIFY_EXECUTED.py.gz","rb").read()) then python verify.py. The checker only uses Python standard library.

Original uncompressed executable SHA-256: 05064e81a379216dd4a6f74502b8cb90726d6699a3354ee00ccf9e6b87487b94.
Compressed executable SHA-256: df8b206f94055e923beadb07ad958046fbe0f9a8cb377b7b4fcf256c6be25dcd.
Expected compressed Git blob SHA-1: 33fe17d1c0960beb1ac572a25ceb97ff1faab3ff.
Local evidence ZIP: EnterpriseMath_R1_N14_NonIID_TwoLaw_20261026.zip, SHA-256 b6283b54e44e1eb14a33aa7cab2b0f1a1bc244a475ae7f4729f53ada26d151dd; this archive includes the longer local derivation, raw script, certificate and file hashes.

Six exact full joint-flow checks completed locally (N=3,4,5 each under P,Q). Author theorem status only; no native Driver review/Result/Working Truth. GitHub storage and readback are not remote program execution.
