# RSA-270：剖面闭式、零点判据、强制零点族与强制格塔定理

Progress-Event-ID: `rsa270-closed-form-zero-criterion-5d8a2c`
At: `2026-09-06T15:30+08:00`
Scope: `enterprise-math / RSA-270 / shortcut hunt (non-exhaustive, exact-identity route)`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journals 9f3b12/7c4d1f/2b8e6a; P000 assumed`
Kind: `PROGRESS / EXACT THEOREMS`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Continued the shortcut hunt for RSA-270 under the standing constraints (no exhaustive search, no classical NFS/ECM-style computation). New exact results; no factor obtained.

### 1. Closed form of the two-plateau profile (exact)

With `W_s(u) = u^(2-s)(1-u^(2(s-1)))/(1-u^2)`, the profile collapses to

`P(u) = 2 u^((2-S)/2) B(u) / (1-u^2)`,   `B(u) = u^((S-N-1)/2)(1-u^(N+1)) + (1-u^S)`,

all exponents integers (`S` even, `N` odd). This is the terminal clean form of the four-layer/two-plateau structure: the entire profile is carried by one bracket `B(u)` and one pole factor. Verified coefficient-exact against direct divisor-sum profiles for `N in {35,143,391,899,3599}`.

### 2. Zero criterion (exact)

`m >= 3`: `P(w_m) = 0` iff `B(w_m) = 0` (the pole factor `1-w^2` never vanishes at `m>=3`). Verified for `m = 3..16` on the same 5 synthetic semiprimes (PASS, after exact modular reduction of exponents).

### 3. Value-forced torsion-zero family (RSA-270, construction-family prior)

At the prior-forced class `S = 16 mod 72`, `B(w_m) = w^(-20)(1-w^56) + 1 - w^16`, and direct enumeration of all admissible classes for **every `m <= 200`** confirms:

`P(w_m) = 0` forced  <=>  `m | 72` and `24 !| m`,  i.e. exactly `{3,4,6,8,9,12,18,36}`.

Nothing else in `m <= 200` is value-forced. Spot values match exact hand computation (`m=24`: `B(w_24) = 3 + i*sqrt(3) != 0`; `m=72`: nonzero).

### 4. Forced-lattice tower theorem

Unconditional 2-adic tower of admissible `S mod 2^k` classes: counts `1,1,1,2,4,8,16,32` for `k=1..8` -> **`a(N)=3`** (max forced 2-adic depth: `S = 0 mod 8`).
Prior 3-adic tower `S mod 3^j`: counts `1,1,2,4` for `j=1..4` -> **`b(N)=2`** (`S = 7 mod 9` forced, `S mod 27` two classes).
Maximal forced modulus `2^a * 3^b = 2^3 * 3^2 = 72`, i.e. `S = 16 mod 72` — matching the 7c4d1f lattice result via a new tower characterization. The tower counts double exactly once past the forced depth: `2^(k-a)` and `2·(3^(j-2) - ...)` respectively.

### Status of the shortcut hunt

- All exact-identity shortcuts now land on the same terminal structure: the profile is `B(u)/(1-u^2)`-shaped; every cheap observable (torsion, moments, truncation, mod-collapse, coarse-grain) is a function of `S`; the N-only computable part of `S` is exactly `S = 16 mod 72` (prior) / `S = 0 mod 8` (unconditional); forced-zero certificate = `{3,4,6,8,9,12,18,36}`.
- RSA-270 factorization is **not achieved**. No known exact-identity route within the Enterprise reformulations (or classical σ(N)/residuosity equivalences) yields sub-`O(sqrt(N))` recovery of the single scalar `S`; this is the same wall recorded in 68d4a1/91ad72/9f3b12/7c4d1f/2b8e6a.
- No exhaustive or traditional (NFS/ECM) computation was used; all results are exact identities + bounded modular enumerations.

## Artifacts

- Script: `rsa270_closed_form.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T144500+0800-rsa270-brc-multilayer-collapse-ledger-2b8e6a.md`.

## Next

1. Generalize Theorem 3: characterize the value-forced family for arbitrary `N` under the prior (likely: `{m | 2^a*3^b : 2^a*3^(b-1) !| ... }`-type lattice condition; small enumeration + residue algebra).
2. The only remaining constructive direction consistent with the constraints: a sub-`O(sqrt(N))` method to compute `sigma(N)/72` (equivalently `S`) from `N` — every EM-exact-identity family tested so far is information-complete but not cheap; new candidates must clear the closed-route ledger (2b8e6a) before testing.
