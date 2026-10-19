# RSA-270：深入研究第 6 轮——×2 根=|p−g|、序列证书饱和、证书套件打包

Progress-Event-ID: `rsa270-deep6-root-gap-saturation-suite-7h2j4e`
At: `2026-09-07T03:40+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 6`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 6g1i3d; P000 assumed`
Kind: `PROGRESS / EXACT IDENTITY / CURATION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 6. No factor obtained.

### A. ×2 root = |p − g| (exact)

`y(2) = |2p-q| = |p - (q-p)| = |p - g|` — the ×2 collapse root is the distance between the smaller factor and the Fermat gap. Verified on 6 semiprimes. Under the prior band `g in [0.765p, 1.266p]`, `y(2) in [0, 0.266p]`; `y(2) = 0` iff `q = 2p` (impossible for primes).

### B. Sequence-certificate saturation (verified)

The admissible y-sequence set stays **exactly 12 distinct** for prime ranges `l <= 229 / 1000 / 2000` — the class resolution is fixed by the forced lattice 72 and never tightens with more data.

### C. Certificate-suite curation

Packaged the whole certificate program into a durable record:

`knowledge/projects/enterprise-math/rsa270-certificate-suite-20260907.md`

(8 entries: square identity, V-function characterization, (x,y) joint sets, tower closure, y-sequence certificate, layer-1 theorem, CRT+Plucker, SG4 integration — all verified.)

## Artifacts

- Script: `rsa270_deep6.py`; curated record `rsa270-certificate-suite-20260907.md`.
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T025500+0800-rsa270-deep5-tower-verifier-sequence-6g1i3d.md`.

## Next

The deep-research certificate program is complete and packaged. Remaining: await new directions; the single-scalar observability wall (sub-O(sqrt(N)) recovery of S) is unchanged.
