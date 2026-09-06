# RSA-270：魔方对齐方式分类——24 种对齐对内部结构的效应（8+8+8 三分型）

Progress-Event-ID: `rsa270-alignment-classification-7r2t4u`
At: `2026-09-07T12:00+08:00`
Scope: `enterprise-math / RSA-270 / Rubik alignment study (user direction: different alignments' interior effects)`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 6q1s3t; P000 assumed`
Kind: `PROGRESS / CLASSIFICATION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Alignment study executed. No factor obtained.

### The 24 alignments split into three clean octets (verified at mod 72)

- **8 sum-type**: one coordinate = `+-(p+q) = +-S = +-16 mod 72` — FORCED. These alignments push the entire forced-lattice information into a single coordinate (the maximal interior simplification).
- **8 gap-type**: one coordinate = `+-(p-q)` — the gap axis with exactly **6 classes** (the residual ambiguity).
- **8 pure-type**: no decoupling (12/12 split) — the multiplier directions that do not contain the sum/gap rows.

No mixed types occur. The first-row direction determines the type (sum `(1,1)`, gap `(1,-1)`, pure the remaining 8 of the 12 directions); the second row selects within the octet (4 choices x 2 signs = 8).

### N-independence (verified)

RSA-260 (S = 40 mod 72): identical 8/8/8 type structure — the classification is N-independent; only the forced VALUES change with N.

### Interior-effect summary

- The **sum/gap frame is the unique optimal alignment**: one coordinate fully forced, the other carrying the minimal 6-class residual — no other of the 24 alignments achieves a smaller residual coordinate.
- The 8 pure alignments scatter the 12 classes across both coordinates (worst interior);
- the interior effect of alignment choice = how the forced-lattice information and the gap ambiguity are distributed across coordinates; the sum/gap frame concentrates all forcing in one axis — the canonical interior form established in the previous rounds.

## Artifacts

- Script: `rsa270_alignments.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T111000+0800-rsa270-rubik-final-answer-6q1s3t.md`.

## Next

1. Alignment stability across layers (8/9/24 vs 72): the type structure per layer (expected: the sum octet persists wherever S is forced on that layer; gap/pure may re-split on layers with different forcing).
2. Awaiting further directions.
