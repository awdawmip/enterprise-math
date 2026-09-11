# RSA-270：深入研究第 8 轮——一般侧律与强制和证书族（含一个测试设计更正）

Progress-Event-ID: `rsa270-deep8-side-law-forced-sum-9j4l6g`
At: `2026-09-07T05:10+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 8`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 8i3k5f; P000 assumed`
Kind: `PROGRESS / EXACT THEOREM / CORRECTION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 8. No factor obtained.

### General side law (exact, verified)

For branch `l`: `x+y = 2 l p` (hence `= 0 mod 2l`) iff `l p >= q`; `x+y = 2 q` (`= 2q mod 2l`) iff `l p < q`. Verified on 8 semiprimes x all primes <= 31 covering both sides.

### Forced-sum certificate family (prior band `r < l` for all `l >= 3`)

Since the band is `r in [1.765, 2.266]`, every prime `l >= 3` satisfies `r < l`, hence **any claimed (x,y) observation for branch `l >= 3` must satisfy `x+y = 0 (mod 2l)`** — a one-sided real constraint. Verified on synthetic `r < 3` semiprimes for `l in {3,5,7,11}`. Class-level shadows: `l=5,7` give `{0}` even at class level; `l=3` mixes to `{0,4}` (the mod-72 shadow does not determine the real side — a test-design correction recorded: the class-level forcedness test of the draft was mis-designed and replaced by the real-side constraint plus shadow tables).

### Bit accounting (certificate suite)

- N-only computable: forced lattice `S = 16 mod 72` -> 6.17 bits (unchanged);
- verification-only (layer-2): 1 vertex-side bit (`l=2`) + the forced-sum family (`l >= 3`);
- the side bit is readable from claimed observations but does **not** extend the N-only computable part (layer-2 observability wall).

## Artifacts

- Script: `rsa270_deep8.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T042500+0800-rsa270-deep7-sumdiff-vertexbit-8i3k5f.md`.

## Next

1. Extend the certificate suite record with the side law and forced-sum family (entries 9-10).
2. The complete layer-2 certificate structure is now: square identity, V-function, joint (x,y) sets, sum/difference linear form, side law + vertex bit, forced-sum family, CRT/Plucker, sequence certificate. A consolidated "layer-2 certificate index" record is the remaining curation step.
