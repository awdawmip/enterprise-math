# RSA-270：深入研究第 7 轮——几何/模二分：纤维整数仿射秩恒为 2，解耦是模现象

Progress-Event-ID: `rsa270-geometric-modular-dichotomy-4y9z0a`
At: `2026-09-07T17:50+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 7`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 3x8y9z; P000 assumed`
Kind: `PROGRESS / EXACT DICHOTOMY / CORRECTION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 7. No factor obtained.

### Affine-rank experiment (corrected twice, final form)

- The transformed fiber's **integer-lift affine rank is 2 under EVERY one of the 24 alignments** — no alignment collapses the fiber to a geometric line.
- The sum-type "line collapse" exists only at the **residue level**: `p' = 16 mod 72` is a modular line because the integer lifts carry `S in {16, 88}` (both `= 16 mod 72`).
- Therefore: **the decoupling is a modular phenomenon, not a geometric one**; the type classification (sum/gap/pure) is exactly the modular-rank classification of the residue fiber.

This closes the geometric side of the alignment program: every alignment preserves the 2-dimensional integer geometry; only the modular shadows differ.

## Artifacts

- Script: `rsa270_align8.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T170000+0800-rsa270-sl2z-type-law-closed-3x8y9z.md`.

## Next

The alignment program is fully closed (types, laws, geometry/modular dichotomy). Remaining: consolidation of the whole Rubik/alignment line into one durable record; then awaiting further directions or external facts.
