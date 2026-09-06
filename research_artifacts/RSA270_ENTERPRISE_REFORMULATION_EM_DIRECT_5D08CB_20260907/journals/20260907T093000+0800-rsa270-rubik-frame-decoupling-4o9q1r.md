# RSA-270：魔方旋转算法——帧群验证、方向轨道、和/差框架逐层解耦

Progress-Event-ID: `rsa270-rubik-frame-decoupling-4o9q1r`
At: `2026-09-07T09:30+08:00`
Scope: `enterprise-math / RSA-270 / user direction: Rubik-cube rotation of the Enterprise frame, layer decoupling, splicing`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; A3_RUBIK_FRAME_TWIST_TOOLKIT_20260828; P000 assumed`
Kind: `PROGRESS / EXACT THEOREM / ROUTE REDUCTION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

User direction executed: Rubik-cube rotations on the Enterprise coordinate frame, per-layer decoupling + splicing. No factor obtained.

### 1. Frame group (verified)

Built the A3 Rubik frame group from `R_sigma = sgn(sigma) * P_sigma |_{Lambda_3}`: `Q^4 = C^3 = I`, orbit of `<Q,C>` = exactly **24** elements (checked to word length 8). Convention note: my generator matrices are the transposed convention of the toolkit record; the group is identical.

### 2. The 24-rotation orbit = the multiplier-direction orbit

Restricted to the (p,q) plane, the 24 frame rotations yield 24 direction pairs `(a,b;c,d)` with determinants `+-1, +-3`; the first-row direction set is exactly the 12 directions `{(+-1,+-1), (+-1,0), (0,+-1), (+-2,+-1), (+-1,+-2)}` — **the Rubik orbit is the cost-field/multiplier-direction orbit** (7e3b5d): rotating the Enterprise frame IS scanning the multiplier lattice.

### 3. Sum/difference decoupling per layer (verified)

The rotation with first row `(1,1)` decouples every layer into `(p+q, p-q)` — the forced-sum axis and the gap axis. Per-layer table (corrected enumeration over `lcm(6, mod, 72)`):

`mod 8: sum {0} (1) gap 2 | mod 9: sum {7} (1) gap 3 | mod 16: sum {0,8} (2) gap 2 | mod 27: sum {7,25} (2) gap 9 | mod 24: sum {16} (1) gap 2 | mod 72: sum {16} (1) gap 6 | mod 144: sum {16,88} (2) gap 6`

On the divisors of 72 the sum is fully forced and the gap carries 2-6 classes; beyond 72 the sum regains the class-doubling ambiguity.

### 4. Conclusion: the Rubik program reduces to the established classification

- decouple = the sum/gap frame (the cleanest frame, exact on the 72-lattice);
- splice = CRT assembly of the gap digits — and the per-layer gap classes are exactly the QR/`phi(N)`-mod ladder (9f3b12/5f0h2c);
- the full gap assembly is the single hard scalar (`g^2 = S^2 - 4N`) — the standing sub-`O(sqrt(N))` wall.

The Rubik rotation therefore reaches the optimal frame and then hits the same boundary; it reproduces and sharpens (sum/gap language) the entire established structure rather than bypassing it.

## Artifacts

- Scripts: `rsa270_rubik.py`, `rsa270_rubik2.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T081000+0800-rsa270-deep12-terminal-consolidation-3n8p0k.md`.

## Next

1. The full splice attempt: CRT-combine the gap classes of all layers up to the 72-lattice (2x3x6 = 36 candidate gaps) and show the candidates close over `g^2 = S^2 - 4N` — a finite 36-way check demonstrating the splice's complete behavior at certificate scale.
2. Beyond 72 the splice diverges (sum regains ambiguity) — the tower behavior is fully characterized.
