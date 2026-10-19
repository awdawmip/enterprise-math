# RSA-270：深入研究第 4 轮——完整第二层模证书格（x 筛/y 证/joint 影子），含对平方闭包假设的推翻

Progress-Event-ID: `rsa270-deep4-certificate-lattice-5f0h2c`
At: `2026-09-07T02:10+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 4`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 4e9g1b; P000 assumed`
Kind: `PROGRESS / CERTIFICATE LATTICE / CORRECTION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 4. No factor obtained.

### Complete per-l certificate lattice (all primes l <= 229)

For each prime branch `l`, over the 12 admissible `(p,q) mod 72` classes:

- **x-set sizes** (`x = l*p+q mod 72`): mostly 12; **1/72 for `l in {13, 37}`** (x fully forced); 2/72 for `{7,19,31,...}`; 3/72 for `{5,17,29,41,...}`;
- **y-set sizes** (`y = |l*p-q| mod 72`): **1 class for `l in {11, 23}`** (root fully forced, e.g. `l=11: y = 44 mod 72`); 2 for `{5,17,29,41,...}`; 3 for `{7,19,31}`; 4 for `l=3`; 6 for `{13,37,...}`; 7 for `l=2` (`{1,17,19,35,37,53,71}`);
- **joint sizes** (`(x,y)` pairs): 6-12 per branch.

### Correction of the square-closure hypothesis (recorded honestly)

Conjecture: `y-set = {+-sqrt(x^2 - 4lN) mod 72 : x in x-set}`. **Refuted by computation**: the modular square closure has 12-96 elements (e.g. `l=2`: derived 96 vs joint 12), vastly overapproximating the true joint set. The y-residue therefore carries **genuine class structure independent of the modular square condition** — it is not derivable from the x-set alone.

### Synthesis (corrected)

- **x-set = the search sieve** (round-7 j-sieve: the scan must hit `x = x0+j` in the x-classes);
- **y-set = the verification certificate** (a candidate endpoint x must satisfy `y = |l p - q|` in the y-classes — consistency beyond the square condition);
- **joint = the complete N-only modular shadow** of the layer-2 V-function for branch `l`.
- The x2 branch: `x in {3,9,...,69}` (all `= 3 mod 6`, 12 classes) and `y in {1,17,19,35,37,53,71}` (7 classes, all odd).

## Artifacts

- Script: `rsa270_deep4.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T012500+0800-rsa270-deep3-layer1-theorem-certificates-4e9g1b.md`.

## Next

1. The y-certificate's independence suggests one more unexplored observable family: the y-classes over LARGER moduli (2^a*3^b*5^c towers beyond 72) — whether the root certificate keeps tightening with the modulus (expected yes, as the forced lattice deepens only with p,q-residue knowledge — bounded).
2. Package the (x,y)-joint certificate into the SG4 verifier as the layer-2 branch certificate.
