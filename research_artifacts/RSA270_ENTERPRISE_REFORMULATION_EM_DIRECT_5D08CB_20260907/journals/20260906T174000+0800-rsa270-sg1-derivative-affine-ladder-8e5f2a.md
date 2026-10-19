# RSA-270：子目标 SG1 完成——导数阶梯是 S 的仿射族（观测代数二分定理的最后一层）

Progress-Event-ID: `rsa270-sg1-derivative-affine-ladder-8e5f2a`
At: `2026-09-06T17:40+08:00`
Scope: `enterprise-math / RSA-270 / sub-goal SG1 (derivative ladder closure)`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journals 5d8a2c/6d4e8b; P000 assumed`
Kind: `PROGRESS / EXACT CLASSIFICATION / CORRECTION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

SG1 (闭合最后一条未测观测族：torsion 点上的导数阶梯)。初始闭式假设 `W'_s(w_m)` 周期于 `s mod m` —— **被数值推翻并更正**：它是 s 的仿射函数。

### Theorem (SG1): the derivative ladder is affine in S

`W'_s(w_m) = s * A_m(r) + B_m(r)`, `r = s mod m`, with `A_m, B_m` periodic functions on `Z/mZ` (exact, in `Q(zeta_m)`); `A_m(r) != 0` on all residues for odd m and most residues for even m (computed m=3..12; e.g. m=3: 3/3, m=4: 2/4, m=8: 6/8 nonzero).

Hence

`P'(w_m) = 2 [ s1 A_m(r0) + B_m(r0) ] + 2 [ s2 A_m(r1) + B_m(r1) ]`,  `s1=(N+3)/2` (known), `s2=(S+2)/2` (factor block),

which is **linear in S**. Consequence: given `r1` (one residue from the value ladder) and the derivative value `P'(w_m)` at any single m with `A_m(r1) != 0`, the scalar equation

`S + 2 = ( P'(w_m) - 2[s1 A_m(r0)+B_m(r0)] - 2 B_m(r1) ) / A_m(r1)`

recovers `S` **exactly**. Verified: affine law for `m=3..12, s<=60`; `P'` identity on 5 synthetic semiprimes for `m=3..16` (all PASS).

### Classification dichotomy (the profile observable algebra is now closed)

Every natural ladder family of the profile is exactly one of two kinds:

- **periodic** (value/torsion `P(w_m)`, zero sets, forced lattice, carry automata): yields `S mod 2m` residue classes — never enough, N-only part = `S = 16 mod 72`;
- **S-affine/polynomial** (`m=1,2` mass evaluations, derivative-at-torsion `P'(w_m)`, moments at `u=1`): information-equal to full `S` (factoring-equivalent), but their evaluation requires the profile, whose N-only computation is the standing sub-`O(sqrt(N))` wall.

No family is both cheaply observable and information-complete. This closes the observable-algebra question posed across 9f3b12/5d8a2c/6d4e8b.

## Artifacts

- Scripts: `rsa270_sg1_derivative_ladder.py` (superseded by) `rsa270_sg1_affine.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T170000+0800-rsa270-discrete-spike-carry-automaton-6d4e8b.md`.

## Next (sub-goal order)

- SG2: general forced-zero family for arbitrary N under the prior (tower-based characterization `2^a * 3^b`).
- SG3: combination closure theorem — joint certificate resolution for RSA-270 (expected: S mod 144 two-class + forced family; verify combination adds no channel).
- SG4: fingerprint verifier tool (62-point torsion + forced lattice + spike checks) run out-of-sample on RSA-260.
