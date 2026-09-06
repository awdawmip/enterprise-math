# RSA-270：深入研究第 10 轮——压力测试发现并修正 C3 符号隐患、套件定版

Progress-Event-ID: `rsa270-deep10-stress-c3-signfix-index-1l6n8i`
At: `2026-09-07T06:40+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 10`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 0k5m7h; P000 assumed`
Kind: `PROGRESS / CORRECTION / SUITE FINALIZATION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 10. No factor obtained.

### Stress test caught a genuine certificate defect (C3 sign hazard)

The 10-semiprime suite stress test initially rejected one REAL factor pair (9/10). Root cause: certificate C3's paired joint set used the class-representative `|l*p0 - q0| mod 72`, but the absolute value is **not modularly equivariant** under sign flips — when the real `l p - q` and the class-rep `l p0 - q0` have opposite signs, `|l p - q| mod 72 != |l p0 - q0| mod 72`, so the pairing `(x mod 72, y mod 72)` mismatched (semiprime 7, l=2: real pair (15, 53) vs class entry (15, 19)).

**Fix (verified)**: the sign-safe joint certificate pairs `x` with BOTH signs: `y = +-(l p - q) mod 72`; the `|.|`-paired form remains valid only conditioned on the vertex-side bit. After the fix: **10/10 real factors accepted, 10/10 wrong factors rejected**.

This is a correction to 5f0h2c's C3 (recorded there as the `|.|` pairing): the unconditional form is the sign-safe two-sign version; the one-sign version requires the side bit of 8i3k5f.

### Final layer-2 certificate index (12 entries)

C1 square identity (1f4c8e) ; C2 V-function/rays/vertex (6f1e8a/3d8f0a) ; C3 (x,y) joint sets — **sign-safe form** (5f0h2c + this round) ; C4 tower closure 72 maximal (6g1i3d) ; C5 y-sequence certificate 12 sequences (6g1i3d/7h2j4e) ; C6 layer-1 structurelessness (4e9g1b) ; C7 CRT root laws (3d8f0a) ; C8 two-l Plucker (3d8f0a) ; C9 sum/diff + vertex-side bit (8i3k5f) ; C10 side law + forced-sum family (9j4l6g) ; C11 parity (0k5m7h) ; C12 full-suite verifier (0k5m7h + this round, stress-tested 10/10).

## Artifacts

- Script: `rsa270_deep10.py` (conversation-local; suite stress test + sign-safe fix).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T055500+0800-rsa270-deep9-parity-suite-integration-0k5m7h.md`.

## Next

The certificate suite is finalized and stress-tested. The deep-research line has no remaining identified executable items within the current frameworks; next rounds without new directions/external facts would re-enter closed routes.
