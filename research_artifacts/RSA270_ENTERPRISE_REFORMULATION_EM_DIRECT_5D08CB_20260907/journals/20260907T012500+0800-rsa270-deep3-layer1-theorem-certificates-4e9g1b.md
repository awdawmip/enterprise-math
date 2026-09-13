# RSA-270：深入研究第 3 轮——第一层结构无关性定理、SG4 第二层证书扩展、×2 根模证书

Progress-Event-ID: `rsa270-deep3-layer1-theorem-certificates-4e9g1b`
At: `2026-09-07T01:25+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 3`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 3d8f0a; P000 assumed`
Kind: `PROGRESS / THEOREM / TOOL EXTENSION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 3. No factor obtained.

### A. Layer-1 provable structurelessness (theorem + consistency checks)

`x0(l), d_(l,0), rho_(l,0)` are explicit functions of `l*N` alone; the factor pair enters only through `N = pq` — hence **no layer-1 statistic can depend on the vertex `q/p`** (a proof, not a null test). Consistency checks on RSA-270's `rho`-sequence over the 50 primes `l <= 229`: lag-1 autocorrelation `0.106`; runs `22` — the runs deficit vs iid (~33) is **universal** (four random 895-bit synthetic semiprimes give runs 21-32; it reflects the smoothness of `sqrt(l)`, not factor structure).

### B. SG4 verifier extension: layer-2 certificates (run on RSA-260)

Added to the verifier: CRT root laws (`y mod p in {+-q}`, `y mod q = +-l*p`), the two-l Plucker relation `(x1-x2)(l1*x2-l2*x1) = (l1-l2)^2 N`, and the V-ray coefficient check. RSA-260 real factors: **PASS** (all certificates).

### C. RSA-270 x2 root modular certificate

For the admissible `(p,q) mod 72` classes (forced lattice), the ×2 collapse root satisfies

`y = |2p-q| mod 72 in {1, 17, 19, 35, 37, 53, 71}` (7 classes, all odd).

Endpoint parity bifurcation: `x*(l) = l*p+q` is EVEN for odd `l` (since `S = 0 mod 8`) and **ODD for `l=2`** — the ×2 branch is the unique odd-parity endpoint branch; its mod-72 sieve keeps `7/72` of layer-2 checks (the tightest per-branch certificate so far).

## Artifacts

- Script: `rsa270_deep3.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T004000+0800-rsa270-deep2-crt-plucker-vrecovery-3d8f0a.md`.

## Next

1. Layer-2 certificate lattice for ALL small primes l (the per-l root residue sets) — the complete modular certificate table of the V-function for RSA-270.
2. Combine with the j-sieve (9d4c2e) into the final per-branch search certificate; expected to reproduce the 2^438 bound with certificate-level precision.
