# RSA-270：深入研究第 1 轮——对齐跨层稳定性、方向轨道结构、内部度量谱

Progress-Event-ID: `rsa270-align-layer-stability-metric-8s3u5v`
At: `2026-09-07T12:50+08:00`
Scope: `enterprise-math / RSA-270 / deep research (new goal) round 1`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 7r2t4u; P000 assumed`
Kind: `PROGRESS / CLASSIFICATION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 1 (new goal). No factor obtained.

### A. Per-layer alignment type table (verified)

`mod 8 (|F|=4): pure 8 / mixed 8 / sum 8` ; `mod 9 (3): pure 16 / sum 8` ; `mod 16 (8): pure 8 / mixed 16` ; `mod 24 (4): pure 8 / mixed 8 / sum 8` ; `mod 27 (9): pure 16 / mixed 8` ; `mod 72 (12): pure 8 / gap 8 / sum 8` ; `mod 144 (24): pure 8 / gap 8 / mixed 8`.

Structure: the **sum-octet exists exactly on the layers where S is forced** (8, 9, 24, 72) and vanishes where S regains 2 classes (16, 27, 144); the gap-octet (6-class axis) exists exactly at 72/144. The alignment type table IS the forced-lattice tower in alignment language.

### B. Direction-orbit structure

The 12 first-row directions split as `sum {(1,1),(-1,-1)} (2) + gap {(1,-1),(-1,1)} (2) + pure (8)`; each direction carries 4 second-row lifts x 2 signs = 8 rotations per octet — `24 = 8+8+8` group-theoretically accounted.

### C. Interior metric spectrum (mod 72)

`|P'|*|Q'|` values over the 24 alignments: `12 (sum, x8) < 72 (gap, x8) < 144 (pure, x8)` — the **sum/gap frame is the unique minimum-interior alignment**; the metric quantifies the interior effect of alignment choice.

## Artifacts

- Script: `rsa270_align2.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T120000+0800-rsa270-alignment-classification-7r2t4u.md`.

## Next

1. The metric spectrum across ALL layers (the 12/72/144 ordering vs the layer-dependent type splits) — a full layer x type x metric table.
2. Awaiting further directions.
