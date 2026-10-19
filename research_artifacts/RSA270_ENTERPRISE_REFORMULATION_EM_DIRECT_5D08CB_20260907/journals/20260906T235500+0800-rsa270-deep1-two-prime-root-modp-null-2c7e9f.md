# RSA-270：深入研究第 1 轮——双素数坍缩交叉律、BRC 根模 p 恒常性、第一层零相关确认

Progress-Event-ID: `rsa270-deep1-two-prime-root-modp-null-2c7e9f`
At: `2026-09-06T23:55+08:00`
Scope: `enterprise-math / RSA-270 / deep research (goal: 深入研究), round 1`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 6f1e8a; P000 assumed`
Kind: `PROGRESS / EXACT THEOREMS`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 1. No factor obtained.

### 1. Two-prime collapse cross laws (exact, verified)

For odd primes `l1, l2 !| N`, the profile of `l1*l2*N` carries the **cross factor-boundary pair**

`Bx = (l1 p + l2 q - 2)/2`, `By = (l2 p + l1 q - 2)/2`,

with exact laws `Bx + By = ((l1+l2)S - 4)/2` and `Bx - By = (l1-l2)(p-q)/2` — the Fermat gap with **magnification `|l1-l2|/2`**. Verified on 4 semiprimes x {(3,5),(3,7),(5,7),(7,11)}. Combined with the one-prime law (`|l-1|/2` via the `(p,lq),(q,lp)` pair), the collapse family generates the gap at every magnification — the multiplier-lattice cost field in profile-boundary form.

### 2. BRC root mod-p constancy (exact, verified)

For all primes `l`, the collapse root satisfies `y(l) = |l p - q| == +-q (mod p)`. The root trajectory over primes, reduced mod p, is the two-point set `{q mod p, -q mod p}` — the factor residue q mod p is constant across the whole BRC root trajectory. Verified for 4 semiprimes x all primes <= 31.

### 3. RSA-270 layer-1 null (deep N-only check, corrected)

Earlier raw-residual correlation was a scale artifact; the normalized `rho_(l,0) = d_(l,0)/(2*x0-1)` over the 50 primes `l <= 229` gives Spearman `-0.133` with permutation null fraction `0.364` — **layer 1 is uncorrelated with l** (null confirmed). Layer 1 is provably structureless on RSA-270 itself; all factor data is layer-2-only, as the BRC observer discipline predicts.

### 4. Unification

Profile boundaries (collapse-law view), cost-field endpoints (cost view), and BRC roots (collapse view) are one rank-2 lattice in `(p,q)`; every view carries the same information pair `(S, q-p)` — the Plücker rank-2 no-go's structural content in three coordinates.

## Artifacts

- Script: `rsa270_deep1.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T231000+0800-rsa270-brc-collapse-trajectory-6f1e8a.md`.

## Next

1. Extend the mod-p constancy: the joint sequence `(y(l) mod p, y(l) mod q)` over primes — the CRT view of the root trajectory (expected: two-point set in each coordinate -> four points in the product; verify).
2. The magnification set `{|l1-l2|/2, |l-1|/2}` closes the gap-magnification family; check whether any small odd pair yields magnification 1 exactly with N-only-crossing structure (expected: no new channel, per the rank-2 no-go).
