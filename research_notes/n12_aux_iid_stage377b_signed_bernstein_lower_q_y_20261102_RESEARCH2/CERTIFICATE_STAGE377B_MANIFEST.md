# Stage377-B exact certificate manifest

Date: 2026-11-02 (Asia/Shanghai).
Source: REPRO_STAGE377B.py, Git blob SHA 9b54a83059ff965e4807577448c3828cc64e8f04, exactly matching the actually executed local original.
Outputs:
- Generation log: REPRO_STAGE377B_EXECUTED_STDOUT.txt.
- Independent CSV replay log: REPRO_STAGE377B_REPLAY_STDOUT.txt.
- Full deterministic CSV filename: CERTIFICATE_STAGE377B_SIGNED_BERNSTEIN.csv.
- CSV raw length: 51353 bytes, 466 leaves.
- CSV SHA256: bcb2b5b8ba4f07288fc462de02ce7cb4873fce84734c1015433beac0e33338c3.
- Two fully repeated source generations yielded identical CSV bytes and stdout; separate CSV path replay verified all 466 leaves and complete binary partition.
- Recreate full CSV: python REPRO_STAGE377B.py --emit CERTIFICATE_STAGE377B_SIGNED_BERNSTEIN.csv
- Reverify provided CSV: python REPRO_STAGE377B.py --verify CERTIFICATE_STAGE377B_SIGNED_BERNSTEIN.csv

Scientific pins stay GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
The original CSV is also provided as a conversation research attachment. Github's complete exact checker deterministically reproduces the same CSV and its SHA256 for future research.
