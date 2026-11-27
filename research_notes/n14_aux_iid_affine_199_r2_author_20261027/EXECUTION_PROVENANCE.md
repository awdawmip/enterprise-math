# Stage199 author local execution and evidence provenance (2026-10-27)

Status: PORTABLE_AUTHOR_EXACT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED. This file records actually observed local execution and identifies GitHub reference implementations separately.

## Actual local execution

1. `verify_stage199.py` executed with Python `fractions.Fraction` suffix dynamic programming and **separate unmerged full-ordered-history integer-weight DFS**, terminal denominator `24**14`. Actual stdout includes:
   `STAGE199_AUTHOR_EXACT_FULL_REAL_PASS 414994 ordered DFS nodes`.
   Four action-corner visits `(104410,104410,103087,103087)`; first arrival B=(7,0,1):7, Z=(14,0,0):1, B→Z:0; four vectors each agree **exactly** between DP and DFS. 680 states, 1238 strict positive gaps.
2. `scan_stage200.py` separately executed exact dual candidate scan; stdout:
   `STAGE200_DUAL_SCAN_PASS`.
   K=L=`1358449620408/10345594439`, H=`1821575844832789801808808179/17710532969288194722889728`; tie states (7,5,2) P/C, (14,0,0) P/Q; primal Stage200 **not proved**.
3. Additional *non-Python* independent arithmetic validation of the published rational Stage199 certificate used native JS `BigInt` and checked four corners, all affine terms, mixed zero, balancing probabilities, endpoints, nonnegative time dominance and dual slope. Actual result `STAGE199_REMOTE_CERTIFICATE_BIGINT_CROSSCHECK_PASS`. This independent arithmetic check is not an independent author/reviewer or an independent proof.

**Original executed local files** (actual SHA256 of original file bytes):
- `verify_stage199.py` — `a2e9ee2a6b48ceee0f9b8a1f4ce576ac2ae79d5f7e3506a56532c34e15793818` (6082 bytes).
- `scan_stage200.py` — `219374d0d69b278e708e009c3d31df0e77da8c2a9e5ae1b1b4c0fc8fe13d2ec5` (2394 bytes).
- `run199.log` — `882b20bf94487e62dcda5427cab006be10f585fe24fa57073aaea30efbbb4da6` (1978 bytes).
- `run200_dual.log` — `9b8bde6b031a2292a3f40754fd76cce52c8a4e0a3a5a26dd00350815189e83d9` (483 bytes).
- Original local `certificate199.json` — `b456774210f82575b369897a372e63343d31b8efadf75fec43620333a53fc61a`; original local `certificate200_dual.json` — `222023e0a79d1bcbcee57a9b047932815982c767f9be0c13352dcfa7d7636004`.
- Local complete nine-item `manifest_sha256.json` checked by computing all eight constituent SHA256 and byte counts. Generated portable original-evidence archive `EM_STAGE199_AUTHOR_EXACT_PORTABLE_20261027.tar.xz` SHA256 `1aef33ad47a02578378979923f2aab60b3f52a44adf0da0527546b1388de7d38`; 9 members, xz integrity verified. This archive is a conversation artifact, **not** asserted to have been uploaded to GitHub or native Source.

## GitHub consumption

Actual reusable, complete **reference** programs stored under this same directory: `REPRO_STAGE199.py` and `REPRO_STAGE200_DUAL.py`. Their saved Git Blob identities were checked via connector, and Stage199 rational certificate independently checked against saved bytes. **Remote storage/readback is not remote program execution**; anyone using these reference programs should run them in their own environment.

Scope: external IID auxiliary mathematics. Exact positive P/Q branch weights preserve provenance (BRC); count-state DP is sufficient only within the declared IID observer. No physical P000/X6 transfer. GitHub identity `awdawmip` had repository write authority, while native Sites MCP status 0.6.11 reported `research_authority_granted=false`; Source CLAIM/Result and independent Driver review remain separate.
