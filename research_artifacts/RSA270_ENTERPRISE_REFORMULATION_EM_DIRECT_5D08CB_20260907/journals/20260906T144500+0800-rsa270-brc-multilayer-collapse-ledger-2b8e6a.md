# RSA-270：BRC 多层坍缩路线总账（广泛测试 + 总结）

Progress-Event-ID: `rsa270-brc-multilayer-collapse-ledger-2b8e6a`
At: `2026-09-06T14:45+08:00`
Scope: `enterprise-math / RSA-270 / BRC multi-layer collapse broad route testing`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; prior journals 68d4a1/91ad72/9f3b12/7c4d1f; P000 assumed`
Kind: `PROGRESS / ROUTE LEDGER / CORRECTION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Per user instruction, BRC multi-layer collapse was applied broadly across the Enterprise-coordinate reformulations of RSA-270. Each route was tested either exactly (derivation + small-N verification) or by broad computation on RSA-270 itself. One of my own conjectures was refuted by enumeration and is corrected below.

### Collapse route ledger

| Route | Retained | Erased | Verdict |
|---|---|---|---|
| `u=+-1` evaluation (mass) | full `S` (`sigma(N)=N+S+1`) | — | factoring-equivalent (classical) |
| torsion `u->w_m`, `m>=3` | `S mod 2m` (`+-` for even m) | all else | closed, 9f3b12 (QR(-3) at m=3) |
| `u=1` moment ladder | polynomials in `S` (even moments) | odd moments vanish | S-functional; no new dimension |
| profile mod 2 | NOTHING | all | total erasure |
| profile mod `c>=3` | plateau boundary `(S-2)/2` | — | S-equivalent |
| dyadic coarse-grain (block sums) | bit ladder of `S` | fine structure | S-equivalent |
| axis truncation `a<B` | `T_B = sum_{a<B} t3((N-B2(a))/2)` | — | closed; conjectured min-form **REFUTED** (see correction) |
| local modular support collapse | N-independent `q(q^2-1)` | all | closed (T104500 theorem; reconfirmed) |
| coordinate-residual gcd sweeps | none | — | closed this turn: 6152 tests, 0 nontrivial |
| prior + torsion joint collapse | forced zeros `m in {3,4,6,9,12,18,36}`; `S = 16 mod 72` | quotient `t=(S-16)/72` | certificate published (below) |
| QS relation-layer collapse | large-prime recoalescence semantics | — | calibrated this turn (below) |

### D2 correction (refuted conjecture, recorded honestly)

Conjecture: axis-truncation count `T_B(N) = #{(a,b,c,d)>=0 : sum B2 = 2N+2, a<B}` equals `sum_{d|N} min(B,(d+N/d)/2)` (slope breaks at `S/2` and `(N+1)/2`).

**Refuted by direct enumeration** (N=143: formula 15 vs enum 42 at B=2 already diverges; N=391 likewise). The correct identity is

`T_B(N) = sum_{a<B} t3((N - B2(a))/2)`,  `t3(n) = #{(x,y,z)>=0 : T_x+T_y+T_z = n} = r3_odd(8n+3)/8`,

the classical three-triangular / odd-three-square count (Gauss-Legendre, class-number flavored) — no clean divisor-pair min-form, no cheap S-encoding. The clean divisor-pair structure lives only in the profile's u-ladder (exponents = pair-difference families, plateau boundary `(S-2)/2`), not in axis truncation. Route closed.

### Broad coordinate-residual gcd sweep on RSA-270 (this turn)

- Family 1: `B_d(r)` L1 balls, `d=2..6`, `r ~ N^(1/d)`, window 256: 2565 tests, 0 nontrivial gcd.
- Family 2: triangular-shell `B2(r)` near `sqrt(N/4)`, multipliers `{1,2,4}`, window 512: 3075 tests, 0.
- Family 3: dimension-descending collapse `6->5->4->3->2->1`: residual bit lengths 895/895/893/892/892/892, all gcd 1 (no telescoping to a factor for RSA-270).
- Family 4: multiplier shell `d_(k,j)` for `k<=64, j<=7`: 512 tests, 0.

### QS relation-layer collapse calibration (12 random 40-bit semiprimes, FB<=293, window 6000)

- full-smooth yields: 15-178 (wide variance);
- one-large-prime recoalescence events: 27-490 per run (common — consistent with the 68d4a1 finding that large-prime/special-q semantics is the correct relation layer);
- k-family square-class duplication among consecutive `k=1..16`: only 1-5 per run — **rare** at this selection; the trivial-cycle dominance reported in 5b8c41 (346/1000 among the 1000 lowest-shell branches) is specific to deep-`rho_k` (low-shell resonance) selections, not a generic k-family phenomenon. Both facts now recorded precisely.

### Joint prior-collapse certificate for RSA-270 (allowed `P(w_m)` sets, m=3..64)

- Forced (allowed set = singleton): `m in {3,4,6,9,12,18,36}`, all values 0 (divisors >=3 of 36).
- Sample multi-class members: `m=5`: `P(w_5) in {-4,0}`; `m=7`: 3 values; `m=11`: 6; `m=16`: 3 distinct of 4 classes; `m=31`: 15.
- Naive joint summary `sum_m log2(m/|adm|)` over `m=3..64`: ~147 bits (upper estimate; overlapping moduli).

### Summary (multi-route thinking)

1. Every BRC collapse family on the Enterprise-coordinate reformulations (X6 shells, four-layer counts, two-plateau profile, multiplier trees) reduces to a **function of the single scalar S** — the reformulations are exact and information-complete, with no hidden channel beyond `S`.
2. The N-only computable part of `S` is now exhausted: `S = 0 mod 8` (unconditional), `S = 16 mod 72` (prior, maximal modulus `72 = 2^3*3^2`), plus the joint torsion forced-zero certificate. Total leverage: ~6.17 bits.
3. The one clean structural reading that survived all tests: the profile is the **axis-difference generating function over divisor-labeled fixed-sum ladders**, and the plateau boundary `(S-2)/2` is the maximal pair-difference — the Enterprise-coordinate form of the Fermat midpoint `A = S/2`.
4. The hard unit is unchanged and now fully delimited: recover `t = (S-16)/72` (equivalently `sigma(N)/72`) at sub-`O(sqrt(N))` cost. No collapse family tested provides it; all cheap observables are `phi(N) mod 2m`/residuosity class.

### BRC audit

Declared populations/observers per collapse: see ledger. Every collapse in the ledger retains at most a `S mod 2m` fiber class or a polynomial image of `S`; no collapse erases provenance silently except mod-2 (documented as total erasure). Reuse: BRC observer/provenance discipline `REUSE_APPLIED` (lineage 9f3b12/7c4d1f); QS calibration `REUSE_EXECUTED` on classical smooth-relation semantics; no new tool family; no factorization claim.

## Artifacts

- Scripts: `rsa270_brc_multilayer.py`, `rsa270_qs_calibration.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T134500+0800-rsa270-enterprise-coordinate-sigma-lattice-7c4d1f.md`.

## Next

1. Generalize the forced-lattice: characterize the maximal forced modulus for arbitrary `N` under the prior (currently `72` for RSA-270) as a function of `N mod 2^k` and `N mod 3^j` (small exact enumeration, likely `2^a*3^b` with `a,b` from the residue data).
2. Package the ledger + certificate into a reusable verification tool (`tools/`-style script) that checks any claimed RSA-270 profile/`S` against the 62-point torsion fingerprint and the mod-72 lattice before any further analysis.
3. Do not reopen the closed routes (axis truncation, local modular support, coordinate-residual sweeps, blind `(k,j)`/ECM expansion) without a new N-dependent observable beyond the `phi(N) mod 2m` class.
