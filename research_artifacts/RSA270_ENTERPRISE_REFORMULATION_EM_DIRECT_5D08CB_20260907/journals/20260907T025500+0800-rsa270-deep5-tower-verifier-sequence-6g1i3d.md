# RSA-270：深入研究第 5 轮——模数塔行为、SG4 联合证书扩展、跨 ℓ y-序列证书

Progress-Event-ID: `rsa270-deep5-tower-verifier-sequence-6g1i3d`
At: `2026-09-07T02:55+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 5`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 5f0h2c; P000 assumed`
Kind: `PROGRESS / CERTIFICATE CLOSURE`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 5. No factor obtained.

### 1. Modulus-tower behavior (question from 5f0h2c Next #1 — closed)

Beyond the forced modulus 72 the certificate sets grow with the admissible class count (mod 144: 24 classes; mod 216: 36; mod 720: 96 -> |x-set| up to 72, |y-set| up to 40). **No free tightening**: the forced lattice `72 = 2^3*3^2` is the maximal certificate modulus — the y-certificate cannot be tightened by larger moduli because the class uncertainty grows at the same rate.

### 2. SG4 verifier extension: (x,y)-joint branch certificate (run on RSA-260)

Added: for all `l <= 31`, the endpoint/root pair must satisfy the square identity and lie in the branch's own joint certificate sets (computed from the N-derived admissible classes). RSA-260 real factors: **PASS**.

### 3. Cross-l y-sequence certificate (complete layer-2 sequence shadow)

The y-sequence over primes `l <= 229` reduced mod 72: RSA-260 has **12 distinct admissible sequences** and its true sequence lies in the set; RSA-270 likewise has **12 distinct admissible sequences** (of its 12 classes). This is the complete N-only sequence certificate of the layer-2 V-function: any claimed layer-2 observation must match one of the 12 sequences.

## Artifacts

- Script: `rsa270_deep5.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T021000+0800-rsa270-deep4-certificate-lattice-5f0h2c.md`.

## Next

The certificate program is now complete: per-branch (x,y) joint sets (5f0h2c), modulus-tower closure (this round), sequence certificate (this round), verifier integration (this round). The deep-research line has fully mapped the N-only modular shadow of every collapse-family observable; the residual unknown remains the single scalar S with the standing sub-O(sqrt(N)) observability wall. Further rounds: package a final "certificate suite" summary record, or await new directions.
