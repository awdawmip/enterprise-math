# RSA-270：第 5 轮——SG4 压力测试、能量恒等式、终态档案整合

Progress-Event-ID: `rsa270-round5-stress-energy-archive-4b7d1e`
At: `2026-09-06T18:50+08:00`
Scope: `enterprise-math / RSA-270 / round 5 (tool validation + S-affine family extension + curation)`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journals 2f7a9c; P000 assumed`
Kind: `PROGRESS / VALIDATION / CURATION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Round 5 of the sub-goal program completion phase. No factor obtained.

### A. SG4 verifier stress test (fixed and validated)

The verifier's mod-72 check was RSA-270-specific; corrected to the N-derived forced modulus `2^a * 9` (a=3 iff N=7 mod 8 else a=2, i.e. modulus 72 or 36). Stress test on 30 random prior-consistent 40-bit semiprimes:

- valid S accepted: **30/30**;
- wrong S (S+144) rejected: **30/30**.

### B. Energy identity (S-affine observable, verified)

`sum_e P(e)^2 = 2(N+1) + 6S` (the profile lives on one parity class, so the outer plateau contributes 2(N+1-S) and the overlap 8S). Verified on 5 synthetic semiprimes. This extends the 8e5f2a dichotomy record: energy/norm observables are S-affine (factoring-equivalent information, unobservable cheaply) — the dichotomy covers them.

### C. Terminal archive (curation step)

Consolidated the entire RSA-270 Enterprise-reformulation line into one durable record:

`knowledge/projects/enterprise-math/rsa270-enterprise-reformulation-terminal-archive-20260906.md`

containing: the core reduction, the 12-theorem list with source journals, the verifier tool, and the honest terminal boundary (completion requires a new observable class beyond the dichotomy, external facts, or a constraint relaxation).

## Artifacts

- Script: `rsa270_round5.py` (conversation-local).
- Curated record: `knowledge/projects/enterprise-math/rsa270-enterprise-reformulation-terminal-archive-20260906.md`.
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T182000+0800-rsa270-sg234-combination-closure-2f7a9c.md`.

## Next

The sub-goal program and its curation are complete. Without a new observable class or external input, further rounds have no verified route to advance the parent objective; the blocking condition (same as recorded at goal revision 3) persists.
