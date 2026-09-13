# RSA-270：深入研究第 2 轮——内部图谱：逐层最优对齐与信息账目

Progress-Event-ID: `rsa270-interior-atlas-accounting-9t4v6w`
At: `2026-09-07T13:40+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 2`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 8s3u5v; P000 assumed`
Kind: `PROGRESS / ATLAS / ACCOUNTING`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 2. No factor obtained.

### Interior atlas (per-layer optimal alignment, verified)

`mod 8 (|F|=4): min metric 4, residual 1 (sum frame) ; mod 9 (3): 3, residual 1 ; mod 16 (8): 16, residual 2 ; mod 24 (4): 4, residual 1 ; mod 27 (9): 18, residual 2 ; mod 72 (12): 12, residual 1 ; mod 144 (24): 48, residual 2 ; mod 216 (36): 72, residual 2 ; mod 432 (72): 288, residual 4`

(Label note: the printed achiever shows the first-row direction; the forced coordinate is the sum row — the achiever is the sum-type alignment at every layer, per 7r2t4u.)

- At every layer the **sum frame is the layer-optimal alignment**; its residual grows `1 -> 2 -> 4` exactly along the forced-lattice tower (layers where S is forced: residual 1; S two-class layers: 2; 432: 4).

### Information accounting

- Within the 72-lattice: gap axis 6 classes = `log2(6) = 2.58` bits of residual ambiguity; the forced sum carries the other `3.58` bits — total `6.17` bits, CRT-consistent (2-adic gap 1 bit + 3-adic gap 1.58 bits).
- The alignment atlas therefore quantifies the interior completely: **sum-coordinate = the forcing carrier, gap-coordinate = the residual carrier**; the best alignment per layer achieves the minimal residual, and the residual grows only with the class tower.

## Artifacts

- Script: `rsa270_align3.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T125000+0800-rsa270-align-layer-stability-metric-8s3u5v.md`.

## Next

1. The atlas is complete for the alignment program; the residual growth `1,2,4` is the tower in metric form. Awaiting further directions or external facts.
